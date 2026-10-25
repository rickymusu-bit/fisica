"""Pedici/apici su dati reali, salvataggi precedenti e testo non attendibile."""
import functools
import http.server
import json
import re
import shutil
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright
from verify_stringhe_browser import QuietHandler, set_theme
from verify_quiz_browser import visible_math_text

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'lavorazione/quiz/termologia/notazione'


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    html = (ROOT / '_site/quiz.html').read_text()
    match = re.search(r'(<script type="application/json" id="quiz-data">)(.*?)(</script>)', html, re.S)
    original = json.loads(match.group(2))
    example = next(q for q in original['questions'] if q['id'] == 'termo-285')
    fixture = {**original, 'questions': [example]}
    all_subscripts = sorted({token for q in original['questions']
                             for text in [q['prompt'], q['explanation']] + q['options']
                             for token in re.findall(r'((?:Δ)?[A-Za-zΑ-Ωα-ω]_[A-Za-zΑ-Ωα-ω0-9°]+)', text)})
    probe = {
        'id': 'notation-test', 'category': 'termologia', 'level': 'medium',
        'prompt': '; '.join(all_subscripts) + '; c_{ghiaccio}; Q₁; L₀; 10⁻⁵; T^4; x^{−2}; <img src=x onerror="window.quizUnsafe=true">',
        'options': ['c_acqua', 'T_amb⁴', '10⁻⁵', '<svg onload="window.quizUnsafe=true">'],
        'correct': 0,
        'explanation': 'Q = m_calda · c_acqua · ΔT; T_amb⁴; 10⁻⁵; <script>window.quizUnsafe=true</script>'}

    def route_content(route):
        payload = json.dumps(fixture, ensure_ascii=False).replace('<', '\\u003c')
        route.fulfill(status=200, content_type='text/html; charset=utf-8',
                      body=html[:match.start(2)] + payload + html[match.end(2):])

    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(ROOT / '_site')))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}/'
    errors = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
            for width in (1440, 390, 320):
                context = browser.new_context(viewport={'width': width, 'height': 1000})
                page = context.new_page()
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.route('**/quiz.html', route_content)
                fixture['questions'] = [example]
                page.goto(base + 'quiz.html')
                page.locator('[name="quiz-level"][value="hard"]').check()
                page.locator('[data-quiz-category][value="termologia"]').check()
                page.locator('#quiz-count').fill('1')
                page.locator('#quiz-start').click()
                assert page.locator('#quiz-prompt sub').all_text_contents() == ['acqua']
                assert '_' not in page.locator('#quiz-prompt').inner_text()
                assert page.locator('#quiz-prompt').inner_text() == visible_math_text(example['prompt'])
                assert page.locator('#quiz-prompt sup').count() == 0
                for theme in ('dark', 'light'):
                    set_theme(page, theme)
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                    assert page.locator('#quiz-prompt sub').evaluate('el => parseFloat(getComputedStyle(el).fontSize) < parseFloat(getComputedStyle(el.parentElement).fontSize)')
                    page.screenshot(path=str(DEST / f'pedici-{width}-{theme}.png'), full_page=True)
                page.locator(f'.quiz-answer input[value="{example["correct"]}"]').check()
                page.locator('#quiz-next').click()
                assert page.locator('#quiz-score').inner_text() == '1 / 1'
                assert '_' not in page.locator('#quiz-review').inner_text()
                page.screenshot(path=str(DEST / f'soluzione-{width}.png'), full_page=True)

                # Una sessione già salvata conserva il testo originale e la scelta.
                fixture['questions'] = [probe]
                page.locator('#quiz-again').click()
                page.reload()
                page.locator('[name="quiz-level"][value="medium"]').check()
                page.locator('[data-quiz-category][value="termologia"]').check()
                page.locator('#quiz-count').fill('1')
                page.locator('#quiz-start').click()
                assert page.locator('#quiz-prompt sub').count() == len(all_subscripts) + 3
                assert page.locator('.quiz-answer:has(input[value="0"]) sub').inner_text() == 'acqua'
                assert page.locator('.quiz-answer:has(input[value="1"]) sub').inner_text() == 'amb'
                assert page.locator('.quiz-answer:has(input[value="1"]) sup').inner_text() == '4'
                assert page.locator('.quiz-answer:has(input[value="2"]) sup').inner_text() == '−5'
                assert page.locator('#quiz-prompt sup').all_text_contents() == ['−5', '4', '−2']
                assert page.locator('#quiz-prompt img, .quiz-answer svg').count() == 0
                assert page.evaluate('window.quizUnsafe === undefined')
                page.locator('.quiz-answer input[value="0"]').check()
                key = page.evaluate("'stringhe.quiz.session.v1:' + location.pathname")
                stored = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                assert stored['session']['questions'][0]['prompt'] == probe['prompt']
                assert stored['session']['pendingResponse'] == 0
                page.goto(base + 'index.html')
                stored['version'] = 1
                page.evaluate('args => localStorage.setItem(args[0], JSON.stringify(args[1]))', [key, stored])
                page.goto(base + 'quiz.html')
                recovered = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                assert recovered == stored
                assert page.locator('.quiz-answer input[value="0"]').is_checked()
                assert page.locator('#quiz-prompt sub').count() == len(all_subscripts) + 3
                page.locator('#quiz-next').click()
                assert page.locator('#quiz-score').inner_text() == '1 / 1'
                assert page.locator('#quiz-review sub').count() > 0
                assert page.locator('#quiz-review sup').count() > 0
                assert page.locator('#quiz-review img, #quiz-review svg, #quiz-review script').count() == 0
                assert page.evaluate('window.quizUnsafe === undefined')
                page.reload()
                assert page.locator('#quiz-score').inner_text() == '1 / 1'
                context.close()
            browser.close()
    finally:
        server.shutdown()
    assert not errors, errors
    report = {'source_record': example['id'], 'viewports': [1440, 390, 320],
              'themes': ['dark', 'light'], 'subscript_tokens': all_subscripts,
              'question_options_and_feedback': 'passed', 'unicode_and_braces': 'passed',
              'legacy_snapshot_preserved': True, 'untrusted_html_stays_text': True,
              'javascript_errors': errors}
    (DEST / 'verifica.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
