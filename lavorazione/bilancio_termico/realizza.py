"""Realizza la bozza approvata nel tema canonico, con il grafico richiesto.

Eseguire poi scripts/credits.py --sync e copia della versione verificata in bozza.html.
Non modifica catalogo, manifest o altri articoli.
"""
from pathlib import Path
from html import escape
import base64
import hashlib
import json
import math
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
TARGET = ROOT / 'bilancio_termico_it.html'
TITLE = 'Il bilancio termico'
COMMONS = 'https://commons.wikimedia.org/wiki/File:'
META = {
    'COP-01': ('copertina-boucher.jpg', COMMONS + 'Fran%C3%A7ois_Boucher_002.jpg',
        'François Boucher; Musée du Louvre, RF 926; The Yorck Project (2002), DIRECTMEDIA',
        'Pubblico dominio — PD-Art, Public Domain Mark 1.0',
        'https://creativecommons.org/publicdomain/mark/1.0/',
        'Le Déjeuner (1739): adulti e bambini attorno a una tavola con tazze e recipienti'),
    'FIG-01': ('caffe.jpg', COMMONS + 'A_small_cup_of_coffee.JPG',
        'Julius Schorzman', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0/',
        'Tazza bianca con caffè nero, piattino e cucchiaino'),
    'FIG-02': ('latte.jpg', COMMONS + 'Glass_of_Milk_(33657535532).jpg',
        'NIAID', 'CC BY 2.0', 'https://creativecommons.org/licenses/by/2.0/',
        'Bicchiere trasparente parzialmente pieno di latte su fondo blu'),
    'FIG-03': ('versamento-rawpixel.jpg', 'https://negativespace.co/pouring-milk-coffee/',
        'Burst (attribuzione sulla fonte NegativeSpace); versione distribuita da Rawpixel',
        'CC0 1.0', 'https://creativecommons.org/publicdomain/zero/1.0/',
        'Una mano versa latte da una lattiera nera nel caffè, su un piano di legno'),
    'FIG-04': ('tazza-black-velvet.jpg', COMMONS + "Hostess_Tableware_%27Black_Velvet%27_coffee_cup_-_2022-08-30_-_Andy_Mabbett_-_03.jpg",
        'Andy Mabbett (Pigsonthewing)', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0/',
        'Tazza vuota e piattino bianchi con decorazioni nere e marroni, modello Hostess Tableware Black Velvet'),
}
SECTIONS = ['quanto-si-raffredda-il-caffe', 'energia-che-esce-e-che-entra',
            'temperatura-e-masse', 'anche-la-tazza-partecipa', 'domande-di-verifica']


def uri(path):
    mime = 'image/svg+xml' if path.suffix == '.svg' else 'image/jpeg'
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()


def sym(letter, sub=None):
    return '<i>' + letter + '</i>' + ('<sub>' + escape(sub) + '</sub>' if sub else '')


def math_markup(tex):
    subs = []
    def sub(match):
        subs.append(sym(match[1], match[2]))
        return '@' + str(len(subs) - 1) + '@'
    value = re.sub(r'([QTCmc])_\{\\mathrm\{([^{}]+)\}\}', sub, tex)
    value = escape(value).replace(r'\cdot', '·').replace(r'\Delta', 'Δ')
    value = re.sub(r'\b([QTCmc])\b', r'<i>\1</i>', value)
    for i, fragment in enumerate(subs):
        value = value.replace('@' + str(i) + '@', fragment)
    assert '\\' not in value, tex
    return value


