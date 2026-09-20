"""Text rendered as vector outlines.

Titles and numbers are converted to SVG paths with fontTools so a page looks
identical on any machine and the exported PDF carries no embedded font
(the bundled faces are OFL, but shipping outlines keeps the PDFs simple).
"""

from __future__ import annotations

import functools
import os

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.misc.transform import Transform

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "fonts")

FONTS = {
    "display": "FredokaOne-Regular.ttf",   # titles, big numbers
    "hand": "AmaticSC-Bold.ttf",           # "I SPY" eyebrow, playful labels
    "hand-light": "AmaticSC-Regular.ttf",  # footers, fine print
}


@functools.lru_cache(maxsize=8)
def _font(kind: str):
    return TTFont(os.path.join(FONT_DIR, FONTS[kind]), lazy=True)


@functools.lru_cache(maxsize=8)
def _metrics(kind: str):
    f = _font(kind)
    return f["head"].unitsPerEm, f.getBestCmap(), f.getGlyphSet(), f["hmtx"].metrics


def measure(s: str, kind="display", size=24.0, tracking=0.0) -> float:
    upem, cmap, _, hmtx = _metrics(kind)
    total = 0.0
    for ch in s:
        gn = cmap.get(ord(ch))
        if gn is None:
            total += upem * 0.32
            continue
        total += hmtx[gn][0]
    return total * size / upem + tracking * max(len(s) - 1, 0)


def text(
    s: str,
    x: float,
    y: float,
    kind: str = "display",
    size: float = 24.0,
    anchor: str = "start",
    tracking: float = 0.0,
    fill: str = "#000",
    extra: str = "",
    pool=None,
) -> str:
    """Return <path> outlines for `s`, baseline at y, aligned by `anchor`."""
    upem, cmap, gs, hmtx = _metrics(kind)
    scale = size / upem
    width = measure(s, kind, size, tracking)
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    pen_x = 0.0
    parts = []
    for ch in s:
        gn = cmap.get(ord(ch))
        if gn is None:
            pen_x += upem * 0.32 + tracking / scale
            continue
        if pool is not None:
            # glyph outlines live once in <defs>; repeated letters cost ~40 bytes
            spen = SVGPathPen(gs, ntos=lambda v: str(round(v)))
            tpen = TransformPen(spen, Transform(1, 0, 0, -1, 0, 0))
            gs[gn].draw(tpen)
            d = spen.getCommands()
            if d:
                ref = pool.glyph(kind, gn, d)
                parts.append(f'<use href="#{ref}" xlink:href="#{ref}" '
                             f'x="{pen_x:.0f}"/>')
        else:
            spen = SVGPathPen(gs)
            tpen = TransformPen(spen, Transform(1, 0, 0, -1, pen_x, 0))
            gs[gn].draw(tpen)
            d = spen.getCommands()
            if d:
                parts.append(f'<path d="{d}"/>')
        pen_x += hmtx[gn][0] + tracking / scale
    if not parts:
        return ""
    body = "".join(parts)
    return (
        f'<g transform="translate({x:.2f} {y:.2f}) scale({scale:.5f})" '
        f'fill="{fill}" stroke="none"{(" " + extra) if extra else ""}>{body}</g>'
    )
