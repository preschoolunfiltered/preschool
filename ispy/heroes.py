"""Full-body character drawings, one per theme, for the coloring pages.

The icon library is drawn to read at 30pt on an I Spy sheet, which is why a
blown-up icon looks thin as the star of a coloring page: a bunny there is a
head, not a character. These are drawn for page size instead - a body, arms,
legs, a face and something to hold - at the fidelity a store-bought sheet has.

Everything lives in the same 100x100 box as the icons, so the coloring page
places a hero exactly the way it places any other subject. The parts below
(head, ears, body, arms, feet) are shared so twenty-odd characters read as
one family rather than twenty separate drawings.
"""

from __future__ import annotations

import math

from ispy.draw import (
    FILLED, arc, circle, dot, ellipse, heart, line, path, pt, rect, star,
    tube, zigzag,
)

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


# ------------------------------------------------------------- body parts ---

def face(cx, cy, w=15.0, eye=3.0, smile=7.0, blush=True, closed=False):
    """Eyes, a smile, and two blush ovals - the set's house expression."""
    out = []
    if closed:
        out.append(arc(cx - w / 2, cy, 4.0, 200, 340))
        out.append(arc(cx + w / 2, cy, 4.0, 200, 340))
    else:
        out.append(dot(cx - w / 2, cy, eye))
        out.append(dot(cx + w / 2, cy, eye))
    out.append(arc(cx, cy + 3.5, smile, 20, 160))
    if blush:
        out.append(ellipse(cx - w / 2 - 7.5, cy + 5.5, 3.6, 2.4))
        out.append(ellipse(cx + w / 2 + 7.5, cy + 5.5, 3.6, 2.4))
    return "".join(out)


def snout(cx, cy, rx=8.0, ry=6.0, nose_r=2.6):
    """A muzzle with a nose and the little W mouth under it."""
    return "".join([
        ellipse(cx, cy, rx, ry, 0, FILLED),
        ellipse(cx, cy - ry * 0.45, nose_r * 1.3, nose_r, 0, "fill=\"#000\" stroke=\"none\""),
        path(f"M {cx} {cy - ry * 0.1} L {cx} {cy + ry * 0.5}"),
        path(f"M {cx} {cy + ry * 0.5} C {cx - 3} {cy + ry * 1.1} "
             f"{cx - 5} {cy + ry * 0.6} {cx - 5.5} {cy + ry * 0.2}"),
        path(f"M {cx} {cy + ry * 0.5} C {cx + 3} {cy + ry * 1.1} "
             f"{cx + 5} {cy + ry * 0.6} {cx + 5.5} {cy + ry * 0.2}"),
    ])


def round_ears(cx, cy, r, spread, ear_r, inner=True):
    out = []
    for s in (-1, 1):
        ex, ey = cx + s * spread, cy
        out.append(circle(ex, ey, ear_r, FILLED))
        if inner:
            out.append(circle(ex, ey, ear_r * 0.5, FILLED))
    return "".join(out)


def pointy_ears(cx, cy, spread, h, w, inner=True):
    out = []
    for s in (-1, 1):
        bx = cx + s * spread
        out.append(path(f"M {bx - w / 2} {cy} L {bx + s * w * 0.15} {cy - h} "
                        f"L {bx + w / 2} {cy + 2} Z", FILLED))
        if inner:
            out.append(path(f"M {bx - w * 0.22} {cy - 1} "
                            f"L {bx + s * w * 0.1} {cy - h * 0.6} "
                            f"L {bx + w * 0.22} {cy} Z"))
    return "".join(out)


def long_ears(cx, cy, spread, h, w, tilt=9.0):
    out = []
    for s in (-1, 1):
        ex = cx + s * spread
        body = (ellipse(ex, cy - h / 2, w / 2, h / 2, 0, FILLED)
                + ellipse(ex, cy - h / 2, w / 5, h / 2.6, 0, FILLED))
        out.append(f'<g transform="rotate({s * tilt} {ex} {cy})">{body}</g>')
    return "".join(out)


def belly(cx, cy, rx, ry):
    return ellipse(cx, cy, rx, ry, 0, FILLED)


