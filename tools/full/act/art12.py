"""Drawings for Acts 21–22. The voyage by Cos, Rhodes and Patara to Tyre on the map; the disciples of Tyre with their wives
and children kneeling on the beach; Philip the evangelist's house at Cæsarea and his four daughters; Agabus binding his own
hands and feet with Paul's girdle; the road up to Jerusalem; James and the elders; Paul in the temple with the four men
under their vow. The riot and the arrest: the court of the temple in uproar, the people laying hold on Paul and the doors
being shut (no blow drawn — the beating told in words); the castle of Antonia and its stairs, the chief captain Claudius
Lysias (bareheaded, a red cloak) and his soldiers running down; Paul bound with two chains; Paul borne up the stairs by
the soldiers; Paul standing on the stairs beckoning with his hand, a great silence. His defence beside his face, with the
history drawn: the young Saul at the feet of Gamaliel; the Damascus road; Ananias; the trance in the temple, the light
(the Lord not drawn); Stephen's garments by the wall. The crowd casting off their garments and throwing dust into the
air; the examining by scourging (22:24–25) told in words only — Paul standing bound with the thongs before the centurion
in the castle court, no blow drawn; the council. Built on act.art11."""
from act.art11 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math

def lysias(p, x, y, s, flip=False, up=None):
    """Claudius Lysias, the chief captain: a red cloak over a cuirass, bareheaded, short dark hair, stubble."""
    cloak = '<path d="M-26 -164 C -40 -120 -36 -60 -30 -20 L -18 -20 C -22 -70 -20 -120 -14 -160 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></path>'
    cuirass = '<path d="M-24 -156 L 24 -156 L 22 -104 L -22 -104 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.6"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#E3B08A", cloth="#8A2A1A", kind="Tunic", sw=3, flip=flip, up=up, extra=cuirass + cloak + hair("#3A2A1A"))
