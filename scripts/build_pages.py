"""Prepara GitHub Pages copiando solo gli HTML italiani collegati dall'indice."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html" and self.language is None:
            self.language = attrs.get("lang")
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if "id" in attrs:
            self.ids.add(attrs["id"])


def read_document(path):
    document = Document()
    document.feed(path.read_text(encoding="utf-8-sig"))
    if document.language != "it":
        raise ValueError(f"Il documento non dichiara lang=it: {path.name}")
    return document


def main():
    index = ROOT / "index.html"
    document = read_document(index)
    sources = {index}
    for link in document.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            raise ValueError(f"Il catalogo deve collegare materiali locali: {link}")
        if url.path in ("", "./"):
            if url.fragment and unquote(url.fragment) not in document.ids:
                raise ValueError(f"Ancora assente dall'indice: {link}")
            continue
        path = (ROOT / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or path.suffix != ".html" or not path.is_file():
            raise ValueError(f"Collegamento HTML non valido: {link}")
        read_document(path)
        sources.add(path)
    if len(sources) <= 1:
        raise ValueError("L'indice non contiene materiali")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    for source in sorted(sources):
        target = OUTPUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    (OUTPUT / ".nojekyll").touch()
    print(f"Preparati {len(sources)} HTML in italiano.")


if __name__ == "__main__":
    main()
