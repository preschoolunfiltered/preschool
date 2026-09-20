"""Snow-day and winter doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group,
    heart, leaf, line, path, petal_flower, poly, pt, rect, rotated, spiral,
    star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("snowflake")
def snowflake():
    out = []
    for i in range(6):
        a = i * 60
        x1, y1 = pt(50, 50, 38, a)
        out.append(line(50, 50, x1, y1))
        bx, by = pt(50, 50, 24, a)
        for da in (-40, 40):
            ex, ey = pt(bx, by, 12, a + da)
            out.append(line(bx, by, ex, ey))
        cx, cy = pt(50, 50, 34, a)
        for da in (-40, 40):
            ex, ey = pt(cx, cy, 8, a + da)
            out.append(line(cx, cy, ex, ey))
    out.append(circle(50, 50, 5, FILLED))
    return "".join(out)


@icon("snowman")
def snowman():
    return "".join([
        circle(50, 72, 22, FILLED),
        circle(50, 40, 16, FILLED),
        path("M 30 24 L 70 24 L 70 14 C 70 8 30 8 30 14 Z", FILLED),
        line(26, 24, 74, 24),
        dot(44, 38, 2.8), dot(56, 38, 2.8),
        poly([(50, 42), (60, 46), (50, 48)], True, FILLED),
        path("M 34 54 C 44 60 56 60 66 54"),
        dot(50, 68, 3), dot(50, 80, 3),
        path("M 30 62 L 14 52 M 20 54 L 14 52 L 16 46"),
        path("M 70 62 L 86 52 M 80 54 L 86 52 L 84 46"),
    ])


@icon("mitten")
def mitten():
    return "".join([
        path("M 34 34 C 34 20 66 20 68 34 C 70 46 68 56 68 72 L 32 72 "
             "C 32 60 34 46 34 34 Z", FILLED),
        path("M 32 48 C 22 44 16 50 18 58 C 20 64 28 64 32 60"),
        rect(28, 72, 44, 14, 4, FILLED),
        line(30, 78, 70, 78),
    ])


@icon("beanie_hat")
def beanie_hat():
    return "".join([
        path("M 22 62 C 22 34 34 22 50 22 C 66 22 78 34 78 62 Z", FILLED),
        rect(16, 62, 68, 14, 6, FILLED),
        circle(50, 16, 9, FILLED),
        line(38, 28, 36, 62), line(50, 24, 50, 62), line(62, 28, 64, 62),
    ])


@icon("scarf")
def scarf():
    band = "".join([
        path("M 12 36 C 30 30 44 42 62 36 C 76 31 84 34 90 38 "
             "L 90 58 C 84 54 76 51 62 56 C 44 62 30 50 12 56 Z", FILLED),
        line(30, 37, 32, 57), line(50, 40, 52, 60), line(70, 35, 72, 55),
    ])
    fringe = "".join([
        line(12, 38, 4, 36), line(12, 46, 4, 46), line(12, 54, 4, 56),
        line(90, 40, 98, 38), line(90, 48, 98, 48), line(90, 56, 98, 58),
    ])
    return group(band + fringe, "rotate(-16 50 46)")


@icon("sled")
def sled():
    return "".join([
        path("M 16 52 L 76 52 L 72 64 L 20 64 Z", FILLED),
        line(24, 64, 24, 74), line(66, 64, 66, 74),
        path("M 14 74 L 80 74 C 88 74 90 64 84 60"),
        path("M 16 52 C 10 46 12 38 20 36"),
    ])


@icon("ice_skate")
def ice_skate():
    return "".join([
        path("M 32 18 L 58 18 C 58 36 62 52 74 58 L 74 68 L 32 68 Z", FILLED),
        line(32, 30, 58, 30), line(32, 42, 58, 42),
        path("M 24 74 L 80 74"),
        line(36, 68, 36, 74), line(66, 68, 66, 74),
        path("M 80 74 C 86 74 88 68 84 64"),
        path("M 24 74 C 18 74 18 80 24 80 L 80 80"),
    ])


@icon("penguin")
def penguin():
    return "".join([
        path("M 50 14 C 68 14 78 30 78 52 C 78 74 66 86 50 86 "
             "C 34 86 22 74 22 52 C 22 30 32 14 50 14 Z", FILLED),
        path("M 50 26 C 62 26 68 40 68 54 C 68 72 60 80 50 80 "
             "C 40 80 32 72 32 54 C 32 40 38 26 50 26 Z", FILLED),
        dot(42, 34, 2.8), dot(58, 34, 2.8),
        poly([(50, 38), (58, 44), (42, 44)], True, FILLED),
        path("M 22 46 C 14 56 14 68 20 74"),
        path("M 78 46 C 86 56 86 68 80 74"),
        path("M 36 86 L 28 92 L 44 92 Z", FILLED),
        path("M 64 86 L 72 92 L 56 92 Z", FILLED),
    ])


@icon("polar_bear")
def polar_bear():
    return "".join([
        circle(50, 54, 30, FILLED),
        circle(26, 26, 12, FILLED), circle(74, 26, 12, FILLED),
        dot(40, 48, 3.2), dot(60, 48, 3.2),
        ellipse(50, 66, 16, 12, 0, FILLED),
        ellipse(50, 60, 7, 5, 0, SOLID),
        path("M 50 66 C 46 72 40 72 38 68"),
        path("M 50 66 C 54 72 60 72 62 68"),
    ])


@icon("icicles")
def icicles():
    out = [line(10, 20, 90, 20)]
    for x, h in ((20, 34), (34, 52), (48, 30), (62, 46), (76, 36)):
        out.append(path(f"M {x - 7} 20 L {x} {20 + h} L {x + 7} 20", FILLED))
    return "".join(out)


@icon("earmuffs")
def earmuffs():
    return "".join([
        path("M 18 52 C 18 22 82 22 82 52"),
        ellipse(18, 60, 14, 16, 0, FILLED),
        ellipse(82, 60, 14, 16, 0, FILLED),
        ellipse(18, 60, 7, 9, 0),
        ellipse(82, 60, 7, 9, 0),
    ])


@icon("pine_tree")
def pine_tree():
    return "".join([
        rect(44, 78, 12, 12, 2, FILLED),
        path("M 50 10 L 68 36 L 32 36 Z", FILLED),
        path("M 50 26 L 74 56 L 26 56 Z", FILLED),
        path("M 50 44 L 80 78 L 20 78 Z", FILLED),
    ])


@icon("skis")
def skis():
    return "".join([
        path("M 22 88 C 22 62 22 40 24 32 C 26 22 36 22 37 30 "
             "C 38 42 37 64 37 88 Z", FILLED),
        path("M 44 88 C 44 62 44 40 46 32 C 48 22 58 22 59 30 "
             "C 60 42 59 64 59 88 Z", FILLED),
        line(20, 58, 61, 58),
        line(74, 26, 74, 88),
        path("M 66 74 L 82 74"),
        rect(70, 18, 9, 8, 3, FILLED),
    ])
