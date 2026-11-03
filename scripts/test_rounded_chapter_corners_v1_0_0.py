"""Regressione CSS 1.0.0: cornici dei capitoli Stringhe."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT / "identita" / "tema-stringhe.css"
GENERATED = (
    ROOT / "riferimenti" / "TEMA_DISPENSE.html",
    ROOT / "crediti.html",
    ROOT / "lavorazione" / "sito" / "anteprima-bordi-stringhe.html",
)


class ChapterCornerTests(unittest.TestCase):
    def test_page_header_and_footer_follow_rounded_border(self):
        css = CSS_PATH.read_text(encoding="utf-8")
        self.assertRegex(css, r"\.page\s*>\s*\.topbar\s*\{border-radius:15px 15px 0 0\}")
        self.assertRegex(css, r"\.page\s*>\s*\.footer\s*\{border-radius:0 0 15px 15px\}")
        # Don't hide overlays (theme menu and fixed article index).
        page_rules = re.findall(r"\.page\s*\{([^}]*)\}", css)
        self.assertTrue(page_rules)
        self.assertFalse(any(re.search(r"overflow\s*:\s*(hidden|clip)", rule) for rule in page_rules))

    def test_embedded_theme_matches_canonical_css(self):
        canonical = CSS_PATH.read_text(encoding="utf-8")
        for path in GENERATED:
            with self.subTest(path=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8")
                match = re.search(r"<style data-stringhe-theme>(.*?)</style>", content, re.S)
                self.assertIsNotNone(match)
                self.assertEqual(match.group(1), canonical)


if __name__ == "__main__":
    unittest.main()
