"""Genera el sistema de logos del Dr. Patricio Gavilanes como SVG con el texto en trazos.

Uso: python branding/manual/src/logos.py  ->  escribe en branding/assets/
Fuentes en ./fonts (Plus Jakarta Sans e Inter, Google Fonts, licencia OFL).

Es la versión vectorial del logo que el doctor ya usa en toda su publicidad
("Medicina Vascular"): dos figuras, una roja y una azul, con las piernas en alto
(la postura que mejora el retorno venoso) bajo una nube de puntos rojos y azules,
los glóbulos de la circulación. Arriba, en arco, "Medicina Vascular"; debajo, el nombre,
"CIRUJANO VASCULAR & ENDOVASCULAR" y el lema "CUIDA TU CIRCULACIÓN".

Las coordenadas del símbolo están en los píxeles de la imagen original (242 x 187),
así que cada punto y cada figura quedan donde estaban.
"""
from math import cos, sin, radians, atan2
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = Path(__file__).parent
OUT = HERE.parent.parent / 'assets'
OUT.mkdir(parents=True, exist_ok=True)

# Paleta (muestreada de la imagen original y llevada a su tono limpio)
MARINO = '#14205F'    # "Medicina", nombre, lema
AZUL = '#1733A0'      # figura y puntos azules
ROJO = '#D11B24'      # "Vascular", figura y puntos rojos, especialidad
# Sobre fondo marino
AZUL_CLARO = '#8EA6FF'
ROJO_VIVO = '#FF4B53'
BLANCO = '#FFFFFF'
NEGRO = '#000000'

FONTS = HERE / 'fonts'
JAKARTA = instantiateVariableFont(TTFont(FONTS / 'PlusJakartaSans-VF.ttf'), {'wght': 800})
INTER_B = instantiateVariableFont(TTFont(FONTS / 'Inter-VF.ttf'), {'wght': 700, 'opsz': 14})
INTER_XB = instantiateVariableFont(TTFont(FONTS / 'Inter-VF.ttf'), {'wght': 800, 'opsz': 14})
ITALICA = 0.2  # inclinación de las letras en arco y del lema (tan del ángulo, ~11°)


