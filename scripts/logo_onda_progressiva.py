"""Logo: quattro creste sinusoidali che si propagano lungo una curva chiusa."""
from math import cos, sin, pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RADIUS = 104
AMPLITUDE = 10
CRESTS = 4
PERIOD = 4
SEGMENTS = 96


def path_data():
    def point(theta):
        r = RADIUS + AMPLITUDE * cos(CRESTS * theta)
        dr = -CRESTS * AMPLITUDE * sin(CRESTS * theta)
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
    d = path_data()
    stroke = 'fill="none" stroke="#000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    # r(theta,t)=R+A*cos(4*theta-2*pi*t/T): la traslazione di fase
    # equivale esattamente a ruotare il profilo di 90 gradi in un periodo T.
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="320" height="320" '
            'role="img" aria-labelledby="logo-title logo-desc">\n'
            '<title id="logo-title">Materia Oscura · Onda progressiva</title>\n'
            '<desc id="logo-desc">Una sinusoide con quattro creste che viaggiano in senso orario lungo '
            'una curva chiusa. Tratto nero su fondo trasparente, ampiezza costante.</desc>\n'
            '<style>.logo-still{display:none}'
            '@media(prefers-reduced-motion:reduce){.logo-moving{display:none}.logo-still{display:inline}}'
            'svg[data-motion="manual"] .logo-moving{display:inline}'
            'svg[data-motion="manual"] .logo-still{display:none}</style>\n'
            f'<path class="logo-moving" {stroke} d="{d}">\n'
            f'<animateTransform attributeName="transform" type="rotate" from="0 160 160" to="90 160 160" '
            f'dur="{PERIOD}s" repeatCount="indefinite" calcMode="linear"/>\n</path>\n'
            f'<path class="logo-still" {stroke} d="{d}"/>\n</svg>\n')


if __name__ == '__main__':
    target = ROOT / 'identita/logo-materia-oscura-onda-progressiva.svg'
    target.write_text(svg(), encoding='utf-8')
    print(target.name, target.stat().st_size, 'byte')
