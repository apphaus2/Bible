"""Drawings for John 18–19, with Matthew's and Mark's passion drawings (mat.art10, mat.art11, mrk.art9). Over the brook
Kidron by night into the garden; the band with lanterns and torches; I am he — the band gone backward and fallen to the
ground before Jesus standing (no one struck); Malchus' ear is words only, the sword lying dropped (mat.arrest); Annas'
hall; the door of the court and the maid that kept it; the officer's blow words only over the shut door; the fire of
coals; the Prætorium — Pilate going out to the Jews at its gate in the early morning, and within, Pilate and Jesus alone;
the purple robe laid aside on the empty court (the scourging and the crown of thorns words only); Behold, the man! — Jesus
far off on the steps in the purple garment beside Pilate, no wound drawn; Gabbatha; the road out of the gate to the hill,
a small procession far off, Jesus bearing the cross; the title in three tongues on its board, the letters not drawn;
three crosses on the hill from far off; his mother, her sister, Mary Magdalene and the beloved disciple small at the foot
of the hill; the darkened hill for I thirst, It is finished and the spear (words only); Joseph and Nicodemus at the new
tomb in the garden with the linen and the hundred pound of myrrh and aloes (no body drawn), and the stone. Built on
jhn.art8."""
from jhn.art8 import *
from jhn.art8 import f, INK, HEB, TWELVE, P, _loaf, LIE
import random, math
from mat.art11 import pilate_fig, roman_fig, golgotha, new_tomb

PURPLE = "#5A1A6A"

def lantern(x, y, s, uid):
    """A hand lantern carried on a pole: a small box of horn lit from within."""
    return (f'<path d="M{f(x)} {f(y)} L {f(x + 4 * s)} {f(y - 60 * s)}" stroke="#5A3A22" stroke-width="{f(4 * s)}"></path>'
            + glow(x + 4 * s, y - 66 * s, 40 * s, "#FFC14D", 0.8, uid)
            + f'<rect x="{f(x - 4 * s)}" y="{f(y - 76 * s)}" width="{f(16 * s)}" height="{f(18 * s)}" fill="#FFD23F" stroke="{INK}" stroke-width="1.6"></rect>')

