"""Componenti incorporabili del tema Stringhe, condivisi da portale e modello.

Nessuna risorsa di rete: ogni HTML generato conserva CSS e comportamenti.
Le varianti sono opzioni di confronto, non una decisione grafica definitiva.
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
    return ('<label class="theme-control">Tema '
            '<select data-theme-select aria-label="Tema del sito">'
            '<option value="auto">Automatico</option><option value="light">Chiaro</option>'
            '<option value="dark">Scuro</option></select></label>')


def logo():
    svg = asset('logo-materia-oscura.svg')
    svg = re.sub(r'^<\?xml[^>]*>\s*', '', svg)
    return ('<button class="brand-logo-toggle" type="button" data-logo-toggle '
            'aria-label="Metti in pausa l’animazione del logo" aria-pressed="false" disabled>'
            + svg + '</button>')


def logo_script():
    return '<script data-common-logo>' + asset('controlli-logo.js') + '</script>'


def apply_theme(document):
    """Idempotente: permette di rigenerare il modello senza doppioni."""
    for marker, tag in [('stringhe-init', 'script'), ('stringhe-theme', 'style'),
                        ('stringhe-controls', 'script')]:
        document = re.sub(rf'<{tag} data-{marker}>[\s\S]*?</{tag}>', '', document)
    # La preferenza si applica subito dopo charset/viewport, prima degli stili.
    document = document.replace('</head>', theme_head() + '</head>', 1)
    document = document.replace('</body>', theme_script() + '</body>', 1)
    return document
