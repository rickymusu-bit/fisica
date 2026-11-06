"""Regressione titoli lunghi Stringhe, versione 1.0.0 — 2026-11-06T19:00:00+01:00."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
THEME_PATH = ROOT / "identita/tema-stringhe.css"
EMBEDDED_PATHS = (
    ROOT / "riferimenti/TEMA_DISPENSE.html",
    ROOT / "lavorazione/sito/anteprima-bordi-stringhe.html",
    ROOT / "crediti.html",
)


class ChapterHeroTitleWrapTests(unittest.TestCase):
    def test_long_chapter_title_is_constrained_and_wrappable(self):
        css = THEME_PATH.read_text(encoding="utf-8")
        selector = r"\\.page main>\\.hero \\.hero-grid>h1"
        rules = re.findall(selector + r"\\s*\\{([^}]+)\\}", css)
        self.assertTrue(rules, "Manca la regola per i titoli dei capitoli")
        self.assertTrue(any(
            all(property_ in rule for property_ in (
                "min-width:0", "max-width:100%", "hyphens:auto",
                "overflow-wrap:anywhere"))
            for rule in rules
        ))
        self.assertIn("font-size:clamp(42px,4.2vw,64px)", css)

    def test_standalone_theme_copies_are_synchronized(self):
        css = THEME_PATH.read_text(encoding="utf-8")
        for path in EMBEDDED_PATHS:
            with self.subTest(path=path.name):
                html = path.read_text(encoding="utf-8")
                styles = re.findall(
                    r"<style data-stringhe-theme>([\\s\\S]*?)</style>", html)
                self.assertEqual(styles, [css])
        model = EMBEDDED_PATHS[0].read_text(encoding="utf-8")
        self.assertIn('<html lang="it"', model)
        self.assertIn('class="hero-grid"', model)


if __name__ == "__main__":
    unittest.main()
