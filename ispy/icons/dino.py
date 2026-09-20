"""Dinosaur doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("t_rex")
def t_rex():
    return "".join([
        path("M 74 20 C 86 20 92 28 92 36 C 92 42 86 46 78 46 "
             "L 62 46 C 58 56 50 62 40 64 C 30 66 22 74 22 84 "
             "L 10 84 C 10 66 22 54 34 50 C 42 47 46 40 46 32 "
             "C 46 24 54 20 62 20 Z", FILLED),
        path("M 46 54 C 42 62 44 70 50 74"),
        path("M 34 64 C 36 74 36 82 34 90"),
        path("M 52 70 C 58 76 60 84 58 90"),
        dot(72, 30, 3),
        line(76, 40, 92, 40),
        line(80, 40, 80, 44), line(86, 40, 86, 44),
    ])


@icon("stegosaurus")
def stegosaurus():
    out = [
        path("M 12 62 C 14 50 22 44 34 44 C 44 44 54 40 62 34 "
             "C 70 28 82 30 86 38 C 90 46 84 54 76 56 "
             "C 60 60 40 66 30 74 C 24 78 16 72 12 62 Z", FILLED),
        dot(80, 40, 2.8),
        line(30, 68, 28, 84), line(48, 64, 48, 84),
        line(64, 58, 66, 80),
    ]
    for x, y in ((28, 44), (42, 42), (56, 36)):
        out.append(path(f"M {x - 7} {y + 2} L {x} {y - 14} L {x + 7} {y + 2} Z",
                        FILLED))
    return "".join(out)


@icon("brontosaurus")
def brontosaurus():
    return "".join([
        tube([(60, 60), (70, 50), (78, 36), (80, 22)], 8, FILLED),
        tube([(36, 64), (22, 72), (10, 78), (2, 80)], 8, FILLED),
        tube([(30, 66), (28, 92)], 7, FILLED),
        tube([(46, 68), (46, 94)], 7, FILLED),
        tube([(60, 68), (62, 92)], 7, FILLED),
        ellipse(44, 60, 28, 19, 0, FILLED),
        ellipse(82, 18, 12, 10, -20, FILLED),
        dot(84, 15, 2.6),
    ])


@icon("triceratops")
def triceratops():
    return "".join([
        path("M 20 70 C 14 60 18 48 30 44 C 42 40 52 42 60 36 "
             "C 66 30 74 30 78 36 C 84 44 80 56 70 60 "
             "C 56 66 40 70 32 78 C 26 82 22 78 20 70 Z", FILLED),
        path("M 58 38 C 56 28 60 20 70 18 C 80 16 88 22 88 32 "
             "C 88 40 84 44 78 46", FILLED),
        line(64, 24, 60, 12), line(78, 20, 78, 10),
        dot(70, 40, 2.8),
        line(30, 74, 28, 88), line(48, 68, 48, 86),
    ])


@icon("pterodactyl")
def pterodactyl():
    return "".join([
        path("M 50 42 C 36 30 18 26 6 30 C 18 36 26 46 30 56 "
             "C 38 50 46 48 52 50 Z", FILLED),
        path("M 52 42 C 64 28 82 24 94 28 C 82 36 74 46 70 58 "
             "C 62 50 56 48 50 50 Z", FILLED),
        ellipse(50, 54, 14, 10, 0, FILLED),
        path("M 62 50 L 84 56 L 62 60", FILLED),
        path("M 44 46 L 34 34 L 48 40", FILLED),
        dot(58, 50, 2.6),
        path("M 44 62 C 42 74 44 84 48 90"),
    ])


@icon("dino_egg")
def dino_egg():
    return "".join([
        path("M 50 12 C 70 26 80 48 80 62 C 80 80 68 90 50 90 "
             "C 32 90 20 80 20 62 C 20 48 30 26 50 12 Z", FILLED),
        zigzag(22, 56, 78, 56, 8, 6),
        dot(40, 36, 3.4), dot(62, 40, 3.4), dot(50, 74, 3.4), dot(66, 72, 3),
    ])


@icon("volcano")
def volcano():
    return "".join([
        path("M 8 86 L 34 34 L 66 34 L 92 86 Z", FILLED),
        path("M 34 34 C 38 26 34 18 38 10 C 44 18 48 12 50 6 "
             "C 54 14 58 12 62 8 C 64 18 62 26 66 34", FILLED),
        path("M 30 40 C 26 50 22 56 18 62"),
        path("M 70 40 C 74 50 78 56 82 62"),
        line(20, 86, 80, 86),
    ])


@icon("fern")
def fern():
    out = [path("M 46 92 C 44 68 46 42 56 16")]
    for i in range(8):
        t = i / 7
        x = 46 + 10 * t * t
        y = 88 - 70 * t
        r = 13 - 8 * t
        out.append(leaf(x - r - 1, y - r * 0.5, r, rot=-55 - 10 * t, vein=False))
        out.append(leaf(x + r + 1, y - r * 0.5, r, rot=55 + 10 * t, vein=False))
    return "".join(out)


@icon("dino_footprint")
def dino_footprint():
    return "".join([
        path("M 50 84 C 34 84 26 74 26 62 C 26 50 32 42 34 34 "
             "C 36 26 44 24 46 32 L 48 44 L 52 44 L 54 32 "
             "C 56 24 64 26 66 34 C 68 42 74 50 74 62 "
             "C 74 74 66 84 50 84 Z", FILLED),
        path("M 34 34 C 30 26 32 18 38 16"),
        path("M 66 34 C 70 26 68 18 62 16"),
    ])


@icon("bone")
def bone():
    return "".join([
        path("M 24 34 C 12 28 4 36 10 45 C 4 54 12 62 24 56 "
             "L 76 64 C 88 70 96 62 90 53 C 96 44 88 36 76 42 Z", FILLED),
    ])


@icon("fossil_skull")
def fossil_skull():
    return "".join([
        path("M 8 50 L 32 44 C 38 30 54 26 70 30 C 84 34 90 46 86 58 "
             "C 82 68 68 74 52 72 L 12 62 Z", FILLED),
        circle(68, 44, 9, SOLID),
        dot(20, 50, 2.6),
        zigzag(14, 60, 50, 68, 7, 3),
        path("M 78 30 C 84 24 90 26 92 32"),
    ])


