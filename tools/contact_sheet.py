"""Render every registered icon to a labelled grid for eyeballing."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ispy.icons import ICONS
from ispy.render import place, svg_doc, write_png
from ispy.text import text

names = sorted(ICONS)
if len(sys.argv) > 1 and sys.argv[1] != "all":
    names = [n for n in names if n in sys.argv[1].split(",")]

COLS, CELL, SIZE = 8, 96, 62
rows = (len(names) + COLS - 1) // COLS
W, H = COLS * CELL + 40, rows * CELL + 60
body = [text("icon contact sheet", 20, 32, "display", 18)]
for i, n in enumerate(names):
    cx = 20 + CELL * (i % COLS) + CELL / 2
    cy = 50 + CELL * (i // COLS) + CELL / 2 - 6
    body.append(f'<rect x="{cx-CELL/2+4}" y="{cy-CELL/2+2}" width="{CELL-8}" '
                f'height="{CELL-8}" fill="none" stroke="#e2e2e2"/>')
    body.append(place(ICONS[n](), cx, cy, SIZE, 0, 1.35))
    body.append(text(n.replace("_", " "), cx, cy + CELL / 2 - 4, "hand-light", 12,
                     "middle"))
svg = svg_doc("".join(body), W, H)
out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/claude-0/-home-user-preschool/526710c1-a0ce-5892-9ead-1b3780dcd259/scratchpad/contact.png"
write_png(svg, out, dpi=150)
print(out, len(names), "icons")