class Renderer:
    def __init__(self):
        self.notes = {}
        self.figures = {}

    def inline(self, source):
        chunks = re.split(r'(\\\(.*?\\\))', source)
        value = ''.join('<span class="inline-math">' + math_markup(c[2:-2]) + '</span>'
                        if c.startswith(r'\(') else escape(c) for c in chunks)
        value = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', value)
        def note(match):
            key = match[1]
            self.notes[key] = self.notes.get(key, 0) + 1
            suffix = '' if self.notes[key] == 1 else '-' + str(self.notes[key])
            return (f'<sup class="note-ref"><a href="#nota-{key}" id="richiamo-{key}{suffix}" '
                    f'role="doc-noteref" aria-label="Nota {key}">[{key}]</a></sup>')
        return re.sub(r'\[\^(\d+)\]', note, value)

    def figure(self, key, caption):
        self.figures[key] = self.figures.get(key, 0) + 1
        suffix = '' if self.figures[key] == 1 else '-tazza'
        name, source, author, license_name, license_url, alt = META[key]
        path = WORK / 'risorse' / name
        width, height = Image.open(path).size
        meta = {'source': source, 'author': author, 'license': license_name,
                'license-url': license_url, 'changes': 'Nessuna modifica; versione scelta incorporata integralmente.'}
        attrs = ' '.join('data-credit-' + k + '="' + escape(v, quote=True) + '"' for k, v in meta.items())
        classes = 'visual cover photo' if key == 'COP-01' else 'visual photo'
        caption_html = self.inline(caption)
        return (f'<figure class="{classes}" id="{key.lower()}{suffix}" {attrs}>'
                '<div class="image-frame"><div class="overview">'
                f'<img src="{uri(path)}" width="{width}" height="{height}" '
                f'alt="{escape(alt, quote=True)}" decoding="async"></div></div>'
                '<figcaption>' + caption_html + '</figcaption></figure>')

    def graph(self, caption):
        path = WORK / 'risorse/temperatura-tempo.svg'
        make_graph(path)
        alt = ('Temperature previste per 100 g di caffè inizialmente a 80 °C e 50 g di latte a 20 °C. '
               'La curva marrone scuro continua scende da 80 verso 60 °C; la curva beige marrone chiaro continua sale '
               'da 20 verso 60 °C. Tempo da 0 a 300 secondi, ipotizzato e non misurato.')
        media = f'<img src="{uri(path)}" width="960" height="690" alt="{escape(alt, quote=True)}" decoding="async"'
        return ('<figure class="visual diagram" id="gra-02" data-credit-id="credit-bilancio-temperatura-tempo">'
                '<div class="image-frame"><div class="overview">' + media + '></div>'
                '<details class="image-zoom"><summary><span class="zoom-expand">Ingrandisci l’immagine</span>'
                '<span class="zoom-collapse">Rimpicciolisci l’immagine</span></summary>'
                '<div class="zoom-scroll" tabindex="0" role="region" aria-label="Grafico ingrandito, scorrevole">' +
                media + ' style="min-width:960px"></div></details></div><figcaption>' +
                self.inline(caption) + '</figcaption></figure>')


def temperatures(t):
    # Due capacità termiche costanti, flusso proporzionale alla differenza di T.
    # Tau = 60 s è un'ipotesi illustrativa. T_eq è imposto dal bilancio.
    decay = math.exp(-t / 60)
    return 60 + 20 * decay, 60 - 40 * decay


def make_graph(path):
    theme = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    font = re.search(r'@font-face\{[^}]+\}', theme)[0]
    x = lambda t: 110 + 730 * t / 300
    y = lambda temp: 495 - 340 * (temp - 10) / 80
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="690" viewBox="0 0 960 690" role="img" aria-labelledby="title desc">',
        '<title id="title">Caffè e latte verso l’equilibrio termico</title>',
        '<desc id="desc">Curve illustrative del modello, non misure. Caffè 100 g a 80 °C; latte 50 g a 20 °C. Calori specifici uguali; tazza e ambiente trascurati. Equilibrio 60 °C; tempo caratteristico ipotizzato 60 secondi.</desc>',
        '<style>' + font + '</style>', '<rect width="960" height="690" fill="white"/>',
        '<g font-family="Lexend,Arial,sans-serif" fill="#080808">',
        '<text x="480" y="42" text-anchor="middle" font-size="27" font-weight="600">Caffè e latte verso l’equilibrio</text>',
        '<text x="480" y="79" text-anchor="middle" font-size="20">Caffè: 100 g a 80 °C; Latte: 50 g a 20 °C</text>',
        '<text x="480" y="112" text-anchor="middle" font-size="18">Stesso calore specifico; tazza e ambiente trascurati</text>']
    for temp in range(10, 91, 10):
        parts += [f'<line x1="110" y1="{y(temp):.2f}" x2="840" y2="{y(temp):.2f}" stroke="#ddd"/>',
                  f'<text x="92" y="{y(temp)+7:.2f}" text-anchor="end" font-size="20">{temp}</text>']
    for t in range(0, 301, 60):
        parts += [f'<line x1="{x(t):.2f}" y1="155" x2="{x(t):.2f}" y2="495" stroke="#ddd"/>',
                  f'<text x="{x(t):.2f}" y="528" text-anchor="middle" font-size="20">{t}</text>']
    parts += ['<path d="M110 145V495H855" fill="none" stroke="#080808" stroke-width="3"/>',
              '<text x="480" y="568" text-anchor="middle" font-size="23">Tempo t (s)</text>',
              '<text transform="translate(35 325) rotate(-90)" text-anchor="middle" font-size="23">Temperatura T (°C)</text>',
              f'<path d="M110 {y(60):.2f}H840" stroke="#555" stroke-width="2" stroke-dasharray="3 5"/>',
              '<text x="130" y="187" font-size="18">Caffè</text>',
              '<text x="130" y="478" font-size="18">Latte</text>',
              '<rect x="650" y="244" width="206" height="27" fill="white"/>',
              '<text x="650" y="264" font-size="18">Equilibrio: 60 °C</text>']
    for index, color, dash in [(0, '#4b2e1e', ''), (1, '#af8961', '')]:
        points = ' '.join(('M' if t == 0 else 'L') + f'{x(t):.2f},{y(temperatures(t)[index]):.2f}' for t in range(301))
        parts.append(f'<path d="{points}" fill="none" stroke="{color}" stroke-width="4" {dash}/>')
        parts.append(f'<circle cx="110" cy="{y(temperatures(0)[index]):.2f}" r="5" fill="{color}"/>')
    parts += ['<path d="M180 608H245" stroke="#4b2e1e" stroke-width="4"/>',
              '<text x="262" y="615" font-size="21">Caffè</text>',
              '<path d="M535 608H600" stroke="#af8961" stroke-width="4"/>',
              '<text x="617" y="615" font-size="21">Latte</text>',
              '<text x="480" y="658" text-anchor="middle" font-size="17">Curve di modello. Tempi ipotizzati, non misurati</text>',
              '</g></svg>']
    path.write_text('\n'.join(parts))


