"""Page composition: header, frame, puzzle field, legend, covers."""

from __future__ import annotations

import math
import random

from ispy import config
from ispy.draw import dot, heart, line, path, pt, rect, star
from ispy.icons import ICONS
from ispy.render import PAGE_H, PAGE_W, SymbolPool, place, svg_doc
from ispy.scatter import counts_for, scatter, tally
from ispy.text import measure, text
from ispy.themes import Theme

MARGIN = 36.0
FRAME = (36.0, 116.0, 576.0, 632.0)      # x0, y0, x1, y1
FIELD_INSET = 21.0
LEGEND_TOP = 652.0
ROW_H = 37.0
FOOTER_Y = 784.0

INK = "#111111"


# --------------------------------------------------------------- header ----

def header(theme: Theme, style: str, note: str = "", pool=None) -> str:
    out = []
    eyebrow = theme.eyebrow
    ew = measure(eyebrow, "hand", 26, 5)
    out.append(text(eyebrow, PAGE_W / 2, 64, "hand", 26, "middle", 5, INK, pool=pool))
    out.append(line(PAGE_W / 2 - ew / 2 - 46, 58, PAGE_W / 2 - ew / 2 - 14, 58,
                    f'stroke="{INK}" stroke-width="1.6" stroke-linecap="round"'))
    out.append(line(PAGE_W / 2 + ew / 2 + 14, 58, PAGE_W / 2 + ew / 2 + 46, 58,
                    f'stroke="{INK}" stroke-width="1.6" stroke-linecap="round"'))

    size = 46.0 if style != "scallop" else 52.0
    kind = "display" if style != "scallop" else "hand"
    while measure(theme.title, kind, size, 0) > 470 and size > 20:
        size -= 1.5
    out.append(text(theme.title, PAGE_W / 2, 106, kind, size, "middle", 0, INK, pool=pool))

    if note:
        # sit the label on the frame's top edge, in a little white cut-out
        w = measure(note, "hand", 18, 2.5) + 30
        out.append(rect(PAGE_W / 2 - w / 2, FRAME[1] - 6, w, 21, 10.5,
                        'fill="#ffffff" stroke="none"'))
        out.append(text(note, PAGE_W / 2, FRAME[1] + 9.5, "hand", 18,
                        "middle", 2.5, INK, pool=pool))
    return "".join(out)


# ---------------------------------------------------------------- frame ----

def _scallop_path(x0, y0, x1, y1, bump=13.0):
    """Rounded cloud-ish border built from half circles."""
    d = []
    def run(ax, ay, bx, by):
        dist = math.hypot(bx - ax, by - ay)
        n = max(3, round(dist / (bump * 2)))
        step = dist / n
        ux, uy = (bx - ax) / dist, (by - ay) / dist
        for i in range(n):
            sx, sy = ax + ux * step * i, ay + uy * step * i
            ex, ey = ax + ux * step * (i + 1), ay + uy * step * (i + 1)
            d.append(f"A {step / 2:.2f} {step / 2:.2f} 0 0 1 {ex:.2f} {ey:.2f}")
        return
    d.append(f"M {x0:.2f} {y0:.2f}")
    run(x0, y0, x1, y0)
    run(x1, y0, x1, y1)
    run(x1, y1, x0, y1)
    run(x0, y1, x0, y0)
    d.append("Z")
    return " ".join(d)


def frame(theme: Theme, style: str, rng: random.Random, pool=None):
    """Returns (svg, obstacles) - obstacles keep doodles off the corner art."""
    x0, y0, x1, y1 = FRAME
    s = []
    obstacles = []
    if style == "classic":
        s.append(rect(x0, y0, x1 - x0, y1 - y0, 16,
                      f'fill="none" stroke="{INK}" stroke-width="2.6"'))
        s.append(rect(x0 + 7, y0 + 7, x1 - x0 - 14, y1 - y0 - 14, 11,
                      f'fill="none" stroke="{INK}" stroke-width="1.1"'))
    elif style == "scallop":
        s.append(path(_scallop_path(x0 + 13, y0 + 13, x1 - 13, y1 - 13, 12.0),
                      f'fill="none" stroke="{INK}" stroke-width="2.2"'))
        s.append(rect(x0 + 25, y0 + 25, x1 - x0 - 50, y1 - y0 - 50, 10,
                      f'fill="none" stroke="{INK}" stroke-width="1.0"'))
    else:  # dashed, with a doodle sitting on each corner
        s.append(rect(x0, y0, x1 - x0, y1 - y0, 18,
                      f'fill="none" stroke="{INK}" stroke-width="2.4" '
                      f'stroke-dasharray="9 7" stroke-linecap="round"'))
        picks = list(theme.icons)
        rng.shuffle(picks)
        for i, (cx, cy) in enumerate(
                [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]):
            s.append(f'<circle cx="{cx}" cy="{cy}" r="23" fill="#ffffff" '
                     f'stroke="none"/>')
            pick = picks[i % len(picks)]
            s.append(place(ICONS[pick](), cx, cy, 34, 0, 1.3, INK,
                           name=pick, pool=pool))
            obstacles.append((cx, cy, 30))
    return "".join(s), obstacles