def fmt(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def text_path(font, text, size, x=0.0, y=0.0, anchor='start', tracking=0.0, skew=0.0):
    """Devuelve (d, ancho) del texto en trazos, con la línea base en y. tracking en em."""
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    pen = SVGPathPen(gs, ntos=fmt)
    s = size / font['head'].unitsPerEm
    names = [cmap[ord(c)] for c in text]
    adv = [gs[n].width * s + tracking * size for n in names]
    width = sum(adv) - tracking * size
    if anchor == 'middle':
        x -= width / 2
    cx = x
    for n, a in zip(names, adv):
        gs[n].draw(TransformPen(pen, (s, 0, s * skew, -s, cx, y)))
        cx += a
    return pen.getCommands(), width


def line(font, parts, size, cx, y, tracking=0.0, skew=0.0):
    """Línea centrada en cx con tramos de distinto color: [(texto, color), ...]."""
    total = text_path(font, ''.join(t for t, _ in parts), size, tracking=tracking)[1]
    x, out = cx - total / 2, ''
    for t, col in parts:
        d, w = text_path(font, t, size, x, y, tracking=tracking, skew=skew)
        out += f'<path fill="{col}" d="{d}"/>'
        x += w + tracking * size
    return out


def fit(font, text, width, tracking=0.0):
    """Tamaño de letra para que el texto mida width."""
    return width / text_path(font, text, 1.0, tracking=tracking)[1]


def arc_text(font, parts, size, center, radius, mid_deg, tracking=0.0, skew=0.0):
    """Texto sobre un arco (por fuera del círculo), centrado en el ángulo mid_deg.
    parts = [(texto, color), ...]. Devuelve el SVG de los trazos."""
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    s = size / font['head'].unitsPerEm
    glyphs = [(cmap[ord(ch)], color) for txt, color in parts for ch in txt]
    adv = [gs[n].width * s + tracking * size for n, _ in glyphs]
    total = sum(adv) - tracking * size
    theta = radians(mid_deg) - total / radius / 2
    out, cum = {}, 0.0
    for (n, color), a in zip(glyphs, adv):
        g = a - tracking * size
        t = theta + (cum + g / 2) / radius
        phi = t + radians(90)
        px, py = center[0] + radius * cos(t), center[1] + radius * sin(t)
        c, sn = cos(phi), sin(phi)
        m = (s * c, s * sn, s * skew * c + s * sn, s * skew * sn - s * c,
             px - c * g / 2, py - sn * g / 2)
        pen = out.setdefault(color, SVGPathPen(gs, ntos=fmt))
        gs[n].draw(TransformPen(pen, m))
        cum += a
    return ''.join(f'<path fill="{col}" d="{p.getCommands()}"/>' for col, p in out.items())


# ── Isotipo: nube de puntos + dos figuras con las piernas en alto ──────────
# (x, y, radio, color 'R' o 'A') en píxeles de la imagen original
PUNTOS = [
    (94.0, 35.0, 3.6, 'R'), (108.0, 33.5, 2.3, 'A'), (116.5, 39.0, 3.9, 'R'), (139.5, 38.3, 2.1, 'A'),
    (126.8, 44.7, 4.0, 'A'), (146.5, 47.0, 3.0, 'A'), (157.0, 50.5, 2.1, 'R'), (86.5, 49.0, 3.5, 'R'),
    (97.8, 51.5, 2.3, 'A'), (79.0, 59.0, 3.6, 'R'), (112.5, 60.0, 4.7, 'R'), (122.5, 62.0, 3.1, 'R'),
    (136.5, 59.5, 2.6, 'A'), (146.5, 65.5, 3.1, 'R'), (65.0, 70.0, 3.5, 'A'), (94.5, 72.0, 5.0, 'R'),
    (130.0, 78.5, 2.7, 'A'), (142.5, 78.5, 3.1, 'R'), (157.5, 78.5, 3.1, 'R'), (84.0, 81.0, 4.3, 'A'),
    (75.0, 93.0, 4.4, 'A'), (93.5, 97.5, 6.0, 'A'),
]


def circle_d(x, y, r):
    return (f'M{fmt(x - r)} {fmt(y)}a{fmt(r)} {fmt(r)} 0 1 0 {fmt(2 * r)} 0'
            f'a{fmt(r)} {fmt(r)} 0 1 0 {fmt(-2 * r)} 0Z')


def limb(p0, p1, w0, w1):
    """Trazo que se afina de w0 a w1 (anchos totales) con extremos redondeados."""
    (x0, y0), (x1, y1) = p0, p1
    a = atan2(y1 - y0, x1 - x0)
    nx, ny = -sin(a), cos(a)
    r0, r1 = w0 / 2, w1 / 2
    pts = [(x0 + nx * r0, y0 + ny * r0), (x1 + nx * r1, y1 + ny * r1),
           (x1 - nx * r1, y1 - ny * r1), (x0 - nx * r0, y0 - ny * r0)]
    return 'M' + ' L'.join(f'{fmt(x)} {fmt(y)}' for x, y in pts) + 'Z' + circle_d(x0, y0, r0) + circle_d(x1, y1, r1)


# Figura roja: cadera abajo, piernas abiertas en V hacia arriba, brazo de apoyo y mano al suelo
CADERA_R = (106.0, 100.0)
FIGURA_ROJA = [
    limb(CADERA_R, (95.6, 79.6), 8.0, 3.6),
    limb(CADERA_R, (116.6, 78.6), 6.8, 3.4),
    limb(CADERA_R, (105.6, 117.6), 7.4, 4.0),
    limb((105.8, 118.4), (117.0, 120.0), 3.2, 1.6),
]
# Figura azul: delante de la roja, un brazo extendido a la derecha y la cabeza junto al suelo
CADERA_A = (116.4, 94.0)
FIGURA_AZUL = [
    limb(CADERA_A, (102.6, 80.2), 7.2, 3.4),
    limb(CADERA_A, (123.2, 73.4), 7.0, 3.4),
    limb((117.4, 98.5), (137.4, 89.6), 5.2, 2.6),
    limb(CADERA_A, (117.6, 115.6), 7.6, 4.0),
    limb((117.6, 116.4), (125.0, 116.4), 2.6, 1.6),
    circle_d(129.4, 112.2, 4.7),
]


def simbolo(rojo, azul, borde=None):
    """Grupo SVG del isotipo en coordenadas originales. borde: color del fondo, que separa
    la figura azul de la roja para que se lean como dos figuras (None en una sola tinta)."""
    col = {'R': rojo, 'A': azul}
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col[c]}"/>' for x, y, r, c in PUNTOS)
    roja = f'<path fill="{rojo}" d="{"".join(FIGURA_ROJA)}"/>'
    azul_d = ''.join(FIGURA_AZUL)
    sep = (f'<path fill="{borde}" stroke="{borde}" stroke-width="1.2" stroke-linejoin="round" d="{azul_d}"/>'
           if borde else '')
    return f'{dots}{roja}{sep}<path fill="{azul}" d="{azul_d}"/>'


# Caja del isotipo (coordenadas originales)
ISO_X, ISO_Y, ISO_W, ISO_H = 58.0, 28.0, 106.0, 96.0
K = 4  # el original mide ~190 px de ancho; los SVG salen a 4x


def svg(w, h, body, label='Dr. Patricio Gavilanes · Medicina Vascular'):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{fmt(w)}" height="{fmt(h)}" '
            f'viewBox="0 0 {fmt(w)} {fmt(h)}" role="img" aria-label="{label}">{body}</svg>\n')


