"""Logo: onda sinusoidale stazionaria su una curva chiusa, con quattro creste."""
from math import sin, pi
from pathlib import Path
from logo_onda_progressiva import path_data, PERIOD

ROOT = Path(__file__).resolve().parents[1]
TEMPORAL_STEPS = 32


def svg():
    # r(theta,t) = R + A*cos(4*theta)*sin(2*pi*t/T).
    # Otto nodi angolari fissi; i ventri cambiano segno senza rotazione.
    circle = path_data(0)
    values = ';'.join(path_data(sin(2 * pi * i / TEMPORAL_STEPS))
                      for i in range(TEMPORAL_STEPS + 1))
    stroke = 'fill="none" stroke="#000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="320" height="320" '
            'role="img" aria-labelledby="logo-title logo-desc">\n'
            '<title id="logo-title">Materia Oscura · Onda stazionaria</title>\n'
            '<desc id="logo-desc">Onda sinusoidale stazionaria su una curva chiusa: nodi fermi '
            'e ventri oscillanti, con quattro creste. Nessuna rotazione. Tratto nero su fondo trasparente.</desc>\n'
            '<style>.logo-still{display:none}'
            '@media(prefers-reduced-motion:reduce){.logo-moving{display:none}.logo-still{display:inline}}'
            'svg[data-motion="manual"] .logo-moving{display:inline}'
            'svg[data-motion="manual"] .logo-still{display:none}</style>\n'
            f'<path class="logo-moving" {stroke} d="{circle}">\n'
            f'<animate attributeName="d" dur="{PERIOD}s" repeatCount="indefinite" '
            f'calcMode="linear" values="{values}"/>\n</path>\n'
            f'<path class="logo-still" {stroke} d="{circle}"/>\n</svg>\n')


if __name__ == '__main__':
    target = ROOT / 'identita/logo-materia-oscura-onda-stazionaria.svg'
    target.write_text(svg(), encoding='utf-8')
    print(target.name, target.stat().st_size, 'byte')
