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

from ispy import config
from ispy.cute import cutify
from ispy.draw import SOLID, circle, dot, heart, line, path, pt, rect, star
from ispy.icons import ICONS, label
from ispy.render import PAGE_H, PAGE_W, SymbolPool, place, svg_doc
from ispy.text import measure, text
from ispy.themes import Theme

INK = "#111111"

# chunky, because a preschooler colors up to the line, not inside it
STROKE_SUBJECT = 4.6
STROKE_FRAME = 3.0
STROKE_SMALL = 2.4
STROKE_TITLE = 3.2

FRAME_CX, FRAME_CY, FRAME_R = PAGE_W / 2, 364.0, 208.0
SUBJECT_FIT = 286.0        # inside a circle frame
SUBJECT_FIT_PANEL = 322.0  # inside the square one

_BOUNDS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            "assets", "icon_bounds.json")
try:
    with open(_BOUNDS_PATH) as _fh:
        BOUNDS = json.load(_fh)
except OSError:  # not measured yet - fall back to the nominal box
    BOUNDS = {}


def outline(body: str) -> str:
    """Solid black accents become outlines, so every shape can be colored."""
    return body.replace(SOLID, 'fill="none"')


def art(name: str) -> str:
    """One subject, de-blackened and smiling."""
    return cutify(name, outline(ICONS[name]()))


def drop(name: str, x: float, y: float, size: float, rot: float = 0.0,
         stroke: float = STROKE_SMALL, pool=None, flip: bool = False) -> str:
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


# ----------------------------------------------------------------- frames ---

def scallop_circle(cx: float, cy: float, r: float, bumps: int = 20) -> str:
    """A circle of little humps - the classic clip-art badge edge."""
    pts = [pt(cx, cy, r, 360 * i / bumps) for i in range(bumps)]
    chord = math.hypot(pts[1][0] - pts[0][0], pts[1][1] - pts[0][1]) / 2
    d = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for i in range(1, bumps + 1):
        x, y = pts[i % bumps]
        d.append(f"A {chord:.1f} {chord:.1f} 0 0 1 {x:.1f} {y:.1f}")
    d.append("Z")
    return path(" ".join(d), f'fill="none" stroke="{INK}" '
                             f'stroke-width="{STROKE_FRAME}" '
                             f'stroke-linejoin="round"')


def cloud_circle(cx: float, cy: float, r: float, bumps: int = 11) -> str:
    pts = [pt(cx, cy, r, 360 * i / bumps) for i in range(bumps)]
    chord = math.hypot(pts[1][0] - pts[0][0], pts[1][1] - pts[0][1]) / 2
    d = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for i in range(1, bumps + 1):
        x, y = pts[i % bumps]
        d.append(f"A {chord:.1f} {chord:.1f} 0 0 1 {x:.1f} {y:.1f}")
    d.append("Z")
    return path(" ".join(d), f'fill="none" stroke="{INK}" '
                             f'stroke-width="{STROKE_FRAME}" '
                             f'stroke-linejoin="round"')


def dashed_panel(cx: float, cy: float, r: float) -> str:
    return (rect(cx - r, cy - r * 1.02, r * 2, r * 2.04, 34,
                 f'fill="none" stroke="{INK}" stroke-width="{STROKE_FRAME}"')
            + rect(cx - r + 13, cy - r * 1.02 + 13, r * 2 - 26, r * 2.04 - 26,
                   26, f'fill="none" stroke="{INK}" stroke-width="1.6" '
                       f'stroke-dasharray="10 9" stroke-linecap="round"'))


FRAMES = (scallop_circle, cloud_circle,
          lambda cx, cy, r: dashed_panel(cx, cy, r))


SPARKLE_SPOTS = ((70, 192), (542, 192), (68, 366), (544, 366),
                 (70, 540), (542, 540))


def confetti(rng: random.Random, cx: float, cy: float, r: float) -> str:
    """Sparkles in the corners the badge leaves empty."""
    out = []
    for i, (x, y) in enumerate(SPARKLE_SPOTS):
        pick = i % 3
        size = rng.uniform(13, 19)
        if pick == 0:
            out.append(star(x, y, size, 5, 0.42, rng.uniform(-30, 30),
                            f'fill="none" stroke="{INK}" '
                            f'stroke-width="{STROKE_SMALL}" '
                            f'stroke-linejoin="round"'))
        elif pick == 1:
            out.append(heart(x, y, size * 0.8,
                             f'fill="none" stroke="{INK}" '
                             f'stroke-width="{STROKE_SMALL}" '
                             f'stroke-linejoin="round"'))
        else:
            out.append(circle(x, y, size * 0.4,
                              f'fill="none" stroke="{INK}" '
                              f'stroke-width="{STROKE_SMALL}"'))
    return "".join(out)


# ------------------------------------------------------------------ pages ---

def subject_page(theme: Theme, name: str, index: int, pool=None) -> str:
    """One picture, one name, one page."""
    rng = random.Random(f"{theme.key}-{name}-{index}")
    word = label(name).upper()

    body = [
        text(theme.title, PAGE_W / 2, 74, "hand", 26, "middle", 6, INK,
             pool=pool),
        FRAMES[index % len(FRAMES)](FRAME_CX, FRAME_CY, FRAME_R),
        confetti(rng, FRAME_CX, FRAME_CY, FRAME_R),
        fitted(name, FRAME_CX, FRAME_CY,
               SUBJECT_FIT_PANEL if index % len(FRAMES) == 2 else SUBJECT_FIT,
               rng.uniform(-3, 3), STROKE_SUBJECT, pool),
    ]

    size = 76.0
    while measure(word, "display", size, 0) > 470 and size > 26:
        size -= 2
    body.append(hollow(word, PAGE_W / 2, 700, size, STROKE_TITLE, pool))
    body.append(text("Color me in!", PAGE_W / 2, 732, "hand", 22, "middle",
                     1.5, INK, pool=pool))
    body.append(footer(f"Page {index + 1}", pool))
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
        body.append(fitted(name, x, y, 82, rng.uniform(-8, 8), STROKE_FRAME,
                           pool))

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
