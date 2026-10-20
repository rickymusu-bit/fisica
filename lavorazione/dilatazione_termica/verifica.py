"""Verifica didascalie, risorse e componenti canoniche del capitolo in bozza.

Eseguire dalla radice del repository: python3 lavorazione/dilatazione_termica/verifica.py
"""
from pathlib import Path
import base64
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from credits import Document, text
from stringhe_theme import asset

source = (ROOT / 'dilatazione_termica_it.html').read_text()
model = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
draft = Path(__file__).with_name('bozza.md').read_text()
expected = re.findall(r'!\[[^\n]*\]\(risorse/([^\n)]+)\)\s*Didascalia: ([^\n]+)', draft)
document = Document(source)
figures = list(document.root.descendants('figure'))
assert len(figures) == len(expected) == 11, 'Inventario delle figure incompleto'
for figure, (filename, caption) in zip(figures, expected):
    identifier = figure.attrs.get('id')
    captions = list(figure.descendants('figcaption'))
    assert len(captions) == 1, f'Didascalia assente o duplicata: {identifier}'
    assert text(document.html(captions[0])) == caption, f'Didascalia diversa dalla bozza: {identifier}'
    original = (Path(__file__).parent / 'risorse' / filename).read_bytes()
    for image in figure.descendants('img'):
        embedded = base64.b64decode(image.attrs['src'].split(',', 1)[1])
        assert embedded == original, f'Immagine diversa dall’originale scelto: {identifier}'
    for zoom in (n for n in figure.descendants('details') if n.has_class('image-zoom')):
        controls = list(zoom.descendants('summary'))
        assert len(controls) == 1 and controls[0].has_class('media-icon-button'), identifier
        assert not text(document.html(controls[0])), f'Comando testuale obsoleto: {identifier}'
        assert controls[0].attrs.get('aria-label') and controls[0].attrs.get('title'), identifier

for tag, attribute, filename in [
    ('style', 'stringhe-theme', 'tema-stringhe.css'),
    ('style', 'media-ui', 'media-controls.css'),
    ('script', 'media-ui', 'media-controls.js'),
    ('script', 'stringhe-init', 'tema-init.js'),
    ('script', 'stringhe-controls', 'tema-controlli.js'),
]:
    embedded = re.findall(fr'<{tag} data-{attribute}>([\s\S]*?)</{tag}>', source)
    assert len(embedded) == 1 and embedded[0] == asset(filename), f'Componente fuori tema: {filename}'
base_styles = lambda html: [style for style in re.findall(r'<style>([\s\S]*?)</style>', html) if '@font-face' in style]
assert base_styles(source) == base_styles(model), 'Stile base diverso dal modello corrente'
notes_style = lambda html: re.search(r'<style data-component="note-pie-pagina">[\s\S]*?</style>', html)[0]
assert notes_style(source) == notes_style(model), 'Note diverse dal modello corrente'
print('Verificate 11 didascalie, originali incorporati, comandi a icona e componenti canoniche del tema.')

nav = lambda html: re.search(r"<!-- stringhe-navigation:start -->[\s\S]*?<!-- stringhe-navigation:end -->", html)[0]
expected_nav = nav(model).replace('href="" download=""', 'href="dilatazione_termica_it.html" download="dilatazione_termica_it.html"')
assert nav(source) == expected_nav, "Navigazione diversa dal modello corrente"
