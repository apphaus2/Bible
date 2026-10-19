"""Drawings for Hosea chapter 3 (Hosea 9–14): the threshing-floor and the winepress, nettles in the tents, grapes in the
wilderness, the glory flown away like a bird from an empty cradle, the dried root, the wanderers, the luxuriant vine with
its altars and pillars, hemlock in the furrows, the calf carried to Assyria, the king as foam upon the water, thistles on
the altars, the fallow ground broken up, the child called out of Egypt, the cords and the yoke lifted, the doves coming
home, Beth-el's pillar, the heaps in the furrows, the morning cloud, the dew, the chaff and the smoke, the lion, the
leopard and the bear as emblems, Samaria dark, the road home, the olive-tree and Lebanon, the green fir-tree."""
from hos.art import *
from hos.art import f, K2
from hos.art2 import calf_broken, eagle, heifer, israel_map, FIELD
import random, math
import samuel4 as S4x, judges1 as J1y, judges2 as JG, egypt as EGx, samuel1 as S1x, exodus5 as V5
from sng.art import leopard
from job.art5 import east_wind, sheol_bars
from job.art2 import balances
from neh.art import ruins
from pro.art import two_ways
from pro.art4 import flocks
from kg1.art import feast_tents

def floor_press(w, h, seed):
    """The threshing-floor and the winepress shall not feed them: an empty threshing-floor and a dry winepress cut in the rock."""
    o = [land(w, h, seed, tone="grey", olives=1, horizon=0.4)]
    o.append(S4x.threshing_floor(w * 0.32, h * 0.84, w * 0.42) + J1y.winepress(w * 0.78, h * 0.84, w * 0.24, h * 0.16))
    return "".join(o)

def nettles_tents(w, h, seed):
    """Nettles shall possess their pleasant things of silver; thorns shall be in their tents: empty tents overgrown."""
    r = random.Random(seed)
    o = [land(w, h, seed, tone="grey", olives=0, horizon=0.44)]
    for i, x in enumerate((0.2, 0.5, 0.8)):
        cx, by = w * x, h * 0.84
        tw, th = w * 0.18, h * 0.26
        o.append(f'<path d="M{f(cx - tw / 2)} {f(by)} L {f(cx)} {f(by - th)} L {f(cx + tw / 2)} {f(by)} Z" fill="#4A3A2A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(cx - tw * 0.1)} {f(by)} L {f(cx)} {f(by - th * 0.6)} L {f(cx + tw * 0.1)} {f(by)} Z" fill="#1A1210"></path>')
    for i in range(70):
        x = r.uniform(0, w); y = r.uniform(h * 0.74, h)
        a = r.uniform(-2.4, -0.7); l = r.uniform(10, 22)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(math.cos(a) * l)} {f(math.sin(a) * l)}" stroke="#3A4A2A" stroke-width="2.2" stroke-linecap="round"></path>')
    return "".join(o)