def kidron(p, w, h, seed):
    """He went forth with his disciples over the brook Kidron, where was a garden: the stony brook in its valley under the
    moon, the olive garden on the far slope, Jesus and the eleven crossing over by the stepping-stones."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(50, w, h * 0.3, seed), moon(w * 0.86, h * 0.12, max(8, h * 0.035)),
         hills(w, h, h * 0.4, seed, color="#1E1E3A", amp=12, step=80)]
    for i, x in enumerate((0.56, 0.7, 0.84, 0.98)):
        o.append(olive(w * x, h * 0.56, h / 700, seed=seed + i).replace("#7A8A5A", "#3A4A3A"))
    o.append(ground(w, h, h * 0.56, "#2A2A40", dy=0))
    o.append(f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h * 0.8)} C {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.3)} {f(h * 0.78)} -10 {f(h * 0.82)} Z" fill="#2A4A6A" stroke="{INK}" stroke-width="2"></path>')
    for k in range(5):
        o.append(f'<ellipse cx="{f(w * (0.3 + 0.08 * k))}" cy="{f(h * 0.77)}" rx="{f(w * 0.025)}" ry="{f(h * 0.015)}" fill="#6A6A7A" stroke="{INK}" stroke-width="1.2"></ellipse>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.62, b, s * 0.94, flip=True))
    for i, who in enumerate(("peter", "john", "james", "andrew")):
        o.append(disciple(p, w * (0.48 - 0.11 * i), b - 4 * (i % 2), s * (0.92 - 0.02 * i), who, flip=True))
    return "".join(o)

def fell_back(p, w, h, seed):
    """When therefore he said unto them, I am he, they went backward, and fell to the ground: in the garden by torchlight
    Jesus standing still in a soft light, and before him the band of soldiers and the officers fallen back on the ground,
    their lanterns and torches tumbled; Judas among them — no one struck."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, *LIE), night(w, h, seed, n=40, top="#05051A", bot="#2A1A1A"), ground(w, h, h * 0.66, "#1E2A1E", dy=0)]
    for x in (0.06, 0.94): o.append(olive(w * x, h * 0.78, h / 300, seed=seed + int(x * 10)).replace("#7A8A5A", "#3A4A3A"))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(glow(w * 0.24, b - 110 * s, 160 * s, "#FFF4C2", 0.7, f"{p}g") + jesus(p, w * 0.24, b, s))
    for i, (x, col) in enumerate(((0.5, "#3A3A4A"), (0.66, "#8A2A1A"), (0.84, "#5A4A3A"))):
        o.append(f'<g transform="translate({f(w * x)} {f(b - 2)}) scale({f(s * 0.6)})" fill="{col}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    o.append(kneeler(w * 0.42, b, s * 0.76, ROBES["judas"], flip=True) + kneeler(w * 0.96, b, s * 0.72, "#4A3A3A", flip=True))
    o.append(f'<g transform="rotate(80 {f(w * 0.58)} {f(b)})">' + torch(w * 0.58, b, s * 0.7, f"{p}t1") + '</g>'
             + f'<g transform="rotate(-70 {f(w * 0.76)} {f(b)})">' + lantern(w * 0.76, b, s * 0.7, f"{p}l1") + '</g>')
    return "".join(o)

def court_door(p, w, h, seed):
    """The court of the high priest by night: the door in the wall, the maid that kept it standing in the doorway with her
    lamp, the other disciple bringing Peter in."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), night(w, h, seed, n=40, top="#05051A", bot="#2A1A2A"),
         f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="{f(b - h * 0.16)}" fill="#3A3038" stroke="{INK}" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.44)} {f(b)} L {f(w * 0.44)} {f(h * 0.4)} Q {f(w * 0.54)} {f(h * 0.28)} {f(w * 0.64)} {f(h * 0.4)} L {f(w * 0.64)} {f(b)} Z" fill="#FFC14D" opacity="0.55" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, b, "#2A2228", dy=0)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(woman_fig(p, w * 0.58, b, s * 0.94, "#5A6A4A", "#8A9A6A", flip=True))
    o.append(clay_lamp(w * 0.58 - 40 * s, b - 120 * s, s * 0.4))
    o.append(disciple(p, w * 0.32, b, s * 0.96, "john", up=UP_BLESS) + disciple(p, w * 0.18, b - 4, s * 0.98, "peter"))
    return "".join(o)

def praetorium(p, w, h, seed, stage="out"):
    """The Prætorium early in the morning. out: its gate and columns, Pilate come out on the steps in his white toga, the
    chief priests and the Jews standing below in the street, not entering; within: inside the hall, Pilate and Jesus alone,
    the morning light from the high windows."""
    b = h * 0.94
    if stage == "within":
        o = [mk.defs(p, *ALL), bgr(w, h, "#B8A888")]
        for x in (0.1, 0.9):
            o.append(f'<rect x="{f(w * x - 20)}" y="-10" width="40" height="{f(b + 10)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
        for x in (0.3, 0.5, 0.7):
            o.append(f'<rect x="{f(w * x - 16)}" y="{f(h * 0.1)}" width="32" height="{f(h * 0.2)}" fill="#FFF4C2" stroke="{INK}" stroke-width="2"></rect>'
                     f'<path d="M{f(w * x - 16)} {f(h * 0.3)} L {f(w * x - 60)} {f(b)} L {f(w * x + 60)} {f(b)} L {f(w * x + 16)} {f(h * 0.3)} Z" fill="#FFF4C2" opacity="0.18"></path>')
        o.append(pavement(w, h, b - h * 0.04, color="#A89878"))
        s = fit(b, max(h * 0.26, b - 230))
        o.append(pilate_fig(p, w * 0.64, b, s, flip=True, up=UP_BLESS))
        o.append(jesus(p, w * 0.36, b, s, glow=False))
        return "".join(o)
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFE6A0")]
    for x in (0.08, 0.2, 0.32, 0.44):
        o.append(f'<rect x="{f(w * x - 12)}" y="{f(h * 0.1)}" width="24" height="{f(h * 0.5)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w * 0.56)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.56)} {f(h * 0.6)} L {f(w * 0.6)} {f(h * 0.7)} L -10 {f(h * 0.7)} Z" fill="#C8B898" stroke="{INK}" stroke-width="2"></path>')
    o.append(pavement(w, h, h * 0.7))
    s = fit(h * 0.6, max(h * 0.12, h * 0.6 - 220))
    o.append(pilate_fig(p, w * 0.42, h * 0.6, s, flip=True, up=UP_BLESS))
    o.append(scribe_fig(p, w * 0.66, b, s * 1.05, white=True, flip=True) + scribe_fig(p, w * 0.78, b, s * 1.02, flip=True))
    o.append(crowd(p, w * 0.84, w * 0.99, b, b - 160 * s, 2, seed, flip=True))
    return "".join(o)

def behold_man(p, w, h, seed):
    """Behold, the man!: the Prætorium steps seen from the crowded street below, far off; Pilate standing on the steps with
    his arm out, and beside him Jesus, small, in the purple garment — nothing of the thorns' wounds drawn; the chief
    priests and the people in the street below, their backs to us."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#8A8A9A", "#E8C8A0")]
    for x in (0.2, 0.34, 0.66, 0.8):
        o.append(f'<rect x="{f(w * x - 12)}" y="{f(h * 0.08)}" width="24" height="{f(h * 0.44)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.02)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#D8CCB0" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(4):
        y = h * (0.52 + 0.04 * k)
        o.append(f'<rect x="{f(w * (0.12 - 0.03 * k))}" y="{f(y)}" width="{f(w * (0.76 + 0.06 * k))}" height="{f(h * 0.04)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(pavement(w, h, h * 0.68, color="#B8A888"))
    s = fit(h * 0.52, h * 0.52 - min(h * 0.3, 150))
    robe = jesus(p, w * 0.54, h * 0.52, s, glow=False).replace(JESUS_TUNIC, PURPLE).replace(JESUS_MANTLE, "#3A0A4A")
    wreath = f'<path d="M{f(w * 0.54 - 13 * s)} {f(h * 0.52 - 194 * s)} C {f(w * 0.54 - 6 * s)} {f(h * 0.52 - 200 * s)} {f(w * 0.54 + 6 * s)} {f(h * 0.52 - 200 * s)} {f(w * 0.54 + 13 * s)} {f(h * 0.52 - 194 * s)}" stroke="#3A2A1A" stroke-width="{f(3 * s)}" fill="none"></path>'
    o.append(robe + wreath)
    o.append(pilate_fig(p, w * 0.4, h * 0.52, s, up=UP_BLESS, flip=True))
    sc = fit(b, b - 180)
    o.append(scribe_fig(p, w * 0.12, b, sc, white=True) + scribe_fig(p, w * 0.86, b, sc * 0.98, flip=True))
    o.append(crowd(p, w * 0.24, w * 0.74, b + 10, b + 10 - 150 * sc * 0.9, 5, seed))
    return "".join(o)

def bearing_cross(p, w, h, seed):
    """He went out, bearing the cross for himself: from far off, the road from the city gate winding to the bare hill under a
    grey sky, a small procession on it — soldiers, and Jesus bearing the cross (nothing near, nothing in detail)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#6A6A7A", "#D8B898"), clouds(w, h * 0.14, seed, n=5, color="#4A4A5A", op=0.7, h=h),
         walls(w * 0.6, w + 10, h * 0.6, h * 0.4, seed, towers=2),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.3)} {f(h * 0.38)} {f(w * 0.44)} {f(h * 0.62)} Z" fill="#6A5A50" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, h * 0.62, "#A8987A", dy=0),
         f'<path d="M{f(w * 0.7)} {f(h * 0.62)} C {f(w * 0.6)} {f(h * 0.74)} {f(w * 0.4)} {f(h * 0.76)} {f(w * 0.2)} {f(h * 0.62)}" stroke="#D0C0A0" stroke-width="{f(max(6, h * 0.04))}" fill="none"></path>']
    y = h * 0.74; s = fit(y, y - h * 0.16)
    o.append(roman_fig(p, w * 0.58, y - 6, s) + roman_fig(p, w * 0.36, y - 4, s * 0.98))
    x = w * 0.47
    o.append(jesus(p, x, y, s, glow=False, up=[(-22, -158), (-30, -170), (-20, -176)]))
    o.append(f'<path d="M{f(x - 50 * s)} {f(y - 176 * s)} L {f(x + 80 * s)} {f(y - 30 * s)}" stroke="#5A3A22" stroke-width="{f(10 * s)}" stroke-linecap="round"></path>'
             f'<path d="M{f(x - 30 * s)} {f(y - 110 * s)} L {f(x + 30 * s)} {f(y - 160 * s)}" stroke="#5A3A22" stroke-width="{f(9 * s)}" stroke-linecap="round"></path>')
    o.append(crowd(p, w * 0.64, w * 0.9, h * 0.7, h * 0.7 - 140 * s, 4, seed, flip=True))
    return "".join(o)

def title_board(p, w, h, seed):
    """Pilate wrote a title also: the board of the title against the grey sky, three lines of writing in three tongues on
    it — Hebrew, Latin, Greek — the letters not drawn."""
    o = [sky(w, h, "#4A4A5A", "#A89888"), clouds(w, h * 0.3, seed, n=5, color="#3A3A4A", op=0.6, h=h)]
    bw, bh = min(w * 0.7, h * 1.4), min(h * 0.5, w * 0.36)
    x0, y0 = w * 0.5 - bw / 2, h * 0.5 - bh / 2
    o.append(f'<path d="M{f(w * 0.5)} {f(y0 + bh)} L {f(w * 0.5)} {f(h + 10)}" stroke="#4A2A18" stroke-width="{f(bh * 0.24)}"></path>')
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(bw)}" height="{f(bh)}" fill="#E8DCB8" stroke="{INK}" stroke-width="3"></rect>')
    for k, dash in enumerate(("10 4 4 4 16 4", "16 6 8 6 12 6", "6 4 12 4 8 4")):
        yy = y0 + bh * (k + 1) / 4
        o.append(f'<path d="M{f(x0 + bw * 0.08)} {f(yy)} L {f(x0 + bw * 0.92)} {f(yy)}" stroke="#2A1A10" stroke-width="{f(bh * 0.07)}" stroke-dasharray="{dash}"></path>')
    return "".join(o)

def at_cross(p, w, h, seed):
    """There were standing by the cross of Jesus his mother, and his mother's sister, Mary the wife of Clopas, and Mary
    Magdalene: the hill of the three crosses far off against the darkening sky, and at its foot, small, the four women and
    the beloved disciple standing together (no one on the hill drawn in any detail)."""
    b = h * 0.94
    o = [golgotha(p, w, h, seed, dark=False)]
    y = h * 0.86; s = fit(y, y - h * 0.18)
    cols = [(ROBES["mary"], "#3A6AA8"), ("#5A5A7A", "#3A3A5A"), ("#6A4A2A", "#5A3A22"), (ROBES["magdalene"], "#C2456A")]
    for i, (c, sc) in enumerate(cols):
        o.append(woman_fig(p, w * (0.36 + 0.07 * i), y - 2 * (i % 2), s * (0.96 - 0.02 * i), c, sc))
    o.append(disciple(p, w * 0.66, y, s, "john"))
    return "".join(o)

def burial(p, w, h, seed):
    """Joseph of Arimathæa and Nicodemus in the garden at evening, at the door of the new tomb: the linen cloths folded in
    Joseph's arms, Nicodemus with the great jar of myrrh and aloes, the tomb hewn in the rock behind (no body drawn)."""
    b = h * 0.94
    o = [new_tomb(p, w, h, seed, stone=False)]
    s = fit(b, max(h * 0.3, b - 220))
    linen_ = '<path d="M-60 -136 L -20 -140 L -18 -116 L -58 -112 Z" fill="#F8F4EC" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(mk.person(p, round(w * 0.3), round(b), round(s, 3), body="#C98E66", cloth="#5A5A4A", kind="Robe", sw=3, up=[(-22, -158), (-40, -134), (-50, -126)],
                       extra=A.headcloth("#1F3A5A", cord="#E8B830") + GREY_BEARD + linen_, flip=True))
    jar_ = '<path d="M-64 -150 C -78 -140 -78 -104 -64 -96 L -40 -96 C -26 -104 -26 -140 -40 -150 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.8"></path>'
    o.append(mk.person(p, round(w * 0.16), round(b), round(s * 0.98, 3), body="#C98E66", cloth="#3E2C62", kind="Robe", sw=3, up=[(-22, -158), (-40, -134), (-50, -120)],
                       extra=A.headcloth("#3E2C62", cord="#E8B830") + GREY_BEARD + jar_, flip=True))
    return "".join(o)

