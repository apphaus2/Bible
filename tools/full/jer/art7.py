"""Drawings for Jeremiah chapter 7 (Jeremiah 19–22), on top of jer.art: the earthen bottle broken at the gate Harsith, the
stocks in the gate of Benjamin, the way of life and the way of death, the king's house of cedar, Coniah's signet."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2

def elder_fig(p, x, y, s, cloth="#5A4A3A", flip=False):
    return man(p, x, y, s, cloth, flip=flip, extra=A.headcloth(cloth) + A.WHITE_BEARD)

def bottle_gate(p, w, h, seed, broken=False):
    """The prophet with a potter's earthen bottle at the gate Harsith above the valley of the son of Hinnom, elders of the
    people and of the priests with him (broken=True: the bottle broken in pieces at his feet)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A3A4A", "#D8906A"), wall(w * 0.5, w + 10, h * 0.26, h * 0.72, seed, towers=2, gate=w * 0.78, color="#B8A07A"),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.66)} {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.74)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.74, "#A88A64", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    if broken:
        o.append(jer_fig(p, w * 0.3, b, s, age=1, up=[(-22, -158), (-46, -186), (-58, -216)]))
        o.append(jar(w * 0.42, b, s * 0.8, broken=True))
    else:
        o.append(jer_fig(p, w * 0.3, b, s, age=1, up=[(-22, -158), (-40, -130), (-46, -110)]) + jar(w * 0.3 - 46 * s, b - 80 * s, s * 0.5, stopper=None))
    for i in range(3): o.append(elder_fig(p, w * (0.56 + i * 0.12), b, s * 0.94, ["#5A4A3A", "#F3EFE6", "#4A4A6A"][i], flip=True))
    return "".join(o)

def siege_night(w, h, seed):
    """In the siege and in the distress: the city wall at night, the fires of the besiegers' camp below it (told in words only)."""
    r = random.Random(seed)
    o = [night(w, h, seed, "#0E0C1E"), wall(-10, w + 10, h * 0.3, h * 0.66, seed, towers=4, color="#5A5048"), ground(w, h, h * 0.66, "#1E1A20", dy=0)]
    for i in range(9):
        x, y = w * (0.05 + i * 0.11) + r.uniform(-10, 10), h * (0.78 + (i % 3) * 0.06)
        o.append(E.blaze(x, y, w * 0.025, h * 0.06, seed + i, n=3) + f'<path d="M{f(x - w * 0.04)} {f(y)} L {f(x - w * 0.02)} {f(y - h * 0.08)} L {f(x)} {f(y)} Z" fill="#2A2420" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def roofs_incense(w, h, seed):
    """The houses upon whose roofs they have burned incense unto all the host of heaven: flat roofs at night under the stars,
    a thread of smoke rising from each."""
    r = random.Random(seed)
    o = [night(w, h, seed, "#14122A"), mk.stars(50, w, h * 0.5, seed + 1)]
    x = -10
    while x < w:
        bw = w * r.uniform(0.1, 0.16); top = h * r.uniform(0.5, 0.64)
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(bw)}" height="{f(h - top)}" fill="#3A3448" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.4)}" y="{f(top - 8)}" width="10" height="8" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="1.2"></rect>'
                 + smoke(x + bw * 0.4 + 5, top - 16, 5, int(x) + seed, r0=0.012, w=0.35, color="#C8C0D0", op=0.4))
        x += bw + 4
    return "".join(o)

def court_people(p, w, h, seed):
    """He stood in the court of Jehovah's house, and said to all the people."""
    return temple_gate(p, w, h, seed)

