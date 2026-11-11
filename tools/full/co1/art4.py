"""Drawings for 1 Corinthians 12–14 (chapter 4 of the volume), on co1.art3: the dumb idols (12:2); the gifts of the one Spirit
as a plate of nine gifts about a light with no figure in it (12:8–10); the body and its members as technical plates — the
whole body tagged, then eye, ear, hand, foot and head each in its cell (12:12–24); the ministries set in the church (12:28);
sounding brass and the clanging cymbal (13:1); love's kindness at a door (13:4); the child and the man (13:11); the bronze
mirror, darkly (13:12); faith, hope, love as three lamps (13:13); prophesying in the assembly, the pipe, the harp and the
trumpet with an uncertain voice (14:7–8), two men who are barbarians to each other (14:11), the unbeliever coming in and
falling on his face (14:24–25), the assembly in order (14:26–40). God is never drawn: the Spirit is light; the Voice box
for 14:21."""
from co1.art3 import *
from co1.art3 import f, INK, _seated_lap
from num.art5 import trumpet
import samuel2 as S2

def jp(x, y, text, size=40, fill="#0D0D0F", stroke="#F3EFE6", rot=-6, roman=None):
    """A sound effect in the drawing: katakana in Noto Sans JP 900 with a stroke, and its romaji under it (svg labels)."""
    o = (f'<g transform="rotate({rot} {f(x)} {f(y)})"><text x="{f(x)}" y="{f(y)}" font-family="Noto Sans JP, sans-serif" font-weight="900" font-size="{f(size)}" '
         f'fill="{fill}" stroke="{stroke}" stroke-width="4" paint-order="stroke" text-anchor="middle">{text}</text>')
    if roman: o += f'<text x="{f(x)}" y="{f(y + size * 0.42)}" font-family="IBM Plex Mono, monospace" font-weight="600" font-size="9" letter-spacing="2" fill="{stroke}" stroke="{fill}" stroke-width="3" paint-order="stroke" text-anchor="middle">{roman}</text>'
    return o + "</g>"

