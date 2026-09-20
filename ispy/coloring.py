"""Coloring pages: one big picture per sheet, drawn like clip art.

A coloring page wants the opposite of an I Spy sheet. One subject, drawn as
large as the paper allows, with a heavy outline a crayon can chase, nothing
filled in solid black, a badge frame around it and its name spelled out in
hollow letters underneath. Objects pick up a kawaii face on the way in
(`ispy.cute`), because clip art for this age group smiles back.
"""

from __future__ import annotations

import json
import math
import os
import random
import re

from ispy import config
from ispy.cute import cutify
from ispy.draw import SOLID, circle, dot, heart, line, path, pt, rect, star
from ispy.icons import ICONS, label
from ispy.render import PAGE_H, PAGE_W, SymbolPool, place, svg_doc
from ispy.text import measure, text
from ispy.themes import Theme

INK = "#111111"

# chunky, because a preschooler colors up to the line, not inside it
STROKE_SUBJECT = 5.4   # the star of the page
STROKE_FILLER = 2.6    # the flowers and butterflies around it
STROKE_BORDER = 3.2
STROKE_TITLE = 4.4

BORDER = (28.0, 28.0, PAGE_W - 28.0, PAGE_H - 28.0)
SUBJECT_CX, SUBJECT_CY = PAGE_W / 2, 486.0
SUBJECT_FIT = 366.0

_BOUNDS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            "assets", "icon_bounds.json")
try:
    with open(_BOUNDS_PATH) as _fh:
        BOUNDS = json.load(_fh)
except OSError:  # not measured yet - fall back to the nominal box
    BOUNDS = {}


_SOLID_EL = re.compile(r'<(circle|ellipse|polygon|path)\b[^>]*?'
                       r'fill="#000" stroke="none"[^>]*?/>')


def outline(body: str) -> str:
    """Hollow out solid black shapes - but leave eyes alone.

    A filled shape is a shape a child cannot color, so the ladybug's head,
    the bee's stripes and the jack-o'-lantern's face all become outlines.
    Pupils are the exception: clip art keeps them solid, and an eye drawn as
    a small empty ring reads as a startled one.
    """
    def repl(m):
        el, tag = m.group(0), m.group(1)
        if tag == "circle":
            r = re.search(r'\br="([\d.]+)"', el)
            if r and float(r.group(1)) <= 6.0:
                return el
        elif tag == "ellipse":
            rx = re.search(r'\brx="([\d.]+)"', el)
            ry = re.search(r'\bry="([\d.]+)"', el)
            if rx and ry and max(float(rx.group(1)), float(ry.group(1))) <= 7.0:
                return el
        return el.replace(SOLID, 'fill="none"')
    return _SOLID_EL.sub(repl, body)


def art(name: str) -> str:
    """One subject, de-blackened and smiling."""
    return cutify(name, outline(ICONS[name]()))


def drop(name: str, x: float, y: float, size: float, rot: float = 0.0,
         stroke: float = STROKE_FILLER, pool=None, flip: bool = False) -> str:
    return place(art(name), x, y, size, rot, stroke, INK, name=name + "-c",
                 pool=pool, flip=flip)


def fitted(name: str, cx: float, cy: float, target: float, rot: float = 0.0,
           stroke: float = STROKE_SUBJECT, pool=None) -> str:
    """Draw `name` so its ink - not its nominal box - is `target` points wide.

    A flower pot covers half its box and a rainbow covers three quarters of
    the width and a third of the height. Scaling by the box would leave one
    subject swimming on the page and crop another, so scale by what the icon
    actually draws, and centre that rather than the box.
    """
    x0, y0, x1, y1 = BOUNDS.get(name, (0.0, 0.0, 100.0, 100.0))
    w, h = max(x1 - x0, 1.0), max(y1 - y0, 1.0)
    size = target * 100.0 / max(w, h)
    s = size / 100.0
    ink_cx, ink_cy = (x0 + x1) / 2, (y0 + y1) / 2
    return place(art(name), cx - (ink_cx - 50) * s, cy - (ink_cy - 50) * s,
                 size, rot, stroke, INK, name=name + "-c", pool=pool)


def hollow(s: str, x: float, y: float, size: float, weight: float,
           pool=None) -> str:
    """Outlined letters - a word the child can color in as well."""
    scale = size / 1000.0
    return text(s, x, y, "display", size, "middle", 0, "none",
                f'stroke="{INK}" stroke-width="{weight / scale:.0f}" '
                f'stroke-linejoin="round"', pool=pool)