def field_rect(style: str):
    x0, y0, x1, y1 = FRAME
    pad = FIELD_INSET + (14 if style == "scallop" else 0)
    return (x0 + pad, y0 + pad, x1 - pad, y1 - pad)


# --------------------------------------------------------------- legend ----

def legend(icons, counts, show_counts: bool, style: str, pool=None) -> str:
    n = len(icons)
    cols = 6 if n % 6 == 0 else 5
    rows = math.ceil(n / cols)
    left, right = 44.0, 568.0
    cell_w = (right - left) / cols
    top = LEGEND_TOP + (0 if rows == 3 else 8)

    out = [text("How many can you find?", PAGE_W / 2, top, "hand", 21,
                "middle", 1.5, INK, pool=pool)]
    for i, name in enumerate(icons):
        r, c = divmod(i, cols)
        cx = left + cell_w * c
        cy = top + 16 + r * ROW_H
        box = 27.0
        bx, by = cx + 5, cy
        if show_counts:
            out.append(rect(bx, by, box, box, 6,
                            f'fill="none" stroke="{INK}" stroke-width="1.3"'))
            out.append(text(str(counts[i]), bx + box / 2, by + box - 7.5,
                            "display", 16, "middle", 0, INK, pool=pool))
        else:
            out.append(rect(bx, by, box, box, 6,
                            f'fill="none" stroke="{INK}" stroke-width="1.3" '
                            f'stroke-dasharray="3.2 3"'))
        out.append(place(ICONS[name](), cx + 33 + box, cy + box / 2, 40, 0,
                         1.3, INK, name=name, pool=pool))
    return "".join(out)


def footer(extra: str = "", pool=None) -> str:
    bits = [config.STORE_LINE]
    if config.WEBSITE:
        bits.append(config.WEBSITE)
    if extra:
        bits.append(extra)
    return text("  ·  ".join(bits), PAGE_W / 2, FOOTER_Y, "hand-light",
                15, "middle", 0.8, "#444444", pool=pool)


# ----------------------------------------------------------------- pages ----

def puzzle_page(theme: Theme, variant: int, difficulty: str,
                style: str, answer_key: bool = False, compact: bool = False,
                pool=None, wrap: bool = True):
    """Build one puzzle (or its answer key). Returns (svg, counts).

    Pass a shared `pool` and `wrap=False` to get the bare page body, so several
    pages can live in one document behind a single set of <defs>.
    """
    seed = f"{theme.key}-{variant}"
    rng = random.Random(seed)
    cfg = config.DIFFICULTY[difficulty]

    owns_pool = pool is None
    pool = pool or (SymbolPool() if compact else None)
    frame_svg, obstacles = frame(theme, style, random.Random(seed + "-frame"),
                                 pool)
    counts = counts_for(len(theme.icons), cfg["total"], rng)
    items = [name for name, c in zip(theme.icons, counts) for _ in range(c)]
    placed = scatter(items, field_rect(style), rng, cfg["size"],
                     obstacles=obstacles, size_jitter=cfg["jitter"],
                     rot=cfg["rot"], flip=cfg["flip"], pack=cfg["pack"],
                     clusters=cfg["clusters"], decoy=cfg["decoy"])
    got = tally(placed)
    final = [got.get(name, 0) for name in theme.icons]

    body = [frame_svg]
    for name, x, y, size, rotation, flipped in placed:
        body.append(place(ICONS[name](), x, y, size, rotation, cfg["stroke"],
                          INK, name=name, pool=pool, flip=flipped))
    note = "ANSWER KEY" if answer_key else ""
    body.insert(0, header(theme, style, note, pool))
    body.append(legend(theme.icons, final, answer_key, style, pool))
    body.append(footer(f"Puzzle {variant + 1}"
                       + (" key" if answer_key else ""), pool))
    if not wrap:
        return "".join(body), final
    if pool is not None and owns_pool:
        body.insert(0, pool.defs())
    return svg_doc("".join(body)), final


