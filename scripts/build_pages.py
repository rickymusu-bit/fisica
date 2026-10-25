"""Prepara GitHub Pages con la home, gli articoli italiani e le copertine."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
import json
from urllib.parse import unquote, urlsplit
from home_covers import load_covers, render_covers
from home_italian import render_italian
from strings_site import render_home, render_catalogue, render_quiz, enhance_article, render_comparison
from credits import load_registry, validate

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
    validate(load_registry())
    index = ROOT / "index.html"
    publication = json.loads((ROOT / "pubblicazione.json").read_text())
    if publication.get("reindirizzamenti"):
        raise ValueError("La pubblicazione dei vecchi reindirizzamenti è disattivata")
    allowed_articles = set(publication["articoli"])
    excluded_articles = set(publication["esclusi_da_pubblicazione_e_aggiornamenti"])
    if allowed_articles & excluded_articles:
        raise ValueError("Un articolo risulta sia ammesso sia escluso")
    covers = load_covers(ROOT)
    document = read_document(index)
    if document.catalogue_links != allowed_articles:
        raise ValueError("Il catalogo non corrisponde agli articoli conformati ammessi")
    service_pages = {"crediti.html", "articoli.html", "quiz.html"}
    sources = {index, ROOT / "crediti.html"}
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
        if url.path == "index.html":
            continue
        path = (ROOT / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or path.suffix != ".html" or not path.is_file():
            raise ValueError(f"Collegamento HTML non valido: {link}")
        if str(path.relative_to(ROOT)) not in allowed_articles | service_pages:
            raise ValueError(f"Articolo non ammesso alla pubblicazione: {link}")
        read_document(path)
        sources.add(path)
    for source in sources - {index, ROOT / "crediti.html"}:
        article = read_document(source)
        for link in article.links:
            url = urlsplit(link)
            if not url.scheme and not url.netloc and url.path.endswith(".html"):
                if unquote(url.path) not in allowed_articles | service_pages | {"index.html"}:
                    raise ValueError(f"Link a un articolo escluso: {source.name}: {link}")
    if len(sources) <= 1:
        raise ValueError("L'indice non contiene materiali")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    for source in sorted(sources):
        target = OUTPUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if source == index:
            target.write_text(render_home(source.read_text(encoding="utf-8"), covers, allowed_articles), encoding="utf-8")
        elif source.name in allowed_articles:
            target.write_text(enhance_article(source.read_text(encoding="utf-8-sig"), source.name), encoding="utf-8")
        else:
            shutil.copyfile(source, target)
    (OUTPUT / "articoli.html").write_text(render_catalogue(index.read_text(encoding="utf-8"), allowed_articles), encoding="utf-8")
    (OUTPUT / "quiz.html").write_text(render_quiz(index.read_text(encoding="utf-8"), allowed_articles), encoding="utf-8")
    (OUTPUT / "anteprima-bordi-stringhe.html").write_text(render_comparison(index.read_text(encoding="utf-8")), encoding="utf-8")
    # La pagina contiene solo il manifest; ogni JSON di categoria si carica a richiesta.
    for name in ("interfaccia.js", "interfaccia.css"):
        target = OUTPUT / "quiz" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "quiz" / name, target)
    from quiz_site import load_categories, load_questions
    from strings_site import catalogue
    quiz_categories = load_categories(catalogue(index.read_text(encoding="utf-8"), allowed_articles))
    load_questions({category["id"] for category in quiz_categories})  # Valida gli archivi.
    for category in quiz_categories:
        source = ROOT / "quiz" / "domande" / (category["id"] + ".json")
        if source.is_file():
            target = OUTPUT / "quiz" / "domande" / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    for cover in covers:
        source = ROOT / cover["src"]
        target = OUTPUT / cover["src"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(ROOT / "copertine" / "manifest.json", OUTPUT / "copertine" / "manifest.json")
    # Solo i due formati del logo definitivo, con URL pubblici stabili.
    for filename in ("logo-materia-oscura.svg", "logo-materia-oscura.gif"):
        source = ROOT / "identita" / filename
        target = OUTPUT / "identita" / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    # Archivio e licenze accompagnano anche le copie scaricate.
    for name in ("risorse/crediti.json", "licenze/Lexend-OFL.txt"):
        target = OUTPUT / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    (OUTPUT / ".nojekyll").touch()
    print(f"Preparati {len(sources) + 3} HTML in italiano e {len(covers)} copertine.")


if __name__ == "__main__":
    main()
