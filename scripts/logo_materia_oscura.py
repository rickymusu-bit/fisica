"""Genera il logo geometrico autorizzato: un solo contorno chiuso in oscillazione."""
from math import cos, sin, pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEGMENTS = 48
RADIUS = 88
AMPLITUDE = .54
DURATION = 8


def contour(amplitude):
    """Curva polare, con quattro massimi; ampiezza negativa = diagonali."""
    def point(theta):
        radius = RADIUS * (1 + amplitude * cos(4 * theta))
        derivative = -4 * RADIUS * amplitude * sin(4 * theta)
        return (160 + radius * cos(theta), 160 + radius * sin(theta),
                derivative * cos(theta) - radius * sin(theta),
                derivative * sin(theta) + radius * cos(theta))
    step = 2 * pi / SEGMENTS
    start = point(0)
    chunks = [f'M{start[0]:.3f},{start[1]:.3f}']
    for n in range(SEGMENTS):
        p, q = point(n * step), point((n + 1) * step)
        chunks.append('C' + ' '.join(f'{x:.3f},{y:.3f}' for x, y in (
            (p[0] + p[2] * step / 3, p[1] + p[3] * step / 3),
            (q[0] - q[2] * step / 3, q[1] - q[3] * step / 3),
            (q[0], q[1]))))
    return ''.join(chunks) + 'Z'


def svg(animated=True):
    circle, cardinal, diagonal = [contour(a) for a in (0, AMPLITUDE, -AMPLITUDE)]
    common = 'fill="none" stroke="#000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    intro = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" '
             'width="320" height="320" role="img" aria-labelledby="logo-title logo-desc">\n'
             '<title id="logo-title">Materia Oscura</title>\n'
             '<desc id="logo-desc">Una sola stringa chiusa nera su fondo trasparente. '
             'Cerchio, quattro lobi orizzontali e verticali, cerchio, quattro lobi diagonali, cerchio.</desc>\n')
    if not animated:
        intro = intro.replace('Cerchio, quattro lobi orizzontali e verticali, cerchio, quattro lobi diagonali, cerchio.', 'Quattro lobi orizzontali e verticali, in una configurazione fissa.')
        return intro + f'<path {common} d="{cardinal}"/>\n</svg>\n'
    # Solo una delle due alternative è visibile: l'altra serve per il movimento ridotto.
    style = ('<style>.logo-still{display:none}'
             '@media(prefers-reduced-motion:reduce){.logo-moving{display:none}.logo-still{display:inline}}'
             'svg[data-motion="manual"] .logo-moving{display:inline}'
             'svg[data-motion="manual"] .logo-still{display:none}</style>\n')
    values = ';'.join([circle, cardinal, circle, diagonal, circle])
    return (intro + style + f'<path class="logo-moving" {common} d="{circle}">\n'
            f'<animate attributeName="d" dur="{DURATION}s" repeatCount="indefinite" '
            'calcMode="spline" keyTimes="0;0.25;0.5;0.75;1" '
            'keySplines=".42 0 .58 1;.42 0 .58 1;.42 0 .58 1;.42 0 .58 1" '
            f'values="{values}"/>\n</path>\n'
            f'<path class="logo-still" {common} d="{circle}"/>\n</svg>\n')


if __name__ == '__main__':
    target = ROOT / 'identita'
    target.mkdir(exist_ok=True)
    for filename, animated in [('logo-materia-oscura.svg', True),
                               ('logo-materia-oscura-statico.svg', False)]:
        path = target / filename
        path.write_text(svg(animated), encoding='utf-8')
        print(filename, path.stat().st_size, 'byte')
