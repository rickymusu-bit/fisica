"""Pagina Quiz di Stringhe: catalogo e dataset esterni, grafica condivisa."""
from html import escape
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "quiz" / "domande"
CATEGORIES = ROOT / "quiz" / "categorie.json"
LEVELS = {"easy": 4, "medium": 4, "hard": 4}


def load_categories(articles):
    """ID stabili per le categorie; nessun legame dei quesiti con titoli o file."""
    registry = json.loads(CATEGORIES.read_text(encoding="utf-8"))
    if not isinstance(registry, dict) or registry.get("schema_version") != 1:
        raise ValueError("Registro delle categorie non valido")
    categories = registry.get("categories")
    if not isinstance(categories, list) or not categories:
        raise ValueError("Categorie mancanti")
    ids, areas = set(), set()
    for category in categories:
        if not isinstance(category, dict):
            raise ValueError("Categoria non valida")
        identifier, area = category.get("id"), category.get("area")
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9_]+", identifier) or identifier in ids:
            raise ValueError("Identificativo categoria assente o duplicato")
        if not isinstance(area, str) or not area.strip() or area in areas:
            raise ValueError("Area categoria assente o duplicata")
        ids.add(identifier)
        areas.add(area)
    if areas != {article["area"] for article in articles}:
        raise ValueError("Le categorie del quiz non corrispondono al catalogo")
    return [{"id": category["id"], "title": category["area"]} for category in categories]


def load_questions(allowed):
    """Legge e valida i JSON separati. Una categoria senza file non è disponibile."""
    questions = []
    identifiers = set()
    for category_id in sorted(allowed):
        source = DATA_DIR / (category_id + ".json")
        if not source.is_file():
            continue
        archive = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(archive, dict) or not isinstance(archive.get("questions"), list):
            raise ValueError(f"Archivio non valido: {source.name}")
        for q in archive["questions"]:
            if not isinstance(q, dict):
                raise ValueError(f"Record non valido in {source.name}")
            if set(q) != {"id", "category", "level", "prompt", "options", "correct", "explanation"}:
                raise ValueError(f"Campi non validi in {source.name}")
            if not isinstance(q["id"], str) or not q["id"] or q["id"] in identifiers:
                raise ValueError(f"ID domanda assente o duplicato: {q['id']}")
            identifiers.add(q["id"])
            if q["category"] != category_id:
                raise ValueError(f"Categoria errata in {source.name}: {q['id']}")
            if q["level"] not in LEVELS or not isinstance(q["options"], list) or len(q["options"]) != LEVELS[q["level"]]:
                raise ValueError(f"Numero alternative errato: {q['id']}")
            if type(q["correct"]) is not int or not 0 <= q["correct"] < len(q["options"]):
                raise ValueError(f"Soluzione non valida: {q['id']}")
            if any(not isinstance(q[field], str) or not q[field].strip()
                   for field in ("prompt", "explanation")):
                raise ValueError(f"Testo incompleto: {q['id']}")
            if any(not isinstance(x, str) or not x.strip() for x in q["options"]):
                raise ValueError(f"Alternativa vuota: {q['id']}")
            if len(set(q["options"])) != len(q["options"]):
                raise ValueError(f"Alternative duplicate: {q['id']}")
            questions.append(q)
    return questions

