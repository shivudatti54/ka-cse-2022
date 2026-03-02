#!/usr/bin/env python3
"""Extract .svg paths from placeholder files and write to svg_path.txt"""
import os

BASE = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template"
OUT = os.path.join(BASE, "content-packs", "vtu-2022-scheme", "svg_path.txt")

FILES = [
    ("content-packs/vtu-2022-scheme/cse/sem-5/sem5-new-placeholder-files.txt", True),   # absolute
    ("content-packs/vtu-2022-scheme/cse/sem-6/sem6-new-placeholder-files.txt", False),  # relative
    ("content-packs/vtu-2022-scheme/cse/sem-7/bcs703-new-placeholder-files.txt", False),
]

paths = []
for rel_path, is_absolute in FILES:
    full_path = os.path.join(BASE, rel_path)
    if not os.path.isfile(full_path):
        continue
    with open(full_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or not line.endswith(".svg"):
                continue
            if is_absolute:
                paths.append(line)
            else:
                paths.append(os.path.join(BASE, line))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write("\n".join(paths) + "\n")

print(f"Wrote {len(paths)} SVG paths to {OUT}")