def footer(note: str = "", pool=None) -> str:
    bits = [config.STORE_LINE]
    if note:
        bits.append(note)
    return text("  ·  ".join(bits), PAGE_W / 2, 772, "hand-light", 15,
                "middle", 0.8, "#444444", pool=pool)


# ----------------------------------------------------- border and fillers ---

def page_border(pool=None) -> str:
    """Thin rounded frame, with the credit line sitting in the bottom edge."""
    x0, y0, x1, y1 = BORDER
    out = [rect(x0, y0, x1 - x0, y1 - y0, 26,
                f'fill="none" stroke="{INK}" stroke-width="{STROKE_BORDER}" '
                f'stroke-linejoin="round"')]
    return "".join(out)


def credit(theme: Theme, pool=None) -> str:
    line_txt = f"{theme.title.title()}  \u00b7  {config.STORE_LINE}"
    w = measure(line_txt, "hand-light", 15, 0.8) + 26
    return (rect(PAGE_W / 2 - w / 2, BORDER[3] - 11, w, 22, 11,
                 'fill="#ffffff" stroke="none"')
            + text(line_txt, PAGE_W / 2, BORDER[3] + 5, "hand-light", 15,
                   "middle", 0.8, "#444444", pool=pool))


def bloom(cx: float, cy: float, r: float, petals: int, style: int) -> str:
    """A filler flower. Three petal shapes, the way a clip-art sheet varies them."""
    g = f'fill="none" stroke="{INK}" stroke-width="{STROKE_FILLER}" ' \
        f'stroke-linejoin="round" stroke-linecap="round"'
    out = []
    petals = min(petals, 6) if style != 1 else petals
    if style == 0:                                   # round petals
        for i in range(petals):
            a = 360 * i / petals
            px, py = pt(cx, cy, r * 0.62, a)
            out.append(circle(px, py, r * 0.40, g))
    elif style == 1:                                 # pointed daisy petals
        for i in range(petals):
            a = 360 * i / petals
            tipx, tipy = pt(cx, cy, r, a)
            lx, ly = pt(cx, cy, r * 0.34, a - 40)
            rx, ry = pt(cx, cy, r * 0.34, a + 40)
            out.append(path(f"M {lx:.1f} {ly:.1f} Q {tipx:.1f} {tipy:.1f} "
                            f"{rx:.1f} {ry:.1f}", g))
    else:                                            # long oval petals
        for i in range(petals):
            a = 360 * i / petals
            px, py = pt(cx, cy, r * 0.60, a)
            out.append(ellipse_petal(px, py, r * 0.46, r * 0.26, a, g))
    out.append(circle(cx, cy, r * 0.22, g))
    return "".join(out)


def ellipse_petal(cx, cy, rx, ry, rot, attrs) -> str:
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" '
            f'ry="{ry:.1f}" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})" '
            f'{attrs}/>')


# small things that read as decoration rather than as a second subject
FILLERS = ("butterfly", "bee", "ladybug", "star", "heart", "cloud",
           "snowflake", "bubbles", "leaf_sprig", "grass_tuft", "shamrock",
           "paw_print", "starfish", "seashell", "crescent_moon", "holly",
           "dragonfly", "moth", "raindrop", "acorn", "maple_leaf", "fern",
           "double_heart", "shooting_star", "bone", "confetti")


def filler_art(theme: Theme, name: str, x: float, y: float, size: float,
               rot: float, pool=None) -> str:
    return place(art(name), x, y, size, rot, STROKE_FILLER, INK,
                 name=name + "-c", pool=pool)


# ------------------------------------------------------------------ pages ---

BLOOM_THEMES = {"spring", "summer", "easter", "bugs", "farm", "jungle",
                "stpatrick", "fall", "valentine", "pets", "birthday"}


def _subject_guard(name: str, target: float):
    """The ellipse the main picture occupies, so fillers keep out of it."""
    x0, y0, x1, y1 = BOUNDS.get(name, (0.0, 0.0, 100.0, 100.0))
    w, h = max(x1 - x0, 1.0), max(y1 - y0, 1.0)
    s = target / max(w, h)
    return w * s / 2 + 16, h * s / 2 + 14


