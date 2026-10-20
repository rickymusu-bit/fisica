"""Tema Stringhe e pagine del portale, generate senza cambiare gli articoli sorgente."""
from html import escape, unescape
import json
import re

BASE = "https://rickymusu-bit.github.io/fisica/"


def e(value):
    return escape(str(value), quote=True)


def text_only(value):
    return unescape(re.sub(r"<[^>]*>", "", value)).strip()


def catalogue(source, allowed):
    records = []
    for group in re.finditer(r'<section class="group"[^>]*>(.*?)</section>', source, re.S):
        body = group.group(1)
        heading = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S)
        area = text_only(heading.group(1)) if heading else "Fisica"
        for item in re.finditer(r'<li class="material">(.*?)</li>', body, re.S):
            fragment = item.group(1)
            read = re.search(r'<a class="read" href="([^"]+)"', fragment)
            title = re.search(r'<h3[^>]*>(.*?)</h3>', fragment, re.S)
            description = re.search(r'<p[^>]*>(.*?)</p>', fragment, re.S)
            if not (read and title):
                raise ValueError("Articolo del catalogo incompleto")
            filename = unescape(read.group(1))
            if filename not in allowed:
                raise ValueError(f"Articolo non approvato nel catalogo: {filename}")
            records.append({"file": filename, "title": text_only(title.group(1)),
                            "description": text_only(description.group(1)) if description else "",
                            "area": area})
    if set(x["file"] for x in records) != set(allowed):
        raise ValueError("La selezione del portale non corrisponde al manifest")
    if len(records) != len(set(x["file"] for x in records)):
        raise ValueError("Articolo duplicato nel catalogo")
    return records


def font_css(source):
    match = re.search(r'@font-face\{.*?\}', source, re.S)
    return match.group(0) if match else ""