def arms(cx, cy, reach=15.0, drop=9.0, w=5.0, mitt=5.4, up=False):
    """Two short limbs with round mitts, held down or up."""
    out = []
    for s in (-1, 1):
        x0, y0 = cx + s * (reach * 0.5), cy
        x1, y1 = cx + s * reach, cy + (-drop if up else drop)
        out.append(tube([(x0, y0), (x1, y1)], w / 2, FILLED))
        out.append(circle(x1, y1, mitt, FILLED))
    return "".join(out)


def feet(cx, cy, spread=11.0, rx=8.0, ry=5.5):
    return "".join(ellipse(cx + s * spread, cy, rx, ry, 0, FILLED)
                   for s in (-1, 1))


def tail_curl(x, y, r=8.0):
    return arc(x, y, r, 250, 520)


# ---------------------------------------------------------------- heroes ----

@hero("easter")
def bunny_on_carrot():
    """A bunny sitting on a giant carrot."""
    carrot = "".join([
        path("M 16 80 C 32 70 72 70 88 82 C 88 90 76 97 58 97 "
             "C 36 97 18 90 16 80 Z", FILLED),
        path("M 32 76 C 34 84 34 92 32 96"),
        path("M 48 72 C 50 80 50 90 48 97"),
        path("M 64 73 C 66 80 66 90 64 96"),
        path("M 16 80 C 6 74 4 64 8 60 C 15 63 20 70 22 77"),
        path("M 18 77 C 14 66 17 57 23 53 C 28 60 28 70 26 77"),
    ])
    bunny = "".join([
        feet(50, 72, 13, 8.5, 5),
        arms(50, 56, 18, 8, 5, 5.4),
        ellipse(50, 56, 18, 16, 0, FILLED),
        belly(50, 60, 10, 9),
        long_ears(50, 24, 8, 30, 13),
        circle(50, 30, 17, FILLED),
        face(50, 28, 14, 3.0, 6.5),
        snout(50, 36, 6, 4.5, 2.2),
    ])
    return carrot + bunny


@hero("fall")
def squirrel_with_acorn():
    """A squirrel holding an acorn, tail up behind it."""
    tail = path("M 74 84 C 92 80 96 56 86 42 C 76 28 56 30 54 44 "
                "C 66 36 80 42 82 56 C 84 70 78 80 68 82 Z", FILLED)
    body = "".join([
        feet(48, 88, 12, 8, 5),
        ellipse(48, 68, 19, 18, 0, FILLED),
        belly(48, 72, 11, 10),
        arms(48, 62, 16, 8, 5, 5.2),
        pointy_ears(48, 30, 11, 12, 9),
        circle(48, 38, 17, FILLED),
        face(48, 36, 14, 3.0, 6.5),
        snout(48, 44, 5.5, 4.2, 2.2),
    ])
    acorn = "".join([
        path("M 40 74 C 40 84 44 90 50 90 C 56 90 60 84 60 74 Z", FILLED),
        path("M 38 74 C 38 68 43 65 50 65 C 57 65 62 68 62 74 Z", FILLED),
        line(50, 65, 50, 60),
    ])
    return tail + body + acorn


@hero("halloween")
def cat_with_lantern():
    """A cat holding a little jack-o'-lantern."""
    return "".join([
        path("M 72 76 C 88 74 92 58 82 52"),
        feet(50, 90, 13, 8.5, 5.2),
        arms(50, 66, 18, 8, 5, 5.4),
        ellipse(50, 68, 19, 18, 0, FILLED),
        belly(50, 72, 10, 9),
        pointy_ears(50, 22, 12, 14, 11),
        circle(50, 32, 18, FILLED),
        face(50, 29, 14, 3.1, 6.5),
        path("M 50 36 L 45.5 40 L 54.5 40 Z", 'fill="#000" stroke="none"'),
        line(32, 34, 18, 31), line(32, 38, 18, 40),
        line(68, 34, 82, 31), line(68, 38, 82, 40),
        ellipse(50, 80, 16, 13, 0, FILLED),
        path("M 50 67 L 50 62"),
        path("M 42 76 L 48 76 L 45 71 Z", 'fill="#000" stroke="none"'),
        path("M 58 76 L 52 76 L 55 71 Z", 'fill="#000" stroke="none"'),
        path("M 42 84 L 46 84 L 48 87 L 52 87 L 54 84 L 58 84 "
             "L 56 89 L 44 89 Z", 'fill="#000" stroke="none"'),
    ])


