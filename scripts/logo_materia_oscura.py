"""Genera il logo definitivo: onda sinusoidale stazionaria con quattro creste."""
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


def svg():
    # r(theta,t) = R + A*cos(4*theta)*sin(2*pi*t/T).
    # Otto nodi angolari fissi; i ventri cambiano segno senza rotazione.
    circle = path_data(0)
    values = ';'.join(path_data(sin(2 * pi * i / TEMPORAL_STEPS))
                      for i in range(TEMPORAL_STEPS + 1))
    stroke = 'fill="none" stroke="#000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="320" height="320" '
            'role="img" aria-labelledby="logo-title logo-desc">\n'
            '<title id="logo-title">Materia Oscura: Onda stazionaria</title>\n'
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
    target = ROOT / 'identita/logo-materia-oscura.svg'
    target.write_text(svg(), encoding='utf-8')
    print(target.name, target.stat().st_size, 'byte')