def grapes_wilderness(w, h, seed):
    """I found Israel like grapes in the wilderness; your fathers as the first-ripe in the fig-tree: a vine with dark clusters
    in a dry land, a fig-tree beside it."""
    o = [wilderness(w, h, seed)]
    k = min(1.4, h / 260)
    cx, by = w * 0.36, h * 0.86
    o.append(f'<path d="M{f(cx)} {f(by)} C {f(cx - 10 * k)} {f(by - 40 * k)} {f(cx + 20 * k)} {f(by - 60 * k)} {f(cx)} {f(by - 90 * k)}" stroke="#5A3A22" stroke-width="{f(6 * k)}" fill="none"></path>')
    for i, (dx, dy) in enumerate(((-30, -86), (26, -76), (-6, -104), (34, -100), (-36, -60))):
        o.append(f'<ellipse cx="{f(cx + dx * k)}" cy="{f(by + dy * k)}" rx="{f(18 * k)}" ry="{f(10 * k)}" fill="#3A7A3A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    for (dx, dy) in ((-14, -70), (18, -62)):
        for j in range(7):
            o.append(f'<circle cx="{f(cx + (dx + (j % 3) * 5 - 5) * k)}" cy="{f(by + (dy + (j // 3) * 6) * k)}" r="{f(3.4 * k)}" fill="#4A1A4A" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    fx = w * 0.72
    o.append(tree(fx, h * 0.86, k, color="#4A7A3A", kind="round", seed=seed))
    for j in range(5): o.append(f'<circle cx="{f(fx + (j - 2) * 12 * k)}" cy="{f(h * 0.62 + (j % 2) * 10 * k)}" r="{f(4 * k)}" fill="#6A3A5A" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    return "".join(o)

def cradle(w, h, seed):
    """Their glory shall fly away like a bird: an empty cradle in a dark house, a bird going out at the window."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2E2A"></rect>',
         f'<rect x="{f(w * 0.6)}" y="{f(h * 0.12)}" width="{f(w * 0.2)}" height="{f(h * 0.36)}" fill="#8A9AB8" stroke="#0D0D0F" stroke-width="3"></rect>',
         f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4030" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.4, h / 220)
    cx, by = w * 0.34, h * 0.86
    o.append(f'<path d="M{f(cx - 50 * k)} {f(by - 30 * k)} C {f(cx - 40 * k)} {f(by)} {f(cx + 40 * k)} {f(by)} {f(cx + 50 * k)} {f(by - 30 * k)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - 60 * k)} {f(by)} C {f(cx - 30 * k)} {f(by - 12 * k)} {f(cx + 30 * k)} {f(by - 12 * k)} {f(cx + 60 * k)} {f(by)}" fill="none" stroke="#5A3A22" stroke-width="{f(4 * k)}"></path>'
             f'<path d="M{f(cx - 40 * k)} {f(by - 28 * k)} C {f(cx - 20 * k)} {f(by - 34 * k)} {f(cx + 20 * k)} {f(by - 34 * k)} {f(cx + 40 * k)} {f(by - 28 * k)}" fill="none" stroke="#E8E2D6" stroke-width="2"></path>')
    o.append(bird(w * 0.72, h * 0.26, 1.2, "#F3EFE6") + bird(w * 0.86, h * 0.16, 1.0, "#F3EFE6"))
    return "".join(o)

def dried_root(w, h, seed):
    """Ephraim is smitten, their root is dried up, they shall bear no fruit: a dead tree, its roots bare in cracked ground."""
    o = [wilderness(w, h, seed, tone="dusk")]
    k = min(1.4, h / 240)
    cx, by = w * 0.5, h * 0.78
    o.append(f'<path d="M{f(cx - 10 * k)} {f(by)} L {f(cx - 6 * k)} {f(by - 100 * k)} L {f(cx + 6 * k)} {f(by - 100 * k)} L {f(cx + 10 * k)} {f(by)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></path>')
    for a, l in ((-40, 50), (-140, 46), (-70, 40), (-110, 36)):
        o.append(f'<path d="M{f(cx)} {f(by - 80 * k)} l {f(math.cos(math.radians(a)) * l * k)} {f(math.sin(math.radians(a)) * l * k)}" stroke="#6A5A4A" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>')
    for a in (20, 60, 120, 160):
        o.append(f'<path d="M{f(cx)} {f(by)} l {f(math.cos(math.radians(a)) * 40 * k)} {f(math.sin(math.radians(a)) * 20 * k)}" stroke="#5A4A3A" stroke-width="{f(3 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def wanderers(p, w, h, seed):
    """Wanderers among the nations: a few figures with bundles going away along a road toward the far horizon."""
    o = [mk.defs(p, *ALL), wilderness(w, h, seed, tone="dusk")]
    b = h * 0.95
    for i in range(5):
        x = w * (0.14 + i * 0.16); y = b - i * h * 0.06
        s = fit(y, y - h * (0.4 - i * 0.05))
        o.append(man(p, x, y, s, ("#5A4A3A", "#6A5A4A", "#4A3A3A", "#7A6A5A", "#5A5A4A")[i], flip=False))
    return "".join(o)

def vine_altars(w, h, seed):
    """Israel is a luxuriant vine: vine rows heavy with fruit on the terraces; among them altars and goodly pillars."""
    o = [land(w, h, seed, olives=0, horizon=0.36), vine_rows(w, h, h * 0.58, h * 0.98, seed, rows=4, grapes=True)]
    k = min(1.2, h / 260)
    for i, x in enumerate((0.18, 0.5, 0.82)):
        if i % 2:
            o.append(f'<rect x="{f(w * x - 8 * k)}" y="{f(h * 0.4)}" width="{f(16 * k)}" height="{f(h * 0.2)}" fill="#C8BCA6" stroke="#0D0D0F" stroke-width="2"></rect>')
        else:
            o.append(f'<path d="M{f(w * x - 14 * k)} {f(h * 0.6)} L {f(w * x - 10 * k)} {f(h * 0.6 - 22 * k)} L {f(w * x + 10 * k)} {f(h * 0.6 - 22 * k)} L {f(w * x + 14 * k)} {f(h * 0.6)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>'
                     + E.flame(w * x, h * 0.6 - 22 * k, 6 * k, 12 * k, 1))
    return "".join(o)

def hemlock(w, h, seed):
    """Judgment springeth up as hemlock in the furrows of the field: plowed furrows, tall umbels of hemlock in them."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A9AA8", "#E8E0C8"), hills(w, h, h * 0.5, seed, "#8A8A5A", amp=10, step=100), ground(w, h, h * 0.6, "#8A6A4A", dy=0)]
    for i in range(8):
        y = h * (0.64 + i * 0.045)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 6)}" stroke="#5A3A22" stroke-width="2.4"></path>')
    for i in range(18):
        x = r.uniform(0.04, 0.96) * w; y = h * r.uniform(0.66, 0.98); hh = h * r.uniform(0.12, 0.24)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - hh)}" stroke="#4A6A3A" stroke-width="2"></path>'
                 + "".join(f'<path d="M{f(x)} {f(y - hh)} L {f(x + d * 3)} {f(y - hh - 8)}" stroke="#4A6A3A" stroke-width="1.2"></path><circle cx="{f(x + d * 3)}" cy="{f(y - hh - 8)}" r="2.2" fill="#F3EFE6"></circle>' for d in (-2, -1, 0, 1, 2)))
    return "".join(o)