CSS = r"""
:root{--ink:#14213d;--blue:#4358ba;--teal:#16899b;--paper:#f6f9fe;--white:#fff;--line:#d8e0ed;--muted:#52617a;--shadow:0 14px 35px rgba(20,33,61,.09)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 Lexend,system-ui,sans-serif}
a{color:inherit}button,input{font:inherit}button{cursor:pointer}a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid var(--blue);outline-offset:4px}
.skip{position:absolute;left:-9999px;top:0;background:white;padding:12px;z-index:100}.skip:focus{left:12px}
.site-header{position:sticky;top:0;z-index:20;background:rgba(250,252,255,.96);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top-inner{max-width:1160px;margin:auto;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;gap:14px}
.brand{display:inline-flex;align-items:center;gap:12px;text-decoration:none;font-weight:750;font-size:22px;letter-spacing:-.045em}
.brand svg{width:48px;height:33px;flex-shrink:0}
.site-nav{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.site-nav>a,.lang>summary{padding:8px 12px;text-decoration:none;border-radius:11px;font-size:14px;font-weight:600;list-style:none;cursor:pointer}.site-nav>a:hover,.lang>summary:hover{background:#e9eefb}.lang{position:relative}.lang>summary{border:1px solid var(--line);background:white}.lang>summary::-webkit-details-marker{display:none}.lang-menu{position:absolute;right:0;top:calc(100% + 8px);min-width:170px;background:white;border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:12px;z-index:22;font-size:14px}
main{max-width:1160px;margin:auto;padding:36px 24px 80px}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(48px,8vw,96px);line-height:1.02;letter-spacing:-.065em;margin-bottom:16px}h2{font-size:clamp(25px,3vw,34px);line-height:1.18;letter-spacing:-.04em}h3{font-size:18px;line-height:1.4}.eyebrow{color:var(--blue);font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.14em}
.subtitle{font-size:clamp(20px,3vw,29px);color:var(--muted);max-width:660px;line-height:1.45}.hero{position:relative;overflow:hidden;border-radius:26px;border:1px solid var(--line);background:linear-gradient(120deg,#fff 40%,#eaf2ff);padding:clamp(25px,5vw,60px);box-shadow:var(--shadow)}.hero-copy{position:relative;z-index:2}
.strings{display:block;width:100%;height:auto}.hero-strings{position:absolute;top:0;right:-10%;width:62%;height:100%;opacity:.28;pointer-events:none}
.strings path{fill:none;stroke-linecap:round;stroke-width:2.4}.strings path:nth-child(1){stroke:var(--blue)}.strings path:nth-child(2){stroke:var(--teal)}.strings path:nth-child(3){stroke:#96a7df}
.hero-strings .strings{height:100%;width:100%;animation:sway 7s ease-in-out infinite alternate}
@keyframes sway{from{transform:translateY(-8px)}to{transform:translateY(8px)}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;scroll-behavior:auto!important}}
.actions{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin:24px 0 42px}
.action{display:flex;flex-direction:column;justify-content:space-between;gap:12px;min-height:128px;padding:22px;border:1px solid var(--line);border-radius:18px;background:var(--white);color:var(--ink);text-align:left;text-decoration:none;box-shadow:0 3px 12px rgba(20,33,61,.035)}
.action:hover{border-color:#9eace0;transform:translateY(-2px);box-shadow:var(--shadow)}.action-symbol{font-size:24px;color:var(--blue);line-height:1}.action strong{font-size:17px;line-height:1.3}.action small{color:var(--muted);font-size:12px}.action.lang-action{display:block;position:relative}.action.lang-action summary{cursor:pointer;list-style:none}.action.lang-action summary::-webkit-details-marker{display:none}.action.lang-action[open]{z-index:3}.action.lang-action .lang-menu{position:static;box-shadow:none;margin-top:10px}
.section-heading{display:flex;align-items:end;justify-content:space-between;gap:15px;margin:32px 0 18px}.section-heading p{color:var(--muted);margin:0}.section-heading a{text-decoration:none;color:var(--blue);font-weight:650}
.covers{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;align-items:stretch;margin-bottom:32px}
.cover{margin:0;overflow:hidden;background:#e4eaf3;border:1px solid var(--line);border-radius:20px}.cover img{width:100%;height:260px;display:block;object-fit:contain;background:#e6edf7}.cover figcaption{font-size:13px;color:var(--muted);background:white;padding:14px}
.category{display:flex;flex-direction:column;justify-content:center;gap:12px;border-radius:20px;background:white;border:1px solid var(--line);padding:30px;text-decoration:none}.category:hover{border-color:var(--blue)}.category span{color:var(--blue);font-weight:650;font-size:13px}.category h3{font-size:27px;letter-spacing:-.04em;margin:0}.category p{color:var(--muted);margin:0}
.featured{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.mini{display:block;border:1px solid var(--line);border-radius:16px;background:#fff;padding:23px;text-decoration:none;min-height:160px}.mini:hover{border-color:var(--blue)}.mini .number{color:var(--teal);font-size:12px;font-weight:700}.mini strong{display:block;margin-top:12px;line-height:1.4}.mini span:last-child{font-size:12px;color:var(--muted)}
.page-title{font-size:clamp(42px,6vw,70px);margin-bottom:14px}.lede{max-width:730px;color:var(--muted);font-size:18px;margin-bottom:26px}
.search{width:100%;padding:17px 20px;border:1px solid #a8b6ca;border-radius:15px;background:white;margin:16px 0 24px}
.chips{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:32px}.chip{border:1px solid var(--line);background:white;padding:10px 15px;border-radius:30px;font-size:13px;font-weight:650}.chip[aria-pressed=true]{background:var(--ink);color:white}
.count{color:var(--muted);font-size:13px}.group-heading{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin:16px 0}
.article-card{background:white;border:1px solid var(--line);border-radius:15px;margin-bottom:10px;padding:19px 22px;display:flex;align-items:center;justify-content:space-between;gap:16px}.article-card a:first-child{text-decoration:none;flex:1}.article-card a:first-child:hover h3{text-decoration:underline}.article-card h3{margin:0 0 7px}.article-card p{margin:0;color:var(--muted);font-size:13px}.download{flex-shrink:0;text-decoration:none;background:#e9eefb;color:var(--ink);border-radius:10px;padding:10px 13px;font-weight:650;font-size:13px}.download:hover{background:#dbe4fa}
.empty{padding:20px;color:var(--muted);border:1px dashed var(--line);border-radius:12px}
.placeholder{padding:36px;border:1px solid var(--line);border-radius:22px;background:white}.placeholder h2{margin-bottom:10px}
.site-footer{padding:22px 24px;border-top:1px solid var(--line);max-width:1160px;margin:auto;color:var(--muted);display:flex;gap:14px;flex-wrap:wrap;justify-content:space-between;font-size:13px}.site-footer a{color:var(--blue)}
[hidden]{display:none!important}
@media(max-width:800px){.actions{grid-template-columns:repeat(2,minmax(0,1fr))}.covers{grid-template-columns:1fr}.hero-strings{width:70%;right:-28%}}
@media(max-width:540px){.top-inner{padding:9px 14px;flex-wrap:wrap}.brand{font-size:19px}.site-nav{width:100%;gap:6px}.site-nav>a,.lang>summary{font-size:12px;padding:6px 9px}.site-nav>a:first-child{margin-left:-9px}main{padding:22px 15px 60px}.hero{padding:30px 23px}.hero-strings{opacity:.17}.action{padding:15px;min-height:112px}.action strong{font-size:14px}.section-heading{align-items:start}.featured{grid-template-columns:1fr}.mini{min-height:90px}.article-card{align-items:start;flex-direction:column}.download{align-self:flex-start}.cover img{height:200px}}
"""


