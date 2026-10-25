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
from media_controls import apply_media_controls
from credits import Document


class CoverMediaTests(unittest.TestCase):
    def test_cover_zoom_is_removed_but_body_zoom_and_main_image_remain(self):
        zoom = '<details class="image-zoom"><summary>Ingrandisci</summary><div class="zoom-scroll"><img src="foto.jpg" alt="Foto"></div></details>'
        source = '<html><head></head><body><figure class="visual cover"><div class="image-frame"><div class="overview"><img src="foto.jpg" alt="Foto"></div>' + zoom + '</div></figure><figure class="visual diagram" id="figura-corpo">' + zoom + '</figure></body></html>'
        result = apply_media_controls(source)
        doc = Document(result)
        cover = next(n for n in doc.root.descendants('figure') if n.has_class('cover'))
        body = next(n for n in doc.root.descendants('figure') if n.attrs.get('id') == 'figura-corpo')
        self.assertEqual(len(list(cover.descendants('img'))), 1)
        self.assertEqual(next(cover.descendants('img')).attrs['src'], 'foto.jpg')
        self.assertFalse(any(n.has_class('image-zoom') for n in cover.descendants('details')))
        self.assertTrue(any(n.has_class('image-zoom') for n in body.descendants('details')))


class QuadraticGraphRegressionTests(unittest.TestCase):
    def test_chapter_nine_quadratic_points_exist(self):
        source = (ROOT / 'relazioni_proporzionalita_it.html').read_text(encoding='utf-8')
        chart = re.search(r'<svg\b[^>]*data-plot="quadratic"[^>]*>[\s\S]*?</svg>', source)
        self.assertIsNotNone(chart)
        coords = re.findall(r'data-point-x="([^"]+)" cx="([^"]+)" cy="([^"]+)"', chart.group(0))
        self.assertEqual([float(x) for x, _, _ in coords], [0, 1, 2, 3, 4])
        for x, cx, cy in coords:
            x = float(x)
            self.assertAlmostEqual(float(cx), 50 + 325 * x / 4)
            self.assertAlmostEqual(float(cy), 245 - 215 * x * x / 32)
        self.assertIn('data-model="quadratic"', source)
        self.assertIn("querySelectorAll('[data-point-x]')", source)

    def test_canonical_zoom_and_table_alignment(self):
        css = (ROOT / 'identita/media-controls.css').read_text(encoding='utf-8')
        self.assertRegex(css, r'\.image-zoom>summary\.media-icon-button\{position:static')
        theme = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text(encoding='utf-8')
        self.assertIn('.article table th,.article table td{text-align:center}', theme)


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
                self.assertEqual(len(re.findall(r'<details\b[^>]*data-theme-menu', published)), 1)
                self.assertNotIn('data-theme-toggle', published)
                self.assertEqual(published.count('aria-label="Navigazione principale"'), 1)
                self.assertIn('class="topbar stringhe-header"', published)
                self.assertIn('aria-label="Scarica il capitolo"', published)
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

    def test_quiz_selects_one_category_and_levels(self):
        quiz = (ROOT / '_site/quiz.html').read_text()
        allowed = set(json.loads((ROOT / 'pubblicazione.json').read_text())['articoli'])
        payload = json.loads(re.search(r'<script type="application/json" id="quiz-data">(.*?)</script>', quiz).group(1))
        self.assertEqual({item['id'] for item in payload['categories']}, {'termologia', 'introduzione_fisica_misura'})
        self.assertNotIn('chapters', payload)
        archive = json.loads((ROOT / 'quiz/domande.json').read_text())
        self.assertEqual(payload['questions'], archive['questions'])
        self.assertEqual(len(payload['questions']), 300)
        self.assertEqual({q['category'] for q in payload['questions']}, {'termologia'})
        for level in ('easy', 'medium', 'hard'):
            self.assertEqual(sum(q['level'] == level for q in payload['questions']), 100)
        self.assertFalse((ROOT / 'quiz/domande-prova.json').exists())
        self.assertNotIn('Nessuna domanda disponibile al momento.', quiz)
        self.assertNotIn('Le domande saranno disponibili quando', quiz)
        self.assertNotIn('Archivio dimostrativo', quiz)
        self.assertNotIn('data-quiz-chapter', quiz)
        self.assertNotIn('data-quiz-group', quiz)
        self.assertEqual(quiz.count('data-quiz-category'), 2)
        self.assertEqual(quiz.count('name="quiz-category"'), 2)
        self.assertIn('id="quiz-clock"', quiz)
        self.assertIn('id="quiz-review"', quiz)
        self.assertIn('id="quiz-score"', quiz)
        self.assertNotIn('id="quiz-grade"', quiz)
        self.assertIn('class="quiz-main-actions"', quiz)
        self.assertIn('id="quiz-stop"', quiz)
        self.assertIn('id="quiz-navigation"', quiz)
        self.assertIn('id="quiz-result-navigation"', quiz)
        self.assertIn('id="quiz-status-summary"', quiz)
        self.assertIn('id="quiz-count"', quiz)
        self.assertIn('id="quiz-count-minus"', quiz)
        self.assertIn('id="quiz-count-plus"', quiz)
        self.assertIn('aria-label="Diminuisci numero di domande"', quiz)
        self.assertIn('aria-label="Aumenta numero di domande"', quiz)
        self.assertIn('max="30"', quiz)
        self.assertIn('value="25"', quiz)
        self.assertIn('id="quiz-duration"', quiz)
        self.assertIn('2 minuti per domanda', quiz)
        self.assertNotIn('2 min 30 s per domanda', quiz)
        self.assertNotIn('1 min 30 s per domanda', quiz)
        self.assertNotIn('Chi vuol essere rimandato', quiz)
        self.assertTrue((ROOT / '_site/quiz/interfaccia.js').is_file())
        self.assertIn('updateAvailability()', (ROOT / '_site/quiz/interfaccia.js').read_text())
        self.assertIn('Non disponibile', (ROOT / '_site/quiz/interfaccia.js').read_text())
        self.assertTrue((ROOT / '_site/quiz/interfaccia.css').is_file())


class NewsTests(unittest.TestCase):
    def test_same_day_uses_publication_time_and_rome_date(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            items = [{'file': f'{i}.html'} for i in range(4)]
            dates = ['2026-10-23T17:11:05Z', '2026-10-23T18:00:00+02:00',
                     '2026-10-23', '2026-10-22T22:30:00Z']
            for item, value in zip(items, dates):
                (root / item['file']).write_text(f'<meta name="date" content="{value}">')
            news = recent_chapters(items, root, limit=4)
            self.assertEqual([x['file'] for x in news], ['0.html', '1.html', '3.html', '2.html'])
            self.assertEqual(news[2]['date_label'], '23 ottobre 2026')
            (root / '0.html').write_text('<meta name="date" content="2026-10-23T19:00:00">')
            with self.assertRaises(ValueError):
                recent_chapters(items, root)

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

