# I Spy printables generator

A from-scratch generator for sellable **I Spy counting printables** — the kind
that sell on Teachers Pay Teachers. It draws every doodle as vector line art,
scatters them across a framed puzzle field, builds a matching answer key, and
exports true US Letter PDFs plus preview PNGs for your listing thumbnails.

Nothing here is traced from someone else's clipart: the 287 doodles are plain
SVG paths written in `ispy/icons/`, so the finished pages are yours to sell.
See [docs/TERMS-OF-USE.md](docs/TERMS-OF-USE.md) for the font licences.

## What gets built

```
output/
  I-Spy-Mega-Bundle.pdf              all 22 themes in one file (176 pages)
  themes/I-Spy-Spring/
    I-Spy-Spring.pdf                 cover + terms + 3 puzzles + 3 answer keys
    previews/                        150 dpi PNGs for TPT thumbnails
    _pages/                          the same pages as single-page PDFs
```

Every theme ships three puzzles at three difficulties — **easy** (92 items,
large art), **medium** (150) and **hard** (215) — so one file works for a whole
mixed-ability class. Each puzzle gets its own frame treatment (double line,
scalloped, dashed with corner doodles) so the set does not look repetitive.

**22 themes:** spring, summer, fall, winter, Christmas, Halloween,
Thanksgiving, Valentine's, Easter, St. Patrick's, ocean, space, farm,
dinosaurs, jungle, school, things that go, camping, birthday, bugs, pets and
food.

## Build it

```bash
pip install -r requirements.txt
python3 build.py                      # everything (about 75 seconds)
python3 build.py --themes spring ocean
python3 build.py --no-previews        # PDFs only, faster
```

## Make it yours

1. **Put your store name on it.** Edit `BRAND`, `WEBSITE` and `STORE_LINE` in
   [`ispy/config.py`](ispy/config.py), then rebuild. That name appears on every
   cover, footer and terms page.
2. **Change the difficulty mix** — `DIFFICULTY` and `VARIANT_DIFFICULTY` in the
   same file control how many items land on a page and how big they are.
   `VARIANTS_PER_THEME` controls how many puzzles each theme gets.
3. **Add a theme** — append a `_t(...)` entry in
   [`ispy/themes.py`](ispy/themes.py) listing 15 or 18 icon names. Any name
   registered in `ispy/icons/` works, so most new themes are just a new mix of
   existing doodles.
4. **Draw a new doodle** — add a function to a pack in `ispy/icons/` decorated
   with `@icon("name")`, drawn inside a 100×100 box using the helpers in
   `ispy/draw.py` (`circle`, `blob`, `tube`, `petal_flower`, `star`, …).
   Check it with:

   ```bash
   python3 tools/contact_sheet.py all /tmp/contact.png   # or a,b,c for a subset
   ```

## Selling it

`python3 tools/listing_copy.py > docs/TPT-LISTING-COPY.md` regenerates
[ready-to-paste listing copy](docs/TPT-LISTING-COPY.md) — product titles, blurbs,
descriptions, tags and suggested prices for each theme and for the bundle.
Reword it in your own voice before you publish.

For listing images, use `previews/00-cover.png` as the main thumbnail and the
puzzle and answer-key previews as supporting images.

## How it works

| File | Does |
| --- | --- |
| `ispy/draw.py` | SVG primitives — arcs, blobs, tubes, petals, kawaii faces |
| `ispy/icons/` | 287 doodles, grouped into themed packs |
| `ispy/text.py` | Renders text as vector outlines via fontTools |
| `ispy/scatter.py` | Picks per-icon counts, dart-throws them without crowding |
| `ispy/layout.py` | Header, frames, puzzle field, legend, cover, terms page |
| `ispy/render.py` | SVG assembly and PDF/PNG export |
| `build.py` | Builds every theme, merges PDFs, writes previews |

Puzzle layouts are seeded from the theme name and variant, so a rebuild always
produces the identical page — and the answer key is tallied from what actually
landed on the page, not from the requested counts, so the numbers are always
right even when the field is crowded.