def agabus(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#6A5A4A", head="#4A3A2A", cord="#2A1A10", bd="#D8D2C6", flip=flip, up=up)
WHO.update({"lysias": lysias, "agabus": agabus})

def beach_farewell(p, w, h, seed):
    """Kneeling down on the beach, we prayed: the shore outside Tyre, the disciples with their wives and children kneeling
    with Paul and his company, the ship waiting in the roads."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sea_(w, h, h * 0.5, seed), ship(w * 0.84, h * 0.58, max(0.4, h / 560)), shore(w, h, h * 0.66, color="#D8C090"),
         walls(-10, w * 0.3, h * 0.5, h * 0.2, seed, towers=2, gate=False)]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(E.kneel(w * 0.2, b, s * 0.86, color=ROBES["paul"], skin=SKIN, flip=True))
    for i, (x, c) in enumerate(((0.34, "#6A4A5A"), (0.46, "#3A4A6A"), (0.58, "#5A6A3A"), (0.7, "#7A3A3A"))):
        o.append(E.kneel(w * x, b, s * (0.84 if i != 2 else 0.6), color=c, skin=SKIN))
    return "".join(o)

def philip_house(p, w, h, seed, agabus_=False):
    """The house of Philip the evangelist at Cæsarea: Philip (a teal headcloth) at the door bidding them in; his four
    daughters sitting in a row in white and blue veils; agabus_=True Agabus come from Judæa, kneeling on the floor, his own
    hands and feet bound about with Paul's girdle, Paul and the others standing over him."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    if not agabus_:
        o.append(philip_ev(p, w * 0.2, b, s, flip=True, up=UP_CALL) + paul(p, w * 0.34, b, s))
        for i, x in enumerate((0.5, 0.62, 0.74, 0.86)):
            o.append(woman_fig(p, w * x, b, s * 0.86, ["#E8E2D6", "#5A6A8A", "#E8E2D6", "#5A6A8A"][i], ["#3A6A8A", "#F3EFE6", "#3A6A8A", "#F3EFE6"][i], flip=True))
    else:
        o.append(E.kneel(w * 0.44, b, s * 0.9, color="#6A5A4A", skin=SKIN))
        k = s * 0.9
        o.append(f'<path d="M{f(w * 0.44 + 20 * k)} {f(b - 126 * k)} C {f(w * 0.44 + 40 * k)} {f(b - 116 * k)} {f(w * 0.44 + 44 * k)} {f(b - 134 * k)} {f(w * 0.44 + 30 * k)} {f(b - 140 * k)}" stroke="#C8963E" stroke-width="{f(6 * k)}" fill="none"></path>'
                 f'<path d="M{f(w * 0.44 - 40 * k)} {f(b - 6 * k)} C {f(w * 0.44 - 20 * k)} {f(b - 16 * k)} {f(w * 0.44)} {f(b - 4 * k)} {f(w * 0.44 + 10 * k)} {f(b - 10 * k)}" stroke="#C8963E" stroke-width="{f(6 * k)}" fill="none"></path>')
        o.append(paul(p, w * 0.66, b, s, flip=True) + philip_ev(p, w * 0.78, b, s, flip=True) + woman_fig(p, w * 0.9, b, s * 0.86, "#E8E2D6", "#3A6A8A", flip=True))
        o.append(man_fig(p, w * 0.2, b, s, "#6A4A3A", hr="#2A1A10", bd="#2A1A10", up=[(22, -158), (14, -176), (8, -190)]))
    return "".join(o)

def up_to_jerusalem(w, h):
    """We went up to Jerusalem: the map, from Patara over against Cyprus to Tyre, Ptolemais, Cæsarea and up to Jerusalem."""
    return third_journey(w, h, legs=10, lit=[8, 9], title="ACTS 21:1–17 · UP TO JERUSALEM", box=(28.6, 36.4, 30.8, 37.0))

def temple_vow(p, w, h, seed):
    """Paul in the court of the temple with the four men that had a vow on them, their heads shaven, a priest receiving the
    offering."""
    bg, b = _temple(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(paul(p, w * 0.2, b, s, flip=True))
    shaved = '<path d="M-13 -190 C -12 -200 12 -200 13 -190 Z" fill="#8A6A4A" opacity="0.4"></path>'
    for i, x in enumerate((0.32, 0.42, 0.52, 0.62)):
        o.append(mk.person(p, round(w * x), round(b), round(s * 0.98, 3), body=SKIN, cloth="#F3EFE6", kind="Robe", sw=3, flip=True, extra=shaved))
    o.append(priest(p, w * 0.8, b, s, up=UP_BLESS))
    return "".join(o)

def temple_uproar(p, w, h, seed):
    """The court of the temple in uproar: the multitude pressing in on Paul from every side, their fists lifted; the great
    doors of the sanctuary swinging shut behind; the beating told in words only."""
    bg, b = _temple(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(crowd(p, w * 0.04, w * 0.36, b - 30 * s, b - 30 * s - 160 * s, 6, seed, up=UP_HIGH, flip=True))
    o.append(paul(p, w * 0.46, b, s))
    o.append(crowd(p, w * 0.56, w * 0.96, b, b - 180 * s, 6, seed + 1, up=UP_HIGH))
    o.append(crowd(p, w * 0.1, w * 0.38, b, b - 180 * s, 4, seed + 2, flip=True))
    return "".join(o)

def antonia(p, w, h, seed, stage="run"):
    """The castle of Antonia at the corner of the temple court: the tower and its wall, the long stairs going up; stage "run" —
    the chief captain and his soldiers running down the stairs, the crowd falling back from Paul; "bound" — Paul bound with two
    chains between two soldiers, Lysias questioning; "borne" — Paul carried up the stairs on the soldiers' shields, the
    multitude below crying out; "speak" — Paul standing on the stairs beckoning with his hand, the people silent below;
    "dust" — the crowd throwing off their garments and casting dust into the air."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.06)}" width="{f(w * 0.52)}" height="{f(b)}" fill="#B8A07A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.74)}" y="{f(-10)}" width="{f(w * 0.2)}" height="{f(b)}" fill="#A8906A" stroke="{INK}" stroke-width="2.4"></rect>']
    bw = max(8, h * 0.04)
    xx = w * 0.5
    while xx < w:
        o.append(f'<rect x="{f(xx)}" y="{f(h * 0.06 - bw)}" width="{f(bw)}" height="{f(bw + 1)}" fill="#B8A07A" stroke="{INK}" stroke-width="1.6"></rect>'); xx += bw * 1.9
    # the stairs from the court (left, low) up to the castle door (right, high)
    n = 8; x0, x1 = w * 0.3, w * 0.7; y0, y1 = b, h * 0.42
    for k in range(n):
        t0, t1 = k / n, (k + 1) / n
        o.append(f'<rect x="{f(x0 + (x1 - x0) * t0)}" y="{f(y0 - (y0 - y1) * t1)}" width="{f(x1 - x0 - (x1 - x0) * t0)}" height="{f((y0 - y1) / n + 1)}" fill="#D8C8A8" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="{f(w * 0.72)}" y="{f(y1 - h * 0.2)}" width="{f(w * 0.1)}" height="{f(h * 0.2)}" fill="#2A1A10" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b - 2)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    def on_stair(t): return x0 + (x1 - x0) * t + 20, y0 - (y0 - y1) * t
    s = fit(b, max(h * 0.4, b - 170))
    if stage == "run":
        for i, t in enumerate((0.3, 0.5, 0.7)):
            x, y = on_stair(t)
            o.append(soldier(p, x, y, s * 0.9, flip=True) if i else lysias(p, x, y, s * 0.94, flip=True, up=UP_BLESS))
        o.append(paul(p, w * 0.18, b, s))
        o.append(crowd(p, w * 0.02, w * 0.12, b, b - 160 * s, 2, seed, up=UP_HIGH))
    elif stage == "bound":
        o.append(soldier(p, w * 0.14, b, s, flip=True) + paul(p, w * 0.24, b, s) + soldier(p, w * 0.34, b, s))
        o.append(f'<path d="M{f(w * 0.18)} {f(b - 96 * s)} L {f(w * 0.24)} {f(b - 100 * s)} L {f(w * 0.3)} {f(b - 96 * s)}" stroke="#8A8A90" stroke-width="{f(3 * s)}" stroke-dasharray="{f(5 * s)} {f(2 * s)}" fill="none"></path>')
        x, y = on_stair(0.2)
        o.append(lysias(p, x, y, s * 0.94, flip=True, up=UP_BLESS))
        o.append(crowd(p, w * 0.0, w * 0.06, b, b - 160 * s, 1, seed, up=UP_HIGH))
    elif stage == "borne":
        x, y = on_stair(0.45)
        o.append(soldier(p, x - 30 * s, y + 20 * s, s * 0.9, flip=True) + soldier(p, x + 30 * s, y - 10 * s, s * 0.9, flip=True))
        o.append(f'<g transform="translate({f(x)} {f(y - 70 * s)}) rotate(-12)">' + paul(p, 0, 0, s * 0.9, up=UP_HIGH) + '</g>')
        o.append(crowd(p, w * 0.0, w * 0.3, b, b - 160 * s, 5, seed, up=UP_HIGH, flip=True))
    elif stage in ("speak", "dust"):
        x, y = on_stair(0.62)
        o.append(paul(p, x, y, s * 0.94, up=UP_HIGH if stage == "speak" else None) + soldier(p, x + 50 * s, y - 20 * s, s * 0.88, flip=True) + lysias(p, x + 100 * s, y - 40 * s, s * 0.88, flip=True))
        o.append(crowd(p, w * 0.0, w * 0.34, b, b - 160 * s, 6, seed, up=UP_HIGH if stage == "dust" else None, flip=True))
        if stage == "dust":
            r = random.Random(seed)
            for _ in range(26):
                o.append(f'<circle cx="{f(r.uniform(0, w * 0.4))}" cy="{f(r.uniform(h * 0.2, b - 120 * s))}" r="{f(r.uniform(3, 9))}" fill="#D8C8A0" opacity="0.7"></circle>')
            for i in range(4):
                cx = r.uniform(w * 0.04, w * 0.34); cy = r.uniform(h * 0.2, h * 0.5)
                o.append(f'<path d="M{f(cx)} {f(cy)} c 14 -10 30 -4 36 8 c -10 6 -24 10 -36 -8 Z" fill="{r.choice(["#6A4A3A", "#3A4A6A", "#8A2A2A"])}" stroke="{INK}" stroke-width="1.4"></path>')
    return "".join(o)

def gamaliel_feet(p, w, h, seed):
    """Brought up in this city at the feet of Gamaliel: the old teacher (white beard, a dark-blue headcloth with a gold band)
    sitting with the scroll of the law open across his knees, the young men sitting on the floor at his feet, Saul among them."""
    bg, b = _synagogue(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(b - 60 * s)}" width="{f(80 * s)}" height="{f(60 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(seated(w * 0.18, b - 46 * s, s * 0.86, "#2A3A5A", head="#2A3A5A", beard="#E8E2D6", band=True) + scroll(w * 0.28, b - 96 * s, 80 * s, 22 * s, lines=2))
    for i, (x, c, hd) in enumerate(((0.42, ROBES["paul"], "#5A4A3A"), (0.54, "#6A5A3A", None), (0.66, "#3A4A6A", "#3A4A6A"), (0.78, "#5A2A4A", None))):
        o.append(seated(w * x, b, s * 0.74, c, head=hd, beard="#3A2A1A" if i == 0 else ("#2A1A10" if i == 2 else None), flip=True))
    return "".join(o)

def temple_trance(p, w, h, seed):
    """While I prayed in the temple, I fell into a trance: Paul kneeling in the court before the sanctuary, a shaft of white
    light falling on him (the Lord not drawn — his words come from the light)."""
    bg, b = _temple(w, h, seed, "dusk")
    o = [mk.defs(p, *ALL), bg, shaft(w * 0.3, w, h, top_w=0.06, bot_w=0.16, op=0.5), glow(w * 0.3, b - h * 0.2, h * 0.4, "#FFFFFF", 0.7, f"{p}t")]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(E.kneel(w * 0.3, b, s * 0.9, color=ROBES["paul"], skin=SKIN, flip=True))
    return "".join(o)

def thongs(p, w, h, seed):
    """When they had tied him up with the thongs: the court within the castle, Paul standing with his hands bound behind him
    by leather thongs, the centurion standing by, soldiers at the gate — the scourging threatened is told in words only."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#B8A07A"), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.8)}" y="{f(h * 0.3)}" width="{f(w * 0.14)}" height="{f(b - h * 0.3)}" fill="#2A1A10" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b - h * 0.04)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.3, b - 200))
    o.append(paul(p, w * 0.3, b, s) + f'<path d="M{f(w * 0.3 - 16 * s)} {f(b - 96 * s)} L {f(w * 0.3 + 16 * s)} {f(b - 96 * s)}" stroke="#6A4A2A" stroke-width="{f(4 * s)}"></path>')
    o.append(centurion(p, w * 0.48, b, s))
    o.append(soldier(p, w * 0.72, b, s * 0.96, flip=True) + soldier(p, w * 0.12, b, s * 0.96))
    return "".join(o)
