"""Drawings for Job 8–10 (Bildad's first speech and Job's answer), and debate(): a friend speaking to Job on the ash heap."""
from job.art2 import *
from job.art2 import f, K2, K3, sea
from genesis.art3 import label
import exo.art6 as A6

def debate(p, w, h, seed, who="bil", speaker=None, night=False):
    """Job on the ash heap and one of his friends standing before him, his hand stretched out as he speaks; speaker='job':
    Job sitting up, his hand raised toward heaven, the friend listening. The other two sit apart."""
    b = h * 0.97
    sk = (K2.sky(w, h, "#1A1A3A", "#5A4A6A") + mk.stars(30, w, h * 0.5, seed)) if night else K2.sky(w, h, "#7A7A8A", "#E8D8B8")
    o = [mk.defs(p, *ALL), sk, J.city_hill(w * 0.86, h * 0.72, w * 0.26, h * 0.12, seed), ground(w, h, h * 0.74, "#8A7A62" if not night else "#4A4248", dy=0),
         ash_mound(w * 0.34, b, w * 0.46, h * 0.1, seed)]
    s = min(1.0, (h * 0.22) / 140)
    o.append(seated(w * 0.32, b - h * 0.08, s, SACK, head=SACK, shard=speaker != "job", ash=True))
    if speaker == "job":
        o.append(f'<path d="M{f(w * 0.32 - 8 * s)} {f(b - h * 0.08 - 90 * s)} L {f(w * 0.32 + 20 * s)} {f(b - h * 0.08 - 130 * s)} L {f(w * 0.32 + 30 * s)} {f(b - h * 0.08 - 166 * s)}" '
                 f'stroke="#0D0D0F" stroke-width="{f(13 * s)}" fill="none" stroke-linecap="round"></path><path d="M{f(w * 0.32 - 8 * s)} {f(b - h * 0.08 - 90 * s)} L {f(w * 0.32 + 20 * s)} {f(b - h * 0.08 - 130 * s)} L {f(w * 0.32 + 30 * s)} {f(b - h * 0.08 - 166 * s)}" '
                 f'stroke="{SACK}" stroke-width="{f(9.5 * s)}" fill="none" stroke-linecap="round"></path>')
    fs = fit(b, max(h * 0.7, b - 220))
    up = [(-22, -158), (-50, -150), (-74, -162)] if speaker != "job" else None
    o.append(friend_fig(p, w * 0.62, b, fs, who, flip=True, up=up))
    rest = [x for x in ("eli", "bil", "zop") if x != who]
    o.append(seated_friend(w * 0.82, b, s * 0.85, rest[0], flip=True) + seated_friend(w * 0.94, b - 4, s * 0.8, rest[1], flip=True))
    return "".join(o)

def old_stones(w, h, seed):
    """Inquire of the former age; our days upon earth are a shadow: ancient standing stones of the fathers on a ridge at
    evening, their long shadows reaching across the ground."""
    o = [K2.sky(w, h, "#4A3A6A", "#F3A86A"), sun(w * 0.9, h * 0.76, min(24, h * 0.06), color="#FF8A3D", op=0.3), ground(w, h, h * 0.8, "#A8805A", dy=0)]
    for i, (x, hh) in enumerate(((0.16, 0.2), (0.28, 0.26), (0.4, 0.18), (0.52, 0.24), (0.64, 0.16))):
        bx = w * x; top = h * (0.84 - hh)
        o.append(f'<path d="M{f(bx - 14)} {f(h * 0.84)} L {f(bx - 140)} {f(h * 0.98)} L {f(bx - 110)} {f(h * 0.99)} L {f(bx + 14)} {f(h * 0.84)} Z" fill="#3A2A2A" opacity="0.45"></path>')
        o.append(P(f"M{f(bx - 16)} {f(h * 0.85)} L {f(bx - 12)} {f(top + 8)} Q {f(bx)} {f(top - 4)} {f(bx + 12)} {f(top + 8)} L {f(bx + 16)} {f(h * 0.85)} Z", "#8A7A6A"))
    return "".join(o)

