"""Isaiah 10–12 drawings (on top of isa.art2): the Assyrian's march on Jerusalem (a map), the nest of the peoples' riches, the
axe and the saw, the forest few enough for a child to write, the shoot out of the stock of Jesse, the peaceable kingdom
(beast(): the wolf, the leopard and the bear), the outcasts gathered, the wells of salvation."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art2 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
import snake as SN

def beast(x, y, s=1.0, kind="wolf", flip=False):
    """A four-footed beast standing, facing right; (x, y) = the ground under its middle; about 100 units tall at s=1.
    kind: wolf (grey, pointed ears, long snout), leopard (tawny, black spots, long tail), bear (brown, heavy, round ears)."""
    sx = -s if flip else s
    col, dark = {"wolf": ("#8A8A90", "#5A5A60"), "leopard": ("#D8A040", "#8A5A1A"), "bear": ("#6A4426", "#3A2414")}[kind]
    heavy = kind == "bear"
    by, bh = (-74, 40) if heavy else (-66, 30)
    leg = lambda x0, x1: f'<path d="M{x0} {by + 10} L {x0 + 2} -2 L {x0 + 2} 0 L {x1} 0 L {x1} {by + 14} Z" fill="{col}" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">']
    if kind == "wolf": o.append(f'<path d="M-62 {by - 4} C -84 {by} -96 {by + 20} -98 {by + 44} C -88 {by + 34} -78 {by + 24} -64 {by + 12} Z" fill="{col}" stroke="#0D0D0F" stroke-width="2"></path>')
    if kind == "leopard": o.append(f'<path d="M-62 {by} C -90 {by + 6} -104 {by - 10} -100 {by - 40}" stroke="#0D0D0F" stroke-width="9" fill="none" stroke-linecap="round"></path><path d="M-62 {by} C -90 {by + 6} -104 {by - 10} -100 {by - 40}" stroke="{col}" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    o.append(leg(-58, -44) + leg(34, 48))
    o.append(f'<path d="M-66 {by + 4} C -70 {by - bh * 0.7} -40 {by - bh} 0 {by - bh} C 40 {by - bh} 62 {by - bh * 0.8} 64 {by} C 64 {by + bh * 0.5} 40 {by + bh * 0.6} 0 {by + bh * 0.6} C -40 {by + bh * 0.6} -64 {by + bh * 0.5} -66 {by + 4} Z" '
             f'fill="{col}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if kind == "leopard":
        r = random.Random(3)
        o.append("".join(f'<circle cx="{r.uniform(-56, 56):.0f}" cy="{r.uniform(by - bh * 0.7, by + bh * 0.4):.0f}" r="3.4" fill="none" stroke="#2A1A0A" stroke-width="2.2"></circle>' for _ in range(16)))
    o.append(leg(-48, -34) + leg(44, 58))
    hx, hy = 70, by - bh * 0.6
    if kind == "wolf":
        o.append(f'<path d="M50 {hy + 14} C 52 {hy - 8} 70 {hy - 16} 84 {hy - 8} L 112 {hy + 4} C 114 {hy + 10} 108 {hy + 14} 100 {hy + 14} L 80 {hy + 20} C 66 {hy + 26} 54 {hy + 24} 50 {hy + 14} Z" fill="{col}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<path d="M66 {hy - 6} L 70 {hy - 26} L 80 {hy - 10} Z" fill="{dark}" stroke="#0D0D0F" stroke-width="1.8"></path><circle cx="112" cy="{hy + 6}" r="3" fill="#0D0D0F"></circle><circle cx="86" cy="{hy}" r="2.4" fill="#FFD23F"></circle>')
    elif kind == "leopard":
        o.append(f'<path d="M52 {hy + 10} C 52 {hy - 10} 70 {hy - 16} 86 {hy - 10} C 98 {hy - 4} 102 {hy + 8} 98 {hy + 16} C 90 {hy + 24} 66 {hy + 26} 52 {hy + 10} Z" fill="{col}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<circle cx="68" cy="{hy - 14}" r="6" fill="{col}" stroke="#0D0D0F" stroke-width="1.8"></circle><circle cx="88" cy="{hy - 2}" r="2.4" fill="#0D0D0F"></circle><circle cx="98" cy="{hy + 10}" r="2.6" fill="#3A1A1A"></circle>'
                 f'<circle cx="74" cy="{hy + 6}" r="2.6" fill="none" stroke="#2A1A0A" stroke-width="1.8"></circle>')
    else:
        o.append(f'<path d="M48 {hy + 18} C 46 {hy - 8} 66 {hy - 18} 84 {hy - 10} C 96 {hy - 4} 104 {hy + 8} 102 {hy + 16} C 96 {hy + 26} 70 {hy + 30} 48 {hy + 18} Z" fill="{col}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<circle cx="64" cy="{hy - 12}" r="7" fill="{col}" stroke="#0D0D0F" stroke-width="1.8"></circle><circle cx="86" cy="{hy - 2}" r="2.4" fill="#0D0D0F"></circle><ellipse cx="100" cy="{hy + 12}" rx="5" ry="4" fill="#2A1A10"></ellipse>')
    o.append('</g>')
    return "".join(o)

# ---- Isaiah 10 ---------------------------------------------------------------------------------------------------------
MARCH = [("AIATH", 0.82, 0.12), ("MIGRON", 0.72, 0.2), ("MICHMASH", 0.66, 0.3), ("GEBA", 0.56, 0.36), ("RAMAH", 0.46, 0.3), ("GIBEAH OF SAUL", 0.4, 0.42),
         ("GALLIM", 0.3, 0.38), ("LAISHAH", 0.26, 0.5), ("ANATHOTH", 0.4, 0.56), ("MADMENAH", 0.3, 0.62), ("GEBIM", 0.42, 0.68), ("NOB", 0.34, 0.76)]
def march_map(w, h, upto=None):
    """He is come to Aiath, he is passed through Migron …: the Assyrian's march from Aiath to Nob as a technical map, the
    towns lit as he passes, and at Nob his hand shaken at the hill of Jerusalem."""
    o = [grid_bg(w, h)]
    pts = [(w * x, h * y) for _, x, y in MARCH]
    n = len(MARCH) if upto is None else upto
    o.append(route(pts[:n], color="#D7261E", sw=2.6))
    for i, (nm, x, y) in enumerate(MARCH):
        o.append(node(w * x, h * y, nm, "#D7261E" if i < n else "#8FD0E2", r=5, dy=-11, size=9))
    jx, jy = w * 0.22, h * 0.88
    o.append(f'<path d="M{f(jx - 50)} {f(jy + 14)} C {f(jx - 30)} {f(jy - 30)} {f(jx + 30)} {f(jy - 30)} {f(jx + 50)} {f(jy + 14)} Z" fill="#1F3A5A" stroke="#FFD23F" stroke-width="2"></path>'
             + node(jx, jy - 4, "JERUSALEM · THE MOUNT OF THE DAUGHTER OF ZION", "#FFD23F", r=6, dy=-24, size=9)
             + route([pts[-1], (jx + 30, jy - 14)], color="#FF8A6A", sw=1.6, dash="3 4"))
    return "".join(o)

def nest(w, h, seed):
    """My hand hath found as a nest the riches of the peoples; as one gathereth eggs that are forsaken: a nest in a bare
    tree full of gold and silver eggs, no bird moving the wing."""
    r = random.Random(seed)
    o = [bg(w, h, "#8A7A9A", "#E8D0B0"), ground(w, h, h * 0.86, "#8A7A5A", dy=0)]
    s = min(1.4, h / 200); cx, cy = w * 0.5, h * 0.6
    for a in (-0.9, -0.5, 0.4, 0.8):
        o.append(f'<path d="M{f(cx)} {f(cy + 20 * s)} L {f(cx + math.sin(a) * 200 * s)} {f(cy - math.cos(a) * 120 * s)}" stroke="#4A3A2A" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(cx)} {f(h)} L {f(cx)} {f(cy + 20 * s)}" stroke="#4A3A2A" stroke-width="{f(14 * s)}"></path>')
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(70 * s)}" ry="{f(26 * s)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>')
    for _ in range(18):
        a = r.uniform(0, math.pi * 2)
        o.append(f'<path d="M{f(cx + math.cos(a) * 66 * s)} {f(cy + math.sin(a) * 22 * s)} l {f(r.uniform(-14, 14) * s)} {f(r.uniform(-6, 6) * s)}" stroke="#5A3A1A" stroke-width="1.6"></path>')
    for i in range(7):
        ex = cx + (i - 3) * 16 * s; ey = cy - 8 * s - (i % 2) * 6 * s
        o.append(f'<ellipse cx="{f(ex)}" cy="{f(ey)}" rx="{f(9 * s)}" ry="{f(12 * s)}" fill="{"#E8B830" if i % 2 else "#D8D8E0"}" stroke="#0D0D0F" stroke-width="1.8"></ellipse>')
    return "".join(o)

def axe_saw(w, h):
    """Shall the axe boast itself against him that heweth therewith? shall the saw magnify itself against him that wieldeth
    it?: the axe, the saw, the rod and the staff on a plate, laid down."""
    o = [grid_bg(w, h)]
    s = min(1.2, h / 200); y = h * 0.6
    items = [("THE AXE", 0.14), ("THE SAW", 0.38), ("THE ROD", 0.62), ("THE STAFF", 0.86)]
    for nm, x in items:
        cx = w * x
        if nm == "THE AXE":
            o.append(f'<path d="M{f(cx - 50 * s)} {f(y + 20 * s)} L {f(cx + 40 * s)} {f(y - 30 * s)}" stroke="#8A5A2A" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>'
                     f'<path d="M{f(cx + 26 * s)} {f(y - 44 * s)} L {f(cx + 52 * s)} {f(y - 40 * s)} L {f(cx + 54 * s)} {f(y - 6 * s)} L {f(cx + 36 * s)} {f(y - 18 * s)} Z" fill="#C8D0D8" stroke="#8FD0E2" stroke-width="1.6"></path>')
        elif nm == "THE SAW":
            teeth = "".join(f"L {f(cx - 50 * s + k * 10 * s + 5 * s)} {f(y + 6 * s)} L {f(cx - 50 * s + (k + 1) * 10 * s)} {f(y)} " for k in range(10))
            o.append(f'<path d="M{f(cx - 50 * s)} {f(y)} {teeth} L {f(cx + 50 * s)} {f(y - 16 * s)} L {f(cx - 50 * s)} {f(y - 16 * s)} Z" fill="#C8D0D8" stroke="#8FD0E2" stroke-width="1.6"></path>'
                     f'<rect x="{f(cx + 48 * s)}" y="{f(y - 22 * s)}" width="{f(22 * s)}" height="{f(22 * s)}" rx="{f(4 * s)}" fill="#8A5A2A"></rect>')
        elif nm == "THE ROD":
            o.append(f'<path d="M{f(cx - 50 * s)} {f(y + 10 * s)} L {f(cx + 50 * s)} {f(y - 30 * s)}" stroke="#8A5A2A" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>')
        else:
            o.append(f'<path d="M{f(cx - 40 * s)} {f(y + 20 * s)} L {f(cx + 30 * s)} {f(y - 40 * s)} C {f(cx + 44 * s)} {f(y - 54 * s)} {f(cx + 54 * s)} {f(y - 36 * s)} {f(cx + 44 * s)} {f(y - 30 * s)}" stroke="#8A5A2A" stroke-width="{f(6 * s)}" fill="none" stroke-linecap="round"></path>')
        o.append(label(cx, y + 44 * s, nm, CYAN, 10))
    return "".join(o)

def few_trees(p, w, h, seed):
    """The remnant of the trees of his forest shall be few, so that a child may write them: a burned forest of stumps, three
    trees left standing, a child with a tablet counting them."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#6A5A6A", "#D8B898"), ground(w, h, h * 0.7, "#5A4A3A", dy=0)]
    for i in range(16):
        x = r.uniform(0, w); y = r.uniform(h * 0.72, h * 0.96); sc = min(1, h / 300) * r.uniform(0.6, 1.0)
        o.append(f'<path d="M{f(x - 10 * sc)} {f(y)} L {f(x - 8 * sc)} {f(y - 18 * sc)} L {f(x + 8 * sc)} {f(y - 18 * sc)} L {f(x + 10 * sc)} {f(y)} Z" fill="#2A1E1A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    for x in (0.56, 0.7, 0.86):
        o.append(J.oak(w * x, h * 0.76, min(0.7, h / 420), seed=int(x * 100)))
    s = fit(b, max(h * 0.55, b - 140))
    o.append(S1.boy(p, w * 0.3, b, s, up=[(-22, -158), (-8, -136), (10, -132)], extra='<rect x="4" y="-150" width="20" height="26" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></rect>'))
    return "".join(o)

def remnant_road(p, w, h, seed):
    """A remnant shall return, even the remnant of Jacob: a small company on the road up to Zion at morning; behind them the
    shore, its sand without number."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FB0D8", "#F3E0B0"), f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.4)} {f(h * 0.62)} L {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8"></path>',
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.4)} {f(h * 0.62)} L {f(w * 0.5)} {f(h * 0.62)} L {f(w * 0.44)} {f(h + 10)} Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="1.6"></path>',
         hills(w, h, h * 0.5, seed, color="#9AA07A", amp=10), J.city_hill(w * 0.86, h * 0.56, w * 0.14, h * 0.18, seed), ground(w, h, h * 0.66, "#C8B080", dy=0) if False else ""]
    o.append(f'<path d="M{f(w * 0.44)} {f(h + 10)} C {f(w * 0.6)} {f(h * 0.8)} {f(w * 0.7)} {f(h * 0.7)} {f(w * 0.84)} {f(h * 0.56)} L {f(w * 0.88)} {f(h * 0.56)} C {f(w * 0.8)} {f(h * 0.7)} {f(w * 0.74)} {f(h * 0.84)} {f(w + 10)} {f(h + 10)} Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></path>')
    s = fit(b, max(h * 0.55, b - 140))
    for i in range(6):
        t = i / 5; x = w * (0.52 + t * 0.26); y = b - t * (b - h * 0.66)
        o.append((man if i % 2 == 0 else woman)(p, x, y, s * (1 - t * 0.6), ["#5A4A6A", "#8A3A2A", "#3A5A6A", "#6A5A3A", "#7A3A5A", "#4A5A3A"][i]))
    return "".join(o)

def felled(w, h, seed):
    """He will lop the boughs with terror; the high of stature shall be hewn down, and Lebanon shall fall by a mighty one: the
    cedars of Lebanon lying felled on the mountainside, an axe in a stump."""
    r = random.Random(seed)
    o = [bg(w, h, "#6A7A9A", "#E8E0D0"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.6)} {f(h * 0.4)} L {f(w * 0.8)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A6A5A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.24)} {f(h * 0.18)} L {f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.36)} {f(h * 0.18)} Z M{f(w * 0.75)} {f(h * 0.26)} L {f(w * 0.8)} {f(h * 0.2)} L {f(w * 0.85)} {f(h * 0.26)} Z" fill="#F3EFE6"></path>',
         ground(w, h, h * 0.7, "#6A5A3A", dy=0)]
    s = min(1.0, h / 260)
    for i in range(5):
        x = w * (0.1 + i * 0.2) + r.uniform(-20, 20); y = h * (0.78 + (i % 2) * 0.08); a = r.choice([-14, -8, 8, 12])
        o.append(f'<g transform="rotate({a} {f(x)} {f(y)})"><rect x="{f(x - 90 * s)}" y="{f(y - 8 * s)}" width="{f(180 * s)}" height="{f(16 * s)}" rx="{f(8 * s)}" fill="#7A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(x + (k - 2) * 34 * s)} {f(y - 6 * s)} l {f(-16 * s)} {f(-22 * s)} l {f(32 * s)} 0 Z" fill="#1F4A34" stroke="#0D0D0F" stroke-width="1.2"></path>' for k in range(5)) + '</g>')
    o.append(f'<path d="M{f(w * 0.5 - 22 * s)} {f(h * 0.74)} L {f(w * 0.5 - 18 * s)} {f(h * 0.74 - 24 * s)} L {f(w * 0.5 + 18 * s)} {f(h * 0.74 - 24 * s)} L {f(w * 0.5 + 22 * s)} {f(h * 0.74)} Z" fill="#7A4A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.74 - 24 * s)} L {f(w * 0.5 + 30 * s)} {f(h * 0.74 - 60 * s)}" stroke="#8A5A2A" stroke-width="{f(5 * s)}"></path><path d="M{f(w * 0.5 - 6 * s)} {f(h * 0.74 - 32 * s)} L {f(w * 0.5 + 10 * s)} {f(h * 0.74 - 20 * s)} L {f(w * 0.5 + 2 * s)} {f(h * 0.74 - 14 * s)} Z" fill="#C8D0D8" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

# ---- Isaiah 11–12 ------------------------------------------------------------------------------------------------------
def peaceable(p, w, h, seed):
    """The wolf shall dwell with the lamb, and the leopard shall lie down with the kid; the calf and the young lion together;
    and a little child shall lead them; the cow and the bear shall feed; the sucking child shall play on the hole of the asp:
    all of them together on a green hill, in my holy mountain."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), bg(w, h, "#8FD0E2", "#F8F0D0"), V.rays(w * 0.5, -h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.25),
         hills(w, h, h * 0.5, seed, color="#8AB06A", amp=10), ground(w, h, h * 0.6, "#9CCB5E", dy=0)]
    s = min(0.62, h / 520)
    o.append(J2.lion(w * 0.12, b, s * 0.8, roar=False) + S1.calf(w * 0.27, b, s * 1.3))
    o.append(beast(w * 0.42, b - 4, s, "wolf") + E3.lamb(w * 0.5, b, s * 0.8))
    o.append(beast(w * 0.66, b, s, "leopard") + E.sheep(w * 0.74, b, s * 0.5, wool="#8A6A4A", face="#3A2A1A"))
    o.append(beast(w * 0.9, b - 2, s * 0.9, "bear", flip=True))
    cs = fit(b, max(h * 0.5, b - 120))
    o.append(S1.boy(p, w * 0.58, b + 2, cs, flip=True, up=[(-22, -158), (-34, -140), (-50, -134)]))
    o.append(f'<ellipse cx="{f(w * 0.84)}" cy="{f(b + 4)}" rx="{f(14 * s * 2)}" ry="{f(5 * s * 2)}" fill="#3A2A1A"></ellipse>'
             + SN.snake([(w * 0.84, b + 2), (w * 0.81, b - 8 * s * 2), (w * 0.79, b - 4 * s * 2), (w * 0.77, b - 12 * s * 2)], 4 * s * 2, f"as{seed}", head_scale=0.4))
    return "".join(o)