def decorations(theme: Theme, rng: random.Random, guard, pool=None) -> str:
    """Flowers, butterflies and sparkles filling the space around the picture."""
    picks = [n for n in theme.icons if n in FILLERS]
    kinds = [("icon", n) for n in picks] * 2
    if theme.key in BLOOM_THEMES or not picks:
        kinds += [("bloom", None)] * 6
    kinds += [("spark", None)] * 3
    rng.shuffle(kinds)

    gx, gy = guard
    x0, y0, x1, y1 = BORDER
    # fixed spots down both margins and along the bottom, the way a clip-art
    # sheet lines its flowers up - a ring around the subject leaves the
    # corners bare and crowds a wide picture
    slots = ((74, 298), (64, 416), (80, 540), (104, 656),
             (538, 298), (548, 416), (532, 540), (508, 656),
             (206, 690), (306, 268), (412, 690))
    placed, out = [], []
    for i, (sx, sy) in enumerate(slots):
        size = rng.uniform(52, 88)
        r = size * 0.5
        x = min(max(sx + rng.uniform(-14, 14), x0 + 20 + r), x1 - 20 - r)
        y = min(max(sy + rng.uniform(-14, 14), 244 + r), y1 - 26 - r)
        dx = (x - SUBJECT_CX) / (gx + r)
        dy = (y - SUBJECT_CY) / (gy + r)
        if dx * dx + dy * dy < 1.0:
            continue
        if any((x - px) ** 2 + (y - py) ** 2 < (0.92 * (r + pr)) ** 2
               for px, py, pr in placed):
            continue
        placed.append((x, y, r))
        kind, name = kinds[len(placed) % len(kinds)]
        rot = rng.uniform(-22, 22)
        if kind == "icon":
            out.append(filler_art(theme, name, x, y, size, rot, pool))
        elif kind == "bloom":
            out.append(bloom(x, y, r * 0.92, rng.choice((5, 6, 7)),
                             rng.randrange(3)))
        else:
            g = (f'fill="none" stroke="{INK}" stroke-width="{STROKE_FILLER}" '
                 f'stroke-linejoin="round"')
            if rng.random() < 0.5:
                out.append(star(x, y, r * 0.8, 5, 0.42, rot - 90, g))
            else:
                out.append(heart(x, y, r * 0.66, g))
    return "".join(out)


def subject_page(theme: Theme, name: str, index: int, pool=None) -> str:
    """One big picture, a bubble-letter title, decorations around the edges."""
    rng = random.Random(f"{theme.key}-{name}-{index}")
    word = label(name).upper()

    lead = 40.0
    big = 92.0
    while measure(word, "display", big, 0) > 432 and big > 30:
        big -= 2

    guard = _subject_guard(name, SUBJECT_FIT)
    body = [
        page_border(pool),
        hollow("COLOR THE", PAGE_W / 2, 128, lead, 3.4, pool),
        hollow(word, PAGE_W / 2, 214, big, STROKE_TITLE, pool),
        decorations(theme, rng, guard, pool),
        fitted(name, SUBJECT_CX, SUBJECT_CY, SUBJECT_FIT, rng.uniform(-3, 3),
               STROKE_SUBJECT, pool),
        credit(theme, pool),
    ]
    return "".join(body)


def pages_for(theme: Theme):
    """One coloring sheet per picture in the theme."""
    out = []
    for i, name in enumerate(theme.icons):
        out.append((
            "subject",
            label(name).title(),
            lambda p, name=name, i=i: subject_page(theme, name, i, p),
        ))
    return out


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
    body.append(hollow(theme.title, PAGE_W / 2, 174, size, 2.8, pool))
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
        body.append(fitted(name, x, y, 82, rng.uniform(-8, 8), 2.8, pool))

    body.append(text(f"{n_pages} coloring pages  ·  one big picture each",
                     PAGE_W / 2, 648, "hand", 25, "middle", 1, INK, pool=pool))
    body.append(text("Preschool · Pre-K · Kindergarten · "
                     "Fine motor · Calm corner", PAGE_W / 2, 676,
                     "hand-light", 19, "middle", 1, INK, pool=pool))
    body.append(text(config.BRAND, PAGE_W / 2, 734, "display", 22, "middle", 0,
                     INK, pool=pool))
    body.append(footer(pool=pool))
    return "".join(body)


def build_page(fn, compact: bool = False) -> str:
    pool = SymbolPool() if compact else None
    body = fn(pool)
    if pool is not None:
        body = pool.defs() + body
    return svg_doc(body)
