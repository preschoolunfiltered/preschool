"""Valentine's Day doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("heart")
def heart_icon():
    return heart(50, 50, 32, FILLED)


@icon("double_heart")
def double_heart():
    return heart(38, 38, 22, FILLED) + heart(64, 64, 18, FILLED)


@icon("love_letter")
def love_letter():
    return "".join([
        rect(14, 30, 72, 46, 4, FILLED),
        path("M 14 34 L 50 58 L 86 34"),
        heart(50, 58, 14, FILLED),
    ])


@icon("cupcake")
def cupcake():
    return "".join([
        path("M 26 52 L 74 52 L 68 86 C 68 89 32 89 32 86 Z", FILLED),
        line(38, 54, 34, 87), line(50, 54, 50, 88), line(62, 54, 66, 87),
        path("M 24 52 C 24 38 34 34 38 34 C 40 22 60 22 62 34 "
             "C 68 34 78 40 76 52 Z", FILLED),
        circle(50, 16, 7, FILLED),
        line(50, 23, 50, 28),
    ])


@icon("rose")
def rose():
    return "".join([
        circle(50, 34, 24, FILLED),
        spiral(50, 34, 4, 19, turns=1.8, start=120),
        line(50, 58, 50, 90),
        path("M 50 70 C 36 70 28 62 28 52 C 40 50 48 58 50 70 Z"),
        path("M 50 80 C 64 80 72 72 72 62 C 60 60 52 68 50 80 Z"),
        line(44, 60, 40, 56), line(58, 66, 62, 62),
    ])


@icon("teddy_bear")
def teddy_bear():
    return "".join([
        circle(28, 26, 12, FILLED), circle(72, 26, 12, FILLED),
        circle(50, 36, 26, FILLED),
        dot(41, 32, 3), dot(59, 32, 3),
        ellipse(50, 44, 12, 9, 0, FILLED),
        ellipse(50, 40, 5, 4, 0, SOLID),
        path("M 50 44 C 47 49 42 49 40 46"),
        path("M 50 44 C 53 49 58 49 60 46"),
        path("M 34 70 C 34 60 66 60 66 70 C 66 82 58 88 50 88 "
             "C 42 88 34 82 34 70 Z", FILLED),
        ellipse(26, 66, 9, 11, -20, FILLED),
        ellipse(74, 66, 9, 11, 20, FILLED),
        heart(50, 74, 8, FILLED),
    ])


@icon("chocolate_box")
def chocolate_box():
    return "".join([
        path("M 50 88 C 16 66 8 48 12 34 C 16 20 34 16 44 28 "
             "L 50 36 L 56 28 C 66 16 84 20 88 34 C 92 48 84 66 50 88 Z",
             FILLED),
        path("M 20 40 C 34 52 66 52 80 40"),
        line(50, 36, 50, 88),
        circle(34, 60, 6, FILLED), circle(66, 60, 6, FILLED),
    ])


@icon("cupid_arrow")
def cupid_arrow():
    return "".join([
        line(18, 78, 74, 26),
        path("M 18 78 L 16 62 L 30 66 Z", FILLED),
        path("M 18 78 L 34 80 L 30 66 Z", FILLED),
        heart(78, 22, 16, FILLED),
    ])


@icon("heart_balloon")
def heart_balloon():
    return "".join([
        heart(50, 34, 28, FILLED),
        path("M 50 60 L 46 68 L 54 68 Z", FILLED),
        path("M 50 68 C 58 76 42 82 50 92"),
    ])


@icon("lollipop")
def lollipop():
    return "".join([
        circle(50, 36, 26, FILLED),
        spiral(50, 36, 3, 22, turns=2.4, start=0),
        line(50, 62, 50, 92),
        path("M 50 72 C 42 66 36 72 42 78 C 46 82 50 76 50 72 Z", FILLED),
        path("M 50 72 C 58 66 64 72 58 78 C 54 82 50 76 50 72 Z", FILLED),
    ])


@icon("heart_banner")
def heart_banner():
    out = [path("M 4 20 C 24 44 40 44 50 30 C 60 16 78 20 96 40")]
    for x, y in ((20, 38), (35, 42), (50, 32), (66, 26), (84, 34)):
        out.append(heart(x, y + 12, 9, FILLED))
        out.append(line(x, y, x, y + 5))
    return "".join(out)


@icon("candy_hearts")
def candy_hearts():
    return "".join([
        heart(30, 36, 17, FILLED),
        heart(70, 40, 15, FILLED),
        heart(48, 70, 19, FILLED),
    ])
