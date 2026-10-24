"""Drawings for Matthew 8–10: the healings and the twelve. The leper touched; the centurion in the street of Capernaum;
Peter's house; the evening at the door; the boat in the tempest and the great calm; the tombs of the Gadarenes (the two men
drawn as men, the demons never drawn) and the swine running down the steep; the bed carried and carried home; the place of
toll; the publicans at meat; the wine-skins; the flute-players at the ruler's door and the damsel raised; the border of
his garment; the two blind men; the harvest and the sheep without a shepherd; the twelve with their names; the sending
forth. Built on mat.art2 (which carries mat.art)."""
from mat.art2 import *
from mat.art2 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, soldier_fig, wolf
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from genesis.art2 import dove as _dove
import exodus as E

LIE = ("LieB", "LieA")

def jesus_lying(p, x, y, s, flip=False):
    """Jesus asleep, lying on his side (the lying figure in his robe, his hair dark at the head); (x, y) under his middle."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})" fill="{JESUS_TUNIC}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use>'
            f'<use href="#{p}LieA" fill="{JESUS_MANTLE}"></use>'
            f'<circle cx="-180" cy="-14" r="12.5" fill="{JESUS_SKIN}"></circle>'
            f'<path d="M-192 -16 C -194 -30 -176 -32 -168 -24 C -172 -22 -176 -20 -178 -14 C -182 -6 -186 0 -190 2 C -196 -4 -194 -10 -192 -16 Z" fill="{JESUS_HAIR}"></path></g>')

def centurion_fig(p, x, y, s, flip=False, up=None):
    """The centurion: a red cloak over his armour, a helmet with a transverse crest."""
    helm = ('<path d="M-14 -190 C -14 -206 14 -206 14 -190 L 14 -180 L -14 -180 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-20 -204 L 20 -204" stroke="#B5121B" stroke-width="7" stroke-linecap="round"></path>'
            '<path d="M-24 -150 L 24 -150 L 22 -110 L -22 -110 Z" fill="#9A8A6A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-26 -164 C -40 -120 -36 -60 -30 -20 L -18 -20 C -22 -70 -20 -120 -14 -160 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#7A1A14", kind="Tunic", sw=3, flip=flip, up=up, extra=helm)

def kneeler(x, y, s, color, flip=False, skin=SKIN):
    return E.kneel(x, y, s, color=color, flip=flip, skin=skin)

def road_scene(p, w, h, seed, tone="day"):
    """A road at the foot of the hills, the lake beyond (a backdrop)."""
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#4A2A5A", "#FFB07A"), "noon": ("#5AB0D8", "#FFF4C2")}[tone]
    return "".join([mk.defs(p, *ALL, *LIE), sky(w, h, top, bot), hills(w, h, h * 0.36, seed, color="#8A9A7A" if tone != "dusk" else "#5A4A5A", amp=14, step=90),
                    lake(w, h, h * 0.42, seed, n=6), hills(w, h, h * 0.5, seed + 1, color="#9AAA6A" if tone != "dusk" else "#6A5A4A", amp=8, step=70),
                    ground(w, h, h * 0.6, "#C8B07A" if tone != "dusk" else "#8A6A4A", dy=0)])

def leper(p, w, h, seed):
    """There came to him a leper and worshipped him: on the road below the mountain the leper kneeling, his garment torn
    and his head bare, Jesus' hand stretched out to touch him; the multitudes behind."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.3, b - 230))
    o.append(crowd(p, w * 0.62, w * 0.98, b - 30 * s, b - 30 * s - 150 * s, 7, seed, flip=True))
    o.append(jesus(p, w * 0.48, b, s, flip=True, up=UP_TOUCH))
    o.append(kneeler(w * 0.3, b, s * 0.9, "#C8BCB0", skin="#D8CCC4"))
    return "".join(o)

def centurion(p, w, h, seed, healed=False):
    """A centurion beseeching him in the street of Capernaum: the soldier before Jesus, the white houses about them, the
    disciples behind (healed=True: the centurion's house, the servant standing in the doorway)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.84, seed, hmin=0.34, hmax=0.52), pavement(w, h, h * 0.84)]
    s = fit(b, max(h * 0.24, b - 240))
    if healed:
        o.append(man(p, w * 0.7, h * 0.84, s * 0.7, "#C8B898"))
        o.append(centurion_fig(p, w * 0.32, b, s))
    else:
        o.append(centurion_fig(p, w * 0.62, b, s, flip=True, up=UP_BLESS))
        o.append(jesus(p, w * 0.36, b, s))
        o.append(disciple(p, w * 0.2, b, s * 0.96, "peter") + disciple(p, w * 0.1, b, s * 0.94, "john"))
    return "".join(o)

def fever(p, w, h, seed):
    """In Peter's house: his wife's mother risen from her bed, serving, a jug in her hands; Jesus seated, the lamp lit."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.08, w * 0.08)), A.lamp(w * 0.86, h * 0.36, max(0.7, h / 300)),
         f'<rect x="{f(w * 0.56)}" y="{f(b - h * 0.08)}" width="{f(w * 0.3)}" height="{f(h * 0.08)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.2, b - 240))
    jug = '<path d="M-26 -126 C -34 -110 -30 -96 -22 -94 L -10 -94 C -2 -96 2 -110 -6 -126 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.8"></path>'
    o.append(woman_fig(p, w * 0.42, b, s * 0.92, "#6A4A5A", "#8A6A7A", flip=True, up=[(-22, -158), (-30, -130), (-18, -120)], extra=jug))
    o.append(jesus_seated(w * 0.22, b, s * 0.82))
    o.append(disciple(p, w * 0.7, b, s, "peter", flip=True))
    return "".join(o)