def stocks(p, w, h, seed):
    """Pashhur put him in the stocks that were in the upper gate of Benjamin: the prophet sitting with his feet fast in a beam
    of wood under the gate's arch, Pashhur the priest standing over him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A878"></rect>',
         f'<path d="M{f(w * 0.12)} {f(h + 10)} L {f(w * 0.12)} {f(h * 0.4)} Q {f(w * 0.5)} {f(h * 0.0)} {f(w * 0.88)} {f(h * 0.4)} L {f(w * 0.88)} {f(h + 10)} Z" fill="#3A2A22" stroke="#0D0D0F" stroke-width="2.6"></path>',
         ground(w, h, h * 0.86, "#7A6A50", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(E.kneel(w * 0.36, b, s * 0.9, color=JER_C, skin="#9A6A4A"))
    bx = w * 0.42
    o.append(f'<rect x="{f(bx - 10)}" y="{f(b - 40 * s)}" width="{f(w * 0.2)}" height="{f(24 * s)}" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2.2"></rect>'
             f'<rect x="{f(bx)}" y="{f(b - 70 * s)}" width="{f(12 * s)}" height="{f(70 * s)}" fill="#6A4A22" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(bx + w * 0.18)}" y="{f(b - 70 * s)}" width="{f(12 * s)}" height="{f(70 * s)}" fill="#6A4A22" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<circle cx="{f(bx + w * (0.06 + k * 0.05))}" cy="{f(b - 28 * s)}" r="{f(5 * s)}" fill="#2A1A10"></circle>' for k in range(2)))
    o.append(priest(p, w * 0.76, b, s, flip=True))
    return "".join(o)

def fire_bones(w, h, seed):
    """As it were a burning fire shut up in my bones: a dark figure-less night, an ember glowing within a closed lamp of clay."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#14080A"></rect>', glow(w * 0.5, h * 0.62, min(w, h) * 0.5, color="#FF6A2A", op=0.5, uid=f"fb{seed}"),
         E.blaze(w * 0.5, h * 0.9, w * 0.2, h * 0.6, seed, n=7)]
    return "".join(o)

def cursed_day(w, h, seed):
    """Cursed be the day wherein I was born: a grey dawn over the overthrown cities of the plain, nothing growing."""
    o = [K2.sky(w, h, "#2A2A3A", "#8A7A7A"), f'<path d="M{f(w * 0.4)} {f(h * 0.66)} a {f(w * 0.08)} {f(w * 0.08)} 0 0 1 {f(w * 0.16)} 0 Z" fill="#B8A8A0"></path>',
         hills(w, h, h * 0.66, seed, "#3A3436", amp=8, step=90), J.collapse(w * 0.1, w * 0.4, h * 0.84, h * 0.2, seed, color="#6A6066"),
         J.collapse(w * 0.6, w * 0.92, h * 0.86, h * 0.16, seed + 1, color="#6A6066"), ground(w, h, h * 0.84, "#2A2628", dy=0)]
    return "".join(o)

def two_ways(w, h, seed):
    """I set before you the way of life and the way of death: the gate of the besieged city, one road going in to the city
    (death, the smoke over it), the other going out to the Chaldeans' camp (life)."""
    o = [K2.sky(w, h, "#5A4A5A", "#E8B880"), wall(w * 0.4, w + 10, h * 0.26, h * 0.6, seed, towers=3, gate=w * 0.62, color="#B8A07A"),
         smoke(w * 0.8, h * 0.24, 7, seed, w=0.7), ground(w, h, h * 0.6, "#B8946A", dy=0),
         N.camp(5, -10, w * 0.3, h * 0.62, h * 0.76, seed, color=(BABEL_C, "#3A4A5A", "#4A5A6A")),
         f'<path d="M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.52)} {f(h * 0.8)} L {f(w * 0.62)} {f(h * 0.6)}" stroke="#E8D0A0" stroke-width="{f(w * 0.03)}" fill="none"></path>',
         f'<path d="M{f(w * 0.52)} {f(h * 0.8)} L {f(w * 0.2)} {f(h * 0.7)}" stroke="#E8D0A0" stroke-width="{f(w * 0.03)}" fill="none"></path>',
         label(w * 0.2, h * 0.86, "THE WAY OF LIFE", "#1A3A1A", 11), label(w * 0.66, h * 0.86, "THE WAY OF DEATH", "#5A0A0A", 11)]
    return "".join(o)

def forest_fire(w, h, seed):
    """I will kindle a fire in her forest, and it shall devour all that is round about her."""
    o = [K2.sky(w, h, "#2A0A0A", "#B8502A"), hills(w, h, h * 0.6, seed, "#2A1A12", amp=10, step=80)]
    for i in range(7):
        x = w * (0.06 + i * 0.15)
        o.append(f'<path d="M{f(x)} {f(h * 0.92)} L {f(x - w * 0.05)} {f(h * 0.92)} L {f(x)} {f(h * 0.5)} L {f(x + w * 0.05)} {f(h * 0.92)} Z" fill="#1E3A22" stroke="#0D0D0F" stroke-width="2"></path>')
    o += [E.blaze(w * (0.12 + i * 0.25), h * 0.92, w * 0.18, h * 0.42, seed + i, n=6) for i in range(4)]
    o.append(ground(w, h, h * 0.92, "#1A0E0A", dy=0))
    return "".join(o)

