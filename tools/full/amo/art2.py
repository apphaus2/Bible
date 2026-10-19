"""Drawings for Amos chapter 2 (Amos 5–9): the city that went forth a thousand, seek me and live (Beth-el, Gilgal and
Beer-sheba struck through on the map), the Pleiades and Orion, the gate, wailing in the broad ways, the lion, the bear and
the serpent, justice rolling down as waters, the star of your god and captivity beyond Damascus, Calneh, Hamath and Gath,
beds of ivory, the house of ten men empty, horses on the rock, the locusts after the king's mowings, the fire on the great
deep, the plumb-line (a blueprint, no hand drawn), Beth-el the king's sanctuary, the sycomore-trees, the basket of summer
fruit, the false ephah and shekel, the sun gone down at noon, the famine of hearing, the altar and its capitals (the Lord
never drawn), the sieve, the tabernacle of David raised up, the plowman overtaking the reaper."""
from amo.art import *
from amo.art import f, K2
import random, math
import ruth1 as R1x, samuel4 as S4x
from job.art3 import constellations
from chr2.art import judges_gate
from neh.art import booth
from pro.art import two_ways
from ecc.art import sowers
from kg2.art import reapers

def thousand(w, h):
    """The city that went forth a thousand shall have a hundred left, and that which went forth a hundred shall have ten left:
    a chart of dots."""
    o = [grid_bg(w, h)]
    for i, (n, c, t) in enumerate(((1000, "#FFD23F", "A THOUSAND"), (100, "#FF8A6A", "A HUNDRED LEFT"), (10, "#D7261E", "TEN LEFT"))):
        x0 = w * (0.04 + i * 0.33); cw = w * 0.28
        cols = {1000: 40, 100: 10, 10: 5}[n]
        sz = cw / cols
        for j in range(n):
            o.append(f'<rect x="{f(x0 + (j % cols) * sz)}" y="{f(h * 0.16 + (j // cols) * sz)}" width="{f(sz * 0.7)}" height="{f(sz * 0.7)}" fill="{c}" opacity="0.8"></rect>')
        o.append(label(x0 + cw / 2, h * 0.92, t, c, 9))
    return "".join(o)