def at_even(p, w, h, seed):
    """When even was come they brought unto him many: the door of the house at sunset, the street full, the sick on their
    beds and leaning on staves, Jesus in the doorway."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#4A2A5A", "#FF8A4A"), sun(w * 0.9, h * 0.5, 16, color="#FFC14D", op=0.3),
         f'<rect x="{f(w * 0.02)}" y="{f(h * 0.2)}" width="{f(w * 0.3)}" height="{f(h * 0.66)}" fill="#C8A878" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.12)}" y="{f(h * 0.44)}" width="{f(w * 0.1)}" height="{f(h * 0.42)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>',
         houses(w, h, h * 0.86, seed, x0=w * 0.34, hmin=0.3, hmax=0.44, lit=True), ground(w, h, h * 0.86, "#6A4A3A", dy=0)]
    s = fit(b, max(h * 0.24, b - 240))
    o.append(jesus(p, w * 0.17, b, s))
    o.append(crowd(p, w * 0.36, w * 0.96, b - 24 * s, b - 24 * s - 160 * s, 7, seed, flip=True))
    o.append(f'<g transform="translate({f(w * 0.54)} {f(b - 4)}) scale({f(s * 0.7)})" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>'
             f'<rect x="{f(w * 0.54 - 196 * s * 0.7)}" y="{f(b - 4)}" width="{f(240 * s * 0.7)}" height="{f(10 * s)}" fill="#C8B088" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def foxes(p, w, h, seed):
    """The foxes have holes, and the birds of the heaven have nests: a fox at its earth under the rocks at dusk, birds
    settling on their nests in a tree, and the open road."""
    b = h * 0.9
    o = [sky(w, h, "#4A2A5A", "#FFB07A"), hills(w, h, h * 0.5, seed, color="#6A4A4A", amp=12, step=80), ground(w, h, h * 0.62, "#8A6A4A", dy=0),
         f'<path d="M{f(w * 0.02)} {f(b)} C {f(w * 0.04)} {f(h * 0.6)} {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.36)} {f(b)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></path>',
         f'<ellipse cx="{f(w * 0.2)}" cy="{f(b - h * 0.08)}" rx="{f(w * 0.05)}" ry="{f(h * 0.06)}" fill="#1A1210"></ellipse>']
    k = max(0.5, h / 260)
    o.append(f'<g transform="translate({f(w * 0.3)} {f(b)}) scale({f(k * 0.5)})"><path d="M-50 -30 C -50 -46 -20 -50 10 -48 L 30 -50 L 40 -74 L 48 -58 L 58 -72 L 60 -52 L 82 -42 L 60 -36 L 36 -30 L 34 0 L 26 0 L 24 -26 L -24 -26 L -28 0 L -36 0 Z" fill="#C8682E" stroke="#0D0D0F" stroke-width="3"></path>'
             '<path d="M-48 -36 C -80 -40 -100 -20 -96 -4 C -80 -14 -66 -22 -50 -26 Z" fill="#C8682E" stroke="#0D0D0F" stroke-width="3"></path><path d="M-92 -8 l 8 -6" stroke="#F3EFE6" stroke-width="5"></path></g>')
    o.append(tree(w * 0.8, b, k * 0.9, color="#3A5A2A", kind="round", seed=seed))
    for i in range(3):
        x, y = w * (0.74 + 0.06 * i), b - k * (110 + 14 * (i % 2))
        o.append(f'<path d="M{f(x - 12)} {f(y)} C {f(x - 10)} {f(y + 8)} {f(x + 10)} {f(y + 8)} {f(x + 12)} {f(y)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4"></path>' + bird(x, y - 4, 0.8))
    o.append(f'<path d="M{f(w * 0.4)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.56)} {f(h * 0.7)} {f(w * 0.62)} {f(h * 0.62)}" stroke="#B89A7A" stroke-width="{f(max(6, h * 0.04))}" fill="none"></path>')
    return "".join(o)

def tempest(p, w, h, seed, calm=False, awake=False):
    """A great tempest in the sea, the boat covered with the waves, the disciples clinging, Jesus asleep in the stern;
    awake=True: Jesus standing in the boat, his arm out over the waves; calm=True: the sea flat and shining, the boat at
    rest, the men looking at him."""
    b = h * 0.78
    if calm:
        o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#5AB0D8", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#7A8A9A", amp=10, step=90), lake(w, h, h * 0.46, seed, n=10, op=0.5)]
        s = min(1.0, (b - h * 0.2) / 140)
        o.append(boat(p, w * 0.5, b, s, crew=[(-70, ROBES["peter"]), (-30, ROBES["andrew"]), (24, "jesus"), (66, ROBES["john"])], mast=True))
        return "".join(o)
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#14141E", "#3A3A5E"), bolt(w * 0.8, 0, h * 0.4, seed), rain(w, h, seed, n=60)]
    from mat.art import boat as _boat
    s = min(1.1, (b - h * 0.18) / 150)
    if awake:
        crew = [(-70, ("up", ROBES["peter"])), (-30, ROBES["andrew"]), (30, "jesus"), (70, ROBES["john"])]
        o.append(_boat(p, w * 0.48, b, s, crew=crew, mast=True, tilt=-6))
        o.append(f'<path d="M{f(w * 0.48 + 30 * s - 10 * s)} {f(b - 90 * s)} L {f(w * 0.48 + 30 * s - 70 * s)} {f(b - 100 * s)}" stroke="{JESUS_SKIN}" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>')
    else:
        lie = jesus_lying(p, 60, -26, 0.36, flip=True)
        crew = [(-74, ("up", ROBES["peter"])), (-40, ROBES["andrew"]), (-6, ("up", ROBES["james"]))]
        o.append(f'<g transform="translate({f(w * 0.48)} {f(b)}) rotate(-12) scale({f(s)})">{lie}</g>')
        o.append(_boat(p, w * 0.48, b, s, crew=crew, mast=True, tilt=-12))
    o.append(waves(w, h, b - h * 0.06, seed))
    return "".join(o)

def waves(w, h, y, seed, amp=None):
    """A storm sea from y down: high crests, foam."""
    r = random.Random(seed); amp = amp or max(8, (h - y) * 0.18)
    o = []
    for k in range(4):
        yy = y + (h - y) * k / 4; a = amp * (0.7 + k * 0.25); n = 7
        d = f"M-10 {f(yy + a)}"
        for i in range(n + 1):
            x1 = -10 + (w + 20) * (i + 0.5) / n; x2 = -10 + (w + 20) * (i + 1) / n
            d += f" Q {f(x1)} {f(yy - a * r.uniform(0.6, 1.3))} {f(x2)} {f(yy + a)}"
        d += f" L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z"
        o.append(f'<path d="{d}" fill="{["#1E4E70", "#184462", "#123A56", "#0C2E48"][k]}" stroke="{INK}" stroke-width="2"></path>')
        for i in range(n):
            x = -10 + (w + 20) * (i + 0.5) / n
            o.append(f'<path d="M{f(x - 14)} {f(yy - a * 0.5)} q 10 -8 22 -2" stroke="#CFEFFF" stroke-width="2.4" fill="none" opacity="0.85"></path>')
    return "".join(o)

def road_two(p, w, h, seed, cloth="#5A4A6A", tone="day"):
    """Jesus and one man face to face on the road by the lake, the disciples behind."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed, tone)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.3, b, s))
    o.append(man(p, w * 0.52, b, s * 0.96, cloth, flip=True, up=UP_BLESS))
    o.append(disciple(p, w * 0.12, b, s * 0.94, "peter") + disciple(p, w * 0.76, b, s * 0.94, "andrew", flip=True) + disciple(p, w * 0.86, b, s * 0.92, "john", flip=True))
    return "".join(o)

