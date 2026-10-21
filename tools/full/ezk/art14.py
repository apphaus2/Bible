"""Drawings for Ezekiel 38–39: Gog of the land of Magog and his hordes as a map — Meshech, Tubal, Persia, Cush, Put, Gomer,
Togarmah from the uttermost parts of the north — coming like a storm and a cloud over the land of unwalled villages; the
great shaking, the hailstones, fire and brimstone over the mountains (no one drawn); the bow smitten out of his hand; the
weapons burned seven years; the valley of Hamon-gog and the signs set up by the bones; the birds called to the feast words
only over an empty field with birds gathering in the sky; and the captivity brought back."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art13 import *
from ezk.art13 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1, bone

GOG = {"MAGOG": (0.62, 0.06), "MESHECH": (0.46, 0.1), "TUBAL": (0.34, 0.14), "GOMER": (0.2, 0.08), "TOGARMAH": (0.74, 0.16), "PERSIA": (0.92, 0.42),
       "CUSH": (0.3, 0.96), "PUT": (0.08, 0.86)}
def gog_map(w, h, stage=0):
    """Gog of the land of Magog, the prince of Rosh, Meshech and Tubal, with Persia, Cush and Put, Gomer and Togarmah, coming
    out of the uttermost parts of the north upon the mountains of Israel as a technical map (stage 1: the hordes converging as
    a cloud upon the land; Sheba, Dedan and Tarshish watching)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.12)} {f(h * 0.4)} {f(w * 0.24)} {f(h * 0.5)} {f(w * 0.28)} {f(h * 0.66)} L {f(w * 0.22)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    I0 = (w * 0.42, h * 0.62)
    o.append(f'<ellipse cx="{f(I0[0])}" cy="{f(I0[1])}" rx="{f(w * 0.08)}" ry="{f(h * 0.12)}" fill="#FFD23F" fill-opacity="0.15" stroke="#FFD23F" stroke-width="2"></ellipse>'
             + label(I0[0], I0[1] + 4, "THE MOUNTAINS OF ISRAEL", "#FFD23F", 8))
    for nm, (x, y) in GOG.items():
        o.append(route([(w * x, h * y), (I0[0] + (w * x - I0[0]) * 0.18, I0[1] + (h * y - I0[1]) * 0.18)], color="#D7261E", sw=2.4 if stage else 1.6, dash="7 5"))
        o.append(node(w * x, h * y, nm, "#FF8A6A" if nm != "MAGOG" else "#D7261E", r=5 if nm != "MAGOG" else 7, dy=-11, size=9 if nm != "MAGOG" else 11))
    if stage:
        o.append(f'<ellipse cx="{f(I0[0])}" cy="{f(I0[1] - h * 0.1)}" rx="{f(w * 0.22)}" ry="{f(h * 0.14)}" fill="#D7261E" fill-opacity="0.12" stroke="#D7261E" stroke-width="1.6" stroke-dasharray="4 4"></ellipse>')
        for nm, (x, y) in (("SHEBA", (0.64, 0.94)), ("DEDAN", (0.76, 0.86)), ("TARSHISH", (0.04, 0.5))):
            o.append(node(w * x, h * y, nm, "#8FD0E2", r=4, dy=-10, size=8))
    return "".join(o)

def hordes(p, w, h, seed):
    """All thine army, horses and horsemen, all of them clothed in full armor, a great company with buckler and shield, all
    of them handling swords: the host of the north on the march under a storm cloud, far off."""
    o = [mk.defs(p, *ALL), bg(f"hd{seed}", w, h, [(0, "#1A1A2A"), (1, "#8A6A5A")]), clouds(w, h * 0.1, seed, n=8, color="#2A2A3A", op=0.95, ry=0.08), hills(w, h, h * 0.58, seed, "#5A4A4A", amp=12, step=70),
         ground(w, h, h * 0.66, "#7A6A5A", dy=0)]
    s = min(fit(h * 0.98, h * 0.62), 0.7)
    for i in range(14):
        x = w * (0.03 + i * 0.07); y = h * (0.94 + (i % 3) * 0.02)
        o.append(warrior(p, x, y, s, ["#4A3A3A", "#3A3A4A", "#5A4A3A"][i % 3]))
    for i in range(2): o.append(E3.chariot(w * (0.3 + i * 0.4), h * 0.78, min(0.6, h / 500), color="#2A1A10", driver="#3A3A4A"))
    return "".join(o)

def unwalled(p, w, h, seed):
    """The land of unwalled villages, them that are at rest, that dwell securely, without bars or gates: villages among green
    hills, flocks, no wall."""
    o = [mk.defs(p, *ALL), mountains(w, h, seed, "fruitful")]
    for i in range(5): o.append(house(w * (0.08 + i * 0.18), h * (0.86 + (i % 2) * 0.04), w * 0.09, h * 0.1, color="#C8A878"))
    return "".join(o)

def gog_storm(w, h, seed):
    """Thou shalt come like a storm, thou shalt be like a cloud to cover the land: a vast dark cloud rolling down from the
    north over the mountains of Israel."""
    o = [mountains(w, h, seed, "fruitful")]
    o.append(f'<rect x="-10" y="-1500" width="{f(w + 20)}" height="{f(h * 0.45 + 1500)}" fill="#1A1A2A" opacity="0.7"></rect>')
    o.append(clouds(w, h * 0.16, seed, n=10, color="#2A2A3A", op=0.95, ry=0.1) + clouds(w, h * 0.32, seed + 1, n=8, color="#3A3040", op=0.9, ry=0.08))
    o.append(wind_lines(w, h, seed, n=8, color="#C8C0D8", op=0.4, y0=0.3, y1=0.7))
    return "".join(o)

def shaking(w, h, seed):
    """A great shaking in the land of Israel: the mountains thrown down, the steep places falling, every wall fallen to the
    ground, and great hailstones, fire and brimstone rained upon the hordes — over empty mountains, no one drawn."""
    o = [bg(f"sk{seed}", w, h, [(0, "#1A0A0A"), (1, "#8A3A1A")])]
    for layer, col in enumerate(("#5A3A2A", "#4A2A1A")):
        svg, pk = ridge(w, h, h * (0.5 + layer * 0.2), 3 + layer, seed + layer, h * 0.18, col)
        o.append(svg)
    for i in range(4):
        x = w * (0.1 + i * 0.26)
        o.append(f'<path d="M{f(x)} {f(h * 0.4)} l {f(w * 0.02)} {f(h * 0.12)} l {f(-w * 0.03)} {f(h * 0.1)} l {f(w * 0.02)} {f(h * 0.14)}" stroke="#FFB04A" stroke-width="2.4" fill="none"></path>')
    o.append(E2.hail(30, 0, w, h * 0.05, h * 0.7, seed))
    for i in range(5):
        o.append(f'<g opacity="0.85">' + E.flame(w * (0.1 + i * 0.2), h * 0.4 + (i % 2) * h * 0.1, w * 0.03, h * 0.12, 4) + '</g>')
    o.append(bolts(w, h, seed, 2, 0.0, 0.4))
    return "".join(o)

def bow_smitten(w, h, seed):
    """I will smite thy bow out of thy left hand, and will cause thine arrows to fall out of thy right hand: a bow and arrows
    fallen on the stones of the mountain, broken."""
    r = random.Random(seed)
    o = [bg(f"bs{seed}", w, h, [(0, "#3A3A4A"), (1, "#A89A8A")]), ground(w, h, h * 0.42, "#7A6A5A", dy=0)]
    k = min(2.6, h / 130)
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.86)} Q {f(w * 0.36)} {f(h * 0.6)} {f(w * 0.48)} {f(h * 0.7)}" stroke="#0D0D0F" stroke-width="{f(8 * k)}" fill="none"></path><path d="M{f(w * 0.2)} {f(h * 0.86)} Q {f(w * 0.36)} {f(h * 0.6)} {f(w * 0.48)} {f(h * 0.7)}" stroke="#8A5A30" stroke-width="{f(5 * k)}" fill="none"></path>'
             f'<path d="M{f(w * 0.2)} {f(h * 0.86)} L {f(w * 0.3)} {f(h * 0.8)}" stroke="#E8E2D6" stroke-width="1.4"></path>')
    for i in range(6):
        x = w * (0.52 + i * 0.07); a = r.uniform(-0.4, 0.4)
        o.append(f'<path d="M{f(x)} {f(h * 0.88)} l {f(math.cos(a) * 60 * k)} {f(math.sin(a) * 20 * k - 10)}" stroke="#C8A878" stroke-width="{f(2 * k)}"></path>')
    for _ in range(6): o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(0.7, 0.98))}" rx="{f(r.uniform(12, 30))}" ry="{f(r.uniform(6, 12))}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    return "".join(o)

