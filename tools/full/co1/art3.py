"""Drawings for 1 Corinthians 8–11 (chapter 3 of the volume), on co1.art2: the idol-temple and its meat (8); the soldier, the
vineyard and the flock, the ox treading out the corn unmuzzled, the altar's portion, all things to all men, the games —
the runners, the corruptible and the incorruptible crown, a boxer striking the air (9); the fathers under the cloud, through
the sea, the manna, the rock (Exodus' and Isaiah's drawings), the calf, the empty desert and the serpents on the sand (no one
bitten), the way of escape, the cup of blessing and the bread, the empty idol court (10:20–21, demons, words only), the
feast (10); praying bareheaded and veiled, the divided supper, the Lord's supper (Matthew's drawing, Jesus' words in
balloons), the table waiting (11; 11:30 words only)."""
from co1.art2 import *
from co1.art2 import f, INK, _seated_lap
from act.art10 import statue
from act.art5 import damascus_road
from exo.art4 import cloud_between
from jhn.art3 import manna_camp
from isa.art13 import rock_water
from mat.art10 import supper
import samuel1 as S1, samuel4 as S4, exodus5 as X5, snake as SN

# ---- 1 Corinthians 8 ---------------------------------------------------------------------------------------------------
def _temple_front(x, base, wd, ht, dark=False):
    """A pagan temple's front: steps, columns, a pediment; the doors open on a dark cella with an idol on its plinth."""
    col = "#C8C0B0" if dark else "#F3EFE6"
    o = [f'<rect x="{f(x)}" y="{f(base - ht * 0.06)}" width="{f(wd)}" height="{f(ht * 0.06)}" fill="#D8CCB0" stroke="{INK}" stroke-width="1.8"></rect>',
         f'<rect x="{f(x + wd * 0.18)}" y="{f(base - ht * 0.76)}" width="{f(wd * 0.64)}" height="{f(ht * 0.7)}" fill="#1A1210" stroke="{INK}" stroke-width="2"></rect>']
    o.append(statue(x + wd * 0.5, base - ht * 0.06, ht * 0.0042, kind=1, color="#C8A040" if not dark else "#8A7A5A"))
    for k in range(6):
        cx = x + wd * (0.06 + k * 0.176)
        o.append(f'<rect x="{f(cx - wd * 0.03)}" y="{f(base - ht * 0.8)}" width="{f(wd * 0.06)}" height="{f(ht * 0.74)}" fill="{col}" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(x - wd * 0.02)}" y="{f(base - ht * 0.88)}" width="{f(wd * 1.04)}" height="{f(ht * 0.08)}" fill="{col}" stroke="{INK}" stroke-width="1.8"></rect>'
             f'<path d="M{f(x - wd * 0.03)} {f(base - ht * 0.88)} L {f(x + wd * 0.5)} {f(base - ht)} L {f(x + wd * 1.03)} {f(base - ht * 0.88)} Z" fill="{col}" stroke="{INK}" stroke-width="1.8"></path>')
    return "".join(o)