def calf_carried(p, w, h, seed):
    """It also shall be carried unto Assyria for a present to king Jareb: the golden calf on a cart, drawn eastward by oxen."""
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="dusk", olives=0, horizon=0.4)]
    k = min(1.6, h / 220)
    o.append(S1x.team(w * 0.04, h * 0.94, k * 0.62))
    o.append(V5.calf(w * 0.08, h * 0.94 - 34 * k, k * 0.45, uid=f"cc{seed}", pedestal=False))
    o.append(label(w * 0.9, h * 0.3, "TO ASSYRIA →", "#F3EFE6", 10, anchor="end"))
    return "".join(o)

def foam(w, h, seed):
    """As for Samaria, her king is cut off, as foam upon the water: dark water, a fleck of foam carried off."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A3A5A", "#8A8AA8"), f'<rect x="-10" y="{f(h * 0.36)}" width="{f(w + 20)}" height="{f(h * 0.7)}" fill="#1F3A5A" stroke="#0D0D0F" stroke-width="2"></rect>']
    for i in range(10):
        y = h * (0.42 + i * 0.06)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 6)} {f(w * 0.6)} {f(y + 6)} {f(w + 10)} {f(y)}" fill="none" stroke="#3A5A7A" stroke-width="2"></path>')
    for i in range(14):
        o.append(f'<circle cx="{f(w * 0.56 + r.uniform(-30, 30))}" cy="{f(h * 0.6 + r.uniform(-8, 8))}" r="{f(r.uniform(2, 6))}" fill="#E8F6FA" stroke="#8FD0E2" stroke-width="0.8"></circle>')
    return "".join(o)

def thistle_altars(w, h, seed):
    """The high places of Aven destroyed: broken altars on the hill overgrown with thorn and thistle; the mountains above."""
    from job.art9 import thistles
    o = [thistles(w, h, seed)]
    k = min(1.2, h / 260)
    for i, x in enumerate((0.3, 0.62)):
        o.append(f'<path d="M{f(w * x - 20 * k)} {f(h * 0.82)} L {f(w * x - 14 * k)} {f(h * 0.82 - 24 * k)} L {f(w * x + 2 * k)} {f(h * 0.82 - 30 * k)} L {f(w * x + 20 * k)} {f(h * 0.82)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def plow(p, w, h, seed, rain=False):
    """Judah shall plow, Jacob shall break his clods; break up your fallow ground: a man plowing behind an ox; rain=True:
    rain coming over the field."""
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="grey" if rain else "day", olives=0, horizon=0.42)]
    for i in range(6):
        y = h * (0.74 + i * 0.04)
        o.append(f'<path d="M-10 {f(y)} L {f(w * 0.56)} {f(y)}" stroke="#6A4A2A" stroke-width="2.4"></path>')
    k = min(0.9, h / 360)
    o.append(S1x.cow(w * 0.7, h * 0.9, k, color="#8A5A30"))
    b = h * 0.95
    s = fit(b, b - h * 0.42)
    o.append(f'<path d="M{f(w * 0.58)} {f(h * 0.84)} L {f(w * 0.48)} {f(h * 0.9)} L {f(w * 0.46)} {f(h * 0.96)}" stroke="#5A3A22" stroke-width="4" fill="none"></path>')
    o.append(man(p, w * 0.42, b, s, "#6A5A3A", up=[(-22, -158), (-2, -130), (16, -114)]))
    if rain:
        r = random.Random(seed)
        o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(h * 0.1, h * 0.6))} l -5 14" stroke="#C8E8F0" stroke-width="1.4" opacity="0.7"></path>' for _ in range(60)))
    return "".join(o)

def child_egypt(p, w, h, seed):
    """When Israel was a child, then I loved him, and called my son out of Egypt: a child walking away from the pyramids
    toward the dawn."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8C890", "#FFE8C0"), V.rays(w * 0.9, h * 0.5, 30, 20, w * 0.8, color="#FFFFFF", op=0.25),
         EGx.pyramid(w * 0.14, h * 0.7, w * 0.22, h * 0.3), EGx.pyramid(w * 0.3, h * 0.7, w * 0.14, h * 0.2), ground(w, h, h * 0.7, "#D8B880", dy=0)]
    b = h * 0.92
    s = fit(b, b - h * 0.3)
    o.append(child_fig(p, w * 0.6, b, s, "#E8E2D6"))
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.92)} C {f(w * 0.44)} {f(h * 0.9)} {f(w * 0.5)} {f(h * 0.94)} {f(w * 0.58)} {f(h * 0.93)}" fill="none" stroke="#B89A6A" stroke-width="2" stroke-dasharray="6 6"></path>')
    return "".join(o)

