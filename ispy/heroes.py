"""Full-body characters, one per theme, drawn chibi for coloring pages.

The rules here are cute-first: a head bigger than the body, big solid eyes,
a small smile, and as few interior lines as possible. A coloring page is not
an anatomy lesson - every extra line is another fiddly gap a four-year-old
has to color around, and the page reads busier for it.

Everything lives in the same 100x100 box as the icons, so a hero is placed
exactly like any other subject. `critter()` builds the standard body, so the
characters read as one family and each one is only its ears, its markings
and the thing it is holding.
"""

from __future__ import annotations

import math

from ispy.draw import (
    FILLED, arc, circle, dot, ellipse, heart, line, path, pt, rect, star,
    tube, zigzag,
)

SOLID_BLACK = 'fill="#000" stroke="none"'

HEROES: dict[str, callable] = {}

# The two-line greeting each hero page opens with: a small line over a big one.
PHRASES: dict[str, tuple[str, str]] = {
    "spring": ("LET'S BUZZ INTO", "SPRING!"),
    "summer": ("SNAP INTO", "SUMMER!"),
    "fall": ("GATHER UP FOR", "FALL!"),
    "winter": ("WADDLE INTO", "WINTER!"),
    "christmas": ("MERRY", "CHRISTMAS!"),
    "halloween": ("HAPPY", "HALLOWEEN!"),
    "thanksgiving": ("HAPPY", "THANKSGIVING!"),
    "valentine": ("BE MY", "VALENTINE!"),
    "easter": ("LET'S HOP INTO", "EASTER!"),
    "stpatrick": ("HAPPY", "ST. PATRICK'S"),
    "ocean": ("DIVE INTO THE", "OCEAN!"),
    "space": ("BLAST OFF INTO", "SPACE!"),
    "farm": ("DOWN ON THE", "FARM!"),
    "dinosaur": ("ROAR WITH THE", "DINOSAURS!"),
    "jungle": ("SWING INTO THE", "JUNGLE!"),
    "school": ("BACK TO", "SCHOOL!"),
    "transport": ("BEEP BEEP!", "THINGS THAT GO"),
    "camping": ("LET'S GO", "CAMPING!"),
    "birthday": ("HAPPY", "BIRTHDAY!"),
    "bugs": ("BUGGY ABOUT", "BUGS!"),
    "pets": ("I LOVE MY", "PETS!"),
    "food": ("YUMMY", "FOOD!"),
}




def hero(key: str):
    def deco(fn):
        HEROES[key] = fn
        return fn
    return deco


# --------------------------------------------------------- the chibi build ---
# One head, one body, one set of limbs, shared by every character.

HEAD_X, HEAD_Y, HEAD_R = 50.0, 34.0, 26.0
BODY_X, BODY_Y, BODY_RX, BODY_RY = 50.0, 75.0, 20.0, 18.0


def eyes(cx=HEAD_X, cy=HEAD_Y + 2, w=19.0, r=4.8, blush=True):
    out = [dot(cx - w / 2, cy, r), dot(cx + w / 2, cy, r)]
    if blush:
        out.append(ellipse(cx - w / 2 - 9, cy + 8, 4.2, 2.6))
        out.append(ellipse(cx + w / 2 + 9, cy + 8, 4.2, 2.6))
    return "".join(out)


def smile(cx=HEAD_X, cy=HEAD_Y + 12, r=6.0):
    return arc(cx, cy, r, 20, 160)


def muzzle(cx=HEAD_X, cy=HEAD_Y + 13, rx=10.0, ry=7.0, nose=3.0):
    """An oval snout with a nose and one smile line - nothing more."""
    return "".join([
        ellipse(cx, cy, rx, ry, 0, FILLED),
        ellipse(cx, cy - ry * 0.35, nose * 1.4, nose, 0, SOLID_BLACK),
        arc(cx, cy + ry * 0.2, rx * 0.45, 20, 160),
    ])


def head_shape():
    return circle(HEAD_X, HEAD_Y, HEAD_R, FILLED)


