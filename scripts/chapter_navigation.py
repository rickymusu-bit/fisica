"""Navigazione dei capitoli nell'ordine dei collegamenti di lettura della Biblioteca."""
from html.parser import HTMLParser
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- chapter-navigation:start -->'
END = '<!-- chapter-navigation:end -->'


class Catalogue(HTMLParser):
    def __init__(self):
        super().__init__()
        self.chapters = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'read' in attrs.get('class', '').split():
            self.chapters.append(attrs['href'])


def chapter_order():
    parser = Catalogue()
    parser.feed((ROOT / 'index.html').read_text())
    return parser.chapters


def navigation(filename):
    chapters = chapter_order()
    i = chapters.index(filename)
    links = []
    for offset, relation, label in [(-1, 'prev', '← Capitolo precedente'), (1, 'next', 'Capitolo successivo →')]:
        position = i + offset
        if 0 <= position < len(chapters):
            target = chapters[position]
            title = re.search(r'<title>(.*?)</title>', (ROOT / target).read_text(), re.S)[1]
            links.append(f'<a rel="{relation}" href="{escape(target, quote=True)}">'
                         f'<span>{label}</span><small>{title}</small></a>')
    return (START + '<style>.chapter-navigation{display:flex;flex-wrap:wrap;gap:16px;'
            'max-width:940px;margin:28px auto;padding:0 20px;box-sizing:border-box;clear:both}'
            '.chapter-navigation a{display:flex;flex:1 1 260px;min-width:0;min-height:48px;'
            'flex-direction:column;justify-content:center;gap:5px;padding:14px 18px;'
            'border:2px solid #080808;background:#eee;color:#080808;text-decoration:none;'
            'font:inherit;line-height:1.45;overflow-wrap:anywhere;box-sizing:border-box}'
            '.chapter-navigation a:hover{background:#ddd}.chapter-navigation a:focus-visible{'
            'outline:3px solid #080808;outline-offset:4px}.chapter-navigation a[rel=next]{text-align:right}'
            '.chapter-navigation small{display:block;font-size:.8em}'
            '@media(max-width:560px){.chapter-navigation{flex-direction:column}.chapter-navigation a{flex:auto}}'
            '</style><nav class="chapter-navigation" aria-label="Navigazione tra capitoli">'
            + ''.join(links) + '</nav>' + END)


def insert_navigation(document, filename):
    component = navigation(filename)
    if START in document:
        return re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: component, document, flags=re.S)
    return re.sub(r'(?=<footer\b)', lambda _: component, document, count=1)


if __name__ == '__main__':
    for filename in chapter_order():
        path = ROOT / filename
        path.write_text(insert_navigation(path.read_text(), filename))
