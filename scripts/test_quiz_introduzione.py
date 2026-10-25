"""Controlli tecnici del dataset introduttivo e dell'archivio condiviso."""
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "lavorazione/quiz/introduzione_fisica_misura"
LEVELS = ("easy", "medium", "hard")
FIELDS = {"id", "category", "level", "prompt", "options", "correct", "explanation"}

class IntroQuizArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.intro = json.loads((WORK / "archivio.json").read_text(encoding="utf-8"))["questions"]
        cls.public = [q for category in ("termologia", "introduzione_fisica_misura")
                      for q in json.loads((ROOT / "quiz/domande" / (category + ".json")).read_text(encoding="utf-8"))["questions"]]
        cls.review = json.loads((WORK / "revisione.json").read_text(encoding="utf-8"))["questions"]

    def test_count_categories_and_preservation(self):
        self.assertEqual(len(self.intro), 300)
        self.assertEqual(len(self.public), 600)
        by_category = Counter(q["category"] for q in self.public)
        self.assertEqual(by_category, {"termologia": 300, "introduzione_fisica_misura": 300})
        self.assertEqual([q for q in self.public if q["category"] == "introduzione_fisica_misura"], self.intro)
        self.assertEqual({q["id"] for q in self.public}, {q["id"] for q in self.intro} |
                         {f"termo-{i:03}" for i in range(1, 301)})

    def test_schema_and_levels(self):
        self.assertEqual([q["id"] for q in self.intro],
                         [f"intro-{i:03}" for i in range(1, 301)])
        self.assertEqual(Counter(q["level"] for q in self.intro),
                         {"easy": 100, "medium": 100, "hard": 100})
        prompts = set()
        for q in self.intro:
            self.assertEqual(set(q), FIELDS)
            self.assertEqual(q["category"], "introduzione_fisica_misura")
            self.assertEqual(len(q["options"]), 4)
            self.assertEqual(len(set(q["options"])), 4)
            self.assertIn(q["correct"], range(4))
            self.assertTrue(q["prompt"].strip())
            self.assertTrue(q["explanation"].strip())
            self.assertNotIn(q["prompt"].casefold(), prompts)
            prompts.add(q["prompt"].casefold())

    def test_sources_and_review(self):
        sample = json.loads((WORK / "campione.json").read_text(encoding="utf-8"))["questions"]
        self.assertEqual(self.intro[:9], sample)
        pieces = ("metodo_scientifico", "grandezze_si", "potenze", "prefissi",
                  "cifre_significative", "strumenti_a", "strumenti_b",
                  "incertezza_a", "incertezza_b", "piano_a", "piano_b",
                  "proporzionalita_a", "proporzionalita_b")
        assembled = sample[:]
        for name in pieces:
            assembled.extend(json.loads((WORK / "lotti" / (name + ".json")).read_text(encoding="utf-8"))["questions"])
        self.assertEqual(self.intro, sorted(assembled, key=lambda q: q["id"]))
        self.assertEqual(len(self.review), 300)
        self.assertEqual({m["id"] for m in self.review}, {q["id"] for q in self.intro})
        for m in self.review:
            self.assertIn(m["type"], ("conoscenza", "ragionamento", "calcolo"))
            self.assertTrue(m["references"])
            self.assertTrue(all((ROOT / p).is_file() for p in m["references"]))
            self.assertGreater(m["estimated_seconds"], 0)
            self.assertLessEqual(m["estimated_seconds"], 120)

if __name__ == "__main__":
    unittest.main()