def cover_page(theme: Theme, n_puzzles: int, compact: bool = False,
               pool=None, wrap: bool = True) -> str:
    rng = random.Random(theme.key + "-cover")
    owns_pool = pool is None
    pool = pool or (SymbolPool() if compact else None)
    body = []
    ew = measure("I SPY", "hand", 34, 7)
    body.append(text("I SPY", PAGE_W / 2, 104, "hand", 34, "middle", 7, INK, pool=pool))
    body.append(line(PAGE_W / 2 - ew / 2 - 52, 96, PAGE_W / 2 - ew / 2 - 16,
                     96, f'stroke="{INK}" stroke-width="1.8" '
                         f'stroke-linecap="round"'))
    body.append(line(PAGE_W / 2 + ew / 2 + 16, 96, PAGE_W / 2 + ew / 2 + 52,
                     96, f'stroke="{INK}" stroke-width="1.8" '
                         f'stroke-linecap="round"'))
    size = 64.0
    while measure(theme.title, "display", size, 0) > 486 and size > 24:
        size -= 2
    body.append(text(theme.title, PAGE_W / 2, 174, "display", size, "middle",
                     0, INK, pool=pool))
    body.append(text(theme.subtitle, PAGE_W / 2, 206, "hand-light", 23,
                     "middle", 1, INK, pool=pool))

    panel = (66.0, 234.0, 546.0, 610.0)
    body.append(rect(panel[0], panel[1], panel[2] - panel[0],
                     panel[3] - panel[1], 22,
                     f'fill="none" stroke="{INK}" stroke-width="2.6"'))
    body.append(rect(panel[0] + 8, panel[1] + 8, panel[2] - panel[0] - 16,
                     panel[3] - panel[1] - 16, 16,
                     f'fill="none" stroke="{INK}" stroke-width="1.0"'))
    picks = list(theme.icons)
    cols = 6 if len(picks) % 6 == 0 else 5
    rows = math.ceil(len(picks) / cols)
    cw = (panel[2] - panel[0]) / cols
    ch = (panel[3] - panel[1]) / rows
    for i, name in enumerate(picks):
        cx = panel[0] + cw * (i % cols) + cw / 2
        cy = panel[1] + ch * (i // cols) + ch / 2
        body.append(place(ICONS[name](), cx, cy, 58,
                          rng.uniform(-9, 9), 1.5, INK, name=name, pool=pool))

    body.append(text(f"{n_puzzles} printable puzzles  \u00b7  answer keys "
                     f"included", PAGE_W / 2, 648, "hand", 25, "middle", 1,
                     INK, pool=pool))
    body.append(text("Preschool \u00b7 Pre-K \u00b7 Kindergarten \u00b7 "
                     "Early finishers \u00b7 Sub tubs", PAGE_W / 2, 676,
                     "hand-light", 19, "middle", 1, INK, pool=pool))
    body.append(text(config.BRAND, PAGE_W / 2, 734, "display", 22, "middle",
                     0, INK, pool=pool))
    body.append(footer(pool=pool))
    if not wrap:
        return "".join(body)
    if pool is not None and owns_pool:
        body.insert(0, pool.defs())
    return svg_doc("".join(body))


TERMS_LINES = [
    ("You may:", True),
    ("Print and use these pages with your own students or children.", False),
    ("Use them in your classroom, co-op, therapy room or home.", False),
    ("Share a printed copy with a parent of a child you teach.", False),
    ("", False),
    ("Please do not:", True),
    ("Share the digital file or post it on a website or shared drive.", False),
    ("Resell, redistribute or claim the artwork as your own.", False),
    ("Use the pages to create another product for sale.", False),
    ("", False),
    ("Extra licences for teammates are available at a discount.", False),
    ("Thank you for respecting the work that went into this set!", False),
]


def terms_page(compact: bool = False, pool=None, wrap: bool = True) -> str:
    owns_pool = pool is None
    pool = pool or (SymbolPool() if compact else None)
    body = [text("TERMS OF USE", PAGE_W / 2, 120, "display", 38, "middle", 0,
                 INK, pool=pool)]
    body.append(text(config.BRAND, PAGE_W / 2, 150, "hand", 22, "middle", 2,
                     INK, pool=pool))
    body.append(rect(70, 180, 472, 420, 18,
                     f'fill="none" stroke="{INK}" stroke-width="2.2"'))
    y = 222.0
    for txt, bold in TERMS_LINES:
        if txt:
            body.append(text(txt, 100, y, "hand" if bold else "hand-light",
                             23 if bold else 20, "start", 0.6, INK, pool=pool))
        y += 30 if txt else 16
    body.append(text("Fonts: Fredoka One & Amatic SC (SIL Open Font Licence). "
                     "Artwork drawn for this set.", PAGE_W / 2, 640,
                     "hand-light", 15, "middle", 0.5, "#555555", pool=pool))
    body.append(footer(pool=pool))
    if not wrap:
        return "".join(body)
    if pool is not None and owns_pool:
        body.insert(0, pool.defs())
    return svg_doc("".join(body))
