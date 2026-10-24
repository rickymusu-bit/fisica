"""Verifica layout, immagini incorporate, interazioni, fallback e navigazione dei capitoli 8–9."""
from pathlib import Path
import json,sys,threading
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright,expect
ROOT=Path(__file__).resolve().parents[2]
PAGES=[('piano_cartesiano_grafici','piano_cartesiano_grafici_it.html',8),('proporzionalita_diretta','relazioni_proporzionalita_it.html',9)]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
origin='http://127.0.0.1:'+str(server.server_port)
report={'layouts':[],'checks':[],'errors':[],'external_requests':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for key,name,count in PAGES:
  shots=ROOT/'lavorazione'/key/'anteprime';shots.mkdir(exist_ok=True)
  for width in [320,390,1440]:
   for theme in ['dark','light']:
    ctx=browser.new_context(viewport={'width':width,'height':1000},reduced_motion='reduce')
    ctx.add_init_script('localStorage.setItem("stringhe-theme",'+json.dumps(theme)+')')
    page=ctx.new_page();page.on('pageerror',lambda e:report['errors'].append(str(e)))
    page.on('request',lambda r:report['external_requests'].append(r.url) if not r.url.startswith((origin,'data:','blob:')) else None)
    page.goto(origin+'/'+name)
    page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(name,width,'overflow')
    assert page.locator('.graph .axis, .graph .guide').evaluate_all('(xs)=>xs.every(x=>getComputedStyle(x).fill==="none")')
    ids=page.locator('[id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids)),(name,'duplicate ids')
    assert page.locator('.cover .image-zoom').count()==0
    assert page.locator('.questions>li').count()==count
    assert page.locator('img').evaluate_all('(xs)=>xs.every(i=>i.naturalWidth>0)')
    assert page.locator('html').get_attribute('data-theme')==theme
    for href in page.locator('a[href^="#"]').evaluate_all('(xs)=>xs.map(x=>x.getAttribute("href")).filter(x=>x.length>1)'):
     assert page.locator('[id="'+href[1:]+'"]').count(),href
    if width in [390,1440]:
     page.screenshot(path=str(shots/f'copertina-{theme}-{width}.png'))
     for n,situation in enumerate(page.locator('.situation').all()):
      situation.screenshot(path=str(shots/f'situazione-{n+1}-{theme}-{width}.png'))
     for n,figure in enumerate(page.locator('.article .visual.graph').all()):
      figure.screenshot(path=str(shots/f'grafico-{n+1}-{theme}-{width}.png'))
    page.locator('#indice>summary').click();expect(page.locator('#indice')).to_have_attribute('open','');page.keyboard.press('Escape')
    page.locator('[data-offline-credits]').click();expect(page.locator('#crediti-autonomi')).to_be_visible();assert 'OFL' in page.locator('#crediti-autonomi').inner_text() or 'Open Font License' in page.locator('#crediti-autonomi').inner_text();page.locator('[data-close-credits]').click();expect(page.locator('[data-offline-credits]')).to_be_focused()
    if count==8:
     point=page.locator('#point');point.focus();page.keyboard.press('ArrowLeft');expect(page.locator('#coordinate-readout')).to_have_text('P = (1,5; 2); I quadrante')
     for _ in range(3):page.keyboard.press('ArrowLeft')
     expect(page.locator('#coordinate-readout')).to_have_text('P = (0; 2); asse y')
     page.keyboard.press('ArrowLeft');expect(page.locator('#coordinate-readout')).to_have_text('P = (-0,5; 2); II quadrante')
     for _ in range(20):page.keyboard.press('ArrowDown')
     expect(page.locator('#coordinate-readout')).to_have_text('P = (-0,5; -5); III quadrante')
     zoom=page.locator('.plane-frame details');zoom.locator('summary').click();expect(zoom).to_have_attribute('open','')
     page.wait_for_timeout(80)
     assert zoom.locator('#plane').count()==1
     point.focus();page.keyboard.press('ArrowUp');expect(page.locator('#coordinate-readout')).to_have_text('P = (-0,5; -4,5); III quadrante')
     zoom.locator('summary').click();page.wait_for_timeout(80);assert page.locator('.plane-frame>.overview>#plane').count()==1
     svg=page.locator('#plane');box=svg.bounding_box()
     # Trascinamento attraverso la trasformazione SVG anche sul layout mobile.
     # Mouse reale da P alla coppia (3; -2).
     point.scroll_into_view_if_needed();a=point.bounding_box()
     target=svg.evaluate('(s)=>{const p=s.createSVGPoint();p.x=360;p.y=320;const q=p.matrixTransform(s.getScreenCTM());return {x:q.x,y:q.y}}')
     page.mouse.move(a['x']+a['width']/2,a['y']+a['height']/2);page.mouse.down();page.mouse.move(target['x'],target['y'],steps=5);page.mouse.up()
     expect(page.locator('#coordinate-readout')).to_have_text('P = (3; -2); IV quadrante')
    else:
     assert page.locator('mfrac').count()==4
     for button in page.locator('[data-toggle]').all():
      button.click();expect(button).to_have_attribute('aria-pressed','true');frame=page.locator('#'+button.get_attribute('data-toggle'));assert frame.locator('.overview .fit').is_visible();
      if width in [390,1440]:frame.screenshot(path=str(shots/f'modello-{button.get_attribute("data-kind")}-{button.get_attribute("data-toggle")}-{theme}-{width}.png'))
      button.click();expect(button).to_have_attribute('aria-pressed','false')
     page.locator('.note-ref a').click();expect(page.locator('.chapter-notes')).to_have_attribute('open','');page.locator('[role="doc-backlink"]').click()
    if count==9:
     for svg in page.locator('.situation .journey, .graph svg[viewBox="0 0 500 270"]').all():
      sizes=svg.locator('text').evaluate_all('(xs)=>xs.map(e=>parseFloat(getComputedStyle(e).fontSize)*e.getScreenCTM().a)');assert min(sizes)>=14,(width,sizes)
    # Zoom dei grafici statici e dei modelli.
    for details in page.locator('.graph details.image-zoom').all():
     details.locator('summary').click();expect(details).to_have_attribute('open','');expect(details.locator('.zoom-scroll svg')).to_have_count(1);details.locator('summary').click()
    report['layouts'].append({'chapter':key,'width':width,'theme':theme,'images':True,'overflow':False,'interactions':True})
    ctx.close()
  # File autonomo, JavaScript disattivato: dati, curve e zoom restano disponibili.
  ctx=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':900});page=ctx.new_page();page.goto(origin+'/'+name)
  assert page.locator('.questions>li').count()==count
  if count==9:assert page.locator('.overview .fit').count()==3 and page.locator('.overview .fit').first.is_visible()
  page.locator('.image-zoom summary').first.click();assert page.locator('.image-zoom[open] .zoom-scroll svg').first.is_visible()
  ctx.close()
 report['checks']=['12 layout senza overflow; immagini decodificate','Tastiera, limiti, quadranti, assi e trascinamento di P','Zoom nativo dei grafici e mantenimento del punto interattivo','Tre comandi mostra/nascondi e stato aria-pressed','Indice, note, crediti incorporati e licenza Lexend','Offline e fallback senza JavaScript; nessuna richiesta esterna']
 browser.close()
assert not report['errors'],report['errors']
assert not report['external_requests'],report['external_requests']
for key,_,_ in PAGES:(ROOT/'lavorazione'/key/'verifiche-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
