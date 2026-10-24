"""Pagina Quiz di Stringhe: catalogo e dataset esterni, grafica condivisa."""
from collections import OrderedDict
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "quiz" / "domande-prova.json"
LEVELS = {"easy": 3, "medium": 4, "hard": 5}


def load_questions(allowed):
    archive = json.loads(DATA.read_text(encoding="utf-8"))
    if archive.get("status") != "demo" or not isinstance(archive.get("questions"), list):
        raise ValueError("Archivio di prova non valido")
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
        + "".join(category_html) +
        '</div><aside class="quiz-panel"><h2>Impostazioni</h2>'
        '<fieldset class="quiz-levels"><legend>Difficoltà</legend>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="easy" checked>'
        '<strong>Facile</strong><small>3 alternative, 2 min 30 s per domanda</small></label>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="medium">'
        '<strong>Media</strong><small>4 alternative, 2 min per domanda</small></label>'
        '<label class="quiz-level"><input type="radio" name="quiz-level" value="hard">'
        '<strong>Difficile</strong><small>5 alternative, 1 min 30 s per domanda</small></label>'
        '</fieldset><p><strong>25 domande</strong> a risposta multipla</p>'
        '<button type="button" class="quiz-action quiz-action-primary" id="quiz-start" disabled>Inizia il quiz →</button>'
        '<p class="quiz-error" id="quiz-config-error" role="alert" hidden></p>'
        '<p class="quiz-help">Archivio dimostrativo: alcune domande possono ripetersi. '
        'Il punteggio è indicativo, non adatto a verifiche valutative.</p>'
        '</aside></div></section>'
        '<section id="quiz-active" hidden aria-label="Quiz in corso"><div class="quiz-panel">'
        '<div class="quiz-status"><strong id="quiz-counter">Domanda 1 di 25</strong>'
        '<div>Tempo rimanente <span class="quiz-clock" id="quiz-clock" role="timer">00:00</span></div></div>'
        '<div class="quiz-progress" aria-hidden="true"><span id="quiz-progress-fill"></span></div>'
        '<p class="quiz-kicker" id="quiz-topic"></p>'
        '<h2 id="quiz-prompt" class="quiz-question" tabindex="-1"></h2>'
        '<fieldset class="quiz-answers" id="quiz-answers" aria-label="Scegli una risposta"></fieldset>'
        '<div class="quiz-actions-row">'
        '<button class="quiz-action" type="button" id="quiz-skip">Salta</button>'
        '<button class="quiz-action" type="button" id="quiz-stop">Concludi</button>'
        '<button class="quiz-action quiz-action-primary" type="button" id="quiz-next" disabled>Conferma e prosegui</button>'
        '</div></div></section>'
        '<section id="quiz-results" hidden aria-labelledby="quiz-results-title">'
        '<div class="quiz-panel"><p class="eyebrow">Risultato</p>'
        '<h2 id="quiz-results-title" tabindex="-1">Il tuo quiz</h2>'
        '<div class="quiz-score" id="quiz-grade">0,0 / 10</div>'
        '<p id="quiz-finished-reason"></p>'
        '<div class="quiz-metrics"><div><strong id="quiz-correct">0</strong>Corrette</div>'
        '<div><strong id="quiz-wrong">0</strong>Errate o non risposte</div></div>'
        '<button type="button" id="quiz-again" class="quiz-action quiz-action-primary">Nuovo quiz</button>'
        '<h2 style="margin-top:36px">Revisione delle risposte</h2>'
        '<ol id="quiz-review" class="quiz-review"></ol></div></section>'
        '<noscript><p>Per svolgere il quiz serve JavaScript.</p></noscript>'
        f'<script type="application/json" id="quiz-data">{payload}</script>'
        '<script src="quiz/interfaccia.js" defer></script>'
    )
    page = shell("Quiz", body, source, service=True)
    return page.replace("</head>", '<link rel="stylesheet" href="quiz/interfaccia.css"></head>', 1)
