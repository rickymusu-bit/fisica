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


def icon(name):
    shapes = {
        'home': '<path d="m3 10 9-7 9 7v10H6V10M9 20v-7h6v7"/>',
        'books': '<path d="M3 4h5v16H3zM8 4h5v16H8zM15 5l4-1 4 15-4 1z"/>',
        'download': '<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',
        'language': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c-5 5-5 13 0 18 5-5 5-13 0-18Z"/>',
        'index': '<path d="M8 5h13M8 12h13M8 19h13M3 5h.01M3 12h.01M3 19h.01"/>',
        'close': '<path d="m6 6 12 12M6 18 18 6"/>',
        'moon': '<path d="M20 15A9 9 0 0 1 9 4a9 9 0 1 0 11 11Z"/>',
        'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1 1m12 12 1 1M5 19l1-1M18 6l1-1"/>',
    }
    return ('<svg class="ui-icon" data-ui-icon viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" focusable="false">' + shapes[name] + '</svg>')


def theme_control():
    return ('<details class="theme-control theme-menu" data-theme-menu>'
            '<summary aria-label="Tema del sito: Scuro" title="Tema: Scuro">'
            f'<span class="theme-current-dark">{icon("moon")}</span>'
            f'<span class="theme-current-light">{icon("sun")}</span>'
            '<span class="menu-chevron" aria-hidden="true">▾</span></summary>'
            '<div class="theme-options" role="group" aria-label="Scegli il tema">'
            f'<button type="button" data-theme-option="dark" aria-pressed="true" disabled>{icon("moon")}<span>Scuro</span></button>'
            f'<button type="button" data-theme-option="light" aria-pressed="false" disabled>{icon("sun")}<span>Chiaro</span></button>'
            '</div></details>')


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
    document = re.sub(r'<details\b[^>]*data-theme-menu[^>]*>[\s\S]*?</details>',
                      lambda _: theme_control(), document)
    document = re.sub(r'<summary\b[^>]*class="index-toggle"[^>]*>[\s\S]*?</summary>',
                      lambda _: '<summary class="index-toggle" aria-label="Indice del capitolo" title="Indice del capitolo">' +
                      icon('index') + '<span class="nav-label">Indice</span><span class="index-close">' + icon('close') + '</span></summary>', document)
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
