# Identidad de marca — Dr. Patricio Gavilanes

Esta carpeta es la fuente de verdad de la marca. Si algo que se publica (web, post, receta,
tarjeta, rótulo, anuncio) contradice lo que dice aquí, lo que está mal es la publicación.

**Manual completo:** [`manual/Manual-de-marca-Dr-Patricio-Gavilanes.pdf`](manual/Manual-de-marca-Dr-Patricio-Gavilanes.pdf) (17 páginas).

## Resumen

| | |
|---|---|
| Nombre | **Dr. Patricio Gavilanes** · descriptor: **Cirugía Vascular y Endovascular** |
| Isotipo | Una **V** formada por dos vasos que se ramifican: la **arteria** en rojo (izquierda) y la **vena** en azul (derecha), unidos abajo. La arteria va por delante en la unión. |
| Logotipo | Isotipo + "Dr. Patricio Gavilanes" (Fraunces SemiBold, azul noche) + descriptor (Inter SemiBold, mayúsculas, +16 % de espaciado, gris). |
| Azul noche | `#0B1F3A` — nombre, fondos de marca |
| Rojo arteria | `#C81E34` — arteria del isotipo, botones y acentos |
| Azul vena | `#1D4E89` — vena del isotipo, subtítulos |
| Rojo vivo | `#E23A50` — el rojo sobre fondo oscuro |
| Crema / Arena | `#F7F4EF` / `#EFE9E1` — fondos suaves y bordes |
| Tipografía | Fraunces (titulares, nombre, citas) · Inter (texto, botones, etiquetas) |
| Voz | Clara, cercana y responsable: se informa y se invita a consultar; nunca se promete un resultado. |

## Assets

| Archivo | Uso |
|---|---|
| `assets/horizontal-claro.svg` | Logo principal, sobre blanco o crema |
| `assets/horizontal-oscuro.svg` | Sobre azul noche |
| `assets/vertical-{claro,oscuro}.svg` | Portadas, tarjetas, formatos cuadrados |
| `assets/{horizontal,vertical,isotipo}-{blanco,negro}.svg` | Una tinta: sobre rojo, sobre fotos con velo, impresión a un color |
| `assets/isotipo-{claro,oscuro}.svg` | Solo el símbolo: sellos, marca de agua, detalles |
| `assets/app-icon.svg` | Ícono: avatar de redes y WhatsApp, favicon |
| `assets/png/` | Los mismos en PNG de alta resolución (4x) con fondo transparente |

Todos los SVG llevan el texto en trazos: no dependen de tener la fuente instalada.

Para regenerar:

```bash
python branding/manual/src/logos.py    # SVG
python branding/manual/src/render.py   # PNG + PDF del manual (Chrome headless)
```

Las fuentes (Fraunces e Inter, licencia OFL) están en `manual/src/fonts/`.

## Dónde se usa en el sitio

- `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `img/icon-*.png` = `assets/app-icon`
- Logo del menú y del pie en `index.html`: símbolo `#i-logo` (misma geometría que `logos.py`)

Si cambias el logo: edita `logos.py`, regenera y actualiza el símbolo `#i-logo` y los íconos.
