"""Drawings for Job 38–39 (Jehovah answers Job out of the whirlwind): the whirlwind over the ash heap, the foundations of
the earth as a blueprint plate, the sea shut in with doors, the dayspring, the storehouses of snow and hail, the rain on the
wilderness, the Pleiades and Orion, and the creatures — the lioness, the raven, the wild goats and the hinds, the wild ass,
the wild-ox, the ostrich, the war-horse, the hawk and the eagle. God is never drawn: his words are in the Voice box.
Creature helpers: ibex(), hind(), raven(), wild_ox_fig()."""
from job.art10 import *
from job.art10 import f, K2, K3, sea, label, SHIELD
import exo.art6 as A6
import re

def ibex(x, y, s=1.0, flip=False):
    """A wild goat of the rock, the great horns swept back; (x, y) = the ground under it; about 110 units tall at s=1."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            + '<path d="M-26 -36 L -30 0 M-16 -34 L -14 0 M18 -34 L 16 0 M28 -36 L 32 0" stroke="#0D0D0F" stroke-width="5.5" stroke-linecap="round"></path>'
            + '<path d="M-26 -36 L -30 0 M-16 -34 L -14 0 M18 -34 L 16 0 M28 -36 L 32 0" stroke="#8A6A4A" stroke-width="3.5" stroke-linecap="round"></path>'
            + P("M-40 -50 C -40 -66 -10 -70 14 -66 C 30 -64 40 -60 42 -52 L 40 -36 C 30 -30 0 -30 -26 -32 C -36 -34 -40 -40 -40 -50 Z", "#A8805A", 2)
            + P("M36 -60 L 44 -78 C 48 -84 58 -84 62 -76 L 66 -66 L 54 -62 Z", "#A8805A", 2)
            + '<path d="M50 -82 C 40 -108 14 -116 0 -100 C 14 -104 32 -98 42 -80" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></path>'
            + '<path d="M44 -98 L 40 -92 M34 -106 L 32 -98 M24 -108 L 24 -100" stroke="#0D0D0F" stroke-width="1.4"></path>'
            + '<path d="M60 -68 L 58 -58" stroke="#3A2A1A" stroke-width="3"></path><circle cx="54" cy="-76" r="1.8" fill="#0D0D0F"></circle></g>')

def hind(x, y, s=1.0, flip=False, fawn=False):
    """A hind (a doe), slender, ears up; fawn=True: a small spotted fawn."""
    sx = -s if flip else s
    c = "#B8784A"
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
         + f'<path d="M-24 -40 L -26 0 M-14 -38 L -12 0 M18 -38 L 16 0 M26 -40 L 30 0" stroke="#0D0D0F" stroke-width="4.5" stroke-linecap="round"></path>'
         + f'<path d="M-24 -40 L -26 0 M-14 -38 L -12 0 M18 -38 L 16 0 M26 -40 L 30 0" stroke="{c}" stroke-width="2.8" stroke-linecap="round"></path>'
         + P("M-34 -52 C -34 -64 -6 -66 16 -62 C 30 -60 36 -56 36 -48 L 32 -38 C 20 -34 -6 -34 -24 -36 C -32 -38 -34 -44 -34 -52 Z", c, 2)
         + P("M30 -56 L 40 -84 C 44 -90 54 -90 56 -82 L 62 -74 L 50 -70 L 40 -54 Z", c, 2)
         + P("M44 -88 L 40 -100 L 48 -92 Z M50 -88 L 52 -100 L 56 -90 Z", c, 1.4) + '<circle cx="52" cy="-82" r="1.6" fill="#0D0D0F"></circle>')
    if fawn: o += "".join(f'<circle cx="{cx}" cy="{cy}" r="2.4" fill="#F3EFE6"></circle>' for cx, cy in ((-20, -54), (-8, -56), (4, -54), (14, -56), (-14, -46), (0, -46)))
    return o + '</g>'

def raven(x, y, s=1.0, flip=False, fly=False):
    """A raven, black, perched (or flying)."""
    sx = -s if flip else s
    if fly:
        body = P("M-40 -10 C -20 -30 -6 -30 0 -14 C 10 -36 30 -40 50 -24 C 30 -20 16 -8 10 0 C 0 6 -14 4 -20 0 C -28 -4 -34 -6 -40 -10 Z", "#14121A", 2)
    else:
        body = (P("M-20 0 C -26 -14 -14 -30 6 -30 C 20 -30 26 -22 24 -12 C 20 -2 4 4 -20 0 Z", "#14121A", 2) + P("M-20 -4 L -40 2 L -20 4 Z", "#14121A", 1.6)
                + P("M16 -28 C 18 -38 30 -40 34 -32 L 44 -30 L 32 -24 Z", "#14121A", 1.6) + '<path d="M2 0 L 0 10 M10 -2 L 10 10" stroke="#3A3430" stroke-width="2"></path><circle cx="28" cy="-33" r="1.4" fill="#C8C8D8"></circle>')
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">' + body + '</g>'

def wild_ox_fig(x, y, s=1.0, flip=False):
    """The wild-ox: a great dark bull, massive in the shoulder, with long horns curving forward."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            + '<path d="M-50 -40 L -54 0 M-36 -38 L -34 0 M34 -40 L 32 0 M48 -44 L 52 0" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path>'
            + '<path d="M-50 -40 L -54 0 M-36 -38 L -34 0 M34 -40 L 32 0 M48 -44 L 52 0" stroke="#2A1A12" stroke-width="6" stroke-linecap="round"></path>'
            + P("M-64 -56 C -66 -76 -40 -84 0 -86 C 30 -96 54 -92 62 -76 L 66 -50 C 56 -38 20 -34 -20 -36 C -48 -38 -62 -44 -64 -56 Z", "#2A1A12", 2.4)
            + P("M-64 -60 C -74 -54 -78 -40 -74 -26", "none", 3)
            + P("M58 -78 L 82 -66 C 90 -60 92 -48 84 -42 L 70 -44 L 60 -56 Z", "#2A1A12", 2.2)
            + '<path d="M70 -74 C 80 -96 96 -100 104 -92 M74 -70 C 92 -80 104 -76 106 -66" stroke="#E8E2D6" stroke-width="4" fill="none" stroke-linecap="round"></path>'
            + '<circle cx="78" cy="-64" r="2" fill="#E8B830"></circle></g>')

