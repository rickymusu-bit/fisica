"""Verifica le figure e i comandi del capitolo con Chromium e Playwright.

Eseguire con playwright installato e chromium disponibile sul sistema.
Le schermate e il rapporto sono aggiornati in anteprime/.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json
import shutil
ROOT=Path(__file__).resolve().parents[2]
A=Path(__file__).parent/'anteprime';A.mkdir(exist_ok=True)
import http.server,threading,functools
class Handler(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/dilatazione_termica_it.html'
reports=[]
figures={'cop-01':'copertina','fig-01':'giunto-ponte','gra-01':'grafico','fig-07':'binari','fig-02':'termometro','fig-03a':'lamina','fig-03b':'termostato','fig-04':'conserve','fig-05':'lago-foto','fig-05b':'lago','fig-06':'gelo'}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path=shutil.which('chromium'),args=['--no-sandbox','--disable-crash-reporter'])
 for name,w in [('desktop',1440),('mobile',390),('320',320),('768',768),('1024',1024)]:
  context=browser.new_context(viewport={'width':w,'height':1000},device_scale_factor=1,color_scheme='light',reduced_motion='reduce')
  context.route('https://**/*',lambda route:route.abort())
  page=context.new_page(); errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(url);page.evaluate('document.fonts.ready');page.evaluate('Promise.all([...document.images].map(i=>{i.loading="eager";return i.decode().catch(()=>{})}))');context.set_offline(True)
  info=page.evaluate('''() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,theme:document.documentElement.dataset.theme,brokenImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).length,questions:document.querySelectorAll('.questions>li').length,captions:[...document.querySelectorAll('figure')].map(f=>({id:f.id,text:f.querySelector('figcaption')?.textContent,visible:!!f.querySelector('figcaption')?.getBoundingClientRect().height})),missingAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>a.hash&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash)})''')
  assert info['width']==info['scroll'] and info['theme']=='dark' and not info['brokenImages'] and not info['missingAnchors'] and info['questions']==12,info
  assert len(info['captions'])==11 and all(c['text'] and c['visible'] for c in info['captions']),info
  if name in ('desktop','mobile'):
   page.screenshot(path=str(A/(name+'.png')))
   for ident,slug in figures.items():page.locator('#'+ident).screenshot(path=str(A/(slug+'-'+name+'.png')))
  zooms=[]
  for ident in ('gra-01','fig-03a','fig-03b','fig-05b'):
   button=page.locator('#'+ident+' .image-zoom summary');button.scroll_into_view_if_needed();button.focus()
   rect=button.bounding_box();frame=page.locator('#'+ident+' .image-frame').bounding_box()
   assert rect['width']>=44 and rect['height']>=44,(ident,rect)
   assert 7<=rect['x']-frame['x']<=11 and 7<=frame['y']+frame['height']-rect['y']-rect['height']<=11,(ident,rect,frame)
   assert button.inner_text()=='' and button.get_attribute('aria-label')=='Ingrandisci l’immagine'
   button.press('Enter');page.wait_for_timeout(80);assert button.get_attribute('aria-label')=='Rimpicciolisci l’immagine'
   assert page.locator('#'+ident+' .image-zoom').get_attribute('open') is not None
   button.press('Space');page.wait_for_timeout(80);assert page.locator('#'+ident+' .image-zoom').get_attribute('open') is None
   zooms.append({'figure':ident,'width':rect['width'],'height':rect['height'],'bottomLeft':True,'keyboard':True,'labels':True})
  page.locator('.index-toggle').click();assert page.locator('#indice').get_attribute('open') is not None
  page.locator('.sidebar-nav a[href="#applicazione-5"]').click();assert page.locator('#indice').get_attribute('open') is None
  page.locator('#richiamo-1').click();assert page.locator('.chapter-notes').get_attribute('open') is not None
  page.locator('[data-offline-credits]').click();assert page.locator('#crediti-autonomi').is_visible();page.keyboard.press('Escape')
  page.locator('[data-theme-menu]>summary').click();page.locator('[data-theme-option="light"]').click();assert page.locator('html').get_attribute('data-theme')=='light'
  assert page.evaluate('document.documentElement.scrollWidth===innerWidth')
  if name in ('desktop','mobile'):
   page.evaluate('scrollTo(0,0)');page.screenshot(path=str(A/(name+'-chiaro.png')))
   page.locator('#fig-05b').screenshot(path=str(A/('lago-'+name+'-chiaro.png')))
  context.set_offline(False);page.reload();assert page.locator('html').get_attribute('data-theme')=='light'
  assert not errors,errors
  reports.append(dict(device=name,**info,errors=errors,offline=True,index=True,notes=True,zoom=zooms,credits=True,themePersistence=True));context.close();print('Verificato',name,w,flush=True)
 # Native zoom and readable captions without JavaScript.
 context=browser.new_context(viewport={'width':390,'height':1000},java_script_enabled=False,reduced_motion='reduce');page=context.new_page();page.goto(url);page.evaluate('document.fonts.ready');page.evaluate('Promise.all([...document.images].map(i=>{i.loading=\"eager\";return i.decode().catch(()=>{})}))')
 assert page.locator('html').get_attribute('data-theme')=='dark'
 for ident in ('gra-01','fig-03a','fig-03b','fig-05b'):
  button=page.locator('#'+ident+' .image-zoom summary');button.focus();button.press('Enter');assert page.locator('#'+ident+' .image-zoom').get_attribute('open') is not None;button.press('Space')
 page.locator('#fig-05b').screenshot(path=str(A/'lago-mobile-no-js.png'));context.close()
 reports.append({'javascript':False,'nativeZoom':True,'captions':11,'defaultTheme':'dark'})
 # Storage unavailable: the theme menu still works and defaults to dark.
 context=browser.new_context(viewport={'width':390,'height':1000});context.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('Storage unavailable for verification')}})")
 page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url);assert page.locator('html').get_attribute('data-theme')=='dark'
 page.locator('[data-theme-menu]>summary').click();page.locator('[data-theme-option="light"]').click();assert page.locator('html').get_attribute('data-theme')=='light';assert not errors,errors;context.close()
 reports.append({'storage':False,'themeMenu':True,'errors':[]});browser.close()
(A/'verifica.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n');print('11 didascalie visibili e comandi verificati a 320, 390, 768, 1024 e 1440 px; zoom nativo senza JS; tema senza storage.')