def fallen_virgin(w, h, seed):
    """The virgin of Israel is fallen; she shall no more rise: the land lying empty under a grey sky, a broken jar on the road."""
    o = [land(w, h, seed, tone="grey", olives=1, horizon=0.44)]
    k = min(1.6, h / 220)
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.9)} C {f(w * 0.44)} {f(h * 0.82)} {f(w * 0.5)} {f(h * 0.78)} {f(w * 0.54)} {f(h * 0.82)} L {f(w * 0.56)} {f(h * 0.9)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.58)} {f(h * 0.9)} l {f(14 * k)} {f(-8 * k)} l {f(6 * k)} {f(8 * k)} Z M{f(w * 0.4)} {f(h * 0.91)} l {f(-12 * k)} {f(-6 * k)} l {f(-4 * k)} {f(6 * k)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def seek_map(w, h, fire=False):
    """Seek not Beth-el, nor enter into Gilgal, and pass not to Beer-sheba: the three struck through on the map; fire=True:
    fire breaking out in the house of Joseph."""
    o = [nations(w, h, extra=("SAMARIA", "BETH-EL", "GILGAL", "JERUSALEM", "BEER-SHEBA"), fire=("BETH-EL",) if fire else (), base=False)]
    for nm in ("BETH-EL", "GILGAL", "BEER-SHEBA"):
        x, y = NAT[nm]
        o.append(f'<path d="M{f(w * x - 12)} {f(h * y - 12)} L {f(w * x + 12)} {f(h * y + 12)} M{f(w * x + 12)} {f(h * y - 12)} L {f(w * x - 12)} {f(h * y + 12)}" stroke="#D7261E" stroke-width="3"></path>')
    return "".join(o)

def mourning_streets(p, w, h, seed):
    """Wailing in all the broad ways: a street of houses, mourners bowed and kneeling, the husbandman called from the field."""
    b = h * 0.95
    from pro.art3 import street_row
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A6A7A", "#B8A8A0"), street_row(w, h, h * 0.72, seed), ground(w, h, h * 0.72, "#9A8A7A", dy=0)]
    s = fit(b, b - h * 0.4)
    for i in range(5):
        x = w * (0.1 + i * 0.2)
        o.append(E.kneel(x, b - (i % 2) * 8, s * 0.9, color=("#5A5048", "#6A5E4A", "#4A4440")[i % 3], skin="#C98E66", flip=i % 2 == 1) if i % 2 else
                 man(p, x, b, s, ("#5A5048", "#6A5E4A", "#4A4440")[i % 3], up=[(-22, -158), (-14, -180), (-4, -190)]))
    return "".join(o)

def flee_lion(w, h):
    """As if a man did flee from a lion, and a bear met him; or leaned his hand on the wall, and a serpent bit him: three
    frames — a lion, a bear, a serpent in the crack of a wall — on the dark field."""
    o = [heraldic(w, h, 3)]
    k = min(h / 200, w / 700)
    o.append(f'<path d="M{f(w * 0.34)} {f(h * 0.1)} L {f(w * 0.34)} {f(h * 0.9)} M{f(w * 0.67)} {f(h * 0.1)} L {f(w * 0.67)} {f(h * 0.9)}" stroke="#FFD23F" stroke-width="1.4" opacity="0.5"></path>')
    o.append(JG.lion(w * 0.02, h * 0.88, k * 0.9, roar=True))
    d = "M-60 0 L -54 -22 C -72 -44 -56 -78 -22 -80 C 12 -84 38 -70 50 -54 C 64 -56 78 -46 78 -36 C 78 -26 68 -22 60 -24 L 52 -14 L 54 0 L 42 0 L 38 -16 L -32 -16 L -34 0 Z"
    o.append(f'<g transform="translate({f(w * 0.5)} {f(h * 0.86)}) scale({f(k * 1.6)})"><path d="{d}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="{f(2.4 / (k * 1.6))}"></path><circle cx="66" cy="-40" r="2.4" fill="#0D0D0F"></circle></g>')
    wx = w * 0.72
    o.append(f'<rect x="{f(wx)}" y="{f(h * 0.18)}" width="{f(w * 0.22)}" height="{f(h * 0.7)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(wx)} {f(h * (0.28 + i * 0.12))} L {f(wx + w * 0.22)} {f(h * (0.28 + i * 0.12))}" stroke="#5A4A3A" stroke-width="1.2"></path>' for i in range(5))
             + f'<path d="M{f(wx + w * 0.1)} {f(h * 0.4)} L {f(wx + w * 0.12)} {f(h * 0.52)} L {f(wx + w * 0.09)} {f(h * 0.62)}" stroke="#1A1210" stroke-width="3" fill="none"></path>')
    from snake import snake
    o.append(snake([(wx + w * 0.11, h * 0.5), (wx + w * 0.16, h * 0.46), (wx + w * 0.2, h * 0.4)], 6 * k * 2, f"sn{int(w)}", 0.6))
    o.append(label(w * 0.17, h * 0.08, "FROM A LION", CYAN, 9) + label(w * 0.5, h * 0.08, "A BEAR MET HIM", CYAN, 9) + label(w * 0.83, h * 0.08, "A SERPENT BIT HIM", CYAN, 9))
    return "".join(o)

def mighty_stream(w, h, seed):
    """Let justice roll down as waters, and righteousness as a mighty stream: a great stream pouring down a rocky slope and
    running on through the valley in the sun."""
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.8, h * 0.16, max(10, h * 0.05), color="#FFE680", op=0.35),
         f'<path d="M-10 {f(h * 0.2)} L {f(w * 0.4)} {f(h * 0.3)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.7, "#8AB84A", dy=0)]
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.22)} C {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.36)} {f(h * 0.72)} C {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.8)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.8)} '
             f'L {f(w + 10)} {f(h * 0.94)} C {f(w * 0.8)} {f(h * 0.92)} {f(w * 0.46)} {f(h * 0.98)} {f(w * 0.24)} {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.6)} {f(w * 0.12)} {f(h * 0.4)} {f(w * 0.02)} {f(h * 0.3)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(24):
        x = r.uniform(0.1, 0.98) * w; y = h * (0.84 if x > w * 0.36 else 0.3 + (x / w) * 1.2)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 24))} 0" stroke="#E8F6FA" stroke-width="2" opacity="0.8"></path>')
    return "".join(o)

