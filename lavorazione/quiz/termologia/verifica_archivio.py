"""Controlli ripetibili sull'archivio candidato; non modifica il sito pubblico."""
import ast
from collections import Counter
import json
import math
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import quiz_site


def arithmetic(expression):
    """Valuta soltanto numeri e operazioni aritmetiche del ricalcolo."""
    tree = ast.parse(expression, mode='eval')
    allowed = (ast.Expression, ast.Constant, ast.BinOp, ast.UnaryOp,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd)
    assert all(isinstance(node, allowed) for node in ast.walk(tree)), expression
    return eval(compile(tree, '<ricalcolo>', 'eval'), {'__builtins__': {}}, {})


def option_number(text):
    match = re.search(r'[−-]?\d+(?:,\d+)?(?: · 10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)?', text)
    assert match, text
    value = match.group().replace('−', '-').replace(',', '.')
    if ' · 10' in value:
        mantissa, power = value.split(' · 10')
        return float(mantissa) * 10 ** int(power.translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')))
    return float(value)


def main():
    registry = json.loads((ROOT / 'quiz/categorie.json').read_text())
    allowed = {c['id'] for c in registry['categories']}
    quiz_site.DATA = HERE / 'archivio.json'
    questions = quiz_site.load_questions(allowed)
    assert len(questions) == 300
    assert {q['id'] for q in questions} == {f'termo-{n:03}' for n in range(1, 301)}
    assert all(q['category'] == 'termologia' for q in questions)
    assert Counter(q['level'] for q in questions) == {'easy': 100, 'medium': 100, 'hard': 100}
    assert Counter(q['correct'] for q in questions) == {0: 75, 1: 75, 2: 75, 3: 75}
    assert len({q['prompt'].casefold() for q in questions}) == 300
    normalized = [re.sub(r'[−-]?\d+(?:[,.]\d+)?[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]*', 'N', q['prompt'].casefold()) for q in questions]
    assert len(set(normalized)) == 300, 'Testi uguali salvo i numeri'
    fields = {'id', 'category', 'level', 'prompt', 'options', 'correct', 'explanation'}
    assert all(set(q) == fields for q in questions)
    original = []
    for name in ('campione', 'lotto'):
        original.extend(json.loads((HERE / (name + '.json')).read_text())['questions'])
    assert questions[:39] == original, 'Campione o primo lotto non allineati con l’archivio corrente'
    data = json.loads((HERE / 'revisione.json').read_text())
    assert data['baseline_ids'] == [q['id'] for q in original]
    assert set(data['approved_ids']) == set(lookup_id['id'] for lookup_id in questions)
    assert data['pending_ids'] == []
    metadata = data['review']
    assert len(metadata) == 261
    lookup = {q['id']: q for q in questions}
    expected = {'conoscenza': 26, 'ragionamento': 35, 'calcolo': 26}
    for level in ('easy', 'medium', 'hard'):
        assert Counter(m['type'] for m in metadata if m['level'] == level) == expected
    original_meta = []
    labels = {'Facile': 'easy', 'Media': 'medium', 'Difficile': 'hard'}
    for name in ('bozza.md', 'lotto.md'):
        matches = re.findall(r'^### (termo-\d{3}) — (Facile|Media|Difficile), (conoscenza|ragionamento|calcolo)$', (HERE / name).read_text(), re.M)
        original_meta.extend(dict(id=i, level=labels[level], type=kind) for i, level, kind in matches)
    assert len(original_meta) == 39
    assert {m['id'] for m in original_meta} == set(data['baseline_ids'])
    for level in ('easy', 'medium', 'hard'):
        assert Counter(m['type'] for m in original_meta + metadata if m['level'] == level) == {'conoscenza': 30, 'ragionamento': 40, 'calcolo': 30}
    audited = 0
    for m in metadata:
        q = lookup[m['id']]
        assert m['category'] == q['category'] and m['level'] == q['level']
        assert m['provided'] == q['prompt']
        assert m['scope'] in ('specifico', 'trasversale')
        assert 0 < m['estimated_seconds'] <= 120
        assert m['required'] and m['difficulty_reason'] and m['references']
        assert all((ROOT / p).is_file() for p in m['references'])
        if m['type'] == 'calcolo':
            calc = m['calculation']
            value = arithmetic(calc['expression'])
            assert math.isclose(value, calc['expected'], rel_tol=1e-9, abs_tol=1e-10), m['id']
            # Anche la risposta presentata deve coincidere, entro l'arrotondamento.
            selected = option_number(q['options'][q['correct']])
            assert math.isclose(value, selected, rel_tol=.015, abs_tol=1e-8), (m['id'], value, selected)
            audited += 1
        else:
            assert m['calculation'] is None
    assert audited == 78
    seen = []
    for path in sorted((HERE / 'lotti').glob('lotto-*.md')):
        doc = path.read_text()
        sections = re.split(r'^## (termo-\d{3}) — ', doc, flags=re.M)
        assert len(sections[1::2]) == 29, path
        for identifier, section in zip(sections[1::2], sections[2::2]):
            q = lookup[identifier]
            assert q['prompt'] in section
            for i, option in enumerate(q['options']):
                assert f'- **{"ABCD"[i]}.** {option}' in section, identifier
            assert f'**Risposta corretta: {"ABCD"[q["correct"]]}.** {q["explanation"]}' in section, identifier
            seen.append(identifier)
        for target in re.findall(r'\]\(([^)]+)\)', doc):
            if not target.startswith('https:'):
                assert (path.parent / target.split('#')[0]).is_file(), target
    assert len(seen) == len(set(seen)) == 261
    assert set(seen) == {m['id'] for m in metadata}
    assert [q for q in json.loads((ROOT / 'quiz/domande.json').read_text())['questions']
            if q['category'] == 'termologia'] == questions
    report = dict(total=300, approved=300, pending=0,
                  levels=dict(Counter(q['level'] for q in questions)),
                  new_types_by_level={level: dict(Counter(m['type'] for m in metadata if m['level'] == level)) for level in ('easy', 'medium', 'hard')},
                  new_calculations_checked=audited, baseline_sources_match=True,
                  review_batches=9, questions_per_batch=29,
                  answer_positions=dict(Counter(q['correct'] for q in questions)),
                  public_archive_matches=True,
                  limitations='Non prova calibrazione didattica o tempi osservati in classe.')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
