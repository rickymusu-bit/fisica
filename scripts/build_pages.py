"""Prepara GitHub Pages con gli articoli, le lingue e le copertine selezionati."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit
from home_covers import load_covers
from home_languages import HOME_FILES, load_languages, localized_home
from home_italian import render_italian

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.links = []
        self.catalogue_links = set()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html" and self.language is None:
            self.language = attrs.get("lang")
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if {"read", "download"} & set(attrs.get("class", "").split()):
                self.catalogue_links.add(attrs["href"])
        if "id" in attrs:
            self.ids.add(attrs["id"])


def read_document(path, language="it"):
    document = Document()
    document.feed(path.read_text(encoding="utf-8-sig"))
    if document.language != language:
        raise ValueError(f"Il documento non dichiara lang={language}: {path.name}")
    return document


def main():
    index = ROOT / "index.html"
    covers = load_covers(ROOT)
    languages = load_languages(ROOT, covers)
    document = read_document(index)
    sources = {index}
    for link in document.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            if link in document.catalogue_links:
                raise ValueError(f"Il catalogo deve collegare materiali locali: {link}")
            # Le fonti e le licenze delle fotografie sono collegamenti esterni.
            continue
        if url.path in ("", "./"):
            if url.fragment and unquote(url.fragment) not in document.ids:
                raise ValueError(f"Ancora assente dall'indice: {link}")
            continue
        if url.path in HOME_FILES.values():
            continue
        path = (ROOT / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or path.suffix != ".html" or not path.is_file():
            raise ValueError(f"Collegamento HTML non valido: {link}")
        read_document(path)
        sources.add(path)
    for language, ui in languages.items():
        for filename, _, _ in ui["articles"].values():
            path = ROOT / filename
            read_document(path, language)
            sources.add(path)
    if len(sources) <= 1:
        raise ValueError("L'indice non contiene materiali")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    for source in sorted(sources):
        target = OUTPUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if source == index:
            target.write_text(render_italian(
                localized_home(source.read_text(encoding="utf-8"), covers), ROOT), encoding="utf-8")
        else:
            shutil.copyfile(source, target)
    for language, ui in languages.items():
        (OUTPUT / HOME_FILES[language]).write_text(
            localized_home(index.read_text(encoding="utf-8"), covers, language, ui), encoding="utf-8")
    for cover in covers:
        source = ROOT / cover["src"]
        target = OUTPUT / cover["src"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(ROOT / "copertine" / "manifest.json", OUTPUT / "copertine" / "manifest.json")
    (OUTPUT / ".nojekyll").touch()
    print(f"Preparati {len(sources) + len(languages)} HTML in tre lingue e {len(covers)} copertine.")


if __name__ == "__main__":
    main()
