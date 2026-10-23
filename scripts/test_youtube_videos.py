"""Casi di rischio del componente remoto, senza dipendere da YouTube online."""
import unittest
from youtube_videos import video_info, player, apply_youtube_videos
from credits import Document

class YoutubeTests(unittest.TestCase):
    def test_urls_and_timestamps(self):
        self.assertEqual(video_info('https://youtu.be/0fKBhvDjuy0?t=1h2m3s'),('0fKBhvDjuy0',3723))
        self.assertEqual(video_info('https://www.youtube.com/watch?v=oSCX78-8-q0&start=90'),('oSCX78-8-q0',90))
        self.assertEqual(video_info('https://www.youtube.com/embed/oSCX78-8-q0#t=20'),('oSCX78-8-q0',20))
        for url in ['https://youtube.com.evil.test/watch?v=oSCX78-8-q0','javascript:alert(1)',
                    'https://example.org/oSCX78-8-q0','https://youtu.be/<script>']:
            self.assertIsNone(video_info(url))

    def test_player_has_no_external_media_and_keeps_exact_link(self):
        url='https://youtu.be/0fKBhvDjuy0?t=90&is=original-value'
        markup=player(url,'Un titolo <scientifico>')
        doc=Document(markup)
        self.assertEqual(next(doc.root.descendants('a')).attrs['href'],url)
        for tag in ['iframe','img','script','link']:
            self.assertEqual(list(doc.root.descendants(tag)),[])
        self.assertIn('Un titolo &lt;scientifico&gt;',markup)
        self.assertIn('data-youtube-start="90"',markup)

    def test_migration_preserves_surrounding_content_and_is_repeatable(self):
        source=('<html lang="it"><head></head><body><p>Testo scientifico.</p><figure>'
                '<a class="video-thumb" href="https://youtu.be/0fKBhvDjuy0?t=12"><img src="data:image/png;base64,AA=="></a>'
                '<figcaption>Osserva il cambio di scala.</figcaption></figure>'
                '<p><a href="https://youtu.be/0fKBhvDjuy0?t=12">Riferimento testuale</a></p></body></html>')
        result=apply_youtube_videos(source)
        self.assertIn('<p>Testo scientifico.</p>',result)
        self.assertIn('<figcaption>Osserva il cambio di scala.</figcaption>',result)
        self.assertIn('>Riferimento testuale</a>',result)
        self.assertEqual(result.count('data-youtube-video='),1)
        self.assertNotIn('data:image/png',result)
        self.assertEqual(apply_youtube_videos(result),result)

if __name__=='__main__':unittest.main()
