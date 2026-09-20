"""Classroom and back-to-school doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("pencil")
def pencil():
    return "".join([
        path("M 38 20 L 62 20 L 62 70 L 50 88 L 38 70 Z", FILLED),
        rect(36, 10, 28, 10, 3, FILLED),
        line(38, 26, 62, 26),
        line(38, 70, 62, 70),
        path("M 44 78 L 56 78"),
        line(50, 26, 50, 70),
    ])


@icon("crayon")
def crayon():
    return "".join([
        path("M 38 34 L 62 34 L 62 84 C 62 88 38 88 38 84 Z", FILLED),
        path("M 50 10 L 62 34 L 38 34 Z", FILLED),
        line(38, 46, 62, 46), line(38, 72, 62, 72),
        line(44, 52, 44, 66), line(56, 52, 56, 66),
    ])


@icon("book")
def book():
    return "".join([
        path("M 16 24 C 30 18 44 20 50 26 C 56 20 70 18 84 24 "
             "L 84 78 C 70 72 56 74 50 80 C 44 74 30 72 16 78 Z", FILLED),
        line(50, 26, 50, 80),
        path("M 24 34 C 32 31 40 32 44 34"),
        path("M 24 46 C 32 43 40 44 44 46"),
        path("M 56 34 C 60 32 68 31 76 34"),
        path("M 56 46 C 60 44 68 43 76 46"),
    ])


@icon("backpack")
def backpack():
    return "".join([
        path("M 22 44 C 22 30 34 22 50 22 C 66 22 78 30 78 44 L 78 84 "
             "C 78 88 22 88 22 84 Z", FILLED),
        path("M 34 44 C 34 32 66 32 66 44"),
        path("M 22 52 C 34 58 66 58 78 52"),
        rect(36, 64, 28, 16, 3, FILLED),
        line(44, 44, 44, 52), line(56, 44, 56, 52),
    ])


@icon("ruler")
def ruler():
    out = [rect(20, 38, 62, 24, 3, FILLED)]
    for i in range(1, 6):
        x = 20 + i * 10
        out.append(line(x, 38, x, 48 if i % 2 else 52))
    out.append(line(24, 58, 78, 58))
    return "".join(out)


@icon("scissors")
def scissors():
    return "".join([
        line(26, 16, 62, 62), line(74, 16, 38, 62),
        circle(30, 74, 12, FILLED), circle(70, 74, 12, FILLED),
        line(62, 62, 66, 64), line(38, 62, 34, 64),
        dot(50, 44, 3),
    ])


@icon("glue_stick")
def glue_stick():
    return "".join([
        rect(34, 30, 32, 56, 4, FILLED),
        rect(30, 14, 40, 16, 4, FILLED),
        line(34, 44, 66, 44), line(34, 70, 66, 70),
        dot(50, 57, 4),
    ])


@icon("notebook")
def notebook():
    out = [rect(24, 16, 54, 68, 4, FILLED), line(38, 16, 38, 84)]
    for y in (30, 42, 54, 66):
        out.append(line(46, y, 70, y))
    for y in (24, 38, 52, 66, 78):
        out.append(path(f"M 34 {y} C 24 {y - 4} 20 {y + 4} 30 {y + 2}"))
    return "".join(out)


@icon("globe")
def globe():
    return "".join([
        circle(50, 44, 32, FILLED),
        ellipse(50, 44, 14, 32, 0),
        line(18, 44, 82, 44),
        path("M 24 28 C 38 34 62 34 76 28"),
        path("M 24 60 C 38 54 62 54 76 60"),
        path("M 40 76 L 40 84 L 60 84 L 60 76"),
        rect(32, 84, 36, 8, 3, FILLED),
    ])


@icon("school_bus")
def school_bus():
    return "".join([
        path("M 10 34 L 72 34 L 88 50 L 88 70 L 10 70 Z", FILLED),
        rect(18, 42, 14, 14, 2, FILLED),
        rect(38, 42, 14, 14, 2, FILLED),
        rect(58, 42, 14, 14, 2, FILLED),
        circle(28, 74, 10, FILLED), circle(70, 74, 10, FILLED),
        line(10, 62, 88, 62),
    ])


@icon("abc_block")
def abc_block():
    return "".join([
        rect(22, 26, 56, 56, 6, FILLED),
        path("M 38 66 L 50 38 L 62 66"),
        line(43, 56, 57, 56),
        line(22, 34, 78, 34),
    ])


@icon("paint_palette")
def paint_palette():
    return "".join([
        path("M 46 18 C 74 18 92 34 90 54 C 88 70 74 78 64 72 "
             "C 56 68 48 72 48 80 C 48 88 38 90 30 84 "
             "C 16 74 10 56 16 40 C 22 26 34 18 46 18 Z", FILLED),
        circle(38, 34, 7, FILLED), circle(62, 32, 7, FILLED),
        circle(74, 50, 7, FILLED), circle(30, 54, 7, FILLED),
    ])


@icon("chalkboard")
def chalkboard():
    return "".join([
        rect(12, 14, 76, 52, 4, FILLED),
        rect(20, 22, 60, 36, 2, FILLED),
        path("M 28 34 C 36 28 44 40 52 34"),
        line(28, 46, 58, 46),
        rect(8, 66, 84, 9, 3, FILLED),
        rect(62, 68, 14, 5, 2, FILLED),
        line(22, 75, 16, 92), line(78, 75, 84, 92),
    ])


@icon("paperclip")
def paperclip():
    return "".join([
        path("M 34 30 L 34 68 C 34 82 66 82 66 68 L 66 24 "
             "C 66 14 44 14 44 24 L 44 66 C 44 74 56 74 56 66 L 56 32"),
    ])


@icon("lunchbox")
def lunchbox():
    return "".join([
        rect(16, 34, 68, 50, 6, FILLED),
        path("M 38 34 C 38 22 62 22 62 34"),
        line(16, 52, 84, 52),
        rect(42, 46, 16, 12, 2, FILLED),
        line(24, 64, 40, 64), line(24, 72, 36, 72),
    ])
