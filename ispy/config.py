"""Product-wide settings you will actually want to edit.

Change BRAND / WEBSITE to your own store name before you publish, then
re-run `python3 build.py`. Everything else is safe to leave alone.
"""

BRAND = "Preschool Unfiltered"
WEBSITE = ""            # e.g. "www.yourstore.com" - blank hides the line
STORE_LINE = "© Preschool Unfiltered · For single-classroom use"

# How many puzzle variants (each with its own answer key) per theme.
VARIANTS_PER_THEME = 3

# Item totals per difficulty - the sum of all the counts on a page.
DIFFICULTY = {
    "easy":   {"total": 92,  "size": 46.0, "stroke": 1.60},
    "medium": {"total": 150, "size": 38.0, "stroke": 1.40},
    "hard":   {"total": 215, "size": 31.0, "stroke": 1.25},
}

# Which difficulty each variant uses, cycled.
VARIANT_DIFFICULTY = ["easy", "medium", "hard"]

# Frame/header treatments, cycled per variant so every page looks different.
VARIANT_STYLE = ["classic", "scallop", "dashed"]