def colocar(body, ox, oy, k):
    """Lleva un grupo en coordenadas originales a (ox, oy) con escala k."""
    return f'<g transform="translate({fmt(ox)} {fmt(oy)}) scale({fmt(k)})">{body}</g>'


NOMBRE = 'Dr. Patricio Gavilanes C.'
ESPECIALIDAD = 'CIRUJANO VASCULAR & ENDOVASCULAR'
LEMA = '“CUIDA TU CIRCULACIÓN”'

# ── Logo principal (vertical): como el original ────────────────────────────
# Medidas tomadas de la imagen original: arco con centro (112, 106) y radio 86 que va
# de -149° a -35°; nombre, especialidad y lema centrados en x = 113.
ARCO_C, ARCO_R, ARCO_MID, ARCO_SPAN = (112.0, 106.0), 86.0, -92.0, 114.0
CX = 113.0
V_X0, V_Y0, V_W, V_H = 6.0, 2.0, 214.0, 174.0
ESP_A, ESP_B = 'CIRUJANO VASCULAR & ', 'ENDOVASCULAR'


def vertical(marino, azul, rojo, borde):
    from math import pi
    arco_txt = 'Medicina Vascular'
    size = fit(JAKARTA, arco_txt, ARCO_R * ARCO_SPAN * pi / 180, tracking=0.04)
    arco = arc_text(JAKARTA, [('Medicina ', marino), ('Vascular', rojo)], size,
                    ARCO_C, ARCO_R, ARCO_MID, tracking=0.04, skew=ITALICA)
    n = line(INTER_B, [(NOMBRE, marino)], fit(INTER_B, NOMBRE, 162), CX, 133.0)
    e = line(INTER_XB, [(ESP_A, marino), (ESP_B, rojo)], fit(INTER_XB, ESPECIALIDAD, 203, 0.01), CX, 151.6, tracking=0.01)
    lema = line(INTER_XB, [(LEMA, marino)], fit(INTER_XB, LEMA, 125, 0.02), CX, 170.4, tracking=0.02, skew=ITALICA)
    body = arco + simbolo(rojo, azul, borde) + n + e + lema
    return svg(V_W * K, V_H * K, colocar(body, -V_X0 * K, -V_Y0 * K, K))


# ── Horizontal: isotipo a la izquierda, textos a la derecha ─────────────────
def horizontal(marino, azul, rojo, borde):
    tx = ISO_W + 12
    n, nw = text_path(INTER_B, NOMBRE, 21, tx, 41)
    _, ew = text_path(INTER_XB, ESPECIALIDAD, 12.2, tracking=0.01)
    e = line(INTER_XB, [(ESP_A, marino), (ESP_B, rojo)], 12.2, tx + 1 + ew / 2, 61, tracking=0.01)
    lema, lw = text_path(INTER_XB, LEMA, 11.0, tx + 1, 80, tracking=0.03, skew=ITALICA)
    w, h = tx + max(nw, ew, lw) + 4, ISO_H
    body = (colocar(simbolo(rojo, azul, borde), -ISO_X, -ISO_Y, 1) +
            f'<path fill="{marino}" d="{n}"/>{e}<path fill="{marino}" d="{lema}"/>')
    return svg(w * K, h * K, f'<g transform="scale({K})">{body}</g>')


def isotipo(azul, rojo, borde):
    return svg(ISO_W * K, ISO_H * K, colocar(simbolo(rojo, azul, borde), -ISO_X * K, -ISO_Y * K, K))


VERSIONES = {
    # nombre: (marino, azul, rojo, color del fondo para separar las figuras)
    'claro': (MARINO, AZUL, ROJO, BLANCO),
    'oscuro': (BLANCO, AZUL_CLARO, ROJO_VIVO, MARINO),
    'blanco': (BLANCO, BLANCO, BLANCO, None),
    'negro': (NEGRO, NEGRO, NEGRO, None),
}

for nombre, (m, a, r, b) in VERSIONES.items():
    (OUT / f'vertical-{nombre}.svg').write_text(vertical(m, a, r, b), encoding='utf-8')
    (OUT / f'horizontal-{nombre}.svg').write_text(horizontal(m, a, r, b), encoding='utf-8')
    (OUT / f'isotipo-{nombre}.svg').write_text(isotipo(a, r, b), encoding='utf-8')

# Ícono / avatar / favicon: el isotipo sobre blanco, en un cuadrado redondeado
k = 400 / max(ISO_W, ISO_H)
(OUT / 'app-icon.svg').write_text(
    svg(512, 512, '<rect width="512" height="512" rx="116" fill="#FFFFFF"/>' +
        colocar(simbolo(ROJO, AZUL, BLANCO), 256 - (ISO_X + ISO_W / 2) * k, 256 - (ISO_Y + ISO_H / 2) * k, k)),
    encoding='utf-8')

print('logos:', len(list(OUT.glob('*.svg'))))
