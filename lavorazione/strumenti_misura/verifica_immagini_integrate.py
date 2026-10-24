"""Verifica delle fotografie scelte e dei bersagli ricreati nei capitoli 6 e 7."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
import json,base64,hashlib
from playwright.sync_api import sync_playwright,expect
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'lavorazione'
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)));Thread(target=server.serve_forever,daemon=True).start();origin='http://127.0.0.1:'+str(server.server_port)
report={'layouts':[],'errors':[],'external_requests':[],'image_slots':{'strumenti_misura':['FIG-06-1a','FIG-06-1b','FIG-06-2','FIG-06-3','FIG-06-4','FIG-06-5'],'errori_incertezza_misura':['SCH-07-1','FIG-07-1','FIG-07-2']}}
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  raw=browser.new_page(viewport={'width':850,'height':850});raw.set_content('<body style="margin:0">'+(W/'errori_incertezza_misura/risorse/bersagli.svg').read_text()+'</body>');raw.screenshot(path=str(W/'errori_incertezza_misura/risorse/bersagli-anteprima.png'));raw.close()
  for chapter in report['image_slots']:
   assets=json.loads((W/chapter/'risorse/immagini.json').read_text())
   for width in (390,1440):
    for theme in ('dark','light'):
     ctx=browser.new_context(viewport={'width':width,'height':1000},reduced_motion='reduce');ctx.add_init_script('localStorage.setItem("stringhe-theme",'+json.dumps(theme)+')');page=ctx.new_page()
     page.on('pageerror',lambda e:report['errors'].append(str(e)));page.on('request',lambda r:report['external_requests'].append(r.url) if not r.url.startswith((origin,'data:','blob:')) else None)
     page.goto(origin+'/'+chapter+'_it.html');page.locator('img').evaluate_all('async xs=>Promise.all(xs.map(i=>{i.loading="eager";return i.decode()}))')
     assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
     page.add_style_tag(content='.topbar{visibility:hidden!important}')
     for slot in report['image_slots'][chapter]:
      figure=page.locator('#'+slot.lower());asset=assets[slot]
      assert figure.locator('figcaption').count()==1
      img=figure.locator('.overview img');assert base64.b64decode(img.get_attribute('src').split(',',1)[1])==(W/chapter/asset['path']).read_bytes()
      assert figure.locator('.image-zoom').count()==(1 if asset.get('zoom') else 0)
      figure.screenshot(path=str(W/chapter/'anteprime'/f'{slot.lower()}-{theme}-{width}.png'))
      if asset.get('zoom'):
       figure.locator('summary').click();expect(figure.locator('details')).to_have_attribute('open','');assert ('Bersagli' if slot=='FIG-07-1' else 'parallasse') in figure.locator('.zoom-scroll').get_attribute('aria-label');assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1');figure.locator('summary').click()
     page.locator('[data-offline-credits]').click();credit=page.locator('#crediti-autonomi').inner_text()
     assert 'Lesselich' in credit and 'CC BY-SA 3.0' in credit
     if chapter=='strumenti_misura':assert 'Photo by CEphoto, Uwe Aranas' in credit and 'Jacek Halicki' in credit and 'CC BY-SA 4.0' in credit
     else:assert 'Ossila' in credit
     ctx.close();report['layouts'].append({'chapter':chapter,'width':width,'theme':theme,'status':'ok'})
  browser.close()
finally:server.shutdown();server.server_close()
assert not report['errors'] and not report['external_requests'],report
report['html_sha256']={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['strumenti_misura_it.html','errori_incertezza_misura_it.html']}
for chapter in report['image_slots']:(W/chapter/'verifiche-immagini-integrate.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
