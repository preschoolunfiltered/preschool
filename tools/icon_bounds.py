#!/usr/bin/env python3
"""Measure each icon's real ink bounds, cached to assets/icon_bounds.json.

Icons are authored inside a 100x100 box but fill wildly different fractions
of it - a rainbow is wide and flat, a pencil is tall and thin, a flower pot
sits in the middle of a lot of air. On an I Spy sheet that variety is a
feature. On a coloring page, where one subject has to fill the paper, it
means every subject needs to be scaled by what it actually covers rather
than by its nominal box. Measuring the rendered ink is the reliable way:
parsing arbitrary path data for a bounding box is a much bigger job.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cairosvg
from PIL import Image

from ispy.coloring import art, outline
from ispy.heroes import HEROES
from ispy.render import svg_doc, place

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "icon_bounds.json")
PX = 200  # render size; 2px of slop at this scale is 1 unit in icon space


def bounds_of(name: str, tmp: str, body: str | None = None):
    svg = svg_doc(place(body or art(name), 100, 100, 200, 0, 3.0, "#000000"),
                  200, 200, units="")
    cairosvg.svg2png(bytestring=svg.encode(), write_to=tmp,
                     output_width=PX, output_height=PX,
                     background_color="#ffffff")
    im = Image.open(tmp).convert("L")
    ink = im.point(lambda v: 255 if v < 200 else 0)
    box = ink.getbbox()
    if not box:
        return [0.0, 0.0, 100.0, 100.0]
    # px -> the 0..100 icon box (the icon was drawn at 2x into a 200px frame)
    return [round(v / PX * 100.0, 2) for v in box]


def main():
    from ispy.icons import ICONS
    tmp = os.path.join(ROOT, ".bounds-tmp.png")
    out = {}
    for name in sorted(ICONS):
        out[name] = bounds_of(name, tmp)
    for key in sorted(HEROES):           # heroes share the same 100-unit box
        out["hero:" + key] = bounds_of(key, tmp, outline(HEROES[key]()))
    os.remove(tmp)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=0, sort_keys=True)
    widest = max(out.items(), key=lambda kv: kv[1][2] - kv[1][0])
    print(f"measured {len(out)} icons -> {os.path.relpath(OUT, ROOT)}")
    print("widest:", widest[0], widest[1])


if __name__ == "__main__":
    main()
