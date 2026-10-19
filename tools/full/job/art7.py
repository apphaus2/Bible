"""Drawings for Job 21–24 (Job's answer to Zophar, Eliphaz's third speech, and Job's answer)."""
from job.art6 import *
from job.art6 import f, K2, K3, sea, label, SHIELD
import samuel2 as S2, samuel3 as S3, ruth1 as R1

def prosper(p, w, h, seed):
    """Wherefore do the wicked live, become old, yea, wax mighty in power? their houses are safe from fear: a great house in
    the evening light, its gate open, children before it and the herds coming home."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A8AB8", "#F3D8A0"), hills(w, h, h * 0.78, seed, "#7A8A5A", amp=8, step=90), ground(w, h, h * 0.84, "#A8B86A", dy=0),
         house(w * 0.08, h * 0.9, w * 0.24, h * 0.14, lit=True, color="#D8B88A"), flock(w * 0.6, w * 0.96, h * 0.86, h * 0.96, 10, seed, cows=0.5, smin=0.14, smax=0.22)]
    s = fit(h * 0.97, h * 0.8)
    for i in range(4): o.append(man(p, w * (0.38 + i * 0.05), h * 0.97, s * (0.7 + 0.08 * (i % 2)), ["#C8506A", "#2C4A7A", "#D8A040", "#5A8A3A"][i]))
    return "".join(o)

def dancing(p, w, h, seed):
    """They send forth their little ones like a flock, and their children dance; they sing to the timbrel and harp, and
    rejoice at the sound of the pipe: children dancing in a ring, a man with a harp and a girl with a timbrel."""
    o = [mk.defs(p, *ALL, "WomanUp"), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.8, "#C8B07A", dy=0)]
    s = fit(h * 0.97, h * 0.8)
    for i in range(6):
        a = 2 * math.pi * i / 6; x = w * 0.46 + math.cos(a) * w * 0.12; y = h * 0.93 + math.sin(a) * h * 0.035
        o.append(mk.person(p, round(x), round(y), round(s * 0.62, 3), body=SKIN, cloth=["#C8506A", "#2C4A7A", "#D8A040", "#5A8A3A", "#8A4AB8", "#B5421E"][i], kind="Tunic", sw=3,
                           flip=i % 2 == 1, up=[(-22, -158), (-46, -184), (-58, -214)]))
    o.append(man(p, w * 0.14, h * 0.97, s, "#5A3A6A") + S2.harp(w * 0.18, h * 0.9, min(0.5, h / 600)))
    o.append(mk.person(p, round(w * 0.8), round(h * 0.97), round(s * 0.92, 3), body=SKIN, cloth="#B5121B", woman=True, hair="#1A1210", sw=3, flip=True, up=[(22, -158), (44, -190), (52, -224)])
             + S3.timbrel(w * 0.8 - 52 * s * 0.92, h * 0.97 - 230 * s * 0.92, min(0.8, h / 400)))
    return "".join(o)

def chaff(w, h, seed):
    """As stubble before the wind, and as chaff that the storm carrieth away: a threshing-floor on a hill under a storm sky,
    the chaff and straw torn off it in a long streamer."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A3A4A", "#8A8070"), hills(w, h, h * 0.8, seed, "#5A5040", amp=8, step=90), S4.threshing_floor(w * 0.3, h * 0.92, w * 0.36)]
    for i in range(120):
        t = r.random(); x = w * (0.3 + t * 0.7) + r.uniform(-20, 20); y = h * (0.9 - t * 0.3) + r.uniform(-14, 14) * (1 + t * 3)
        o.append(f'<path d="M{f(x)} {f(y)} l 8 -2" stroke="#E8D090" stroke-width="2" opacity="{0.9 - t * 0.6:.2f}"></path>')
    return "".join(o)

def two_graves(w, h, seed):
    """One dieth in his full strength, another in bitterness of soul; they lie down alike in the dust: two graves side by
    side at evening, one with a full milk-pail left at its head, one bare."""
    o = [K2.sky(w, h, "#4A3A5A", "#E8A06A"), ground(w, h, h * 0.84, "#8A6A4A", dy=0)]
    for x in (0.3, 0.64):
        o.append(P(f"M{f(w * x - w * 0.14)} {f(h * 0.94)} C {f(w * x - w * 0.1)} {f(h * 0.86)} {f(w * x + w * 0.1)} {f(h * 0.86)} {f(w * x + w * 0.14)} {f(h * 0.94)} Z", "#A88A6A")
                 + S4.stone_heap(w * x, h * 0.94, w * 0.18, h * 0.05, seed + int(x * 10)))
    k = min(1.0, h / 300)
    o.append(f'<g transform="translate({f(w * 0.1)} {f(h * 0.96)}) scale({f(k)})">' + P("M-16 0 L -20 -34 L 20 -34 L 16 0 Z", "#8A6A4A") + '<ellipse cx="0" cy="-34" rx="20" ry="5" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></ellipse></g>')
    return "".join(o)

