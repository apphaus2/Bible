"""Drawings for John 11–12. Bethany on the slope of the mount of Olives; Lazarus sick on his bed, his sisters by him; the
messenger setting out; the road back into Judæa; Martha going out to meet Jesus on the road; Mary fallen at his feet, the
mourners weeping behind; the tomb — a cave with a stone laid against it, Jesus weeping (his face, JESUS_GRIEF, in the
chapter), the stone taken away and the dark doorway, Jesus with his eyes lifted up; Lazarus come forth: a standing figure
wrapped in white grave-clothes, his face bound about with the napkin, in the tomb door — no decay drawn. The council of the
chief priests; Ephraim near the wilderness; the supper at Bethany — Martha serving, Lazarus at the table, Mary at Jesus'
feet with the pound of nard and her hair, the odour filling the house; the entry with the branches of the palm trees (the
young ass); the Greeks coming to Philip; the grain of wheat falling into the earth and its much fruit; the sky over the
temple court where the voice came out of heaven (the Voice box in the chapter, God never drawn); the light going down at
dusk on the road; Isaiah's scroll. Built on jhn.art5."""
from jhn.art5 import *
from jhn.art5 import f, INK, HEB, TWELVE, P, LIE, on_bed, lying, bedroll, blind_fig, fold
import random, math
from mat.art8 import jesus_riding
from ecc.art import loaf as _loaf

MARTHA_C, MARTHA_VEIL = "#8A6A2A", "#6A4A1A"                     # Martha: ochre robe, a dark-ochre veil (ntcast.ROBES["martha"])
MARYB_C, MARYB_VEIL = "#3A6A5A", "#2E5A42"                       # Mary of Bethany: a deep-green robe and veil

def martha_fig(p, x, y, s, flip=False, up=None, extra=""):
    return woman_fig(p, x, y, s, MARTHA_C, MARTHA_VEIL, flip=flip, up=up, extra=extra)

def maryb_fig(p, x, y, s, flip=False, up=None):
    return woman_fig(p, x, y, s, MARYB_C, MARYB_VEIL, flip=flip, up=up)

def lazarus_bound(p, x, y, s, flip=False):
    """Lazarus come forth, bound hand and foot with grave-clothes, his face bound about with a napkin: a standing figure
    all in white linen wrapped round with bands, no face showing, nothing of death drawn."""
    bands = "".join(f'<path d="M-26 {yy} C -10 {yy - 8} 10 {yy - 8} 26 {yy - 2}" stroke="#B8B0A0" stroke-width="2.4" fill="none"></path>' for yy in range(-150, -10, 18))
    nap = '<path d="M-14 -186 C -16 -204 14 -206 14 -186 L 16 -168 C 6 -162 -6 -162 -16 -168 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.8"></path><path d="M-14 -178 L 14 -176 M-12 -170 L 14 -168" stroke="#B8B0A0" stroke-width="1.6"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#E8E2D6", cloth="#F3EFE6", kind="Robe", sw=3, flip=flip, extra=bands + nap)

def bethany_village(w, h, seed, tone="day"):
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#3A2A5A", "#FF9A5A")}[tone]
    return (sky(w, h, top, bot) + hills(w, h, h * 0.4, seed, color="#8A8A6A" if tone == "day" else "#5A4A5A", amp=12, step=80)
            + hill_town(w * 0.7, h * 0.56, w * 0.4, h * 0.24, seed, hill="#8A7A5A", lit=tone == "dusk") + ground(w, h, h * 0.58, "#B8A06A", dy=0)
            + "".join(olive(w * x, h * 0.98, h / 360, seed=seed + int(x * 10)) for x in (0.06, 0.94)))

