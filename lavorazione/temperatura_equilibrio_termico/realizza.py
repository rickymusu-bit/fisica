"""Genera l'articolo autonomo dal tema canonico e dalla bozza approvata.

Eseguire dalla radice, poi scripts/credits.py --sync e copiare il risultato
in bozza.html. Non modifica il catalogo o l'ammissione alla pubblicazione.
"""
from pathlib import Path
from html import escape
import base64
import re

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
TARGET = ROOT / 'temperatura_equilibrio_termico_it.html'
TITLE = 'Temperatura ed equilibrio termico'
META = {
    'COP-01': (
        'copertina-termometro-galileiano.jpg',
        'Galileo_Thermometer_in_Tokyo.jpg', 'Syced', 'CC0 1.0',
        'https://creativecommons.org/publicdomain/zero/1.0/',
        'Termometro galileiano con ampolle colorate e contrassegni numerici nel liquido',
    ),
    'FIG-01': (
        'misura-temperatura-paziente.jpg',
        'Physician_taking_temperature_of_young_patient_(4644489973).jpg',
        'Roy Perry; National Library of Medicine — History of Medicine',
        'No known copyright restrictions — Flickr Commons',
        'https://www.flickr.com/commons/usage/',
        'Un medico misura la temperatura di una giovane paziente con un termometro in bocca',
    ),
    'FIG-02': (
        'bevanda-fredda.jpg', 'Cold_Drink_on_a_patio_table.jpg',
        'Henryemix', 'CC0 1.0',
        'https://creativecommons.org/publicdomain/zero/1.0/',
        'Bicchiere di bevanda fredda con cubetti di ghiaccio su un tavolo',
    ),
}
SECTIONS = [
    'quando-fidarsi-del-termometro', 'equilibrio-termico',
    'principio-zero', 'scale-di-temperatura', 'domande-di-verifica',
]

# Soltanto i componenti specifici (tabella e frazioni nel testo) estendono il tema.
# CSS, font e comandi comuni restano quelli del modello senza sovrascritture.
COMPONENT_STYLE = '''<style data-component="scale-di-temperatura">
.inline-math .fraction{display:inline-flex;flex-direction:column;vertical-align:middle;font-size:.8em;line-height:1.25;text-align:center;white-space:normal}
.thermal-scales-scroll{max-width:100%;overflow-x:auto}
.thermal-scales-scroll:focus-visible{outline:3px solid #080808;outline-offset:4px}
.thermal-scales{width:100%;min-width:650px;border-collapse:collapse;font-size:16px;line-height:1.6;text-align:left}
.thermal-scales caption{text-align:left;padding:14px 16px;font-weight:600;background:#c4c4c4;border-bottom:2px solid #080808}
.thermal-scales th,.thermal-scales td{padding:12px 14px;border-bottom:1px solid #aaa;vertical-align:top}
.thermal-scales thead th{border-bottom:2px solid #080808;background:#eee;font-weight:600}
.thermal-scales th+th,.thermal-scales td{border-left:1px solid #aaa}
.thermal-scales tbody th{font-weight:500}
.thermal-scales tbody tr:last-child>*{border-bottom:0}
.thermal-scales td{white-space:nowrap}
</style>'''


def fraction(numerator, denominator):
    return f'<span class="fraction"><span>{numerator}</span><span>{denominator}</span></span>'


def inline_math(tex):
    values = {
        r'T/\mathrm{K}': (fraction('<i>T</i>', 'K'), 'T diviso kelvin'),
        r'T/^\circ\mathrm{C}': (fraction('<i>T</i>', '°C'), 'T diviso gradi Celsius'),
        r'\frac{9}{5}': (fraction('9', '5'), 'nove quinti'),
    }
    content, label = values[tex]
    return f'<span class="inline-math" role="math" aria-label="{label}">{content}</span>'


