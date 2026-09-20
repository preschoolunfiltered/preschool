"""Outer space doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("rocket")
def rocket():
    return "".join([
        path("M 50 8 C 64 22 70 44 70 62 L 30 62 C 30 44 36 22 50 8 Z",
             FILLED),
        circle(50, 34, 11, FILLED),
        path("M 30 48 L 18 66 L 30 62 Z", FILLED),
        path("M 70 48 L 82 66 L 70 62 Z", FILLED),
        path("M 38 62 L 62 62 L 58 72 L 42 72 Z", FILLED),
        path("M 44 74 C 46 82 48 88 50 94 C 52 88 54 82 56 74 Z", FILLED),
    ])


@icon("planet")
def planet():
    return "".join([
        circle(48, 48, 26, FILLED),
        ellipse(48, 52, 44, 11, -18),
        circle(40, 40, 6, FILLED), circle(58, 56, 5, FILLED),
        circle(38, 60, 4, FILLED),
    ])


@icon("star")
def star_icon():
    return star(50, 50, 38, 5, 0.45, -90, FILLED)


@icon("shooting_star")
def shooting_star():
    return "".join([
        star(64, 34, 24, 5, 0.45, -90, FILLED),
        path("M 40 46 C 28 52 18 58 10 66"),
        path("M 46 56 C 36 62 28 70 22 78"),
        path("M 34 38 C 26 40 18 44 12 48"),
    ])


@icon("astronaut")
def astronaut():
    return "".join([
        path("M 32 30 C 32 18 68 18 68 30 L 68 44 C 68 56 32 56 32 44 Z",
             FILLED),
        path("M 40 28 C 40 24 60 24 60 28 C 60 34 40 34 40 28 Z", FILLED),
        path("M 34 54 L 66 54 L 70 80 L 30 80 Z", FILLED),
        path("M 34 58 L 16 70 L 22 80", FILLED),
        path("M 66 58 L 84 70 L 78 80", FILLED),
        rect(32, 80, 14, 12, 3, FILLED),
        rect(54, 80, 14, 12, 3, FILLED),
        rect(42, 62, 16, 10, 2, FILLED),
    ])


@icon("ufo")
def ufo():
    return "".join([
        path("M 32 42 C 32 26 68 26 68 42 Z", FILLED),
        path("M 14 48 C 14 38 86 38 86 48 C 86 58 14 58 14 48 Z", FILLED),
        dot(28, 52, 3.4), dot(50, 55, 3.4), dot(72, 52, 3.4),
        path("M 34 58 L 22 86"), path("M 66 58 L 78 86"),
        path("M 30 86 L 70 86"),
    ])


@icon("moon_craters")
def moon_craters():
    return "".join([
        circle(50, 50, 34, FILLED),
        circle(38, 38, 8, FILLED), circle(62, 56, 10, FILLED),
        circle(42, 66, 6, FILLED), circle(66, 32, 5, FILLED),
    ])


@icon("satellite")
def satellite():
    return "".join([
        rect(40, 38, 20, 26, 4, FILLED),
        rect(10, 40, 26, 22, 3, FILLED),
        rect(64, 40, 26, 22, 3, FILLED),
        line(23, 40, 23, 62), line(77, 40, 77, 62),
        line(36, 50, 40, 50), line(60, 50, 64, 50),
        path("M 50 38 L 50 24"),
        path("M 38 18 C 44 12 56 12 62 18"),
        dot(50, 22, 3.4),
    ])


@icon("comet")
def comet():
    return "".join([
        path("M 46 40 C 26 46 12 60 4 84 C 28 78 46 66 58 54 Z", FILLED),
        circle(64, 36, 20, FILLED),
        circle(58, 30, 5, FILLED),
        circle(70, 42, 4, FILLED),
        path("M 30 34 C 22 36 14 40 8 44"),
        path("M 44 18 C 40 24 38 30 36 36"),
    ])


@icon("telescope")
def telescope():
    return "".join([
        path("M 20 62 L 66 30 L 78 50 L 32 82 Z", FILLED),
        line(40, 50, 52, 70),
        rect(14, 56, 14, 14, 3, FILLED),
        line(46, 74, 34, 92), line(46, 74, 58, 92),
        line(38, 84, 54, 84),
    ])


@icon("alien")
def alien():
    return "".join([
        path("M 50 20 C 70 20 82 34 82 52 C 82 72 68 86 50 86 "
             "C 32 86 18 72 18 52 C 18 34 30 20 50 20 Z", FILLED),
        ellipse(38, 50, 9, 12, 20, SOLID),
        ellipse(62, 50, 9, 12, -20, SOLID),
        arc(50, 64, 8, 20, 160),
        line(32, 24, 26, 10), line(68, 24, 74, 10),
        dot(25, 8, 3.2), dot(75, 8, 3.2),
    ])


@icon("space_helmet")
def space_helmet():
    return "".join([
        circle(50, 50, 32, FILLED),
        path("M 50 26 C 64 26 74 36 74 50 C 74 60 66 68 50 68 "
             "C 34 68 26 60 26 50 C 26 36 36 26 50 26 Z", FILLED),
        path("M 36 38 C 40 34 46 32 52 32"),
        rect(78, 42, 10, 16, 3, FILLED),
        rect(12, 42, 10, 16, 3, FILLED),
    ])
