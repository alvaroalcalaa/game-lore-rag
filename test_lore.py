import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import lore


class RetrievalTests(unittest.TestCase):
    def test_founder_retrieval_and_citation(self):
        chunks = lore.load_chunks(Path(__file__).parent / "docs")
        results = lore.search("¿Quién fundó Aurora? Nara", chunks, 1)
        self.assertEqual(len(results), 1)
        self.assertIn("fundada", results[0]["text"])
        self.assertIn("Fuente: aurora.md", lore.extractive_answer(results))

    def test_unknown_question_abstains(self):
        chunks = lore.load_chunks(Path(__file__).parent / "docs")
        results = lore.search("¿Cuántos dinosaurios jurásicos existen?", chunks)
        self.assertEqual(results, [])
        self.assertIn("No encuentro evidencia", lore.extractive_answer(results))

    def test_accent_normalization(self):
        self.assertEqual(lore.tokens("BRÚJULA"), ["brujula"])

    def test_long_document_is_chunked(self):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "long.txt").write_text("semilla " * 450)
            chunks = lore.load_chunks(Path(directory))
            self.assertGreater(len(chunks), 1)
            self.assertTrue(all(len(c["text"].split()) <= 200 for c in chunks))

    def test_empty_query(self):
        self.assertEqual(lore.search("¿de la y?", [{"text": "Aurora"}]), [])

    def test_generation_abstains_without_network(self):
        with patch("lore.urlopen") as request:
            self.assertIn("No encuentro evidencia", lore.generate("nada", [], "demo"))
            request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
