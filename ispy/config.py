"""Product-wide settings you will actually want to edit.

Change BRAND / WEBSITE to your own store name before you publish, then
re-run `python3 build.py`. Everything else is safe to leave alone.
"""

BRAND = "Preschool Unfiltered"
WEBSITE = ""            # e.g. "www.yourstore.com" - blank hides the line
STORE_LINE = "© Preschool Unfiltered · For single-classroom use"

# How many puzzle variants (each with its own answer key) per theme.
VARIANTS_PER_THEME = 3

# How hard each level is to search.
#   total   - the sum of all the counts on a page
#   size    - the base size of a doodle in points
#   jitter  - how far a copy may stray from that size
#   rot     - maximum tilt in degrees (180 = any angle, upside down included)
#   flip    - chance a copy is mirrored
#   pack    - spacing factor; below 1 lets doodles nest into each other
#   clusters- clumps to pull items toward; 0 spreads them evenly, which is
#             the easiest possible page to scan
#   decoy   - chance of parking a copy beside a lookalike or another of its
#             own kind, which is what makes a child's count come out wrong
DIFFICULTY = {
    "easy": {
        "total": 128, "size": 40.0, "stroke": 1.45,
        "jitter": (0.78, 1.22), "rot": 90.0, "flip": 0.32,
        "pack": 0.88, "clusters": 3, "decoy": 0.28,
    },
    "medium": {
        "total": 196, "size": 33.0, "stroke": 1.30,
        "jitter": (0.70, 1.30), "rot": 180.0, "flip": 0.45,
        "pack": 0.79, "clusters": 6, "decoy": 0.40,
    },
    "hard": {
        "total": 272, "size": 28.0, "stroke": 1.15,
        "jitter": (0.62, 1.38), "rot": 180.0, "flip": 0.55,
        "pack": 0.70, "clusters": 9, "decoy": 0.52,
    },
}

# Which difficulty each variant uses, cycled.
VARIANT_DIFFICULTY = ["easy", "medium", "hard"]

# Frame/header treatments, cycled per variant so every page looks different.
VARIANT_STYLE = ["classic", "scallop", "dashed"]