def papyrus(w, h, seed, withered=False):
    """Can the rush grow up without mire? can the flag grow without water?: papyrus and flags standing green in the mire of
    a pool; withered=True: the pool dried, the rushes brown and bent."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2" if not withered else "#E8C890", "#E8F0D8" if not withered else "#F3E0B0"), ground(w, h, h * 0.8, "#6A5A3A" if not withered else "#C8A06A", dy=0)]
    if not withered: o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.9)}" rx="{f(w * 0.44)}" ry="{f(h * 0.07)}" fill="#3A6A6A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for i in range(30):
        x = w * (0.08 + r.random() * 0.84); top = h * r.uniform(0.6, 0.74); lean = r.uniform(-12, 12) + (30 if withered and i % 2 else 0)
        c = "#2E6B3A" if not withered else "#8A6A3A"
        o.append(f'<path d="M{f(x)} {f(h * 0.92)} Q {f(x + lean * 0.3)} {f((top + h * 0.92) / 2)} {f(x + lean)} {f(top)}" stroke="{c}" stroke-width="3" fill="none"></path>')
        if i % 3 == 0:
            o.append(f'<path d="M{f(x + lean)} {f(top)} l -12 -10 M{f(x + lean)} {f(top)} l 0 -14 M{f(x + lean)} {f(top)} l 12 -10 M{f(x + lean)} {f(top)} l -7 -13 M{f(x + lean)} {f(top)} l 7 -13" stroke="{"#5A8A3A" if not withered else "#A8804A"}" stroke-width="2"></path>')
    return "".join(o)

def spider_web(w, h, seed):
    """Whose trust is a spider's web: a web strung between dry stalks, torn on one side, against a low sun."""
    o = [K2.sky(w, h, "#5A4A6A", "#E8B88A"), sun(w * 0.3, h * 0.78, min(26, h * 0.07), color="#FFB04A", op=0.3), ground(w, h, h * 0.94, "#6A5A3A", dy=0)]
    cx, cy, R = w * 0.62, h * 0.8, min(h * 0.2, w * 0.18)
    o.append(f'<path d="M{f(cx - R * 1.4)} {f(h)} L {f(cx - R * 1.2)} {f(cy - R * 1.3)} M{f(cx + R * 1.4)} {f(h)} L {f(cx + R * 1.2)} {f(cy - R * 1.2)}" stroke="#5A4A2A" stroke-width="4"></path>')
    spokes = 12
    for i in range(spokes):
        a = 2 * math.pi * i / spokes
        if 1 <= i <= 3: continue
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(cx + math.cos(a) * R)} {f(cy + math.sin(a) * R)}" stroke="#F3EFE6" stroke-width="1.2" opacity="0.85"></path>')
    for k in range(1, 7):
        rr = R * k / 6
        pts = [(cx + math.cos(2 * math.pi * i / spokes) * rr, cy + math.sin(2 * math.pi * i / spokes) * rr) for i in range(spokes) if not 1 <= i <= 3]
        o.append('<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + '" fill="none" stroke="#F3EFE6" stroke-width="1" opacity="0.8"></path>')
    o.append(f'<circle cx="{f(cx + 6)}" cy="{f(cy + 4)}" r="4" fill="#1A1210"></circle>')
    return "".join(o)

def shoots(w, h, seed):
    """He is green before the sun, and his shoots go forth over his garden; his roots are wrapped about the stone-heap: a
    green vine spreading over a heap of stones in full sun."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#F3F0D0"), sun(w * 0.86, h * 0.2, min(24, h * 0.06), op=0.35), ground(w, h, h * 0.84, "#B89A6A", dy=0),
         S4.stone_heap(w * 0.44, h * 0.98, w * 0.4, h * 0.16, seed)]
    for i in range(7):
        x0 = w * 0.44 + r.uniform(-0.15, 0.15) * w; y0 = h * 0.86
        pts = [(x0, y0)]
        for k in range(5): pts.append((pts[-1][0] + r.uniform(-40, 40), pts[-1][1] + r.uniform(-14, 10)))
        o.append('<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + '" fill="none" stroke="#2E6B3A" stroke-width="3"></path>')
        for x, y in pts[1:]: o.append(f'<ellipse cx="{f(x)}" cy="{f(y - 4)}" rx="7" ry="4" fill="#5A9A3A" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    return "".join(o)

def quake(w, h, seed):
    """Him that removeth the mountains, that shaketh the earth out of its place, and the pillars thereof tremble: mountains
    tilting and breaking, rocks falling, the ground split."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A2A3A", "#C8805A")]
    for i in range(4):
        x = w * (0.1 + i * 0.26); hh = h * r.uniform(0.2, 0.3)
        o.append(f'<g transform="rotate({r.choice([-8, 6, -5, 9])} {f(x)} {f(h * 0.82)})">' + P(f"M{f(x - w * 0.16)} {f(h * 0.84)} L {f(x - w * 0.02)} {f(h * 0.82 - hh)} L {f(x + 10)} {f(h * 0.84 - hh * 0.8)} L {f(x + w * 0.16)} {f(h * 0.84)} Z", ["#6A4A3A", "#7A5A4A", "#5A3A3A", "#8A6A4A"][i]) + '</g>')
    o.append(ground(w, h, h * 0.84, "#4A3A2A", dy=0))
    o.append(P(f"M{f(w * 0.3)} {f(h * 0.84)} L {f(w * 0.36)} {f(h * 0.9)} L {f(w * 0.32)} {f(h * 0.94)} L {f(w * 0.4)} {f(h + 10)} L {f(w * 0.46)} {f(h + 10)} L {f(w * 0.4)} {f(h * 0.94)} L {f(w * 0.44)} {f(h * 0.9)} L {f(w * 0.38)} {f(h * 0.84)} Z", "#1A1210", 2))
    for i in range(14):
        x = r.uniform(0, w); y = r.uniform(h * 0.5, h * 0.8)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(3, 8))}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    o.append(mk.speed(w * 0.5, h * 0.7, 18, w * 0.3, w * 0.7, seed, color="#F3D8B0", op=0.3))
    return "".join(o)

