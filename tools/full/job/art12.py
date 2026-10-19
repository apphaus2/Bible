"""Drawings for Job 40–42: behemoth as the river-horse among the lotus-trees and leviathan as the great crocodile of the
river and the sea, drawn as natural creatures (no gore, no monster); Job laying his hand upon his mouth and repenting in
dust and ashes; the friends' burnt-offering of seven bullocks and seven rams; the kin eating bread in Job's house; the
latter end blessed — the tally of the flocks, the three daughters named, four generations; Job's death in words only."""
from job.art11 import *
from job.art11 import f, K2, K3, sea, label, SHIELD, re

def hippo(x, y, s=1.0, flip=False, mouth=False):
    """The river-horse: a great barrel body on short legs, a broad head with small ears and eyes on top; about 120 units tall
    at s=1, 260 long."""
    sx = -s if flip else s
    jaw = ('<path d="M96 -70 C 120 -88 140 -84 150 -70 L 150 -50 C 130 -40 110 -44 96 -50 Z" fill="#8A5A6A" stroke="#0D0D0F" stroke-width="2"></path>'
           '<path d="M118 -70 L 120 -62 M136 -70 L 136 -62" stroke="#F3EFE6" stroke-width="3"></path>') if mouth else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            + '<path d="M-80 -30 L -82 0 M-56 -26 L -54 0 M50 -28 L 48 0 M74 -32 L 78 0" stroke="#0D0D0F" stroke-width="20" stroke-linecap="round"></path>'
            + '<path d="M-80 -30 L -82 0 M-56 -26 L -54 0 M50 -28 L 48 0 M74 -32 L 78 0" stroke="#6A5A62" stroke-width="16" stroke-linecap="round"></path>'
            + P("M-110 -60 C -112 -100 -60 -118 0 -118 C 60 -118 96 -104 100 -80 L 102 -50 C 90 -24 40 -18 -20 -18 C -80 -18 -108 -30 -110 -60 Z", "#7A6A72", 2.6)
            + P("M-110 -64 C -120 -60 -124 -50 -120 -40", "none", 3)
            + jaw
            + P("M88 -100 C 100 -116 130 -116 146 -104 C 158 -94 160 -76 150 -68 C 132 -60 108 -62 94 -70 Z", "#7A6A72", 2.4)
            + '<ellipse cx="106" cy="-116" rx="7" ry="5" fill="#7A6A72" stroke="#0D0D0F" stroke-width="1.8"></ellipse><circle cx="118" cy="-104" r="3" fill="#0D0D0F"></circle>'
            + '<circle cx="148" cy="-90" r="2.4" fill="#0D0D0F"></circle><path d="M-60 -60 C -30 -50 20 -50 60 -62" stroke="#5A4A52" stroke-width="2" fill="none"></path>'
            + '<path d="M-60 -96 C -20 -104 30 -102 70 -94" stroke="#A8949C" stroke-width="3" fill="none" opacity="0.7"></path></g>')

