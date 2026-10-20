"""Verifica Chromium desktop/Android emulato e salva i confronti riproducibili.

Richiede playwright e un browser Chromium. Avvia autonomamente un server locale.
Nessun test su un dispositivo Android fisico viene dichiarato da questo script.
"""
import functools
import http.server
import json
import os
from pathlib import Path
import shutil
import threading
from playwright.sync_api import sync_playwright, Error

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
SHOTS = ROOT / 'lavorazione/sito/schermate'


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    SHOTS.mkdir(parents=True, exist_ok=True)
    # Il modello è verificato ma non diventa un articolo pubblicato.
    shutil.copyfile(ROOT / 'riferimenti/TEMA_DISPENSE.html', SITE / 'modello-dispense.html')
    handler = functools.partial(QuietHandler, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}/'
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    pages = ['index.html', 'articoli.html', 'quiz.html', 'crediti.html', 'anteprima-bordi-stringhe.html', 'modello-dispense.html'] + publication['articoli']
    checks, errors = [], []
    offline_status = 'file:// verificato'
    try:
        with sync_playwright() as playwright:
            executable = os.environ.get('CHROMIUM_PATH') or shutil.which('chromium')
            browser = playwright.chromium.launch(**({'executable_path': executable} if executable else {}), args=['--no-sandbox'])
            context = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True, device_scale_factor=1)
            context.add_init_script("Math.random=()=>Number(sessionStorage.getItem('test-random')||0)")
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            # Tutte le pagine, tutti i viewport e i due temi, con immagini caricate.
            for name in pages:
                page.goto(base + name)
                page.wait_for_function('document.fonts.status === "loaded"')
                for width in [320, 390, 768, 1024, 1440]:
                    page.set_viewport_size({'width': width, 'height': 900})
                    for theme in ['light', 'dark']:
                        page.locator('[data-theme-select]').select_option(theme)
                        assert page.evaluate('document.documentElement.dataset.theme') == theme
                        size = page.evaluate('({actual:document.documentElement.scrollWidth, viewport:innerWidth})')
                        assert size['actual'] <= size['viewport'] + 1, (name, width, theme, size)
                        checks.append([name, width, theme])
            # Controllo delle 20 scelte casuali e associazione immagine/alt/didascalia.
            covers = json.loads((ROOT / 'copertine/manifest.json').read_text())
            for i, cover in enumerate(covers):
                page.evaluate('(value)=>sessionStorage.setItem("test-random",String(value))', (i + .1) / len(covers))
                page.goto(base + 'index.html')
                assert page.locator('#random-cover').get_attribute('src') == cover['src']
                assert page.locator('#random-cover').get_attribute('alt') == cover['alt']
                assert page.locator('#cover-caption').inner_text() == cover['caption']
                assert page.locator('#random-cover').evaluate('(img)=>img.complete && img.naturalWidth>0')
            paths = page.locator('#catalogue-data').text_content()
            paths = json.loads(paths)
            for i, name in enumerate(paths):
                page.evaluate('(value)=>sessionStorage.setItem("test-random",String(value))', (i + .1) / len(paths))
                page.goto(base + 'index.html'); page.locator('#random-article').click()
                page.wait_for_url(base + name)
            page.locator('[data-theme-select]').select_option('dark')
            page.goto(base + 'articoli.html')
            assert page.locator('[data-theme-select]').input_value() == 'dark'
            page.reload()
            assert page.evaluate('document.documentElement.dataset.theme') == 'dark'
            page.locator('#article-search').fill('conduzione')
            assert page.locator('.article-card:visible').count() >= 1
            page.locator('#article-search').fill('zzzzzz')
            assert page.locator('.article-card:visible').count() == 0
            assert page.locator('#no-results').is_visible()
            page.locator('#article-search').fill('')
            page.locator('.chip').last.click()
            assert page.locator('.chip').last.get_attribute('aria-pressed') == 'true'
            page.goto(base + publication['articoli'][0])
            # Tastiera, menu indice, note, zoom, crediti e download reale.
            logo = page.locator('[data-logo-toggle]').first
            logo.focus(); old = logo.get_attribute('aria-pressed'); page.keyboard.press('Space')
            assert logo.get_attribute('aria-pressed') != old
            page.locator('.index-toggle').click()
            assert page.locator('.reader-index').get_attribute('open') is not None
            page.keyboard.press('Escape')
            assert page.locator('.reader-index').get_attribute('open') is None
            assert page.locator('.index-toggle').evaluate('(e)=>e===document.activeElement')
            if page.locator('[role=doc-noteref]').count():
                page.locator('[role=doc-noteref]').first.click()
                assert page.locator('.chapter-notes').get_attribute('open') is not None
            if page.locator('.image-zoom summary').count():
                page.locator('.image-zoom summary').first.click()
                assert page.locator('.image-zoom').first.get_attribute('open') is not None
            page.locator('[data-offline-credits]').click()
            assert page.locator('#crediti-autonomi').is_visible()
            page.keyboard.press('Escape')
            page.goto(base + publication['articoli'][0])
            with page.expect_download() as download:
                page.locator('.string-nav[download]').click()
            assert Path(download.value.path()).read_bytes() == (SITE / publication['articoli'][0]).read_bytes()
            # Cambio di sistema, reset Automatico, storage non disponibile e movimento ridotto.
            page.locator('[data-theme-select]').select_option('auto')
            page.emulate_media(color_scheme='light'); assert page.evaluate('document.documentElement.dataset.theme') == 'light'
            page.emulate_media(color_scheme='dark'); page.wait_for_function('document.documentElement.dataset.theme === "dark"')
            page.emulate_media(reduced_motion='reduce')
            page.wait_for_function('document.querySelector("[data-logo-toggle]").getAttribute("aria-pressed") === "true"')
            denied = browser.new_context()
            denied.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked')}})")
            blocked = denied.new_page(); blocked.on('pageerror', lambda error: errors.append(str(error)))
            blocked.goto(base+'index.html'); blocked.locator('[data-theme-select]').select_option('dark');blocked.reload()
            offline = denied.new_page(); offline.on('pageerror', lambda error: errors.append(str(error)))
            try:
                offline.goto((SITE / publication['articoli'][0]).as_uri())
            except Error as error:
                if 'ERR_BLOCKED_BY_ADMINISTRATOR' not in str(error):
                    raise
                offline_status = 'file:// bloccato dalla policy del browser; HTML verificato in memoria con rete bloccata'
                offline.route('**/*', lambda route: route.abort())
                offline.set_content((SITE / publication['articoli'][0]).read_text())
            offline.locator('[data-theme-select]').select_option('dark')
            if offline_status == 'file:// verificato':
                assert offline.locator('.string-nav').first.get_attribute('href').startswith('https://rickymusu-bit.github.io/fisica/')
            denied.close()
            for theme in ['light', 'dark']:
                nojs = browser.new_context(java_script_enabled=False, color_scheme=theme, viewport={'width':390,'height':844})
                plain = nojs.new_page();plain.goto(base+'index.html')
                assert plain.locator('#random-cover').get_attribute('src') == covers[0]['src']
                assert plain.locator('#random-cover').evaluate('(img)=>img.complete && img.naturalWidth>0')
                assert plain.locator('body').evaluate('(e)=>getComputedStyle(e).color') == ('rgb(32, 38, 55)' if theme == 'light' else 'rgb(240, 242, 248)')
                plain.goto(base+publication['articoli'][0])
                plain.locator('[data-offline-credits]').click()
                assert plain.locator('#crediti-autonomi').is_visible()
                nojs.close()
            # Schermate nello stesso contesto per variante e reticolo, in entrambi i temi.
            for width in [390,1440]:
                page.set_viewport_size({'width':width,'height':900})
                for theme in ['light','dark']:
                    for name, label in [('index.html','home'),('articoli.html','catalogo'), (publication['articoli'][0], 'articolo')]:
                        page.goto(base+name);page.locator('[data-theme-select]').select_option(theme)
                        page.screenshot(path=str(SHOTS/f'{label}-{width}-{theme}.png'), full_page=(label!='articolo'), animations='disabled')
                    for variant in ['A','B']:
                        page.goto(base+'anteprima-bordi-stringhe.html');page.locator('[data-theme-select]').select_option(theme)
                        page.locator('#border-variant').select_option(variant)
                        for grid in ['A', 'B']:
                            page.locator('#grid-variant').select_option(grid)
                            page.screenshot(path=str(SHOTS/f'confronto-{width}-{theme}-{variant}-reticolo-{grid}.png'), full_page=True, animations='disabled')
                        page.locator('#edge-variant').select_option('top')
                        page.locator('[data-demo-dialog]').first.click()
                        assert page.locator('#demo-dialog').is_visible()
                        page.keyboard.press('Escape')
            browser.close()
    finally:
        server.shutdown()
        (SITE / 'modello-dispense.html').unlink(missing_ok=True)
    assert not errors, errors
    report = {'viewport_tema_pagina':checks,'errori_javascript':errors,'copertine_verificate':len(covers),
              'offline':offline_status,'browser':'Chromium; mobile e touch emulati, nessun dispositivo Android fisico',
              'controlli':['persistenza','automatico e cambio sistema','storage bloccato','senza JavaScript','logo e movimento ridotto','ricerca e filtro','indice tastiera','note','zoom','crediti','download identico']}
    (ROOT/'lavorazione/sito/verifica-stringhe.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'Verificate {len(checks)} combinazioni pagina/viewport/tema e {len(covers)} copertine; nessun errore JavaScript')


if __name__ == '__main__':
    main()
