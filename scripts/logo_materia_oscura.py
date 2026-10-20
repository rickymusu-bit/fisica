"""Genera il logo Stringhe: curva nera originale e curva blu in opposizione di fase."""
from math import cos, sin, pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RADIUS = 104
AMPLITUDE = 20
CRESTS = 4
PERIOD = 4
SEGMENTS = 96
TEMPORAL_STEPS = 32


def path_data(temporal_factor=1):
    def point(theta):
        r = RADIUS + AMPLITUDE * temporal_factor * cos(CRESTS * theta)
        dr = -CRESTS * AMPLITUDE * temporal_factor * sin(CRESTS * theta)
        return (160 + r * cos(theta), 160 + r * sin(theta),
                dr * cos(theta) - r * sin(theta),
                dr * sin(theta) + r * cos(theta))
    step = 2 * pi / SEGMENTS
    first = point(0)
    parts = [f'M{first[0]:.3f},{first[1]:.3f}']
    for i in range(SEGMENTS):
        a, b = point(i * step), point((i + 1) * step)
        parts.append('C' + ' '.join(f'{x:.3f},{y:.3f}' for x, y in (
            (a[0] + a[2] * step / 3, a[1] + a[3] * step / 3),
            (b[0] - b[2] * step / 3, b[1] - b[3] * step / 3),
            (b[0], b[1]))))
    return ''.join(parts) + 'Z'


def svg(animated=True, temporal_factor=1):
    """La curva nera originale resta r=R+A*cos(4θ)*sin(ωt); la blu usa -sin(ωt)."""
    gradient = ('<defs><linearGradient id="logo-blue-gradient" gradientUnits="userSpaceOnUse" '
                'x1="40" y1="160" x2="280" y2="160">'
                '<stop stop-color="#83D4FA"/><stop offset=".5" stop-color="#337CD8"/>'
                '<stop offset="1" stop-color="#4140A3"/></linearGradient></defs>')

    def curve(color, factor, css, moving=False):
        stroke = '#000' if color == 'black' else 'url(#logo-blue-gradient)'
        result = (f'<path class="{css}" data-logo-wave="{color}" fill="none" stroke="{stroke}" '
                  f'stroke-width="7" stroke-linecap="round" stroke-linejoin="round" '
                  f'd="{path_data(factor)}">')
        if moving:
            sign = 1 if color == 'black' else -1
            values = ';'.join(path_data(sign * sin(2 * pi * i / TEMPORAL_STEPS))
                              for i in range(TEMPORAL_STEPS + 1))
            result += (f'<animate attributeName="d" dur="{PERIOD}s" repeatCount="indefinite" '
                       f'calcMode="linear" values="{values}"/>')
        return result + '</path>'

    if animated:
        paths = (curve('blue', 0, 'logo-moving', True) + curve('black', 0, 'logo-moving', True) +
                 curve('blue', -1, 'logo-still') + curve('black', 1, 'logo-still'))
    else:
        paths = curve('blue', -temporal_factor, 'logo-static') + curve('black', temporal_factor, 'logo-static')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="320" height="320" '
            'role="img" aria-labelledby="logo-title logo-desc">\n'
            '<title id="logo-title">Stringhe: onde circolari in opposizione di fase</title>\n'
            '<desc id="logo-desc">Due curve a quattro creste, una nera e una in gradiente blu, '
            'di uguale ampiezza e in opposizione di fase. Nodi fermi, periodo di quattro secondi, '
            'nessuna rotazione. Fondo trasparente.</desc>\n' + gradient +
            '<style>.logo-still{display:none}'
            '@media(prefers-reduced-motion:reduce){.logo-moving{display:none}.logo-still{display:inline}}'
            'svg[data-motion="manual"] .logo-moving{display:inline}'
            'svg[data-motion="manual"] .logo-still{display:none}</style>\n' + paths + '\n</svg>\n')


def export_gif(target):
    """Copia raster trasparente dello stesso SVG: 80 campioni, 20 fps, periodo 4 s.

    Richiede Playwright/Chromium e Pillow solo per la rigenerazione del file.
    Il sito non dipende da questi strumenti.
    """
    from io import BytesIO
    import shutil
    from PIL import Image
    from playwright.sync_api import sync_playwright
    frames = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
        page = browser.new_page(viewport={'width': 256, 'height': 256}, device_scale_factor=1)
        page.set_content('<style>html,body{margin:0;background:transparent}svg{display:block;width:256px;height:256px}</style>' + svg(False, 0))
        for index in range(80):
            factor = sin(2 * pi * index / 80)
            for color, sign in [('blue', -1), ('black', 1)]:
                page.locator(f'[data-logo-wave="{color}"]').evaluate('(path,d)=>path.setAttribute("d",d)', path_data(sign * factor))
            rgba = Image.open(BytesIO(page.screenshot(omit_background=True))).convert('RGBA')
            quantized = rgba.convert('RGB').quantize(colors=255)
            palette = [0, 0, 0] + quantized.getpalette()[:765]
            indexed = quantized.point(lambda value: value + 1)
            indexed.putpalette(palette)
            indexed.paste(0, mask=rgba.getchannel('A').point(lambda value: 255 if value < 128 else 0))
            indexed.info['transparency'] = 0
            frames.append(indexed)
        browser.close()
    frames[0].save(target, save_all=True, append_images=frames[1:], duration=50,
                   loop=0, transparency=0, disposal=2, optimize=False)
    with Image.open(target) as result:
        total = 0
        for index in range(result.n_frames):
            result.seek(index)
            total += result.info['duration']
        assert total == 4000 and result.size == (256, 256)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gif', action='store_true', help='Rigenera anche la copia GIF dallo stesso SVG')
    args = parser.parse_args()
    target = ROOT / 'identita/logo-materia-oscura.svg'
    target.write_text(svg(), encoding='utf-8')
    print(target.name, target.stat().st_size, 'byte')
    if args.gif:
        export_gif(target.with_suffix('.gif'))
        print('GIF trasparente: 256 × 256 px, periodo 4 secondi')