def feast_hated(w, h, seed):
    """Your feasts and solemn assemblies, burnt-offerings and the noise of songs and viols: an altar smoking, harps laid down,
    the smoke blown away."""
    o = [K2.sky(w, h, "#5A3A5A", "#C88A6A"), ground(w, h, h * 0.76, "#7A6A5A", dy=0)]
    k = min(1.6, h / 240)
    o.append(horned_altar(w * 0.36, h * 0.8, k * 0.8, fire=True, seed=seed))
    for i in range(2):
        o.append(f'<g transform="translate({f(w * (0.66 + i * 0.14))} {f(h * 0.8)}) rotate({-70 + i * 10}) scale({f(k * 0.6)})"><path d="M-20 0 L -20 -80 C 0 -80 20 -60 20 0 Z" fill="none" stroke="#C8963E" stroke-width="5"></path>'
                 + "".join(f'<path d="M{-20 + j * 8} 0 L {-20 + j * 8} {-76 + j * 6}" stroke="#E8D8B0" stroke-width="1.4"></path>' for j in range(1, 5)) + '</g>')
    return "".join(o)

def beyond_damascus(w, h):
    """Ye have borne the tabernacle of your king and the star of your god; captivity beyond Damascus: the map with the road
    going out past Damascus, a star drawn over it."""
    o = [nations(w, h, lit="DAMASCUS", extra=("SAMARIA", "KIR"), moves=[("SAMARIA", "DAMASCUS"), ("DAMASCUS", "KIR")], title="CAPTIVITY BEYOND DAMASCUS")]
    cx, cy = w * 0.86, h * 0.3
    pts = " ".join(f"{f(cx + math.cos(math.radians(a)) * (18 if i % 2 == 0 else 7))},{f(cy + math.sin(math.radians(a)) * (18 if i % 2 == 0 else 7))}" for i, a in enumerate(range(-90, 270, 36)))
    o.append(f'<polygon points="{pts}" fill="#FF8A6A" fill-opacity="0.4" stroke="#FF8A6A" stroke-width="1.6"></polygon>')
    return "".join(o)

def ease_map(w, h):
    """Pass ye unto Calneh, and see; go to Hamath the great; go down to Gath of the Philistines: the three on the map."""
    return nations(w, h, extra=("JERUSALEM", "SAMARIA", "CALNEH", "HAMATH", "GATH"), moves=[("SAMARIA", "CALNEH"), ("SAMARIA", "HAMATH"), ("JERUSALEM", "GATH")], title="ARE THEY BETTER THAN THESE KINGDOMS?", base=False)

def ivory_beds(w, h, seed):
    """Beds of ivory, lambs and calves of the stall, idle songs to the viol, wine in bowls, the chief oils: the couch, the
    bowls and the viol, and no one grieved."""
    o = [couch(w, h, seed)]
    k = min(1.4, h / 220)
    for i in range(3): o.append(bowl(w * (0.16 + i * 0.07), h * 0.98, k * 0.8, fill="#7A1A3A", color="#E8B830"))
    o.append(f'<g transform="translate({f(w * 0.84)} {f(h * 0.96)}) rotate(-20) scale({f(k * 0.7)})"><path d="M-20 0 L -20 -80 C 0 -80 20 -60 20 0 Z" fill="none" stroke="#C8963E" stroke-width="5"></path>'
             + "".join(f'<path d="M{-20 + j * 8} 0 L {-20 + j * 8} {-76 + j * 6}" stroke="#E8D8B0" stroke-width="1.4"></path>' for j in range(1, 5)) + '</g>')
    return "".join(o)

