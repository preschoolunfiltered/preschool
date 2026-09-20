"""Pet and treat doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("dog")
def dog():
    return "".join([
        ellipse(18, 46, 11, 20, 10, FILLED),
        ellipse(82, 46, 11, 20, -10, FILLED),
        circle(50, 48, 28, FILLED),
        dot(40, 42, 3.2), dot(60, 42, 3.2),
        ellipse(50, 62, 16, 12, 0, FILLED),
        ellipse(50, 56, 6, 5, 0, SOLID),
        path("M 50 61 C 46 68 40 68 38 64"),
        path("M 50 61 C 54 68 60 68 62 64"),
        path("M 50 68 L 50 74"),
    ])


@icon("cat")
def cat():
    return "".join([
        path("M 50 24 C 66 24 78 36 78 52 C 78 68 66 80 50 80 "
             "C 34 80 22 68 22 52 C 22 36 34 24 50 24 Z", FILLED),
        path("M 26 32 L 22 12 L 42 24 Z", FILLED),
        path("M 74 32 L 78 12 L 58 24 Z", FILLED),
        dot(40 , 46, 3.2), dot(60, 46, 3.2),
        poly([(50, 54), (55, 58), (45, 58)], True, SOLID),
        path("M 50 60 C 46 66 40 66 38 62"),
        path("M 50 60 C 54 66 60 66 62 62"),
        line(20, 50, 6, 46), line(20, 56, 6, 58),
        line(80, 50, 94, 46), line(80, 56, 94, 58),
    ])


@icon("fish_bowl")
def fish_bowl():
    return "".join([
        path("M 14 48 C 14 30 30 20 50 20 C 70 20 86 30 86 48 "
             "C 86 68 70 82 50 82 C 30 82 14 68 14 48 Z", FILLED),
        path("M 18 38 C 30 46 70 46 82 38"),
        path("M 56 58 C 56 50 48 46 40 50 C 32 54 32 62 40 66 "
             "C 48 70 56 66 56 58 Z", FILLED),
        path("M 56 58 L 68 50 L 68 66 Z", FILLED),
        dot(42, 55, 2.4),
        circle(62, 34, 4, FILLED), circle(70, 28, 3, FILLED),
    ])


@icon("bird_cage")
def bird_cage():
    out = [
        path("M 24 78 C 24 40 30 26 50 26 C 70 26 76 40 76 78 Z", FILLED),
        rect(20, 78, 60, 8, 3, FILLED),
        path("M 44 26 C 44 16 56 16 56 26"),
        line(50, 16, 50, 10),
    ]
    for x in (36, 50, 64):
        out.append(path(f"M {x} 28 C {x - (x - 50) * 0.3} 50 "
                        f"{x - (x - 50) * 0.6} 64 {x - (x - 50) * 0.9} 78"))
    out.append(line(26, 50, 74, 50))
    return "".join(out)


@icon("ball_of_yarn")
def ball_of_yarn():
    return "".join([
        circle(48, 54, 30, FILLED),
        path("M 24 38 C 40 46 56 62 62 80"),
        path("M 36 26 C 46 44 58 56 76 64"),
        path("M 20 60 C 38 56 56 44 64 28"),
        path("M 30 74 C 44 70 62 58 72 40"),
        path("M 78 54 C 88 52 94 60 90 68 C 86 76 92 82 96 80"),
    ])


@icon("hamster")
def hamster():
    return "".join([
        circle(28, 34, 11, FILLED), circle(72, 34, 11, FILLED),
        path("M 50 24 C 70 24 82 38 82 54 C 82 72 68 84 50 84 "
             "C 32 84 18 72 18 54 C 18 38 30 24 50 24 Z", FILLED),
        dot(40, 48, 3.2), dot(60, 48, 3.2),
        ellipse(50, 62, 13, 9, 0, FILLED),
        dot(50, 59, 3),
        path("M 50 63 C 47 68 43 68 41 65"),
        path("M 50 63 C 53 68 57 68 59 65"),
        line(22, 56, 8, 52), line(78, 56, 92, 52),
    ])


@icon("pet_bowl")
def pet_bowl():
    return "".join([
        path("M 20 52 L 80 52 L 72 78 C 72 82 28 82 28 78 Z", FILLED),
        ellipse(50, 52, 30, 9, 0, FILLED),
        circle(40, 46, 7, FILLED), circle(58, 44, 7, FILLED),
        line(24, 66, 76, 66),
    ])


@icon("dog_house")
def dog_house():
    return "".join([
        path("M 50 14 L 88 46 L 80 46 L 80 84 L 20 84 L 20 46 L 12 46 Z",
             FILLED),
        path("M 38 84 L 38 62 C 38 52 62 52 62 62 L 62 84 Z", FILLED),
        line(50, 30, 50, 22),
        dot(50, 20, 3.4),
    ])


@icon("collar")
def collar():
    return "".join([
        circle(50, 46, 30, FILLED),
        circle(50, 46, 22, FILLED),
        rect(42, 12, 16, 10, 2, FILLED),
        path("M 44 76 C 44 88 56 88 56 76 Z", FILLED),
        heart(50, 84, 9, FILLED),
    ])


@icon("mouse")
def mouse():
    return "".join([
        circle(26, 40, 15, FILLED), circle(74, 40, 15, FILLED),
        path("M 50 30 C 68 30 80 44 80 60 C 80 76 66 86 50 86 "
             "C 34 86 20 76 20 60 C 20 44 32 30 50 30 Z", FILLED),
        dot(41, 54, 3), dot(59, 54, 3),
        dot(50, 66, 3.6),
        line(22, 66, 8, 62), line(78, 66, 92, 62),
        path("M 80 74 C 92 76 96 86 88 90"),
    ])