def whirl_over(p, w, h, seed):
    """Then Jehovah answered Job out of the whirlwind: the whirlwind coming down out of a black sky toward the ash heap, Job
    and his friends small beneath it, lightning about (God is never drawn)."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#05051A", "#5B2470"), clouds(w, h * 0.12, seed, 10, color="#1E1650", op=0.9, ry=0.06, h=h),
         V.rays(w * 0.62, h * 0.3, 30, 30, max(w, h), color="#FFF4C2", op=0.1),
         whirl(w * 0.62, h * 0.12, h * 0.86, w * 0.42, w * 0.05, seed, color="#8A7AB8", op=0.55, n=16)]
    for i in range(2): o.append(E2.bolt(w * (0.18 + i * 0.66), h * 0.1, h * 0.4, seed + i, w=1.2))
    o.append(ground(w, h, h * 0.9, "#2A2238", dy=0) + ash_mound(w * 0.3, h * 0.99, w * 0.24, h * 0.06, seed))
    k = min(0.8, h * 0.16 / 140)
    o.append(seated_job(w * 0.3, h * 0.95, k, shard=False) + seated_friend(w * 0.08, h * 0.99, k * 0.8, "eli") + seated_friend(w * 0.16, h * 0.99, k * 0.8, "bil")
             + seated_friend(w * 0.46, h * 0.99, k * 0.8, "zop", flip=True))
    return "".join(o)

def foundations(w, h, seed):
    """Where wast thou when I laid the foundations of the earth? who determined the measures thereof, who stretched the line
    upon it? who laid the corner-stone, when the morning stars sang together?: a blueprint plate — the earth's footings in
    section, the measuring line stretched over them, the corner-stone marked, the morning stars above."""
    o = [grid_bg(w, h)]
    gy = h * 0.88
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(gy)}" width="{f(w * 0.84)}" height="{f(h * 0.07)}" fill="#1E3A5A" stroke="#8FD0E2" stroke-width="2"></rect>')
    for i in range(7):
        x = w * (0.1 + i * 0.13)
        o.append(f'<rect x="{f(x)}" y="{f(gy + h * 0.07)}" width="{f(w * 0.06)}" height="{f(h * 0.04)}" fill="none" stroke="#8FD0E2" stroke-width="1.6" stroke-dasharray="4 3"></rect>')
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(gy - h * 0.04)}" width="{f(w * 0.08)}" height="{f(h * 0.04)}" fill="#FFD23F" fill-opacity="0.35" stroke="#FFD23F" stroke-width="2"></rect>'
             + label(w * 0.24, gy - h * 0.01, "THE CORNER-STONE", "#FFD23F", 9))
    o.append(f'<path d="M{f(w * 0.08)} {f(gy - h * 0.1)} L {f(w * 0.92)} {f(gy - h * 0.1)}" stroke="#F3EFE6" stroke-width="1.6"></path>'
             + "".join(f'<path d="M{f(w * (0.08 + i * 0.084))} {f(gy - h * 0.11)} L {f(w * (0.08 + i * 0.084))} {f(gy - h * 0.09)}" stroke="#F3EFE6" stroke-width="1.4"></path>' for i in range(11))
             + label(w * 0.6, gy - h * 0.12, "THE LINE STRETCHED UPON IT", "#F3EFE6", 9))
    o.append(label(w * 0.5, gy + h * 0.045, "THE FOUNDATIONS OF THE EARTH", "#8FD0E2", 10))
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.2 + i * 0.1); y = h * (0.73 + r.uniform(-0.015, 0.015))
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="#FFF4C2"></circle><circle cx="{f(x)}" cy="{f(y)}" r="9" fill="#FFF4C2" opacity="0.25"></circle>')
    return "".join(o)

def sea_bound(w, h, seed):
    """Who shut up the sea with doors, when I made clouds the garment thereof, and set bars and doors, and said, Hitherto
    shalt thou come, but no further: the sea heaving under a mantle of thick cloud, its waves breaking against a line of
    cliffs and stopping there."""
    o = [K2.sky(w, h, "#1A1A3A", "#5A6A8A"), clouds(w, h * 0.5, seed, 10, color="#2A2A44", op=0.95, ry=0.07, h=h),
         sea(w, h, h * 0.76, seed, color="#1F4A6A", deep="#0B2A3A"),
         P(f"M{f(w * 0.62)} {f(h + 10)} L {f(w * 0.66)} {f(h * 0.7)} L {f(w * 0.74)} {f(h * 0.66)} L {f(w * 0.86)} {f(h * 0.68)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} Z", "#5A5048")]
    r = random.Random(seed)
    for i in range(10):
        y = h * r.uniform(0.7, 0.98)
        o.append(f'<path d="M{f(w * 0.62 - r.uniform(0, 30))} {f(y)} q -20 -16 -40 -4 q 10 -10 30 -6" fill="#E8F6FA" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(w * 0.63)} {f(h * 0.7)} L {f(w * 0.6)} {f(h + 10)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 5"></path>')
    return "".join(o)

def dayspring(w, h, seed):
    """Hast thou commanded the morning, and caused the dayspring to know its place, that it might take hold of the ends of
    the earth?: the curve of the earth from on high, a line of dawn running along its rim from end to end."""
    o = [K2.sky(w, h, "#05051A", "#1A1A3A"), mk.stars(80, w, h * 0.7, seed),
         f'<path d="M-10 {f(h * 0.94)} Q {f(w * 0.5)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.94)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A2A3A"></path>',
         f'<path d="M-10 {f(h * 0.94)} Q {f(w * 0.5)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.94)}" stroke="#FFD890" stroke-width="10" fill="none" opacity="0.5"></path>',
         f'<path d="M-10 {f(h * 0.94)} Q {f(w * 0.5)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.94)}" stroke="#FFF4C2" stroke-width="3" fill="none"></path>',
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.82)}" rx="{f(w * 0.1)}" ry="{f(h * 0.03)}" fill="#FFF4C2" opacity="0.8"></ellipse>']
    return "".join(o)

def hail(w, h, seed):
    """Hast thou entered the treasuries of the snow, or seen the treasures of the hail, which I have reserved against the day
    of battle?: hail driving down out of a black cloud onto the hills, stones of ice bouncing on the ground."""
    o = [K2.sky(w, h, "#2A2A3A", "#8A90A0"), clouds(w, h * 0.06, seed, 10, color="#1A1A28", op=0.95, ry=0.08, h=h),
         hills(w, h, h * 0.84, seed, "#4A5040", amp=10, step=80), ground(w, h, h * 0.9, "#5A6048", dy=0), E2.hail(140, -10, w + 10, 0, h, seed)]
    return "".join(o)

def desert_rain(w, h, seed):
    """To cause it to rain on a land where no man is, to satisfy the waste and desolate ground, and to cause the tender grass
    to spring forth: rain falling on empty desert hills, green grass springing up where it lands."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A6A7A", "#C8B890"), clouds(w, h * 0.08, seed, 7, color="#4A5A6A", op=0.9, ry=0.07, h=h),
         hills(w, h, h * 0.8, seed, "#B8986A", amp=12, step=80), ground(w, h, h * 0.88, "#C8A06A", dy=0)]
    for i in range(80):
        x = r.uniform(0, w + 30); y = r.uniform(0, h * 0.86)
        o.append(f'<path d="M{f(x)} {f(y)} l -5 16" stroke="#DCEFF8" stroke-width="1.3" opacity="0.7"></path>')
    for i in range(60):
        x = r.uniform(0, w); y = h * r.uniform(0.9, 1.0)
        o.append(f'<path d="M{f(x)} {f(y)} l -3 -10 M{f(x)} {f(y)} l 0 -12 M{f(x)} {f(y)} l 3 -10" stroke="#5A9A3A" stroke-width="1.6"></path>')
    return "".join(o)