# ---- 1 Corinthians 12 --------------------------------------------------------------------------------------------------
def dumb_idols(p, w, h, seed):
    """When ye were Gentiles ye were led away unto those dumb idols: in a dim temple, men and women bowed down on the floor
    before images on their plinths that have no voice."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#4A3A4A", floor="#2A2028"), lamp_glow(w * 0.7, h * 0.3, max(w, h) * 0.4, f"{p}di", color="#FF9A4A", op=0.4)]
    k = min(1.3, h / 200)
    for i, x in enumerate((0.56, 0.72, 0.88)):
        o.append(statue(w * x, b, k * 0.9, kind=i, color=["#C8A040", "#B8B0A0", "#8A6A3A"][i]))
    s = fit(b, b - min(h * 0.62, 170))
    for i, x in enumerate((0.1, 0.22, 0.34)):
        o.append(E.kneel(w * x, b, s * 0.8, color=["#6A4A5A", "#4A5A6A", "#7A5A3A"][i], skin=SKIN))
    return "".join(o)

GIFTS = ["WISDOM", "KNOWLEDGE", "FAITH", "HEALINGS", "MIRACLES", "PROPHECY", "DISCERNINGS", "TONGUES", "INTERPRETATION"]

def gifts_plate(w, h):
    """To one is given through the Spirit the word of wisdom; and to another …: a plate — the light of the one Spirit in the
    middle (no figure), and the nine gifts set about it, each joined to the light."""
    o = [plate_bg(w, h, "1 CORINTHIANS 12:8–11 · ONE AND THE SAME SPIRIT")]
    cx, cy = w * 0.5, h * 0.56
    rx, ry = w * 0.4, h * 0.34
    o.append(halo(cx, cy, min(w, h) * 0.32, "#FFF4C2", 0.7) + rays(cx, cy, 18, 10, min(w, h) * 0.3, "#FFF4C2", 0.4, 3))
    for i, g in enumerate(GIFTS):
        a = math.radians(-90 + i * 360 / len(GIFTS))
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        o.append(route([(cx + 30 * math.cos(a), cy + 30 * math.sin(a)), (x - 24 * math.cos(a), y - 12 * math.sin(a))], color="#C8A040", sw=1.6, dash="5 4"))
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="7" fill="#FFD23F" stroke="{INK}" stroke-width="1.6"></circle>')
        o.append(plate_label(x, y + (18 if math.sin(a) > 0.2 else -12), g, CY, 9.5))
    return "".join(o)

def body_plate(p, w, h):
    """As the body is one, and hath many members … so also is Christ: a technical plate — the one body standing in the
    middle, tagged: the head, the eye, the ear, the hand, the foot; the many members, one body."""
    o = [plate_bg(w, h, "1 CORINTHIANS 12:12 · ONE BODY · MANY MEMBERS"), mk.defs(p, *ALL)]
    b = h * 0.94; s = fit(b, b - min(h * 0.8, 300)); cx = w * 0.5
    figure = robed(p, cx, b, s, "#1E4A6A", skin="#2A5A7A", hair="#163A56", line=CY)
    o.append(figure)
    pts = {"THE HEAD": (0, -196), "THE EYE": (6, -186), "THE EAR": (-12, -184), "THE HAND": (28, -92), "THE FOOT": (12, -6)}
    sides = {"THE HEAD": (-1, -0.2), "THE EYE": (1, -0.25), "THE EAR": (-1, 0.15), "THE HAND": (1, 0.1), "THE FOOT": (-1, 0)}
    for nm, (px, py) in pts.items():
        x, y = cx + px * s, b + py * s
        dx, dy = sides[nm]
        tx, ty = x + dx * w * 0.24, y + dy * h * 0.3
        o.append(tag(x, y, nm, tx, ty, color=GOLD))
    return "".join(o)

def _eye(cx, cy, r):
    return (f'<path d="M{f(cx - r)} {f(cy)} C {f(cx - r * 0.5)} {f(cy - r * 0.7)} {f(cx + r * 0.5)} {f(cy - r * 0.7)} {f(cx + r)} {f(cy)} C {f(cx + r * 0.5)} {f(cy + r * 0.7)} {f(cx - r * 0.5)} {f(cy + r * 0.7)} {f(cx - r)} {f(cy)} Z" fill="#F3EFE6" stroke="{CY}" stroke-width="2"></path>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.36)}" fill="#3A6A8A" stroke="{INK}" stroke-width="1.4"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.14)}" fill="#0D0D0F"></circle>')

def _ear(cx, cy, r):
    return (f'<path d="M{f(cx - r * 0.3)} {f(cy + r)} C {f(cx - r * 0.2)} {f(cy + r * 0.4)} {f(cx - r * 0.8)} {f(cy + r * 0.2)} {f(cx - r * 0.7)} {f(cy - r * 0.4)} '
            f'C {f(cx - r * 0.6)} {f(cy - r)} {f(cx + r * 0.6)} {f(cy - r * 1.1)} {f(cx + r * 0.6)} {f(cy - r * 0.2)} C {f(cx + r * 0.6)} {f(cy + r * 0.4)} {f(cx + r * 0.1)} {f(cy + r * 0.5)} {f(cx - r * 0.3)} {f(cy + r)} Z" '
            f'fill="#C98E66" stroke="{CY}" stroke-width="2"></path><path d="M{f(cx - r * 0.3)} {f(cy - r * 0.3)} C {f(cx)} {f(cy - r * 0.6)} {f(cx + r * 0.3)} {f(cy - r * 0.3)} {f(cx + r * 0.1)} {f(cy + r * 0.1)}" fill="none" stroke="#5A3A2A" stroke-width="1.6"></path>')

def _hand(cx, cy, r):
    o = [f'<path d="M{f(cx - r * 0.5)} {f(cy + r)} L {f(cx - r * 0.55)} {f(cy)} L {f(cx + r * 0.5)} {f(cy)} L {f(cx + r * 0.45)} {f(cy + r)} Z" fill="#C98E66" stroke="{CY}" stroke-width="2"></path>']
    for i in range(4):
        x = cx - r * 0.42 + i * r * 0.28
        o.append(f'<rect x="{f(x - r * 0.1)}" y="{f(cy - r * (0.9 - abs(i - 1.5) * 0.12))}" width="{f(r * 0.22)}" height="{f(r * (0.92 - abs(i - 1.5) * 0.12))}" rx="{f(r * 0.1)}" fill="#C98E66" stroke="{CY}" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(cx - r * 0.5)} {f(cy + r * 0.2)} C {f(cx - r * 0.8)} {f(cy)} {f(cx - r * 0.9)} {f(cy - r * 0.3)} {f(cx - r * 0.8)} {f(cy - r * 0.4)}" fill="none" stroke="{CY}" stroke-width="{f(r * 0.2)}" stroke-linecap="round"></path>'
             f'<path d="M{f(cx - r * 0.5)} {f(cy + r * 0.2)} C {f(cx - r * 0.8)} {f(cy)} {f(cx - r * 0.9)} {f(cy - r * 0.3)} {f(cx - r * 0.8)} {f(cy - r * 0.4)}" fill="none" stroke="#C98E66" stroke-width="{f(r * 0.14)}" stroke-linecap="round"></path>')
    return "".join(o)

def _foot(cx, cy, r):
    return (f'<path d="M{f(cx - r * 0.3)} {f(cy - r)} L {f(cx + r * 0.1)} {f(cy - r)} L {f(cx + r * 0.15)} {f(cy + r * 0.2)} C {f(cx + r * 0.6)} {f(cy + r * 0.3)} {f(cx + r)} {f(cy + r * 0.5)} {f(cx + r)} {f(cy + r * 0.8)} '
            f'L {f(cx - r * 0.4)} {f(cy + r * 0.8)} C {f(cx - r * 0.5)} {f(cy + r * 0.2)} {f(cx - r * 0.35)} {f(cy - r * 0.2)} {f(cx - r * 0.3)} {f(cy - r)} Z" fill="#C98E66" stroke="{CY}" stroke-width="2"></path>')

def _head(cx, cy, r):
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.7)}" fill="#C98E66" stroke="{CY}" stroke-width="2"></circle>'
            f'<path d="M{f(cx - r * 0.7)} {f(cy - r * 0.1)} C {f(cx - r * 0.7)} {f(cy - r * 0.9)} {f(cx + r * 0.7)} {f(cy - r * 0.9)} {f(cx + r * 0.7)} {f(cy - r * 0.1)} C {f(cx + r * 0.3)} {f(cy - r * 0.4)} {f(cx - r * 0.3)} {f(cy - r * 0.4)} {f(cx - r * 0.7)} {f(cy - r * 0.1)} Z" fill="#2A1A10"></path>')

def members(w, h, which=("FOOT", "HAND", "EAR", "EYE"), title="1 CORINTHIANS 12:15–17 · IF THE FOOT SHALL SAY"):
    """The members each in its cell of a plate, joined to one another by gold lines: foot, hand, ear, eye (12:15–17), or
    eye, hand, head, feet (12:21)."""
    o = [plate_bg(w, h, title)]
    n = len(which); cw = w / n; cy = h * 0.56; r = min(cw * 0.26, h * 0.22)
    draw = {"FOOT": _foot, "FEET": _foot, "HAND": _hand, "EAR": _ear, "EYE": _eye, "HEAD": _head}
    o.append(route([(cw * 0.5, cy), (w - cw * 0.5, cy)], color="#C8A040", sw=2, dash="7 5"))
    for i, nm in enumerate(which):
        cx = cw * (i + 0.5)
        o.append(f'<rect x="{f(cx - r * 1.3)}" y="{f(cy - r * 1.3)}" width="{f(r * 2.6)}" height="{f(r * 2.6)}" fill="#0F2440" stroke="{CY}" stroke-width="1.6"></rect>')
        o.append(draw[nm](cx, cy, r))
        o.append(plate_label(cx, min(cy + r * 1.3 + 16, h - 6), "THE " + nm, GOLD, 10))
    return "".join(o)

def ministries(w, h):
    """God hath set some in the church, first apostles, secondly prophets, thirdly teachers, then …: a plate — the order set
    as a ladder of rungs, each with its name."""
    o = [plate_bg(w, h, "1 CORINTHIANS 12:28 · GOD HATH SET SOME IN THE CHURCH")]
    items = ["FIRST · APOSTLES", "SECONDLY · PROPHETS", "THIRDLY · TEACHERS", "THEN · MIRACLES", "GIFTS OF HEALINGS", "HELPS", "GOVERNMENTS", "DIVERS KINDS OF TONGUES"]
    top, bot = h * 0.18, h * 0.94
    cols = 2; rows_ = 4
    for i, it in enumerate(items):
        c, r_ = i // rows_, i % rows_
        x = w * (0.08 + 0.46 * c); y = top + (bot - top) * (r_ + 0.5) / rows_
        bw = w * 0.4; bh = (bot - top) / rows_ * 0.66
        o.append(f'<rect x="{f(x)}" y="{f(y - bh / 2)}" width="{f(bw)}" height="{f(bh)}" fill="#12304A" stroke="{GOLD if i < 3 else CY}" stroke-width="{2.2 if i < 3 else 1.4}"></rect>'
                 + plate_label(x + bw / 2, y + 4, it, GOLD if i < 3 else CY, 10))
    return "".join(o)

# ---- 1 Corinthians 13 --------------------------------------------------------------------------------------------------
def brass_cymbal(w, h, seed):
    """Sounding brass, or a clanging cymbal: a great bronze gong hung in its frame and a pair of cymbals struck together,
    the noise breaking out from them — and nothing else in the dark."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1418"></rect>', halo(w * 0.3, h * 0.5, h * 0.5, "#C8803A", 0.4)]
    k = min(w / 560, h / 220)
    gx, gy, gr = w * 0.3, h * 0.52, min(h * 0.36, w * 0.18)
    o.append(f'<path d="M{f(gx - gr * 1.3)} {f(h)} L {f(gx - gr * 1.3)} {f(gy - gr * 1.3)} L {f(gx + gr * 1.3)} {f(gy - gr * 1.3)} L {f(gx + gr * 1.3)} {f(h)}" fill="none" stroke="#5A3A22" stroke-width="{f(8 * k)}"></path>'
             f'<path d="M{f(gx - gr * 0.6)} {f(gy - gr * 1.3)} L {f(gx - gr * 0.5)} {f(gy - gr * 0.86)} M{f(gx + gr * 0.6)} {f(gy - gr * 1.3)} L {f(gx + gr * 0.5)} {f(gy - gr * 0.86)}" stroke="#2A1A10" stroke-width="2"></path>'
             f'<circle cx="{f(gx)}" cy="{f(gy)}" r="{f(gr)}" fill="#B8803A" stroke="{INK}" stroke-width="2.6"></circle>'
             f'<circle cx="{f(gx)}" cy="{f(gy)}" r="{f(gr * 0.7)}" fill="none" stroke="#E8B860" stroke-width="2"></circle><circle cx="{f(gx)}" cy="{f(gy)}" r="{f(gr * 0.25)}" fill="#D8A050" stroke="{INK}" stroke-width="1.6"></circle>')
    for kk in range(3):
        rr = gr * (1.2 + kk * 0.25)
        o.append(f'<path d="M{f(gx + rr * 0.8)} {f(gy - rr * 0.6)} A {f(rr)} {f(rr)} 0 0 1 {f(gx + rr * 0.8)} {f(gy + rr * 0.6)}" fill="none" stroke="#FFD23F" stroke-width="3" opacity="{0.8 - kk * 0.2:.2f}"></path>')
    cx, cy = w * 0.74, h * 0.5
    for side in (-1, 1):
        o.append(f'<g transform="rotate({side * 18} {f(cx + side * 36 * k)} {f(cy)})"><ellipse cx="{f(cx + side * 36 * k)}" cy="{f(cy)}" rx="{f(14 * k)}" ry="{f(48 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="2.2"></ellipse>'
                 f'<ellipse cx="{f(cx + side * 36 * k)}" cy="{f(cy)}" rx="{f(5 * k)}" ry="{f(12 * k)}" fill="#8A6A2A"></ellipse></g>')
    o.append(mk.speed(cx, cy, 14, 30 * k, 110 * k, seed, color="#FFD23F", op=0.7))
    o.append(jp(w * 0.56, h * 0.24, "ガーン", min(44, h * 0.18), roman="GAAN") + jp(w * 0.88, h * 0.86, "ジャーン", min(34, h * 0.14), rot=8, roman="JAAN"))
    return "".join(o)

