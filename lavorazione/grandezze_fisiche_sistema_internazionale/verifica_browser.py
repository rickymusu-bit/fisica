"""Controlli e anteprime del capitolo corrente, inclusa apertura file offline."""
import json
import functools
import http.server
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
TARGET = ROOT / 'grandezze_fisiche_sistema_internazionale_it.html'


def main():
    report = {'viewports': [], 'errors': [], 'network_requests': [], 'controls': {}}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(offline=True, accept_downloads=True, reduced_motion='reduce')
        page = context.new_page()
        page.on('pageerror', lambda e: report['errors'].append(str(e)))
        page.on('request', lambda r: report['network_requests'].append(r.url) if r.url.startswith(('http:', 'https:')) else None)
        page.goto(TARGET.as_uri())
        page.evaluate('document.fonts.ready')
        assert page.title() == 'Le grandezze fisiche e il Sistema internazionale — Stringhe'
        for width in [320, 390, 768, 1024, 1440]:
            page.set_viewport_size({'width': width, 'height': 1000})
            page.wait_for_timeout(100)
            result = page.evaluate('''() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,
              images:[...document.images].every(i=>i.complete&&i.naturalWidth>0),
              questions:document.querySelectorAll('.questions>li').length,
              rows:[...document.querySelectorAll('.si-table tbody')].map(t=>t.rows.length),
              tables:[...document.querySelectorAll('.si-table-scroll')].map(t=>({client:t.clientWidth,scroll:t.scrollWidth})),
              formulas:[...document.querySelectorAll('.equation')].every(e=>e.scrollWidth<=e.clientWidth+1),
              brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>a.hash&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash)})''')
            assert result['scroll'] <= width + 1, result
            assert result['images'] and result['questions'] == 9 and result['rows'] == [7, 13]
            assert result['formulas'] and not result['brokenAnchors']
            report['viewports'].append(result)
        page.set_viewport_size({'width': 390, 'height': 844})
        page.locator('#indice > summary').click()
        assert page.locator('#indice').evaluate('(e)=>e.open')
        page.keyboard.press('Escape')
        assert not page.locator('#indice').evaluate('(e)=>e.open')
        page.locator('#indice > summary').click()
        page.locator('.sidebar-nav a[href="#unita-derivate"]').click()
        assert not page.locator('#indice').evaluate('(e)=>e.open')
        assert page.evaluate('document.activeElement.id') == 'unita-derivate'
        report['controls']['index_keyboard_and_jump'] = True
        page.locator('#fig-03 .image-zoom > summary').click()
        assert page.locator('#fig-03 .image-zoom').evaluate('(e)=>e.open')
        assert page.locator('#fig-03 .zoom-scroll').evaluate('(e)=>e.scrollWidth>e.clientWidth')
        page.locator('#fig-03 .image-zoom > summary').click()
        report['controls']['zoom'] = True
        page.locator('[data-offline-credits]').click()
        assert page.locator('#crediti-autonomi').evaluate('(e)=>e.open')
        credits = page.locator('#crediti-autonomi').inner_text()
        for required in ['Nenad Stojkovic', 'Netol', 'BIPM', 'CC BY-SA 3.0 IGO', 'CC BY 2.0', 'CC BY-SA 3.0', 'SIL OPEN FONT LICENSE', 'FC Barcelona']:
            assert required in credits, required
        assert 'Risorse senza attribuzione' not in credits
        page.locator('[data-close-credits]').click()
        report['controls']['credits_and_OFL_offline'] = True
        page.evaluate('scrollTo(0,0)')
        # Il download viene verificato attraverso un server HTTP locale:
        # Chromium non emette l'evento download per il collegamento file locale.
        download_context = browser.new_context(accept_downloads=True)
        class Handler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *args):
                pass
        server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(ROOT)))
        threading.Thread(target=server.serve_forever, daemon=True).start()
        download_page = download_context.new_page()
        download_page.goto(f'http://127.0.0.1:{server.server_port}/' + TARGET.name)
        with download_page.expect_download() as download:
            download_page.locator('a[download]').click()
        downloaded = download.value
        assert not downloaded.failure(), downloaded.failure()
        saved = WORK / 'download-verificato.html'
        downloaded.save_as(saved)
        assert saved.read_bytes() == TARGET.read_bytes()
        saved.unlink()
        report['controls']['download_HTTP_local_bytes_equal'] = True
        download_context.close()
        server.shutdown(); server.server_close()
        # Confronti delle due palette e dettagli della stessa composizione.
        for theme in ['dark', 'light']:
            page.locator('[data-theme-menu] > summary').click()
            page.locator(f'[data-theme-option="{theme}"]').click()
            assert page.locator('html').get_attribute('data-theme') == theme
            page.reload(); page.evaluate('document.fonts.ready')
            assert page.locator('html').get_attribute('data-theme') == theme
            for width in [390, 1440]:
                page.set_viewport_size({'width': width, 'height': 1000})
                page.evaluate('scrollTo(0,0)')
                page.screenshot(path=str(WORK / f'anteprima-copertina-{theme}-{width}.png'))
                page.screenshot(path=str(WORK / f'anteprima-{theme}-{width}.png'), full_page=True)
                page.locator('#fig-01').screenshot(path=str(WORK / f'anteprima-metro-{theme}-{width}.png'))
                page.locator('#fig-03').screenshot(path=str(WORK / f'anteprima-campo-{theme}-{width}.png'))
                page.locator('#tab-01').screenshot(path=str(WORK / f'anteprima-tabella-{theme}-{width}.png'))
        report['controls']['themes_and_persistence_file'] = True
        nojs = browser.new_context(java_script_enabled=False, offline=True, viewport={'width': 390, 'height': 844})
        static = nojs.new_page(); static.goto(TARGET.as_uri())
        assert static.locator('html').get_attribute('data-theme') == 'dark'
        static.locator('#indice > summary').click()
        assert static.locator('#indice').evaluate('(e)=>e.open')
        static.locator('#indice > summary').click()
        static.locator('#fig-03 .image-zoom > summary').click()
        assert static.locator('#fig-03 .image-zoom').evaluate('(e)=>e.open')
        static.locator('[data-offline-credits]').click()
        assert static.locator('#crediti-autonomi').is_visible()
        report['controls']['no_javascript_index_zoom_credits_dark'] = True
        assert not report['errors'] and not report['network_requests'], report
        browser.close()
    (WORK / 'verifiche-browser.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
