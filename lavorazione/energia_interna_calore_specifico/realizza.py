"""Realizza il testo approvato nel tema canonico; poi eseguire credits.py --sync.

Non modifica catalogo, manifest o altri articoli. Le immagini scelte restano intatte.
"""
from pathlib import Path
from html import escape
import base64
import hashlib
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
TARGET = ROOT / 'energia_interna_calore_specifico_it.html'
TITLE = 'Energia interna, calore e calore specifico'
COMMONS = 'https://commons.wikimedia.org/wiki/File:'
META = {
    'COP-01': ('copertina-ivy-mike.jpg', 'Ivy_Mike_-_fireball.jpg',
               'Charles Wyckoff; NNSA Nevada Site Office Photo Library, IVY-52-07',
               'Pubblico dominio — PD-USGov-DOE',
               'https://commons.wikimedia.org/wiki/Template:PD-USGov-DOE',
               'Sfera incandescente del test Ivy Mike in una fotografia in bianco e nero'),
    'FIG-01': ('spiaggia-notturna.webp',
               '1008_Beach_at_Night_with_Moon_and_Stars_in_Ko_Li_Pe_-_Tarutao_National_Park,_Satun,_Thailand.jpg',
               'Piith.hant (Piith Hant)', 'CC BY-SA 4.0',
               'https://creativecommons.org/licenses/by-sa/4.0/',
               'Spiaggia sabbiosa con rocce e mare sotto la Luna e le stelle a Ko Li Pe'),
    'FIG-02': ('acqua-movimento-molecolare.gif', 'MD_water.gif', 'Kmckiern',
               'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0/',
               'Modello animato di molecole d’acqua in movimento: ossigeno rosso e idrogeni bianchi'),
}
SECTIONS = ['mare-dopo-il-tramonto', 'energia-che-non-vediamo', 'calore-energia-che-passa',
            'energia-per-un-grado', 'calore-e-temperatura', 'mare-resta-tiepido', 'domande-di-verifica']
STYLE = '''<style data-component="calore-specifico">
.heat-table-scroll{max-width:100%;overflow-x:auto}
.heat-table-scroll:focus-visible{outline:3px solid #080808;outline-offset:4px}
.heat-table{width:100%;min-width:600px;border-collapse:collapse;font-size:16px;line-height:1.6;text-align:left}
.heat-table caption{text-align:left;padding:14px 16px;font-weight:600;background:#c4c4c4;border-bottom:2px solid #080808}
.heat-table th,.heat-table td{padding:12px 14px;border-bottom:1px solid #aaa;vertical-align:top}
.heat-table thead th{border-bottom:2px solid #080808;background:#eee;font-weight:600}
.heat-table th+th,.heat-table td+th,.heat-table td+td{border-left:1px solid #aaa}
.heat-table tbody th{font-weight:500}.heat-table .water-row>*{font-weight:650;background:#eee}
.heat-table .state-start>*{border-top:2px solid #080808}
.heat-table tbody tr:last-child>*{border-bottom:0}
.heat-table td:last-child{white-space:nowrap}
.water-motion .image-frame{max-width:480px;margin:auto}
.water-controls{display:flex;justify-content:center;margin-top:14px}
.water-controls .button{font-family:inherit;cursor:pointer}
</style>'''
MOTION = '''<script data-component="movimento-acqua">
(() => {
 const figure=document.getElementById('fig-02');
 const image=figure.querySelector('img');
 const source=figure.querySelector('source');
 const button=figure.querySelector('[data-water-toggle]');
 const animation=image.getAttribute('src'),still=image.dataset.still;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let playing=!reduced.matches;
 // Il source mantiene il movimento ridotto anche senza JavaScript.
 source.media='not all';
 function sync(){
  image.src=playing?animation:still;
  button.textContent=playing?'Metti in pausa l’animazione':'Riprendi l’animazione';
  button.setAttribute('aria-pressed',String(!playing));
  figure.dataset.playing=String(playing);
 }
 button.disabled=false;
 button.addEventListener('click',()=>{playing=!playing;sync();});
 reduced.addEventListener('change',()=>{playing=!reduced.matches;sync();});
 sync();
})();
</script>'''


def uri(path):
    mime = {'.jpg':'image/jpeg', '.gif':'image/gif', '.png':'image/png', '.svg':'image/svg+xml', '.webp':'image/webp'}[path.suffix]
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()


def fraction(n, d):
    return f'<span class="fraction"><span>{n}</span><span>{d}</span></span>'


