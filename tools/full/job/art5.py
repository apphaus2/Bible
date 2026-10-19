"""Drawings for Job 15–17 (Eliphaz's second speech and Job's answer)."""
from job.art4 import *
from job.art4 import f, K2, K3, sea, label
import exodus4 as E4

SHIELD = '<ellipse cx="22" cy="-110" rx="20" ry="26" fill="#B5844A" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="22" cy="-110" r="6" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></circle>'

def east_wind(w, h, seed):
    """Should a wise man fill himself with the east wind?: the hot wind off the desert driving the sand in long streamers
    over the dunes, the sun white."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#E8C890", "#F3E0B0"), sun(w * 0.12, h * 0.3, min(22, h * 0.06), color="#FFF4C2", op=0.3)]
    for i in range(3):
        y = h * (0.78 + i * 0.07)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 26)} {f(w * 0.6)} {f(y + 10)} {f(w + 10)} {f(y - 16)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#E8C88A", "#D8B070", "#C89A5A"][i]}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for i in range(24):
        y = r.uniform(h * 0.5, h * 0.9); x = r.uniform(-w * 0.2, w * 0.8); L = r.uniform(80, 220)
        o.append(f'<path d="M{f(x + L)} {f(y)} C {f(x + L * 0.6)} {f(y - 8)} {f(x + L * 0.3)} {f(y + 8)} {f(x)} {f(y)}" stroke="#F3E8D0" stroke-width="{r.uniform(1.5, 3.5):.1f}" opacity="0.6" fill="none"></path>')
    return "".join(o)

def charger(p, w, h, seed):
    """He runneth upon him with a stiff neck, with the thick bosses of his bucklers: a man of war charging up a slope with
    his spear and buckler into a storm-dark sky."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#1A1A2E", "#6A4A5A"), clouds(w, h * 0.5, seed, 7, color="#14142A", op=0.9, ry=0.07, h=h),
         P(f"M-10 {f(h + 10)} L -10 {f(h * 0.96)} L {f(w * 0.7)} {f(h * 0.76)} L {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} Z", "#4A3A3A")]
    s = fit(h * 0.94, h * 0.74)
    o.append(mk.person(p, round(w * 0.42), round(h * 0.93), s, body=SKIN, cloth="#7A2A1E", kind="Tunic", sw=3, extra=E4.SPEAR + SHIELD))
    return "".join(o)