def sick_bed(p, w, h, seed):
    """A certain man was sick, Lazarus of Bethany: within the house the lamp lit, Lazarus lying on his bed, his sisters
    Martha and Mary sitting by him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, *LIE), room(w, h, b, wall="#B89A78", floor="#6A4A3A"), clay_lamp(w * 0.5, h * 0.22, min(1.2, max(0.6, h / 320)))]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(on_bed(p, w * 0.5, b - 30 * s, 260 * s, cloth="#C8B898", flip=False))
    o.append(seated(w * 0.16, b, s * 0.82, MARTHA_C, head=MARTHA_VEIL, beard=None) + seated(w * 0.84, b, s * 0.82, MARYB_C, head=MARYB_VEIL, beard=None, flip=True))
    return "".join(o)

def messenger(p, w, h, seed):
    """The sisters therefore sent unto him: from the door of the house at Bethany a messenger going out along the road
    east toward the Jordan, the sisters at the door."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bethany_village(w, h, seed),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.16)} {f(h * 0.66)} {f(-10)} {f(h * 0.62)}" stroke="#E0D0A8" stroke-width="{f(max(10, h * 0.07))}" fill="none"></path>']
    s = fit(b, max(h * 0.26, b - 230))
    o.append(man(p, w * 0.16, h * 0.74, fit(h * 0.74, h * 0.74 - 140 * s), "#7A6A4A", flip=True))
    o.append(martha_fig(p, w * 0.5, b, s, flip=True, up=UP_BLESS) + maryb_fig(p, w * 0.6, b - 4, s * 0.96, flip=True))
    return "".join(o)

def road_judaea(p, w, h, seed):
    """Let us go into Judæa again: the road climbing up out of the Jordan valley into the bare hills of Judæa, Jesus going
    first and the disciples following, Thomas among them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.3, seed, color="#C8A06A", amp=22, step=70), hills(w, h, h * 0.46, seed + 1, color="#B8905A", amp=16, step=90),
         ground(w, h, h * 0.6, "#D8B880", dy=0),
         f'<path d="M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.6)}" stroke="#E8D8B0" stroke-width="{f(max(10, h * 0.08))}" fill="none"></path>']
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.62, b - h * 0.08, s * 0.94))
    for i, who in enumerate(("peter", "thomas", "john", "andrew")):
        o.append(disciple(p, w * (0.46 - 0.12 * i), b - h * (0.06 - 0.02 * i), s * (0.94 - 0.01 * i), who))
    return "".join(o)

def martha_road(p, w, h, seed):
    """Martha went and met him: on the road below Bethany, Martha come out to Jesus, her hands held out; the village
    behind, Mary sitting still in the house."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bethany_village(w, h, seed)]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.26, b, s))
    o.append(martha_fig(p, w * 0.5, b, s * 0.96, up=UP_BLESS))
    o.append(disciple(p, w * 0.1, b - 4, s * 0.94, "peter") + disciple(p, w * 0.02, b - 6, s * 0.92, "thomas"))
    return "".join(o)