def kindness(p, w, h, seed):
    """Love suffereth long, and is kind: at the door of a house at evening a woman giving bread and water to a tired
    traveller who has sat down on the step."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), house_door(w, h, seed, open_=True, dusk=True)]
    s = fit(b, b - min(h * 0.72, 196))
    gift = '<ellipse cx="-62" cy="-136" rx="12" ry="6" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
    o.append(robed(p, w * 0.72, b, s * 0.94, "#5A6A8A", woman=True, veil="#2A3A5A", up=[(-22, -158), (-42, -140), (-58, -136)], extra=gift))
    o.append(seated(w * 0.5, b, s * 0.74, "#7A6A5A", head="#4A4A54", beard="#5A4A3A"))
    return "".join(o)

def child_man(p, w, h, seed):
    """When I was a child, I spake as a child … now that I am become a man, I have put away childish things: at the left a
    boy on the floor with his clay toys and a spinning top; at the right the same grown, a man with a scroll, the toys put
    away on the shelf."""
    b = h * 0.9
    o = [mk.defs(p, *ALL, "ManUp"), room(w, h, b, wall="#C8A878", floor="#8A6A4A"), f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>']
    s = fit(b, b - min(h * 0.74, 200))
    o.append(seated(w * 0.18, b, s * 0.64, "#C8A060", head="#3A2214", beard=None))
    k = s
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.3 - 8 * k)} {f(b - 16 * k)} L {f(w * 0.3 + 8 * k)} {f(b - 16 * k)} Z" fill="#B5121B" stroke="{INK}" stroke-width="1.4"></path>'
             f'<ellipse cx="{f(w * 0.38)}" cy="{f(b - 8 * k)}" rx="{f(12 * k)}" ry="{f(7 * k)}" fill="#B8784A" stroke="{INK}" stroke-width="1.4"></ellipse><circle cx="{f(w * 0.38 + 12 * k)}" cy="{f(b - 14 * k)}" r="{f(5 * k)}" fill="#B8784A" stroke="{INK}" stroke-width="1.4"></circle>')
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.3)}" width="{f(w * 0.14)}" height="{f(h * 0.04)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.62 - 6 * k)} {f(h * 0.3 - 12 * k)} L {f(w * 0.62 + 6 * k)} {f(h * 0.3 - 12 * k)} Z" fill="#B5121B" stroke="{INK}" stroke-width="1.2"></path>'
             f'<ellipse cx="{f(w * 0.7)}" cy="{f(h * 0.3 - 6 * k)}" rx="{f(10 * k)}" ry="{f(6 * k)}" fill="#B8784A" stroke="{INK}" stroke-width="1.2"></ellipse>')
    o.append(robed(p, w * 0.8, b, s, "#C8A060", hair="#2A1A10", beard="#2A1A10", mantle="#8A6A3A", up=[(-22, -158), (-42, -150), (-58, -152)], extra=sealed_scroll(-60, -152, 0.2, rot=80)))
    return "".join(o)

def bronze_mirror(w, h, seed):
    """Now we see in a mirror, darkly; but then face to face: at the left a hand-mirror of polished bronze, the face in it
    a dim blur in the dark; at the right the same place open to the full light."""
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#1E1820"></rect>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#FFF8E6"></rect>',
         f'<defs><clipPath id="bmc{seed}"><rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}"></rect></clipPath></defs>',
         f'<g clip-path="url(#bmc{seed})">' + halo(w * 0.75, h * 0.5, h * 0.7, "#FFFFFF", 0.9) + rays(w * 0.75, h * 0.5, 22, h * 0.1, h * 0.8, "#FFE680", 0.4, 4) + '</g>']
    cx, cy, r = w * 0.25, h * 0.42, min(h * 0.3, w * 0.14)
    uid = f"bm{seed}"
    o.append(f'<defs><radialGradient id="{uid}" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#C89A5A"></stop><stop offset="1" stop-color="#6A4A2A"></stop></radialGradient>'
             f'<filter id="{uid}b"><feGaussianBlur stdDeviation="{f(r * 0.08)}"></feGaussianBlur></filter></defs>'
             f'<rect x="{f(cx - r * 0.14)}" y="{f(cy + r)}" width="{f(r * 0.28)}" height="{f(r * 1.1)}" rx="{f(r * 0.08)}" fill="#5A3A1A" stroke="{INK}" stroke-width="2"></rect>'
             f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="url(#{uid})" stroke="{INK}" stroke-width="3"></circle>'
             f'<g filter="url(#{uid}b)" opacity="0.55"><ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(r * 0.34)}" ry="{f(r * 0.46)}" fill="#3A2A1A"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - r * 0.34)}" rx="{f(r * 0.4)}" ry="{f(r * 0.2)}" fill="#2A1A10"></ellipse></g>'
             f'<path d="M{f(cx - r * 0.6)} {f(cy - r * 0.5)} C {f(cx - r * 0.4)} {f(cy - r * 0.7)} {f(cx - r * 0.1)} {f(cy - r * 0.78)} {f(cx + r * 0.1)} {f(cy - r * 0.78)}" fill="none" stroke="#E8C890" stroke-width="2" opacity="0.6"></path>')
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(w * 0.25, h * 0.92, "DARKLY", "#E8E2D6", 11, halo_="#1E1820") + plate_label(w * 0.75, h * 0.92, "FACE TO FACE", "#7A4A2A", 11, halo_="#FFF8E6"))
    return "".join(o)

def three_lamps(w, h, seed):
    """Now abideth faith, hope, love, these three; and the greatest of these is love: three lamps burning on a ledge, the
    third the brightest."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1028"></rect>']
    ty = h * 0.72
    o.append(f'<rect x="-10" y="{f(ty)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2418" stroke="{INK}" stroke-width="2.4"></rect>')
    k = min(w / 520, h / 200)
    for i, (x, nm) in enumerate(((0.22, "FAITH"), (0.5, "HOPE"), (0.78, "LOVE"))):
        big = i == 2
        o.append(lamp_glow(w * x, ty - 30 * k, (90 if big else 60) * k * (1.6 if big else 1), f"tl{seed}{i}", op=0.8 if big else 0.5)
                 + clay_lamp(w * x, ty - 2, k * (1.5 if big else 1.1)))
        o.append(plate_label(w * x, min(ty + 30 * k, h - 6), nm, "#FFE6A0" if big else "#E8D8B0", 12 if big else 11, halo_="#1A1028"))
    return "".join(o)