def desolate(w, h, seed, flame=True):
    """He hath dwelt in desolate cities, in houses which no man inhabited, ready to become heaps; the flame shall dry up his
    branches: roofless houses and heaps of stones at dusk, a dead tree scorched black beside them."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A2A3A", "#C8805A"), ground(w, h, h * 0.84, "#8A6A4A", dy=0)]
    for i in range(5):
        x = w * (0.04 + i * 0.13); hh = h * r.uniform(0.08, 0.14)
        o.append(P(f"M{f(x)} {f(h * 0.88)} L {f(x)} {f(h * 0.88 - hh)} L {f(x + w * 0.04)} {f(h * 0.88 - hh * 0.7)} L {f(x + w * 0.07)} {f(h * 0.88 - hh)} L {f(x + w * 0.1)} {f(h * 0.88 - hh * 0.6)} L {f(x + w * 0.1)} {f(h * 0.88)} Z", "#A8886A")
                 + f'<rect x="{f(x + w * 0.03)}" y="{f(h * 0.88 - hh * 0.5)}" width="{f(w * 0.025)}" height="{f(hh * 0.5)}" fill="#1A1210"></rect>')
    o.append(S4.stone_heap(w * 0.74, h * 0.94, w * 0.16, h * 0.08, seed))
    tx = w * 0.9
    o.append(f'<path d="M{f(tx)} {f(h * 0.9)} L {f(tx)} {f(h * 0.62)} M{f(tx)} {f(h * 0.72)} L {f(tx - 30)} {f(h * 0.6)} M{f(tx)} {f(h * 0.68)} L {f(tx + 26)} {f(h * 0.58)}" stroke="#1A1210" stroke-width="6" fill="none" stroke-linecap="round"></path>')
    if flame: o.append(E.blaze(tx, h * 0.66, w * 0.05, h * 0.08, seed, n=4))
    return "".join(o)

def vine_olive(w, h, seed):
    """He shall shake off his unripe grape as the vine, and cast off his flower as the olive-tree: a vine on its stakes
    dropping green grapes, an olive tree shedding its white blossom in the wind."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), ground(w, h, h * 0.84, "#A88A5A", dy=0)]
    for i in range(3):
        x = w * (0.1 + i * 0.12)
        o.append(f'<path d="M{f(x)} {f(h * 0.94)} L {f(x)} {f(h * 0.68)}" stroke="#6A4A2A" stroke-width="4"></path>'
                 f'<path d="M{f(x)} {f(h * 0.74)} C {f(x + 20)} {f(h * 0.68)} {f(x + 40)} {f(h * 0.76)} {f(x + w * 0.12)} {f(h * 0.7)}" stroke="#4A6A2A" stroke-width="3" fill="none"></path>'
                 + "".join(f'<path d="M{f(x + 14 + k * 18)} {f(h * 0.72)} l -8 -8 l 10 -4 l 8 6 Z" fill="#4A8A3A" stroke="#0D0D0F" stroke-width="1"></path>' for k in range(3)))
    for i in range(16):
        x = w * r.uniform(0.08, 0.4); y = h * r.uniform(0.76, 0.96)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="3.4" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    ox = w * 0.72
    o.append(f'<path d="M{f(ox)} {f(h * 0.94)} C {f(ox - 10)} {f(h * 0.84)} {f(ox + 10)} {f(h * 0.78)} {f(ox)} {f(h * 0.7)}" stroke="#5A4A3A" stroke-width="10" fill="none"></path>'
             f'<ellipse cx="{f(ox)}" cy="{f(h * 0.64)}" rx="{f(w * 0.14)}" ry="{f(h * 0.1)}" fill="#7A9A6A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for i in range(30):
        x = ox + r.uniform(-0.2, 0.24) * w; y = h * r.uniform(0.6, 0.96)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="2.4" fill="#FFFFFF" stroke="#8A8A7A" stroke-width="0.6"></circle>')
    return "".join(o)

def mockers(p, w, h, seed):
    """They have gaped upon me with their mouth; they gather themselves together against me: a ring of dark figures about the
    ash heap pointing and jeering, Job small and bowed among them."""
    b = h * 0.97
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A3A3A", "#D8906A"), ground(w, h, h * 0.76, "#7A5A4A", dy=0), ash_mound(w * 0.5, b, w * 0.3, h * 0.08, seed)]
    o.append(seated_job(w * 0.5, b - h * 0.06, min(0.8, h * 0.18 / 140), shard=False))
    s = fit(b, max(h * 0.7, b - 200))
    for i, x in enumerate((0.08, 0.2, 0.32, 0.68, 0.8, 0.92)):
        fl = x > 0.5
        o.append(mk.person(p, round(w * x), round(b - (i % 2) * 6), s * (0.9 + 0.1 * (i % 2)), body="#1A1210", cloth="#2A2026", sw=2, flip=fl,
                           up=[(22, -158), (50, -150), (74, -160)] if i % 2 == 0 else None))
    return "".join(o)

def target(p, w, h, seed):
    """He hath set me up for his mark; his archers compass me round about: a lone post in an open field stuck with arrows,
    archers standing far off on the ridges all round."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A7A8A", "#E8C8A0"), hills(w, h, h * 0.76, seed, "#7A6A5A", amp=8, step=80), ground(w, h, h * 0.82, "#A8906A", dy=0)]
    cx = w * 0.5
    o.append(f'<path d="M{f(cx)} {f(h * 0.98)} L {f(cx)} {f(h * 0.72)}" stroke="#5A3A1E" stroke-width="8"></path>'
             f'<circle cx="{f(cx)}" cy="{f(h * 0.76)}" r="{f(h * 0.05)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></circle><circle cx="{f(cx)}" cy="{f(h * 0.76)}" r="{f(h * 0.025)}" fill="#B5121B"></circle>')
    for i in range(7):
        a = r.uniform(-0.6, 0.6); x = cx + r.uniform(-12, 12); y = h * 0.76 + r.uniform(-14, 14)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(math.cos(a) * 34 * (1 if i % 2 else -1))} {f(math.sin(a) * 20)}" stroke="#3A2214" stroke-width="2"></path>')
    s = fit(h * 0.78, h * 0.68)
    for x in (0.08, 0.2, 0.82, 0.94):
        o.append(mk.person(p, round(w * x), round(h * 0.79), s, body="#1A1210", cloth="#3A2A22", kind="Tunic", sw=2, flip=x > 0.5,
                           extra='<path d="M20 -170 C 40 -150 40 -110 20 -90" stroke="#3A2214" stroke-width="5" fill="none"></path>'))
    return "".join(o)

def witness(p, w, h, seed, jx=0.3):
    """Even now, behold, my witness is in heaven, and he that voucheth for me is on high: Job small upon the ash heap at
    night, looking up into a deep sky where one great light shines (no one is drawn in it)."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#05051A", "#2A1E50"), mk.stars(120, w, h * 0.8, seed),
         f'<circle cx="{f(w * (1 - jx))}" cy="{f(h * 0.6)}" r="{f(h * 0.6)}" fill="#FFF4C2" opacity="0.08"></circle>',
         V.rays(w * (1 - jx), h * 0.3, 24, 8, h * 0.7, color="#FFF4C2", op=0.15), f'<circle cx="{f(w * (1 - jx))}" cy="{f(h * 0.6)}" r="6" fill="#FFFFFF"></circle>',
         ground(w, h, h * 0.88, "#1A1A28", dy=0), ash_mound(w * jx, h * 0.99, w * 0.3, h * 0.08, seed)]
    o.append(seated(w * jx, h * 0.93, min(0.8, h * 0.18 / 140), SACK, head=SACK, ash=True, shard=False))
    return "".join(o)

