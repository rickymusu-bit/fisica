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
    report={'layouts':[],'checks':[],'errors':[],'external_requests':[], 'limits':['Immagini del corpo, della bilancia e dei pesetti ancora da fornire; gli spazi sono dichiarati nell’anteprima. Nessun diritto dedotto.']}
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
              page.goto(origin+'/'+name);page.locator('.sim-ready').wait_for()
              assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(key,width,'overflow')
              assert page.locator('html').get_attribute('data-theme')==theme
              ids=page.locator('[id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids)),(key,'duplicate ids')
              assert page.locator('.cover .image-zoom').count()==0
              assert page.locator('.questions>li').count()==(8 if key=='strumenti_misura' else 9)
              page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
              assert page.locator('img').evaluate_all('(xs)=>xs.every(i=>i.naturalWidth>0)')
              assert page.locator('mfrac').count()>0
              if key=='errori_incertezza_misura':
                graph=page.locator('[data-chart]').bounding_box();parent=page.locator('.sim-chart-frame>.overview').bounding_box()
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
                page.locator('.measurement-sim').scroll_into_view_if_needed()
                page.locator('.measurement-sim').screenshot(path=str(shots/f'simulazione-{theme}-{width}.png'))
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
        page.locator('[data-weight="100"]').click();assert page.locator('[data-record]').is_enabled()
        page.clock.run_for(250);page.locator('[data-record]').click()
        assert 'Anticipata' in page.locator('[data-rows]').inner_text()
        page.clock.run_for(850);assert page.locator('[data-display]').inner_text()=='100 g'
        assert page.locator('[data-record]').is_enabled();page.locator('[data-record]').click()
        assert 'Stabilizzata' in page.locator('[data-rows]').inner_text()
        set_range(page,'sensitivity',2);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='100 g'
        assert page.locator('[data-signal]').inner_text()=='500 mV'
        page.locator('[data-record]').click();assert page.locator('[data-record]').is_disabled()
        set_range(page,'capacity',0);page.locator('[data-weight="200"]').click()
        assert page.locator('[data-display]').inner_text()=='Fuori scala';assert page.locator('[data-record]').is_disabled()
        page.locator('[data-weight="200"]').click();page.clock.run_for(1100)
        set_range(page,'offset',2);page.clock.run_for(1100);assert page.locator('[data-display]').inner_text()=='102 g'
        set_range(page,'step',2);page.clock.run_for(1100);assert page.locator('[data-display]').inner_text()=='100 g'
        slider=page.locator('[data-property="step"]');slider.focus();page.keyboard.press('ArrowLeft');assert slider.input_value()=='1'
        page.locator('[data-reset]').click();page.clock.run_for(2500)
        assert page.locator('[data-display]').inner_text()=='0 g';assert page.locator('[data-record]').is_disabled()
        assert page.locator('[data-property="sensitivity"]').input_value()=='0'
        page.locator('[data-weight="10"]').click();set_range(page,'step',1);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='20 g'
        set_range(page,'step',2);page.clock.run_for(1100)
        assert page.locator('[data-display]').inner_text()=='0 g'
        assert page.locator('[data-loaded-mass]').inner_text()=='10 g'
        report['checks'].append('Capitolo 6: lettura anticipata, stabilizzazione, sensibilità calibrata, fuori scala, zero, passo, tastiera e reset durante acquisizione.')
        page.goto(origin+'/'+PAGES['errori_incertezza_misura'])
        assert page.locator('.chapter-navigation a[rel=prev]').get_attribute('href')==PAGES['strumenti_misura']
        assert page.locator('[data-property]').count()==0
        page.locator('[data-check]').click();assert 'almeno cinque' in page.locator('[data-feedback]').inner_text()
        for i in range(5):
          page.locator('[data-measure]').click();assert page.locator('[data-record]').is_disabled()
          page.clock.run_for(1100);page.locator('[data-record]').click();assert page.locator('[data-record]').is_disabled()
        av=page.locator('[data-rows] tr').evaluate_all('(rs)=>rs.map(r=>Number(r.cells[2].textContent.replace(" g","").replace(",",".")))')
        amean=sum(av)/len(av)
        page.locator('[data-answer=mean]').fill(str(round(amean,2)).replace('.',','));page.locator('[data-answer=error]').fill(str(round(amean-100,2)).replace('.',','))
        page.locator('[data-check]').click();assert 'corretti' in page.locator('[data-feedback]').inner_text()
        assert 'Errore del valore medio' in page.locator('[data-results]').inner_text()
        page.locator('[data-sample]').select_option('B')
        assert page.locator('[data-record]').is_disabled();assert page.locator('[data-answer=error]').is_hidden()
        assert page.locator('[data-results]').is_hidden()
        for i in range(5):
          page.locator('[data-measure]').click();page.clock.run_for(1100);page.locator('[data-record]').click()
        bv=page.locator('[data-rows] tr').evaluate_all('(rs)=>rs.filter(r=>r.cells[0].textContent.startsWith("B")).map(r=>Number(r.cells[2].textContent.replace(" g","").replace(",",".")))')
        mean=sum(bv)/len(bv);disp=(max(bv)-min(bv))/2;u=max(1,disp)
        for key,value in [('mean',mean),('dispersion',disp),('uncertainty',u)]:page.locator('[data-answer='+key+']').fill(str(round(value,2)).replace('.',','))
        page.locator('[data-check]').click();assert 'corretti' in page.locator('[data-feedback]').inner_text()
        assert 'riferimento della massa ignota non è disponibile' in page.locator('[data-results]').inner_text()
        assert page.locator('[data-chart] .plot-point').count()==10
        assert page.locator('[data-chart] .plot-reference').count()==1
        assert '125 g' not in page.locator('[data-chart-description]').inner_text().split('riferimento')[-1] or 'riferimento 125' not in page.locator('[data-chart-description]').inner_text()
        for width in [390,1440]:
          page.set_viewport_size({'width':width,'height':1000})
          hide_bar=page.add_style_tag(content='.topbar{visibility:hidden!important}')
          page.locator('[data-chart]').screenshot(path=str(ROOT/'lavorazione/errori_incertezza_misura/anteprime'/f'grafico-dati-{width}.png'))
          hide_bar.evaluate('(e)=>e.remove()')
        page.locator('.sim-chart-frame .image-zoom>summary').click()
        expect(page.locator('.sim-chart-frame .image-zoom')).to_have_attribute('open','')
        assert page.locator('[data-chart-copy] .plot-point').count()==10
        scroll=page.locator('.sim-chart-frame .zoom-scroll');scroll.focus();before=scroll.evaluate('(e)=>e.scrollLeft');page.keyboard.press('ArrowRight');page.wait_for_timeout(300)
        assert scroll.evaluate('(e)=>e.scrollLeft')>before
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
        page.locator('.sim-chart-frame .image-zoom>summary').click()
        page.locator('[data-sample]').select_option('A');assert len(page.locator('[data-rows] tr').all())==10
        page.locator('[data-clear]').click();assert page.locator('[data-chart] .plot-a').count()==0;assert page.locator('[data-chart] .plot-b').count()==5
        page.locator('[data-reset]').click();assert page.locator('[data-chart] .plot-point').count()==0
        # Grafico su casi asimmetrici e coincidenti: browser deterministico, non sequenza forzata nell'app.
        page.evaluate('''()=>{let a=[.5,.5,.5,.5,1],i=0;Math.random=()=>a[i++%a.length]}''')
        for i in range(5):
          page.locator('[data-measure]').click();page.clock.run_for(1100);page.locator('[data-record]').click()
        assert page.locator('[data-chart] .plot-point').count()==5
        page.locator('[data-sample]').select_option('B')
        page.evaluate('()=>{Math.random=()=>.5}')
        for i in range(5):
          page.locator('[data-measure]').click();page.clock.run_for(1100);page.locator('[data-record]').click()
        page.locator('[data-solution]').click();assert '0 g' in page.locator('[data-results]').inner_text()
        assert 'U = 1 g' in page.locator('[data-chart]').inner_text()
        page.locator('[data-chart]').screenshot(path=str(ROOT/'lavorazione/errori_incertezza_misura/anteprime/grafico-letture-identiche.png'))
        for i in range(5):
          page.locator('[data-measure]').click();page.clock.run_for(1100);page.locator('[data-record]').click()
        assert page.locator('[data-record]').is_disabled();assert page.locator('[data-chart] .plot-b').count()==10
        assert page.locator('[data-measure]').is_disabled();assert 'dieci letture' in page.locator('[data-status]').inner_text()
        report['checks'].append('Capitolo 7: cinque acquisizioni indipendenti per campione, limite dieci, controlli dei calcoli, campioni separati, grafico, cancellazione e ripristino; letture identiche con d=0 e U=1 g.')
        # Download esatto, nessuna dipendenza di rete e fallback senza JavaScript.
        for key,name in PAGES.items():
          page.goto(origin+'/'+name)
          with page.expect_download() as dl:page.locator('a[download]').click()
          target=ROOT/'lavorazione'/key/'anteprime'/'verifica-download.html';dl.value.save_as(str(target))
          assert target.read_bytes()==(ROOT/name).read_bytes();target.unlink()
          off=browser.new_context(offline=True,viewport={'width':390,'height':900})
          plain=off.new_page();plain.set_content((ROOT/name).read_text())
          plain.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
          assert plain.locator('.sim-ready').count()==1;assert plain.locator('img').evaluate_all('(xs)=>xs.every(i=>i.naturalWidth>0)')
          assert plain.locator('mfrac').count()>0;off.close()
          nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':900})
          plain=nojs.new_page();plain.goto(origin+'/'+name);assert plain.locator('html').get_attribute('data-theme')=='dark'
          assert plain.locator('[data-record]').is_disabled();assert plain.locator('.questions>li').count()>0
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
