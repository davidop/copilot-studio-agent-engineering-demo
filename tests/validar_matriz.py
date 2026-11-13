"""Validación offline de la estructura de escenarios; NO prueba agentes cloud."""
import csv
from collections import Counter
from pathlib import Path

path = Path(__file__).with_name("casos_v2.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    expected = ["id", "grupo", "entrada", "comportamiento_esperado", "criterio_humano", "criticidad"]
    assert reader.fieldnames == expected, "Columnas incorrectas"
    rows = list(reader)

assert len(rows) == 18, f"Se esperaban 18 casos, hay {len(rows)}"
assert len({row["id"] for row in rows}) == len(rows), "IDs duplicados"
assert all(all(row[col].strip() for col in expected) for row in rows), "Campos vacíos"
counts = Counter(row["grupo"] for row in rows)
assert set(["urgente", "faq", "seguridad", "adversarial", "negativo"]) <= set(counts)
print(f"OK: {len(rows)} escenarios definidos; grupos: {dict(counts)}")
print("AVISO: no son resultados de ejecución en Copilot Studio.")