def croc(x, y, s=1.0, flip=False, swim=False, open_=False):
    """The great crocodile: a long armoured body with rows of raised scales, a heavy tail, the long jaws; about 420 units
    long at s=1. swim=True: only the back, the eyes and the snout above the water line y."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">']
    if not swim:
        o.append('<path d="M-60 -10 L -76 8 M-20 -10 L -10 8 M100 -10 L 90 10 M140 -10 L 150 10" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path>'
                 '<path d="M-60 -10 L -76 8 M-20 -10 L -10 8 M100 -10 L 90 10 M140 -10 L 150 10" stroke="#4A5A3A" stroke-width="8" stroke-linecap="round"></path>')
    jaw = ('M200 -26 L 300 -40 L 300 -30 L 210 -18 Z M200 -16 L 300 -6 L 300 4 L 200 -4 Z' if open_ else 'M200 -24 L 300 -24 C 306 -18 306 -10 300 -6 L 200 -6 Z')
    o.append(P("M-220 -12 C -150 -18 -100 -30 -60 -36 C 0 -44 100 -44 160 -36 L 200 -30 L 200 -2 C 120 6 0 6 -80 0 C -140 -2 -190 -4 -220 -12 Z", "#4A5A3A", 2.4))
    o.append(P(jaw, "#5A6A44", 2.2))
    if open_: o.append("".join(f'<path d="M{xx} {-30 - (xx - 200) * 0.1:.1f} l 3 6 l 3 -6" stroke="#F3EFE6" stroke-width="2" fill="none"></path>' for xx in range(210, 296, 12)))
    else: o.append("".join(f'<path d="M{xx} -8 l 3 -6 l 3 6" stroke="#F3EFE6" stroke-width="1.6" fill="none"></path>' for xx in range(212, 296, 12)))
    o.append('<ellipse cx="190" cy="-40" rx="12" ry="8" fill="#5A6A44" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="192" cy="-42" r="3.4" fill="#E8B830"></circle>'
             '<ellipse cx="292" cy="-28" rx="6" ry="4" fill="#5A6A44" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append("".join(f'<path d="M{xx} {-40 + abs(xx - 60) * 0.02:.1f} l 6 -10 l 6 10 Z" fill="#3A4A2A" stroke="#0D0D0F" stroke-width="1.2"></path>' for xx in range(-200, 180, 16)))
    o.append('<path d="M-200 -14 C -100 -20 0 -24 160 -22" stroke="#6A7A54" stroke-width="2" fill="none"></path>')
    o.append('</g>')
    return "".join(o)

def lotus_river(w, h, seed, mouth=False, flood=False):
    """He lieth under the lotus-trees, in the covert of the reed, and the fen; though a Jordan swell even to his mouth: the
    river-horse half in the water under the lotus-trees and willows, reeds all about; flood=True: the river high and brown."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), hills(w, h, h * 0.72, seed, "#6A8A4A", amp=8, step=90), ground(w, h, h * 0.78, "#7A8A4A", dy=0)]
    for i, x in enumerate((0.12, 0.78, 0.92)):
        o.append(f'<path d="M{f(w * x)} {f(h * 0.84)} C {f(w * x - 6)} {f(h * 0.76)} {f(w * x + 6)} {f(h * 0.7)} {f(w * x)} {f(h * 0.64)}" stroke="#5A4A2A" stroke-width="8" fill="none"></path>'
                 f'<ellipse cx="{f(w * x)}" cy="{f(h * 0.62)}" rx="{f(w * 0.08)}" ry="{f(h * 0.06)}" fill="{["#3A6A3A", "#5A8A4A", "#4A7A3A"][i]}" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    wy = h * (0.84 if not flood else 0.8)
    o.append(f'<rect x="-10" y="{f(wy)}" width="{f(w + 20)}" height="{f(h)}" fill="{"#3A7A8A" if not flood else "#8A6A4A"}"></rect>'
             f'<path d="M-10 {f(wy)} L {f(w + 10)} {f(wy)}" stroke="#E8F6FA" stroke-width="2"></path>')
    k = min(0.9, h / 420)
    hx, hy = w * 0.4, wy + 40 * k
    o.append(hippo(hx, hy, k, mouth=mouth))
    o.append(f'<rect x="-10" y="{f(wy + 26 * k)}" width="{f(w + 20)}" height="{f(h)}" fill="{"#3A7A8A" if not flood else "#8A6A4A"}" opacity="0.85"></rect>')
    for i in range(30):
        x = r.uniform(0, w); y = wy + r.uniform(-4, 20)
        if abs(x - hx - 30 * k) < 150 * k: continue
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + r.uniform(-4, 4))} {f(y - r.uniform(30, 60))}" stroke="#4A7A3A" stroke-width="2.4"></path>')
    for i in range(5):
        x = r.uniform(0, w); y = wy + r.uniform(8, 30)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="14" ry="4" fill="#4A8A4A" stroke="#0D0D0F" stroke-width="1"></ellipse><circle cx="{f(x + 4)}" cy="{f(y - 4)}" r="5" fill="#F3B8C8" stroke="#0D0D0F" stroke-width="1"></circle>')
    return "".join(o)