def inline_math(tex):
    value = escape(tex).replace(r'\Delta T', 'Δ<i>T</i>').replace(r'\cdot', '·').replace('{,}', ',')
    value = re.sub(r'10\^(\d+)', r'10<sup>\1</sup>', value)
    value = re.sub(r'(?<![\w>])([UCQmc])(?![\w<])', r'<i>\1</i>', value)
    assert '\\' not in value, tex
    return '<span class="inline-math">' + value + '</span>'


def attributes(meta):
    return ' '.join('data-credit-' + k + '="' + escape(v, quote=True) + '"' for k, v in meta.items())


class Renderer:
    def __init__(self):
        self.notes = {}

    def inline(self, source):
        chunks = re.split(r'(\\\(.*?\\\))', source)
        value = ''.join(inline_math(c[2:-2]) if c.startswith(r'\(') else escape(c) for c in chunks)
        value = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', value)
        def note(match):
            key = match[1]
            self.notes[key] = self.notes.get(key, 0) + 1
            suffix = '' if self.notes[key] == 1 else '-' + str(self.notes[key])
            return (f'<sup class="note-ref"><a href="#nota-{key}" id="richiamo-{key}{suffix}" '
                    f'role="doc-noteref" aria-label="Nota {key}">[{key}]</a></sup>')
        return re.sub(r'\[\^(\d+)\]', note, value)

    def figure(self, key, caption):
        name, source, author, license_name, license_url, alt = META[key]
        path = WORK / 'risorse' / name
        width, height = Image.open(path).size
        meta = attributes({'source':COMMONS + source, 'author':author,
                           'license':license_name, 'license-url':license_url,
                           'changes':('Riduzione proporzionale da 5760 × 3840 a 1920 × 1280 px e compressione WebP, qualità 85; nessun ritaglio. Originale conservato.' if key == 'FIG-01' else 'Nessuna modifica ai pixel; visualizzazione proporzionale senza ritaglio.')})
        classes = 'visual cover photo' if key == 'COP-01' else 'visual photo'
        extra = ''
        if key == 'FIG-02':
            classes = 'visual gif water-motion'
            still = WORK / 'risorse/acqua-fotogramma-statico.png'
            Image.open(path).convert('RGB').save(still)
            still_uri = uri(still)
            media = (f'<picture><source media="(prefers-reduced-motion: reduce)" srcset="{still_uri}">'
                     f'<img src="{uri(path)}" data-still="{still_uri}" width="{width}" height="{height}" '
                     f'alt="{escape(alt,quote=True)}" decoding="async"></picture>')
            extra = ('<div class="water-controls"><button type="button" class="button" '
                     'data-water-toggle aria-controls="fig-02" aria-pressed="false" disabled>'
                     'Metti in pausa l’animazione</button></div>')
        else:
            media = f'<img src="{uri(path)}" width="{width}" height="{height}" alt="{escape(alt,quote=True)}" decoding="async">'
        return (f'<figure class="{classes}" id="{key.lower()}" {meta}>'
                '<div class="image-frame"><div class="overview">' + media + '</div></div>' + extra +
                '<figcaption>' + self.inline(caption) + '</figcaption></figure>')

    def table(self, block, caption):
        rows = [[c.strip() for c in line.strip('|').split('|')] for line in block.splitlines()]
        header = '<thead><tr>' + ''.join('<th scope="col">' + self.inline(c) + '</th>' for c in rows[0]) + '</tr></thead>'
        body, previous = [], None
        for row in rows[2:]:
            state = row[0].strip('*')
            classes = ['state-start'] if previous and previous != state else []
            if 'Acqua pura' in row[1]:
                classes.append('water-row')
            body.append('<tr class="' + ' '.join(classes) + '"><td>' + self.inline(row[0]) +
                        '</td><th scope="row">' + self.inline(row[1]) + '</th><td>' + self.inline(row[2]) + '</td></tr>')
            previous = state
        return ('<figure class="visual" id="tab-01"><div class="image-frame">'
                '<div class="heat-table-scroll" tabindex="0" role="region" aria-label="Calori specifici: tabella scorrevole">'
                '<table class="heat-table"><caption>Calore specifico di solidi, liquidi e gas</caption>' + header +
                '<tbody>' + ''.join(body) + '</tbody></table></div></div><figcaption>' + self.inline(caption) + '</figcaption></figure>')

    def graph(self, caption):
        path = WORK / 'risorse/calore-temperatura.svg'
        make_graph(path)
        alt = ('Grafico della temperatura in funzione del calore assorbito: masse di 1 kg di acqua e sabbia quarzosa '
               'partono da 20 gradi Celsius. La retta della sabbia cresce più rapidamente di quella dell’acqua.')
        image = f'<img src="{uri(path)}" alt="{escape(alt,quote=True)}" width="900" height="600" decoding="async"'
        return ('<figure class="visual diagram" id="gra-01" data-credit-id="credit-grafico-calore-temperatura">'
                '<div class="image-frame"><div class="overview">' + image + '></div>'
                '<details class="image-zoom"><summary><span class="zoom-expand">Ingrandisci l’immagine</span>'
                '<span class="zoom-collapse">Rimpicciolisci l’immagine</span></summary>'
                '<div class="zoom-scroll" tabindex="0" role="region" aria-label="Grafico ingrandito, scorrevole">' +
                image + ' style="min-width:900px"></div></details></div><figcaption>' + self.inline(caption) + '</figcaption></figure>')


