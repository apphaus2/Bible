"""Drawings for the Jonah volume, on the minor prophets' kit (oba.minor): Joppa and the ship of Tarshish, the tempest, the
wares cast into the sea, the sleeper in the innermost part of the ship, the lots, the sea calmed; the great fish (a great
whale-like fish; Jonah inside only a dark shape), the deep with its weeds and the bars of the earth, the dry land; Nineveh,
that great city of three days' journey, in sackcloth; the king in ashes; the booth east of the city, the gourd, the worm,
the sultry east wind. God is never drawn: the tempest is wind and lightning, his word comes in the Voice box."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from job.art import seated
from kg1.art import bed

JONAH_C = "#1F5A7A"
SACK = "#6A5A48"

def jonah_fig(p, x, y, s, flip=False, up=None):
    """Jonah at a distance: a sea-blue tunic and headcloth, brown beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JONAH_C, kind="Tunic", sw=3, flip=flip, up=up, extra=A.headcloth(JONAH_C) + BLACK_BEARD.replace("#2A1A10", "#4A2A1A"))

def jonah_kneel(x, y, s, flip=False):
    """Jonah kneeling in prayer (exodus.kneel), sea-blue, his face and hand in skin."""
    return E.kneel(x, y, s, color=JONAH_C, skin="#C98E66", flip=flip)

def _smooth(pts):
    """A Catmull-Rom curve through pts as cubic segments (the path continues from pts[0])."""
    d = ""
    for i in range(len(pts) - 1):
        p0 = pts[max(0, i - 1)]; p1, p2 = pts[i], pts[i + 1]; p3 = pts[min(len(pts) - 1, i + 2)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C {f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return d

def great_fish(x, y, s=1.0, flip=False, mouth=0.0, window=False, rot=0, seed=1):
    """The great fish Jehovah prepared: a long dark-blue body, a pale ridged belly, barnacles, a broad forked tail; mouth 0..1
    opens the jaw (the gape dark red); window=True cuts a lit window into the belly with Jonah kneeling in prayer inside.
    (x, y) = the middle of the body; facing right unless flip; about 640 units long at s=1."""
    sx = -s if flip else s
    m = mouth
    lip = (262, 4 + 92 * m)
    under = [lip, (214, 34 + 76 * m), (130, 60 + 42 * m), (40, 72 + 20 * m), (-80, 74), (-200, 52), (-272, 12)]
    belly = [(lip[0] - 16, lip[1] - 6), (206, 18 + 70 * m), (126, 40 + 38 * m), (40, 50 + 18 * m), (-80, 52), (-200, 34), (-262, 6)]
    o = [f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(sx)} {f(s)})">']
    # the tail
    o.append('<path d="M-262 -6 C -296 -40 -318 -70 -360 -104 C -352 -70 -344 -36 -330 -2 C -344 34 -354 70 -366 102 C -322 72 -298 42 -262 14 Z" fill="#22344A" stroke="#0D0D0F" stroke-width="3"></path>'
             '<path d="M-300 -40 L -340 -84 M-302 34 L -346 80" stroke="#3E5670" stroke-width="2.4"></path>')
    if m > 0:                                               # the gape behind the jaws
        o.append(f'<path d="M274 -12 L 124 6 L {f(lip[0])} {f(lip[1])} C {f(lip[0] + 20)} {f(lip[1] * 0.6)} 290 0 274 -12 Z" fill="#4A0E18" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<path d="M150 8 C 190 {f(10 + 30 * m)} 226 {f(14 + 50 * m)} {f(lip[0] - 10)} {f(lip[1] - 8)}" stroke="#A84A5A" stroke-width="{f(6 + 8 * m)}" fill="none" stroke-linecap="round"></path>')
    # the body: back from the tail to the snout, the jaw line, the underside back to the tail
    jaw = f" L 124 6 L {f(lip[0])} {f(lip[1])}" if m > 0 else f" C 276 -2 270 4 {f(lip[0])} {f(lip[1])}"
    o.append(f'<path d="M-272 -12 C -200 -80 -40 -98 120 -82 C 204 -74 256 -48 276 -12{jaw}{_smooth(under)} Z" fill="#30475F" stroke="#0D0D0F" stroke-width="3"></path>')
    o.append(f'<path d="M-250 -30 C -150 -76 0 -86 120 -74 C 190 -66 236 -48 256 -26" stroke="#4E6A86" stroke-width="5" fill="none" opacity="0.7"></path>')
    # the pale belly with its ridges
    o.append(f'<path d="M{f(under[0][0])} {f(under[0][1])}{_smooth(under)} L {f(belly[-1][0])} {f(belly[-1][1])}{_smooth(belly[::-1])} Z" fill="#C8D4DA" stroke="#0D0D0F" stroke-width="2"></path>')
    for k in range(1, 6):
        a, b = under[k], belly[k]
        o.append(f'<path d="M{f(b[0])} {f(b[1])} L {f(a[0] - 6)} {f(a[1] - 2)}" stroke="#7A8A96" stroke-width="2"></path>')
    # barnacles, the eye, the fins
    r = random.Random(seed)
    for _ in range(9):
        bx, by = r.uniform(-180, 160), r.uniform(-74, -40)
        if window and ((bx + 50) / 112) ** 2 + ((by + 8) / 58) ** 2 < 1: continue
        o.append(f'<circle cx="{f(bx)}" cy="{f(by)}" r="{f(r.uniform(2.5, 5))}" fill="#9AA6A8" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append('<path d="M-70 -86 C -56 -112 -28 -118 -6 -88 Z" fill="#22344A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<ellipse cx="206" cy="-34" rx="11" ry="9" fill="#E8E2C8" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="209" cy="-34" r="5.5" fill="#0D0D0F"></circle><circle cx="211" cy="-36" r="1.8" fill="#FFF"></circle>'
             '<path d="M190 -48 C 200 -54 216 -54 224 -46" stroke="#0D0D0F" stroke-width="2.4" fill="none"></path>'
             '<path d="M150 -14 C 158 -4 158 8 152 16" stroke="#1A2838" stroke-width="2.4" fill="none"></path>'
             f'<path d="M60 {f(44 + 18 * m)} C 40 {f(80 + 18 * m)} 6 {f(104 + 16 * m)} -36 {f(112 + 14 * m)} C -18 {f(90 + 14 * m)} 4 {f(66 + 16 * m)} 20 {f(46 + 18 * m)} Z" fill="#22344A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if window:                                              # the belly cut open to show Jonah praying within
        o.append('<ellipse cx="-50" cy="-8" rx="104" ry="50" fill="#2A0E10" stroke="#0D0D0F" stroke-width="3"></ellipse>'
                 '<ellipse cx="-50" cy="-8" rx="96" ry="43" fill="#6A2A22"></ellipse>'
                 + halo(-50, -10, 70, "#FFC14D", 0.55) +
                 '<path d="M-144 12 C -100 24 0 24 44 10 C 30 30 -10 40 -50 40 C -90 40 -130 30 -144 12 Z" fill="#3A1410"></path>'
                 + "".join(f'<path d="M{-130 + i * 26} -38 C {-124 + i * 26} -28 {-124 + i * 26} -16 {-130 + i * 26} -8" stroke="#8A3A30" stroke-width="2.4" fill="none" opacity="0.7"></path>' for i in range(8))
                 + jonah_kneel(-56, 28, 0.5)
                 + '<ellipse cx="-50" cy="-8" rx="104" ry="50" fill="none" stroke="#0D0D0F" stroke-width="3" stroke-dasharray="14 6"></ellipse>')
    return "".join(o) + "</g>"

def tossed(x, y, s, rot, sail="#E8E2D6", crew=0, p=None, seed=1):
    """The ship heeling over at angle rot, with a few mariners on deck."""
    o = ship(0, 0, 1, sail=sail)
    if crew and p:
        r = random.Random(seed)
        for i in range(crew):
            o += man(p, -60 + i * 40, -22, 0.22, r.choice(["#6A4A3A", "#3A4A6A", "#7A3A3A", "#5A5A3A"]), flip=i % 2 == 1, up=[(22, -158), (40, -176), (58, -196)] if i % 2 else None)
    return f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})">{o}</g>'

