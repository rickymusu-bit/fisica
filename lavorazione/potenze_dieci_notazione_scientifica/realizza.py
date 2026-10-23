"""Realizza l'anteprima dal testo approvato, senza modificare il manifest.

Il registro viene esteso soltanto con il nuovo documento; gli altri inventari
e le associazioni esistenti rimangono identici. Nessuna pubblicazione.
"""
from pathlib import Path
from html import escape
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
import credits
from stringhe_theme import navigation_header
from media_controls import apply_media_controls

NAME = 'potenze_dieci_notazione_scientifica_it.html'
TITLE = 'Le potenze di dieci e la notazione scientifica'
AREA = 'Introduzione alla fisica e alla misura'
IDS = ['scale', 'potenze', 'notazione', 'confronti', 'calcoli', 'domande-di-verifica']
TABLES = {'TAB-02': 'Le potenze di dieci', 'TAB-03': 'Scritture equivalenti della stessa lunghezza',
          'TAB-01L': 'Ordini di grandezza delle lunghezze'}
EXTRA = '''<style data-component="tabelle-notazione">
.notation-scroll{max-width:100%;overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink)}
.notation-scroll:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.notation-table{width:100%;min-width:500px;border-collapse:collapse;text-align:left;font-size:16px;line-height:1.6}
.notation-table caption{padding:14px;text-align:left;font-weight:600;background:var(--surface-soft)}
.notation-table th,.notation-table td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.notation-table thead th{background:var(--surface-soft)}.notation-table tbody th{font-weight:500}
.notation-table tr:last-child>*{border-bottom:0}.notation-table td:last-child{white-space:nowrap}
.video-thumb{position:relative;display:block;max-width:100%;overflow:hidden;border:1px solid var(--line);border-radius:10px;background:#000}
.video-thumb img{display:block;width:100%;max-width:100%;height:auto}
.video-thumb .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:64px;height:48px;border-radius:12px;background:rgb(0 0 0 / .8)}
.video-thumb .play:after{content:'';position:absolute;left:27px;top:14px;border-left:17px solid white;border-top:10px solid transparent;border-bottom:10px solid transparent}
.video-thumb:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.notation-equation .math{overflow-x:auto;max-width:100%;white-space:nowrap;text-align:center;padding:8px 4px}
.notation-equation .fraction{display:inline-flex;flex-direction:column;text-align:center;vertical-align:middle;line-height:1.35;margin:0 .15em}
.notation-equation .fraction>span:first-child{border-bottom:1px solid currentColor;padding:0 .2em}
.notation-equation .fraction>span:last-child{padding:0 .2em}
</style>'''

def inline(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(s))
    return re.sub(r'\[\^(\d+)\]', lambda m: '<sup class="note-ref"><a href="#nota-' + m[1] +
                  '" id="richiamo-' + m[1] + '" role="doc-noteref" aria-label="Nota ' + m[1] + '">[' + m[1] + ']</a></sup>', s)

def math_html(s):
    """Sottoinsieme tipografico usato nelle undici formule approvate."""
    s = s.strip().removeprefix(r'\[').removesuffix(r'\]').strip()
    def group(pos):
        if s[pos] != '{':
            return escape(s[pos]), pos + 1
        content, pos = parse(pos + 1, True)
        return content, pos
    def parse(pos, closing=False):
        out = []
        while pos < len(s):
            ch = s[pos]
            if ch == '}' and closing:
                return ''.join(out), pos + 1
            if s.startswith(r'\frac', pos):
                num, pos = group(pos + 5); den, pos = group(pos)
                out.append('<span class="fraction"><span>' + num + '</span><span>' + den + '</span></span>')
            elif s.startswith(r'\mathrm', pos):
                value, pos = group(pos + 7); out.append('<span>' + value + '</span>')
            elif s.startswith(r'\cdot', pos):
                out.append(' · '); pos += 5
            elif s.startswith((r'\,', r'\ '), pos):
                out.append('&#8239;'); pos += 2
            elif ch == '^':
                value, pos = group(pos + 1); out.append('<sup>' + value + '</sup>')
            elif ch == '{':
                value, pos = group(pos); out.append(value)
            else:
                out.append(escape(ch)); pos += 1
        return ''.join(out), pos
    return parse(0)[0]

