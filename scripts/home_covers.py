"""Renderizza copertina, catalogo e attribuzioni dalla raccolta approvata."""
from html import escape
import json
from pathlib import Path
import re


def load_covers(root):
    folder = root / "copertine"
    covers = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    if not isinstance(covers, list) or not covers:
        raise ValueError("La raccolta delle copertine è vuota")
    ids = set()
    paths = set()
    for cover in covers:
        for key in ("id", "src", "title", "caption", "alt", "credit", "license", "licenseUrl", "source", "originalTitle", "changes"):
            if not isinstance(cover.get(key), str) or not cover[key].strip():
                raise ValueError(f"Dato della copertina assente: {key}")
        path = (root / cover["src"]).resolve()
        if not path.is_relative_to(folder.resolve()) or path.suffix != ".webp" or not path.is_file():
            raise ValueError(f"Copertina locale non valida: {cover['src']}")
        if cover["id"] in ids or path in paths:
            raise ValueError("Copertina duplicata")
        if any(not isinstance(cover.get(k), int) or cover[k] <= 0 for k in ("width", "height")):
            raise ValueError("Dimensioni della copertina non valide")
        if not all(cover[k].startswith("https://") for k in ("source", "licenseUrl")):
            raise ValueError("Fonte o licenza non valida")
        ids.add(cover["id"])
        paths.add(path)
    return covers


def cover_figure(covers):
    first = covers[0]
    image = (f'<img src="{escape(first["src"], quote=True)}" '
             f'width="{first["width"]}" height="{first["height"]}" '
             f'alt="{escape(first["alt"], quote=True)}" fetchpriority="high">')
    return f'''<figure class="cover">
            <div class="cover-media">
              <img id="cover-image" width="{first["width"]}" height="{first["height"]}" alt="{escape(first["alt"], quote=True)}" fetchpriority="high" decoding="async">
              <noscript>{image}</noscript>
            </div>
            <figcaption id="cover-caption">{escape(first["caption"])}</figcaption>
          </figure>'''


def cover_credits(covers, ui):
    lines = ['<details class="credits" id="crediti-copertine"><summary>' + escape(ui["credits"]) + '</summary>',
             '<p id="cover-credit-current">' + escape(ui["prefix"] + ' ' + covers[0]["credit"] + '. ' + covers[0]["license"] + '.') + '</p>', '<ol class="cover-credits-list">']
    for cover in covers:
        e = lambda key: escape(cover[key], quote=True)
        lines.append(f'<li id="credito-{e("id")}">'
                     f'<a href="{e("source")}">{e("originalTitle")}</a> — {e("credit")}. '
                     f'<a href="{e("licenseUrl")}">{e("license")}</a>. {e("changes")}</li>')
    lines.extend(['</ol>', '</details>'])
    return '\n'.join(lines)


def render_covers(html, covers, ui=None):
    ui = ui or {"credits": "Crediti delle immagini", "prefix": "In copertina:",
                "unavailable": "La copertina non è disponibile.",
                "fallback": "Le fotografie della raccolta e i relativi crediti sono elencati qui sotto."}
    data = json.dumps(covers, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    blocks = {"cover-figure": cover_figure(covers),
              "cover-data": '<script id="cover-data" type="application/json" ' + ' '.join(
                  f'data-{key}="{escape(ui[key], quote=True)}"' for key in ("prefix", "unavailable", "fallback")
              ) + '>' + data + '</script>',
              "cover-credits": cover_credits(covers, ui)}
    for marker, content in blocks.items():
        pattern = rf'<!-- {marker}:start -->[\s\S]*?<!-- {marker}:end -->'
        html, count = re.subn(pattern, lambda _: f'<!-- {marker}:start -->\n{content}\n<!-- {marker}:end -->', html)
        if count != 1:
            raise ValueError(f"Segnaposto della home assente o duplicato: {marker}")
    return html
