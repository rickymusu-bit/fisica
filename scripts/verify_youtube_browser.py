"""Privacy prima del clic e ciclo di vita iframe, con rete video intercettata.

Non simula o certifica la riproduzione dei filmati. Le schermate mostrano
esclusivamente i riquadri reali prima del clic, mai il contenuto di test.
"""
from pathlib import Path
from urllib.parse import urlsplit,parse_qs
import json
from playwright.sync_api import sync_playwright,expect
from youtube_videos import player,apply_youtube_videos

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'lavorazione/sito/video_youtube'
BASE='http://127.0.0.1:8766/'

def external(url):
    host=urlsplit(url).hostname or ''
    return host.endswith(('youtube.com','youtube-nocookie.com','ytimg.com','googlevideo.com','ggpht.com'))

def main():
    inventory=json.loads((WORK/'inventario.json').read_text())
    docs=[d for d in inventory['documents'] if d['video_urls']]
    report={'network_test':'Richieste al lettore intercettate per verificare il ciclo iframe; riproduzione remota non certificata.', 'views':[]}
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        for document in docs:
            for width in [390,1440]:
                for theme in ['dark','light']:
                    context=browser.new_context(viewport={'width':width,'height':950})
                    requests=[]
                    def route(request):
                        if external(request.request.url):
                            requests.append(request.request.url)
                            request.fulfill(status=200,content_type='text/html',body='<html><body>Iframe lifecycle test</body></html>')
                        else:request.continue_()
                    context.route('**/*',route)
                    page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
                    page.goto(BASE+document['file']);page.evaluate('(t)=>document.documentElement.dataset.theme=t',theme);page.evaluate('document.fonts.ready')
                    # Fermare soltanto lo scorrimento animato durante le acquisizioni.
                    page.evaluate("document.documentElement.style.setProperty('scroll-behavior','auto','important')")
                    assert not requests,requests
                    assert page.locator('.youtube-stage iframe').count()==0
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),document['file']
                    players=page.locator('[data-youtube-video]')
                    assert players.count()==len(document['video_urls'])
                    for i,url in enumerate(document['video_urls']):
                        current=players.nth(i)
                        assert current.locator('img').count()==0
                        link=current.locator('.youtube-fallback');assert link.get_attribute('href')==url
                        expect(link).to_be_visible()
                        button=current.locator('[data-youtube-load]');expect(button).to_be_visible()
                        if theme=='dark' and document['file'] in ['conduzione_it.html','potenze_dieci_notazione_scientifica_it.html']:
                            current.screenshot(path=str(WORK/(document['file'].replace('_it.html','')+f'-{i+1}-{width}.png')))
                        button.focus();page.keyboard.press('Enter')
                        frame=current.locator('iframe');expect(frame).to_have_count(1)
                        parsed=urlsplit(frame.get_attribute('src'));params=parse_qs(parsed.query)
                        assert parsed.scheme=='https' and parsed.hostname=='www.youtube-nocookie.com'
                        assert params['autoplay']==['0'] and params['playsinline']==['1']
                        assert frame.get_attribute('referrerpolicy')=='strict-origin-when-cross-origin'
                        assert frame.get_attribute('allowfullscreen') is not None
                        assert 'autoplay' not in frame.get_attribute('allow')
                        size=frame.bounding_box();assert size['width']>=200 and size['height']>=200
                        expect(link).to_be_visible()
                        current.locator('[data-youtube-stop]').click()
                        expect(frame).to_have_count(0);expect(button).to_be_focused()
                        # Riapertura e chiusura: un solo iframe, senza duplicare listener o link.
                        page.keyboard.press('Space');expect(frame).to_have_count(1)
                        current.locator('[data-youtube-stop]').click();expect(frame).to_have_count(0)
                    assert not errors,errors
                    report['views'].append({'file':document['file'],'width':width,'theme':theme,'players':players.count(),'before_click_requests':0,'overflow':False,'errors':errors})
                    context.close()
        # Senza JavaScript, ogni video conserva titolo e collegamento originale.
        for document in docs:
            context=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
            page=context.new_page();page.goto(BASE+document['file'])
            for current in page.locator('[data-youtube-video]').all():
                expect(current.locator('.youtube-fallback')).to_be_visible()
                expect(current.locator('.youtube-load')).to_be_hidden()
                expect(current.locator('noscript .youtube-name')).to_be_visible()
                assert current.locator('iframe').count()==0
            context.close()
        # Offline: nessun iframe, avviso utile e testo del capitolo ancora leggibile.
        context=browser.new_context();page=context.new_page();page.goto(BASE+'potenze_dieci_notazione_scientifica_it.html');context.set_offline(True)
        first=page.locator('[data-youtube-video]').first;first.locator('[data-youtube-load]').click()
        assert first.locator('iframe').count()==0
        expect(first.locator('[data-youtube-notice]')).to_contain_text('offline')
        expect(first.locator('.youtube-fallback')).to_be_visible();context.close()
        # Connessione bloccata dopo il clic: il collegamento resta fuori dall'iframe.
        context=browser.new_context();context.route('https://www.youtube-nocookie.com/**',lambda route:route.abort())
        page=context.new_page();page.goto(BASE+'potenze_dieci_notazione_scientifica_it.html')
        first=page.locator('[data-youtube-video]').first;first.locator('[data-youtube-load]').click()
        expect(first.locator('.youtube-fallback')).to_be_visible();first.locator('[data-youtube-stop]').click();context.close()
        # Timestamp in ore/minuti/secondi verificato anche nell'URL effettivo dell'iframe.
        context=browser.new_context();context.route('https://www.youtube-nocookie.com/**',lambda route:route.fulfill(status=200,body='timestamp test'))
        page=context.new_page();fixture='<html><head></head><body>'+player('https://youtu.be/0fKBhvDjuy0?t=1m30s','Timestamp')+'</body></html>'
        page.set_content(apply_youtube_videos(fixture));page.locator('[data-youtube-load]').click()
        assert parse_qs(urlsplit(page.locator('iframe').get_attribute('src')).query)['start']==['90'];context.close()
        browser.close()
    report.update(no_javascript='passed: tutti i sei documenti',offline='passed',blocked_embed_fallback='passed',timestamp='passed: start=90')
    (WORK/'verifiche.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f"Verificate {len(report['views'])} combinazioni documento/viewport/tema; fallback, privacy al caricamento e timestamp superati.")

if __name__=='__main__':main()
