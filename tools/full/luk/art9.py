"""Drawings for Luke 14–15: the ruler's house on the sabbath and the man with the dropsy; the excuses — a field, five yoke
of oxen, a wedding; the tower begun and not finished; the shepherd carrying home the lost sheep on his shoulders; the woman
with her lamp and broom seeking the lost piece of silver; and the prodigal son — the portion divided, the far country lit
at night (the riotous living in words only), the famine, the swine in a bare field and the young man among them in a torn
grey tunic, the road home, the father running to him while he was yet afar off, the best robe, the ring and the shoes, the
house lit with music and dancing, the elder brother angry in the field and his father come out to entreat him. Built on
luk.art8."""
from luk.art8 import *
from luk.art8 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig, RICH_C, rich_fig, barn
import random, math

SON_C, SON_RAGS, ROBE_BEST = "#C8A878", "#7A7A7E", "#F3EFE6"
FATHER_C, ELDER_C = "#1F3A6A", "#6A4A2A"

def son_fig(p, x, y, s, rags=False, best=False, flip=False, up=None):
    """The younger son: bareheaded, brown hair and a short beard; a sand tunic; rags=True a torn grey tunic; best=True the
    best robe, white with a gold border, a ring on his hand."""
    hair = '<path d="M-13.5 -186 C -16 -205 16 -205 13.5 -186 L 14 -178 C 10 -192 -10 -192 -14 -178 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.3"></path>'
    tear = ""
    hem = '<path d="M-26 -8 L 26 -8" stroke="#E8B830" stroke-width="5"></path>' if best else ""
    return mk.person(p, round(x), round(y), round(s, 3), body="#C98E66", cloth=SON_RAGS if rags else ROBE_BEST if best else SON_C, kind="Tunic" if not best else "Robe",
                     sw=3, flip=flip, up=up, extra=hair + A.BLACK_BEARD.replace("#2A1A10", "#3A2214") + tear + hem)

