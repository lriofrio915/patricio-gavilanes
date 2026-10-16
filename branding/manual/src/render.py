"""Exporta los logos SVG a PNG (al cuádruple) y el manual a PDF con Chrome headless.

Uso: python branding/manual/src/render.py
"""
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ASSETS = HERE.parent.parent / 'assets'
PDF = HERE.parent / 'Manual-de-marca-Dr-Patricio-Gavilanes.pdf'
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PROFILE = str(Path(tempfile.gettempdir()) / 'chrome-headless-gavilanes-brand')
BASE = [CHROME, '--headless=new', '--disable-gpu', f'--user-data-dir={PROFILE}', '--hide-scrollbars',
        '--allow-file-access-from-files', '--virtual-time-budget=6000']


def shot(url, w, h, out):
    subprocess.run(BASE + ['--force-device-scale-factor=1', f'--window-size={w},{h}',
                           '--default-background-color=00000000', f'--screenshot={out}', url],
                   check=True, capture_output=True)


png = ASSETS / 'png'
png.mkdir(exist_ok=True)
page = HERE / '_logo.html'
for svg in sorted(ASSETS.glob('*.svg')):
    txt = svg.read_text(encoding='utf-8')
    w = int(txt.split('width="')[1].split('"')[0])
    h = int(txt.split('height="')[1].split('"')[0])
    k = 1 if svg.stem == 'app-icon' else 4  # isotipos y logos a 4x; el ícono ya mide 512
    page.write_text(f'<html><body style="margin:0;background:transparent"><img src="{svg.as_uri()}" '
                    f'style="width:{w * k}px;height:{h * k}px;display:block"></body></html>', encoding='utf-8')
    shot(page.as_uri(), w * k, h * k, str(png / f'{svg.stem}.png'))
page.unlink()
print('logos png:', len(list(png.glob('*.png'))))

subprocess.run(BASE + ['--no-pdf-header-footer', f'--print-to-pdf={PDF}', (HERE / 'manual.html').as_uri()],
               check=True, capture_output=True)
print('pdf:', PDF.name, PDF.stat().st_size // 1024, 'KB')