def yoke_plate(w, h):
    """I drew them with cords of a man, with bands of love; as they that lift up the yoke on their jaws; I laid food before
    them: a plate of a yoke lifted from an ox's neck, the cords, a manger of food."""
    o = [grid_bg(w, h)]
    k = min(1.4, h / 160)
    cx, cy = w * 0.32, h * 0.56
    o.append(f'<path d="M{f(cx - 70 * k)} {f(cy - 30 * k)} C {f(cx - 40 * k)} {f(cy - 44 * k)} {f(cx + 40 * k)} {f(cy - 44 * k)} {f(cx + 70 * k)} {f(cy - 30 * k)}" fill="none" stroke="#C8A06A" stroke-width="{f(8 * k)}" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(cx + d * k)} {f(cy - 36 * k)} C {f(cx + (d - 10) * k)} {f(cy)} {f(cx + (d + 10) * k)} {f(cy)} {f(cx + d * k)} {f(cy - 36 * k)}" fill="none" stroke="#C8A06A" stroke-width="2"></path>' for d in (-40, 40))
             + route([(cx, cy + 20 * k), (cx, cy - 60 * k)], color="#FFD23F") + label(cx, h * 0.84, "THE YOKE LIFTED", CYAN, 9))
    o.append(f'<path d="M{f(w * 0.5)} {f(cy)} C {f(w * 0.56)} {f(cy - 30 * k)} {f(w * 0.6)} {f(cy + 30 * k)} {f(w * 0.66)} {f(cy)}" fill="none" stroke="#FF8A6A" stroke-width="2.4"></path>'
             + label(w * 0.58, h * 0.84, "CORDS OF A MAN · BANDS OF LOVE", "#FF8A6A", 8))
    mx = w * 0.84
    o.append(f'<path d="M{f(mx - 40 * k)} {f(cy - 10 * k)} L {f(mx + 40 * k)} {f(cy - 10 * k)} L {f(mx + 30 * k)} {f(cy + 20 * k)} L {f(mx - 30 * k)} {f(cy + 20 * k)} Z" fill="#E8C88A" fill-opacity="0.3" stroke="#E8C88A" stroke-width="2"></path>'
             + label(mx, h * 0.84, "FOOD LAID BEFORE THEM", "#E8C88A", 8))
    return "".join(o)

