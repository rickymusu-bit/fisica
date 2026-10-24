"""Verifiche dei due capitoli e dei protocolli delle bilance con Chromium."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import base64
import hashlib
import json
import threading
import sys
from playwright.sync_api import sync_playwright, expect

ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parent
PAGES={'strumenti_misura':'strumenti_misura_it.html','errori_incertezza_misura':'errori_incertezza_misura_it.html'}

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass

def set_range(page,key,value):
    page.locator('[data-property="'+key+'"]').evaluate('(e,v)=>{e.value=String(v);e.dispatchEvent(new Event("input",{bubbles:true}));}',value)

def seed(page):
    page.add_init_script('''{let state=2931;Math.random=()=>{state=(1664525*state+1013904223)>>>0;return state/4294967296}}''')

def main():
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    origin='http://127.0.0.1:'+str(server.server_port)
    report={'layouts':[],'checks':[],'errors':[],'external_requests':[], 'limits':[]}
    lab_only='--lab-layouts-only' in sys.argv
    interactions_only='--interactions-only' in sys.argv
    if lab_only or interactions_only:
        previous=json.loads((WORK/'verifiche-browser.json').read_text())
        report['layouts']=previous['layouts'] if interactions_only else [r for r in previous['layouts'] if r['chapter']=='strumenti_misura']
    try:
      with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
        for key,name in ([] if interactions_only else [("errori_incertezza_misura",PAGES['errori_incertezza_misura'])] if lab_only else PAGES.items()):
          shots=ROOT/'lavorazione'/key/'anteprime';shots.mkdir(exist_ok=True)
          for width in [320,390,768,1024,1440]:
            for theme in ['dark','light']:
              ctx=browser.new_context(viewport={'width':width,'height':1000},reduced_motion='reduce',accept_downloads=True)
              ctx.add_init_script('localStorage.setItem("stringhe-theme",'+json.dumps(theme)+')')
              page=ctx.new_page();seed(page)
              page.on('pageerror',lambda e:report['errors'].append(str(e)))
              page.on('request',lambda r:report['external_requests'].append(r.url) if not r.url.startswith((origin,'data:','blob:')) else None)
              page.goto(origin+'/'+name);page.locator('.sim-ready').first.wait_for()
              assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(key,width,'overflow')
              assert page.locator('html').get_attribute('data-theme')==theme
              ids=page.locator('[id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids)),(key,'duplicate ids')
              assert page.locator('.cover .image-zoom').count()==0
              assert page.locator('.questions>li').count()==(8 if key=='strumenti_misura' else 10)
              page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
              assert page.locator('img').evaluate_all('(xs)=>xs.every(i=>i.naturalWidth>0)')
              assert page.locator('mfrac').count()>0 if key=='errori_incertezza_misura' else page.locator('.measure-sensor-table').count()==0
              assert page.locator('.sim-has-balance').count()==(1 if key=='strumenti_misura' else 2)
              assert page.locator('[data-display]').first.bounding_box()['width']<=page.locator('.sim-balance-scene').first.bounding_box()['width']
              assert page.locator('image[id="sim-balance-art"]').count()==1
              assert page.locator('image[id="sim-weight-art"]').count()==1
              if key=='errori_incertezza_misura':
                page.wait_for_timeout(80)
                for chart in page.locator('[data-chart]').all():
                  sizes=chart.locator('text').evaluate_all('(xs)=>xs.map(e=>parseFloat(getComputedStyle(e).fontSize)*e.getScreenCTM().a)')
                  assert min(sizes)>=13.9,(width,sizes)
                graph=page.locator('[data-chart]').first.bounding_box();parent=page.locator('.sim-chart-frame>.overview').first.bounding_box()
                assert abs(graph['width']-parent['width'])<=2,(graph,parent)
              for selector in ['button[data-interactive]','input[type=range]','select[data-interactive]']:
                for box in page.locator(selector).evaluate_all('(xs)=>xs.filter(x=>x.getClientRects().length).map(x=>({w:x.getBoundingClientRect().width,h:x.getBoundingClientRect().height}))'):
                  assert box['h']>=43.5,(selector,box)
              page.locator('#indice>summary').click();expect(page.locator('#indice')).to_have_attribute('open','')
              page.keyboard.press('Escape');assert page.locator('#indice').get_attribute('open') is None
              page.locator('#richiamo-1').click();expect(page.locator('.chapter-notes')).to_have_attribute('open','')
              page.locator('#nota-1 [role="doc-backlink"]').first.click();assert '#richiamo-1' in page.url
              page.locator('[data-offline-credits]').click();expect(page.locator('#crediti-autonomi')).to_be_visible()
              credittext=page.locator('#crediti-autonomi').inner_text();assert 'SIL OPEN FONT LICENSE' in credittext
              assert ('N. Phillips/NIST' if key=='strumenti_misura' else 'Mysid') in credittext
              page.locator('[data-close-credits]').click()
              if width in [390,1440]:
                hide_bar=page.add_style_tag(content='.topbar{visibility:hidden!important}')
                for sim in page.locator('.measurement-sim').all():
                  sim.scroll_into_view_if_needed();study=sim.get_attribute('data-study')
                  sim.screenshot(path=str(shots/(f'simulazione-{study}-{theme}-{width}.png' if study else f'simulazione-{theme}-{width}.png')))
                hide_bar.evaluate('(e)=>e.remove()')
                page.goto(origin+'/'+name);page.locator('.cover').screenshot(path=str(shots/f'copertina-{theme}-{width}.png'))
              report['layouts'].append({'chapter':key,'width':width,'theme':theme,'status':'ok'})
              ctx.close()
        # Modello visibile, acquisizioni e risposte: timer virtuale del browser.
        ctx=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True)
        page=ctx.new_page();seed(page);page.clock.install()
        page.on('pageerror',lambda e:report['errors'].append(str(e)))
        page.goto(origin+'/'+PAGES['strumenti_misura'])
        assert page.locator('.chapter-navigation a[rel=next]').get_attribute('href')==PAGES['errori_incertezza_misura']
        assert 'configurazione' not in page.locator('.measurement-sim').inner_text().lower()
        assert 'valori simulati' not in page.locator('.measurement-sim').inner_text().lower()
        settings=page.locator('.sim-settings')
        assert settings.get_attribute('open') is not None
        assert page.locator('[data-property-output=capacity]').inner_text()=='500 g'
        assert 'Risoluzione' in settings.inner_text() and 'Sensibilità' not in settings.inner_text()
        before=page.locator('[data-record]').bounding_box()['y']+page.evaluate('scrollY')
        settings.locator('summary').click()
        assert settings.get_attribute('open') is None
        assert page.locator('[data-property=step]').is_hidden()
        assert page.locator('[data-record]').bounding_box()['y']+page.evaluate('scrollY') < before-100
        settings.locator('summary').focus();page.keyboard.press('Enter')
        assert settings.get_attribute('open') is not None
        assert page.locator('[data-property-output=capacity]').inner_text()=='500 g'

        page.locator('[data-weight="100"]').click();assert page.locator('[data-record]').is_enabled()
        assert page.locator('[data-pan] .sim-pan-weight').count()==1
        page.clock.run_for(250);page.locator('[data-record]').click()
        assert 'Anticipata' in page.locator('[data-rows]').inner_text()
        page.clock.run_for(850);assert page.locator('[data-display]').inner_text()=='100 g'
        assert page.locator('[data-record]').is_enabled();page.locator('[data-record]').click()
        assert 'Stabilizzata' in page.locator('[data-rows]').inner_text()
        set_range(page,'step',2);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='100 g'
        assert page.locator('[data-property-output=step]').inner_text()=='50 g'
        assert 'mV' not in page.locator('.measurement-sim').inner_text()
        page.locator('[data-record]').click();assert page.locator('[data-record]').is_disabled()
        set_range(page,'step',0);set_range(page,'capacity',0);page.locator('[data-weight="200"]').click()
        assert page.locator('[data-display]').get_attribute('data-value')=='overload';assert page.locator('[data-display]').inner_text()=='OL';assert page.locator('[data-record]').is_disabled()
        page.locator('[data-weight="200"]').click();page.clock.run_for(1100)
        set_range(page,'offset',3);page.clock.run_for(1100);assert page.locator('[data-display]').inner_text()=='102 g'
        set_range(page,'step',2);page.clock.run_for(1100);assert page.locator('[data-display]').inner_text()=='100 g'
        slider=page.locator('[data-property="step"]');slider.focus();page.keyboard.press('ArrowLeft');assert slider.input_value()=='1'
        page.locator('[data-reset]').click();page.clock.run_for(2500)
        assert page.locator('[data-display]').inner_text()=='0 g';assert page.locator('[data-record]').is_disabled()
        assert page.locator('[data-pan] .sim-pan-weight').count()==0
        assert page.locator('[data-property="step"]').input_value()=='0'
        assert page.locator('[data-property-output=offset]').inner_text()=='Alta'
        assert page.locator('[data-property-output=noise]').inner_text()=='Alta'
        set_range(page,'noise',0);assert page.locator('[data-property-output=noise]').inner_text()=='Molto bassa'
        set_range(page,'noise',5)
        page.locator('[data-weight="10"]').click();set_range(page,'step',1);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='20 g'
        set_range(page,'step',2);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='0 g'
        assert page.locator('[data-loaded-mass]').inner_text()=='10 g'
        set_range(page,'step',0)
        for mass in [20,50,100,200]:page.locator('[data-weight="'+str(mass)+'"]').click()
        page.clock.run_for(1100)
        assert page.locator('[data-pan] .sim-pan-weight').count()==5
        assert page.locator('[data-pan] .sim-mass-label').all_text_contents()==['10 g','20 g','50 g','100 g','200 g']
        assert page.locator('[data-display]').inner_text()=='380 g'
        set_range(page,'capacity',1);assert page.locator('[data-display]').inner_text()=='OL'
        set_range(page,'capacity',2);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='380 g'

        for width in [390,1440]:
          page.set_viewport_size({'width':width,'height':1000})
          scene=page.locator('.sim-balance-scene').bounding_box()
          for box in page.locator('[data-pan] svg').evaluate_all('(xs)=>xs.map(e=>{const b=e.getBoundingClientRect();return {x:b.x,y:b.y,w:b.width,h:b.height}})'):
            assert box['x']>=scene['x'] and box['x']+box['w']<=scene['x']+scene['width']+1
            assert box['y']>=scene['y'] and box['y']+box['h']<=scene['y']+scene['height']+1
          bar=page.add_style_tag(content='.topbar{visibility:hidden!important}')
          page.locator('.sim-stage').screenshot(path=str(WORK/'anteprime'/f'bilancia-carica-{width}.png'))
          settings.locator('summary').click()
          page.locator('.measurement-sim').screenshot(path=str(WORK/'anteprime'/f'slider-collassati-{width}.png'))
          assert page.locator('[data-display]').inner_text()=='380 g'
          settings.locator('summary').click()
          bar.evaluate('(e)=>e.remove()')
        report['checks'].append('Capitolo 6: lettura anticipata, stabilizzazione, risoluzione in grammi, portata massima 500 g e pannello richiudibile, fuori scala, zero, passo, tastiera e reset durante acquisizione.')
        page.goto(origin+'/'+PAGES['errori_incertezza_misura'])
        uncertainty=page.locator('[data-study=uncertainty]');error=page.locator('[data-study=error]')
        assert page.locator('[data-sample]').count()==0
        assert page.locator('[data-answer],[data-check],[data-solution],.sim-help,.sim-fields').count()==0
        assert page.locator('.measurement-sim .image-zoom').count()==0
        assert uncertainty.locator('[data-answer=error]').count()==0
        assert error.locator('[data-answer=uncertainty]').count()==0
        assert error.locator('[data-answer=dispersion]').count()==0
        for sim in [uncertainty,error]:
          for i in range(5):
            sim.locator('[data-measure]').click();page.clock.run_for(1100);sim.locator('[data-record]').click()
          values=sim.locator('[data-rows] tr').evaluate_all('(rs)=>rs.map(r=>Number(r.cells[2].textContent.replace(" g","").replace(",",".")))')
          mean=sum(values)/len(values);disp=(max(values)-min(values))/2
          assert 'Media ' in sim.locator('[data-chart]').inner_text()
          bounds=sim.locator('[data-chart] svg').evaluate('(e)=>[Number(e.dataset.axisMin),Number(e.dataset.axisMax)]')
          assert bounds[1]-bounds[0]<=14
          assert min(values)>=bounds[0] and max(values)<=bounds[1]
          assert sim.locator('[data-chart] .plot-point').count()==5
          assert sim.locator('[data-chart] .plot-reference').count()==(1 if sim==error else 0)
          assert sim.locator('[data-chart] .plot-band').count()==(0 if sim==error else 1)
          assert sim.locator('[data-chart] .plot-error').count()==(3 if sim==error else 0)
          assert 'riferimento 125' not in sim.inner_text().lower()
          if sim==uncertainty:assert sim.locator('[data-pan] .sim-mass-label').inner_text()=='B'
          for width in [390,1440]:
            page.set_viewport_size({'width':width,'height':1000});bar=page.add_style_tag(content='.topbar{visibility:hidden!important}')
            sim.locator('[data-chart]').screenshot(path=str(ROOT/'lavorazione/errori_incertezza_misura/anteprime'/f'grafico-{sim.get_attribute("data-study")}-{width}.png'));bar.evaluate('(e)=>e.remove()')
          assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
        uncertainty.locator('[data-clear]').click()
        assert uncertainty.locator('[data-chart] .plot-point').count()==0
        assert error.locator('[data-chart] .plot-point').count()==5
        error.locator('[data-measure]').click();uncertainty.locator('[data-reset]').click();page.clock.run_for(1100)
        assert error.locator('[data-record]').is_enabled();error.locator('[data-record]').click()
        assert error.locator('[data-chart] .plot-point').count()==6
        page.evaluate('()=>{Math.random=()=>.5}')
        for i in range(5):
          uncertainty.locator('[data-measure]').click();page.clock.run_for(1100);uncertainty.locator('[data-record]').click()
        assert 'U = 1 g' in uncertainty.locator('[data-chart]').inner_text()
        error.locator('[data-reset]').click();assert uncertainty.locator('[data-chart] .plot-point').count()==5
        for i in range(5):
          uncertainty.locator('[data-measure]').click();page.clock.run_for(1100);uncertainty.locator('[data-record]').click()
        assert uncertainty.locator('[data-record]').is_disabled() and uncertainty.locator('[data-measure]').is_disabled()
        assert error.locator('[data-measure]').is_enabled()
        report['checks'].append('Capitolo 7: due attività indipendenti; cinque letture e riepiloghi automatici per ciascuna, scala stretta e testo leggibile senza zoom, riferimenti/fasce esclusivi, reset e cancellazione isolati, limite dieci e U=1 g per letture identiche.')
        # Download esatto, nessuna dipendenza di rete e fallback senza JavaScript.
        for key,name in PAGES.items():
          page.goto(origin+'/'+name)
          with page.expect_download() as dl:page.locator('a[download]').click()
          target=ROOT/'lavorazione'/key/'anteprime'/'verifica-download.html';dl.value.save_as(str(target))
          assert target.read_bytes()==(ROOT/name).read_bytes();target.unlink()
          off=browser.new_context(offline=True,viewport={'width':390,'height':900})
          plain=off.new_page();plain.set_content((ROOT/name).read_text())
          plain.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
          assert plain.locator('.sim-ready').count()==(1 if key=='strumenti_misura' else 2);assert plain.locator('img').evaluate_all('(xs)=>xs.every(i=>i.naturalWidth>0)')
          assert (plain.locator('mfrac').count()>0) if key=='errori_incertezza_misura' else plain.locator('.measure-sensor-table').count()==0
          off.close()
          nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':900})
          plain=nojs.new_page();plain.goto(origin+'/'+name);assert plain.locator('html').get_attribute('data-theme')=='dark'
          assert plain.locator('[data-record]').first.is_disabled();assert plain.locator('.questions>li').count()>0
          plain.locator('[data-offline-credits]').click();expect(plain.locator('#crediti-autonomi')).to_be_visible();nojs.close()
        report['checks'].append('Download identico, copertine/MathML/simulazioni offline, teoria e crediti senza JavaScript, default scuro.')
        ctx.close();browser.close()
    finally:server.shutdown();server.server_close()
    assert not report['errors'] and not report['external_requests'],report
    report['offline_method']='HTML caricato in memoria con rete disabilitata; immagini incorporate decodificate, MathML e simulazione disponibili. Navigazione file:// bloccata dalla policy del Chromium dell’ambiente e non dichiarata eseguita.'
    report['html_sha256']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in PAGES.values()}
    for key in PAGES:(ROOT/'lavorazione'/key/'verifiche-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'layouts':len(report['layouts']),'checks':report['checks'],'errors':report['errors'],'external_requests':report['external_requests']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