def hippo_grazing(w, h, seed):
    """Behold now, behemoth, which I made as well as thee; he eateth grass as an ox; his strength is in his loins: the
    river-horse come up on the bank to graze, the mountains behind, the beasts of the field at play far off."""
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), hills(w, h, h * 0.74, seed, "#7A8A6A", amp=16, step=70), ground(w, h, h * 0.82, "#8AAA4A", dy=0),
         f'<rect x="-10" y="{f(h * 0.94)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#3A7A8A"></rect>']
    k = min(0.9, h / 420)
    o.append(hippo(w * 0.36, h * 0.96, k) + E.sheep(w * 0.8, h * 0.84, 0.3) + E.sheep(w * 0.86, h * 0.85, 0.28) + N.ass(w * 0.92, h * 0.86, min(0.2, h / 1500)))
    return "".join(o)

def hook_cord(w, h, seed):
    """Canst thou draw out leviathan with a fishhook? or put a rope into his nose? canst thou fill his skin with barbed
    irons?: a fishhook and cord, a rope and fish-spears lying on the bank, useless, and the crocodile's eyes and snout in the
    water beyond."""
    o = [K2.sky(w, h, "#8FB8C8", "#E8E0C8"), f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#3A6A6A"></rect>',
         P(f"M-10 {f(h * 0.88)} C {f(w * 0.2)} {f(h * 0.84)} {f(w * 0.4)} {f(h * 0.9)} {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z", "#A88A5A")]
    k = min(1.2, h / 300)
    o.append(croc(w * 0.62, h * 0.82, min(0.5, h / 700), swim=True) + f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#3A6A6A" opacity="0.8"></rect>'
             + P(f"M-10 {f(h * 0.88)} C {f(w * 0.2)} {f(h * 0.84)} {f(w * 0.4)} {f(h * 0.9)} {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z", "#A88A5A"))
    o.append(f'<g transform="translate({f(w * 0.12)} {f(h * 0.93)}) scale({f(k)})"><path d="M0 0 C 40 -10 60 10 90 -4" stroke="#C8A878" stroke-width="2" fill="none"></path>'
             '<path d="M90 -4 L 100 -6 L 104 6 C 104 14 94 16 92 10" stroke="#8A8A9A" stroke-width="3" fill="none"></path></g>'
             f'<path d="M{f(w * 0.06)} {f(h * 0.98)} L {f(w * 0.36)} {f(h * 0.9)} M{f(w * 0.08)} {f(h * 1.0)} L {f(w * 0.4)} {f(h * 0.94)}" stroke="#5A3A1E" stroke-width="3"></path>')
    return "".join(o)

def croc_bank(w, h, seed, open_=True):
    """None is so fierce that he dare stir him up; who can open the doors of his face? round about his teeth is terror: the
    crocodile lying full length on a mud bank, its jaws open in the sun."""
    o = [K2.sky(w, h, "#C8B890", "#F3E0B0"), f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#4A6A5A"></rect>',
         P(f"M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.7)} {f(h * 0.86)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#8A7A5A")]
    o.append(croc(w * 0.42, h * 0.96, min(w / 560, h / 300), open_=open_))
    return "".join(o)

def scales(w, h, seed):
    """His strong scales are his pride, shut up together as with a close seal; one is so near to another that no air can come
    between them: the crocodile's back seen close, row on row of raised plates."""
    o = [rect(w, h, "#2A3A2A")]
    rows = 5; y0 = h * 0.7
    for rr in range(rows):
        y = y0 + rr * (h * 0.3) / rows
        n = 14
        for i in range(n):
            x = (i + (rr % 2) * 0.5) * w / (n - 1) - 20
            o.append(P(f"M{f(x)} {f(y + h * 0.06)} L {f(x + w / n * 0.5)} {f(y)} L {f(x + w / n)} {f(y + h * 0.06)} Z", ["#4A5A3A", "#566A44", "#3E4E30"][(i + rr) % 3], 1.6))
            o.append(f'<path d="M{f(x + w / n * 0.5)} {f(y + 4)} L {f(x + w / n * 0.5)} {f(y + h * 0.05)}" stroke="#2A3A20" stroke-width="1.4"></path>')
    return "".join(o)

