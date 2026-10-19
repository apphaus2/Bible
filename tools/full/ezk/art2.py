"""Drawings for Ezekiel 4–7 (the signs of the siege, the mountains of Israel, the end), and the general scenes the rest of the
book reuses: jerusalem() (the city on its hill: day, dusk, night, siege, burning, empty), mountains() (the mountains of
Israel: high places, broken, fruitful, desolate), lying() (Ezekiel lying on his side), and the plates of the signs.
Restraint: the slain are never drawn — words over broken altars, smoke and empty streets."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art import *
from ezk.art import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad
import kg2.art as KK2

GOLD, CYAN, RED_C = "#FFD23F", "#8FD0E2", "#D7261E"

# ---- the city and the mountains ----------------------------------------------------------------------------------------
SKIES = {"day": ("#6AB0D8", "#F3E8C8"), "dusk": ("#2A1A3A", "#E8803A"), "night": ("#05051A", "#2A2A5A"), "siege": ("#5A4A5A", "#C8A080"),
         "burning": ("#2A0A0A", "#C84A1A"), "empty": ("#6A6A7A", "#C8B8A8"), "storm": ("#1A1A2A", "#5A5A6A")}

def jerusalem(p, w, h, seed, mode="day", temple=True, people=False):
    """Jerusalem on her hill: the wall with its towers along the slope, houses within, the house of Jehovah on the summit.
    mode: day, dusk, night, siege (forts, a mound, camps and battering rams), burning (fire and smoke, no one drawn),
    empty (the wall broken, the houses dark), storm."""
    r = random.Random(seed)
    top, bot = SKIES.get(mode, SKIES["day"])
    o = [mk.defs(p, *ALL), bg(f"js{seed}{mode}", w, h, [(0, top), (1, bot)])]
    if mode == "night": o.append(mk.stars(50, w, h * 0.5, seed))
    if mode == "dusk": o.append(sun(w * 0.86, h * 0.56, max(10, h * 0.05), color="#FF8A3D", op=0.4))
    o.append(hills(w, h, h * 0.62, seed, "#6A5A6A" if mode in ("night", "storm", "burning") else "#9A8A7A", amp=10, step=80))
    cx, base, hw, ht = w * 0.5, h * 0.9, w * 0.42, h * 0.36
    hill = f"M{f(cx - hw * 1.3)} {f(base)} C {f(cx - hw * 0.7)} {f(base - ht * 0.9)} {f(cx + hw * 0.7)} {f(base - ht * 0.9)} {f(cx + hw * 1.3)} {f(base)} Z"
    hc = {"burning": "#4A2A1A", "night": "#2A2A3A", "storm": "#3A3A3A", "empty": "#7A6A5A"}.get(mode, "#8A6A4A")
    o.append(P(hill, hc, 2.4))
    wall_y = base - ht * 0.42
    lit = mode in ("dusk", "night", "siege")
    hcol = {"burning": "#5A3A2A", "night": "#3A3446", "empty": "#9A8A7A"}.get(mode, "#C8A878")
    for i in range(16):
        x = cx - hw * 0.62 + r.uniform(0, hw * 1.24); bw = r.uniform(18, 34) * w / 702; bh = r.uniform(14, 28) * h / 400
        y = wall_y - r.uniform(0, ht * 0.24)
        if temple and abs(x - cx) < hw * 0.22 and y < wall_y - ht * 0.1: continue
        o.append(f'<rect x="{f(x)}" y="{f(y - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{hcol}" stroke="{INK}" stroke-width="1.6"></rect>')
        if lit and r.random() < 0.5: o.append(f'<rect x="{f(x + bw * 0.4)}" y="{f(y - bh * 0.7)}" width="4" height="6" fill="#FFC14D"></rect>')
    if temple:
        o.append(K1.temple_front(cx, wall_y - ht * 0.2, w * 0.18, seed))
    wc = {"burning": "#6A3A2A", "night": "#4A4456", "empty": "#A89A8A"}.get(mode, "#B89A6A")
    x0, x1 = cx - hw * 0.78, cx + hw * 0.78
    o.append(f'<rect x="{f(x0)}" y="{f(wall_y)}" width="{f(x1 - x0)}" height="{f(ht * 0.16)}" fill="{wc}" stroke="{INK}" stroke-width="2.2"></rect>')
    for i in range(int((x1 - x0) / 16)):
        if mode == "empty" and r.random() < 0.25: continue
        o.append(f'<rect x="{f(x0 + i * 16 + 2)}" y="{f(wall_y - 7)}" width="9" height="8" fill="{wc}" stroke="{INK}" stroke-width="1.2"></rect>')
    for tx in (x0, cx - hw * 0.26, cx + hw * 0.26, x1):
        o.append(f'<rect x="{f(tx - 12)}" y="{f(wall_y - ht * 0.12)}" width="24" height="{f(ht * 0.28)}" fill="{wc}" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(cx - 10)} {f(wall_y + ht * 0.16)} L {f(cx - 10)} {f(wall_y + ht * 0.06)} Q {f(cx)} {f(wall_y)} {f(cx + 10)} {f(wall_y + ht * 0.06)} L {f(cx + 10)} {f(wall_y + ht * 0.16)} Z" fill="#1A1010"></path>')
    if mode == "empty":
        for i in range(3):
            gx = x0 + (x1 - x0) * r.uniform(0.1, 0.9)
            o.append(f'<path d="M{f(gx - 14)} {f(wall_y - 8)} L {f(gx - 6)} {f(wall_y + ht * 0.1)} L {f(gx + 4)} {f(wall_y + 2)} L {f(gx + 14)} {f(wall_y - 8)} Z" fill="{SKIES["empty"][1]}" stroke="{INK}" stroke-width="1.4"></path>')
    if mode == "burning":
        for i in range(6):
            o.append(f'<g opacity="0.9">' + E.blaze(cx + hw * r.uniform(-0.6, 0.6), wall_y - r.uniform(0, ht * 0.2), w * 0.08, h * 0.16, seed + i, n=5) + '</g>')
        o.append(smoke(cx - hw * 0.3, wall_y - ht * 0.3, 8, seed, color="#2A1A1A", op=0.7, k=w / 600))
        o.append(smoke(cx + hw * 0.3, wall_y - ht * 0.3, 8, seed + 1, color="#2A1A1A", op=0.7, k=w / 600))
    if mode == "siege":
        for fx in (0.08, 0.92):
            o.append(f'<path d="M{f(w * fx - 26)} {f(base)} L {f(w * fx - 18)} {f(base - ht * 0.5)} L {f(w * fx + 18)} {f(base - ht * 0.5)} L {f(w * fx + 26)} {f(base)} Z" fill="#7A6A4A" stroke="{INK}" stroke-width="2.2"></path>')
        o.append(f'<path d="M{f(cx + hw * 0.2)} {f(base)} L {f(cx + hw * 0.6)} {f(wall_y + ht * 0.16)} L {f(cx + hw * 0.9)} {f(base)} Z" fill="#9A7A4A" stroke="{INK}" stroke-width="2"></path>')
        o.append(N.camp(9, -10, w + 10, base - h * 0.02, h + 10, seed, color=("#3A3A5A", "#5A4A3A", "#4A3A4A")))
        o.append(ram(cx - hw * 0.5, base + h * 0.02, min(1.0, h / 400)))
    o.append(ground(w, h, base, {"burning": "#1A0A0A", "night": "#1A1A2A"}.get(mode, "#8A7A5A"), dy=0))
    return "".join(o)

def ram(x, y, s=1.0):
    """A battering ram: a covered frame on wheels, the beam with an iron head."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M-50 -20 L -40 -56 L 40 -56 L 50 -20 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.2"></path>'
            '<rect x="-70" y="-38" width="120" height="10" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></rect>'
            '<path d="M-70 -42 L -84 -33 L -70 -24 Z" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<circle cx="-30" cy="-12" r="10" fill="#4A3A2A" stroke="#0D0D0F" stroke-width="2"></circle><circle cx="30" cy="-12" r="10" fill="#4A3A2A" stroke="#0D0D0F" stroke-width="2"></circle></g>')

