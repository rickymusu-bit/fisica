"""Prepara GitHub Pages copiando solo gli HTML italiani collegati dall'indice."""
from html.parser import HTMLParser
from pathlib import Path
from html import escape
import json
import shutil
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html" and self.language is None:
            self.language = attrs.get("lang")
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if "id" in attrs:
            self.ids.add(attrs["id"])


def read_document(path):
    document = Document()
    document.feed(path.read_text(encoding="utf-8-sig"))
    if document.language != "it":
        raise ValueError(f"Il documento non dichiara lang=it: {path.name}")
    return document


def main():
    index = ROOT / "index.html"
    document = read_document(index)
    sources = {index}
    for link in document.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            raise ValueError(f"Il catalogo deve collegare materiali locali: {link}")
        if url.path in ("", "./"):
            if url.fragment and unquote(url.fragment) not in document.ids:
                raise ValueError(f"Ancora assente dall'indice: {link}")
            continue
        path = (ROOT / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or path.suffix != ".html" or not path.is_file():
            raise ValueError(f"Collegamento HTML non valido: {link}")
        read_document(path)
        sources.add(path)
    if len(sources) <= 1:
        raise ValueError("L'indice non contiene materiali")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    for source in sorted(sources):
        target = OUTPUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    redirects_path = ROOT / "site-redirects.json"
    redirects = json.loads(redirects_path.read_text()) if redirects_path.exists() else {}
    for previous, current in redirects.items():
        previous_path = Path(previous)
        current_path = (ROOT / current).resolve()
        if previous_path.name != previous or previous_path.suffix != ".html":
            raise ValueError(f"Percorso di reindirizzamento non valido: {previous}")
        if current_path not in sources or previous == current or (OUTPUT / previous).exists():
            raise ValueError(f"Destinazione di reindirizzamento non valida: {current}")
        destination = json.dumps(current, ensure_ascii=False)
        page = f'''<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dispensa aggiornata · Materiale Didattico</title>
<script>location.replace({destination}+location.search+location.hash);</script>
<meta http-equiv="refresh" content="0;url={escape(current, quote=True)}"></head>
<body><p>La dispensa è stata aggiornata. <a href="{escape(current, quote=True)}">Apri la versione corrente</a>.</p></body></html>
'''
        (OUTPUT / previous).write_text(page, encoding="utf-8")
    (OUTPUT / ".nojekyll").touch()
    print(f"Preparati {len(sources)} HTML in italiano e {len(redirects)} reindirizzamenti dai collegamenti precedenti.")


if __name__ == "__main__":
    main()