STARS_BEAR = [(0.06, 0.3), (0.13, 0.26), (0.2, 0.28), (0.26, 0.32), (0.27, 0.42), (0.36, 0.44), (0.35, 0.34)]
STARS_ORION = [(0.47, 0.22), (0.58, 0.24), (0.5, 0.36), (0.525, 0.37), (0.55, 0.38), (0.46, 0.52), (0.6, 0.5)]
STARS_PLEIADES = [(0.78, 0.3), (0.8, 0.28), (0.81, 0.31), (0.83, 0.29), (0.79, 0.33), (0.82, 0.34), (0.845, 0.32)]
def constellations(w, h, seed, names=True, top=0.48):
    """That maketh the Bear, Orion, and the Pleiades, and the chambers of the south: the night sky over the hills with the
    three asterisms drawn and named in technical labels."""
    o = [K2.sky(w, h, "#05051A", "#1E1650"), mk.stars(160, w, h, seed, color="#C8C8E8")]
    sy = lambda y: h * (top + 0.65 * y)
    for pts, nm, lines in ((STARS_BEAR, "THE BEAR", [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 3)]),
                           (STARS_ORION, "ORION", [(0, 2), (1, 4), (2, 3), (3, 4), (2, 5), (4, 6)]), (STARS_PLEIADES, "THE PLEIADES", [])):
        for a, b in lines:
            o.append(f'<path d="M{f(w * pts[a][0])} {f(sy(pts[a][1]))} L {f(w * pts[b][0])} {f(sy(pts[b][1]))}" stroke="#8FD0E2" stroke-width="1.2" opacity="0.6" stroke-dasharray="4 4"></path>')
        for x, y in pts: o.append(f'<circle cx="{f(w * x)}" cy="{f(sy(y))}" r="{2.6 if lines else 2}" fill="#FFF4C2"></circle><circle cx="{f(w * x)}" cy="{f(sy(y))}" r="7" fill="#FFF4C2" opacity="0.2"></circle>')
        if names:
            mx = sum(x for x, _ in pts) / len(pts); my = max(y for _, y in pts)
            o.append(label(w * mx, sy(my) + 20, nm, "#8FD0E2", 10))
    o.append(hills(w, h, h * 0.94, seed, "#0B0B1A", amp=6, step=80))
    return "".join(o)

def unseen(w, h, seed):
    """Lo, he goeth by me, and I see him not: a whirl of dust passing over the empty desert, the grasses bending, no one there."""
    o = [K2.sky(w, h, "#C8B890", "#F3E0B0"), hills(w, h, h * 0.76, seed, "#B8986A", amp=8, step=90), ground(w, h, h * 0.84, "#D8B87A", dy=0),
         whirl(w * 0.6, h * 0.6, h * 0.92, w * 0.12, w * 0.02, seed, color="#A8885A", op=0.5, n=10)]
    r = random.Random(seed)
    for i in range(30):
        x = r.uniform(0, w); y = r.uniform(h * 0.86, h)
        o.append(f'<path d="M{f(x)} {f(y)} q 6 -10 16 -14" stroke="#8A7A3A" stroke-width="2" fill="none"></path>')
    return "".join(o)