def altar_stones(x, y, s=1.0, fire=False, broken=False, seed=1):
    """An altar of the high places: a heap of stones (broken=True: thrown down)."""
    r = random.Random(seed); o = []
    if broken:
        for i in range(7):
            o.append(f'<ellipse cx="{f(x + r.uniform(-40, 40) * s)}" cy="{f(y - r.uniform(2, 10) * s)}" rx="{f(r.uniform(9, 15) * s)}" ry="{f(r.uniform(6, 9) * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
        return "".join(o)
    for row in range(3):
        for k in range(3 - row):
            o.append(f'<rect x="{f(x + (-30 + row * 10 + k * 20) * s)}" y="{f(y - (row + 1) * 14 * s)}" width="{f(20 * s)}" height="{f(14 * s)}" rx="3" fill="#9A8A7A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    if fire: o.append(E.blaze(x, y - 42 * s, 30 * s, 40 * s, seed, n=4))
    return "".join(o)

def sun_image(x, y, s=1.0, fallen=False):
    """A sun-image: a pillar crowned with a sun disc (fallen=True: broken, lying)."""
    if fallen:
        return (f'<g transform="translate({f(x)} {f(y)}) rotate(78) scale({f(s)})"><rect x="-7" y="-70" width="14" height="70" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></rect></g>'
                f'<circle cx="{f(x + 82 * s)}" cy="{f(y - 8 * s)}" r="{f(10 * s)}" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></circle>')
    return (f'<rect x="{f(x - 7 * s)}" y="{f(y - 70 * s)}" width="{f(14 * s)}" height="{f(70 * s)}" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></rect>'
            f'<circle cx="{f(x)}" cy="{f(y - 80 * s)}" r="{f(12 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>'
            + "".join(f'<path d="M{f(x + math.cos(a) * 15 * s)} {f(y - 80 * s + math.sin(a) * 15 * s)} L {f(x + math.cos(a) * 22 * s)} {f(y - 80 * s + math.sin(a) * 22 * s)}" stroke="#E8B830" stroke-width="2"></path>' for a in [i * math.pi / 4 for i in range(8)]))

def idol(x, y, s=1.0, fallen=False, color="#C8A040"):
    """A small graven image on a pedestal (fallen=True: toppled)."""
    g = (f'<rect x="-10" y="-14" width="20" height="14" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
         f'<path d="M-6 -14 L -7 -40 L -11 -44 L -6 -52 L 6 -52 L 11 -44 L 7 -40 L 6 -14 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
         f'<circle cx="0" cy="-58" r="6" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    if fallen:
        return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><rect x="-10" y="-14" width="20" height="14" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="1.6"></rect></g>' \
               f'<g transform="translate({f(x + 34 * s)} {f(y - 4 * s)}) rotate(96) scale({f(s)})"><path d="M-6 -14 L -7 -40 L -11 -44 L -6 -52 L 6 -52 L 11 -44 L 7 -40 L 6 -14 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="0" cy="-58" r="6" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></circle></g>'
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{g}</g>'

def mountains(w, h, seed, mode="idols"):
    """The mountains of Israel. mode: idols (altars burning on the heights, sun-images, idols under green trees), broken
    (the altars thrown down, the images broken, smoke drifting — no one drawn), fruitful (green, trees in fruit, flocks),
    desolate (bare and brown, thorns)."""
    r = random.Random(seed)
    sky_ = {"idols": ("#3A2A4A", "#E8A070"), "broken": ("#3A3A4A", "#A89A8A"), "fruitful": ("#6AB0D8", "#F3E8C8"), "desolate": ("#8A6A5A", "#E8C8A0")}[mode]
    o = [bg(f"mt{seed}{mode}", w, h, [(0, sky_[0]), (1, sky_[1])])]
    green = mode == "fruitful"
    cols = (["#7A9A6A", "#5A7A4A", "#3A5A2A"] if green else ["#8A7A7A", "#6A5A5A", "#4A4040"] if mode == "broken" else ["#A88A6A", "#8A6A4A", "#6A4A3A"] if mode == "desolate" else ["#7A7A6A", "#5A5A4A", "#3A3A30"])
    peaks = []
    for layer, col in enumerate(cols):
        svg, pk = ridge(w, h, h * (0.4 + layer * 0.17), 3 + layer, seed + layer, h * (0.16 - layer * 0.03), col)
        o.append(svg); peaks += [(x, y, layer) for x, y in pk]
    k = min(1.0, h / 420)
    for i, (px, py, layer) in enumerate(peaks[-6:]):
        s = k * (0.6 + 0.15 * layer)
        if mode == "idols":
            if i % 2 == 0:
                o.append(tree(px - 34 * s, py + 6 * s, 0.4 * s, color="#2E6B3A", seed=seed + i))
                o.append(altar_stones(px, py + 2, s, fire=True, seed=seed + i))
            else: o.append(sun_image(px, py + 2, s))
            if i % 3 == 1: o.append(idol(px + 30 * s, py + 4, s * 0.9))
        elif mode == "broken":
            o.append(altar_stones(px, py + 4, s, broken=True, seed=seed + i))
            if i % 2: o.append(sun_image(px - 20 * s, py + 4, s, fallen=True))
            else: o.append(idol(px - 26 * s, py + 4, s * 0.9, fallen=True))
        elif mode == "fruitful":
            o.append(tree(px - 20 * s, py + 8 * s, 0.4 * s, color="#2E8A3A", seed=seed + i))
            o.append("".join(f'<circle cx="{f(px - 20 * s + r.uniform(-14, 14) * s)}" cy="{f(py - r.uniform(40, 56) * s)}" r="{f(3 * s)}" fill="#D7261E"></circle>' for _ in range(4)))
        else:
            o.append("".join(f'<path d="M{f(px + r.uniform(-30, 30) * s)} {f(py + 10 * s)} l {f(r.uniform(-8, 8) * s)} {f(-14 * s)}" stroke="#3A2A1A" stroke-width="2"></path>' for _ in range(5)))
    if mode == "broken":
        for i in range(3): o.append(smoke(w * (0.2 + i * 0.3), h * 0.6, 7, seed + i, color="#3A3A3A", op=0.45, k=min(1.2, h / 300)))
    if mode == "fruitful":
        o.append(flock(w * 0.05, w * 0.6, h * 0.86, h * 0.98, 9, seed, cows=0.2))
    return "".join(o)

# ---- the signs of the siege (Ezekiel 4–5) ------------------------------------------------------------------------------
def tile_plan(w, h, pan=True):
    """The tile with a city portrayed upon it, even Jerusalem, and the siege laid against it: forts, a mound, camps,
    battering rams round about; the iron pan set for a wall of iron between the prophet and the city."""
    o = [bp(w, h), title_bar(w, "THE TILE · A CITY, EVEN JERUSALEM")]
    cx, cy = w * 0.46, h * 0.56; R = min(w * 0.2, h * 0.28)
    o.append(f'<rect x="{f(cx - R * 1.6)}" y="{f(cy - R * 1.3)}" width="{f(R * 3.2)}" height="{f(R * 2.6)}" fill="#B86A3A" stroke="#0D0D0F" stroke-width="2.6"></rect>')
    o.append(f'<path d="M{f(cx - R * 0.9)} {f(cy - R * 0.6)} L {f(cx - R * 0.3)} {f(cy - R * 0.9)} L {f(cx + R * 0.8)} {f(cy - R * 0.7)} L {f(cx + R * 0.9)} {f(cy + R * 0.5)} L {f(cx - R * 0.2)} {f(cy + R * 0.85)} L {f(cx - R * 0.95)} {f(cy + R * 0.3)} Z" fill="none" stroke="#3A1A0A" stroke-width="3"></path>')
    o.append(f'<rect x="{f(cx - R * 0.2)}" y="{f(cy - R * 0.5)}" width="{f(R * 0.4)}" height="{f(R * 0.3)}" fill="none" stroke="#3A1A0A" stroke-width="2.4"></rect>')
    for i in range(8):
        a = i * math.pi / 4 + 0.2
        x, y = cx + math.cos(a) * R * 1.25, cy + math.sin(a) * R * 1.05
        o.append(f'<rect x="{f(x - 6)}" y="{f(y - 6)}" width="12" height="12" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(tag(cx + R * 1.25 * math.cos(0.2), cy + R * 1.05 * math.sin(0.2), "FORTS", w * 0.86, h * 0.36))
    o.append(f'<path d="M{f(cx - R * 1.5)} {f(cy + R * 1.15)} Q {f(cx - R * 0.5)} {f(cy + R * 0.7)} {f(cx + R * 0.4)} {f(cy + R * 1.15)}" fill="none" stroke="#E8C88A" stroke-width="7"></path>')
    o.append(tag(cx - R * 0.6, cy + R * 0.98, "A MOUND", w * 0.12, h * 0.94))
    for i in range(5):
        x = cx + R * (-1.4 + i * 0.7); y = cy - R * 1.12
        o.append(f'<path d="M{f(x - 8)} {f(y + 5)} L {f(x)} {f(y - 7)} L {f(x + 8)} {f(y + 5)} Z" fill="#FF8A6A" stroke="#0D0D0F" stroke-width="1.2"></path>')
    o.append(tag(cx + R * 1.4, cy - R * 1.12, "CAMPS", w * 0.86, h * 0.18))
    for a in (2.4, 3.6, 4.4):
        x, y = cx + math.cos(a) * R * 1.48, cy + math.sin(a) * R * 1.2
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + math.cos(a + math.pi) * 18)} {f(y + math.sin(a + math.pi) * 18)}" stroke="#C8C8D0" stroke-width="5"></path>')
    o.append(tag(cx + math.cos(3.6) * R * 1.48, cy + math.sin(3.6) * R * 1.2, "BATTERING RAMS", w * 0.06, h * 0.3))
    if pan:
        px = cx + R * 2.05
        o.append(f'<rect x="{f(px)}" y="{f(cy - R * 1.2)}" width="10" height="{f(R * 2.4)}" fill="#5A5A6A" stroke="#C8C8D0" stroke-width="2"></rect>')
        o.append(tag(px + 5, cy + R * 0.9, "AN IRON PAN · A WALL OF IRON", w * 0.6, h * 0.86))
    return "".join(o)

def lie(x, y, s, cloth=EZ_C, flip=False, bands=False):
    """Ezekiel lying on his side, head to the left (white headcloth, blue cord, grey-black beard); bands=True: cords
    laid over him."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">',
         P("M-118 0 C -122 -22 -96 -34 -56 -32 L 14 -26 C 30 -24 38 -12 36 0 Z", cloth, 2.4),
         P("M36 -4 L 52 -4 C 54 -12 48 -16 40 -14 Z", SKIN, 1.6),
         f'<circle cx="-134" cy="-18" r="16" fill="{SKIN}" stroke="{INK}" stroke-width="2.2"></circle>',
         P("M-152 -14 C -156 -38 -120 -44 -116 -24 L -120 -8 L -136 -30 L -150 0 Z", "#F3EFE6", 2),
         '<path d="M-150 -26 C -142 -34 -128 -36 -118 -30" fill="none" stroke="#1F5FAD" stroke-width="3.4"></path>',
         P("M-126 -8 C -120 2 -112 2 -108 -6 C -112 -12 -118 -12 -124 -10 Z", "#4A4640", 1.4),
         '<path d="M-90 -24 C -70 -20 -40 -18 -10 -18" fill="none" stroke="#0D0D0F" stroke-width="1.2" opacity="0.5"></path>']
    if bands:
        for bx in (-80, -30, 10):
            o.append(f'<path d="M{bx} -36 C {bx + 6} -20 {bx + 6} -8 {bx} 4" fill="none" stroke="#0D0D0F" stroke-width="5"></path><path d="M{bx} -36 C {bx + 6} -20 {bx + 6} -8 {bx} 4" fill="none" stroke="#C8A878" stroke-width="3"></path>')
    return "".join(o) + "</g>"

def lying(p, w, h, seed, side="left", bread=False):
    """Ezekiel lying on his side in his house before the tile, his arm uncovered toward the siege of Jerusalem; bands upon
    him; bread=True: the barley cakes and the water by measure beside him."""
    o = [bg(f"ly{seed}", w, h, [(0, "#3A2A2A"), (1, "#8A6A4A")]), f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#6A5040" stroke="{INK}" stroke-width="2"></rect>']
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(h * 0.2)}" width="{f(w * 0.12)}" height="{f(h * 0.16)}" fill="#E8A040" stroke="{INK}" stroke-width="2"></rect>')
    s = min(1.3, h / 300, w / 520)
    tx = w * 0.78
    o.append(f'<path d="M{f(tx - 60 * s)} {f(h * 0.86)} L {f(tx - 40 * s)} {f(h * 0.8)} L {f(tx + 50 * s)} {f(h * 0.8)} L {f(tx + 66 * s)} {f(h * 0.86)} Z" fill="#B86A3A" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(tx - 30 * s)} {f(h * 0.835)} L {f(tx + 34 * s)} {f(h * 0.835)}" stroke="#3A1A0A" stroke-width="2"></path>')
    o.append(f'<rect x="{f(tx - 80 * s)}" y="{f(h * 0.72)}" width="{f(6 * s)}" height="{f(h * 0.14)}" fill="#5A5A6A" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(lie(w * 0.42, h * 0.9, s, bands=True, flip=side == "right"))
    if bread:
        o.append("".join(f'<ellipse cx="{f(w * 0.12 + i * 22 * s)}" cy="{f(h * 0.9)}" rx="{f(12 * s)}" ry="{f(5 * s)}" fill="#C8A060" stroke="{INK}" stroke-width="1.4"></ellipse>' for i in range(3)))
        o.append(f'<path d="M{f(w * 0.22)} {f(h * 0.9)} L {f(w * 0.22 - 6 * s)} {f(h * 0.82)} L {f(w * 0.22 + 14 * s)} {f(h * 0.82)} L {f(w * 0.22 + 8 * s)} {f(h * 0.9)} Z" fill="#8A6A5A" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def days_plate(w, h):
    """The days of the bearing of iniquity as a plate: three hundred and ninety days on the left side for the house of
    Israel, forty days on the right side for the house of Judah, each day for a year."""
    o = [bp(w, h), title_bar(w, "EACH DAY FOR A YEAR")]
    cols = 30; cell = min(w * 0.6 / cols, h * 0.5 / 14)
    x0, y0 = w * 0.06, h * 0.2
    for i in range(390):
        r_, c = divmod(i, cols)
        o.append(f'<rect x="{f(x0 + c * cell)}" y="{f(y0 + r_ * cell)}" width="{f(cell - 2)}" height="{f(cell - 2)}" fill="{CYAN}" opacity="0.85"></rect>')
    o.append(label(x0, y0 + 13 * cell + 20, "LEFT SIDE · THE HOUSE OF ISRAEL · 390", CYAN, 9, "start"))
    x1 = x0 + cols * cell + w * 0.06
    for i in range(40):
        r_, c = divmod(i, 4)
        o.append(f'<rect x="{f(x1 + c * cell)}" y="{f(y0 + r_ * cell)}" width="{f(cell - 2)}" height="{f(cell - 2)}" fill="{GOLD}"></rect>')
    o.append(label(x1, y0 + 10 * cell + 20, "RIGHT SIDE · JUDAH · 40", GOLD, 9, "start"))
    return "".join(o)

def ration_plate(w, h):
    """The bread of the siege as a plate: wheat, barley, beans, lentils, millet and spelt in one vessel; twenty shekels a
    day by weight; water by measure, the sixth part of a hin; barley cakes."""
    o = [bp(w, h), title_bar(w, "THE BREAD OF THE SIEGE · BY WEIGHT AND BY MEASURE")]
    names = ["WHEAT", "BARLEY", "BEANS", "LENTILS", "MILLET", "SPELT"]
    colors = ["#E8C060", "#D8B070", "#8A5A3A", "#C87A3A", "#E8D890", "#C8A060"]
    cx, cy = w * 0.22, h * 0.62
    o.append(f'<path d="M{f(cx - w * 0.1)} {f(cy - h * 0.18)} L {f(cx + w * 0.1)} {f(cy - h * 0.18)} C {f(cx + w * 0.12)} {f(cy + h * 0.1)} {f(cx + w * 0.06)} {f(cy + h * 0.22)} {f(cx)} {f(cy + h * 0.22)} C {f(cx - w * 0.06)} {f(cy + h * 0.22)} {f(cx - w * 0.12)} {f(cy + h * 0.1)} {f(cx - w * 0.1)} {f(cy - h * 0.18)} Z" fill="#8A5A3A" stroke="{CYAN}" stroke-width="2"></path>')
    for i, (nm, c) in enumerate(zip(names, colors)):
        y = cy - h * 0.12 + i * h * 0.05
        o.append(f'<rect x="{f(cx - w * 0.07)}" y="{f(y)}" width="{f(w * 0.14)}" height="{f(h * 0.045)}" fill="{c}" stroke="#0D0D0F" stroke-width="1"></rect>')
        o.append(label(cx + w * 0.13, y + h * 0.035, nm, c, 8, "start"))
    bx, by = w * 0.62, h * 0.5
    o.append(f'<path d="M{f(bx)} {f(by - h * 0.2)} L {f(bx)} {f(by + h * 0.24)} M{f(bx - w * 0.12)} {f(by - h * 0.14)} L {f(bx + w * 0.12)} {f(by - h * 0.14)}" stroke="{CYAN}" stroke-width="3"></path>')
    for sx in (-1, 1):
        x = bx + sx * w * 0.12
        o.append(f'<path d="M{f(x)} {f(by - h * 0.14)} L {f(x - w * 0.04)} {f(by)} M{f(x)} {f(by - h * 0.14)} L {f(x + w * 0.04)} {f(by)}" stroke="{CYAN}" stroke-width="1.4"></path>'
                 f'<path d="M{f(x - w * 0.05)} {f(by)} Q {f(x)} {f(by + h * 0.06)} {f(x + w * 0.05)} {f(by)} Z" fill="#3A4A5A" stroke="{CYAN}" stroke-width="2"></path>')
    o.append(label(bx, by + h * 0.32, "TWENTY SHEKELS A DAY", GOLD, 10))
    wx, wy = w * 0.88, h * 0.66
    o.append(f'<path d="M{f(wx - w * 0.04)} {f(wy - h * 0.12)} L {f(wx + w * 0.04)} {f(wy - h * 0.12)} L {f(wx + w * 0.05)} {f(wy + h * 0.12)} L {f(wx - w * 0.05)} {f(wy + h * 0.12)} Z" fill="none" stroke="{CYAN}" stroke-width="2"></path>'
             f'<rect x="{f(wx - w * 0.045)}" y="{f(wy + h * 0.08)}" width="{f(w * 0.09)}" height="{f(h * 0.04)}" fill="#2C9DB8"></rect>')
    o.append(label(wx, wy + h * 0.2, "1/6 HIN", CYAN, 9))
    return "".join(o)

def hair_plate(w, h):
    """The hair shaven with a sharp sword as a barber's razor, weighed in balances and divided: a third burned in the
    fire in the midst of the city, a third smitten with the sword round about, a third scattered to the wind; a few bound
    in the skirts."""
    o = [bp(w, h), title_bar(w, "THE HAIR DIVIDED · A THIRD PART, A THIRD PART, A THIRD PART")]
    cx = w * 0.5
    o.append(f'<path d="M{f(cx - w * 0.3)} {f(h * 0.16)} L {f(cx + w * 0.26)} {f(h * 0.16)} L {f(cx + w * 0.32)} {f(h * 0.19)} L {f(cx - w * 0.3)} {f(h * 0.2)} Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(cx - w * 0.38)}" y="{f(h * 0.15)}" width="{f(w * 0.08)}" height="{f(h * 0.06)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(tag(cx + w * 0.1, h * 0.18, "A SHARP SWORD · AS A BARBER'S RAZOR", cx + w * 0.16, h * 0.28))
    xs = [w * 0.2, w * 0.5, w * 0.8]
    for i, x in enumerate(xs):
        y = h * 0.62
        o.append("".join(f'<path d="M{f(x - 30 + k * 6)} {f(y)} C {f(x - 26 + k * 6)} {f(y - 20)} {f(x - 20 + k * 6)} {f(y - 30)} {f(x - 14 + k * 6)} {f(y - 36)}" fill="none" stroke="#4A4640" stroke-width="2"></path>' for k in range(10)))
        if i == 0: o.append(E.blaze(x, y + h * 0.18, w * 0.12, h * 0.14, 51, n=4))
        if i == 1: o.append(f'<path d="M{f(x - 40)} {f(y + h * 0.14)} L {f(x + 40)} {f(y + h * 0.1)}" stroke="#C8C8D0" stroke-width="5"></path>')
        if i == 2: o.append(wind_lines(w * 0.26, h * 0.2, 52, n=5, color=CYAN, op=0.7).replace("<path ", f'<path transform="translate({f(x - w * 0.12)} {f(y + h * 0.02)})" '))
    o.append(label(xs[0], h * 0.94, "BURNED IN THE FIRE", GOLD, 9))
    o.append(label(xs[1], h * 0.94, "SMITTEN WITH THE SWORD", GOLD, 9))
    o.append(label(xs[2], h * 0.94, "SCATTERED TO THE WIND", GOLD, 9))
    return "".join(o)

def nations_center(w, h, hi=None):
    """Jerusalem set in the midst of the nations, countries round about her, as a technical map."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.58
    ring = [("EGYPT", -2.5), ("ASSYRIA", -0.6), ("BABYLON", 0.2), ("EDOM", 1.6), ("MOAB", 1.1), ("PHILISTIA", 2.7), ("TYRE", -1.8), ("SYRIA", -1.2)]
    for nm, a in ring:
        x, y = cx + math.cos(a) * w * 0.36, cy + math.sin(a) * h * 0.32
        o.append(route([(cx, cy), (x, y)], color="#4A7A9A", sw=1.4, dash="4 5", arrow=False) + node(x, y, nm, CYAN if nm != hi else GOLD, r=5, dy=-10, size=9))
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(min(w, h) * 0.1)}" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="6 4"></circle>')
    o.append(node(cx, cy, "JERUSALEM", RED_C, r=8, dy=-16, size=11))
    return "".join(o)

# ---- the end (Ezekiel 7) -----------------------------------------------------------------------------------------------
def four_corners(w, h):
    """An end is come upon the four corners of the land: the land as a map, the four corners lit red."""
    o = [grid_bg(w, h)]
    x0, x1, y0, y1 = w * 0.3, w * 0.7, h * 0.14, h * 0.94
    o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y0 + 10)} L {f(x1 + 10)} {f(y1)} L {f(x0 - 16)} {f(y1 - 8)} Z" fill="#1A2A3A" stroke="{CYAN}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.6)} {f(y0 + 20)} C {f(w * 0.62)} {f(h * 0.4)} {f(w * 0.58)} {f(h * 0.6)} {f(w * 0.62)} {f(h * 0.7)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>')
    for x, y in ((x0, y0), (x1, y0 + 10), (x1 + 10, y1), (x0 - 16, y1 - 8)):
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="16" fill="{RED_C}" fill-opacity="0.35" stroke="{RED_C}" stroke-width="2.4"></circle><circle cx="{f(x)}" cy="{f(y)}" r="5" fill="{RED_C}"></circle>')
    o.append(node(w * 0.5, h * 0.56, "JERUSALEM", GOLD, r=5, dy=-12, size=9))
    o.append(label(w * 0.5, h * 0.06 + 14, "THE FOUR CORNERS OF THE LAND", RED_C, 10))
    return "".join(o)

