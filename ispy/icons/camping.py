"""Camping and outdoors doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("tent")
def tent():
    return "".join([
        path("M 50 14 L 88 82 L 12 82 Z", FILLED),
        path("M 50 14 L 62 82 L 38 82 Z", FILLED),
        path("M 44 82 C 46 60 48 44 50 30"),
        path("M 56 82 C 54 60 52 44 50 30"),
        line(6, 82, 94, 82),
        line(50, 14, 50, 6),
    ])


@icon("campfire")
def campfire():
    return "".join([
        path("M 50 16 C 60 30 66 40 66 52 C 66 66 58 76 50 76 "
             "C 42 76 34 66 34 52 C 34 40 40 30 50 16 Z", FILLED),
        path("M 50 42 C 56 50 58 56 58 62 C 58 70 54 76 50 76 "
             "C 46 76 42 70 42 62 C 42 56 44 50 50 42 Z", FILLED),
        path("M 14 80 L 86 88"), path("M 14 88 L 86 80"),
        path("M 20 84 L 80 84"),
    ])


@icon("marshmallow_stick")
def marshmallow_stick():
    return "".join([
        line(8, 82, 70, 34),
        rect(62, 22, 22, 18, 5, FILLED),
        path("M 64 40 C 70 44 78 44 82 40"),
        path("M 30 66 C 34 62 38 64 40 60"),
    ])


@icon("compass")
def compass():
    return "".join([
        circle(50, 50, 34, FILLED),
        circle(50, 50, 26, FILLED),
        poly([(50, 28), (58, 50), (50, 44)], True, SOLID),
        poly([(50, 72), (42, 50), (50, 56)], True, FILLED),
        line(50, 12, 50, 18), line(50, 82, 50, 88),
        line(12, 50, 18, 50), line(82, 50, 88, 50),
    ])


@icon("lantern")
def lantern():
    return "".join([
        path("M 30 32 L 70 32 L 74 70 L 26 70 Z", FILLED),
        rect(34, 24, 32, 8, 3, FILLED),
        path("M 42 24 C 42 12 58 12 58 24"),
        rect(22, 70, 56, 10, 3, FILLED),
        path("M 42 42 C 46 50 54 50 58 42 C 60 52 58 60 50 62 "
             "C 42 60 40 52 42 42 Z", FILLED),
    ])


@icon("canoe")
def canoe():
    return "".join([
        line(30, 26, 66, 56),
        path("M 26 18 C 18 26 22 34 32 32 Z", FILLED),
        path("M 4 46 L 22 58 C 36 62 64 62 78 58 L 96 46 "
             "C 92 72 74 84 50 84 C 26 84 8 72 4 46 Z", FILLED),
        path("M 14 58 C 30 66 70 66 86 58"),
        line(36, 62, 34, 74), line(64, 62, 66, 74),
    ])


@icon("fishing_rod")
def fishing_rod():
    return "".join([
        line(14, 84, 74, 22),
        circle(28, 68, 7, FILLED),
        path("M 74 22 C 78 40 80 56 80 64"),
        path("M 80 64 C 72 64 68 70 70 76 C 72 82 82 84 88 78 "
             "C 92 74 92 68 88 64 Z", FILLED),
        dot(84, 70, 2.4),
    ])


@icon("binoculars")
def binoculars():
    return "".join([
        rect(14, 34, 28, 48, 10, FILLED),
        rect(58, 34, 28, 48, 10, FILLED),
        rect(18, 22, 20, 14, 4, FILLED),
        rect(62, 22, 20, 14, 4, FILLED),
        rect(40, 42, 20, 12, 3, FILLED),
        circle(28, 70, 8, FILLED), circle(72, 70, 8, FILLED),
        line(16, 58, 40, 58), line(60, 58, 84, 58),
    ])


@icon("map")
def map_icon():
    return "".join([
        path("M 10 28 L 36 20 L 64 32 L 90 22 L 90 74 L 64 84 "
             "L 36 72 L 10 80 Z", FILLED),
        line(36, 20, 36, 72), line(64, 32, 64, 84),
        path("M 20 62 C 30 50 44 56 52 44"),
        dot(22, 64, 3.2),
        poly([(54, 40), (58, 48), (50, 48)], True, SOLID),
    ])


@icon("flashlight")
def flashlight():
    return "".join([
        path("M 30 26 L 52 38 L 52 66 L 30 78 Z", FILLED),
        rect(52, 40, 32, 24, 5, FILLED),
        line(62, 40, 62, 64),
        rect(66, 46, 10, 6, 2, FILLED),
        path("M 24 34 L 10 26"), path("M 22 52 L 6 52"),
        path("M 24 70 L 10 78"),
    ])


@icon("mountain")
def mountain():
    return "".join([
        path("M 6 80 L 34 30 L 52 60 L 62 44 L 94 80 Z", FILLED),
        path("M 26 44 L 34 38 L 42 44 L 34 50 Z", FILLED),
        path("M 58 50 L 62 47 L 68 54 L 62 56 Z", FILLED),
        line(6, 80, 94, 80),
    ])


@icon("bear")
def bear():
    return "".join([
        circle(24, 28, 12, FILLED), circle(76, 28, 12, FILLED),
        circle(50, 52, 30, FILLED),
        dot(40, 46, 3.2), dot(60, 46, 3.2),
        ellipse(50, 64, 17, 13, 0, FILLED),
        ellipse(50, 58, 7, 5, 0, SOLID),
        path("M 50 63 C 46 70 40 70 38 66"),
        path("M 50 63 C 54 70 60 70 62 66"),
    ])


@icon("smore")
def smore():
    return "".join([
        rect(18, 26, 64, 16, 3, FILLED),
        rect(18, 56, 64, 18, 3, FILLED),
        path("M 22 42 C 30 50 40 46 50 50 C 60 54 72 48 78 56 L 78 42 Z",
             FILLED),
        dot(30, 32, 2.6), dot(50, 34, 2.6), dot(70, 32, 2.6),
        dot(34, 66, 2.6), dot(58, 66, 2.6),
    ])


@icon("log")
def log():
    return "".join([
        path("M 26 30 L 74 30 C 84 30 84 74 74 74 L 26 74 Z", FILLED),
        ellipse(26, 52, 10, 22, 0, FILLED),
        ellipse(26, 52, 5, 11, 0, FILLED),
        line(40, 32, 44, 72), line(58, 30, 62, 74),
    ])