def broken_house(w, h, seed):
    """The great house smitten with breaches, and the little house with clefts: two houses cracked and empty (no one drawn)."""
    o = [K2.sky(w, h, "#5A4A5A", "#B8A090"), ground(w, h, h * 0.84, "#7A6A5A", dy=0)]
    for (x, bw, bh) in ((0.32, 0.36, 0.5), (0.76, 0.2, 0.3)):
        X, B = w * x, h * 0.84
        o.append(f'<rect x="{f(X - w * bw / 2)}" y="{f(B - h * bh)}" width="{f(w * bw)}" height="{f(h * bh)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 f'<rect x="{f(X - w * bw * 0.08)}" y="{f(B - h * bh * 0.5)}" width="{f(w * bw * 0.16)}" height="{f(h * bh * 0.5)}" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M{f(X + w * bw * 0.2)} {f(B - h * bh)} L {f(X + w * bw * 0.12)} {f(B - h * bh * 0.7)} L {f(X + w * bw * 0.26)} {f(B - h * bh * 0.5)} L {f(X + w * bw * 0.18)} {f(B - h * bh * 0.2)}" stroke="#0D0D0F" stroke-width="3" fill="none"></path>')
    return "".join(o)

def rock_plow(p, w, h, seed):
    """Shall horses run upon the rock? will one plow there with oxen?: a bare crag, a horse balking at its edge."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#E8E0C8"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.6)} L {f(w * 0.2)} {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.46)} L {f(w * 0.7)} {f(h * 0.36)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A847A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(6):
        o.append(f'<path d="M{f(w * (0.1 + i * 0.15))} {f(h * 0.6)} l {f(w * 0.06)} {f(h * 0.1)} l {f(-w * 0.03)} {f(h * 0.1)}" stroke="#5A5450" stroke-width="2" fill="none"></path>')
    k = min(1.0, h / 300)
    o.append(E3.horse(w * 0.5, h * 0.46, k * 0.6, color="#5A3A22"))
    return "".join(o)

def hamath_arabah(w, h):
    """A nation raised up to afflict them from the entrance of Hamath unto the brook of the Arabah, as a map."""
    o = [nations(w, h, extra=("HAMATH", "SAMARIA", "JERUSALEM", "ARABAH"), title="FROM THE ENTRANCE OF HAMATH UNTO THE BROOK OF THE ARABAH", base=False)]
    (x0, y0), (x1, y1) = NAT["HAMATH"], NAT["ARABAH"]
    o.append(f'<path d="M{f(w * x0)} {f(h * y0 + 10)} C {f(w * 0.7)} {f(h * 0.3)} {f(w * 0.56)} {f(h * 0.6)} {f(w * x1)} {f(h * y1)}" fill="none" stroke="#D7261E" stroke-width="{f(max(6, w * 0.02))}" opacity="0.5"></path>')
    return "".join(o)

def mowings(w, h, seed):
    """Locusts formed in the beginning of the shooting up of the latter growth, after the king's mowings: a mown field with
    green regrowth, a swarm coming down on it."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.44, seed, "#8A9A5A", amp=12, step=100), ground(w, h, h * 0.54, "#C8B070", dy=0)]
    for i in range(6):
        y = h * (0.6 + i * 0.07)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 4)}" stroke="#8AB84A" stroke-width="{f(4 + i)}"></path>')
    o.append(swarm(w, h, seed, n=int(w * h / 1600), y0=0.04, y1=0.5, dark=False))
    return "".join(o)

def fire_deep(w, h, seed):
    """The Lord Jehovah called to contend by fire; and it devoured the great deep: the sea dried to its bed, fire upon it,
    reaching toward the land."""
    o = [K2.sky(w, h, "#3A1A1A", "#C8603A"), f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#5A3A2A" stroke="#0D0D0F" stroke-width="2"></rect>']
    for i in range(6):
        o.append(E.blaze(w * (0.08 + i * 0.17), h * 0.9, w * 0.14, h * 0.3, seed + i, n=5))
    o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.42)} L {f(w + 10)} {f(h * 0.5)} Z" fill="#7A9A4A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def plumb(w, h, labels=True):
    """A wall made by a plumb-line, and a plumb-line set in the midst of the people, as a blueprint: the wall in elevation, a
    line hanging straight from above with its weight (no hand drawn), the bow of the wall measured against it."""
    o = [bp(w, h)] + ([title_bar(w, "A WALL MADE BY A PLUMB-LINE")] if labels else [])
    x0, x1, top, base = w * 0.18, w * 0.62, h * 0.24, h * 0.9
    rows = 9
    for i in range(rows):
        y = base - (base - top) * i / rows
        lean = (i / rows) ** 2 * w * 0.04
        o.append(f'<rect x="{f(x0 + lean)}" y="{f(y - (base - top) / rows)}" width="{f(x1 - x0)}" height="{f((base - top) / rows)}" fill="none" stroke="{CYAN}" stroke-width="1.4"></rect>')
    px = x1 + w * 0.06
    o.append(f'<path d="M{f(px)} {f(h * 0.12)} L {f(px)} {f(base - 22)}" stroke="#FFD23F" stroke-width="1.6"></path>'
             f'<path d="M{f(px - 9)} {f(base - 26)} L {f(px + 9)} {f(base - 26)} L {f(px)} {f(base - 4)} Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></path>')
    o.append(dim(x1 + 4, top, px - 4, top, "OUT OF TRUE", color="#FF8A6A", size=8))
    o.append(tag(px, h * 0.5, "THE PLUMB-LINE", w * 0.96, h * 0.42, color="#FFD23F"))
    if labels: o.append(tag(x0 + w * 0.2, base - 10, "MY PEOPLE ISRAEL", x1 + w * 0.1, h * 0.97, color=CYAN))
    return "".join(o)