def idol_meat(p, w, h, seed):
    """Things sacrificed to idols: an idol's temple on its steps, the gilded image in the dark of its doors and the altar
    smoking before it; and in the forecourt a butcher's stall, the joints from the sacrifice hung up for sale and a buyer
    at the counter."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), pavement(w, h, b, color="#D8D0C0")]
    o.append(_temple_front(w * 0.04, b, w * 0.44, min(h * 0.86, w * 0.4)))
    o.append(S4.altar(w * 0.56, b, min(0.7, h / 360), fire=True, seed=seed))
    sx, sw_ = w * 0.68, w * 0.3                                 # the stall
    o.append(f'<rect x="{f(sx)}" y="{f(h * 0.3)}" width="{f(sw_)}" height="{f(b - h * 0.3)}" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(sx - 8)} {f(h * 0.3)} L {f(sx + sw_ + 8)} {f(h * 0.3)} L {f(sx + sw_)} {f(h * 0.16)} L {f(sx)} {f(h * 0.16)} Z" fill="#B5121B" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(sx + 6)} {f(h * 0.36)} L {f(sx + sw_ - 6)} {f(h * 0.36)}" stroke="#2A1A10" stroke-width="3"></path>')
    for k in range(3):
        jx = sx + sw_ * (0.2 + 0.3 * k)
        o.append(f'<path d="M{f(jx)} {f(h * 0.36)} l 0 {f(h * 0.05)}" stroke="#8A8A94" stroke-width="2"></path>'
                 f'<path d="M{f(jx - h * 0.04)} {f(h * 0.41)} C {f(jx - h * 0.06)} {f(h * 0.5)} {f(jx - h * 0.02)} {f(h * 0.6)} {f(jx)} {f(h * 0.6)} C {f(jx + h * 0.03)} {f(h * 0.58)} {f(jx + h * 0.05)} {f(h * 0.48)} {f(jx + h * 0.04)} {f(h * 0.41)} Z" fill="#A8402A" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(sx - 4)}" y="{f(b - h * 0.22)}" width="{f(sw_ + 8)}" height="{f(h * 0.22)}" fill="#C8A878" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, b - min(h * 0.7, 190))
    o.append(folk(p, w * 0.64, b, s, 3, flip=True, up=[(-22, -158), (-44, -146), (-64, -146)]))
    return "".join(o)

def one_god(w, h, seed):
    """Gods many, and lords many; yet to us there is one God, the Father … and one Lord, Jesus Christ: at the left, in the
    dusk, idols on their plinths — stone, gilt, bronze — and nothing in them; at the right, light from above on the open
    land, no figure in it."""
    o = [f'<defs><linearGradient id="og{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2A2034"></stop><stop offset="0.5" stop-color="#5A4A5A"></stop>'
         f'<stop offset="0.62" stop-color="#E8D8B0"></stop><stop offset="1" stop-color="#FFF8E6"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#og{seed})"></rect>',
         halo(w * 0.8, -h * 0.05, h * 0.9, "#FFFFFF", 0.7), rays(w * 0.8, -h * 0.05, 18, h * 0.2, h * 1.2, "#FFF4C2", 0.35, 4, a0=20, a1=160)]
    b = h * 0.86
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3E3A" stroke="{INK}" stroke-width="2"></rect>')
    k = min(1.2, h / 200)
    for i, (x, c) in enumerate(((0.1, "#B8B0A0"), (0.24, "#C8A040"), (0.38, "#8A6A3A"))):
        o.append(statue(w * x, b, k * 0.8, kind=i, color=c))
    o.append(plate_label(w * 0.24, h * 0.1, "GODS MANY · LORDS MANY", "#E8E2D6", 10.5, halo_="#1A1420")
             + plate_label(w * 0.78, h * 0.9 + 4 if h * 0.9 + 4 < h - 6 else h * 0.94, "ONE GOD · ONE LORD", "#7A4A2A", 10.5, halo_="#FFF8E6"))
    return "".join(o)

def temple_meal(p, w, h, seed):
    """Sitting at meat in an idol's temple: the dining hall of the temple, a man of knowledge reclining at the table with
    the sacrificed meat before him, the image on its plinth behind; and in the doorway, half in shadow, a weak brother
    watching."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), room(w, h, b, wall="#7A5A4A", floor="#4A3A2A"), lamp_glow(w * 0.4, h * 0.3, max(w, h) * 0.5, f"{p}tm", op=0.45)]
    o.append(statue(w * 0.12, b - h * 0.02, min(1.2, h / 220), kind=2, color="#C8A040"))
    k = min(1.0, h / 240)
    o.append(EP.couch(w * 0.26, b, w * 0.3, k * 1.2))
    o.append(EP.low_table(w * 0.36, b, w * 0.16, k) + f'<ellipse cx="{f(w * 0.44)}" cy="{f(b - 34 * k)}" rx="{f(w * 0.05)}" ry="{f(6 * k)}" fill="#C8B488" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(w * 0.41)} {f(b - 36 * k)} C {f(w * 0.42)} {f(b - 50 * k)} {f(w * 0.46)} {f(b - 50 * k)} {f(w * 0.47)} {f(b - 36 * k)} Z" fill="#8A3A22" stroke="{INK}" stroke-width="1.4"></path>')
    s = fit(b, b - min(h * 0.72, 196))
    o.append(seated(w * 0.3, b - 34 * k, s * 0.72, "#C8C0E0", head=None, beard="#3A2A1A"))
    dx, dw = w * 0.74, w * 0.16
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.14)}" width="{f(dw)}" height="{f(b - h * 0.14)}" fill="#1A1210" stroke="{INK}" stroke-width="2.6"></rect>')
    o.append(folk(p, dx + dw * 0.5, b, s, 2, flip=False).replace('fill="#6A7A4A"', 'fill="#4A5A3A"'))
    return "".join(o)

# ---- 1 Corinthians 9 ---------------------------------------------------------------------------------------------------
def seen_lord(p, w, h, seed):
    """Have I not seen Jesus our Lord? The road near Damascus at noon, the light out of heaven poured down on it (Acts'
    drawing; Jesus is not drawn)."""
    return damascus_road(p, w, h, seed, fallen=True, lit=True)

