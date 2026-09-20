#!/usr/bin/env python3
"""Generate ready-to-paste TPT listing copy from the theme definitions.

    python3 tools/listing_copy.py > docs/TPT-LISTING-COPY.md
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ispy import config
from ispy.icons import label
from ispy.themes import THEMES

GRADES = "PreK, Kindergarten, 1st grade"
BASE_TAGS = ["i spy", "count and write", "counting to 20", "visual discrimination",
             "morning work", "early finishers", "sub plans", "no prep printables"]

SEASONAL = {
    "spring": "spring, april, may, earth day",
    "summer": "summer, beach, end of year, summer school",
    "fall": "fall, autumn, september, october",
    "winter": "winter, january, snow day",
    "christmas": "christmas, december, holidays",
    "halloween": "halloween, october, not scary",
    "thanksgiving": "thanksgiving, november, turkey",
    "valentine": "valentines day, february, hearts",
    "easter": "easter, spring, april",
    "stpatrick": "st patricks day, march, shamrock",
}

COLORING_LONG = """**What you get**

- {n} coloring pages, each on its own full-page US Letter sheet (8.5 x 11 in)
- One big picture per page, drawn clip-art style with a heavy outline, so
  even the youngest hands have somewhere easy to start
- A bubble-letter title the children color in as well - COLOR THE BUNNY -
  so the page builds vocabulary and print awareness while it is worked on
- Flowers, butterflies and stars down the margins, so there is plenty to
  do once the main picture is finished
- Chunky outlines with nothing filled in solid black, so every single shape
  can take a crayon - including the letters of the word
- Black-and-white line art, no colour ink needed to print
- A printable terms-of-use page

**How to use it**

Morning tubs, calm corners, early finishers, fine-motor practice, sub tubs,
indoor recess, or a quiet-time folder that goes home. Laminate them and they
work with dry-erase markers again and again.

**Pictures in this set**

{icons}

**Skills**

Pencil grip and crayon control, staying inside the line, color recognition,
focus and stamina, vocabulary building.

**Format**

PDF, {pages} pages, US Letter, print-and-go. No prep and nothing to assemble."""

LONG = """**What you get**

- {n} I Spy puzzles, each on its own full-page US Letter sheet (8.5 x 11 in)
- A matching answer key for every puzzle
- Three levels in one set: easy, medium and challenging, so one file covers
  a whole mixed-ability class
- Black-and-white line art - prints clean on any printer, no colour ink needed
- A printable terms-of-use page

**How to use it**

Children hunt for each picture in the border box, count how many they find and
write the number in the box beside it. Great for maths centres, morning tubs,
early finishers, sub plans, fine-motor and one-to-one correspondence practice,
or for laminating and using with dry-erase markers again and again.

**Pictures in this set**

{icons}

**Skills**

Counting and cardinality, one-to-one correspondence, number writing, visual
discrimination, focus and attention to detail, vocabulary building.

**Format**

PDF, {pages} pages, US Letter, print-and-go. No prep and nothing to assemble."""


def pretty(title: str) -> str:
    return title.title().replace("'S", "'s")


def block(theme):
    n = config.VARIANTS_PER_THEME
    pages = 2 + n * 2
    icons = ", ".join(label(i) for i in theme.icons)
    title_word = pretty(theme.title)
    tags = BASE_TAGS + [t.strip() for t in
                        SEASONAL.get(theme.key, theme.key).split(",")]
    out = [
        f"## {title_word}",
        "",
        "**Product title**  ",
        f"I Spy {title_word} Count and Write Worksheets | {n} Puzzles + "
        f"Answer Keys",
        "",
        "**Short blurb**  ",
        f"{theme.subtitle} - {n} no-prep I Spy counting puzzles with answer "
        f"keys for PreK and Kindergarten.",
        "",
        "**Description**",
        "",
        LONG.format(n=n, icons=icons, pages=pages),
        "",
        f"**Grades**: {GRADES}  ",
        f"**Suggested price**: $3.50 (single theme)  ",
        f"**Tags**: {', '.join(tags)}",
        "",
        "---",
        "",
    ]
    return "\n".join(out)


def coloring_block(theme):
    n = len(theme.icons)
    pages = 2 + n
    icons = ", ".join(label(i) for i in theme.icons)
    title_word = pretty(theme.title)
    tags = ["coloring pages", "coloring sheets", "fine motor", "morning tubs",
            "calm corner", "early finishers", "sub plans", "no prep"]
    tags += [t.strip() for t in SEASONAL.get(theme.key, theme.key).split(",")]
    return "\n".join([
        f"## {title_word} (coloring)",
        "",
        "**Product title**  ",
        f"{title_word} Coloring Pages | {n} No-Prep Sheets for Preschool "
        f"and Pre-K",
        "",
        "**Short blurb**  ",
        f"{n} chunky-line {title_word.lower()} coloring pages - one big "
        f"picture per sheet, print and go.",
        "",
        "**Description**",
        "",
        COLORING_LONG.format(n=n, icons=icons, pages=pages),
        "",
        f"**Grades**: {GRADES}  ",
        f"**Suggested price**: $3.00 (single theme)  ",
        f"**Tags**: {', '.join(tags)}",
        "",
        "---",
        "",
    ])


def main():
    n = config.VARIANTS_PER_THEME
    total_pages = len(THEMES) * (2 + n * 2)
    print("# TPT listing copy")
    print()
    print("Generated by `python3 tools/listing_copy.py`. Edit the wording to "
          "sound like you before you publish - copy that reads like a person "
          "converts better than copy that reads like a template.")
    print()
    print("## Bundle")
    print()
    print("**Product title**  ")
    print(f"I Spy MEGA Bundle | {len(THEMES)} Themes, "
          f"{len(THEMES) * n} Counting Puzzles + Answer Keys")
    print()
    print("**Short blurb**  ")
    print(f"A full year of I Spy counting printables - {len(THEMES)} themed "
          f"sets, {len(THEMES) * n} puzzles, every answer key included.")
    print()
    print("**Description**")
    print()
    print(f"""Every I Spy set in the store in one download: {len(THEMES)}
themes covering the whole school year, {len(THEMES) * n} puzzles in total,
each with its own answer key. Three difficulty levels in every theme so the
same file works for your youngest counters and your early finishers.

Themes included: """ + ", ".join(pretty(t.title) for t in THEMES) + f""".

Black-and-white, print-and-go, US Letter. {total_pages} pages.""")
    print()
    print("**Suggested price**: $18.00 (bundle) - roughly half the price of "
          "buying the sets separately.")
    print()
    print("---")
    print()
    print("# Single themes")
    print()
    for t in THEMES:
        print(block(t))

    cn = sum(len(t.icons) for t in THEMES)
    print("# Coloring pages")
    print()
    print("**Bundle title**  ")
    print(f"Coloring Pages MEGA Bundle | {len(THEMES)} Themes, {cn} Pages")
    print()
    print(f"""A year of coloring in one download: {len(THEMES)} themes and
{cn} pages, each one a single big picture with its name spelled out
underneath in hollow letters. Chunky outlines throughout, nothing filled in
solid black, so every shape - and every letter - can be colored.""")
    print()
    print("**Suggested price**: $15.00 (bundle)")
    print()
    print("---")
    print()
    for t in THEMES:
        print(coloring_block(t))


if __name__ == "__main__":
    main()
