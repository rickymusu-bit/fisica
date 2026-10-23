"""Genera l'anteprima autonoma dal testo v3; nessun cambio di pubblicazione.

Copertina scelta dall'utente, incorporata senza ritagli.
Usa tema e crediti canonici, conserva gli altri inventari e HTML.
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

NAME = 'prefissi_sistema_internazionale_it.html'
TITLE = 'I prefissi del Sistema internazionale'
AREA = 'Introduzione alla fisica e alla misura'
VERSION = 'v3'
TABLES = {'TAB-01': 'Prefissi SI: multipli e sottomultipli',
          'TAB-02': 'La stessa lunghezza in due scritture',
          'TAB-03A': 'Equivalenze della massa',
          'TAB-03B': 'Fattori per lunghezza, area e volume'}
IDS = ['lunghezza', 'prefissi', 'conversione', 'massa-potenze', 'esempi', 'domande-di-verifica']
EXTRA = '''<style data-component="conversioni-prefissi">
.conversion-scroll{max-width:100%;overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink)}
.conversion-scroll:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.conversion-table{width:100%;min-width:500px;border-collapse:collapse;text-align:left;font-size:16px;line-height:1.6}
.conversion-table caption{padding:14px;text-align:left;font-weight:600;background:var(--surface-soft)}
.conversion-table th,.conversion-table td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.conversion-table thead th{background:var(--surface-soft)}.conversion-table tbody th{font-weight:500}
.conversion-table tr:last-child>*{border-bottom:0}
#tab-01 tr>:nth-child(4){border-left:2px solid var(--muted)}
.conversion-table td{white-space:nowrap}
.conversion-math{overflow-x:auto;max-width:100%}
.conversion-math .math-step{flex:0 0 auto;max-width:100%;overflow-x:auto}
.conversion-math math{font-family:Lexend,Arial,sans-serif;font-size:1em}
.conversion-procedure{padding-left:30px}.conversion-procedure li{margin-bottom:18px}
.cover-pending{padding:28px;text-align:center;color:var(--muted);font-size:17px}
.cover-pending p{margin:0}
</style>'''


def mathml(source):
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
                    out.append('<mstyle mathvariant="normal">' + group() + '</mstyle>')
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


def inline(s):
    pieces = re.split(r'(\\\([\s\S]*?\\\))', s)
    output = []
    for piece in pieces:
        if piece.startswith(r'\('):
            output.append(mathml(piece[2:-2]))
        else:
            value = escape(piece)
            value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
            # Pedici dei valori numerici nella spiegazione dei simboli.
            value = value.replace('x_partenza', '<i>x</i><sub>partenza</sub>').replace('x_arrivo', '<i>x</i><sub>arrivo</sub>')
            output.append(value)
    return ''.join(output)


def equation(block):
    source = block.strip().removeprefix(r'\[').removesuffix(r'\]').strip()
    boxed = source.startswith(r'\boxed{')
    if boxed:
        source = source[7:-1].strip()
    # Una catena di uguaglianze può andare a capo senza spezzare una frazione.
    depth, parts, start = 0, [], 0
    for pos, c in enumerate(source):
        if c == '{': depth += 1
        elif c == '}': depth -= 1
        elif c == '=' and depth == 0:
            parts.append(source[start:pos].strip())
            start = pos
    parts.append(source[start:].strip())
    label = ('<div class="equation-label">' + ('Conversione tra prefissi' if 'n(p-q)' not in source else 'Conversione di unità elevate a potenza') + '</div>') if boxed else ''
    return '<div class="equation">' + label + '<div class="math conversion-math" role="math">' + ''.join('<span class="math-step">' + mathml(p) + '</span>' for p in parts) + '</div></div>'


def table(block, key, caption):
    rows = [[c.strip() for c in line.strip('|').split('|')] for line in block.splitlines()]
    head = '<thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in rows[0]) + '</tr></thead>'
    body = '<tbody>' + ''.join('<tr><th scope="row">' + inline(row[0]) + '</th>' + ''.join('<td>' + inline(c) + '</td>' for c in row[1:]) + '</tr>' for row in rows[2:]) + '</tbody>'
    title = TABLES[key]
    return '<figure class="visual" id="' + key.lower() + '"><div class="conversion-scroll" tabindex="0" role="region" aria-label="' + title + ', tabella scorrevole"><table class="conversion-table"><caption>' + title + '</caption>' + head + body + '</table></div><figcaption>' + inline(caption) + '</figcaption></figure>'


def diagram(template, caption):
    doc = credits.Document(template)
    model = next(n for n in doc.root.descendants('template') if n.attrs.get('id') == 'modello-schema-ingrandibile')
    fig = next(model.descendants('figure'))
    result = doc.html(fig)
    raw = (WORK / 'risorse/schema-conversioni.svg').read_bytes()
    uri = 'data:image/svg+xml;base64,' + base64.b64encode(raw).decode()
    result = result.replace('<figure class="visual diagram">', '<figure class="visual diagram" id="sch-01" data-credit-id="schema-conversioni-prefissi">')
    result = result.replace('src=""', 'src="' + uri + '"')
    result = result.replace('[Descrizione dell’immagine]', 'Conversioni km–m–mm e cm–mm–µm: fattori in potenze di dieci e frecce nei due versi.')
    result = result.replace('[Didascalia]', inline(caption)).replace('min-width:900px', 'min-width:960px')
    return result


def conversion_path(key):
    paths = {
        'CONV-01': ('2,4 MPa', '10⁶⁻³ = 10³', 'kPa'),
        'CONV-02': ('250 cm²', '(10⁻²)² = 10⁻⁴', 'm²'),
        'CONV-03': ('4,5 mm³', '(10⁻¹)³ = 10⁻³', 'cm³'),
        'CONV-04': ('1,2 g/cm³', '10⁻³ al numeratore, 10⁻⁶ al denominatore', 'kg/m³')}
    datum, factor, target = paths[key]
    factor_html = inline(factor).replace(', 10⁻⁶ al denominatore', '<br>10⁻⁶ al denominatore')
    return '<figure class="visual conversion-path" id="' + key.lower() + '"><div class="conversion-scroll" tabindex="0" role="region" aria-label="Impostazione della conversione, tabella scorrevole"><table class="conversion-table"><caption>Dati e passaggi della conversione</caption><thead><tr><th scope="col">Dato</th><th scope="col">Fattore</th><th scope="col">Unità di arrivo</th></tr></thead><tbody><tr><th scope="row">' + inline(datum) + '</th><td>' + factor_html + '</td><td>' + inline(target) + '</td></tr></tbody></table></div></figure>'


def render():
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    markdown = (WORK / 'bozza.md').read_text().split('\n---\n', 1)[0]
    markdown = re.sub(r'<!--[\s\S]*?-->', '', markdown)
    blocks = [b.strip() for b in markdown.split('\n\n') if b.strip()]
    body, headings, table_key, pending, formulas = [], [], None, None, 0
    for block in blocks:
        if block.startswith('# '): continue
        if block.startswith('[COP-'): continue
        if block.startswith('[TAB-'):
            table_key = re.match(r'\[(TAB-\d+[A-Z]?)', block)[1]; continue
        if block.startswith('[SCH-'): continue
        if block.startswith('[CONV-'):
            body.append(conversion_path(re.match(r'\[(CONV-\d+)', block)[1])); continue
        if block.startswith('|'):
            pending = block; continue
        if block.startswith('Didascalia: '):
            caption = block[len('Didascalia: '):]
            if caption.startswith(('Colonia di batteri e funghi', 'Alghe e batteri osservati')):
                continue
            if table_key:
                body.append(table(pending, table_key, caption)); pending = table_key = None
            else:
                body.append(diagram(template, caption))
            continue
        if block.startswith('!['): continue
        if block.startswith('## '):
            title = block[3:]; sid = IDS[len(headings)]
            headings.append((sid, title))
            body.append('<div class="section-heading"><span class="section-number" aria-hidden="true">' + str(len(headings)).zfill(2) + '</span><h2 id="' + sid + '" data-toc tabindex="-1">' + inline(title) + '</h2></div>'); continue
        if block.startswith('### '):
            title = block[4:]
            sid = 'procedura' if title == 'Procedura' else 'esempio-' + str(sum('id="esempio-' in p for p in body) + 1)
            body.append('<h3 id="' + sid + '">' + inline(title) + '</h3>'); continue
        if block.startswith(r'\['):
            formulas += 1; body.append(equation(block)); continue
        if re.match(r'1\. ', block):
            items = re.split(r'\n(?=\d+\. )', block)
            cls = 'questions' if headings[-1][0] == 'domande-di-verifica' else 'conversion-procedure'
            body.append('<ol class="' + cls + '">' + ''.join('<li>' + inline(re.sub(r'^\d+\. ', '', item)) + '</li>' for item in items) + '</ol>'); continue
        body.append('<p>' + inline(block) + '</p>')
    assert len(headings) == 6 and pending is None and table_key is None
    assert formulas == 18, formulas
    meta = json.loads((WORK / 'risorse/copertina-fonte.json').read_text())
    uri = 'data:image/jpeg;base64,' + base64.b64encode((WORK / 'risorse' / meta['file']).read_bytes()).decode()
    attrs = {'source':meta['source'],'author':meta['author'],'license':meta['license'],'license-url':meta['license_url'],'changes':meta['changes']}
    metadata = ' '.join('data-credit-' + k + '="' + escape(v,quote=True) + '"' for k,v in attrs.items())
    cover = '<figure class="visual cover photo" id="cop-01" ' + metadata + '><div class="image-frame"><div class="overview"><img src="' + uri + '" alt="Alghe e batteri osservati al microscopio elettronico a scansione; in basso è visibile la barra di scala di 5 µm." width="960" height="768" decoding="async"></div></div><figcaption>Alghe e batteri osservati al microscopio elettronico a scansione. La barra di scala indica 5 µm.</figcaption></figure>'
    doc = credits.Document(template)
    edits = []
    for node in doc.root.descendants():
        if node.tag == 'title': edits.append((node.start, node.end, '<title>' + TITLE + ' — Stringhe</title>'))
        elif node.tag == 'meta' and node.attrs.get('name') in {'version','date','description'}:
            value = {'version': VERSION,'date':'2026-10-23','description':'Prefissi SI, formula e procedura di conversione, esempi con pressione, area, volume e densità.'}[node.attrs['name']]
            edits.append((node.start,node.end,'<meta name="' + node.attrs['name'] + '" content="' + value + '">'))
        elif node.tag == 'figure' and node.has_class('cover'):
            edits.append((node.start,node.end,cover))
        elif node.tag == 'article' and node.has_class('article'):
            bottom = next(n for n in node.descendants('nav') if n.has_class('bottom-links'))
            edits.append((node.start,node.end,'<article class="article">' + '\n'.join(body) + doc.html(bottom) + '</article>'))
        elif node.tag == 'details' and node.has_class('chapter-notes'):
            edits.append((node.start,node.end,''))
        elif node.tag == 'header' and node.has_class('topbar'):
            index = next(n for n in node.descendants('details') if n.has_class('reader-index'))
            markup = doc.html(index).replace('Titolo del capitolo',TITLE).replace('<span class="sidebar-label">Fisica</span>','<span class="sidebar-label">' + AREA + '</span>')
            nav = '<nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>' + ''.join('<li class="level-2"><a href="#' + sid + '"><span class="item-number" aria-hidden="true">' + str(i).zfill(2) + '</span><span>' + escape(title) + '</span></a></li>' for i,(sid,title) in enumerate(headings,1)) + '</ol></nav>'
            markup = re.sub(r'<nav class="sidebar-nav"[\s\S]*?</nav>',lambda _:nav,markup)
            edits.append((node.start,node.end,navigation_header('chapter',NAME,markup)))
        elif node.tag == 'footer' and node.has_class('footer'):
            edits.append((node.start,node.end,'<footer class="footer">Versione ' + VERSION + ' — 23 ottobre 2026</footer>'))
    for start,end,value in sorted(edits,reverse=True):
        template = template[:start] + value + template[end:]
    template = template.replace('Nome dell’area tematica',AREA).replace('Titolo del capitolo',TITLE)
    template = re.sub(r'<!-- MODELLO CANONICO[\s\S]*?-->', '<!-- Anteprima del capitolo 4 dal testo v3 e dal modello Stringhe v23; copertina scelta dall’utente nella bozza v4. -->',template,count=1)
    template = template.replace('</head>',EXTRA + '</head>',1)
    prev = '<nav class="chapter-navigation" aria-label="Navigazione tra capitoli"><a rel="prev" href="potenze_dieci_notazione_scientifica_it.html" data-site-path="potenze_dieci_notazione_scientifica_it.html"><span>← Capitolo precedente</span><small>Le potenze di dieci e la notazione scientifica</small></a><a rel="next" href="termodinamica_sistemi_it.html" data-site-path="termodinamica_sistemi_it.html"><span>Capitolo successivo →</span><small>La termodinamica e i sistemi termodinamici</small></a></nav>'
    template = template.replace('<!-- chapter-navigation:end -->',prev + '<!-- chapter-navigation:end -->',1)
    return template


def register(registry, source):
    registry['documents'][NAME] = {'title':TITLE,'anchor':NAME[:-5].replace('_','-'),'credits':[],'lexend':True,'chapter_labels':True,
        'review':None}
    identity = 'schema-conversioni-prefissi'
    if not any(r['id'] == identity for r in registry['resources']):
        registry['resources'].append({'id':identity,'description':'Schema numerico delle conversioni tra prefissi','source':None,'author':None,'license':None,'license_url':None,
          'changes':'Schema SVG originale realizzato per il progetto su richiesta; nessuna immagine esterna riprodotta.','status':'documented','links':[],
          'notices':['Schema numerico delle conversioni tra prefissi: elaborazione originale per Stringhe realizzata con ChatGPT; nessuna immagine esterna riprodotta.'],
          'metadata_sources':[NAME],'fingerprints':[]})
    for title,url in [('BIPM, SI prefixes','https://www.bipm.org/en/measurement-units/si-prefixes'),('BIPM, SI Brochure, sezioni 3 e 5','https://www.bipm.org/en/publications/si-brochure')]:
        resource = next((r for r in registry['resources'] if r.get('source') == url and r.get('status') == 'reference'),None)
        if not resource:
            resource = {'id':'credit-' + hashlib.sha256(url.encode()).hexdigest()[:16],'description':title,'source':url,'author':'BIPM','license':None,'license_url':None,
             'changes':'Fonte delle convenzioni SI; nessuna immagine riprodotta.','status':'reference','links':[],
             'notices':[escape(title) + '. <a href="' + url + '">Fonte delle convenzioni e dei prefissi</a>. Nessuna immagine riprodotta.'],
             'metadata_sources':[NAME],'fingerprints':[]}
            registry['resources'].append(resource)
        association = {'resource':resource['id'],'notice':0}
        if association not in registry['documents'][NAME]['credits']:
            registry['documents'][NAME]['credits'].append(association)
    credits.sync_inventory(registry)
    return registry


def main():
    source = render()
    target = ROOT / NAME
    target.write_text(source)
    registry = register(credits.load_registry(), source)
    target.write_text(credits.update_component(source,registry,NAME))
    (WORK / 'bozza.html').write_bytes(target.read_bytes())
    credits.REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2) + '\n')
    # Il capitolo non ammesso non modifica la pagina pubblica dei crediti.
    if NAME in json.loads((ROOT / 'pubblicazione.json').read_text())['articoli']:
        (ROOT / 'crediti.html').write_text(credits.render_page(registry))
    else:
        assert (ROOT / 'crediti.html').read_text() == credits.render_page(registry)
    assert credits.component(registry,NAME) in target.read_text()
    print(NAME,target.stat().st_size,'byte; crediti incorporati aggiornati')


if __name__ == '__main__':
    main()