def wages(p, w, h, seed):
    """What soldier ever serveth at his own charges? who planteth a vineyard, and eateth not the fruit thereof? or who
    feedeth a flock, and eateth not of the milk? Three cells: the soldier at his rations, the vinedresser with a cluster in
    his hand, the shepherd with his flock and a bowl of milk."""
    o = [mk.defs(p, *ALL, "ManUp")]
    cw = w / 3; b = h * 0.93
    s = fit(b, b - min(h * 0.72, 190))
    for i, (top, bot) in enumerate((("#C8B490", "#8A6A4A"), ("#9CCB5E", "#5A7A3A"), ("#8FD0E2", "#C8B080"))):
        x0 = i * cw; uid = f"{p}wg{i}"
        o.append(f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"></stop><stop offset="1" stop-color="{bot}"></stop></linearGradient></defs>'
                 f'<rect x="{f(x0)}" y="-10" width="{f(cw + 1)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>'
                 f'<rect x="{f(x0)}" y="{f(b)}" width="{f(cw + 1)}" height="{f(h)}" fill="{bot}" stroke="{INK}" stroke-width="1.6"></rect>')
    helm = ('<path d="M-14 -190 C -14 -206 14 -206 14 -190 L 14 -180 L -14 -180 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-20 -204 L 20 -204" stroke="#B5121B" stroke-width="7" stroke-linecap="round"></path>'
            '<path d="M-58 -140 L -48 -138 L -50 -128 L -60 -130 Z" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(robed(p, cw * 0.5, b, s, "#A8382E", hair="#3A2A1A", belt="#5A3A1A", flip=True, up=[(-22, -158), (-40, -140), (-56, -136)], extra=helm))
    vx = cw * 1.22                                             # the vine on its trellis
    o.append(f'<path d="M{f(vx)} {f(b)} C {f(vx - 10)} {f(b - h * 0.3)} {f(vx + 10)} {f(b - h * 0.5)} {f(vx)} {f(b - h * 0.66)}" stroke="#5A3A1A" stroke-width="5" fill="none"></path>'
             + "".join(f'<circle cx="{f(vx + (k % 3 - 1) * 14)}" cy="{f(b - h * (0.5 + 0.06 * (k // 3)))}" r="{f(max(8, h * 0.04))}" fill="#4A8A3A" stroke="{INK}" stroke-width="1.2"></circle>' for k in range(6))
             + "".join(f'<circle cx="{f(vx + 18 + (k % 2) * 6)}" cy="{f(b - h * 0.4 + (k // 2) * 7)}" r="4" fill="#5A2A6A" stroke="{INK}" stroke-width="1"></circle>' for k in range(6)))
    grapes = "".join(f'<circle cx="{-66 + (k % 2) * 6}" cy="{-140 + (k // 2) * 7}" r="4" fill="#5A2A6A" stroke="#0D0D0F" stroke-width="1"></circle>' for k in range(6))
    o.append(robed(p, cw * 1.62, b, s, "#6A5A3A", head="#3A4A3A", cord="#1A2A1A", beard="#3A2A1A", up=[(-22, -158), (-44, -150), (-62, -144)], extra=grapes))
    o.append(E.sheep(cw * 2.2, b, s * 0.5) + E.sheep(cw * 2.36, b + 2, s * 0.44))
    bowl = '<path d="M-74 -140 C -72 -128 -54 -128 -52 -140 Z" fill="#B8784A" stroke="#0D0D0F" stroke-width="1.4"></path><ellipse cx="-63" cy="-140" rx="11" ry="3" fill="#FFFDF4" stroke="#0D0D0F" stroke-width="1"></ellipse>'
    o.append(robed(p, cw * 2.74, b, s, "#8A6A4A", head="#E8E2D6", cord="#5A4A3A", beard="#5A4A3A", up=[(-22, -158), (-44, -150), (-60, -144)], extra=bowl))
    for k in (1, 2):
        o.append(f'<path d="M{f(cw * k)} -10 L {f(cw * k)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    return "".join(o)

def ox(x, y, s=1.0, flip=False, color="#7A5A3A", patch="#4A3220"):
    """An ox (Samuel's cow drawing without the udder), his head low to the grain."""
    g = S1.cow(x, y, s, flip=flip, color=color, patch=patch, low=True)
    return re.sub(r'<path d="M-36 -50 C -36 -38 -16 -36 -14 -50 Z"[^>]*></path><path d="M-30 -42 L -30 -36 M-20 -42 L -20 -36"[^>]*></path>', "", g)

def ox_tread(p, w, h, seed):
    """Thou shalt not muzzle the ox when he treadeth out the corn: a threshing floor on a hill at harvest, the ox going
    round on the spread sheaves, his mouth free to the grain; the thresher with his fork behind him, sheaves stacked."""
    b = h * 0.9
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.5, seed, color="#C8A84A", amp=12, step=90),
         ground(w, h, h * 0.6, "#C8A06A", dy=-4)]
    o.append(S4.threshing_floor(w * 0.5, b - h * 0.06, w * 0.7))
    r = random.Random(seed)
    for _ in range(30):                                        # the spread grain
        x = w * 0.5 + r.uniform(-0.3, 0.3) * w; y = b - h * 0.06 + r.uniform(-0.06, 0.06) * w
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-10, 10))} {f(r.uniform(-4, 4))}" stroke="#E8C870" stroke-width="2"></path>')
    k = min(1.0, h / 220)
    o.append(ox(w * 0.52, b - h * 0.02, k * 0.7))
    for x in (0.08, 0.16, 0.9):                                # sheaves standing
        sx = w * x
        o.append(f'<path d="M{f(sx - 14 * k)} {f(h * 0.62)} L {f(sx)} {f(h * 0.62 - 60 * k)} L {f(sx + 14 * k)} {f(h * 0.62)} Z" fill="#E8C870" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<path d="M{f(sx - 10 * k)} {f(h * 0.62 - 26 * k)} L {f(sx + 10 * k)} {f(h * 0.62 - 26 * k)}" stroke="#8A6A2A" stroke-width="2.4"></path>')
    s = fit(b, b - min(h * 0.62, 170))
    fork = '<path d="M-66 -150 L -50 -40 M-74 -156 L -66 -150 L -58 -160" stroke="#8A6A3A" stroke-width="3" fill="none"></path>'
    o.append(robed(p, w * 0.22, b, s, "#8A6A4A", head="#E8E2D6", cord="#5A4A3A", beard="#5A4A3A", belt="#4A3A2A", flip=True, up=[(-22, -158), (-46, -150), (-66, -150)], extra=fork))
    return "".join(o)