def weapon_fires(p, w, h, seed):
    """They that dwell in the cities of Israel shall go forth and make fires of the weapons, the shields and the bucklers, the
    bows and the arrows, the handstaves and the spears, seven years: heaps of weapons burning outside a city, people tending them."""
    o = [mk.defs(p, *ALL), bg(f"wf{seed}", w, h, [(0, "#2A2A4A"), (1, "#E8A070")]), J.city_hill(w * 0.84, h * 0.62, w * 0.18, h * 0.2, seed), ground(w, h, h * 0.62, "#9A8A6A", dy=0)]
    r = random.Random(seed)
    for i in range(3):
        cx = w * (0.16 + i * 0.26)
        for _ in range(6):
            a = r.uniform(-0.8, 0.8)
            o.append(f'<path d="M{f(cx)} {f(h * 0.9)} l {f(math.sin(a) * 50)} {f(-math.cos(a) * 30)}" stroke="#5A3A1A" stroke-width="4"></path>')
        o.append(f'<circle cx="{f(cx - 20)}" cy="{f(h * 0.88)}" r="{f(h * 0.04)}" fill="#B8863E" stroke="{INK}" stroke-width="1.6"></circle>')
        o.append(E.blaze(cx, h * 0.92, w * 0.12, h * 0.2, seed + i, n=5))
        o.append(smoke(cx, h * 0.6, 5, seed + i, color="#5A5A5A", op=0.4, k=h / 400))
    s = min(h * 0.44 / 200, 0.7)
    o.append(man(p, w * 0.06, h * 0.96, s, "#5A4A3A") + man(p, w * 0.94, h * 0.96, s, "#3A4A5A", flip=True))
    return "".join(o)