def string_mark(large=False):
    css = ' class="strings"' if large else ''
    return ('<svg' + css + ' viewBox="0 0 180 76" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<path d="M-10 36 Q13 3 36 36 T82 36 T128 36 T174 36 T220 36" stroke="#4358ba" stroke-width="3" fill="none"/>'
            '<path d="M-10 42 Q13 70 36 42 T82 42 T128 42 T174 42 T220 42" stroke="#16899b" stroke-width="2.5" fill="none"/>'
            '<path d="M-10 38 H190" stroke="#9facce" stroke-width="1" fill="none"/></svg>')


def topbar():
    return (f'<header class="site-header"><div class="top-inner"><a class="brand" href="index.html" aria-label="Stringhe, vai alla home">'
            f'{string_mark()}<span>Stringhe</span></a><nav class="site-nav" aria-label="Navigazione principale">'
            '<a href="articoli.html">Articoli</a><a href="quiz.html">Quiz</a>'
            '<details class="lang" id="lingua"><summary aria-label="Seleziona la lingua">Italiano ▾</summary>'
            '<div class="lang-menu"><strong>Lingue disponibili</strong><p lang="it">✓ Italiano</p></div></details>'
            '</nav></div></header>')


def shell(title, body, source):
    return (f'<!doctype html><html lang="it"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="theme-color" content="#f6f9fe">'
            f'<meta name="description" content="Stringhe — L’essenziale della Fisica. Articoli e quiz di Fisica.">'
            f'<title>{e(title)} — Stringhe</title><style>{font_css(source)}{CSS}</style></head>'
            f'<body><a class="skip" href="#main">Vai al contenuto</a>{topbar()}'
            f'<main id="main">{body}</main>'
            '<footer class="site-footer"><span>Stringhe — L’essenziale della Fisica</span>'
            '<a href="crediti.html">Crediti e licenze</a></footer></body></html>')


def inline_covers(covers):
    return json.dumps([{"src": x["src"], "alt": x["alt"], "caption": x["caption"]}
                       for x in covers], ensure_ascii=False).replace("<", "\\u003c")


