"""Comandi media del tema: markup nativo e risorse incorporate, senza rete."""
import re
from credits import Document
from stringhe_theme import asset, icon


def remove_cover_zoom(source):
    """Le copertine non hanno zoom; conserva intatta l'immagine principale."""
    document = Document(source)
    edits = []
    for figure in document.root.descendants('figure'):
        if not figure.has_class('cover'):
            continue
        for zoom in figure.descendants('details'):
            if zoom.has_class('image-zoom'):
                edits.append((zoom.start, zoom.end))
    for start, end in sorted(edits, reverse=True):
        source = source[:start] + source[end:]
    return source


def apply_media_controls(source):
    source = remove_cover_zoom(source)
    # I vecchi gestori scrivevano testo nei pulsanti: ora un solo gestore comune.
    source = re.sub(r'<script\b[^>]*data-chapter-media[^>]*>[\s\S]*?</script>', '', source)
    source = re.sub(r'<script\b[^>]*>[\s\S]*?</script>',
                    lambda m: '' if "const figure=document.getElementById('fig-02')" in m[0] and 'data-water-toggle' in m[0] else m[0], source)
    for tag in ['style', 'script']:
        source = re.sub(rf'<{tag}\b[^>]*data-media-ui[^>]*>[\s\S]*?</{tag}>', '', source)
    document = Document(source)
    edits = []
    for figure in document.root.descendants('figure'):
        if not figure.has_class('visual'):
            continue
        for zoom in (n for n in figure.descendants('details') if n.has_class('image-zoom')):
            summary = next(zoom.descendants('summary'))
            replacement = ('<summary class="media-icon-button" aria-label="Ingrandisci o rimpicciolisci l’immagine" '
                           'title="Ingrandisci o rimpicciolisci l’immagine">'
                           '<span class="zoom-expand">' + icon('zoom-in') + '</span>'
                           '<span class="zoom-collapse">' + icon('zoom-out') + '</span></summary>')
            edits.append((summary.start, summary.end, replacement))
        for image in figure.descendants('img'):
            if not image.attrs.get('src', '').startswith('data:image/gif'):
                continue
            if image.parent.has_class('gif-stage') or (image.parent.tag == 'picture' and image.parent.parent.has_class('gif-stage')):
                continue
            still = image.attrs.get('data-still')
            picture = image.parent if image.parent.tag == 'picture' else None
            if picture and not still:
                still = next((n.attrs.get('srcset') for n in picture.descendants('source')), None)
            if not still:
                raise ValueError('GIF priva di fermo immagine: preparare data-still prima dell’impaginazione')
            original = document.html(image)
            if 'data-still' not in image.attrs:
                original = original.replace('<img ', '<img data-still="' + still + '" ', 1)
            if picture:
                content = document.html(picture).replace(document.html(image), original)
            else:
                content = ('<picture><source media="(prefers-reduced-motion: reduce)" srcset="' + still + '">' + original + '</picture>')
            button = ('<button type="button" class="media-icon-button" data-animation-toggle '
                      'aria-label="Metti in pausa l’animazione" title="Metti in pausa l’animazione" '
                      'aria-pressed="false" disabled><span class="media-pause">' + icon('pause') + '</span>'
                      '<span class="media-play">' + icon('play') + '</span></button>')
            target = picture or image
            edits.append((target.start, target.end, '<span class="gif-stage">' + content + button + '</span>'))
        # Elimina soltanto i precedenti controlli testuali delle GIF.
        for button in figure.descendants('button'):
            if not any(key in button.attrs for key in ['data-animation-toggle', 'data-water-toggle']):
                continue
            if button.parent.has_class('gif-stage'):
                continue
            target = button.parent if button.parent.tag == 'p' or button.parent.has_class('water-controls') else button
            edits.append((target.start, target.end, ''))
    for start, end, replacement in sorted(edits, reverse=True):
        source = source[:start] + replacement + source[end:]
    source = source.replace('</head>', '<style data-media-ui>' + asset('media-controls.css') + '</style></head>', 1)
    return source.replace('</body>', '<script data-media-ui>' + asset('media-controls.js') + '</script></body>', 1)
