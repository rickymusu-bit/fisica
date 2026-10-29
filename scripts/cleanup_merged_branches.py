#!/usr/bin/env python3
"""Elimina soltanto i branch la cui punta è già un antenato di main.

Esecuzione tramite workflow dedicato su main. Non tocca branch divergenti, PR
aperte, branch protetti o branch tecnici di anteprima. Non riscrive Git.
"""
import json
import os
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen


REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
BASE = f"https://api.github.com/repos/{REPO}"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "Stringhe-cleanup-integrated-branches",
}
TECHNICAL_BRANCHES = {
    "main", "stringhe-preview", "quiz-verifiche-preview",
    "anteprima/economia-informativa",
}


def api(method, path):
    request = Request(BASE + path, method=method, headers=HEADERS)
    with urlopen(request, timeout=25) as response:
        payload = response.read()
        return json.loads(payload) if payload else None


def paged(path):
    page = 1
    while True:
        batch = api("GET", f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        if not batch:
            return
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def safe_to_delete(entry, active_pr_heads):
    name = entry["name"]
    if (name in TECHNICAL_BRANCHES or entry.get("protected")
            or name in active_pr_heads or name.endswith("-preview")
            or name.startswith("anteprima/")):
        return False, "protetto, tecnico o PR aperta"
    encoded = quote(name, safe="")
    try:
        comparison = api("GET", f"/compare/main...{encoded}")
    except HTTPError as exc:
        if exc.code == 404:
            return False, "nessun antenato comune"
        raise
    # La sola assenza di differenze nei file non basta (squash merge).
    if comparison.get("ahead_by") != 0 or comparison.get("status") != "behind":
        return False, f"commit esclusivi / confronto {comparison.get('status')}"
    current = api("GET", f"/branches/{encoded}")
    if current["commit"]["sha"] != entry["commit"]["sha"] or current.get("protected"):
        return False, "branch modificato o protetto nel frattempo"
    return True, "interamente integrato"


def main():
    branches = list(paged("/branches"))
    open_prs = list(paged("/pulls?state=open"))
    active_pr_heads = {pr["head"]["ref"] for pr in open_prs
                       if pr["head"]["repo"] and pr["head"]["repo"]["full_name"] == REPO}
    removed, retained = [], []
    for branch in branches:
        name = branch["name"]
        safe, explanation = safe_to_delete(branch, active_pr_heads)
        if not safe:
            retained.append(name)
            print(f"CONSERVATO {name}: {explanation}")
            continue
        try:
            api("DELETE", f"/git/refs/heads/{quote(name, safe='')}")
            removed.append(name)
            print(f"ELIMINATO {name}: {explanation}")
        except HTTPError as exc:
            retained.append(name)
            print(f"NON ELIMINATO {name}: API {exc.code}")
    print(f"RIEPILOGO eliminati={len(removed)}, conservati={len(retained)}")
    if removed:
        print("Branch eliminati: " + ", ".join(removed))


if __name__ == "__main__":
    main()
