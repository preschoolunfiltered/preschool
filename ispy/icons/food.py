"""Snack and lunchbox doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("pizza_slice")
def pizza_slice():
    return "".join([
        path("M 50 12 L 86 82 C 64 92 36 92 14 82 Z", FILLED),
        path("M 20 76 C 40 84 60 84 80 76"),
        circle(50, 48, 6, FILLED), circle(36, 66, 6, FILLED),
        circle(62, 68, 6, FILLED), circle(50, 30, 4, FILLED),
    ])


@icon("burger")
def burger():
    return "".join([
        path("M 14 42 C 14 24 32 14 50 14 C 68 14 86 24 86 42 Z", FILLED),
        path("M 12 46 C 24 54 76 54 88 46 C 80 40 20 40 12 46 Z", FILLED),
        rect(14, 54, 72, 10, 3, FILLED),
        path("M 14 66 C 14 82 30 88 50 88 C 70 88 86 82 86 66 Z", FILLED),
        dot(34, 28, 2.6), dot(52, 24, 2.6), dot(66, 32, 2.6),
    ])


@icon("hot_dog")
def hot_dog():
    return "".join([
        ellipse(50, 46, 34, 13, 0, FILLED),
        path("M 8 62 C 8 52 24 48 50 48 C 76 48 92 52 92 62 "
             "C 92 74 76 80 50 80 C 24 80 8 74 8 62 Z", FILLED),
        path("M 24 46 C 34 36 42 54 52 44 C 60 36 70 54 78 44"),
    ])


@icon("taco")
def taco():
    return "".join([
        path("M 12 46 C 20 30 30 40 38 28 C 46 18 54 34 62 26 "
             "C 70 18 80 32 88 44"),
        circle(32, 40, 7, FILLED), circle(64, 36, 7, FILLED),
        path("M 8 48 C 8 76 28 92 50 92 C 72 92 92 76 92 48 "
             "C 70 60 30 60 8 48 Z", FILLED),
        path("M 14 56 C 32 64 68 64 86 56"),
    ])


@icon("strawberry")
def strawberry():
    return "".join([
        path("M 50 32 C 72 32 84 46 80 62 C 76 78 62 90 50 90 "
             "C 38 90 24 78 20 62 C 16 46 28 32 50 32 Z", FILLED),
        path("M 34 30 L 50 36 L 66 30 L 58 42 L 42 42 Z", FILLED),
        line(50, 30, 50, 22),
        dot(38, 52, 2.6), dot(56, 50, 2.6), dot(46, 64, 2.6),
        dot(64, 62, 2.6), dot(54, 76, 2.6), dot(34, 70, 2.6),
    ])


@icon("grapes")
def grapes():
    out = []
    for cx, cy in ((50, 34), (36, 48), (64, 48), (50, 52),
                   (28, 64), (50, 70), (72, 64), (38, 80), (62, 80)):
        out.append(circle(cx, cy, 11, FILLED))
    out.append(path("M 50 24 C 54 14 62 10 70 12"))
    out.append(leaf(64, 16, 10, rot=40, vein=False))
    return "".join(out)


@icon("cheese")
def cheese():
    return "".join([
        path("M 10 44 L 78 22 L 90 40 L 90 72 L 10 72 Z", FILLED),
        path("M 10 44 L 90 40"),
        circle(30, 58, 8, FILLED), circle(58, 54, 7, FILLED),
        circle(76, 62, 6, FILLED),
    ])


@icon("broccoli")
def broccoli():
    return "".join([
        blob(34, 34, 18, n=10, wobble=0.12, extra=FILLED),
        blob(64, 32, 17, n=10, wobble=0.12, phase=30, extra=FILLED),
        blob(50, 48, 19, n=10, wobble=0.12, phase=60, extra=FILLED),
        path("M 38 60 C 36 74 38 84 44 90 L 60 90 C 64 80 64 70 62 58",
             FILLED),
        line(50, 64, 50, 86),
    ])