def gathering(w, h):
    """The Lord will set his hand again the second time to recover the remnant of his people from Assyria, and from Egypt, and
    from Pathros, and from Cush, and from Elam, and from Shinar, and from Hamath, and from the islands of the sea: arrows from
    every land in to Jerusalem."""
    src = ["NINEVEH", "EGYPT", "ETHIOPIA", "ELAM", "BABYLON", "HAMATH", "KITTIM"]
    return nations_map(w, h, hi=src, arrows=[(s_, "JERUSALEM") for s_ in src], lit="#FFD23F",
                       show=src + ["JERUSALEM", "DAMASCUS", "PHILISTIA", "MOAB", "EDOM"])

def wells(p, w, h, seed):
    """With joy shall ye draw water out of the wells of salvation: a stone well at morning, women drawing water and lifting
    their pitchers, the city of Zion on its hill behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FD0E2", "#FFF0C0"), V.rays(w * 0.8, h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         J.city_hill(w * 0.76, h * 0.6, w * 0.24, h * 0.3, seed), K1.temple_front(w * 0.76, h * 0.36, min(w * 0.1, h * 0.24), seed), ground(w, h, h * 0.62, "#C8B888", dy=0)]
    s = min(1.0, h / 300); cx = w * 0.36
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(b - 40 * s)}" rx="{f(60 * s)}" ry="{f(14 * s)}" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<path d="M{f(cx - 60 * s)} {f(b - 40 * s)} L {f(cx - 60 * s)} {f(b)} L {f(cx + 60 * s)} {f(b)} L {f(cx + 60 * s)} {f(b - 40 * s)}" fill="#B8A888" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(cx - 60 * s)} {f(b - k * 13 * s)} L {f(cx + 60 * s)} {f(b - k * 13 * s)}" stroke="#8A7A5A" stroke-width="1.4"></path>' for k in range(1, 3)))
    fs = fit(b, max(h * 0.55, b - 150))
    o.append(woman(p, cx - 90 * s, b, fs, "#C2456A", up=[(-22, -158), (-30, -190), (-20, -222)]) + woman(p, cx + 90 * s, b, fs, "#2E6B8A", flip=True)
             + woman(p, cx + 150 * s, b, fs * 0.94, "#E8B830", flip=True, up=[(-22, -158), (-34, -186), (-28, -214)]))
    return "".join(o)
