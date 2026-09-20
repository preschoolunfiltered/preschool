"""SVG assembly plus PNG/PDF export."""

from __future__ import annotations

import os

import cairosvg

PAGE_W, PAGE_H = 612.0, 792.0  # US Letter in points


def svg_doc(body: str, w: float = PAGE_W, h: float = PAGE_H, bg: str = "#ffffff",
            units: str = "pt") -> str:
    """Wrap `body` in an SVG document.

    Sizes are declared in points so a letter page lands at exactly 8.5x11in
    in the PDF (cairosvg would otherwise read bare numbers as CSS pixels and
    shrink every page to 75%).
    """
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}{units}" '
        f'height="{h}{units}" viewBox="0 0 {w} {h}">'
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>'
        f"{body}</svg>"
    )


def place(
    body: str,
    x: float,
    y: float,
    size: float,
    rot: float = 0.0,
    stroke: float = 1.35,
    stroke_color: str = "#000000",
) -> str:
    """Drop a 100-unit icon centred at (x, y) at `size` points.

    Stroke width is divided by the scale so every icon on the page keeps the
    same optical line weight no matter how big or small it is drawn.
    """
    s = size / 100.0
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