def swell(w, h, y, seed, color="#0F3A52", foam="#CFEFFF", n=5, amp=0.12):
    """Great breaking waves across the panel."""
    r = random.Random(seed); o = []
    for k in range(n):
        yy = y + (h - y) * k / n; a = h * amp * r.uniform(0.6, 1.2)
        d = f"M-20 {f(yy)}"
        x = -20
        while x < w + 40:
            d += f" Q {f(x + 40)} {f(yy - a)} {f(x + 90)} {f(yy - a * 0.2)} Q {f(x + 110)} {f(yy + a * 0.3)} {f(x + 150)} {f(yy)}"; x += 150
        d += f" L {f(w + 20)} {f(h + 20)} L -20 {f(h + 20)} Z"
        o.append(f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2" opacity="{0.9 if k else 0.8}"></path>')
        x = r.uniform(0, 60)
        while x < w:
            o.append(f'<path d="M{f(x + 70)} {f(yy - a * 0.9)} q 14 -4 26 6" stroke="{foam}" stroke-width="3" fill="none"></path>'); x += 150
    return "".join(o)

def joppa(p, w, h, seed):
    """Jonah went down to Joppa and found a ship going to Tarshish: the harbour, the ship at the quay, Jonah at its side."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.42, seed, color="#A8906A", amp=16),
         walls(w * 0.02, w * 0.4, h * 0.5, h * 0.2, seed, towers=2), sea(w, h, h * 0.5, seed),
         f'<path d="M-10 {f(h * 0.74)} L {f(w * 0.46)} {f(h * 0.74)} L {f(w * 0.46)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.2"></path>',
         ship(w * 0.74, h * 0.8, min(1.3, h / 260), sail="#E8E2D6")]
    s = fit(b, h * 0.44)
    o.append(jonah_fig(p, w * 0.36, b, s, flip=False) + man(p, w * 0.2, b, s * 0.96, "#6A4A3A", flip=False, up=[(22, -158), (40, -150), (56, -140)]))
    return "".join(o)

def tempest(p, w, h, seed, crew=3, bolts_=2):
    """A great wind upon the sea and a mighty tempest: the ship like to be broken (God is not drawn: wind and lightning)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B1A", "#3A3A4E"), clouds(w, h * 0.1, seed, n=7, color="#1A1A28", op=0.9, h=h)]
    for i in range(bolts_): o.append(bolt(w * (0.2 + 0.55 * i), 0, h * 0.5, seed + i))
    o.append(wind_lines(w, h, seed, n=12, color="#CFE0FF", op=0.4, y0=0.05, y1=0.6))
    o.append(swell(w, h, h * 0.62, seed + 3, n=2))
    o.append(tossed(w * 0.5, h * 0.7, min(1.8, h / 170), -18, crew=crew, p=p, seed=seed))
    o.append(swell(w, h, h * 0.8, seed + 5, n=2, color="#0B2E42"))
    return "".join(o)

def wares(p, w, h, seed):
    """The mariners cast forth the wares into the sea: jars and bales falling from the heeling ship."""
    o = [tempest(p, w, h, seed, crew=4, bolts_=1)]
    r = random.Random(seed)
    k = min(1.4, h / 240)
    for i in range(5):
        x, y = w * (0.62 + i * 0.06), h * (0.5 + r.uniform(0, 0.2))
        o.append(f'<g transform="rotate({r.randint(-40, 40)} {f(x)} {f(y)})"><path d="M{f(x - 8 * k)} {f(y)} C {f(x - 12 * k)} {f(y - 20 * k)} {f(x + 12 * k)} {f(y - 20 * k)} {f(x + 8 * k)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def hold(p, w, h, seed):
    """Jonah gone down into the innermost parts of the ship, fast asleep: the dark hold, its ribs, a swinging lamp, the
    cargo jars, and Jonah lying on a heap of sacks and coiled rope."""
    from genesis.art4 import clay_lamp
    b = h * 0.94
    o = [mk.defs(p, "LieB", "LieA"), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A120C"></rect>']
    for i in range(9):
        x = w * (i + 0.5) / 9
        o.append(f'<path d="M{f(x)} -10 C {f(x - 14)} {f(h * 0.4)} {f(x - 14)} {f(h * 0.7)} {f(x + (x - w / 2) * 0.1)} {f(h + 10)}" stroke="#4A3220" stroke-width="12" fill="none"></path>'
                 f'<path d="M{f(x)} -10 C {f(x - 14)} {f(h * 0.4)} {f(x - 14)} {f(h * 0.7)} {f(x + (x - w / 2) * 0.1)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="1.4" fill="none"></path>')
    o.append(halo(w * 0.22, h * 0.3, h * 0.6, "#FFC14D", 0.4))
    o.append(f'<path d="M{f(w * 0.22)} 0 L {f(w * 0.23)} {f(h * 0.26)}" stroke="#0D0D0F" stroke-width="2"></path>' + clay_lamp(w * 0.23, h * 0.32, min(1.0, h / 300)))
    k = min(1.3, h / 200)
    for i in range(4):                                      # cargo jars against the hull
        x = w * (0.7 + i * 0.075)
        o.append(f'<path d="M{f(x - 14 * k)} {f(b)} C {f(x - 26 * k)} {f(b - 30 * k)} {f(x - 16 * k)} {f(b - 56 * k)} {f(x - 6 * k)} {f(b - 62 * k)} L {f(x - 6 * k)} {f(b - 72 * k)} L {f(x + 6 * k)} {f(b - 72 * k)} L {f(x + 6 * k)} {f(b - 62 * k)} C {f(x + 16 * k)} {f(b - 56 * k)} {f(x + 26 * k)} {f(b - 30 * k)} {f(x + 14 * k)} {f(b)} Z" fill="#9A5A2E" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2614" stroke="#0D0D0F" stroke-width="2"></rect>')
    sx0, sx1 = w * 0.18, w * 0.6                            # the heap of sacks
    for i in range(5):
        x = sx0 + (sx1 - sx0) * (i + 0.5) / 5
        o.append(f'<ellipse cx="{f(x)}" cy="{f(b - 14 * k)}" rx="{f((sx1 - sx0) / 8)}" ry="{f(16 * k)}" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(f'<ellipse cx="{f(w * 0.64)}" cy="{f(b - 8 * k)}" rx="{f(34 * k)}" ry="{f(10 * k)}" fill="none" stroke="#C8A878" stroke-width="{f(5 * k)}"></ellipse>'
             f'<ellipse cx="{f(w * 0.64)}" cy="{f(b - 14 * k)}" rx="{f(26 * k)}" ry="{f(8 * k)}" fill="none" stroke="#C8A878" stroke-width="{f(5 * k)}"></ellipse>')
    sl = k * 0.95
    o.append(f'<g transform="translate({f(w * 0.56)} {f(b - 26 * k)}) scale({f(sl)})" fill="{JONAH_C}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    o.append(label(w * 0.34, b - 70 * k, "Z z z", "#FFE6A0", 14))
    return "".join(o)

def lots(w, h, seed):
    """They cast lots, and the lot fell upon Jonah: the potsherds thrown on the wet deck, one lit."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>']
    for i in range(12):
        o.append(f'<path d="M-10 {f(h * i / 12)} L {f(w + 10)} {f(h * i / 12)}" stroke="#241810" stroke-width="3"></path>')
    o.append(rain(w, h, seed, n=40, op=0.3))
    k = min(1.4, h / 200)
    for i in range(9):
        x, y = w * r.uniform(0.12, 0.88), h * r.uniform(0.3, 0.85)
        lit = i == 4
        if lit: x, y = w * 0.5, h * 0.56; o.append(halo(x, y, 70 * k, "#FFD23F", 0.6))
        o.append(f'<path d="M{f(x - 16 * k)} {f(y)} L {f(x - 6 * k)} {f(y - 12 * k)} L {f(x + 14 * k)} {f(y - 8 * k)} L {f(x + 12 * k)} {f(y + 8 * k)} L {f(x - 8 * k)} {f(y + 10 * k)} Z" '
                 f'fill="{"#FFD23F" if lit else "#B5652E"}" stroke="#0D0D0F" stroke-width="1.8" transform="rotate({r.randint(-40, 40)} {f(x)} {f(y)})"></path>')
    o.append(label(w * 0.5, h * 0.56 + 40 * k, "THE LOT", "#FFD23F", 11))
    return "".join(o)

def cast_forth(w, h, seed, calm=True):
    """Cast forth into the sea, and the sea ceased from its raging: the ship on a stilled sea, the ring of the splash."""
    o = [sky(w, h, "#5A6A8A", "#E8D8C8") if calm else sky(w, h, "#1A1A2A", "#4A4A5E"), clouds(w, h * 0.16, seed, n=5, color="#8A8AA0", op=0.6, h=h),
         sea(w, h, h * 0.56, seed, rough=not calm), ship(w * 0.62, h * 0.66, min(1.3, h / 260))]
    x, y = w * 0.3, h * 0.78
    for k in (1, 1.8, 2.6):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(26 * k)}" ry="{f(7 * k)}" fill="none" stroke="#E8F6FA" stroke-width="2.4" opacity="{1.2 - k * 0.35:.2f}"></ellipse>')
    return "".join(o)

def vows(p, w, h, seed):
    """The men feared Jehovah exceedingly, and offered a sacrifice, and made vows: the smoke of the offering rising from the
    ship on the calm sea at evening."""
    o = [sky(w, h, "#2A2A5A", "#FFB07A"), sea(w, h, h * 0.58, seed), ship(w * 0.5, h * 0.72, min(1.5, h / 230)),
         smoke(w * 0.42, h * 0.6, 9, seed, color="#E8E2D6", op=0.5, k=max(0.6, h / 300))]
    return "".join(o)

def _fs(w, h, k=0.84):
    """The scale at which the great fish (about 730 × 230 units) fills k of a w × h drawing."""
    return min(w * k / 730, h * k / 230)

def deep(w, h, seed, weeds=True, mountains=False, light=False):
    """The depth, in the heart of the seas: dark water, shafts of light from far above, bubbles, weeds (no fish)."""
    r = random.Random(seed)
    o = [hgrad(f"dp{seed}", [("0", "#1F5A7A"), ("0.5", "#0B2A44"), ("1", "#03101E")], vertical=True),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#dp{seed})"></rect>']
    for i in range(5):
        x = w * r.uniform(0.1, 0.9)
        o.append(f'<path d="M{f(x)} -10 L {f(x + w * 0.06)} -10 L {f(x + w * 0.16)} {f(h * 0.8)} L {f(x + w * 0.1)} {f(h * 0.8)} Z" fill="#8FD0E2" opacity="0.08"></path>')
    if light: o.append(halo(w * 0.5, -h * 0.05, h * 0.6, "#FFE680", 0.5))
    if mountains:
        o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.62)} L {f(w * 0.16)} {f(h * 0.4)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.52)} {f(h * 0.34)} L {f(w * 0.7)} {f(h * 0.66)} L {f(w * 0.86)} {f(h * 0.44)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#06121E" stroke="#1F4A6A" stroke-width="2"></path>')
    for i in range(14):
        x, y = r.uniform(0, w), r.uniform(0, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.5, 4))}" fill="none" stroke="#8FD0E2" stroke-width="1" opacity="0.5"></circle>')
    if weeds: o.append(weed_bed(w, h, seed))
    return "".join(o)

def weed_bed(w, h, seed, n=10, color="#2E6B3A"):
    r = random.Random(seed + 7); o = []
    for i in range(n):
        x = w * (i + 0.5) / n + r.uniform(-14, 14); hh = h * r.uniform(0.2, 0.4)
        o.append(f'<path d="M{f(x)} {f(h + 4)} C {f(x - 16)} {f(h - hh * 0.4)} {f(x + 16)} {f(h - hh * 0.7)} {f(x - 6)} {f(h - hh)}" stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def swallow(p, w, h, seed):
    """Jehovah prepared a great fish to swallow up Jonah: under the stilled sea, Jonah sinking from the bright surface, the
    great fish rising beneath him with its jaws open."""
    o = [mk.defs(p, *ALL), deep(w, h, seed, weeds=False)]
    o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#8FD0E2" opacity="0.5"></rect>'
             f'<path d="M-10 {f(h * 0.09)}' + "".join(f" q 20 -6 40 0" for _ in range(int(w / 40) + 2)) + '" stroke="#CFEFFF" stroke-width="2.4" fill="none"></path>')
    s = _fs(w, h, 0.86)
    fx, fy = w * 0.34, h * 0.64
    o.append(great_fish(fx, fy, s, mouth=1.0, rot=-16, seed=seed))
    jx, jy = fx + 316 * s, fy - 4 * s
    js = s * 0.62
    r = random.Random(seed)
    o.append(f'<g transform="rotate(-24 {f(jx)} {f(jy)})">{jonah_fig(p, jx, jy, js, up=[(22, -158), (40, -186), (52, -214)])}</g>')
    for i in range(10):
        bx, by = jx + r.uniform(-20, 30) * js, jy - (230 + i * 30) * js
        if by > 0: o.append(f'<circle cx="{f(bx)}" cy="{f(by)}" r="{f(r.uniform(2, 5))}" fill="none" stroke="#CFEFFF" stroke-width="1.4"></circle>')
    return "".join(o)

def belly(w, h, seed, light=False, rot=0, weeds=True, k=0.88):
    """In the belly of the fish: the great fish in the deep, its side cut away to show Jonah kneeling in prayer within."""
    s = _fs(w, h, k)
    return deep(w, h, seed, weeds=weeds, light=light) + great_fish(w * 0.5, h * 0.52, s, window=True, rot=rot, seed=seed)

def bars(w, h, seed):
    """I went down to the bottoms of the mountains; the earth with its bars closed upon me; the weeds were wrapped about my
    head: the roots of the mountains, the sea floor barred like a gate, the weeds streaming."""
    o = [deep(w, h, seed, mountains=True, weeds=False)]
    for i in range(11):
        x = w * (i + 0.5) / 11
        o.append(f'<path d="M{f(x)} {f(h * 0.5)} L {f(x)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="7"></path><path d="M{f(x)} {f(h * 0.5)} L {f(x)} {f(h + 10)}" stroke="#3A4A5A" stroke-width="3"></path>')
    o.append(f'<path d="M-10 {f(h * 0.56)} L {f(w + 10)} {f(h * 0.56)} M-10 {f(h * 0.84)} L {f(w + 10)} {f(h * 0.84)}" stroke="#3A4A5A" stroke-width="5"></path>')
    o.append(weed_bed(w, h, seed, n=14))
    return "".join(o)

def temple_far(w, h, seed):
    """Yet I will look again toward thy holy temple: from the deep, the light far above and the house on its hill seen as
    through the water; below, the great fish with Jonah praying within."""
    s = _fs(w, h * 0.6, 0.9)
    o = [deep(w, h, seed, weeds=True, light=True),
         f'<g opacity="0.55">{temple_front(w * 0.5, h * 0.3, w * 0.2, seed)}</g>', great_fish(w * 0.5, h * 0.7, s, flip=True, window=True, seed=seed)]
    return "".join(o)

def dry_land(p, w, h, seed):
    """It vomited out Jonah upon the dry land: the great fish in the shallows with its jaws open, Jonah on his knees on
    the sand, the morning over the sea."""
    o = [sky(w, h, "#FFE6A0", "#F3C890"), sun(w * 0.12, h * 0.34, max(14, h * 0.07), color="#FFF4C2", op=0.4), sea(w, h, h * 0.4, seed)]
    s = _fs(w * 0.62, h, 0.9)
    fx, fy = w * 0.26, h * 0.62
    o.append(great_fish(fx, fy, s, mouth=0.8, rot=-6, seed=seed))
    wy = h * 0.7                                            # the water over the fish's lower body, foam at the line
    o.append(f'<path d="M-10 {f(wy)}' + "".join(f" q 18 -7 36 0" for _ in range(int(w * 0.62 / 36) + 1)) + f' L {f(w * 0.62)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="#CFEFFF" stroke-width="2.4" opacity="0.92"></path>')
    o.append(f'<path d="M{f(w * 0.4)} {f(h + 10)} C {f(w * 0.44)} {f(h * 0.82)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.62)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h + 10)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.2"></path>')
    o.append(f'<path d="M{f(w * 0.45)} {f(h * 0.84)} C {f(w * 0.5)} {f(h * 0.74)} {f(w * 0.56)} {f(h * 0.68)} {f(w * 0.66)} {f(h * 0.64)}" stroke="#CFEFFF" stroke-width="3" fill="none" stroke-dasharray="10 8"></path>')
    o.append(jonah_kneel(w * 0.58, h * 0.86, min(1.0, h * 0.42 / 130), flip=True))
    return "".join(o)

def nineveh_great(p, w, h, seed, jonah=True, sack=False, dusk=False):
    """Nineveh, that great city, an exceeding great city of three days' journey: walls and towers to the horizon, a stepped
    temple-tower, the river; Jonah at the gate crying (sack=True: the people in sackcloth on the walls and before the gate)."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A") if dusk else sky(w, h, "#E8C890", "#F3E8C8")]
    for k in range(3):
        o.append(walls(w * (-0.05 + k * 0.08), w * (1.05 - k * 0.04), h * (0.42 + k * 0.1), h * (0.12 + k * 0.05), seed + k, color=["#B8986A", "#C8A878", "#D8B888"][k], towers=4 + k, gate=k == 2))
        if k == 0:
            for i in range(4):
                x, wd = w * 0.62, w * (0.26 - i * 0.05)
                o.append(f'<rect x="{f(x - wd / 2)}" y="{f(h * (0.3 - i * 0.07))}" width="{f(wd)}" height="{f(h * 0.07)}" fill="{["#A8804A", "#B8905A", "#C8A06A", "#D8B07A"][i]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, h * 0.78, "#C8A878", dy=0))
    o.append(river(w, h * 0.84, h * 0.06, seed=seed))
    s = fit(b, h * 0.5)
    if jonah: o.append(jonah_fig(p, w * 0.22, b, s, up=[(22, -158), (40, -176), (58, -196)]))
    if sack:
        o.append(crowd(p, w * 0.42, w * 0.96, b, h * 0.56, 8, seed, colors=(SACK, "#5A4A3A", "#7A6A58"), flip=None))
    return "".join(o)

def sackcloth(p, w, h, seed):
    """From the greatest of them even to the least of them: the people in sackcloth, kneeling and bowed, in the street."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#6A6A7A", "#C8B8A0"), walls(w * -0.05, w * 1.05, h * 0.5, h * 0.24, seed, color="#A8906A", towers=4, gate=False),
         ground(w, h, h * 0.54, "#8A7A60", dy=0)]
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.06 + i * 0.11); bb = b - (i % 2) * h * 0.06
        if i % 3 == 1: o.append(E.kneel(x, bb, fit(bb, h * 0.62) * 0.9, color=SACK, flip=i % 2 == 0))
        else: o.append(figure(p, x, bb, h * 0.5 + (i % 2) * h * 0.06, r.choice([SACK, "#5A4A3A", "#7A6A58"]), "woman" if i % 4 == 0 else "man", flip=i % 2 == 0))
    return "".join(o)

def king_ashes(p, w, h, seed):
    """The king of Nineveh arose from his throne, laid his robe from him, covered him with sackcloth and sat in ashes: the
    empty throne between the winged bulls, the robe on its step, the king sitting in the ash below."""
    from est.art import lamassu
    b = h * 0.94
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>',
         f'<rect x="-10" y="{f(h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></rect>',
         lamassu(w * 0.14, h * 0.82, min(0.9, h / 400)), lamassu(w * 0.86, h * 0.82, min(0.9, h / 400), flip=True),
         f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></rect>']
    tx, ty, k = w * 0.62, h * 0.82, min(1.2, h / 300)
    o.append(f'<g transform="translate({f(tx)} {f(ty)}) scale({f(k)})"><rect x="-50" y="-150" width="100" height="18" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             '<rect x="-46" y="-132" width="92" height="70" fill="#C8963E" stroke="#0D0D0F" stroke-width="2.4"></rect><rect x="-60" y="-62" width="120" height="16" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             '<path d="M-50 -46 L -50 0 M50 -46 L 50 0" stroke="#8A5A1E" stroke-width="10"></path>'
             '<path d="M-70 0 C -60 -20 -20 -26 0 -18 C 20 -26 60 -20 74 0 Z" fill="#6A1A5A" stroke="#0D0D0F" stroke-width="2.4"></path></g>')
    o.append(f'<ellipse cx="{f(w * 0.34)}" cy="{f(b)}" rx="{f(w * 0.14)}" ry="{f(h * 0.04)}" fill="#A8A29A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(seated(w * 0.32, b, min(1.4, h / 220), SACK, head=SACK, beard="#1A1210", bowed=True))
    return "".join(o)

def called(p, w, h, seed, dawn=False):
    """The word of Jehovah came unto Jonah: Jonah standing alone under the night sky (dawn=True: at sunrise, the second
    time), the land rolling away toward the east."""
    o = [mk.defs(p, *ALL), vista(w, h, seed, tone="dawn" if dawn else "night", stars=not dawn, sun_at=(0.78, 0.52) if dawn else None,
                                 hills_n=2, horizon=0.7)]
    b = h * 0.96
    o.append(jonah_fig(p, w * 0.34, b, fit(b, h * 0.42)))
    return "".join(o)

def sackcow(x, y, s, flip=False):
    """A cow covered with sackcloth (samuel1.cow under a rough cloth over its back)."""
    from samuel1 import cow
    sx = -1 if flip else 1
    cloth = (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx * s)} {f(s)})">'
             '<path d="M-84 -104 C -40 -116 30 -118 66 -110 L 72 -64 L 60 -58 L 50 -66 L 38 -56 L 24 -64 L 10 -54 L -6 -64 L -22 -54 L -38 -64 L -54 -56 L -70 -64 L -86 -58 Z" '
             f'fill="{SACK}" stroke="#0D0D0F" stroke-width="2.2"></path>'
             '<path d="M-60 -108 L -56 -62 M-20 -114 L -18 -60 M20 -114 L 22 -60 M50 -112 L 52 -64" stroke="#4A3E30" stroke-width="1.6" opacity="0.7"></path></g>')
    return cow(x, y, s, flip=flip) + cloth

def trough(x, y, s):
    return (f'<path d="M{f(x - 46 * s)} {f(y - 22 * s)} L {f(x + 46 * s)} {f(y - 22 * s)} L {f(x + 38 * s)} {f(y)} L {f(x - 38 * s)} {f(y)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M{f(x - 40 * s)} {f(y - 18 * s)} L {f(x + 40 * s)} {f(y - 18 * s)}" stroke="#4A3220" stroke-width="{f(4 * s)}"></path>')

def decree(p, w, h, seed):
    """Let neither man nor beast, herd nor flock, taste anything: a herald with the decree on the wall, the herds standing
    covered with sackcloth by their empty troughs, the flock beside them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#7A7A8A", "#D8C8B0"), walls(w * 0.3, w * 1.05, h * 0.44, h * 0.22, seed, color="#B8986A", towers=3, gate=False),
         ground(w, h, h * 0.48, "#9A8A6A", dy=0)]
    s = fit(h * 0.3, h * 0.08)
    o.append(man(p, w * 0.58, h * 0.3, s * 0.6, "#5A3A6A", up=[(22, -158), (38, -180), (34, -206)]) + scroll(w * 0.62, h * 0.08, w * 0.08, h * 0.06, lines=3))
    k = min(0.85, h / 380)
    o.append(sackcow(w * 0.16, b - 16 * k, k * 0.9) + sackcow(w * 0.42, b - 22 * k, k * 0.8, flip=True))
    o.append(trough(w * 0.24, b, k) + trough(w * 0.5, b + 2, k * 0.9))
    o.append(sheep_row(w * 0.64, w * 0.96, b, 4, seed, s=k * 0.7))
    return "".join(o)

def gourd_leaf(x, y, s, rot, fill="#3F8A34", vein="#2A5A22"):
    """A broad five-lobed gourd leaf on its stalk, rot degrees (0 = pointing up)."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot:.1f}) scale({f(s)})">'
            f'<path d="M0 0 C -8 -10 -30 -12 -34 -30 C -24 -32 -20 -42 -22 -54 C -10 -50 -4 -60 0 -70 C 4 -60 10 -50 22 -54 C 20 -42 24 -32 34 -30 C 30 -12 8 -10 0 0 Z" fill="{fill}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M0 0 L 0 -62 M0 -14 L -24 -30 M0 -14 L 24 -30 M0 -30 L -14 -50 M0 -30 L 14 -50" stroke="{vein}" stroke-width="1.6" fill="none"></path></g>')

def gourd_fruit(x, y, s, fill="#A8C46A"):
    return (f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + 8 * s)}" stroke="#2E5A22" stroke-width="{f(2.4 * s)}"></path>'
            f'<path d="M{f(x)} {f(y + 6 * s)} C {f(x - 7 * s)} {f(y + 8 * s)} {f(x - 6 * s)} {f(y + 20 * s)} {f(x - 12 * s)} {f(y + 30 * s)} C {f(x - 18 * s)} {f(y + 44 * s)} {f(x + 18 * s)} {f(y + 44 * s)} {f(x + 12 * s)} {f(y + 30 * s)} C {f(x + 6 * s)} {f(y + 20 * s)} {f(x + 7 * s)} {f(y + 8 * s)} {f(x)} {f(y + 6 * s)} Z" '
            f'fill="{fill}" stroke="#0D0D0F" stroke-width="1.8"></path>')

def gourd_vine(bx, b, k, seed, stage="gourd"):
    """The gourd grown up over the booth: a thick vine climbing the left post and running along the roof, broad leaves,
    curling tendrils and hanging gourds. stage 'gourd' green and full; 'wind' withered brown, leaves fallen on the sand."""
    r = random.Random(seed)
    dead = stage != "gourd"
    leaf, vein = {"gourd": ("#3F8A34", "#2A5A22"), "wind": ("#8A6A3A", "#5A4022")}[stage]
    stem = "#2E6A2A" if not dead else "#6A5A2A"
    o = [f'<path d="M{f(bx - 96 * k)} {f(b)} C {f(bx - 112 * k)} {f(b - 50 * k)} {f(bx - 80 * k)} {f(b - 90 * k)} {f(bx - 96 * k)} {f(b - 128 * k)} '
         f'C {f(bx - 60 * k)} {f(b - 148 * k)} {f(bx - 10 * k)} {f(b - 126 * k)} {f(bx + 30 * k)} {f(b - 140 * k)} C {f(bx + 60 * k)} {f(b - 150 * k)} {f(bx + 90 * k)} {f(b - 130 * k)} {f(bx + 110 * k)} {f(b - 136 * k)}" '
         f'stroke="{stem}" stroke-width="{f(7 * k)}" fill="none" stroke-linecap="round"></path>']
    for i in range(6):                                      # tendrils
        tx, ty = bx + (-90 + i * 36) * k, b - (132 + r.uniform(-6, 8)) * k
        o.append(f'<path d="M{f(tx)} {f(ty)} c {f(6 * k)} {f(8 * k)} {f(14 * k)} {f(4 * k)} {f(10 * k)} {f(-4 * k)} c {f(-3 * k)} {f(-5 * k)} {f(-8 * k)} {f(-2 * k)} {f(-6 * k)} {f(2 * k)}" stroke="{stem}" stroke-width="{f(1.8 * k)}" fill="none"></path>')
    for i in range(13):                                     # leaves up the post and along the roof
        if i < 4: lx, ly, rot = bx - 98 * k + r.uniform(-8, 8) * k, b - (36 + i * 26) * k, r.choice([-60, 60]) + r.uniform(-15, 15)
        else: lx, ly, rot = bx + (-96 + (i - 4) * 25) * k, b - (136 + r.uniform(-4, 10)) * k, r.uniform(-40, 40)
        if stage == "wind": rot = 160 + r.uniform(-30, 30)
        o.append(gourd_leaf(lx, ly, k * r.uniform(0.8, 1.05) * (0.8 if stage == "wind" else 1), rot, leaf, vein))
    if stage == "gourd":
        for i in range(3):
            o.append(gourd_fruit(bx + (-50 + i * 54) * k, b - 132 * k, k))
    else:
        for i in range(7):
            o.append(gourd_leaf(bx + r.uniform(-150, 170) * k, b - r.uniform(0, 4) * k, k * 0.6, r.choice([95, -95]) + r.uniform(-20, 20), leaf, vein))
    return "".join(o)

def booth(p, w, h, seed, stage="booth"):
    """On the east side of the city: Jonah sitting under his booth, watching the city. stage 'booth', 'gourd' (the gourd
    grown over it, green and shading), 'wind' (the sun beating and the sultry east wind, the gourd withered, Jonah
    fainting)."""
    b = h * 0.94
    hot = stage in ("wind",)
    o = [sky(w, h, "#FFE680", "#FFB04A") if hot else sky(w, h, "#8FD0E2", "#F3E8C8")]
    o.append(sun(w * 0.82, h * 0.16, max(14, h * 0.07), color="#FFF4C2" if hot else "#FFE680", op=0.7 if hot else 0.4))
    o.append(walls(w * 0.52, w * 1.02, h * 0.5, h * 0.16, seed, color="#C8A878", towers=3, gate=False))
    o.append(ground(w, h, h * 0.52, "#D8B880", dy=0))
    if hot: o.append(wind_lines(w, h, seed, n=10, color="#FFF4C2", op=0.6, y0=0.3, y1=0.9))
    bx, k = w * 0.3, min(1.5, h / 230)
    if stage == "gourd":                                    # the cool shade under the gourd
        o.append(f'<ellipse cx="{f(bx)}" cy="{f(b)}" rx="{f(130 * k)}" ry="{f(10 * k)}" fill="#6A5A3A" opacity="0.35"></ellipse>')
    o.append(f'<g transform="translate({f(bx)} {f(b)}) scale({f(k)})"><path d="M-90 0 L -84 -120 M90 0 L 84 -120 M-90 -120 L 92 -122" stroke="#6A4A2A" stroke-width="7" fill="none" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{-96 + i * 24} -124 l 12 -8 l 14 8" stroke="#8A6A3A" stroke-width="4" fill="none"></path>' for i in range(8)) + '</g>')
    if stage in ("gourd", "wind"): o.append(gourd_vine(bx, b, k, seed, stage))
    o.append(seated(bx + 10 * k, b, k * 0.62, JONAH_C, head=JONAH_C, beard="#4A2A1A", flip=True, bowed=stage == "wind"))
    return "".join(o)

def worm_close(w, h, seed):
    """When the morning rose the next day, God prepared a worm, and it smote the gourd, that it withered: the gourd's stem
    close up at dawn, the worm boring into it, the leaves above already yellowing and drooping."""
    o = [sky(w, h, "#5A4A7A", "#FFB07A"), sun(w * 0.84, h * 0.86, max(14, h * 0.08), color="#FFC14D", op=0.45)]
    k = min(2.4, h / 120)
    sx = w * 0.3
    d = f"M{f(sx)} {f(h + 10)} C {f(sx + 10)} {f(h * 0.6)} {f(sx - 14)} {f(h * 0.34)} {f(sx + 40)} {f(h * 0.12)} C {f(sx + 120)} {f(-h * 0.02)} {f(w * 0.7)} {f(h * 0.14)} {f(w + 10)} {f(h * 0.06)}"
    o.append(f'<path d="{d}" stroke="#0D0D0F" stroke-width="{f(12 * k + 4)}" fill="none"></path><path d="{d}" stroke="#5A7A2A" stroke-width="{f(12 * k)}" fill="none"></path>')
    r = random.Random(seed)
    for i in range(6):
        lx, ly = sx + 70 + i * (w * 0.62 - 40) / 6, h * (0.12 + r.uniform(0, 0.05))
        o.append(gourd_leaf(lx, ly, k * 0.85, 150 + r.uniform(-30, 30), "#C8B040" if i % 2 else "#9AA03A", "#6A5A22"))
    wx, wy = sx + 2, h * 0.62                               # the worm at its bore-hole in the stem
    wd = f"M{f(wx + 2 * k)} {f(wy)} c {f(6 * k)} {f(-8 * k)} {f(12 * k)} {f(6 * k)} {f(18 * k)} 0 c {f(6 * k)} {f(-8 * k)} {f(12 * k)} {f(6 * k)} {f(18 * k)} {f(-2 * k)}"
    o.append(f'<ellipse cx="{f(wx)}" cy="{f(wy)}" rx="{f(5 * k)}" ry="{f(3.4 * k)}" fill="#2A1A10"></ellipse>'
             f'<path d="{wd}" stroke="#0D0D0F" stroke-width="{f(7 * k + 3)}" fill="none" stroke-linecap="round"></path>'
             f'<path d="{wd}" stroke="#E8C8A8" stroke-width="{f(7 * k)}" fill="none" stroke-linecap="round"></path>'
             f'<circle cx="{f(wx + 37 * k)}" cy="{f(wy - 2 * k)}" r="{f(1.6 * k)}" fill="#3A2A1A"></circle>')
    return "".join(o)

def sixscore(p, w, h, seed):
    """Nineveh, that great city, wherein are more than sixscore thousand persons, and also much cattle: the city at evening,
    its lamps lit, herds on the plain before it (to the left, clear of the end mark)."""
    from samuel1 import cow
    o = [nineveh_great(p, w, h, seed, jonah=False, dusk=True)]
    k = min(0.62, h / 480)
    for i in range(4): o.append(cow(w * (0.08 + i * 0.13), h * 0.97, k * (0.9 + (i % 2) * 0.1), flip=i % 2 == 1))
    return "".join(o)