def wayfarers(p, w, h, seed):
    """Have ye not asked wayfaring men? and do ye not know their evidences: travellers with staffs and laden asses resting
    by the road, pointing back the way they came."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB8D8", "#F3E0B0"), hills(w, h, h * 0.78, seed, "#A88A6A", amp=10, step=90), ground(w, h, h * 0.84, "#C8A87A", dy=0),
         P(f"M-10 {f(h * 0.92)} C {f(w * 0.4)} {f(h * 0.86)} {f(w * 0.7)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h * 0.9)} C {f(w * 0.7)} {f(h * 0.94)} {f(w * 0.4)} {f(h * 0.9)} -10 {f(h * 0.97)} Z", "#E0C8A0", 1.4)]
    s = fit(h * 0.97, h * 0.76)
    o.append(man(p, w * 0.3, h * 0.97, s, "#5A4A3A", up=[(-22, -158), (-50, -166), (-78, -176)], extra='<path d="M30 -170 L 34 6" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(man(p, w * 0.42, h * 0.97, s * 0.95, "#3A4A6A", flip=True, extra='<path d="M-50 -170 L -46 6" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(N.ass(w * 0.6, h * 0.97, min(0.3, h / 900), color="#8A8478"))
    return "".join(o)

def turned_away(p, w, h, seed):
    """Thou hast sent widows away empty, and the arms of the fatherless have been broken: a widow in dark clothes leading
    her child away from a shut door, empty-handed (Eliphaz's charge)."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A6A7A", "#D8C0A0"), ground(w, h, h * 0.86, "#8A7A5A", dy=0), house(w * 0.06, h * 0.92, w * 0.28, h * 0.18, color="#C8A878")]
    s = fit(h * 0.97, h * 0.76)
    o.append(mk.person(p, round(w * 0.6), round(h * 0.97), s, body=SKIN, cloth="#2A2A30", woman=True, hair="#1A1210", sw=3, flip=False)
             + mk.person(p, round(w * 0.68), round(h * 0.97), round(s * 0.55, 3), body=SKIN, cloth="#5A4A3A", kind="Tunic", sw=3))
    return "".join(o)

def stars_clouds(w, h, seed):
    """Is not God in the height of heaven? behold the height of the stars; thick clouds are a covering to him: the deep night
    full of stars above, and banks of thick cloud rolling under them (no one is drawn)."""
    o = [K2.sky(w, h, "#05051A", "#2A2A4A"), mk.stars(200, w, h * 0.9, seed), clouds(w, h * 0.8, seed, 10, color="#3A3A5A", op=0.95, ry=0.07, h=h),
         clouds(w, h * 0.92, seed + 1, 10, color="#2A2A3E", op=0.95, ry=0.07, h=h)]
    return "".join(o)

def gold_brook(w, h, seed):
    """Lay thou thy treasure in the dust, and the gold of Ophir among the stones of the brooks: a shallow brook running over
    stones, gold glinting among them."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), ground(w, h, h * 0.8, "#9A8A5A", dy=0),
         P(f"M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#5AA8C8")]
    for i in range(22):
        o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(0.88, 1.0))}" rx="{f(r.uniform(6, 14))}" ry="{f(r.uniform(4, 7))}" fill="#A8A098" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    for i in range(12):
        x = r.uniform(0, w); y = h * r.uniform(0.88, 1.0)
        o.append(f'<path d="M{f(x - 5)} {f(y)} L {f(x)} {f(y - 4)} L {f(x + 6)} {f(y)} L {f(x)} {f(y + 3)} Z" fill="#FFD23F" stroke="#8A6A1A" stroke-width="1"></path><circle cx="{f(x)}" cy="{f(y - 2)}" r="8" fill="#FFF4C2" opacity="0.3"></circle>')
    return "".join(o)

def four_ways(w, h, seed):
    """Behold, I go forward, but he is not there; and backward, but I cannot perceive him; on the left hand, on the right
    hand: a compass of four ways drawn as a technical plan, Job's place at the centre, every arm marked empty."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.74
    L = min(w * 0.36, h * 0.14)
    for dx, dy, nm in ((0, -1, "FORWARD"), (0, 1, "BACKWARD"), (-1, 0, "LEFT HAND"), (1, 0, "RIGHT HAND")):
        x1, y1 = cx + dx * L * (2.2 if dx else 1), cy + dy * L
        o.append(route([(cx, cy), (x1, y1)], color="#8FD0E2", sw=2.4))
        o.append(f'<circle cx="{f(x1)}" cy="{f(y1)}" r="10" fill="none" stroke="#FF8A6A" stroke-width="2" stroke-dasharray="4 3"></circle>')
        o.append(label(x1 + dx * 10, y1 + (dy * 24 if dy else -16), nm, "#8FD0E2", 10, anchor="middle"))
    o.append(node(cx, cy, "JOB", "#FFD23F", r=6, dy=22, size=10))
    return "".join(o)

def crucible(w, h, seed):
    """When he hath tried me, I shall come forth as gold: a crucible glowing in the refiner's furnace, the molten gold
    running clear, the dross skimmed aside."""
    o = [rect(w, h, "#2A1210"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.86)}" r="{f(h * 0.3)}" fill="#FF6A2A" opacity="0.18"></circle>']
    k = min(1.4, h / 280); x, y = w * 0.5, h * 0.98
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-110 0 L -100 -60 L 100 -60 L 110 0 Z", "#5A4A40") + P("M-60 -60 L -50 -20 L 50 -20 L 60 -60 Z", "#1A0A08") + '</g>')
    o.append(E.blaze(x, y - 20 * k, 120 * k, 60 * k, seed, n=7))
    o.append(f'<g transform="translate({f(x)} {f(y - 56 * k)}) scale({f(k)})">' + P("M-40 0 C -44 -30 -40 -50 -34 -56 L 34 -56 C 40 -50 44 -30 40 0 Z", "#8A6A5A")
             + '<ellipse cx="0" cy="-56" rx="34" ry="8" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></ellipse><ellipse cx="-6" cy="-57" rx="16" ry="3" fill="#FFF4C2"></ellipse></g>')
    o.append(f'<g transform="translate({f(w * 0.82)} {f(y)}) scale({f(k)})">' + P("M-24 0 C -20 -10 20 -10 24 0 Z", "#3A3430") + '</g>')
    return "".join(o)

def landmark(p, w, h, seed):
    """There are that remove the landmarks; they violently take away flocks; they drive away the ass of the fatherless: a
    boundary stone pulled up and lying in a furrow, a flock being driven off over the hill."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A9AB8", "#E8D8B0"), hills(w, h, h * 0.78, seed, "#8A8A5A", amp=10, step=90), ground(w, h, h * 0.84, "#A89A5A", dy=0)]
    o.append(f'<ellipse cx="{f(w * 0.24)}" cy="{f(h * 0.92)}" rx="{f(w * 0.05)}" ry="{f(h * 0.02)}" fill="#3A2A1A"></ellipse>'
             f'<g transform="translate({f(w * 0.32)} {f(h * 0.94)}) rotate(70) scale({f(min(1.2, h / 280))})">' + P("M-14 0 L -12 -60 Q 0 -70 12 -60 L 14 0 Z", "#A89A8A") + '</g>')
    o.append(flock(w * 0.58, w * 0.9, h * 0.84, h * 0.9, 9, seed, cows=0, smin=0.12, smax=0.18, flip=False))
    s = fit(h * 0.92, h * 0.76)
    o.append(man(p, w * 0.54, h * 0.92, s, "#3A2A22", up=[(-22, -158), (-50, -170), (-70, -190)], extra='<path d="M-50 -170 L -46 6" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(N.ass(w * 0.94, h * 0.9, min(0.22, h / 1200)))
    return "".join(o)

def huddled(p, w, h, seed):
    """They are wet with the showers of the mountains, and embrace the rock for want of a shelter: poor folk crouched against
    a great rock on the mountain-side in the driving rain."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#4A5060", "#8A90A0"), P(f"M-10 {f(h + 10)} L -10 {f(h * 0.86)} L {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} Z", "#5A5450"),
         P(f"M{f(w * 0.46)} {f(h * 0.98)} L {f(w * 0.48)} {f(h * 0.74)} L {f(w * 0.62)} {f(h * 0.7)} L {f(w * 0.76)} {f(h * 0.76)} L {f(w * 0.8)} {f(h * 0.98)} Z", "#7A7068")]
    k = min(1.0, h / 360)
    for i, x in enumerate((0.38, 0.42, 0.34)):
        o.append(E.kneel(w * x, h * (0.96 - i * 0.01), k * (0.32 - i * 0.04), color=["#5A4A3A", "#4A4A5A", "#6A5A4A"][i], skin="#3A1E14"))
    for i in range(110):
        x = r.uniform(-40, w + 40); y = r.uniform(0, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -10 22" stroke="#C8D0E0" stroke-width="1.3" opacity="0.5"></path>')
    return "".join(o)

def winepress_thirst(p, w, h, seed):
    """They make oil within the walls of these men; they tread their winepresses, and suffer thirst: labourers treading the
    grapes in a rock-cut press under the hot sun, the wine running into the vat below."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8B880", "#F3E0B0"), sun(w * 0.86, h * 0.2, min(24, h * 0.06), op=0.35), ground(w, h, h * 0.84, "#B89A6A", dy=0),
         J1.winepress(w * 0.4, h * 0.93, w * 0.4, h * 0.08), J1.winepress(w * 0.74, h * 0.97, w * 0.14, h * 0.04).replace("#5A4A4A", "#6A1A2A")]
    s = fit(h * 0.93, h * 0.76)
    for i, x in enumerate((0.3, 0.4, 0.5)):
        o.append(man(p, w * x, h * 0.93, s, ["#6A5A4A", "#5A4A3A", "#7A6A5A"][i], up=[(-22, -158), (-40, -186), (-46, -214)]))
    o.append(f'<ellipse cx="{f(w * 0.4)}" cy="{f(h * 0.93)}" rx="{f(w * 0.18)}" ry="{f(h * 0.03)}" fill="#6A1A3A" opacity="0.7"></ellipse>')
    return "".join(o)

def dug_wall(w, h, seed):
    """In the dark they dig through houses; they shut themselves up in the day-time: a mud-brick wall at night with a hole
    dug through it, a mattock left on the ground, the street empty under the moon."""
    o = [K2.sky(w, h, "#05051A", "#1A1A3A"), mk.stars(40, w, h * 0.6, seed), J.moon(w * 0.84, h * 0.66, min(16, h * 0.05)),
         P(f"M-10 {f(h * 0.68)} L {f(w * 0.7)} {f(h * 0.68)} L {f(w * 0.7)} {f(h + 10)} L -10 {f(h + 10)} Z", "#5A4A3A")]
    for row in range(8):
        y = h * (0.7 + row * 0.04)
        for i in range(10):
            o.append(f'<rect x="{f(i * w * 0.07 + (row % 2) * w * 0.035 - 10)}" y="{f(y)}" width="{f(w * 0.07)}" height="{f(h * 0.04)}" fill="none" stroke="#3A2A20" stroke-width="1.2"></rect>')
    o.append(P(f"M{f(w * 0.3)} {f(h * 0.98)} C {f(w * 0.28)} {f(h * 0.82)} {f(w * 0.44)} {f(h * 0.8)} {f(w * 0.44)} {f(h * 0.98)} Z", "#0B0606"))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.99)} L {f(w * 0.6)} {f(h * 0.93)}" stroke="#5A3A1E" stroke-width="5"></path><path d="M{f(w * 0.6)} {f(h * 0.93)} l 10 4 l -6 6" stroke="#8A8A9A" stroke-width="4" fill="none"></path>')
    o.append(ground(w, h, h * 0.99, "#2A2018", dy=0))
    return "".join(o)

def grain_tops(w, h, seed):
    """They are brought low, taken out of the way as all others, and cut off as the tops of the ears of grain: a field of
    ripe grain with a swathe of heads cut off, the cut ears lying in a row."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.8, "#C8A86A", dy=0)]
    for i in range(46):
        x = w * (i / 45); cut = 0.36 < i / 45 < 0.66; top = h * (0.84 if cut else r.uniform(0.7, 0.76))
        o.append(f'<path d="M{f(x)} {f(h * 0.99)} L {f(x + 2)} {f(top)}" stroke="#B89A3A" stroke-width="2"></path>')
        if not cut: o.append(f'<ellipse cx="{f(x + 2)}" cy="{f(top - 8)}" rx="3.4" ry="9" fill="#E8C050" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    for i in range(12):
        x = w * (0.38 + i * 0.024)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(h * 0.97)}" rx="9" ry="3" fill="#E8C050" stroke="#0D0D0F" stroke-width="1" transform="rotate(-20 {f(x)} {f(h * 0.97)})"></ellipse>')
    return "".join(o)