def render_home(source, covers, allowed):
    items = catalogue(source, allowed)
    paths = json.dumps([x["file"] for x in items], ensure_ascii=False).replace("<", "\\u003c")
    first = covers[0]
    groups = {}
    for item in items:
        groups.setdefault(item["area"], []).append(item)
    categories = "".join(
        f'<a class="category" href="articoli.html"><span>AREA TEMATICA</span><h3>{e(name)} ↗</h3>'
        f'<p>{len(group)} articoli. Esplora tutti i contenuti.</p></a>'
        for name, group in groups.items())
    selection = [items[i] for i in dict.fromkeys([0, len(items)//2, len(items)-1])]
    featured = "".join(
        f'<a class="mini" href="{e(x["file"])}"><span class="number">ARTICOLO {i+1:02d}</span>'
        f'<strong>{e(x["title"])}</strong><span>Leggi →</span></a>'
        for i, x in enumerate(selection))
    body = (f'<section class="hero"><div class="hero-strings">{string_mark(True)}</div>'
            '<div class="hero-copy"><p class="eyebrow">Articoli di fisica</p>'
            '<h1>Stringhe</h1><p class="subtitle">L’essenziale della Fisica</p></div></section>'
            '<section class="actions" aria-label="Accessi principali">'
            '<a class="action" href="articoli.html"><span class="action-symbol">≡</span><strong>Tutti gli articoli</strong><small>Scegli un argomento</small></a>'
            '<button class="action" id="random-article" type="button"><span class="action-symbol">↝</span><strong>Mi sento fortunato</strong><small>Leggi un articolo casuale</small></button>'
            '<a class="action" href="quiz.html"><span class="action-symbol">?</span><strong>Quiz</strong><small>Prossimamente</small></a>'
            '<details class="action lang-action"><summary><span class="action-symbol">文</span>'
            '<br><strong>Lingua</strong><br><small>Italiano ▾</small></summary>'
            '<div class="lang-menu">Disponibile: <strong>Italiano</strong></div></details></section>'
            '<section><div class="section-heading"><h2>Esplora gli argomenti</h2>'
            '<a href="articoli.html">Vedi tutti →</a></div><div class="covers">'
            f'<figure class="cover"><img id="random-cover" src="{e(first["src"])}" alt="{e(first["alt"])}" loading="eager">'
            f'<figcaption id="cover-caption">{e(first["caption"])}</figcaption></figure>'
            f'<div class="categories">{categories}</div></div></section>'
            '<section><div class="section-heading"><h2>Da leggere</h2></div>'
            f'<div class="featured">{featured}</div></section>'
            f'<script type="application/json" id="catalogue-data">{paths}</script>'
            f'<script type="application/json" id="cover-data">{inline_covers(covers)}</script>'
            '<script>(()=>{const articles=JSON.parse(document.getElementById("catalogue-data").textContent);'
            'const button=document.getElementById("random-article");'
            'button.addEventListener("click",()=>{if(articles.length)location.href=articles[Math.floor(Math.random()*articles.length)]});'
            'const covers=JSON.parse(document.getElementById("cover-data").textContent);'
            'if(covers.length){const c=covers[Math.floor(Math.random()*covers.length)];'
            'const img=document.getElementById("random-cover");img.src=c.src;img.alt=c.alt;'
            'document.getElementById("cover-caption").textContent=c.caption;}})();</script>'
            '<noscript><p>Per la scelta casuale serve JavaScript; puoi consultare il catalogo degli articoli.</p></noscript>')
    return shell("Home", body, source)


def render_catalogue(source, allowed):
    items = catalogue(source, allowed)
    groups = {}
    for x in items:
        groups.setdefault(x["area"], []).append(x)
    chips = '<button class="chip" data-area="all" aria-pressed="true">Tutti</button>'
    for area in groups:
        chips += f'<button class="chip" data-area="{e(area)}" aria-pressed="false">{e(area)}</button>'
    sections = ""
    for area, group in groups.items():
        cards = ""
        for record in group:
            search = (record["title"] + " " + record["description"] + " " + area).casefold()
            cards += (f'<article class="article-card" data-search="{e(search)}" data-area="{e(area)}">'
                      f'<a href="{e(record["file"])}"><h3>{e(record["title"])}</h3>'
                      f'<p>{e(record["description"])}</p></a>'
                      f'<a class="download" href="{e(record["file"])}" download="{e(record["file"])}"'
                      f' aria-label="Scarica {e(record["title"])} in HTML">↓ Scarica</a></article>')
        sections += (f'<section class="catalogue-group"><div class="group-heading">'
                     f'<h2>{e(area)}</h2></div>{cards}</section>')
    body = (f'<p class="eyebrow">Esplora</p><h1 class="page-title">Tutti gli articoli</h1>'
            f'<p class="lede">Cerca un argomento oppure esplora le aree tematiche. '
            f'Tutti gli articoli sono leggibili online e scaricabili in HTML.</p>'
            '<label for="article-search">Cerca nel catalogo</label>'
            '<input id="article-search" class="search" type="search" placeholder="Titolo o parola chiave" autocomplete="off">'
            f'<div class="chips" role="group" aria-label="Filtra per area tematica">{chips}</div>'
            f'<p class="count" id="result-count" aria-live="polite">{len(items)} articoli</p>'
            f'<div id="articles-list">{sections}</div>'
            '<p id="no-results" class="empty" hidden>Nessun articolo trovato. Prova un’altra ricerca.</p>'
            '<script>(()=>{const input=document.getElementById("article-search");'
            'const cards=[...document.querySelectorAll(".article-card")];'
            'const chips=[...document.querySelectorAll(".chip")];let area="all";'
            'const normalize=s=>s.toLocaleLowerCase("it").normalize("NFD").replace(/[\\u0300-\\u036f]/g,"");'
            'function filter(){const q=normalize(input.value.trim());let n=0;'
            'for(const card of cards){const ok=(area==="all"||card.dataset.area===area)'
            '&&normalize(card.dataset.search).includes(q);card.hidden=!ok;if(ok)n++;}'
            'for(const group of document.querySelectorAll(".catalogue-group")){'
            'group.hidden=![...group.querySelectorAll(".article-card")].some(card=>!card.hidden)}'
            'document.getElementById("result-count").textContent=n+" "+(n===1?"articolo":"articoli");'
            'document.getElementById("no-results").hidden=n!==0;}'
            'input.addEventListener("input",filter);'
            'for(const chip of chips)chip.addEventListener("click",()=>{area=chip.dataset.area;'
            'for(const b of chips)b.setAttribute("aria-pressed",String(b===chip));filter()});'
            'filter();})();</script>')
    return shell("Tutti gli articoli", body, source)


def render_quiz(source):
    body = ('<p class="eyebrow">In preparazione</p><h1 class="page-title">Quiz</h1>'
            '<p class="lede">Qui troverai quiz per verificare quello che hai imparato '
            'e giochi da svolgere in classe.</p>'
            '<section class="placeholder"><h2>Chi vuol essere rimandato</h2>'
            '<p>La funzionalità verrà integrata in una prossima versione. '
            'Nel frattempo puoi continuare a consultare gli articoli.</p>'
            '<a class="download" href="articoli.html">Vai agli articoli →</a></section>')
    return shell("Quiz", body, source)


ARTICLE_CSS = r"""
/* Navigazione e identità Stringhe; il contenuto scientifico resta invariato. */
body{background:#edf2fa!important;color:#14213d}
.page{border-color:#14213d;background:#fff}
.topbar{background:#f5f8ff!important;border-bottom:2px solid #cbd6e9!important;box-shadow:0 5px 20px rgba(20,33,61,.07);min-height:60px!important;flex-wrap:wrap!important}
.brand>a{color:#14213d!important;font-weight:750}
.top-links{display:flex!important;align-items:center;flex-wrap:wrap!important;gap:8px!important}
.top-links>.string-nav,.top-links>.string-lang>summary{display:inline-flex;align-items:center;justify-content:center;padding:9px 12px;border:1px solid #bdcae4;background:white;border-radius:10px;color:#14213d;text-decoration:none;font-size:13px;font-weight:650;line-height:1.25;min-height:40px;max-width:none}
.top-links>.string-nav:hover,.top-links>.string-lang>summary:hover{background:#e6edfa}
.string-lang{position:relative}
.string-lang>summary{cursor:pointer;list-style:none}
.string-lang>summary::-webkit-details-marker{display:none}
.string-lang>.string-languages{position:absolute;right:0;top:calc(100% + 8px);min-width:140px;padding:12px;border:1px solid #bdcae4;border-radius:10px;background:white;z-index:31;box-shadow:0 10px 24px rgba(20,33,61,.15);font-size:13px}
.hero{background:linear-gradient(140deg,#fff 65%,#f0f5ff)}
.kicker{color:#4358ba}
.hero:before{content:"";display:block;height:3px;width:min(300px,70%);background:linear-gradient(90deg,#4358ba,#16899b,transparent);margin-bottom:16px;border-radius:3px}
@media(max-width:560px){.topbar{padding:8px!important}.top-links>.string-nav,.top-links>.string-lang>summary{font-size:12px;padding:7px 8px;min-height:37px}.brand{font-size:18px!important}.top-links{gap:5px!important}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto!important}}
"""


def enhance_article(document, filename):
    # Barra integrata nel tema esistente: l'indice interno rimane operativo.
    document = document.replace("Materia Oscura", "Stringhe")
    document = document.replace("Guida pratica per fare luce sulla Fisica", "L’essenziale della Fisica")
    document = document.replace("https://rickymusu-bit.github.io/fisica/#indice", BASE + "articoli.html")
    document = document.replace('<a href="#inizio">Fisica</a>', '<a href="#inizio">Stringhe</a>', 1)
    document = re.sub(r'<a[^>]*>\s*← Articoli\s*</a>', '', document, count=1)
    controls = (f'<a class="string-nav" href="{BASE}">⌂ Home</a>'
                f'<a class="string-nav" href="{BASE}articoli.html">← Articoli</a>'
                f'<a class="string-nav" href="{e(filename)}" download="{e(filename)}">↓ Scarica</a>'
                '<details class="string-lang"><summary aria-label="Seleziona lingua">IT ▾</summary>'
                '<div class="string-languages" lang="it">✓ Italiano</div></details>')
    # Gli articoli hanno piccole variazioni negli attributi del nav.
    # Individua l'elemento dalla classe, senza dipendere dall'aria-label esatta.
    navigation_pattern = r'<nav\\b[^>]*\\bclass\\s*=\\s*["\\\'][^"\\\']*\\btop-links\\b[^"\\\']*["\\\'][^>]*>'
    document, inserted = re.subn(navigation_pattern,
                                 lambda match: match.group(0) + controls,
                                 document, count=1, flags=re.I)
    if inserted != 1:
        raise ValueError(f"Barra di navigazione top-links non trovata: {filename}")
    document = document.replace('</head>', '<style data-theme="stringhe">' + ARTICLE_CSS + '</style></head>', 1)
    return document