def palace(p, w, h, seed, prophet=True):
    """The house of the king of Judah: a great house with cedar pillars and a gate, the prophet going down to it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), ground(w, h, h * 0.8, "#D8C8A0", dy=0),
         f'<rect x="{f(w * 0.36)}" y="{f(h * 0.3)}" width="{f(w * 0.6)}" height="{f(h * 0.5)}" fill="#E8D8B8" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         f'<rect x="{f(w * 0.34)}" y="{f(h * 0.24)}" width="{f(w * 0.64)}" height="{f(h * 0.07)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for k in range(6):
        o.append(f'<rect x="{f(w * (0.4 + k * 0.1))}" y="{f(h * 0.31)}" width="{f(w * 0.03)}" height="{f(h * 0.49)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(h * 0.52)}" width="{f(w * 0.08)}" height="{f(h * 0.28)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>')
    if prophet:
        s = fit(b, max(h * 0.4, b - 230))
        o.append(jer_fig(p, w * 0.18, b, s, age=1))
    return "".join(o)

def cedars_fire(p, w, h, seed):
    """They shall cut down thy choice cedars, and cast them into the fire: felled cedar trunks heaped and burning, a stump."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A1A1A", "#C8703A"), hills(w, h, h * 0.56, seed, "#3A3A2A", amp=10, step=80), ground(w, h, h * 0.7, "#5A4A3A", dy=0)]
    for i in range(5):
        y = h * (0.9 - i * 0.04)
        o.append(f'<path d="M{f(w * 0.2 + i * 8)} {f(y)} L {f(w * 0.7 - i * 8)} {f(y - 10)}" stroke="#6A3A1E" stroke-width="16" stroke-linecap="round"></path>')
    o.append(E.blaze(w * 0.46, h * 0.86, w * 0.42, h * 0.5, seed, n=9))
    o.append(f'<path d="M{f(w * 0.84)} {f(h * 0.9)} L {f(w * 0.85)} {f(h * 0.78)} L {f(w * 0.9)} {f(h * 0.78)} L {f(w * 0.91)} {f(h * 0.9)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def passers(p, w, h, seed):
    """Many nations shall pass by this city and say, Wherefore hath Jehovah done thus unto this great city?: travellers on the
    road looking up at the ruined city."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A8A9A", "#E8D0B0"), jerusalem(w * 0.4, w + 10, h * 0.66, h * 0.24, seed, broken=True, color="#B8A07A"),
         ground(w, h, h * 0.66, "#A89070", dy=0)]
    s = fit(b, max(h * 0.4, b - 210))
    for i in range(3): o.append(man(p, w * (0.08 + i * 0.1), b, s * (1 - i * 0.04), ["#6A3A5A", "#3A5A6A", "#7A6A3A"][i], up=[(-22, -158), (-14, -186), (8, -200)] if i == 1 else None))
    o.append(J1.camel(w * 0.4, b, min(0.8, s * 0.9), color="#B5844A"))
    return "".join(o)

def cedar_house(p, w, h, seed):
    """Woe unto him that buildeth his house by unrighteousness: a wide house with spacious chambers and cut-out windows, ceiled
    with cedar and painted with vermilion; labourers carrying beams without wages."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), ground(w, h, h * 0.84, "#C8B080", dy=0),
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.26)}" width="{f(w * 0.56)}" height="{f(h * 0.58)}" fill="#C8302A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         f'<rect x="{f(w * 0.38)}" y="{f(h * 0.2)}" width="{f(w * 0.6)}" height="{f(h * 0.07)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for k in range(4):
        o.append(f'<rect x="{f(w * (0.44 + k * 0.13))}" y="{f(h * 0.36)}" width="{f(w * 0.07)}" height="{f(h * 0.14)}" fill="#3A1A10" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M{f(w * (0.44 + k * 0.13))} {f(h * 0.43)} l {f(w * 0.07)} 0 M{f(w * (0.475 + k * 0.13))} {f(h * 0.36)} l 0 {f(h * 0.14)}" stroke="#8A5A30" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.2)} L {f(w * 0.5)} {f(h * 0.06)} M{f(w * 0.9)} {f(h * 0.2)} L {f(w * 0.86)} {f(h * 0.06)} M{f(w * 0.48)} {f(h * 0.12)} L {f(w * 0.88)} {f(h * 0.12)}" stroke="#6A4A2A" stroke-width="4"></path>')
    s = fit(b, max(h * 0.4, b - 210))
    for i in range(3):
        x = w * (0.08 + i * 0.1)
        o.append(man(p, x, b, s * 0.9, ["#7A6A4A", "#6A5A4A", "#5A4A3A"][i], up=[(-22, -158), (-26, -190), (-10, -206)]))
    o.append(f'<path d="M{f(w * 0.02)} {f(b - 206 * s * 0.9)} L {f(w * 0.34)} {f(b - 206 * s * 0.9)}" stroke="#8A5A30" stroke-width="{f(10 * s)}" stroke-linecap="round"></path>')
    return "".join(o)