def altar_portion(p, w, h, seed):
    """They that wait upon the altar have their portion with the altar: the altar of burnt-offering with its fire, and a
    priest in white carrying away his portion on a dish."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#E8D8B0", "#C8B080"), pavement(w, h, b, color="#E8DCC0"),
         f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(6):
        o.append(f'<rect x="{f(w * (0.04 + k * 0.18))}" y="{f(h * 0.16)}" width="{f(w * 0.03)}" height="{f(b - h * 0.16)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(S4.altar(w * 0.36, b, min(0.9, h / 290), fire=True, seed=seed))
    s = fit(b, b - min(h * 0.72, 196))
    dish = '<ellipse cx="-68" cy="-150" rx="16" ry="5" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.4"></ellipse><path d="M-78 -152 C -76 -164 -60 -164 -58 -152 Z" fill="#8A3A22" stroke="#0D0D0F" stroke-width="1.2"></path>'
    o.append(robed(p, w * 0.72, b, s, "#F3EFE6", head="#F3EFE6", cord="#1F3A7A", beard="#3A2A1A", belt="#1F3A7A", up=[(-22, -158), (-46, -152), (-62, -150)], extra=dish, flip=True))
    return "".join(o)

def all_men(p, w, h, seed):
    """I am become all things to all men: Paul in the midst, his hand out; at the left a Jew in a white headcloth and one
    under the law with the scroll; at the right a Greek philosopher, and a weak man leaning on his staff."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.78, seed, hmin=0.2, hmax=0.3), pavement(w, h, b, color="#D8CCB0")]
    s = fit(b, b - min(h * 0.74, 200))
    o.append(robed(p, w * 0.1, b, s, "#E8E2D6", head="#F3EFE6", cord="#1F3A7A", beard="#3A2A1A", mantle="#3A4A7A", flip=True))
    o.append(robed(p, w * 0.26, b, s * 0.98, "#3A3A5A", head="#E8E2D6", cord="#3A3A5A", beard="#8A847A", flip=True, up=[(-22, -158), (-40, -150), (-56, -154)],
                   extra=sealed_scroll(-60, -152, 0.2, rot=80)))
    o.append(paul_fig(p, w * 0.5, b, s, flip=True, up=[(-22, -158), (-46, -150), (-70, -156)]))
    o.append(philo(p, w * 0.74, b, s, 3))
    staff = '<path d="M-30 -110 L -40 0" stroke="#6A4A2A" stroke-width="4"></path>'
    o.append(robed(p, w * 0.9, b, s * 0.94, "#7A7A6A", hair="#8A847A", beard="#8A847A", up=[(-22, -158), (-30, -134), (-32, -112)], extra=staff))
    return "".join(o)

POSES = {   # limbs as (back arm, back leg, front leg, front arm): joint points from the shoulder / hip; the body leaning forward
    "run_a": dict(sh=(8, -158), hip=(-4, -98), head=(14, -180), lean=-10,
                  barm=[(8, -156), (-14, -132), (-30, -146)], bleg=[(-4, -98), (-18, -52), (-50, -24), (-44, -14)],
                  fleg=[(-4, -98), (28, -72), (20, -30), (34, -26)], farm=[(8, -156), (30, -136), (42, -158)]),
    "run_b": dict(sh=(8, -158), hip=(-4, -98), head=(14, -180), lean=-10,
                  barm=[(8, -156), (26, -134), (40, -150)], bleg=[(-4, -98), (20, -60), (4, -20), (16, -12)],
                  fleg=[(-4, -98), (-22, -56), (-48, -34), (-46, -22)], farm=[(8, -156), (-12, -134), (-28, -150)]),
    "box": dict(sh=(4, -160), hip=(-2, -100), head=(8, -182), lean=-4,
                barm=[(4, -158), (22, -146), (30, -164)], bleg=[(-2, -100), (-22, -54), (-30, -2), (-20, 0)],
                fleg=[(-2, -100), (20, -56), (26, -2), (38, 0)], farm=[(4, -158), (40, -158), (78, -160)]),
}

def athlete(x, y, s, pose="run_a", skin="#C98E66", cloth="#F3EFE6", hair="#2A1A10", flip=False, gloves=False):
    """An athlete at the games, in profile facing right, a short belted tunic, the limbs drawn as jointed strokes so the
    stride shows (no blob): pose "run_a" / "run_b" (the two halves of a stride), "box" (a boxer striking out, his hands
    bound in thongs with gloves=True). (x, y) the ground under him; about 200 units tall."""
    P = POSES[pose]; sx = -s if flip else s
    dark = "#8A5A40"
    def limb(pts, col, wd=13):
        d = "M" + " L ".join(f"{a} {b}" for a, b in pts)
        return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{wd}" stroke-linecap="round" stroke-linejoin="round"></path>'
                f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{wd - 3.5}" stroke-linecap="round" stroke-linejoin="round"></path>')
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">', limb(P["barm"], dark, 12), limb(P["bleg"], dark, 15)]
    (shx, shy), (hx, hy) = P["sh"], P["hip"]
    o.append(f'<path d="M{shx - 14} {shy - 4} C {shx - 4} {shy - 8} {shx + 10} {shy - 6} {shx + 16} {shy} L {hx + 22} {hy + 8} L {hx + 14} {hy + 20} L {hx - 22} {hy + 16} L {hx - 16} {hy} Z" '
             f'fill="{cloth}" stroke="{INK}" stroke-width="2.6"></path>'
             f'<path d="M{hx - 17} {hy - 2} L {hx + 19} {hy + 2}" stroke="#8A5A30" stroke-width="3.4"></path>')
    o.append(limb(P["fleg"], skin, 15) + limb(P["farm"], skin, 12))
    if gloves:
        for pt in (P["barm"][-1], P["farm"][-1]):
            o.append(f'<circle cx="{pt[0]}" cy="{pt[1]}" r="8" fill="#8A5A30" stroke="{INK}" stroke-width="1.6"></circle>')
    cx, cy = P["head"]
    o.append(f'<path d="M{shx - 2} {shy - 4} L {cx - 4} {cy + 8}" stroke="{INK}" stroke-width="11" stroke-linecap="round"></path><path d="M{shx - 2} {shy - 4} L {cx - 4} {cy + 8}" stroke="{skin}" stroke-width="7.5" stroke-linecap="round"></path>'
             f'<circle cx="{cx}" cy="{cy}" r="13" fill="{skin}" stroke="{INK}" stroke-width="2.4"></circle>'
             f'<path d="M{cx + 11} {cy - 2} l 5 4 l -5 2" fill="{skin}" stroke="{INK}" stroke-width="1.4"></path>'
             f'<path d="M{cx - 14} {cy + 4} C {cx - 16} {cy - 18} {cx + 10} {cy - 20} {cx + 13} {cy - 6} C {cx + 6} {cy - 10} {cx - 2} {cy - 8} {cx - 6} {cy + 2} Z" fill="{hair}" stroke="{INK}" stroke-width="1.4"></path>')
    return "".join(o) + "</g>"

