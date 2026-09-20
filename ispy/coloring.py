"""Coloring pages built from the same doodle library as the puzzles.

A coloring page wants the opposite of an I Spy sheet: a few big shapes with
chunky outlines and nothing solid black, because a filled shape is a shape a
child cannot color. Every icon is passed through `outline()` on the way in,
which turns the library's solid accents (a ladybug's head, a bee's stripes, a
jack-o'-lantern's face) into empty outlines.
"""

from __future__ import annotations

import math
import random

from ispy import config
from ispy.draw import SOLID, circle, line, path, pt, rect
from ispy.icons import ICONS
from ispy.render import PAGE_H, PAGE_W, SymbolPool, place, svg_doc
from ispy.text import measure, text
from ispy.themes import Theme

INK = "#111111"
MARGIN = 36.0

# chunky, because a preschooler colors up to the line, not inside it
STROKE_HERO = 3.1
STROKE_MID = 2.6
STROKE_SMALL = 2.1
STROKE_TITLE = 2.6

# scenery that reads as sky or ground rather than as a subject
SKY = {"sun", "cloud", "rainbow", "star", "crescent_moon", "moon_craters",
       "shooting_star", "snowflake", "bird", "seagull", "butterfly", "bee",
       "bubbles", "planet", "raindrop", "kite", "bat", "dragonfly"}
GROUND = {"grass_tuft", "sprout", "leaf_sprig", "seaweed", "coral", "fern",
          "mushroom", "pinecone", "acorn", "jelly_bean", "shamrock"}


def outline(body: str) -> str:
    """Solid black accents become outlines, so every shape can be colored."""
    return body.replace(SOLID, 'fill="none"')


def drop(name: str, x: float, y: float, size: float, rot: float = 0.0,
         stroke: float = STROKE_MID, pool=None, flip: bool = False) -> str:
    return place(outline(ICONS[name]()), x, y, size, rot, stroke, INK,
                 name=name + "-c", pool=pool, flip=flip)


def title_block(theme: Theme, note: str, pool=None) -> str:
    """Big hollow letters at the top - the title is colorable too."""
    size = 62.0
    while measure(theme.title, "display", size, 0) > 470 and size > 26:
        size -= 2
    scale = size / 1000.0  # Fredoka's em, near enough for a stroke width
    out = [text(theme.title, PAGE_W / 2, 92, "display", size, "middle", 0,
                "none", f'stroke="{INK}" stroke-width="{STROKE_TITLE / scale:.0f}" '
                        f'stroke-linejoin="round"', pool=pool)]
    if note:
        out.append(text(note, PAGE_W / 2, 118, "hand", 22, "middle", 1.5, INK,
                        pool=pool))
    return "".join(out)


def footer(note: str = "", pool=None) -> str:
    bits = [config.STORE_LINE]
    if note:
        bits.append(note)
    return text("  ·  ".join(bits), PAGE_W / 2, 772, "hand-light", 15,
                "middle", 0.8, "#444444", pool=pool)


def ground_line(y: float, rng: random.Random, tufts: str | None = None,
                pool=None) -> str:
    """A soft wavy horizon so the subjects have somewhere to stand."""
    pts = [(24.0, y)]
    x = 24.0
    while x < PAGE_W - 24:
        x += 58
        pts.append((x, y + rng.uniform(-9, 9)))
    d = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for i in range(1, len(pts) - 1):
        mx = (pts[i][0] + pts[i + 1][0]) / 2
        my = (pts[i][1] + pts[i + 1][1]) / 2
        d.append(f"Q {pts[i][0]:.1f} {pts[i][1]:.1f} {mx:.1f} {my:.1f}")
    d.append(f"L {pts[-1][0]:.1f} {pts[-1][1]:.1f}")
    out = [path(" ".join(d), f'fill="none" stroke="{INK}" '
                             f'stroke-width="{STROKE_HERO}" '
                             f'stroke-linecap="round"')]
    if tufts:
        for tx in (70, 190, 330, 470, 560):
            out.append(drop(tufts, tx + rng.uniform(-14, 14),
                            y + rng.uniform(4, 14), rng.uniform(34, 50), 0,
                            STROKE_SMALL, pool))
    return "".join(out)


def cycler(names, rng: random.Random):
    """Hand out names without repeating until the list is used up."""
    bag = list(names)
    rng.shuffle(bag)
    state = {"i": 0}

    def nxt():
        if state["i"] >= len(bag):
            rng.shuffle(bag)
            state["i"] = 0
        state["i"] += 1
        return bag[state["i"] - 1]
    return nxt


