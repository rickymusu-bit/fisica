"""Verifica della revisione richiesta: dipendenza, schemi, k e assenza di zoom interattivo."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import threading,json,sys
from playwright.sync_api import sync_playwright,expect
ROOT=Path(__file__).resolve().parents[2]
PAGES=[('piano_cartesiano_grafici','piano_cartesiano_grafici_it.html',8),('proporzionalita_diretta','relazioni_proporzionalita_it.html',9)]
if '--chapter-8' in sys.argv:PAGES=PAGES[:1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start();origin=f'http://127.0.0.1:{server.server_port}'
report={'layouts':[],'checks':[],'errors':[],'external_requests':[],'parameter_cases':[]}
# Casi di controllo indipendenti: prezzo di due libri, tempo a 60 km/h, valore a x = 2.
CASES={'direct':[(10,20),(15,30),(20,40)],'inverse':[(60,1),(120,2),(180,3)],'quadratic':[(.5,2),(1,4),(2,8)]}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for key,name,count in PAGES:
  shots=ROOT/'lavorazione'/key/'anteprime';shots.mkdir(exist_ok=True)
  # Le schermate precedenti sono sostituite dalle nuove nello stesso percorso stabile.
  for old in shots.glob('*.png'):old.unlink()
  for width in [320,390,1440]:
   for theme in ['dark','light']:
    ctx=browser.new_context(viewport={'width':width,'height':1000},reduced_motion='reduce')
    ctx.add_init_script('localStorage.setItem("stringhe-theme",'+json.dumps(theme)+')')
    page=ctx.new_page();page.on('pageerror',lambda e:report['errors'].append(str(e)))
    page.on('request',lambda r:report['external_requests'].append(r.url) if not r.url.startswith((origin,'data:','blob:')) else None)
    page.goto(origin+'/'+name)
    page.locator('img').evaluate_all('async(xs)=>Promise.all(xs.map(i=>i.decode()))')
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(name,width,'overflow')
    ids=page.locator('[id]').evaluate_all('(xs)=>xs.map(x=>x.id)');assert len(ids)==len(set(ids)),(name,'duplicate ids')
    assert page.locator('.questions>li').count()==count
    alignments=page.locator('.data-table th,.data-table td').evaluate_all('(xs)=>xs.map(x=>getComputedStyle(x).textAlign)');assert set(alignments)=={'center'},alignments
    assert page.locator('html').get_attribute('data-theme')==theme
    assert page.locator('.article img').count()==0,'Fotografie degli esempi ancora incorporate'
    assert page.locator('.cover .image-zoom, [data-model] .image-zoom, #plane .image-zoom').count()==0
    assert page.locator('.graph .axis, .graph .guide').evaluate_all('(xs)=>xs.every(x=>getComputedStyle(x).fill==="none")')
    for fig in page.locator('.visual').all():assert fig.locator('figcaption').count()==1
    for svg in page.locator('.article>figure:not(.scale-comparison) svg').all():
     sizes=svg.locator('text').evaluate_all('(xs)=>xs.map(e=>parseFloat(getComputedStyle(e).fontSize)*e.getScreenCTM().a)')
     assert not sizes or min(sizes)>=14,(name,width,min(sizes))
    for href in page.locator('a[href^="#"]').evaluate_all('(xs)=>xs.map(x=>x.getAttribute("href")).filter(x=>x.length>1)'):
     assert page.locator('[id="'+href[1:]+'"]').count(),href
    if width in [390,1440]:
     page.screenshot(path=str(shots/f'copertina-{theme}-{width}.png'))
     for n,table in enumerate(page.locator('.data-scroll').all()):table.screenshot(path=str(shots/f'tabella-{n+1}-{theme}-{width}.png'))
     for n,figure in enumerate(page.locator('.article>figure').all()):figure.screenshot(path=str(shots/f'figura-{n+1}-{theme}-{width}.png'))
    page.locator('#indice>summary').click();expect(page.locator('#indice')).to_have_attribute('open','');page.keyboard.press('Escape')
    page.locator('[data-offline-credits]').click();expect(page.locator('#crediti-autonomi')).to_be_visible()
    credittext=page.locator('#crediti-autonomi').inner_text();assert 'Open Font License' in credittext and 'ArticCynda' not in credittext and 'JoyD' not in credittext
    page.locator('[data-close-credits]').click();expect(page.locator('[data-offline-credits]')).to_be_focused()
    if count==8:
     assert 'libri' not in page.locator('.article').inner_text().lower()
     assert page.locator('.image-zoom').count()==1
     for plot in page.locator('.graph svg[data-plot], #plane').all():
      assert plot.locator('[data-axis-tip="x"]').count()==1 and plot.locator('[data-axis-tip="y"]').count()==1
     ends=page.locator('[marker-end="url(#arrow-dependence)"]').evaluate_all('(xs)=>xs.map(p=>{const q=p.getPointAtLength(p.getTotalLength());return [q.x,q.y]})');assert len(ends)==3 and len({y for x,y in ends})==3
     assert page.locator('image[data-credit-id="clipart-robinet-spadassin"]').count()==1
     assert page.locator('image[data-credit-id="clipart-robinet-senza-goccia"]').count()==1
     assert page.locator('.scene').first.locator('[stroke-dasharray]').count()==0
     point=page.locator('#point');point.focus();page.keyboard.press('ArrowLeft');expect(page.locator('#coordinate-readout')).to_have_text('P = (1,5; 2); I quadrante')
     for _ in range(3):page.keyboard.press('ArrowLeft')
     expect(page.locator('#coordinate-readout')).to_have_text('P = (0; 2); asse y')
     page.keyboard.press('ArrowLeft')
     for _ in range(20):page.keyboard.press('ArrowDown')
     expect(page.locator('#coordinate-readout')).to_have_text('P = (-0,5; -5); III quadrante')
     point.scroll_into_view_if_needed();a=point.bounding_box();svg=page.locator('#plane')
     target=svg.evaluate('(s)=>{const p=s.createSVGPoint();p.x=232;p.y=208;const q=p.matrixTransform(s.getScreenCTM());return {x:q.x,y:q.y}}')
     page.mouse.move(a['x']+a['width']/2,a['y']+a['height']/2);page.mouse.down();page.mouse.move(target['x'],target['y'],steps=5);page.mouse.up()
     expect(page.locator('#coordinate-readout')).to_have_text('P = (3; -2); IV quadrante')
     zoom=page.locator('.scale-comparison .image-zoom');zoom.locator('summary').click();expect(zoom).to_have_attribute('open','');assert zoom.locator('.zoom-scroll>svg').is_visible();zoom.locator('summary').click()
    else:
     assert page.locator('.image-zoom').count()==0
     assert page.locator('image[data-credit-id="clipart-red-book-nerdy"]').count()==6
     assert page.locator('image[data-credit-id="clipart-double-decker-bus-j4p4n"]').count()==1
     assert 'in autobus' in page.locator('.article').inner_text()
     for button in page.locator('[data-toggle]').all():button.click();expect(button).to_have_attribute('aria-pressed','true')
     for model,cases in CASES.items():
      figure=page.locator('[data-model="'+model+'"]');svg=figure.locator('svg');initialbox=svg.bounding_box();xmax=float(svg.get_attribute('data-xmax'));ymax=float(svg.get_attribute('data-ymax'))
      for k,answer in cases:
       figure.locator('input').evaluate('(e,v)=>{e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}))}',k)
       expect(figure).to_have_attribute('data-current-k',str(k))
       assert svg.bounding_box()['width']==initialbox['width']
       marker=figure.locator('.probe');cy=float(marker.get_attribute('cy'));actual=(245-cy)*ymax/215
       assert abs(actual-answer)<1e-8,(model,k,actual,answer)
       expect(figure.locator('[data-toggle]')).to_have_attribute('aria-pressed','true')
       if k!=float(figure.get_attribute('data-initial')):assert figure.locator('[data-reference]').is_visible()
       else:assert not figure.locator('[data-reference]').is_visible()
       # Tabella e punti devono restare coerenti con il modello anche dopo la variazione.
       table=page.locator('[data-model-table="'+model+'"]')
       if table.count():
        values=table.locator('tbody tr').evaluate_all('(rs)=>rs.map(r=>[...r.cells].map(c=>Number(c.textContent.replace(",","."))))')
        for x,y in values:
         assert abs(y-(k*x if model=='direct' else k/x))<1e-8
        for point in figure.locator('[data-point-x]').all():
         x=float(point.get_attribute('data-point-x'));y=(245-float(point.get_attribute('cy')))*ymax/215
         assert abs(y-(k*x if model=='direct' else k/x))<1e-8
       if width in [390,1440]:figure.screenshot(path=str(shots/f'{model}-k-{k}-{theme}-{width}.png'))
       report['parameter_cases'].append({'model':model,'k':k,'value':answer,'width':width,'theme':theme})
      # Tastiera nativa sullo slider e limiti.
      slider=figure.locator('input');slider.focus();page.keyboard.press('Home');expect(slider).to_have_value(slider.get_attribute('min'));page.keyboard.press('End');expect(slider).to_have_value(slider.get_attribute('max'))
     page.locator('.note-ref a').click();expect(page.locator('.chapter-notes')).to_have_attribute('open','')
    report['layouts'].append({'chapter':key,'width':width,'theme':theme,'labels_at_least_14px':True,'no_overflow':True,'no_interactive_zoom':True})
    ctx.close()
  ctx=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':900});page=ctx.new_page();page.goto(origin+'/'+name)
  assert page.locator('.questions>li').count()==count
  if count==9:
   assert page.locator('.overview [data-curve]').count()==4
   for fit in page.locator('.overview [data-curve]').all():assert fit.is_visible()
   assert not page.locator('.parameter-controls').first.is_visible()
  else:
   page.locator('.image-zoom summary').click();assert page.locator('.zoom-scroll>svg').is_visible()
  ctx.close()
 browser.close()
report['checks']=['Intestazioni e dati delle tabelle tutti centrati; clip art specifiche incorporate; schema del rubinetto senza tratteggio, originale a sinistra e senza goccia a destra','Tutti i grafici interattivi senza zoom; etichette >=14 CSS px a 320 px','Un solo zoom sul confronto statico delle scale, fuori dai dati; assi orientati e punte separate; SVG Robinet incorporato','P: tastiera, assi, quadranti, limiti e trascinamento',f'k: {len(report["parameter_cases"])} confronti numerici nella selezione corrente; verifiche del capitolo 9 conservate se escluso','Indice, note, crediti OFL, fallback senza JavaScript e nessuna risorsa esterna']
assert not report['errors'],report['errors'];assert not report['external_requests'],report['external_requests']
for key,_,_ in PAGES:(ROOT/'lavorazione'/key/'verifiche-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'layouts':len(report['layouts']),'parameter_cases':len(report['parameter_cases']),'errors':report['errors'],'checks':report['checks']},ensure_ascii=False,indent=2))
