"""Render the hero characters big, to check them the way a child sees them."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ispy.heroes import HEROES
from ispy.render import place, svg_doc, write_png
from ispy.text import text

names = sorted(HEROES)
if len(sys.argv) > 1 and sys.argv[1] != "all":
    names = [n for n in names if n in sys.argv[1].split(",")]
COLS, CELL, SIZE = 3, 300, 270
rows = (len(names) + COLS - 1) // COLS
W, H = COLS * CELL + 40, rows * CELL + 50
body = [text("hero characters", 20, 34, "display", 20)]
for i, n in enumerate(names):
    cx = 20 + CELL * (i % COLS) + CELL / 2
    cy = 46 + CELL * (i // COLS) + CELL / 2
    body.append(f'<rect x="{cx-CELL/2+6}" y="{cy-CELL/2+6}" width="{CELL-12}" '
                f'height="{CELL-12}" fill="none" stroke="#e4e4e4"/>')
    body.append(place(HEROES[n](), cx, cy, SIZE, 0, 4.4, "#111111"))
    body.append(text(n, cx, cy + CELL / 2 - 12, "hand-light", 15, "middle"))
out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/heroes.png"
write_png(svg_doc("".join(body), W, H, units=""), out, dpi=96)
print(out, len(names), "heroes")
