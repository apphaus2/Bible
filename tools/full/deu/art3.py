"""Drawings for Deuteronomy chapter 3 (Deuteronomy 5–6): the two tables of stone glowing on the mount, the people afar
off from the burning mountain, and the words upon the door-posts of the house and upon the gates (6:9), with a father
teaching his son at the table (6:7, 6:20)."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus4 as E4, exodus5 as V
from genesis.art2 import fit, ground, hills
from genesis.art3 import label, man, woman, sun
from exo import art as A
from num.art import ALL
def f(v): return f"{v:.1f}"

def tables(w, h, seed):
    """The two tables of stone, written on the mount out of the midst of the fire."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#1A0E1E"></rect>', V.rays(w * 0.5, h * 0.5, 40, 30, max(w, h), color="#FFC14D", op=0.25)]
    o.append(V.tables(w * 0.5, h * 0.92, min(1.6, h / 260), uid=f"tb{seed}", glow=True))
    return "".join(o)

def afar(p, w, h, seed):
    """The heads of the tribes and the elders drawn back from the mountain burning with fire, the darkness over it."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#2A0A0A"></rect>', E4.sinai(w * 0.66, h * 0.7, w * 0.8, h * 0.62, seed, fire=True), ground(w, h, h * 0.7, "#3A2A2A", dy=0)]
    for i in range(9):
        x = w * (0.04 + i * 0.06); o.append(A.elder(r.choice(A.CLOTHS), i)(p, x, b - (i % 2) * 6, fit(b, h * 0.5), up=[(-22, -158), (-10, -150), (6, -150)] if i % 3 == 0 else None))
    return "".join(o)

def doorposts(p, w, h, seed):
    """A house door with the words written upon the door-posts; a father teaching his son at the threshold."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.16, 14, op=0.25), ground(w, h, h * 0.8, "#C8A06A", dy=0)]
    dx = w * 0.6
    o.append(f'<rect x="{f(dx - w * 0.26)}" y="{f(h * 0.14)}" width="{f(w * 0.52)}" height="{f(h * 0.7)}" fill="#C8B090" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    o.append(f'<rect x="{f(dx - w * 0.09)}" y="{f(h * 0.34)}" width="{f(w * 0.18)}" height="{f(h * 0.5)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>')
    for side in (-1, 1):
        x = dx + side * w * 0.12
        o.append(f'<rect x="{f(x - 7)}" y="{f(h * 0.4)}" width="14" height="{f(h * 0.12)}" rx="3" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 + "".join(f'<path d="M{f(x - 4)} {f(h * 0.42 + i * 6)} L {f(x + 4)} {f(h * 0.42 + i * 6)}" stroke="#5A4A3A" stroke-width="1"></path>' for i in range(int(h * 0.1 / 6))))
    s = fit(b, h * 0.42)
    o.append(man(p, w * 0.14, b, s, "#5A3A22", up=[(-22, -158), (8, -150), (30, -140)]))
    o.append(man(p, w * 0.28, b, s * 0.62, "#8A6A4A", flip=True))
    return "".join(o)

def household(p, w, h, seed):
    """When thy son asketh thee: a family about the table by lamplight (the Exodus passover scene)."""
    from exo import art3 as A3
    return mk.defs(p, *ALL) + A3.household_meal(p, w, h, seed)