def equation(index):
    qc, ql, qt = [sym('Q', s) for s in ['caffè', 'latte', 'tazza']]
    mc, ml = sym('m', 'caffè'), sym('m', 'latte')
    te, tc, tl, tt = [sym('T', s) for s in ['eq', 'caffè', 'latte', 'tazza']]
    dc, dl = '(' + te + ' − ' + tc + ')', '(' + te + ' − ' + tl + ')'
    formulae = [
        ('Bilancio termico delle due bevande', [qc, '+', ql, '= 0'], 'Calore del caffè più calore del latte uguale zero'),
        ('Calore scambiato dal caffè', [qc + ' =', mc + ' · ' + sym('c') + ' ·', dc], 'Calore del caffè uguale massa del caffè per calore specifico per temperatura finale meno iniziale'),
        ('Calore scambiato dal latte', [ql + ' =', ml + ' · ' + sym('c') + ' ·', dl], 'Calore del latte uguale massa del latte per calore specifico per temperatura finale meno iniziale'),
        ('Bilancio con il calore specifico comune semplificato', [mc + ' · ' + dc, '+', ml + ' · ' + dl, '= 0'], 'Massa del caffè per la sua variazione di temperatura più massa del latte per la sua variazione uguale zero'),
        ('Temperatura finale di equilibrio', [te + ' =', '<span class="fraction"><span>' + mc + ' · ' + tc + ' +<wbr> ' + ml + ' · ' + tl + '</span><span>' + mc + ' + ' + ml + '</span></span>'], 'Temperatura di equilibrio uguale somma dei prodotti di ciascuna massa per la rispettiva temperatura iniziale, divisa per la somma delle masse'),
        ('Calore scambiato dalla tazza', [qt + ' =', sym('C', 'tazza') + ' ·', '(' + te + ' − ' + tt + ')'], 'Calore della tazza uguale capacità termica della tazza per temperatura finale meno iniziale'),
        ('Bilancio con il contributo della tazza', [qc, '+', ql, '+', qt, '= 0'], 'Somma dei calori di caffè latte e tazza uguale zero'),
    ]
    label, terms, description = formulae[index]
    # Il tema permette di mandare a capo i termini, senza ridurre la leggibilità.
    rendered = ''.join(t if t.startswith('<span class="fraction"') else '<span>' + t + '</span>' for t in terms)
    return (f'<div class="equation" id="formula-{index+1}"><div class="equation-label">{label}</div>'
            f'<div class="math" role="math" aria-label="{escape(description, quote=True)}">{rendered}</div></div>')