def _pick(theme: Theme, rng: random.Random):
    """Split a theme's icons into subjects, sky things and ground things."""
    icons = list(theme.icons)
    sky = [n for n in icons if n in SKY]
    ground = [n for n in icons if n in GROUND]
    subjects = [n for n in icons if n not in SKY and n not in GROUND] or icons
    return subjects, sky, ground


# ------------------------------------------------------------------ pages ---

def hero_page(theme: Theme, index: int, pool=None) -> str:
    """One big character in the middle, friends all around it."""
    rng = random.Random(f"{theme.key}-hero-{index}")
    subjects, sky, ground = _pick(theme, rng)
    star = subjects[index % len(subjects)]
    friends = cycler([n for n in theme.icons if n != star], rng)

    body = [title_block(theme, "Color me in!", pool)]
    body.append(rect(30, 132, PAGE_W - 60, 620, 26,
                     f'fill="none" stroke="{INK}" stroke-width="2.2" '
                     f'stroke-dasharray="11 9" stroke-linecap="round"'))
    body.append(ground_line(690, rng, ground[0] if ground else None, pool))
    body.append(drop(star, PAGE_W / 2, 430, 250, rng.uniform(-4, 4),
                     STROKE_HERO, pool))

    ring = [(122, 218), (306, 190), (492, 218), (96, 372),
            (516, 372), (126, 560), (306, 606), (492, 560)]
    for i, (x, y) in enumerate(ring):
        body.append(drop(friends(), x, y, rng.uniform(96, 124),
                         rng.uniform(-12, 12), STROKE_MID, pool,
                         flip=bool(i % 2)))
    body.append(footer("Coloring page " + str(index + 1), pool))
    return "".join(body)