def lioness(w, h, seed):
    """Canst thou hunt the prey for the lioness, or satisfy the appetite of the young lions, when they couch in their dens?:
    a lioness crouched in the long grass by her den in the rocks, her young lions beside her."""
    o = [K2.sky(w, h, "#E8A06A", "#F3D8A0"), P(f"M{f(w * 0.6)} {f(h + 10)} L {f(w * 0.66)} {f(h * 0.72)} L {f(w * 0.9)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} Z", "#8A7060"),
         P(f"M{f(w * 0.7)} {f(h * 0.98)} C {f(w * 0.7)} {f(h * 0.84)} {f(w * 0.86)} {f(h * 0.82)} {f(w * 0.88)} {f(h * 0.98)} Z", "#1A120E"),
         ground(w, h, h * 0.86, "#C8A060", dy=0)]
    k = min(0.6, h / 600)
    o.append(re.sub(r'<path d="[^"]*" fill="#8A4A16"[^>]*></path>', "", J2.lion(w * 0.28, h * 0.98, k, roar=False)) + J2.lion(w * 0.48, h * 0.98, k * 0.5, roar=False, flip=True) + J2.lion(w * 0.56, h * 0.99, k * 0.45, roar=True))
    r = random.Random(seed)
    for i in range(40):
        x = r.uniform(0, w * 0.66); y = h * r.uniform(0.92, 1.0)
        o.append(f'<path d="M{f(x)} {f(y)} q 3 -12 8 -18" stroke="#A8803A" stroke-width="1.6" fill="none"></path>')
    return "".join(o)