def marvel(p, w, h, seed):
    """The dumb man spake, and the multitudes marvelled: on the road, the healed man with his arms lifted, the people about
    him amazed, Jesus beside, and at the edge two Pharisees in white turning away."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.36, w * 0.74, b - 20 * s, b - 20 * s - 150 * s, 6, seed, flip=True, up=UP_HIGH))
    o.append(jesus(p, w * 0.16, b, s))
    o.append(man(p, w * 0.32, b, s * 0.96, "#6A5A3A", flip=True, up=[(-22, -158), (-30, -190), (-24, -222)]))
    o.append(scribe_fig(p, w * 0.82, b, s * 0.94, white=True) + scribe_fig(p, w * 0.92, b, s * 0.92))
    return "".join(o)

def dust_gate(p, w, h, seed):
    """Shake off the dust of your feet: two of the twelve walking out of a town gate onto the open road, a puff of dust
    beaten from their sandals, the gate behind them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8A890", "#F3E8C8"), walls(w * 0.5, w + 10, h * 0.7, h * 0.4, seed, towers=2), ground(w, h, h * 0.7, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(disciple(p, w * 0.32, b, s, "thomas") + disciple(p, w * 0.2, b, s * 0.98, "matthew"))
    r = random.Random(seed)
    for _ in range(14):
        o.append(f'<circle cx="{f(w * 0.38 + r.uniform(0, w * 0.1))}" cy="{f(b - r.uniform(0, 30 * s))}" r="{f(r.uniform(3, 9) * s)}" fill="#D8C8A0" opacity="0.7"></circle>')
    return "".join(o)

