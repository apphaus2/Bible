"""Drawings for Job 32–37 (Elihu): Elihu young in green before the four seated men, the wine-skins ready to burst, the sick
man on his bed and the pit with the light over it, then the gathering storm of 36–37 — rain, lightning, snow, ice, and the
golden splendor out of the north."""
from job.art9 import *
from job.art9 import f, K2, K3, sea, label, SHIELD

def elihu_scene(p, w, h, seed, speaking=True, night=False):
    """Elihu the son of Barachel, young, standing in green before Job on the ash heap and the three friends sitting on the
    ground; speaking=True: his hand stretched out."""
    b = h * 0.97
    sk = (K2.sky(w, h, "#1A1A3A", "#5A4A6A") + mk.stars(30, w, h * 0.5, seed)) if night else K2.sky(w, h, "#7A7A8A", "#E8D8B8")
    o = [mk.defs(p, *ALL), sk, J.city_hill(w * 0.12, h * 0.72, w * 0.2, h * 0.1, seed), ground(w, h, h * 0.74, "#8A7A62" if not night else "#4A4248", dy=0),
         ash_mound(w * 0.68, b, w * 0.36, h * 0.09, seed)]
    s = min(1.0, (h * 0.2) / 140)
    o.append(seated(w * 0.7, b - h * 0.07, s, SACK, head=SACK, ash=True, flip=True))
    o.append(seated_friend(w * 0.08, b, s * 0.85, "eli", bowed=False) + seated_friend(w * 0.2, b + 2, s * 0.85, "bil", bowed=False) + seated_friend(w * 0.9, b - 2, s * 0.8, "zop", flip=True, bowed=False))
    fs = fit(b, max(h * 0.68, b - 230))
    o.append(friend_fig(p, w * 0.42, b, fs, "elihu", up=[(-22, -158), (-50, -170), (-76, -190)] if speaking else None))
    return "".join(o)

def wineskins(w, h, seed):
    """My breast is as wine which hath no vent; like new wine-skins it is ready to burst: new goatskin bottles hanging from a
    beam, swollen tight, one straining at its seams."""
    o = [rect(w, h, "#4A3428"), f'<path d="M-10 {f(h * 0.6)} L {f(w + 10)} {f(h * 0.6)}" stroke="#2A1A10" stroke-width="10"></path>', ground(w, h, h * 0.96, "#2A1E18", dy=0)]
    k = min(1.4, h / 260)
    for i, x in enumerate((0.24, 0.5, 0.76)):
        cx = w * x; sw = 1.0 + 0.18 * (i == 1)
        o.append(f'<path d="M{f(cx)} {f(h * 0.6)} L {f(cx)} {f(h * 0.66)}" stroke="#8A6A3A" stroke-width="3"></path>'
                 f'<g transform="translate({f(cx)} {f(h * 0.66)}) scale({f(k * sw)} {f(k)})">' + P("M-6 0 L 6 0 L 10 8 C 44 12 52 50 40 70 C 30 86 -30 86 -40 70 C -52 50 -44 12 -10 8 Z", "#8A5A30", 2.2)
                 + '<path d="M-30 30 C -20 26 -10 30 0 26 M10 50 C 20 46 30 52 36 46" stroke="#5A3A1E" stroke-width="1.4" fill="none"></path></g>')
        if i == 1:
            o.append("".join(f'<path d="M{f(cx + 40 * k * sw)} {f(h * 0.66 + (40 + j * 8) * k)} l {f(10 + j * 4)} {f(-4 + j * 3)}" stroke="#F3EFE6" stroke-width="2"></path>' for j in range(3)))
    return "".join(o)

