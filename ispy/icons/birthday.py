"""Birthday party doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("birthday_cake")
def birthday_cake():
    return "".join([
        path("M 18 52 L 82 52 L 78 84 C 78 88 22 88 22 84 Z", FILLED),
        path("M 20 62 C 32 70 44 56 56 64 C 66 70 74 60 81 64"),
        rect(24, 44, 52, 8, 3, FILLED),
        line(36, 44, 36, 28), line(50, 44, 50, 24), line(64, 44, 64, 28),
        path("M 36 28 C 32 22 40 18 36 12 C 44 16 42 24 36 28 Z", FILLED),
        path("M 50 24 C 46 18 54 14 50 8 C 58 12 56 20 50 24 Z", FILLED),
        path("M 64 28 C 60 22 68 18 64 12 C 72 16 70 24 64 28 Z", FILLED),
    ])


@icon("party_hat")
def party_hat():
    return "".join([
        path("M 50 12 L 76 78 L 24 78 Z", FILLED),
        circle(50, 8, 7, FILLED),
        path("M 33 50 C 42 44 58 44 67 50"),
        path("M 28 66 C 40 58 60 58 72 66"),
        path("M 20 82 C 30 76 38 86 50 82 C 62 78 70 86 80 82"),
    ])


@icon("balloon")
def balloon():
    return "".join([
        path("M 50 10 C 68 10 80 26 80 44 C 80 62 66 72 50 72 "
             "C 34 72 20 62 20 44 C 20 26 32 10 50 10 Z", FILLED),
        path("M 44 72 L 50 64 L 56 72 Z", FILLED),
        path("M 50 72 C 58 80 42 86 50 94"),
        path("M 34 30 C 34 24 38 20 42 18"),
    ])


@icon("candle")
def candle():
    return "".join([
        rect(38, 34, 24, 54, 4, FILLED),
        line(38, 48, 62, 48), line(38, 62, 62, 62),
        line(50, 34, 50, 26),
        path("M 50 6 C 60 16 62 24 58 30 C 54 36 46 36 42 30 "
             "C 38 24 40 16 50 6 Z", FILLED),
    ])


@icon("confetti")
def confetti():
    return "".join([
        rect(16, 18, 12, 7, 2, FILLED),
        rect(64, 12, 12, 7, 2, FILLED),
        star(80, 44, 11, 5, 0.42, -90, FILLED),
        circle(28, 52, 8, FILLED),
        rect(44, 68, 12, 7, 2, FILLED),
        circle(70, 78, 7, FILLED),
        path("M 12 76 C 18 70 24 82 30 76"),
        path("M 44 34 C 50 28 56 40 62 34"),
    ])


@icon("bunting")
def bunting():
    out = [path("M 4 20 C 26 44 42 44 52 32 C 62 20 78 24 96 44")]
    pts = ((16, 34), (30, 42), (44, 38), (58, 28), (74, 30), (88, 38))
    for x, y in pts:
        out.append(path(f"M {x - 9} {y} L {x + 9} {y} L {x} {y + 20} Z", FILLED))
    return "".join(out)


@icon("donut")
def donut():
    out = [circle(50, 52, 34, FILLED), circle(50, 52, 12, FILLED),
           path("M 18 46 C 24 58 30 40 38 52 C 44 62 54 42 62 54 "
                "C 68 62 76 46 82 54")]
    for x, y, a in ((34, 30, 30), (62, 28, -20), (24, 64, 10),
                    (74, 68, 40), (50, 80, -30), (78, 44, 70)):
        out.append(group(rect(-6, -2, 12, 4, 2, FILLED),
                         f"translate({x} {y}) rotate({a})"))
    return "".join(out)


@icon("party_popper")
def party_popper():
    return "".join([
        path("M 12 88 L 36 40 L 58 62 Z", FILLED),
        line(24, 64, 42, 60),
        star(72, 26, 10, 5, 0.42, -90, FILLED),
        circle(84, 50, 6, FILLED),
        rect(56, 14, 11, 6, 2, FILLED),
        path("M 60 40 C 68 36 72 40 76 38"),
        path("M 50 26 C 54 20 60 24 64 20"),
    ])


@icon("gift_bag")
def gift_bag():
    return "".join([
        path("M 24 34 L 76 34 L 72 86 L 28 86 Z", FILLED),
        path("M 38 34 C 38 20 62 20 62 34"),
        line(24, 44, 76, 44),
        heart(50, 62, 13, FILLED),
    ])