def register_notices():
    path = ROOT / 'risorse/crediti.json'
    registry = json.loads(path.read_text())
    # Schede preesistenti riusate per fonte; aggiungere soltanto gli avvisi specifici.
    supplements = {
        META['COP-01'][1]: 'Le Déjeuner (1739), François Boucher, Musée du Louvre, RF 926. The Yorck Project (2002), 10.000 Meisterwerke der Malerei, DIRECTMEDIA Publishing GmbH. La fonte dichiara opera e riproduzione in pubblico dominio; il copyright della compilazione, distinta dalla singola immagine, è detenuto da Zenodot Verlagsgesellschaft mbH e la compilazione è distribuita sotto GNU Free Documentation License.',
        META['FIG-01'][1]: 'Avviso originale di Julius Schorzman: “NOTE: I only require attribution if you publish this photo in print or if it is used in a for-profit project.” Attribuzione completa comunque conservata.',
        META['FIG-02'][1]: 'Fonte originaria NIAID: https://www.flickr.com/photos/54591706@N02/33657535532/ . La revisione Commons scelta è già ritagliata; nessun nuovo ritaglio eseguito.',
        META['FIG-03'][1]: 'Attribuzione sulla fonte: By Burst. Versione distribuita da Rawpixel, https://www.rawpixel.com/image/5915327 . Il file originale conserva i metadati XMP con i rimandi a NegativeSpace e CC0.',
    }
    for resource in registry['resources']:
        extra = supplements.get(resource.get('source'))
        if extra and escape(extra) not in resource['notices'][0]:
            resource['notices'][0] += '<br>' + escape(extra)
    museum = 'https://collections.louvre.fr/ark:/53355/cl010059924'
    for resource in registry['resources']:
        if resource.get('source') == META['COP-01'][1]:
            link = {'url': museum, 'label': 'Scheda dell’opera al Louvre'}
            if link not in resource.setdefault('links', []):
                resource['links'].append(link)
            if museum not in resource['notices'][0]:
                resource['notices'][0] += '<br>Presentazione del quadro: <a href="' + museum + '">Musée du Louvre, Le déjeuner, RF 926</a>. Autore, titolo, data 1739 e collocazione; descrizione della scena da osservazione dell’opera.'
    key = 'credit-bilancio-temperatura-tempo'
    if not any(r['id'] == key for r in registry['resources']):
        registry['resources'].append({'id': key, 'description': 'Temperature del caffè e del latte nel tempo — grafico di modello',
            'source': None, 'author': 'Materia Oscura', 'license': None, 'license_url': None,
            'changes': None, 'status': 'documented', 'links': [], 'fingerprints': [],
            'metadata_sources': [TARGET.name], 'notices': [
                'Grafico originale per Materia Oscura, richiesto dall’utente. Modello illustrativo: caffè 100 g a 80 °C, latte 50 g a 20 °C, calori specifici uguali, temperatura di equilibrio 60 °C. T_c = 60 + 20 exp(−t/60); T_l = 60 − 40 exp(−t/60), t in secondi. Tempo caratteristico ipotizzato di 60 s, non misurato; tazza e ambiente trascurati. Le curve conservano il bilancio energetico e rappresentano un flusso proporzionale alla differenza di temperatura, non dati sperimentali.']})
    path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n')