def race(p, w, h, seed):
    """They that run in a race run all, but one receiveth the prize: the stadium at the games, its banks of spectators,
    the runners stretched out down the track, the turning-post and the judges' stand with the victor's wreath."""
    b = h * 0.9
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8")]
    o.append(f'<path d="M-10 {f(h * 0.2)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.56)} L -10 {f(h * 0.56)} Z" fill="#9AA06A" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for row in range(4):
        y = h * (0.32 + row * 0.06)
        for i in range(int(w / 12)):
            if r.random() < 0.75:
                o.append(f'<circle cx="{f(i * 12 + r.uniform(-3, 3))}" cy="{f(y + r.uniform(-2, 2))}" r="{f(max(2.2, h * 0.012))}" fill="{r.choice(["#3A2A2A", "#E8E2D6", "#5A3A2A", "#B5121B", "#2A3A6A"])}"></circle>')
    o.append(f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h)}" fill="#E8C890" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(4):
        y = h * (0.62 + k * 0.08)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#F3EFE6" stroke-width="2" opacity="0.8"></path>')
    o.append(f'<rect x="{f(w * 0.9)}" y="{f(h * 0.34)}" width="{f(w * 0.02)}" height="{f(b - h * 0.34)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<circle cx="{f(w * 0.91)}" cy="{f(h * 0.3)}" r="{f(max(10, h * 0.05))}" fill="none" stroke="#4A8A3A" stroke-width="{f(max(4, h * 0.02))}"></circle>')
    s = fit(b, b - min(h * 0.56, 160))
    for i, x in enumerate((0.66, 0.48, 0.34, 0.2)):
        o.append(athlete(w * x, b - (i % 2) * h * 0.04, s * (1 - 0.03 * i), pose="run_a" if i % 2 == 0 else "run_b", skin=["#C98E66", "#A8704E", "#D9A27A", "#B98A6E"][i],
                         cloth=["#F3EFE6", "#E8D8B0", "#F3EFE6", "#D8E0E8"][i], hair=["#2A1A10", "#1A1210", "#5A3A1A", "#2A1A10"][i]))
        o.append(mk.speed(w * x - 60 * s, b - 100 * s, 6, 20 * s, 70 * s, seed + i, color="#FFFFFF", op=0.5) if i == 0 else "")
    return "".join(o)

def crowns(w, h, seed):
    """They do it to receive a corruptible crown; but we an incorruptible: a plate — at the left the victor's wreath of
    pine, drying and shedding its needles; at the right a crown of light that does not fade."""
    o = [plate_bg(w, h, "1 CORINTHIANS 9:25 · A CORRUPTIBLE CROWN · AN INCORRUPTIBLE")]
    k = min(w / 560, (h - 40) / 200); cy = h * 0.58
    lx, rx = w * 0.27, w * 0.73
    r = random.Random(seed)
    for a in range(0, 360, 12):                                # the wreath of pine, withering
        t = math.radians(a)
        x, y = lx + 60 * k * math.cos(t), cy + 34 * k * math.sin(t)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(10 * k * math.cos(t + 1))} {f(10 * k * math.sin(t + 1))}" stroke="{"#6A7A3A" if a % 36 else "#8A6A3A"}" stroke-width="{f(3 * k)}"></path>')
    for _ in range(12):
        x, y = lx + r.uniform(-70, 70) * k, cy + 50 * k + r.uniform(0, 30) * k
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-6, 6) * k)} {f(3 * k)}" stroke="#8A6A3A" stroke-width="{f(2 * k)}"></path>')
    o.append(halo(rx, cy, 110 * k, "#FFE680", 0.55) + rays(rx, cy, 16, 60 * k, 130 * k, "#FFF4C2", 0.4, 3))
    o.append(f'<path d="M{f(rx - 60 * k)} {f(cy + 20 * k)} L {f(rx - 64 * k)} {f(cy - 30 * k)} L {f(rx - 32 * k)} {f(cy - 6 * k)} L {f(rx)} {f(cy - 44 * k)} L {f(rx + 32 * k)} {f(cy - 6 * k)} '
             f'L {f(rx + 64 * k)} {f(cy - 30 * k)} L {f(rx + 60 * k)} {f(cy + 20 * k)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(rx - 60 * k)}" y="{f(cy + 14 * k)}" width="{f(120 * k)}" height="{f(14 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>')
    ly = min(cy + 90 * k, h - 10)
    o.append(plate_label(lx, ly, "CORRUPTIBLE", CY, 10) + plate_label(rx, ly, "INCORRUPTIBLE", GOLD, 10))
    return "".join(o)