def ravens(w, h, seed):
    """Who provideth for the raven his prey, when his young ones cry unto God?: a raven bringing food to its nest of crying
    young on a bare crag, another raven wheeling over."""
    o = [K2.sky(w, h, "#8A9AB8", "#E8E0D0"), P(f"M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.76)} L {f(w * 0.6)} {f(h * 0.72)} L {f(w * 0.66)} {f(h + 10)} Z", "#6A6058")]
    nx, ny = w * 0.54, h * 0.73
    o.append(P(f"M{f(nx - 36)} {f(ny)} C {f(nx - 30)} {f(ny + 14)} {f(nx + 30)} {f(ny + 14)} {f(nx + 36)} {f(ny)} Z", "#6A4A2A"))
    for i in range(3):
        bx = nx - 16 + i * 16
        o.append(f'<circle cx="{f(bx)}" cy="{f(ny - 6)}" r="7" fill="#2A2830" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M{f(bx)} {f(ny - 12)} l -4 -10 l 8 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path>')
    k = min(1.4, h / 240)
    o.append(raven(w * 0.72, h * 0.66, k, flip=True, fly=True) + raven(w * 0.2, h * 0.5, k * 0.6, fly=True))
    return "".join(o)

def goats_hinds(w, h, seed):
    """Knowest thou the time when the wild goats of the rock bring forth? or canst thou mark when the hinds do calve?: wild
    goats with their kids on a high crag, and below in the open field a hind with her fawn."""
    o = [K2.sky(w, h, "#8FB8D8", "#F0E8D0"), P(f"M{f(w * 0.02)} {f(h + 10)} L {f(w * 0.1)} {f(h * 0.72)} L {f(w * 0.3)} {f(h * 0.68)} L {f(w * 0.42)} {f(h + 10)} Z", "#8A7060"),
         ground(w, h, h * 0.88, "#9AB86A", dy=0)]
    k = min(0.7, h / 500)
    o.append(ibex(w * 0.18, h * 0.71, k) + ibex(w * 0.28, h * 0.7, k * 0.5, flip=True))
    o.append(hind(w * 0.64, h * 0.98, k * 1.1) + hind(w * 0.76, h * 0.99, k * 0.6, fawn=True, flip=True))
    return "".join(o)

