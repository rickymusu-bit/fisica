"""Verifiche dell'articolo autonomo e anteprime, con Chromium e rete disabilitata."""
from pathlib import Path
import base64
import hashlib
import json
import re
import shutil
import sys
from lxml import html
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
TARGET = ROOT / 'energia_interna_calore_specifico_it.html'
SOURCE = TARGET.read_text()


def static_checks():
    document = html.fromstring(SOURCE, parser=html.HTMLParser(huge_tree=True))
    theme = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    styles = re.findall(r'<style[^>]*>[\s\S]*?</style>', SOURCE)
    scripts = re.findall(r'<script[^>]*>[\s\S]*?</script>', SOURCE)
    assert all(s in styles for s in re.findall(r'<style[^>]*>[\s\S]*?</style>', theme))
    assert all(s in scripts for s in re.findall(r'<script[^>]*>[\s\S]*?</script>', theme))
    ids = document.xpath('//@id')
    assert len(ids) == len(set(ids)), 'ID duplicati'
    missing = [a for a in document.xpath('//a/@href') if a.startswith('#') and a != '#' and a[1:] not in ids]
    assert not missing, missing
    for key, filename in [('cop-01','copertina-ivy-mike.jpg'),('fig-01','spiaggia-notturna.webp'),('fig-02','acqua-movimento-molecolare.gif')]:
        src = document.get_element_by_id(key).xpath('.//img/@src')[0]
        assert base64.b64decode(src.split(',',1)[1]) == (WORK/'risorse'/filename).read_bytes()
    assert len(document.xpath('//ol[@class="questions"]/li')) == 8
    assert len(document.xpath('//div[@class="equation"]')) == 5
    assert len(document.xpath('//table/tbody/tr')) == 10
    assert len(document.xpath('//details[@class="chapter-notes"]//li')) == 4
    assert not document.xpath('//article//a[starts-with(@href,"http")]')[2:], 'Collegamenti esterni nel testo'
    assert not re.search(r'\\[\[\](]|\[COP-|\[FIG-|\[TAB-|\[GRA-',document.text_content())
    assert TARGET.stat().st_size < 20_000_000
    manifest = json.loads((ROOT/'pubblicazione.json').read_text())
    assert TARGET.name not in manifest['esclusi_da_pubblicazione_e_aggiornamenti']
    registry = json.loads((ROOT/'risorse/crediti.json').read_text())
    sys.path.insert(0,str(ROOT/'scripts'))
    import credits
    assert not credits.unassociated(registry,TARGET.name)
    results = {'byte':TARGET.stat().st_size, 'limite_byte':20_000_000,
               'sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
               'stili_e_script_comuni_identici':True, 'immagini_correnti_incorporate':True, 'copertina_e_gif_originali_invariate':True,
               'domande':8,'formule':5,'righe_tabella':10,'note':4,
               'id_univoci_e_ancore_valide':True, 'risorse_senza_crediti':[],
               'ammesso_alla_pubblicazione':TARGET.name in manifest['articoli']}
    (WORK/'verifiche-finali.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')


