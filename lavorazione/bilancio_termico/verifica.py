"""Controlli scientifici, integrità delle immagini e lettura offline dell'articolo."""
from pathlib import Path
import base64
import hashlib
import json
import re
import shutil
import sys
from lxml import html
from playwright.sync_api import sync_playwright
from realizza import META, ROOT, WORK, TARGET, temperatures


def static_checks():
    source = TARGET.read_text()
    doc = html.fromstring(source)
    theme = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
    # Il codice canonico è riutilizzato integralmente, inclusi font e logo.
    for tag in ['style', 'script']:
        for block in re.findall(r'<' + tag + r'[^>]*>[\s\S]*?</' + tag + '>', theme):
            assert block in source, 'Componente del tema diverso: ' + tag
    ids = doc.xpath('//@id')
    assert len(ids) == len(set(ids)), 'ID duplicati'
    assert not [link for link in doc.xpath('//a/@href') if link.startswith('#') and link != '#' and link[1:] not in ids]
    checks = []
    for key, (name, *_) in META.items():
        figure = doc.get_element_by_id(key.lower())
        raw = base64.b64decode(figure.xpath('.//img/@src')[0].split(',', 1)[1])
        assert raw == (WORK / 'risorse' / name).read_bytes()
        checks.append({'file': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
    assert len(doc.xpath('//figure[contains(@class,"cover")]')) == 1
    assert len(doc.xpath('//ol[@class="questions"]/li')) == 9
    assert len(doc.xpath('//div[@class="equation"]')) == 7
    assert len(doc.xpath('//details[@class="chapter-notes"]//li')) == 3
    assert len(doc.xpath('//article//figure')) == 5
    assert len(doc.xpath('//nav[@class="credits-navigation"]/a')) == 1
    assert not re.search(r'\\[\[\](]|\[IMMAGINE|\[GRAFICO|\[Didascalia', doc.text_content())
    assert not any(mark in doc.xpath('//footer')[0].text_content() for mark in '·•⋅')
    graph = html.fromstring((WORK / 'risorse/temperatura-tempo.svg').read_text())
    assert not any(mark in ''.join(graph.xpath('//text/text()')) for mark in '·•⋅')
    assert 'Materia Oscura ·' not in source
    assert TARGET.stat().st_size < 20_000_000
    sys.path.insert(0, str(ROOT / 'scripts'))
    import credits
    registry = credits.load_registry()
    assert not credits.unassociated(registry, TARGET.name)
    credits_text = doc.get_element_by_id('crediti-autonomi').text_content()
    for text in ['François Boucher', 'The Yorck Project', 'Zenodot', 'Julius Schorzman',
                 'NOTE: I only require attribution', 'NIAID', 'Burst', 'Andy Mabbett', 'SIL OPEN FONT LICENSE']:
        assert text in credits_text, text
    assert temperatures(0) == (80, 20)
    maximum_balance_error = 0
    previous = temperatures(0)
    initial_energy = 0.100 * 4180 * 80 + 0.050 * 4180 * 20
    for t in range(301):
        coffee, milk = temperatures(t)
        energy = 0.100 * 4180 * coffee + 0.050 * 4180 * milk
        maximum_balance_error = max(maximum_balance_error, abs(energy - initial_energy))
        assert 60 < coffee <= previous[0] and previous[1] <= milk < 60
        assert abs((80 - coffee) * 0.100 - (milk - 20) * 0.050) < 1e-10
        previous = coffee, milk
    assert maximum_balance_error < 1e-9
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    assert TARGET.name in publication['articoli']
    assert (ROOT / '_site' / TARGET.name).exists()
    report = {'bytes': TARGET.stat().st_size, 'sha256': hashlib.sha256(TARGET.read_bytes()).hexdigest(),
              'tema_css_script_identici': True, 'immagini_originali': checks, 'domande': 9,
              'formule': 7, 'note': 3, 'id_univoci_ancore_risolte': True,
              'grafico': {'temperature_iniziali': [80, 20], 'masse_kg': [0.1, 0.05],
                         'equilibrio_C': 60, 'tempo_caratteristico_s_ipotizzato': 60,
                         'campioni_verificati': 301, 'errore_massimo_bilancio_J': maximum_balance_error,
                         'monotonia_e_assenza_incroci': True, 'dati_sperimentali': False},
              'ammesso_a_pages': True}
    (WORK / 'verifiche-finali.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


def browser_checks():
    source = TARGET.read_text()
    results = {'caricamento': 'HTML autonomo offline, rete disattivata', 'viste': []}
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
        for width in [1280, 390]:
            context = browser.new_context(viewport={'width': width, 'height': 900}, offline=True)
            page = context.new_page()
            errors, requests = [], []
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.on('request', lambda r: requests.append(r.url) if not r.url.startswith('data:') else None)
            page.set_content(source, wait_until='load')
            page.evaluate('document.fonts.ready')
            page.wait_for_function('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)')
            assert page.locator('h1').inner_text() == 'Il bilancio termico'
            assert page.locator('.kicker').inner_text() == 'MATERIA E CALORE'
            assert page.evaluate('document.documentElement.scrollWidth') == width
            assert page.evaluate("document.fonts.check('21px Lexend')")
            formula_sizes = page.locator('.equation').evaluate_all('(es)=>es.map(e=>({width:e.clientWidth,content:e.scrollWidth}))')
            assert all(e['content'] <= e['width'] for e in formula_sizes), formula_sizes
            assert not page.locator('.chapter-notes').evaluate('(e)=>e.open')
            page.locator('#indice > summary').click()
            assert page.locator('#indice').evaluate('(e)=>e.open')
            page.keyboard.press('Escape')
            assert not page.locator('#indice').evaluate('(e)=>e.open')
            page.locator('#indice > summary').click()
            page.locator('.sidebar-nav a[href="#temperatura-e-masse"]').click()
            assert not page.locator('#indice').evaluate('(e)=>e.open')
            page.wait_for_function('document.activeElement.id==="temperatura-e-masse"')
            page.locator('#richiamo-3').click()
            assert page.locator('.chapter-notes').evaluate('(e)=>e.open')
            page.locator('#nota-3 a').click()
            assert page.evaluate('location.hash') == '#richiamo-3'
            page.locator('.chapter-notes > summary').click()
            page.locator('[data-offline-credits]').click()
            assert page.locator('#crediti-autonomi').evaluate('(e)=>e.open')
            assert 'François Boucher' in page.locator('#crediti-autonomi').inner_text()
            assert page.locator('#crediti-autonomi a', has_text='Crediti di tutti gli articoli').count() == 1
            page.keyboard.press('Escape')
            toggle = page.locator('[data-logo-toggle]')
            toggle.click(); assert toggle.get_attribute('aria-pressed') == 'true'
            toggle.click(); assert toggle.get_attribute('aria-pressed') == 'false'
            zoom = page.locator('#gra-02 .image-zoom')
            zoom.locator('summary').click()
            assert zoom.evaluate('(e)=>e.open')
            assert zoom.locator('.zoom-scroll img').evaluate('(e)=>e.getBoundingClientRect().width') >= 960
            if width == 390:
                zoom.locator('.zoom-scroll').evaluate('(e)=>e.scrollLeft=300')
                assert zoom.locator('.zoom-scroll').evaluate('(e)=>e.scrollLeft') > 0
            zoom.locator('summary').click()
            page.emulate_media(reduced_motion='reduce')
            page.wait_for_function('document.querySelector("[data-logo-toggle]").getAttribute("aria-pressed")==="true"')
            page.evaluate('scrollTo(0,0)')
            page.screenshot(path=str(WORK / f'anteprima-{width}.png'))
            for selector, name in [('#gra-02', 'grafico'), ('#formula-5', 'formula'), ('#fig-03', 'versamento'), ('#fig-04', 'tazza')]:
                page.locator(selector).scroll_into_view_if_needed()
                page.locator(selector).screenshot(path=str(WORK / f'anteprima-{name}-{width}.png'))
            assert not errors and not requests, (errors, requests)
            results['viste'].append({'larghezza': width, 'overflow_pagina': False, 'formule': formula_sizes,
                'indice_esc_focus': True, 'note_e_ritorni': True, 'crediti_offline': True,
                'grafico_ingrandimento_scorrimento': True, 'logo_pausa_movimento_ridotto': True,
                'errori_js': errors, 'richieste_rete': requests})
            context.close()
        context = browser.new_context(viewport={'width': 390, 'height': 900}, offline=True, java_script_enabled=False, reduced_motion='reduce')
        page = context.new_page(); page.set_content(source, wait_until='load')
        page.locator('#indice > summary').click()
        assert page.locator('#indice').evaluate('(e)=>e.open')
        page.locator('#indice > summary').click()
        page.locator('#gra-02 .image-zoom > summary').click()
        assert page.locator('#gra-02 .image-zoom').evaluate('(e)=>e.open')
        page.locator('[data-offline-credits]').click()
        assert page.locator('#crediti-autonomi').is_visible()
        results['senza_javascript'] = {'indice': True, 'crediti_offline': True, 'grafico_ingrandibile': True}
        context.close(); browser.close()
    (WORK / 'verifiche-browser.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    shutil.copyfile(TARGET, WORK / 'bozza.html')


if __name__ == '__main__':
    static_checks()
    browser_checks()
    print('Controlli scientifici, immagini, tema, lettura offline desktop/mobile e senza JavaScript superati.')
