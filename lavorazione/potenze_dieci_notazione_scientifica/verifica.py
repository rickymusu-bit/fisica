"""Verifiche mirate dell'HTML e anteprime riproducibili con Chromium locale."""
from pathlib import Path
import hashlib
import json
import re
import sys
from playwright.sync_api import sync_playwright, expect

ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parent
NAME='potenze_dieci_notazione_scientifica_it.html'
sys.path.insert(0,str(ROOT/'scripts'))
import credits

def main():
    html=(ROOT/NAME).read_text();doc=credits.Document(html)
    assert (WORK/'bozza.html').read_bytes()==(ROOT/NAME).read_bytes()
    assert len(list(doc.root.descendants('table')))==3
    assert len([n for n in doc.root.descendants('h2') if 'data-toc' in n.attrs])==6
    assert len([n for n in doc.root.descendants('div') if n.has_class('notation-equation')])==11
    assert len([n for n in doc.root.descendants('figure') if n.has_class('video')])==2
    assert not list(doc.root.descendants('iframe'))
    assert 'IMG-01' not in html and 'Mount St. Helens' not in html and 'TAB-01M' not in html
    assert NAME not in json.loads((ROOT/'pubblicazione.json').read_text())['articoli']
    assert (ROOT/NAME).stat().st_size<20_000_000
    # CSS e script canonici conservati byte per byte; sole estensioni specifiche.
    model=(ROOT/'riferimenti/TEMA_DISPENSE.html').read_text()
    def shared(source):
        return [m[0] for m in re.finditer(r'<(?:style|script)\b[^>]*>[\s\S]*?</(?:style|script)>',source)
                if 'data-component="tabelle-notazione"' not in m[0] and 'data-resource-credits' not in m[0]]
    assert shared(html)==shared(model)
    ids=[n.attrs['id'] for n in doc.root.descendants() if n.attrs.get('id')]
    assert len(ids)==len(set(ids))
    for n in doc.root.descendants('a'):
        href=n.attrs.get('href','')
        if href.startswith('#') and href!='#': assert href[1:] in ids,href
    output={'html_sha256':hashlib.sha256((ROOT/NAME).read_bytes()).hexdigest(),'bytes':len((ROOT/NAME).read_bytes()),'views':[]}
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        for width in [320,390,768,1024,1440]:
            for theme in ['dark','light']:
                context=browser.new_context(viewport={'width':width,'height':950},accept_downloads=True)
                page=context.new_page();errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
                page.goto('http://127.0.0.1:8765/'+NAME)
                page.evaluate('(theme)=>{localStorage.setItem("stringhe-theme",theme);document.documentElement.dataset.theme=theme}',theme)
                page.evaluate('document.fonts.ready')
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),width
                assert page.locator('.questions>li').count()==8
                assert page.locator('#tab-01l tbody tr').count()==8
                assert page.locator('.chapter-notes').get_attribute('open') is None
                assert page.locator('img').evaluate_all('(images)=>images.every(i=>i.complete&&i.naturalWidth>0)')
                page.locator('#richiamo-1').click()
                expect(page.locator('.chapter-notes')).to_have_attribute('open','')
                page.locator('#nota-1 [role=doc-backlink]').click()
                page.locator('.reader-index>summary').click()
                expect(page.locator('.reader-index')).to_have_attribute('open','')
                page.keyboard.press('Escape')
                expect(page.locator('.reader-index')).not_to_have_attribute('open','')
                if width in [390,1440] and theme=='dark':
                    page.locator('.chapter-notes>summary').click()
                    page.evaluate('scrollTo(0,0)')
                    page.screenshot(path=str(WORK/f'anteprima-{width}.png'),full_page=True)
                    page.locator('#tab-01l').screenshot(path=str(WORK/f'tabella-{width}.png'))
                    if width==1440:
                        with page.expect_download() as pending: page.locator('a[download]').click()
                        downloaded=pending.value
                        assert Path(downloaded.path()).read_bytes()==(ROOT/NAME).read_bytes()
                assert not errors,errors
                output['views'].append({'width':width,'theme':theme,'overflow':False,'errors':errors})
                context.close()
        # Documento autonomo con rete disattivata e JS disattivato.
        for js in [True,False]:
            context=browser.new_context(viewport={'width':390,'height':844},java_script_enabled=js)
            page=context.new_page();page.goto('http://127.0.0.1:8765/'+NAME)
            context.set_offline(True)
            # Una ricarica HTTP offline non può raggiungere il server: usare il documento già scaricato.
            page.set_content(html,wait_until='load')
            assert page.locator('img').evaluate_all('(images)=>images.every(i=>i.complete&&i.naturalWidth>0)')
            assert page.locator('.questions>li').count()==8
            context.close()
        browser.close()
    output['offline_embedded_images']=True
    (WORK/'verifiche.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(output,ensure_ascii=False))

if __name__=='__main__': main()