def road_away(w, h, seed):
    """I shall go the way whence I shall not return: a road running out over the hills into the dusk and the dark."""
    o = [K2.sky(w, h, "#1A1A3A", "#C8805A"), hills(w, h, h * 0.74, seed, "#3A2A3A", amp=10, step=90), ground(w, h, h * 0.8, "#5A4A3A", dy=0),
         P(f"M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.9)} {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.58)} {f(h * 0.8)} L {f(w * 0.6)} {f(h * 0.8)} C {f(w * 0.64)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.94)} {f(w * 0.56)} {f(h + 10)} Z", "#A8906A", 1.6)]
    return "".join(o)

def open_tomb(w, h, seed):
    """My days are extinct, the grave is ready for me: a tomb hewn in the rock face, its door open and dark, the round stone
    rolled aside, at evening."""
    o = [K2.sky(w, h, "#3A2A4A", "#E8A06A"), P(f"M-10 {f(h * 0.6)} L {f(w * 0.8)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#8A6A5A")]
    dx, dw, dh = w * 0.36, w * 0.12, h * 0.2
    o.append(P(f"M{f(dx)} {f(h * 0.94)} L {f(dx)} {f(h * 0.94 - dh * 0.7)} Q {f(dx + dw / 2)} {f(h * 0.94 - dh * 1.1)} {f(dx + dw)} {f(h * 0.94 - dh * 0.7)} L {f(dx + dw)} {f(h * 0.94)} Z", "#120A0A"))
    o.append(f'<circle cx="{f(dx + dw * 1.8)}" cy="{f(h * 0.94 - dh * 0.4)}" r="{f(dh * 0.42)}" fill="#A89A8A" stroke="#0D0D0F" stroke-width="2.4"></circle>'
             + ground(w, h, h * 0.94, "#6A5A4A", dy=0))
    return "".join(o)

