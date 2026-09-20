"""Icon registry.

An icon is a zero-argument function returning SVG elements drawn inside a
100x100 box. Stroke styling is inherited from the placing <g>, so icons only
describe geometry (plus the odd solid-black or white-fill accent).
"""

from __future__ import annotations

ICONS: dict[str, callable] = {}


def icon(name: str):
    def deco(fn):
        if name in ICONS:
            raise ValueError(f"duplicate icon name: {name}")
        ICONS[name] = fn
        return fn
    return deco


def render(name: str) -> str:
    try:
        return ICONS[name]()
    except KeyError:
        raise KeyError(f"unknown icon {name!r}") from None


def label(name: str) -> str:
    return name.replace("_", " ")
