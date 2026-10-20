"""Controlli della pubblicazione e dell'isolamento dei contenuti scientifici."""
import json
import hashlib
import xml.etree.ElementTree as ET
from pathlib import Path
import re
import unittest
import tempfile
from strings_site import enhance_article, catalogue, recent_chapters
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
                def without_logo(text):
                    text = re.sub(r'<button\b[^>]*data-logo-toggle[^>]*>[\s\S]*?</button>', '', text)
                    return re.sub(r'<svg\b[^>]*data-ui-icon[^>]*>[\s\S]*?</svg>', '', text)
                self.assertEqual(re.findall(r'<path\b[^>]*>', without_logo(source)), re.findall(r'<path\b[^>]*>', without_logo(published)))
                self.assertEqual(published.count('data-stringhe-theme'), 1)
                self.assertEqual(published.count('data-theme-toggle'), 3)  # markup e due script comuni
                self.assertIn('data-logo-toggle', published)
                self.assertIn('data-edge="sides"', published)
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


class NewsTests(unittest.TestCase):
    def test_news_uses_editorial_dates_and_updates_reorder_chapters(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            items = [{'file': f'{i}.html'} for i in range(4)]
            for i, day in enumerate(['2026-10-19', '2026-10-17', '2026-10-19', '2026-10-18']):
                (root / items[i]['file']).write_text(f'<meta content="{day}" name="date"/>')
            # Un file escluso, anche se più recente, non deve comparire.
            (root / 'escluso.html').write_text('<meta name="date" content="2026-10-20">')
            news = recent_chapters(items, root)
            self.assertEqual([x['file'] for x in news], ['2.html', '0.html', '3.html'])
            self.assertEqual(news[0]['date_label'], '19 ottobre 2026')
            (root / '1.html').write_text('<meta name="date" content="2026-10-20">')
            self.assertEqual(recent_chapters(items, root)[0]['file'], '1.html')
            (root / '1.html').write_text('<meta name="date" content="2026-02-30">')
            with self.assertRaises(ValueError):
                recent_chapters(items, root)



class LogoTests(unittest.TestCase):
    def test_original_black_animation_and_opposite_blue_phase(self):
        from logo_materia_oscura import svg
        source = (ROOT / 'identita/logo-materia-oscura.svg').read_text()
        self.assertEqual(source, svg())
        root = ET.fromstring(source)
        ns = {'s': 'http://www.w3.org/2000/svg'}
        moving = {path.attrib['data-logo-wave']: path for path in root.findall('s:path', ns)
                  if path.attrib['class'] == 'logo-moving'}
        self.assertEqual(set(moving), {'black', 'blue'})
        animations = {name: path.find('s:animate', ns) for name, path in moving.items()}
        # Impronta della sequenza nera approvata prima dell’aggiunta della curva blu.
        self.assertEqual(hashlib.sha256(animations['black'].attrib['values'].encode()).hexdigest(),
                         '8ddfec332b812e2175e12513ffc1f3ae610a5468555051f0c3163daaf69b9f23')
        black = animations['black'].attrib['values'].split(';')
        blue = animations['blue'].attrib['values'].split(';')
        self.assertEqual(len(black), 33)
        self.assertEqual(black[0], black[-1])
        for index in range(33):
            self.assertEqual(blue[index], black[(index + 16) % 32])
        self.assertEqual({a.attrib['dur'] for a in animations.values()}, {'4s'})
        self.assertEqual(moving['black'].attrib['stroke'], '#000')
        self.assertEqual(moving['blue'].attrib['stroke'], 'url(#logo-blue-gradient)')
        self.assertEqual([s.attrib['stop-color'] for s in root.findall('s:defs/s:linearGradient/s:stop', ns)],
                         ['#83D4FA', '#337CD8', '#4140A3'])
        still = [path for path in root.findall('s:path', ns) if path.attrib['class'] == 'logo-still']
        self.assertEqual(len(still), 2)
        self.assertNotEqual(still[0].attrib['d'], still[1].attrib['d'])


if __name__ == '__main__':
    unittest.main()
