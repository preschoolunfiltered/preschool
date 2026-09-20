"""Deciding how many of each doodle appear, and where they land."""

from __future__ import annotations

import math
import random


def counts_for(n_icons: int, total: int, rng: random.Random,
               lo: int = 2, hi: int = 18) -> list[int]:
    """Split `total` items across `n_icons` kinds with a pleasant spread."""
    weights = [rng.uniform(0.45, 1.8) for _ in range(n_icons)]
    s = sum(weights)
    counts = [max(lo, min(hi, round(w / s * total))) for w in weights]
    # nudge toward the requested total without breaking the bounds
    guard = 0
    while sum(counts) != total and guard < 4000:
        guard += 1
        i = rng.randrange(n_icons)
        if sum(counts) < total and counts[i] < hi:
            counts[i] += 1
        elif sum(counts) > total and counts[i] > lo:
            counts[i] -= 1
    return counts


def scatter(items, area, rng: random.Random, base_size: float,
            obstacles=(), size_jitter=(0.88, 1.12), rot=18.0):
    """Dart-throw `items` into `area` without crowding.

    items     : list of icon names (one entry per drawn item)
    area      : (x0, y0, x1, y1) in points
    obstacles : pre-occupied circles (x, y, r) to keep clear
    returns   : list of (name, x, y, size, rotation)
    """
    x0, y0, x1, y1 = area
    order = list(items)
    rng.shuffle(order)
    placed: list[tuple[float, float, float]] = [tuple(o) for o in obstacles]
    out = []
    for name in order:
        size = base_size * rng.uniform(*size_jitter)
        r = size * 0.46
        spot = None
        for attempt in range(900):
            # relax the spacing requirement the longer we struggle
            k = 0.98 - min(attempt / 900.0, 1.0) * 0.42
            px = rng.uniform(x0 + r, x1 - r)
            py = rng.uniform(y0 + r, y1 - r)
            ok = True
            for (qx, qy, qr) in placed:
                if (px - qx) ** 2 + (py - qy) ** 2 < (k * (r + qr)) ** 2:
                    ok = False
                    break
            if ok:
                spot = (px, py)
                break
        if spot is None:                      # page is full - drop the item
            continue
        placed.append((spot[0], spot[1], r))
        out.append((name, spot[0], spot[1], size, rng.uniform(-rot, rot)))
    return out


def tally(placed) -> dict[str, int]:
    """What actually made it onto the page - the answer key's source of truth."""
    counts: dict[str, int] = {}
    for name, *_ in placed:
        counts[name] = counts.get(name, 0) + 1
    return counts