def mary_feet(p, w, h, seed):
    """Mary fell down at his feet: on the road Mary kneeling before Jesus weeping, the Jews who came with her standing
    behind, weeping too; Martha beside."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bethany_village(w, h, seed, tone="dusk")]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.24, b, s))
    o.append(kneeler(w * 0.4, b, s * 0.84, MARYB_C, flip=True))
    o.append(martha_fig(p, w * 0.56, b, s * 0.94, flip=True))
    o.append(crowd(p, w * 0.66, w * 0.98, b, b - 160 * s, 4, seed, flip=True))
    return "".join(o)

def tomb_cave(p, w, h, seed, stage="stone"):
    """Now it was a cave, and a stone lay against it: the rock face of the tomb at Bethany. stone: the great stone laid
    against the cave's mouth, Jesus standing before it, the sisters and the Jews behind. taken: the stone rolled aside, the
    doorway dark, Jesus with his eyes and his hand lifted up to heaven. forth: Lazarus standing in the tomb door bound in his
    grave-clothes, his face bound with the napkin, Jesus with his arm out — Loose him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A6A" if stage == "stone" else "#5A6A9A", "#E8B07A" if stage == "stone" else "#FFE6A0"),
         hills(w, h, h * 0.44, seed, color="#7A6A5A", amp=12, step=80),
         f'<path d="M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.54)} {f(h * 0.16)} C {f(w * 0.7)} {f(h * 0.06)} {f(w * 0.9)} {f(h * 0.1)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         ground(w, h, h * 0.8, "#7A6A4A", dy=0)]
    cx = w * 0.76; dt = h * 0.36; db = h * 0.8; dw = w * 0.1
    o.append(f'<path d="M{f(cx - dw)} {f(db)} L {f(cx - dw)} {f(dt + dw * 0.6)} Q {f(cx)} {f(dt - dw * 0.3)} {f(cx + dw)} {f(dt + dw * 0.6)} L {f(cx + dw)} {f(db)} Z" fill="#14100E" stroke="{INK}" stroke-width="2.4"></path>')
    s = fit(b, max(h * 0.26, b - 230)); r = random.Random(seed)
    if stage == "stone":
        o.append(f'<ellipse cx="{f(cx)}" cy="{f((dt + db) / 2 + 4)}" rx="{f(dw * 1.25)}" ry="{f((db - dt) * 0.56)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></ellipse>'
                 f'<path d="M{f(cx - dw * 0.8)} {f(dt + (db - dt) * 0.3)} q {f(dw * 0.6)} -10 {f(dw * 1.4)} 4" stroke="#8A7E70" stroke-width="2" fill="none"></path>')
        o.append(jesus(p, w * 0.44, b, s, flip=True))
        o.append(martha_fig(p, w * 0.3, b, s * 0.94, flip=True) + maryb_fig(p, w * 0.2, b - 4, s * 0.94, flip=True))
        o.append(crowd(p, w * 0.0, w * 0.14, b, b - 160 * s, 2, seed, flip=True))
    else:
        o.append(f'<ellipse cx="{f(cx - dw * 2.6)}" cy="{f(db - (db - dt) * 0.4)}" rx="{f(dw * 1.1)}" ry="{f((db - dt) * 0.42)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></ellipse>')
        if stage == "taken":
            o.append(rays(w * 0.3, -10, 24, 10, h, color="#FFF4C2", op=0.25, a0=40, a1=140))
            o.append(jesus(p, w * 0.3, b, s, flip=True, up=[(-22, -158), (-34, -190), (-38, -222)]))
        else:
            o.append(glow(cx, (dt + db) / 2, dw * 2.2, "#FFF4C2", 0.6, f"{p}g"))
            ls = fit(db, db - 0.92 * (db - dt))
            o.append(lazarus_bound(p, cx, db, min(ls, s * 0.98), flip=True))
            o.append(jesus(p, w * 0.3, b, s, flip=True, up=UP_BLESS))
        o.append(martha_fig(p, w * 0.16, b, s * 0.94, flip=True) + maryb_fig(p, w * 0.06, b - 4, s * 0.94, flip=True))
    return "".join(o)

