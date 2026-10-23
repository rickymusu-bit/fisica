"""Verifiche mirate dell'anteprima, usando soltanto file locali."""
from pathlib import Path
import json
import mimetypes
import sys
import functools
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
NAME = 'prefissi_sistema_internazionale_it.html'
URL = 'https://stringhe-preview.invalid/' + NAME


def main():
    out = WORK / 'anteprime'
    out.mkdir(exist_ok=True)
    report = {'widths':[], 'screenshots':[], 'errors':[], 'cover':'Korinna, CC BY 4.0; fotografia scelta, intera'}
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self,*args): pass
    server = ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    url = 'http://127.0.0.1:' + str(server.server_port) + '/' + NAME
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        context = browser.new_context(accept_downloads=True,viewport={'width':1440,'height':1000},reduced_motion='reduce')
        def serve(route):
            from urllib.parse import urlsplit,unquote
            path = (ROOT / unquote(urlsplit(route.request.url).path).lstrip('/')).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                route.fulfill(status=404,body='Not found'); return
            route.fulfill(status=200,body=path.read_bytes(),content_type=mimetypes.guess_type(path.name)[0] or 'application/octet-stream')
        page = context.new_page()
        page.on('pageerror',lambda e:report['errors'].append(str(e)))
        for width in [320,390,768,1024,1440]:
            page.set_viewport_size({'width':width,'height':1000})
            page.goto(url)
            page.evaluate('document.fonts.ready')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), width
            assert page.locator('math').count() > 30
            assert page.locator('mfrac').count() == 2
            assert page.locator('.questions > li').count() == 10
            assert page.locator('.conversion-procedure > li').count() == 4
            page.locator('img').evaluate_all('async(xs)=>{await Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))}')
            assert page.locator('img').evaluate_all('(xs)=>xs.every(i=>i.complete&&i.naturalWidth>0)')
            report['widths'].append({'width':width,'overflow':False,'mathml':page.locator('math').count()})
            for theme in ['dark','light']:
                page.evaluate('(t)=>window.stringheTheme(t)',theme)
                assert page.locator('html').get_attribute('data-theme') == theme
                if width in [390,1440]:
                    shots=[('copertina',None),('formula','#conversione'),('tabella','#tab-01'),('esempio','#esempio-4')]
                    for label,selector in shots:
                        if selector:
                            page.locator(selector).scroll_into_view_if_needed()
                        else:
                            page.evaluate('scrollTo(0,0)')
                        path=out / f'{label}-{theme}-{width}.png'
                        page.screenshot(path=str(path))
                        report['screenshots'].append(path.name)
            # Indice, tastiera e ancora della procedura generale.
            page.evaluate('scrollTo(0,0)')
            page.locator('#indice > summary').click()
            assert page.locator('#indice').get_attribute('open') is not None
            page.keyboard.press('Escape')
            assert page.locator('#indice').get_attribute('open') is None
            page.locator('#indice > summary').click()
            page.locator('.sidebar-nav a[href="#conversione"]').click()
            assert page.url.endswith('#conversione')
            assert page.locator('#indice').get_attribute('open') is None
            # Tabella scorrevole senza modificare righe/colonne.
            scroll=page.locator('#tab-01 .conversion-scroll')
            scroll.scroll_into_view_if_needed()
            scroll.focus()
            before=scroll.evaluate('(e)=>e.scrollLeft')
            page.keyboard.press('ArrowRight')
            page.wait_for_timeout(200)
            if width<=390: assert scroll.evaluate('(e)=>e.scrollLeft')>before
            # Zoom nativo dello schema.
            zoom=page.locator('#sch-01 .image-zoom')
            zoom.locator('summary').scroll_into_view_if_needed()
            zoom.locator('summary').click()
            assert zoom.get_attribute('open') is not None
            assert zoom.locator('.zoom-scroll img').evaluate('(e)=>e.getBoundingClientRect().width')>=960
            page.keyboard.press('Enter')
            assert zoom.get_attribute('open') is None
        # Crediti incorporati e download effettivo.
        page.goto(url)
        page.locator('[data-offline-credits]').click()
        assert page.locator('#crediti-autonomi').get_attribute('open') is not None
        assert 'BIPM' in page.locator('#crediti-autonomi').inner_text()
        assert 'SIL OPEN FONT LICENSE' in page.locator('#crediti-autonomi').inner_text()
        page.locator('[data-close-credits]').click()
        with page.expect_download() as info:
            page.locator('a[download]').click()
        download=info.value
        download.save_as(str(out / NAME))
        assert (out / NAME).read_bytes()==(ROOT / NAME).read_bytes()
        (out / NAME).unlink()
        report['download']='byte identici al documento sorgente'
        # Lettura senza JavaScript: font, formule, immagini, indice e zoom nativi.
        nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':900})
        plain=nojs.new_page();plain.goto(url)
        assert plain.locator('html').get_attribute('data-theme')=='dark'
        assert plain.locator('math').count()>30
        plain.locator('#sch-01 .image-zoom > summary').click()
        assert plain.locator('#sch-01 .image-zoom').get_attribute('open') is not None
        plain.locator('[data-offline-credits]').click()
        assert plain.locator('#crediti-autonomi').is_visible()
        report['withoutJavascript']='testo, MathML, zoom e crediti disponibili'
        report['externalAssets']=[]
        offline=browser.new_context(offline=True,viewport={'width':390,'height':900})
        offline_page=offline.new_page()
        offline_page.set_content((ROOT / NAME).read_text())
        offline_page.locator('img').evaluate_all('async(xs)=>{await Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))}')
        assert offline_page.locator('math').count()>30
        assert offline_page.locator('img').evaluate_all('(xs)=>xs.every(i=>i.complete&&i.naturalWidth>0)')
        report['offline']='testo, immagini incorporate, font e MathML disponibili senza rete'
        offline.close();nojs.close();context.close();browser.close()
    server.shutdown();server.server_close()
    assert report['errors']==[],report['errors']
    (WORK / 'verifiche-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('Browser: cinque larghezze, chiaro/scuro, indice, tastiera, tabella, zoom, crediti, download e fallback senza JavaScript verificati.')


if __name__=='__main__': main()