@hero("valentine")
def bear_with_heart():
    """A teddy bear hugging a heart."""
    return "".join([
        feet(50, 88, 13, 9, 6),
        arms(50, 62, 19, 4, 5.4, 6.0, up=True),
        ellipse(50, 66, 20, 19, 0, FILLED),
        belly(50, 70, 12, 11),
        round_ears(50, 24, 16, 15, 8),
        circle(50, 34, 19, FILLED),
        face(50, 31, 15, 3.1, 7),
        snout(50, 41, 8, 5.5, 2.6),
        heart(50, 70, 13, FILLED),
    ])


@hero("ocean")
def octopus_with_starfish():
    """An octopus holding a starfish, tentacles curling below."""
    legs = []
    for i, x in enumerate((22, 34, 46, 58, 70)):
        d = 1 if i % 2 else -1
        legs.append(path(f"M {x} 62 C {x + 7 * d} 74 {x - 7 * d} 84 "
                         f"{x + 5 * d} 94", FILLED))
    return "".join([
        "".join(legs),
        path("M 20 60 C 20 34 34 20 51 20 C 68 20 82 34 82 60 "
             "C 66 68 36 68 20 60 Z", FILLED),
        face(51, 44, 16, 3.2, 7.5),
        star(80, 80, 15, 5, 0.45, -90, FILLED),
        dot(80, 80, 2.6),
    ])


@hero("pets")
def dog_with_bone():
    """A sitting dog with a bone at its paws."""
    return "".join([
        path("M 72 76 C 88 74 92 58 82 52"),
        feet(50, 86, 15, 9, 5.5),
        arms(50, 70, 19, 12, 5, 5.4),
        ellipse(50, 68, 19, 18, 0, FILLED),
        belly(50, 73, 9, 8),
        ellipse(26, 34, 8, 14, -12, FILLED),
        ellipse(74, 34, 8, 14, 12, FILLED),
        circle(50, 32, 18, FILLED),
        face(50, 29, 14, 3.1, 6.5),
        snout(50, 40, 8, 5.5, 2.8),
        path("M 28 93 C 22 88 14 90 14 95 C 14 99 20 100 24 97 "
             "L 72 97 C 76 100 82 99 82 95 C 82 90 74 88 68 93 Z", FILLED),
    ])


@hero("spring")
def bee_with_flower():
    """A round bee holding a flower."""
    wings = (ellipse(24, 46, 18, 11, -26, FILLED)
             + ellipse(76, 46, 18, 11, 26, FILLED))
    body = "".join([
        feet(50, 88, 11, 7, 4.6),
        arms(50, 64, 17, 7, 4.8, 5.2),
        ellipse(50, 66, 20, 19, 0, FILLED),
        path("M 33 58 C 42 56 58 56 67 58"),
        path("M 31 72 C 42 74 58 74 69 72"),
        circle(50, 34, 17, FILLED),
        line(42, 20, 38, 10), line(58, 20, 62, 10),
        dot(37, 8, 3.2), dot(63, 8, 3.2),
        face(50, 32, 14, 3.0, 6.5),
    ])
    flower = "".join([
        "".join(circle(*pt(72, 78, 7, a), 5.4, FILLED) for a in range(0, 360, 72)),
        circle(72, 78, 4, FILLED),
        path("M 72 86 C 71 92 70 96 68 99"),
    ])
    return wings + body + flower