# ---- 1 Corinthians 14 --------------------------------------------------------------------------------------------------
def assembly(p, w, h, seed, stage="prophesy"):
    """The church come together in a house by lamplight: stage "prophesy" one standing to prophesy, his hand out, the rest
    seated listening; "unlearned" one praying aloud in a tongue (the jumble of his words a squiggle in a balloon), a man at the
    back with his head on one side; "order" one with a harp (a psalm) and one with a scroll (a teaching) waiting their turn
    while one speaks; "women" the women of the church seated together veiled, listening."""
    b = h * 0.92
    lx = 0.66 if stage in ("order", "unlearned") else 0.5
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * lx, h * 0.26, max(w, h) * 0.55, f"{p}as", op=0.5),
         clay_lamp(w * lx, h * 0.28, max(0.6, h / 300))]
    s = fit(b, b - min(h * 0.72, 196))
    sit = lambda x, i, fl=False: seated(w * x, b, s * 0.72, ["#6A5A3A", "#3A4A6A", "#7A3A3A", "#4A5A3A", "#5A4A6A"][i % 5], head=["#3A4A5A", None, "#E8E2D6", None, "#2A2A3A"][i % 5],
                                       beard=["#3A2A1A", "#2A1A10", "#8A847A", None, "#1A1210"][i % 5], flip=fl)
    if stage == "prophesy":
        o.append(robed(p, w * 0.2, b, s, "#4A5A7A", head="#E8E2D6", cord="#3A3A5A", beard="#5A4A3A", flip=True, up=[(-22, -158), (-46, -150), (-70, -156)]))
        for i, x in enumerate((0.44, 0.58, 0.72, 0.86)): o.append(sit(x, i, True))
    elif stage == "unlearned":
        o.append(robed(p, w * 0.24, b, s, "#6A4A5A", hair="#2A1A10", beard="#2A1A10", flip=True, up=[(-22, -158), (-34, -190), (-38, -222)]))
        bx, by = w * 0.24 + 40, b - 200 * s - 30
        o.append(f'<ellipse cx="{f(bx + 60)}" cy="{f(max(24, by))}" rx="70" ry="22" fill="#FFFFFF" stroke="{INK}" stroke-width="2"></ellipse>'
                 f'<path d="M{f(bx + 10)} {f(max(24, by))} q 8 -10 16 0 t 16 0 t 16 0 t 16 0 t 16 0 t 16 0" fill="none" stroke="{INK}" stroke-width="2"></path>')
        for i, x in enumerate((0.48, 0.62)): o.append(sit(x, i, True))
        o.append(robed(p, w * 0.86, b, s, "#8A8270", hair="#3A2A1A", beard="#3A2A1A", flip=True, up=[(-22, -158), (-30, -176), (-20, -196)]))
        o.append(jp(w * 0.86 + 30, b - 200 * s - 10, "?", 36, fill="#FFD23F", stroke="#0D0D0F", rot=10))
    elif stage == "order":
        o.append(robed(p, w * 0.5, b, s, "#4A5A7A", head="#E8E2D6", cord="#3A3A5A", beard="#5A4A3A", flip=True, up=[(-22, -158), (-46, -150), (-70, -156)]))
        o.append(robed(p, w * 0.16, b, s, "#6A7A4A", hair="#2A1A10", beard="#2A1A10", flip=True, up=[(-22, -158), (-40, -140), (-56, -130)]) + S2.harp(w * 0.16 + 60 * s, b - 120 * s, s * 0.8))
        o.append(robed(p, w * 0.84, b, s, "#7A5A3A", head="#3A4A5A", cord="#1A2A3A", beard="#3A2A1A", up=[(-22, -158), (-42, -150), (-58, -152)], extra=sealed_scroll(-60, -152, 0.2, rot=80)))
        o.append(sit(0.32, 3) + sit(0.68, 1, True))
    else:
        for i, x in enumerate((0.42, 0.56, 0.7, 0.84)):
            o.append(robed(p, w * x, b, s * 0.9, ["#7A5A6A", "#5A6A8A", "#6A7A5A", "#8A6A5A"][i], woman=True, veil=["#2A2A4A", "#E8E2D6", "#3A4A3A", "#2A3A5A"][i], flip=True))
        o.append(robed(p, w * 0.16, b, s, "#4A5A7A", head="#E8E2D6", cord="#3A3A5A", beard="#5A4A3A", flip=True, up=[(-22, -158), (-46, -150), (-70, -156)]))
    return "".join(o)

