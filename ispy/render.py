"""SVG assembly plus PNG/PDF export."""

from __future__ import annotations

import os
import re

import cairosvg

PAGE_W, PAGE_H = 612.0, 792.0  # US Letter in points


def _safe_id(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "_", s)


def svg_doc(body: str, w: float = PAGE_W, h: float = PAGE_H, bg: str = "#ffffff",
            units: str = "pt") -> str:
    """Wrap `body` in an SVG document.

    Sizes are declared in points so a letter page lands at exactly 8.5x11in
    in the PDF (cairosvg would otherwise read bare numbers as CSS pixels and
    shrink every page to 75%).
    """
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}{units}" '
        f'height="{h}{units}" viewBox="0 0 {w} {h}">'
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>'
        f"{body}</svg>"
    )


class SymbolPool:
    """Collects artwork so a page can reference it instead of repeating it.

    A dense page draws the same 18 doodles 200-odd times and the same letters
    over and over. Inlined that is ~300KB of duplicated path data per page; as
    <use> references it is a fraction of that, which matters when the pages are
    served to a browser rather than flattened into a PDF.

    One pool is one page, and every icon in it is drawn in a single colour.
    """

    def __init__(self):
        self.items: dict[str, str] = {}

    def icon(self, name: str, body: str, color: str) -> str:
        key = "i-" + _safe_id(name)
        if key not in self.items:
            self.items[key] = (
                f'<g id="{key}" fill="none" stroke="{color}" '
                f'stroke-linecap="round" stroke-linejoin="round" '
                f'transform="translate(-50 -50)">{body}</g>'
            )
        return key

    def glyph(self, kind: str, name: str, d: str) -> str:
        key = f"g-{_safe_id(kind)}-{_safe_id(name)}"
        if key not in self.items:
            self.items[key] = f'<path id="{key}" d="{d}"/>'
        return key

    def defs(self) -> str:
        if not self.items:
            return ""
        return "<defs>" + "".join(self.items.values()) + "</defs>"


def place(
    body: str,
    x: float,
    y: float,
    size: float,
    rot: float = 0.0,
    stroke: float = 1.35,
    stroke_color: str = "#000000",
    name: str | None = None,
    pool: "SymbolPool | None" = None,
) -> str:
    """Drop a 100-unit icon centred at (x, y) at `size` points.

    Stroke width is divided by the scale so every icon on the page keeps the
    same optical line weight no matter how big or small it is drawn.
    """
    s = size / 100.0
    if pool is not None and name:
        ref = pool.icon(name, body, stroke_color)
        return (
            f'<use href="#{ref}" xlink:href="#{ref}" '
            f'transform="translate({x:.1f} {y:.1f}) rotate({rot:.1f}) '
            f'scale({s:.3f})" stroke-width="{stroke / s:.2f}"/>'
        )
    return (
        f'<g transform="translate({x:.2f} {y:.2f}) rotate({rot:.2f}) '
        f'scale({s:.4f}) translate(-50 -50)" fill="none" stroke="{stroke_color}" '
        f'stroke-width="{stroke / s:.2f}" stroke-linecap="round" '
        f'stroke-linejoin="round">{body}</g>'
    )


def write_png(svg: str, path: str, dpi: int = 150) -> str:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=path, dpi=dpi,
                     background_color="#ffffff")
    return path


def write_pdf(svg: str, path: str) -> str:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=path)
    return path