def doves_home(w, h, seed):
    """They shall come trembling as a bird out of Egypt, and as a dove out of the land of Assyria, to dwell in their houses:
    a map with the doves flying home from both sides; the lion's roar as rings."""
    o = [israel_map(w, h, ("SAMARIA", "JERUSALEM"))]
    o.append(node(w * 0.06, h * 0.9, "EGYPT", "#FFD23F", r=5, dy=-10, size=9) + node(w * 0.94, h * 0.12, "ASSYRIA", "#FFD23F", r=5, dy=18, size=9))
    o.append(route([(w * 0.08, h * 0.86), (w * 0.44, h * 0.56)], color="#8FD0E2") + route([(w * 0.92, h * 0.16), (w * 0.5, h * 0.42)], color="#8FD0E2"))
    k = min(1.0, h / 220)
    o.append(sdove(w * 0.24, h * 0.72, k * 0.5) + sdove(w * 0.72, h * 0.28, k * 0.5, flip=True))
    for i in range(3):
        o.append(f'<circle cx="{f(w * 0.48)}" cy="{f(h * 0.5)}" r="{f((30 + i * 26) * k)}" fill="none" stroke="#FFD23F" stroke-width="1.4" opacity="{0.6 - i * 0.15}"></circle>')
    return "".join(o)

def bethel(w, h, seed):
    """He found him at Beth-el, and there he spake with us: a stone set up for a pillar on the hill under the stars."""
    o = [K2.sky(w, h, "#0F0E2A", "#3A2A5A"), mk.stars(70, w, h * 0.6, seed), hills(w, h, h * 0.66, seed, "#2A2230", amp=12, step=90), ground(w, h, h * 0.78, "#3A3034", dy=0)]
    k = min(1.4, h / 240)
    cx, by = w * 0.5, h * 0.8
    o.append(f'<path d="M{f(cx - 14 * k)} {f(by)} L {f(cx - 12 * k)} {f(by - 70 * k)} C {f(cx - 8 * k)} {f(by - 80 * k)} {f(cx + 8 * k)} {f(by - 80 * k)} {f(cx + 12 * k)} {f(by - 70 * k)} L {f(cx + 14 * k)} {f(by)} Z" fill="#8A847A" stroke="#0D0D0F" stroke-width="2"></path>'
             + V.rays(cx, by - 120 * k, 20, 10, h * 0.5, color="#FFF4C2", op=0.15))
    return "".join(o)

