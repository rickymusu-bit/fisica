"""Componente Quiz di Stringhe: presentazione separata dal dataset di prova."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render_quiz_body(items):
    groups = {}
    for item in items:
        groups.setdefault(item["area"], []).append(item)
    categories = []
    for area, chapters in groups.items():
        controls = []
        for item in chapters:
            controls.append(
                '<label class="quiz-check">'
                f'<input type="checkbox" data-quiz-chapter data-category="{escape(area, quote=True)}" '
                f'value="{escape(item["file"], quote=True)}">'
                f'<span>{escape(item["title"])}</span></label>')
        categories.append(
            '<section class="quiz-category">'
            '<div class="quiz-category-head"><label class="quiz-check">'
            f'<input type="checkbox" data-quiz-category value="{escape(area, quote=True)}">'
            f'<span>{escape(area)}</span></label>'
            f'<small>{len(chapters)} capitoli</small></div>'
            f'<div class="quiz-chapters">{"".join(controls)}</div>'
            '</section>')
    levels = [
        ('facile', 'Facile', '3 alternative, 2 min 30 s a domanda'),
        ('medio', 'Medio', '4 alternative, 2 min a domanda'),
        ('difficile', 'Difficile', '5 alternative, 1 min 30 s a domanda'),
    ]
    difficulty = ''.join(
        f'<label><input type="radio" name="quiz-livello" value="{value}" '
        f'{"checked" if value == "facile" else ""}>'
        f'<strong>{label}</strong><small>{desc}</small></label>'
        for value, label, desc in levels)
    return (
        '<div class="quiz-layout" data-quiz-app>'
        '<section class="quiz-screen" id="quiz-selection">'
        '<p class="eyebrow">Mettiti alla prova</p><h1 class="page-title">Quiz</h1>'
        '<p class="lede quiz-intro">Scegli i capitoli e la difficoltà. '
        'Puoi combinare argomenti di aree diverse.</p>'
        '<div class="quiz-panel"><div class="quiz-heading"><h2>Argomenti</h2>'
        '<span class="quiz-counter" id="quiz-selection-count">0 capitoli selezionati</span></div>'
        f'{"".join(categories)}</div>'
        '<div class="quiz-panel"><h2>Difficoltà</h2>'
        f'<div class="quiz-difficulty" role="radiogroup" aria-label="Scegli difficoltà">{difficulty}</div>'
        '<div class="quiz-summary"><div><strong id="quiz-length">25 domande</strong>'
        '<small>Tempo massimo: <span id="quiz-total-time">62:30</span></small></div>'
        '<button class="quiz-start" type="button" id="quiz-start" disabled>Inizia il quiz →</button></div>'
        '<p class="quiz-error" id="quiz-warning" role="status"></p>'
        '<p class="quiz-footnote">Versione di prova con domande dimostrative, non ancora validate per la valutazione.</p>'
        '</div></section>'
        '<section id="quiz-game" class="quiz-screen" hidden>'
        '<div class="quiz-panel"><div class="quiz-top">'
        '<strong id="quiz-current">Domanda 1 di 25</strong>'
        '<div aria-label="Tempo totale residuo"><span class="quiz-footnote">Tempo rimasto</span> '
        '<span id="quiz-clock" class="quiz-clock">62:30</span></div></div>'
        '<progress id="quiz-progress" class="quiz-progress" max="25" value="1" aria-label="Avanzamento del quiz"></progress>'
        '<p class="quiz-question-label" id="quiz-topic"></p>'
        '<h2 id="quiz-question-text" class="quiz-question" tabindex="-1"></h2>'
        '<div id="quiz-answers" role="radiogroup" aria-label="Seleziona la risposta"></div>'
        '<div class="quiz-question-actions"><button id="quiz-skip" class="quiz-muted-button" type="button">Salta</button>'
        '<button id="quiz-next" class="quiz-next" type="button" disabled>Conferma e continua</button></div>'
        '<div class="quiz-summary"><small>Il tempo non utilizzato in una domanda non si trasferisce alla successiva.</small>'
        '<button id="quiz-finish" type="button" class="quiz-muted-button">Termina</button></div>'
        '</div></section>'
        '<section id="quiz-results-screen" class="quiz-screen" hidden>'
        '<p class="eyebrow">Risultati</p><h1 id="quiz-results-title" class="page-title" tabindex="-1">Il tuo risultato</h1>'
        '<p id="quiz-result-note" class="lede"></p>'
        '<div class="quiz-results" aria-label="Riepilogo del quiz">'
        '<div class="quiz-result-stat"><strong id="quiz-mark">—</strong><span>Voto in decimi</span></div>'
        '<div class="quiz-result-stat"><strong id="quiz-correct">—</strong><span>Risposte corrette</span></div>'
        '<div class="quiz-result-stat"><strong id="quiz-wrong">—</strong><span>Risposte errate</span></div>'
        '</div><p><span id="quiz-unanswered">0</span> domande senza risposta.</p>'
        '<div class="quiz-panel"><h2>Correzione completa</h2><div id="quiz-review-list"></div></div>'
        '<button class="quiz-retry" type="button" id="quiz-retry">Nuovo quiz →</button>'
        '</section>'
        '<script type="application/json" id="quiz-catalogue-data">'
        + json.dumps(items, ensure_ascii=False).replace('<', r'\u003c') + '</script>'
        '<script type="application/json" id="quiz-demo-data">'
        + json.dumps(json.loads((ROOT / "quiz/domande-prova.json").read_text(encoding="utf-8")),
                     ensure_ascii=False, separators=(",", ":")).replace('<', r'\u003c') + '</script>'
        '</div>')


def add_quiz_assets(document):
    css = (ROOT / "quiz/interfaccia.css").read_text(encoding="utf-8")
    javascript = (ROOT / "quiz/interfaccia.js").read_text(encoding="utf-8")
    document = document.replace("</head>", "<style data-quiz-styles>" + css + "</style></head>", 1)
    return document.replace("</body>", "<script data-quiz-engine>" + javascript + "</script></body>", 1)
