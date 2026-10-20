"""Aggiorna solo modello ufficiale e confronto; mai i sorgenti degli articoli."""
from pathlib import Path
import argparse
import re
from strings_site import enhance_article, render_comparison
from credits import load_registry, render_page

ROOT = Path(__file__).resolve().parents[1]


def outputs():
    model = ROOT / 'riferimenti/TEMA_DISPENSE.html'
    source = model.read_text(encoding='utf-8')
    # Lo snapshot dei crediti resta esattamente quello verificato dal registro.
    credits = re.search(r'<!-- resource-credits:start -->[\s\S]*?<!-- resource-credits:end -->', source).group(0)
    result = enhance_article(source, '')
    result = re.sub(r'<!-- resource-credits:start -->[\s\S]*?<!-- resource-credits:end -->', lambda _: credits, result)
    return {model: result,
            ROOT / 'lavorazione/sito/anteprima-bordi-stringhe.html': render_comparison((ROOT / 'index.html').read_text()),
            ROOT / 'crediti.html': render_page(load_registry())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    # Il generatore dei crediti legge gli stili del modello: aggiornare in due passi.
    for path, content in outputs().items():
        if path.name == 'crediti.html':
            content = render_page(load_registry())
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise ValueError(f'Componente non aggiornato: {path.relative_to(ROOT)}')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    print('Tema Stringhe e confronto allineati')


if __name__ == '__main__':
    main()