def boxer(p, w, h, seed):
    """So fight I, as not beating the air: in the palaestra, a boxer with his hands bound in thongs striking out, his blows
    aimed true (no opponent drawn); the colonnade of the training ground behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#E8905A", "#F3D8A0")]
    for k in range(7):
        o.append(f'<rect x="{f(w * (0.02 + k * 0.16))}" y="{f(h * 0.14)}" width="{f(w * 0.03)}" height="{f(b - h * 0.14)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#E8C890" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, b - min(h * 0.76, 210))
    x = w * 0.42
    o.append(athlete(x, b, s, pose="box", skin="#B98A6E", cloth="#F3EFE6", gloves=True))
    o.append(mk.speed(x + 120 * s, b - 160 * s, 9, 16 * s, 80 * s, seed, color="#FFFFFF", op=0.8))
    return "".join(o)

# ---- 1 Corinthians 10 --------------------------------------------------------------------------------------------------
def under_cloud(p, w, h, seed):
    """Our fathers were all under the cloud, and all passed through the sea: the pillar of cloud between the camps (Exodus)."""
    return cloud_between(p, w, h, seed)

def manna(p, w, h, seed):
    """Did all eat the same spiritual food: the manna lying about the camp at dawn (John's drawing)."""
    return manna_camp(p, w, h, seed)

def rock(p, w, h, seed):
    """Did all drink the same spiritual drink: the cloven rock in the desert and the waters gushing (Isaiah's drawing)."""
    return rock_water(p, w, h, seed)

def desert_empty(w, h, seed):
    """They were overthrown in the wilderness: the empty desert, the hills bare, no one in it."""
    return vista(w, h, seed, tone="desert", horizon=0.6, hills_n=2, sun_at=(0.8, 0.2))

def calf_camp(p, w, h, seed):
    """The people sat down to eat and drink, and rose up to play: the molten calf on its pedestal before the tents, the
    smoke of the altar going up beside it, the camp a crowd far off with its hands thrown up."""
    b = h * 0.9
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), vista(w, h, seed, tone="desert", horizon=0.56, hills_n=1, ground_=True)]
    r = random.Random(seed)
    for i in range(7):                                         # the tents
        tx = w * (0.04 + 0.14 * i); ty = h * 0.6
        o.append(f'<path d="M{f(tx)} {f(ty)} L {f(tx + w * 0.05)} {f(ty - h * 0.1)} L {f(tx + w * 0.1)} {f(ty)} Z" fill="{r.choice(["#8A6A4A", "#6A4A3A", "#A8865A"])}" stroke="{INK}" stroke-width="1.6"></path>')
    k = min(1.0, h / 260)
    o.append(S4.altar(w * 0.3, b, k * 0.6, fire=True, seed=seed))
    o.append(X5.calf(w * 0.5, b, k * 0.9, uid=f"{p}cf"))
    s = fit(b, b - min(h * 0.4, 110))
    o.append(crowd(p, w * 0.66, w * 0.98, b, b - 190 * s, 7, seed, women=0.4, up=UP_HIGH))
    return "".join(o)

def serpents(w, h, seed):
    """And perished by the serpents: the empty desert at evening and the serpents on the sand among the stones — no one
    drawn."""
    o = [vista(w, h, seed, tone="dusk", horizon=0.5, hills_n=2)]
    r = random.Random(seed)
    for i in range(5):
        x, y, s = w * (0.1 + 0.2 * i + r.uniform(-0.04, 0.04)), h * r.uniform(0.66, 0.9), min(1.4, h / 180) * r.uniform(0.8, 1.1)
        d = 1 if i % 2 else -1
        pts = [(x - 30 * s * d, y), (x - 12 * s * d, y - 8 * s), (x + 6 * s * d, y + 4 * s), (x + 22 * s * d, y - 6 * s), (x + 34 * s * d, y - 14 * s)]
        o.append(SN.snake(pts, 4.2 * s, f"sp{seed}{i}", head_scale=0.55))
    for _ in range(8):
        x, y, s = w * r.uniform(0, 1), h * r.uniform(0.6, 0.96), h * r.uniform(0.02, 0.05)
        o.append(f'<path d="M{f(x - s * 1.4)} {f(y)} L {f(x - s * 0.5)} {f(y - s)} L {f(x + s * 0.8)} {f(y - s * 0.7)} L {f(x + s * 1.4)} {f(y)} Z" fill="#6A4A3A" stroke="{INK}" stroke-width="1.4"></path>')
    return "".join(o)

