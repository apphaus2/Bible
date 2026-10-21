"""Drawings for Zechariah 9–11 (chapter 3 of the volume), on zec.art: the burden upon Hadrach as a map, Tyre's stronghold
in the sea burning, the Philistine cities, the house encamped about; the king lowly riding upon an ass, a colt the foal of
an ass; the prisoners in the pit without water; the bow of Judah and the arrow as lightning; the latter rain; the flock
without a shepherd; the scattered gathered from Egypt and Assyria (a map); Lebanon's cedars burning; the flock of slaughter
and the two staves Beauty and Bands; the thirty pieces of silver weighed and cast to the potter; the foolish shepherd's
gear. Restraint: 11:4–9 and 11:16 are words over the empty pasture and the scattered flock."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from zec.art import *
from zec.art import f, vision, GOLD, CY
import numbers1 as N1
from genesis.art3 import STAFF, HOLD_STAFF

NORTH = [("HADRACH", 0.7, 0.12), ("HAMATH", 0.56, 0.18), ("DAMASCUS", 0.72, 0.34), ("SIDON", 0.32, 0.3), ("TYRE", 0.28, 0.42),
         ("ASHDOD", 0.18, 0.74), ("EKRON", 0.3, 0.7), ("ASHKELON", 0.14, 0.84), ("GAZA", 0.1, 0.94), ("JERUSALEM", 0.42, 0.78)]

def burden_map(w, h, lit=()):
    """The burden upon the land of Hadrach and Damascus, Hamath, Tyre and Sidon, and the cities of the Philistines: a
    technical map from Hadrach in the north down the coast to Gaza."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.24)} -10 C {f(w * 0.22)} {f(h * 0.3)} {f(w * 0.16)} {f(h * 0.6)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.08, h * 0.2, "THE SEA", CY, 9))
    for name, x, y in NORTH:
        c = GOLD if name == "JERUSALEM" else ("#FF8A6A" if name in lit else CY)
        o.append(node(w * x, h * y, "", color=c, r=5) + label(w * x + 10, h * y + 4, name, c, 9, anchor="start"))
    return "".join(o)

def tyre_fire(w, h, seed):
    """Tyre did build herself a stronghold, and heaped up silver as the dust; she shall be devoured with fire: the island
    fortress in the sea burning."""
    o = [sky(w, h, "#2A0A10", "#C8502A"), sea(w, h, h * 0.62, seed, color="#1F4A6A", deep="#0B1A2E"),
         f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.66)}" rx="{f(w * 0.3)}" ry="{f(h * 0.06)}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></ellipse>',
         walls(w * 0.3, w * 0.82, h * 0.66, h * 0.3, seed, color="#8A6A5A", towers=3), fires(w * 0.3, w * 0.82, h * 0.52, h * 0.26, seed, n=5),
         smokes([w * 0.4, w * 0.56, w * 0.72], h * 0.36, seed, k=max(0.6, h / 360), color="#2A1A1E")]
    return "".join(o)

def encamp(w, h, seed):
    """I will encamp about my house against the army, that none pass through or return: the house on the mount ringed with
    a guarding light."""
    o = [sky(w, h, "#0B0B2A", "#3A2A5A"), starfield(w, h, seed, 40, 0.5), mount_zion(w * 0.5, h * 0.92, w * 0.36, h * 0.56, seed, color="#4A4060", lit=True)]
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" rx="{f(w * 0.42)}" ry="{f(h * 0.26)}" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 6" opacity="0.8"></ellipse>'
             + halo(w * 0.5, h * 0.5, h * 0.4, "#FFE680", 0.3))
    return "".join(o)

