"""Drawings for the 2 Corinthians volume, chapter 3 (2 Corinthians 10–13): the strongholds cast down (a plate); the letters
weighed (a plate); the measure of the province (a map); the betrothal as an emblem; Paul at the tent-cloth with the
brethren come from Macedonia; the stars over the tents of Abraham; then Paul's sufferings as words over empty places — the
prison cell, the rods laid down and the stones before the gate, a broken ship on an empty sea, the eight perils as a plate
of empty places, a cold camp at night — and the basket at Damascus (Acts' drawing); caught up to the third heaven, a road
of light going up through the heavens; the thorn branch; the light from heaven over Paul praying; the staff by the door;
the empty street of shut doors; the gate and the witnesses; the letter sealed. The cast and helpers are co2.art's. No one
is drawn suffering; Satan is never drawn; the Lord is not drawn (the light only)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from co2.art import *
from co2.art2 import bag
from ntcast import ROBES

# ---- 2 Corinthians 10 -----------------------------------------------------------------------------------------------------
def strongholds(w, h):
    """The weapons of our warfare are … mighty before God to the casting down of strongholds; casting down imaginations,
    and every high thing that is exalted against the knowledge of God: a plate — a fortress on its rock drawn in lines, its
    high tower broken and its walls breached, the stones fallen down the slope."""
    o = [plate_bg(w, h, "2 CORINTHIANS 10:4–5 · THE CASTING DOWN OF STRONGHOLDS")]
    k = min(w / 560, (h - 44) / 262); cx, b = w * 0.46, h - 14
    o.append(f'<path d="M{f(cx - 230 * k)} {f(b)} L {f(cx - 160 * k)} {f(b - 60 * k)} L {f(cx + 150 * k)} {f(b - 66 * k)} L {f(cx + 240 * k)} {f(b)} Z" fill="#14283C" stroke="{CY}" stroke-width="1.6"></path>')
    wy = b - 64 * k
    o.append(f'<path d="M{f(cx - 150 * k)} {f(wy)} L {f(cx - 150 * k)} {f(wy - 56 * k)} L {f(cx - 40 * k)} {f(wy - 56 * k)} L {f(cx - 30 * k)} {f(wy - 30 * k)} L {f(cx - 10 * k)} {f(wy - 44 * k)} '
             f'L {f(cx + 4 * k)} {f(wy - 20 * k)} L {f(cx + 20 * k)} {f(wy - 56 * k)} L {f(cx + 140 * k)} {f(wy - 56 * k)} L {f(cx + 140 * k)} {f(wy)} Z" fill="#1E3A5A" stroke="{CY}" stroke-width="2"></path>')
    for i in range(10):
        x = cx - 150 * k + i * 30 * k
        if -40 * k < x - cx < 20 * k: continue
        o.append(f'<rect x="{f(x)}" y="{f(wy - 66 * k)}" width="{f(14 * k)}" height="{f(10 * k)}" fill="#1E3A5A" stroke="{CY}" stroke-width="1.4"></rect>')
    tx = cx + 80 * k
    o.append(f'<path d="M{f(tx - 34 * k)} {f(wy - 56 * k)} L {f(tx - 30 * k)} {f(wy - 120 * k)} L {f(tx - 6 * k)} {f(wy - 134 * k)} L {f(tx + 6 * k)} {f(wy - 112 * k)} L {f(tx + 18 * k)} {f(wy - 126 * k)} '
             f'L {f(tx + 30 * k)} {f(wy - 104 * k)} L {f(tx + 34 * k)} {f(wy - 56 * k)} Z" fill="#1E3A5A" stroke="{CY}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(tx - 30 * k)} {f(wy - 190 * k)} L {f(tx + 30 * k)} {f(wy - 190 * k)} L {f(tx + 30 * k)} {f(wy - 140 * k)} L {f(tx - 30 * k)} {f(wy - 140 * k)} Z" fill="none" stroke="{CY}" stroke-width="1.4" stroke-dasharray="5 4"></path>')
    r = random.Random(105)
    for _ in range(16):
        x = cx + r.uniform(-30, 40) * k + r.uniform(0, 1) * 60 * k; y = wy + r.uniform(0, 1) * 60 * k
        sz = r.uniform(5, 11) * k
        o.append(f'<rect x="{f(x)}" y="{f(y - sz)}" width="{f(sz * 1.4)}" height="{f(sz)}" fill="#2C5A7A" stroke="{CY}" stroke-width="1.2" transform="rotate({r.randint(-30, 30)} {f(x)} {f(y)})"></rect>')
    o.append(dim(tx + 46 * k, wy - 190 * k, tx + 46 * k, wy - 124 * k, "CAST DOWN", size=9, color="#FF6A4A"))
    o.append(tag(cx - 120 * k, wy - 40 * k, "STRONGHOLDS", cx - 200 * k, wy - 110 * k, color=CY)
             + tag(tx, wy - 190 * k, "EVERY HIGH THING", tx + 100 * k, wy - 160 * k, color=GOLD))
    return "".join(o)

def balance(cx, top, s, tilt, left="", right=""):
    """A balance: the beam on its post tilted by `tilt` degrees (positive: the left pan down), the pans on cords; left /
    right svg set in the pans (their own units, the pan at 0, 0)."""
    o = [f'<g transform="translate({f(cx)} {f(top)}) scale({f(s)})">',
         f'<path d="M0 0 L 0 170 M-40 170 L 40 170" stroke="#B8860E" stroke-width="6"></path><circle cx="0" cy="0" r="7" fill="#E8B830" stroke="{INK}" stroke-width="2"></circle>']
    a = math.radians(-tilt)
    for side, svg in ((-1, left), (1, right)):
        ex, ey = side * 110 * math.cos(a), side * 110 * math.sin(a)
        o.append(f'<path d="M{f(ex)} {f(ey)} L {f(ex - 34)} {f(ey + 70)} M{f(ex)} {f(ey)} L {f(ex + 34)} {f(ey + 70)}" stroke="#C8A060" stroke-width="1.6"></path>'
                 f'<path d="M{f(ex - 44)} {f(ey + 70)} C {f(ex - 40)} {f(ey + 92)} {f(ex + 40)} {f(ey + 92)} {f(ex + 44)} {f(ey + 70)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>'
                 + f'<g transform="translate({f(ex)} {f(ey + 70)})">{svg}</g>')
    o.append(f'<path d="M{f(-110 * math.cos(a))} {f(-110 * math.sin(a))} L {f(110 * math.cos(a))} {f(110 * math.sin(a))}" stroke="{INK}" stroke-width="9" stroke-linecap="round"></path>'
             f'<path d="M{f(-110 * math.cos(a))} {f(-110 * math.sin(a))} L {f(110 * math.cos(a))} {f(110 * math.sin(a))}" stroke="#E8B830" stroke-width="5" stroke-linecap="round"></path>')
    return "".join(o) + "</g>"

def letters_weighed(w, h):
    """His letters, they say, are weighty and strong; but his bodily presence is weak, and his speech of no account: a plate
    — the balance of the gainsayers, the sealed letter weighing its pan down, the other pan empty and high."""
    import exo.art8 as B
    o = [plate_bg(w, h, "2 CORINTHIANS 10:10 · HIS LETTERS, THEY SAY")]
    k = min(w / 520, (h - 46) / 200)
    o.append(balance(w * 0.5, 50 + 24 * k, k * 0.95, 16, left=sealed_scroll(0, -12, 0.42, rot=-6)))
    a = math.radians(-16); lx = w * 0.5 - 110 * k * 0.95 * math.cos(a); rx = w * 0.5 + 110 * k * 0.95 * math.cos(a)
    ly = 50 + 24 * k + (110 * math.sin(-a) + 100) * k * 0.95; ry = 50 + 24 * k + (-110 * math.sin(-a) + 100) * k * 0.95
    o.append(label(lx, min(ly + 22 * k, h - 10), "WEIGHTY AND STRONG", GOLD, 10) + label(rx, ry + 22 * k, "HIS BODILY PRESENCE · WEAK", CY, 10))
    return "".join(o)

def province(w, h):
    """According to the measure of the province which God apportioned to us as a measure, to reach even unto you … unto the
    parts beyond you: the map — the road of the gospel from Jerusalem and Antioch through Asia and Macedonia even as far as
    Corinth, and an arrow on beyond it westward, over the sea toward Italy (Rom 15:24)."""
    o = geo.med_map(w, h, box=(13.6, 37.4, 30.6, 42.4), places=("JERUSALEM", "ANTIOCH", "TARSUS", "EPHESUS", "TROAS", "PHILIPPI", "CORINTH", "ROME"),
                    routes=[["JERUSALEM", "CÆSAREA", (34.4, 34.6), "ANTIOCH", "TARSUS", "DERBE", "ICONIUM", "ANTIOCH OF PISIDIA", "EPHESUS", "TROAS", "PHILIPPI", "THESSALONICA", "BERŒA", (22.6, 38.6), "CORINTH"],
                            ["CORINTH", (21.0, 38.4), (18.6, 38.9), (16.4, 40.2)]],
                    hi=("CORINTH",), regions=("SYRIA", "ASIA", "MACEDONIA", "ACHAIA", "ITALY", "GALATIA"), lit_routes=[1], size=9,
                    title="2 CORINTHIANS 10:13–16 · THE MEASURE OF THE PROVINCE")
    P = geo.Proj(w, h, (13.6, 37.4, 30.6, 42.4))
    x, y = P(17.6, 39.4)
    return o[:-4] + plate_label(x, y - 10, "THE PARTS BEYOND", "#FF6A4A", 9) + o[-4:]

# ---- 2 Corinthians 11 -----------------------------------------------------------------------------------------------------
def betrothal(w, h, seed):
    """I espoused you to one husband, that I might present you as a pure virgin to Christ: an emblem — two gold rings and a
    lamp burning, laid on a fine white cloth (no bride is drawn)."""
    uid = f"bt{seed}"
    o = [f'<defs><radialGradient id="{uid}" cx="0.5" cy="0.4" r="0.7"><stop offset="0" stop-color="#FFF8E6"></stop><stop offset="0.6" stop-color="#C8A0B8"></stop>'
         f'<stop offset="1" stop-color="#3A2A4A"></stop></radialGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>']
    ty = h * 0.66; k = min(w / 560, h / 240)
    o.append(f'<path d="M-10 {f(ty)} C {f(w * 0.3)} {f(ty - 10)} {f(w * 0.7)} {f(ty - 10)} {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(w * t)} {f(ty)} C {f(w * t + 10)} {f(ty + h * 0.12)} {f(w * t - 8)} {f(ty + h * 0.24)} {f(w * t + 4)} {f(h + 10)}" fill="none" stroke="#D8D2C6" stroke-width="2"></path>' for t in (0.14, 0.32, 0.6, 0.84)))
    cx = w * 0.4
    for dx, rot in ((-24, -10), (24, 14)):
        o.append(f'<ellipse cx="{f(cx + dx * k)}" cy="{f(ty + 6 * k)}" rx="{f(40 * k)}" ry="{f(18 * k)}" fill="none" stroke="{INK}" stroke-width="{f(11 * k)}" transform="rotate({rot} {f(cx + dx * k)} {f(ty + 6 * k)})"></ellipse>'
                 f'<ellipse cx="{f(cx + dx * k)}" cy="{f(ty + 6 * k)}" rx="{f(40 * k)}" ry="{f(18 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(7 * k)}" transform="rotate({rot} {f(cx + dx * k)} {f(ty + 6 * k)})"></ellipse>')
    lx = w * 0.7
    o.append(halo(lx, ty - 40 * k, 90 * k, "#FFE680", 0.6) + clay_lamp(lx, ty + 4 * k, 2.2 * k))
    return "".join(o)

def tent_cloth(p, w, h, seed):
    """When I was present with you and was in want, I was not a burden on any man; for the brethren, when they came from
    Macedonia, supplied the measure of my want: the workshop at Corinth, the dark goat-hair cloth of a tent on its frame (as
    Acts draws Aquila's), Paul sitting at work on it, and two of the brethren come in from Macedonia, one holding out a bag."""
    from act.art import _house
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), bg]
    k = max(0.5, h / 340)
    o.append(f'<path d="M{f(w * 0.14)} {f(b)} L {f(w * 0.2)} {f(b - 150 * k)} L {f(w * 0.54)} {f(b - 160 * k)} L {f(w * 0.6)} {f(b)}" fill="none" stroke="#5A3A22" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(w * 0.21)} {f(b - 146 * k)} L {f(w * 0.53)} {f(b - 156 * k)} L {f(w * 0.52)} {f(b - 50 * k)} L {f(w * 0.23)} {f(b - 46 * k)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(w * 0.22)} {f(b - (140 - 18 * j) * k)} L {f(w * 0.52)} {f(b - (150 - 18 * j) * k)}" stroke="#5A4A3A" stroke-width="1.4"></path>' for j in range(5)))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(seated(w * 0.4, b, s * 0.8, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A"))
    o.append(brother(p, w * 0.7, b, s * 0.98, 0, up=[(-22, -158), (-42, -136), (-60, -128)], extra=bag(-64, -118, 0.5, "#8A6A3A"))
             + brother(p, w * 0.8, b, s, 3) + bag(w * 0.62, b, s * 0.6, "#6A5A3A"))
    return "".join(o)

def abraham_stars(w, h, seed):
    """Are they the seed of Abraham? so am I: the night sky over the desert full of stars, as the stars of heaven were shown
    to Abraham, and the black tents of a camp under them."""
    hz = h * 0.72
    o = [sky(w, h, "#05051A", "#2A2050"), starfield(w, h, seed, 260, 0.72), halo(w * 0.5, h * 0.2, max(w, h) * 0.3, "#8FA8FF", 0.15),
         hills(w, h, hz, seed, color="#14142E", amp=10, step=90), ground(w, h, hz + h * 0.04, "#1A1830", dy=0)]
    for i, x in enumerate((0.16, 0.34, 0.6, 0.8)):
        tw, th = w * 0.12, h * 0.12; y = h * (0.92 + 0.02 * (i % 2))
        o.append(f'<path d="M{f(w * x - tw / 2)} {f(y)} L {f(w * x - tw * 0.36)} {f(y - th)} L {f(w * x + tw * 0.36)} {f(y - th * 0.9)} L {f(w * x + tw / 2)} {f(y)} Z" fill="#0D0D0F" stroke="#3A3456" stroke-width="1.6"></path>'
                 f'<path d="M{f(w * x - tw * 0.08)} {f(y)} L {f(w * x - tw * 0.04)} {f(y - th * 0.5)} L {f(w * x + tw * 0.08)} {f(y)} Z" fill="#FFC14D" opacity="0.7"></path>')
    return "".join(o)

def prison_cell(w, h, seed):
    """In prisons more abundantly: a prison cell, empty — the stone walls, the chains hanging from their rings, a little
    straw on the floor, moonlight through the barred window high in the wall."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2630"></rect>']
    for i in range(int(h / 34) + 2):
        y = i * 34
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#1E1A22" stroke-width="2"></path>')
        for j in range(int(w / 70) + 2):
            x = j * 70 + (35 if i % 2 else 0)
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + 34)}" stroke="#1E1A22" stroke-width="1.6"></path>')
    wx, wy, ww = w * 0.62, h * 0.12, min(w * 0.14, h * 0.3)
    o.append(f'<path d="M{f(wx)} {f(wy + ww * 0.7)} L {f(wx - w * 0.16)} {f(h * 0.94)} L {f(wx + ww + w * 0.06)} {f(h * 0.94)} L {f(wx + ww)} {f(wy + ww * 0.7)} Z" fill="#C8D0E8" opacity="0.18"></path>'
             f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(ww * 0.7)}" fill="#3A4A7A" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(wx + ww * t)} {f(wy)} L {f(wx + ww * t)} {f(wy + ww * 0.7)}" stroke="#1A1A1A" stroke-width="4"></path>' for t in (0.25, 0.5, 0.75)))
    o.append(f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3438" stroke="{INK}" stroke-width="2"></rect>')
    r = random.Random(seed)
    for _ in range(30):
        x = w * r.uniform(0.1, 0.5); y = h * r.uniform(0.9, 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-14, 14))} {f(r.uniform(-3, 3))}" stroke="#B8A060" stroke-width="1.6"></path>')
    for cx in (w * 0.22, w * 0.34):
        o.append(f'<circle cx="{f(cx)}" cy="{f(h * 0.36)}" r="6" fill="none" stroke="#7A7A80" stroke-width="3"></circle>' + chains(cx, h * 0.36 + 6, max(0.6, h / 300), seed, n=1))
    return "".join(o)

def rods_stones(w, h, seed):
    """Thrice was I beaten with rods, once was I stoned: outside the gate of a town in the evening, a bundle of rods laid down
    against the wall, and before the gate a heap of stones on the road — no one there."""
    b = h * 0.92
    o = [sky(w, h, "#3A2A4A", "#D8885A"), hills(w, h, h * 0.56, seed, color="#5A3A44", amp=12, step=80), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    o.append(walls(w * 0.02, w * 0.62, h * 0.66, h * 0.36, seed, color="#A88A6A", gate=True, towers=2))
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.66)} L {f(w * 0.36)} {f(h * 0.66)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#B89A6A" stroke="{INK}" stroke-width="1.6"></path>')
    r = random.Random(seed); hx, hy = w * 0.52, b
    for i in range(26):
        row = i // 6
        x = hx + r.uniform(-1, 1) * (70 - row * 14) * min(1.4, h / 260); y = hy - row * 10 * min(1.4, h / 260) - r.uniform(0, 4)
        rr = r.uniform(7, 12) * min(1.4, h / 260)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr * 1.3)}" ry="{f(rr)}" fill="{r.choice(["#8A8478", "#9A9488", "#7A7468"])}" stroke="{INK}" stroke-width="1.6"></ellipse>')
    rx = w * 0.72; k = min(1.4, h / 260)
    for j in range(7):
        o.append(f'<path d="M{f(rx + j * 7 * k)} {f(b)} L {f(rx + 34 * k + j * 5 * k)} {f(b - 130 * k)}" stroke="{INK}" stroke-width="{f(4.4 * k)}" stroke-linecap="round"></path>'
                 f'<path d="M{f(rx + j * 7 * k)} {f(b)} L {f(rx + 34 * k + j * 5 * k)} {f(b - 130 * k)}" stroke="#8A6A3A" stroke-width="{f(2.4 * k)}" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(rx + 6 * k)} {f(b - 30 * k)} L {f(rx + 56 * k)} {f(b - 30 * k)} M{f(rx + 20 * k)} {f(b - 84 * k)} L {f(rx + 66 * k)} {f(b - 84 * k)}" stroke="#2A1A10" stroke-width="{f(3 * k)}"></path>')
    return "".join(o)

def wreck(p, w, h, seed):
    """Thrice I suffered shipwreck, a night and a day have I been in the deep: a grey sea under a breaking sky, the broken
    hull of a ship lying over in the water, planks and a spar drifting — no one in the water."""
    hz = h * 0.42
    o = [sky(w, h, "#2A3448", "#9AA8B8"), halo(w * 0.8, hz, h * 0.3, "#FFE6B0", 0.35), sea_(w, h, hz, seed, color="#2A5A7A", deep="#0F2A3A", rough=True)]
    k = min(0.9, h / 420)
    o.append(grain_ship(p, w * 0.42, h * 0.66, k, sail="none", tilt=-16, broken=True, mast=False, boat_=False))
    o.append(f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#1F4A66" opacity="0.75"></rect>')
    r = random.Random(seed)
    for _ in range(7):
        x, y = w * r.uniform(0.05, 0.95), h * r.uniform(0.74, 0.96); L = w * r.uniform(0.04, 0.09)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(L)}" height="{f(max(4, h * 0.016))}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4" transform="rotate({r.randint(-14, 14)} {f(x)} {f(y)})"></rect>')
    o.append(waves(w, h, h * 0.86, seed))
    return "".join(o)

def _cell_bg(x, y, cw, ch, top, bot, uid):
    return (f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"></stop><stop offset="1" stop-color="{bot}"></stop></linearGradient></defs>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}" fill="url(#{uid})"></rect>')

def perils(w, h):
    """In perils of rivers, in perils of robbers, in perils from my countrymen, in perils from the Gentiles, in perils in the
    city, in perils in the wilderness, in perils in the sea, in perils among false brethren: a plate of eight cells, each an
    empty place — a river in flood, a narrow pass among the rocks, a synagogue door shut, an idol temple's steps, a city
    street at night, the wilderness, the sea in a storm, a house door ajar in the dark. No one is in any of them."""
    o = [plate_bg(w, h, "2 CORINTHIANS 11:26 · IN PERILS")]
    top, gap, cols = 32, 8, 4
    cw, ch = (w - (cols + 1) * gap) / cols, (h - top - 3 * gap) / 2
    names = ["OF RIVERS", "OF ROBBERS", "FROM MY COUNTRYMEN", "FROM THE GENTILES", "IN THE CITY", "IN THE WILDERNESS", "IN THE SEA", "AMONG FALSE BRETHREN"]
    for i, nm in enumerate(names):
        x, y = gap + (i % cols) * (cw + gap), top + (i // cols) * (ch + gap)
        uid = f"pl{i}"
        o.append(f'<defs><clipPath id="{uid}c"><rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}"></rect></clipPath></defs><g clip-path="url(#{uid}c)">')
        b = y + ch; gy = y + ch * 0.62
        if i == 0:
            o.append(_cell_bg(x, y, cw, ch, "#4A5A6A", "#A8B0B8", uid) + f'<rect x="{f(x)}" y="{f(gy)}" width="{f(cw)}" height="{f(ch)}" fill="#6A5A3A"></rect>'
                     + f'<path d="M{f(x)} {f(gy + 8)} C {f(x + cw * 0.4)} {f(gy)} {f(x + cw * 0.6)} {f(gy + 30)} {f(x + cw)} {f(gy + 14)} L {f(x + cw)} {f(b)} L {f(x)} {f(b)} Z" fill="#5A7A8A" stroke="{INK}" stroke-width="1.4"></path>'
                     + "".join(f'<path d="M{f(x + cw * t)} {f(gy + 24 + 10 * (j % 2))} q 8 -6 16 0 q 8 6 16 0" fill="none" stroke="#D8E8F0" stroke-width="1.6"></path>' for j, t in enumerate((0.1, 0.4, 0.66, 0.2, 0.5))))
        elif i == 1:
            o.append(_cell_bg(x, y, cw, ch, "#3A2A3A", "#C8885A", uid)
                     + f'<path d="M{f(x)} {f(b)} L {f(x)} {f(y + ch * 0.2)} L {f(x + cw * 0.3)} {f(y + ch * 0.34)} L {f(x + cw * 0.4)} {f(b)} Z" fill="#5A4038" stroke="{INK}" stroke-width="1.6"></path>'
                     + f'<path d="M{f(x + cw)} {f(b)} L {f(x + cw)} {f(y + ch * 0.14)} L {f(x + cw * 0.66)} {f(y + ch * 0.3)} L {f(x + cw * 0.58)} {f(b)} Z" fill="#4A3430" stroke="{INK}" stroke-width="1.6"></path>'
                     + f'<path d="M{f(x + cw * 0.4)} {f(b)} L {f(x + cw * 0.47)} {f(y + ch * 0.5)} L {f(x + cw * 0.53)} {f(y + ch * 0.5)} L {f(x + cw * 0.58)} {f(b)} Z" fill="#A88A6A"></path>')
        elif i == 2:
            o.append(_cell_bg(x, y, cw, ch, "#8FD0E2", "#F3E8C8", uid) + f'<rect x="{f(x + cw * 0.14)}" y="{f(y + ch * 0.26)}" width="{f(cw * 0.72)}" height="{f(ch)}" fill="#D8C8A8" stroke="{INK}" stroke-width="1.6"></rect>'
                     + f'<path d="M{f(x + cw * 0.1)} {f(y + ch * 0.26)} L {f(x + cw * 0.5)} {f(y + ch * 0.12)} L {f(x + cw * 0.9)} {f(y + ch * 0.26)} Z" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></path>'
                     + f'<rect x="{f(x + cw * 0.38)}" y="{f(y + ch * 0.5)}" width="{f(cw * 0.24)}" height="{f(ch * 0.5)}" fill="#5A3A1E" stroke="{INK}" stroke-width="1.6"></rect>'
                     + f'<path d="M{f(x + cw * 0.34)} {f(y + ch * 0.72)} L {f(x + cw * 0.66)} {f(y + ch * 0.72)}" stroke="#3A2410" stroke-width="4"></path>')
        elif i == 3:
            o.append(_cell_bg(x, y, cw, ch, "#3A2440", "#C8704A", uid) + f'<path d="M{f(x + cw * 0.08)} {f(y + ch * 0.3)} L {f(x + cw * 0.5)} {f(y + ch * 0.14)} L {f(x + cw * 0.92)} {f(y + ch * 0.3)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="1.6"></path>'
                     + "".join(f'<rect x="{f(x + cw * t)}" y="{f(y + ch * 0.3)}" width="{f(cw * 0.06)}" height="{f(ch * 0.4)}" fill="#9A8A7A" stroke="{INK}" stroke-width="1.2"></rect>' for t in (0.14, 0.32, 0.62, 0.8))
                     + "".join(f'<rect x="{f(x + cw * (0.06 - j * 0.03))}" y="{f(y + ch * (0.7 + j * 0.1))}" width="{f(cw * (0.88 + j * 0.06))}" height="{f(ch * 0.1)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.2"></rect>' for j in range(3)))
        elif i == 4:
            o.append(_cell_bg(x, y, cw, ch, "#05050E", "#2A1A30", uid) + f'<g transform="translate({f(x)} {f(y)})">' + mk.stars(8, cw, ch * 0.3, 40 + i) + '</g>'
                     + "".join(f'<rect x="{f(x + cw * t)}" y="{f(y + ch * hh)}" width="{f(cw * 0.3)}" height="{f(ch)}" fill="#3A3448" stroke="{INK}" stroke-width="1.4"></rect>' for t, hh in ((-0.04, 0.3), (0.74, 0.24)))
                     + f'<path d="M{f(x + cw * 0.26)} {f(b)} L {f(x + cw * 0.44)} {f(y + ch * 0.56)} L {f(x + cw * 0.56)} {f(y + ch * 0.56)} L {f(x + cw * 0.74)} {f(b)} Z" fill="#3A3238"></path>')
        elif i == 5:
            o.append(_cell_bg(x, y, cw, ch, "#FFE6A0", "#E8B880", uid) + f'<rect x="{f(x)}" y="{f(gy)}" width="{f(cw)}" height="{f(ch)}" fill="#D8B880"></rect>'
                     + f'<path d="M{f(x)} {f(gy)} C {f(x + cw * 0.3)} {f(gy - 12)} {f(x + cw * 0.6)} {f(gy - 4)} {f(x + cw)} {f(gy - 14)} L {f(x + cw)} {f(gy)} Z" fill="#C8985A"></path>'
                     + f'<path d="M{f(x + cw * 0.7)} {f(gy + 30)} l 2 -26 m -2 10 l -8 -6 m 9 2 l 7 -8" stroke="#6A5A3A" stroke-width="2" fill="none"></path>')
        elif i == 6:
            o.append(_cell_bg(x, y, cw, ch, "#14141E", "#4A4A5E", uid) + bolt(x + cw * 0.7, y, y + ch * 0.4, 61, color="#C8C8E8", sw=2)
                     + f'<g transform="translate({f(x)} 0)">' + waves(cw, ch + y, y + ch * 0.5, 66) + '</g>')
        else:
            o.append(_cell_bg(x, y, cw, ch, "#1A1420", "#3A2A30", uid) + f'<rect x="{f(x + cw * 0.2)}" y="{f(y + ch * 0.2)}" width="{f(cw * 0.6)}" height="{f(ch)}" fill="#4A3E44" stroke="{INK}" stroke-width="1.6"></rect>'
                     + f'<rect x="{f(x + cw * 0.38)}" y="{f(y + ch * 0.46)}" width="{f(cw * 0.24)}" height="{f(ch * 0.54)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.4"></rect>'
                     + f'<path d="M{f(x + cw * 0.38)} {f(y + ch * 0.46)} L {f(x + cw * 0.5)} {f(y + ch * 0.5)} L {f(x + cw * 0.5)} {f(b)} L {f(x + cw * 0.38)} {f(b)} Z" fill="#3A2410" stroke="{INK}" stroke-width="1.4"></path>')
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="20" fill="#0B1A2E" opacity="0.85"></rect>'
                 + label(x + cw / 2, y + 14, nm, GOLD, 9) + '</g>' + f'<rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}" fill="none" stroke="{CY}" stroke-width="1.4"></rect>')
    return "".join(o)

def cold_camp(w, h, seed):
    """In watchings often, in hunger and thirst, in fastings often, in cold and nakedness: a camp by the road on a frosty
    night, the fire gone to grey ash, a thin cloak and an empty bowl on the ground, the moon small and cold — no one there."""
    hz = h * 0.6
    o = [sky(w, h, "#05051A", "#2A3450"), starfield(w, h, seed, 60, 0.6), moon_(w * 0.8, h * 0.18, max(8, h * 0.035)),
         hills(w, h, hz, seed, color="#1E2438", amp=14, step=80), ground(w, h, hz + h * 0.04, "#3A4050", dy=0)]
    r = random.Random(seed)
    for _ in range(40):
        x, y = w * r.uniform(0, 1), h * r.uniform(0.66, 0.98)
        o.append(f'<path d="M{f(x - 3)} {f(y)} L {f(x + 3)} {f(y)} M{f(x)} {f(y - 3)} L {f(x)} {f(y + 3)}" stroke="#C8D8F0" stroke-width="1" opacity="0.6"></path>')
    k = min(1.4, h / 240); fx, fy = w * 0.42, h * 0.88
    o.append("".join(f'<ellipse cx="{f(fx + dx * k)}" cy="{f(fy)}" rx="{f(9 * k)}" ry="{f(6 * k)}" fill="#5A5A60" stroke="{INK}" stroke-width="1.4"></ellipse>' for dx in (-30, -15, 0, 15, 30))
             + f'<ellipse cx="{f(fx)}" cy="{f(fy - 4 * k)}" rx="{f(22 * k)}" ry="{f(6 * k)}" fill="#8A8A90"></ellipse>' + smoke(fx, fy - 8 * k, 3, seed, color="#8A8A9A", op=0.3))
    o.append(f'<path d="M{f(w * 0.56)} {f(fy + 4)} C {f(w * 0.6)} {f(fy - 20 * k)} {f(w * 0.74)} {f(fy - 18 * k)} {f(w * 0.8)} {f(fy + 4)} Z" fill="#5A4A3A" stroke="{INK}" stroke-width="1.8"></path>'
             f'<path d="M{f(w * 0.24)} {f(fy)} C {f(w * 0.24)} {f(fy + 10 * k)} {f(w * 0.3)} {f(fy + 10 * k)} {f(w * 0.3)} {f(fy)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="1.6"></path>'
             f'<ellipse cx="{f(w * 0.27)}" cy="{f(fy)}" rx="{f(w * 0.03)}" ry="{f(3 * k)}" fill="#2A1A10" stroke="{INK}" stroke-width="1.4"></ellipse>')
    return "".join(o)

# ---- 2 Corinthians 12 -----------------------------------------------------------------------------------------------------
def third_heaven(w, h, seed):
    """Such a one caught up even to the third heaven … caught up into Paradise: a road of light going up from the dark earth
    through the clouds of the sky, through the stars, into a height of white and gold light. (Light only: no one is drawn,
    and God is not drawn.)"""
    uid = f"th{seed}"
    o = [f'<defs><linearGradient id="{uid}" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#0B0B2A"></stop><stop offset="0.45" stop-color="#1E1650"></stop>'
         f'<stop offset="0.75" stop-color="#C8903A"></stop><stop offset="1" stop-color="#FFF8DC"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>', starfield(w, h * 0.7, seed, 70, 1.0)]
    o.append(halo(w * 0.5, -h * 0.05, max(w, h) * 0.5, "#FFFFFF", 0.85) + rays(w * 0.5, -h * 0.05, 30, h * 0.1, max(w, h) * 0.8, "#FFF4C2", 0.3, 5, a0=20, a1=160))
    o.append(f'<path d="M{f(w * 0.47)} {f(h + 10)} L {f(w * 0.53)} {f(h + 10)} L {f(w * 0.6)} -10 L {f(w * 0.4)} -10 Z" fill="#FFF4C2" opacity="0.45"></path>')
    for y, op in ((0.66, 0.5), (0.4, 0.35)):
        o.append(clouds(w, h * y, seed + int(y * 10), n=6, color="#C8C0D8", op=op, h=h))
    o.append(hills(w, h, h * 0.9, seed, color="#0B0B1E", amp=12, step=80) + ground(w, h, h * 0.94, "#05050E", dy=0))
    return "".join(o)

def thorn_branch(w, h, seed):
    """There was given to me a thorn in the flesh: an emblem — a dry branch of thorn lying across a cloth, its long spines
    dark against the evening light. (The messenger of Satan is words only.)"""
    uid = f"tb{seed}"
    o = [f'<defs><radialGradient id="{uid}" cx="0.5" cy="0.45" r="0.7"><stop offset="0" stop-color="#E8B880"></stop><stop offset="1" stop-color="#3A1A2A"></stop></radialGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>']
    k = min(w / 600, h / 220); cy = h * 0.56
    pts = [(w * 0.08, cy + 30 * k), (w * 0.3, cy + 6 * k), (w * 0.55, cy - 4 * k), (w * 0.8, cy - 22 * k), (w * 0.94, cy - 30 * k)]
    d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
    o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{f(13 * k)}" stroke-linecap="round" stroke-linejoin="round"></path>'
             f'<path d="{d}" fill="none" stroke="#5A3A22" stroke-width="{f(8 * k)}" stroke-linecap="round" stroke-linejoin="round"></path>')
    for (x0, y0), (x1, y1), side in ((pts[1], (pts[1][0] + 60 * k, pts[1][1] - 60 * k), -1), (pts[2], (pts[2][0] + 70 * k, pts[2][1] + 50 * k), 1), (pts[3], (pts[3][0] + 40 * k, pts[3][1] - 54 * k), -1)):
        o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="{INK}" stroke-width="{f(8 * k)}" stroke-linecap="round"></path><path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#5A3A22" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>')
    r = random.Random(seed)
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        for j in range(5):
            t = (j + 0.5) / 5; x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t; side = 1 if (i + j) % 2 else -1
            L = r.uniform(22, 34) * k
            o.append(f'<path d="M{f(x - 4 * k)} {f(y)} L {f(x + 10 * k)} {f(y + side * L)} L {f(x + 4 * k)} {f(y)} Z" fill="#2A1A10" stroke="{INK}" stroke-width="1.2"></path>')
    return "".join(o)

def grace_light(p, w, h, seed):
    """I besought the Lord thrice, that it might depart from me. And he hath said unto me, My grace is sufficient for thee:
    Paul sitting bowed on the floor of a room at night, the roll laid by, and the light come down upon him from above (the
    Lord is not drawn: his words are spoken out of the light)."""
    b = h * 0.95
    o = [room(w, h, b, wall="#2A2438", floor="#1E1A28"),
         f'<path d="M{f(w * 0.3)} -10 L {f(w * 0.56)} -10 L {f(w * 0.66)} {f(b)} L {f(w * 0.12)} {f(b)} Z" fill="#FFF4C2" opacity="0.4"></path>',
         halo(w * 0.42, -h * 0.05, max(w, h) * 0.3, "#FFFFFF", 0.85), rays(w * 0.42, -h * 0.06, 20, h * 0.1, h * 1.0, "#FFF4C2", 0.3, 5, a0=50, a1=130)]
    s = (b - max(h * 0.24, b - 200)) / 135
    o.append(seated(w * 0.4, b, s, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A", bowed=True))
    o.append(open_letter(w * 0.66, b - 14, w * 0.12, 12, rows=2, seed=seed))
    return "".join(o)

def ready_to_come(w, h, seed):
    """Behold, this is the third time I am ready to come to you: inside the door at dawn, the traveller's things made ready —
    the staff leaning by the door, the cloak folded and the bag tied, the sandals set out, the door open on the road."""
    b = h * 0.92
    o = [room(w, h, b, wall="#C8A878", floor="#8A6A4A")]
    k = min(1.4, h / 240)
    dx, dw = w * 0.5, min(w * 0.26, 170 * k)
    o.append(doorway(dx, b - 200 * k, dw, b, seed, night=False).replace("#8FD0E2", "#FFD8A0"))
    o.append(f'<path d="M{f(dx - 20 * k)} {f(b)} L {f(dx - 6 * k)} {f(b - 190 * k)}" stroke="{INK}" stroke-width="{f(8 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(dx - 20 * k)} {f(b)} L {f(dx - 6 * k)} {f(b - 190 * k)}" stroke="#7A5A30" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>')
    cx = w * 0.26
    o.append(f'<rect x="{f(cx - 60 * k)}" y="{f(b - 26 * k)}" width="{f(120 * k)}" height="{f(26 * k)}" rx="{f(6 * k)}" fill="#3E3228" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(cx - 56 * k)}" y="{f(b - 44 * k)}" width="{f(112 * k)}" height="{f(20 * k)}" rx="{f(6 * k)}" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></rect>'
             + bag(cx + 20 * k, b - 44 * k, k * 0.9, "#8A6A3A"))
    for sx in (w * 0.36, w * 0.4):
        o.append(f'<ellipse cx="{f(sx)}" cy="{f(b - 3)}" rx="{f(12 * k)}" ry="{f(4 * k)}" fill="#8A5A30" stroke="{INK}" stroke-width="1.6"></ellipse>'
                 f'<path d="M{f(sx - 8 * k)} {f(b - 4)} L {f(sx + 2 * k)} {f(b - 10 * k)} L {f(sx + 8 * k)} {f(b - 4)}" stroke="#5A3418" stroke-width="2" fill="none"></path>')
    return "".join(o)

# ---- 2 Corinthians 13 -----------------------------------------------------------------------------------------------------
def witnesses(p, w, h, seed):
    """At the mouth of two witnesses or three shall every word be established: the gate of the city in the morning, where
    judgment is given, the stone bench in it, and three witnesses standing before it."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.66, "#C8B088", dy=0)]
    gx, gw = w * 0.5, min(w * 0.6, h * 1.4)
    o.append(f'<rect x="{f(gx - gw / 2)}" y="{f(h * 0.08)}" width="{f(gw)}" height="{f(b - h * 0.08)}" fill="#C8A878" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(gx - gw / 2 + j * gw / 9)}" y="{f(h * 0.02)}" width="{f(gw / 18)}" height="{f(h * 0.06 + 1)}" fill="#C8A878" stroke="{INK}" stroke-width="1.6"></rect>' for j in range(9))
             + f'<path d="M{f(gx - gw * 0.3)} {f(b)} L {f(gx - gw * 0.3)} {f(h * 0.42)} C {f(gx - gw * 0.3)} {f(h * 0.2)} {f(gx + gw * 0.3)} {f(h * 0.2)} {f(gx + gw * 0.3)} {f(h * 0.42)} L {f(gx + gw * 0.3)} {f(b)} Z" fill="#E8D8B0" stroke="{INK}" stroke-width="2.2"></path>'
             + f'<rect x="{f(gx - gw * 0.28)}" y="{f(b - h * 0.1)}" width="{f(gw * 0.2)}" height="{f(h * 0.1)}" fill="#9A8A70" stroke="{INK}" stroke-width="1.8"></rect>')
    s = fit(b, max(h * 0.24, b - 200))
    for i, x in enumerate((0.48, 0.6, 0.72)):
        o.append(brother(p, w * x, b, s * (0.97 + 0.03 * (i % 2)), [1, 3, 6][i], flip=True))
    return "".join(o)
