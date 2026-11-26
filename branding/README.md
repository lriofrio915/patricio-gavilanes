# Identidad de marca — Dr. Patricio Gavilanes

Esta carpeta es la fuente de verdad de la marca. Si algo que se publica (web, post, receta,
tarjeta, rótulo, anuncio) contradice lo que dice aquí, lo que está mal es la publicación.

**Manual completo:** [`manual/Manual-de-marca-Dr-Patricio-Gavilanes.pdf`](manual/Manual-de-marca-Dr-Patricio-Gavilanes.pdf) (17 páginas).

## Resumen

| | |
|---|---|
| Logo | El logo original del doctor, **redibujado en vectores** (v2.0, nov-2026): "Medicina Vascular" en arco, nube de puntos rojos y azules, dos figuras (roja y azul) con las piernas en alto; debajo "Dr. Patricio Gavilanes C.", "CIRUJANO VASCULAR & ENDOVASCULAR" y el lema "CUIDA TU CIRCULACIÓN". |
| Isotipo | Las dos figuras + la nube de puntos. Coordenadas tomadas de la imagen original (22 puntos). La figura azul va delante, separada por un filo del color del fondo. |
| Azul marino | `#14205F` — "Medicina", nombre, lema, fondos de marca |
| Azul circulación | `#1733A0` — figura y puntos azules, subtítulos |
| Rojo vascular | `#D11B24` — "Vascular", figura y puntos rojos, "ENDOVASCULAR", botones |
| Sobre marino | rojo vivo `#FF4B53` · azul claro `#8EA6FF` |
| Crema / Gris | `#F7F4EF` / `#64748B` |
| Tipografía | Plus Jakarta Sans ExtraBold (titulares, arco del logo) · Inter (nombre, especialidad, textos, botones) |
| Voz | Clara, cercana y responsable: se informa y se invita a consultar; nunca se promete un resultado. |

La v1.0 (octubre 2026) proponía un logo nuevo (una V de arteria y vena) que el doctor no adoptó;
toda su publicidad usa el logo original, así que la v2.0 vuelve a él.

## Assets

| Archivo | Uso |
|---|---|
| `assets/vertical-claro.svg` | **Logo principal** (el original completo), sobre blanco o crema |
| `assets/horizontal-claro.svg` | Horizontal: web, firmas, encabezados |
| `assets/horizontal-oscuro.svg` | Sobre azul noche |
| `assets/vertical-oscuro.svg` | Principal sobre azul marino |
| `assets/{horizontal,vertical,isotipo}-{blanco,negro}.svg` | Una tinta: sobre rojo, sobre fotos con velo, impresión a un color |
| `assets/isotipo-{claro,oscuro}.svg` | Solo el símbolo: sellos, marca de agua, detalles |
| `assets/app-icon.svg` | Ícono: avatar de redes y WhatsApp, favicon |
| `assets/png/` | Los mismos en PNG (4x el tamaño de la imagen original) con fondo transparente |

Todos los SVG llevan el texto en trazos: no dependen de tener la fuente instalada.

Para regenerar:

```bash
python branding/manual/src/logos.py    # SVG
python branding/manual/src/render.py   # PNG + PDF del manual (Chrome headless)
```

Las fuentes (Plus Jakarta Sans e Inter, licencia OFL) están en `manual/src/fonts/`.

## Dónde se usa en el sitio

- `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `img/icon-*.png` = `assets/app-icon`
- Logo del menú y del pie en `index.html`: símbolo `#i-logo` (misma geometría que `logos.py`)

Si cambias el logo: edita `logos.py`, regenera y actualiza el símbolo `#i-logo` y los íconos.

> **Pendiente (nov-2026):** el sitio todavía usa el logo y los colores de la v1.0 (favicon, `#i-logo`,
> imagen OG, Fraunces). Pasarlo a la v2.0 es un cambio aparte del sitio.
