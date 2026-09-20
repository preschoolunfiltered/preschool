# I Spy printables generator

A from-scratch generator for sellable **I Spy counting printables** — the kind
that sell on Teachers Pay Teachers. It draws every doodle as vector line art,
scatters them across a framed puzzle field, builds a matching answer key, and
exports true US Letter PDFs plus preview PNGs for your listing thumbnails.

Nothing here is traced from someone else's clipart: the 287 doodles are plain
SVG paths written in `ispy/icons/`, so the finished pages are yours to sell.
See [docs/TERMS-OF-USE.md](docs/TERMS-OF-USE.md) for the font licences.

Two product lines come out of the same 287 doodles: **I Spy counting
puzzles** and **coloring pages**.

## What gets built

```
output/
  I-Spy-Mega-Bundle.pdf              all 22 I Spy themes (176 pages)
  Coloring-Mega-Bundle.pdf           all 22 coloring themes (434 pages)
  themes/I-Spy-Spring/
    I-Spy-Spring.pdf                 cover + terms + 3 puzzles + 3 answer keys
    previews/                        150 dpi PNGs for TPT thumbnails
    _pages/                          the same pages as single-page PDFs
  coloring/Color-Spring/
    Color-Spring.pdf                 cover + terms + one page per picture
```

Every theme ships three puzzles at three difficulties — **easy** (128 items,
large art), **medium** (196) and **hard** (272) — so one file works for a whole
mixed-ability class. Difficulty is not just item count: each level also sets
how far a doodle may tilt (up to any angle), how often a copy is mirrored, how
much sizes vary, how tightly items nest into each other, how many clumps pull
them off an even grid, and how often a copy is parked beside a near-twin —
all in `DIFFICULTY` in `ispy/config.py`. Which doodles count as near-twins is
`ispy/lookalikes.py`. Each puzzle gets its own frame treatment (double line,
scalloped, dashed with corner doodles) so the set does not look repetitive.

**22 themes:** spring, summer, fall, winter, Christmas, Halloween,
Thanksgiving, Valentine's, Easter, St. Patrick's, ocean, space, farm,
dinosaurs, jungle, school, things that go, camping, birthday, bugs, pets and
food.

## Build it

```bash
pip install -r requirements.txt
python3 build.py                      # both lines (about 2 minutes)
python3 build.py --only coloring      # just the coloring pages
python3 build.py --themes spring ocean
python3 build.py --no-previews        # PDFs only, faster
```

### Coloring pages

One big picture per sheet, clip-art style: a two-line bubble-letter title
("COLOR THE BUNNY"), the subject drawn large with a heavy 5.4pt outline, and
flowers, butterflies and stars down both margins, inside a thin page border
whose bottom edge carries the credit line.

Every theme opens with its **hero** — a full-body character drawn for page
size in [`ispy/heroes.py`](ispy/heroes.py): a bunny riding a carrot, a squirrel
hugging an acorn, an owl in reading glasses, a crab in sunglasses with an ice
cream. A blown-up icon can't carry a page (a bunny there is a head, not a
character), so the heroes are drawn separately, on chibi proportions — head
bigger than the body, big solid eyes, a small smile, and as few interior lines
as the character can carry. Every extra line is another fiddly gap a
four-year-old has to color around.

`critter()` builds the standard body and every character is then just its ears,
its markings and the thing it holds, which is what makes twenty-two of them
read as one family. Props are drawn before the arms, so the mitts land on top
and the character reads as *holding* the thing rather than standing behind it. Then one page per picture in the theme, so a
set runs 16–19 pages — 456 in total.

Three things make a doodle work at page size:

- `outline()` turns the library's solid black accents — a ladybug's head, a
  bee's stripes, a jack-o'-lantern's face — into empty outlines, because a
  filled shape is a shape a child cannot color. Pupils are the exception:
  clip art keeps eyes solid, and an eye drawn as an empty ring looks
  startled.
- [`ispy/cute.py`](ispy/cute.py) adds a kawaii face to objects that don't have
  one. Only objects with an empty belly are listed; anything whose middle is
  already busy is left alone rather than given a face over its own detail.
- `fitted()` scales each subject by its measured ink bounds
  (`assets/icon_bounds.json`, rebuilt with `python3 tools/icon_bounds.py`)
  rather than its nominal box, so a rainbow and a pencil both fill the frame.

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

## Browse it in the browser

```bash
python3 tools/web_build.py     # writes web/index.html + one SVG per theme
```

This builds a self-contained viewer: a shelf of all 22 themes, then a page
rail for paging through every puzzle, answer key, cover and terms sheet.
Each theme exports as one tall SVG holding its eight pages behind a single
shared set of `<defs>`, so the doodle artwork is stored once per theme rather
than once per page — a dense sheet drops from ~300KB to ~80KB. The viewer's
markup lives in `web_src/index.template.html`; the build injects the manifest
into it, so edit the template, not `web/index.html`.

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
| `ispy/scatter.py` | Picks per-icon counts, then hides them: tilt, mirror, clump, nest |
| `ispy/lookalikes.py` | Shape families, so near-twins get parked together |
| `ispy/layout.py` | Header, frames, puzzle field, legend, cover, terms page |
| `ispy/coloring.py` | The coloring line: one subject per page, badge frames |
| `ispy/cute.py` | Kawaii faces for objects drawn at page size |
| `ispy/heroes.py` | 22 full-body characters, one per theme, and their greetings |
| `ispy/render.py` | SVG assembly and PDF/PNG export |
| `build.py` | Builds every theme, merges PDFs, writes previews |

Puzzle layouts are seeded from the theme name and variant, so a rebuild always
produces the identical page — and the answer key is tallied from what actually
landed on the page, not from the requested counts, so the numbers are always
right even when the field is crowded.