def way_escape(w, h, seed):
    """With the temptation make also the way of escape: a dark ravine between sheer rocks, and a narrow path climbing out
    of it into the light."""
    o = [sky(w, h, "#FFF4C2", "#FFE6A0"), halo(w * 0.62, h * 0.1, h * 0.7, "#FFFFFF", 0.7)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.5)} -10 L {f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.46)} {f(h * 0.6)} L {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2030" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(w + 10)} -10 L {f(w * 0.72)} -10 L {f(w * 0.68)} {f(h * 0.34)} L {f(w * 0.78)} {f(h * 0.62)} L {f(w * 0.74)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2030" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.74)} {f(h + 10)} L {f(w * 0.78)} {f(h * 0.62)} L {f(w * 0.68)} {f(h * 0.34)} L {f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.46)} {f(h * 0.6)} Z" fill="#5A4A5A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h + 10)} C {f(w * 0.56)} {f(h * 0.8)} {f(w * 0.52)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.5)} C {f(w * 0.64)} {f(h * 0.42)} {f(w * 0.6)} {f(h * 0.36)} {f(w * 0.62)} {f(h * 0.3)}" '
             f'stroke="#E8D8B0" stroke-width="{f(max(6, h * 0.04))}" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def cup_bread(w, h, seed):
    """The cup of blessing which we bless … the bread which we break: on a white cloth in lamplight, the cup and the one
    loaf broken in two."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1E1A"></rect>', lamp_glow(w * 0.5, h * 0.4, max(w, h) * 0.6, f"cb{seed}", op=0.55)]
    ty = h * 0.66
    o.append(f'<path d="M-10 {f(ty)} L {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.18)} {f(ty + 6)} L {f(w * 0.82)} {f(ty + 6)} L {f(w * 0.84)} {f(min(h + 10, ty + 120 * min(w / 520, h / 230)))} L {f(w * 0.16)} {f(min(h + 10, ty + 120 * min(w / 520, h / 230)))} Z" fill="#F8F4EA" stroke="{INK}" stroke-width="1.8"></path>')
    k = min(w / 520, h / 230)
    o.append(cup(w * 0.38, ty + 14 * k, k * 0.8))
    lx = w * 0.62
    o.append(f'<path d="M{f(lx - 56 * k)} {f(ty + 14 * k)} C {f(lx - 60 * k)} {f(ty - 20 * k)} {f(lx - 20 * k)} {f(ty - 28 * k)} {f(lx - 6 * k)} {f(ty - 22 * k)} L {f(lx - 10 * k)} {f(ty + 14 * k)} Z" fill="#D9A25A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(lx + 4 * k)} {f(ty + 16 * k)} L {f(lx + 2 * k)} {f(ty - 22 * k)} C {f(lx + 20 * k)} {f(ty - 30 * k)} {f(lx + 62 * k)} {f(ty - 20 * k)} {f(lx + 60 * k)} {f(ty + 16 * k)} Z" fill="#D9A25A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(lx - 8 * k)} {f(ty - 18 * k)} l {f(-3 * k)} {f(30 * k)} M{f(lx + 4 * k)} {f(ty - 18 * k)} l {f(2 * k)} {f(30 * k)}" stroke="#F3E2B0" stroke-width="{f(3 * k)}"></path>')
    return "".join(o)

def idol_court(w, h, seed):
    """The things which the Gentiles sacrifice: an idol's temple at night, its altar cold and its table bare, the image in
    the dark of the doors — no one there (10:20–21 are words only)."""
    b = h * 0.92
    o = [sky(w, h, "#05051A", "#2A2040"), mk.stars(26, w, h * 0.3, seed), pavement(w, h, b, color="#3A3440", line="#2A2430")]
    o.append(_temple_front(w * 0.3, b, w * 0.4, min(h * 0.86, w * 0.38), dark=True))
    o.append(S4.altar(w * 0.16, b, min(0.7, h / 360), fire=False, seed=seed))
    k = min(1.0, h / 240)
    o.append(EP.low_table(w * 0.76, b, 110 * k, k))
    return "".join(o)

def feast(p, w, h, seed):
    """If one of them that believe not biddeth you to a feast: the dining room of a house in Corinth, the table spread, the
    host in his toga bidding his guest sit, and one at the table pointing to a dish — This hath been offered in sacrifice."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), room(w, h, b, wall="#8A4A3A", floor="#4A3A2A"), lamp_glow(w * 0.5, h * 0.3, max(w, h) * 0.5, f"{p}fs", op=0.4)]
    k = min(1.0, h / 240)
    tx = w * 0.34
    o.append(EP.low_table(tx, b, w * 0.32, k * 1.1))
    for i in range(4):
        o.append(f'<ellipse cx="{f(tx + w * (0.05 + 0.075 * i))}" cy="{f(b - 35 * k)}" rx="{f(w * 0.028)}" ry="{f(5 * k)}" fill="#C8B488" stroke="{INK}" stroke-width="1.4"></ellipse>')
    o.append(f'<path d="M{f(tx + w * 0.17)} {f(b - 37 * k)} C {f(tx + w * 0.18)} {f(b - 50 * k)} {f(tx + w * 0.21)} {f(b - 50 * k)} {f(tx + w * 0.22)} {f(b - 37 * k)} Z" fill="#8A3A22" stroke="{INK}" stroke-width="1.4"></path>')
    s = fit(b, b - min(h * 0.72, 196))
    o.append(robed(p, w * 0.14, b, s, "#F3EFE6", skin="#E3B08A", hair="#4A3A2A", mantle="#2A4A6A", flip=True, up=[(-22, -158), (-46, -150), (-70, -150)]))
    o.append(folk(p, w * 0.86, b, s, 6))
    o.append(_seated_lap(w * 0.62, b - 4, s * 0.74, "#6A7A4A", None, "#3A2A1A", '<path d="M10 -96 L 60 -86" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M10 -96 L 60 -86" stroke="#6A7A4A" stroke-width="7" stroke-linecap="round"></path>', flip=True))
    return "".join(o)

