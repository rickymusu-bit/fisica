"""Componenti incorporabili del tema Stringhe, condivisi da portale e modello.

Nessuna risorsa di rete: ogni HTML generato conserva CSS e comportamenti.
Tema scelto: reticolo regolare e sinusoidi verticali di uguale ampiezza.
Le alternative rimangono nella pagina di confronto.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'identita'


def asset(name):
    return (ASSETS / name).read_text(encoding='utf-8')


def theme_head():
    return ('<script data-stringhe-init>' + asset('tema-init.js') + '</script>'
            '<style data-stringhe-theme>' + asset('tema-stringhe.css') + '</style>')


def theme_script():
    return '<script data-stringhe-controls>' + asset('tema-controlli.js') + '</script>'


def theme_control():
    return ('<button class="theme-control theme-switch" type="button" role="switch" '
            'aria-label="Tema scuro" aria-checked="true" data-theme-toggle disabled>'
            '<span class="theme-track" aria-hidden="true"><span class="theme-thumb"></span></span>'
            '<span data-theme-label>Scuro</span></button>')


def logo():
    svg = asset('logo-materia-oscura.svg')
    svg = re.sub(r'^<\?xml[^>]*>\s*', '', svg)
    svg = svg.replace('<svg ', '<svg id="brand-logo" class="brand-logo" aria-hidden="true" focusable="false" ', 1)
    return ('<button class="brand-logo-toggle" type="button" data-logo-toggle '
            'aria-label="Metti in pausa l’animazione del logo" aria-pressed="false" disabled>'
            + svg + '</button>')


def update_logo_components(document):
    """Aggiorna solo il logo dell’interfaccia; nessun SVG scientifico viene riscritto."""
    replacement = re.search(r'<svg[\s\S]*?</svg>', logo()).group(0)
    return re.sub(r'(<button\b[^>]*\bdata-logo-toggle\b[^>]*>)[\s\S]*?(</button>)',
                  lambda match: match[1] + replacement + match[2], document)


def logo_script():
    return '<script data-common-logo>' + asset('controlli-logo.js') + '</script>'


def apply_theme(document):
    """Idempotente: permette di rigenerare il modello senza doppioni."""
    for marker, tag in [('stringhe-init', 'script'), ('stringhe-theme', 'style'),
                        ('stringhe-controls', 'script')]:
        document = re.sub(rf'<{tag} data-{marker}>[\s\S]*?</{tag}>', '', document)
    # Migra il controllo nel modello esistente e nelle pagine di servizio.
    document = re.sub(r'<label class="theme-control">[\s\S]*?</label>',
                      lambda _: theme_control(), document)
    document = re.sub(r'<button\b[^>]*data-theme-toggle[^>]*>[\s\S]*?</button>',
                      lambda _: theme_control(), document)
    document = update_logo_components(document)
    # Impostazione strutturale anche senza JavaScript e nelle copie autonome.
    document = re.sub(r'(<html\b)([^>]*)(>)',
                      lambda match: match[1] + match[2] +
                      (' data-edge="sides"' if 'data-edge=' not in match[2] else '') +
                      (' data-theme="dark"' if 'data-theme=' not in match[2] else '') + match[3],
                      document, count=1, flags=re.I)
    # La preferenza si applica prima del primo rendering.
    document = document.replace('</head>', theme_head() + '</head>', 1)
    document = document.replace('</body>', theme_script() + '</body>', 1)
    return document
