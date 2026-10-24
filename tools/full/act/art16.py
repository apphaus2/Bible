"""Drawings for Acts 28. Melita: the barbarians' fire on the shore in the rain, Paul laying on a bundle of sticks; the viper
(snake.py) fastened on his hand, then shaken off into the fire; the islanders watching; Publius (white beard, a toga) and
his father healed on his bed; the sick of the island coming; the ship of Alexandria whose sign was the Twin Brothers (two
stars on her bow); the voyage by Syracuse, Rhegium and Puteoli to Rome on the map; the Appian Way, the Market of Appius and
the Three Taverns, the brethren coming to meet Paul; Rome on its hills (temples, red roofs, an aqueduct); and Paul's own
hired dwelling, chained to the soldier that guarded him, the chief of the Jews and all that went in unto him. Built on
act.art15."""
from act.art15 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
import snake as SN
from oba.minor import rain
from act.art8 import jupiter_temple

def islander(p, x, y, s, i=0, flip=False, up=None):
    c = ["#8A6A3A", "#5A4A3A", "#7A5A2A", "#6A4A4A"][i % 4]
    return man_fig(p, x, y, s, c, hr="#1A1210", bd=["#1A1210", None, "#3A2A1A", None][i % 4], kind="Tunic", flip=flip, up=up)
def publius(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#B8B2A6", border="#2A4A6A", flip=flip, up=up, extra=beard("#C8C2B6"))
WHO.update({"publius": publius})

def melita_fire(p, w, h, seed, stage="kindle"):
    """The barbarians of Melita kindling a fire on the shore in the rain and the cold: stage "kindle" — the islanders and
    the shipwrecked about the fire, Paul laying on a bundle of sticks; "viper" — a viper come out of the heat fastened on his
    hand, the islanders drawing back; "shaken" — the viper shaken off, falling into the flames, Paul unharmed; "watch" —
    long after, the islanders watching Paul standing well, their hands lifted in wonder."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A4A5A", "#8A9AA0"), sea_(w, h, h * 0.44, seed, color="#3A5A6A", deep="#1A2A3A"),
         f'<path d="M-10 {f(h * 0.52)} C {f(w * 0.3)} {f(h * 0.48)} {f(w * 0.7)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>',
         rain(w, h, seed, n=70, color="#BFD8F2", op=0.45)]
    s = fit(b, max(h * 0.34, b - 190))
    fx = w * 0.5
    o.append(glow(fx, b - 40 * s, 170 * s, "#FF8A3D", 0.7, f"{p}f") + E.blaze(fx, b, 80 * s, 90 * s, seed, n=5))
    px = fx - 90 * s
    if stage == "kindle":
        o.append(paul(p, px, b, s, up=[(22, -158), (40, -140), (56, -128)]))
        o.append(f'<path d="M{f(px + 40 * s)} {f(b - 128 * s)} L {f(px + 80 * s)} {f(b - 140 * s)} M{f(px + 42 * s)} {f(b - 122 * s)} L {f(px + 82 * s)} {f(b - 130 * s)}" stroke="#6A4A2A" stroke-width="{f(4 * s)}"></path>')
    elif stage == "viper":
        o.append(paul(p, px, b, s, up=[(22, -158), (42, -150), (62, -150)]))
        hx, hy = px + 62 * s, b - 150 * s
        o.append(SN.snake([(hx - 2 * s, hy + 4 * s), (hx + 4 * s, hy + 22 * s), (hx - 4 * s, hy + 40 * s), (hx + 6 * s, hy + 56 * s)][::-1], 3.4 * s, f"{p}vp", head_scale=0.5))
    elif stage == "shaken":
        o.append(paul(p, px, b, s, up=[(22, -158), (46, -140), (64, -120)]))
        vx, vy = fx - 10 * s, b - 70 * s
        o.append(SN.snake([(vx - 20 * s, vy - 14 * s), (vx - 6 * s, vy - 4 * s), (vx + 8 * s, vy - 12 * s), (vx + 20 * s, vy + 2 * s)], 3.4 * s, f"{p}vs", head_scale=0.5))
    else:
        o.append(glow(px, b - 110 * s, 120 * s, "#FFF4C2", 0.4, f"{p}w") + paul(p, px, b, s, flip=True))
    ups = (stage in ("viper", "watch"))
    for i, x in enumerate((0.66, 0.76, 0.86, 0.95)):
        o.append(islander(p, w * x, b, s * (1 - 0.02 * i), i, flip=False, up=UP_HIGH if ups and i % 2 == 0 else None))
    o.append(julius(p, w * 0.16, b, s) + soldier(p, w * 0.06, b, s * 0.96))
    return "".join(o)

def publius_house(p, w, h, seed, crowd_=False):
    """In the house of Publius, the chief man of the island: his father lying sick on his bed, Paul laying his hands on him,
    Publius standing by; crowd_=True the rest that had diseases in the island coming to the door to be cured."""
    if crowd_:
        bg, b = _street(w, h, seed)
        o = [mk.defs(p, *ALL, *LIE), bg]
        s = fit(b, max(h * 0.34, b - 190))
        o.append(paul(p, w * 0.14, b, s, flip=True, up=UP_BLESS) + publius(p, w * 0.26, b, s, flip=True))
        o.append(man_fig(p, w * 0.42, b, s, "#7A7A60", hr="#3A2A1A", bd="#3A2A1A", kind="Tunic", extra='<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'))
        o.append(woman_fig(p, w * 0.54, b, s * 0.92, "#6A4A3A", "#3A3A4A") + islander(p, w * 0.66, b, s, 2) + crowd(p, w * 0.76, w * 0.96, b, b - 170 * s, 2, seed))
        return "".join(o)
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL, *LIE), bg]
    s = fit(b, max(h * 0.34, b - 190))
    o.append(on_bed(p, w * 0.56, b - 26 * s, 220 * s, cloth="#F3EFE6"))
    o.append(paul(p, w * 0.3, b, s, up=[(22, -158), (50, -140), (74, -116)]) + publius(p, w * 0.86, b, s, flip=True))
    return "".join(o)

def twin_brothers(p, w, h, seed):
    """A ship of Alexandria which had wintered in the island, whose sign was The Twin Brothers: the grain ship in the harbour of
    Melita under a clear sky, the two stars painted on her bow, Paul and the company going aboard."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#C8B890", amp=14, step=100), sea_(w, h, h * 0.5, seed),
         f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w * 0.4)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>']
    k = min(w * 0.5 / 500, h / 600)
    sx, sy_ = w * 0.66, h * 0.7
    o.append(grain_ship(p, sx, sy_, k, sail="reefed", crew=[("#6A5A4A", -40), ("#4A5A6A", 60)]))
    for dy in (-90, -70):
        o.append(f'<g transform="translate({f(sx + 236 * k)} {f(sy_ + dy * k)}) scale({f(k)})"><path d="M0 -9 L 2.6 -2.6 L 9 0 L 2.6 2.6 L 0 9 L -2.6 2.6 L -9 0 L -2.6 -2.6 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></path></g>')
    s = fit(b, max(h * 0.4, b - 170))
    o.append(paul(p, w * 0.14, b, s) + julius(p, w * 0.26, b, s) + soldier(p, w * 0.04, b, s * 0.96))
    return "".join(o)