# ---- 1 Corinthians 11 --------------------------------------------------------------------------------------------------
def praying(p, w, h, seed, stage="both"):
    """Every man praying … having his head covered … every woman praying … with her head unveiled: the church at prayer in
    a house by lamplight — a man praying with his head bare and his hands lifted, a woman praying with her veil over her
    head; stage "hair": the woman's long hair under her veil, a man with his hair cut short beside her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, h * 0.28, max(w, h) * 0.55, f"{p}pr", op=0.5),
         clay_lamp(w * 0.5, h * 0.3, max(0.6, h / 300))]
    s = fit(b, b - min(h * 0.72, 196))
    hand_up = [(-22, -158), (-34, -190), (-38, -222)]
    if stage == "both":
        o.append(robed(p, w * 0.3, b, s, "#5A6A7A", hair="#2A1A10", beard="#2A1A10", flip=True, up=hand_up))
        o.append(robed(p, w * 0.7, b, s * 0.94, "#7A5A6A", woman=True, veil="#2A2A4A", up=hand_up))
        o.append(seated(w * 0.1, b, s * 0.7, "#6A5A3A", head="#3A4A5A", beard="#3A2A1A") + seated(w * 0.9, b, s * 0.7, "#5A4A3A", head=None, beard="#8A847A", flip=True))
    else:
        long_hair = '<path d="M-16 -186 C -22 -170 -24 -140 -18 -120 L -10 -122 C -12 -140 -10 -160 -8 -176 Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="1.2"></path>'
        o.append(robed(p, w * 0.36, b, s, "#6A7A5A", hair="#2A1A10", beard="#2A1A10", flip=True))
        o.append(robed(p, w * 0.64, b, s * 0.94, "#8A6A7A", woman=True, veil="#E8E2D6", extra=long_hair))
    return "".join(o)

def divided_supper(p, w, h, seed):
    """Each one taketh before other his own supper; and one is hungry, and another is drunken: the dining room, a few at
    the laden table with their cups lifted, and by the door the poor of the church standing with empty hands."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#7A4A3A", floor="#4A3A2A"), lamp_glow(w * 0.3, h * 0.3, max(w, h) * 0.45, f"{p}ds", op=0.5)]
    k = min(1.0, h / 240)
    tx = w * 0.08
    o.append(EP.low_table(tx, b, w * 0.4, k * 1.1))
    for i in range(6):
        x = tx + w * (0.03 + 0.065 * i)
        o.append(loaf(x, b - 37 * k, k * 0.6) if i % 2 else cup(x, b - 33 * k, k * 0.14))
    s = fit(b, b - min(h * 0.72, 196))
    o.append(seated(w * 0.12, b, s * 0.72, "#8A3A5A", head=None, beard="#2A1A10") + seated(w * 0.42, b, s * 0.72, "#C8A040", head="#F3EFE6", beard="#5A4A3A", flip=True))
    dx, dw = w * 0.82, w * 0.14
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.16)}" width="{f(dw)}" height="{f(b - h * 0.16)}" fill="#1A1A2A" stroke="{INK}" stroke-width="2.6"></rect>')
    o.append(robed(p, w * 0.66, b, s * 0.94, "#7A7A6A", woman=True, veil="#4A4A3A") + robed(p, w * 0.78, b, s, "#8A8270", hair="#3A2A1A", beard="#3A2A1A")
             + robed(p, w * 0.9, b, s * 0.6, "#9A8A6A", hair="#3A2A1A"))
    return "".join(o)

def lords_supper(p, w, h, seed, stage="bread"):
    """The Lord Jesus in the night in which he was betrayed took bread: Matthew's last supper — Jesus at the table among the
    twelve under the lamps, the loaf broken in his hands (stage "bread") or the cup lifted ("cup")."""
    return supper(p, w, h, seed, bread=stage == "bread", cupup=stage == "cup")

def table_waiting(w, h, seed):
    """When ye come together to eat, wait one for another: the long table set with the loaves and the cups, the lamps lit
    and the door standing open to the street, no one yet come."""
    b = h * 0.9
    o = [room(w, h, b, wall="#6A4A3A", floor="#3A2A20"), lamp_glow(w * 0.42, b - h * 0.3, max(w, h) * 0.55, f"tw{seed}", op=0.5)]
    dx, dw = w * 0.8, w * 0.14
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.16)}" width="{f(dw)}" height="{f(b - h * 0.16)}" fill="#2A2050" stroke="{INK}" stroke-width="2.6"></rect>'
             + "".join(f'<circle cx="{f(dx + dw * (0.2 + 0.15 * i))}" cy="{f(h * (0.22 + 0.05 * (i % 3)))}" r="1.6" fill="#F3EFE6"></circle>' for i in range(5)))
    k = min(1.0, h / 240)
    tx = w * 0.08
    o.append(EP.low_table(tx, b, w * 0.64, k * 1.1))
    for i in range(9):
        x = tx + w * (0.04 + 0.07 * i)
        o.append(loaf(x, b - 37 * k, k * 0.6) if i % 2 == 0 else cup(x, b - 33 * k, k * 0.14))
    o.append(clay_lamp(w * 0.4, b - 40 * k, k * 0.9))
    return "".join(o)
