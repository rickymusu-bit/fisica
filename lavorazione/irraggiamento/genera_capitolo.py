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
CSS = r'''
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:115px}body{margin:0;padding:18px;background:#080808;color:#080808;font-family:Lexend,Arial,sans-serif;font-size:21px;line-height:1.65;letter-spacing:.01em;text-align:left}a{color:inherit;text-underline-offset:4px}a:hover{text-decoration-thickness:3px}a:focus-visible,summary:focus-visible,.zoom-scroll:focus-visible{outline:3px solid #080808;outline-offset:4px}.page{max-width:1600px;margin:auto;border:3px solid #080808;background:#fff}.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:72px;padding:10px 30px;background:#c4c4c4;border-bottom:4px solid #080808}.brand{display:flex;align-items:center;gap:13px;text-decoration:none;font-size:29px;font-weight:650;min-height:44px}.app-icon{display:grid;place-items:center;width:40px;height:40px;border:3px solid #080808;box-shadow:inset 0 0 0 3px white;background:#080808;color:white;font-family:Georgia,serif;font-size:25px}.top-links{display:flex;align-items:center;gap:24px}.top-links>a{display:flex;align-items:center;min-height:44px;text-decoration:none;font-size:17px;font-weight:600;line-height:1.4}.hero{max-width:1160px;margin:auto;padding:65px 38px 58px}.kicker{font-size:14px;font-weight:650;letter-spacing:.08em;text-transform:uppercase;margin:0 0 25px}.hero-grid{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(280px,1fr);gap:45px;align-items:center}h1{font-size:clamp(46px,5.3vw,76px);font-weight:650;letter-spacing:0;line-height:1.15;margin:0}.hero .cover{margin:0;min-width:0}.cover .image-frame{box-shadow:8px 8px 0 #080808;transform:rotate(-1.5deg)}.cover img{width:100%;height:auto}.article-wrap{padding:0 36px 55px;border-top:3px solid #080808;background-image:repeating-conic-gradient(#ececec 0% 25%,#fff 0% 50%);background-size:6px 6px}.article{max-width:940px;margin:0 auto;padding:58px 72px 45px;border-right:3px solid #080808;border-left:3px solid #080808;background:white;min-width:0}.section-heading{margin:65px 0 28px;padding-top:35px;border-top:3px solid #080808}.section-heading:first-child{margin-top:0;padding-top:0;border:0}.section-number{display:block;font-size:14px;font-weight:650;letter-spacing:.07em;color:#444;margin-bottom:10px}h2{font-size:clamp(32px,3.3vw,45px);font-weight:650;line-height:1.25;letter-spacing:0;margin:0}h3{font-size:30px;line-height:1.35;font-weight:650;letter-spacing:0;margin:48px 0 25px}p{margin:0 0 27px}strong{font-weight:650}.visual{margin:35px 0 42px;min-width:0}.image-frame{border:3px solid #080808;background:#fff;min-width:0}.overview{display:flex;justify-content:center;align-items:center;min-width:0}.overview img{display:block;width:100%;max-width:100%;height:auto}.photo.portrait .image-frame{max-width:480px;margin:auto}.small .image-frame{max-width:240px;margin:auto}.small .overview img{width:240px}.gif .image-frame{max-width:600px;margin:auto}.gif picture{display:block;width:100%}.gif img{max-width:600px}.visual figcaption{font-size:16px;line-height:1.55;letter-spacing:.005em;color:#333;margin-top:14px}.image-zoom{border-top:2px solid #080808;font-size:14px;line-height:1.4}.image-zoom summary{min-height:44px;padding:12px 15px;cursor:pointer;background:#eee;font-weight:500}.zoom-scroll{overflow:auto;max-height:80vh;max-width:100%;background:white;padding:0}.zoom-scroll img{display:block;max-width:none;width:100%;height:auto}.image-frame:has(.image-zoom[open])>.overview{display:none}.equation{margin:32px 0 35px;border:2px solid #080808;box-shadow:5px 5px 0 #080808;background:#f7f7f7;min-width:0}.equation-label{padding:9px 15px;font-size:14px;font-weight:600;border-bottom:2px solid #080808;background:#c4c4c4;line-height:1.45}.math{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:7px 10px;padding:22px 12px;font-size:25px;line-height:1.85;letter-spacing:0}.math>span{white-space:nowrap}.math sub{font-size:.58em}.math sup{font-size:.68em}.math .fraction{display:inline-flex;flex-direction:column;vertical-align:middle;font-size:.8em;line-height:1.25;text-align:center;white-space:normal}.fraction>span:first-child{border-bottom:1.5px solid;padding:0 8px 4px}.fraction>span:last-child{padding-top:4px}.inline-math{white-space:nowrap;letter-spacing:0}.inline-math sub{font-size:.65em}.questions{padding-left:30px;margin:0}.questions li{padding-left:7px;margin-bottom:25px}.questions li::marker{font-weight:600}.bottom-links{display:flex;justify-content:space-between;flex-wrap:wrap;gap:15px;margin-top:45px}.button{display:inline-flex;align-items:center;justify-content:center;min-height:48px;border:3px solid #080808;background:#c4c4c4;padding:10px 15px;text-decoration:none;font-size:16px;font-weight:600;line-height:1.45}.button:hover{background:#080808;color:white}.credits{max-width:940px;margin:26px auto 0;padding:12px 20px;border:2px solid #080808;background:white;font-size:14px;line-height:1.6;overflow-wrap:anywhere}.credits>summary,.font-license>summary{min-height:34px;cursor:pointer;font-weight:500}.credits ul{padding-left:20px}.credits li{margin-bottom:12px}.credits p{font-size:14px;margin:20px 0 10px}.font-license pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px/1.5 monospace}.footer{border-top:3px solid #080808;background:#c4c4c4;padding:15px;text-align:center;font-size:14px;line-height:1.5}
.reader-index{display:block}.index-toggle{font:inherit;color:inherit;cursor:pointer;border:2px solid #080808;border-radius:0;background:#eee;min-height:44px;padding:8px 13px;display:inline-flex;align-items:center;justify-content:center;gap:10px;font-size:16px;line-height:1.4;font-weight:600;list-style:none;touch-action:manipulation}.index-toggle::-webkit-details-marker{display:none}.index-toggle::marker{content:''}.index-toggle:hover{background:#080808;color:white}.index-toggle:focus-visible{outline:3px solid #080808;outline-offset:4px}.summary-close{display:none}.list-icon{display:inline-block;width:17px;height:13px;border-top:2px solid currentColor;border-bottom:2px solid currentColor;position:relative}.list-icon:after{content:'';position:absolute;left:0;right:0;top:4px;border-top:2px solid currentColor}.reader-index[open]>.index-toggle{position:fixed;top:15px;left:246px;z-index:63;font-size:13px;padding:7px 10px}.reader-index[open] .summary-open,.reader-index[open] .list-icon{display:none}.reader-index[open] .summary-close{display:inline}.sidebar-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.24);z-index:60}.reader-sidebar{position:fixed;inset:0 auto 0 0;margin:0;width:350px;max-width:calc(100vw - 24px);height:100vh;height:100dvh;max-height:100vh;max-height:100dvh;padding:0;border:0;border-right:3px solid #080808;background:#eee;color:#080808;box-shadow:8px 0 0 #080808;font-family:Lexend,Arial,sans-serif;font-size:17px;line-height:1.6;z-index:61;display:flex;flex-direction:column}.sidebar-head{display:flex;align-items:center;min-height:77px;padding:16px 105px 16px 16px;background:#c4c4c4;border-bottom:3px solid #080808;flex-shrink:0}.sidebar-head h2{font-size:16px;line-height:1.4;margin:0;letter-spacing:0;font-weight:650}.sidebar-book{padding:24px 22px 20px;border-bottom:1px solid #aaa;background:white}.sidebar-label{font-size:13px;color:#444}.sidebar-book p{font-size:25px;font-weight:650;line-height:1.4;margin:7px 0 0}.sidebar-nav{overflow:auto;padding:15px 12px 30px;flex:1}.sidebar-nav ol{list-style:none;padding:0;margin:0}.sidebar-nav li+li{margin-top:7px}.sidebar-nav a{display:flex;align-items:flex-start;gap:11px;padding:12px 10px;min-height:48px;border:2px solid transparent;border-left:4px solid transparent;text-decoration:none;font-size:15px;font-weight:400;line-height:1.6;overflow-wrap:anywhere}.sidebar-nav .level-3 a{font-size:14px;padding-left:21px}.sidebar-nav a:hover{border-color:#080808;background:white}.sidebar-nav a[aria-current="location"]{border-left-color:#080808;background:white;font-weight:600}.sidebar-nav a:focus-visible{outline:3px solid #080808;outline-offset:-3px}.item-number{font-size:12px;padding-top:3px;flex-shrink:0;color:#444;min-width:20px}body.index-open,body:has(.reader-index[open]){overflow:hidden}[data-toc]:focus{outline:none}[data-toc]:focus-visible{outline:2px solid #080808;outline-offset:5px}
@media(max-width:1000px){.hero-grid{grid-template-columns:1fr}.hero{padding:42px 35px 48px}.hero .cover{max-width:600px}.article{padding:45px 38px}.topbar{padding:10px 20px}.hero-grid{gap:30px}.cover .image-frame{transform:none}.top-links{gap:18px}}
@media(max-width:560px){body{padding:6px;font-size:19px;line-height:1.65}.topbar{flex-wrap:nowrap;gap:8px;padding:8px 14px}.brand{font-size:21px;gap:8px}.app-icon{width:30px;height:30px;font-size:20px}.top-links{gap:10px}.top-links>a{font-size:12px;line-height:1.4;max-width:130px}.index-toggle{font-size:13px;padding:7px 9px;gap:7px}.hero{padding:30px 20px 35px}.kicker{font-size:12px;letter-spacing:.07em;margin-bottom:18px}h1{font-size:clamp(29px,8.3vw,44px)}.hero-grid{gap:24px}.hero .cover{margin-right:6px}.article-wrap{padding:0 12px 30px}.article{padding:32px 20px 35px}.section-heading{margin-top:48px;padding-top:28px;margin-bottom:23px}.section-number{font-size:13px}h2{font-size:29px;line-height:1.3}h3{font-size:25px;line-height:1.4;margin-top:35px}p{margin-bottom:25px}.visual{margin:29px 0 33px}.visual figcaption{font-size:15px;line-height:1.6}.equation{margin:27px 0 30px}.equation-label{font-size:13px;padding:8px 10px}.math{font-size:20px;padding:20px 8px;gap:5px 8px}.math>span:last-child{max-width:100%}.image-zoom summary{font-size:13px}.questions{padding-left:23px}.questions li{padding-left:3px;margin-bottom:24px}.bottom-links{flex-direction:column}.button{font-size:15px}.credits{font-size:13px;padding:12px 15px}.reader-sidebar{width:330px}.reader-index[open]>.index-toggle{left:min(226px,calc(100vw - 110px))}.sidebar-head h2{font-size:16px}}
@media(max-width:360px){.topbar{flex-wrap:wrap}.top-links{flex:1;justify-content:space-between}.top-links>a{max-width:none}.article{padding-left:15px;padding-right:15px}.math{font-size:18px}.math>span{white-space:normal}.hero{padding-left:16px;padding-right:16px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{body{padding:0;background:white}.page{border:0}.topbar,.reader-index,.bottom-links,.image-zoom{display:none!important}.article-wrap{padding:0;background:white}.article{border:0;padding:20px}.hero{padding:20px}.hero-grid{display:block}.hero .cover{max-width:500px;margin-top:25px}.cover .image-frame{transform:none;box-shadow:none}.visual,.equation{break-inside:avoid}.credits{max-width:none}body.index-open{overflow:visible}}
'''.replace("\n+", "\n")