@hero("summer")
def crab_with_ice_cream():
    """A crab in sunglasses holding an ice cream."""
    legs = "".join(
        path(f"M {x} 76 C {x + 6 * d} 86 {x + 12 * d} 90 {x + 18 * d} 90")
        for x, d in ((34, -1), (44, -1), (56, 1), (66, 1))
    )
    claw_l = path("M 24 56 C 10 50 6 36 14 30 C 18 36 16 44 24 46 "
                  "C 16 42 20 32 26 34 C 33 37 32 52 24 56 Z", FILLED)
    claw_r = path("M 76 56 C 90 50 94 36 86 30 C 82 36 84 44 76 46 "
                  "C 84 42 80 32 74 34 C 67 37 68 52 76 56 Z", FILLED)
    body = "".join([
        ellipse(50, 62, 27, 20, 0, FILLED),
        line(40, 46, 36, 34), line(60, 46, 64, 34),
        dot(35, 32, 3.4), dot(65, 32, 3.4),
        path("M 30 52 C 36 48 44 48 48 52 L 52 52 C 56 48 64 48 70 52 "
             "C 70 58 62 62 58 56 L 52 56 L 48 56 C 44 62 30 58 30 52 Z",
             FILLED),
        arc(50, 68, 9, 20, 160),
    ])
    cone = "".join([
        path("M 74 66 L 90 66 L 82 88 Z", FILLED),
        circle(78, 60, 8, FILLED), circle(87, 60, 7, FILLED),
        circle(82, 52, 7.5, FILLED),
    ])
    return legs + claw_l + claw_r + body + cone


@hero("winter")
def penguin_in_scarf():
    """A penguin in a scarf and bobble hat."""
    return "".join([
        path("M 22 62 C 12 70 12 82 20 86"),
        path("M 78 62 C 88 70 88 82 80 86"),
        path("M 34 92 L 26 98 L 46 98 Z", FILLED),
        path("M 66 92 L 74 98 L 54 98 Z", FILLED),
        path("M 50 26 C 70 26 80 46 80 66 C 80 84 66 94 50 94 "
             "C 34 94 20 84 20 66 C 20 46 30 26 50 26 Z", FILLED),
        path("M 50 46 C 63 46 70 58 70 70 C 70 84 62 90 50 90 "
             "C 38 90 30 84 30 70 C 30 58 37 46 50 46 Z", FILLED),
        dot(43, 36, 3.2), dot(57, 36, 3.2),
        path("M 50 40 L 58 46 L 42 46 Z", FILLED),
        path("M 24 52 C 34 58 66 58 76 52 C 76 60 68 64 50 64 "
             "C 32 64 24 60 24 52 Z", FILLED),
        path("M 62 62 L 62 80 L 74 80 L 74 60", FILLED),
        line(64, 80, 64, 86), line(68, 80, 68, 86), line(72, 80, 72, 86),
        path("M 30 26 C 30 12 70 12 70 26 Z", FILLED),
        rect(26, 20, 48, 9, 4, FILLED),
        circle(50, 8, 7, FILLED),
    ])


@hero("christmas")
def reindeer_with_gift():
    """A reindeer holding a wrapped present."""
    antlers = "".join([
        path("M 34 26 C 28 16 26 8 28 2 M 28 12 L 18 8 M 31 18 L 21 18"),
        path("M 66 26 C 72 16 74 8 72 2 M 72 12 L 82 8 M 69 18 L 79 18"),
    ])
    return "".join([
        antlers,
        feet(50, 90, 13, 9, 5.5),
        arms(50, 64, 19, 4, 5.2, 5.6, up=True),
        ellipse(50, 68, 20, 19, 0, FILLED),
        belly(50, 72, 12, 11),
        ellipse(24, 36, 9, 6, -20, FILLED),
        ellipse(76, 36, 9, 6, 20, FILLED),
        circle(50, 34, 18, FILLED),
        face(50, 30, 14, 3.1, 6.5),
        ellipse(50, 42, 8, 6, 0, FILLED),
        circle(50, 41, 4, 'fill="#000" stroke="none"'),
        rect(36, 62, 28, 24, 3, FILLED),
        rect(34, 56, 32, 8, 3, FILLED),
        line(50, 56, 50, 86),
        path("M 50 56 C 42 56 36 52 38 47 C 41 43 48 48 50 56 Z", FILLED),
        path("M 50 56 C 58 56 64 52 62 47 C 59 43 52 48 50 56 Z", FILLED),
    ])


