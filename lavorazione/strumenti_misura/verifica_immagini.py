"""Verifica mirata alle immagini sostituite del capitolo 6, senza ripetere il modello."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright, expect
import base64
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parent
NAME='strumenti_misura_it.html'
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass

def main():
    svg=(WORK/'risorse/parallasse.svg').read_text()
    geometry=json.loads((WORK/'risorse/parallasse-geometria.json').read_text())
    assert geometry['object']['base'][1]==geometry['object']['zero_on_scale'][1]==750
    assert 'id="matita"' in svg and geometry['object']['kind']=='matita'
    a,b,c,d,e,f=geometry['pencil']['svg_matrix']
    for source,target in [(geometry['pencil']['source_tip'],[400,450]),(geometry['pencil']['source_base'],[400,750])]:
        actual=[a*source[0]+c*source[1]+e,b*source[0]+d*source[1]+f]
        assert max(abs(actual[i]-target[i]) for i in [0,1])<1e-8
    assert all(label in svg for label in ['Vista dall’alto','Vista frontale','Vista dal basso'])
    assert 'Vista laterale schematica' not in svg and 'Indice fermo' not in svg
    assert '>Base allineata allo zero<' not in svg and '>La base è sullo zero' not in svg
    assert 'Separazione dalla scala</text>' not in svg
    assert 'M440 581 408 548' not in svg
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
    Thread(target=server.serve_forever,daemon=True).start()
    origin='http://127.0.0.1:'+str(server.server_port)
    report={'layouts':[],'errors':[],'external_requests':[],'images':['FIG-06-1a','FIG-06-2'],'geometry':json.loads((WORK/'risorse/parallasse-geometria.json').read_text()),'license_check':'Bilancia Batholith PD-self verificata sulla pagina Commons; riferimento Vecteezy Pro non incorporato. Schema originale con geometria SVG ed elemento occhio generato su richiesta.'}
    try:
      with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
        viewbox=geometry['viewbox']
        preview=browser.new_page(viewport={'width':viewbox[2],'height':viewbox[3]})
        svg_uri='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
        preview.set_content('<style>body{margin:0}svg{display:block;width:100vw;height:100vh}</style>'+svg)
        preview.wait_for_load_state('load')
        boxes=preview.locator('svg text').evaluate_all('(xs)=>xs.map(e=>{const b=e.getBBox();return {x:b.x,y:b.y,w:b.width,h:b.height}})')
        assert all(b['x']>=viewbox[0] and b['y']>=viewbox[1] and b['x']+b['w']<=viewbox[0]+viewbox[2] and b['y']+b['h']<=viewbox[1]+viewbox[3] for b in boxes)
        preview.screenshot(path=str(WORK/'risorse/parallasse-anteprima.png'))
        preview.close()
        for width in [320,390,768,1024,1440]:
          for theme in ['dark','light']:
            ctx=browser.new_context(viewport={'width':width,'height':1000},reduced_motion='reduce')
            ctx.add_init_script('localStorage.setItem("stringhe-theme",'+json.dumps(theme)+')')
            page=ctx.new_page();page.on('pageerror',lambda e:report['errors'].append(str(e)))
            page.on('request',lambda r:report['external_requests'].append(r.url) if not r.url.startswith((origin,'data:','blob:')) else None)
            page.goto(origin+'/'+NAME);page.locator('.sim-ready').wait_for()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
            ids=page.locator('[id]').evaluate_all('(xs)=>xs.map(e=>e.id)');assert len(ids)==len(set(ids))
            photo=page.locator('#fig-06-1a');diagram=page.locator('#fig-06-2')
            assert photo.locator('.image-zoom').count()==0
            assert photo.locator('figcaption').count()==1 and diagram.locator('figcaption').count()==1
            assert photo.locator('img').get_attribute('src').split(',',1)[0]=='data:image/jpeg;base64'
            assert base64.b64decode(photo.locator('img').get_attribute('src').split(',',1)[1])==(WORK/'risorse/bilancia-analogica.jpg').read_bytes()
            assert base64.b64decode(diagram.locator('.overview img').get_attribute('src').split(',',1)[1])==(WORK/'risorse/parallasse.svg').read_bytes()
            assert diagram.locator('img').count()==2
            page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
            if width in [390,1440]:
              bar=page.add_style_tag(content='.topbar{visibility:hidden!important}')
              for fig,filename in [(photo,'bilancia-analogica'),(diagram,'parallasse')]:
                fig.screenshot(path=str(WORK/'anteprime'/f'{filename}-{theme}-{width}.png'))
              bar.evaluate('(e)=>e.remove()')
            diagram.locator('summary').click();expect(diagram.locator('details')).to_have_attribute('open','')
            expect(diagram.locator('.overview')).to_be_hidden()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
            scroll=diagram.locator('.zoom-scroll');scroll.focus();before=scroll.evaluate('(e)=>e.scrollLeft')
            page.keyboard.press('ArrowRight');page.wait_for_timeout(200)
            assert scroll.evaluate('(e)=>e.scrollLeft')>before
            diagram.locator('summary').click();expect(diagram.locator('.overview')).to_be_visible()
            page.locator('#richiamo-1').click();expect(page.locator('.chapter-notes')).to_have_attribute('open','')
            page.locator('[data-offline-credits]').click();text=page.locator('#crediti-autonomi').inner_text()
            assert 'Batholith' in text and 'PD-self' in text and 'Schema originale' in text
            assert 'Vecteezy non' in text and 'ChatGPT' in text
            ctx.close();report['layouts'].append({'width':width,'theme':theme,'status':'ok'})
        offline=browser.new_context(offline=True,viewport={'width':390,'height':1000})
        page=offline.new_page();page.set_content((ROOT/NAME).read_text())
        page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
        assert page.locator('#fig-06-2 img').evaluate_all('(xs)=>xs.every(i=>i.complete&&i.naturalWidth>0)')
        offline.close();browser.close()
    finally:server.shutdown();server.server_close()
    assert not report['errors'] and not report['external_requests'],report
    report['html_sha256']=hashlib.sha256((ROOT/NAME).read_bytes()).hexdigest()
    (WORK/'verifiche-immagini.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'image_layouts':len(report['layouts']),'errors':report['errors'],'external_requests':report['external_requests']},ensure_ascii=False))

if __name__=='__main__': main()
