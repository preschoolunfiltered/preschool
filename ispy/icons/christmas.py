"""Christmas doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group,
    heart, leaf, line, path, petal_flower, poly, pt, rect, rotated, spiral,
    star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("christmas_tree")
def christmas_tree():
    return "".join([
        rect(44, 80, 12, 10, 2, FILLED),
        path("M 50 8 L 66 32 L 34 32 Z", FILLED),
        path("M 50 24 L 72 52 L 28 52 Z", FILLED),
        path("M 50 42 L 80 80 L 20 80 Z", FILLED),
        star(50, 8, 10, 5, 0.45, -90, FILLED),
        dot(44, 44, 3), dot(60, 46, 3), dot(38, 70, 3),
        dot(54, 68, 3), dot(68, 74, 3),
    ])


@icon("gift")
def gift():
    return "".join([
        rect(18, 38, 64, 48, 3, FILLED),
        rect(14, 26, 72, 14, 3, FILLED),
        line(50, 26, 50, 86),
        path("M 50 26 C 40 26 30 22 32 14 C 34 8 46 12 50 26 Z", FILLED),
        path("M 50 26 C 60 26 70 22 68 14 C 66 8 54 12 50 26 Z", FILLED),
    ])


@icon("candy_cane")
def candy_cane():
    spine = [(38, 92), (38, 74), (39, 58), (42, 44), (50, 34),
             (62, 30), (72, 34), (76, 44), (76, 54)]
    return "".join([
        tube(spine, 9, FILLED),
        cross_ticks(spine, 9, [1, 3, 5, 7]),
    ])


@icon("stocking")
def stocking():
    return "".join([
        path("M 34 32 L 62 32 L 60 56 C 60 66 70 66 78 70 "
             "C 86 74 84 86 74 86 C 58 86 36 80 36 62 Z", FILLED),
        rect(30, 20, 36, 14, 4, FILLED),
        line(38, 46, 60, 46),
        path("M 40 74 C 52 82 66 82 76 78"),
    ])


@icon("santa_hat")
def santa_hat():
    return "".join([
        path("M 20 62 C 20 34 34 20 52 22 C 72 24 84 34 84 40 "
             "C 84 46 76 48 70 46 C 60 42 50 48 48 62 Z", FILLED),
        rect(14, 62, 62, 14, 7, FILLED),
        circle(86, 40, 9, FILLED),
    ])


@icon("reindeer")
def reindeer():
    return "".join([
        path("M 50 34 C 66 34 76 46 76 60 C 76 76 64 86 50 86 "
             "C 36 86 24 76 24 60 C 24 46 34 34 50 34 Z", FILLED),
        path("M 34 38 C 26 28 24 18 26 10 M 26 22 L 14 16 M 30 30 L 18 30"),
        path("M 66 38 C 74 28 76 18 74 10 M 74 22 L 86 16 M 70 30 L 82 30"),
        dot(40, 54, 3.2), dot(60, 54, 3.2),
        circle(50, 70, 9, SOLID),
        ellipse(20, 52, 8, 11, -20, FILLED),
        ellipse(80, 52, 8, 11, 20, FILLED),
    ])


@icon("bell")
def bell():
    return "".join([
        path("M 50 20 C 68 20 74 42 74 58 C 74 66 78 70 82 72 L 18 72 "
             "C 22 70 26 66 26 58 C 26 42 32 20 50 20 Z", FILLED),
        rect(42, 12, 16, 9, 4, FILLED),
        path("M 40 72 C 40 82 60 82 60 72"),
        circle(50, 84, 6, FILLED),
    ])


@icon("wreath")
def wreath():
    out = [blob(50, 48, 34, n=12, wobble=0.07, extra=FILLED),
           blob(50, 48, 18, n=10, wobble=0.09, extra=FILLED)]
    for a in range(0, 360, 45):
        x, y = pt(50, 48, 26, a)
        out.append(dot(x, y, 3.4))
    out.append(path("M 50 82 C 40 82 32 88 34 94 C 38 96 46 90 50 82 Z", FILLED))
    out.append(path("M 50 82 C 60 82 68 88 66 94 C 62 96 54 90 50 82 Z", FILLED))
    return "".join(out)


@icon("gingerbread_man")
def gingerbread_man():
    return "".join([
        circle(50, 26, 17, FILLED),
        path("M 38 44 C 30 48 14 56 12 64 C 10 72 18 74 24 70 "
             "L 36 62 L 34 80 C 34 88 40 92 44 88 L 50 76 L 56 88 "
             "C 60 92 66 88 66 80 L 64 62 L 76 70 C 82 74 90 72 88 64 "
             "C 86 56 70 48 62 44 Z", FILLED),
        dot(44, 24, 2.6), dot(56, 24, 2.6),
        arc(50, 28, 7, 20, 160),
        line(34, 58, 42, 54), line(66, 58, 58, 54),
        dot(50, 56, 3), dot(50, 68, 3),
    ])


@icon("ornament")
def ornament():
    out = [circle(50, 58, 28, FILLED),
           rect(42, 24, 16, 10, 2, FILLED),
           path("M 44 24 C 44 12 56 12 56 24")]
    out.append(path("M 24 50 C 38 58 62 58 76 50"))
    out.append(path("M 26 68 C 38 62 62 62 74 68"))
    for x in (36, 50, 64):
        out.append(dot(x, 59, 3))
    return "".join(out)


@icon("sleigh")
def sleigh():
    return "".join([
        path("M 24 34 L 24 62 C 24 68 30 72 40 72 L 76 72 L 76 34 "
             "C 76 30 70 30 70 34 L 70 60 L 30 60 L 30 34 Z", FILLED),
        path("M 24 40 C 12 38 8 26 18 22 C 26 19 30 28 24 32", FILLED),
        line(24, 50, 70, 50),
        path("M 16 80 L 78 80 C 88 80 90 70 84 66"),
        path("M 16 80 C 8 80 8 88 16 88 L 78 88"),
        line(34, 72, 34, 80), line(64, 72, 64, 80),
    ])


@icon("snow_globe")
def snow_globe():
    return "".join([
        circle(50, 44, 30, FILLED),
        path("M 50 60 L 60 74 L 40 74 Z", FILLED),
        path("M 50 46 L 58 60 L 42 60 Z", FILLED),
        dot(32, 34, 2.6), dot(66, 30, 2.6), dot(70, 50, 2.6), dot(30, 54, 2.6),
        path("M 24 72 L 76 72 L 82 88 L 18 88 Z", FILLED),
    ])


@icon("holly")
def holly():
    return "".join([
        path("M 48 44 C 34 38 30 26 34 16 C 42 20 46 18 50 14 "
             "C 52 22 58 26 58 34 C 58 40 54 44 48 44 Z", FILLED),
        path("M 52 48 C 66 44 76 50 80 60 C 70 60 66 64 64 70 "
             "C 58 64 52 58 52 48 Z", FILLED),
        path("M 46 50 C 34 54 28 62 30 72 C 38 68 44 70 48 74 "
             "C 50 66 50 56 46 50 Z", FILLED),
        circle(60, 40, 7, FILLED), circle(72, 36, 6, FILLED),
        circle(66, 28, 6, FILLED),
    ])


@icon("string_lights")
def string_lights():
    out = [path("M 6 22 C 24 46 40 46 50 32 C 60 18 78 22 94 42")]
    for x, y, a in ((20, 40, 30), (34, 44, 5), (50, 34, -20),
                    (64, 26, 10), (82, 34, 35)):
        out.append(group(
            rect(-5, 0, 10, 7, 2, FILLED) + path("M -7 7 L 7 7 L 0 22 Z", FILLED),
            f"translate({x} {y}) rotate({a})"))
    return "".join(out)


@icon("santa_face")
def santa_face():
    return "".join([
        path("M 24 46 C 24 26 36 16 52 18 C 70 20 80 28 80 34 "
             "C 80 40 72 42 66 40 C 58 38 50 42 48 50 Z", FILLED),
        rect(18, 44, 58, 12, 6, FILLED),
        circle(82, 34, 8, FILLED),
        path("M 30 56 C 30 76 40 88 52 88 C 64 88 74 76 74 56 Z", FILLED),
        dot(42, 60, 2.8), dot(60, 60, 2.8),
        circle(51, 68, 5, FILLED),
        path("M 40 74 C 44 78 48 78 51 74 C 54 78 58 78 62 74"),
    ])


@icon("cookie")
def cookie():
    return "".join([
        blob(50, 52, 30, n=11, wobble=0.05, extra=FILLED),
        dot(40, 42, 4), dot(60, 46, 4), dot(46, 62, 4),
        dot(64, 66, 3.6), dot(32, 58, 3.4),
    ])