def father_fig(p, x, y, s, flip=False, up=None):
    """The father: a dark-blue robe and headcloth, a white beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#C98E66", cloth=FATHER_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#2A4A7A", cord="#E8B830") + A.WHITE_BEARD)

def elder_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=ELDER_C, kind="Tunic", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#6A4A2A") + A.BLACK_BEARD)

def farm(w, h, seed, tone="day", lit=False):
    """The father's house among its fields: a large house with an upper room and a courtyard wall, olive trees, the hills."""
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#4A3A6A", "#FFB07A"), "night": ("#0B0B2A", "#2A2050")}[tone]
    o = [sky(w, h, top, bot)]
    if tone == "night": o.append(mk.stars(50, w, h * 0.4, seed))
    o += [hills(w, h, h * 0.46, seed, color="#8A9A6A" if tone == "day" else "#3A3448", amp=14, step=80), ground(w, h, h * 0.62, "#B8A06A" if tone == "day" else "#4A4038", dy=0)]
    hx0, hx1, top_ = w * 0.56, w * 0.98, h * 0.3
    o.append(f'<rect x="{f(hx0)}" y="{f(top_)}" width="{f(hx1 - hx0)}" height="{f(h * 0.62 - top_)}" fill="{"#E0CFA8" if tone == "day" else "#7A6A5A"}" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 + w * 0.08)}" y="{f(top_ - h * 0.1)}" width="{f(w * 0.16)}" height="{f(h * 0.1)}" fill="{"#D8C098" if tone == "day" else "#6A5A4A"}" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(hx0 + w * 0.14)} {f(h * 0.62)} L {f(hx0 + w * 0.14)} {f(h * 0.48)} Q {f(hx0 + w * 0.18)} {f(h * 0.43)} {f(hx0 + w * 0.22)} {f(h * 0.48)} L {f(hx0 + w * 0.22)} {f(h * 0.62)} Z" fill="{"#FFC14D" if lit else "#3A2A1E"}" stroke="{INK}" stroke-width="2"></path>')
    for x in (hx0 + w * 0.04, hx0 + w * 0.32):
        o.append(f'<rect x="{f(x)}" y="{f(top_ + h * 0.08)}" width="{f(w * 0.05)}" height="{f(h * 0.06)}" fill="{"#FFC14D" if lit else "#3A2A1E"}" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(olive(w * 0.08, h * 0.66, max(0.4, h / 600), seed=seed) + olive(w * 0.24, h * 0.64, max(0.35, h / 700), seed=seed + 1))
    return "".join(o)

def dropsy(p, w, h, seed, healed=False):
    """In the house of one of the rulers of the Pharisees on a sabbath: the Pharisees seated about the table watching; before
    Jesus a man standing heavily, swollen with the dropsy, his robe loose about him (healed=True: the man going out at the
    door, upright)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.08, w * 0.08)), A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300))]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(b - 36 * s)}" width="{f(w * 0.36)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i, x in enumerate((0.6, 0.72, 0.84, 0.95)):
        o.append(seated(w * x, b, s * 0.76, "#E8E2D6" if i % 2 == 0 else "#3A4A6A", head="#F3EFE6" if i % 2 == 0 else "#3A4A6A", beard="#6A645E", band=True, flip=True))
    o.append(jesus(p, w * 0.22, b, s, flip=True, up=UP_BLESS))
    if healed:
        o.append(f'<path d="M{f(w * 0.02)} {f(b)} L {f(w * 0.02)} {f(b - 220 * s)} L {f(w * 0.1)} {f(b - 220 * s)} L {f(w * 0.1)} {f(b)} Z" fill="#FFE6B0" stroke="{INK}" stroke-width="2"></path>')
        o.append(man(p, w * 0.08, b, s * 0.92, "#7A6A5A"))
    else:
        o.append(mk.person(p, round(w * 0.4), round(b), round(s * 0.96, 3), body=SKIN, cloth="#7A6A5A", kind="Robe", sw=3, flip=True,
                           extra='<ellipse cx="0" cy="-90" rx="34" ry="44" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>' + A.headcloth("#8A7A6A")))
    return "".join(o)

def excuses(p, w, h, seed):
    """They all with one consent began to make excuse: three frames side by side — a field newly bought, with its boundary
    stones; five yoke of oxen under their yokes; a wedding canopy hung with lamps — each one's reason."""
    o = [bgr(w, h, "#2A2030")]
    fw, gap = (w - 48) / 3, 12
    for i in range(3):
        x0 = 12 + i * (fw + gap)
        inner = []
        if i == 0:
            inner += [sky(fw, h - 24, "#8FD0E2", "#F3E8C8"), ground(fw, h - 24, (h - 24) * 0.5, "#9AAA5A", dy=0)]
            for k in range(4):
                inner.append(f'<rect x="{f(fw * (0.12 + 0.24 * k))}" y="{f((h - 24) * 0.62)}" width="10" height="16" fill="#B8B0A0" stroke="{INK}" stroke-width="1.4"></rect>')
            inner.append(grain(0, fw, (h - 24) * 0.96, (h - 24) * 0.2, seed))
        elif i == 1:
            import samuel1 as S1
            inner += [sky(fw, h - 24, "#8FD0E2", "#F3E8C8"), ground(fw, h - 24, (h - 24) * 0.5, "#B8A06A", dy=0)]
            for k in range(5):
                inner.append(S1.cow(fw * (0.22 + 0.14 * k), (h - 24) * (0.66 + 0.06 * (k % 2)), max(0.14, h / 2000), color=["#8A5A30", "#5A3A22", "#C9A27A"][k % 3], patch="#8A5A30"))
        else:
            inner += [bgr(fw, h - 24, "#3A1A2A"), f'<path d="M{f(fw * 0.1)} {f((h - 24) * 0.3)} C {f(fw * 0.3)} {f((h - 24) * 0.16)} {f(fw * 0.7)} {f((h - 24) * 0.16)} {f(fw * 0.9)} {f((h - 24) * 0.3)}" stroke="#E8B830" stroke-width="4" fill="none"></path>']
            for k in range(5):
                lx = fw * (0.14 + 0.18 * k); ly = (h - 24) * (0.3 - 0.1 * math.sin(math.pi * (k / 4)))
                inner.append(glow(lx, ly + 10, 18, "#FFE680", 0.9, f"{p}w{k}") + f'<circle cx="{f(lx)}" cy="{f(ly + 10)}" r="4" fill="#FFE680"></circle>')
            inner.append(f'<path d="M{f(fw * 0.16)} {f(h - 24)} L {f(fw * 0.16)} {f((h - 24) * 0.3)} M{f(fw * 0.84)} {f(h - 24)} L {f(fw * 0.84)} {f((h - 24) * 0.3)}" stroke="#E8B830" stroke-width="5"></path>')
        o.append(f'<g transform="translate({f(x0)} 12)"><svg width="{f(fw)}" height="{f(h - 24)}" viewBox="0 0 {f(fw)} {f(h - 24)}" overflow="hidden">{"".join(inner)}</svg>'
                 f'<rect x="0" y="0" width="{f(fw)}" height="{f(h - 24)}" fill="none" stroke="#F3EFE6" stroke-width="3"></rect></g>')
    return "".join(o)

def tower_cost(p, w, h, seed):
    """Desiring to build a tower, doth not first sit down and count the cost?: a tower's foundation and its first courses of
    stone standing unfinished in a vineyard, the scaffold poles bare; a man sitting on a stone with a tally, counting."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=12, step=80), ground(w, h, h * 0.62, "#B8A06A", dy=0),
         vines(w * 0.02, w * 0.4, h * 0.74, h * 0.9, seed, rows=2)]
    tx, tw = w * 0.66, w * 0.22
    for k in range(4):
        y = b - k * h * 0.07; inset = 0
        o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(y - h * 0.07)}" width="{f(tw)}" height="{f(h * 0.07)}" fill="#C8B088" stroke="{INK}" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(tx - tw / 2 + tw * m / 5 + (k % 2) * tw / 10)} {f(y - h * 0.07)} L {f(tx - tw / 2 + tw * m / 5 + (k % 2) * tw / 10)} {f(y)}" stroke="#8A7A5A" stroke-width="1.4"></path>' for m in range(1, 5)))
    for x in (tx - tw * 0.6, tx + tw * 0.6):
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(h * 0.2)}" stroke="#6A4A2A" stroke-width="4"></path>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(seated(w * 0.42, b, s * 0.8, "#6A5A3A", head="#6A5A3A", beard="#2A1A10"))
    return "".join(o)

def on_shoulders(p, w, h, seed):
    """When he hath found it, he layeth it on his shoulders, rejoicing: the shepherd coming home down the hill at evening with
    the lost sheep across his shoulders, his friends and neighbors at the fold with their arms lifted."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFC890"), hills(w, h, h * 0.44, seed, color="#7A7A5A", amp=18, step=70), ground(w, h, h * 0.62, "#8AAA4A", dy=-6)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(shepherd_fig(p, w * 0.34, b, s, 0, up=[(-22, -158), (-30, -176), (-14, -184)]))
    o.append(E.sheep(w * 0.34 - 4 * s, b - 186 * s, s * 0.34))
    for i, x in enumerate((0.66, 0.78, 0.9)):
        o.append(man(p, w * x, b, s * 0.94, HEB[i], flip=True, up=UP_HIGH) if i != 1 else woman_fig(p, w * x, b, s * 0.9, "#6A3A4A", "#8A5A3A", flip=True, up=UP_HIGH))
    return "".join(o)