def main():
    renderer = Renderer()
    source = (WORK / 'bozza.md').read_text().split('\n---\n')[0]
    theory, tail = source.split('## Domande di verifica\n', 1)
    questions, notes_text = tail.split('## Note\n', 1)
    blocks = [b.strip() for b in theory.split('\n\n') if b.strip()]
    body, headings = [], []
    current = cover = None
    count = 0
    for block in blocks:
        if block.startswith(('# ', '<!--')):
            continue
        if block.startswith(('[IMMAGINE ', '[GRAFICO ')):
            current = re.search(r'(COP|FIG|GRA)-\d+', block)[0]
        elif block.startswith('Didascalia:'):
            caption = block.removeprefix('Didascalia:').strip()
            figure = renderer.graph(caption) if current == 'GRA-02' else renderer.figure(current, caption)
            if current == 'COP-01': cover = figure
            else: body.append(figure)
            current = None
        elif block.startswith(r'\['):
            body.append(equation(count)); count += 1
        elif block.startswith('## '):
            title = block[3:]; sid = SECTIONS[len(headings)]; headings.append((sid, title))
            body.append(f'<div class="section-heading"><span class="section-number" aria-hidden="true">{len(headings):02}</span><h2 id="{sid}" data-toc tabindex="-1">{escape(title)}</h2></div>')
        else:
            body.append('<p>' + renderer.inline(block) + '</p>')
    headings.append((SECTIONS[-1], 'Domande di verifica'))
    body.append('<div class="section-heading"><span class="section-number" aria-hidden="true">05</span><h2 id="domande-di-verifica" data-toc tabindex="-1">Domande di verifica</h2></div>')
    items = re.split(r'\n(?=\d+\. )', questions.strip())
    body.append('<ol class="questions">')
    for item in items:
        text = re.sub(r'^\d+\. ', '', item).strip()
        if '\n   - ' in text:
            first, alternatives = text.split('\n   - ', 1)
            choices, after = alternatives.split('\n   \n', 1)
            choices = choices.split('\n   - ')
            rendered = renderer.inline(first) + '<ul>' + ''.join('<li>' + renderer.inline(c) + '</li>' for c in choices) + '</ul><p>' + renderer.inline(after.strip()) + '</p>'
        else:
            rendered = renderer.inline(text)
        body.append('<li>' + rendered + '</li>')
    body.append('</ol>')
    notes = []
    for key, text in re.findall(r'\[\^(\d+)\]: ([\s\S]*?)(?=\n\n\[\^|\Z)', notes_text.strip()):
        returns = ' '.join(f'<a href="#richiamo-{key}{"" if i == 1 else "-" + str(i)}" role="doc-backlink" aria-label="Torna al richiamo {i} della nota {key}">↩{i if renderer.notes[key] > 1 else ""}</a>' for i in range(1, renderer.notes[key] + 1))
        notes.append(f'<li id="nota-{key}">{renderer.inline(text.strip())} {returns}</li>')
    assert cover and count == 7 and len(headings) == 5 and len(notes) == 3 and len(items) == 9
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    template = re.sub(r'<!-- MODELLO CANONICO.*?-->', '<!-- Articolo autonomo dal tema canonico v10; testo approvato e grafico richiesto. -->', template, count=1, flags=re.S)
    template = template.replace('<title>Tema grafico delle dispense — modello riutilizzabile</title>', '<title>' + TITLE + ' — Materia Oscura</title>')
    template = template.replace('name="version" content="v10"', 'name="version" content="v6"', 1)
    template = template.replace('Modello autonomo del tema grafico comune a tutti i capitoli futuri.', 'Il bilancio termico: caffè e latte, calori scambiati, temperatura di equilibrio e contributo della tazza.')
    template = template.replace('Nome dell’area tematica', 'Materia e calore').replace('Titolo dell’articolo', TITLE)
    template = template.replace('<span class="sidebar-label">Fisica</span>', '<span class="sidebar-label">Materia e calore</span>')
    sidebar = '<nav class="sidebar-nav" aria-label="Sezioni dell’articolo"><ol>' + ''.join(f'<li class="level-2"><a href="#{sid}"><span class="item-number" aria-hidden="true">{i:02}</span><span>{escape(title)}</span></a></li>' for i, (sid, title) in enumerate(headings, 1)) + '</ol></nav>'
    template = re.sub(r'<nav class="sidebar-nav".*?</nav>', lambda _: sidebar, template, count=1, flags=re.S)
    template = re.sub(r'<figure class="visual cover">.*?</figure>', lambda _: cover, template, count=1, flags=re.S)
    template = re.sub(r'(<article class="article">).*?(<nav class="bottom-links")', lambda m: m[1] + '\n'.join(body) + m[2], template, count=1, flags=re.S)
    template = re.sub(r'(<details class="chapter-notes".*?<ol>).*?(</ol>)', lambda m: m[1] + ''.join(notes) + m[2], template, count=1, flags=re.S)
    template = template.replace('Versione v10 — 19 ottobre 2026', 'Versione v6 — 19 ottobre 2026')
    # Dilatazione è ancora pianificata: nella sequenza pubblicata segue Stati della materia.
    navigation = ('<nav class="chapter-navigation" aria-label="Navigazione tra articoli"><a rel="prev" href="https://rickymusu-bit.github.io/fisica/energia_interna_calore_specifico_it.html"><span>← Articolo precedente</span><small>Energia interna, calore e calore specifico</small></a><a rel="next" href="https://rickymusu-bit.github.io/fisica/stati_della_materia.html"><span>Articolo successivo →</span><small>Stati della materia</small></a></nav>')
    template = template.replace('<!-- chapter-navigation:end -->', navigation + '<!-- chapter-navigation:end -->')
    TARGET.write_text(template)
    register_notices()
    print(TARGET.name, TARGET.stat().st_size, 'byte prima della sincronizzazione dei crediti')


if __name__ == '__main__':
    main()
