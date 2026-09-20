"""Beach, sun and summer-holiday doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group,
    heart, leaf, line, path, petal_flower, poly, pt, rect, rotated, spiral,
    star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("beach_ball")
def beach_ball():
    return "".join([
        circle(50, 52, 32, FILLED),
        path("M 50 20 C 34 36 34 68 50 84"),
        path("M 50 20 C 66 36 66 68 50 84"),
        path("M 20 42 C 38 50 62 50 80 42"),
        circle(50, 52, 5, SOLID),
    ])


@icon("ice_cream_cone")
def ice_cream_cone():
    return "".join([
        circle(40, 36, 15, FILLED),
        circle(60, 36, 15, FILLED),
        circle(50, 24, 14, FILLED),
        path("M 26 46 L 74 46 L 52 90 Z", FILLED),
        line(36, 56, 58, 50), line(44, 70, 64, 62),
        circle(50, 12, 5, FILLED),
    ])


@icon("popsicle")
def popsicle():
    return "".join([
        path("M 32 18 C 32 12 68 12 68 18 L 68 62 C 68 72 32 72 32 62 Z", FILLED),
        path("M 32 34 C 42 42 58 26 68 34"),
        rect(45, 70, 10, 20, 3, FILLED),
        line(44, 24, 44, 56),
    ])


@icon("sunglasses")
def sunglasses():
    return "".join([
        path("M 16 40 C 16 58 24 64 32 64 C 42 64 46 56 46 44 "
             "C 40 42 22 40 16 40 Z", FILLED),
        path("M 84 40 C 84 58 76 64 68 64 C 58 64 54 56 54 44 "
             "C 60 42 78 40 84 40 Z", FILLED),
        path("M 46 46 C 49 43 51 43 54 46"),
        path("M 16 42 C 12 38 10 34 10 30"),
        path("M 84 42 C 88 38 90 34 90 30"),
    ])


@icon("flip_flop")
def flip_flop():
    out = []
    for cx, tilt in ((30, -10), (70, 10)):
        body = "".join([
            path(f"M {cx} 16 C {cx + 13} 16 {cx + 15} 28 {cx + 14} 42 "
                 f"C {cx + 13} 58 {cx + 10} 84 {cx} 84 "
                 f"C {cx - 10} 84 {cx - 13} 58 {cx - 14} 42 "
                 f"C {cx - 15} 28 {cx - 13} 16 {cx} 16 Z", FILLED),
            path(f"M {cx - 10} 28 C {cx - 5} 34 {cx - 1} 38 {cx} 44"),
            path(f"M {cx + 10} 28 C {cx + 5} 34 {cx + 1} 38 {cx} 44"),
            dot(cx, 45, 3.4),
        ])
        out.append(group(body, f"rotate({tilt} {cx} 50)"))
    return "".join(out)


@icon("sandcastle")
def sandcastle():
    return "".join([
        path("M 16 84 L 16 50 L 22 50 L 22 44 L 28 44 L 28 50 L 34 50 L 34 84 Z",
             FILLED),
        path("M 66 84 L 66 50 L 72 50 L 72 44 L 78 44 L 78 50 L 84 50 L 84 84 Z",
             FILLED),
        path("M 34 84 L 34 38 L 42 38 L 42 32 L 50 32 L 50 38 L 58 38 L 58 32 "
             "L 66 32 L 66 84 Z", FILLED),
        path("M 44 84 L 44 64 C 44 58 56 58 56 64 L 56 84", FILLED),
        line(50, 32, 50, 14),
        poly([(50, 16), (68, 21), (50, 26)], True, FILLED),
        line(10, 84, 90, 84),
    ])


@icon("surfboard")
def surfboard():
    return "".join([
        path("M 50 8 C 66 26 70 56 62 80 C 58 90 42 90 38 80 "
             "C 30 56 34 26 50 8 Z", FILLED),
        line(50, 18, 50, 78),
        path("M 38 40 C 46 36 54 36 62 40"),
        path("M 39 58 C 46 54 54 54 61 58"),
    ])


@icon("beach_umbrella")
def beach_umbrella():
    return "".join([
        path("M 10 50 C 12 26 30 12 50 12 C 70 12 88 26 90 50 "
             "C 80 44 72 44 64 50 C 58 43 42 43 36 50 C 28 44 20 44 10 50 Z",
             FILLED),
        path("M 36 50 C 38 32 44 18 50 12"),
        path("M 64 50 C 62 32 56 18 50 12"),
        line(50, 14, 62, 88),
    ])


@icon("watermelon_slice")
def watermelon_slice():
    return "".join([
        path("M 12 34 L 88 34 C 88 66 72 84 50 84 C 28 84 12 66 12 34 Z", FILLED),
        path("M 20 40 L 80 40"),
        dot(38, 52, 3.4), dot(58, 54, 3.4), dot(48, 66, 3.4), dot(66, 44, 3.2),
        dot(32, 44, 3.2),
    ])


@icon("lemonade")
def lemonade():
    return "".join([
        path("M 30 30 L 70 30 L 64 84 C 64 88 36 88 36 84 Z", FILLED),
        path("M 32 46 C 44 52 58 40 68 46"),
        line(56, 12, 48, 44),
        circle(74, 26, 12, FILLED),
        line(74, 14, 74, 38), line(62, 26, 86, 26),
        dot(44, 60, 3), dot(54, 70, 3),
    ])


@icon("pineapple")
def pineapple():
    out = [
        path("M 50 88 C 30 88 22 72 22 54 C 22 38 34 28 50 28 "
             "C 66 28 78 38 78 54 C 78 72 70 88 50 88 Z", FILLED)
    ]
    for i in range(-2, 3):
        out.append(line(50 + i * 13 - 12, 32, 50 + i * 13 + 12, 84))
        out.append(line(50 + i * 13 + 12, 32, 50 + i * 13 - 12, 84))
    out.append(path("M 22 54 C 22 38 34 28 50 28 C 66 28 78 38 78 54 "
                    "C 78 72 70 88 50 88 C 30 88 22 72 22 54 Z", "fill=\"none\""))
    out.append(path("M 50 28 C 44 20 40 12 42 6 C 48 8 52 14 54 20"))
    out.append(path("M 50 28 C 56 20 62 14 68 12 C 68 20 62 26 56 28"))
    out.append(path("M 50 28 C 42 22 34 18 28 18 C 30 24 38 28 46 30"))
    return "".join(out)


@icon("palm_tree")
def palm_tree():
    return "".join([
        path("M 46 88 C 42 66 44 44 52 26", FILLED),
        path("M 54 88 C 52 66 52 44 58 26"),
        line(46, 70, 54, 70), line(46, 56, 53, 56), line(47, 42, 55, 42),
        path("M 54 24 C 40 16 26 18 18 28 C 30 26 44 28 54 24 Z", FILLED),
        path("M 54 24 C 68 14 82 16 88 26 C 76 24 62 26 54 24 Z", FILLED),
        path("M 54 24 C 46 12 34 6 24 8 C 34 14 46 20 54 24 Z", FILLED),
        path("M 54 24 C 62 10 74 6 84 8 C 74 14 62 20 54 24 Z", FILLED),
        dot(44, 30, 4), dot(64, 32, 4),
    ])


@icon("kite")
def kite():
    return "".join([
        poly([(50, 10), (78, 44), (50, 82), (22, 44)], True, FILLED),
        line(50, 10, 50, 82), line(22, 44, 78, 44),
        path("M 50 82 C 56 88 44 92 50 96"),
        path("M 44 88 L 56 92"), path("M 46 95 L 56 90"),
    ])


@icon("swim_ring")
def swim_ring():
    out = [circle(50, 52, 34, FILLED), circle(50, 52, 14, FILLED)]
    for i in range(4):
        a = i * 90 + 45
        x0, y0 = pt(50, 52, 14, a)
        x1, y1 = pt(50, 52, 34, a)
        out.append(line(x0, y0, x1, y1))
    return "".join(out)


@icon("sand_bucket")
def sand_bucket():
    return "".join([
        path("M 26 36 L 74 36 L 66 84 L 34 84 Z", FILLED),
        rect(22, 30, 56, 8, 3, FILLED),
        path("M 28 34 C 34 12 66 12 72 34"),
        line(38, 56, 64, 56),
    ])


@icon("sailboat")
def sailboat():
    return "".join([
        path("M 14 66 L 86 66 L 74 82 L 26 82 Z", FILLED),
        line(50, 66, 50, 14),
        path("M 46 62 L 46 20 L 18 62 Z", FILLED),
        path("M 54 62 L 54 24 L 78 62 Z", FILLED),
        path("M 10 88 C 20 82 30 94 40 88 C 50 82 60 94 70 88 C 78 84 84 90 90 88"),
    ])


@icon("seagull")
def seagull():
    return "".join([
        path("M 10 58 C 20 40 30 40 38 54 C 46 40 56 40 64 58"),
        path("M 58 34 C 66 24 74 24 80 34"),
    ])


@icon("sun_lotion")
def sun_lotion():
    return "".join([
        path("M 30 40 L 70 40 L 70 84 C 70 88 66 88 50 88 C 34 88 30 88 30 84 Z",
             FILLED),
        rect(42, 26, 16, 14, 3, FILLED),
        rect(44, 16, 12, 10, 3, FILLED),
        circle(50, 60, 11, FILLED),
        line(50, 49, 50, 71), line(39, 60, 61, 60),
    ])