CSS += '\n.image-zoom .zoom-collapse{display:none}.image-zoom[open] .zoom-expand{display:none}.image-zoom[open] .zoom-collapse{display:inline}\n'

sidebar_items = ''.join(f'<li class="level-{level}"><a href="#{ident}"><span class="item-number" aria-hidden="true">{number}</span><span>{html.escape(title)}</span></a></li>'
                        for level, ident, title, number in toc)
sidebar = ('<details class="reader-index" id="indice"><summary class="index-toggle"><span class="list-icon" aria-hidden="true"></span><span class="summary-open">Indice</span><span class="summary-close">Chiudi ×</span></summary>'
           '<div class="sidebar-backdrop" aria-hidden="true"></div><aside class="reader-sidebar" aria-labelledby="reader-index-title"><div class="sidebar-head"><h2 id="reader-index-title">Indice del capitolo</h2></div>'
           '<div class="sidebar-book"><span class="sidebar-label">Fisica</span><p>Irraggiamento</p></div><nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>' + sidebar_items + '</ol></nav></aside></details>')
JS = r'''
(()=>{
 const index=document.getElementById('indice'),toggle=index.querySelector('summary');
 const links=[...index.querySelectorAll('.sidebar-nav a')];
 const outside=[document.querySelector('main'),document.querySelector('.footer'),...document.querySelectorAll('.topbar>.brand,.top-links>a')];
 function sync(){document.body.classList.toggle('index-open',index.open);outside.forEach(e=>{if(e)e.inert=index.open;});}
 function closeIndex(restore=true){index.open=false;sync();if(restore)toggle.focus({preventScroll:true});}
 index.addEventListener('toggle',sync);
 index.querySelector('.sidebar-backdrop').addEventListener('click',()=>closeIndex());
 document.addEventListener('keydown',e=>{if(!index.open)return;if(e.key==='Escape'){e.preventDefault();closeIndex();}if(e.key==='Tab'){const items=[toggle,...links],first=items[0],last=items[items.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}});
 function mark(id){links.forEach(a=>{if(a.hash==='#'+id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}
 links.forEach(a=>a.addEventListener('click',()=>{mark(a.hash.slice(1));closeIndex(false);const heading=document.getElementById(a.hash.slice(1));if(heading)setTimeout(()=>heading.focus({preventScroll:true}),0);}));
 const headings=[...document.querySelectorAll('[data-toc]')];let scheduled=false;
 function current(){scheduled=false;let active=headings[0];for(const h of headings){if(h.getBoundingClientRect().top<=150)active=h;else break;}if(active)mark(active.id);}
 window.addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(current);}},{passive:true});current();
})();
'''

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