def body_shape():
    return ellipse(BODY_X, BODY_Y, BODY_RX, BODY_RY, 0, FILLED)


def arms(up=False, reach=15.0, mitt=6.0):
    out = []
    for s in (-1, 1):
        x1 = BODY_X + s * reach
        y1 = BODY_Y + (-8 if up else 6)
        out.append(tube([(BODY_X + s * 6, BODY_Y - 2), (x1, y1)], 3.4, FILLED))
        out.append(circle(x1, y1, mitt, FILLED))
    return "".join(out)


def feet(y=BODY_Y + 16, spread=10.0, rx=8.5, ry=5.5):
    return "".join(ellipse(BODY_X + s * spread, y, rx, ry, 0, FILLED)
                   for s in (-1, 1))


def round_ears(spread=20.0, r=10.0, y=HEAD_Y - 18):
    return "".join(circle(HEAD_X + s * spread, y, r, FILLED) for s in (-1, 1))


def pointy_ears(spread=17.0, h=17.0, w=15.0, y=HEAD_Y - 15):
    out = []
    for s in (-1, 1):
        bx = HEAD_X + s * spread
        out.append(path(f"M {bx - w / 2} {y + 4} L {bx + s * 2} {y - h} "
                        f"L {bx + w / 2} {y + 6} Z", FILLED))
    return "".join(out)


def long_ears(spread=11.0, h=34.0, w=14.0, tilt=10.0, y=HEAD_Y - 14):
    out = []
    for s in (-1, 1):
        ex = HEAD_X + s * spread
        shape = ellipse(ex, y - h / 2, w / 2, h / 2, 0, FILLED)
        out.append(f'<g transform="rotate({s * tilt} {ex} {y})">{shape}</g>')
    return "".join(out)


def floppy_ears(spread=24.0, rx=9.0, ry=14.0, y=HEAD_Y):
    return "".join(ellipse(HEAD_X + s * spread, y, rx, ry, s * 12, FILLED)
                   for s in (-1, 1))


def critter(ears="", behind="", marks="", extras="", prop="",
            snout=False, arms_up=False, has_feet=True, blush=True,
            face_parts=None):
    """Standard build, in the order things overlap.

    The prop goes on before the arms so the mitts land on top of it and the
    character reads as holding the thing rather than standing behind it.
    """
    return "".join([
        behind,
        feet() if has_feet else "",
        body_shape(),
        marks,
        prop,
        arms(up=arms_up),
        ears,
        head_shape(),
        face_parts if face_parts is not None
        else eyes(blush=blush) + (muzzle() if snout else smile()),
        extras,
    ])


# ---------------------------------------------------------------- heroes ----

def held(body: str) -> str:
    """Wrap a prop so it sits in the character's hands, in front of the body."""
    return body


@hero("easter")
def bunny_on_carrot():
    carrot = "".join([
        path("M 10 84 C 30 74 72 74 92 86 C 92 94 76 99 54 99 "
             "C 30 99 12 93 10 84 Z", FILLED),
        path("M 32 80 C 34 88 34 95 32 98"),
        path("M 54 76 C 56 84 56 93 54 99"),
        path("M 74 79 C 76 86 76 94 74 98"),
        path("M 10 84 C 0 78 -2 68 2 64 C 9 67 14 74 16 81"),
    ])
    return critter(behind=carrot, ears=long_ears(), snout=True, has_feet=False)


@hero("fall")
def squirrel_with_acorn():
    tail = path("M 74 88 C 94 84 98 56 86 42 C 74 28 54 32 54 46 "
                "C 68 38 82 46 84 60 C 86 74 80 84 68 86 Z", FILLED)
    acorn = "".join([
        path("M 40 84 C 40 94 45 98 50 98 C 55 98 60 94 60 84 Z", FILLED),
        path("M 38 84 C 38 77 43 74 50 74 C 57 74 62 77 62 84 Z", FILLED),
    ])
    return critter(behind=tail, ears=pointy_ears(14, 14, 13), snout=True,
                   prop=acorn)


