"""Regressioni su categoria unica e indipendenza da titoli e percorsi."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import quiz_site


class QuizCategoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.registry = self.root / 'categorie.json'
        self.archive = self.root / 'domande.json'
        self.registry.write_text(json.dumps({'schema_version': 1, 'categories': [
            {'id': 'thermal', 'area': 'Termologia'},
            {'id': 'measure', 'area': 'Misure'}]}))
        self.articles = [{'file': 'old.html', 'title': 'Vecchio titolo', 'area': 'Termologia'},
                         {'file': 'misure.html', 'title': 'Misure', 'area': 'Misure'}]
        self.patcher = patch.multiple(quiz_site, CATEGORIES=self.registry, DATA=self.archive)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_rename_chapter_does_not_change_category_ids(self):
        before = quiz_site.load_categories(self.articles)
        self.articles[0].update(file='nuovo.html', title='Nuovo titolo')
        self.assertEqual(before, quiz_site.load_categories(self.articles))

    def test_unknown_or_duplicate_registry_categories_fail(self):
        self.articles[0]['area'] = 'Non registrata'
        with self.assertRaises(ValueError):
            quiz_site.load_categories(self.articles)
        data = json.loads(self.registry.read_text())
        data['categories'][1]['id'] = 'thermal'
        self.registry.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            quiz_site.load_categories(self.articles)

    def test_only_known_single_category_and_new_schema_are_accepted(self):
        q = {'id': 'q1', 'category': 'thermal', 'level': 'easy', 'prompt': 'Test?',
             'options': ['A', 'B', 'C', 'D'], 'correct': 0, 'explanation': 'Risposta.'}
        self.archive.write_text(json.dumps({'questions': [q]}))
        self.assertEqual(quiz_site.load_questions({'thermal'}), [q])
        for change in ({'category': 'unknown'}, {'chapter': 'old.html'},
                       {'tags': ['calore']}, {'category': ['thermal', 'measure']}):
            with self.subTest(change=change):
                invalid = {**q, **change}
                self.archive.write_text(json.dumps({'questions': [invalid]}))
                with self.assertRaises(ValueError):
                    quiz_site.load_questions({'thermal'})

    def test_four_options_are_required_for_every_level(self):
        for level in ('easy', 'medium', 'hard'):
            for count in (3, 4, 5):
                with self.subTest(level=level, count=count):
                    q = {'id': 'q1', 'category': 'thermal', 'level': level,
                         'prompt': 'Test?', 'options': [str(i) for i in range(count)],
                         'correct': 0, 'explanation': 'Risposta.'}
                    self.archive.write_text(json.dumps({'questions': [q]}))
                    if count == 4:
                        self.assertEqual(quiz_site.load_questions({'thermal'}), [q])
                    else:
                        with self.assertRaises(ValueError):
                            quiz_site.load_questions({'thermal'})

    def test_no_archive_and_radio_categories_without_chapters(self):
        self.assertEqual(quiz_site.load_questions({'thermal'}), [])
        html = quiz_site.render_quiz_page('', [], lambda *_: self.articles,
                                         lambda _title, body, *_args, **_kwargs: body)
        self.assertEqual(html.count('data-quiz-category'), 2)
        self.assertEqual(html.count('type="radio" name="quiz-category"'), 2)
        self.assertNotIn('data-quiz-chapter', html)
        self.assertNotIn('4 alternative', html)
        for level in ('easy', 'medium', 'hard'):
            self.assertIn(f'name="quiz-level" value="{level}"', html)
        self.assertNotIn('3 alternative', html)
        self.assertNotIn('5 alternative', html)
        self.assertIn('Nessuna domanda disponibile', html)


if __name__ == '__main__':
    unittest.main()