def sick_bed(w, h, seed):
    """He is chastened also with pain upon his bed; his soul draweth near unto the pit: a sick man under his covering on a
    low bed in a dim room, a lamp burning low, untouched bread beside him."""
    from genesis.art4 import clay_lamp
    o = [rect(w, h, "#2A2430"), f'<circle cx="{f(w * 0.84)}" cy="{f(h * 0.76)}" r="{f(h * 0.2)}" fill="#FFC14D" opacity="0.12"></circle>',
         K1.bed(w, h, w * 0.1, w * 0.62, h * 0.98, cover="#4A4A5A", head="#B8957E", hair="#6A645E"), clay_lamp(w * 0.84, h * 0.8, min(1.2, h / 260)),
         f'<ellipse cx="{f(w * 0.72)}" cy="{f(h * 0.95)}" rx="18" ry="6" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>']
    return "".join(o)

def pit_light(w, h, seed, rising=False):
    """He keepeth back his soul from the pit; he hath redeemed my soul from going into the pit, and my life shall behold the
    light: the mouth of a deep pit seen from within, the light of day falling down into it; rising=True: a rope let down."""
    o = [rect(w, h, "#0B0806")]
    cx = w * 0.5
    o.append(f'<path d="M{f(cx - w * 0.2)} -10 L {f(cx + w * 0.2)} -10 L {f(cx + w * 0.34)} {f(h + 10)} L {f(cx - w * 0.34)} {f(h + 10)} Z" fill="#FFF4C2" opacity="0.18"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(h * 0.06)}" rx="{f(w * 0.2)}" ry="{f(h * 0.05)}" fill="#C8E0F0" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             + V.rays(cx, h * 0.06, 16, 10, h, color="#FFF4C2", op=0.15))
    o.append(f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.1)} {f(h * 0.5)} {f(w * 0.06)} {f(h * 0.8)} {f(w * 0.12)} {f(h + 10)} M{f(w + 10)} {f(h * 0.3)} C {f(w * 0.9)} {f(h * 0.5)} {f(w * 0.94)} {f(h * 0.8)} {f(w * 0.88)} {f(h + 10)}" stroke="#2A2018" stroke-width="3" fill="none"></path>')
    if rising: o.append(f'<path d="M{f(cx + 10)} {f(h * 0.06)} C {f(cx + 4)} {f(h * 0.4)} {f(cx + 14)} {f(h * 0.7)} {f(cx + 6)} {f(h * 0.98)}" stroke="#C8A878" stroke-width="3" fill="none"></path>')
    return "".join(o)

