"""Low-level SVG drawing primitives.

Every icon is authored inside a 100x100 box (origin top-left, y grows down).
Primitives return SVG element strings; icons return a concatenation of them.
Stroke styling is inherited from the parent <g>, so primitives only set
geometry unless they explicitly need a solid fill.
"""

from __future__ import annotations

import math

SOLID = 'fill="#000" stroke="none"'
FILLED = 'fill="#fff"'  # opaque white, keeps overlapping shapes readable


def _attrs(extra: str | None) -> str:
    return f" {extra}" if extra else ""


def circle(cx, cy, r, extra=None):
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}"{_attrs(extra)}/>'


def dot(cx, cy, r=3.2):
    return circle(cx, cy, r, SOLID)


def ellipse(cx, cy, rx, ry, rot=0, extra=None):
    t = f' transform="rotate({rot:.2f} {cx:.2f} {cy:.2f})"' if rot else ""
    return (
        f'<ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}"'
        f'{t}{_attrs(extra)}/>'
    )


def line(x1, y1, x2, y2, extra=None):
    return (
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"'
        f'{_attrs(extra)}/>'
    )


def path(d, extra=None):
    return f'<path d="{d}"{_attrs(extra)}/>'


def rect(x, y, w, h, rx=0, extra=None):
    r = f' rx="{rx:.2f}"' if rx else ""
    return (
        f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}"'
        f'{r}{_attrs(extra)}/>'
    )


def poly(points, close=True, extra=None):
    pts = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    tag = "polygon" if close else "polyline"
    return f'<{tag} points="{pts}"{_attrs(extra)}/>'


def pt(cx, cy, r, ang):
    """Point on a circle. Angle in degrees, 0 = east, clockwise on screen."""
    a = math.radians(ang)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc(cx, cy, r, a0, a1, extra=None, ry=None):
    """Elliptical arc from a0 to a1 (degrees, clockwise)."""
    ry = r if ry is None else ry
    x0 = cx + r * math.cos(math.radians(a0))
    y0 = cy + ry * math.sin(math.radians(a0))
    x1 = cx + r * math.cos(math.radians(a1))
    y1 = cy + ry * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 1 if a1 > a0 else 0
    d = (
        f"M {x0:.2f} {y0:.2f} A {r:.2f} {ry:.2f} 0 {large} {sweep} "
        f"{x1:.2f} {y1:.2f}"
    )
    return path(d, extra)


def curve(points, extra=None, close=False):
    """Smooth curve through points using quadratic midpoint interpolation."""
    if len(points) < 3:
        return poly(points, close=close, extra=extra)
    d = [f"M {points[0][0]:.2f} {points[0][1]:.2f}"]
    for i in range(1, len(points) - 1):
        x, y = points[i]
        nx, ny = points[i + 1]
        mx, my = (x + nx) / 2, (y + ny) / 2
        d.append(f"Q {x:.2f} {y:.2f} {mx:.2f} {my:.2f}")
    d.append(f"L {points[-1][0]:.2f} {points[-1][1]:.2f}")
    if close:
        d.append("Z")
    return path(" ".join(d), extra)


def blob(cx, cy, r, n=9, wobble=0.13, phase=0.0, extra=None, squash=1.0):
    """Closed wobbly circle - clouds, bushes, rocks, scribbly foliage."""
    pts = []
    for i in range(n):
        a = 360 * i / n + phase
        rr = r * (1 + wobble * math.sin(math.radians(a * 3 + phase * 2)))
        x = cx + rr * math.cos(math.radians(a))
        y = cy + rr * squash * math.sin(math.radians(a))
        pts.append((x, y))
    pts.append(pts[0])
    pts.append(pts[1])
    return curve(pts, extra=extra, close=True)


