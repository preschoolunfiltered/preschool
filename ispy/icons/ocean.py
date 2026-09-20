"""Under-the-sea doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group,
    heart, leaf, line, path, petal_flower, poly, pt, rect, rotated, spiral,
    star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("fish")
def fish():
    return "".join([
        path("M 66 52 C 66 34 50 24 34 30 C 18 36 12 50 12 52 "
             "C 12 54 18 68 34 74 C 50 80 66 70 66 52 Z", FILLED),
        path("M 66 52 C 72 44 82 34 88 32 C 86 44 86 60 88 72 "
             "C 82 70 72 60 66 52 Z", FILLED),
        path("M 40 30 C 44 22 52 20 56 24"),
        path("M 34 74 C 36 82 42 84 46 80"),
        dot(26, 46, 3),
        path("M 48 36 C 44 46 44 58 48 68"),
    ])


@icon("whale")
def whale():
    return "".join([
        path("M 14 56 C 14 40 30 30 48 30 C 66 30 78 40 78 56 "
             "C 78 70 64 78 46 78 C 28 78 14 70 14 56 Z", FILLED),
        path("M 78 54 C 86 44 92 36 96 30 C 96 44 96 62 96 76 "
             "C 90 68 84 60 78 60"),
        path("M 18 66 C 34 74 60 74 74 66"),
        dot(32, 50, 3),
        arc(28, 56, 5, 10, 150),
        path("M 40 30 C 36 20 38 12 46 10"),
        path("M 40 30 C 46 20 54 16 60 18"),
    ])


@icon("dolphin")
def dolphin():
    return "".join([
        path("M 10 52 C 20 38 36 28 54 30 C 70 32 80 42 84 54 "
             "C 86 62 82 70 74 72 C 60 76 38 72 26 64 C 18 60 12 56 10 52 Z",
             FILLED),
        path("M 52 30 C 54 18 62 12 72 12 C 68 20 64 26 64 32"),
        path("M 84 56 C 90 50 96 44 98 38 C 98 52 98 66 100 78 "
             "C 92 72 84 66 78 68"),
        path("M 44 70 C 42 80 46 88 54 90 C 52 82 50 74 50 70"),
        dot(24, 48, 2.8),
        path("M 10 52 C 14 54 18 56 22 56"),
    ])


@icon("octopus")
def octopus():
    out = [
        path("M 22 52 C 22 30 36 18 50 18 C 64 18 78 30 78 52 L 78 62 "
             "C 60 70 40 70 22 62 Z", FILLED),
        dot(40, 44, 3), dot(60, 44, 3),
        arc(50, 50, 7, 20, 160),
    ]
    for i, x in enumerate([26, 38, 50, 62, 74]):
        d = 1 if i % 2 else -1
        out.append(path(
            f"M {x} 62 C {x + 6 * d} 72 {x - 6 * d} 78 {x + 4 * d} 88"))
    return "".join(out)


@icon("jellyfish")
def jellyfish():
    out = [
        path("M 20 54 C 20 32 34 20 50 20 C 66 20 80 32 80 54 "
             "C 70 62 30 62 20 54 Z", FILLED),
        dot(42, 44, 2.8), dot(58, 44, 2.8),
        arc(50, 48, 6, 20, 160),
    ]
    for x in [28, 40, 52, 64, 74]:
        out.append(path(f"M {x} 58 C {x + 7} 68 {x - 7} 76 {x + 4} 88"))
    return "".join(out)


@icon("sea_turtle")
def sea_turtle():
    return "".join([
        ellipse(50, 52, 30, 26, 0, FILLED),
        ellipse(50, 52, 15, 13, 0),
        line(50, 26, 50, 39), line(50, 65, 50, 78),
        line(20, 52, 35, 52), line(65, 52, 80, 52),
        path("M 74 30 C 84 22 92 28 90 38 C 88 46 80 46 76 40", FILLED),
        dot(86, 32, 2.4),
        path("M 26 28 C 16 24 10 32 16 40"),
        path("M 26 76 C 16 80 10 72 16 64"),
        path("M 74 76 C 84 80 90 72 84 64"),
    ])


@icon("seahorse")
def seahorse():
    return "".join([
        tube([(80, 22), (66, 20), (56, 26), (52, 38), (56, 50),
              (50, 62), (42, 70), (46, 80), (58, 80), (58, 70)], 9, FILLED),
        path("M 56 12 C 60 6 68 6 70 12 C 66 14 62 16 60 20"),
        path("M 46 32 C 38 28 32 32 32 40"),
        path("M 48 52 C 38 54 34 62 38 68"),
        dot(68, 22, 2.8),
    ])


@icon("crab")
def crab():
    out = [
        ellipse(50, 56, 28, 19, 0, FILLED),
        arc(50, 56, 13, 200, 340),
        dot(41, 48, 3), dot(59, 48, 3),
        line(41, 42, 37, 30), line(59, 42, 63, 30),
        path("M 24 50 C 12 48 6 38 12 30 C 18 34 16 42 24 42 "
             "C 18 38 22 28 28 30 C 34 32 32 46 24 50 Z", FILLED),
        path("M 76 50 C 88 48 94 38 88 30 C 82 34 84 42 76 42 "
             "C 82 38 78 28 72 30 C 66 32 68 46 76 50 Z", FILLED),
    ]
    for x, d in [(34, -1), (44, -1), (56, 1), (66, 1)]:
        out.append(path(f"M {x} 72 C {x + 4 * d} 82 {x + 9 * d} 86 {x + 15 * d} 86"))
    return "".join(out)


@icon("starfish")
def starfish():
    out = [star(50, 52, 36, 5, 0.46, -90, FILLED)]
    for x, y in [(50, 34), (38, 56), (62, 56), (44, 74), (58, 74)]:
        out.append(dot(x, y, 3))
    return "".join(out)


@icon("seashell")
def seashell():
    out = [path("M 50 84 C 20 84 12 58 22 38 C 32 18 68 18 78 38 "
                "C 88 58 80 84 50 84 Z", FILLED)]
    for a in (-40, -20, 0, 20, 40):
        x, y = pt(50, 82, 56, 270 + a)
        out.append(line(50, 82, x, y))
    out.append(arc(50, 82, 12, 200, 340))
    return "".join(out)


@icon("conch_shell")
def conch_shell():
    return "".join([
        path("M 74 30 C 86 44 84 70 66 80 C 48 90 24 82 18 66 "
             "C 30 72 44 70 50 60 C 56 50 52 38 62 30 C 66 26 70 26 74 30 Z",
             FILLED),
        spiral(66, 46, 3, 17, turns=1.6, start=150),
        line(30, 74, 40, 64), line(44, 78, 52, 68),
    ])


@icon("coral")
def coral():
    return "".join([
        path("M 50 88 C 46 74 46 60 48 44 C 49 36 52 32 56 30"),
        path("M 47 64 C 36 58 32 46 34 30"),
        path("M 48 52 C 58 46 64 38 68 24"),
        path("M 49 74 C 40 72 32 66 28 56"),
        path("M 50 80 C 60 76 66 70 70 62"),
        arc(50, 94, 22, 200, 340),
        line(34, 30, 34, 26), line(56, 30, 57, 25),
        line(68, 24, 69, 20), line(28, 56, 25, 53), line(70, 62, 73, 59),
    ])


@icon("anchor")
def anchor():
    return "".join([
        circle(50, 20, 9, FILLED),
        line(50, 29, 50, 82),
        line(32, 38, 68, 38),
        path("M 18 54 C 18 76 34 86 50 86 C 66 86 82 76 82 54"),
        line(18, 54, 10, 60), line(18, 54, 26, 60),
        line(82, 54, 74, 60), line(82, 54, 90, 60),
    ])


@icon("treasure_chest")
def treasure_chest():
    return "".join([
        path("M 16 46 C 16 28 84 28 84 46 Z", FILLED),
        rect(16, 46, 68, 34, 3, FILLED),
        line(16, 56, 84, 56),
        rect(44, 50, 12, 16, 2, FILLED),
        dot(50, 58, 2.6),
        line(26, 34, 26, 80), line(74, 34, 74, 80),
    ])


@icon("submarine")
def submarine():
    return "".join([
        ellipse(46, 58, 34, 19, 0, FILLED),
        path("M 38 40 L 38 28 L 56 28 L 56 40", FILLED),
        line(47, 28, 47, 14), path("M 47 16 L 60 16"),
        circle(34, 58, 8, FILLED), circle(58, 58, 8, FILLED),
        path("M 80 58 L 90 48 L 90 68 Z", FILLED),
        line(12, 50, 12, 66),
    ])


@icon("bubbles")
def bubbles():
    return "".join([
        circle(34, 64, 16, FILLED),
        circle(62, 44, 11, FILLED),
        circle(48, 24, 7, FILLED),
        arc(34, 64, 9, 180, 260),
        arc(62, 44, 6, 180, 260),
    ])


@icon("seaweed")
def seaweed():
    return "".join([
        path("M 34 88 C 24 74 42 64 32 50 C 24 38 38 30 34 18"),
        path("M 56 88 C 66 72 48 62 58 46 C 66 34 54 28 58 16"),
        path("M 74 88 C 82 78 70 70 78 58"),
        arc(50, 90, 22, 200, 340),
    ])


@icon("shark")
def shark():
    return "".join([
        path("M 10 58 C 22 40 44 32 64 36 C 80 40 88 50 90 58 "
             "C 84 66 70 74 52 74 C 32 74 18 68 10 58 Z", FILLED),
        path("M 52 34 L 60 14 L 70 38"),
        path("M 10 58 C 6 48 4 40 4 34 C 12 42 18 50 20 56"),
        path("M 36 68 C 38 78 44 84 50 84"),
        path("M 24 60 C 36 68 56 70 74 64"),
        dot(30, 52, 2.8),
        line(44, 46, 44, 54), line(50, 46, 50, 54),
    ])


@icon("lighthouse")
def lighthouse():
    return "".join([
        path("M 36 42 L 64 42 L 70 82 L 30 82 Z", FILLED),
        path("M 38 34 L 62 34 L 64 42 L 36 42 Z", FILLED),
        path("M 40 22 L 60 22 L 62 34 L 38 34 Z", FILLED),
        path("M 50 10 L 62 22 L 38 22 Z", FILLED),
        line(34, 58, 68, 58), line(32, 70, 70, 70),
        line(22, 24, 32, 28), line(78, 24, 68, 28),
        line(10, 82, 90, 82),
    ])


@icon("wave")
def wave():
    return "".join([
        path("M 10 74 C 14 46 34 28 56 30 C 76 32 84 48 78 60 "
             "C 72 72 56 72 52 62 C 48 54 56 46 64 50", FILLED),
        path("M 10 82 C 24 76 34 88 48 82 C 62 76 72 88 90 82"),
    ])


@icon("clam_pearl")
def clam_pearl():
    out = [
        path("M 12 68 C 12 86 30 92 50 92 C 70 92 88 86 88 68 "
             "C 74 74 26 74 12 68 Z", FILLED),
        path("M 18 56 C 20 38 34 28 50 28 C 66 28 80 38 82 56 "
             "C 70 50 30 50 18 56 Z", FILLED),
    ]
    for a in (-36, -18, 0, 18, 36):
        x, y = pt(50, 58, 30, 270 + a)
        out.append(line(50, 56, x, y))
    out.append(circle(50, 60, 9, FILLED))
    return "".join(out)