def ephraim(p, w, h, seed):
    """He departed thence into the country near to the wilderness, into a city called Ephraim: a small town on a ridge at
    the edge of the bare wilderness, Jesus and the disciples going up to it at evening."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#FFB07A"), hills(w, h, h * 0.4, seed, color="#B8905A", amp=22, step=70),
         hill_town(w * 0.66, h * 0.56, w * 0.36, h * 0.24, seed, hill="#9A7A5A"), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.4, b, s, flip=True))
    for i, who in enumerate(("peter", "john", "andrew")):
        o.append(disciple(p, w * (0.26 - 0.1 * i), b - 4 * (i % 2), s * (0.95 - 0.02 * i), who, flip=True))
    return "".join(o)

def supper_bethany(p, w, h, seed, stage="supper"):
    """They made him a supper there: within the house at Bethany the low table and the lamps; Martha serving with a dish;
    Lazarus sitting at meat with Jesus and the disciples, Judas among them. supper: the meal. anoint: Mary kneeling at
    Jesus' feet with the open cruse of nard, wiping his feet with her hair; the fragrance rising and filling the house."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#C8A878", floor="#7A5A40")]
    for x in (0.3, 0.7): o.append(clay_lamp(w * x, h * 0.2, min(1.1, max(0.5, h / 340))))
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(b - 40 * s)}" width="{f(w * 0.62)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(4): o.append(_loaf(w * (0.36 + 0.14 * i), b - 44 * s, s * 0.6) + cup(w * (0.42 + 0.14 * i), b - 40 * s, s * 0.12, color="#B5652E"))
    o.append(jesus_seated(w * 0.28, b, s * 0.86))
    o.append(seated(w * 0.5, b, s * 0.8, "#C8B898", head=None, beard="#2A1A10", flip=True))                       # Lazarus
    o.append(seated(w * 0.66, b, s * 0.8, ROBES["peter"], head=None, beard="#4A4440", flip=True))
    o.append(seated(w * 0.82, b, s * 0.8, ROBES["judas"], head="#6A2A1A", beard="#1A1210", flip=True))         # Judas
    if stage == "supper":
        dish = '<ellipse cx="-56" cy="-150" rx="20" ry="6" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
        o.append(martha_fig(p, w * 0.1, b, s, flip=True, up=[(-22, -158), (-40, -150), (-56, -150)], extra=dish))
    else:
        o.append(martha_fig(p, w * 0.94, b, s * 0.98))
        o.append(kneeler(w * 0.12, b, s * 0.74, MARYB_C))
        o.append(f'<path d="M{f(w * 0.17)} {f(b - 6)} c 4 -14 10 -14 12 0 z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></path>')
        r = random.Random(seed)
        for k in range(7):
            x0 = w * r.uniform(0.1, 0.9); y0 = b - r.uniform(40, 100) * s
            o.append(f'<path d="M{f(x0)} {f(y0)} c 10 -14 -10 -26 0 -40 c 10 -14 -10 -26 0 -40" stroke="#E8C8E8" stroke-width="2.4" fill="none" opacity="0.6"></path>')
    return "".join(o)

def greeks(p, w, h, seed):
    """Certain Greeks came to Philip, saying, Sir, we would see Jesus: in the temple court two Greeks, bareheaded, in short
    cloaks, speaking with Philip; Andrew coming."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.6, h * 0.5, min(w * 0.5, h * 0.9)), pavement(w, h, h * 0.5)]
    s = fit(b, max(h * 0.26, b - 230))
    hair = '<path d="M-13 -188 C -14 -204 14 -204 13 -188 L 14 -182 L 9 -186 L -9 -186 L -14 -182 Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="1.4"></path>'
    beard_ = A.BLACK_BEARD.replace("#2A1A10", "#7A5A3A")
    o.append(mk.person(p, round(w * 0.62), round(b), round(s, 3), body="#D9A27A", cloth="#E8E2D6", kind="Tunic", sw=3, extra=hair + beard_ + '<path d="M-24 -160 L 24 -100 L 24 -88 L -24 -148 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    o.append(mk.person(p, round(w * 0.74), round(b - 4), round(s * 0.97, 3), body="#D9A27A", cloth="#C8C0A8", kind="Tunic", sw=3, extra=hair + '<path d="M-24 -160 L 24 -100 L 24 -88 L -24 -148 Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    o.append(mk.person(p, round(w * 0.42), round(b), round(s * 0.98, 3), body="#C98E66", cloth="#7A6A3A", kind="Robe", sw=3, flip=True, up=UP_BLESS))
    o.append(disciple(p, w * 0.22, b - 4, s * 0.96, "andrew", flip=True))
    return "".join(o)

def grain_wheat(p, w, h, seed):
    """Except a grain of wheat fall into the earth and die: the field cut open like a plan — above, the ripe ears standing
    thick in the sun; below, in the dark earth, the one grain fallen in, split, its roots going down and its shoot going up
    into the many ears."""
    r = random.Random(seed)
    g = h * 0.5
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), sun(w * 0.84, h * 0.12, max(12, h * 0.04), color="#FFE680", op=0.4),
         f'<rect x="-10" y="{f(g)}" width="{f(w + 20)}" height="{f(h - g + 10)}" fill="#4A2418" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="-10" y="{f(g + (h - g) * 0.5)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A1A10" opacity="0.6"></rect>']
    for _ in range(30):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(g + 8, h))}" r="{f(r.uniform(1.5, 4))}" fill="#6A3A28"></circle>')
    sx, sy = w * 0.5, g + (h - g) * 0.45
    o.append(grain(w * 0.06, w * 0.94, g, h * 0.36, seed, color="#E8C060", n=40))
    for k in range(7):
        a = math.pi * (0.2 + 0.6 * k / 6)
        o.append(f'<path d="M{f(sx)} {f(sy + 6)} C {f(sx + 30 * math.cos(a))} {f(sy + 40)} {f(sx + 70 * math.cos(a))} {f(sy + 50 * math.sin(a))} {f(sx + 90 * math.cos(a))} {f(min(h - 4, sy + 90 * math.sin(a)))}" stroke="#D8C8A0" stroke-width="2" fill="none"></path>')
    o.append(f'<path d="M{f(sx)} {f(sy)} L {f(sx)} {f(g)}" stroke="#7AAA3A" stroke-width="4"></path>')
    o.append(f'<ellipse cx="{f(sx - 7)}" cy="{f(sy)}" rx="8" ry="14" fill="#C8A050" stroke="{INK}" stroke-width="1.6" transform="rotate(-20 {f(sx - 7)} {f(sy)})"></ellipse>'
             f'<ellipse cx="{f(sx + 7)}" cy="{f(sy)}" rx="8" ry="14" fill="#C8A050" stroke="{INK}" stroke-width="1.6" transform="rotate(20 {f(sx + 7)} {f(sy)})"></ellipse>')
    o.append(glow(sx, g - h * 0.2, h * 0.2, "#FFF4C2", 0.6, f"{p}g"))
    return "".join(o)

def voice_sky(p, w, h, seed):
    """Father, glorify thy name. There came therefore a voice out of heaven: the temple court under a great sky split with
    light and thundercloud, the multitude looking up, some with their hands raised, Jesus standing among them (God never
    drawn: the light and the cloud only)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A5A", "#FFE6A0"), clouds(w, h * 0.18, seed, n=7, color="#4A4A6A", op=0.9, h=h),
         rays(w * 0.5, h * 0.1, 30, 20, h, color="#FFFFFF", op=0.3, a0=30, a1=150), glow(w * 0.5, h * 0.08, h * 0.5, "#FFFFFF", 0.95, f"{p}g"),
         pavement(w, h, h * 0.66, color="#C8B898")]
    s = fit(b, max(h * 0.26, b - 230)); r = random.Random(seed)
    o.append(jesus(p, w * 0.5, b, s, up=[(-22, -158), (-34, -190), (-38, -222)]))
    for i, x in enumerate((0.08, 0.2, 0.32, 0.68, 0.8, 0.92)):
        o.append(figure(p, w * x, b - 4 * (i % 2), b - 4 * (i % 2) - 190 * s, r.choice(HEB), "woman" if i % 3 == 1 else "man", flip=x > 0.5,
                        up=[(-22, -158), (-30, -186), (-28, -210)] if i % 2 == 0 else None))
    return "".join(o)

