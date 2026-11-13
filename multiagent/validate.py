"""Valida el MATERIAL LOCAL; no autentica ni ejecuta Copilot Studio."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parent
with (root / "evaluation/delegation-matrix.csv").open(encoding="utf-8", newline="") as f:
    matrix = list(csv.DictReader(f))
with (root / "evaluation/copilot-harness-conversations.csv").open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ["conversationNumber", "question", "response"], "CSV harness inválido"
    conversations = list(reader)
assert len(matrix) == len(conversations) == 8, "Se esperaban 8 casos"
assert len({r["id"] for r in matrix}) == 8, "ID duplicado"
assert {r["group"] for r in matrix} >= {"urgente","faq","mixto","seguridad","negativo","adversarial"}
assert all(r["question"].strip() and r["expected_agent_route"].strip() for r in matrix)
assert [r["question"] for r in matrix] == [r["question"] for r in conversations]
assert all(not r["response"].strip() for r in conversations), "Las respuestas deben permanecer vacías: no inventar resultados"
for x in ["agents/orchestrator.md","agents/security.md","agents/knowledge.md","delegation-contract.md"]:
    assert (root/x).exists(), x
print("OK: 3 especificaciones de agentes, 8 casos y CSV importable estructuralmente.")
print("No se ha evaluado ningún agente real.")