def instruments(w, h, seed):
    """Whether pipe or harp, if they give not a distinction in the sounds …; if the trumpet give an uncertain voice, who
    shall prepare himself for war? Three cells: the double pipe and its notes, the harp and its notes, and the trumpet blaring
    a wavering, broken sound."""
    o = []
    cw = w / 3
    k = min(cw / 200, h / 200)
    for i, c in enumerate(("#2A3A5A", "#3A2A4A", "#5A1A1A")):
        o.append(f'<rect x="{f(i * cw)}" y="-10" width="{f(cw + 1)}" height="{f(h + 20)}" fill="{c}"></rect>')
    px, py = cw * 0.5, h * 0.62                                  # the double pipe
    for d in (-1, 1):
        o.append(f'<path d="M{f(px)} {f(py + 40 * k)} L {f(px + d * 34 * k)} {f(py - 70 * k)}" stroke="{INK}" stroke-width="{f(9 * k)}" stroke-linecap="round"></path>'
                 f'<path d="M{f(px)} {f(py + 40 * k)} L {f(px + d * 34 * k)} {f(py - 70 * k)}" stroke="#C8A060" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>')
    o.append(S2.harp(cw * 1.5, h * 0.78, k * 1.3))
    o.append(trumpet(cw * 2.08, h * 0.66, k * 0.56, rot=-16))
    for i in range(2):                                          # clear notes from pipe and harp
        cx = cw * (i + 0.5)
        for j in range(3):
            nx, ny = cx + (j - 1) * 28 * k, h * (0.2 + 0.06 * (j % 2))
            o.append(f'<circle cx="{f(nx)}" cy="{f(ny)}" r="{f(5 * k)}" fill="#FFF4C2"></circle><path d="M{f(nx + 5 * k)} {f(ny)} l 0 {f(-20 * k)}" stroke="#FFF4C2" stroke-width="2"></path>')
    tx, ty = cw * 2.76, h * 0.42                                 # the trumpet's uncertain voice
    o.append(f'<path d="M{f(tx - 20 * k)} {f(ty + 10 * k)} l {f(14 * k)} {f(-22 * k)} l {f(8 * k)} {f(30 * k)} l {f(12 * k)} {f(-40 * k)} l {f(10 * k)} {f(34 * k)} l {f(10 * k)} {f(-20 * k)}" fill="none" stroke="#FFD23F" stroke-width="3"></path>')
    o.append(jp(cw * 2.52, h * 0.2, "ブ…ブォ?", min(26, h * 0.12), fill="#FFD23F", stroke="#0D0D0F", rot=8, roman="BU...BUO?"))
    for kk in (1, 2):
        o.append(f'<path d="M{f(cw * kk)} -10 L {f(cw * kk)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(cw * 0.5, h * 0.88, "PIPE", "#E8E2D6", 10, halo_="#0D0D0F") + plate_label(cw * 1.5, h * 0.88, "HARP", "#E8E2D6", 10, halo_="#0D0D0F")
             + plate_label(cw * 2.4, h * 0.88, "TRUMPET", "#E8E2D6", 10, halo_="#0D0D0F"))
    return "".join(o)