def original_media():
    source = credits.Document((ROOT / 'sistema_internazionale_notazione_it.html').read_text())
    images = list(source.root.descendants('img'))
    result = {'COP-01': next(n for n in images if 'Terra sorge' in n.attrs.get('alt', ''))}
    for key, video_id in [('VID-01', '0fKBhvDjuy0'), ('VID-02', 'oSCX78-8-q0')]:
        link = next(n for n in source.root.descendants('a') if video_id in n.attrs.get('href', ''))
        result[key] = next(link.descendants('img'))
    return result

def figure(key, caption, media):
    src = media[key].attrs['src']
    alt = media[key].attrs.get('alt', '')
    img = f'<img src="{src}" alt="{escape(alt, quote=True)}" decoding="async">'
    if key == 'COP-01':
        content = '<div class="image-frame"><div class="overview">' + img + '</div></div>'
        cls = 'visual cover photo'
    else:
        vid = '0fKBhvDjuy0' if key == 'VID-01' else 'oSCX78-8-q0'
        label = 'Powers of Ten' if key == 'VID-01' else 'A Boy and His Atom'
        content = ('<a class="video-thumb" href="https://www.youtube.com/watch?v=' + vid +
                   '" target="_blank" rel="noopener" aria-label="Apri su YouTube: ' + label + '">' + img +
                   '<span class="play" aria-hidden="true"></span></a>')
        cls = 'visual video'
    return f'<figure class="{cls}" id="{key.lower()}">{content}<figcaption>{inline(caption)}</figcaption></figure>'

def table(block, key, caption):
    rows = [[c.strip() for c in line.strip('|').split('|')] for line in block.splitlines()]
    head = '<thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in rows[0]) + '</tr></thead>'
    body = '<tbody>' + ''.join('<tr><th scope="row">' + inline(row[0]) + '</th>' +
                              ''.join('<td>' + inline(c) + '</td>' for c in row[1:]) + '</tr>' for row in rows[2:]) + '</tbody>'
    return ('<figure class="visual" id="' + key.lower() + '"><div class="notation-scroll" tabindex="0" role="region" aria-label="' +
            TABLES[key] + ', scorrevole"><table class="notation-table"><caption>' + TABLES[key] + '</caption>' + head + body +
            '</table></div><figcaption>' + inline(caption) + '</figcaption></figure>')

