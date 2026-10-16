"""Genera el sistema de logos del Dr. Patricio Gavilanes como SVG con el texto en trazos.

Uso: python branding/manual/src/logos.py  ->  escribe en branding/assets/
Fuentes en ./fonts (Fraunces e Inter, Google Fonts, licencia OFL).

El isotipo es una V formada por dos vasos sanguíneos que se ramifican: la arteria en
rojo (izquierda) y la vena en azul (derecha). Se unen abajo, como la circulación que
el doctor cuida. La V es también la inicial de "Vascular".
Todo vive en una caja de 100 x 100.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = Path(__file__).parent
OUT = HERE.parent.parent / 'assets'
OUT.mkdir(parents=True, exist_ok=True)

# Paleta
NOCHE = '#0B1F3A'     # azul noche: nombre, fondos oscuros
ROJO = '#C81E34'      # rojo arteria: rama izquierda, acentos
ROJO_VIVO = '#E23A50' # rojo arteria sobre fondo oscuro
AZUL = '#1D4E89'      # azul vena: rama derecha
GRIS = '#64748B'      # descriptor sobre fondo claro
NIEBLA = '#AFBED6'    # descriptor sobre fondo oscuro
BLANCO = '#FFFFFF'
NEGRO = '#000000'

FR = instantiateVariableFont(TTFont(HERE / 'fonts' / 'Fraunces-VF.ttf'),
                             {'wght': 600, 'opsz': 72, 'SOFT': 0, 'WONK': 0})
INTER = instantiateVariableFont(TTFont(HERE / 'fonts' / 'Inter-VF.ttf'), {'wght': 600, 'opsz': 14})


def text_path(font, text, size, x=0.0, y=0.0, anchor='start', tracking=0.0):
    """Devuelve (d, ancho) del texto en trazos, con la línea base en y. tracking en em."""
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    s = size / font['head'].unitsPerEm
    names = [cmap[ord(c)] for c in text]
    adv = [gs[n].width * s + tracking * size for n in names]
    width = sum(adv) - tracking * size
    if anchor == 'middle':
        x -= width / 2
    pen = SVGPathPen(gs, ntos=lambda v: f'{v:.2f}'.rstrip('0').rstrip('.'))
    cx = x
    for n, a in zip(names, adv):
        gs[n].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        cx += a
    return pen.getCommands(), width


# ── Isotipo (caja 100 x 100) ────────────────────────────────────────────────
ARTERIA = ('M24 12C24 44 38 64 50 88', 'M28 48C20 44 14 36 12 26')
VENA = ('M76 12C76 44 62 64 50 88', 'M72 48C80 44 86 36 88 26')
TRONCO, RAMA = 9, 6


def mark(art, ven, ox=0.0, oy=0.0, k=1.0):
    def vaso(d, color):
        return ''.join(f'<path d="{p}" fill="none" stroke="{color}" stroke-width="{w}" '
                       f'stroke-linecap="round"/>' for p, w in zip(d, (TRONCO, RAMA)))
    # La vena se dibuja primero para que la arteria quede delante en la unión.
    return f'<g transform="translate({ox} {oy}) scale({k})">{vaso(VENA, ven)}{vaso(ARTERIA, art)}</g>'


def svg(w, h, body, label='Dr. Patricio Gavilanes'):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{label}">{body}</svg>\n')


NOMBRE = 'Dr. Patricio Gavilanes'
DESCRIPTOR = 'CIRUGÍA VASCULAR Y ENDOVASCULAR'

# ── Horizontal: isotipo + nombre + descriptor ───────────────────────────────
H_ISO = 76
nombre_d, nombre_w = text_path(FR, NOMBRE, 40, 0, 0)
desc_d, desc_w = text_path(INTER, DESCRIPTOR, 11.4, 0, 0, tracking=0.16)
TX = H_ISO + 18
H_W = round(TX + max(nombre_w, desc_w) + 4)
H_H = 84


def horizontal(art, ven, nombre, desc):
    n, _ = text_path(FR, NOMBRE, 40, TX, 46)
    d, _ = text_path(INTER, DESCRIPTOR, 11.4, TX + 1.5, 68, tracking=0.16)
    return svg(H_W, H_H, mark(art, ven, 0, 4, H_ISO / 100) +
               f'<path fill="{nombre}" d="{n}"/><path fill="{desc}" d="{d}"/>')


# ── Vertical: isotipo arriba, nombre y descriptor centrados ─────────────────
V_W = round(max(nombre_w, desc_w) + 16)
V_H = 222


def vertical(art, ven, nombre, desc):
    n, _ = text_path(FR, NOMBRE, 40, V_W / 2, 168, 'middle')
    d, _ = text_path(INTER, DESCRIPTOR, 11.4, V_W / 2, 196, 'middle', tracking=0.16)
    return svg(V_W, V_H, mark(art, ven, V_W / 2 - 60, 6, 1.2) +
               f'<path fill="{nombre}" d="{n}"/><path fill="{desc}" d="{d}"/>')


VERSIONES = {
    # nombre: (arteria, vena, nombre, descriptor)
    'claro': (ROJO, AZUL, NOCHE, GRIS),
    'oscuro': (ROJO_VIVO, BLANCO, BLANCO, NIEBLA),
    'blanco': (BLANCO, BLANCO, BLANCO, BLANCO),
    'negro': (NEGRO, NEGRO, NEGRO, NEGRO),
}

for nombre, (a, v, n, d) in VERSIONES.items():
    (OUT / f'horizontal-{nombre}.svg').write_text(horizontal(a, v, n, d), encoding='utf-8')
    (OUT / f'vertical-{nombre}.svg').write_text(vertical(a, v, n, d), encoding='utf-8')
    (OUT / f'isotipo-{nombre}.svg').write_text(svg(100, 100, mark(a, v)), encoding='utf-8')

# Ícono de app / avatar / favicon: caja azul noche, vasos en rojo vivo y blanco
(OUT / 'app-icon.svg').write_text(
    svg(512, 512, f'<rect width="512" height="512" rx="116" fill="{NOCHE}"/>' +
        mark(ROJO_VIVO, BLANCO, 76, 72, 3.6)), encoding='utf-8')

print('logos:', len(list(OUT.glob('*.svg'))), '| horizontal', H_W, 'x', H_H, '| vertical', V_W, 'x', V_H)
