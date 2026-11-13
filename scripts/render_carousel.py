#!/usr/bin/env python3
"""Render four public Christmas carousel SVGs to matching PNGs.

Deterministic export, no external network or cloud credentials. Requires CairoSVG.
This does not convert or reupload the original AI-generated artwork from ChatGPT;
it rasterizes the versioned, editable SVGs stored in this repository.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "assets" / "carousel"
NAMES = (
    "10-multiagent-arquitectura",
    "11-multiagent-mcp",
    "12-multiagent-evaluacion",
    "13-multiagent-quality-gate",
)

def main():
    for name in NAMES:
        src = DIR / f"{name}.svg"
        dest = DIR / f"{name}.png"
        ET.parse(src)  # fail if the SVG source is malformed
        cairosvg.svg2png(
            url=str(src),
            write_to=str(dest),
            output_width=1200,
            output_height=1500,
        )
        with dest.open("rb") as image:
            assert image.read(8) == b"\x89PNG\r\n\x1a\n", dest
        print(f"OK {dest.relative_to(ROOT)} ({dest.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