def tombs(p, w, h, seed, men=True, jesus_=True, swine=False):
    """The country of the Gadarenes: a steep rocky hillside over the lake, tombs cut in the rock; two men coming out of the
    tombs, their garments torn, no one else on the way (drawn as men; the demons are never drawn)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#6A6A8A", "#E8C8A0"), lake(w, h, h * 0.5, seed, n=6),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.36)} {f(h * 0.3)} C {f(w * 0.5)} {f(h * 0.16)} {f(w * 0.8)} {f(h * 0.14)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>']
    r = random.Random(seed)
    for i in range(5):
        x = w * (0.46 + 0.1 * i); y = h * (0.4 + 0.08 * (i % 2))
        o.append(f'<path d="M{f(x - 16)} {f(y + 24)} L {f(x - 16)} {f(y)} Q {f(x)} {f(y - 14)} {f(x + 16)} {f(y)} L {f(x + 16)} {f(y + 24)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>'
                 f'<circle cx="{f(x + 24)}" cy="{f(y + 16)}" r="9" fill="#9A8A7A" stroke="{INK}" stroke-width="1.6"></circle>')
    o.append(shore(w, h, h * 0.86, x0=-10, x1=w * 0.4))
    s = fit(b, max(h * 0.3, b - 230))
    if swine:
        for i in range(8):
            o.append(creature("swine", w * (0.66 + 0.04 * i), h * (0.2 + 0.012 * (i % 3)), max(0.3, h / 900), color="#C89080"))
    if men:
        torn = '<path d="M-14 -60 L -8 -40 L -2 -62 L 6 -38 L 12 -60" stroke="#0D0D0F" stroke-width="2" fill="none"></path>'
        o.append(man(p, w * 0.56, h * 0.74, s * 0.6, "#6A6058", flip=True, extra=torn) + man(p, w * 0.64, h * 0.76, s * 0.62, "#5A5048", flip=True, extra=torn))
    if jesus_:
        o.append(boat(p, w * 0.12, h * 0.86, s * 0.6, mast=False))
        o.append(jesus(p, w * 0.3, b, s * 0.9))
    return "".join(o)

def swine_steep(p, w, h, seed):
    """The whole herd rushed down the steep into the sea: the swine pouring down the cliff into the water, the keepers
    running off up the hill toward the city."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#6A6A8A", "#E8C8A0"), lake(w, h, h * 0.62, seed, n=8),
         f'<path d="M-10 {f(h * 0.22)} L {f(w * 0.3)} {f(h * 0.26)} C {f(w * 0.44)} {f(h * 0.4)} {f(w * 0.5)} {f(h * 0.56)} {f(w * 0.56)} {f(h * 0.7)} L {f(w * 0.56)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A5A" stroke="{INK}" stroke-width="2.4"></path>']
    k = max(0.6, h / 260)
    for i in range(14):
        t = i / 13; x = w * (0.08 + 0.48 * t) + r.uniform(-12, 12); y = h * (0.26 + 0.44 * t * t) + r.uniform(-6, 6)
        o.append(f'<g transform="rotate({f(20 + 30 * t)} {f(x)} {f(y)})">' + creature("swine", x, y, k * 0.8, color="#C89080") + '</g>')
    for i in range(4):
        x = w * (0.62 + 0.08 * i); y = h * 0.66 + r.uniform(-8, 8)
        o.append(f'<path d="M{f(x - 20)} {f(y)} q 10 -10 20 0 t 20 0" stroke="#F3EFE6" stroke-width="3" fill="none"></path>')
    s = fit(h * 0.3, h * 0.12)
    o.append(man(p, w * 0.08, h * 0.25, s * 0.8, "#6A5A3A", flip=True) + man(p, w * 0.16, h * 0.255, s * 0.78, "#5A4A3A", flip=True))
    return "".join(o)