def make_graph(path):
    # Dati del modello: Q da 0 a 1000 J; m = 1 kg; T_i = 20 °C.
    def x(q): return 115 + 640 * q / 1000
    def y(t): return 425 - 270 * (t - 20) / 1.5
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="900" height="600" role="img" aria-labelledby="titolo descrizione">',
           '<title id="titolo">Stessa energia, temperature diverse</title>',
           '<desc id="descrizione">Previsioni di T = T iniziale + Q diviso massa per calore specifico, non misure. Acqua: c = 4180; sabbia quarzosa: c = 830 joule per chilogrammo e kelvin. Masse uguali di 1 kg, temperatura iniziale 20 gradi Celsius.</desc>',
           '<rect width="900" height="600" fill="white"/>',
           '<g font-family="Lexend,Arial,sans-serif" fill="#080808">',
           '<text x="450" y="45" text-anchor="middle" font-size="26" font-weight="600">Stessa energia, temperature diverse</text>',
           '<text x="450" y="83" text-anchor="middle" font-size="20">Masse uguali: 1 kg · Temperatura iniziale: 20 °C</text>']
    for i in range(6):
        q = i * 200
        svg += [f'<line x1="{x(q)}" y1="155" x2="{x(q)}" y2="425" stroke="#ddd"/>',
                f'<text x="{x(q)}" y="456" text-anchor="middle" font-size="20">{q/1000:.1f}</text>'.replace('.0<', ',0<').replace('.2<', ',2<').replace('.4<', ',4<').replace('.6<', ',6<').replace('.8<', ',8<')]
    for i in range(6):
        t = 20 + .3 * i
        svg += [f'<line x1="115" y1="{y(t):.2f}" x2="755" y2="{y(t):.2f}" stroke="#ddd"/>',
                f'<text x="96" y="{y(t)+7:.2f}" text-anchor="end" font-size="20">{t:.1f}</text>'.replace(f'{t:.1f}</text>', f'{t:.1f}'.replace('.', ',')+'</text>')]
    svg += ['<path d="M115 145V425H770" fill="none" stroke="#080808" stroke-width="3"/>',
            '<text x="435" y="499" text-anchor="middle" font-size="22">Calore assorbito Q (kJ)</text>',
            '<text transform="translate(38 290) rotate(-90)" text-anchor="middle" font-size="22">Temperatura T (°C)</text>']
    for c, color, dash in [(830, '#b58a00', ''), (4180, '#0066cc', '')]:
        svg += [f'<path d="M115 425L755 {y(20+1000/c):.3f}" fill="none" stroke="{color}" stroke-width="4" {dash}/>']
    svg += ['<line x1="165" y1="548" x2="225" y2="548" stroke="#b58a00" stroke-width="4"/>',
            '<text x="240" y="555" font-size="20">Sabbia quarzosa</text>',
            '<line x1="505" y1="548" x2="565" y2="548" stroke="#0066cc" stroke-width="4"/>',
            '<text x="580" y="555" font-size="20">Acqua</text>',
            '<text x="450" y="588" text-anchor="middle" font-size="16">Previsioni del modello, non misure sperimentali</text>', '</g></svg>']
    path.write_text('\n'.join(svg))


def equation(i):
    formulas = [
        ('Calore e capacità termica', '<i>Q</i> = <i>C</i> · Δ<i>T</i>', 'Q uguale C per delta T'),
        ('Variazione di temperatura', 'Δ<i>T</i> = <i>T</i><sub>f</sub> − <i>T</i><sub>i</sub>', 'Delta T uguale temperatura finale meno temperatura iniziale'),
        ('Capacità termica del corpo', '<i>C</i> = <i>m</i> · <i>c</i>', 'C uguale massa per calore specifico'),
        ('Legge fondamentale della calorimetria', '<i>Q</i> = <i>m</i> · <i>c</i> · Δ<i>T</i>', 'Q uguale massa per calore specifico per variazione di temperatura'),
        ('Variazione di temperatura a parità di calore', 'Δ<i>T</i> = ' + fraction('<i>Q</i>', '<i>m</i> · <i>c</i>'), 'Delta T uguale Q diviso il prodotto di massa e calore specifico'),
    ]
    label, formula, description = formulas[i]
    return (f'<div class="equation" id="formula-{i+1}"><div class="equation-label">{label}</div>'
            f'<div class="math" role="math" aria-label="{description}"><span>{formula}</span></div></div>')


