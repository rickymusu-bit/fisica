"""Realizza il capitolo 5 approvato usando il modello Stringhe v23.

Genera l'anteprima autonoma; non modifica l'ammissione alla pubblicazione.
"""
from pathlib import Path
from html import escape
import base64
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
import credits
from stringhe_theme import navigation_header

NAME = 'cifre_significative_it.html'
TITLE = 'Le cifre significative'
AREA = 'Introduzione alla fisica e alla misura'
IDS = ['zero-misura', 'contare', 'arrotondare', 'calcoli', 'esempio', 'conversioni', 'domande-di-verifica']
CAPTIONS = {'TAB-01':'Leggere gli zeri nella scrittura di una misura',
            'TAB-02':'Arrotondare senza perdere la posizione della virgola',
            'TAB-03':'Due operazioni, due criteri diversi'}
EXTRA = '''<style data-component="cifre-significative">
.significant-scroll{max-width:100%;overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink)}
.significant-scroll:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.significant-table{width:100%;min-width:540px;border-collapse:collapse;text-align:left;font-size:16px;line-height:1.6}
.significant-table caption{padding:14px;text-align:left;font-weight:600;background:var(--surface-soft)}
.significant-table th,.significant-table td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.significant-table thead th{background:var(--surface-soft)}.significant-table tbody th{font-weight:500;white-space:nowrap}
.significant-table tr:last-child>*{border-bottom:0}
.significant-math{max-width:100%;overflow-x:auto}.significant-math .math-step{flex:0 0 auto;max-width:100%;overflow-x:auto}
.significant-math math{font-family:Lexend,Arial,sans-serif;font-size:1em}
.significant-procedure{padding-left:30px}.significant-procedure li{margin-bottom:18px}
</style>'''

def basic_mathml(source):
    """Sottoinsieme LaTeX della bozza convertito in MathML nativo, senza rete."""
    source = source.strip().replace('{,}', ',').replace('−', '-')
    if source.startswith(r'\boxed{') and source.endswith('}'):
        source = source[7:-1].strip()
    pos = 0

    def group():
        nonlocal pos
        while pos < len(source) and source[pos].isspace():
            pos += 1
        if pos >= len(source):
            raise ValueError('Gruppo matematico mancante')
        if source[pos] == '{':
            pos += 1
            result = parse(True)
            return '<mrow>' + result + '</mrow>'
        value = source[pos]
        pos += 1
        return '<mn>' + escape(value) + '</mn>' if value.isdigit() else '<mi>' + escape(value) + '</mi>'

    def parse(closing=False):
        nonlocal pos
        out = []
        while pos < len(source):
            c = source[pos]
            if c == '}' and closing:
                pos += 1
                return ''.join(out)
            if c.isspace():
                pos += 1
            elif c == '{':
                out.append(group())
            elif c in '^_':
                pos += 1
                assert out, 'Esponente/pedice senza base'
                value = group()
                base = out.pop()
                tag = 'msup' if c == '^' else 'msub'
                out.append(f'<{tag}>' + base + value + f'</{tag}>')
            elif c == '\\':
                if source.startswith(r'\frac', pos):
                    pos += 5
                    num, den = group(), group()
                    out.append('<mfrac>' + num + den + '</mfrac>')
                elif source.startswith(r'\mathrm', pos):
                    pos += 7
                    out.append(group().replace('<mi>', '<mi mathvariant="normal">'))
                elif source.startswith(r'\cdot', pos):
                    pos += 5
                    out.append('<mo>·</mo>')
                elif source.startswith(r'\mu', pos):
                    pos += 3
                    out.append('<mi mathvariant="normal">µ</mi>')
                elif pos + 1 < len(source) and source[pos+1] in ', ':
                    pos += 2
                    out.append('<mspace width="0.2em"/>')
                else:
                    raise ValueError('Comando non gestito: ' + source[pos:pos+24])
            elif c.isdigit():
                match = re.match(r'\d+(?:,\d+)?', source[pos:])
                out.append('<mn>' + match[0] + '</mn>')
                pos += len(match[0])
            elif c.isalpha():
                match = re.match(r'[A-Za-z]+', source[pos:])
                if not match:
                    out.append('<mi>' + escape(c) + '</mi>'); pos += 1
                else:
                    out.append('<mi>' + match[0] + '</mi>'); pos += len(match[0])
            else:
                out.append('<mo>' + escape('−' if c == '-' else c) + '</mo>')
                pos += 1
        assert not closing, 'Gruppo matematico non chiuso'
        return ''.join(out)
    result = parse()
    return '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>' + result + '</mrow></math>'




