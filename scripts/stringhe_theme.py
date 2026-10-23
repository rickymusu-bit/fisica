"""Componenti incorporabili del tema Stringhe, condivisi da portale e modello.

Nessuna risorsa di rete: ogni HTML generato conserva CSS e comportamenti.
Tema scelto: reticolo regolare e sinusoidi verticali di uguale ampiezza.
Le alternative rimangono nella pagina di confronto.
"""
from pathlib import Path
from html import escape
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
        'play': '<path d="m8 4 13 8-13 8Z"/>',
        'pause': '<path d="M8 4v16M16 4v16"/>',
        'zoom-in': '<circle cx="10" cy="10" r="7"/><path d="m15 15 6 6M7 10h6M10 7v6"/>',
        'zoom-out': '<circle cx="10" cy="10" r="7"/><path d="m15 15 6 6M7 10h6"/>',
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



def navigation_header(page, filename='', index_markup=''):
    """Unica barra Stringhe: navigazione a sinistra, Lingua e Tema a destra.

    Le pagine usano lo stesso markup, le icone e i controlli. Cambia soltanto
    l'insieme dei comandi contestuali, mai la posizione delle impostazioni.
    """
    if page not in {'home', 'catalogue', 'quiz', 'chapter', 'credits', 'comparison'}:
        raise ValueError(f'Tipo di pagina sconosciuto: {page}')
    if page == 'chapter' and not index_markup:
        raise ValueError('Indice del capitolo mancante')
    def link(href, label, symbol, *, download=False):
        safe = escape(href, quote=True)
        special = f' download="{safe}"' if download else f' data-site-path="{safe}"'
        return (f'<a class="string-nav" href="{safe}"{special} '
                f'aria-label="{label}" title="{label}">'
                f'{icon(symbol)}<span class="nav-label">{label}</span></a>')
    actions = []
    if page != 'home':
        actions.append(link('index.html', 'Home', 'home'))
    if page in {'chapter', 'credits'}:
        actions.append(link('articoli.html', 'Tutti i capitoli', 'books'))
    if page == 'chapter':
        actions.append(link(filename, 'Scarica il capitolo', 'download', download=True))
        actions.append(index_markup)
    language = ('<details class="string-lang" name="stringhe-header-menu">'
                '<summary aria-label="Seleziona lingua" title="Lingua: Italiano">'
                '<span class="language-code">IT ▾</span></summary>'
                '<div class="string-languages" lang="it">✓ Italiano</div></details>')
    nav = ('<nav class="stringhe-navigation site-nav top-links" aria-label="Navigazione principale">'
           '<div class="nav-primary">' + ''.join(actions) + '</div>'
           '<div class="nav-settings">' + language + theme_control() + '</div></nav>')
    if page == 'chapter':
        return '<header class="topbar stringhe-header">' + nav + '</header>'
    classes = 'site-header stringhe-header'
    if page == 'home':
        classes += ' home-header'
    elif page in {'catalogue', 'quiz'}:
        classes += ' service-header'
    return f'<header class="{classes}"><div class="top-inner">{nav}</div></header>'


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
    # Un solo menu Lingua/Tema aperto, anche senza JavaScript nei browser moderni.
    def group_header_menu(match):
        tag = match.group(0)
        classes = re.search(r'class="([^"]*)"', tag)
        is_language = classes and {'lang', 'string-lang'} & set(classes.group(1).split())
        if ('data-theme-menu' in tag or is_language) and not re.search(r'\bname=', tag):
            return tag[:-1] + ' name="stringhe-header-menu">'
        return tag
    document = re.sub(r'<details\b[^>]*>', group_header_menu, document)
    document = update_logo_components(document)
    # Impostazione strutturale anche senza JavaScript e nelle copie autonome.
    document = re.sub(r'(<html\b)([^>]*)(>)',
                      lambda match: match[1] + match[2] +
                      (' data-edge="sides"' if 'data-edge=' not in match[2] else '') +
                      (' data-theme="dark"' if 'data-theme=' not in match[2] else '') + match[3],
                      document, count=1, flags=re.I)
    from media_controls import apply_media_controls
    document = apply_media_controls(document)
    # La preferenza si applica prima del primo rendering.
    document = document.replace('</head>', theme_head() + '</head>', 1)
    document = document.replace('</body>', theme_script() + '</body>', 1)
    from youtube_videos import apply_youtube_videos
    document = apply_youtube_videos(document, include_assets='MODELLO CANONICO DEL TEMA' in document)
    return document