def city_gate(p, w, h, seed, crowd_n=9):
    """All the city came out to meet Jesus: the gate of a walled town, the people pouring out toward him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), walls(w * 0.4, w + 10, h * 0.66, h * 0.36, seed, towers=3), ground(w, h, h * 0.66, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.4, w * 0.96, b, b - 170 * s, crowd_n, seed, flip=True))
    o.append(jesus(p, w * 0.14, b, s))
    return "".join(o)

def bed_carried(p, w, h, seed, rise=False):
    """They brought to him a man sick of the palsy, lying on a bed: four men setting the bed down before Jesus in the
    street; rise=True: the man walking away with his bed on his shoulder, the multitudes amazed."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.8, seed, hmin=0.3, hmax=0.46), pavement(w, h, h * 0.8)]
    s = fit(b, max(h * 0.24, b - 230))
    if rise:
        mat_ = '<rect x="-34" y="-200" width="70" height="14" rx="4" fill="#C8B088" stroke="#0D0D0F" stroke-width="2" transform="rotate(-10)"></rect>'
        o.append(man(p, w * 0.66, b, s, "#C8B898", up=[(-22, -158), (-26, -184), (-12, -196)], extra=mat_))
        o.append(crowd(p, w * 0.06, w * 0.4, b, b - 160 * s, 5, seed, up=UP_HIGH))
        return "".join(o)
    bx, by = w * 0.56, b - 40 * s
    o.append(f'<rect x="{f(bx - 110 * s)}" y="{f(by)}" width="{f(220 * s)}" height="{f(14 * s)}" fill="#C8B088" stroke="{INK}" stroke-width="2"></rect>'
             f'<g transform="translate({f(bx + 80 * s)} {f(by + 2)}) scale({f(s * 0.86)})" fill="#C8B898" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    for dx in (-130, 130):
        o.append(man(p, bx + dx * s, b, s * 0.9, random.Random(seed + dx).choice(HEB), flip=dx > 0))
    o.append(jesus(p, w * 0.16, b, s))
    return "".join(o)

def toll(p, w, h, seed):
    """Matthew sitting at the place of toll: a booth by the road at the lake side, a table with the coins and the tablets,
    Matthew seated at it, Jesus passing by, his hand out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A7A", amp=12, step=90), lake(w, h, h * 0.46, seed, n=6),
         ground(w, h, h * 0.64, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    bx = w * 0.62
    o.append(f'<path d="M{f(bx - 100 * s)} {f(b - 200 * s)} L {f(bx + 120 * s)} {f(b - 200 * s)} L {f(bx + 130 * s)} {f(b - 180 * s)} L {f(bx - 110 * s)} {f(b - 180 * s)} Z" fill="#B5121B" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(bx - 96 * s)} {f(b - 182 * s)} L {f(bx - 96 * s)} {f(b)} M{f(bx + 116 * s)} {f(b - 182 * s)} L {f(bx + 116 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>')
    o.append(seated(bx + 30 * s, b, s * 0.9, ROBES["matthew"], head=ROBES["matthew"], beard="#1A1210", flip=True, band=True))
    o.append(f'<rect x="{f(bx - 70 * s)}" y="{f(b - 70 * s)}" width="{f(90 * s)}" height="{f(70 * s)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(6):
        o.append(f'<circle cx="{f(bx - 60 * s + i * 13 * s)}" cy="{f(b - 74 * s)}" r="{f(5 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></circle>')
    o.append(jesus(p, w * 0.24, b, s, up=UP_CALL))
    o.append(disciple(p, w * 0.1, b, s * 0.96, "peter"))
    return "".join(o)

def at_meat(p, w, h, seed, pharisees=False):
    """He sat at meat in the house: a low table spread with bread and cups, the guests reclining on cushions about it,
    publicans and sinners with Jesus and his disciples; pharisees=True: two Pharisees in white looking in at the door."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#8A6A4A", floor="#5A4A3A"), A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300))]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(b - 40 * s)}" width="{f(w * 0.6)}" height="{f(16 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(6):
        o.append(loaf(w * (0.24 + i * 0.1), b - 46 * s, s * 0.8))
    r = random.Random(seed)
    o.append(jesus_seated(w * 0.44, b, s * 0.8))
    for i, x in enumerate((0.16, 0.28, 0.6, 0.72, 0.84)):
        c = r.choice(HEB + TWELVE)
        o.append(seated(w * x, b, s * 0.8, c, head=r.choice([None, c, "#E8E2D6"]), beard=r.choice(["#2A1A10", "#6A645E", ""]), flip=x > 0.5))
    if pharisees:
        o.append(f'<rect x="{f(w * 0.9)}" y="{f(b - 230 * s)}" width="{f(w * 0.1 + 10)}" height="{f(230 * s)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>')
        o.append(scribe_fig(p, w * 0.95, b, s * 0.9, white=True, flip=True))
    return "".join(o)

def wineskins(p, w, h, seed):
    """New wine into old wine-skins: an old skin burst and the red wine running out on the floor; beside it new skins full
    and whole; an old garment with a new patch torn away."""
    b = h * 0.9
    o = [bgr(w, h, "#E8D8B8"), f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#A8885A" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.6, h / 240)
    def skin(x, y, burst=False, c="#8A5A30"):
        o_ = (f'<path d="M{f(x - 40 * k)} {f(y)} C {f(x - 60 * k)} {f(y - 60 * k)} {f(x - 20 * k)} {f(y - 100 * k)} {f(x)} {f(y - 96 * k)} L {f(x + 6 * k)} {f(y - 116 * k)} L {f(x + 18 * k)} {f(y - 112 * k)} '
              f'L {f(x + 14 * k)} {f(y - 92 * k)} C {f(x + 40 * k)} {f(y - 80 * k)} {f(x + 54 * k)} {f(y - 30 * k)} {f(x + 40 * k)} {f(y)} Z" fill="{c}" stroke="{INK}" stroke-width="2.4"></path>')
        if burst:
            o_ += (f'<path d="M{f(x + 10 * k)} {f(y - 60 * k)} L {f(x + 24 * k)} {f(y - 50 * k)} L {f(x + 14 * k)} {f(y - 40 * k)} L {f(x + 28 * k)} {f(y - 30 * k)}" stroke="{INK}" stroke-width="3" fill="none"></path>'
                   f'<path d="M{f(x + 26 * k)} {f(y - 34 * k)} C {f(x + 50 * k)} {f(y - 20 * k)} {f(x + 60 * k)} {f(y)} {f(x + 120 * k)} {f(y + 6)} L {f(x + 30 * k)} {f(y + 8)} Z" fill="#7A0A1A" stroke="{INK}" stroke-width="1.6"></path>')
        return o_
    o.append(skin(w * 0.18, b, burst=True, c="#6A4A30"))
    o.append(skin(w * 0.56, b, c="#A8743A") + skin(w * 0.7, b, c="#A8743A"))
    gx = w * 0.88
    o.append(f'<path d="M{f(gx - 30 * k)} {f(b)} L {f(gx - 26 * k)} {f(b - 90 * k)} L {f(gx + 26 * k)} {f(b - 90 * k)} L {f(gx + 30 * k)} {f(b)} Z" fill="#8A8070" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(gx - 10 * k)} {f(b - 60 * k)} L {f(gx + 14 * k)} {f(b - 62 * k)} L {f(gx + 12 * k)} {f(b - 36 * k)} L {f(gx - 8 * k)} {f(b - 40 * k)} Z" fill="#E8E2D6" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(gx - 12 * k)} {f(b - 36 * k)} L {f(gx - 18 * k)} {f(b - 20 * k)} L {f(gx - 6 * k)} {f(b - 24 * k)}" stroke="{INK}" stroke-width="2" fill="none"></path>')
    return "".join(o)

def ruler_house(p, w, h, seed, raised=False):
    """The ruler's house: outside, the flute-players and the crowd making a tumult; raised=True: within, the damsel sitting
    up on her bed, Jesus holding her hand, her father and mother by the door."""
    b = h * 0.92
    if raised:
        o = [mk.defs(p, *ALL), room(w, h, b, wall="#C8A878", window=(w * 0.08, w * 0.1)), glow(w * 0.5, b - h * 0.3, h * 0.5, "#FFF4C2", 0.5, f"{p}g")]
        s = fit(b, max(h * 0.2, b - 240))
        o.append(f'<rect x="{f(w * 0.4)}" y="{f(b - 46 * s)}" width="{f(w * 0.3)}" height="{f(20 * s)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>')
        o.append(seated(w * 0.56, b - 40 * s, s * 0.6, "#F3EFE6", head="#2A1A10", beard="", flip=True))
        o.append(jesus(p, w * 0.36, b, s, up=UP_TOUCH))
        o.append(man(p, w * 0.84, b, s * 0.96, "#2A5A5A", flip=True, kind="Robe", extra=A.headcloth("#2A5A5A", cord="#3A2214") + A.BLACK_BEARD)
                 + woman_fig(p, w * 0.92, b, s * 0.9, "#6A3A5A", flip=True))
        return "".join(o)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.82, seed, hmin=0.4, hmax=0.56, stairs=False), pavement(w, h, h * 0.82)]
    s = fit(b, max(h * 0.24, b - 230))
    pipe = '<path d="M16 -168 L 50 -150" stroke="#C8963E" stroke-width="5"></path>'
    for i in range(3):
        o.append(man(p, w * (0.44 + 0.08 * i), b - 6 * i, s * 0.92, ["#5A4A6A", "#6A5A3A", "#3A4A5A"][i], up=[(22, -158), (30, -156), (36, -154)], extra=pipe))
    o.append(crowd(p, w * 0.68, w * 0.98, b, b - 160 * s, 5, seed, flip=True, up=UP_HIGH))
    o.append(jesus(p, w * 0.14, b, s, up=UP_BLESS))
    return "".join(o)

def border(p, w, h, seed):
    """She came behind him and touched the border of his garment: the press of the crowd on the road, a woman stooping at
    his back, her hand on the tassel of his robe; Jesus turning."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.5, w * 0.98, b - 20 * s, b - 20 * s - 160 * s, 8, seed, flip=True))
    o.append(jesus(p, w * 0.38, b, s, flip=True))
    o.append(f'<path d="M{f(w * 0.38 + 18 * s)} {f(b - 20 * s)} l {f(4 * s)} {f(14 * s)}" stroke="#2A5A8A" stroke-width="{f(3 * s)}"></path>')
    o.append(E.kneel(w * 0.52, b, s * 0.8, color="#6A5A7A", flip=True, skin=SKIN))
    o.append(disciple(p, w * 0.18, b, s * 0.96, "peter") + disciple(p, w * 0.08, b, s * 0.94, "james"))
    return "".join(o)

def blind_two(p, w, h, seed, healed=False):
    """Two blind men followed him, crying out: two men in grey, one leading the other by the shoulder, staves in their
    hands; healed=True: in the house, the two standing straight, their staves laid down, Jesus touching their eyes."""
    b = h * 0.94
    if healed:
        o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.84, w * 0.08)), glow(w * 0.5, b - h * 0.4, h * 0.5, "#FFF4C2", 0.5, f"{p}g")]
    else:
        o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.24, b - 230))
    staff = '<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'
    if healed:
        o.append(jesus(p, w * 0.34, b, s, up=UP_BLESS))
        o.append(man(p, w * 0.54, b, s * 0.96, "#7A7A80", flip=True) + man(p, w * 0.66, b, s * 0.94, "#6A6A72", flip=True))
        o.append(f'<path d="M{f(w * 0.8)} {f(b)} L {f(w * 0.9)} {f(b - 6)} M{f(w * 0.78)} {f(b - 4)} L {f(w * 0.92)} {f(b - 2)}" stroke="#5A3A22" stroke-width="5"></path>')
    else:
        o.append(jesus(p, w * 0.2, b, s))
        o.append(disciple(p, w * 0.32, b, s * 0.96, "john"))
        o.append(man(p, w * 0.62, b, s * 0.94, "#7A7A80", flip=True, up=UP_BLESS) + man(p, w * 0.74, b, s * 0.92, "#6A6A72", flip=True, extra=staff))
    return "".join(o)

def harvest(p, w, h, seed):
    """The harvest indeed is plenteous, but the laborers are few: wide fields of ripe grain under the evening sky, two
    reapers far off with their sickles; on the hill, the scattered sheep with no shepherd."""
    o = [sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.82, h * 0.42, 16, color="#FFE680", op=0.3), hills(w, h, h * 0.44, seed, color="#8A7A5A", amp=10, step=80),
         ground(w, h, h * 0.5, "#D8B060", dy=0), grain(-10, w + 10, h * 0.7, h * 0.14, seed), grain(-10, w + 10, h * 1.0, h * 0.22, seed + 1)]
    o.append(sheep_row(w * 0.06, w * 0.5, h * 0.46, 6, seed, s=max(0.2, h / 1100)))
    return "".join(o)

def twelve_named(p, w, h, seed):
    """The names of the twelve apostles: the twelve standing in a row, each in his colour, his name beneath him, as the
    verses give them in pairs."""
    b = h * 0.74
    names = ["SIMON PETER", "ANDREW", "JAMES", "JOHN", "PHILIP", "BARTHOLOMEW", "THOMAS", "MATTHEW", "JAMES", "THADDÆUS", "SIMON", "JUDAS ISCARIOT"]
    cols = [ROBES["peter"], ROBES["andrew"], ROBES["james"], ROBES["john"], "#4A6A4A", "#7A5A2A", ROBES["thomas"], ROBES["matthew"], "#5A5A7A", "#6A3A3A", "#3A5A5A", ROBES["judas"]]
    o = [mk.defs(p, *ALL), grid_bg(w, h)]
    s = min(fit(b, max(h * 0.12, b - 230)) * 0.9, w * 0.8 / 12 / 62)
    for i, (nm, c) in enumerate(zip(names, cols)):
        x = w * (0.05 + 0.75 * i / 11)
        o.append(mk.person(p, round(x), round(b), round(s, 3), body="#B98A6E", cloth=c, kind="Robe", sw=3))
        o.append(f'<path d="M{f(x)} {f(b + 4)} L {f(x)} {f(b + 10 + (i % 2) * 14)}" stroke="#4A7A9A" stroke-width="1.4"></path>')
        o.append(label(x, b + 20 + (i % 2) * 14, nm, "#FFD23F" if i < 4 else "#8FD0E2", 8.5))
    return "".join(o)

def sent_forth(p, w, h, seed):
    """These twelve Jesus sent forth: from the hill-top the roads going out to the villages of Galilee, the twelve two and
    two along them without wallet or staff, Jesus standing at the crossing."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#8A9A7A", amp=14, step=90)]
    for i, x in enumerate((0.14, 0.42, 0.74, 0.94)):
        o.append(hill_town(w * x, h * 0.42, w * 0.12, h * 0.1, seed + i, hill="#9AAA7A"))
    o.append(ground(w, h, h * 0.44, "#B8B07A", dy=0))
    for ex in (0.1, 0.4, 0.72, 0.96):
        o.append(f'<path d="M{f(w * 0.5)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * ex)} {f(h * 0.56)} {f(w * ex)} {f(h * 0.44)}" stroke="#D8C8A0" stroke-width="{f(max(5, h * 0.03))}" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 220))
    for i, (x, y) in enumerate(((0.18, 0.62), (0.36, 0.6), (0.66, 0.6), (0.84, 0.62))):
        for j in range(2):
            yy = h * y; ss = fit(yy, yy - h * 0.12)
            o.append(mk.person(p, round(w * x + j * 14), round(yy), round(ss, 3), body="#B98A6E", cloth=TWELVE[(i * 2 + j) % 12], kind="Robe", sw=3))
    o.append(jesus(p, w * 0.5, b, s * 0.9))
    return "".join(o)

def sheep_wolves(p, w, h, seed):
    """As sheep in the midst of wolves: the flock in the pasture at evening, wolves circling in the dark at its edge; a
    serpent in the grass and a dove on the fold's wall."""
    from snake import snake
    b = h * 0.92
    o = [sky(w, h, "#2A1A3A", "#C8682E"), hills(w, h, h * 0.5, seed, color="#3A2A3A", amp=10, step=80), ground(w, h, h * 0.6, "#4A4A3A", dy=0)]
    k = max(0.5, h / 260)
    o.append(sheep_row(w * 0.3, w * 0.7, b, 6, seed, s=k * 0.6))
    o.append(wolf(w * 0.1, b - h * 0.1, k * 0.5) + wolf(w * 0.9, b - h * 0.12, k * 0.5, flip=True))
    o.append(snake([(w * 0.3, h * 0.98), (w * 0.36, h * 0.95), (w * 0.42, h * 0.99), (w * 0.48, h * 0.96)], 4 * k, f"{p}sn", 0.6))
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(h * 0.56)}" width="{f(w * 0.3)}" height="{f(h * 0.06)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>' + _dove(w * 0.74, h * 0.56, k * 0.6, wings="down"))
    return "".join(o)

def housetops(p, w, h, seed):
    """What ye hear in the ear, proclaim upon the house-tops: dawn over the flat roofs of a town, a man standing on a roof
    with his arm raised, crying out."""
    b = h * 0.6
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A7A", "#FFC890"), sun(w * 0.8, h * 0.5, 18, color="#FFE680", op=0.4),
         houses(w, h, h + 10, seed, hmin=0.3, hmax=0.42, stairs=True)]
    s = fit(h * 0.6, h * 0.36) * 0.8
    o.append(man(p, w * 0.36, h * 0.62, s, "#5A4A6A", up=UP_HIGH))
    return "".join(o)

