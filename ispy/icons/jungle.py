"""Jungle and safari doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("lion")
def lion():
    return "".join([
        blob(50, 52, 38, n=16, wobble=0.12, extra=FILLED),
        circle(50, 52, 24, FILLED),
        circle(30, 30, 9, FILLED), circle(70, 30, 9, FILLED),
        dot(42, 48, 3), dot(58, 48, 3),
        poly([(50, 56), (56, 60), (44, 60)], True, SOLID),
        path("M 50 62 C 46 68 40 68 38 64"),
        path("M 50 62 C 54 68 60 68 62 64"),
        line(26, 56, 16, 54), line(26, 62, 16, 64),
        line(74, 56, 84, 54), line(74, 62, 84, 64),
    ])


@icon("monkey")
def monkey():
    return "".join([
        circle(22, 48, 13, FILLED), circle(78, 48, 13, FILLED),
        circle(50, 46, 28, FILLED),
        path("M 50 46 C 66 46 72 56 72 64 C 72 74 62 80 50 80 "
             "C 38 80 28 74 28 64 C 28 56 34 46 50 46 Z", FILLED),
        dot(41, 42, 3.2), dot(59, 42, 3.2),
        dot(45, 60, 2.4), dot(55, 60, 2.4),
        arc(50, 66, 9, 20, 160),
        path("M 38 22 C 42 14 50 14 54 20"),
    ])


@icon("elephant")
def elephant():
    return "".join([
        blob(20, 46, 21, n=10, wobble=0.09, extra=FILLED),
        blob(80, 46, 21, n=10, wobble=0.09, phase=40, extra=FILLED),
        tube([(46, 66), (42, 78), (48, 90), (62, 88)], 9, FILLED),
        path("M 50 16 C 68 16 78 30 78 48 C 78 60 72 68 64 72 "
             "L 36 72 C 28 68 22 60 22 48 C 22 30 32 16 50 16 Z", FILLED),
        dot(38, 44, 3.2), dot(62, 44, 3.2),
        path("M 34 70 C 30 78 32 84 36 86"),
        path("M 64 70 C 68 78 66 84 62 86"),
    ])


@icon("giraffe")
def giraffe():
    return "".join([
        tube([(50, 92), (52, 70), (56, 52)], 13, FILLED),
        path("M 54 26 C 70 26 80 32 80 42 C 80 52 68 58 54 58 "
             "C 42 58 34 50 34 40 C 34 30 42 26 54 26 Z", FILLED),
        line(46, 26, 43, 12), line(62, 26, 65, 12),
        dot(42, 11, 3.6), dot(66, 11, 3.6),
        path("M 34 34 L 22 28 L 27 41 Z", FILLED),
        dot(50, 36, 2.8),
        dot(70, 46, 2.4), dot(76, 40, 2.2),
        circle(48, 62, 6, FILLED), circle(58, 78, 6, FILLED),
        circle(44, 82, 5, FILLED),
    ])


@icon("zebra")
def zebra():
    return "".join([
        path("M 50 22 C 64 22 72 34 72 50 C 72 68 62 82 50 82 "
             "C 38 82 28 68 28 50 C 28 34 36 22 50 22 Z", FILLED),
        path("M 32 32 L 26 12 L 44 24 Z", FILLED),
        path("M 68 32 L 74 12 L 56 24 Z", FILLED),
        path("M 34 34 C 42 38 42 44 40 48"),
        path("M 66 34 C 58 38 58 44 60 48"),
        path("M 30 52 C 38 54 40 58 40 62"),
        path("M 70 52 C 62 54 60 58 60 62"),
        dot(41, 44, 3), dot(59, 44, 3),
        ellipse(50, 68, 15, 11, 0, FILLED),
        dot(45, 66, 2.4), dot(55, 66, 2.4),
    ])


@icon("tiger")
def tiger():
    return "".join([
        circle(50, 52, 30, FILLED),
        circle(26, 28, 11, FILLED), circle(74, 28, 11, FILLED),
        path("M 42 26 C 44 32 44 38 42 42"),
        path("M 58 26 C 56 32 56 38 58 42"),
        path("M 24 48 C 30 50 34 52 36 54"),
        path("M 76 48 C 70 50 66 52 64 54"),
        dot(41, 48, 3), dot(59, 48, 3),
        poly([(50, 56), (56, 60), (44, 60)], True, SOLID),
        path("M 50 62 C 46 68 40 68 38 64"),
        path("M 50 62 C 54 68 60 68 62 64"),
        line(30, 62, 18, 60), line(70, 62, 82, 60),
    ])


@icon("snake")
def snake():
    return "".join([
        tube([(14, 84), (34, 80), (44, 66), (36, 52), (22, 44),
              (26, 30), (44, 24), (62, 28), (70, 38)], 9, FILLED),
        circle(74, 46, 12, FILLED),
        dot(70, 42, 2.6), dot(79, 44, 2.6),
        path("M 74 58 L 74 70 M 74 66 L 69 72 M 74 66 L 79 72"),
        dot(34, 74, 2.6), dot(30, 38, 2.6),
    ])


@icon("parrot")
def parrot():
    return "".join([
        path("M 52 70 C 66 76 80 86 90 94 C 78 92 62 86 50 80 Z", FILLED),
        path("M 58 66 C 72 70 84 78 92 86 C 80 86 64 80 54 74 Z", FILLED),
        ellipse(44, 54, 21, 26, 6, FILLED),
        circle(46, 26, 15, FILLED),
        path("M 58 22 C 70 22 74 32 68 38 C 62 42 56 38 56 30", FILLED),
        dot(42, 22, 2.8),
        path("M 40 48 C 54 46 62 54 62 66 C 50 70 40 62 40 48 Z"),
        line(40, 80, 38, 90), line(50, 80, 52, 90),
    ])


@icon("banana")
def banana():
    return "".join([
        path("M 20 24 C 16 46 26 70 50 78 C 70 84 84 76 88 66 "
             "C 76 70 60 66 48 54 C 36 42 32 30 32 22 Z", FILLED),
        path("M 20 24 L 16 16 L 30 18 L 32 22"),
        path("M 88 66 C 92 70 90 74 86 74"),
    ])


@icon("hippo")
def hippo():
    return "".join([
        circle(24, 26, 9, FILLED), circle(76, 26, 9, FILLED),
        path("M 50 20 C 70 20 82 32 82 48 C 82 68 68 82 50 82 "
             "C 32 82 18 68 18 48 C 18 32 30 20 50 20 Z", FILLED),
        dot(36, 38, 3), dot(64, 38, 3),
        ellipse(50, 62, 27, 17, 0, FILLED),
        ellipse(40, 56, 5, 6, 0, SOLID), ellipse(60, 56, 5, 6, 0, SOLID),
        path("M 38 68 C 44 74 56 74 62 68"),
        rect(42, 70, 6, 7, 1, FILLED), rect(52, 70, 6, 7, 1, FILLED),
    ])


@icon("crocodile")
def crocodile():
    return "".join([
        path("M 6 70 C 6 62 16 58 30 58 L 70 58 C 84 58 92 62 92 70 "
             "C 92 78 84 82 70 82 L 30 82 C 16 82 6 78 6 70 Z", FILLED),
        circle(30, 50, 11, FILLED), circle(52, 48, 11, FILLED),
        dot(30, 48, 3), dot(52, 46, 3),
        zigzag(66, 58, 92, 58, 6, 5),
        path("M 12 66 L 20 72 L 28 66 L 36 72 L 44 66"),
        line(20, 82, 18, 90), line(64, 82, 66, 90),
    ])


@icon("monstera_leaf")
def monstera_leaf():
    out = [
        path("M 50 10 C 74 18 86 40 84 58 C 82 76 68 86 50 88 "
             "C 32 86 18 76 16 58 C 14 40 26 18 50 10 Z", FILLED),
        line(50, 86, 50, 20),
    ]
    for y, w in ((32, 20), (48, 28), (64, 26), (77, 18)):
        out.append(path(f"M {50 + w} {y - 5} L {54} {y} L {50 + w} {y + 6}"))
        out.append(path(f"M {50 - w} {y - 5} L {46} {y} L {50 - w} {y + 6}"))
    return "".join(out)


@icon("paw_print")
def paw_print():
    return "".join([
        ellipse(28, 40, 9, 12, -18, FILLED),
        ellipse(44, 30, 9, 12, -6, FILLED),
        ellipse(62, 32, 9, 12, 8, FILLED),
        ellipse(76, 44, 9, 12, 20, FILLED),
        path("M 50 50 C 66 50 78 60 78 70 C 78 82 66 88 50 88 "
             "C 34 88 22 82 22 70 C 22 60 34 50 50 50 Z", FILLED),
    ])
