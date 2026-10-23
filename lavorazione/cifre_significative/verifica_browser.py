"""Verifiche dell'anteprima del capitolo 5 in Chromium, senza servizi esterni."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import base64
import hashlib
import json
import threading
from playwright.sync_api import sync_playwright, expect

ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parent
NAME='cifre_significative_it.html'


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass


def theme(page,value):
    if page.locator('html').get_attribute('data-theme')!=value:
        page.locator('[data-theme-menu]>summary').click()
        page.locator('[data-theme-option="'+value+'"]').click()
    assert page.locator('html').get_attribute('data-theme')==value


def main():
    shots=WORK/'anteprime';shots.mkdir(exist_ok=True)
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url='http://127.0.0.1:'+str(server.server_port)+'/'+NAME
    report={'browser':'Chromium, viewport emulati','combinazioni':[],'errori':[],'richieste_esterne':[],'schermate':[]}
    try:
        with sync_playwright() as pw:
            browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
            context=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True,reduced_motion='reduce')
            page=context.new_page();page.on('pageerror',lambda e:report['errori'].append(str(e)))
            page.on('request',lambda r:report['richieste_esterne'].append(r.url) if not r.url.startswith(('http://127.0.0.1:','data:','blob:')) else None)
            for width in [320,390,768,1024,1440]:
                page.set_viewport_size({'width':width,'height':1000});page.goto(url)
                page.evaluate('document.fonts.ready')
                page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
                for value in ['light','dark']:
                    theme(page,value)
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,value)
                    assert page.locator('#fig-01 .image-zoom, #fig-01 summary, #fig-01 button').count()==0
                    assert page.locator('.article').inner_text().count('cifre significative')==1
                    assert 'che indicheremo con C.S.' in page.locator('.article').inner_text()
                    assert 'non in scala' not in page.locator('#fig-02').inner_text()
                    assert page.locator('.cover img').count()==1
                    assert page.locator('.cover .image-zoom,.cover summary,.cover button').count()==0
                    assert page.locator('.cover img').evaluate('(i)=>i.naturalWidth===960&&i.naturalHeight===540')
                    assert page.locator('.questions>li').count()==10
                    assert page.locator('.significant-procedure').count()==2
                    assert page.locator('.significant-procedure>li').count()==8
                    assert page.locator('.equation').count()==12
                    assert page.locator('mfrac').count()==2
                    assert page.locator('.significant-table').count()==3
                    assert page.locator('.significant-table tbody tr').count()==13
                    assert page.locator('img').evaluate_all('(xs)=>xs.every(i=>i.complete&&i.naturalWidth>0)')
                    for math in page.locator('math').all():
                        box=math.bounding_box();assert box and box['height']>8 and box['width']>0
                    for link in page.locator('.sidebar-nav a').all():
                        assert page.locator(link.get_attribute('href')).count()==1
                    report['combinazioni'].append({'width':width,'theme':value,'overflow':False,'formule':12,'tabelle':3})
                    if width in [390,1440]:
                        for label,selector in [('copertina',None),('confronto','#fig-01'),('tabella','#tab-01'),('schema','#fig-02'),('frazione',':nth-match(.equation:has(mfrac), 2)'),('perimetro','#esempio-3')]:
                            if selector:page.locator(selector).scroll_into_view_if_needed()
                            else:page.evaluate('scrollTo(0,0)')
                            path=shots/f'{label}-{value}-{width}.png';page.screenshot(path=str(path));report['schermate'].append(path.name)
                # Comandi effettivi, tastiera e ancore.
                page.evaluate('scrollTo(0,0)');page.locator('#indice>summary').click();expect(page.locator('#indice')).to_have_attribute('open','')
                page.keyboard.press('Escape');assert page.locator('#indice').get_attribute('open') is None
                page.locator('#indice>summary').click();page.locator('.sidebar-nav a[href="#esempio"]').click()
                assert page.url.endswith('#esempio') and page.locator('#indice').get_attribute('open') is None
                scroll=page.locator('#tab-01 .significant-scroll');scroll.scroll_into_view_if_needed();scroll.focus()
                before=scroll.evaluate('(e)=>e.scrollLeft');page.keyboard.press('ArrowRight');page.wait_for_timeout(150)
                if width<=390:assert scroll.evaluate('(e)=>e.scrollLeft')>before
                zoom=page.locator('#fig-02 .image-zoom');zoom.locator('summary').click();expect(zoom).to_have_attribute('open','')
                assert zoom.locator('img').evaluate('(i)=>i.getBoundingClientRect().width')>=1100
                page.keyboard.press('Enter');assert zoom.get_attribute('open') is None
                page.locator('#richiamo-1').click();expect(page.locator('.chapter-notes')).to_have_attribute('open','')
                page.locator('#nota-1 [role="doc-backlink"]').click();assert page.url.endswith('#richiamo-1')
                page.locator('.chapter-notes>summary').click()
            page.goto(url);page.locator('[data-offline-credits]').click()
            text=page.locator('#crediti-autonomi').inner_text()
            assert 'Uriah Welcome' in text and 'CC BY 2.0' in text and 'generata con ChatGPT' in text
            assert 'SIL OPEN FONT LICENSE' in text and 'Provenienza e diritti da verificare' not in text
            page.locator('[data-close-credits]').click()
            with page.expect_download() as info:page.locator('a[download]').click()
            target=shots/NAME;info.value.save_as(str(target));assert target.read_bytes()==(ROOT/NAME).read_bytes();target.unlink()
            report['download']='identico byte per byte'
            cover=page.locator('.cover img').get_attribute('src').split(',',1)[1]
            assert base64.b64decode(cover)==(WORK/'risorse/copertina-egizia.jpg').read_bytes()
            for value in ['light','dark']:
                nojs=browser.new_context(java_script_enabled=False,color_scheme=value,viewport={'width':390,'height':900})
                plain=nojs.new_page();plain.goto(url);assert plain.locator('html').get_attribute('data-theme')=='dark'
                plain.locator('#fig-02 .image-zoom>summary').click();expect(plain.locator('#fig-02 .image-zoom')).to_have_attribute('open','')
                plain.locator('[data-offline-credits]').click();expect(plain.locator('#crediti-autonomi')).to_be_visible();nojs.close()
            offline=browser.new_context(offline=True,viewport={'width':390,'height':900});plain=offline.new_page()
            plain.set_content((ROOT/NAME).read_text());plain.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
            assert plain.locator('img').evaluate_all('(xs)=>xs.every(i=>i.complete&&i.naturalWidth>0)')
            assert plain.locator('mfrac').count()==2;offline.close()
            report['offline']='HTML in memoria, rete bloccata; immagini e MathML disponibili'
            report['senza_javascript']='figure, zoom nativo e crediti disponibili; default scuro'
            browser.close()
    finally:server.shutdown();server.server_close()
    assert not report['errori'] and not report['richieste_esterne'],report
    report['html_sha256']=hashlib.sha256((ROOT/NAME).read_bytes()).hexdigest()
    (WORK/'verifiche-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('Capitolo 5: dieci combinazioni viewport/tema, comandi, note, download, offline e senza JavaScript verificati.')


if __name__=='__main__':main()