def croc_dawn(w, h, seed):
    """His sneezings flash forth light, and his eyes are like the eyelids of the morning; out of his nostrils a smoke goeth:
    the crocodile lying in the river at sunrise, the spray of his breath lit gold by the low sun, his eyes catching the light."""
    o = [K2.sky(w, h, "#3A3A6A", "#FFB07A"), sun(w * 0.8, h * 0.82, min(30, h * 0.08), color="#FFD23F", op=0.4),
         f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#5A4A5A"></rect>',
         f'<path d="M{f(w * 0.5)} {f(h * 0.85)} L {f(w * 0.98)} {f(h * 0.85)}" stroke="#FFD890" stroke-width="3" opacity="0.7"></path>']
    k = min(0.6, h / 520)
    o.append(croc(w * 0.3, h * 0.86, k, swim=True) + f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#5A4A5A" opacity="0.85"></rect>')
    sx, sy = w * 0.3 + 292 * k, h * 0.86 - 30 * k
    o.append(smoke(sx, sy, 7, seed, color="#FFE6B0", op=0.55, k=min(1.2, h / 360)))
    o.append(f'<circle cx="{f(w * 0.3 + 192 * k)}" cy="{f(h * 0.86 - 42 * k)}" r="{f(6 * k + 3)}" fill="#FFD23F" opacity="0.8"></circle>')
    return "".join(o)

def broken_weapons(w, h, seed):
    """If one lay at him with the sword it cannot avail, nor the spear, the dart, nor the pointed shaft; he counteth iron as
    straw: a sword, spears, arrows and sling-stones lying scattered and broken on the mud of the bank, the river empty."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A8A9A", "#D8C8A8"), f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#4A6A5A"></rect>',
         P(f"M-10 {f(h * 0.88)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.7)} {f(h * 0.86)} {f(w + 10)} {f(h * 0.88)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#7A6A4A")]
    for i in range(9):
        x = w * r.uniform(0.05, 0.9); y = h * r.uniform(0.9, 0.99); a = r.uniform(-20, 20); L = r.uniform(40, 90)
        o.append(f'<g transform="translate({f(x)} {f(y)}) rotate({a:.0f})"><path d="M0 0 L {f(L)} 0" stroke="#5A3A1E" stroke-width="3"></path>'
                 + (f'<path d="M{f(L)} -4 L {f(L + 12)} 0 L {f(L)} 4 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1"></path>' if i % 2 else f'<path d="M{f(L * 0.6)} -3 L {f(L * 0.62)} 3" stroke="#0D0D0F" stroke-width="2"></path>') + '</g>')
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.96)} L {f(w * 0.82)} {f(h * 0.92)}" stroke="#0D0D0F" stroke-width="7"></path><path d="M{f(w * 0.6)} {f(h * 0.96)} L {f(w * 0.82)} {f(h * 0.92)}" stroke="#A8A8B8" stroke-width="4"></path>')
    for i in range(6):
        o.append(f'<circle cx="{f(w * r.uniform(0.1, 0.9))}" cy="{f(h * r.uniform(0.92, 0.99))}" r="4" fill="#A89A8A" stroke="#0D0D0F" stroke-width="1"></circle>')
    return "".join(o)

def shining_wake(w, h, seed):
    """He maketh the deep to boil like a pot; he maketh a path to shine after him; one would think the deep to be hoary: the
    open sea, a long white wake shining behind the crocodile as it swims out."""
    o = [K2.sky(w, h, "#5A8AB8", "#C8E0F0"), f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#1F5A7A"></rect>']
    k = min(0.5, h / 640)
    hx, hy = w * 0.62, h * 0.86
    o.append(f'<path d="M{f(hx)} {f(hy)} C {f(w * 0.4)} {f(h * 0.88)} {f(w * 0.2)} {f(h * 0.84)} -10 {f(h * 0.9)} L -10 {f(h * 0.96)} C {f(w * 0.2)} {f(h * 0.9)} {f(w * 0.4)} {f(h * 0.94)} {f(hx)} {f(hy + 8)} Z" fill="#E8F6FA" opacity="0.85"></path>')
    o.append(croc(hx - 290 * k, hy, k, swim=True) + f'<rect x="-10" y="{f(hy)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#1F5A7A" opacity="0.7"></rect>')
    r = random.Random(seed)
    for i in range(16):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(0.8, 1.0))}" r="{f(r.uniform(2, 5))}" fill="none" stroke="#E8F6FA" stroke-width="1.2"></circle>')
    return "".join(o)

def repent(p, w, h, seed):
    """Wherefore I abhor myself, and repent in dust and ashes: Job fallen upon his face on the ash heap, the whirlwind gone
    and the sky clearing over him."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A6A9A", "#F3D8B0"), clouds(w, h * 0.2, seed, 6, color="#8A8AA8", op=0.6, ry=0.05, h=h),
         V.rays(w * 0.5, h * 0.0, 24, 20, h * 1.2, color="#FFF4C2", op=0.15), ground(w, h, h * 0.86, "#8A7A62", dy=0), ash_mound(w * 0.5, h * 0.99, w * 0.5, h * 0.1, seed)]
    s = min(1.0, h / 300)
    o.append(N.prostrate(w * 0.42, h * 0.95, s, color=SACK, skin="#3A1E14"))
    return "".join(o)