def wild_ox(w, h, seed):
    """Will the wild-ox be content to serve thee, or abide by thy crib? canst thou bind him with his band in the furrow?: the
    wild-ox standing free on the open range, and in the field below a plow and a yoke lying unused."""
    o = [K2.sky(w, h, "#8FB8D8", "#F0E8D0"), hills(w, h, h * 0.8, seed, "#8A9A5A", amp=10, step=90), ground(w, h, h * 0.86, "#A8986A", dy=0)]
    for i in range(5): o.append(f'<path d="M{f(w * 0.5)} {f(h * (0.9 + i * 0.022))} L {f(w + 10)} {f(h * (0.89 + i * 0.022))}" stroke="#7A6A3A" stroke-width="2"></path>')
    k = min(1.0, h / 360)
    o.append(wild_ox_fig(w * 0.24, h * 0.97, k))
    o.append(P(f"M{f(w * 0.62)} {f(h * 0.95)} l 60 -4 l 24 -24 l 6 4 l -20 26 l 8 12 l -8 4 l -12 -12 l -58 4 Z", "#8A5A30", 2)
             + P(f"M{f(w * 0.8)} {f(h * 0.99)} l 80 -2 l 0 6 l -80 2 Z", "#5A3A1E", 2))
    return "".join(o)