def kings_sanctuary(p, w, h, seed, amos=True):
    """Beth-el, the king's sanctuary and a royal house: the calf's high place and the altar; Amaziah in white before it,
    Amos with his staff facing him."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A3A5A", "#E8A06A"), hills(w, h, h * 0.5, seed, "#6A5A4A", amp=14, step=100), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    k = min(1.2, h / 300)
    o.append(V.calf(w * 0.5, h * 0.62, k * 0.55, uid=f"ks{seed}"))
    s = fit(b, b - h * 0.5)
    o.append(amaziah_fig(p, w * 0.72, b, s, flip=True, up=[(-22, -158), (-46, -168), (-70, -170)]))
    if amos: o.append(amos_fig(p, w * 0.24, b, s))
    return "".join(o)

def sycomore(p, w, h, seed):
    """I was a herdsman, and a dresser of sycomore-trees: Amos at a broad sycomore-fig, his flock under it."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#9AB8D8", "#F3E0B0"), hills(w, h, h * 0.5, seed, "#B8A070", amp=14, step=110), ground(w, h, h * 0.62, "#C8A878", dy=0)]
    k = min(2.0, h / 180)
    o.append(tree(w * 0.66, h * 0.86, k, color="#4A7A3A", kind="round", seed=seed))
    o.append(flock(w * 0.5, w * 0.96, h * 0.82, b, 7, seed))
    o.append(amos_fig(p, w * 0.24, b, fit(b, b - h * 0.5), up=[(-22, -158), (-34, -184), (-28, -210)]))
    return "".join(o)

def summer_basket(w, h, seed):
    """A basket of summer fruit: a woven basket heaped with figs, grapes and pomegranates (a plate)."""
    o = [grid_bg(w, h), title_bar(w, "A BASKET OF SUMMER FRUIT")]
    k = min(2.0, h / 150)
    cx, cy = w * 0.5, h * 0.66
    o.append(f'<path d="M{f(cx - 90 * k)} {f(cy - 20 * k)} L {f(cx + 90 * k)} {f(cy - 20 * k)} L {f(cx + 70 * k)} {f(cy + 40 * k)} L {f(cx - 70 * k)} {f(cy + 40 * k)} Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(cx - 86 * k + i * 12 * k)} {f(cy - 20 * k)} L {f(cx - 68 * k + i * 10 * k)} {f(cy + 40 * k)}" stroke="#8A6A3A" stroke-width="1.4"></path>' for i in range(15)))
    r = random.Random(seed)
    for i in range(16):
        x = cx + r.uniform(-80, 80) * k; y = cy - 20 * k - r.uniform(0, 34) * k * (1 - abs(x - cx) / (100 * k))
        kind = i % 3
        c = ("#5A2A4A", "#4A1A4A", "#C8303A")[kind]
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f((8, 5, 11)[kind] * k)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)