@hero("farm")
def cow_with_bell():
    """A cow with horns, a bell and two spots."""
    return "".join([
        path("M 80 72 C 92 70 96 56 88 50"),
        feet(50, 92, 15, 8.5, 5.2),
        ellipse(50, 72, 22, 18, 0, FILLED),
        circle(36, 70, 6.5, FILLED),
        ellipse(63, 78, 7, 5, 20, FILLED),
        ellipse(20, 36, 10, 7, -22, FILLED),
        ellipse(80, 36, 10, 7, 22, FILLED),
        path("M 36 20 C 30 14 32 8 38 9 C 41 12 40 17 38 20 Z", FILLED),
        path("M 64 20 C 70 14 68 8 62 9 C 59 12 60 17 62 20 Z", FILLED),
        circle(50, 34, 19, FILLED),
        dot(42, 30, 3.2), dot(58, 30, 3.2),
        ellipse(50, 45, 12, 8, 0, FILLED),
        dot(45, 43, 2.4), dot(55, 43, 2.4),
        arc(50, 48, 5, 20, 160),
        path("M 33 56 C 40 61 60 61 67 56"),
        path("M 50 60 C 45 60 44 67 50 69 C 56 67 55 60 50 60 Z", FILLED),
        dot(50, 65, 2.2),
    ])


@hero("jungle")
def monkey_with_banana():
    """A monkey holding a banana."""
    return "".join([
        path("M 74 74 C 90 72 94 54 84 46 C 78 42 72 46 74 52"),
        feet(50, 90, 14, 9, 5.5),
        arms(50, 66, 19, 8, 5.2, 5.6),
        ellipse(50, 70, 19, 18, 0, FILLED),
        belly(50, 74, 11, 10),
        circle(22, 34, 10, FILLED), circle(78, 34, 10, FILLED),
        circle(22, 34, 5, FILLED), circle(78, 34, 5, FILLED),
        circle(50, 34, 18, FILLED),
        path("M 50 30 C 62 30 68 38 68 44 C 68 51 60 55 50 55 "
             "C 40 55 32 51 32 44 C 32 38 38 30 50 30 Z", FILLED),
        dot(43, 28, 3.1), dot(57, 28, 3.1),
        dot(46, 42, 2.3), dot(54, 42, 2.3),
        arc(50, 45, 6, 20, 160),
        path("M 62 78 C 60 88 70 96 84 94 C 86 90 84 86 80 84 "
             "C 74 88 68 86 66 78 Z", FILLED),
        path("M 62 78 L 60 74 L 66 75 L 66 78"),
    ])


@hero("thanksgiving")
def turkey_with_fan():
    """A turkey with a full feather fan."""
    fan = "".join(
        ellipse(*pt(50, 66, 32, a), 14, 9, a, FILLED)
        for a in range(190, 356, 27)
    )
    inner = "".join(
        ellipse(*pt(50, 66, 18, a), 9, 6, a, FILLED)
        for a in range(200, 345, 36)
    )
    return "".join([
        fan, inner,
        path("M 40 92 L 34 98 L 48 98 Z", FILLED),
        path("M 60 92 L 66 98 L 52 98 Z", FILLED),
        ellipse(50, 70, 21, 20, 0, FILLED),
        circle(50, 38, 15, FILLED),
        dot(44, 34, 3.1), dot(56, 34, 3.1),
        path("M 50 42 L 62 46 L 50 50 Z", FILLED),
        path("M 54 49 C 60 54 58 62 51 59"),
        path("M 42 22 C 40 15 46 13 48 18 C 52 11 58 15 56 22", FILLED),
        arc(50, 76, 9, 20, 160),
    ])


@hero("stpatrick")
def pot_of_gold():
    """A smiling pot of gold with a four-leaf clover."""
    return "".join([
        circle(34, 40, 9, FILLED), circle(52, 36, 9, FILLED),
        circle(68, 42, 9, FILLED),
        circle(34, 40, 4, FILLED), circle(52, 36, 4, FILLED),
        path("M 16 48 C 16 78 30 92 50 92 C 70 92 84 78 84 48 Z", FILLED),
        rect(10, 40, 80, 11, 5, FILLED),
        face(50, 66, 17, 3.4, 8),
        "".join(
            f'<g transform="rotate({a} 84 24)">'
            + heart(84, 14, 9, FILLED) + "</g>"
            for a in (0, 90, 180, 270)
        ),
        path("M 84 32 C 86 40 86 44 84 48"),
    ])


