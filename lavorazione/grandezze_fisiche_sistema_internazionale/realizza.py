"""Genera il capitolo dal testo approvato e dal modello Stringhe corrente.

Eseguire dalla radice. Aggiorna soltanto il nuovo capitolo e le sue associazioni
nel registro unico; non cambia manifest, catalogo o sorgenti storici.
"""
from pathlib import Path
from html import escape
import base64
import hashlib
import json
import re
import sys

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
import credits
from media_controls import apply_media_controls
from stringhe_theme import navigation_header

NAME = 'grandezze_fisiche_sistema_internazionale_it.html'
TITLE = 'Le grandezze fisiche e il Sistema internazionale'
AREA = 'Introduzione alla fisica e alla misura'
VERSION = 'v4'
DATE = '2026-10-23'
DATE_LABEL = '23 ottobre 2026'
COMMONS = 'https://commons.wikimedia.org/wiki/File:'
META = {
    'COP-01': ('chilogrammo.jpg', 'International_prototype_of_the_kilogram_aka_Le_Grand_K.jpg',
               'BIPM', 'CC BY-SA 3.0 IGO', 'https://creativecommons.org/licenses/by-sa/3.0/igo/',
               'Prototipo internazionale del chilogrammo sotto campane di vetro'),
    'FIG-01': ('metro.jpg', 'A_pair_of_hands_holding_a_construction_measuring_tape.jpg',
               'Nenad Stojkovic', 'CC BY 2.0', 'https://creativecommons.org/licenses/by/2.0/',
               'Mani che tengono un metro a nastro disteso contro un pannello di legno'),
    'FIG-03': ('campo.jpg', 'Camp_nou_before_F.C._Barcelona_-_Real_Madrid_league_match_of_2012.JPG',
               'Netol', 'CC BY-SA 3.0',
               'https://creativecommons.org/licenses/by-sa/3.0/',
               'Il campo del Camp Nou prima di una partita nel 2012'),
}
SECTIONS = ['misurare', 'riferimento-comune', 'grandezze-di-base', 'unita-derivate', 'domande-di-verifica']
TABLE_STYLE = '''<style data-component="tabelle-si">
.si-table-scroll{max-width:100%;overflow-x:auto;background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:10px}
.si-table-scroll:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.si-table{width:100%;min-width:550px;border-collapse:collapse;font-size:16px;line-height:1.6;text-align:left}
.si-table caption{text-align:left;padding:14px;font-weight:600;background:var(--surface-soft)}
.si-table th,.si-table td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.si-table thead th{background:var(--surface-soft);font-weight:600}
.si-table tbody th{font-weight:500}.si-table tbody tr:last-child>*{border-bottom:0}
.si-table td:last-child{white-space:nowrap}
</style>'''


def data_uri(path):
    mime = 'image/svg+xml' if path.suffix == '.svg' else 'image/jpeg'
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()


def inline(source):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(source))


def figure(key, caption):
    filename, source, author, license_name, license_url, alt = META[key]
    path = WORK / 'risorse' / filename
    diagram = path.suffix == '.svg'
    width, height = (960, 743) if diagram else Image.open(path).size
    uri = data_uri(path)
    changes = ('Annotazioni dei lati e cornice superiore aggiunte alla foto integrale, senza ritaglio; '
               'schema distribuito con la stessa licenza CC BY-SA 3.0. Dimensioni dalla scheda FC Barcelona.'
               if diagram else 'Nessuna modifica alla versione scelta; visualizzazione proporzionale senza ritaglio.')
    attrs = {'source': COMMONS + source, 'author': author, 'license': license_name,
             'license-url': license_url, 'changes': changes}
    metadata = ' '.join(f'data-credit-{k}="{escape(v, quote=True)}"' for k, v in attrs.items())
    classes = 'visual cover photo portrait' if key == 'COP-01' else ('visual diagram' if diagram else 'visual photo')
    img = f'<img src="{uri}" width="{width}" height="{height}" alt="{escape(alt, quote=True)}" decoding="async">'
    zoom = ''
    if diagram:
        zoom = ('<details class="image-zoom"><summary>Ingrandisci l’immagine</summary>'
                '<div class="zoom-scroll" tabindex="0" role="region" aria-label="Schema del campo ingrandito, scorrevole">'
                + img.replace(' decoding=', ' style="min-width:960px" decoding=') + '</div></details>')
    return (f'<figure class="{classes}" id="{key.lower()}" {metadata}><div class="image-frame">'
            '<div class="overview">' + img + '</div>' + zoom + '</div><figcaption>' + inline(caption) + '</figcaption></figure>')


