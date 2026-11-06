"""Regressione home Stringhe 1.0.0: marchio su due colonne senza divisorio."""
import re
import unittest

from stringhe_theme import ROOT


class HomeBrandLayoutTests(unittest.TestCase):
    def test_generated_home_keeps_accessible_logo_title_and_subtitle(self):
        html = (ROOT / "_site/index.html").read_text(encoding="utf-8")
        brand = re.search(r'<div class="hero-title">(.*?)</div></div></div><figure', html, re.S)
        self.assertIsNotNone(brand)
        markup = brand.group(1)
        self.assertIn('data-logo-toggle', markup)
        self.assertIn('class="home-brand-text"', markup)
        self.assertIn('class="home-title-link" href="index.html"', markup)
        self.assertIn('<p class="subtitle">L’essenziale della Fisica</p>', markup)
        self.assertLess(markup.index('data-logo-toggle'), markup.index('class="home-brand-text"'))
        self.assertLess(markup.index('<h1>'), markup.index('class="subtitle"'))
        self.assertEqual(html.count('class="home-brand-text"'), 1)
        self.assertIn('id="random-cover"', html)
        self.assertIn('id="cover-caption"', html)

    def test_theme_copies_match_and_no_separator_exists(self):
        css = (ROOT / "identita/tema-stringhe.css").read_text(encoding="utf-8")
        self.assertIn('.home-intro .home-brand-text .subtitle{', css)
        self.assertIn('.home-intro .hero-title .brand-logo-toggle{', css)
        self.assertNotIn('home-brand-divider', css)
        for filename in ("riferimenti/TEMA_DISPENSE.html",
                         "lavorazione/sito/anteprima-bordi-stringhe.html",
                         "crediti.html"):
            with self.subTest(filename=filename):
                page = (ROOT / filename).read_text(encoding="utf-8")
                embedded = re.findall(r"<style data-stringhe-theme>(.*?)</style>", page, re.S)
                self.assertEqual(embedded, [css])


if __name__ == "__main__":
    unittest.main()
