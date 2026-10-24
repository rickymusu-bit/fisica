"""Tema Stringhe e pagine del portale, generate senza cambiare gli articoli sorgente."""
from html import escape, unescape
from html.parser import HTMLParser
from datetime import datetime, time
from zoneinfo import ZoneInfo
import json
import re
from stringhe_theme import apply_theme, navigation_header, logo, logo_script, ROOT, icon

BASE = "./"


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
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 Lexend,system-ui,sans-serif}
a{color:inherit}button,input{font:inherit}button{cursor:pointer}a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid var(--blue);outline-offset:4px}
.skip{position:absolute;left:-9999px;top:0;background:var(--surface);padding:12px;z-index:100}.skip:focus{left:12px}
.site-header{position:sticky;top:0;z-index:20;background:var(--surface);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top-inner{max-width:1160px;margin:auto;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;gap:14px}
.brand{display:inline-flex;align-items:center;gap:12px;text-decoration:none;font-weight:750;font-size:22px;letter-spacing:-.045em}
.brand svg{width:48px;height:33px;flex-shrink:0}
.home-title-link{display:inline-flex;align-items:center;min-height:44px;text-decoration:none}
.site-nav{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.site-nav>a,.lang>summary{padding:8px 12px;text-decoration:none;border-radius:11px;font-size:14px;font-weight:600;list-style:none;cursor:pointer}.site-nav>a:hover,.lang>summary:hover{background:var(--surface-soft)}.lang{position:relative}.lang>summary{border:1px solid var(--line);background:var(--surface)}.lang>summary::-webkit-details-marker{display:none}.lang-menu{position:absolute;right:0;top:calc(100% + 8px);min-width:170px;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:12px;z-index:22;font-size:14px}
main{max-width:1160px;margin:auto;padding:36px 24px 80px}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(48px,8vw,96px);line-height:1.02;letter-spacing:-.065em;margin-bottom:16px}h2{font-size:clamp(25px,3vw,34px);line-height:1.18;letter-spacing:-.04em}h3{font-size:18px;line-height:1.4}.eyebrow{color:var(--blue);font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.14em}
.subtitle{font-size:clamp(20px,3vw,29px);color:var(--accent);max-width:660px;line-height:1.45}.hero{position:relative;overflow:hidden;border-radius:26px;border:1px solid var(--line);background:var(--surface);padding:clamp(25px,5vw,60px);box-shadow:var(--shadow)}.hero-copy{position:relative;z-index:2}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;scroll-behavior:auto!important}}
.actions{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:24px 0 42px}
.action{display:flex;flex-direction:column;justify-content:space-between;gap:12px;min-height:128px;padding:22px;border:1px solid var(--line);border-radius:18px;background:var(--white);color:var(--ink);text-align:left;text-decoration:none;box-shadow:0 3px 12px rgba(20,33,61,.035)}
.action:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:var(--shadow)}.action-symbol{font-size:24px;color:var(--blue);line-height:1}.action strong{font-size:17px;line-height:1.3}.action small{color:var(--muted);font-size:12px}.action.lang-action{display:block;position:relative}.action.lang-action summary{cursor:pointer;list-style:none}.action.lang-action summary::-webkit-details-marker{display:none}.action.lang-action[open]{z-index:3}.action.lang-action .lang-menu{position:static;box-shadow:none;margin-top:10px}
.section-heading{display:flex;align-items:end;justify-content:space-between;gap:15px;margin:32px 0 18px}.section-heading p{color:var(--muted);margin:0}.section-heading a{text-decoration:none;color:var(--blue);font-weight:650}
.covers{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;align-items:stretch;margin-bottom:32px}
.cover{margin:0;overflow:hidden;background:var(--surface-soft);border:1px solid var(--line);border-radius:20px}.cover img{width:100%;height:260px;display:block;object-fit:contain;background:#fff}.cover figcaption{font-size:13px;color:var(--muted);background:var(--surface);padding:14px}
.category{display:flex;flex-direction:column;justify-content:center;gap:12px;border-radius:20px;background:var(--surface);border:1px solid var(--line);padding:30px;text-decoration:none}.category:hover{border-color:var(--blue)}.category span{color:var(--blue);font-weight:650;font-size:13px}.category h3{font-size:27px;letter-spacing:-.04em;margin:0}.category p{color:var(--muted);margin:0}
.featured{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.mini{display:block;border:1px solid var(--line);border-radius:16px;background:var(--surface);padding:23px;text-decoration:none;min-height:160px}.mini:hover{border-color:var(--blue)}.mini .chapter-update{color:var(--teal);font-size:12px;font-weight:700}.mini strong{display:block;margin-top:12px;line-height:1.4}.mini span:last-child{font-size:12px;color:var(--muted)}
.page-title{font-size:clamp(42px,6vw,70px);margin-bottom:14px}.lede{max-width:730px;color:var(--muted);font-size:18px;margin-bottom:26px}
.search{width:100%;padding:17px 20px;border:1px solid var(--line);border-radius:15px;background:var(--surface);margin:16px 0 24px}
.chips{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:32px}.chip{border:1px solid var(--line);background:var(--surface);padding:10px 15px;border-radius:30px;font-size:13px;font-weight:650}.chip[aria-pressed=true]{background:var(--ink);color:var(--surface)}
.count{color:var(--muted);font-size:13px}.group-heading{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin:16px 0}
.article-card{background:var(--surface);border:1px solid var(--line);border-radius:15px;margin-bottom:10px;padding:19px 22px;display:flex;align-items:center;justify-content:space-between;gap:16px}.article-card a:first-child{text-decoration:none;flex:1}.article-card a:first-child:hover h3{text-decoration:underline}.article-card h3{margin:0 0 7px}.article-card p{margin:0;color:var(--muted);font-size:13px}.download{flex-shrink:0;text-decoration:none;background:var(--surface-soft);color:var(--ink);border-radius:10px;padding:10px 13px;font-weight:650;font-size:13px}.download:hover{background:var(--surface-soft)}
.empty{padding:20px;color:var(--muted);border:1px dashed var(--line);border-radius:12px}
.placeholder{padding:36px;border:1px solid var(--line);border-radius:22px;background:var(--surface)}.placeholder h2{margin-bottom:10px}
.site-footer{padding:22px 24px;border-top:1px solid var(--line);max-width:1160px;margin:auto;color:var(--muted);display:flex;gap:14px;flex-wrap:wrap;justify-content:space-between;font-size:13px}.site-footer a{color:var(--blue)}
[hidden]{display:none!important}
@media(max-width:800px){.actions{grid-template-columns:repeat(3,minmax(0,1fr))}.covers{grid-template-columns:1fr}.hero-strings{width:70%;right:-28%}}
@media(max-width:540px){.actions{grid-template-columns:1fr}.top-inner{padding:9px 14px;flex-wrap:wrap}.brand{font-size:19px}.site-nav{width:100%;gap:6px}.site-nav>a,.lang>summary{font-size:12px;padding:6px 9px}.site-nav>a:first-child{margin-left:-9px}main{padding:22px 15px 60px}.hero{padding:30px 23px}.hero-strings{opacity:.17}.action{padding:15px;min-height:112px}.action strong{font-size:14px}.section-heading{align-items:start}.featured{grid-template-columns:1fr}.mini{min-height:90px}.article-card{align-items:start;flex-direction:column}.download{align-self:flex-start}.cover img{height:200px}}
"""



def chapter_labels(document):
    """Aggiorna solo diciture di servizio, conservando testo scientifico e URL."""
    for old, new in {
        '← Articoli': '← Capitoli',
        'Indice dell’articolo': 'Indice del capitolo',
        "Indice dell'articolo": "Indice del capitolo",
        'Articolo precedente': 'Capitolo precedente',
        'Articolo successivo': 'Capitolo successivo',
        'Articolo collegato': 'Capitolo collegato',
        'Crediti di tutti gli articoli': 'Crediti di tutti i capitoli',
        'Titolo dell’articolo': 'Titolo del capitolo',
    }.items():
        document = document.replace(old, new)
    return document


def shell(title, body, source, home=False, service=False):
    credits = re.search(r'<!-- resource-credits:start -->[\s\S]*?<!-- resource-credits:end -->', source)
    credits = chapter_labels(credits.group(0)) if credits else '<a href="crediti.html">Crediti e licenze</a>'
    return apply_theme(f'<!doctype html><html lang="it"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="theme-color" content="#f6f9fe">'
            f'<meta name="description" content="Stringhe — L’essenziale della Fisica. Capitoli e quiz di Fisica.">'
            f'<title>{e(title)} — Stringhe</title><style>{font_css(source)}{CSS}</style></head>'
            f'<body><a class="skip" href="#main">Vai al contenuto</a>{navigation_header('home' if home else ('catalogue' if title == 'Tutti i capitoli' else ('quiz' if title == 'Quiz' else 'comparison')))}'
            f'<main id="main">{body}</main>'
            '<footer class="site-footer"><span>Stringhe — L’essenziale della Fisica</span>'
            f'</footer>{credits}{logo_script()}</body></html>')


def inline_covers(covers):
    return json.dumps([{"src": x["src"], "alt": x["alt"], "caption": x["caption"], "width": x["width"], "height": x["height"]}
                       for x in covers], ensure_ascii=False).replace("<", "\\u003c")


class ChapterDate(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.value = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name') == 'date':
            self.value = attrs.get('content')


def recent_chapters(items, root=ROOT, limit=3):
    """Date editoriali dei soli capitoli ammessi; nessuna dipendenza da Git/mtime."""
    months = ('gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno',
              'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre')
    dated = []
    for position, item in enumerate(items):
        value = ChapterDate((root / item['file']).read_text(encoding='utf-8-sig')).value
        if value is None:
            raise ValueError(f"Data editoriale mancante: {item['file']}")
        changed = datetime.fromisoformat(value)
        rome = ZoneInfo('Europe/Rome')
        if changed.tzinfo is None:
            if len(value) != 10:
                raise ValueError(f"Orario editoriale senza fuso: {item['file']}")
            changed = datetime.combine(changed.date(), time.min, rome)
        changed = changed.astimezone(rome)
        dated.append((changed, position, {**item, 'date': changed.isoformat(),
                      'date_label': f'{changed.day} {months[changed.month - 1]} {changed.year}'}))
    # Orario di pubblicazione incluso; ordine del catalogo solo a pari istante.
    dated.sort(key=lambda entry: (entry[0], entry[1]), reverse=True)
    return [entry[2] for entry in dated[:limit]]


def render_home(source, covers, allowed):
    items = catalogue(source, allowed)
    paths = json.dumps([x["file"] for x in items], ensure_ascii=False).replace("<", "\\u003c")
    first = covers[0]
    featured = "".join(
        f'<a class="mini" href="{e(x["file"])}">'
        f'<span class="chapter-update">Aggiornato il <time datetime="{x["date"]}">{x["date_label"]}</time></span>'
        f'<strong>{e(x["title"])}</strong><span>Leggi →</span></a>'
        for x in recent_chapters(items))
    body = (f'<section class="hero home-title home-intro">'
            '<div class="hero-copy">'
            f'<div class="hero-title">{logo()}<h1><a class="home-title-link" href="index.html" aria-label="Stringhe, home">Stringhe</a></h1></div><p class="subtitle">L’essenziale della Fisica</p></div>'
            f'<figure class="home-cover" style="--cover-ratio:{first["width"]/first["height"]:.8f}"><img id="random-cover" src="{e(first["src"])}" alt="{e(first["alt"])}" width="{first["width"]}" height="{first["height"]}" loading="eager">'
            f'<figcaption id="cover-caption">{e(first["caption"])}</figcaption></figure></section>'
            '<section class="actions" aria-label="Accessi principali">'
            '<a class="action" href="articoli.html"><span class="action-symbol">≡</span><strong>Tutti i capitoli</strong><small>Scegli un argomento</small></a>'
            '<button class="action" id="random-article" type="button"><span class="action-symbol">↝</span><strong>Mi sento fortunato</strong><small>Leggi un capitolo casuale</small></button>'
            '<a class="action" href="quiz.html"><span class="action-symbol">?</span><strong>Quiz</strong><small>25 domande, tre livelli</small></a>'
            '</section>'
            '<section aria-labelledby="news-title"><div class="section-heading"><h2 id="news-title">Novità</h2>'
            '<a href="articoli.html">Tutti i capitoli →</a></div>'
            f'<div class="featured">{featured}</div></section>'
            f'<script type="application/json" id="catalogue-data">{paths}</script>'
            f'<script type="application/json" id="cover-data">{inline_covers(covers)}</script>'
            '<script>(()=>{const articles=JSON.parse(document.getElementById("catalogue-data").textContent);'
            'const button=document.getElementById("random-article");'
            'button.addEventListener("click",()=>{if(articles.length)location.href=articles[Math.floor(Math.random()*articles.length)]});'
            'const covers=JSON.parse(document.getElementById("cover-data").textContent);'
            'if(covers.length){const c=covers[Math.floor(Math.random()*covers.length)];'
            'const img=document.getElementById("random-cover");img.width=c.width;img.height=c.height;'
            'img.closest("figure").style.setProperty("--cover-ratio",c.width/c.height);img.src=c.src;img.alt=c.alt;'
            'document.getElementById("cover-caption").textContent=c.caption;}})();</script>'
            '<noscript><p>Per la scelta casuale serve JavaScript; puoi consultare il catalogo dei capitoli.</p></noscript>')
    return shell("Home", body, source, home=True)


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
    body = (f'<p class="eyebrow">Esplora</p><h1 class="page-title">Tutti i capitoli</h1>'
            f'<p class="lede">Cerca un argomento oppure esplora le aree tematiche. '
            f'Tutti i capitoli sono leggibili online e scaricabili in HTML.</p>'
            '<label for="article-search">Cerca nel catalogo</label>'
            '<input id="article-search" class="search" type="search" placeholder="Titolo o parola chiave" autocomplete="off">'
            f'<div class="chips" role="group" aria-label="Filtra per area tematica">{chips}</div>'
            f'<p class="count" id="result-count" aria-live="polite">{len(items)} capitoli</p>'
            f'<div id="articles-list">{sections}</div>'
            '<p id="no-results" class="empty" hidden>Nessun capitolo trovato. Prova un’altra ricerca.</p>'
            '<script>(()=>{const input=document.getElementById("article-search");'
            'const cards=[...document.querySelectorAll(".article-card")];'
            'const chips=[...document.querySelectorAll(".chip")];let area="all";'
            'const normalize=s=>s.toLocaleLowerCase("it").normalize("NFD").replace(/[\\u0300-\\u036f]/g,"");'
            'function filter(){const q=normalize(input.value.trim());let n=0;'
            'for(const card of cards){const ok=(area==="all"||card.dataset.area===area)'
            '&&normalize(card.dataset.search).includes(q);card.hidden=!ok;if(ok)n++;}'
            'for(const group of document.querySelectorAll(".catalogue-group")){'
            'group.hidden=![...group.querySelectorAll(".article-card")].some(card=>!card.hidden)}'
            'document.getElementById("result-count").textContent=n+" "+(n===1?"capitolo":"capitoli");'
            'document.getElementById("no-results").hidden=n!==0;}'
            'input.addEventListener("input",filter);'
            'for(const chip of chips)chip.addEventListener("click",()=>{area=chip.dataset.area;'
            'for(const b of chips)b.setAttribute("aria-pressed",String(b===chip));filter()});'
            'filter();})();</script>')
    return shell("Tutti i capitoli", body, source, service=True)


def render_quiz(source, allowed):
    from quiz_site import render_quiz_page
    return render_quiz_page(source, allowed, catalogue, shell)


def enhance_article(document, filename):
    # Solo l'HTML pubblicabile viene modificato: sorgenti originali intatti.
    document = document.replace("Materia Oscura", "Stringhe")
    document = document.replace("Guida pratica per fare luce sulla Fisica", "L’essenziale della Fisica")
    document = document.replace("https://rickymusu-bit.github.io/fisica/#indice", "articoli.html")
    header_pattern = r'<header\b[^>]*class="[^"]*\btopbar\b[^"]*"[^>]*>[\s\S]*?</header>'
    def replace_header(match):
        original = match.group(0)
        index = re.search(r'<details\b[^>]*class="[^"]*\breader-index\b[^"]*"[^>]*>[\s\S]*?</details>', original)
        if not index:
            raise ValueError(f'Indice del capitolo assente: {filename}')
        return navigation_header('chapter', filename, index.group(0))
    document, matched = re.subn(header_pattern, replace_header, document, count=1)
    if matched != 1:
        raise ValueError(f'Barra del capitolo assente: {filename}')
    document = document.replace('href="articoli.html">← Articoli', 'href="articoli.html" data-site-path="articoli.html">← Articoli')
    document = document.replace('href="https://rickymusu-bit.github.io/fisica/crediti.html"', 'href="crediti.html" data-site-path="crediti.html"')
    return apply_theme(chapter_labels(document))


def render_comparison(source):
    body = '''<p class="eyebrow">Confronto del tema</p><h1 class="page-title">Bordi e reticolo</h1>
<p class="lede">Confronta le stesse superfici con due curve tracciate separatamente. Configurazione scelta: reticolo regolare e sinusoidi verticali di uguale ampiezza. Le alternative restano disponibili per confronto.</p>
<div class="comparison-toolbar">
<label>Bordi <select id="border-variant"><option value="A">A — ampiezze uguali</option><option value="B">B — seconda ampiezza al 60%</option></select></label>
<label>Reticolo <select id="grid-variant"><option value="A">A — ortogonale</option><option value="B">B — lieve curvatura</option></select></label>
<label>Posizione <select id="edge-variant"><option value="sides">Ai lati, in verticale</option><option value="both">Sopra e sotto</option><option value="top">Solo sopra</option></select></label>
</div>
<section class="hero"><div class="hero-copy"><p class="eyebrow">Stringhe</p><h2>L’essenziale della Fisica</h2><p>Un tema leggero intorno ai contenuti.</p></div></section>
<div class="actions"><a class="action" href="articoli.html"><strong>Tutti i capitoli</strong><small>Scegli un argomento</small></a><button class="action" type="button" data-demo-dialog><strong>Mi sento fortunato</strong><small>Apri la finestra di esempio</small></button><a class="action" href="quiz.html"><strong>Quiz</strong><small>Prossimamente</small></a><details class="action lang-action"><summary>Lingua</summary><p>Italiano</p></details></div>
<div class="comparison-grid"><article class="comparison-card"><h2>Una card del catalogo</h2><p>Termologia</p><p>Una descrizione breve: le curve rimangono sul bordo e non attraversano il testo.</p><a href="articoli.html">Esplora i capitoli →</a></article>
<section class="comparison-card"><h2>Una lettura più lunga</h2><p>La superficie di lettura è uniforme e opaca. Il reticolo resta visibile soltanto negli spazi esterni alle card, mentre gli accenti blu accompagnano i comandi.</p><p>Le due curve hanno lo stesso periodo e sono in opposizione di fase: qui sono disegni distinti, non la loro somma. In A hanno la stessa ampiezza; in B la seconda ha un’ampiezza pari al 60% della prima.</p><button class="download" type="button" data-demo-dialog>Apri la finestra</button></section></div>
<dialog class="comparison-dialog" id="demo-dialog"><h2>Una finestra del sito</h2><p>Stesso contenuto, con le varianti di bordo e di tema selezionate.</p><form method="dialog"><button class="download">Chiudi</button></form></dialog>
<noscript><p>I controlli di confronto richiedono JavaScript. Il campione statico mostra A e segue il tema di sistema.</p></noscript>
<script>(()=>{
 for(const [id,key] of [['border-variant','border'],['grid-variant','grid'],['edge-variant','edge']]){
 const control=document.getElementById(id);control.addEventListener('change',()=>{document.documentElement.dataset[key]=control.value;});}
 const dialog=document.getElementById('demo-dialog');document.querySelectorAll('[data-demo-dialog]').forEach(button=>button.addEventListener('click',()=>dialog.showModal()));
})();</script>'''
    return shell('Confronto bordi e reticolo', body, source)