def appian_way(p, w, h, seed):
    """The Appian Way: the paved Roman road running straight across the plain between cypresses and milestones, the inn of
    the Three Taverns by it; the brethren from Rome come out to meet Paul, Paul with his hands lifted, giving thanks, Julius
    and the soldiers behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.46, seed, color="#8A9A7A", amp=10, step=110), ground(w, h, h * 0.54, "#9AAA6A", dy=0),
         f'<path d="M{f(w * 0.46)} {f(h * 0.54)} L {f(w * 0.54)} {f(h * 0.54)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#A8A098" stroke="{INK}" stroke-width="2"></path>']
    for k in range(1, 8):
        t = k / 8; y = h * 0.54 + (h * 0.46) * t * t
        x0 = w * (0.46 - 0.36 * t * t); x1 = w * (0.54 + 0.36 * t * t)
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="#8A847A" stroke-width="1.4"></path>')
    for i, (x, sc) in enumerate(((0.36, 0.5), (0.3, 0.7), (0.2, 1.0), (0.66, 0.5), (0.74, 0.7), (0.86, 1.0))):
        yy = h * (0.6 + 0.12 * (i % 3)); kk = sc * max(0.4, h / 400)
        o.append(f'<path d="M{f(w * x)} {f(yy)} C {f(w * x - 14 * kk)} {f(yy - 60 * kk)} {f(w * x - 6 * kk)} {f(yy - 120 * kk)} {f(w * x)} {f(yy - 150 * kk)} C {f(w * x + 6 * kk)} {f(yy - 120 * kk)} {f(w * x + 14 * kk)} {f(yy - 60 * kk)} {f(w * x)} {f(yy)} Z" fill="#2E5A3A" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(h * 0.5)}" width="{f(w * 0.16)}" height="{f(h * 0.1)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.05)} {f(h * 0.5)} L {f(w * 0.14)} {f(h * 0.44)} L {f(w * 0.23)} {f(h * 0.5)} Z" fill="#B5583A" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.36, b - 180))
    o.append(paul(p, w * 0.44, b, s, flip=True, up=UP_HIGH) + julius(p, w * 0.32, b, s) + soldier(p, w * 0.22, b, s * 0.96))
    o.append(crowd(p, w * 0.58, w * 0.86, b, b - 170 * s, 4, seed))
    return "".join(o)

def rome(p, w, h, seed, paul_=False):
    """Rome on its hills: the temples on the Capitol, the red roofs of the city climbing the slopes, the long arches of an
    aqueduct across the plain, cypresses; paul_=True Paul and the soldier on the road coming in."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE6A0"), hills(w, h, h * 0.44, seed, color="#9AA07A", amp=30, step=140)]
    r = random.Random(seed)
    for i in range(26):
        x = r.uniform(0, w); y = h * r.uniform(0.42, 0.62); bw = r.uniform(30, 70); bh = r.uniform(20, 46)
        o.append(f'<rect x="{f(x)}" y="{f(y - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{r.choice(["#E8D8B0", "#D8C098", "#F3E8D0"])}" stroke="{INK}" stroke-width="1.4"></rect>'
                 f'<path d="M{f(x - 3)} {f(y - bh)} L {f(x + bw / 2)} {f(y - bh - 10)} L {f(x + bw + 3)} {f(y - bh)} Z" fill="#B5583A" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(jupiter_temple(w * 0.3, h * 0.36, w * 0.26) + jupiter_temple(w * 0.68, h * 0.4, w * 0.18))
    ay = h * 0.7
    o.append(f'<rect x="-10" y="{f(ay - h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.025)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>')
    for k in range(16):
        x = w * k / 15
        o.append(f'<path d="M{f(x - w / 30 + 3)} {f(ay)} L {f(x - w / 30 + 3)} {f(ay - h * 0.06)} Q {f(x)} {f(ay - h * 0.1)} {f(x + w / 30 - 3)} {f(ay - h * 0.06)} L {f(x + w / 30 - 3)} {f(ay)}" fill="none" stroke="#A89878" stroke-width="5"></path>')
    o.append(ground(w, h, ay, "#A8A86A", dy=0))
    if paul_:
        s = fit(b, max(h * 0.4, b - 170))
        o.append(paul(p, w * 0.36, b, s) + soldier(p, w * 0.48, b, s, flip=True))
    return "".join(o)

def lodging(p, w, h, seed, visitors="jews", night=False):
    """Paul's own hired dwelling at Rome: a room with a window on the city, Paul sitting with the chain from his wrist to the
    soldier that guarded him; visitors= "jews" (the chief of the Jews, grey beards and headcloths, listening) or "all" (all
    that went in unto him, men and women, Jews and Gentiles), the scrolls of the law and the prophets open on the table."""
    bg, b = _house(w, h, seed, "night" if night else "day")
    o = [mk.defs(p, *ALL), bg, f'<rect x="{f(w * 0.64)}" y="{f(h * 0.18)}" width="{f(w * 0.16)}" height="{f(h * 0.26)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<g transform="translate({f(w * 0.64)} {f(h * 0.3)})">' + jupiter_temple(w * 0.08, h * 0.12, w * 0.1) + '</g>']
    s = fit(b, max(h * 0.34, b - 190))
    o.append(seated(w * 0.22, b, s * 0.84, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A") + soldier(p, w * 0.08, b, s))
    o.append(f'<path d="M{f(w * 0.12)} {f(b - 100 * s)} C {f(w * 0.15)} {f(b - 70 * s)} {f(w * 0.2)} {f(b - 70 * s)} {f(w * 0.24)} {f(b - 80 * s)}" stroke="#8A8A90" stroke-width="{f(3 * s)}" stroke-dasharray="{f(5 * s)} {f(2 * s)}" fill="none"></path>')
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(b - 50 * s)}" width="{f(w * 0.12)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>' + scroll(w * 0.36, b - 58 * s, 60 * s, 14 * s, lines=2))
    if visitors == "jews":
        for i, x in enumerate((0.5, 0.6, 0.7)):
            o.append(seated(w * x, b, s * 0.78, ["#5A5A6A", "#E8E2D6", "#3A4A6A"][i], head=["#5A5A6A", "#F3EFE6", "#3A4A6A"][i], beard=["#7A746A", "#9A948A", "#6A645E"][i], flip=True))
    else:
        o.append(seated(w * 0.44, b, s * 0.74, "#6A4A3A", head=None, beard="#2A1A10", flip=True) + woman_fig(p, w * 0.5, b - 34 * s, s * 0.8, "#5A6A8A", "#3A6A8A", flip=True))
    return "".join(o)
