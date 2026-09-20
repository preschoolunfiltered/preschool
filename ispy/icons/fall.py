"""Autumn, harvest and Thanksgiving doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group,
    heart, leaf, line, path, petal_flower, poly, pt, rect, rotated, spiral,
    star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("acorn")
def acorn():
    return "".join([
        path("M 26 44 C 26 64 36 84 50 84 C 64 84 74 64 74 44 Z", FILLED),
        path("M 22 44 C 22 30 34 22 50 22 C 66 22 78 30 78 44 Z", FILLED),
        line(30, 32, 30, 44), line(42, 26, 42, 44),
        line(58, 26, 58, 44), line(70, 32, 70, 44),
        line(50, 22, 50, 12),
    ])


@icon("pumpkin")
def pumpkin():
    return "".join([
        ellipse(50, 58, 34, 28, 0, FILLED),
        path("M 36 32 C 28 42 28 74 36 84"),
        path("M 64 32 C 72 42 72 74 64 84"),
        path("M 50 30 L 50 16"),
        path("M 50 20 C 60 10 72 12 76 20 C 66 20 58 24 54 30"),
    ])


@icon("maple_leaf")
def maple_leaf():
    return "".join([
        poly([(50, 6), (53, 22), (64, 20), (61, 30), (76, 18), (73, 34),
              (88, 33), (78, 44), (84, 49), (60, 66), (63, 74), (52, 72),
              (48, 72), (37, 74), (40, 66), (16, 49), (22, 44), (12, 33),
              (27, 34), (24, 18), (39, 30), (36, 20), (47, 22)], True, FILLED),
        line(50, 70, 50, 94),
    ])


@icon("oak_leaf")
def oak_leaf():
    return "".join([
        path("M 50 10 C 60 14 58 22 64 24 C 72 26 72 34 68 38 "
             "C 76 42 74 50 68 52 C 76 58 70 66 64 66 "
             "C 66 74 58 78 52 74 L 50 86 L 48 74 "
             "C 42 78 34 74 36 66 C 30 66 24 58 32 52 "
             "C 26 50 24 42 32 38 C 28 34 28 26 36 24 "
             "C 42 22 40 14 50 10 Z", FILLED),
        line(50, 70, 50, 20),
    ])


@icon("apple")
def apple():
    return "".join([
        path("M 50 32 C 42 24 26 26 22 42 C 18 60 30 84 42 84 "
             "C 46 84 48 82 50 82 C 52 82 54 84 58 84 "
             "C 70 84 82 60 78 42 C 74 26 58 24 50 32 Z", FILLED),
        line(50, 32, 50, 18),
        path("M 50 24 C 58 12 70 12 74 16 C 68 24 58 28 50 24 Z", FILLED),
    ])


@icon("corn")
def corn():
    out = [path("M 50 14 C 66 20 74 38 74 58 C 74 76 64 88 50 88 "
                "C 36 88 26 76 26 58 C 26 38 34 20 50 14 Z", FILLED)]
    for y in (30, 42, 54, 66, 78):
        out.append(line(30, y, 70, y))
    out.append(line(50, 18, 50, 88))
    out.append(path("M 26 58 C 14 56 8 66 12 80 C 20 78 26 72 28 64", FILLED))
    out.append(path("M 74 58 C 86 56 92 66 88 80 C 80 78 74 72 72 64", FILLED))
    return "".join(out)


@icon("sunflower")
def sunflower():
    out = []
    for i in range(12):
        a = i * 30
        x, y = pt(50, 40, 22, a)
        out.append(ellipse(x, y, 10, 6, a, FILLED))
    out.append(circle(50, 40, 15, FILLED))
    out.append(dot(45, 36, 2.2)); out.append(dot(55, 38, 2.2))
    out.append(dot(48, 45, 2.2)); out.append(dot(56, 46, 2.2))
    out.append(line(50, 55, 50, 92))
    out.append(leaf(36, 74, 11, rot=-60, vein=False))
    out.append(leaf(64, 80, 11, rot=60, vein=False))
    return "".join(out)


@icon("hay_bale")
def hay_bale():
    return "".join([
        rect(16, 34, 68, 50, 10, FILLED),
        line(16, 50, 84, 50), line(16, 68, 84, 68),
        line(38, 34, 38, 84), line(62, 34, 62, 84),
        line(20, 42, 30, 42), line(68, 60, 78, 60),
    ])


@icon("mushroom")
def mushroom():
    return "".join([
        path("M 14 52 C 14 30 30 18 50 18 C 70 18 86 30 86 52 Z", FILLED),
        circle(34, 38, 6, FILLED), circle(58, 32, 7, FILLED),
        circle(70, 46, 5, FILLED),
        path("M 36 52 C 36 72 34 84 40 88 L 60 88 C 66 84 64 72 64 52 Z",
             FILLED),
    ])


@icon("squirrel")
def squirrel():
    return "".join([
        path("M 58 84 C 80 84 92 64 82 46 C 74 32 56 34 54 48 "
             "C 64 42 76 48 78 60 C 80 74 70 82 58 84 Z", FILLED),
        path("M 30 48 C 30 34 40 26 50 28 C 60 30 64 38 62 46 "
             "C 60 54 52 56 50 62 C 48 70 54 78 62 82 L 34 86 "
             "C 22 82 22 64 30 48 Z", FILLED),
        path("M 34 32 C 30 24 38 20 43 26"),
        dot(43, 42, 2.8),
        dot(30, 48, 2.6),
        path("M 36 78 C 32 84 36 88 42 86"),
    ])


@icon("owl")
def owl():
    return "".join([
        path("M 50 16 C 72 16 84 34 84 54 C 84 74 70 86 50 86 "
             "C 30 86 16 74 16 54 C 16 34 28 16 50 16 Z", FILLED),
        circle(38, 46, 12, FILLED), circle(62, 46, 12, FILLED),
        dot(38, 46, 4), dot(62, 46, 4),
        poly([(50, 50), (56, 58), (44, 58)], True, FILLED),
        path("M 30 22 L 24 12 L 38 18"), path("M 70 22 L 76 12 L 62 18"),
        path("M 22 58 C 26 70 28 76 32 82"),
        path("M 78 58 C 74 70 72 76 68 82"),
        path("M 36 68 C 44 72 56 72 64 68"),
        line(44, 86, 44, 92), line(56, 86, 56, 92),
    ])


@icon("pinecone")
def pinecone():
    out = [path("M 50 12 C 68 24 76 44 76 58 C 76 76 64 88 50 88 "
                "C 36 88 24 76 24 58 C 24 44 32 24 50 12 Z", FILLED)]
    for y in (30, 44, 58, 72):
        out.append(arc(50, y, 22, 20, 160))
        out.append(arc(34, y + 7, 12, 20, 160))
        out.append(arc(66, y + 7, 12, 20, 160))
    return "".join(out)


@icon("sweater")
def sweater():
    return "".join([
        path("M 34 30 L 66 30 L 82 44 L 74 54 L 68 48 L 68 84 L 32 84 "
             "L 32 48 L 26 54 L 18 44 Z", FILLED),
        path("M 40 30 C 44 38 56 38 60 30"),
        line(32, 60, 68, 60), line(32, 68, 68, 68),
        line(36, 84, 36, 90), line(64, 84, 64, 90),
    ])


@icon("wheelbarrow")
def wheelbarrow():
    return "".join([
        path("M 18 34 L 84 34 L 68 62 L 30 62 Z", FILLED),
        line(68, 46, 92, 56),
        circle(34, 72, 12, FILLED), circle(34, 72, 4, FILLED),
        line(30, 62, 26, 78), line(60, 62, 64, 76),
        line(84, 34, 92, 56),
    ])


@icon("pie")
def pie():
    out = [path("M 12 60 C 12 48 30 42 50 42 C 70 42 88 48 88 60 "
                "C 88 74 72 84 50 84 C 28 84 12 74 12 60 Z", FILLED),
           path("M 16 58 C 28 50 72 50 84 58")]
    for x in (34, 50, 66):
        out.append(line(x - 4, 50, x + 2, 42))
    out.append(path("M 38 32 C 34 26 42 22 38 16"))
    out.append(path("M 58 32 C 54 26 62 22 58 16"))
    return "".join(out)


@icon("hot_cocoa")
def hot_cocoa():
    return "".join([
        path("M 24 38 L 72 38 L 68 80 C 68 84 64 86 48 86 "
             "C 32 86 28 84 28 80 Z", FILLED),
        path("M 72 46 C 86 46 88 66 72 68"),
        path("M 26 46 C 40 52 56 42 70 48"),
        rect(38, 34, 10, 8, 2, FILLED), rect(52, 32, 10, 8, 2, FILLED),
        path("M 38 26 C 34 20 42 16 38 10"),
        path("M 58 26 C 54 20 62 16 58 10"),
    ])


@icon("fox")
def fox():
    return "".join([
        path("M 50 84 C 30 84 20 68 22 50 C 24 36 34 28 50 28 "
             "C 66 28 76 36 78 50 C 80 68 70 84 50 84 Z", FILLED),
        path("M 24 44 L 16 18 L 40 30", FILLED),
        path("M 76 44 L 84 18 L 60 30", FILLED),
        dot(38, 50, 3.2), dot(62, 50, 3.2),
        path("M 34 64 C 40 76 60 76 66 64 C 60 60 40 60 34 64 Z", FILLED),
        dot(50, 66, 3.4),
        line(50, 70, 50, 76),
    ])


@icon("turkey")
def turkey():
    out = []
    for a in range(192, 350, 26):
        x, y = pt(50, 62, 32, a)
        out.append(ellipse(x, y, 15, 9, a, FILLED))
    for a in range(205, 340, 33):
        x, y = pt(50, 62, 18, a)
        out.append(ellipse(x, y, 10, 7, a, FILLED))
    out.append(ellipse(50, 68, 21, 19, 0, FILLED))
    out.append(circle(50, 44, 13, FILLED))
    out.append(dot(45, 41, 2.6))
    out.append(dot(55, 41, 2.6))
    out.append(poly([(50, 46), (60, 51), (50, 55)], True, FILLED))
    out.append(path("M 53 54 C 59 58 58 66 51 64"))
    out.append(line(43, 87, 41, 93))
    out.append(line(57, 87, 59, 93))
    return "".join(out)


@icon("scarecrow")
def scarecrow():
    return "".join([
        circle(50, 34, 18, FILLED),
        dot(44, 32, 2.8), dot(56, 32, 2.8),
        arc(50, 36, 7, 20, 160),
        path("M 26 20 C 34 12 66 12 74 20 Z", FILLED),
        line(24, 20, 76, 20),
        line(50, 52, 50, 88),
        line(22, 62, 78, 62),
        path("M 22 62 L 14 56"), path("M 22 62 L 14 68"),
        path("M 78 62 L 86 56"), path("M 78 62 L 86 68"),
        path("M 40 60 L 60 60 L 62 80 L 38 80 Z", FILLED),
    ])


@icon("wheat_stalk")
def wheat_stalk():
    out = [line(50, 92, 50, 34)]
    for i, y in enumerate((36, 46, 56, 66)):
        out.append(ellipse(40, y, 10, 5, -35, FILLED))
        out.append(ellipse(60, y, 10, 5, 35, FILLED))
    out.append(ellipse(50, 26, 6, 11, 0, FILLED))
    return "".join(out)




@icon("pilgrim_hat")
def pilgrim_hat():
    return "".join([
        path("M 30 62 L 30 26 C 30 20 70 20 70 26 L 70 62 Z", FILLED),
        ellipse(50, 66, 40, 10, 0, FILLED),
        rect(28, 44, 44, 12, 2, FILLED),
        rect(44, 44, 12, 12, 2, FILLED),
    ])
