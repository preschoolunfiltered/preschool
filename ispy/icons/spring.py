"""Spring, garden and growing-things doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group,
    heart, leaf, line, path, petal_flower, poly, pt, rect, rotated, star,
    spiral, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("tulip")
def tulip():
    cup = ("M 32 42 C 32 30 38 22 50 20 C 62 22 68 30 68 42 "
           "C 68 54 60 60 50 60 C 40 60 32 54 32 42 Z")
    return "".join([
        path(cup, FILLED),
        path("M 38 26 C 42 34 42 44 41 52"),
        path("M 62 26 C 58 34 58 44 59 52"),
        line(50, 58, 50, 88),
        path("M 50 70 C 38 68 30 62 26 52 C 36 50 46 58 50 70 Z"),
        path("M 50 78 C 62 76 70 70 74 60 C 64 58 54 66 50 78 Z"),
    ])


@icon("daisy")
def daisy():
    return "".join([
        line(50, 44, 50, 88),
        path("M 50 70 C 40 70 32 64 30 56 C 40 54 48 60 50 70 Z"),
        petal_flower(50, 38, 26, petals=8, petal=0.40, center=0.22),
    ])


@icon("leaf_sprig")
def leaf_sprig():
    out = [path("M 22 84 C 34 62 44 40 58 18")]
    for i, (x, y, r) in enumerate(
        [(36, 62, 11), (46, 46, 11), (56, 30, 10), (30, 50, 10), (41, 34, 9)]
    ):
        out.append(leaf(x, y, r, rot=35 if i < 3 else -35, vein=False))
    return "".join(out)


@icon("seed_packet")
def seed_packet():
    return "".join([
        path("M 28 22 L 72 22 L 72 84 L 28 84 Z", FILLED),
        path("M 28 34 C 38 28 62 28 72 34"),
        petal_flower(50, 52, 13, petals=5, petal=0.46, center=0.2),
        line(38, 72, 62, 72),
        line(42, 78, 58, 78),
    ])


@icon("watering_can")
def watering_can():
    return "".join([
        poly([(36, 52), (12, 36), (5, 46), (36, 66)], True, FILLED),
        line(12, 36, 5, 46),
        path("M 36 44 L 80 44 L 74 84 C 74 87 70 88 55 88 C 42 88 40 87 40 84 Z",
             FILLED),
        rect(32, 40, 52, 8, 3, FILLED),
        path("M 54 40 C 54 28 68 24 76 30 C 81 34 80 40 78 44"),
    ])


@icon("flower_pot")
def flower_pot():
    return "".join([
        rect(26, 34, 48, 12, 4, FILLED),
        path("M 30 46 L 70 46 L 64 84 L 36 84 Z", FILLED),
        line(38, 60, 62, 60),
    ])


@icon("garden_glove")
def garden_glove():
    return "".join([
        path("M 32 52 C 32 32 36 22 42 22 C 47 22 48 30 48 42 "
             "L 48 30 C 48 22 52 20 56 22 C 59 24 59 32 58 44 "
             "C 60 36 64 34 68 37 C 72 40 70 52 66 62 "
             "C 62 72 58 78 46 78 C 34 78 30 68 32 52 Z", FILLED),
        path("M 32 62 C 26 60 22 56 22 50 C 22 44 28 42 32 46"),
        path("M 33 74 L 60 74"),
    ])


@icon("sun_hat")
def sun_hat():
    return "".join([
        ellipse(50, 66, 38, 12, 0, FILLED),
        path("M 26 64 C 26 38 36 28 50 28 C 64 28 74 38 74 64", FILLED),
        path("M 26 60 C 38 66 62 66 74 60"),
        path("M 28 58 L 72 58"),
    ])


@icon("sprout")
def sprout():
    return "".join([
        path("M 50 84 L 50 44"),
        path("M 50 58 C 34 58 24 50 22 38 C 36 34 48 42 50 58 Z"),
        path("M 50 50 C 66 50 76 42 78 30 C 64 26 52 34 50 50 Z"),
        arc(50, 74, 22, 200, 340),
    ])


@icon("hand_fork")
def hand_fork():
    return "".join([
        path("M 44 12 C 40 20 40 30 44 38 L 56 38 C 60 30 60 20 56 12 Z", FILLED),
        line(44, 22, 56, 22), line(44, 30, 56, 30),
        rect(46, 38, 8, 10, 2, FILLED),
        path("M 36 52 C 44 48 56 48 64 52"),
        path("M 38 52 C 32 64 32 76 40 82"),
        path("M 50 52 C 50 64 50 74 50 84"),
        path("M 62 52 C 68 64 68 76 60 82"),
    ])


@icon("trowel")
def trowel():
    return "".join([
        path("M 44 10 C 40 18 40 26 44 32 L 56 32 C 60 26 60 18 56 10 Z", FILLED),
        line(44, 20, 56, 20),
        rect(46, 32, 8, 10, 2, FILLED),
        path("M 50 44 C 36 48 30 58 34 68 L 50 88 L 66 68 "
             "C 70 58 64 48 50 44 Z", FILLED),
        line(50, 52, 50, 82),
    ])


@icon("snail")
def snail():
    return "".join([
        path("M 18 80 C 10 80 8 70 18 68 L 58 68 L 58 80 Z", FILLED),
        circle(58, 50, 26, FILLED),
        spiral(58, 50, 4, 23, turns=2.2, start=200),
        path("M 20 68 C 16 56 20 46 30 42"),
        line(24, 52, 16, 42), line(31, 46, 28, 34),
        dot(15, 40, 2.6), dot(27, 32, 2.6),
        dot(25, 60, 2.4),
        arc(21, 62, 4, 10, 150),
    ])


@icon("ladybug")
def ladybug():
    return "".join([
        ellipse(50, 54, 30, 28, 0, FILLED),
        path("M 50 26 C 36 26 26 34 24 44 C 34 40 66 40 76 44 C 74 34 64 26 50 26 Z",
             SOLID),
        line(50, 28, 50, 82),
        dot(36, 56, 5), dot(64, 56, 5), dot(40, 70, 4), dot(60, 70, 4),
        line(38, 32, 30, 20), line(62, 32, 70, 20),
        dot(29, 18, 3), dot(71, 18, 3),
    ])


@icon("bee")
def bee():
    return "".join([
        ellipse(46, 58, 25, 19, -12, FILLED),
        path("M 40 40 C 46 46 48 62 44 76"),
        path("M 54 42 C 60 50 62 64 58 74"),
        poly([(68, 52), (82, 46), (72, 62)], True, FILLED),
        ellipse(38, 30, 15, 9, -28, FILLED),
        ellipse(60, 28, 15, 9, 22, FILLED),
        line(30, 44, 22, 34), line(40, 40, 36, 28),
        dot(21, 32, 2.4), dot(35, 26, 2.4),
        dot(29, 56, 2.6),
        arc(26, 60, 5, 10, 150),
    ])


@icon("butterfly")
def butterfly():
    return "".join([
        ellipse(50, 52, 5, 22, 0, FILLED),
        path("M 46 38 C 28 18 8 26 12 44 C 15 58 32 58 46 50 Z", FILLED),
        path("M 54 38 C 72 18 92 26 88 44 C 85 58 68 58 54 50 Z", FILLED),
        path("M 46 56 C 32 62 22 76 32 84 C 42 90 48 76 48 64 Z", FILLED),
        path("M 54 56 C 68 62 78 76 68 84 C 58 90 52 76 52 64 Z", FILLED),
        line(48, 32, 40, 16), line(52, 32, 60, 16),
        dot(39, 14, 2.6), dot(61, 14, 2.6),
        dot(26, 40, 3), dot(74, 40, 3),
    ])


@icon("worm")
def worm():
    return "".join([
        tube(wave_points(20, 78, 74, 34, 9, 1.35), 9, FILLED),
        dot(70, 32, 2.6),
        arc(68, 40, 4.5, 10, 150),
        line(66, 26, 62, 16), line(76, 28, 82, 20),
        dot(61, 14, 2.4), dot(83, 18, 2.4),
    ])


@icon("birds_nest")
def birds_nest():
    return "".join([
        ellipse(38, 58, 10, 8, -15, FILLED),
        ellipse(62, 58, 10, 8, 15, FILLED),
        ellipse(50, 52, 10, 8, 0, FILLED),
        path("M 18 58 C 18 82 32 88 50 88 C 68 88 82 82 82 58 "
             "C 70 66 30 66 18 58 Z", FILLED),
        path("M 24 66 C 36 74 64 74 76 66"),
        path("M 22 74 C 36 82 64 82 78 74"),
    ])


@icon("chick")
def chick():
    return "".join([
        blob(50, 56, 27, n=10, wobble=0.04, extra=FILLED),
        path("M 42 30 C 44 21 50 19 53 25"),
        poly([(60, 54), (76, 58), (60, 63)], True, FILLED),
        dot(42, 50, 2.8), dot(56, 50, 2.8),
        path("M 28 60 C 20 64 22 74 31 74"),
        line(42, 82, 40, 91), line(56, 82, 58, 91),
        line(36, 91, 44, 91), line(54, 91, 62, 91),
    ])


@icon("rain_boot")
def rain_boot():
    return "".join([
        path("M 32 22 L 60 22 L 58 60 C 58 70 66 70 76 70 L 76 82 "
             "C 52 82 34 78 34 62 Z", FILLED),
        line(32, 32, 60, 32),
        path("M 34 74 L 76 74"),
    ])


@icon("raincoat")
def raincoat():
    return "".join([
        path("M 34 34 L 66 34 L 74 50 L 68 54 L 68 82 L 32 82 L 32 54 "
             "L 26 50 Z", FILLED),
        arc(50, 34, 16, 200, 340, FILLED),
        line(50, 44, 50, 82),
        dot(50, 56, 2.6), dot(50, 68, 2.6),
        path("M 40 34 C 44 42 56 42 60 34"),
    ])


@icon("birdhouse")
def birdhouse():
    return "".join([
        path("M 26 46 L 74 46 L 74 84 L 26 84 Z", FILLED),
        path("M 50 14 L 84 48 L 16 48 Z", FILLED),
        circle(50, 60, 11, FILLED),
        line(50, 71, 50, 79),
        dot(50, 80, 3.2),
        line(50, 14, 50, 8),
        dot(50, 7, 3),
    ])


@icon("umbrella")
def umbrella():
    return "".join([
        path("M 12 54 C 12 30 30 16 50 16 C 70 16 88 30 88 54 "
             "C 78 46 70 46 62 54 C 56 46 44 46 38 54 C 30 46 22 46 12 54 Z",
             FILLED),
        line(50, 18, 50, 76),
        path("M 50 76 C 50 86 40 88 36 80"),
    ])


@icon("rainbow")
def rainbow():
    return "".join([
        arc(50, 74, 36, 180, 360),
        arc(50, 74, 26, 180, 360),
        arc(50, 74, 16, 180, 360),
    ])


@icon("cloud")
def cloud():
    return "".join([
        path("M 22 68 C 12 68 10 54 20 50 C 18 34 36 26 46 36 "
             "C 52 24 72 26 74 40 C 88 40 90 62 78 68 Z", FILLED),
    ])


@icon("raindrop")
def raindrop():
    return teardrop(50, 50, 24, FILLED)


@icon("sun")
def sun():
    out = [circle(50, 50, 24, FILLED)]
    for i in range(8):
        a = i * 45
        x0, y0 = pt(50, 50, 30, a)
        x1, y1 = pt(50, 50, 42, a)
        out.append(line(x0, y0, x1, y1))
    out.append(face(50, 48, 16, 2.8, 7))
    return "".join(out)


@icon("grass_tuft")
def grass_tuft():
    return "".join([
        path("M 50 84 C 44 70 42 56 44 42"),
        path("M 50 84 C 56 70 58 58 56 46"),
        path("M 50 84 C 38 74 30 62 28 50"),
        path("M 50 84 C 62 74 70 64 72 52"),
        path("M 50 84 C 48 76 50 66 50 58"),
    ])


@icon("blossom_branch")
def blossom_branch():
    out = [path("M 16 82 C 30 68 44 50 58 26"), line(34, 62, 24, 54),
           line(46, 46, 58, 42)]
    for x, y, r in [(58, 22, 11), (24, 50, 9), (62, 40, 9)]:
        out.append(petal_flower(x, y, r, petals=5, petal=0.5, center=0.18))
    return "".join(out)


@icon("bird")
def bird():
    return "".join([
        path("M 22 62 C 22 44 36 32 52 32 C 68 32 80 42 80 56 "
             "C 80 70 66 78 50 78 C 34 78 22 74 22 62 Z", FILLED),
        path("M 44 52 C 54 48 66 52 70 62 C 60 68 48 64 44 52 Z"),
        poly([(22, 58), (8, 62), (22, 66)], True, FILLED),
        dot(30, 52, 2.6),
        path("M 80 44 C 88 34 92 32 96 30 C 92 40 88 46 84 50"),
        line(46, 78, 44, 88), line(58, 78, 60, 88),
    ])