def rod(w, h, seed):
    """The rod hath blossomed, pride hath budded: a rod of iron standing in the dark, budding with red blossoms."""
    r = random.Random(seed)
    o = [bg(f"rd{seed}", w, h, [(0, "#1A0A0A"), (1, "#5A1A1A")]), ground(w, h, h * 0.9, "#2A1A1A", dy=0)]
    x = w * 0.5
    o.append(f'<path d="M{f(x)} {f(h * 0.92)} C {f(x - 6)} {f(h * 0.7)} {f(x + 8)} {f(h * 0.5)} {f(x)} {f(h * 0.36)}" stroke="#0D0D0F" stroke-width="16" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(x)} {f(h * 0.92)} C {f(x - 6)} {f(h * 0.7)} {f(x + 8)} {f(h * 0.5)} {f(x)} {f(h * 0.36)}" stroke="#5A4A3A" stroke-width="11" fill="none" stroke-linecap="round"></path>')
    for i in range(7):
        y = h * (0.4 + i * 0.07); sx = 1 if i % 2 else -1
        bx, by = x + sx * 22, y - 10
        o.append(f'<path d="M{f(x)} {f(y)} Q {f(x + sx * 12)} {f(y - 4)} {f(bx)} {f(by)}" stroke="#3A5A2A" stroke-width="3" fill="none"></path>')
        o.append("".join(f'<ellipse cx="{f(bx + math.cos(a) * 6)}" cy="{f(by + math.sin(a) * 6)}" rx="6" ry="4" transform="rotate({f(math.degrees(a))} {f(bx + math.cos(a) * 6)} {f(by + math.sin(a) * 6)})" fill="#D7261E" stroke="#0D0D0F" stroke-width="1"></ellipse>' for a in [k * 2 * math.pi / 5 for k in range(5)]))
        o.append(f'<circle cx="{f(bx)}" cy="{f(by)}" r="3" fill="#FFD23F"></circle>')
    return "".join(o)