def heaps(w, h, seed):
    """Their altars are as heaps in the furrows of the field: plowed furrows with heaps of stones along them."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A9AA8", "#E8E0C8"),hills(w, h, h * 0.5, seed, "#8A8A5A", amp=10, step=100), ground(w, h, h * 0.6, "#8A6A4A", dy=0)]
    for i in range(8):
        y = h * (0.64 + i * 0.045)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 6)}" stroke="#5A3A22" stroke-width="2.4"></path>')
    for i in range(6):
        x = w * (0.1 + i * 0.16); y = h * (0.7 + (i % 3) * 0.1)
        for j in range(7):
            o.append(f'<ellipse cx="{f(x + r.uniform(-14, 14))}" cy="{f(y - r.uniform(0, 12))}" rx="7" ry="5" fill="{r.choice(("#A89E92", "#8A8478", "#B8AE9E"))}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    return "".join(o)

def vanish(w, h, seed):
    """As the morning cloud, as the dew that passeth early away, as the chaff driven with the whirlwind out of the
    threshing-floor, as the smoke out of the chimney: four plates, each going away."""
    o = [grid_bg(w, h)]
    k = min(1.2, h / 160)
    for i, t in enumerate(("THE MORNING CLOUD", "THE DEW", "THE CHAFF", "THE SMOKE")):
        cx = w * (0.13 + i * 0.25); cy = h * 0.46
        o.append(f'<rect x="{f(cx - w * 0.11)}" y="{f(h * 0.16)}" width="{f(w * 0.22)}" height="{f(h * 0.7)}" fill="none" stroke="#1E5A7A" stroke-width="1.4"></rect>')
        if i == 0: o.append("".join(f'<ellipse cx="{f(cx + d * 14 * k)}" cy="{f(cy - abs(d) * 4)}" rx="{f(18 * k)}" ry="{f(10 * k)}" fill="#E8E2D6" fill-opacity="{0.6 - abs(d) * 0.2}"></ellipse>' for d in (-1, 0, 1)))
        if i == 1: o.append("".join(f'<circle cx="{f(cx + d * 12 * k)}" cy="{f(cy + (d % 2) * 10)}" r="{f(4 * k)}" fill="#8FD0E2" opacity="{0.9 - abs(d) * 0.25}"></circle>' for d in (-2, -1, 0, 1, 2)))
        if i == 2: o.append("".join(f'<path d="M{f(cx - 30 * k + j * 9 * k)} {f(cy + 10 * k - j * 4 * k)} l {f(6 * k)} {f(-2 * k)}" stroke="#E8C88A" stroke-width="2.2"></path>' for j in range(8)))
        if i == 3: o.append(f'<rect x="{f(cx - 8 * k)}" y="{f(cy + 6 * k)}" width="{f(16 * k)}" height="{f(30 * k)}" fill="#8A6A4A" stroke="#C8A06A" stroke-width="1.4"></rect>' + smoke(cx, cy + 2 * k, 4, seed, color="#C8C2B6", op=0.5, k=k * 0.5))
        o.append(label(cx, h * 0.1, t, CYAN, max(7, min(9, 8 * k))))
    return "".join(o)

def three_beasts(w, h, seed):
    """As a lion, as a leopard by the way, as a bear bereaved of her whelps: three beasts as emblems on the dark field."""
    o = [heraldic(w, h, seed)]
    k = min(h / 300, w / 900)
    o.append(JG.lion(w * 0.04, h * 0.9, k, roar=True))
    o.append(leopard(w * 0.52, h * 0.86, k * 1.6))
    d = "M-60 0 L -54 -22 C -72 -44 -56 -78 -22 -80 C 12 -84 38 -70 50 -54 C 64 -56 78 -46 78 -36 C 78 -26 68 -22 60 -24 L 52 -14 L 54 0 L 42 0 L 38 -16 L -32 -16 L -34 0 Z"
    o.append(f'<g transform="translate({f(w * 0.84)} {f(h * 0.88)}) scale({f(-k * 1.6)} {f(k * 1.6)})"><path d="{d}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="{f(2.4 / (k * 1.6))}" stroke-linejoin="round"></path><circle cx="66" cy="-40" r="2.4" fill="#0D0D0F"></circle><circle cx="46" cy="-64" r="7" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.4"></circle><ellipse cx="76" cy="-32" rx="5" ry="4" fill="#2A1A10"></ellipse>'
             + "".join(f'<path d="M{a} 0 l -3 5 M{a + 5} 0 l 0 6 M{a + 10} 0 l 3 5" stroke="#0D0D0F" stroke-width="1.4"></path>' for a in (-34, 42)) + '</g>')
    o.append(label(w * 0.14, h * 0.12, "A LION", CYAN, 9) + label(w * 0.5, h * 0.12, "A LEOPARD", CYAN, 9) + label(w * 0.84, h * 0.12, "A BEAR", CYAN, 9))
    return "".join(o)

def samaria_dark(w, h, seed):
    """Samaria shall bear her guilt: the city on its hill under a dark sky, its gate empty (no one drawn); the east wind and
    the dried fountain."""
    o = [K2.sky(w, h, "#1A1220", "#5A3A3A"), J.city_hill(w * 0.5, h * 0.84, w * 0.36, h * 0.4, seed), ground(w, h, h * 0.84, "#2A2220", dy=0)]
    o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0F0E2A" opacity="0.35"></rect>')
    for i in range(5):
        y = h * (0.14 + i * 0.07)
        o.append(f'<path d="M{f(w + 10)} {f(y)} C {f(w * 0.6)} {f(y - 14)} {f(w * 0.3)} {f(y + 14)} -10 {f(y)}" fill="none" stroke="#C8A890" stroke-width="1.6" opacity="0.4" stroke-dasharray="14 10"></path>')
    return "".join(o)

def return_road(p, w, h, seed):
    """O Israel, return unto Jehovah thy God: a road winding home through the hills at dawn, a man walking it."""
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="dawn", olives=2, horizon=0.4)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.76)} {f(w * 0.64)} {f(h * 0.62)} L {f(w * 0.66)} {f(h * 0.62)} C {f(w * 0.66)} {f(h * 0.78)} {f(w * 0.46)} {f(h * 0.86)} {f(w * 0.42)} {f(h + 10)} Z" fill="#D8C090" stroke="#0D0D0F" stroke-width="1.6"></path>')
    b = h * 0.86
    o.append(man(p, w * 0.52, b, fit(b, b - h * 0.32), "#6A5A4A"))
    return "".join(o)

def olive_lebanon(w, h, seed):
    """His branches shall spread, and his beauty shall be as the olive-tree, and his smell as Lebanon: Lebanon's snowy peaks
    behind, a great olive-tree in front, grain and vines below."""
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8")]
    for i, (x, ht) in enumerate(((0.5, 0.5), (0.72, 0.62), (0.92, 0.46))):
        cx, by = w * x, h * 0.62
        o.append(f'<path d="M{f(cx - w * 0.2)} {f(by)} L {f(cx)} {f(by - h * ht)} L {f(cx + w * 0.2)} {f(by)} Z" fill="#6A7A8A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(cx - w * 0.06)} {f(by - h * ht * 0.7)} L {f(cx)} {f(by - h * ht)} L {f(cx + w * 0.06)} {f(by - h * ht * 0.7)} L {f(cx + w * 0.02)} {f(by - h * ht * 0.74)} L {f(cx - w * 0.02)} {f(by - h * ht * 0.68)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(label(w * 0.72, h * 0.08, "LEBANON", "#3A4A5A", 9))
    o.append(ground(w, h, h * 0.62, "#8A9A5A", dy=0) + vine_rows(w, h, h * 0.74, h * 0.98, seed, rows=3, grapes=True))
    k = min(2.6, h / 120)
    o.append(olive(w * 0.2, h * 0.96, k, seed))
    return "".join(o)

def fir(w, h, seed):
    """I am like a green fir-tree; from me is thy fruit found: one tall evergreen on the hill, full and green."""
    o = [land(w, h, seed, tone="day", olives=0, horizon=0.5)]
    cx, by = w * 0.5, h * 0.9
    th = h * 0.8; tw = min(w * 0.3, th * 0.5)
    o.append(f'<rect x="{f(cx - tw * 0.05)}" y="{f(by - th * 0.16)}" width="{f(tw * 0.1)}" height="{f(th * 0.16)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(5):
        y0 = by - th * 0.12 - i * th * 0.17; ww = tw * (1 - i * 0.17)
        o.append(f'<path d="M{f(cx - ww / 2)} {f(y0)} L {f(cx)} {f(y0 - th * 0.3)} L {f(cx + ww / 2)} {f(y0)} Z" fill="{("#1F4A34", "#2E6B3A", "#2A5A3A")[i % 3]}" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)