def barbarians(p, w, h, seed):
    """I shall be to him that speaketh a barbarian, and he … a barbarian unto me: two men face to face in the street, each
    speaking, and between them balloons of nothing but squiggles."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.8, seed, hmin=0.24, hmax=0.36), pavement(w, h, b, color="#D8CCB0")]
    s = fit(b, b - min(h * 0.66, 180))
    o.append(robed(p, w * 0.26, b, s, "#7A5A3A", head="#3A4A5A", cord="#1A2A3A", beard="#3A2A1A", flip=True, up=[(-22, -158), (-44, -146), (-62, -152)]))
    o.append(robed(p, w * 0.74, b, s, "#5A6A3A", hair="#B8A070", beard="#B8A070", skin="#E3B08A", up=[(-22, -158), (-44, -146), (-62, -152)]))
    for x, y, d in ((w * 0.4, b - 210 * s, 1), (w * 0.6, b - 170 * s, -1)):
        y = max(26, y)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="62" ry="20" fill="#FFFFFF" stroke="{INK}" stroke-width="2"></ellipse>'
                 f'<path d="M{f(x - 44)} {f(y)} q 7 -9 14 0 t 14 0 t 14 0 t 14 0 t 14 0 t 14 0" fill="none" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def voice_storm(w, h, seed):
    """By men of strange tongues … will I speak unto this people: a storm over the hills, the lightning — the Voice box over
    it (God is not drawn)."""
    return vista(w, h, seed, tone="storm", horizon=0.66, hills_n=2, bolts=2, rain_=True)

def falls_down(p, w, h, seed):
    """He will fall down on his face and worship God, declaring that God is among you indeed: the stranger who came in,
    on his knees on the floor of the assembly, his face to the ground, the church about him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, h * 0.26, max(w, h) * 0.55, f"{p}fd", op=0.55)]
    s = fit(b, b - min(h * 0.72, 196))
    o.append(E.kneel(w * 0.5, b, s * 0.9, color="#8A6A4A", skin=SKIN))
    o.append(robed(p, w * 0.18, b, s, "#4A5A7A", head="#E8E2D6", cord="#3A3A5A", beard="#5A4A3A", flip=True) + robed(p, w * 0.32, b, s * 0.94, "#7A5A6A", woman=True, veil="#2A2A4A", flip=True))
    o.append(robed(p, w * 0.72, b, s, "#6A7A4A", hair="#2A1A10", beard="#2A1A10") + robed(p, w * 0.86, b, s * 0.94, "#5A6A8A", woman=True, veil="#E8E2D6"))
    return "".join(o)
