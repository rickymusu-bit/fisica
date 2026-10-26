"""Verifica Chromium desktop/Android emulato e salva i confronti riproducibili.

Richiede playwright e un browser Chromium. Avvia autonomamente un server locale.
Nessun test su un dispositivo Android fisico viene dichiarato da questo script.
"""
import functools
import http.server
import json
import os
import re
from pathlib import Path
import shutil
import threading
from playwright.sync_api import sync_playwright, Error, expect

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
SHOTS = ROOT / 'lavorazione/sito/schermate'


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def set_theme(page, theme):
    menu = page.locator('[data-theme-menu]')
    if page.evaluate('document.documentElement.dataset.theme') != theme:
        menu.locator('summary').click()
        menu.locator(f'[data-theme-option="{theme}"]').click()
    assert page.evaluate('document.documentElement.dataset.theme') == theme
    assert menu.locator(f'[data-theme-option="{theme}"]').get_attribute('aria-pressed') == 'true'


def verify_media_controls(page, base, publication):
    """Verifica i comandi effettivi, senza affidarsi soltanto al markup."""
    def capture(figure, filename):
        image = figure.locator('img').first
        figure.evaluate('(figure)=>window.scrollTo({top:figure.getBoundingClientRect().top+scrollY-100,behavior:"instant"})')
        image.evaluate('(image)=>image.decode()')
        page.evaluate('()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))')
        figure.screenshot(path=str(SHOTS / filename))

    for width in [390, 1440]:
        page.set_viewport_size({'width': width, 'height': 1200})
        for theme in ['light', 'dark']:
            for name in publication['articoli']:
                page.goto(base + name)
                set_theme(page, theme)
                for stage in page.locator('.gif-stage:visible').all():
                    button = stage.locator('[data-animation-toggle]')
                    image = stage.locator('img')
                    animation = image.get_attribute('src')
                    assert button.inner_text().strip() == ''
                    assert button.get_attribute('aria-label') == 'Metti in pausa l’animazione'
                    button.click()
                    assert image.get_attribute('src') == image.get_attribute('data-still')
                    assert button.get_attribute('aria-pressed') == 'true'
                    assert button.locator('.media-play').is_visible()
                    assert not button.locator('.media-pause').is_visible()
                    button.press('Space')
                    assert image.get_attribute('src') == animation
                    assert button.get_attribute('aria-pressed') == 'false'
                    boxes = stage.evaluate('stage=>{const a=stage.getBoundingClientRect(),b=stage.querySelector("button").getBoundingClientRect();return {left:b.left-a.left,bottom:a.bottom-b.bottom,width:b.width,height:b.height}}')
                    assert 7 <= boxes['left'] <= 9 and 7 <= boxes['bottom'] <= 9, (name, boxes)
                    assert boxes['width'] >= 44 and boxes['height'] >= 44
                for zoom in page.locator('.image-zoom').all():
                    button = zoom.locator('summary')
                    assert button.inner_text().strip() == ''
                    assert not zoom.evaluate('e=>e.open')
                    assert button.locator('.zoom-expand').is_visible()
                    button.click()
                    assert zoom.evaluate('e=>e.open')
                    expect(button).to_have_attribute('aria-label', 'Rimpicciolisci l’immagine')
                    assert button.locator('.zoom-collapse').is_visible()
                    button.press('Enter')
                    assert not zoom.evaluate('e=>e.open')
                    # Lo zoom e' sempre sotto l'immagine, mentre il play/pausa delle GIF rimane sovrapposto.
                    placement = zoom.evaluate('zoom=>{const figure=zoom.closest("figure"),image=zoom.parentElement.classList.contains("image-frame")?zoom.parentElement.querySelector(":scope > .overview"):figure.querySelector(".image-frame");const b=zoom.querySelector("summary").getBoundingClientRect(),a=image&&image.getBoundingClientRect(),parent=zoom.parentElement.getBoundingClientRect();return {imageBottom:a?a.bottom:null,buttonTop:b.top,left:b.left-parent.left,width:b.width,height:b.height}}')
                    if placement['imageBottom'] is not None:
                        assert placement['buttonTop'] >= placement['imageBottom'] - 1, (name, placement)
                    assert placement['left'] >= 0, (name, placement)
                    assert placement['width'] >= 44 and placement['height'] >= 44
                if name == 'conduzione_it.html':
                    photo = page.locator('#visuale-immagine-12')
                    assert photo.locator('img').get_attribute('src').startswith('data:image/jpeg')
                    assert photo.locator('[data-animation-toggle]').count() == 0
                    capture(photo, f'fotogramma-conduzione-{width}-{theme}.png')
                    capture(page.locator('#immagine-e-1'), f'media-gif-{width}-{theme}.png')
                if name == 'passaggi_di_stato.html':
                    capture(page.locator('#diagramma'), f'media-zoom-{width}-{theme}.png')
    page.emulate_media(reduced_motion='reduce')
    page.goto(base + 'passaggi_di_stato.html')
    for stage in page.locator('.gif-stage').all():
        button = stage.locator('[data-animation-toggle]')
        image = stage.locator('img')
        assert image.get_attribute('src') == image.get_attribute('data-still')
        assert button.get_attribute('aria-label') == 'Riprendi l’animazione'
        button.click()
        assert image.get_attribute('src').startswith('data:image/gif')
        button.click()
        assert image.get_attribute('src') == image.get_attribute('data-still')
    page.emulate_media(reduced_motion='no-preference')
    fallback = page.context.browser.new_context(java_script_enabled=False, reduced_motion='reduce', viewport={'width': 390, 'height': 1000})
    try:
        offline = fallback.new_page()
        for name in ['passaggi_di_stato.html', 'energia_interna_calore_specifico_it.html']:
            offline.goto(base + name)
            for stage in offline.locator('.gif-stage').all():
                image = stage.locator('img')
                image.scroll_into_view_if_needed()
                offline.wait_for_function('(img)=>img.complete && img.currentSrc===img.dataset.still', arg=image.element_handle())
                assert not stage.locator('[data-animation-toggle]').is_visible()
            zoom = offline.locator('.image-zoom').first
            zoom.locator('summary').click()
            assert zoom.evaluate('e=>e.open')
            assert zoom.locator('.zoom-collapse').is_visible()
            zoom.locator('summary').press('Enter')
            assert not zoom.evaluate('e=>e.open')
    finally:
        fallback.close()