@hero("space")
def alien_with_star():
    """A little alien holding a star."""
    return "".join([
        feet(50, 92, 12, 8, 5),
        arms(50, 66, 18, 4, 4.8, 5.2, up=True),
        ellipse(50, 70, 17, 16, 0, FILLED),
        line(40, 24, 34, 12), line(60, 24, 66, 12),
        circle(33, 10, 4.4, FILLED), circle(67, 10, 4.4, FILLED),
        path("M 50 16 C 70 16 82 30 82 44 C 82 58 68 64 50 64 "
             "C 32 64 18 58 18 44 C 18 30 30 16 50 16 Z", FILLED),
        ellipse(38, 40, 8, 11, 18, 'fill="#000" stroke="none"'),
        ellipse(62, 40, 8, 11, -18, 'fill="#000" stroke="none"'),
        arc(50, 52, 7, 20, 160),
        star(50, 74, 14, 5, 0.45, -90, FILLED),
    ])


@hero("dinosaur")
def dino_with_spikes():
    """A chubby dinosaur with a long tail and spiky back."""
    return "".join([
        path("M 24 72 C 10 74 2 84 8 90 C 14 95 24 90 26 82", FILLED),
        feet(46, 90, 17, 10, 6),
        path("M 36 48 L 30 36 L 44 40 Z", FILLED),
        path("M 48 36 L 46 22 L 58 32 Z", FILLED),
        path("M 62 32 L 66 20 L 72 32 Z", FILLED),
        tube([(54, 62), (64, 50), (70, 42)], 9, FILLED),
        ellipse(46, 66, 26, 22, 0, FILLED),
        ellipse(44, 74, 13, 10, 0, FILLED),
        circle(72, 36, 15, FILLED),
        ellipse(84, 42, 10, 7, 10, FILLED),
        dot(70, 32, 3.2),
        dot(88, 40, 2.2),
        arc(80, 46, 5, 20, 160),
    ])


@hero("school")
def owl_with_book():
    """A bespectacled owl holding a book."""
    return "".join([
        path("M 38 90 L 32 97 L 46 97 Z", FILLED),
        path("M 62 90 L 68 97 L 54 97 Z", FILLED),
        path("M 50 12 C 72 12 84 30 84 54 C 84 78 70 90 50 90 "
             "C 30 90 16 78 16 54 C 16 30 28 12 50 12 Z", FILLED),
        path("M 30 20 L 24 10 L 38 16"),
        path("M 70 20 L 76 10 L 62 16"),
        circle(37, 42, 12, FILLED), circle(63, 42, 12, FILLED),
        dot(37, 42, 4.6), dot(63, 42, 4.6),
        circle(37, 42, 15), circle(63, 42, 15),
        line(48, 42, 52, 42),
        path("M 22 40 L 16 36"), path("M 78 40 L 84 36"),
        path("M 50 50 L 56 57 L 44 57 Z", FILLED),
        path("M 20 60 C 22 70 24 76 28 82"),
        path("M 80 60 C 78 70 76 76 72 82"),
        path("M 28 72 C 34 66 44 66 50 70 C 56 66 66 66 72 72 "
             "L 72 88 C 66 82 56 82 50 86 C 44 82 34 82 28 88 Z", FILLED),
        line(50, 70, 50, 86),
    ])


@hero("transport")
def happy_car():
    """A little car with a face in the windscreen."""
    return "".join([
        path("M 10 62 L 14 46 C 16 38 24 34 36 34 L 64 34 "
             "C 76 34 84 38 88 46 L 92 62 C 92 70 88 72 80 72 "
             "L 20 72 C 12 72 8 70 10 62 Z", FILLED),
        path("M 28 34 L 32 18 L 68 18 L 72 34", FILLED),
        line(50, 18, 50, 34),
        circle(28, 78, 13, FILLED), circle(72, 78, 13, FILLED),
        circle(28, 78, 5, FILLED), circle(72, 78, 5, FILLED),
        dot(38, 52, 4), dot(62, 52, 4),
        arc(50, 56, 9, 20, 160),
        ellipse(22, 60, 5, 3.4, 0, FILLED),
        ellipse(78, 60, 5, 3.4, 0, FILLED),
    ])


