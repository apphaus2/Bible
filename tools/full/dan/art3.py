"""Drawings for Daniel chapter 3 (Daniel 5–6): Belshazzar's feast, the writing on the plaster (a script of light, no hand
drawn), MENE, TEKEL, PERES as a plate, Babylon dark in that night; Darius's hundred and twenty satraps as a chart, Daniel
at his open window toward Jerusalem, the den of lions from above (the stone and the seals), the den within."""
from dan.art import *
from dan.art import f, K2, GREY_BEARD
import random, math

def lampstand(x, y, k):
    """A tall lampstand of gold with its lamps lit ((x, y) = its foot)."""
    o = [f'<path d="M{f(x - 16 * k)} {f(y)} L {f(x - 4 * k)} {f(y - 12 * k)} L {f(x + 4 * k)} {f(y - 12 * k)} L {f(x + 16 * k)} {f(y)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<rect x="{f(x - 3 * k)}" y="{f(y - 120 * k)}" width="{f(6 * k)}" height="{f(110 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>',
         f'<path d="M{f(x - 30 * k)} {f(y - 120 * k)} L {f(x + 30 * k)} {f(y - 120 * k)}" stroke="#0D0D0F" stroke-width="{f(7 * k)}"></path><path d="M{f(x - 30 * k)} {f(y - 120 * k)} L {f(x + 30 * k)} {f(y - 120 * k)}" stroke="#E8B830" stroke-width="{f(4 * k)}"></path>']
    for d in (-28, -10, 10, 28):
        o.append(E.flame(x + d * k, y - 124 * k, 6 * k, 16 * k, 1))
    return "".join(o)