def swift(w, h, seed):
    """Swifter than a post; passed away as the swift ships; as the eagle that swoopeth on the prey: reed ships running before
    the wind on a river, and an eagle stooping out of the sky."""
    o = [K2.sky(w, h, "#5A8AB8", "#E8F0E0"), f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#2C7DA0"></rect>']
    for i in range(3):
        x = w * (0.12 + i * 0.2); y = h * 0.86
        o.append(K1.ship(x, y, min(0.6, h / 600), sail="#E8E2D6") + "".join(f'<path d="M{f(x - 50 - k * 10)} {f(y - 8 - k * 8)} L {f(x - 110 - k * 10)} {f(y - 8 - k * 8)}" stroke="#FFFFFF" stroke-width="2" opacity="0.7"></path>' for k in range(3)))
    o.append(A6.eagle(w * 0.8, h * 0.72, min(1.6, h / 240), flip=True) + "".join(f'<path d="M{f(w * 0.8 + 30 + i * 12)} {f(h * 0.62 - i * 16)} L {f(w * 0.8 + 70 + i * 14)} {f(h * 0.5 - i * 18)}" stroke="#FFFFFF" stroke-width="2" opacity="0.7"></path>' for i in range(4)))
    return "".join(o)

def snow_wash(w, h, seed):
    """If I wash myself with snow water, and make my hands never so clean, yet wilt thou plunge me in the ditch: a basin of
    snow water on the rim of a muddy ditch, the snow on the hills behind."""
    o = [K2.sky(w, h, "#8A9AB8", "#D8E0E8"), hills(w, h, h * 0.72, seed, "#E8EEF4", amp=10, step=80), ground(w, h, h * 0.8, "#8A7A62", dy=0),
         P(f"M{f(w * 0.5)} {f(h * 0.86)} C {f(w * 0.56)} {f(h * 1.02)} {f(w * 0.9)} {f(h * 1.02)} {f(w * 0.96)} {f(h * 0.86)} Z", "#3A2A1A"),
         f'<ellipse cx="{f(w * 0.73)}" cy="{f(h * 0.9)}" rx="{f(w * 0.18)}" ry="{f(h * 0.03)}" fill="#5A4A2A"></ellipse>']
    k = min(1.4, h / 260); x, y = w * 0.24, h * 0.94
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-46 -30 C -40 0 40 0 46 -30 Z", "#B5652E") + '<ellipse cx="0" cy="-30" rx="46" ry="8" fill="#DCEFF8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             + '<g fill="#FFFFFF" stroke="#8FB8D8" stroke-width="0.8"><circle cx="-14" cy="-32" r="4"></circle><circle cx="10" cy="-29" r="3"></circle><circle cx="22" cy="-33" r="3.4"></circle></g></g>')
    return "".join(o)

def umpire(w, h, seed):
    """There is no umpire betwixt us, that might lay his hand upon us both: the place of judgment in the gate, two seats set
    over against each other, the umpire's seat between them empty, a rod laid across it."""
    o = [K2.sky(w, h, "#5A5A7A", "#D8C8B0"), P(f"M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.86)} L -10 {f(h * 0.86)} Z", "#A8906A"),
         P(f"M{f(w * 0.7)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.86)} L {f(w * 0.7)} {f(h * 0.86)} Z", "#A8906A"),
         ground(w, h, h * 0.86, "#C8B088", dy=0)]
    def seat(x, y, k, hi=False):
        return (f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-30 0 L -30 -40 L 30 -40 L 30 0 Z", "#8A5A30") + P("M-30 -40 L -30 -90 L -20 -90 L -20 -40 Z", "#8A5A30")
                + (P("M-40 -40 L 40 -40 L 40 -50 L -40 -50 Z", "#E8B830") if hi else "") + '</g>')
    k = min(1.4, h / 280)
    o.append(seat(w * 0.2, h * 0.96, k) + seat(w * 0.8, h * 0.96, k).replace(f"scale({f(k)})", f"scale({f(-k)} {f(k)})") + seat(w * 0.5, h * 0.92, k * 1.1, hi=True))
    o.append(f'<path d="M{f(w * 0.42)} {f(h * 0.92 - 56 * k)} L {f(w * 0.6)} {f(h * 0.92 - 48 * k)}" stroke="#5A3A1E" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def potter(w, h, seed):
    """Thou hast fashioned me as clay; hast thou not poured me out as milk, and curdled me like cheese?: a potter's wheel
    with a vessel of wet clay upon it, and beside it a jar of milk and a round of white cheese."""
    o = [rect(w, h, "#5A3A2A"), f'<circle cx="{f(w * 0.4)}" cy="{f(h * 0.7)}" r="{f(h * 0.3)}" fill="#FFC14D" opacity="0.15"></circle>', ground(w, h, h * 0.9, "#3A2418", dy=0)]
    k = min(1.4, h / 280); x, y = w * 0.36, h * 0.96
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-60 0 L 60 0 L 50 -20 L -50 -20 Z", "#6A4A2A") + '<path d="M0 -20 L 0 -50" stroke="#3A2214" stroke-width="8"></path>'
             + '<ellipse cx="0" cy="-52" rx="56" ry="9" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             + P("M-26 -56 C -36 -80 -30 -100 -14 -110 L -16 -124 L 16 -124 L 14 -110 C 30 -100 36 -80 26 -56 Z", "#B5652E")
             + '<path d="M-20 -80 C -6 -76 6 -76 20 -80 M-22 -94 C -6 -90 6 -90 22 -94" stroke="#8A3A1E" stroke-width="1.6" fill="none"></path></g>')
    x2 = w * 0.7
    o.append(f'<g transform="translate({f(x2)} {f(y)}) scale({f(k)})">' + P("M-22 0 C -30 -30 -26 -56 -12 -64 L -12 -76 L 12 -76 L 12 -64 C 26 -56 30 -30 22 0 Z", "#C8A878")
             + '<ellipse cx="0" cy="-76" rx="12" ry="4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></ellipse></g>'
             + f'<g transform="translate({f(w * 0.84)} {f(y)}) scale({f(k)})">' + P("M-30 0 L -30 -22 C -30 -32 30 -32 30 -22 L 30 0 Z", "#F3EAD0") + '<ellipse cx="0" cy="-22" rx="30" ry="8" fill="#FFF8E6" stroke="#0D0D0F" stroke-width="1.6"></ellipse></g>')
    return "".join(o)

def dark_land(w, h, seed):
    """The land of darkness and of the shadow of death, where the light is as midnight: hills black under a black sky, the
    faintest glimmer behind them."""
    o = [K2.sky(w, h, "#020206", "#0B0B1A"), f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.82)}" rx="{f(w * 0.5)}" ry="{f(h * 0.08)}" fill="#1E1E3A" opacity="0.7"></ellipse>',
         hills(w, h, h * 0.8, seed, "#000000", amp=16, step=60), hills(w, h, h * 0.9, seed + 1, "#05050A", amp=10, step=80)]
    return "".join(o)

