"""Things that go."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("car")
def car():
    return "".join([
        path("M 12 62 L 16 48 C 18 42 24 38 34 38 L 66 38 "
             "C 76 38 82 42 86 48 L 88 62 Z", FILLED),
        path("M 30 38 L 34 22 L 66 22 L 70 38", FILLED),
        line(50, 22, 50, 38),
        circle(28, 66, 11, FILLED), circle(72, 66, 11, FILLED),
        line(12, 56, 88, 56),
        dot(18, 52, 2.6), dot(82, 52, 2.6),
    ])


@icon("train")
def train():
    return "".join([
        path("M 14 36 L 44 36 L 44 70 L 14 70 Z", FILLED),
        path("M 44 50 L 86 50 L 86 70 L 44 70 Z", FILLED),
        rect(20, 42, 18, 14, 2, FILLED),
        rect(54, 30, 12, 20, 2, FILLED),
        circle(26, 76, 9, FILLED), circle(56, 76, 9, FILLED),
        circle(78, 76, 9, FILLED),
        line(44, 62, 86, 62),
        circle(68, 22, 7, FILLED), circle(80, 12, 5, FILLED),
    ])


@icon("airplane")
def airplane():
    return "".join([
        path("M 8 54 C 8 46 18 40 34 40 L 70 40 C 84 40 92 46 92 52 "
             "C 92 58 84 62 70 62 L 34 62 C 18 62 8 60 8 54 Z", FILLED),
        path("M 34 40 L 46 18 L 58 18 L 54 40", FILLED),
        path("M 34 62 L 44 80 L 54 80 L 52 62", FILLED),
        path("M 12 42 L 24 42 L 20 54", FILLED),
        dot(80, 50, 2.6), dot(70, 50, 2.6), dot(60, 50, 2.6),
    ])


@icon("bicycle")
def bicycle():
    return "".join([
        circle(24, 64, 18, FILLED), circle(76, 64, 18, FILLED),
        circle(24, 64, 4, FILLED), circle(76, 64, 4, FILLED),
        path("M 24 64 L 44 64 L 58 36 L 66 36"),
        path("M 44 64 L 58 36"), path("M 76 64 L 62 36"),
        path("M 38 36 L 50 36"), line(44, 36, 44, 64),
        path("M 62 32 C 66 28 72 28 74 32"),
    ])


@icon("dump_truck")
def dump_truck():
    return "".join([
        path("M 52 30 L 92 30 L 88 60 L 52 60 Z", FILLED),
        path("M 14 42 L 48 42 L 48 62 L 10 62 L 10 48 Z", FILLED),
        rect(18, 46, 14, 12, 2, FILLED),
        circle(24, 70, 11, FILLED), circle(70, 70, 11, FILLED),
        line(10, 62, 92, 62),
    ])


@icon("helicopter")
def helicopter():
    return "".join([
        path("M 22 54 C 22 40 34 32 50 32 C 64 32 74 40 78 50 "
             "L 92 54 L 92 62 L 30 62 C 24 62 22 58 22 54 Z", FILLED),
        rect(34, 38, 16, 12, 2, FILLED),
        line(50, 32, 50, 22),
        path("M 16 22 L 84 22"),
        path("M 88 50 L 96 42 M 88 58 L 96 66"),
        path("M 26 70 L 74 70"),
        line(34, 62, 32, 70), line(62, 62, 64, 70),
    ])


@icon("hot_air_balloon")
def hot_air_balloon():
    return "".join([
        path("M 50 10 C 70 10 84 26 84 44 C 84 58 70 66 50 66 "
             "C 30 66 16 58 16 44 C 16 26 30 10 50 10 Z", FILLED),
        path("M 50 10 C 40 24 38 50 44 66"),
        path("M 50 10 C 60 24 62 50 56 66"),
        line(38, 66, 42, 78), line(62, 66, 58, 78),
        rect(38, 78, 24, 14, 3, FILLED),
    ])


@icon("fire_truck")
def fire_truck():
    return "".join([
        path("M 10 44 L 62 44 L 62 66 L 10 66 Z", FILLED),
        path("M 62 50 L 88 50 L 88 66 L 62 66 Z", FILLED),
        rect(68, 54, 14, 10, 2, FILLED),
        circle(26, 70, 10, FILLED), circle(72, 70, 10, FILLED),
        path("M 16 40 L 62 24"), path("M 16 34 L 62 18"),
        line(24, 38, 26, 30), line(40, 34, 42, 26), line(56, 30, 58, 22),
        circle(36, 38, 5, FILLED),
    ])


@icon("scooter")
def scooter():
    return "".join([
        circle(20, 72, 12, FILLED), circle(80, 72, 12, FILLED),
        path("M 20 72 L 56 72 L 74 36"),
        path("M 74 36 L 62 30"), path("M 74 36 L 86 30"),
        path("M 56 72 L 80 72"),
        line(66, 52, 78, 58),
    ])


@icon("traffic_light")
def traffic_light():
    return "".join([
        rect(30, 10, 40, 62, 8, FILLED),
        circle(50, 24, 9, FILLED),
        circle(50, 41, 9, FILLED),
        circle(50, 58, 9, SOLID),
        line(50, 72, 50, 92),
        line(38, 92, 62, 92),
    ])


@icon("skateboard")
def skateboard():
    return "".join([
        path("M 8 48 C 14 40 22 44 30 46 L 70 46 C 78 44 86 40 92 48 "
             "C 88 58 78 58 70 56 L 30 56 C 22 58 12 58 8 48 Z", FILLED),
        line(28, 58, 28, 66), line(72, 58, 72, 66),
        circle(24, 72, 7, FILLED), circle(76, 72, 7, FILLED),
    ])