def render():
    markdown = (WORK / 'bozza.md').read_text().split('\n---\n', 1)[0]
    markdown = re.sub(r'<!--[\s\S]*?-->', '', markdown)
    blocks = [b.strip() for b in markdown.split('\n\n') if b.strip()]
    body, headings, notes = [], [], []
    media = original_media()
    cover = None
    key = None
    pending_table = None
    formulas = 0
    for block in blocks:
        if block.startswith('# '):
            continue
        if re.match(r'\[(?:COP|VID|TAB)-', block):
            key = re.match(r'\[([A-Z]+-\d+[A-Z]?)', block)[1]; continue
        if block.startswith('|'):
            pending_table = block; continue
        if block.startswith('Didascalia: '):
            caption = block[len('Didascalia: '):]
            if key.startswith('TAB'):
                body.append(table(pending_table, key, caption)); pending_table = None
            else:
                rendered = figure(key, caption, media)
                if key == 'COP-01': cover = rendered
                else: body.append(rendered)
            key = None; continue
        if block == '## Note':
            continue
        if block.startswith('[^'):
            match = re.match(r'\[\^(\d+)\]:\s*([\s\S]*)', block)
            notes.append('<li id="nota-' + match[1] + '">' + inline(match[2]) +
                         ' <a href="#richiamo-' + match[1] + '" role="doc-backlink" aria-label="Torna al richiamo della nota ' + match[1] + '">↩</a></li>')
            continue
        if block.startswith('## '):
            title = block[3:]; sid = IDS[len(headings)]; headings.append((sid, title))
            body.append(f'<div class="section-heading"><span class="section-number" aria-hidden="true">{len(headings):02}</span>' +
                        f'<h2 id="{sid}" data-toc tabindex="-1">{escape(title)}</h2></div>'); continue
        if block.startswith(r'\['):
            formulas += 1
            body.append('<div class="equation notation-equation"><div class="math" role="math">' + math_html(block) + '</div></div>'); continue
        if re.match(r'1\. ', block):
            items = re.split(r'\n(?=\d+\. )', block)
            body.append('<ol class="questions">' + ''.join('<li>' + inline(re.sub(r'^\d+\. ', '', item)) + '</li>' for item in items) + '</ol>'); continue
        body.append('<p>' + inline(block) + '</p>')
    assert cover and len(headings) == 6 and len(notes) == 2 and formulas == 11 and key is None
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    doc = credits.Document(template); edits = []
    for node in doc.root.descendants():
        if node.tag == 'title':
            edits.append((node.start, node.end, '<title>' + TITLE + ' — Stringhe</title>'))
        elif node.tag == 'meta' and node.attrs.get('name') in {'version', 'date', 'description'}:
            value = {'version':'v1', 'date':'2026-10-23', 'description':'Potenze di dieci, notazione scientifica, confronto fra lunghezze e operazioni con gli esponenti.'}[node.attrs['name']]
            edits.append((node.start, node.end, '<meta name="' + node.attrs['name'] + '" content="' + value + '">'))
        elif node.tag == 'figure' and node.has_class('cover'):
            edits.append((node.start, node.end, cover))
        elif node.tag == 'article' and node.has_class('article'):
            bottom = next(n for n in node.descendants('nav') if n.has_class('bottom-links'))
            edits.append((node.start, node.end, '<article class="article">' + '\n'.join(body) + doc.html(bottom) + '</article>'))
        elif node.tag == 'details' and node.has_class('chapter-notes'):
            original = doc.html(node)
            replacement = re.sub(r'<ol>[\s\S]*?</ol>', lambda _: '<ol>' + ''.join(notes) + '</ol>', original)
            edits.append((node.start, node.end, replacement))
        elif node.tag == 'header' and node.has_class('topbar'):
            index = next(n for n in node.descendants('details') if n.has_class('reader-index'))
            index_markup = doc.html(index).replace('Titolo del capitolo', TITLE).replace('<span class="sidebar-label">Fisica</span>', '<span class="sidebar-label">' + AREA + '</span>')
            nav = '<nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>' + ''.join(
                f'<li class="level-2"><a href="#{sid}"><span class="item-number" aria-hidden="true">{i:02}</span><span>{escape(title)}</span></a></li>' for i,(sid,title) in enumerate(headings,1)) + '</ol></nav>'
            index_markup = re.sub(r'<nav class="sidebar-nav"[\s\S]*?</nav>', lambda _: nav, index_markup)
            edits.append((node.start,node.end,navigation_header('chapter',NAME,index_markup)))
        elif node.tag == 'footer' and node.has_class('footer'):
            edits.append((node.start,node.end,'<footer class="footer">Versione v1 — 23 ottobre 2026</footer>'))
    for start,end,value in sorted(edits,reverse=True):
        template = template[:start] + value + template[end:]
    template = template.replace('Nome dell’area tematica',AREA).replace('Titolo del capitolo',TITLE)
    template = re.sub(r'<!-- MODELLO CANONICO[\s\S]*?-->', '<!-- Anteprima dal testo v2 approvato e dal modello canonico Stringhe v22. -->', template,count=1)
    template = template.replace('</head>',EXTRA + '</head>',1)
    prev = ('<nav class="chapter-navigation" aria-label="Navigazione tra capitoli"><a rel="prev" href="grandezze_fisiche_sistema_internazionale_it.html" data-site-path="grandezze_fisiche_sistema_internazionale_it.html">'
            '<span>← Capitolo precedente</span><small>Le grandezze fisiche e il Sistema internazionale</small></a></nav>')
    template = template.replace('<!-- chapter-navigation:end -->',prev + '<!-- chapter-navigation:end -->',1)
    # Non vi sono GIF o nuovi zoom: i comandi canonici sono già nel modello.
    return template