def beyond_gates(w, h, seed):
    """Drawn and cast forth beyond the gates of Jerusalem: the gate from outside, a bare rubbish-slope below it, nothing more."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#6A5A5A", "#D8B090"), wall(-10, w + 10, h * 0.2, h * 0.56, seed, towers=4, gate=w * 0.3, color="#B8A07A"),
         f'<path d="M-10 {f(h * 0.56)} L {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A54" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append("".join(f'<ellipse cx="{f(r.uniform(w * 0.4, w))}" cy="{f(r.uniform(h * 0.66, h))}" rx="{f(r.uniform(6, 16))}" ry="{f(r.uniform(3, 6))}" fill="#5A4A3E" stroke="#0D0D0F" stroke-width="1"></ellipse>' for _ in range(24)))
    o.append(bird(w * 0.6, h * 0.14, 1.4) + bird(w * 0.7, h * 0.1, 1.2))
    return "".join(o)

def lebanon_nest(w, h, seed):
    """Go up to Lebanon, and cry; lift up thy voice in Bashan, and cry from Abarim; O inhabitant of Lebanon, that makest thy
    nest in the cedars: the cedar mountains, a nest in the boughs."""
    o = [K2.sky(w, h, "#6A8AB0", "#E8E8E0"), f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.4)} {f(h * 0.5)} L {f(w * 0.6)} {f(h * 0.26)} L {f(w * 0.8)} {f(h * 0.46)} L {f(w + 10)} {f(h * 0.36)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A5A5A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(8):
        x = w * (0.04 + i * 0.13); y = h * (0.94 - (i % 2) * 0.04)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.3)}" stroke="#4A2A1A" stroke-width="5"></path>'
                 + "".join(f'<path d="M{f(x - w * (0.06 - k * 0.012))} {f(y - h * (0.1 + k * 0.07))} L {f(x + w * (0.06 - k * 0.012))} {f(y - h * (0.1 + k * 0.07))} L {f(x)} {f(y - h * (0.16 + k * 0.07))} Z" fill="#2E5A3A" stroke="#0D0D0F" stroke-width="1.6"></path>' for k in range(3)))
    nx, ny = w * 0.43, h * 0.74
    o.append(f'<ellipse cx="{f(nx)}" cy="{f(ny)}" rx="16" ry="7" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def signet(w, h, seed):
    """Though Coniah were the signet upon my right hand, yet would I pluck thee thence: a gold signet ring falling through dark
    air (no hand drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1428"></rect>', V.rays(w * 0.5, h * 0.5, 24, 10, max(w, h), color="#E8B830", op=0.08)]
    cx, cy, R = w * 0.5, h * 0.56, min(w, h) * 0.16
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(R)}" ry="{f(R * 0.5)}" fill="none" stroke="#0D0D0F" stroke-width="{f(R * 0.32)}"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(R)}" ry="{f(R * 0.5)}" fill="none" stroke="#E8B830" stroke-width="{f(R * 0.24)}"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - R * 0.5)}" rx="{f(R * 0.42)}" ry="{f(R * 0.3)}" fill="#7A2A5A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<path d="M{f(cx - R * 0.2)} {f(cy - R * 0.5)} l {f(R * 0.4)} 0 M{f(cx)} {f(cy - R * 0.68)} l 0 {f(R * 0.36)}" stroke="#E8B830" stroke-width="2"></path>')
    return "".join(o)

def broken_vessel(w, h, seed):
    """Is this man Coniah a despised broken vessel? a vessel wherein none delighteth?: a cracked jar cast out on the ground."""
    o = [K2.sky(w, h, "#5A4A5A", "#D8B090"), ground(w, h, h * 0.66, "#8A7A5A", dy=0),
         jar(w * 0.4, h * 0.94, min(1.4, h / 170), color="#A8603A", broken=True), jar(w * 0.64, h * 0.92, min(1.2, h / 200), color="#8A5A3A", stopper=None)]
    return "".join(o)

def empty_throne(w, h, seed):
    """Write ye this man childless: no more shall a man of his seed prosper, sitting upon the throne of David — the throne
    empty."""
    return S3.cedar(w, h, h * 0.86) + glow(w * 0.3, h * 0.7, min(w, h) * 0.4, color="#FFE680", op=0.2, uid=f"et{seed}") + S3.throne(w * 0.3, h * 0.88, min(1.3, h / 230))
