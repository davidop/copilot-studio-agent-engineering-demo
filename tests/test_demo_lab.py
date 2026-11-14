"""Static / local checks only. Real agent calls must be verified in Copilot Studio."""
import csv
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "multiagent" / "demo-lab"
sys.path.insert(0, str(LAB / "tools"))
from mock_stock import lookup  # noqa: E402


class DemoLabTests(unittest.TestCase):
    def test_lab_assets(self):
        for p in (
            "knowledge/seguridad-incidentes.md",
            "knowledge/soporte-navidad.md",
            "skills/security-triage/SKILL.md",
            "tools/README.md",
            "tools/fixtures/stock.json",
            "evaluation/proof-matrix.csv",
        ):
            with self.subTest(asset=p):
                self.assertTrue((LAB / p).is_file())

    def test_domain_knowledge_is_separate(self):
        sec = (LAB / "knowledge/seguridad-incidentes.md").read_text(encoding="utf-8")
        it = (LAB / "knowledge/soporte-navidad.md").read_text(encoding="utf-8")
        self.assertIn("SEG-INC-2026", sec)
        self.assertIn("IT-NAV-2026", it)
        self.assertNotIn("availableUnits", it)
        self.assertNotIn("LOAN-14", sec)

    def test_skill_has_upload_frontmatter(self):
        skill = (LAB / "skills/security-triage/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\nname: security-triage\n"))
        self.assertIn("description:", skill)
        self.assertIn("## Procedimiento", skill)

    def test_mock_stock_available(self):
        result = lookup("LOAN-14", "MAD")
        self.assertTrue(result["simulated"])
        self.assertTrue(result["available"])
        self.assertEqual(2, result["availableUnits"])
        self.assertEqual("read_only_lookup", result["operationPerformed"])

    def test_mock_stock_unknown_not_misrepresented(self):
        result = lookup("UNKNOWN", "MAD")
        self.assertFalse(result["knownItem"])
        self.assertFalse(result["available"])
        self.assertTrue(result["simulated"])

    def test_proof_matrix_is_unfilled(self):
        with (LAB / "evaluation/proof-matrix.csv").open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(6, len(rows))
        self.assertIn("MIX-TOOL", {r["case_id"] for r in rows})
        self.assertTrue(all(not r["real_evaluation_result"] for r in rows))


if __name__ == "__main__":
    unittest.main()
