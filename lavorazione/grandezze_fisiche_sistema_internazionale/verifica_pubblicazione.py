"""Verifica il catalogo e i collegamenti della build da pubblicare."""
from pathlib import Path
import functools
import http.server
import json
import threading
from playwright.sync_api import sync_playwright

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
NAME = 'grandezze_fisiche_sistema_internazionale_it.html'
AREA = 'Introduzione alla fisica e alla misura'
TITLE = 'Le grandezze fisiche e il Sistema internazionale'


def main():
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(ROOT / '_site')))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}/'
    report = {'errors': [], 'viewports': [], 'catalogue_count': 12}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(accept_downloads=True, reduced_motion='reduce')
            page = context.new_page()
            page.on('pageerror', lambda e: report['errors'].append(str(e)))
            for width in [390, 1440]:
                page.set_viewport_size({'width': width, 'height': 1000})
                page.goto(base + 'articoli.html'); page.evaluate('document.fonts.ready')
                assert page.locator('.article-card').count() == 12
                assert page.locator(f'.article-card[data-area="{AREA}"]').count() == 2
                page.locator(f'.chip[data-area="{AREA}"]').click()
                assert page.locator('.article-card:visible').count() == 2
                page.screenshot(path=str(WORK / f'anteprima-catalogo-pubblicazione-{width}.png'), full_page=True)
                page.locator('#article-search').fill('Sistema internazionale')
                assert page.locator('.article-card:visible').count() == 1
                page.locator(f'.article-card:visible a[href="{NAME}"]').first.click()
                assert page.locator('h1').inner_text() == TITLE
                assert page.locator('.chapter-navigation a[rel="prev"]').get_attribute('href') == 'metodo_scientifico_it.html'
                assert page.locator('.chapter-navigation a[rel="next"]').get_attribute('href') == 'termodinamica_sistemi_it.html'
                page.locator('.chapter-navigation').screenshot(path=str(WORK / f'anteprima-navigazione-pubblicazione-{width}.png'))
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                page.locator('.chapter-navigation a[rel="prev"]').click()
                assert page.locator('.chapter-navigation a[rel="next"]').get_attribute('href') == NAME
                page.locator('.chapter-navigation a[rel="next"]').click()
                page.locator('.chapter-navigation a[rel="next"]').click()
                assert page.locator('.chapter-navigation a[rel="prev"]').get_attribute('href') == NAME
                page.goto(base + 'index.html')
                random = json.loads(page.locator('#catalogue-data').text_content())
                assert len(random) == 12 and random[1] == NAME
                assert page.locator('.featured .mini').first.get_attribute('href') == NAME
                page.evaluate('Math.random=()=>1.1/12')
                page.locator('#random-article').click();page.wait_for_url('**/' + NAME)
                with page.expect_download() as event:
                    page.locator('a[download]').click()
                download = event.value
                saved = WORK / 'download-pubblicazione.html';download.save_as(saved)
                assert saved.read_bytes() == (ROOT / '_site' / NAME).read_bytes();saved.unlink()
                report['viewports'].append({'width': width, 'filter_search_navigation_news_random_download': True})
            page.goto(base + 'crediti.html')
            assert page.locator('#grandezze-fisiche-sistema-internazionale-it').count() == 1
            assert 'Netol' in page.locator('#grandezze-fisiche-sistema-internazionale-it').inner_text()
            assert not report['errors'], report
            browser.close()
    finally:
        server.shutdown();server.server_close()
    (WORK / 'verifiche-pubblicazione.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