def strike_hands(w, h, seed):
    """Give now a pledge, be surety for me; who is there that will strike hands with me?: two hands clasped in pledge, the
    sleeves of two robes, against a plain ground."""
    o = [rect(w, h, "#5A4A3A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.82)}" r="{f(h * 0.2)}" fill="#FFC14D" opacity="0.15"></circle>']
    k = min(1.6, h / 240); cx, cy = w * 0.5, h * 0.84
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(k)})">'
             + P("M-160 10 L -40 -6 L -36 18 L -160 34 Z", SACK) + P("M160 10 L 40 -6 L 36 18 L 160 34 Z", FRIEND_C["eli"])
             + P("M-44 -8 C -30 -16 -10 -14 4 -8 L 10 2 C 0 6 -14 4 -20 12 L -40 20 Z", "#C98E66")
             + P("M44 -6 C 30 -18 10 -18 -6 -12 L -10 0 C 0 2 12 2 16 12 L 40 20 Z", "#B98A6E")
             + '<path d="M-6 -12 C 0 -4 4 4 2 10 M4 -14 C 10 -6 12 2 10 8" stroke="#0D0D0F" stroke-width="1.2" fill="none"></path></g>')
    return "".join(o)

def twilight(w, h, seed):
    """They change the night into day; the light, say they, is near unto the darkness: a sky split down the middle, day at
    one side and night with its stars at the other, over the same hills."""
    o = [f'<rect x="-10" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#8FD0E2"></rect><rect x="{f(w / 2)}" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>',
         mk.stars(40, w / 2, h * 0.8, seed).replace("<g ", f'<g transform="translate({f(w / 2)} 0)" '), sun(w * 0.2, h * 0.7, min(22, h * 0.06), op=0.3),
         J.moon(w * 0.82, h * 0.68, min(16, h * 0.05)), hills(w, h, h * 0.84, seed, "#3A3A4A", amp=10, step=80),
         f'<path d="M{f(w / 2)} -10 L {f(w / 2)} {f(h * 0.82)}" stroke="#0D0D0F" stroke-width="2.4"></path>']
    return "".join(o)

def sheol_bars(w, h, seed):
    """It shall go down to the bars of Sheol, when once there is rest in the dust: a stair of rock going down into the dark,
    and at its foot gates of bars, shut."""
    o = [rect(w, h, "#05050A"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.36)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2420"></path>',
         f'<path d="M{f(w + 10)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.5)} L {f(w * 0.64)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2420"></path>']
    for i in range(7):
        y = h * (0.5 + i * 0.06); x0 = w * (0.3 + i * 0.01); x1 = w * (0.7 - i * 0.01)
        o.append(f'<rect x="{f(x0)}" y="{f(y)}" width="{f(x1 - x0)}" height="{f(h * 0.03)}" fill="{["#5A5048", "#4A4038", "#3A322C"][i % 3]}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    gx0, gx1, gy = w * 0.4, w * 0.6, h * 0.92
    o.append(f'<rect x="{f(gx0)}" y="{f(gy - h * 0.12)}" width="{f(gx1 - gx0)}" height="{f(h * 0.14)}" fill="#0B0B12" stroke="#5A5A6A" stroke-width="3"></rect>'
             + "".join(f'<path d="M{f(gx0 + (gx1 - gx0) * k / 8)} {f(gy - h * 0.12)} L {f(gx0 + (gx1 - gx0) * k / 8)} {f(gy + h * 0.02)}" stroke="#6A6A7A" stroke-width="3"></path>' for k in range(1, 8))
             + f'<path d="M{f(gx0)} {f(gy - h * 0.05)} L {f(gx1)} {f(gy - h * 0.05)}" stroke="#6A6A7A" stroke-width="4"></path>')
    return "".join(o)