def midnight_palace(w, h, seed):
    """In a moment they die, even at midnight; the people are shaken, and the mighty are taken away without hand: a palace
    on its hill at midnight, every window dark, a crown left upon the empty steps."""
    o = [K2.sky(w, h, "#05051A", "#1A1A3A"), mk.stars(80, w, h * 0.7, seed), J.moon(w * 0.16, h * 0.62, min(14, h * 0.04)),
         P(f"M-10 {f(h + 10)} L -10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.7)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} Z", "#1A1A22")]
    px, pw, ph = w * 0.3, w * 0.4, h * 0.2
    o.append(P(f"M{f(px)} {f(h * 0.86)} L {f(px)} {f(h * 0.86 - ph)} L {f(px + pw)} {f(h * 0.86 - ph)} L {f(px + pw)} {f(h * 0.86)} Z", "#2A2A36"))
    for i in range(6):
        o.append(f'<rect x="{f(px + pw * (0.08 + i * 0.15))}" y="{f(h * 0.86 - ph * 0.7)}" width="{f(pw * 0.06)}" height="{f(ph * 0.3)}" fill="#0B0B12" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    for i in range(4):
        o.append(f'<rect x="{f(px + pw * 0.3 - i * 8)}" y="{f(h * 0.86 + i * h * 0.02)}" width="{f(pw * 0.4 + i * 16)}" height="{f(h * 0.02)}" fill="#3A3A44" stroke="#0D0D0F" stroke-width="1"></rect>')
    o.append(f'<g transform="translate({f(px + pw * 0.5)} {f(h * 0.92)}) scale({f(min(1.0, h / 300))})">' + P("M-14 0 L -14 -14 L -7 -6 L 0 -18 L 7 -6 L 14 -14 L 14 0 Z", "#B8962A", 1.6) + '</g>')
    return "".join(o)

def night_singer(p, w, h, seed):
    """Where is God my Maker, who giveth songs in the night?: a shepherd sitting by a small fire under the stars with a harp,
    his flock lying about him."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#05051A", "#1E1650"), mk.stars(120, w, h * 0.8, seed), hills(w, h, h * 0.84, seed, "#0B0B1A", amp=10, step=80),
         ground(w, h, h * 0.9, "#14141E", dy=0), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.94)}" r="{f(h * 0.14)}" fill="#FF8A3D" opacity="0.15"></circle>',
         E.blaze(w * 0.5, h * 0.97, w * 0.05, h * 0.07, seed, n=4)]
    k = min(0.8, h * 0.18 / 140)
    o.append(seated(w * 0.38, h * 0.97, k, "#5A4A3A", head="#3A3A4A", beard="#2A1A10") + S2.harp(w * 0.42, h * 0.9, min(0.5, h / 600)))
    o.append(flock(w * 0.6, w * 0.92, h * 0.92, h * 0.98, 7, seed, cows=0, smin=0.12, smax=0.16))
    return "".join(o)

def storm_cattle(p, w, h, seed):
    """The noise thereof telleth concerning him, the cattle also concerning the storm that cometh up: cattle standing with
    their heads turned toward a wall of storm cloud climbing over the hills, the first lightning in it."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A4A", "#C8B890"), f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.5)} {f(h * 0.2)} {f(w * 0.7)} {f(h * 0.4)} C {f(w * 0.8)} {f(h * 0.3)} {f(w)} {f(h * 0.2)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.82)} Z" fill="#1A1A2A" opacity="0.9"></path>',
         f'<path d="M{f(w * 0.6)} {f(h * 0.5)} l -14 {f(h * 0.12)} l 16 0 l -20 {f(h * 0.16)}" stroke="#FFF4C2" stroke-width="3" fill="none"></path>',
         hills(w, h, h * 0.82, seed, "#4A5A3A", amp=8, step=90), ground(w, h, h * 0.88, "#6A8A4A", dy=0)]
    k = min(0.5, h / 700)
    for i in range(4): o.append(S1.cow(w * (0.1 + i * 0.2), h * (0.97 - (i % 2) * 0.02), k * (1 - 0.08 * (i % 2)), color=["#8A5A30", "#C9A27A", "#5A3A22", "#A87A4A"][i]))
    return "".join(o)

def lightning_world(w, h, seed):
    """He sendeth it forth under the whole heaven, and his lightning unto the ends of the earth; after it a voice roareth:
    the curve of the earth under a sky full of lightning from edge to edge."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#05051A", "#3A2A5A"), f'<path d="M-10 {f(h * 0.9)} Q {f(w * 0.5)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A1A2A" stroke="#5A8AB8" stroke-width="2"></path>']
    for i in range(6):
        x = w * (0.06 + i * 0.18); y = r.uniform(0, h * 0.3); pts = [(x, y)]
        while pts[-1][1] < h * 0.84:
            pts.append((pts[-1][0] + r.uniform(-30, 30), pts[-1][1] + r.uniform(18, 34)))
        d = "M" + " L ".join(f"{f(a)} {f(b)}" for a, b in pts)
        o.append(f'<path d="{d}" stroke="#FFF4C2" stroke-width="8" fill="none" opacity="0.25"></path><path d="{d}" stroke="#FFFFFF" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def snow_land(p, w, h, seed):
    """He saith to the snow, Fall thou on the earth; he sealeth up the hand of every man: snow falling thick on the hills and
    on a village, every door shut, no one abroad."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A9AB0", "#D8E0E8"), hills(w, h, h * 0.8, seed, "#F3F6FA", amp=10, step=80), ground(w, h, h * 0.88, "#E8EEF4", dy=0)]
    for i in range(4):
        x = w * (0.1 + i * 0.2)
        o.append(house(x, h * 0.96, w * 0.12, h * 0.1, color="#B8A890") + f'<path d="M{f(x - 6)} {f(h * 0.86 - 8)} L {f(x + w * 0.12 + 6)} {f(h * 0.86 - 8)}" stroke="#FFFFFF" stroke-width="6"></path>')
    for i in range(180):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h))}" r="{f(r.uniform(1, 2.6))}" fill="#FFFFFF" opacity="0.9"></circle>')
    return "".join(o)