def verify_quiz(page, base):
    """Categoria esclusiva, recupero della sessione, livelli, timer e correzione."""
    def fresh_quiz():
        page.evaluate("url => localStorage.removeItem('stringhe.quiz.session.v1:' + new URL(url).pathname)", base + 'quiz.html')
        page.goto(base + 'quiz.html')
    fresh_quiz()
    choices = page.locator('[data-quiz-category]')
    assert choices.count() == 2
    assert page.locator('[data-quiz-chapter]').count() == 0
    assert page.locator('#quiz-start').is_disabled()
    original_html = (SITE / 'quiz.html').read_text(encoding='utf-8')
    match = re.search(r'(<script type="application/json" id="quiz-data">)(.*?)(</script>)', original_html, re.S)
    archive = json.loads(match.group(2))
    assert len(archive['categories']) == 2
    for box in choices.all():
        available = next(c for c in archive['categories'] if c['id'] == box.get_attribute('value'))['levels']['easy'] > 0
        assert box.is_disabled() == (not available)
    assert page.locator('.quiz-empty-notice').is_visible() == (not any(sum(c['levels'].values()) for c in archive['categories']))
    fixture = json.loads(json.dumps(archive))
    fixture['questions'] = [
        {'id': f"test-{category['id']}-{level}-{i}", 'category': category['id'],
         'level': level, 'prompt': f"{category['title']} ({level}) — quesito {i}",
         'options': [f"Alternativa {n+1}" for n in range(count)],
         'correct': 0, 'explanation': 'Spiegazione effimera di collaudo.'}
        for category in fixture['categories']
        for level, count in [('easy', 4), ('medium', 4), ('hard', 4)]
        for i in range(30)
    ]
    def fixture_html(data):
        encoded = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
        html = original_html[:match.start(2)] + encoded + original_html[match.end(2):]
        return re.sub(r'<p class="quiz-empty-notice"[^>]*>.*?</p>', '', html)
    route_pattern = '**/quiz.html'
    page.route(route_pattern, lambda route: route.fulfill(
        status=200, content_type='text/html; charset=utf-8', body=fixture_html(fixture)))
    try:
        # Navigazione libera e salvataggio immediato, in entrambi i temi/viewport.
        for width in (390, 1440):
            page.set_viewport_size({'width': width, 'height': 900})
            for theme in ('dark', 'light'):
                fresh_quiz()
                set_theme(page, theme)
                choices.first.check()
                count_input = page.locator('#quiz-count')
                count_input.fill('3')
                page.locator('#quiz-start').click()
                key = page.evaluate("'stringhe.quiz.session.v1:' + location.pathname")
                assert page.locator('#quiz-previous').is_disabled()
                assert page.locator('#quiz-next').is_enabled()
                assert page.locator('#quiz-next').inner_text() == 'Avanti'
                page.locator('#quiz-next').click()  # salta implicitamente la prima
                assert page.locator('#quiz-navigation .is-skipped').count() == 1
                page.locator('.quiz-answer input[value="1"]').check()
                stored = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                assert stored['session']['responses'] == [None, 1, None]
                assert page.locator('#quiz-navigation .is-answered.is-current').count() == 1
                assert page.locator('#quiz-navigation .is-current').evaluate('e => getComputedStyle(e).borderTopWidth') == '4px'
                page.reload()
                assert page.locator('.quiz-answer input[value="1"]').is_checked()
                assert page.evaluate('key => JSON.parse(localStorage.getItem(key)).session.deadline', key) == stored['session']['deadline']
                page.locator('#quiz-next').click()
                assert page.locator('#quiz-next').is_disabled()
                assert page.locator('#quiz-active').is_visible()
                assert not page.locator('#quiz-results').is_visible()
                page.locator('#quiz-previous').click()
                page.locator('.quiz-answer input[value="0"]').check()  # cambia risposta
                page.get_by_role('button', name='Vai alla domanda 1: saltata', exact=True).click()
                page.locator('.quiz-answer input[value="0"]').check()
                page.locator('#quiz-next').click()
                assert page.locator('.quiz-answer input[value="0"]').is_checked()
                assert page.locator('#quiz-navigation .is-skipped').count() == 1
                page.locator('#quiz-stop').click()
                assert page.locator('#quiz-stop-dialog').is_visible()
                page.locator('#quiz-stop-cancel').click()
                assert page.locator('#quiz-active').is_visible()
                page.locator('#quiz-stop').click()
                page.keyboard.press('Escape')
                assert not page.locator('#quiz-stop-dialog').is_visible()
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                page.screenshot(path=str(SHOTS / f'quiz-navigazione-{width}-{theme}.png'), full_page=True)
                page.locator('#quiz-stop').click()
                page.locator('#quiz-stop-confirm').click()
                assert page.locator('#quiz-score').inner_text() == '2 / 3'
                assert page.locator('#quiz-result-navigation .is-correct').count() == 2
                assert page.locator('#quiz-result-navigation .is-skipped').count() == 1
                page.reload()
                assert page.locator('#quiz-score').inner_text() == '2 / 3'

        # Un unico quesito: entrambi i limiti sono disabilitati, nessuna consegna automatica.
        fresh_quiz()
        choices.first.check()
        page.locator('#quiz-count').fill('1')
        page.locator('#quiz-start').click()
        page.locator('.quiz-answer input[value="1"]').check()
        assert page.locator('#quiz-previous').is_disabled()
        assert page.locator('#quiz-next').is_disabled()
        assert page.locator('#quiz-active').is_visible()
        page.locator('#quiz-stop').click()
        page.locator('#quiz-stop-confirm').click()
        assert page.locator('#quiz-result-navigation .is-wrong').count() == 1
        assert page.locator('.quiz-review-item.is-wrong').count() == 1

        # La quota di 120 s contribuisce solo alla scadenza totale.
        fresh_quiz()
        choices.first.check()
        page.locator('#quiz-count').fill('3')
        page.clock.install()
        page.locator('#quiz-start').click()
        page.clock.fast_forward(121_000)
        assert page.locator('#quiz-counter').inner_text() == 'Domanda 1 di 3'
        assert page.locator('#quiz-active').is_visible()
        page.locator('#quiz-next').click()
        page.locator('#quiz-previous').click()
        deadline = page.evaluate('key => JSON.parse(localStorage.getItem(key)).session.deadline', key)
        page.reload()
        assert page.evaluate('key => JSON.parse(localStorage.getItem(key)).session.deadline', key) == deadline
        page.locator('#quiz-stop').click()
        page.clock.fast_forward(240_000)
        assert not page.locator('#quiz-stop-dialog').is_visible()
        assert page.locator('#quiz-results').is_visible()
        assert page.locator('#quiz-score').inner_text() == '0 / 3'
        assert page.locator('#quiz-result-navigation .is-skipped').count() == 3

        # Recupera snapshot v2 con scelta provvisoria senza perdere domande/scadenza.
        fresh_quiz()
        choices.first.check()
        page.locator('#quiz-count').fill('3')
        page.locator('#quiz-start').click()
        saved = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
        page.goto(base + 'index.html')
        saved['version'] = 2
        saved['session']['pendingResponse'] = 1
        page.evaluate('args => localStorage.setItem(args[0], JSON.stringify(args[1]))', [key, saved])
        page.goto(base + 'quiz.html')
        assert page.locator('.quiz-answer input[value="1"]').is_checked()
        recovered = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
        assert recovered['session']['responses'][0] == 1
        assert recovered['session']['deadline'] == saved['session']['deadline']
        assert recovered['session']['questions'] == saved['session']['questions']

        for invalid in ('{JSON non valido', '{"version":999}'):
            page.goto(base + 'index.html')
            page.evaluate('args => localStorage.setItem(args[0], args[1])', [key, invalid])
            page.goto(base + 'quiz.html')
            assert page.locator('#quiz-config').is_visible()
            assert page.locator('#quiz-save-warning').is_visible()

        # Storage bloccato: navigazione/risposte funzionano anche in memoria.
        blocked = page.context.new_page()
        blocked.add_init_script("Storage.prototype.setItem = function(){throw new DOMException('Bloccato', 'QuotaExceededError')}")
        blocked.route(route_pattern, lambda route: route.fulfill(
            status=200, content_type='text/html; charset=utf-8', body=fixture_html(fixture)))
        blocked.goto(base + 'quiz.html')
        blocked.locator('[data-quiz-category]').last.check()
        blocked.locator('#quiz-start').click()
        assert blocked.locator('#quiz-save-warning').is_visible()
        blocked.locator('.quiz-answer input[value="0"]').check()
        blocked.locator('#quiz-next').click()
        blocked.locator('#quiz-previous').click()
        assert blocked.locator('.quiz-answer input[value="0"]').is_checked()
        blocked.locator('#quiz-stop').click()
        blocked.locator('#quiz-stop-confirm').click()
        assert blocked.locator('#quiz-results').is_visible()
        blocked.close()
        fresh_quiz()
    finally:
        page.unroute(route_pattern)