def table(block, key):
    rows = [[c.strip() for c in line.strip('|').split('|')] for line in block.splitlines()]
    caption = 'Le sette grandezze e unità di base del SI' if key == 'TAB-01' else 'Alcune grandezze e unità derivate del SI'
    head = '<thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in rows[0]) + '</tr></thead>'
    body = '<tbody>' + ''.join('<tr><th scope="row">' + inline(row[0]) + '</th>' +
                               ''.join('<td>' + inline(c) + '</td>' for c in row[1:]) + '</tr>' for row in rows[2:]) + '</tbody>'
    return (f'<div class="visual si-table-scroll" id="{key.lower()}" tabindex="0" role="region" '
            f'aria-label="{caption}, con scorrimento orizzontale se necessario">'
            f'<table class="si-table"><caption>{caption}</caption>{head}{body}</table></div>')


def render():
    body, headings, cover = [], [], None
    pending = None
    formula = 0
    text = (WORK / 'bozza.md').read_text().split('\n---\n', 1)[0]
    for block in (b.strip() for b in text.split('\n\n') if b.strip()):
        if block.startswith(('# ', 'Bozza v', '[Servizio')):
            continue
        if re.match(r'\[(COP|FIG|TAB)-\d+', block):
            pending = re.match(r'\[([A-Z]+-\d+)', block)[1]
            continue
        if block.startswith('*Didascalia proposta:*'):
            rendered = figure(pending, block.split(':* ', 1)[1])
            if pending == 'COP-01':
                cover = rendered
            else:
                body.append(rendered)
            pending = None
            continue
        if block.startswith('|'):
            body.append(table(block, pending)); pending = None
            continue
        if block.startswith('## '):
            title = block[3:]; sid = SECTIONS[len(headings)]
            headings.append((sid, title))
            body.append(f'<div class="section-heading"><span class="section-number" aria-hidden="true">{len(headings):02}</span>'
                        f'<h2 id="{sid}" data-toc tabindex="-1">{escape(title)}</h2></div>')
            continue
        if block.startswith(r'\['):
            values = [
                ('Il prodotto delle unità', '<span>m · m = m<sup>2</sup></span>', 'Metro per metro uguale metro quadrato'),
                ('L’area del terreno di gioco', '<span><i>A</i> = 105 m · 68 m</span><span>= 7140 m<sup>2</sup></span>',
                 'Area uguale 105 metri per 68 metri uguale 7140 metri quadrati'),
            ]
            label, equation, alt = values[formula]; formula += 1
            body.append(f'<div class="equation"><div class="equation-label">{label}</div><div class="math" role="math" aria-label="{alt}">{equation}</div></div>')
            continue
        if re.match(r'1\. ', block):
            items = re.split(r'\n(?=\d+\. )', block)
            body.append('<ol class="questions">' + ''.join('<li>' + inline(re.sub(r'^\d+\. ', '', item)) + '</li>' for item in items) + '</ol>')
            continue
        body.append('<p>' + inline(block) + '</p>')
    assert cover and len(headings) == 5 and formula == 2 and pending is None
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    doc = credits.Document(template)
    edits = []
    for node in doc.root.descendants():
        if node.tag == 'title':
            edits.append((node.start, node.end, '<title>' + TITLE + ' — Stringhe</title>'))
        elif node.tag == 'meta' and node.attrs.get('name') in {'version', 'date', 'description'}:
            value = {'version': VERSION, 'date': DATE, 'description': 'Grandezze fisiche, misura, sette unità di base del SI e unità derivate.'}[node.attrs['name']]
            edits.append((node.start, node.end, f'<meta name="{node.attrs["name"]}" content="{value}">'))
        elif node.tag == 'figure' and node.has_class('cover'):
            edits.append((node.start, node.end, cover))
        elif node.tag == 'article' and node.has_class('article'):
            bottom = next(n for n in node.descendants('nav') if n.has_class('bottom-links'))
            edits.append((node.start, node.end, '<article class="article">' + '\n'.join(body) + doc.html(bottom) + '</article>'))
        elif node.tag == 'details' and node.has_class('chapter-notes'):
            edits.append((node.start, node.end, ''))
        elif node.tag == 'header' and node.has_class('topbar'):
            index = next(n for n in node.descendants('details') if n.has_class('reader-index'))
            index_markup = doc.html(index).replace('Titolo del capitolo', TITLE).replace('<span class="sidebar-label">Fisica</span>', f'<span class="sidebar-label">{AREA}</span>')
            sidebar = '<nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>' + ''.join(
                f'<li class="level-2"><a href="#{sid}"><span class="item-number" aria-hidden="true">{i:02}</span><span>{escape(title)}</span></a></li>'
                for i, (sid, title) in enumerate(headings, 1)) + '</ol></nav>'
            index_markup = re.sub(r'<nav class="sidebar-nav"[\s\S]*?</nav>', lambda _: sidebar, index_markup)
            edits.append((node.start, node.end, navigation_header('chapter', NAME, index_markup)))
        elif node.tag == 'footer' and node.has_class('footer'):
            edits.append((node.start, node.end, f'<footer class="footer">Versione {VERSION} — {DATE_LABEL}</footer>'))
    for start, end, replacement in sorted(edits, reverse=True):
        template = template[:start] + replacement + template[end:]
    template = template.replace('Nome dell’area tematica', AREA).replace('Titolo del capitolo', TITLE)
    template = re.sub(r'<!-- MODELLO CANONICO[\s\S]*?-->', '<!-- Capitolo autonomo dal modello canonico Stringhe v22. -->', template, count=1)
    template = template.replace('</head>', TABLE_STYLE + '</head>', 1)
    navigation = ('<nav class="chapter-navigation" aria-label="Navigazione tra capitoli">'
                  '<a rel="prev" href="metodo_scientifico_it.html" data-site-path="metodo_scientifico_it.html">'
                  '<span>← Capitolo precedente</span><small>Il metodo scientifico</small></a>'
                  '<a rel="next" href="termodinamica_sistemi_it.html" data-site-path="termodinamica_sistemi_it.html">'
                  '<span>Capitolo successivo →</span><small>La termodinamica e i sistemi termodinamici</small></a></nav>')
    template = template.replace('<!-- chapter-navigation:end -->', navigation + '<!-- chapter-navigation:end -->', 1)
    return apply_media_controls(template)


