"""Genera le home nelle lingue per le quali esistono già articoli."""
from copy import deepcopy
from html import escape
import json
import re

from home_covers import render_covers

HOME_FILES = {"it": "index.html", "fr": "index_fr.html", "sq": "index_sq.html"}


def load_languages(root, covers):
    languages = json.loads((root / "lingue/home.json").read_text(encoding="utf-8"))
    if set(languages) != {"fr", "sq"}:
        raise ValueError("Lingue della home non valide")
    for language, ui in languages.items():
        if len(ui["captions"]) != len(covers):
            raise ValueError("Le didascalie devono coprire tutte le copertine")
        for source, (filename, title, description) in ui["articles"].items():
            path = (root / filename).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file() or path.suffix != ".html":
                raise ValueError(f"Articolo tradotto assente: {filename}")
            if not all((source, title, description)):
                raise ValueError("Titolo o descrizione tradotti assenti")
    return languages


def localized_home(document, covers, language="it", ui=None):
    if language == "it":
        return render_covers(document, covers)
    ui = ui or {}
    document = document.replace('<html lang="it">', f'<html lang="{language}">')
    document = re.sub(r'<meta name="description"[^>]*>',
                      '<meta name="description" content="' + escape(ui["description"], quote=True) + '">', document)
    for key in ("index", "languageName", "skip", "subtitle", "downloadNote", "explore"):
        pattern = rf'(<[^>]+data-i18n="{key}"[^>]*>)[\s\S]*?(</[^>]+>)'
        document, count = re.subn(pattern, lambda m: m[1] + escape(ui[key]) + m[2], document)
        if count != 1:
            raise ValueError(f"Testo della home assente: {key}")
    document = document.replace('aria-label="Indice degli argomenti"', 'aria-label="' + escape(ui["indexAria"], quote=True) + '"')
    document = document.replace('aria-label="Lingua"', 'aria-label="' + escape(ui["languageAria"], quote=True) + '"')
    document = document.replace('aria-label="Scegli la lingua"', 'aria-label="' + escape(ui["chooseLanguage"], quote=True) + '"')

    def language_link(match):
        attrs = match[1].replace(' aria-current="page"', '')
        if match[2] == language:
            attrs += ' aria-current="page"'
        return attrs + '>'
    document = re.sub(r'(<a[^>]*hreflang="([^"]+)"[^>]*)(>)', language_link, document)

    def article(match):
        block = match[0]
        href = re.search(r'class="read" href="([^"]+)"', block)[1]
        if href not in ui["articles"]:
            return ''
        filename, title, description = ui["articles"][href]
        block = block.replace(href, filename)
        block = re.sub(r'<h3>[^<]*</h3>', '<h3>' + escape(title) + '</h3>', block)
        block = re.sub(r'<p>[^<]*</p>', '<p>' + escape(description) + '</p>', block)
        block = re.sub(r'aria-label="Scarica l’articolo:[^"]+"',
                       'aria-label="' + escape(ui["downloadAria"] + ' ' + title + ' (HTML)', quote=True) + '"', block)
        return block.replace('>Scarica HTML</a>', '>' + escape(ui["download"]) + '</a>')

    document = re.sub(r'<li class="material">[\s\S]*?</li>', article, document)
    empty = []
    def group(match):
        block = match[0]
        group_id = re.search(r'id="([^"]+)"', block)[1]
        if 'class="material"' not in block:
            empty.append(group_id)
            return ''
        block = re.sub(r'(<h2 id="titolo-[^"]+">)[^<]*(</h2>)',
                       lambda m: m[1] + escape(ui["group"]) + m[2], block)
        return re.sub(r'(<span>)[0-9]+ articoli(</span>)',
                      lambda m: m[1] + escape(ui["groupCount"]) + m[2], block, count=1)
    document = re.sub(r'<section class="group"[\s\S]*?</section>', group, document)
    for group_id in empty:
        document = re.sub(r'<li><a href="#' + re.escape(group_id) + r'">[^<]*</a></li>', '', document)
    document = document.replace('>Misure e metodo</a>', '>' + escape(ui["group"]) + '</a>')
    document = re.sub(r'(<span class="count">)[^<]*(</span>)',
                      lambda m: m[1] + escape(ui["count"]) + m[2], document)
    document = document.replace('Carattere tipografico e licenza', escape(ui["fontCredits"]))
    document = document.replace('Font incorporato per la lettura offline.',
                                'Police intégrée pour la lecture hors connexion.' if language == "fr" else 'Shkronjat janë të përfshira për lexim pa internet.')
    localized_covers = deepcopy(covers)
    for cover, caption in zip(localized_covers, ui["captions"]):
        cover["caption"] = caption
        cover["alt"] = caption
        cover["changes"] = ui["changes"]
    return render_covers(document, localized_covers, ui)