def register_sources():
    # Registro unico: anche le fonti informative confluiscono nei crediti comuni.
    path = ROOT / 'risorse/crediti.json'
    registry = json.loads(path.read_text())
    doc = registry['documents'].setdefault(TARGET.name, {'title': TITLE + ' — Materia Oscura',
        'anchor': 'energia-interna-calore-specifico-it', 'credits': [], 'lexend':True, 'review':''})
    # La nuova variante della spiaggia sostituisce l’associazione al vecchio
    # avviso del solo articolo corrente; la scheda e l’originale restano conservati.
    beach_source = COMMONS + META['FIG-01'][1]
    beach_ids = {r['id'] for r in registry['resources'] if r.get('source') == beach_source}
    doc['credits'] = [a for a in doc['credits'] if a['resource'] not in beach_ids]
    sources = [
        ('https://www.engineeringtoolbox.com/specific-heat-capacity-d_391.html', 'Engineering ToolBox',
         'Dati della tabella TAB-01 e del grafico GRA-01',
         'Calori specifici a pressione costante; valori arrotondati. Acqua pura a 20 °C: 4182 J/(kg · K), arrotondata a 4180 nel grafico. Sabbia quarzosa: 830 J/(kg · K), temperatura e umidità non precisate. Consultazione dei dati, senza riproduzione di immagini o testo.'),
        ('https://openstax.org/books/biology-2e/pages/2-2-water', 'OpenStax',
         'Calore specifico dell’acqua e legami a idrogeno', 'Biology 2e, §2.2 — Water. Informazioni rielaborate con formulazioni originali.'),
        ('https://openstax.org/books/college-physics/pages/14-2-temperature-change-and-heat-capacity', 'OpenStax',
         'Verifica di formule e unità della calorimetria', 'College Physics, §14.2 — Temperature Change and Heat Capacity. Consultato per il controllo scientifico; nessun testo o immagine riprodotti.'),
    ]
    def add(resource):
        existing = next((r for r in registry['resources'] if r.get('id') == resource['id']), None)
        if not existing:
            registry['resources'].append(resource)
        association = {'resource': resource['id'], 'notice':0}
        if association not in doc['credits']:
            doc['credits'].append(association)
    for url, author, description, detail in sources:
        add({'id':'credit-' + hashlib.sha256(url.encode()).hexdigest()[:16],
             'description':description, 'source':url, 'author':author, 'license':None,
             'license_url':None, 'changes':None, 'type':'scientific-source', 'status':'documented',
             'links':[{'url':url, 'label':'Fonte scientifica'}],
             'notices':[escape(description) + ' — ' + escape(author) + '. <a href="' + url + '">Fonte scientifica</a>. ' + escape(detail)],
             'metadata_sources':[TARGET.name], 'fingerprints':[]})
    add({'id':'credit-grafico-calore-temperatura', 'description':'Grafico originale T(Q) di acqua e sabbia quarzosa',
         'source':None, 'author':'Materia Oscura', 'license':None, 'license_url':None, 'changes':None,
         'status':'documented', 'links':[], 'metadata_sources':[TARGET.name], 'fingerprints':[],
         'notices':['Grafico GRA-01 — realizzazione originale per Materia Oscura. Previsioni da T = T iniziale + Q/(m · c), con m = 1 kg, T iniziale = 20 °C e i calori specifici della tabella. Dati sperimentali non inventati; la fonte dei valori è accreditata separatamente.']})
    path.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')