def lost_coin(p, w, h, seed, found=False):
    """Ten pieces of silver: within a dim house, a woman with a lamp held low and a broom of twigs, sweeping the floor, a
    small coin shining in a corner; found=True: the coin held up in the lamplight, her friends and neighbors come in."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#5A4A48", floor="#4A3A30"), glow(w * 0.4, b - 30, h * 0.4, "#FFE680", 0.5, f"{p}g")]
    s = fit(b, max(h * 0.2, b - 230))
    if found:
        o.append(woman_fig(p, w * 0.4, b, s, "#6A3A4A", "#2A5A5A", up=UP_HIGH))
        o.append(f'<circle cx="{f(w * 0.4 - 46 * s)}" cy="{f(b - 230 * s)}" r="{f(7 * s)}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.4"></circle>' + glow(w * 0.4 - 46 * s, b - 230 * s, 30 * s, "#FFFDF0", 0.9, f"{p}c"))
        for i, x in enumerate((0.64, 0.76, 0.88)):
            o.append(woman_fig(p, w * x, b, s * 0.9, ["#4A5A3A", "#7A5A3A", "#3A4A6A"][i], ["#5A6A4A", "#8A6A2A", "#4A5A7A"][i], flip=True, up=UP_HIGH if i == 1 else None))
    else:
        o.append(f'<path d="M{f(w * 0.36)} {f(b - 110 * s)} L {f(w * 0.2)} {f(b)}" stroke="#8A6A3A" stroke-width="{f(5 * s)}"></path>'
                 f'<path d="M{f(w * 0.2)} {f(b)} l -24 -6 M{f(w * 0.2)} {f(b)} l -26 2 M{f(w * 0.2)} {f(b)} l -20 -14" stroke="#A88A4A" stroke-width="3"></path>')
        o.append(woman_fig(p, w * 0.4, b, s, "#6A3A4A", "#2A5A5A", up=[(-22, -158), (-36, -120), (-40, -100)]))
        o.append(A.lamp(w * 0.5, b - 70 * s, s * 0.6) + glow(w * 0.5, b - 80 * s, 50 * s, "#FFE680", 0.8, f"{p}l"))
        o.append(f'<circle cx="{f(w * 0.86)}" cy="{f(b - 4)}" r="{f(5 * s)}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.2"></circle>' + glow(w * 0.86, b - 4, 16 * s, "#FFFDF0", 0.8, f"{p}c"))
    return "".join(o)

def prodigal(p, w, h, seed, stage="portion"):
    """The prodigal son, scene by scene (stage): 'portion' at the father's house, the father counting out the son's portion
    into his bag; 'far' the young man on the road at evening toward a far city lit all night (his riotous living in words
    only); 'famine' the far country in famine, cracked fields, a dead tree; 'swine' a bare field with the swine feeding,
    the young man sitting among them in a torn grey tunic, a pod of husks in his hand; 'arise' he stands up and turns back
    on the road; 'run' the father running down the road from his house toward his son while he is yet afar off; 'embrace'
    the father's arms about his son's neck; 'robe' the servants bringing out the best robe, the son in it, the father by; 'feast'
    the house lit at night, music and dancing within (lamps, a pipe and a timbrel at the window); 'elder' the elder son
    coming in from the field at dusk, a servant at the gate telling him; 'entreat' the father come out to the angry son."""
    b = h * 0.94
    s = fit(b, max(h * 0.24, b - 230))
    if stage in ("portion", "run", "embrace", "robe", "elder", "entreat"):
        tone = "dusk" if stage in ("elder", "entreat") else "day"
        o = [mk.defs(p, *ALL), farm(w, h, seed, tone=tone, lit=stage in ("elder", "entreat"))]
    elif stage == "feast":
        o = [mk.defs(p, *ALL), farm(w, h, seed, tone="night", lit=True)]
    elif stage == "far":
        o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A"), hills(w, h, h * 0.56, seed, color="#3A2A3A", amp=10, step=80),
             walls(w * 0.56, w * 0.98, h * 0.6, h * 0.24, seed, lit=True, towers=3, color="#6A4A4A"), glow(w * 0.77, h * 0.5, h * 0.3, "#FFC14D", 0.5, f"{p}g"),
             ground(w, h, h * 0.64, "#5A3A3A", dy=0)]
    else:
        r = random.Random(seed)
        o = [mk.defs(p, *ALL), sky(w, h, "#C8B898", "#E8D8B0"), hills(w, h, h * 0.5, seed, color="#A8906A", amp=10, step=90), ground(w, h, h * 0.58, "#B89A6A", dy=0)]
        for _ in range(16):
            x, y = r.uniform(0, w), r.uniform(h * 0.64, h)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 24))} {f(r.uniform(-4, 4))} l {f(r.uniform(6, 14))} {f(r.uniform(4, 10))}" stroke="#7A5A3A" stroke-width="1.6" fill="none"></path>')
        o.append(fig_tree(w * 0.88, h * 0.7, max(0.4, h / 500), bare=True, fruit=False, seed=seed))
    if stage == "portion":
        o.append(father_fig(p, w * 0.48, b, s, up=[(-22, -158), (-40, -136), (-58, -128)]))
        o.append(son_fig(p, w * 0.32, b, s * 0.96, flip=True, up=[(-22, -158), (-40, -136), (-50, -128)]))
        o.append(f'<path d="M{f(w * 0.4 - 6)} {f(b - 122 * s)} C {f(w * 0.4 - 14)} {f(b - 104 * s)} {f(w * 0.4 + 14)} {f(b - 104 * s)} {f(w * 0.4 + 6)} {f(b - 122 * s)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(elder_fig(p, w * 0.12, b, s * 0.96))
    elif stage == "far":
        o.append(son_fig(p, w * 0.3, b, s, flip=True))
    elif stage == "famine":
        o.append(son_fig(p, w * 0.4, b, s * 0.9, up=[(-22, -158), (-16, -176), (-6, -186)]))
    elif stage == "swine":
        for i in range(7):
            x = w * (0.06 + 0.12 * i); y = h * (0.72 + 0.06 * (i % 3))
            o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(max(0.3, h / 900))})"><path d="M-40 0 C -44 -30 -10 -40 20 -34 C 40 -30 50 -16 46 0 L 40 0 L 38 10 L 30 10 L 30 0 L -24 0 L -26 10 L -34 10 Z" fill="#B8908A" stroke="#0D0D0F" stroke-width="2"></path>'
                     '<path d="M44 -14 L 54 -12 L 52 -4 Z" fill="#B8908A" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
        o.append(seated(w * 0.56, b, s * 0.82, SON_RAGS, head=None, beard="#3A2214", bowed=True))
    elif stage == "arise":
        o.append(son_fig(p, w * 0.5, b, s, rags=True, flip=True))
    elif stage == "run":
        o.append(father_fig(p, w * 0.5, b - 10, s * 0.9, up=[(-22, -158), (-44, -172), (-64, -180)]))
        o.append(son_fig(p, w * 0.12, h * 0.74, s * 0.5, rags=True, flip=False))
    elif stage == "embrace":
        o.append(glow(w * 0.4, b - 120 * s, 150 * s, "#FFF4C2", 0.6, f"{p}g"))
        o.append(son_fig(p, w * 0.34, b, s * 0.94, rags=True, flip=True, up=[(-22, -158), (-40, -150), (-50, -160)]))
        o.append(father_fig(p, w * 0.44, b, s, up=[(-22, -158), (-44, -168), (-60, -164)]))
    elif stage == "robe":
        o.append(son_fig(p, w * 0.36, b, s * 0.96, best=True))
        o.append(father_fig(p, w * 0.5, b, s, up=UP_BLESS))
        o.append(man(p, w * 0.2, b, s * 0.9, "#7A6A4A", flip=True, up=[(-22, -158), (-40, -136), (-56, -128)]))
        o.append(man(p, w * 0.08, b, s * 0.88, "#5A6A4A", flip=True))
    elif stage == "feast":
        for k in range(3):
            o.append(glow(w * (0.62 + 0.12 * k), h * 0.4, 40, "#FFE680", 0.6, f"{p}f{k}"))
    elif stage == "elder":
        o.append(elder_fig(p, w * 0.22, b, s, flip=True))
        o.append(man(p, w * 0.4, b, s * 0.9, "#7A6A4A", up=UP_BLESS))
    elif stage == "entreat":
        o.append(elder_fig(p, w * 0.26, b, s, up=[(-22, -158), (-40, -136), (-30, -120)]))
        o.append(father_fig(p, w * 0.42, b, s, up=UP_BLESS))
    return "".join(o)
