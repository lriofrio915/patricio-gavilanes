"""Genera /tratamientos/<slug>.html a partir de index.html (estilos, iconos, cabecera, pie y
script) y de scripts/contenido_tratamientos.py. También actualiza sitemap.xml.

Uso (desde la raíz del repo):  python scripts/generar_tratamientos.py
index.html sigue siendo la fuente única del diseño: si cambia, basta con volver a ejecutar.
"""
import html
import json
import pathlib
import re
import sys
from datetime import date
from urllib.parse import quote

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / 'scripts'))
from contenido_tratamientos import TRATAMIENTOS, WA  # noqa: E402

SITIO = 'https://drpatriciogavilanes.com'
HOY = date.today().isoformat()
e = html.escape

index = (RAIZ / 'index.html').read_text(encoding='utf-8')


def entre(inicio, fin, texto=index):
    i = texto.index(inicio)
    j = texto.index(fin, i) + len(fin)
    return texto[i:j]


ESTILO = entre('<style>', '</style>')
SPRITE = entre('<!-- Iconos (sprite SVG) -->', '</svg>\n\n')
TOPBAR = entre('<div class="topbar">', '</header>')
PIE = entre('<footer>', '</footer>')
FLOTANTE = entre('<a class="wa-float"', '</a>')
SCRIPT = index[index.rindex('<script>'):index.rindex('</script>') + len('</script>')]

# En subpáginas, las anclas de la portada apuntan a "/#seccion".
TOPBAR = TOPBAR.replace('href="#inicio"', 'href="/"')
TOPBAR = re.sub(r'href="#(doctor|tratamientos|sintomas|consultorios|preguntas)"', r'href="/#\1"', TOPBAR)
PIE = re.sub(r'href="#(tratamientos|consultorios)"', r'href="/#\1"', PIE)

EXTRA = """
    <style>
        .crumbs { font-size: 14px; color: var(--muted); padding-top: 28px; }
        .crumbs a { color: var(--blue); }
        .crumbs a:hover { text-decoration: underline; }
        .page-hero { padding: 24px 0 48px; background: var(--cream); }
        .page-hero h1 { font-size: clamp(30px, 4.2vw, 46px); margin: 12px 0 16px; max-width: 900px; }
        .page-hero .lead { font-size: 19px; max-width: 820px; }
        .page-hero .hero-cta { margin-top: 26px; display: flex; flex-wrap: wrap; gap: 12px; }
        .prose { max-width: 820px; }
        .prose h2 { font-size: clamp(24px, 3vw, 32px); margin: 44px 0 14px; }
        .prose > :first-child { margin-top: 0; }
        .prose p + p { margin-top: 14px; }
        .prose .alert { margin-top: 28px; }
        .prose .chips { margin-top: 8px; }
        .otros { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }
        .otros a { border: 1px solid var(--line); border-radius: 999px; padding: 8px 16px; font-size: 15px; background: #fff; }
        .otros a:hover { border-color: var(--blue); color: var(--blue); }
    </style>"""


def wa(texto):
    return WA + quote(texto, safe='')


def pagina(t):
    url = f'{SITIO}/tratamientos/{t["slug"]}'
    enlace_wa = wa(t['wa'])
    secciones = ''.join(
        f'<h2>{e(titulo)}</h2>' + ''.join(f'<p>{e(p)}</p>' for p in parrafos)
        for titulo, parrafos in t['secciones']
    )
    alerta = (
        f'<div class="alert" role="note"><svg class="i"><use href="#i-alert"/></svg><span>{e(t["alerta"])}</span></div>'
        if t.get('alerta') else ''
    )
    sintomas = (
        '<h2>¿Cuándo consultar?</h2><div class="chips">'
        + ''.join(f'<div class="chip"><svg class="i"><use href="#i-check"/></svg> {e(s)}</div>' for s in t['sintomas'])
        + '</div>'
        if t['sintomas'] else ''
    )
    preguntas = ''.join(
        f'<details><summary>{e(q)} <svg class="i"><use href="#i-chev"/></svg></summary><p>{e(r)}</p></details>'
        for q, r in t['preguntas']
    )
    otros = ''.join(
        f'<a href="/tratamientos/{o["slug"]}">{e(o["nombre"])}</a>' for o in TRATAMIENTOS if o['slug'] != t['slug']
    )

    tema = {'@type': t['tipo'], 'name': t['nombre']}
    if t.get('condicion'):
        tema = {'@type': 'MedicalCondition', 'name': t['condicion'],
                'possibleTreatment': {'@type': t['tipo'], 'name': t['nombre']}} if t['tipo'] != 'MedicalTest' else tema
    esquema = {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'MedicalWebPage',
                '@id': f'{url}#webpage',
                'url': url,
                'name': t['titulo'],
                'description': t['descripcion'],
                'inLanguage': 'es-EC',
                'isPartOf': {'@id': f'{SITIO}/#website'},
                'about': tema,
                'author': {'@id': f'{SITIO}/#doctor'},
                'reviewedBy': {'@id': f'{SITIO}/#doctor'},
                'lastReviewed': HOY,
                'specialty': 'https://schema.org/Vascular',
                'breadcrumb': {'@id': f'{url}#breadcrumb'},
            },
            {
                '@type': 'BreadcrumbList',
                '@id': f'{url}#breadcrumb',
                'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': f'{SITIO}/'},
                    {'@type': 'ListItem', 'position': 2, 'name': 'Tratamientos', 'item': f'{SITIO}/#tratamientos'},
                    {'@type': 'ListItem', 'position': 3, 'name': t['nombre'], 'item': url},
                ],
            },
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="es-EC">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Generado por scripts/generar_tratamientos.py: editar el contenido en scripts/contenido_tratamientos.py -->
    <title>{e(t['titulo'])}</title>
    <meta name="description" content="{e(t['descripcion'])}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="author" content="Dr. Patricio Gavilanes">
    <link rel="canonical" href="{url}">
    <meta name="theme-color" content="#0B1F3A">
    <meta property="fb:app_id" content="1133083328336580">
    <meta property="og:type" content="article">
    <meta property="og:locale" content="es_EC">
    <meta property="og:site_name" content="Dr. Patricio Gavilanes — Cirugía Vascular">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{e(t['titulo'])}">
    <meta property="og:description" content="{e(t['descripcion'])}">
    <meta property="og:image" content="{SITIO}/img/og-dr-patricio-gavilanes.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{e(t['titulo'])}">
    <meta name="twitter:description" content="{e(t['descripcion'])}">
    <meta name="twitter:image" content="{SITIO}/img/og-dr-patricio-gavilanes.jpg">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script type="application/ld+json">{json.dumps(esquema, ensure_ascii=False).replace('<', '\\u003c')}</script>
    {ESTILO}{EXTRA}