def feast(p, w, h, seed, stage="feast"):
    """The great feast to a thousand lords: long tables set with gold and silver vessels, the lords and the king drinking, the
    lampstand by the plastered wall. stage "write": over against the lampstand, upon the plaster, lines of a script of light
    (no hand drawn); the king risen, the lords turned to the wall."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>',
         f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#E8DCC0" stroke="#0D0D0F" stroke-width="2"></rect>',
         frieze(w, h * 0.04, h * 0.05, color=GLAZE), bab_floor(w, h, h * 0.64, color="#8A6A4A")]
    k = min(1.4, h / 360)
    o.append(lampstand(w * 0.62, h * 0.64, k))
    if stage == "write":
        r = random.Random(seed)
        gx, gy = w * 0.38, h * 0.14
        o.append(f'<rect x="{f(gx - 10)}" y="{f(gy - 14)}" width="{f(w * 0.27)}" height="{f(h * 0.28)}" fill="#5A4A3A" opacity="0.35"></rect>')
        for row in range(3):
            x = gx
            while x < gx + w * 0.24:
                ww = r.uniform(10, 20) * k
                d = f"M{f(x)} {f(gy + row * h * 0.08 + r.uniform(0, 6))} l {f(ww * 0.3)} {f(-12 * k)} l {f(ww * 0.4)} {f(20 * k)} l {f(ww * 0.3)} {f(-14 * k)}"
                o.append(f'<path d="{d}" fill="none" stroke="#FFF4C2" stroke-width="{f(7 * k)}" stroke-linecap="round" stroke-linejoin="round" opacity="0.6"></path>'
                         f'<path d="{d}" fill="none" stroke="#FF8A3D" stroke-width="{f(2.6 * k)}" stroke-linecap="round" stroke-linejoin="round"></path>')
                x += ww + 8 * k
        o.append(V.rays(gx + w * 0.12, gy + h * 0.1, 20, 10, w * 0.3, color="#FFF4C2", op=0.18))
    s = fit(b, max(h * 0.2, b - 230))
    ty = h * 0.84
    o.append(f'<rect x="{f(w * 0.02)}" y="{f(ty)}" width="{f(w * 0.5)}" height="{f(10 * k)}" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(6):
        x = w * (0.06 + i * 0.08)
        o.append(prince(p, x, ty + 10 * k - 2, s * 0.8, PRINCE[i % 7], flip=stage == "write" and i % 2 == 0))
    o.append(f'<rect x="{f(w * 0.0)}" y="{f(ty + 2)}" width="{f(w * 0.54)}" height="{f(h - ty)}" fill="#7A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(7):
        x = w * (0.05 + i * 0.07)
        o.append(cup(x, ty + 2, k * 0.5, fill="#7A1A2A") if i % 2 == 0 else bowl(x, ty + 2, k * 0.45, fill="#C8D0D8", color="#C8D0D8"))
    o.append(bel(p, w * 0.86, b, s * 1.06, flip=stage != "write", up=[(-22, -158), (-26, -176), (-14, -196)] if stage == "feast" else [(-22, -158), (-40, -150), (-56, -160)]))
    if stage == "feast": o.append(cup(w * 0.86 - 12 * s, b - 196 * s, s * 0.7, fill="#7A1A2A"))
    return "".join(o)

def mene_plate(w, h):
    """MENE, TEKEL, PERES as a technical plate: numbered (a count closed off), weighed (a balance, the pan of the king found
    wanting), divided (a kingdom split in two, to the Medes and the Persians)."""
    o = [grid_bg(w, h)]
    k = min(1.3, h / 200, w / 600)
    cols = [("MENE", "NUMBERED"), ("TEKEL", "WEIGHED"), ("PERES", "DIVIDED")]
    for i, (a, b2) in enumerate(cols):
        cx = w * (0.18 + i * 0.32); cy = h * 0.46
        o.append(f'<rect x="{f(cx - w * 0.14)}" y="{f(h * 0.08)}" width="{f(w * 0.28)}" height="{f(h * 0.84)}" fill="none" stroke="#1E5A7A" stroke-width="1.4"></rect>')
        if i == 0:
            for j in range(9):
                o.append(f'<path d="M{f(cx - 40 * k + j * 10 * k)} {f(cy - 26 * k)} L {f(cx - 40 * k + j * 10 * k)} {f(cy + 26 * k)}" stroke="#FFD23F" stroke-width="2.4"></path>')
            o.append(f'<path d="M{f(cx - 48 * k)} {f(cy + 20 * k)} L {f(cx + 48 * k)} {f(cy - 20 * k)}" stroke="#D7261E" stroke-width="3"></path>')
        elif i == 1:
            o.append(f'<path d="M{f(cx)} {f(cy - 40 * k)} L {f(cx)} {f(cy + 34 * k)} M{f(cx - 18 * k)} {f(cy + 34 * k)} L {f(cx + 18 * k)} {f(cy + 34 * k)}" stroke="#FFD23F" stroke-width="2.4"></path>'
                     f'<path d="M{f(cx - 54 * k)} {f(cy - 40 * k)} L {f(cx + 54 * k)} {f(cy - 20 * k)}" stroke="#FFD23F" stroke-width="2.4"></path>')
            for sx, dy, lab in ((-1, -40, "THE KING"), (1, -20, "")):
                x0 = cx + sx * 54 * k; y0 = cy + dy * k
                o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x0 - 16 * k)} {f(y0 + 26 * k)} M{f(x0)} {f(y0)} L {f(x0 + 16 * k)} {f(y0 + 26 * k)}" stroke="#FFD23F" stroke-width="1.4"></path>'
                         f'<path d="M{f(x0 - 20 * k)} {f(y0 + 26 * k)} C {f(x0 - 16 * k)} {f(y0 + 36 * k)} {f(x0 + 16 * k)} {f(y0 + 36 * k)} {f(x0 + 20 * k)} {f(y0 + 26 * k)} Z" fill="#FFD23F" fill-opacity="0.3" stroke="#FFD23F" stroke-width="2"></path>')
            o.append(label(cx - 54 * k, cy + 2 * k, "FOUND WANTING", "#FF8A6A", max(7, 8 * k)))
        else:
            o.append(f'<path d="M{f(cx - 50 * k)} {f(cy - 30 * k)} L {f(cx - 6 * k)} {f(cy - 34 * k)} L {f(cx - 12 * k)} {f(cy)} L {f(cx - 4 * k)} {f(cy + 32 * k)} L {f(cx - 46 * k)} {f(cy + 30 * k)} Z" fill="#8FD0E2" fill-opacity="0.25" stroke="#8FD0E2" stroke-width="2"></path>'
                     f'<path d="M{f(cx + 50 * k)} {f(cy - 30 * k)} L {f(cx + 8 * k)} {f(cy - 34 * k)} L {f(cx + 2 * k)} {f(cy)} L {f(cx + 10 * k)} {f(cy + 32 * k)} L {f(cx + 46 * k)} {f(cy + 30 * k)} Z" fill="#FF8A6A" fill-opacity="0.25" stroke="#FF8A6A" stroke-width="2"></path>'
                     + label(cx - 28 * k, cy + 50 * k, "MEDES", CYAN, max(7, 8 * k)) + label(cx + 28 * k, cy + 50 * k, "PERSIANS", "#FF8A6A", max(7, 8 * k)))
        o.append(label(cx, h * 0.2, a, "#FFD23F", max(12, 18 * k)) + label(cx, h * 0.86, b2, CYAN, max(8, 10 * k)))
    return "".join(o)

def purple_chain(p, w, h, seed):
    """Daniel clothed with purple, a chain of gold about his neck, proclaimed third ruler, in the emptied banquet house."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>',
         f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#C8BCA0" stroke="#0D0D0F" stroke-width="2"></rect>',
         frieze(w, h * 0.04, h * 0.05, color=GLAZE), bab_floor(w, h, h * 0.64, color="#8A6A4A"), lampstand(w * 0.14, h * 0.64, min(1.4, h / 360))]
    s = fit(b, max(h * 0.2, b - 250))
    o.append(mk.person(p, round(w * 0.5), round(b), round(s, 3), body=SKIN, cloth="#5A1A6A", sw=3, extra=A.headcloth(DAN_H, cord="#2A1A10") + beard("#6A645E") + CHAIN))
    o.append(bel(p, w * 0.8, b, s * 1.02, flip=True, up=[(-22, -158), (-46, -164), (-70, -170)]))
    for i in range(3): o.append(prince(p, w * (0.26 + i * 0.07), b - 14, s * 0.86, PRINCE[i]))
    return "".join(o)