def silent_court(w, h, seed):
    """The songs of the temple shall be wailings in that day; in every place they shall cast them forth with silence: the
    court of the house empty at dusk (nothing else drawn)."""
    o = [K2.sky(w, h, "#2A1A2A", "#8A5A5A"), temple_front(w * 0.5, h * 0.8, w * 0.5, seed), ground(w, h, h * 0.8, "#5A4A44", dy=0),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0F0E2A" opacity="0.3"></rect>']
    return "".join(o)

def false_measures(w, h):
    """Making the ephah small, and the shekel great, and dealing falsely with balances of deceit: the true ephah beside the
    small one, the true shekel beside the great one, a balance tipped."""
    o = [grid_bg(w, h)]
    k = min(1.6, h / 140)
    for i, (x, sc, t, c) in enumerate(((0.12, 1.0, "AN EPHAH", "#8FD0E2"), (0.28, 0.7, "SMALL", "#FF8A6A"))):
        cx, by = w * x, h * 0.74
        o.append(f'<path d="M{f(cx - 30 * k * sc)} {f(by)} L {f(cx - 24 * k * sc)} {f(by - 50 * k * sc)} L {f(cx + 24 * k * sc)} {f(by - 50 * k * sc)} L {f(cx + 30 * k * sc)} {f(by)} Z" fill="{c}" fill-opacity="0.25" stroke="{c}" stroke-width="2"></path>'
                 + label(cx, h * 0.88, t, c, 8))
    for i, (x, r_, t, c) in enumerate(((0.48, 10, "A SHEKEL", "#8FD0E2"), (0.62, 16, "GREAT", "#FF8A6A"))):
        o.append(f'<circle cx="{f(w * x)}" cy="{f(h * 0.6)}" r="{f(r_ * k)}" fill="{c}" fill-opacity="0.25" stroke="{c}" stroke-width="2"></circle>' + label(w * x, h * 0.88, t, c, 8))
    cx, cy = w * 0.86, h * 0.36
    o.append(f'<path d="M{f(cx)} {f(cy)} L {f(cx)} {f(h * 0.8)}" stroke="#FFD23F" stroke-width="2"></path><path d="M{f(cx - 50 * k)} {f(cy + 16 * k)} L {f(cx + 50 * k)} {f(cy - 16 * k)}" stroke="#FFD23F" stroke-width="2"></path>'
             + label(cx, h * 0.88, "BALANCES OF DECEIT", "#FF8A6A", 8))
    return "".join(o)

def noon_dark(w, h, seed):
    """I will cause the sun to go down at noon, and darken the earth in the clear day: the sun black at its height over a
    darkened land; the River rising."""
    o = [land(w, h, seed, tone="night", olives=2, horizon=0.5), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0F0E2A" opacity="0.3"></rect>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.18)}" r="{f(min(w, h) * 0.08)}" fill="#0D0D0F" stroke="#FF8A3D" stroke-width="3"></circle>']
    return "".join(o)

def famine_map(w, h):
    """They shall wander from sea to sea, and from the north even to the east, to seek the word of Jehovah, and shall not find
    it: the map crossed with wandering paths that lead nowhere."""
    o = [nations(w, h, extra=("SAMARIA", "DAN", "BEER-SHEBA"), title="FROM SEA TO SEA · FROM THE NORTH EVEN TO THE EAST")]
    r = random.Random(4)
    for i in range(5):
        pts = [(w * r.uniform(0.15, 0.85), h * r.uniform(0.1, 0.9)) for _ in range(4)]
        o.append(route(pts, color="#8FD0E2", arrow=False))
    return "".join(o)

def altar_capitals(w, h, seed):
    """Smite the capitals, that the thresholds may shake: the altar before the house, the capitals of its pillars cracking and
    falling, the thresholds shaken (the Lord standing beside the altar is never drawn)."""
    o = [K2.sky(w, h, "#2A1A2A", "#8A4A3A"), ground(w, h, h * 0.86, "#4A3A34", dy=0)]
    k = min(1.6, h / 240)
    for i, x in enumerate((0.28, 0.72)):
        X = w * x
        o.append(f'<rect x="{f(X - 14 * k)}" y="{f(h * 0.3)}" width="{f(28 * k)}" height="{f(h * 0.56)}" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<g transform="rotate({-14 if i == 0 else 18} {f(X)} {f(h * 0.3)})"><rect x="{f(X - 26 * k)}" y="{f(h * 0.3 - 30 * k)}" width="{f(52 * k)}" height="{f(30 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect></g>'
                 f'<path d="M{f(X - 6 * k)} {f(h * 0.32)} L {f(X + 4 * k)} {f(h * 0.42)} L {f(X - 4 * k)} {f(h * 0.5)}" stroke="#0D0D0F" stroke-width="2" fill="none"></path>')
    o.append(horned_altar(w * 0.5, h * 0.88, k * 0.6, fire=True, seed=seed))
    o.append("".join(f'<path d="M{f(w * (0.1 + i * 0.2))} {f(h * 0.88)} l 8 6 l -6 6 l 10 6" stroke="#C8A06A" stroke-width="2" fill="none"></path>' for i in range(5)))
    return "".join(o)

def nowhere(w, h):
    """Though they dig into Sheol, though they climb up to heaven, though they hide in the top of Carmel, though they be hid in
    the bottom of the sea, though they go into captivity: five frames, each with a place and a mark found there."""
    o = [grid_bg(w, h)]
    m = min(w, h)
    for i, t in enumerate(("SHEOL", "HEAVEN", "THE TOP OF CARMEL", "THE BOTTOM OF THE SEA", "CAPTIVITY")):
        cx = w * (0.1 + i * 0.2); cy = h * 0.48
        o.append(f'<rect x="{f(cx - w * 0.085)}" y="{f(h * 0.16)}" width="{f(w * 0.17)}" height="{f(h * 0.64)}" fill="none" stroke="#1E5A7A" stroke-width="1.4"></rect>')
        if i == 0: o.append("".join(f'<path d="M{f(cx - m * 0.12 + j * m * 0.02)} {f(cy - m * 0.1 + j * m * 0.05)} L {f(cx + m * 0.12 - j * m * 0.02)} {f(cy - m * 0.1 + j * m * 0.05)}" stroke="#8A7A6A" stroke-width="2"></path>' for j in range(5)))
        if i == 1: o.append(mk.stars(14, m * 0.24, m * 0.2, 9 + i).replace('<g fill', f'<g transform="translate({f(cx - m * 0.12)} {f(cy - m * 0.1)})" fill'))
        if i == 2: o.append(f'<path d="M{f(cx - m * 0.12)} {f(cy + m * 0.08)} L {f(cx)} {f(cy - m * 0.1)} L {f(cx + m * 0.12)} {f(cy + m * 0.08)} Z" fill="#3A5A3A" stroke="#9CCB5E" stroke-width="1.6"></path>')
        if i == 3: o.append("".join(f'<path d="M{f(cx - m * 0.12)} {f(cy - m * 0.08 + j * m * 0.05)} q {f(m * 0.06)} {f(-m * 0.03)} {f(m * 0.12)} 0 t {f(m * 0.12)} 0" fill="none" stroke="#2C9DB8" stroke-width="2"></path>' for j in range(4)))
        if i == 4: o.append("".join(f'<ellipse cx="{f(cx - m * 0.08 + j * m * 0.055)}" cy="{f(cy)}" rx="{f(m * 0.035)}" ry="{f(m * 0.022)}" fill="none" stroke="#C8D0D8" stroke-width="2.4"></ellipse>' for j in range(4)))
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(m * 0.05)}" fill="none" stroke="#FF8A6A" stroke-width="2" opacity="0.8"></circle>' + label(cx, h * 0.9, t, CYAN, 8))
    return "".join(o)

def chambers(w, h, seed):
    """He that buildeth his chambers in the heavens and hath founded his vault upon the earth, that calleth for the waters of
    the sea and poureth them out upon the face of the earth: the sky vaulted over the land, rain pouring from the clouds."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A4A6A", "#9AB8D8"), f'<path d="M-10 {f(h * 0.7)} A {f(w * 0.6)} {f(h * 0.6)} 0 0 1 {f(w + 10)} {f(h * 0.7)}" fill="none" stroke="#C8E8F0" stroke-width="2" opacity="0.6"></path>',
         hills(w, h, h * 0.66, seed, "#6A7A5A", amp=10, step=100), ground(w, h, h * 0.76, "#7A8A5A", dy=0)]
    from job.art import clouds
    o.append(clouds(w, h * 0.2, seed, n=6, color="#8A9AA8", op=0.9, ry=0.06))
    o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(h * 0.26, h * 0.7))} l -5 14" stroke="#C8E8F0" stroke-width="1.4"></path>' for _ in range(70)))
    return "".join(o)

def sieve(w, h):
    """I will sift the house of Israel among all the nations, like as grain is sifted in a sieve, yet shall not the least kernel
    fall upon the earth: a sieve, the chaff falling through and the kernels kept."""
    o = [grid_bg(w, h)]
    k = min(1.8, h / 140)
    cx, cy = w * 0.5, h * 0.42
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(110 * k)}" ry="{f(26 * k)}" fill="none" stroke="#C8A06A" stroke-width="4"></ellipse>'
             f'<path d="M{f(cx - 110 * k)} {f(cy)} C {f(cx - 100 * k)} {f(cy + 40 * k)} {f(cx + 100 * k)} {f(cy + 40 * k)} {f(cx + 110 * k)} {f(cy)}" fill="none" stroke="#C8A06A" stroke-width="2"></path>')
    for i in range(-8, 9):
        o.append(f'<path d="M{f(cx + i * 12 * k)} {f(cy - 20 * k)} L {f(cx + i * 12 * k)} {f(cy + 28 * k)}" stroke="#8A6A3A" stroke-width="0.8" opacity="0.7"></path>')
    r = random.Random(2)
    o.append("".join(f'<ellipse cx="{f(cx + r.uniform(-80, 80) * k)}" cy="{f(cy - r.uniform(0, 14) * k)}" rx="{f(4 * k)}" ry="{f(2.4 * k)}" fill="#FFD23F"></ellipse>' for _ in range(24)))
    o.append("".join(f'<path d="M{f(cx + r.uniform(-90, 90) * k)} {f(cy + r.uniform(40, 120) * k)} l {f(4 * k)} {f(2 * k)}" stroke="#8A8460" stroke-width="1.6"></path>' for _ in range(20)))
    o.append(label(cx, h * 0.12, "NOT THE LEAST KERNEL SHALL FALL", "#FFD23F", 9))
    return "".join(o)

def exodus_peoples(w, h):
    """Have not I brought up Israel out of the land of Egypt, and the Philistines from Caphtor, and the Syrians from Kir? —
    three arrows on the map."""
    o = [grid_bg(w, h),
         f'<path d="M-10 {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>']
    pts = {"EGYPT": (0.3, 0.86), "CAPHTOR": (0.12, 0.6), "KIR": (0.92, 0.12), "ISRAEL": (0.6, 0.42), "PHILISTIA": (0.52, 0.56), "SYRIA": (0.72, 0.24)}
    for nm, (x, y) in pts.items(): o.append(node(w * x, h * y, nm, "#FFD23F" if nm in ("ISRAEL", "PHILISTIA", "SYRIA") else CYAN, r=6, dy=-12, size=9))
    for a, b2 in (("EGYPT", "ISRAEL"), ("CAPHTOR", "PHILISTIA"), ("KIR", "SYRIA")):
        (x0, y0), (x1, y1) = pts[a], pts[b2]
        o.append(route([(w * x0, h * y0), (w * x1, h * y1)], color="#FF8A6A"))
    return "".join(o)

def tabernacle_david(p, w, h, seed):
    """I will raise up the tabernacle of David that is fallen, and close up the breaches thereof: a booth rebuilt on the hill
    of Zion, builders setting its poles, the breaches in the wall closed with new stones."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="dawn", olives=1, horizon=0.4)]
    o.append(booth(w * 0.56, h * 0.82, w * 0.3, h * 0.4, seed))
    s = fit(b, b - h * 0.4)
    o.append(man(p, w * 0.18, b, s, "#6A5A3A", up=[(-22, -158), (-34, -184), (-28, -210)]) + man(p, w * 0.86, b, s, "#5A6A8A", flip=True, up=[(-22, -158), (-40, -172), (-56, -186)]))
    return "".join(o)

def overtake(p, w, h, seed):
    """The plowman shall overtake the reaper, and the treader of grapes him that soweth seed; the mountains shall drop sweet
    wine: reapers in ripe grain, a plowman already behind them, vineyards on the hills."""
    o = [reapers(p, w, h, seed)]
    return "".join(o)

def planted(w, h, seed):
    """I will plant them upon their land, and they shall no more be plucked up: the land with waste cities rebuilt, vineyards
    and gardens planted, a young tree set in the ground."""
    o = [land(w, h, seed, tone="day", olives=3, horizon=0.4), J.city_hill(w * 0.76, h * 0.56, w * 0.18, h * 0.14, seed), vine_rows(w, h, h * 0.72, h * 0.98, seed, rows=3, grapes=True)]
    return "".join(o)
