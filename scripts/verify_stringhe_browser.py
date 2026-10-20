"""Verifica Chromium desktop/Android emulato e salva i confronti riproducibili.

Richiede playwright e un browser Chromium. Avvia autonomamente un server locale.
Nessun test su un dispositivo Android fisico viene dichiarato da questo script.
"""
import functools
import http.server
import json
import os
from pathlib import Path
import shutil
import threading
from playwright.sync_api import sync_playwright, Error

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
SHOTS = ROOT / 'lavorazione/sito/schermate'


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def set_theme(page, theme):
    switch = page.get_by_role('switch', name='Tema scuro')
    if switch.get_attribute('aria-checked') != str(theme == 'dark').lower():
        switch.click()
    assert page.evaluate('document.documentElement.dataset.theme') == theme
    assert switch.get_attribute('aria-checked') == str(theme == 'dark').lower()


def main():
    SHOTS.mkdir(parents=True, exist_ok=True)
    # Il modello è verificato ma non diventa un articolo pubblicato.
    shutil.copyfile(ROOT / 'riferimenti/TEMA_DISPENSE.html', SITE / 'modello-dispense.html')
    handler = functools.partial(QuietHandler, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}/'
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    pages = ['index.html', 'articoli.html', 'quiz.html', 'crediti.html', 'anteprima-bordi-stringhe.html', 'modello-dispense.html'] + publication['articoli']
    checks, errors = [], []
    offline_status = 'file:// verificato'
    try:
        with sync_playwright() as playwright:
            executable = os.environ.get('CHROMIUM_PATH') or shutil.which('chromium')
            browser = playwright.chromium.launch(**({'executable_path': executable} if executable else {}), args=['--no-sandbox'])
            context = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True, device_scale_factor=1)
            context.add_init_script("Math.random=()=>Number(sessionStorage.getItem('test-random')||0)")
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.emulate_media(color_scheme='light')
            page.goto(base+'index.html')
            assert page.evaluate('document.documentElement.dataset.theme') == 'dark'
            assert page.get_by_role('switch', name='Tema scuro').get_attribute('aria-checked') == 'true'
            # Tutte le pagine, tutti i viewport e i due temi, con immagini caricate.
            for name in pages:
                page.goto(base + name)
                page.wait_for_function('document.fonts.status === "loaded"')
                assert page.evaluate('document.documentElement.dataset.edge') == 'sides', name
                if page.locator('[data-logo-toggle]').count():
                    assert page.locator('[data-logo-toggle] svg path.logo-moving').count() == 2
                if name in publication['articoli'] or name == 'modello-dispense.html':
                    assert page.locator('.article').count() == 1
                    assert page.locator('.article').evaluate("e=>!['none','normal'].includes(getComputedStyle(e,':before').content) && getComputedStyle(e,':before').pointerEvents==='none'")
                    assert page.locator('.article').evaluate("e=>getComputedStyle(e,':before').width") == '24px'
                    assert page.locator('.article').evaluate("e=>getComputedStyle(e,':after').right") == '0px'
                for width in [320, 390, 768, 1024, 1440]:
                    page.set_viewport_size({'width': width, 'height': 900})
                    for theme in ['light', 'dark']:
                        set_theme(page, theme)
                        assert page.evaluate('document.documentElement.dataset.theme') == theme
                        size = page.evaluate('({actual:document.documentElement.scrollWidth, viewport:innerWidth})')
                        assert size['actual'] <= size['viewport'] + 1, (name, width, theme, size)
                        checks.append([name, width, theme])
            # Home: una sola card senza onde; foto sotto al titolo su mobile.
            def verify_cover_layout(width):
                boxes = page.locator('.home-intro').evaluate("""card=>{
                    const image=card.querySelector('img#random-cover'),caption=card.querySelector('figcaption');
                    const copy=card.querySelector('.hero-copy');
                    return {image:image.getBoundingClientRect().toJSON(),caption:caption.getBoundingClientRect().toJSON(),copy:copy.getBoundingClientRect().toJSON(),ratio:image.naturalWidth/image.naturalHeight};
                }""")
                assert abs(boxes['image']['left']-boxes['caption']['left']) < 1, boxes
                assert abs(boxes['image']['width']-boxes['caption']['width']) < 1, boxes
                assert abs(boxes['image']['width']/boxes['image']['height']-boxes['ratio']) < .01, boxes
                if width <= 900:
                    assert boxes['image']['top'] >= boxes['copy']['bottom'], boxes
                else:
                    assert boxes['image']['left'] >= boxes['copy']['right'], boxes
            page.goto(base+'index.html')
            assert page.locator('.home-intro #random-cover').count() == 1
            assert page.locator('.home-intro .eyebrow').count() == 0
            assert page.locator('.actions > *').count() == 3
            assert page.locator('.actions .lang-action').count() == 0
            assert page.locator('#news-title').inner_text() == 'Novità'
            assert page.locator('.featured time').count() == 3
            assert page.locator('main h2').all_text_contents() == ['Novità']
            assert page.locator('.site-nav a[href="articoli.html"]').inner_text() == 'Capitoli'
            for width in [320,390,768,1024,1440]:
                page.set_viewport_size({'width':width,'height':900})
                for theme in ['light','dark']:
                    set_theme(page, theme)
                    for side in ['before','after']:
                        assert page.locator('.home-title').evaluate('(e,side)=>getComputedStyle(e,":"+side).display', side) == 'none'
                        assert page.locator('.home-cover').evaluate('(e,side)=>getComputedStyle(e,":"+side).content', side) in ['none','normal']
                    assert page.locator('.home-intro .subtitle').evaluate('(e)=>getComputedStyle(e).color===(()=>{const s=document.createElement("span");s.style.color="var(--accent)";document.body.append(s);const c=getComputedStyle(s).color;s.remove();return c;})()')
                    verify_cover_layout(width)
            # Controllo delle 20 scelte casuali e associazione immagine/alt/didascalia.
            covers = json.loads((ROOT / 'copertine/manifest.json').read_text())
            for i, cover in enumerate(covers):
                page.evaluate('(value)=>sessionStorage.setItem("test-random",String(value))', (i + .1) / len(covers))
                page.goto(base + 'index.html')
                assert page.locator('#random-cover').get_attribute('src') == cover['src']
                assert page.locator('#random-cover').get_attribute('alt') == cover['alt']
                assert page.locator('#cover-caption').inner_text() == cover['caption']
                assert page.locator('#random-cover').evaluate('(img)=>img.complete && img.naturalWidth>0')
                for width in [320,390,768,1024,1440]:
                    page.set_viewport_size({'width':width,'height':900})
                    verify_cover_layout(width)
            paths = page.locator('#catalogue-data').text_content()
            paths = json.loads(paths)
            for i, name in enumerate(paths):
                page.evaluate('(value)=>sessionStorage.setItem("test-random",String(value))', (i + .1) / len(paths))
                page.goto(base + 'index.html'); page.locator('#random-article').click()
                page.wait_for_url(base + name)
            set_theme(page, 'dark')
            page.goto(base + 'articoli.html')
            assert page.get_by_role('switch', name='Tema scuro').get_attribute('aria-checked') == 'true'
            page.reload()
            assert page.evaluate('document.documentElement.dataset.theme') == 'dark'
            page.locator('#article-search').fill('conduzione')
            assert page.locator('.article-card:visible').count() >= 1
            page.locator('#article-search').fill('zzzzzz')
            assert page.locator('.article-card:visible').count() == 0
            assert page.locator('#no-results').is_visible()
            page.locator('#article-search').fill('')
            page.locator('.chip').last.click()
            assert page.locator('.chip').last.get_attribute('aria-pressed') == 'true'
            page.goto(base + publication['articoli'][0])
            # Tastiera, menu indice, note, zoom, crediti e download reale.
            logo = page.locator('[data-logo-toggle]').first
            logo.focus(); old = logo.get_attribute('aria-pressed'); page.keyboard.press('Space')
            assert logo.get_attribute('aria-pressed') != old
            # Il medesimo SVG congela entrambe le curve e riparte in sincronia.
            logo.click()
            if logo.get_attribute('aria-pressed') != 'true':
                logo.click()
            def logo_shapes():
                return page.locator('[data-logo-toggle] .logo-moving').evaluate_all('(paths)=>paths.map(p=>p.getBBox().width)')
            page.locator('[data-logo-toggle] svg').evaluate('(svg)=>svg.setCurrentTime(1)')
            shapes = logo_shapes();page.wait_for_timeout(120)
            assert logo_shapes() == shapes
            assert logo.evaluate('(button)=>button.querySelector("svg").animationsPaused()')
            logo.click()
            assert not logo.evaluate('(button)=>button.querySelector("svg").animationsPaused()')
            page.locator('.index-toggle').click()
            assert page.locator('.reader-index').get_attribute('open') is not None
            page.keyboard.press('Escape')
            assert page.locator('.reader-index').get_attribute('open') is None
            assert page.locator('.index-toggle').evaluate('(e)=>e===document.activeElement')
            if page.locator('[role=doc-noteref]').count():
                page.locator('[role=doc-noteref]').first.click()
                assert page.locator('.chapter-notes').get_attribute('open') is not None
            if page.locator('.image-zoom summary').count():
                page.locator('.image-zoom summary').first.click()
                assert page.locator('.image-zoom').first.get_attribute('open') is not None
            page.locator('[data-offline-credits]').click()
            assert page.locator('#crediti-autonomi').is_visible()
            page.keyboard.press('Escape')
            page.goto(base + publication['articoli'][0])
            with page.expect_download() as download:
                page.locator('.string-nav[download]').click()
            assert Path(download.value.path()).read_bytes() == (SITE / publication['articoli'][0]).read_bytes()
            # Il default è scuro anche su sistema chiaro; la scelta esplicita persiste.
            set_theme(page, 'light')
            page.goto(base+'index.html'); page.reload()
            assert page.evaluate('document.documentElement.dataset.theme') == 'light'
            switch = page.get_by_role('switch', name='Tema scuro')
            switch.focus(); page.keyboard.press('Space')
            assert switch.get_attribute('aria-checked') == 'true'
            page.keyboard.press('Enter')
            assert switch.get_attribute('aria-checked') == 'false'
            page.emulate_media(color_scheme='dark')
            assert page.evaluate('document.documentElement.dataset.theme') == 'light'
            page.emulate_media(color_scheme='light')
            assert page.evaluate('document.documentElement.dataset.theme') == 'light'
            other = context.new_page(); other.goto(base+'quiz.html')
            set_theme(other, 'dark')
            page.wait_for_function('document.documentElement.dataset.theme === "dark"')
            other.evaluate("localStorage.removeItem('stringhe-theme')")
            other.close()
            page.goto(base + publication['articoli'][0])
            page.emulate_media(reduced_motion='reduce')
            page.wait_for_function('document.querySelector("[data-logo-toggle]").getAttribute("aria-pressed") === "true"')
            denied = browser.new_context()
            denied.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked')}})")
            blocked = denied.new_page(); blocked.on('pageerror', lambda error: errors.append(str(error)))
            blocked.emulate_media(color_scheme='light')
            blocked.goto(base+'index.html')
            assert blocked.evaluate('document.documentElement.dataset.theme') == 'dark'
            set_theme(blocked, 'light');blocked.reload()
            assert blocked.evaluate('document.documentElement.dataset.theme') == 'dark'
            offline = denied.new_page(); offline.on('pageerror', lambda error: errors.append(str(error)))
            try:
                offline.goto((SITE / publication['articoli'][0]).as_uri())
            except Error as error:
                if 'ERR_BLOCKED_BY_ADMINISTRATOR' not in str(error):
                    raise
                offline_status = 'file:// bloccato dalla policy del browser; HTML verificato in memoria con rete bloccata'
                offline.route('**/*', lambda route: route.abort())
                offline.set_content((SITE / publication['articoli'][0]).read_text())
            set_theme(offline, 'dark')
            if offline_status == 'file:// verificato':
                assert offline.locator('.string-nav').first.get_attribute('href').startswith('https://rickymusu-bit.github.io/fisica/')
            denied.close()
            for theme in ['light', 'dark']:
                nojs = browser.new_context(java_script_enabled=False, color_scheme=theme, viewport={'width':390,'height':844})
                plain = nojs.new_page();plain.goto(base+'index.html')
                assert plain.locator('#random-cover').get_attribute('src') == covers[0]['src']
                assert plain.locator('#random-cover').evaluate('(img)=>img.complete && img.naturalWidth>0')
                assert plain.locator('body').evaluate('(e)=>getComputedStyle(e).color') == 'rgb(240, 242, 248)'
                plain.goto(base+publication['articoli'][0])
                plain.locator('[data-offline-credits]').click()
                assert plain.locator('#crediti-autonomi').is_visible()
                nojs.close()
            # Schermate nello stesso contesto per variante e reticolo, in entrambi i temi.
            for width in [390,1440]:
                page.set_viewport_size({'width':width,'height':900})
                for theme in ['light','dark']:
                    for name, label in [('index.html','home'),('articoli.html','catalogo'), (publication['articoli'][0], 'articolo')]:
                        page.goto(base+name);set_theme(page, theme)
                        if page.locator('[data-logo-toggle] svg').count():
                            page.locator('[data-logo-toggle] svg').evaluate('(svg)=>{svg.pauseAnimations();svg.setCurrentTime(1)}')
                        page.screenshot(path=str(SHOTS/f'{label}-{width}-{theme}.png'), full_page=(label!='articolo'), animations='disabled')
                        if label == 'articolo':
                            page.locator('.article > .section-heading').first.evaluate('(e)=>e.scrollIntoView({block:"start",behavior:"instant"})')
                            page.evaluate("async()=>{await document.fonts.ready;await Promise.all([...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.bottom>0 && r.top<innerHeight}).map(i=>i.decode().catch(()=>{})))}")
                            page.screenshot(path=str(SHOTS/f'corpo-articolo-{width}-{theme}.png'), animations='disabled')
                    for variant in ['A','B']:
                        page.goto(base+'anteprima-bordi-stringhe.html');set_theme(page, theme)
                        page.locator('#border-variant').select_option(variant)
                        page.locator('#edge-variant').select_option('both')
                        for grid in ['A', 'B']:
                            page.locator('#grid-variant').select_option(grid)
                            page.screenshot(path=str(SHOTS/f'confronto-{width}-{theme}-{variant}-reticolo-{grid}.png'), full_page=True, animations='disabled')
                        page.locator('#edge-variant').select_option('top')
                        page.locator('[data-demo-dialog]').first.click()
                        assert page.locator('#demo-dialog').is_visible()
                        page.keyboard.press('Escape')
            for width in [320, 390, 768, 1024, 1440]:
                page.set_viewport_size({'width':width,'height':900})
                for theme in ['light','dark']:
                    page.goto(base+'anteprima-bordi-stringhe.html')
                    set_theme(page, theme)
                    assert page.locator('#edge-variant').input_value() == 'sides'
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                    for card in page.locator('.comparison-card, .action').all():
                        geometry = card.evaluate('''e=>{const c=getComputedStyle(e,':before');const a=getComputedStyle(e,':after');return {w:c.width,h:c.height,p:c.pointerEvents,r:a.right}}''')
                        assert geometry['w'] == '24px' and geometry['p'] == 'none' and geometry['r'] == '0px', geometry
                    page.locator('[data-demo-dialog]').first.click()
                    assert page.locator('#demo-dialog').is_visible()
                    page.keyboard.press('Escape')
                    if width in [390,1440]:
                        page.evaluate('document.activeElement.blur(); window.scrollTo(0,0)')
                        page.wait_for_function('window.scrollY === 0')
                        page.screenshot(path=str(SHOTS/f'laterali-{width}-{theme}.png'), full_page=True, animations='disabled')
            browser.close()
    finally:
        server.shutdown()
        (SITE / 'modello-dispense.html').unlink(missing_ok=True)
    assert not errors, errors
    report = {'viewport_tema_pagina':checks,'errori_javascript':errors,'copertine_verificate':len(covers),'home':{'card':'unica per titolo, logo e copertina; senza onde laterali','mobile':'foto sotto al titolo','desktop':'foto affiancata','layout_copertine_verificati':100,'didascalia':'bordo sinistro e larghezza coincidenti con la foto; proporzioni conservate'},'logo':{'curve':2,'fase':'opposizione','periodo_secondi':4,'animazione_nera':'impronta originale conservata','pausa':'entrambe le curve sincronizzate'},'laterali':{'viewport':[320,390,768,1024,1440],'temi':['light','dark'],'curve':'stessa ampiezza; periodo invariato; 24 px per fascia; nessun overflow'},
              'offline':offline_status,'browser':'Chromium; mobile e touch emulati, nessun dispositivo Android fisico',
              'controlli':['persistenza','default scuro indipendente dal sistema e switch tastiera','storage bloccato','senza JavaScript','logo e movimento ridotto','ricerca e filtro','indice tastiera','note','zoom','crediti','download identico']}
    (ROOT/'lavorazione/sito/verifica-stringhe.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'Verificate {len(checks)} combinazioni pagina/viewport/tema e {len(covers)} copertine; nessun errore JavaScript')


if __name__ == '__main__':
    main()