def dark_palace(w, h, seed):
    """In that night: the palace of Babylon dark against the stars, one lamp gone out (no one drawn)."""
    o = [babylon(w, h, seed, tone="night")]
    o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0F0E2A" opacity="0.35"></rect>')
    o.append(smoke(w * 0.72, h * 0.3, 5, seed, color="#3A3A5A", op=0.5, k=min(1.4, h / 300)))
    return "".join(o)

# ---- Daniel 6 ------------------------------------------------------------------------------------------------------------------
def satraps_chart(w, h):
    """Darius's kingdom as a chart: the king, the three presidents (Daniel one of them, lit), a hundred and twenty satraps."""
    o = [grid_bg(w, h)]
    kx, ky = w * 0.5, h * 0.14
    o.append(node(kx, ky, "DARIUS · THE KING", "#FF8A6A", r=8, dy=-14, size=11))
    xs = [w * 0.24, w * 0.5, w * 0.76]
    for i, x in enumerate(xs):
        o.append(route([(kx, ky + 8), (x, h * 0.36 - 8)], color="#8FD0E2", arrow=False))
        o.append(f'<rect x="{f(x - w * 0.09)}" y="{f(h * 0.33)}" width="{f(w * 0.18)}" height="{f(h * 0.08)}" fill="{"#1F5FAD" if i == 1 else "#12113A"}" fill-opacity="0.5" stroke="{"#FFD23F" if i == 1 else CYAN}" stroke-width="2"></rect>'
                 + label(x, h * 0.385, "DANIEL" if i == 1 else "A PRESIDENT", "#FFD23F" if i == 1 else CYAN, 10))
    for j in range(120):
        col, row = j % 30, j // 30
        x = w * (0.04 + col * 0.0315); y = h * (0.56 + row * 0.09)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.022)}" height="{f(h * 0.05)}" fill="#FFD23F" fill-opacity="0.18" stroke="#FFD23F" stroke-width="1"></rect>')
    o.append(label(w * 0.5, h * 0.53, "A HUNDRED AND TWENTY SATRAPS · THROUGHOUT THE WHOLE KINGDOM", "#FFD23F", 9))
    return "".join(o)