def ostrich_eggs(w, h, seed):
    """The wings of the ostrich wave proudly; she leaveth her eggs on the earth, and warmeth them in the dust; what time she
    lifteth up herself on high, she scorneth the horse and his rider: her eggs lying in a scrape in the sand, and the ostrich
    racing away past a horse and rider."""
    o = [K2.sky(w, h, "#E8C890", "#F3E8C8"), ground(w, h, h * 0.84, "#D8B87A", dy=0),
         f'<ellipse cx="{f(w * 0.18)}" cy="{f(h * 0.96)}" rx="{f(w * 0.1)}" ry="{f(h * 0.025)}" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.4"></ellipse>']
    for i in range(5):
        o.append(f'<ellipse cx="{f(w * (0.12 + i * 0.03))}" cy="{f(h * 0.955)}" rx="9" ry="7" fill="#F3EAD0" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    k = min(1.0, h / 340)
    o.append(E3.horse(w * 0.46, h * 0.98, k * 0.5, color="#5A3A22") + f'<g transform="translate({f(w * 0.46 + 30 * k * 0.5)} {f(h * 0.98 - 36 * k * 0.5)}) scale({f(k * 0.5)})">' + P("M-10 -40 L -14 -90 L 2 -92 C 8 -80 12 -66 16 -56 L 6 -40 Z", "#7A2A2A", 2) + '<circle cx="-6" cy="-100" r="11" fill="#3A1E14" stroke="#0D0D0F" stroke-width="2"></circle></g>')
    o.append(ostrich(w * 0.8, h * 0.98, k * 0.62, run=True) + mk.speed(w * 0.66, h * 0.86, 8, 10, w * 0.12, seed, color="#F3E8C8", op=0.6))
    return "".join(o)

def war_horse(p, w, h, seed):
    """Hast thou given the horse his might? he paweth in the valley, he goeth out to meet the armed men; he smelleth the battle
    afar off, the thunder of the captains, and the shouting: a war-horse rearing with its mane flying, a trumpeter beyond, the
    spears of the armed men on the ridge."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8805A", "#F3D8A0"), hills(w, h, h * 0.8, seed, "#8A6A4A", amp=10, step=90), ground(w, h, h * 0.88, "#B8905A", dy=0)]
    s = fit(h * 0.82, h * 0.7)
    for i in range(7): o.append(warrior(p, w * (0.56 + i * 0.06), h * 0.82, s, WAR[i % 4]))
    o.append(J.trumpeter(p, w * 0.94, h * 0.9, fit(h * 0.9, h * 0.72), flip=True))
    k = min(1.4, h / 240)
    o.append(f'<g transform="rotate(-18 {f(w * 0.3)} {f(h * 0.98)})">' + E3.horse(w * 0.3, h * 0.98, k, color="#3A2214") + '</g>')
    o.append(mk.speed(w * 0.3, h * 0.8, 10, 20, w * 0.18, seed, color="#F3E8C8", op=0.5))
    return "".join(o)

def eagle_cliff(w, h, seed):
    """Is it by thy wisdom that the hawk soareth? is it at thy command that the eagle mounteth up, and maketh her nest on high,
    upon the point of the cliff?: an eagle on her nest at the point of a high crag, a hawk soaring southward over the void."""
    o = [K2.sky(w, h, "#5A8AB8", "#E8F0E0"), P(f"M{f(w * 0.56)} {f(h + 10)} L {f(w * 0.62)} {f(h * 0.8)} L {f(w * 0.72)} {f(h * 0.76)} L {f(w * 0.78)} {f(h * 0.82)} L {f(w * 0.84)} {f(h + 10)} Z", "#7A6A5A"),
         P(f"M{f(w * 0.64)} {f(h * 0.8)} C {f(w * 0.66)} {f(h * 0.84)} {f(w * 0.74)} {f(h * 0.84)} {f(w * 0.76)} {f(h * 0.8)} Z", "#6A4A2A", 1.8)]
    k = min(1.2, h / 300)
    o.append(f'<g transform="translate({f(w * 0.7)} {f(h * 0.78)}) scale({f(k * 0.6)})">' + P("M-20 0 C -26 -30 -10 -50 10 -50 C 30 -50 36 -30 30 0 Z", "#5A3A22", 2)
             + P("M4 -50 C 6 -66 22 -68 26 -58 L 38 -56 L 24 -50 Z", "#F3EFE6", 1.8) + '<path d="M36 -56 l 6 4 l -8 2 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path></g>')
    o.append(A6.eagle(w * 0.24, h * 0.86, min(1.0, h / 330)) + "".join(f'<path d="M{f(w * 0.24 - 100 - i * 12)} {f(h * 0.86 - 10 + i * 8)} L {f(w * 0.24 - 140 - i * 14)} {f(h * 0.86 - 10 + i * 8)}" stroke="#FFFFFF" stroke-width="1.6" opacity="0.6"></path>' for i in range(3)))
    return "".join(o)