def mathml(source):
    source = source.replace(r'\approx', '≈').replace(r'\quad', ' ')
    match = re.search(r'\s*\\text\{([^{}]*)\}\s*$', source)
    suffix = ''
    if match:
        suffix = '<mspace width="0.8em"/><mtext>' + escape(match[1]) + '</mtext>'
        source = source[:match.start()]
    result = basic_mathml(source)
    return result.replace('</mrow></math>', suffix + '</mrow></math>') if suffix else result


def inline(source):
    source = escape(source)
    source = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', source)
    source = re.sub(r'\[([123])\]', lambda m:'<sup class="note-ref"><a href="#nota-' + m[1] + '" id="richiamo-' + m[1] + '" role="doc-noteref" aria-label="Nota ' + m[1] + '">[' + m[1] + ']</a></sup>', source)
    return source


def equation(block):
    source = block.removeprefix(r'\[').removesuffix(r'\]').strip()
    depth, parts, start = 0, [], 0
    for pos, char in enumerate(source):
        if char == '{': depth += 1
        elif char == '}': depth -= 1
        elif char in '=≈' and depth == 0:
            if pos > start: parts.append(source[start:pos].strip())
            start = pos
    parts.append(source[start:].strip())
    return '<div class="equation"><div class="math significant-math" role="math">' + ''.join('<span class="math-step">' + mathml(part) + '</span>' for part in parts) + '</div></div>'


def diagram(template, key, caption):
    doc = credits.Document(template)
    model = next(n for n in doc.root.descendants('template') if n.attrs.get('id') == 'modello-schema-ingrandibile')
    figure = next(model.descendants('figure'))
    result = doc.html(figure)
    name, alt, minimum, identity = {
        'FIG-01':('confronto-cifre.svg','12,4 centimetri: tre C.S., fino ai decimi. 12,40 centimetri: quattro C.S., fino ai centesimi.',620,'confronto-cifre-significative'),
        'FIG-02':('schema-cassa.svg','Cassa a base rettangolare, con quote sui due lati adiacenti della base: a = 2,34 m; b = 1,2 m. Illustrazione generata con quote dei due lati adiacenti della base.',1100,'cassa-cifre-generata')
    }[key]
    uri = 'data:image/svg+xml;base64,' + base64.b64encode((WORK / 'risorse' / name).read_bytes()).decode()
    if key in {'FIG-01', 'FIG-02'}:
        parsed = credits.Document(result)
        zoom = next(n for n in parsed.root.descendants('details') if n.has_class('image-zoom'))
        result = result[:zoom.start] + result[zoom.end:]
    return (result.replace('<figure class="visual diagram">','<figure class="visual diagram" id="' + key.lower() + '" data-credit-id="' + identity + '">')
            .replace('src=""','src="' + uri + '"').replace('[Descrizione dell’immagine]',alt)
            .replace('[Didascalia]',inline(caption)).replace('min-width:900px','min-width:' + str(minimum) + 'px'))


def table(block, key, caption):
    rows = [[cell.strip() for cell in row.strip('|').split('|')] for row in block.splitlines()]
    head = '<thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in rows[0]) + '</tr></thead>'
    body = '<tbody>' + ''.join('<tr>' + ''.join(('<th scope="row">' if i==0 else '<td>') + inline(cell) + ('</th>' if i==0 else '</td>') for i,cell in enumerate(row)) + '</tr>' for row in rows[2:]) + '</tbody>'
    return '<figure class="visual" id="' + key.lower() + '"><div class="significant-scroll" tabindex="0" role="region" aria-label="' + CAPTIONS[key] + ', tabella scorrevole"><table class="significant-table"><caption>' + CAPTIONS[key] + '</caption>' + head + body + '</table></div><figcaption>' + inline(caption) + '</figcaption></figure>'


