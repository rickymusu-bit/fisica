"""Controlli della pubblicazione e dell'isolamento dei contenuti scientifici."""
import json
from pathlib import Path
import re
import unittest
from strings_site import enhance_article, catalogue
from stringhe_theme import ROOT


class PublicationTests(unittest.TestCase):
    def test_publication_preserves_science_and_embedded_assets(self):
        publication = json.loads((ROOT / 'pubblicazione.json').read_text())
        for name in publication['articoli']:
            with self.subTest(article=name):
                source = (ROOT / name).read_text(encoding='utf-8-sig')
                published = (ROOT / '_site' / name).read_text()
                science = re.search(r'<article class="article">[\s\S]*?</article>', source)
                self.assertIsNotNone(science)
                scientific_content = re.sub(r'<nav[^>]*class="bottom-links"[^>]*>[\s\S]*?</nav>', '', science.group(0))
                published_science = re.search(r'<article class="article">[\s\S]*?</article>', published).group(0)
                published_science = re.sub(r'<nav[^>]*class="bottom-links"[^>]*>[\s\S]*?</nav>', '', published_science)
                self.assertTrue(scientific_content == published_science, f'Contenuto scientifico alterato: {name}')
                self.assertEqual(re.findall(r'<img\b[^>]*>', source), re.findall(r'<img\b[^>]*>', published))
                self.assertEqual(re.findall(r'<path\b[^>]*>', source), re.findall(r'<path\b[^>]*>', published))
                self.assertEqual(published.count('data-stringhe-theme'), 1)
                self.assertEqual(published.count('data-theme-select'), 3)  # markup e due script comuni
                self.assertIn('data-logo-toggle', published)
                self.assertNotIn('href="https://rickymusu-bit.github.io/fisica/#indice"', published)
        for name in publication['esclusi_da_pubblicazione_e_aggiornamenti'] + publication['indirizzi_storici_dismessi']:
            self.assertFalse((ROOT / '_site' / name).exists(), name)

    def test_enhancement_is_repeatable(self):
        source = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text()
        once = enhance_article(source, 'esempio.html')
        self.assertEqual(enhance_article(once, 'esempio.html'), once)

    def test_catalogue_and_random_use_exactly_the_manifest(self):
        allowed = json.loads((ROOT / 'pubblicazione.json').read_text())['articoli']
        source = (ROOT / 'index.html').read_text()
        self.assertEqual(len(catalogue(source, allowed)), len(allowed))
        home = (ROOT / '_site/index.html').read_text()
        random = json.loads(re.search(r'<script type="application/json" id="catalogue-data">(.*?)</script>', home).group(1))
        self.assertEqual(set(random), set(allowed))
        self.assertEqual(len(random), len(allowed))

    def test_quiz_has_only_the_future_generator(self):
        quiz = (ROOT / '_site/quiz.html').read_text()
        self.assertIn('generare quiz di verifica scegliendo gli argomenti', quiz)
        self.assertNotIn('Chi vuol essere rimandato', quiz)


if __name__ == '__main__':
    unittest.main()