def den(w, h, seed):
    """Then the beasts go into coverts, and remain in their dens: a lion lying in the mouth of its den in the rocks while the
    storm passes outside."""
    o = [K2.sky(w, h, "#3A3A4A", "#8A8A9A"), P(f"M-10 {f(h + 10)} L -10 {f(h * 0.6)} L {f(w * 0.5)} {f(h * 0.66)} L {f(w * 0.7)} {f(h + 10)} Z", "#6A5A4A"),
         P(f"M{f(w * 0.12)} {f(h * 0.98)} C {f(w * 0.12)} {f(h * 0.76)} {f(w * 0.44)} {f(h * 0.74)} {f(w * 0.46)} {f(h * 0.98)} Z", "#120A08"),
         J2.lion(w * 0.2, h * 0.98, min(0.36, h / 900), roar=False)]
    r = random.Random(seed)
    for i in range(60):
        x = r.uniform(w * 0.5, w + 30); y = r.uniform(0, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -8 20" stroke="#C8D0E0" stroke-width="1.3" opacity="0.6"></path>')
    return "".join(o)

def ice(w, h, seed):
    """By the breath of God ice is given, and the breadth of the waters is straitened: a river frozen between its banks, the
    cold wind out of the north streaming over it."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A6A8A", "#C8D8E8"), hills(w, h, h * 0.78, seed, "#E8EEF4", amp=10, step=80), ground(w, h, h * 0.84, "#D8E0E8", dy=0),
         P(f"M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.94)} {f(w + 10)} {f(h * 0.88)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#B8D8E8")]
    for i in range(14):
        x = r.uniform(0, w); y = h * r.uniform(0.92, 1.0)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-30, 30))} {f(r.uniform(-4, 4))} l {f(r.uniform(-20, 20))} {f(r.uniform(-3, 3))}" stroke="#FFFFFF" stroke-width="1.6" fill="none"></path>')
    for i in range(10):
        y = h * (0.3 + i * 0.05)
        o.append(f'<path d="M{f(w + 10)} {f(y)} C {f(w * 0.7)} {f(y - 10)} {f(w * 0.4)} {f(y + 10)} {f(-10)} {f(y)}" stroke="#FFFFFF" stroke-width="1.6" opacity="0.4" fill="none"></path>')
    return "".join(o)

def golden_north(w, h, seed):
    """Out of the north cometh golden splendor; the wind passeth, and cleareth them: the storm clouds driven off southward, a
    great golden light breaking over the hills of the north (no one is drawn in it)."""
    o = [K2.sky(w, h, "#2A2A5A", "#FFD890"), V.rays(w * 0.5, h * 0.86, 40, 30, max(w, h) * 1.2, color="#FFE680", op=0.35),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.86)}" rx="{f(w * 0.3)}" ry="{f(h * 0.12)}" fill="#FFF4C2" opacity="0.7"></ellipse>',
         clouds(w, h * 0.1, seed, 8, color="#3A3A5A", op=0.8, ry=0.06, h=h), hills(w, h, h * 0.86, seed, "#4A3A3A", amp=12, step=70)]
    return "".join(o)

def mirror_sky(w, h, seed):
    """Canst thou with him spread out the sky, which is strong as a molten mirror?: a hard, bright, cloudless sky over a
    burning plain, the sun white in it, the heat shimmering."""
    o = [K2.sky(w, h, "#C8D8E0", "#F3F0E0"), sun(w * 0.5, h * 0.2, min(30, h * 0.08), color="#FFFFFF", glow="#FFF4C2", op=0.4),
         ground(w, h, h * 0.86, "#D8B87A", dy=0)]
    for i in range(5):
        y = h * (0.88 + i * 0.025)
        o.append(f'<path d="M-10 {f(y)} q 30 -6 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0" stroke="#F3E8C8" stroke-width="1.6" fill="none" opacity="0.6"></path>')
    return "".join(o)