class Renderer:
    def __init__(self):
        self.note_counts = {}

    def inline(self, source):
        chunks = re.split(r'(\\\(.*?\\\))', source)
        content = ''.join(inline_math(c[2:-2]) if c.startswith(r'\(') else escape(c)
                          for c in chunks)
        content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)

        def note(match):
            key = match[1]
            self.note_counts[key] = self.note_counts.get(key, 0) + 1
            suffix = '' if self.note_counts[key] == 1 else '-' + str(self.note_counts[key])
            return (f'<sup class="note-ref"><a href="#nota-{key}" '
                    f'id="richiamo-{key}{suffix}" role="doc-noteref" '
                    f'aria-label="Nota {key}">[{key}]</a></sup>')
        return re.sub(r'\[\^(\d+)\]', note, content)

    def figure(self, key, caption):
        filename, source, author, license_name, license_url, alt = META[key]
        path = WORK / 'risorse' / filename
        with Image.open(path) as im:
            width, height = im.size
        uri = 'data:image/jpeg;base64,' + base64.b64encode(path.read_bytes()).decode()
        attrs = {
            'source': 'https://commons.wikimedia.org/wiki/File:' + source,
            'author': author, 'license': license_name, 'license-url': license_url,
            'changes': 'Nessuna modifica alla versione scelta; visualizzazione proporzionale senza ritaglio.',
        }
        metadata = ' '.join(f'data-credit-{k}="{escape(v, quote=True)}"' for k, v in attrs.items())
        classes = 'visual cover photo portrait' if key == 'COP-01' else 'visual photo'
        return (f'<figure class="{classes}" id="{key.lower()}" {metadata}>'
                '<div class="image-frame"><div class="overview">'
                f'<img src="{uri}" width="{width}" height="{height}" '
                f'alt="{escape(alt, quote=True)}" decoding="async">'
                '</div></div><figcaption>' + self.inline(caption) + '</figcaption></figure>')

    def table(self, block, caption):
        rows = [[c.strip() for c in line.strip().strip('|').split('|')]
                for line in block.splitlines()]
        header = '<thead><tr>' + ''.join(f'<th scope="col">{self.inline(v)}</th>'
                                        for v in rows[0]) + '</tr></thead>'
        body = '<tbody>'
        for row in rows[2:]:
            body += '<tr><th scope="row">' + self.inline(row[0]) + '</th>'
            body += ''.join('<td>' + self.inline(v) + '</td>' for v in row[1:]) + '</tr>'
        body += '</tbody>'
        return ('<figure class="visual" id="tab-01"><div class="image-frame">'
                '<div class="thermal-scales-scroll" tabindex="0" role="region" '
                'aria-label="Tabella delle scale, con scorrimento orizzontale se necessario">'
                '<table class="thermal-scales"><caption>Corrispondenze fra le scale di temperatura</caption>'
                + header + body + '</table></div></div><figcaption>'
                + self.inline(caption) + '</figcaption></figure>')


def equation(index):
    kelvin = fraction('<i>T</i>', 'K')
    celsius = fraction('<i>T</i>', '°C')
    fahrenheit = fraction('<i>T</i>', '°F')
    values = [
        ('Dai gradi Celsius ai kelvin',
         f'<span>{kelvin}</span><span>=</span><span>{celsius}</span><span>+ 273,15</span>',
         'Il valore della temperatura in kelvin è uguale al valore in gradi Celsius più 273 virgola 15'),
        ('Dai gradi Celsius ai gradi Fahrenheit',
         f'<span>{fahrenheit}</span><span>=</span><span>{fraction("9", "5")} · {celsius}</span><span>+ 32</span>',
         'Il valore in gradi Fahrenheit è uguale a nove quinti per il valore in gradi Celsius più 32'),
        ('Dai gradi Fahrenheit ai gradi Celsius',
         f'<span>{celsius}</span><span>=</span><span>{fraction("5", "9")} · ( {fahrenheit} − 32 )</span>',
         'Il valore in gradi Celsius è uguale a cinque noni per la differenza fra il valore in gradi Fahrenheit e 32'),
    ]
    label, formula, description = values[index]
    return (f'<div class="equation" id="conversione-{index+1}">'
            f'<div class="equation-label">{label}</div>'
            f'<div class="math" role="math" aria-label="{description}">{formula}</div></div>')