def darius_court(p, w, h, seed, n=5):
    """Darius on his throne; the presidents and satraps assembled before him."""
    b = h * 0.94
    o = [bab_hall(p, w, h, seed, floor=0.62), throne_k(p, w, h, w * 0.84, b, "darius")]
    s = fit(b, max(h * 0.2, b - 250))
    for i in range(n): o.append(prince(p, w * (0.08 + i * 0.1), b - (i % 2) * 10, s * (0.92 + (i % 2) * 0.04), PRINCE[(i + 2) % 7]))
    return "".join(o)

def signed(w, h, seed):
    """The writing and the interdict signed, sealed with the king's seal: according to the law of the Medes and Persians."""
    return letter_scroll(w, h, seed, seal="#A8283A", text_lines=7)

from ezr.art import letter_scroll

def window_prayer(p, w, h, seed, watchers=False):
    """Daniel's upper chamber: the windows open toward Jerusalem, the hills far off in the sun, Daniel kneeling upon his
    knees; watchers=True: the men assembled at the door, finding him in prayer."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8A6A4A"></rect>']
    wx, ww, wy, wh = w * 0.36, w * 0.4, h * 0.08, h * 0.56
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#8FD0E2" stroke="#0D0D0F" stroke-width="3"></rect>')
    o.append(f'<g clip-path="none">' + f'<path d="M{f(wx)} {f(wy + wh * 0.72)} C {f(wx + ww * 0.3)} {f(wy + wh * 0.6)} {f(wx + ww * 0.6)} {f(wy + wh * 0.66)} {f(wx + ww)} {f(wy + wh * 0.58)} L {f(wx + ww)} {f(wy + wh)} L {f(wx)} {f(wy + wh)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    o.append(sun(wx + ww * 0.7, wy + wh * 0.3, max(6, h * 0.03), color="#FFE680", op=0.3))
    o.append(label(wx + ww * 0.75, wy + wh * 0.16, "TOWARD JERUSALEM", "#0B2A4A", max(8, min(11, h / 40))))
    o.append(f'<path d="M{f(wx + ww / 2)} {f(wy)} L {f(wx + ww / 2)} {f(wy + wh)}" stroke="#5A3A22" stroke-width="6"></path>')
    o.append(f'<path d="M{f(wx - 10)} {f(wy + wh)} L {f(wx + ww + 10)} {f(wy + wh)}" stroke="#5A3A22" stroke-width="10"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4030" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(V.rays(wx + ww / 2, wy + wh * 0.4, 16, 10, h * 0.7, color="#FFF4C2", op=0.12))
    ks = h * 0.4 / 130
    o.append(E.kneel(w * 0.52, h * 0.86, ks, color=DAN_C, skin="#C98E66"))
    if watchers:
        o.append(f'<rect x="{f(w * 0.02)}" y="{f(h * 0.2)}" width="{f(w * 0.2)}" height="{f(h * 0.66)}" fill="#2A1A10" stroke="#0D0D0F" stroke-width="3"></rect>')
        s = fit(h * 0.86, h * 0.28)
        for i in range(3): o.append(prince(p, w * (0.06 + i * 0.06), h * 0.86, s * (1 - i * 0.04), PRINCE[(i + 3) % 7]))
    return "".join(o)

def den_mouth(p, w, h, seed, stage="sealed"):
    """The den of lions seen from without: a pit in the rock, its mouth. stage "cast": Daniel brought to the mouth, the king
    and his men about it; "sealed": the stone laid upon the mouth, sealed with the king's signet and his lords'; "dawn": the
    king come in haste very early, crying at the stone; "up": Daniel taken up out of the den, unhurt; "empty": the sealed
    stone at dusk, no one drawn."""
    b = h * 0.95
    skies = {"cast": ("#5A3A5A", "#E88A5A"), "sealed": ("#2A1A3A", "#8A5A6A"), "dawn": ("#8A9AC8", "#FFD8A0"), "up": ("#8FD0E2", "#FFE8C0"), "empty": ("#2A1A3A", "#C86A3A")}
    o = [mk.defs(p, *ALL), K2.sky(w, h, *skies[stage]), ground(w, h, h * 0.62, "#8A7A6A", dy=0)]
    mx, my = w * 0.5, h * 0.76
    o.append(f'<ellipse cx="{f(mx)}" cy="{f(my)}" rx="{f(w * 0.2)}" ry="{f(h * 0.08)}" fill="#120A08" stroke="#0D0D0F" stroke-width="3"></ellipse>'
             f'<path d="M{f(mx - w * 0.22)} {f(my)} C {f(mx - w * 0.2)} {f(my - h * 0.12)} {f(mx + w * 0.2)} {f(my - h * 0.12)} {f(mx + w * 0.22)} {f(my)}" fill="none" stroke="#6A5A4A" stroke-width="{f(max(6, h * 0.03))}"></path>')
    if stage in ("sealed", "dawn", "empty"):
        o.append(f'<ellipse cx="{f(mx)}" cy="{f(my - h * 0.02)}" rx="{f(w * 0.21)}" ry="{f(h * 0.08)}" fill="#6A6470" stroke="#0D0D0F" stroke-width="2.6"></ellipse>'
                 f'<path d="M{f(mx - w * 0.21)} {f(my - h * 0.02)} L {f(mx - w * 0.21)} {f(my + h * 0.02)} M{f(mx + w * 0.21)} {f(my - h * 0.02)} L {f(mx + w * 0.21)} {f(my + h * 0.02)}" stroke="#0D0D0F" stroke-width="2"></path>')
        for dx in (-0.08, 0.0, 0.08):
            o.append(f'<path d="M{f(mx + dx * w)} {f(my - h * 0.1)} L {f(mx + dx * w)} {f(my - h * 0.02)}" stroke="#C8A06A" stroke-width="2"></path>'
                     f'<circle cx="{f(mx + dx * w)}" cy="{f(my - h * 0.02)}" r="{f(max(5, h * 0.018))}" fill="{"#E8B830" if dx == 0 else "#B5121B"}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    s = fit(b, b - h * 0.48)
    if stage == "cast":
        o.append(darius(p, w * 0.86, b, s, flip=True, up=[(-22, -158), (-44, -166), (-66, -170)]))
        o.append(dan_fig(p, mx, my - h * 0.06, s * 0.9, age=3))
        for i in range(3): o.append(guard(p, w * (0.12 + i * 0.08), b - (i % 2) * 6, s * 0.95, cloth="#5A4A6A"))
    if stage == "sealed":
        o.append(darius(p, w * 0.82, b, s, flip=True) + prince(p, w * 0.12, b, s, PRINCE[0]) + prince(p, w * 0.2, b - 6, s * 0.96, PRINCE[3]))
    if stage == "dawn":
        o.append(sun(w * 0.86, h * 0.56, max(10, h * 0.05), color="#FFE680", op=0.35))
        o.append(darius(p, w * 0.76, b, s, flip=True, up=[(-22, -158), (-46, -150), (-70, -140)]))
    if stage == "up":
        o.append(darius(p, w * 0.82, b, s, flip=True, up=[(-22, -158), (-40, -190), (-34, -224)]))
        o.append(dan_fig(p, w * 0.5, my - h * 0.04, s * 0.9, age=3))
        for i in range(2): o.append(man(p, w * (0.22 + i * 0.08), b, s * 0.94, "#5A4A3A", up=[(-22, -158), (-6, -150), (14, -140)]))
        o.append(f'<path d="M{f(w * 0.3)} {f(b - 120 * s)} C {f(w * 0.4)} {f(b - 80 * s)} {f(w * 0.45)} {f(my - h * 0.1)} {f(w * 0.5)} {f(my - h * 0.1)}" fill="none" stroke="#8A6A3A" stroke-width="3"></path>')
    return "".join(o)

def king_night(p, w, h, seed):
    """The king in his palace passing the night fasting: his bed, no instruments of music, the lamp, his sleep fled from him."""
    o = [bab_hall(p, w, h, seed, floor=0.7, tone="night")]
    o.append(K1.bed(w, h, w * 0.16, w * 0.62, h * 0.86, cover="#8A1A2A", head="#C98E66", hair="#8A847A"))
    o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.86)} l 8 -30 l 8 30 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>' + E.flame(w * 0.7 + 8, h * 0.86 - 32, 8, 18, 2))
    return "".join(o)