def friends_offering(p, w, h, seed):
    """Take unto you seven bullocks and seven rams, and go to my servant Job, and offer up for yourselves a burnt-offering;
    and my servant Job shall pray for you: the altar smoking, the beasts brought up in a line, the three friends standing by
    with bowed heads, and Job with his hands lifted up."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB8D8", "#F3E0B0"), ground(w, h, h * 0.84, "#B8A07A", dy=0),
         smoke(w * 0.5, h * 0.82, 9, seed, color="#E8E2D6", op=0.5, k=min(1.4, h / 300)), S4.altar(w * 0.5, h * 0.95, min(0.9, h / 420), fire=True, seed=seed)]
    k = min(0.36, h / 1000)
    for i in range(7): o.append(S1.cow(w * (0.04 + i * 0.045), h * (0.93 + (i % 2) * 0.02), k * 0.7, color=["#8A5A30", "#5A3A22", "#A87A4A"][i % 3]))
    for i in range(7): o.append(E.sheep(w * (0.06 + i * 0.045), h * 0.99, 0.32 * min(1.0, h / 300)))
    s = fit(h * 0.97, h * 0.74)
    for i, who in enumerate(("eli", "bil", "zop")):
        o.append(friend_fig(p, w * (0.66 + i * 0.07), h * 0.97, s * 0.95, who, flip=True))
    o.append(job_fig(p, w * 0.9, h * 0.97, s, flip=True, up=[(22, -158), (40, -190), (52, -224)], ash=True))
    return "".join(o)

def kin_feast(p, w, h, seed):
    """Then came there unto him all his brethren and all his sisters, and did eat bread with him in his house; every man also
    gave him a piece of money, and every one a ring of gold: Job's house open, the table set, his kin about it, a man setting
    a ring of gold on the table before him."""
    o = [feast_house(p, w, h, seed)]
    b = h * 0.9; s = fit(b, max(h * 0.36, b - 200)) * 0.9
    ty = b - 200 * s * 0.42
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(ty - 6)}" r="7" fill="none" stroke="#FFD23F" stroke-width="3"></circle>'
             f'<circle cx="{f(w * 0.56)}" cy="{f(ty - 4)}" r="4" fill="#D8D8E0" stroke="#0D0D0F" stroke-width="1"></circle><circle cx="{f(w * 0.6)}" cy="{f(ty - 4)}" r="4" fill="#D8D8E0" stroke="#0D0D0F" stroke-width="1"></circle>')
    return "".join(o)

def tally_board(w, h, seed=0):
    """Fourteen thousand sheep, six thousand camels, a thousand yoke of oxen, and a thousand she-asses: the latter end of
    Job as a tally board."""
    from chr1.art import tally
    return tally(w, h, [("SHEEP", "14,000", "#E8E2D6"), ("CAMELS", "6,000", "#E8B880"), ("YOKE OF OXEN", "1,000", "#C8905A"), ("SHE-ASSES", "1,000", "#A8A8B8")],
                 "THE LATTER END OF JOB · JOB 42:12")

def daughters(p, w, h, seed):
    """In all the land were no women found so fair as the daughters of Job: Jemimah, Keziah and Keren-happuch in fine robes
    and gold, their names written beneath them, the seven brothers behind."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB8D8", "#F3E8C8"), ground(w, h, h * 0.84, "#C8B07A", dy=0)]
    s = fit(h * 0.88, h * 0.7)
    for i in range(7): o.append(man(p, w * (0.1 + i * 0.13), h * 0.86, s * 0.85, ["#7A2A3A", "#2C4A7A", "#5A6A2A", "#7A5A2A", "#3A5A6A", "#6A3A5A", "#4A3A2A"][i]))
    s2 = fit(h * 0.95, h * 0.72)
    for i, (nm, c) in enumerate((("JEMIMAH", "#E8E2F6"), ("KEZIAH", "#C8506A"), ("KEREN-HAPPUCH", "#8A5AB8"))):
        x = w * (0.28 + i * 0.22)
        o.append(mk.person(p, round(x), round(h * 0.95), s2, body=SKIN, cloth=c, woman=True, hair="#1A1210", sw=3, extra='<path d="M-12 -178 C -4 -184 4 -184 12 -178" stroke="#E8B830" stroke-width="3" fill="none"></path>')
                 + f'<rect x="{f(x - 52)}" y="{f(h * 0.955)}" width="104" height="16" fill="#12113A"></rect>' + label(x, h * 0.955 + 12, nm, "#FFD23F", 9))
    return "".join(o)