@hero("spring")
def bee_with_flower():
    wings = (ellipse(22, 62, 17, 10, -24, FILLED)
             + ellipse(78, 62, 17, 10, 24, FILLED))
    stripes = (path("M 35 70 C 43 68 57 68 65 70")
               + path("M 34 80 C 43 82 57 82 66 80"))
    antennae = "".join([
        line(40, 14, 34, 4), line(60, 14, 66, 4),
        dot(33, 3, 3.6), dot(67, 3, 3.6),
    ])
    flower = "".join([
        "".join(circle(*pt(50, 84, 7, a), 5.6, FILLED)
                for a in range(0, 360, 72)),
        circle(50, 84, 4, FILLED),
    ])
    return critter(behind=wings, marks=stripes, extras=antennae, prop=flower)


@hero("valentine")
def bear_with_heart():
    return critter(ears=round_ears(), snout=True, arms_up=True,
                   prop=heart(50, 84, 13, FILLED))


@hero("camping")
def bear_with_marshmallow():
    stick = (line(64, 82, 92, 52) + rect(84, 38, 16, 14, 6, FILLED))
    return critter(ears=round_ears(), snout=True, extras=stick)


@hero("pets")
def dog_with_bone():
    bone = "".join([
        path("M 36 84 C 31 79 24 81 24 86 C 24 90 29 91 33 88 "
             "L 67 88 C 71 91 76 90 76 86 C 76 81 69 79 64 84 Z", FILLED),
    ])
    return critter(ears=floppy_ears(), snout=True, prop=bone)


@hero("halloween")
def cat_with_lantern():
    whiskers = "".join([
        line(26, 40, 10, 36), line(26, 46, 10, 48),
        line(74, 40, 90, 36), line(74, 46, 90, 48),
    ])
    nose = path("M 50 44 L 45 49 L 55 49 Z", SOLID_BLACK)
    lantern = "".join([
        ellipse(50, 86, 15, 12, 0, FILLED),
        path("M 50 74 L 50 70"),
        path("M 43 83 L 48 83 L 45.5 78 Z", SOLID_BLACK),
        path("M 57 83 L 52 83 L 54.5 78 Z", SOLID_BLACK),
        path("M 42 89 L 46 89 L 48 92 L 52 92 L 54 89 L 58 89 "
             "L 56 94 L 44 94 Z", SOLID_BLACK),
    ])
    return critter(ears=pointy_ears(16, 16, 14), extras=whiskers + nose,
                   prop=lantern)


@hero("christmas")
def reindeer_with_gift():
    antlers = "".join([
        path("M 32 18 C 26 8 24 2 26 -2 M 26 8 L 16 4 M 29 14 L 19 14"),
        path("M 68 18 C 74 8 76 2 74 -2 M 74 8 L 84 4 M 71 14 L 81 14"),
    ])
    gift = "".join([
        rect(38, 76, 24, 20, 3, FILLED),
        rect(35, 71, 30, 7, 3, FILLED),
        line(50, 71, 50, 96),
    ])
    nose = circle(50, 45, 5, SOLID_BLACK)
    return critter(ears=floppy_ears(26, 10, 6, 30), snout=True,
                   extras=antlers + nose, prop=gift, arms_up=True)


@hero("birthday")
def fox_with_cupcake():
    hat = (path("M 50 -4 L 40 14 L 60 14 Z", FILLED) + circle(50, -7, 4.6, FILLED))
    cupcake = "".join([
        path("M 40 84 L 60 84 L 57 96 L 43 96 Z", FILLED),
        path("M 38 84 C 38 74 45 70 50 74 C 55 70 62 74 62 84 Z", FILLED),
        circle(50, 68, 3.6, FILLED),
    ])
    tail = path("M 72 86 C 92 84 98 64 88 54 C 82 48 74 54 78 62", FILLED)
    return critter(behind=tail, ears=pointy_ears(17, 18, 15), snout=True,
                   extras=hat, prop=cupcake)