def browser_checks():
    results = {'caricamento':'HTML completo in memoria, rete disabilitata','viste':[]}
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        for width in [1280,390]:
            context = browser.new_context(viewport={'width':width,'height':900},offline=True,reduced_motion='no-preference')
            page = context.new_page()
            errors, requests = [], []
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('request',lambda r:requests.append(r.url) if not r.url.startswith('data:') else None)
            page.set_content(SOURCE,wait_until='load')
            page.evaluate('document.fonts.ready')
            page.wait_for_function('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)')
            assert page.locator('.kicker').text_content() == 'Materia e calore'
            assert page.locator('h1').inner_text() == 'Energia interna, calore e calore specifico'
            dimensions = page.evaluate('''() => ({
              pagina:document.documentElement.scrollWidth,
              viewport:innerWidth,
              tabella:document.querySelector('.heat-table-scroll').clientWidth,
              contenutoTabella:document.querySelector('table').offsetWidth,
              colonne:document.querySelector('thead tr').children.length,
              grafico:document.querySelector('#gra-01 img').naturalWidth,
              font:document.fonts.check('21px Lexend')
            })''')
            assert dimensions['pagina'] == width, dimensions
            assert dimensions['colonne'] == 3 and dimensions['font']
            assert page.locator('.chapter-notes').get_attribute('open') is None
            page.locator('#indice > summary').click()
            assert page.locator('#indice').get_attribute('open') is not None
            page.keyboard.press('Escape')
            assert page.locator('#indice').get_attribute('open') is None
            page.locator('#indice > summary').click()
            page.locator('.sidebar-nav a[href="#energia-per-un-grado"]').click()
            assert page.locator('#indice').get_attribute('open') is None
            assert page.locator('#energia-per-un-grado').evaluate('(e)=>e===document.activeElement')
            page.locator('#richiamo-2').click()
            assert page.locator('.chapter-notes').get_attribute('open') is not None
            page.locator('#nota-2 a').click()
            assert page.evaluate('location.hash') == '#richiamo-2'
            page.locator('.chapter-notes > summary').click()
            page.locator('[data-offline-credits]').click()
            assert page.locator('#crediti-autonomi').evaluate('(d)=>d.open')
            credit_text = page.locator('#crediti-autonomi').inner_text()
            assert all(t in credit_text for t in ['Engineering ToolBox','OpenStax','Kmckiern','Wyckoff','Piith','SIL OPEN FONT LICENSE'])
            page.locator('[data-close-credits]').click()
            toggle = page.locator('[data-water-toggle]')
            assert page.locator('#fig-02').get_attribute('data-playing') == 'true'
            toggle.click()
            assert page.locator('#fig-02').get_attribute('data-playing') == 'false'
            assert page.locator('#fig-02 img').evaluate('(i)=>i.src===i.dataset.still')
            toggle.click()
            assert page.locator('#fig-02').get_attribute('data-playing') == 'true'
            logo = page.locator('[data-logo-toggle]')
            logo.click()
            assert logo.get_attribute('aria-pressed') == 'true'
            logo.click()
            zoom = page.locator('#gra-01 .image-zoom')
            zoom.locator('summary').click()
            assert zoom.get_attribute('open') is not None
            assert zoom.locator('.zoom-scroll img').evaluate('(e)=>e.getBoundingClientRect().width') >= 900
            zoom.locator('summary').click()
            if width == 390:
                assert dimensions['contenutoTabella'] > dimensions['tabella']
                page.locator('.heat-table-scroll').evaluate('(e)=>e.scrollLeft=200')
                assert page.locator('.heat-table-scroll').evaluate('(e)=>e.scrollLeft') > 0
                page.locator('.heat-table-scroll').evaluate('(e)=>e.scrollLeft=0')
            assert all(page.locator('.equation').nth(i).evaluate('(e)=>e.scrollWidth<=e.clientWidth') for i in range(5))
            page.evaluate('scrollTo(0,0)')
            page.screenshot(path=str(WORK/f'anteprima-{width}.png'))
            for target,name in [('#fig-02','animazione'),('#tab-01','tabella'),('#gra-01','grafico'),('#formula-5','formula')]:
                node=page.locator(target)
                node.scroll_into_view_if_needed()
                node.screenshot(path=str(WORK/f'anteprima-{name}-{width}.png'))
            page.emulate_media(reduced_motion='reduce')
            page.wait_for_function('document.querySelector("#fig-02").dataset.playing === "false"')
            assert page.locator('#fig-02').get_attribute('data-playing') == 'false'
            assert logo.get_attribute('aria-pressed') == 'true'
            assert not errors and not requests, (errors, requests)
            results['viste'].append({'larghezza':width,**dimensions,'indice':True,'note_e_ritorni':True,
                'crediti_offline':True,'controlli_animazione':True,'movimento_ridotto':True,
                'grafico_ingrandibile':True,'formule_senza_overflow':True,'errori_js':errors,'richieste_rete':requests})
            context.close()
        context=browser.new_context(viewport={'width':390,'height':900},offline=True,java_script_enabled=False,reduced_motion='reduce')
        page=context.new_page();page.set_content(SOURCE,wait_until='load')
        page.locator('#indice > summary').click()
        assert page.locator('#indice').get_attribute('open') is not None
        page.locator('#indice > summary').click()
        page.locator('[data-offline-credits]').click()
        assert page.locator('#crediti-autonomi').is_visible()
        assert page.locator('#fig-02 img').evaluate('(i)=>i.currentSrc.startsWith("data:image/png")')
        results['senza_javascript']={'indice':True,'crediti_offline':True,'gif_statica_con_movimento_ridotto':True}
        context.close();browser.close()
    (WORK/'verifiche-browser.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')


if __name__ == '__main__':
    static_checks()
    browser_checks()
    shutil.copyfile(TARGET,WORK/'bozza.html')
    print('Controlli statici, desktop/mobile e senza JavaScript superati; anteprime e bozza.html aggiornati.')