def dusk_road(p, w, h, seed):
    """Yet a little while is the light among you: a road at the last of the light, the sun going down behind the hills,
    the dark coming on from the other side, a traveller with a lamp hurrying while there is light."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#FF8A3D"), sun(w * 0.82, h * 0.56, max(12, h * 0.05), color="#FFB04A", op=0.4),
         f'<rect x="-10" y="-10" width="{f(w * 0.4)}" height="{f(h + 20)}" fill="#05051A" opacity="0.5"></rect>',
         hills(w, h, h * 0.56, seed, color="#3A2A3A", amp=12, step=80), ground(w, h, h * 0.66, "#4A3A3A", dy=0),
         f'<path d="M-10 {f(h * 0.92)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.68)}" stroke="#8A6A5A" stroke-width="{f(max(10, h * 0.07))}" fill="none"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    lampx = w * 0.56 - 40 * s
    o.append(man(p, w * 0.56, b - h * 0.06, s * 0.9, "#6A5A4A", flip=False, up=[(-22, -158), (-36, -130), (-40, -110)]))
    o.append(glow(lampx, b - h * 0.06 - 104 * s * 0.9, 40 * s, "#FFC14D", 0.9, f"{p}l") + clay_lamp(lampx, b - h * 0.06 - 100 * s * 0.9, s * 0.4))
    return "".join(o)