@hero("jungle")
def monkey_with_banana():
    ears = "".join(circle(HEAD_X + s * 26, HEAD_Y, 10, FILLED) for s in (-1, 1))
    face_patch = path("M 50 30 C 64 30 70 40 70 47 C 70 55 61 60 50 60 "
                      "C 39 60 30 55 30 47 C 30 40 36 30 50 30 Z", FILLED)
    banana = path("M 36 86 C 34 95 46 100 60 97 C 62 93 60 90 56 89 "
                  "C 50 93 43 91 41 84 Z", FILLED)
    tail = path("M 70 84 C 90 82 96 62 86 54 C 80 50 74 56 78 62")
    return critter(behind=tail, ears=ears, prop=banana,
                   face_parts=face_patch + eyes(w=19, r=4.8)
                   + dot(46, 46, 2.6) + dot(54, 46, 2.6)
                   + arc(50, 50, 6, 20, 160))


@hero("farm")
def cow_with_bell():
    horns = "".join([
        path("M 32 8 C 24 2 26 -4 33 -3 C 37 0 36 5 34 8 Z", FILLED),
        path("M 68 8 C 76 2 74 -4 67 -3 C 63 0 64 5 66 8 Z", FILLED),
    ])
    spots = (circle(34, 76, 6, FILLED) + ellipse(64, 82, 7, 5, 20, FILLED))
    bell = "".join([
        path("M 46 58 C 46 54 54 54 54 58 C 56 62 56 64 50 64 "
             "C 44 64 44 62 46 58 Z", FILLED),
        dot(50, 63, 2.2),
    ])
    return critter(ears=floppy_ears(28, 11, 7, 32), snout=True, marks=spots,
                   extras=horns + bell)


@hero("winter")
def penguin_in_hat():
    wings = (path("M 30 66 C 20 74 20 88 28 92", FILLED)
             + path("M 70 66 C 80 74 80 88 72 92", FILLED))
    feet_tri = (path("M 40 92 L 32 98 L 50 98 Z", FILLED)
                + path("M 60 92 L 68 98 L 50 98 Z", FILLED))
    beak = path("M 50 44 L 58 50 L 42 50 Z", FILLED)
    hat = "".join([
        path("M 28 12 C 30 -2 70 -2 72 12 Z", FILLED),
        rect(24, 8, 52, 9, 4, FILLED),
        circle(50, -6, 6.5, FILLED),
    ])
    scarf = "".join([
        path("M 26 58 C 34 64 66 64 74 58 C 74 66 66 70 50 70 "
             "C 34 70 26 66 26 58 Z", FILLED),
        path("M 62 68 L 62 86 L 74 86 L 74 66", FILLED),
    ])
    return critter(behind=wings + feet_tri, extras=beak + scarf + hat,
                   has_feet=False)


@hero("thanksgiving")
def turkey_with_fan():
    fan = "".join(ellipse(*pt(50, 74, 34, a), 15, 10, a, FILLED)
                  for a in range(188, 356, 24))
    beak = path("M 50 46 L 62 51 L 50 56 Z", FILLED)
    wattle = path("M 55 55 C 61 60 59 68 52 65")
    tuft = path("M 42 10 C 40 2 46 0 48 5 C 52 -2 58 2 56 10", FILLED)
    feet_tri = (path("M 42 92 L 34 98 L 50 98 Z", FILLED)
                + path("M 58 92 L 66 98 L 50 98 Z", FILLED))
    return critter(behind=fan + feet_tri, extras=beak + wattle + tuft,
                   has_feet=False)


@hero("space")
def alien_with_star():
    antennae = "".join([
        line(38, 14, 32, 2), line(62, 14, 68, 2),
        circle(31, 0, 5, FILLED), circle(69, 0, 5, FILLED),
    ])
    big_eyes = (ellipse(38, 34, 9, 12, 16, FILLED)
                + ellipse(62, 34, 9, 12, -16, FILLED))
    return "".join([
        feet(), arms(up=True), body_shape(),
        path("M 50 8 C 72 8 84 22 84 38 C 84 54 70 60 50 60 "
             "C 30 60 16 54 16 38 C 16 22 28 8 50 8 Z", FILLED),
        big_eyes, arc(50, 48, 7, 20, 160), antennae,
        star(50, 78, 16, 5, 0.45, -90, FILLED),
    ])