def trumpet_gate(p, w, h, seed):
    """They have blown the trumpet and made all ready, but none goeth to the battle: an empty gate, the trumpet lying on
    the wall, shields and spears stacked and left."""
    o = [bg(f"tg{seed}", w, h, [(0, "#4A3A4A"), (1, "#C8A080")]), hills(w, h, h * 0.6, seed, "#7A6A6A", amp=8, step=90)]
    o.append(S4.gatehouse(w * 0.5, h * 0.92, w * 0.66, h * 0.62))
    o.append(J.shofar(w * 0.2, h * 0.4, 1.2, rot=-8))
    for i in range(4):
        x = w * (0.72 + i * 0.05)
        o.append(f'<path d="M{f(x)} {f(h * 0.94)} L {f(x + 6)} {f(h * 0.56)}" stroke="#5A3A1A" stroke-width="3"></path><path d="M{f(x + 6)} {f(h * 0.56)} l -3 -12 l 6 0 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1"></path>')
    o.append("".join(f'<circle cx="{f(w * (0.18 + i * 0.07))}" cy="{f(h * 0.88)}" r="{f(h * 0.06)}" fill="#B8863E" stroke="#0D0D0F" stroke-width="2"></circle>' for i in range(3)))
    o.append(ground(w, h, h * 0.94, "#6A5A4A", dy=0))
    return "".join(o)

