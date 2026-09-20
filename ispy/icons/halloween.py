"""Halloween doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("jack_o_lantern")
def jack_o_lantern():
    return "".join([
        ellipse(50, 58, 34, 28, 0, FILLED),
        path("M 36 32 C 28 42 28 74 36 84"),
        path("M 64 32 C 72 42 72 74 64 84"),
        path("M 50 30 L 50 16"),
        poly([(36, 50), (46, 50), (41, 40)], True, SOLID),
        poly([(64, 50), (54, 50), (59, 40)], True, SOLID),
        path("M 32 62 L 40 62 L 44 68 L 56 68 L 60 62 L 68 62 "
             "L 64 76 L 36 76 Z", SOLID),
    ])


@icon("ghost")
def ghost():
    return "".join([
        path("M 22 82 L 22 48 C 22 28 34 16 50 16 C 66 16 78 28 78 48 "
             "L 78 82 C 72 74 66 86 58 80 C 52 76 48 86 42 80 "
             "C 34 74 28 88 22 82 Z", FILLED),
        dot(40, 44, 4), dot(62, 44, 4),
        ellipse(51, 58, 6, 8, 0, FILLED),
    ])


@icon("bat")
def bat():
    return "".join([
        ellipse(50, 52, 14, 18, 0, FILLED),
        path("M 38 42 C 26 28 14 26 6 32 C 14 34 14 44 8 50 "
             "C 18 50 22 58 20 68 C 28 60 34 58 40 62 Z", FILLED),
        path("M 62 42 C 74 28 86 26 94 32 C 86 34 86 44 92 50 "
             "C 82 50 78 58 80 68 C 72 60 66 58 60 62 Z", FILLED),
        path("M 40 38 L 38 24 L 46 32"), path("M 60 38 L 62 24 L 54 32"),
        dot(44, 46, 2.6), dot(56, 46, 2.6),
        arc(50, 52, 5, 20, 160),
    ])


@icon("spider")
def spider():
    out = [circle(50, 58, 20, FILLED), circle(50, 36, 12, FILLED),
           dot(45, 34, 2.6), dot(55, 34, 2.6)]
    for i, y in enumerate((48, 58, 68)):
        out.append(path(f"M 31 {y} C 18 {y - 6} 12 {y + 4} 10 {y + 14}"))
        out.append(path(f"M 69 {y} C 82 {y - 6} 88 {y + 4} 90 {y + 14}"))
    out.append(line(50, 24, 50, 14))
    return "".join(out)


@icon("spider_web")
def spider_web():
    out = [line(6, 6, 6, 92), line(6, 6, 92, 6)]
    for i in range(5):
        a = 90 - i * 22.5
        x, y = pt(6, 6, 92, -a + 90)
        out.append(line(6, 6, x, y))
    for r in (28, 48, 68, 88):
        out.append(path(f"M 6 {6 + r} C {6 + r * 0.42} {6 + r * 0.82} "
                        f"{6 + r * 0.82} {6 + r * 0.42} {6 + r} 6"))
    return "".join(out)


@icon("candy_corn")
def candy_corn():
    return "".join([
        path("M 50 10 C 60 28 74 68 78 84 C 66 90 34 90 22 84 "
             "C 26 68 40 28 50 10 Z", FILLED),
        path("M 33 46 C 44 42 56 42 67 46"),
        path("M 26 68 C 40 62 60 62 74 68"),
    ])


@icon("witch_hat")
def witch_hat():
    return "".join([
        path("M 50 8 C 58 24 66 44 72 62 C 60 68 40 68 28 62 "
             "C 34 44 42 24 50 8 Z", FILLED),
        ellipse(50, 70, 42, 12, 0, FILLED),
        path("M 31 56 C 42 62 58 62 69 56 L 72 64 C 58 70 42 70 28 64 Z",
             FILLED),
        rect(44, 56, 12, 10, 2, FILLED),
        star(72, 26, 8, 5, 0.42, -90),
    ])


@icon("cauldron")
def cauldron():
    return "".join([
        path("M 16 44 C 16 72 30 84 50 84 C 70 84 84 72 84 44 Z", FILLED),
        rect(10, 36, 80, 10, 5, FILLED),
        line(30, 84, 26, 92), line(70, 84, 74, 92),
        path("M 28 36 C 34 24 40 20 44 18"),
        circle(56, 22, 6, FILLED), circle(70, 14, 5, FILLED),
    ])


@icon("black_cat")
def black_cat():
    return "".join([
        path("M 50 26 C 66 26 76 38 76 52 C 76 68 64 78 50 78 "
             "C 36 78 24 68 24 52 C 24 38 34 26 50 26 Z", FILLED),
        path("M 28 34 L 24 14 L 42 26"), path("M 72 34 L 76 14 L 58 26"),
        ellipse(40, 48, 5, 7, 0, SOLID), ellipse(60, 48, 5, 7, 0, SOLID),
        poly([(50, 56), (55, 60), (45, 60)], True, SOLID),
        path("M 50 62 C 46 68 40 68 38 64"),
        path("M 50 62 C 54 68 60 68 62 64"),
        line(22, 52, 6, 48), line(22, 58, 6, 60),
        line(78, 52, 94, 48), line(78, 58, 94, 60),
        path("M 70 76 C 84 82 88 92 80 94"),
    ])


@icon("skull")
def skull():
    return "".join([
        path("M 50 12 C 72 12 84 28 84 46 C 84 58 78 64 72 68 L 72 78 "
             "C 72 82 66 84 50 84 C 34 84 28 82 28 78 L 28 68 "
             "C 22 64 16 58 16 46 C 16 28 28 12 50 12 Z", FILLED),
        ellipse(37, 44, 10, 11, 0, SOLID),
        ellipse(63, 44, 10, 11, 0, SOLID),
        poly([(50, 54), (55, 64), (45, 64)], True, SOLID),
        line(38, 70, 38, 82), line(50, 70, 50, 84), line(62, 70, 62, 82),
        line(30, 70, 70, 70),
    ])


@icon("broom")
def broom():
    out = [
        line(50, 8, 50, 54),
        path("M 38 54 L 62 54 L 72 86 C 72 90 28 90 28 86 Z", FILLED),
        rect(36, 50, 28, 9, 3, FILLED),
    ]
    for x0, x1 in ((44, 38), (50, 50), (56, 62), (41, 33), (59, 67)):
        out.append(line(x0, 60, x1, 86))
    return "".join(out)


@icon("wrapped_candy")
def wrapped_candy():
    return "".join([
        ellipse(50, 50, 22, 18, 0, FILLED),
        path("M 30 42 L 12 30 L 16 50 L 10 68 L 30 58 Z", FILLED),
        path("M 70 42 L 88 30 L 84 50 L 90 68 L 70 58 Z", FILLED),
        path("M 42 42 C 46 48 46 54 42 58"),
        path("M 56 42 C 60 48 60 54 56 58"),
    ])


@icon("tombstone")
def tombstone():
    return "".join([
        path("M 24 84 L 24 42 C 24 22 76 22 76 42 L 76 84 Z", FILLED),
        line(38, 46, 62, 46), line(50, 40, 50, 62),
        line(36, 62, 64, 62),
        path("M 10 86 C 20 80 26 90 36 86 C 46 82 54 90 64 86 "
             "C 74 82 82 90 92 86"),
    ])


@icon("crescent_moon")
def crescent_moon():
    return "".join([
        path("M 62 12 C 40 16 26 34 26 54 C 26 74 42 90 62 90 "
             "C 50 80 44 68 44 52 C 44 34 52 20 62 12 Z", FILLED),
        star(76, 26, 9, 5, 0.42, -90, FILLED),
        star(80, 62, 6, 5, 0.42, -90, FILLED),
    ])


@icon("mummy")
def mummy():
    out = [path("M 50 12 C 68 12 78 26 78 46 L 78 76 C 78 86 66 90 50 90 "
                "C 34 90 22 86 22 76 L 22 46 C 22 26 32 12 50 12 Z", FILLED)]
    for i, y in enumerate((24, 36, 60, 72, 84)):
        d = 6 if i % 2 else -6
        out.append(path(f"M 22 {y} C 40 {y + d} 60 {y - d} 78 {y}"))
    out.append(dot(40, 48, 3.4))
    out.append(dot(60, 48, 3.4))
    out.append(path("M 22 48 C 34 54 44 44 52 52"))
    return "".join(out)


@icon("potion_bottle")
def potion_bottle():
    return "".join([
        path("M 40 22 L 60 22 L 60 40 C 74 48 80 60 80 70 "
             "C 80 82 70 88 50 88 C 30 88 20 82 20 70 "
             "C 20 60 26 48 40 40 Z", FILLED),
        rect(38, 12, 24, 10, 3, FILLED),
        path("M 24 64 C 38 72 62 56 76 64"),
        dot(38, 74, 3), dot(56, 78, 3.4), dot(66, 70, 2.6),
    ])