def dark_hill(p, w, h, seed):
    """The darkness: the hill of the three crosses far off under a black sky, a dull red glow low behind the hilltop so the
    three crosses stand out as small dark shapes — nothing on them drawn, no one near."""
    hx = w * 0.56
    o = [sky(w, h, "#05050E", "#2A1012"), glow(hx, h * 0.46, h * 0.5, "#8A2A1A", 0.55, f"{p}g"),
         f'<path d="M{f(hx - w * 0.5)} {f(h * 0.78)} C {f(hx - w * 0.24)} {f(h * 0.4)} {f(hx + w * 0.2)} {f(h * 0.38)} {f(hx + w * 0.5)} {f(h * 0.78)} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>']
    k = max(0.3, h / 900)
    for dx, tall in ((-0.12, 0.9), (0, 1.0), (0.12, 0.9)):
        x = hx + dx * w; base = h * 0.44 + abs(dx) * h * 0.1; ch = 120 * k * tall
        o.append(f'<path d="M{f(x)} {f(base)} L {f(x)} {f(base - ch)} M{f(x - 30 * k)} {f(base - ch * 0.78)} L {f(x + 30 * k)} {f(base - ch * 0.78)}" stroke="#050505" stroke-width="{f(6 * k + 1)}"></path>')
    o.append(ground(w, h, h * 0.8, "#120E12", dy=0))
    return "".join(o)
