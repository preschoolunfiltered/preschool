"""Kawaii faces for objects that are about to be drawn page-sized.

The doodle library gives animals faces already. Objects don't have one, which
is fine at 30pt on an I Spy sheet but reads as plain at 300pt on a coloring
page - clip art for this age group smiles back. Each entry below is where a
face sits inside the icon's 100x100 box: (centre x, eye line y, eye spacing).

Only objects with a clear, empty belly are listed. Anything whose middle is
already busy - a book's spine, a bus window, a lollipop's spiral - is left
alone rather than given a face over the top of its own detail.
"""

from __future__ import annotations

from ispy.draw import face

# name -> (cx, cy, eye spacing)
FACE_ANCHORS: dict[str, tuple[float, float, float]] = {
    # garden and spring
    "flower_pot": (50, 64, 17),
    "watering_can": (57, 64, 16),
    "sand_bucket": (50, 62, 16),
    "seed_packet": (50, 72, 14),
    "rain_boot": (46, 52, 13),
    "mitten": (50, 50, 14),
    "sun_hat": (50, 48, 15),
    # food
    "apple": (50, 56, 16),
    "acorn": (50, 62, 14),
    "cookie": (50, 52, 17),
    "cupcake": (50, 70, 14),
    "birthday_cake": (50, 70, 15),
    "ice_cream_cone": (50, 26, 13),
    "popsicle": (50, 40, 14),
    "strawberry": (50, 58, 15),
    "watermelon_slice": (50, 58, 15),
    "pie": (50, 68, 14),
    "hot_cocoa": (48, 64, 13),
    "milk_bottle": (50, 70, 13),
    "taco": (50, 74, 13),
    "carrot": (50, 56, 11),
    "jelly_bean": (48, 52, 13),
    "candy_corn": (50, 64, 12),
    "wrapped_candy": (50, 50, 11),
    "pumpkin": (50, 58, 18),
    "mushroom": (50, 70, 12),
    # party and presents
    "gift": (50, 64, 17),
    "gift_bag": (50, 64, 15),
    "balloon": (50, 38, 17),
    "heart": (50, 50, 16),
    "candle": (50, 62, 11),
    "party_hat": (50, 58, 13),
    # weather and sky
    "cloud": (50, 52, 16),
    "star": (50, 52, 14),
    "crescent_moon": (54, 52, 11),
    "raindrop": (50, 54, 12),
    # clothes and cosy
    "beanie_hat": (50, 44, 15),
    "sweater": (50, 64, 15),
    "stocking": (48, 68, 12),
    "backpack": (50, 44, 14),
    # holidays
    "bell": (50, 48, 14),
    "cauldron": (50, 64, 15),
    "potion_bottle": (50, 70, 14),
    "witch_hat": (50, 40, 12),
    "pot_of_gold": (50, 64, 15),
    "shamrock": (50, 54, 12),
    "easter_basket": (50, 72, 14),
    # sea and shell
    "seashell": (50, 60, 14),
    # school and desk
    "crayon": (50, 60, 11),
    "glue_stick": (50, 58, 12),
    "lunchbox": (50, 68, 13),
    "paint_palette": (48, 64, 12),
    # outdoors
    "log": (50, 52, 12),
    "pet_bowl": (50, 66, 12),
    "bone": (50, 50, 10),
}


def cutify(name: str, body: str, blush: bool = True) -> str:
    """Add a little face to `body` when the icon is an object without one."""
    anchor = FACE_ANCHORS.get(name)
    if anchor is None:
        return body
    cx, cy, w = anchor
    return body + face(cx, cy, w, eye=2.9, smile=w * 0.46, blush=blush)
