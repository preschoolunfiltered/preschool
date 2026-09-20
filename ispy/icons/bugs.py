"""Bug and minibeast doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("ant")
def ant():
    return "".join([
        circle(74, 52, 15, FILLED),
        ellipse(50, 52, 12, 11, 0, FILLED),
        ellipse(24, 52, 16, 13, 0, FILLED),
        dot(20, 48, 2.6),
        line(14, 44, 6, 34), line(20, 40, 16, 28),
        dot(5, 32, 2.4), dot(15, 26, 2.4),
        path("M 44 44 C 40 32 34 26 28 22"),
        path("M 50 42 C 50 30 52 24 54 18"),
        path("M 58 44 C 64 34 70 28 76 24"),
        path("M 44 62 C 40 74 34 80 28 84"),
        path("M 50 64 C 50 76 52 82 54 88"),
        path("M 58 62 C 64 72 70 78 76 82"),
    ])


@icon("caterpillar")
def caterpillar():
    out = [circle(20, 66, 13, FILLED), circle(40, 60, 13, FILLED),
           circle(60, 54, 13, FILLED), circle(78, 44, 15, FILLED),
           dot(80, 40, 2.6),
           line(74, 30, 68, 18), line(84, 30, 90, 18),
           dot(67, 16, 2.4), dot(91, 16, 2.4)]
    for x, y in ((16, 78), (36, 72), (56, 66)):
        out.append(line(x, y, x - 4, 88))
    return "".join(out)


@icon("dragonfly")
def dragonfly():
    return "".join([
        ellipse(50, 60, 7, 30, 0, FILLED),
        circle(50, 24, 12, FILLED),
        dot(45, 21, 2.6), dot(55, 21, 2.6),
        ellipse(26, 44, 22, 8, -18, FILLED),
        ellipse(74, 44, 22, 8, 18, FILLED),
        ellipse(28, 60, 18, 7, 12, FILLED),
        ellipse(72, 60, 18, 7, -12, FILLED),
        line(44, 14, 38, 6), line(56, 14, 62, 6),
    ])


@icon("grasshopper")
def grasshopper():
    return "".join([
        path("M 16 62 C 22 48 40 42 58 44 C 74 46 84 54 84 62 "
             "C 84 70 72 74 56 74 C 36 74 20 70 16 62 Z", FILLED),
        circle(82, 56, 13, FILLED),
        dot(86, 52, 2.6),
        line(84, 44, 90, 32), line(76, 46, 74, 32),
        path("M 46 72 C 40 82 30 86 22 84"),
        path("M 62 72 C 60 84 66 90 74 90"),
        path("M 40 46 C 46 38 56 36 62 38"),
    ])


@icon("beetle")
def beetle():
    return "".join([
        ellipse(50, 56, 26, 30, 0, FILLED),
        line(50, 26, 50, 86),
        path("M 30 34 C 38 26 62 26 70 34"),
        circle(50, 22, 12, FILLED),
        line(43, 12, 36, 4), line(57, 12, 64, 4),
        dot(35, 3, 2.4), dot(65, 3, 2.4),
        line(24, 44, 12, 38), line(22, 58, 8, 58), line(24, 72, 12, 80),
        line(76, 44, 88, 38), line(78, 58, 92, 58), line(76, 72, 88, 80),
    ])


@icon("firefly")
def firefly():
    return "".join([
        ellipse(46, 58, 20, 14, -8, FILLED),
        line(34, 54, 58, 60),
        circle(24, 42, 11, FILLED),
        dot(20, 39, 2.4),
        line(18, 33, 12, 22), line(28, 32, 30, 20),
        ellipse(42, 34, 18, 8, -18, FILLED),
        ellipse(60, 40, 16, 7, 8, FILLED),
        circle(72, 70, 11, SOLID),
        line(84, 62, 92, 58), line(86, 74, 96, 76), line(78, 84, 82, 92),
    ])


@icon("moth")
def moth():
    return "".join([
        ellipse(50, 52, 8, 26, 0, FILLED),
        path("M 44 34 C 26 22 8 32 12 48 C 16 62 34 60 44 50 Z", FILLED),
        path("M 56 34 C 74 22 92 32 88 48 C 84 62 66 60 56 50 Z", FILLED),
        path("M 44 56 C 30 60 22 74 32 80 C 42 84 46 70 46 62 Z", FILLED),
        path("M 56 56 C 70 60 78 74 68 80 C 58 84 54 70 54 62 Z", FILLED),
        path("M 46 30 C 42 20 34 14 26 14"),
        path("M 54 30 C 58 20 66 14 74 14"),
        dot(30, 42, 3), dot(70, 42, 3),
    ])


@icon("honeycomb")
def honeycomb():
    def hexa(cx, cy, r):
        return poly([pt(cx, cy, r, 90 + i * 60) for i in range(6)], True, FILLED)
    return "".join([
        hexa(50, 30, 17), hexa(30, 62, 17), hexa(70, 62, 17),
        dot(50, 30, 4), dot(70, 62, 4),
    ])


@icon("magnifying_glass")
def magnifying_glass():
    return "".join([
        circle(44, 40, 28, FILLED),
        circle(44, 40, 21, FILLED),
        path("M 62 62 L 84 86"),
        path("M 58 58 L 80 82"),
        path("M 34 30 C 30 34 28 38 28 42"),
    ])