def bumps(cx, cy, r, n=5, a0=180, a1=360, extra=None, squash=1.0):
    """Scalloped arc (cloud tops, sheep wool, tree crowns)."""
    d = []
    step = (a1 - a0) / n
    start = pt(cx, cy, r, a0)
    d.append(f"M {start[0]:.2f} {cy + (start[1] - cy) * squash:.2f}")
    for i in range(n):
        a = a0 + step * (i + 1)
        x, y = pt(cx, cy, r, a)
        y = cy + (y - cy) * squash
        d.append(f"A {r * step / 90:.2f} {r * step / 90:.2f} 0 0 1 {x:.2f} {y:.2f}")
    return path(" ".join(d), extra)


def star(cx, cy, r, points=5, inner=0.42, rot=-90, extra=None):
    pts = []
    for i in range(points * 2):
        rr = r if i % 2 == 0 else r * inner
        a = rot + 180 * i / points
        pts.append(pt(cx, cy, rr, a))
    return poly(pts, extra=extra)


def heart(cx, cy, r, extra=None):
    d = (
        f"M {cx:.2f} {cy + r * 0.95:.2f} "
        f"C {cx - r * 1.35:.2f} {cy + r * 0.05:.2f} "
        f"{cx - r * 0.95:.2f} {cy - r * 1.05:.2f} {cx:.2f} {cy - r * 0.35:.2f} "
        f"C {cx + r * 0.95:.2f} {cy - r * 1.05:.2f} "
        f"{cx + r * 1.35:.2f} {cy + r * 0.05:.2f} {cx:.2f} {cy + r * 0.95:.2f} Z"
    )
    return path(d, extra)


def teardrop(cx, cy, r, extra=None):
    d = (
        f"M {cx:.2f} {cy - r * 1.35:.2f} "
        f"C {cx + r * 1.05:.2f} {cy - r * 0.1:.2f} "
        f"{cx + r:.2f} {cy + r * 1.15:.2f} {cx:.2f} {cy + r * 1.15:.2f} "
        f"C {cx - r:.2f} {cy + r * 1.15:.2f} "
        f"{cx - r * 1.05:.2f} {cy - r * 0.1:.2f} {cx:.2f} {cy - r * 1.35:.2f} Z"
    )
    return path(d, extra)


def petal_flower(cx, cy, r, petals=5, petal=0.46, center=0.2, rot=-90):
    out = []
    for i in range(petals):
        a = rot + 360 * i / petals
        px, py = pt(cx, cy, r * (1 - petal * 0.85), a)
        out.append(circle(px, py, r * petal))
    out.append(circle(cx, cy, r * center))
    return "".join(out)


def leaf(cx, cy, r, rot=0, vein=True):
    d = (
        f"M {cx:.2f} {cy - r:.2f} "
        f"C {cx + r * 0.85:.2f} {cy - r * 0.45:.2f} "
        f"{cx + r * 0.6:.2f} {cy + r * 0.8:.2f} {cx:.2f} {cy + r:.2f} "
        f"C {cx - r * 0.6:.2f} {cy + r * 0.8:.2f} "
        f"{cx - r * 0.85:.2f} {cy - r * 0.45:.2f} {cx:.2f} {cy - r:.2f} Z"
    )
    out = [path(d)]
    if vein:
        out.append(line(cx, cy - r * 0.72, cx, cy + r * 0.82))
    g = "".join(out)
    if rot:
        return f'<g transform="rotate({rot:.2f} {cx:.2f} {cy:.2f})">{g}</g>'
    return g


def face(cx, cy, w=14, eye=2.6, smile=6.5, blush=False, closed=False):
    """Kawaii face: two eyes and a little smile."""
    out = []
    if closed:
        out.append(arc(cx - w / 2, cy, 3.4, 200, 340))
        out.append(arc(cx + w / 2, cy, 3.4, 200, 340))
    else:
        out.append(dot(cx - w / 2, cy, eye))
        out.append(dot(cx + w / 2, cy, eye))
    out.append(arc(cx, cy + 3.0, smile, 25, 155))
    if blush:
        out.append(ellipse(cx - w / 2 - 6.5, cy + 5, 3.2, 2.2))
        out.append(ellipse(cx + w / 2 + 6.5, cy + 5, 3.2, 2.2))
    return "".join(out)


