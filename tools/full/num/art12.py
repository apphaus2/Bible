"""New drawings for Numbers chapter 12 (Numbers 25–26): Baal-peor at Shittim (an idol on a high place, the people bowing,
seen from afar), the hard sun over an empty plain (25:4–5 are told in captions only), the pavilion with its door shut and
Phinehas' spear (25:8 is never shown), the people weeping at the door of the tent, and the lot for the inheritance.
Phinehas: young, black beard, white headcloth with a gold band (a priest), crimson rim light."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, judges1 as J1
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from lev.art import altar
from num.art import ALL, TRIBE_C, wilderness_camp
def f(v): return f"{v:.1f}"
PHINEHAS = F("adam", skin="#C98E66", shadow="#5A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#F3EFE6", band=True, brow="scowl", light="#D7261E")
PHINEHAS_CALM = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#F3EFE6", band=True, light="#FFD23F")

def peor(p, w, h, seed):
    """Shittim: on a high place a carved idol of Baal-peor before an altar; the people bowing down to it, far off."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#C85A3A"></rect>', sun(w * 0.2, h * 0.2, 22, color="#FFC14D", op=0.4)]
    o.append(J1.palm(w * 0.06, h * 0.72, h / 360) + J1.palm(w * 0.94, h * 0.74, h / 380))
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.72)} L {f(w * 0.46)} {f(h * 0.42)} L {f(w * 0.6)} {f(h * 0.42)} L {f(w * 0.76)} {f(h * 0.72)} Z" fill="#6A3A2A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    ix, iy = w * 0.53, h * 0.42
    o.append(f'<path d="M{f(ix - 14)} {f(iy)} L {f(ix - 10)} {f(iy - h * 0.16)} L {f(ix - 18)} {f(iy - h * 0.2)} L {f(ix)} {f(iy - h * 0.26)} L {f(ix + 18)} {f(iy - h * 0.2)} L {f(ix + 10)} {f(iy - h * 0.16)} L {f(ix + 14)} {f(iy)} Z" fill="#B8862A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(altar(w * 0.44, h * 0.44, min(1.0, h / 320), fire=True, smoke=True))
    o.append(ground(w, h, h * 0.72, "#8A5A3A", dy=0))
    for i in range(10):
        x = w * (0.06 + i * 0.09); o.append(E.kneel(x, b - (i % 2) * 6, fit(b, h * 0.62) * 0.7, color=r.choice(A.HEBREW + ["#8A3A5A", "#C2456A"]), skin="#8A5A3E", flip=False))
    return "".join(o)

def hard_sun(w, h, seed):
    """Before the sun: a white sun high over an empty plain, the camp small beneath (no one is shown)."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#F3D8A0"></rect>', V.rays(w * 0.5, h * 0.22, 40, 30, max(w, h), color="#FFFFFF", op=0.45),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.22)}" r="{f(min(w, h) * 0.08)}" fill="#FFFFF0" stroke="#FFD23F" stroke-width="3"></circle>', ground(w, h, h * 0.7, "#D8B878", dy=0)]
    return "".join(o)

def pavilion(p, w, h, seed, phinehas=True, entering=False):
    """A pavilion (a domed tent) with its door: entering=True, the man of Israel and the Midianitish woman going in, as
    silhouettes; phinehas=True, Phinehas with his spear at the door (the door shut; nothing within is shown)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#3A1A2A"></rect>', ground(w, h, h * 0.62, "#4A2A2A", dy=0)]
    cx = w * 0.62
    o.append(f'<path d="M{f(cx - w * 0.26)} {f(b)} C {f(cx - w * 0.26)} {f(h * 0.2)} {f(cx + w * 0.26)} {f(h * 0.2)} {f(cx + w * 0.26)} {f(b)} Z" fill="#8A2A4A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             + "".join(f'<path d="M{f(cx + dx)} {f(h * 0.26)} C {f(cx + dx * 1.2)} {f(h * 0.5)} {f(cx + dx * 1.1)} {f(h * 0.8)} {f(cx + dx)} {f(b)}" fill="none" stroke="#5A1A2A" stroke-width="2"></path>' for dx in (-w * 0.14, 0, w * 0.14)))
    o.append(f'<path d="M{f(cx - w * 0.06)} {f(b)} L {f(cx - w * 0.06)} {f(h * 0.56)} C {f(cx - w * 0.04)} {f(h * 0.5)} {f(cx + w * 0.04)} {f(h * 0.5)} {f(cx + w * 0.06)} {f(h * 0.56)} L {f(cx + w * 0.06)} {f(b)} Z" fill="{"#FFC14D" if entering else "#2A0A1A"}" stroke="#0D0D0F" stroke-width="2"></path>')
    s = fit(b, h * 0.42)
    if entering:
        o.append(man(p, cx - w * 0.02, b, s * 0.9, "#0D0D0F") + woman(p, cx + w * 0.03, b, s * 0.86, "#0D0D0F"))
    if phinehas:
        x = w * 0.24
        o.append(Q.son_priest(p, x, b, s, up=[(-22, -158), (-6, -196), (8, -230)]))
        o.append(f'<path d="M{f(x + 8 * s)} {f(b - 30 * s)} L {f(x + 8 * s)} {f(b - 300 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path><path d="M{f(x + 8 * s)} {f(b - 300 * s)} l -8 24 l 16 0 z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def lots(w, h):
    """The land divided by lot: twelve tribe tokens drawn from an urn; to the more the more inheritance."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE LAND SHALL BE DIVIDED BY LOT")]
    ux, uy = w * 0.62, h * 0.86; s = min(1.4, h / 200)
    o.append(f'<path d="M{f(ux - 40 * s)} {f(uy)} C {f(ux - 60 * s)} {f(uy - 60 * s)} {f(ux - 40 * s)} {f(uy - 100 * s)} {f(ux - 24 * s)} {f(uy - 110 * s)} L {f(ux + 24 * s)} {f(uy - 110 * s)} C {f(ux + 40 * s)} {f(uy - 100 * s)} {f(ux + 60 * s)} {f(uy - 60 * s)} {f(ux + 40 * s)} {f(uy)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    names = ["REUBEN", "SIMEON", "GAD", "JUDAH", "ISSACHAR", "ZEBULUN", "MANASSEH", "EPHRAIM", "BENJAMIN", "DAN", "ASHER", "NAPHTALI"]
    for i, nm in enumerate(names):
        a = -math.pi * (0.1 + 0.8 * i / 11); r = 140 * s
        x, y = ux + r * math.cos(a), uy - 110 * s + r * math.sin(a) * 0.6
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(12 * s)}" fill="{TRIBE_C[nm]}" stroke="#0D0D0F" stroke-width="1.4"></circle>' + label(x, y - 16 * s, nm, B8.CY, 7))
    return "".join(o)