def pattern_page(theme: Theme, index: int, pool=None) -> str:
    """A whole page of pictures to work through - the long, calm one."""
    rng = random.Random(f"{theme.key}-pattern-{index}")
    nxt = cycler(theme.icons, rng)

    body = [title_block(theme, "Color them all", pool)]
    cols, rows = 3, 4
    x0, y0, x1, y1 = 48.0, 148.0, 564.0, 744.0
    cw = (x1 - x0) / cols
    ch = (y1 - y0) / rows
    for i in range(cols * rows):
        cx = x0 + cw * (i % cols) + cw / 2 + rng.uniform(-9, 9)
        cy = y0 + ch * (i // cols) + ch / 2 + rng.uniform(-8, 8)
        body.append(drop(nxt(), cx, cy, rng.uniform(118, 140),
                         rng.uniform(-10, 10), STROKE_HERO, pool,
                         flip=bool((i + index) % 3 == 0)))
    body.append(footer("Coloring page " + str(index + 1), pool))
    return "".join(body)


def grid_page(theme: Theme, index: int, pool=None) -> str:
    """Six framed pictures - one color each."""
    rng = random.Random(f"{theme.key}-grid-{index}")
    nxt = cycler(theme.icons, rng)

    body = [title_block(theme, "Give each one a color", pool)]
    cols, rows = 2, 3
    x0, y0, x1, y1 = 56.0, 150.0, 556.0, 736.0
    cw = (x1 - x0) / cols
    ch = (y1 - y0) / rows
    for i in range(cols * rows):
        cx = x0 + cw * (i % cols) + cw / 2
        cy = y0 + ch * (i // cols) + ch / 2
        body.append(rect(cx - cw / 2 + 9, cy - ch / 2 + 8, cw - 18, ch - 16, 18,
                         f'fill="none" stroke="{INK}" stroke-width="2.2" '
                         f'stroke-dasharray="9 8" stroke-linecap="round"'))
        body.append(drop(nxt(), cx, cy, min(cw, ch) * 0.78, rng.uniform(-6, 6),
                         STROKE_HERO, pool))
    body.append(footer("Coloring page " + str(index + 1), pool))
    return "".join(body)


def poster_page(theme: Theme, index: int, pool=None) -> str:
    """Hollow title in the middle with the theme's pictures ringed around it."""
    rng = random.Random(f"{theme.key}-poster-{index}")
    subjects, sky, ground = _pick(theme, rng)
    ring = (subjects + sky)
    rng.shuffle(ring)

    size = 96.0
    while measure(theme.title, "display", size, 0) > 380 and size > 34:
        size -= 3
    scale = size / 1000.0
    body = [
        text(theme.title, PAGE_W / 2, 452, "display", size, "middle", 0, "none",
             f'stroke="{INK}" stroke-width="{3.4 / scale:.0f}" '
             f'stroke-linejoin="round"', pool=pool),
        text("Color every picture", PAGE_W / 2, 500, "hand", 26, "middle", 2,
             INK, pool=pool),
    ]
    cx, cy = PAGE_W / 2, 432.0
    nxt = cycler(ring, rng)
    for i in range(12):
        a = -90 + i * 30
        rx, ry = 242, 268
        x = cx + rx * math.cos(math.radians(a))
        y = cy + ry * math.sin(math.radians(a))
        body.append(drop(nxt(), x, y, rng.uniform(104, 132),
                         rng.uniform(-14, 14), STROKE_MID, pool,
                         flip=bool(i % 3 == 0)))
    body.append(footer("Coloring page " + str(index + 1), pool))
    return "".join(body)


PAGE_KINDS = (
    ("hero", "Big picture", hero_page),
    ("pattern", "Color them all", pattern_page),
    ("grid", "Six pictures", grid_page),
    ("poster", "Poster", poster_page),
)


def cover_page(theme: Theme, n_pages: int, pool=None) -> str:
    rng = random.Random(theme.key + "-color-cover")
    ew = measure("COLOR ME", "hand", 32, 7)
    body = [
        text("COLOR ME", PAGE_W / 2, 104, "hand", 32, "middle", 7, INK,
             pool=pool),
        line(PAGE_W / 2 - ew / 2 - 50, 96, PAGE_W / 2 - ew / 2 - 16, 96,
             f'stroke="{INK}" stroke-width="1.8" stroke-linecap="round"'),
        line(PAGE_W / 2 + ew / 2 + 16, 96, PAGE_W / 2 + ew / 2 + 50, 96,
             f'stroke="{INK}" stroke-width="1.8" stroke-linecap="round"'),
    ]
    size = 64.0
    while measure(theme.title, "display", size, 0) > 486 and size > 24:
        size -= 2
    scale = size / 1000.0
    body.append(text(theme.title, PAGE_W / 2, 174, "display", size, "middle", 0,
                     "none", f'stroke="{INK}" stroke-width="{2.8 / scale:.0f}" '
                             f'stroke-linejoin="round"', pool=pool))
    body.append(text(theme.subtitle, PAGE_W / 2, 206, "hand-light", 23,
                     "middle", 1, INK, pool=pool))

    panel = (66.0, 234.0, 546.0, 610.0)
    body.append(rect(panel[0], panel[1], panel[2] - panel[0],
                     panel[3] - panel[1], 22,
                     f'fill="none" stroke="{INK}" stroke-width="2.6"'))
    picks = list(theme.icons)
    cols = 4
    rows = math.ceil(min(len(picks), 12) / cols)
    cw = (panel[2] - panel[0]) / cols
    ch = (panel[3] - panel[1]) / rows
    for i, name in enumerate(picks[:cols * rows]):
        x = panel[0] + cw * (i % cols) + cw / 2
        y = panel[1] + ch * (i // cols) + ch / 2
        body.append(drop(name, x, y, 86, rng.uniform(-8, 8), STROKE_MID, pool))

    body.append(text(f"{n_pages} coloring pages  ·  big, chunky lines",
                     PAGE_W / 2, 648, "hand", 25, "middle", 1, INK, pool=pool))
    body.append(text("Preschool · Pre-K · Kindergarten · "
                     "Fine motor · Calm corner", PAGE_W / 2, 676,
                     "hand-light", 19, "middle", 1, INK, pool=pool))
    body.append(text(config.BRAND, PAGE_W / 2, 734, "display", 22, "middle", 0,
                     INK, pool=pool))
    body.append(footer(pool=pool))
    return "".join(body)


def pages_for(theme: Theme, per_kind: int = 1):
    """[(kind, label, svg_body_fn), ...] for one theme's coloring set."""
    out = []
    for i in range(per_kind):
        for kind, label, fn in PAGE_KINDS:
            out.append((kind, label if per_kind == 1 else f"{label} {i + 1}",
                        lambda p, fn=fn, i=i: fn(theme, i, p)))
    return out


def build_page(fn, compact: bool = False) -> str:
    pool = SymbolPool() if compact else None
    body = fn(pool)
    if pool is not None:
        body = pool.defs() + body
    return svg_doc(body)
