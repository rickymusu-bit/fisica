import json,functools,http.server,threading
from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path.cwd();D=R/'lavorazione/sito/economia-informativa'
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(R/'_site')));threading.Thread(target=srv.serve_forever,daemon=True).start()
selectors=['#sim-title','#misurare','#potenze','#prefissi','#calcoli','#quanto-puo-misurare-e-quanto-rapidamente','#stimare-lincertezza-di-una-massa-ignota','figure:has(img[alt*="thermos"])','#equilibrio-termico','#energia-per-un-grado','#temperatura-e-masse','#quando-cambiano-le-dimensioni','figure:has(#solidMotion)','.heating-curve','#la-caffettiera-materiali-con-compiti-diversi','#le-celle-convettive-del-sole','#quanta-energia-emette-una-superficie']
with sync_playwright() as p:
 b=p.chromium.launch(args=['--no-sandbox']);page=b.new_page(reduced_motion='reduce')
 for file,sel in zip(json.loads((R/'pubblicazione.json').read_text())['articoli'],selectors):
  page.goto(f'http://127.0.0.1:{srv.server_port}/'+file);page.evaluate('async()=>{await document.fonts.ready;await Promise.all([...document.images].map(async i=>{i.loading="eager";try{await i.decode()}catch(e){}}))}')
  page.evaluate('document.documentElement.dataset.theme="dark"')
  loc=page.locator(sel).first
  if not loc.count():loc=page.locator('.article [data-toc]').first
  for width in [390,1440]:
   page.set_viewport_size({'width':width,'height':1000});loc.evaluate('(e)=>window.scrollTo(0,e.getBoundingClientRect().top+scrollY-95)');page.wait_for_timeout(100);page.screenshot(path=str(D/'schermate'/f'{Path(file).stem}-{width}.png'),animations='disabled')
 b.close()
srv.shutdown()