def group(body, transform=None, extra=None):
    t = f' transform="{transform}"' if transform else ""
    return f"<g{t}{_attrs(extra)}>{body}</g>"


def rotated(body, deg, cx=50, cy=50):
    return group(body, f"rotate({deg:.2f} {cx:.2f} {cy:.2f})")


def zigzag(x0, y0, x1, y1, n=6, amp=5, extra=None):
    pts = []
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    for i in range(n + 1):
        t = i / n
        s = amp if i % 2 else -amp
        if i in (0, n):
            s = 0
        pts.append((x0 + dx * t + nx * s, y0 + dy * t + ny * s))
    return poly(pts, close=False, extra=extra)


def spiral(cx, cy, r0, r1, turns=2.5, start=0.0, steps=90, extra=None):
    """Snail shells, lollipops, curly vines."""
    pts = []
    for i in range(steps + 1):
        t = i / steps
        a = start + 360 * turns * t
        r = r0 + (r1 - r0) * t
        pts.append(pt(cx, cy, r, a))
    d = [f"M {pts[0][0]:.2f} {pts[0][1]:.2f}"] + [
        f"L {x:.2f} {y:.2f}" for x, y in pts[1:]
    ]
    return path(" ".join(d), extra)


def tube(points, w, extra=None):
    """Outline a wavy centreline with constant half-width and round caps.

    Used for worms, snakes, hoses, candy canes - anything that reads as a
    rounded noodle rather than a line.
    """
    n = len(points)
    norms = []
    for i in range(n):
        px = points[max(i - 1, 0)]
        nx = points[min(i + 1, n - 1)]
        dx, dy = nx[0] - px[0], nx[1] - px[1]
        L = math.hypot(dx, dy) or 1
        norms.append((-dy / L, dx / L))
    left = [(x + nx * w, y + ny * w) for (x, y), (nx, ny) in zip(points, norms)]
    right = [(x - nx * w, y - ny * w) for (x, y), (nx, ny) in zip(points, norms)]
    d = [f"M {left[0][0]:.2f} {left[0][1]:.2f}"]
    d += [f"L {x:.2f} {y:.2f}" for x, y in left[1:]]
    d.append(
        f"A {w:.2f} {w:.2f} 0 0 1 {right[-1][0]:.2f} {right[-1][1]:.2f}"
    )
    d += [f"L {x:.2f} {y:.2f}" for x, y in reversed(right[:-1])]
    d.append(f"A {w:.2f} {w:.2f} 0 0 1 {left[0][0]:.2f} {left[0][1]:.2f} Z")
    return path(" ".join(d), extra)


def wave_points(x0, y0, x1, y1, amp=10, cycles=1.5, steps=28):
    """Sampled sine wave between two points - feeds tube()."""
    pts = []
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    for i in range(steps + 1):
        t = i / steps
        s = amp * math.sin(2 * math.pi * cycles * t)
        pts.append((x0 + dx * t + nx * s, y0 + dy * t + ny * s))
    return pts


def cross_ticks(points, w, idxs, extra=None):
    """Short ticks across a centreline - candy-cane stripes, rope whipping."""
    out = []
    n = len(points)
    for i in idxs:
        i = max(1, min(n - 2, i))
        px, py = points[i - 1]
        nx_, ny_ = points[i + 1]
        dx, dy = nx_ - px, ny_ - py
        L = math.hypot(dx, dy) or 1
        ox, oy = -dy / L * w, dx / L * w
        x, y = points[i]
        out.append(line(x - ox, y - oy, x + ox, y + oy, extra))
    return "".join(out)