def tempest(w, h, seed, sea_=False, rain=True):
    """He breaketh me with a tempest: black cloud low over the hills (or the sea), forks of lightning striking down to the
    ground, the rain driven slanting."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0B0B1A", "#3A3A5A")]
    o.append(sea(w, h, h * 0.8, seed, color="#1F3A5A", deep="#0B1A2A") if sea_ else hills(w, h, h * 0.8, seed, "#1A1A28", amp=12, step=70) + ground(w, h, h * 0.9, "#2A2A30", dy=0))
    if rain:
        for i in range(110):
            x = r.uniform(-40, w + 40); y = r.uniform(0, h)
            o.append(f'<path d="M{f(x)} {f(y)} l -10 22" stroke="#A8B8D8" stroke-width="1.3" opacity="0.5"></path>')
    for i in range(3):
        x = w * (0.2 + i * 0.3) + r.uniform(-30, 30); y = h * 0.5
        pts = [(x, y)]
        while pts[-1][1] < h * 0.86:
            pts.append((pts[-1][0] + r.uniform(-24, 24), pts[-1][1] + r.uniform(16, 30)))
        d = "M" + " L ".join(f"{f(a)} {f(b)}" for a, b in pts)
        o.append(f'<path d="{d}" stroke="#FFF4C2" stroke-width="7" fill="none" opacity="0.35"></path><path d="{d}" stroke="#FFFFFF" stroke-width="2.6" fill="none"></path>')
    o.append(clouds(w, h * 0.5, seed, 9, color="#14142A", op=0.92, ry=0.07, h=h))
    return "".join(o)