@hero("ocean")
def octopus_with_star():
    legs = "".join(
        path(f"M {x} 68 C {x + 8 * d} 80 {x - 8 * d} 90 {x + 6 * d} 98",
             FILLED)
        for x, d in ((24, -1), (37, 1), (50, -1), (63, 1), (76, -1))
    )
    return "".join([
        legs,
        path("M 50 10 C 74 10 88 28 88 50 C 88 66 70 72 50 72 "
             "C 30 72 12 66 12 50 C 12 28 26 10 50 10 Z", FILLED),
        eyes(50, 40, 22, 5.2),
        arc(50, 54, 7, 20, 160),
        star(80, 84, 14, 5, 0.45, -90, FILLED),
    ])


@hero("bugs")
def ladybug_with_dots():
    legs = "".join([
        line(20, 66, 8, 62), line(20, 76, 6, 78), line(24, 86, 14, 94),
        line(80, 66, 92, 62), line(80, 76, 94, 78), line(76, 86, 86, 94),
    ])
    antennae = "".join([
        line(38, 12, 30, 2), line(62, 12, 70, 2),
        dot(29, 1, 4), dot(71, 1, 4),
    ])
    shell = "".join([
        ellipse(50, 66, 32, 30, 0, FILLED),
        line(50, 36, 50, 96),
        circle(34, 60, 7, FILLED), circle(66, 60, 7, FILLED),
        circle(36, 80, 6, FILLED), circle(64, 80, 6, FILLED),
    ])
    head = "".join([
        path("M 50 12 C 68 12 78 22 78 34 C 66 40 34 40 22 34 "
             "C 22 22 32 12 50 12 Z", FILLED),
        eyes(50, 26, 18, 4.4),
        arc(50, 34, 6, 20, 160),
    ])
    return legs + shell + head + antennae


@hero("school")
def owl_with_book():
    book = "".join([
        path("M 26 76 C 33 70 44 70 50 74 C 56 70 67 70 74 76 "
             "L 74 92 C 67 86 56 86 50 90 C 44 86 33 86 26 92 Z", FILLED),
        line(50, 74, 50, 90),
    ])
    tufts = (path("M 30 16 L 24 4 L 40 12") + path("M 70 16 L 76 4 L 60 12"))
    specs = (circle(37, 36, 15) + circle(63, 36, 15) + line(48, 36, 52, 36))
    return "".join([
        path("M 40 92 L 32 98 L 48 98 Z", FILLED),
        path("M 60 92 L 68 98 L 52 98 Z", FILLED),
        path("M 50 6 C 76 6 90 28 90 56 C 90 82 72 94 50 94 "
             "C 28 94 10 82 10 56 C 10 28 24 6 50 6 Z", FILLED),
        circle(37, 36, 11, FILLED), circle(63, 36, 11, FILLED),
        dot(37, 36, 5), dot(63, 36, 5),
        specs, tufts,
        path("M 50 46 L 56 54 L 44 54 Z", FILLED),
        book,
    ])


@hero("dinosaur")
def dino_with_spikes():
    tail = path("M 22 76 C 8 78 2 90 10 95 C 17 99 26 93 28 86", FILLED)
    spikes = "".join([
        path("M 30 40 L 24 28 L 38 32 Z", FILLED),
        path("M 42 26 L 40 12 L 52 22 Z", FILLED),
        path("M 58 22 L 62 10 L 70 22 Z", FILLED),
    ])
    return "".join([
        tail, spikes,
        feet(88, 14, 10, 6),
        ellipse(44, 70, 28, 24, 0, FILLED),
        circle(72, 36, 20, FILLED),
        ellipse(88, 44, 11, 8, 10, FILLED),
        dot(70, 30, 4.4),
        ellipse(63, 42, 4, 2.6, 0),
        arc(82, 48, 6, 20, 160),
        dot(92, 42, 2.4),
    ])


