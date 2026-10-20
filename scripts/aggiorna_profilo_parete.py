#!/usr/bin/env python3
"""Integra il nuovo SVG senza riserializzare gli altri contenuti del capitolo."""
from pathlib import Path
import base64
import re
import sys
from credits import Document

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'conduzione_it.html'
SVG = ROOT / 'lavorazione/conduzione/risorse/parete-temperatura-profilo-curvo.svg'
FIGURE = 'visuale-immagine-06-e-grafico-g-1'
CREDIT = 'parete-temperatura-profilo-curvo'
ALT = ('Profilo qualitativo di temperatura attraverso un muro: aria interna a 25 °C '
       'e aria esterna a −5 °C; raccordi curvi nell’aria e variazione lineare nello spessore della parete.')
CAPTION = ('L’aria interna è a 25 °C e quella esterna a −5 °C. Il profilo è qualitativo: '
           'la temperatura varia nell’aria vicino alle superfici e diminuisce linearmente '
           'nello spessore del muro omogeneo, in condizioni stazionarie.')
PARAGRAPH = ('Tra l’aria interna e quella esterna c’è una differenza di temperatura di 30 K. '
             'Questa non è però, in generale, la differenza tra le temperature delle due facce '
             'della parete richiesta dalla legge di Fourier: gli scambi tra l’aria e le superfici '
             'producono ulteriori variazioni. Per calcolare la conduzione nel solo muro occorre '
             'conoscere la differenza di temperatura fra le due facce; la figura ne mostra il '
             'significato senza assegnarle valori numerici.')


def update(source):
    document = Document(source)
    figure = next(n for n in document.root.descendants('figure') if n.attrs.get('id') == FIGURE)
    uri = 'data:image/svg+xml;base64,' + base64.b64encode(SVG.read_bytes()).decode('ascii')
    edits = []
    opening = source[figure.start:source.index('>', figure.start)+1]
    if 'data-credit-id' not in opening:
        edits.append((figure.start, figure.start+len(opening), opening[:-1]+' data-credit-id="'+CREDIT+'">'))
    for image in figure.descendants('img'):
        tag = document.html(image)
        for key, value in [('src', uri), ('alt', ALT), ('width', '1040'), ('height', '680')]:
            if re.search(r'\b'+key+r'="[^"]*"', tag):
                tag = re.sub(r'\b'+key+r'="[^"]*"', lambda _: key+'="'+value+'"', tag)
            else:
                tag = tag.replace('<img ', '<img '+key+'="'+value+'" ', 1)
        edits.append((image.start, image.end, tag))
    caption = next(figure.descendants('figcaption'))
    edits.append((caption.start, caption.end, '<figcaption>'+CAPTION+'</figcaption>'))
    for paragraph in document.root.descendants('p'):
        if document.html(paragraph).startswith('<p>Nell’illustrazione le due facce'):
            edits.append((paragraph.start, paragraph.end, '<p>'+PARAGRAPH+'</p>'))
    for start, end, replacement in sorted(edits, reverse=True):
        source = source[:start]+replacement+source[end:]
    return source


def main():
    source = HTML.read_text()
    result = update(source)
    if '--check' in sys.argv:
        if source != result:
            raise SystemExit('Profilo non ancora allineato nell’HTML.')
        print('SVG, ingrandimento, didascalia e testo allineati.')
    else:
        HTML.write_text(result)
        print('Profilo della parete integrato nel capitolo.')


if __name__ == '__main__':
    main()