def main():
    renderer = Renderer()
    source = (WORK / 'bozza.md').read_text().split('<details>')[0]
    blocks = [b.strip() for b in source.split('\n\n') if b.strip()]
    body, headings, notes = [], [], []
    current = cover = table = None
    count = 0
    for block in blocks:
        if block.startswith(('# ', 'Versione ', 'Bozza testuale')):
            continue
        if re.match(r'\[(?:COP|FIG|TAB|GRA)-', block):
            current = re.match(r'\[([A-Z]+-\d+)', block)[1]
            continue
        if block.startswith('|'):
            table = block
            continue
        if block.startswith('Didascalia:'):
            caption = block.removeprefix('Didascalia:').strip()
            if current == 'TAB-01':
                figure = renderer.table(table, caption)
            elif current == 'GRA-01':
                figure = renderer.graph(caption)
            else:
                figure = renderer.figure(current, caption)
            if current == 'COP-01':
                cover = figure
            else:
                body.append(figure)
            current = None
            continue
        if block.startswith(r'\['):
            body.append(equation(count))
            count += 1
            continue
        if block.startswith('[^'):
            key, text = re.fullmatch(r'\[\^(\d+)\]: (.*)', block).groups()
            notes.append(f'<li id="nota-{key}">{renderer.inline(text)} '
                         f'<a href="#richiamo-{key}" role="doc-backlink" aria-label="Torna al primo richiamo della nota {key}">↩</a></li>')
            continue
        if block.startswith('## '):
            title = block[3:]
            if title == 'Note':
                continue
            sid = SECTIONS[len(headings)]
            headings.append((sid,title))
            body.append('<div class="section-heading">' + f'<span class="section-number" aria-hidden="true">{len(headings):02}</span>' +
                        f'<h2 id="{sid}" data-toc tabindex="-1">{escape(title)}</h2></div>')
            continue
        if block.startswith('1. '):
            items = re.split(r'\n(?=\d+\. )',block)
            body.append('<ol class="questions">' + ''.join('<li>' + renderer.inline(re.sub(r'^\d+\. ','',item)) + '</li>' for item in items) + '</ol>')
            continue
        body.append('<p>' + renderer.inline(block) + '</p>')
    assert cover and count == 5 and len(headings) == 7 and len(notes) == 4
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    template = re.sub(r'<!-- MODELLO CANONICO.*?-->', '<!-- Articolo autonomo dal tema canonico v8; testo approvato. -->',template,count=1,flags=re.S)
    template = template.replace('<title>Tema grafico delle dispense — modello riutilizzabile</title>', '<title>' + TITLE + ' — Materia Oscura</title>')
    template = template.replace('name="version" content="v8"', 'name="version" content="v4"',1)
    template = template.replace('name="date" content="2026-10-18"', 'name="date" content="2026-10-19"',1)
    template = template.replace('Modello autonomo del tema grafico comune a tutti i capitoli futuri.', 'Energia interna, calore, capacità termica e calore specifico: perché il mare resta tiepido di notte.')
    template = template.replace('Nome dell’area tematica','Materia e calore').replace('Titolo dell’articolo',TITLE)
    template = template.replace('<span class="sidebar-label">Fisica</span>','<span class="sidebar-label">Materia e calore</span>')
    sidebar = '<nav class="sidebar-nav" aria-label="Sezioni dell’articolo"><ol>'
    sidebar += ''.join(f'<li class="level-2"><a href="#{sid}"><span class="item-number" aria-hidden="true">{i:02}</span><span>{escape(title)}</span></a></li>' for i,(sid,title) in enumerate(headings,1)) + '</ol></nav>'
    template = re.sub(r'<nav class="sidebar-nav".*?</nav>',lambda _:sidebar,template,count=1,flags=re.S)
    template = re.sub(r'<figure class="visual cover">.*?</figure>',lambda _:cover,template,count=1,flags=re.S)
    template = re.sub(r'(<article class="article">).*?(<nav class="bottom-links")',lambda m:m[1]+'\n'.join(body)+m[2],template,count=1,flags=re.S)
    template = re.sub(r'(<details class="chapter-notes".*?<ol>).*?(</ol>)',lambda m:m[1]+''.join(notes)+m[2],template,count=1,flags=re.S)
    template = template.replace('</head>',STYLE+'</head>',1)
    navigation = ('<nav class="chapter-navigation" aria-label="Navigazione tra articoli">'
                  '<a rel="prev" href="https://rickymusu-bit.github.io/fisica/temperatura_equilibrio_termico_it.html">'
                  '<span>← Articolo precedente</span><small>Temperatura ed equilibrio termico</small></a>'
                  '<a rel="next" href="https://rickymusu-bit.github.io/fisica/stati_della_materia.html">'
                  '<span>Articolo successivo →</span><small>Stati della materia</small></a></nav>')
    template = template.replace('<!-- chapter-navigation:end -->',navigation+'<!-- chapter-navigation:end -->')
    template = template.replace('Versione v8 · 2026-10-18','Versione v4 · 19 ottobre 2026')
    template = template.replace('</body>',MOTION+'</body>')
    TARGET.write_text(template)
    register_sources()
    print(TARGET.name,TARGET.stat().st_size,'byte, prima della sincronizzazione dei crediti')


if __name__ == '__main__':
    main()