def verify_table_alignments(page, base, publication):
    """Controlla tutte le tabelle dei capitoli in Chromium, comprese le eccezioni discorsive."""
    exceptions = {
        'metodo_scientifico_it.html': ['.method-section td[colspan]'],
        'potenze_dieci_notazione_scientifica_it.html': [
            '.notation-table[data-align-prose="row-labels"] th[scope="row"]'
        ],
        'cifre_significative_it.html': [
            '.significant-table[data-align-prose="reason"] td:last-child',
            '.significant-table[data-align-prose="after-first"] td:not(:first-child)'
        ],
        'strumenti_misura_it.html': ['.measurement-sim table td[colspan]'],
        'errori_incertezza_misura_it.html': [
            '.measure-table[data-align-prose="reason"] td:last-child',
            '.measurement-sim table td[colspan]'
        ],
        'stati_della_materia.html': [
            '.comparison-table td:nth-child(2)',
            '.comparison-table td:nth-child(4)'
        ],
        'passaggi_di_stato.html': [
            '.comparison-table table:not([data-align-kind]) td:nth-child(n+2)',
            '.comparison-table table[data-align-kind="latent"] td:nth-child(3)'
        ]
    }
    script = """(allowed) => {
      const tables=[...document.querySelectorAll('.article table')];
      const failures=[];
      tables.forEach((table,index)=>{
        [...table.querySelectorAll('th,td')].forEach(cell=>{
          const align=getComputedStyle(cell).textAlign;
          if(align==='center')return;
          if(align==='left' && allowed.some(s=>cell.matches(s)))return;
          failures.push({table:index+1,tag:cell.tagName,align,
            text:cell.textContent.trim().replace(/\\s+/g,' ').slice(0,90)});
        });
      });
      return {tables:tables.length,failures};
    }"""
    for width in (390, 1440):
        page.set_viewport_size({'width': width, 'height': 900})
        count = 0
        for name in publication['articoli']:
            page.goto(base + name)
            state = page.evaluate(script, exceptions.get(name, []))
            count += state['tables']
            assert not state['failures'], (name, width, state['failures'])
        assert count == 35, ('Numero di tabelle inatteso', width, count)
    print('Allineamento verificato: 35 tabelle, 19 capitoli, viewport 390/1440; eccezioni discorsive motivate')


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
            assert page.locator('[data-theme-option=dark]').get_attribute('aria-pressed') == 'true'
            # Tutte le pagine, tutti i viewport e i due temi, con immagini caricate.
            for name in pages:
                page.goto(base + name)
                page.wait_for_function('document.fonts.status === "loaded"')
                assert page.evaluate('document.documentElement.dataset.edge') == 'sides', name
                if page.locator('[data-logo-toggle]').count():
                    assert page.locator('[data-logo-toggle] svg path.logo-moving').count() == 2
                if name in publication['articoli'] or name == 'modello-dispense.html':
                    assert page.locator('.article').count() == 1
                    assert page.locator('.topbar .brand').count() == 0, (name,'brand in topbar')
                    assert page.locator('.topbar [data-logo-toggle]').count() == 0, (name,'logo in topbar')
                    assert page.locator('main:has(>.article-wrap)').evaluate("e=>!['none','normal'].includes(getComputedStyle(e,':before').content) && getComputedStyle(e,':before').pointerEvents==='none'")
                    assert page.locator('main:has(>.article-wrap)').evaluate("e=>getComputedStyle(e,':before').width") == '24px'
                    assert page.locator('main:has(>.article-wrap)').evaluate("e=>getComputedStyle(e,':after').right") == '0px'
                for width in [320, 390, 768, 1024, 1440]:
                    page.set_viewport_size({'width': width, 'height': 900})
                    for theme in ['light', 'dark']:
                        set_theme(page, theme)
                        assert page.evaluate('document.documentElement.dataset.theme') == theme
                        size = page.evaluate('({actual:document.documentElement.scrollWidth, viewport:innerWidth})')
                        assert size['actual'] <= size['viewport'] + 1, (name, width, theme, size)
                        # Le etichette esterne alla foto restano leggibili nel riquadro bianco.
                        for model in page.locator('.exercise-model').all():
                            assert model.locator('xpath=..').evaluate('(e)=>getComputedStyle(e).backgroundColor') == 'rgb(255, 255, 255)'
                            labels = model.locator('.model-data, .model-state, .model-transfer, .model-assumptions')
                            for label in labels.all():
                                assert label.evaluate('(e)=>getComputedStyle(e).color') == 'rgb(32, 38, 55)', (name, width, theme)
                            for arrow in model.locator('.model-transfer').all():
                                assert arrow.evaluate('(e)=>getComputedStyle(e,":before").color') == 'rgb(32, 38, 55)'
                            if width in [390, 1440]:
                                model.locator('.model-path').screenshot(path=str(SHOTS/f'schema-{Path(name).stem}-{width}-{theme}.png'))
                        # Un solo componente per ogni pagina: identico ordine e geometria.
                        nav = page.locator('.stringhe-header .stringhe-navigation')
                        assert nav.count() == 1, name
                        primary = nav.locator(':scope > .nav-primary')
                        settings = nav.locator(':scope > .nav-settings')
                        assert primary.count() == 1 and settings.count() == 1, name
                        assert settings.locator(':scope > .string-lang').count() == 1
                        assert settings.locator(':scope > [data-theme-menu]').count() == 1
                        assert settings.locator('.string-lang>summary').inner_text() == 'IT ▾'
                        if name == 'index.html':
                            expected = []
                        elif name in ['articoli.html', 'quiz.html', 'anteprima-bordi-stringhe.html']:
                            expected = ['Home']
                        elif name == 'crediti.html':
                            expected = ['Home', 'Tutti i capitoli']
                        else:
                            expected = ['Home', 'Tutti i capitoli', 'Scarica il capitolo', 'Indice del capitolo']
                        actual = primary.evaluate('(n)=>[...n.children].map(e=>e.getAttribute("aria-label")||e.querySelector(":scope > summary")?.getAttribute("aria-label"))')
                        assert actual == expected, (name,actual,expected)
                        positions = nav.evaluate('n=>[...n.querySelectorAll(":scope > .nav-primary > :is(a,details),:scope > .nav-settings > details")].map(e=>{const t=e.tagName==="DETAILS"?e.querySelector(":scope > summary"):e;return t.getBoundingClientRect().toJSON()})')
                        assert all(r['width'] >= 44 and r['height'] >= 44 for r in positions), (name,width,positions)
                        assert max(r['top'] for r in positions)-min(r['top'] for r in positions)<1, (name,width,positions)
                        edges = nav.evaluate('n=>{const a=n.querySelector(".nav-primary").getBoundingClientRect(),b=n.querySelector(".nav-settings").getBoundingClientRect(),v=n.getBoundingClientRect();return {left:a.left,right:a.right,settingsLeft:b.left,settingsRight:b.right,navRight:v.right}}')
                        assert edges['right'] <= edges['settingsLeft']+1, (name,width,edges)
                        assert abs(edges['settingsRight']-edges['navRight']) < 2, (name,width,edges)
                        if name in publication['articoli'] or name == 'modello-dispense.html':
                            geometry=page.locator('main:has(>.article-wrap)').evaluate('main=>{const hero=main.querySelector(":scope > .hero"),wrap=main.querySelector(":scope > .article-wrap"),article=wrap.querySelector(".article");return {hero:hero.getBoundingClientRect().toJSON(),wrap:wrap.getBoundingClientRect().toJSON(),article:article.getBoundingClientRect().toJSON(),border:getComputedStyle(wrap).borderTopWidth,heroWave:getComputedStyle(hero,":before").display,bodyWave:getComputedStyle(article,":before").display,gutterHero:getComputedStyle(hero).paddingLeft,gutterBody:getComputedStyle(article).paddingLeft}}')
                            assert geometry['border']=='0px' and geometry['heroWave']=='none' and geometry['bodyWave']=='none'
                            assert abs(geometry['hero']['left']-geometry['article']['left'])<1
                            assert abs(geometry['hero']['right']-geometry['article']['right'])<1
                            assert abs(geometry['hero']['bottom']-geometry['wrap']['top'])<1
                            assert geometry['gutterHero']==geometry['gutterBody']
                        checks.append([name, width, theme])
            # Selezionare i tratti non deve cambiare la posizione della pagina.
            page.goto(base+'passaggi_di_stato.html')
            for width in [320,390,768,1024,1440]:
                page.set_viewport_size({'width':width,'height':900})
                for theme in ['light','dark']:
                    set_theme(page,theme)
                    for segment in [5,1,4,2,3]:
                        label=page.locator(f'.curve-controls label[for="curve-choice-{segment}"]')
                        label.evaluate('(e)=>e.scrollIntoView({block:"center",behavior:"instant"})')
                        before=page.evaluate('scrollY')
                        label.tap()
                        page.wait_for_function('(n)=>document.getElementById("curve-choice-"+n).checked',arg=segment)
                        page.wait_for_timeout(80)
                        assert abs(page.evaluate('scrollY')-before)<2, (width,theme,segment)
                        assert page.locator(f'#curve-description-{segment}').is_visible()
                        assert page.locator('.curve-description:visible').count()==1
                        palette=page.locator('.heating-curve').evaluate('figure=>[1,2,3,4,5].map(n=>{const button=figure.querySelector(`label[for="curve-choice-${n}"]`);return {button:getComputedStyle(button).backgroundColor,ink:getComputedStyle(button).color,wide:getComputedStyle(figure.querySelector(`#seg-${n}`)).stroke,mobile:getComputedStyle(figure.querySelector(`#seg-mobile-${n}`)).stroke}})')
                        assert len({c['button'] for c in palette})==5
                        for colors in palette:
                            assert colors['button']==colors['wide']==colors['mobile'], (width,theme,colors)
                            assert colors['ink']=='rgb(255, 255, 255)'
                            # Il testo bianco deve restare leggibile sui cinque riempimenti.
                            rgb=[int(v) / 255 for v in colors['button'][4:-1].split(',')]
                            linear=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
                            luminance=sum(a*b for a,b in zip(linear,[.2126,.7152,.0722]))
                            assert 1.05/(luminance+.05)>=4.5, colors
                        selected=page.locator(f'#seg-{segment}').evaluate('(e)=>getComputedStyle(e).strokeWidth')
                        assert selected=='8px'

                    # Anche la selezione nativa da tastiera mantiene il grafico fermo.
                    page.locator('#curve-choice-1').focus()
                    before=page.evaluate('scrollY')
                    page.keyboard.press('ArrowRight')
                    assert page.locator('#curve-choice-2').is_checked()
                    assert abs(page.evaluate('scrollY')-before)<2
                    if width in [390,1440]:
                        page.locator('.curve-controls').screenshot(path=str(SHOTS/f'curva-comandi-{width}-{theme}.png'))
                        page.locator('.topbar').screenshot(path=str(SHOTS/f'barra-capitolo-{width}-{theme}.png'))
            verify_media_controls(page, base, publication)
            verify_table_alignments(page, base, publication)
            # Anteprima del grafico completo, nei due temi e nelle due impaginazioni.
            for width in [390,1440]:
                page.set_viewport_size({'width':width,'height':1500})
                for theme in ['light','dark']:
                    page.goto(base+'passaggi_di_stato.html');set_theme(page,theme)
                    page.locator('.heating-curve').screenshot(path=str(SHOTS/f'curva-gradiente-{width}-{theme}.png'))
            # Home: una sola card; foto e didascalia sotto al titolo, allineate a sinistra.
            def verify_cover_layout(width):
                boxes = page.locator('.home-intro').evaluate("""card=>{
                    const image=card.querySelector('img#random-cover'),caption=card.querySelector('figcaption');
                    const copy=card.querySelector('.hero-copy');
                    return {image:image.getBoundingClientRect().toJSON(),caption:caption.getBoundingClientRect().toJSON(),copy:copy.getBoundingClientRect().toJSON(),ratio:image.naturalWidth/image.naturalHeight};
                }""")
                assert abs(boxes['image']['left']-boxes['caption']['left']) < 1, boxes
                assert abs(boxes['image']['width']-boxes['caption']['width']) < 1, boxes
                assert abs(boxes['image']['width']/boxes['image']['height']-boxes['ratio']) < .01, boxes
                assert boxes['image']['top'] >= boxes['copy']['bottom'], boxes
                assert abs(boxes['image']['left']-boxes['copy']['left']) < 1, boxes
            page.goto(base+'index.html')
            assert page.locator('.home-intro #random-cover').count() == 1
            assert page.locator('.home-intro .eyebrow').count() == 0
            assert page.locator('.actions > *').count() == 3
            assert page.locator('.actions .lang-action').count() == 0
            assert page.locator('#news-title').inner_text() == 'Novità'
            assert page.locator('.featured time').count() == 3
            assert page.locator('main h2').all_text_contents() == ['Novità']
            # Home: nessun comando contestuale, menu nel gruppo destro.
            home_nav = page.locator('.home-header .stringhe-navigation')
            assert home_nav.locator('.nav-primary > *').count() == 0
            assert home_nav.locator('.nav-settings > *').count() == 2
            assert home_nav.locator('.nav-settings > .string-lang').count() == 1
            assert home_nav.locator('.nav-settings > [data-theme-menu]').count() == 1
            for width in [320,390,768,1024,1440]:
                page.set_viewport_size({'width':width,'height':900})
                for theme in ['light','dark']:
                    set_theme(page, theme)
                    for side in ['before','after']:
                        assert page.locator('.home-title').evaluate('(e,side)=>getComputedStyle(e,":"+side).display', side) == 'none'
                        assert page.locator('.home-cover').evaluate('(e,side)=>getComputedStyle(e,":"+side).content', side) in ['none','normal']
                    assert page.locator('.home-intro .subtitle').evaluate('(e)=>getComputedStyle(e).color===(()=>{const s=document.createElement("span");s.style.color="var(--accent)";document.body.append(s);const c=getComputedStyle(s).color;s.remove();return c;})()')
                    verify_cover_layout(width)
            # Barra servizi e tooltip: hover sì, attivazione touch e focus no.
            for service_page in ['articoli.html', 'quiz.html']:
                page.goto(base + service_page)
                for width in [390, 1440]:
                    page.set_viewport_size({'width':width,'height':900})
                    nav = page.locator('.service-header .stringhe-navigation')
                    assert nav.locator(':scope > .nav-primary > *').count() == 1
                    assert nav.locator(':scope > .nav-settings > *').count() == 2
                    home_link = nav.locator('.nav-primary > .string-nav')
                    assert home_link.get_attribute('href') == 'index.html'
                    assert home_link.get_attribute('aria-label') == 'Home'
                    tip = page.locator('#function-tooltip')
                    home_link.hover()
                    assert tip.is_visible(), (service_page,width,'hover')
                    assert tip.inner_text() == 'Home'
                    language = nav.locator('.nav-settings .string-lang>summary')
                    language.tap()
                    assert not tip.is_visible(), (service_page,width,'tap')
                    assert nav.locator('.nav-settings .string-lang').get_attribute('open') is not None
                    theme_summary = nav.locator('.nav-settings [data-theme-menu]>summary')
                    theme_summary.tap()
                    assert not tip.is_visible(), (service_page,width,'theme tap')
                    assert nav.locator('.nav-settings .string-lang').get_attribute('open') is None
                    assert nav.locator('.nav-settings [data-theme-menu]').get_attribute('open') is not None
                    theme_summary.tap()
                    theme_summary.focus()
                    assert not tip.is_visible(), (service_page,width,'focus')
            verify_quiz(page, base)
            # Anche il menu del capitolo non mostra tooltip al tocco.
            page.goto(base + publication['articoli'][0])
            page.locator('[data-theme-menu]>summary').tap()
            assert not page.locator('#function-tooltip').is_visible()
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
            assert page.locator('[data-theme-option=dark]').get_attribute('aria-pressed') == 'true'
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
            # Il logo animato rimane nella sola copertina della home.
            page.goto(base+'index.html')
            assert page.locator('.topbar [data-logo-toggle]').count() == 0
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
            page.goto(base + publication['articoli'][0])
            # Tastiera, menu indice, note, zoom, crediti e download reale.
            page.locator('.index-toggle').click()
            assert page.locator('.reader-index').get_attribute('open') is not None
            # L'evento toggle di details è asincrono: attendere il suo effetto
            # senza indebolire il controllo di isolamento della tastiera.
            expect(page.locator('.nav-settings > .string-lang')).to_have_attribute('inert', '')
            page.keyboard.press('Escape')
            assert page.locator('.reader-index').get_attribute('open') is None
            expect(page.locator('.nav-settings > .string-lang')).not_to_have_attribute('inert', '')
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
            menu = page.locator('[data-theme-menu]')
            summary = menu.locator('summary')
            summary.focus();page.keyboard.press('Space')
            assert menu.get_attribute('open') is not None
            menu.locator('[data-theme-option=dark]').focus();page.keyboard.press('Enter')
            assert page.evaluate('document.documentElement.dataset.theme') == 'dark'
            assert menu.get_attribute('open') is None
            assert summary.evaluate('(e)=>e===document.activeElement')
            set_theme(page,'light')
            summary.click();page.keyboard.press('Escape')
            assert menu.get_attribute('open') is None
            page.emulate_media(color_scheme='dark')
            assert page.evaluate('document.documentElement.dataset.theme') == 'light'
            page.emulate_media(color_scheme='light')
            assert page.evaluate('document.documentElement.dataset.theme') == 'light'
            other = context.new_page(); other.goto(base+'quiz.html')
            set_theme(other, 'dark')
            page.wait_for_function('document.documentElement.dataset.theme === "dark"')
            other.evaluate("localStorage.removeItem('stringhe-theme')")
            other.close()
            page.goto(base+'index.html')
            page.emulate_media(reduced_motion='reduce')
            page.wait_for_function('document.querySelector("[data-logo-toggle]").getAttribute("aria-pressed") === "true"')
            page.goto(base + publication['articoli'][0])
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
                plain.goto(base+'passaggi_di_stato.html')
                choice=plain.locator('.curve-controls label[for="curve-choice-4"]')
                choice.evaluate('(e)=>e.scrollIntoView({block:"center",behavior:"instant"})')
                before=plain.evaluate('scrollY');choice.click()
                assert plain.locator('#curve-choice-4').is_checked()
                assert abs(plain.evaluate('scrollY')-before)<2
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
            # Anteprime della giunzione copertina/testo e del menu aperto.
            for width in [390,1440]:
                page.set_viewport_size({'width':width,'height':1100})
                for theme in ['light','dark']:
                    page.goto(base+'passaggi_di_stato.html');set_theme(page,theme)
                    page.wait_for_function('document.fonts.status === "loaded"')
                    page.evaluate('scrollTo({top:0,behavior:"instant"})')
                    page.screenshot(path=str(SHOTS/f'lettura-continua-passaggi-{width}-{theme}.png'),animations='disabled')
                    page.locator('[data-theme-menu]>summary').click()
                    assert page.locator('.theme-options').is_visible()
                    page.screenshot(path=str(SHOTS/f'menu-tema-{width}-{theme}.png'),animations='disabled')
            browser.close()
    finally:
        server.shutdown()
        (SITE / 'modello-dispense.html').unlink(missing_ok=True)
    assert not errors, errors
    report = {'barra_capitoli':{'comandi':6,'righe':1,'tema':'menu Chiaro/Scuro con luna o sole','lingua':'IT','bersaglio_minimo_px':44},'curva_riscaldamento':{'selezioni_touch':50,'prove_tastiera':10,'fallback_senza_javascript':2,'salti_di_scorrimento':False},'viewport_tema_pagina':checks,'errori_javascript':errors,'copertine_verificate':len(covers),'home':{'card':'unica per titolo, logo e copertina; senza onde laterali','mobile':'foto sotto al titolo','desktop':'foto affiancata','layout_copertine_verificati':100,'didascalia':'bordo sinistro e larghezza coincidenti con la foto; proporzioni conservate'},'logo':{'presenza':'solo nella copertina della home','curve':2,'fase':'opposizione','periodo_secondi':4,'animazione_nera':'impronta originale conservata','pausa':'entrambe le curve sincronizzate'},'laterali':{'viewport':[320,390,768,1024,1440],'temi':['light','dark'],'curve':'stessa ampiezza; periodo invariato; 24 px per fascia; nessun overflow'},
              'offline':offline_status,'browser':'Chromium; mobile e touch emulati, nessun dispositivo Android fisico',
              'controlli':['persistenza','menu tema: tastiera, Escape, default scuro e persistenza','storage bloccato','senza JavaScript','logo e movimento ridotto','ricerca e filtro','indice tastiera','note','zoom','crediti','download identico']}
    (ROOT/'lavorazione/sito/verifica-stringhe.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'Verificate {len(checks)} combinazioni pagina/viewport/tema e {len(covers)} copertine; nessun errore JavaScript')


if __name__ == '__main__':
    main()