def main():
    renderer = Renderer()
    blocks = [b.strip() for b in (WORK / 'bozza.md').read_text().split('\n\n') if b.strip()]
    body, headings, notes = [], [], []
    current = cover = table = None
    equation_count = 0
    for block in blocks:
        if block.startswith(('# ', 'Bozza v', '[TABELLA')):
            continue
        if block.startswith('[IMMAGINE'):
            current = re.search(r'(?:COP|FIG)-\d+', block)[0]
            continue
        if block.startswith('Didascalia:'):
            figure = renderer.figure(current, block.removeprefix('Didascalia:').strip())
            if current == 'COP-01':
                cover = figure
            else:
                body.append(figure)
            current = None
            continue
        if block.startswith('Didascalia proposta:'):
            assert table
            body.append(renderer.table(table, block.removeprefix('Didascalia proposta:').strip()))
            table = None
            continue
        if block.startswith('|'):
            table = block
            continue
        if block.startswith(r'\['):
            body.append(equation(equation_count))
            equation_count += 1
            continue
        if block.startswith('[^'):
            key, text = re.fullmatch(r'\[\^(\d+)\]: (.*)', block).groups()
            notes.append(f'<li id="nota-{key}">{renderer.inline(text)} '
                         f'<a href="#richiamo-{key}" role="doc-backlink" '
                         f'aria-label="Torna al primo richiamo della nota {key}">↩</a></li>')
            continue
        if block.startswith('## '):
            title = block[3:]
            if title == 'Note':
                continue
            sid = SECTIONS[len(headings)]
            headings.append((sid, title))
            body.append('<div class="section-heading">'
                        f'<span class="section-number" aria-hidden="true">{len(headings):02}</span>'
                        f'<h2 id="{sid}" data-toc tabindex="-1">{escape(title)}</h2></div>')
            continue
        if re.match(r'1\. ', block):
            items = re.split(r'\n(?=\d+\. )', block)
            body.append('<ol class="questions">' + ''.join(
                '<li>' + renderer.inline(re.sub(r'^\d+\. ', '', item)) + '</li>'
                for item in items) + '</ol>')
            continue
        body.append('<p>' + renderer.inline(block) + '</p>')
    assert cover and equation_count == 3 and len(headings) == 5 and len(notes) == 2
    template = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    template = re.sub(r'<!-- MODELLO CANONICO.*?-->',
                      '<!-- Articolo autonomo; tema canonico v8, contenuto approvato. -->',
                      template, count=1, flags=re.S)
    template = template.replace('<title>Tema grafico delle dispense — modello riutilizzabile</title>',
                                f'<title>{TITLE} — Materia Oscura</title>')
    template = template.replace('name="version" content="v8"', 'name="version" content="v1"', 1)
    template = template.replace('name="date" content="2026-10-18"', 'name="date" content="2026-10-19"', 1)
    template = template.replace('Modello autonomo del tema grafico comune a tutti i capitoli futuri.',
                                'Temperatura, equilibrio termico, principio zero, termometro e scale Celsius, Kelvin e Fahrenheit.')
    template = template.replace('Nome dell’area tematica', 'Materia e calore').replace('Titolo dell’articolo', TITLE)
    template = template.replace('<span class="sidebar-label">Fisica</span>',
                                '<span class="sidebar-label">Materia e calore</span>')
    sidebar = '<nav class="sidebar-nav" aria-label="Sezioni dell’articolo"><ol>'
    sidebar += ''.join(f'<li class="level-2"><a href="#{sid}">'
                       f'<span class="item-number" aria-hidden="true">{i:02}</span>'
                       f'<span>{escape(title)}</span></a></li>'
                       for i, (sid, title) in enumerate(headings, 1)) + '</ol></nav>'
    template = re.sub(r'<nav class="sidebar-nav".*?</nav>', lambda _: sidebar,
                      template, count=1, flags=re.S)
    template = re.sub(r'<figure class="visual cover">.*?</figure>', lambda _: cover,
                      template, count=1, flags=re.S)
    template = re.sub(r'(<article class="article">).*?(<nav class="bottom-links")',
                      lambda m: m[1] + '\n'.join(body) + m[2], template, count=1, flags=re.S)
    template = re.sub(r'(<details class="chapter-notes".*?<ol>).*?(</ol>)',
                      lambda m: m[1] + ''.join(notes) + m[2], template, count=1, flags=re.S)
    template = template.replace('</head>', COMPONENT_STYLE + '</head>', 1)
    navigation = ('<nav class="chapter-navigation" aria-label="Navigazione tra articoli">'
                  '<a rel="prev" href="https://rickymusu-bit.github.io/fisica/termodinamica_sistemi_it.html">'
                  '<span>← Articolo precedente</span><small>La termodinamica e i sistemi termodinamici</small></a>'
                  '<a rel="next" href="https://rickymusu-bit.github.io/fisica/stati_della_materia.html">'
                  '<span>Articolo successivo →</span><small>Stati della materia</small></a></nav>')
    template = template.replace('<!-- chapter-navigation:end -->', navigation + '<!-- chapter-navigation:end -->')
    template = template.replace('Versione v8 · 2026-10-18', 'Versione v1 · 19 ottobre 2026')
    TARGET.write_text(template)
    print(TARGET.name, TARGET.stat().st_size, 'byte')


if __name__ == '__main__':
    main()