@hero("camping")
def bear_with_marshmallow():
    """A bear toasting a marshmallow on a stick."""
    return "".join([
        feet(50, 90, 13, 9, 5.6),
        arms(50, 64, 19, 8, 5.4, 5.8),
        ellipse(50, 68, 20, 19, 0, FILLED),
        belly(50, 72, 11, 10),
        round_ears(50, 26, 16, 15, 8),
        circle(50, 36, 19, FILLED),
        face(50, 33, 15, 3.1, 7),
        snout(50, 43, 8, 5.5, 2.6),
        line(66, 74, 92, 44),
        rect(84, 30, 16, 14, 5, FILLED),
        path("M 86 44 C 90 48 96 48 98 44"),
    ])


@hero("birthday")
def fox_with_cupcake():
    """A fox in a party hat holding a cupcake."""
    return "".join([
        path("M 74 80 C 92 78 96 60 86 52 C 80 48 74 54 78 60"),
        feet(50, 90, 13, 8.5, 5.2),
        arms(50, 66, 18, 8, 5, 5.4),
        ellipse(50, 68, 19, 18, 0, FILLED),
        belly(50, 72, 10, 9),
        path("M 30 32 L 22 12 L 44 24 Z", FILLED),
        path("M 70 32 L 78 12 L 56 24 Z", FILLED),
        circle(50, 36, 18, FILLED),
        face(50, 32, 14, 3.1, 0),
        path("M 50 40 C 44 40 40 46 44 50 C 48 53 52 53 56 50 "
             "C 60 46 56 40 50 40 Z", FILLED),
        dot(50, 44, 3),
        path("M 50 10 L 42 24 L 58 24 Z", FILLED),
        circle(50, 7, 4, FILLED),
        path("M 40 76 L 60 76 L 57 90 L 43 90 Z", FILLED),
        path("M 38 76 C 38 66 46 62 50 66 C 54 62 62 66 62 76 Z", FILLED),
        circle(50, 60, 3.4, FILLED),
    ])


@hero("bugs")
def ladybug_with_leaf():
    """A ladybug with spots, holding a leaf."""
    return "".join([
        line(22, 62, 10, 58), line(22, 70, 10, 72), line(24, 78, 12, 86),
        line(78, 62, 90, 58), line(78, 70, 90, 72), line(76, 78, 88, 86),
        ellipse(50, 64, 28, 26, 0, FILLED),
        line(50, 38, 50, 90),
        circle(36, 58, 6, FILLED), circle(64, 58, 6, FILLED),
        circle(38, 76, 5, FILLED), circle(62, 76, 5, FILLED),
        path("M 50 16 C 66 16 76 26 76 38 C 64 42 36 42 24 38 "
             "C 24 26 34 16 50 16 Z", FILLED),
        face(50, 28, 14, 3.1, 6.5, blush=False),
        line(40, 16, 34, 6), line(60, 16, 66, 6),
        dot(33, 4, 3.4), dot(67, 4, 3.4),
        path("M 88 84 C 96 76 96 64 90 58 C 82 62 78 74 82 86 Z", FILLED),
        line(86, 84, 90, 62),
    ])


@hero("food")
def strawberry_friend():
    """A strawberry with a leafy crown and a big smile."""
    seeds = "".join(dot(x, y, 2.4) for x, y in
                    ((24, 74), (76, 74), (34, 84), (66, 84), (50, 88)))
    leaves = "".join(
        ellipse(*pt(50, 36, 15, a), 11, 6, a, FILLED)
        for a in (196, 232, 270, 308, 344)
    )
    return "".join([
        feet(50, 92, 12, 8, 5),
        arms(50, 62, 21, 8, 5, 5.4),
        path("M 50 32 C 74 32 86 48 82 66 C 78 84 64 93 50 93 "
             "C 36 93 22 84 18 66 C 14 48 26 32 50 32 Z", FILLED),
        leaves,
        line(50, 22, 50, 14),
        face(50, 56, 16, 3.2, 7.5),
        seeds,
    ])
