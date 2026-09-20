#!/usr/bin/env python3
"""Build every I Spy product: per-theme PDFs, answer keys and previews.

    python3 build.py                 # everything
    python3 build.py --themes spring ocean
    python3 build.py --no-previews   # PDFs only (fast)
    python3 build.py --bundle-only
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pypdf import PdfWriter

from ispy import coloring, config
from ispy.layout import cover_page, puzzle_page, terms_page
from ispy.render import write_pdf, write_png
from ispy.themes import THEMES, BY_KEY

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "output")


def slug(s: str) -> str:
    words = re.sub(r"[^A-Za-z0-9 ]+", "", s).split()
    return "-".join(w.capitalize() for w in words)


def merge(pdfs, dest):
    writer = PdfWriter()
    for p in pdfs:
        writer.append(p)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        writer.write(fh)
    return dest


def build_theme(theme, previews=True, dpi=150):
    name = f"I-Spy-{slug(theme.title)}"
    folder = os.path.join(OUT, "themes", name)
    work = os.path.join(folder, "_pages")
    prev = os.path.join(folder, "previews")
    os.makedirs(work, exist_ok=True)

    pages = []
    cover = cover_page(theme, config.VARIANTS_PER_THEME)
    pages.append(("00-cover", cover))
    pages.append(("01-terms", terms_page()))

    for v in range(config.VARIANTS_PER_THEME):
        difficulty = config.VARIANT_DIFFICULTY[v % len(config.VARIANT_DIFFICULTY)]
        style = config.VARIANT_STYLE[v % len(config.VARIANT_STYLE)]
        puzzle, counts = puzzle_page(theme, v, difficulty, style)
        key, _ = puzzle_page(theme, v, difficulty, style, answer_key=True)
        pages.append((f"{10 + v * 2:02d}-puzzle-{v + 1}-{difficulty}", puzzle))
        pages.append((f"{11 + v * 2:02d}-answer-key-{v + 1}", key))

    pdf_paths = []
    for stem, svg in pages:
        p = write_pdf(svg, os.path.join(work, f"{stem}.pdf"))
        pdf_paths.append(p)
        if previews and ("cover" in stem or stem.endswith("-easy")
                         or "answer-key-1" in stem):
            write_png(svg, os.path.join(prev, f"{stem}.png"), dpi=dpi)

    combined = merge(pdf_paths, os.path.join(folder, f"{name}.pdf"))
    return combined


def build_coloring(theme, previews=True, dpi=150):
    name = f"Color-{slug(theme.title)}"
    folder = os.path.join(OUT, "coloring", name)
    work = os.path.join(folder, "_pages")
    prev = os.path.join(folder, "previews")
    os.makedirs(work, exist_ok=True)

    sheets = coloring.pages_for(theme)
    pages = [("00-cover", coloring.build_page(
        lambda p: coloring.cover_page(theme, len(sheets), p))),
        ("01-terms", terms_page())]
    for i, (kind, label, fn) in enumerate(sheets):
        pages.append((f"{10 + i:02d}-{kind}-{i + 1}", coloring.build_page(fn)))

    pdf_paths = []
    for stem, svg in pages:
        pdf_paths.append(write_pdf(svg, os.path.join(work, f"{stem}.pdf")))
        if previews and stem in ("00-cover", "10-hero-1", "12-subject-3"):
            write_png(svg, os.path.join(prev, f"{stem}.png"), dpi=dpi)

    return merge(pdf_paths, os.path.join(folder, f"{name}.pdf"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--themes", nargs="*", default=None)
    ap.add_argument("--no-previews", action="store_true")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--bundle-only", action="store_true")
    ap.add_argument("--only", choices=["puzzles", "coloring", "all"],
                    default="all")
    args = ap.parse_args()

    themes = THEMES
    if args.themes:
        themes = [BY_KEY[k] for k in args.themes]

    built, colored = [], []
    for t in themes:
        if args.only in ("puzzles", "all"):
            path = build_theme(t, previews=not args.no_previews, dpi=args.dpi)
            built.append(path)
            print(f"  built {os.path.relpath(path, ROOT)}")
        if args.only in ("coloring", "all"):
            path = build_coloring(t, previews=not args.no_previews,
                                  dpi=args.dpi)
            colored.append(path)
            print(f"  built {os.path.relpath(path, ROOT)}")

    if not args.bundle_only:
        if len(built) > 1:
            bundle = merge(built, os.path.join(OUT, "I-Spy-Mega-Bundle.pdf"))
            print(f"  built {os.path.relpath(bundle, ROOT)}")
        if len(colored) > 1:
            bundle = merge(colored,
                           os.path.join(OUT, "Coloring-Mega-Bundle.pdf"))
            print(f"  built {os.path.relpath(bundle, ROOT)}")
    print(f"done - {len(themes)} theme(s)")


if __name__ == "__main__":
    main()