</head>

<body>
    {SPRITE}
    <a class="skip" href="#contenido">Saltar al contenido</a>

    {TOPBAR}

    <main id="contenido">
        <section class="page-hero">
            <div class="container">
                <nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › <a href="/#tratamientos">Tratamientos</a> › {e(t['nombre'])}</nav>
                <h1>{e(t['h1'])}</h1>
                <p class="lead">{e(t['intro'])}</p>
                <div class="hero-cta">
                    <a class="btn btn-wa" href="{enlace_wa}" target="_blank" rel="noopener"><svg class="i"><use href="#i-chat"/></svg> Consultar por WhatsApp</a>
                    <a class="btn btn-outline" href="/#consultorios"><svg class="i"><use href="#i-pin"/></svg> Ver consultorios</a>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container prose">
                {alerta}
                {secciones}
                {sintomas}
                <h2>Valoración en Quito y Cumbayá</h2>
                <p>El Dr. Patricio Gavilanes, especialista en angiología, cirugía vascular y endovascular, atiende con cita previa en el
                    Centro Médico Metropolitano (Quito, Piso 2, Consultorio 210) y en el Hospital de los Valles (Cumbayá, Edificio de
                    Especialidades, Consultorio 334). Cada caso empieza con una valoración completa para decidir el tratamiento adecuado.</p>
                <h2>Preguntas frecuentes</h2>
                <div class="faq">{preguntas}</div>
                <h2>Otros tratamientos</h2>
                <div class="otros">{otros}</div>
            </div>
        </section>

        <section class="section" style="padding-top:0;padding-bottom:0">
            <div class="container">
                <div class="cta">
                    <div>
                        <h2>Agende su valoración</h2>
                        <p>Escríbanos por WhatsApp e indique la sede de su preferencia: Quito o Cumbayá.</p>
                    </div>
                    <div class="cta-actions">
                        <a class="btn btn-wa" href="{enlace_wa}" target="_blank" rel="noopener"><svg class="i"><use href="#i-chat"/></svg> Escribir por WhatsApp</a>
                        <a class="btn btn-ghost" href="tel:+593998340502"><svg class="i"><use href="#i-phone"/></svg> Llamar al 099 834 0502</a>
                    </div>
                </div>
            </div>
        </section>
    </main>

    {PIE}

    {FLOTANTE}

    {SCRIPT}
</body>

</html>
"""


def sitemap():
    actual = (RAIZ / 'sitemap.xml').read_text(encoding='utf-8')
    inicio = actual[:actual.index('</urlset>')]
    inicio = re.sub(r'\s*<url>\s*<loc>https://drpatriciogavilanes\.com/tratamientos/.*?</url>', '', inicio, flags=re.S)
    urls = ''.join(
        f"""  <url>
    <loc>{SITIO}/tratamientos/{t['slug']}</loc>
    <lastmod>{HOY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
""" for t in TRATAMIENTOS)
    return inicio.rstrip() + '\n' + urls + '</urlset>\n'


if __name__ == '__main__':
    carpeta = RAIZ / 'tratamientos'
    carpeta.mkdir(exist_ok=True)
    for t in TRATAMIENTOS:
        assert len(t['titulo']) <= 60, (t['slug'], len(t['titulo']))
        assert len(t['descripcion']) <= 160, (t['slug'], len(t['descripcion']))
        (carpeta / f'{t["slug"]}.html').write_text(pagina(t), encoding='utf-8', newline='\n')
    (RAIZ / 'sitemap.xml').write_text(sitemap(), encoding='utf-8', newline='\n')
    print(f'{len(TRATAMIENTOS)} páginas en tratamientos/ y sitemap.xml actualizado')
