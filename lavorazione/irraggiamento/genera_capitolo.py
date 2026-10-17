"""Genera l'HTML autonomo dal testo concordato e dai materiali conservati."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import base64
import html
import json
import re
import unicodedata
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from chapter_navigation import insert_navigation
RES = HERE / "risorse"
ASSETS = json.loads((RES / "asset-finali.json").read_text())
REGISTRY = json.loads((RES / "registro-visuali.json").read_text())
HOME = "https://rickymusu-bit.github.io/fisica/#indice"
TODAY = datetime.now(ZoneInfo("Europe/Rome")).strftime("%d/%m/%Y")


def data_uri(path):
    path = Path(path)
    mime = {".webp": "image/webp", ".png": "image/png", ".gif": "image/gif",
            ".svg": "image/svg+xml", ".jpg": "image/jpeg", ".ttf": "font/ttf"}[path.suffix]
    return "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode()


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",
                  lambda m: '<a href="' + m[2] + '" target="_blank" rel="noopener">' + m[1] + '</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    mappings = {
        r"\(P_{\mathrm{emessa}}\)": '<span class="inline-math">P<sub>emessa</sub></span>',
        r"\(P_{\mathrm{netta}}\)": '<span class="inline-math">P<sub>netta</sub></span>',
        r"\(T_{\mathrm{amb}}\)": '<span class="inline-math">T<sub>amb</sub></span>',
        r"\(A\)": '<span class="inline-math">A</span>',
        r"\(T\)": '<span class="inline-math">T</span>',
        r"\(\sigma\)": "σ",
        r"\(\varepsilon\)": "ε",
    }
    for before, after in mappings.items():
        text = text.replace(before, after)
    return text


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def figure(ident, caption="", cover=False):
    asset = ASSETS[ident]
    full_uri = data_uri(RES / asset["file"])
    preview_uri = data_uri(RES / asset.get("preview", asset["file"]))
    alt = html.escape(asset["alt"], quote=True)
    width, height = asset["size"]
    media = f'<img src="{preview_uri}" alt="{alt}" width="{width}" height="{height}" loading="{"eager" if cover else "lazy"}" decoding="async">'
    if asset.get("kind") == "gif":
        still = data_uri(RES / "ottimizzate/effetto-serra-statico.webp")
        media = f'<picture><source media="(prefers-reduced-motion: reduce)" srcset="{still}">{media}</picture>'
    zoom = ""
    if asset.get("zoom"):
        minimum = asset.get("min_width", 800)
        zoom = (f'<details class="image-zoom"><summary><span class="zoom-expand">Ingrandisci l’immagine</span><span class="zoom-collapse">Rimpicciolisci l’immagine</span></summary>'
                f'<div class="zoom-scroll" tabindex="0" role="region" aria-label="Immagine ingrandita scorrevole: {alt}">'
                f'<img src="{full_uri}" alt="{alt}" width="{width}" height="{height}" loading="lazy" decoding="async" style="min-width:{minimum}px">'
                '</div></details>')
    kind = "cover" if cover else asset.get("kind", "photo")
    frame = f'<div class="image-frame"><div class="overview">{media}</div>{zoom}</div>'
    cap = f'<figcaption>{inline(caption)}</figcaption>' if caption else ""
    return f'<figure class="visual {kind}" id="visual-{ident}" data-visual="{ident}">{frame}{cap}</figure>'


EQUATIONS = [
    ('Potenza termica emessa', '<span>P<sub>emessa</sub> =</span> <span>ε · σ · A · T<sup>4</sup></span>',
     'Potenza emessa uguale a emissività per costante di Stefan Boltzmann per area per temperatura assoluta alla quarta'),
    ('Costante di Stefan–Boltzmann', '<span>σ ≈ 5,67 · 10<sup>−8</sup></span> <span class="fraction"><span>W</span><span>m² · K⁴</span></span>',
     'Sigma circa 5 virgola 67 per dieci alla meno otto watt diviso metri quadrati per kelvin alla quarta'),
    ('Confronto fra temperature assolute', '<span>2<sup>4</sup> = 16</span>', 'Due alla quarta uguale sedici'),
    ('Potenza netta ceduta', '<span>P<sub>netta</sub> =</span> <span>P<sub>emessa</sub> − P<sub>assorbita</sub></span>',
     'Potenza netta ceduta uguale a potenza emessa meno potenza assorbita'),
    ('Scambio con un ambiente a temperatura uniforme', '<span>P<sub>netta</sub> =</span> <span>ε · σ · A · (T<sup>4</sup> − T<sub>amb</sub><sup>4</sup>)</span>',
     'Potenza netta ceduta uguale a emissività per sigma per area per la differenza fra le quarte potenze delle temperature assolute del corpo e dell’ambiente'),
]


paragraphs = re.split(r"\n\s*\n", (HERE / "bozza.md").read_text().strip())
body = []
toc = []
questions = []
equation_i = 0
heading_i = 0
subheading_i = 0
cover_html = ""
last_was_question = False
i = 0
while i < len(paragraphs):
    part = paragraphs[i].strip()
    if part.startswith("# "):
        i += 1
        continue
    match = re.match(r"\[(COPERTINA|IMMAGINE|GRAFICO|ANIMAZIONE) ([\w-]+)", part)
    if match:
        ident = match[2]
        j = i + 1
        if j < len(paragraphs) and paragraphs[j].startswith("!["):
            j += 1
        caption = ""
        if j < len(paragraphs) and paragraphs[j].startswith("*") and paragraphs[j].endswith("*"):
            caption = paragraphs[j][1:-1]
            j += 1
        rendered = figure(ident, caption, cover=match[1] == "COPERTINA")
        if match[1] == "COPERTINA":
            cover_html = rendered
        else:
            body.append(rendered)
        i = j
        continue
    if part.startswith("\\["):
        name, expression, aria = EQUATIONS[equation_i]
        body.append(f'<div class="equation" data-equation="{equation_i + 1}"><div class="equation-label">{name}</div><div class="math" role="math" aria-label="{aria}">{expression}</div></div>')
        equation_i += 1
    elif part.startswith("### "):
        title = part[4:]
        subheading_i += 1
        ident = slug(title)
        toc.append((3, ident, title, f"{heading_i}.{subheading_i}"))
        body.append(f'<h3 id="{ident}" data-toc tabindex="-1">{inline(title)}</h3>')
    elif part.startswith("## "):
        title = part[3:]
        heading_i += 1
        subheading_i = 0
        ident = slug(title)
        toc.append((2, ident, title, f"{heading_i:02d}"))
        body.append(f'<div class="section-heading"><span class="section-number" aria-hidden="true">{heading_i:02d}</span><h2 id="{ident}" data-toc tabindex="-1">{inline(title)}</h2></div>')
    elif re.match(r"^\d+\. ", part):
        for line in part.splitlines():
            m = re.match(r"^(\d+)\. (.*)", line)
            if m:
                questions.append(m[2])
        last_was_question = True
    else:
        body.append("<p>" + inline(part) + "</p>")
    i += 1

assert equation_i == len(EQUATIONS)
assert len(questions) == 15
body.append('<ol class="questions">' + ''.join('<li>' + inline(q) + '</li>' for q in questions) + '</ol>')
body.append(f'<nav class="bottom-links" aria-label="Navigazione finale"><a class="button" href="{HOME}">← Biblioteca</a><a class="button" href="#inizio">Torna all’inizio</a></nav>')

credits = []
for item in REGISTRY["materiali"]:
    ident = item["id"]
    source = item.get("pagina_fonte") or item.get("url_originale_fornito")
    if ident == "T1-bilancio":
        author = item.get("autore_originale", "")
    else:
        author = item.get("autore") or "Autore non identificato"
    license_name = item.get("licenza") or "Licenza non identificata"
    line = html.escape(item["soggetto"]) + " — " + html.escape(author) + ". " + html.escape(license_name) + "."
    if source:
        line += ' <a href="' + html.escape(source, quote=True) + '" target="_blank" rel="noopener">Fonte</a>.'
    if item.get("url_licenza"):
        line += ' <a href="' + html.escape(item["url_licenza"], quote=True) + '" target="_blank" rel="noopener">Licenza</a>.'
    if ident in ["T2", "T6", "T7", "A4"]:
        line += " Etichette in italiano; copia adattata e ottimizzata."
    elif ident == "T1-bilancio":
        line += " Modifica: frecce, legenda e temperature di un esempio ipotetico."
    elif ident == "G1":
        line += " Curva teorica, nessuna misura sperimentale."
    credits.append("<li>" + line + "</li>")
license_text = html.escape((RES / "lexend-licenza.txt").read_text(encoding="utf-8-sig"))
credits_html = ('<details class="credits"><summary>Crediti delle immagini e del carattere</summary><ul>' + ''.join(credits) +
                '</ul><p>Lexend — The Lexend Project Authors. Font incorporato, SIL Open Font License 1.1.</p>'
                '<details class="font-license"><summary>Licenza del carattere</summary><pre>' + license_text + '</pre></details></details>')

font_uri = data_uri(RES / "lexend.ttf")
CSS = (ROOT / "tema/capitolo.css").read_text()


sidebar_items = ''.join(f'<li class="level-{level}"><a href="#{ident}"><span class="item-number" aria-hidden="true">{number}</span><span>{html.escape(title)}</span></a></li>'
                        for level, ident, title, number in toc)
sidebar = ('<details class="reader-index" id="indice"><summary class="index-toggle"><span class="list-icon" aria-hidden="true"></span><span class="summary-open">Indice</span><span class="summary-close">Chiudi ×</span></summary>'
           '<div class="sidebar-backdrop" aria-hidden="true"></div><aside class="reader-sidebar" aria-labelledby="reader-index-title"><div class="sidebar-head"><h2 id="reader-index-title">Indice del capitolo</h2></div>'
           '<div class="sidebar-book"><span class="sidebar-label">Fisica</span><p>Irraggiamento</p></div><nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>' + sidebar_items + '</ol></nav></aside></details>')
JS = (ROOT / "tema/indice.js").read_text()

document = (f'<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<meta name="version" content="v3"><meta name="date" content="{TODAY}"><meta name="author" content="Riccardo Musumarra">'
            '<meta name="description" content="Irraggiamento termico: radiazione elettromagnetica, emissività, legge di Stefan–Boltzmann, bilancio radiativo e applicazioni.">'
            '<title>Irraggiamento</title><style>'
            f'@font-face{{font-family:Lexend;src:url({font_uri}) format("truetype");font-weight:100 900;font-display:swap}}'
            + CSS + '</style></head><body><div class="page" id="inizio">'
            f'<header class="topbar"><a class="brand" href="#inizio"><span class="app-icon" aria-hidden="true">φ</span>Fisica</a><nav class="top-links" aria-label="Navigazione principale"><a href="{HOME}">← Biblioteca</a>{sidebar}</nav></header>'
            '<main><div class="hero"><p class="kicker">Fisica</p><div class="hero-grid"><h1>Irraggiamento</h1>' + cover_html + '</div></div>'
            '<div class="article-wrap"><article class="article">' + ''.join(body) + '</article>' + credits_html + '</div></main>'
            f'<footer class="footer">Versione v3 · {TODAY}</footer></div><script>' + JS + '</script></body></html>')
assert "\\[" not in document and "\\(" not in document
assert len(re.findall(r'data-visual="', document)) == len(ASSETS)
assert len(questions) == 15
target = ROOT / "irraggiamento_it.html"
document = insert_navigation(document, target.name)
target.write_text(document)
(HERE / "bozza.html").write_text(document)
print({"file": str(target), "byte": target.stat().st_size, "immagini": len(ASSETS), "domande": len(questions), "formule": equation_i})