def sparrows(p, w, h, seed):
    """Are not two sparrows sold for a penny?: two small birds on the edge of a market basket, a copper coin beside it; one
    fallen sparrow on the ground — and the Father's care is told in the words."""
    b = h * 0.86
    o = [bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.8, h / 160)
    bx = w * 0.4
    o.append(f'<path d="M{f(bx - 80 * k)} {f(b - 50 * k)} L {f(bx + 80 * k)} {f(b - 50 * k)} L {f(bx + 64 * k)} {f(b)} L {f(bx - 64 * k)} {f(b)} Z" fill="#C8A060" stroke="{INK}" stroke-width="2.4"></path>')
    for i in range(5):
        o.append(f'<path d="M{f(bx - 76 * k + i * 4 * k)} {f(b - 40 * k + i * 9 * k)} L {f(bx + 76 * k - i * 4 * k)} {f(b - 40 * k + i * 9 * k)}" stroke="#8A6A3A" stroke-width="1.6"></path>')
    def sparrow(x, y, s, flip=False):
        sx = -s if flip else s
        return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-14 0 C -16 -12 -6 -18 4 -16 C 10 -22 18 -20 20 -14 L 26 -12 L 20 -10 C 18 -2 8 2 -2 2 L -22 6 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.4"></path>'
                '<path d="M-6 -10 C 0 -6 6 -6 10 -10" stroke="#3A2A1A" stroke-width="1.4" fill="none"></path><circle cx="15" cy="-15" r="1.4" fill="#0D0D0F"></circle>'
                '<path d="M0 2 L -2 8 M4 2 L 4 8" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
    o.append(sparrow(bx - 30 * k, b - 52 * k, k * 1.4) + sparrow(bx + 24 * k, b - 52 * k, k * 1.4, flip=True))
    o.append(f'<circle cx="{f(w * 0.72)}" cy="{f(b - 6 * k)}" r="{f(7 * k)}" fill="#C8783A" stroke="{INK}" stroke-width="1.6"></circle>')
    return "".join(o)

def cup_water(p, w, h, seed):
    """A cup of cold water only, given to one of these little ones: a hand holding out a clay cup to a child at a well."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#9AAA7A", amp=10, step=80), ground(w, h, h * 0.62, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    wx = w * 0.7
    o.append(f'<ellipse cx="{f(wx)}" cy="{f(b - 40 * s)}" rx="{f(60 * s)}" ry="{f(14 * s)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<path d="M{f(wx - 60 * s)} {f(b - 40 * s)} L {f(wx - 60 * s)} {f(b)} L {f(wx + 60 * s)} {f(b)} L {f(wx + 60 * s)} {f(b - 40 * s)}" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></path>')
    cup = '<path d="M-74 -132 L -54 -132 L -58 -116 L -70 -116 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man(p, w * 0.36, b, s, "#5A4A6A", up=[(-22, -158), (-44, -136), (-64, -124)], extra=cup, flip=False))
    o.append(mk.person(p, round(w * 0.22), round(b), round(s * 0.55, 3), body=SKIN, cloth="#C8783A", kind="Tunic", sw=3, flip=True, up=[(22, -158), (40, -170), (48, -186)]))
    return "".join(o)