def hamon_gog(p, w, h, seed):
    """The valley of them that pass through on the east of the sea, the valley of Hamon-gog: men passing through the land, and
    where any seeth a man's bone a sign set up by it (a cairn with a pole), till the buriers have buried it; the city Hamonah."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(f"hg{seed}", w, h, [(0, "#4A5A7A"), (1, "#E8C8A0")]), hills(w, h, h * 0.5, seed, "#8A7A6A", amp=10, step=80), ground(w, h, h * 0.58, "#B8A07A", dy=0)]
    o.append(f'<ellipse cx="{f(w * 0.92)}" cy="{f(h * 0.56)}" rx="{f(w * 0.12)}" ry="{f(h * 0.04)}" fill="#3A7A9A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(J.city_hill(w * 0.12, h * 0.6, w * 0.12, h * 0.12, seed))
    for i in range(5):
        x = w * (0.22 + i * 0.15); y = h * (0.76 + (i % 2) * 0.12)
        o.append(f'<path d="M{f(x - 10)} {f(y)} L {f(x)} {f(y - 12)} L {f(x + 10)} {f(y)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="1.4"></path>'
                 f'<path d="M{f(x)} {f(y - 10)} L {f(x)} {f(y - 50)}" stroke="#5A3A1A" stroke-width="3"></path><path d="M{f(x)} {f(y - 50)} l 16 5 l -16 5" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></path>')
    s = min(h * 0.4 / 200, 0.7)
    o.append(man(p, w * 0.86, h * 0.96, s, "#6A5A4A", flip=True))
    return "".join(o)

def birds_gather(w, h, seed):
    """Speak unto the birds of every sort, and to every beast of the field: Assemble yourselves — birds gathering in a great
    wheel in the sky over an empty field on the mountains of Israel (words only)."""
    r = random.Random(seed)
    o = [bg(f"bg{seed}", w, h, [(0, "#3A2A3A"), (1, "#E8A070")]), hills(w, h, h * 0.66, seed, "#6A5A4A", amp=12, step=70), ground(w, h, h * 0.76, "#8A7A5A", dy=0)]
    cx, cy = w * 0.5, h * 0.36
    for i in range(28):
        a = r.uniform(0, 2 * math.pi); d = r.uniform(0.2, 1.0)
        x, y = cx + math.cos(a) * w * 0.4 * d, cy + math.sin(a) * h * 0.24 * d
        k = r.uniform(0.6, 1.2) * min(1.2, h / 260)
        o.append(f'<path d="M{f(x - 12 * k)} {f(y)} q {f(6 * k)} {f(-8 * k)} {f(12 * k)} 0 q {f(6 * k)} {f(-8 * k)} {f(12 * k)} 0" stroke="#1A1010" stroke-width="{f(2.4 * k)}" fill="none"></path>')
    return "".join(o)
