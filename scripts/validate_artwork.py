#!/usr/bin/env python3
"""Fail CI when native-resolution X1 artwork or its HTML contract drifts."""
from pathlib import Path
import re
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
BOSSES = ("chill-penguin", "spark-mandrill", "armored-armadillo",
          "launch-octopus", "boomer-kuwanger", "sting-chameleon",
          "storm-eagle", "flame-mammoth")
ITEMS = ("legs", "body", "helmet", "arms", "sub-tank", "extra-life")
errors = []
html = (ROOT / "index.html").read_text(encoding="utf-8")
x1 = html.split('data-game="x1"', 1)[-1].split('data-game="x2"', 1)[0]

def validate_png(name, expected):
    path = ROOT / (name + ".png")
    if not path.is_file():
        errors.append(f"Missing: {path.name}")
        return
    raw = path.read_bytes()
    if len(raw) < 24 or raw[:8] != b"\x89PNG\\r\n\x1a\n" or raw[12:16] != b"IHDR":
        errors.append(f"Invalid PNG header: {path.name}")
        return
    size = struct.unpack(">II", raw[16:24])
    if size != expected:
        errors.append(f"{path.name}: {size}, expected {expected}")

for name in BOSSES:
    validate_png(name, (28, 31))
    if f'src="./{name}.png" width="28" height="31"' not in x1:
        errors.append(f"Missing native-size HTML portrait reference: {name}")
for name in ITEMS:
    validate_png(name, (22, 24))
    if f'src="./{name}.png" width="22" height="24"' not in x1:
        errors.append(f"Missing native-size HTML icon reference: {name}")

if x1.count('class="boss-art"') != 8:
    errors.append("X1 must contain exactly eight boss portraits")
if x1.count('class="item-art"') != 8:
    errors.append("X1 must contain exactly eight collectible images")
if x1.count('class="collect-toggle"') != 8:
    errors.append("X1 must retain eight collectible toggles")
if 'mmxguide-snes-sprites.webp' in x1 or '--sx:' in x1:
    errors.append("X1 must not use legacy sprite-sheet cropping")
if '.boss-art' not in html or '.item-art' not in html:
    errors.append("Native-size artwork CSS rules missing")
if 'object-fit:contain' not in html:
    errors.append("Artwork must use contain, not crop")
if errors:
    print("Artwork QA failed:\n" + "\n".join(" - " + e for e in errors))
    sys.exit(1)
print("Artwork QA passed: 8 bosses, 6 icon types, 8 collectibles; native PNG dimensions verified.")
