"""Pagina Quiz di Stringhe: catalogo e dataset esterni, grafica condivisa."""
from collections import OrderedDict
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "quiz" / "domande.json"
LEVELS = {"easy": 3, "medium": 4, "hard": 5}


def load_questions(allowed):
    # Nessun archivio: l'interfaccia rimane visibile, ma non avviabile.
    if not DATA.is_file():
        return []
    archive = json.loads(DATA.read_text(encoding="utf-8"))
    if not isinstance(archive, dict) or not isinstance(archive.get("questions"), list):
        raise ValueError("Archivio delle domande non valido")
    questions = archive["questions"]
    if len({q["id"] for q in questions}) != len(questions):
        raise ValueError("Identificativi duplicati nelle domande")
    for q in questions:
        if q["chapter"] not in allowed:
            raise ValueError(f"Capitolo della domanda non pubblicato: {q['chapter']}")
        if q["level"] not in LEVELS or len(q["options"]) != LEVELS[q["level"]]:
            raise ValueError(f"Numero alternative errato: {q['id']}")
        if not isinstance(q["correct"], int) or not 0 <= q["correct"] < len(q["options"]):
            raise ValueError(f"Soluzione non valida: {q['id']}")
        if any(not isinstance(q[field], str) or not q[field].strip()
               for field in ("prompt", "explanation")):
            raise ValueError(f"Testo incompleto: {q['id']}")
        if any(not isinstance(x, str) or not x.strip() for x in q["options"]):
            raise ValueError(f"Alternativa vuota: {q['id']}")
        if len(set(q["options"])) != len(q["options"]):
            raise ValueError(f"Alternative duplicate: {q['id']}")
    return questions


def render_quiz_page(source, allowed, catalogue, shell):
    articles = catalogue(source, allowed)
    questions = load_questions(allowed)
    grouped = OrderedDict()
    for article in articles:
        grouped.setdefault(article["area"], []).append(article)
    category_html = []
    for area, items in grouped.items():
        choices = "".join(
            '<label class="quiz-choice"><input type="checkbox" data-quiz-chapter '
            f'data-category="{escape(area, quote=True)}" '
            f'value="{escape(a["file"], quote=True)}">'
            f'<span>{escape(a["title"])}</span></label>'
            for a in items
        )
        category_html.append(
            '<div class="quiz-category">'
            '<label class="quiz-choice quiz-category-title">'
            f'<input type="checkbox" data-quiz-group value="{escape(area, quote=True)}">'
            f'<span>{escape(area)}</span></label>'
            f'<div class="quiz-options">{choices}</div></div>'
        )
    payload = json.dumps({"chapters": articles, "questions": questions},
                         ensure_ascii=False).replace("<", "\\u003c")
    body = (
        '<p class="eyebrow">Mettiti alla prova</p>'
        '<h1 class="page-title">Quiz</h1>'
        '<p class="lede">Scegli i capitoli, anche di categorie differenti, e il livello di difficoltà.</p>'
        '<section id="quiz-config" aria-labelledby="quiz-config-title">'
        '<div class="quiz-layout"><div class="quiz-panel">'
        '<h2 id="quiz-config-title" tabindex="-1">Capitoli</h2>'
        '<p class="quiz-muted">Seleziona uno o più capitoli, oppure un’intera categoria.</p>'
        + ('<p class="quiz-empty-notice" role="status">Nessuna domanda disponibile al momento.</p>'
           if not questions else '') +
        "".join(category_html) +
        '</div><aside class="quiz-panel"><h2>Impostazioni</h2>'
        '<fieldset class="quiz-levels"><legend>Difficoltà</legend>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="easy" checked>'
        '<strong>Facile</strong><small>3 alternative</small></label>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="medium">'
        '<strong>Media</strong><small>4 alternative</small></label>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="hard">'
        '<strong>Difficile</strong><small>5 alternative</small></label>'
        '</fieldset><div class="quiz-count-control">'
        '<label for="quiz-count">Numero di domande</label>'
        '<div class="quiz-count-stepper">'
        '<button type="button" id="quiz-count-minus" aria-label="Diminuisci numero di domande">−</button>'
        '<input type="number" id="quiz-count" min="1" max="30" step="1" value="25" inputmode="numeric">'
        '<button type="button" id="quiz-count-plus" aria-label="Aumenta numero di domande">+</button>'
        '</div></div>'
        '<p class="quiz-duration-note">2 minuti per domanda · Tempo massimo: '
        '<output id="quiz-duration" for="quiz-count">50:00</output></p>'
        '<button type="button" class="quiz-action quiz-action-primary" id="quiz-start" disabled>Inizia il quiz →</button>'
        '<p class="quiz-error" id="quiz-config-error" role="alert" hidden></p>'
        '<p class="quiz-help">Le domande saranno disponibili quando verrà caricato il relativo archivio.</p>'
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
        '<button class="quiz-action" type="button" id="quiz-skip">Salta</button>'
        '<button class="quiz-action quiz-action-primary" type="button" id="quiz-next" disabled>Conferma e prosegui</button>'
        '</div>'
        '<button class="quiz-action quiz-action-stop" type="button" id="quiz-stop">Concludi</button>'
        '</div></div></section>'
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
        '<span><i class="quiz-legend-marker is-answered" aria-hidden="true"></i>Risposta data</span>'
        '<span><i class="quiz-legend-marker is-skipped" aria-hidden="true"></i>Saltata</span>'
        '<span><i class="quiz-legend-marker" aria-hidden="true"></i>Non raggiunta</span></div>'
        '<ol id="quiz-review" class="quiz-review"></ol></div></section>'
        '<noscript><p>Per svolgere il quiz serve JavaScript.</p></noscript>'
        f'<script type="application/json" id="quiz-data">{payload}</script>'
        '<script src="quiz/interfaccia.js" defer></script>'
    )
    page = shell("Quiz", body, source, service=True)
    return page.replace("</head>", '<link rel="stylesheet" href="quiz/interfaccia.css"></head>', 1)