def silver_street(w, h, seed):
    """They shall cast their silver in the streets: an empty street between houses, silver and gold strewn upon it."""
    r = random.Random(seed)
    o = [bg(f"ss{seed}", w, h, [(0, "#5A5A6A"), (1, "#B8A898")])]
    for side in (0, 1):
        for i in range(4):
            x = (w * 0.02 + i * w * 0.1) if side == 0 else (w * 0.62 + i * w * 0.1)
            hh = h * r.uniform(0.3, 0.46)
            o.append(house(x, h * 0.7, w * 0.1, hh, color=r.choice(["#A8946A", "#B8A47A", "#98845A"])))
    o.append(f'<path d="M{f(w * 0.42)} {f(h * 0.7)} L {f(w * 0.58)} {f(h * 0.7)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.7, "#8A7A6A", dy=0).replace('d="M-10', 'opacity="0.0" d="M-10'))
    for _ in range(30):
        x = w * r.uniform(0.2, 0.8); y = h * r.uniform(0.74, 0.98)
        c = r.choice(["#C8C8D0", "#E8E8F0", "#E8B830"])
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(4, 8))}" ry="{f(r.uniform(2, 4))}" fill="{c}" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    return "".join(o)

def chain(w, h, seed):
    """Make the chain: a great chain of iron links laid out on the ground before the city gate."""
    o = [bg(f"ch{seed}", w, h, [(0, "#2A2A3A"), (1, "#6A5A5A")]), ground(w, h, h * 0.6, "#4A4040", dy=0)]
    n = 9
    for i in range(n):
        x = w * (0.08 + i * 0.1); y = h * (0.78 + 0.05 * math.sin(i * 0.9))
        if i % 2 == 0:
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.06)}" ry="{f(h * 0.06)}" fill="none" stroke="#0D0D0F" stroke-width="12"></ellipse><ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.06)}" ry="{f(h * 0.06)}" fill="none" stroke="#7A7A8A" stroke-width="8"></ellipse>')
        else:
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.06)}" ry="{f(h * 0.02)}" fill="none" stroke="#0D0D0F" stroke-width="12"></ellipse><ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.06)}" ry="{f(h * 0.02)}" fill="none" stroke="#9A9AAA" stroke-width="8"></ellipse>')
    return "".join(o)

