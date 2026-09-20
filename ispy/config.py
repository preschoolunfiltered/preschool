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
DIFFICULTY = {
    "easy": {
        "total": 100, "size": 44.0, "stroke": 1.55,
        "jitter": (0.82, 1.18), "rot": 42.0, "flip": 0.22,
        "pack": 0.94, "clusters": 0,
    },
    "medium": {
        "total": 168, "size": 36.0, "stroke": 1.35,
        "jitter": (0.74, 1.26), "rot": 110.0, "flip": 0.38,
        "pack": 0.84, "clusters": 5,
    },
    "hard": {
        "total": 240, "size": 30.0, "stroke": 1.20,
        "jitter": (0.66, 1.34), "rot": 180.0, "flip": 0.5,
        "pack": 0.74, "clusters": 8,
    },
}

# Which difficulty each variant uses, cycled.
VARIANT_DIFFICULTY = ["easy", "medium", "hard"]

# Frame/header treatments, cycled per variant so every page looks different.
VARIANT_STYLE = ["classic", "scallop", "dashed"]