def register_document(registry, html):
    # Riusa inventario e schede esistenti, senza sincronizzare altri documenti.
    registry['documents'][NAME] = {'title':TITLE,'anchor':NAME[:-5].replace('_','-'),'credits':[],
        'lexend':True,'chapter_labels':True,'review':'Anteprima: copertina e miniature ereditate con attribuzioni/licenze da verificare prima della pubblicazione.'}
    resources = {r['id']:r for r in registry['resources']}
    fingerprints = {fp:r['id'] for r in registry['resources'] for fp in r.get('fingerprints',[])}
    assets = {a['id']:a for a in registry['assets']}
    for asset in assets.values():
        asset['uses'] = [u for u in asset['uses'] if u['document'] != NAME]
    for occurrence in credits.inventory(html):
        identity = occurrence.pop('id'); occurrence.pop('metadata',None)
        occurrence['credit_id'] = occurrence.get('credit_id') or fingerprints.get(identity)
        asset = assets.setdefault(identity, {'id':identity,'kind':occurrence['kind'],'uses':[]})
        asset['uses'].append({'document':NAME,**occurrence})
        if occurrence['credit_id'] and occurrence['credit_id'] != 'font-lexend':
            association={'resource':occurrence['credit_id'],'notice':0}
            if association not in registry['documents'][NAME]['credits']:
                registry['documents'][NAME]['credits'].append(association)
    registry['assets'] = sorted((a for a in assets.values() if a['uses']),key=lambda a:a['id'])
    # Le fonti scientifiche correnti sono tutte nella sezione di servizio approvata.
    service=(WORK/'bozza.md').read_text().split('## Servizio editoriale',1)[1]
    for title,url in re.findall(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',service):
        if 'youtube.com' in url: continue
        existing=next((r for r in registry['resources'] if r.get('source')==url and r.get('status')=='reference'),None)
        identity=existing['id'] if existing else 'credit-'+hashlib.sha256(url.encode()).hexdigest()[:16]
        if not existing:
            resource={'id':identity,'description':title,'source':url,'author':None,'license':None,'license_url':None,
                'changes':'Fonte di dati e spiegazioni; nessuna immagine riprodotta.','status':'reference','links':[],
                'notices':[escape(title)+'. <a href="'+escape(url,quote=True)+'">Fonte dei dati e delle spiegazioni</a>. Nessuna immagine riprodotta.'],
                'metadata_sources':[NAME],'fingerprints':[]}
            if identity not in resources: registry['resources'].append(resource); resources[identity]=resource
        association={'resource':identity,'notice':0}
        if association not in registry['documents'][NAME]['credits']: registry['documents'][NAME]['credits'].append(association)
    return registry

def main():
    html=render(); target=ROOT/NAME; target.write_text(html)
    registry=register_document(credits.load_registry(),html)
    # Inventario completo con le funzioni canoniche; nessuno snapshot estraneo riscritto.
    credits.sync_inventory(registry)
    target.write_text(credits.update_component(html,registry,NAME))
    (WORK/'bozza.html').write_bytes(target.read_bytes())
    credits.REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    # La pagina pubblica resta identica: il capitolo non è nel manifest.
    assert (ROOT/'crediti.html').read_text() == credits.render_page(registry)
    assert credits.component(registry,NAME) in target.read_text()
    print(NAME,target.stat().st_size,'byte; snapshot crediti verificato')

if __name__ == '__main__': main()