def doves(w, h, seed):
    """Those that escape shall be on the mountains like doves of the valleys, all of them mourning."""
    r = random.Random(seed)
    o = [mountains(w, h, seed, "desolate")]
    for i in range(7):
        x = w * r.uniform(0.1, 0.9); y = h * r.uniform(0.5, 0.7); s = r.uniform(0.6, 1.0) * min(1.2, h / 300)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-14 0 C -10 -10 10 -10 16 -2 L 26 -6 L 20 2 C 10 8 -8 8 -14 0 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 '<circle cx="14" cy="-6" r="5" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-6 -4 C -2 -14 6 -14 8 -6" fill="#C8C2B6" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
    return "".join(o)

def crown_dust(w, h, seed):
    """The king shall mourn and the prince be clothed with desolation: a crown and a torn royal mantle cast in the dust
    before the palace door."""
    o = [bg(f"cd{seed}", w, h, [(0, "#2A2A3A"), (1, "#7A6A6A")]), f'<rect x="{f(w * 0.2)}" y="{f(h * 0.2)}" width="{f(w * 0.6)}" height="{f(h * 0.62)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.42)} {f(h * 0.82)} L {f(w * 0.42)} {f(h * 0.44)} Q {f(w * 0.5)} {f(h * 0.36)} {f(w * 0.58)} {f(h * 0.44)} L {f(w * 0.58)} {f(h * 0.82)} Z" fill="#1A1010" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, h * 0.82, "#5A4A40", dy=0)]
    o.append(P(f"M{f(w * 0.2)} {f(h * 0.94)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.44)} {f(h * 0.86)} {f(w * 0.5)} {f(h * 0.92)} L {f(w * 0.46)} {f(h * 0.97)} L {f(w * 0.36)} {f(h * 0.94)} L {f(w * 0.3)} {f(h * 0.98)} Z", "#5A1A4A", 2))
    k = min(1.4, h / 260)
    o.append(f'<g transform="translate({f(w * 0.62)} {f(h * 0.93)}) rotate(-18) scale({f(k)})"><path d="M-24 0 L -24 -18 L -12 -8 L 0 -24 L 12 -8 L 24 -18 L 24 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path></g>')
    return "".join(o)

def staff_broken(w, h, seed):
    """I will break the staff of bread: a broken staff over an empty bread basket and a dry water jar."""
    o = [bg(f"sb{seed}", w, h, [(0, "#3A2A2A"), (1, "#9A7A5A")]), ground(w, h, h * 0.72, "#6A5040", dy=0)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.86)} L {f(w * 0.46)} {f(h * 0.62)}" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path><path d="M{f(w * 0.2)} {f(h * 0.86)} L {f(w * 0.46)} {f(h * 0.62)}" stroke="#8A5A30" stroke-width="8" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.72)} {f(h * 0.5)}" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path><path d="M{f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.72)} {f(h * 0.5)}" stroke="#8A5A30" stroke-width="8" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.9)} L {f(w * 0.54)} {f(h * 0.76)} L {f(w * 0.74)} {f(h * 0.76)} L {f(w * 0.72)} {f(h * 0.9)} Z" fill="#B8945A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.8)} {f(h * 0.92)} C {f(w * 0.76)} {f(h * 0.84)} {f(w * 0.78)} {f(h * 0.74)} {f(w * 0.82)} {f(h * 0.72)} L {f(w * 0.86)} {f(h * 0.72)} C {f(w * 0.9)} {f(h * 0.74)} {f(w * 0.92)} {f(h * 0.84)} {f(w * 0.88)} {f(h * 0.92)} Z" fill="#8A5A3A" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def ridge(w, h, y, n, seed, amp, col, sw=2.2):
    """A mountain ridge: n peaks along height y (peaks up to amp above it), valleys between; returns (svg, peaks)."""
    r = random.Random(seed)
    xs = [w * (i + 0.5) / n + r.uniform(-w * 0.04, w * 0.04) for i in range(n)]
    pk = [(x, y - r.uniform(amp * 0.5, amp)) for x in xs]
    pts = [(-10, y + amp * 0.2)]
    for i, (x, py) in enumerate(pk):
        if i: pts.append(((pk[i - 1][0] + x) / 2, y + r.uniform(0, amp * 0.25)))
        pts.append((x, py))
    pts.append((w + 10, y + amp * 0.2))
    d = f"M-10 {f(h + 10)} L " + " L ".join(f"{f(a)} {f(b)}" for a, b in pts) + f" L {f(w + 10)} {f(h + 10)} Z"
    return P(d, col, sw), pk
