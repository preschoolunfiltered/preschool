"""Easter doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("easter_egg_stripes")
def easter_egg_stripes():
    return "".join([
        path("M 50 10 C 68 24 78 46 78 60 C 78 78 66 90 50 90 "
             "C 34 90 22 78 22 60 C 22 46 32 24 50 10 Z", FILLED),
        path("M 25 44 C 36 52 64 36 76 46"),
        path("M 22 60 C 34 68 66 52 78 62"),
        path("M 26 76 C 36 84 64 68 74 78"),
    ])


@icon("easter_egg_dots")
def easter_egg_dots():
    return "".join([
        path("M 50 10 C 68 24 78 46 78 60 C 78 78 66 90 50 90 "
             "C 34 90 22 78 22 60 C 22 46 32 24 50 10 Z", FILLED),
        dot(50, 30, 4), dot(34, 48, 4), dot(66, 48, 4),
        dot(50, 58, 4), dot(34, 72, 4), dot(66, 72, 4),
        zigzag(24, 62, 76, 62, 6, 0),
    ])


@icon("hatching_egg")
def hatching_egg():
    return "".join([
        path("M 26 60 C 26 46 34 26 50 18 C 66 26 74 46 74 60 "
             "L 66 54 L 58 60 L 50 54 L 42 60 L 34 54 Z", FILLED),
        path("M 26 64 L 34 58 L 42 64 L 50 58 L 58 64 L 66 58 L 74 64 "
             "C 74 80 64 90 50 90 C 36 90 26 80 26 64 Z", FILLED),
        dot(42, 40, 2.6), dot(58, 40, 2.6),
        poly([(50, 44), (56, 48), (44, 48)], True, FILLED),
    ])


@icon("bunny")
def bunny():
    return "".join([
        ellipse(38, 26, 9, 22, -10, FILLED),
        ellipse(62, 26, 9, 22, 10, FILLED),
        circle(50, 58, 26, FILLED),
        dot(41, 54, 3), dot(59, 54, 3),
        poly([(50, 62), (56, 66), (44, 66)], True, FILLED),
        path("M 50 68 C 46 74 40 74 38 70"),
        path("M 50 68 C 54 74 60 74 62 70"),
        line(24, 58, 12, 54), line(24, 64, 12, 66),
        line(76, 58, 88, 54), line(76, 64, 88, 66),
    ])


@icon("easter_basket")
def easter_basket():
    out = [circle(34, 46, 11, FILLED), circle(52, 42, 11, FILLED),
           circle(68, 48, 11, FILLED),
           path("M 18 52 L 82 52 L 74 84 C 74 87 26 87 26 84 Z", FILLED),
           path("M 26 52 C 26 22 74 22 74 52")]
    for x in (34, 50, 66):
        out.append(line(x, 54, x - 4, 85))
    out.append(line(20, 66, 80, 66))
    return "".join(out)


@icon("carrot")
def carrot():
    return "".join([
        path("M 36 40 L 64 40 L 52 90 C 51 93 49 93 48 90 Z", FILLED),
        line(40, 52, 58, 52), line(43, 64, 55, 64),
        path("M 44 40 C 36 32 34 20 38 12 C 46 18 48 30 48 40"),
        path("M 56 40 C 64 32 68 22 66 14 C 58 18 54 30 52 40"),
        path("M 50 38 C 50 28 54 18 60 12"),
    ])


@icon("lamb")
def lamb():
    return "".join([
        blob(44, 52, 28, n=12, wobble=0.10, extra=FILLED),
        ellipse(76, 46, 15, 13, 0, FILLED),
        ellipse(64, 44, 10, 5, 20, FILLED),
        ellipse(89, 42, 10, 5, -20, FILLED),
        dot(72, 44, 2.6), dot(84, 44, 2.6),
        path("M 74 52 C 78 56 82 54 82 50"),
        line(32, 78, 30, 92), line(50, 80, 50, 92),
    ])


@icon("jelly_bean")
def jelly_bean():
    return "".join([
        path("M 28 34 C 46 26 66 30 74 42 C 84 56 76 72 58 74 "
             "C 40 76 22 66 20 52 C 19 44 22 37 28 34 Z", FILLED),
        path("M 34 42 C 42 38 52 38 58 42"),
    ])