def add_reference(registry, source, title, author):
    identity = 'credit-' + hashlib.sha256(source.encode()).hexdigest()[:16]
    if not any(r['id'] == identity for r in registry['resources']):
        registry['resources'].append({'id': identity, 'description': title, 'source': source, 'author': author,
                                     'license': None, 'license_url': None, 'changes': 'Fonte dei dati e delle spiegazioni; nessuna riproduzione del documento.',
                                     'status': 'reference', 'links': [],
                                     'notices': [escape(title) + ' — ' + escape(author) + '. <a href="' + escape(source, quote=True) + '">Fonte scientifica</a>. Riferimento per dati e spiegazioni; nessuna immagine riprodotta.'],
                                     'metadata_sources': [NAME], 'fingerprints': []})
    association = {'resource': identity, 'notice': 0}
    if association not in registry['documents'][NAME]['credits']:
        registry['documents'][NAME]['credits'].append(association)


def main():
    target = ROOT / NAME
    target.write_text(render(), encoding='utf-8')
    registry = credits.load_registry()
    field_resource = None
    field_notice = None
    for resource in registry['resources']:
        if resource.get('source') == COMMONS + META['FIG-03'][1]:
            field_resource = resource
            resource['description'] = META['FIG-03'][5]
            resource['author'] = 'Netol'
            resource['changes'] = 'Nessuna modifica alla versione scelta; visualizzazione proporzionale senza ritaglio.'
            field_notice = (escape(resource['description']) + ' — Netol. '
                            '<a href="' + escape(resource['source'], quote=True) + '">Fonte originale</a>. '
                            '<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>. '
                            'Modifiche: ' + resource['changes'])
            if field_notice not in resource['notices']:
                resource['notices'].append(field_notice)
    credits.sync_inventory(registry)
    if field_resource:
        for association in registry['documents'][NAME]['credits']:
            if association['resource'] == field_resource['id']:
                association['notice'] = field_resource['notices'].index(field_notice)
    registry['documents'][NAME]['title'] = TITLE
    registry['documents'][NAME]['review'] = 'Testo, immagini e revisione della didascalia approvati; pubblicazione esplicitamente autorizzata. Licenze e fonti documentate.'
    add_reference(registry, 'https://www.bipm.org/en/publications/si-brochure',
                  'The International System of Units, 9th edition, e sintesi aggiornata nel 2026', 'Bureau International des Poids et Mesures')
    add_reference(registry, 'https://www.fcbarcelona.com/en/club/facilities/spotify-camp-nou',
                  'Scheda del Camp Nou: terreno di gioco di 105 m per 68 m', 'FC Barcelona')
    add_reference(registry, 'https://www.nist.gov/si-redefinition/kilogram-introduction',
                  'Kilogram: Introduction, storia del prototipo internazionale e credito fotografico BIPM', 'National Institute of Standards and Technology')
    # Aggiornamento circoscritto: gli snapshot degli altri capitoli restano intatti.
    target.write_text(credits.update_component(target.read_text(), registry, NAME), encoding='utf-8')
    credits.REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'crediti.html').write_text(credits.render_page(registry), encoding='utf-8')
    (WORK / 'bozza.html').write_bytes(target.read_bytes())
    credits.validate(registry)
    print(NAME, target.stat().st_size, 'byte; crediti verificati; manifest gestito separatamente')


if __name__ == '__main__':
    main()
