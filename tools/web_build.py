#!/usr/bin/env python3
"""Export one stacked SVG per theme, for the web viewer.

    python3 tools/web_build.py [outdir]

Each file holds all eight pages of a theme end to end in a single tall
document (612 x 6336pt) behind one shared set of <defs>. The viewer shows a
page by cropping to its slice, so a theme is one request instead of eight, and
the doodle artwork is stored once per theme instead of once per page.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ispy import coloring, config
from ispy.config import DIFFICULTY
from ispy.icons import label
from ispy.layout import cover_page, puzzle_page, terms_page
from ispy.render import PAGE_H, PAGE_W, SymbolPool, svg_doc
from ispy.themes import THEMES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pretty(title: str) -> str:
    """SPRING -> Spring, ST. PATRICK'S -> St. Patrick's (sheets shout, UI does not)."""
    return title.title().replace("'S", "'s")


def theme_document(theme):
    """Returns (svg, page descriptors) for one theme."""
    pool = SymbolPool()
    bodies, pages = [], []

    def add(kind, title, body, **extra):
        pages.append(dict(kind=kind, label=title, **extra))
        bodies.append(body)

    add("cover", "Cover",
        cover_page(theme, config.VARIANTS_PER_THEME, pool=pool, wrap=False))
    for v in range(config.VARIANTS_PER_THEME):
        difficulty = config.VARIANT_DIFFICULTY[v % len(config.VARIANT_DIFFICULTY)]
        style = config.VARIANT_STYLE[v % len(config.VARIANT_STYLE)]
        puzzle, counts = puzzle_page(theme, v, difficulty, style, pool=pool,
                                     wrap=False)
        key, _ = puzzle_page(theme, v, difficulty, style, answer_key=True,
                             pool=pool, wrap=False)
        d = DIFFICULTY[difficulty]
        hiding = (f"any angle to {round(d['rot'])}\u00b0, "
                  f"{round(d['flip'] * 100)}% mirrored, "
                  f"{round(d['decoy'] * 100)}% beside a lookalike")
        add("puzzle", f"Puzzle {v + 1}", puzzle, difficulty=difficulty,
            items=sum(counts), frame=style, hiding=hiding)
        add("key", f"Key {v + 1}", key, difficulty=difficulty)
    add("terms", "Terms", terms_page(pool=pool, wrap=False))

    stacked = "".join(
        f'<g transform="translate(0 {i * PAGE_H:.0f})">{b}</g>'
        for i, b in enumerate(bodies)
    )
    svg = svg_doc(pool.defs() + stacked, PAGE_W, PAGE_H * len(bodies))
    return svg, pages


def coloring_document(theme):
    """Same stacking trick for the coloring set."""
    pool = SymbolPool()
    bodies, pages = [], []
    sheets = coloring.pages_for(theme)
    bodies.append(coloring.cover_page(theme, len(sheets), pool))
    pages.append({"kind": "cover", "label": "Cover"})
    for kind, label, fn in sheets:
        bodies.append(fn(pool))
        pages.append({"kind": kind, "label": label})
    bodies.append(terms_page(pool=pool, wrap=False))
    pages.append({"kind": "terms", "label": "Terms"})

    stacked = "".join(
        f'<g transform="translate(0 {i * PAGE_H:.0f})">{b}</g>'
        for i, b in enumerate(bodies)
    )
    return svg_doc(pool.defs() + stacked, PAGE_W, PAGE_H * len(bodies)), pages


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "web")
    os.makedirs(os.path.join(out, "themes"), exist_ok=True)
    os.makedirs(os.path.join(out, "covers"), exist_ok=True)
    os.makedirs(os.path.join(out, "color"), exist_ok=True)
    os.makedirs(os.path.join(out, "color-covers"), exist_ok=True)
    ispy_themes, color_themes = [], []
    manifest = {
        "brand": config.BRAND, "pageWidth": PAGE_W, "pageHeight": PAGE_H,
        "collections": [
            {"id": "ispy", "label": "I Spy puzzles", "themes": ispy_themes,
             "note": "Each theme holds three puzzles at three densities - 128,"
                     " 196 and 272 things to find - plus a matching answer key"
                     " for each one. Pictures are tilted to any angle,"
                     " mirrored, drawn at different sizes and clumped"
                     " together, and near-twins are parked side by side on"
                     " purpose."},
            {"id": "color", "label": "Coloring pages", "themes": color_themes,
             "note": "One big picture per sheet, clip-art style: a bubble"
                     " -letter title, a smiling subject drawn heavy enough for"
                     " a crayon to chase, and flowers, butterflies and stars"
                     " down the margins. Every theme opens with its own"
                     " full-body character - a bunny on a carrot, a squirrel"
                     " with an acorn, an owl in glasses."},
        ],
    }
    total = 0
    for theme in THEMES:
        svg, pages = theme_document(theme)
        path = os.path.join(out, "themes", f"{theme.key}.svg")
        with open(path, "w") as fh:
            fh.write(svg)
        total += os.path.getsize(path)
        cover = os.path.join(out, "covers", f"{theme.key}.svg")
        with open(cover, "w") as fh:  # shelf thumbnails, so a card is ~70KB
            fh.write(cover_page(theme, config.VARIANTS_PER_THEME, compact=True))
        csvg, cpages = coloring_document(theme)
        cpath = os.path.join(out, "color", f"{theme.key}.svg")
        with open(cpath, "w") as fh:
            fh.write(csvg)
        total += os.path.getsize(cpath)
        ccover = os.path.join(out, "color-covers", f"{theme.key}.svg")
        with open(ccover, "w") as fh:
            fh.write(coloring.build_page(
                lambda p: coloring.cover_page(theme, len(cpages) - 2, p),
                compact=True))
        total += os.path.getsize(ccover)
        color_themes.append({
            "key": theme.key,
            "name": pretty(theme.title),
            "cover": f"color-covers/{theme.key}.svg",
            "subtitle": theme.subtitle,
            "icons": [label(i) for i in theme.icons],
            "file": f"color/{theme.key}.svg",
            "pages": cpages,
        })
        ispy_themes.append({
            "key": theme.key,
            "name": pretty(theme.title),
            "cover": f"covers/{theme.key}.svg",
            "title": theme.title,
            "subtitle": theme.subtitle,
            "icons": [label(i) for i in theme.icons],
            "file": f"themes/{theme.key}.svg",
            "pages": pages,
        })
    blob = json.dumps(manifest, separators=(",", ":"))
    with open(os.path.join(out, "manifest.json"), "w") as fh:
        fh.write(blob)

    template = os.path.join(ROOT, "web_src", "index.template.html")
    if os.path.exists(template):
        page = open(template).read().replace("/*__MANIFEST__*/null", blob)
        with open(os.path.join(out, "index.html"), "w") as fh:
            fh.write(page)
        print(f"index.html {len(page) / 1024:.0f} KB")
    print(f"{len(THEMES)} theme files, {total / 1_048_576:.1f} MB total, "
          f"largest {max(os.path.getsize(os.path.join(out, 'themes', t.key + '.svg')) for t in THEMES) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