def king_ass(p, w, h, seed):
    """Behold, thy king cometh unto thee; he is just, and having salvation; lowly, and riding upon an ass, even upon a colt
    the foal of an ass: a king in a plain white robe with a small gold circlet, on an ass, a colt beside her, the gate of
    Jerusalem ahead (no face)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A7AB8", "#FFE6A0"), sun(w * 0.2, h * 0.24, max(14, h * 0.06), color="#FFE680", op=0.4),
         walls(w * 0.5, w * 1.06, h * 0.7, min(h * 0.46, w * 0.36), seed, color="#C8A878", towers=2), ground(w, h, h * 0.7, "#C8B080", dy=0),
         f'<path d="M{f(w * 0.02)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.56)} {f(h * 0.76)} {f(w * 0.66)} {f(h * 0.7)} L {f(w * 0.72)} {f(h * 0.7)} C {f(w * 0.66)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.92)} {f(w * 0.36)} {f(h + 10)} Z" fill="#E0CC98" opacity="0.8"></path>']
    k = min(0.7, h / 520)
    crown = '<path d="M-12 -196 L 12 -196 L 10 -202 L -10 -202 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>'
    o.append(N1.mount(w * 0.36, b, k, color="#8A8478", rider_body=SKIN, rider_cloth="#F3EFE6", p=p, extra=crown))
    o.append(N1.ass(w * 0.36 - 96 * k, b + 4, k * 0.6, color="#9A948A"))
    o.append(halo(w * 0.36, b - 160 * k, 70 * k, "#FFF4C2", 0.35))
    return "".join(o)

def peace_nations(w, h, seed):
    """I will cut off the chariot and the horse and the battle bow; he shall speak peace unto the nations, and his dominion
    from sea to sea: a broken bow and a chariot wheel laid down, and a map of the earth from sea to sea."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.06)} {f(h * 0.6)} {f(w * 0.04)} {f(h * 0.8)} -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             f'<path d="M{f(w + 10)} {f(h * 0.3)} C {f(w * 0.92)} {f(h * 0.5)} {f(w * 0.94)} {f(h * 0.8)} {f(w + 10)} {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + route([(w * 0.06, h * 0.2), (w * 0.94, h * 0.2)], color=GOLD) + route([(w * 0.94, h * 0.2), (w * 0.06, h * 0.2)], color=GOLD)
             + label(w * 0.5, h * 0.14, "FROM SEA TO SEA", GOLD, 10))
    k = min(1.2, h / 260); x, y = w * 0.36, h * 0.74
    o.append(f'<path d="M{f(x - 60 * k)} {f(y - 40 * k)} C {f(x - 20 * k)} {f(y - 90 * k)} {f(x + 10 * k)} {f(y - 70 * k)} {f(x + 4 * k)} {f(y - 30 * k)}" stroke="#C8A060" stroke-width="{f(6 * k)}" fill="none"></path>'
             f'<path d="M{f(x + 14 * k)} {f(y - 24 * k)} C {f(x + 30 * k)} {f(y + 10 * k)} {f(x + 60 * k)} {f(y + 20 * k)} {f(x + 80 * k)} {f(y + 10 * k)}" stroke="#C8A060" stroke-width="{f(6 * k)}" fill="none"></path>')
    cx, cy, r = w * 0.66, h * 0.72, 40 * k
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="{CY}" stroke-width="{f(5 * k)}"></circle>'
             + "".join(f'<path d="M{f(cx)} {f(cy)} L {f(cx + r * math.cos(a))} {f(cy + r * math.sin(a))}" stroke="{CY}" stroke-width="{f(3 * k)}"></path>' for a in (0.3, 1.5, 2.6, 3.8, 5.0)))
    return "".join(o)

