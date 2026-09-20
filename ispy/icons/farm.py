"""Farm and barnyard doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("barn")
def barn():
    return "".join([
        path("M 16 46 L 50 22 L 84 46 L 84 84 L 16 84 Z", FILLED),
        path("M 16 46 L 22 36 L 50 16 L 78 36 L 84 46", FILLED),
        path("M 38 84 L 38 58 C 38 52 62 52 62 58 L 62 84 Z", FILLED),
        line(50, 54, 50, 84),
        line(40, 62, 60, 62),
        path("M 46 30 L 54 30 L 54 42 L 46 42 Z", FILLED),
    ])


@icon("cow")
def cow():
    return "".join([
        path("M 50 24 C 70 24 80 38 80 54 C 80 72 68 82 50 82 "
             "C 32 82 20 72 20 54 C 20 38 30 24 50 24 Z", FILLED),
        path("M 20 40 C 10 32 8 22 14 18 C 22 22 24 32 24 38"),
        path("M 80 40 C 90 32 92 22 86 18 C 78 22 76 32 76 38"),
        path("M 26 36 C 22 28 26 22 32 24"),
        path("M 74 36 C 78 28 74 22 68 24"),
        dot(40, 44, 3.2), dot(60, 44, 3.2),
        ellipse(50, 66, 18, 13, 0, FILLED),
        dot(44, 64, 3), dot(56, 64, 3),
        path("M 30 52 C 24 56 24 62 28 64"),
    ])


@icon("pig")
def pig():
    return "".join([
        path("M 50 26 C 70 26 82 40 82 56 C 82 74 68 84 50 84 "
             "C 32 84 18 74 18 56 C 18 40 30 26 50 26 Z", FILLED),
        path("M 28 34 L 20 16 L 40 26 Z", FILLED),
        path("M 72 34 L 80 16 L 60 26 Z", FILLED),
        dot(38, 48, 3.2), dot(62, 48, 3.2),
        ellipse(50, 66, 17, 13, 0, FILLED),
        ellipse(44, 66, 4, 5, 0, SOLID), ellipse(56, 66, 4, 5, 0, SOLID),
    ])


@icon("hen")
def hen():
    return "".join([
        path("M 34 56 C 34 38 48 28 62 30 C 76 32 84 46 82 60 "
             "C 80 76 64 84 50 82 C 38 80 34 70 34 56 Z", FILLED),
        path("M 50 52 C 62 46 74 52 78 62 C 68 70 54 64 50 52 Z"),
        poly([(34, 48), (20, 54), (34, 58)], True, FILLED),
        path("M 24 58 L 16 66 L 28 64", FILLED),
        dot(42, 46, 2.8),
        path("M 42 30 C 40 22 46 20 48 26 C 52 18 58 22 56 28"),
        line(52, 82, 50, 92), line(66, 80, 68, 90),
        line(44, 92, 56, 92), line(62, 90, 74, 90),
    ])


@icon("sheep")
def sheep():
    return "".join([
        blob(46, 50, 28, n=13, wobble=0.10, extra=FILLED),
        ellipse(76, 52, 14, 15, 0, FILLED),
        ellipse(66, 44, 10, 5, 25, FILLED),
        ellipse(88, 44, 10, 5, -25, FILLED),
        dot(71, 50, 2.6), dot(82, 50, 2.6),
        arc(76, 56, 5, 20, 160),
        line(32, 76, 30, 92), line(52, 78, 52, 92),
    ])


@icon("horse")
def horse():
    return "".join([
        path("M 50 24 C 64 24 72 36 72 52 C 72 70 62 84 50 84 "
             "C 38 84 28 70 28 52 C 28 36 36 24 50 24 Z", FILLED),
        path("M 32 34 L 26 14 L 44 26 Z", FILLED),
        path("M 68 34 L 74 14 L 56 26 Z", FILLED),
        path("M 30 40 C 20 34 18 22 24 14 C 28 22 34 26 38 28"),
        dot(40, 48, 3.2), dot(60, 48, 3.2),
        ellipse(50, 70, 16, 12, 0, FILLED),
        dot(44, 68, 2.6), dot(56, 68, 2.6),
        path("M 44 78 C 48 80 52 80 56 78"),
    ])


@icon("tractor")
def tractor():
    return "".join([
        path("M 34 40 L 62 40 L 62 60 L 20 60 L 20 48 Z", FILLED),
        rect(38, 26, 22, 14, 3, FILLED),
        circle(30, 68, 18, FILLED), circle(30, 68, 6, FILLED),
        circle(72, 72, 13, FILLED), circle(72, 72, 5, FILLED),
        line(62, 52, 86, 52), line(86, 52, 86, 62),
        line(22, 48, 34, 48),
    ])


@icon("duck")
def duck():
    return "".join([
        path("M 30 60 C 30 46 42 38 56 38 C 72 38 82 48 82 60 "
             "C 82 74 68 82 54 82 C 38 82 30 74 30 60 Z", FILLED),
        circle(38, 34, 15, FILLED),
        poly([(24, 34), (8, 38), (24, 42)], True, FILLED),
        dot(38, 30, 2.8),
        path("M 52 54 C 64 50 74 56 76 66 C 66 72 54 66 52 54 Z"),
        path("M 20 84 C 34 92 66 92 84 84"),
    ])


@icon("fence")
def fence():
    out = []
    for x in (16, 38, 60, 82):
        out.append(path(f"M {x - 6} 34 L {x} 26 L {x + 6} 34 L {x + 6} 84 "
                        f"L {x - 6} 84 Z", FILLED))
    out.append(line(8, 46, 92, 46))
    out.append(line(8, 66, 92, 66))
    return "".join(out)


@icon("milk_bottle")
def milk_bottle():
    return "".join([
        path("M 38 30 L 62 30 L 62 42 C 72 48 74 58 74 68 "
             "C 74 82 68 88 50 88 C 32 88 26 82 26 68 "
             "C 26 58 28 48 38 42 Z", FILLED),
        rect(36, 20, 28, 10, 3, FILLED),
        path("M 28 62 C 40 68 62 56 73 62"),
        circle(50, 76, 8, FILLED),
    ])


@icon("rooster")
def rooster():
    return "".join([
        path("M 36 58 C 36 42 48 32 60 34 C 74 36 80 50 78 64 "
             "C 76 78 62 84 50 82 C 40 80 36 70 36 58 Z", FILLED),
        path("M 78 56 C 88 46 94 34 92 22 C 84 30 76 40 74 50"),
        path("M 84 62 C 94 56 98 44 96 34 C 88 42 82 52 80 58"),
        poly([(36, 48), (22, 54), (36, 58)], True, FILLED),
        path("M 30 58 L 24 66 L 34 64", FILLED),
        dot(44, 46, 2.8),
        path("M 44 32 C 42 24 48 22 50 28 C 54 20 60 24 58 30"),
        line(54, 82, 52, 92), line(66, 80, 68, 90),
    ])


@icon("pitchfork")
def pitchfork():
    return "".join([
        line(50, 44, 50, 92),
        path("M 30 44 L 70 44"),
        path("M 30 44 C 28 30 28 20 30 10"),
        path("M 50 44 C 50 30 50 20 50 8"),
        path("M 70 44 C 72 30 72 20 70 10"),
        rect(44, 80, 12, 8, 3, FILLED),
    ])


@icon("silo")
def silo():
    return "".join([
        path("M 30 40 L 30 86 L 70 86 L 70 40 Z", FILLED),
        path("M 28 40 C 28 20 72 20 72 40 Z", FILLED),
        line(30, 54, 70, 54), line(30, 68, 70, 68),
        line(50, 14, 50, 22),
    ])


@icon("egg_basket")
def egg_basket():
    return "".join([
        ellipse(36, 50, 11, 14, -10, FILLED),
        ellipse(58, 48, 11, 14, 8, FILLED),
        path("M 20 56 L 80 56 L 72 84 C 72 87 28 87 28 84 Z", FILLED),
        line(28, 58, 24, 84), line(44, 58, 42, 86),
        line(60, 58, 60, 86), line(74, 58, 76, 84),
        line(22, 70, 78, 70),
    ])
