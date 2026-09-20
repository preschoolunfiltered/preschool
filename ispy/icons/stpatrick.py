"""St. Patrick's Day doodles."""

from ispy.draw import (
    SOLID, FILLED, arc, blob, bumps, circle, cross_ticks, curve, dot, ellipse,
    face, group, heart, leaf, line, path, petal_flower, poly, pt, rect, rotated,
    spiral, star, teardrop, tube, wave_points, zigzag,
)
from ispy.icons.registry import icon


@icon("shamrock")
def shamrock():
    return "".join([
        heart(50, 32, 18, FILLED),
        group(heart(50, 32, 18, FILLED), "rotate(120 50 52)"),
        group(heart(50, 32, 18, FILLED), "rotate(-120 50 52)"),
        path("M 50 58 C 54 72 52 84 44 92"),
    ])


@icon("four_leaf_clover")
def four_leaf_clover():
    body = "".join(
        group(heart(50, 30, 17, FILLED), f"rotate({a} 50 50)")
        for a in (0, 90, 180, 270)
    )
    return body + path("M 50 62 C 56 74 54 84 46 92")


@icon("pot_of_gold")
def pot_of_gold():
    return "".join([
        circle(34, 40, 9, FILLED), circle(52, 36, 9, FILLED),
        circle(68, 42, 9, FILLED),
        path("M 18 46 C 18 74 30 86 50 86 C 70 86 82 74 82 46 Z", FILLED),
        rect(12, 38, 76, 10, 5, FILLED),
        circle(34, 40, 4, FILLED), circle(52, 36, 4, FILLED),
    ])


@icon("horseshoe")
def horseshoe():
    return "".join([
        path("M 26 80 L 26 50 C 26 30 36 18 50 18 C 64 18 74 30 74 50 "
             "L 74 80 C 74 88 62 88 62 80 L 62 50 C 62 40 58 34 50 34 "
             "C 42 34 38 40 38 50 L 38 80 C 38 88 26 88 26 80 Z", FILLED),
        dot(32, 42, 2.4), dot(68, 42, 2.4),
        dot(32, 56, 2.4), dot(68, 56, 2.4),
        dot(32, 70, 2.4), dot(68, 70, 2.4),
    ])


@icon("leprechaun_hat")
def leprechaun_hat():
    return "".join([
        path("M 28 60 L 28 26 C 28 20 72 20 72 26 L 72 60 Z", FILLED),
        ellipse(50, 64, 40, 10, 0, FILLED),
        rect(26, 44, 48, 12, 2, FILLED),
        rect(42, 44, 16, 12, 2, FILLED),
        path("M 74 26 C 80 20 86 24 82 30 C 88 28 90 36 82 38 "
             "C 84 44 76 46 74 38 C 72 46 64 44 66 38 "
             "C 58 36 60 28 66 30 C 62 24 68 20 74 26 Z"),
    ])


@icon("gold_coin")
def gold_coin():
    return "".join([
        circle(50, 52, 30, FILLED),
        circle(50, 52, 22, FILLED),
        heart(50, 44, 9, FILLED),
        group(heart(50, 44, 9, FILLED), "rotate(120 50 56)"),
        group(heart(50, 44, 9, FILLED), "rotate(-120 50 56)"),
    ])




@icon("lucky_coin_bag")
def lucky_coin_bag():
    return "".join([
        path("M 34 34 C 20 44 14 60 18 72 C 22 84 36 90 50 90 "
             "C 64 90 78 84 82 72 C 86 60 80 44 66 34 Z", FILLED),
        path("M 34 34 C 38 28 62 28 66 34"),
        path("M 30 32 C 40 24 60 24 70 32"),
        heart(50, 58, 10, FILLED),
        group(heart(50, 58, 10, FILLED), "rotate(120 50 70)"),
        group(heart(50, 58, 10, FILLED), "rotate(-120 50 70)"),
    ])
