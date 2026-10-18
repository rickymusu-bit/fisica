"""Regressioni del registro: deduplicazione, riuso e autonomia senza dipendenze."""
import base64
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import credits


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'riferimenti').mkdir()
        (self.root / 'copertine').mkdir()
        (self.root / 'copertine/manifest.json').write_text('[]')
        for name in ['index.html', 'riferimenti/TEMA_DISPENSE.html']:
            (self.root / name).write_text('<html><title>Modello</title></html>')
        self.registry = {'resources': [], 'documents': {}, 'assets': [], 'font_license': 'OFL notice'}
        self.patch = patch.object(credits, 'ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def article(self, name, changes='Nessuna'):
        image = base64.b64encode(b'identical-media-bytes').decode()
        html = ('<html><head><title>Test</title></head><body>'
                '<figure id="fig-1" data-credit-source="https://example.org/image" '
                'data-credit-author="Autore" data-credit-license="CC BY 4.0" '
                'data-credit-license-url="https://creativecommons.org/licenses/by/4.0/" '
                f'data-credit-changes="{changes}">'
                f'<img alt="Immagine di prova" src="data:image/png;base64,{image}">'
                '</figure></body></html>')
        (self.root / name).write_text(html)
        return html

    def test_same_resource_registered_once_and_associated_with_both_articles(self):
        self.article('one.html')
        self.article('two.html')
        credits.sync_inventory(self.registry)
        self.assertEqual(len(self.registry['resources']), 1)
        self.assertEqual(len(self.registry['assets']), 1)
        self.assertEqual(len(self.registry['assets'][0]['uses']), 2)
        one = self.registry['documents']['one.html']['credits'][0]
        two = self.registry['documents']['two.html']['credits'][0]
        self.assertEqual(one, two)
        before = json.dumps(self.registry, sort_keys=True)
        credits.sync_inventory(self.registry)
        self.assertEqual(before, json.dumps(self.registry, sort_keys=True))

    def test_reused_image_records_changes_per_use(self):
        self.article('one.html')
        self.article('two.html', 'Etichette tradotte')
        credits.sync_inventory(self.registry)
        self.assertEqual(len(self.registry['resources']), 1)
        self.assertIn('Etichette tradotte', credits.notice_html(self.registry, 'two.html'))
        self.assertNotIn('Etichette tradotte', credits.notice_html(self.registry, 'one.html'))

    def test_sync_preserves_media_and_adds_embedded_font_license(self):
        original = self.article('one.html').replace('</head>', '<style>@font-face{font-family:Lexend}</style></head>')
        (self.root / 'one.html').write_text(original)
        credits.sync_inventory(self.registry)
        result = credits.update_component(original, self.registry, 'one.html')
        self.assertEqual(credits.inventory(original), credits.inventory(result))
        self.assertIn('OFL notice', result)
        self.assertIn('https://example.org/image', result)
        self.assertIn(':target', result)
        self.assertEqual(result, credits.update_component(result, self.registry, 'one.html'))

    def test_resource_without_license_is_flagged_without_invented_rights(self):
        html = self.article('one.html')
        html = html.replace('data-credit-license="CC BY 4.0"', '').replace(
            'data-credit-license-url="https://creativecommons.org/licenses/by/4.0/"', '')
        (self.root / 'one.html').write_text(html)
        credits.sync_inventory(self.registry)
        self.assertEqual(self.registry['resources'][0]['status'], 'review')
        self.assertIsNone(self.registry['resources'][0]['license'])
        self.assertIn('Licenza non documentata', credits.notice_html(self.registry, 'one.html'))


if __name__ == '__main__':
    unittest.main()