@hero("stpatrick")
def pot_of_gold():
    clover = "".join(
        f'<g transform="rotate({a} 80 20)">{heart(80, 10, 10, FILLED)}</g>'
        for a in (0, 90, 180, 270)
    )
    coins = "".join([
        circle(32, 38, 10, FILLED), circle(52, 34, 10, FILLED),
        circle(70, 40, 10, FILLED),
    ])
    return "".join([
        coins,
        path("M 14 46 C 14 78 30 94 50 94 C 70 94 86 78 86 46 Z", FILLED),
        rect(8, 38, 84, 12, 6, FILLED),
        eyes(50, 62, 22, 5.2),
        arc(50, 76, 8, 20, 160),
        clover,
        path("M 80 30 C 82 38 82 42 80 46"),
    ])


@hero("transport")
def happy_car():
    return "".join([
        path("M 6 62 L 12 42 C 15 32 26 28 38 28 L 62 28 "
             "C 74 28 85 32 88 42 L 94 62 C 94 72 88 74 78 74 "
             "L 22 74 C 12 74 6 72 6 62 Z", FILLED),
        path("M 28 28 L 32 10 L 68 10 L 72 28", FILLED),
        line(50, 10, 50, 28),
        circle(26, 82, 15, FILLED), circle(74, 82, 15, FILLED),
        circle(26, 82, 6, FILLED), circle(74, 82, 6, FILLED),
        dot(36, 50, 5), dot(64, 50, 5),
        arc(50, 56, 10, 20, 160),
        ellipse(15, 58, 6, 4, 0, FILLED), ellipse(85, 58, 6, 4, 0, FILLED),
    ])


@hero("summer")
def crab_with_ice_cream():
    legs = "".join(
        path(f"M {x} 84 C {x + 6 * d} 94 {x + 12 * d} 97 {x + 18 * d} 96")
        for x, d in ((32, -1), (44, -1), (56, 1), (68, 1))
    )
    claws = "".join([
        path("M 20 62 C 6 56 2 40 12 34 C 16 40 14 48 22 50 "
             "C 12 46 16 34 24 37 C 32 41 30 58 20 62 Z", FILLED),
        path("M 80 62 C 94 56 98 40 88 34 C 84 40 86 48 78 50 "
             "C 88 46 84 34 76 37 C 68 41 70 58 80 62 Z", FILLED),
    ])
    shades = path("M 28 42 C 34 38 42 38 46 42 L 54 42 C 58 38 66 38 72 42 "
                  "C 72 50 62 54 58 46 L 42 46 C 38 54 28 50 28 42 Z", FILLED)
    cone = "".join([
        path("M 72 70 L 92 70 L 82 96 Z", FILLED),
        circle(76, 62, 9, FILLED), circle(88, 62, 8, FILLED),
        circle(82, 52, 8.5, FILLED),
    ])
    stalks = (line(38, 30, 34, 16) + line(62, 30, 66, 16)
              + dot(33, 14, 4) + dot(67, 14, 4))
    return "".join([
        legs, claws,
        ellipse(50, 62, 32, 24, 0, FILLED),
        stalks, shades,
        arc(50, 70, 10, 20, 160),
        cone,
    ])


@hero("food")
def strawberry_friend():
    leaves = "".join(ellipse(*pt(50, 30, 16, a), 12, 7, a, FILLED)
                     for a in (196, 232, 270, 308, 344))
    seeds = "".join(dot(x, y, 2.8) for x, y in
                    ((26, 72), (74, 72), (34, 86), (66, 86), (50, 92)))
    return "".join([
        feet(94, 12, 8, 5),
        arms(reach=22),
        path("M 50 26 C 78 26 92 46 88 68 C 84 88 68 97 50 97 "
             "C 32 97 16 88 12 68 C 8 46 22 26 50 26 Z", FILLED),
        leaves,
        eyes(50, 58, 22, 5.2),
        arc(50, 72, 8, 20, 160),
        seeds,
    ])
