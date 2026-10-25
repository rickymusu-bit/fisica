"""Collauda l'archivio reale e salva l'anteprima del quiz desktop/mobile."""
import functools
import http.server
import json
import argparse
import re
import shutil
import tempfile
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright
import verify_stringhe_browser as shared

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / 'lavorazione/quiz/termologia/anteprima'


def visible_math_text(value):
    """Testo leggibile del dataset una volta applicati pedici e apici HTML."""
    value = re.sub(r'_\{([^}]+)\}|_([A-Za-zÀ-ÖØ-öø-ÿΑ-Ωα-ω0-9°]+)',
                   lambda match: match.group(1) or match.group(2), value)
    value = re.sub(r'\^\{([^}]+)\}|\^([−+\-]?\d+)',
                   lambda match: match.group(1) or match.group(2), value)
    return value.translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀₁₂₃₄₅₆₇₈₉', '0123456789−+0123456789'))


def verify_real(page, base, width):
    page.goto(base + 'quiz.html')
    payload = page.locator('#quiz-data').text_content()
    data = json.loads(payload)
    assert len(data['questions']) == 600
    by_id = {q['id']: q for q in data['questions']}
    thermal = page.locator('[data-quiz-category][value="termologia"]')
    other = page.locator('[data-quiz-category][value="introduzione_fisica_misura"]')
    assert thermal.is_enabled() and other.is_enabled()
    assert page.locator('.quiz-empty-notice').count() == 0
    count = 30 if width == 1440 else 3
    for theme in ('dark', 'light'):
        shared.set_theme(page, theme)
        thermal.check()
        assert page.locator('#quiz-start').is_enabled()
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        page.screenshot(path=str(SHOTS / f'config-{width}-{theme}.png'), full_page=True)
    shared.set_theme(page, 'dark')
    for level in ('easy', 'medium', 'hard'):
        page.locator(f'input[name="quiz-level"][value="{level}"]').check()
        assert thermal.is_enabled() and other.is_enabled()
        page.locator('#quiz-count').fill(str(count))
        page.locator('#quiz-start').click()
        key = page.evaluate("'stringhe.quiz.session.v1:' + location.pathname")
        saved = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
        session = saved['session']
        assert len({q['id'] for q in session['questions']}) == count
        assert all(q['category'] == 'termologia' and q['level'] == level for q in session['questions'])
        assert all(q['prompt'] == by_id[q['id']]['prompt'] for q in session['questions'])
        for i, question in enumerate(session['questions']):
            actual = page.locator('#quiz-prompt').inner_text()
            expected = visible_math_text(question['prompt'])
            assert actual == expected, (question['id'], actual, expected)
            assert page.locator('.quiz-answer input').count() == 4
            assert not page.locator('#quiz-results').is_visible()
            if i == 0:
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                page.screenshot(path=str(SHOTS / f'domanda-{level}-{width}.png'), full_page=True)
            page.locator(f'.quiz-answer input[value="{question["correct"]}"]').check()
            if i == 1:
                before = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                page.reload()
                after = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                assert before == after
                assert page.locator(f'.quiz-answer input[value="{question["correct"]}"]').is_checked()
            page.locator('#quiz-next').click()
        assert page.locator('#quiz-results').is_visible()
        assert page.locator('#quiz-score').inner_text() == f'{count} / {count}'
        assert page.locator('.quiz-review-item').count() == count
        for i, question in enumerate(session['questions']):
            item = page.locator('.quiz-review-item').nth(i)
            assert visible_math_text(question['explanation']) in item.inner_text()
            assert visible_math_text(question['options'][question['correct']]) in item.inner_text()
        if width == 390:
            page.screenshot(path=str(SHOTS / f'risultato-{level}-{width}.png'), full_page=True)
        page.reload()
        assert page.locator('#quiz-score').inner_text() == f'{count} / {count}'
        page.locator('#quiz-again').click()
        assert page.evaluate('key => localStorage.getItem(key)', key) is None
    # Verifica reale della seconda categoria, senza mescolare gli archivi.
    for level in ('easy', 'medium', 'hard'):
        page.locator(f'input[name="quiz-level"][value="{level}"]').check()
        assert thermal.is_enabled() and other.is_enabled()
        other.check()
        page.locator('#quiz-count').fill(str(count))
        page.locator('#quiz-start').click()
        key = page.evaluate("'stringhe.quiz.session.v1:' + location.pathname")
        saved = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
        session = saved['session']
        assert len({q['id'] for q in session['questions']}) == count
        assert all(q['category'] == 'introduzione_fisica_misura' and q['level'] == level for q in session['questions'])
        assert all(q['prompt'] == by_id[q['id']]['prompt'] for q in session['questions'])
        for i, question in enumerate(session['questions']):
            actual = page.locator('#quiz-prompt').inner_text()
            expected = visible_math_text(question['prompt'])
            assert actual == expected, (question['id'], actual, expected)
            assert page.locator('.quiz-answer input').count() == 4
            assert not page.locator('#quiz-results').is_visible()
            if i == 0:
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                page.screenshot(path=str(SHOTS / f'intro-domanda-{level}-{width}.png'), full_page=True)
            page.locator(f'.quiz-answer input[value="{question["correct"]}"]').check()
            if i == 1:
                before = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                page.reload()
                after = page.evaluate('key => JSON.parse(localStorage.getItem(key))', key)
                assert before == after
                assert page.locator(f'.quiz-answer input[value="{question["correct"]}"]').is_checked()
            page.locator('#quiz-next').click()
        assert page.locator('#quiz-results').is_visible()
        assert page.locator('#quiz-score').inner_text() == f'{count} / {count}'
        assert page.locator('.quiz-review-item').count() == count
        for i, question in enumerate(session['questions']):
            item = page.locator('.quiz-review-item').nth(i)
            assert visible_math_text(question['explanation']) in item.inner_text()
            assert visible_math_text(question['options'][question['correct']]) in item.inner_text()
        if width == 390:
            page.screenshot(path=str(SHOTS / f'intro-risultato-{level}-{width}.png'), full_page=True)
        page.reload()
        assert page.locator('#quiz-score').inner_text() == f'{count} / {count}'
        page.locator('#quiz-again').click()
        assert page.evaluate('key => localStorage.getItem(key)', key) is None
    return {'width': width, 'levels': ['easy', 'medium', 'hard'],
            'categories': ['termologia', 'introduzione_fisica_misura'], 'questions_per_session': count, 'score': f'{count} / {count}',
            'unique_questions': True, 'resume_and_results': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--real-only', action='store_true', help='La suite generale è già eseguita separatamente in CI')
    args = parser.parse_args()
    SHOTS.mkdir(parents=True, exist_ok=True)
    handler = functools.partial(shared.QuietHandler, directory=str(ROOT / '_site'))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}/'
    checks, errors = [], []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
            for width in (1440, 390):
                context = browser.new_context(viewport={'width': width, 'height': 950},
                                              is_mobile=width == 390, has_touch=width == 390)
                page = context.new_page()
                page.on('pageerror', lambda error: errors.append(str(error)))
                checks.append(verify_real(page, base, width))
                context.close()
            # La suite esistente verifica timer, scadenze, storage bloccato,
            # dati corrotti, categorie mancanti e compatibilità delle sessioni.
            if not args.real_only:
                with tempfile.TemporaryDirectory() as temporary:
                    shared.SHOTS = Path(temporary)
                    context = browser.new_context(viewport={'width': 390, 'height': 900})
                    page = context.new_page()
                    page.on('pageerror', lambda error: errors.append(str(error)))
                    page.goto(base + 'quiz.html')
                    shared.verify_quiz(page, base)
                    context.close()
            browser.close()
    finally:
        server.shutdown()
    assert not errors, errors
    report = {'archive': 600, 'checks': checks, 'existing_quiz_browser_suite': 'not_run' if args.real_only else 'passed',
              'javascript_errors': errors, 'mobile': 'Chromium emulato, non dispositivo fisico'}
    (ROOT / 'lavorazione/quiz/termologia/verifica-integrazione.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