def pit(w, h, seed):
    """I have set free thy prisoners from the pit wherein is no water; turn you to the stronghold, ye prisoners of hope: a
    dry cistern seen from inside, its mouth open to the light, a rope let down."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1E16"></rect>',
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.1)}" rx="{f(w * 0.2)}" ry="{f(h * 0.08)}" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="2.4"></ellipse>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.1)} {f(h + 10)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.7)} {f(h * 0.1)}" fill="#4A3424" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.12)} L {f(w * 0.26)} {f(h + 10)} L {f(w * 0.74)} {f(h + 10)} L {f(w * 0.64)} {f(h * 0.12)} Z" fill="#FFE680" opacity="0.18"></path>']
    r = random.Random(seed)
    for i in range(16):
        y = h * (0.2 + i * 0.05); x = w * (0.3 - (i * 0.05) * 0.4) if i % 2 else w * (0.7 + (i * 0.05) * 0.4)
        o.append(f'<path d="M{f(x - 20)} {f(y)} l 40 0" stroke="#2A1A10" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.1)} C {f(w * 0.52)} {f(h * 0.4)} {f(w * 0.48)} {f(h * 0.6)} {f(w * 0.5)} {f(h * 0.9)}" stroke="#C8A060" stroke-width="4" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.94)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.9)} {f(h * 0.94)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(w * r.uniform(0.2, 0.8))} {f(h * 0.95)} l {f(r.uniform(-14, 14))} 6" stroke="#5A3A22" stroke-width="1.6"></path>' for _ in range(8)))
    return "".join(o)

def bow_lightning(w, h, seed):
    """I have bent Judah for me, I have filled the bow with Ephraim; his arrow shall go forth as the lightning; the Lord
    Jehovah will blow the trumpet and go with whirlwinds of the south: a great bow drawn against a stormy sky, lightning
    for the arrow (God is not drawn)."""
    o = [sky(w, h, "#0B0B2A", "#5A4A7A"), clouds(w, h * 0.12, seed, n=7, color="#1A1430", op=0.9, h=h)]
    k = min(1.4, h / 260); x, y = w * 0.3, h * 0.56
    o.append(f'<path d="M{f(x)} {f(y - 140 * k)} C {f(x + 90 * k)} {f(y - 80 * k)} {f(x + 90 * k)} {f(y + 80 * k)} {f(x)} {f(y + 140 * k)}" stroke="#C8A060" stroke-width="{f(9 * k)}" fill="none"></path>'
             f'<path d="M{f(x)} {f(y - 140 * k)} L {f(x - 40 * k)} {f(y)} L {f(x)} {f(y + 140 * k)}" stroke="#E8E2D6" stroke-width="2"></path>')
    o.append(f'<path d="M{f(x - 40 * k)} {f(y)} L {f(x + 60 * k)} {f(y - 10 * k)} L {f(x + 40 * k)} {f(y + 6 * k)} L {f(w * 0.96)} {f(y - 40 * k)}" stroke="#FFF4C2" stroke-width="{f(6 * k)}" fill="none" stroke-linejoin="bevel"></path>'
             + halo(w * 0.9, y - 40 * k, 40 * k, "#FFF4C2", 0.6))
    o.append(wind_lines(w, h, seed, n=8, color="#CFE0FF", op=0.4, y0=0.6, y1=0.95))
    return "".join(o)

def crown_stones(w, h, seed):
    """They shall be as the stones of a crown, lifted on high over his land; grain shall make the young men flourish, and new
    wine the virgins: a crown of bright stones over a land of grain and vines."""
    import samuel2 as S2
    o = [sky(w, h, "#3A5A9A", "#FFE6A0"), hills(w, h, h * 0.6, seed, color="#8A9A5A", amp=12), ground(w, h, h * 0.66, "#C8B060", dy=0),
         grain(-10, w * 0.5, h * 0.98, h * 0.2, seed), vines(w * 0.54, w * 0.98, h * 0.82, h * 0.94, seed, rows=2), halo(w * 0.5, h * 0.26, h * 0.2, "#FFF4C2", 0.6)]
    k = min(1.6, h / 200)
    o.append(S2.crown(w * 0.5, h * 0.34, k))
    r = random.Random(seed)
    for i in range(5):
        o.append(f'<circle cx="{f(w * 0.5 + (i - 2) * 16 * k)}" cy="{f(h * 0.34 - 24 * k)}" r="{f(4 * k)}" fill="{["#C8202A", "#1F5FAD", "#2E9A4A", "#E8C840", "#8A4AC8"][i]}" stroke="#0D0D0F" stroke-width="1"></circle>')
    return "".join(o)

def latter_rain(w, h, seed):
    """Ask ye of Jehovah rain in the time of the latter rain; he will give showers of rain, to every one grass in the field:
    rain falling from dark clouds onto green fields, lightning far off (God is not drawn)."""
    o = [sky(w, h, "#3A4A6A", "#8AA8C8"), clouds(w, h * 0.12, seed, n=8, color="#4A5A7A", op=0.95, h=h), bolt(w * 0.8, h * 0.1, h * 0.4, seed),
         hills(w, h, h * 0.6, seed, color="#4A7A4A", amp=12), ground(w, h, h * 0.66, "#6AA84A", dy=0), rain(w, h, seed, n=80, color="#CFE0FF", op=0.6)]
    r = random.Random(seed)
    for i in range(40):
        x, y = r.uniform(0, w), r.uniform(h * 0.7, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -3 -12 M{f(x)} {f(y)} l 3 -10" stroke="#2E6B3A" stroke-width="2"></path>')
    return "".join(o)

def no_shepherd(w, h, seed, scatter=True):
    """They go their way like sheep, they are afflicted, because there is no shepherd: sheep wandering on the bare hills,
    a teraphim fallen in the dust."""
    o = [vista(w, h, seed, tone="grey", hills_n=2, horizon=0.5)]
    r = random.Random(seed)
    for i in range(8):
        o.append(E.sheep(w * r.uniform(0.05, 0.95), h * r.uniform(0.6, 0.96), min(0.5, h / 560) * r.uniform(0.8, 1.1), flip=r.random() < 0.5))
    if scatter:
        o.append(f'<g transform="rotate(80 {f(w * 0.16)} {f(h * 0.92)})"><path d="M{f(w * 0.16 - 8)} {f(h * 0.92)} L {f(w * 0.16 - 10)} {f(h * 0.92 - 40)} L {f(w * 0.16 + 10)} {f(h * 0.92 - 40)} L {f(w * 0.16 + 8)} {f(h * 0.92)} Z" fill="#A8603A" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<circle cx="{f(w * 0.16)}" cy="{f(h * 0.92 - 48)}" r="8" fill="#A8603A" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')
    return "".join(o)

def cornerstone(w, h, seed):
    """From him shall come forth the corner-stone, from him the nail, from him the battle bow, from him every ruler: four
    cells, a corner-stone, a tent nail, a bow, a sceptre."""
    cw = w / 4; o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>']
    k = min(1.0, h / 220)
    for i, name in enumerate(("THE CORNER-STONE", "THE NAIL", "THE BATTLE BOW", "EVERY RULER")):
        x0 = i * cw; cx, cy = x0 + cw / 2, h * 0.62
        o.append(f'<rect x="{f(x0 + 8)}" y="{f(h * 0.12)}" width="{f(cw - 16)}" height="{f(h * 0.76)}" fill="#1A1A4A" stroke="{GOLD}" stroke-width="1.6"></rect>' + label(cx, h * 0.22, name, GOLD, 9))
        if i == 0: o.append(f'<path d="M{f(cx - 40 * k)} {f(cy + 30 * k)} L {f(cx - 40 * k)} {f(cy - 20 * k)} L {f(cx + 10 * k)} {f(cy - 40 * k)} L {f(cx + 40 * k)} {f(cy - 20 * k)} L {f(cx + 40 * k)} {f(cy + 30 * k)} Z" fill="#D8CDB8" stroke="#0D0D0F" stroke-width="2"></path>')
        if i == 1: o.append(f'<path d="M{f(cx - 6 * k)} {f(cy - 50 * k)} L {f(cx + 6 * k)} {f(cy - 50 * k)} L {f(cx + 4 * k)} {f(cy + 30 * k)} L {f(cx)} {f(cy + 44 * k)} L {f(cx - 4 * k)} {f(cy + 30 * k)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>')
        if i == 2: o.append(f'<path d="M{f(cx - 10 * k)} {f(cy - 60 * k)} C {f(cx + 40 * k)} {f(cy - 30 * k)} {f(cx + 40 * k)} {f(cy + 30 * k)} {f(cx - 10 * k)} {f(cy + 60 * k)}" stroke="#C8A060" stroke-width="{f(6 * k)}" fill="none"></path><path d="M{f(cx - 10 * k)} {f(cy - 60 * k)} L {f(cx - 10 * k)} {f(cy + 60 * k)}" stroke="#E8E2D6" stroke-width="1.6"></path>')
        if i == 3: o.append(f'<path d="M{f(cx)} {f(cy + 50 * k)} L {f(cx)} {f(cy - 40 * k)}" stroke="#E8B830" stroke-width="{f(6 * k)}"></path><circle cx="{f(cx)}" cy="{f(cy - 46 * k)}" r="{f(10 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>')
    return "".join(o)

def gather_map(w, h):
    """I will hiss for them, and gather them; I will bring them again out of the land of Egypt, and gather them out of
    Assyria, into the land of Gilead and Lebanon: arrows from Egypt and Assyria converging on the land."""
    o = [grid_bg(w, h)]
    pts = {"EGYPT": (0.14, 0.86), "ASSYRIA": (0.88, 0.16), "GILEAD": (0.56, 0.48), "LEBANON": (0.46, 0.22), "JUDAH": (0.42, 0.6)}
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.7)} C {f(w * 0.1)} {f(h * 0.8)} {f(w * 0.12)} {f(h * 0.9)} {f(w * 0.1)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>' + label(w * 0.04, h * 0.66, "NILE", CY, 8, anchor="start"))
    o.append(route([(w * 0.16, h * 0.82), (w * 0.4, h * 0.62)], color=GOLD) + route([(w * 0.86, h * 0.2), (w * 0.58, h * 0.46)], color=GOLD))
    for name, (x, y) in pts.items(): o.append(node(w * x, h * y, name, color=GOLD if name in ("GILEAD", "LEBANON", "JUDAH") else "#FF8A6A", r=5))
    return "".join(o)

def lebanon_fire(w, h, seed):
    """Open thy doors, O Lebanon, that the fire may devour thy cedars; wail, O fir-tree, for the cedar is fallen: the
    mountain forest burning, the oaks of Bashan bowed, the shepherds' voice wailing."""
    o = [sky(w, h, "#2A0A0A", "#C8502A"), f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.3)} {f(h * 0.2)} L {f(w * 0.56)} {f(h * 0.42)} L {f(w * 0.8)} {f(h * 0.16)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2"></path>']
    r = random.Random(seed)
    for i in range(12):
        x, y = w * r.uniform(0.05, 0.95), h * r.uniform(0.45, 0.9)
        o.append(tree(x, y, min(0.5, h / 600), color="#1E3A22", kind="tall", seed=seed + i))
    o.append(fires(-10, w + 10, h * 0.8, h * 0.4, seed, n=6) + smokes([w * 0.2, w * 0.5, w * 0.8], h * 0.4, seed, k=max(0.6, h / 300), color="#2A1A1E"))
    return "".join(o)

def staves(p, w, h, seed, broken=0):
    """So I fed the flock of slaughter; and I took unto me two staves, the one I called Beauty, and the other Bands: a
    shepherd (Zechariah) with the flock, the two staves planted beside him (broken=1: Beauty cut asunder; broken=2: Bands
    also)."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#8A7A8A", "#E8D0B0"), hills(w, h, h * 0.52, seed, color="#8A8A6A", amp=12), ground(w, h, h * 0.58, "#A8A070", dy=0)]
    s = fit(b, h * 0.36)
    o.append(zech_fig(p, w * 0.2, b, s))
    for i, (name, c) in enumerate((("BEAUTY", "#E8B830"), ("BANDS", "#B5652E"))):
        x = w * (0.36 + i * 0.12); top = b - 200 * s
        if broken > i:
            o.append(f'<path d="M{f(x)} {f(b)} L {f(x + 4 * s)} {f(b - 90 * s)}" stroke="{c}" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>'
                     f'<path d="M{f(x + 14 * s)} {f(b - 2)} L {f(x + 90 * s)} {f(b - 30 * s)}" stroke="{c}" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>')
            o.append(label(x, b - 110 * s, name, c, 10))
        else:
            o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(top)}" stroke="{c}" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>'
                     f'<path d="M{f(x)} {f(top)} C {f(x)} {f(top - 20 * s)} {f(x + 20 * s)} {f(top - 24 * s)} {f(x + 22 * s)} {f(top - 8 * s)}" stroke="{c}" stroke-width="{f(7 * s)}" fill="none" stroke-linecap="round"></path>')
            o.append(label(x, top - 34 * s, name, c, 10))
    o.append(sheep_row(w * 0.62, w * 0.98, h * 0.94, 4, seed, s=min(0.5, h / 600)))
    return "".join(o)

def slaughter_flock(w, h, seed):
    """The flock of slaughter, whose possessors slay them and hold themselves not guilty; I will no more pity the inhabitants
    of the land: an empty fold under a grey sky, the gate open, a few sheep straying (no slaughter drawn)."""
    o = [sky(w, h, "#4A4A5A", "#B8A8A0"), hills(w, h, h * 0.5, seed, color="#6A6A5A", amp=14), ground(w, h, h * 0.56, "#8A8060", dy=0)]
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.94)} L {f(w * 0.1)} {f(h * 0.66)} L {f(w * 0.6)} {f(h * 0.66)} L {f(w * 0.6)} {f(h * 0.8)}" stroke="#7A6A5A" stroke-width="{f(h * 0.04)}" fill="none"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.8)} L {f(w * 0.7)} {f(h * 0.88)}" stroke="#6A4A2A" stroke-width="6"></path>')
    o.append(sheep_row(w * 0.66, w * 0.98, h * 0.96, 3, seed, s=min(0.5, h / 560)))
    return "".join(o)

def thirty(w, h, seed):
    """So they weighed for my hire thirty pieces of silver: the scale and the thirty pieces counted out on a cloth."""
    from ecc.art import scales
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2420"></rect>', halo(w * 0.5, h * 0.5, h * 0.6, "#FFC14D", 0.3),
         f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.0, h / 300)
    o.append(scales(w * 0.24, h * 0.78, k, tilt=-6))
    for i in range(30):
        x = w * (0.46 + (i % 10) * 0.05); y = h * (0.84 + (i // 10) * 0.05)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(10 * k)}" ry="{f(4 * k)}" fill="#E8E2D6" stroke="#5A5A6A" stroke-width="1.2"></ellipse>')
    return "".join(o)

def potter_cast(w, h, seed):
    """Cast it unto the potter, the goodly price that I was prized at by them: the pieces of silver falling onto the floor of
    the potter's workshop in the house of Jehovah, his wheel and jars."""
    from job.art3 import potter
    o = [potter(w, h, seed)]
    r = random.Random(seed)
    for i in range(14):
        x, y = w * r.uniform(0.1, 0.9), h * r.uniform(0.1, 0.8)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="8" ry="3.4" fill="#E8E2D6" stroke="#5A5A6A" stroke-width="1.2" transform="rotate({r.randint(-60, 60)} {f(x)} {f(y)})"></ellipse>')
    o.append(mk.speed(w * 0.5, h * 0.3, 10, 10, h * 0.4, seed, color="#E8E2D6", op=0.4))
    return "".join(o)

def foolish_shepherd(w, h, seed):
    """Take unto thee yet again the instruments of a foolish shepherd; woe to the worthless shepherd that leaveth the flock:
    a shepherd's bag, staff and sling thrown down on a bare hill, the flock scattered far off."""
    o = [vista(w, h, seed, tone="dusk", hills_n=2, horizon=0.5)]
    r = random.Random(seed)
    for i in range(6):
        o.append(E.sheep(w * r.uniform(0.5, 0.98), h * r.uniform(0.56, 0.7), min(0.3, h / 900), flip=r.random() < 0.5))
    k = min(1.0, h / 280)
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.94)} L {f(w * 0.44)} {f(h * 0.88)}" stroke="#6A4A2A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.44)} {f(h * 0.88)} C {f(w * 0.46)} {f(h * 0.84)} {f(w * 0.5)} {f(h * 0.84)} {f(w * 0.5)} {f(h * 0.88)}" stroke="#6A4A2A" stroke-width="{f(6 * k)}" fill="none"></path>'
             f'<path d="M{f(w * 0.24)} {f(h * 0.98)} C {f(w * 0.22)} {f(h * 0.9)} {f(w * 0.34)} {f(h * 0.88)} {f(w * 0.36)} {f(h * 0.98)} Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)