def resources():
    # FIG-01 conserva la composizione SVG numerica del sorgente storico.
    source = (ROOT / 'sistema_internazionale_notazione_it.html').read_text()
    section = source[source.index('<section id="cifre-significative"'):]
    doc = credits.Document(section)
    figure = next(n for n in doc.root.descendants('figure') if n.has_class('sig-reading'))
    svg = doc.html(next(figure.descendants('svg'))).replace('viewbox=', 'viewBox=').replace('cifre significative', 'C.S.')
    (WORK / 'risorse/confronto-cifre.svg').write_text(svg)
    image = 'data:image/png;base64,' + base64.b64encode((WORK / 'risorse/cassa-generata.png').read_bytes()).decode()
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 620" role="img" aria-labelledby="titolo descrizione">
<title id="titolo">Cassa: lunghezze dei lati della base</title><desc id="descrizione">Quote su due spigoli adiacenti della base: a = 2,34 m e b = 1,2 m.</desc>
<defs><marker id="freccia" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto-start-reverse"><path d="M0 0 8 4 0 8" fill="none" stroke="#155e75" stroke-width="1.4"/></marker></defs>
<rect width="1100" height="620" fill="#fff"/>
<image x="70" y="70" width="887" height="443.5" href="''' + image + '''"/>
<g fill="none" stroke="#155e75" stroke-width="2.5"><path d="M87 346V430M780 507V590M780 507 865 549M940 376 1023 417"/>
<path d="M87 414 780 575" marker-start="url(#freccia)" marker-end="url(#freccia)"/>
<path d="M850 542 1010 411" marker-start="url(#freccia)" marker-end="url(#freccia)"/></g>
<g font-family="Arial,sans-serif" font-size="34" fill="#183047" text-anchor="middle"><text x="410" y="558">a = 2,34 m</text><text x="970" y="555">b = 1,2 m</text></g>
</svg>'''
    (WORK / 'risorse/schema-cassa.svg').write_text(svg)


def render():
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    markdown = (WORK / 'bozza.md').read_text().split('\n---\n', 1)[0]
    main, notes = markdown.split('\n## Note\n',1)
    blocks = [b.strip() for b in main.split('\n\n') if b.strip()]
    body, headings, pending, visual = [], [], None, None
    formulas = 0
    for block in blocks:
        if block.startswith(('# ', 'Versione v', '[COP-')): continue
        if block.startswith(('[FIG-', '[TAB-')):
            visual = re.match(r'\[((?:FIG|TAB)-\d+)',block)[1]; continue
        if block.startswith('|'): pending = block; continue
        if block.startswith('Didascalia: '):
            caption = block[len('Didascalia: '):]
            if visual:
                body.append(table(pending,visual,caption) if visual.startswith('TAB-') else diagram(template,visual,caption))
                visual = pending = None
            continue
        if block.startswith('## '):
            title = block[3:];sid = IDS[len([h for h in headings if h[2]==2])]
            number = len([h for h in headings if h[2]==2])+1
            headings.append((sid,title,2))
            body.append('<div class="section-heading"><span class="section-number" aria-hidden="true">' + str(number).zfill(2) + '</span><h2 id="' + sid + '" data-toc tabindex="-1">' + inline(title) + '</h2></div>');continue
        if block.startswith('### '):
            sid='esempio-' + str(sum(h[2]==3 for h in headings)+1);headings.append((sid,block[4:],3))
            body.append('<h3 id="' + sid + '" data-toc tabindex="-1">' + inline(block[4:]) + '</h3>');continue
        if block.startswith(r'\['):
            body.append(equation(block));formulas+=1;continue
        if re.match(r'1\. ',block):
            cls = 'questions' if headings[-1][0]=='domande-di-verifica' else 'significant-procedure'
            body.append('<ol class="' + cls + '">' + ''.join('<li>' + inline(re.sub(r'^\d+\. ','',item)) + '</li>' for item in re.split(r'\n(?=\d+\. )',block)) + '</ol>');continue
        body.append('<p>' + inline(block) + '</p>')
    assert len([h for h in headings if h[2]==2])==7 and visual is None and pending is None
    note_items=[]
    for block in notes.strip().split('\n\n'):
        number,text=re.match(r'\[(\d)\] (.*)',block, re.S).groups()
        note_items.append('<li id="nota-' + number + '">' + escape(text) + ' <a href="#richiamo-' + number + '" role="doc-backlink" aria-label="Torna al richiamo della nota ' + number + '">↩</a></li>')
    notes_html='<details class="chapter-notes" aria-labelledby="titolo-note"><summary id="titolo-note">Note</summary><div role="doc-endnotes" aria-labelledby="titolo-note"><ol>' + ''.join(note_items) + '</ol></div></details>'
    meta=json.loads((WORK/'risorse/copertina-fonte.json').read_text())
    attrs={'source':meta['source'],'author':meta['author'],'license':meta['license'],'license-url':meta['license_url'],'changes':meta['changes']}
    metadata=' '.join('data-credit-' + k + '="' + escape(v,quote=True) + '"' for k,v in attrs.items())
    uri='data:image/jpeg;base64,'+base64.b64encode((WORK/'risorse/copertina-egizia.jpg').read_bytes()).decode()
    cover='<figure class="visual cover photo" id="cop-01" ' + metadata + '><div class="image-frame"><div class="overview"><img src="' + uri + '" width="960" height="540" alt="Strumento di misura egizio con suddivisioni e iscrizioni incise lungo l’asta." decoding="async"></div></div><figcaption>Strumento di misura egizio con suddivisioni incise lungo l’asta.</figcaption></figure>'
    doc=credits.Document(template);edits=[]
    for node in doc.root.descendants():
        if node.tag=='title':edits.append((node.start,node.end,'<title>' + TITLE + ' — Stringhe</title>'))
        elif node.tag=='meta' and node.attrs.get('name') in {'version','date','description'}:
            val={'version':'v4','date':'2026-10-23','description':'Cifre significative, zeri, arrotondamento e regole nei calcoli con misure, con esempi e procedure.'}[node.attrs['name']]
            edits.append((node.start,node.end,'<meta name="' + node.attrs['name'] + '" content="' + val + '">'))
        elif node.tag=='figure' and node.has_class('cover'):edits.append((node.start,node.end,cover))
        elif node.tag=='article' and node.has_class('article'):
            bottom=next(n for n in node.descendants('nav') if n.has_class('bottom-links'))
            edits.append((node.start,node.end,'<article class="article">' + '\n'.join(body) + doc.html(bottom) + '</article>'))
        elif node.tag=='details' and node.has_class('chapter-notes'):edits.append((node.start,node.end,notes_html))
        elif node.tag=='header' and node.has_class('topbar'):
            index=next(n for n in node.descendants('details') if n.has_class('reader-index'))
            markup=doc.html(index).replace('Titolo del capitolo',TITLE).replace('<span class="sidebar-label">Fisica</span>','<span class="sidebar-label">' + AREA + '</span>')
            nav='<nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>'+''.join('<li class="level-' + str(level) + '"><a href="#' + sid + '"><span>' + escape(title) + '</span></a></li>' for sid,title,level in headings)+'</ol></nav>'
            markup=re.sub(r'<nav class="sidebar-nav"[\s\S]*?</nav>',lambda _:nav,markup)
            edits.append((node.start,node.end,navigation_header('chapter',NAME,markup)))
        elif node.tag=='footer' and node.has_class('footer'):edits.append((node.start,node.end,'<footer class="footer">Versione v4 — 23 ottobre 2026</footer>'))
    for start,end,value in sorted(edits,reverse=True):template=template[:start]+value+template[end:]
    template=template.replace('Nome dell’area tematica',AREA).replace('Titolo del capitolo',TITLE)
    template=re.sub(r'<!-- MODELLO CANONICO[\s\S]*?-->','<!-- Capitolo 5, testo approvato e modello Stringhe v23; cassa generata su richiesta. -->',template,count=1)
    template=template.replace('</head>',EXTRA+'</head>',1)
    prev='<nav class="chapter-navigation" aria-label="Navigazione tra capitoli"><a rel="prev" href="prefissi_sistema_internazionale_it.html" data-site-path="prefissi_sistema_internazionale_it.html"><span>← Capitolo precedente</span><small>I prefissi del Sistema internazionale</small></a><a rel="next" href="termodinamica_sistemi_it.html" data-site-path="termodinamica_sistemi_it.html"><span>Capitolo successivo →</span><small>La termodinamica e i sistemi termodinamici</small></a></nav>'
    template=template.replace('<!-- chapter-navigation:end -->',prev+'<!-- chapter-navigation:end -->',1)
    return template,formulas


def main():
    resources()
    source,formulas=render()
    target=ROOT/NAME;target.write_text(source)
    registry=credits.load_registry()
    registry['documents'][NAME]={'title':TITLE,'anchor':NAME[:-5].replace('_','-'),'credits':[],'lexend':True,'chapter_labels':True,'review':None}
    for identity,description,notice in [
        ('confronto-cifre-significative','Confronto numerico fra 12,4 cm e 12,40 cm','Confronto numerico delle scritture: schema SVG del progetto, riutilizzato dal sorgente storico. Nessuna immagine esterna riprodotta.'),
        ('cassa-cifre-generata','Cassa con quote dei lati della base','Illustrazione della cassa generata con ChatGPT su richiesta esplicita dell’utente; quote e schema SVG realizzati per Stringhe. Nessuna fotografia di misure reali o immagine di terzi riprodotta.')]:
        if not any(r['id']==identity for r in registry['resources']):
            registry['resources'].append({'id':identity,'description':description,'source':None,'author':None,'license':None,'license_url':None,'changes':notice,'status':'documented','links':[],'notices':[notice],'metadata_sources':[NAME],'fingerprints':[]})
    cassa = next(r for r in registry['resources'] if r['id']=='cassa-cifre-generata')
    cassa['notices'] = [notice.replace(' Dati illustrativi, disegno non in scala.', '') for notice in cassa['notices']]
    cassa['changes'] = cassa['changes'].replace(' Dati illustrativi, disegno non in scala.', '')
    credits.sync_inventory(registry)
    target.write_text(credits.update_component(source,registry,NAME))
    (WORK/'bozza.html').write_bytes(target.read_bytes())
    credits.REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    if NAME in json.loads((ROOT/'pubblicazione.json').read_text())['articoli']:
        (ROOT/'crediti.html').write_text(credits.render_page(registry))
    else:
        assert (ROOT/'crediti.html').read_text()==credits.render_page(registry)
    print(NAME,target.stat().st_size,'byte;',formulas,'formule; crediti incorporati aggiornati')


if __name__=='__main__':main()
