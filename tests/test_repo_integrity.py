"""Pruebas locales del material educativo, no de un agente en la nube."""
import csv
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class DemoKitTests(unittest.TestCase):
    def test_docs(self):
        for name in ["README.md", "SECURITY.md", "docs/03-arquitectura.md",
                     "docs/05-sdd-contrato.md", "samples/bienvenida-ejemplo.mcs.yaml"]:
            with self.subTest(path=name):
                self.assertTrue((ROOT / name).is_file())

    def test_matrix(self):
        with (ROOT / "tests/casos_v2.csv").open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(18, len(rows))
        self.assertEqual(18, len({r["id"] for r in rows}))

    def test_mcp_example(self):
        with (ROOT / ".vscode/mcp.example.json").open(encoding="utf-8") as f:
            config = json.load(f)
        self.assertEqual("npx", config["servers"]["copilot-studio-mcp"]["command"])
        self.assertNotIn("client_secret", str(config).lower())

    def test_svg_architecture(self):
        self.assertTrue((ROOT / "assets/carousel/01-arquitectura.svg").is_file())

if __name__ == "__main__":
    unittest.main()