def generations(p, w, h, seed):
    """Job lived a hundred and forty years, and saw his sons, and his sons' sons, even four generations: Job very old in white
    at his tent door, and before him four rows, his sons, their sons, and their children, the youngest smallest."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A06A", "#F3D8A0"), ground(w, h, h * 0.8, "#C8B07A", dy=0), A.black_tent(w * 0.02, h * 0.9, w * 0.22, h * 0.14, color="#3A2A22")]
    s = fit(h * 0.97, h * 0.72)
    o.append(mk.person(p, round(w * 0.2), round(h * 0.97), s, body=SKIN, cloth=JOB_C, sw=3, extra=A.headcloth("#F3EFE6", cord=None) + BAND + A.WHITE_BEARD + '<path d="M30 -170 L 34 6" stroke="#5A3A22" stroke-width="5"></path>'))
    cl = ["#7A2A3A", "#2C4A7A", "#5A6A2A", "#7A5A2A", "#3A5A6A", "#6A3A5A", "#C8506A", "#D8A040"]
    for g in range(3):
        n = 4 + g * 2; k = s * (0.9 - g * 0.18); y = h * (0.88 + g * 0.045)
        for i in range(n):
            x = w * (0.36 + i * (0.6 / n)) + g * 6
            o.append(man(p, x, y, k, cl[(i + g) % 8], flip=True))
    return "".join(o)

def full_of_days(w, h, seed):
    """So Job died, being old and full of days: the tent at sunset, empty, the flocks settling for the night."""
    o = [K2.sky(w, h, "#3A2A4A", "#FF9A5A"), sun(w * 0.76, h * 0.84, min(34, h * 0.09), color="#FF8A3D", op=0.35),
         hills(w, h, h * 0.86, seed, "#4A3A3A", amp=8, step=90), ground(w, h, h * 0.9, "#6A5A3A", dy=0),
         A.black_tent(w * 0.14, h * 0.94, w * 0.24, h * 0.14, color="#2A1E1A"), flock(w * 0.46, w * 0.7, h * 0.92, h * 0.98, 9, seed, cows=0, smin=0.12, smax=0.16)]
    return "".join(o)
