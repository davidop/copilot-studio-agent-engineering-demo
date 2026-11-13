"""Pruebas offline de integridad del repositorio; no se conectan a Copilot Studio."""
import csv
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class DemoKitTests(unittest.TestCase):
    def test_required_docs_and_agents(self):
        required = [
            "README.md", "SECURITY.md", "docs/02-guion-directo.md",
            "docs/00-checklist-20min.md", "multiagent/README.md",
            "multiagent/agents/orchestrator.md", "multiagent/agents/security.md",
            "multiagent/agents/knowledge.md", "multiagent/delegation-contract.md",
            "legacy-standard/README.md"
        ]
        for name in required:
            with self.subTest(path=name):
                self.assertTrue((ROOT / name).is_file())

    def test_new_harness_csv_structure(self):
        with (ROOT / "multiagent/evaluation/copilot-harness-conversations.csv").open(encoding="utf-8", newline="") as f:
            reader=csv.DictReader(f)
            self.assertEqual(["conversationNumber","question","response"],reader.fieldnames)
            rows=list(reader)
        self.assertEqual(8,len(rows))
        self.assertEqual([str(x) for x in range(1,9)],[r["conversationNumber"] for r in rows])
        self.assertTrue(all(not r["response"] for r in rows))

    def test_multiagent_expected_routes(self):
        with (ROOT / "multiagent/evaluation/delegation-matrix.csv").open(encoding="utf-8", newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(8,len(rows))
        self.assertEqual(8,len({r["id"] for r in rows}))
        expected={r["id"]:r["expected_agent_route"] for r in rows}
        self.assertIn("Security Agent",expected["SEC-01"])
        self.assertIn("Knowledge Agent",expected["KNO-01"])
        self.assertIn("Security Agent + Knowledge Agent",expected["MIX-01"])

    def test_architecture_art(self):
        for n in range(10,14):
            matches=list((ROOT/"assets/carousel").glob(f"{n}-*.svg"))
            self.assertEqual(1,len(matches))
            self.assertIn("<svg",matches[0].read_text(encoding="utf-8"))

    def test_legacy_scenarios_still_present(self):
        with (ROOT / "tests/casos_v2.csv").open(encoding="utf-8-sig",newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(18,len(rows))

    def test_mcp_example_valid(self):
        with (ROOT / ".vscode/mcp.example.json").open(encoding="utf-8") as f:
            data=json.load(f)
        self.assertEqual("npx",data["servers"]["copilot-studio-mcp"]["command"])

if __name__=="__main__":
    unittest.main()
