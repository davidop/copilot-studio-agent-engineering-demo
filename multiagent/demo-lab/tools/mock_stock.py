#!/usr/bin/env python3
"""Local deterministic read-only mock. NOT a deployed Copilot Studio tool."""
import argparse
import json
from pathlib import Path

DATA = Path(__file__).with_name("fixtures") / "stock.json"

def lookup(item_code: str, location: str) -> dict:
    fixture = json.loads(DATA.read_text(encoding="utf-8"))
    match = next((x for x in fixture["items"]
                  if x["itemCode"] == item_code and x["location"] == location), None)
    units = int(match["availableUnits"]) if match else 0
    return {
        "itemCode": item_code,
        "location": location,
        "knownItem": bool(match),
        "available": units > 0,
        "availableUnits": units,
        "simulated": True,
        "source": fixture["fixtureId"],
        "asOf": fixture["timestamp"],
        "operationPerformed": "read_only_lookup",
        "note": "Inventario sintético de demostración. No garantiza disponibilidad real."
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--item-code", required=True)
    parser.add_argument("--location", required=True)
    args = parser.parse_args()
    print(json.dumps(lookup(args.item_code, args.location), ensure_ascii=False))