def render_quiz_page(source, allowed, catalogue, shell):
    articles = catalogue(source, allowed)
    categories = load_categories(articles)
    questions = load_questions({category["id"] for category in categories})
    for category in categories:
        category["file"] = "quiz/domande/" + category["id"] + ".json"
        category["levels"] = {
            level: sum(q["category"] == category["id"] and q["level"] == level
                       for q in questions)
            for level in LEVELS
        }
    category_html = "".join(
        '<label class="quiz-choice quiz-category-title">'
        '<input type="radio" name="quiz-category" data-quiz-category '
        f'value="{escape(category["id"], quote=True)}">'
        f'<span>{escape(category["title"])}</span></label>'
        for category in categories
    )
    payload = json.dumps({"categories": categories},
                         ensure_ascii=False).replace("<", "\\u003c")
    body = (
        '<p class="eyebrow">Mettiti alla prova</p>'
        '<h1 class="page-title">Quiz</h1>'
        '<p class="lede">Scegli una categoria e il livello di difficoltà.</p>'
        '<p id="quiz-save-warning" class="quiz-error" role="alert" hidden></p>'
        '<section id="quiz-config" aria-labelledby="quiz-config-title">'
        '<div class="quiz-layout"><div class="quiz-panel">'
        '<h2 id="quiz-config-title" tabindex="-1">Categoria</h2>'
        + ('<p class="quiz-empty-notice" role="status">Nessuna domanda disponibile al momento.</p>'
           if not questions else '') +
        '<fieldset class="quiz-categories"><legend class="quiz-sr-only">Scegli una categoria</legend>' + category_html + '</fieldset>' +
        '</div><aside class="quiz-panel"><h2>Impostazioni</h2>'
        '<fieldset class="quiz-levels"><legend>Difficoltà</legend>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="easy" checked>'
        '<strong>Facile</strong></label>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="medium">'
        '<strong>Media</strong></label>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="hard">'
        '<strong>Difficile</strong></label>'
        '</fieldset><div class="quiz-count-control">'
        '<label for="quiz-count">Numero di domande</label>'
        '<div class="quiz-count-stepper">'
        '<button type="button" id="quiz-count-minus" aria-label="Diminuisci numero di domande">−</button>'
        '<input type="number" id="quiz-count" min="1" max="30" step="1" value="25" inputmode="numeric">'
        '<button type="button" id="quiz-count-plus" aria-label="Aumenta numero di domande">+</button>'
        '</div></div>'
        '<p class="quiz-duration-note">Tempo totale (2 minuti per domanda): '
        '<output id="quiz-duration" for="quiz-count">50:00</output></p>'
        '<button type="button" class="quiz-action quiz-action-primary" id="quiz-start" disabled>Inizia il quiz →</button>'
        '<p class="quiz-error" id="quiz-config-error" role="alert" hidden></p>'
        + ('<p class="quiz-help">Le soluzioni e le spiegazioni saranno mostrate al termine.</p>'
           if questions else '<p class="quiz-help">Le domande saranno disponibili quando verrà caricato il relativo archivio.</p>') +
        '</aside></div></section>'
        '<section id="quiz-active" hidden aria-label="Quiz in corso"><div class="quiz-panel">'
        '<div class="quiz-status"><strong id="quiz-counter">Domanda 1 di 25</strong>'
        '<div>Tempo rimanente <span class="quiz-clock" id="quiz-clock" role="timer">00:00</span></div></div>'
        '<div class="quiz-progress" aria-hidden="true"><span id="quiz-progress-fill"></span></div>'
        '<p class="quiz-status-summary" id="quiz-status-summary" aria-live="polite"></p>'
        '<ol id="quiz-navigation" class="quiz-navigation" aria-label="Stato delle domande"></ol>'
        '<div class="quiz-legend" aria-label="Legenda">'
        '<span><i class="quiz-legend-marker is-answered" aria-hidden="true"></i>Risposta data</span>'
        '<span><i class="quiz-legend-marker is-skipped" aria-hidden="true"></i>Saltata</span>'
        '<span><i class="quiz-legend-marker is-current" aria-hidden="true"></i>Corrente</span>'
        '<span><i class="quiz-legend-marker" aria-hidden="true"></i>Da affrontare</span></div>'
        '<p class="quiz-kicker" id="quiz-topic"></p>'
        '<h2 id="quiz-prompt" class="quiz-question" tabindex="-1"></h2>'
        '<fieldset class="quiz-answers" id="quiz-answers" aria-label="Scegli una risposta"></fieldset>'
        '<div class="quiz-actions-row">'
        '<div class="quiz-main-actions">'
        '<button class="quiz-action" type="button" id="quiz-previous" disabled>Indietro</button>'
        '<button class="quiz-action quiz-action-primary" type="button" id="quiz-next">Avanti</button>'
        '</div>'
        '<button class="quiz-action quiz-action-stop" type="button" id="quiz-stop">Concludi</button>'
        '</div></div></section>'
        '<dialog id="quiz-stop-dialog" class="quiz-stop-dialog" aria-labelledby="quiz-stop-title" aria-describedby="quiz-stop-description">'
        '<h2 id="quiz-stop-title">Concludere il quiz?</h2>'
        '<p id="quiz-stop-description">Le domande senza risposta saranno conteggiate come errate.</p>'
        '<div class="quiz-actions-row">'
        '<button type="button" id="quiz-stop-cancel" class="quiz-action" autofocus>Ritorna al quiz</button>'
        '<button type="button" id="quiz-stop-confirm" class="quiz-action quiz-action-stop">Concludi</button>'
        '</div></dialog>'
        '<section id="quiz-results" hidden aria-labelledby="quiz-results-title">'
        '<div class="quiz-panel"><p class="eyebrow">Risultato</p>'
        '<h2 id="quiz-results-title" tabindex="-1">Il tuo quiz</h2>'
        '<div class="quiz-score" id="quiz-score">0 / 25</div>'
        '<p id="quiz-finished-reason"></p>'
        '<div class="quiz-metrics"><div><strong id="quiz-correct">0</strong>Corrette</div>'
        '<div><strong id="quiz-wrong">0</strong>Errate o non risposte</div></div>'
        '<button type="button" id="quiz-again" class="quiz-action quiz-action-primary">Nuovo quiz</button>'
        '<h2 style="margin-top:36px">Revisione delle risposte</h2>'
        '<p class="quiz-status-summary" id="quiz-result-summary"></p>'
        '<ol id="quiz-result-navigation" class="quiz-navigation" aria-label="Stato finale delle domande"></ol>'
        '<div class="quiz-legend" aria-label="Legenda">'
        '<span><i class="quiz-legend-marker is-correct" aria-hidden="true"></i>Corretta</span>'
        '<span><i class="quiz-legend-marker is-skipped" aria-hidden="true"></i>Saltata</span>'
        '<span><i class="quiz-legend-marker is-wrong" aria-hidden="true"></i>Errata</span></div>'
        '<ol id="quiz-review" class="quiz-review"></ol></div></section>'
        '<noscript><p>Per svolgere il quiz serve JavaScript.</p></noscript>'
        f'<script type="application/json" id="quiz-data">{payload}</script>'
        '<script src="quiz/interfaccia.js" defer></script>'
    )
    page = shell("Quiz", body, source, service=True)
    return page.replace("</head>", '<link rel="stylesheet" href="quiz/interfaccia.css"></head>', 1)


