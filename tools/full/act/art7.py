"""Drawings for Acts 12–13. Herod the king (Agrippa: a gold diadem, a black beard, royal purple — not the tetrarch); James'
death (12:2) told in words only over the palace doorway at night; Peter seized and kept by four quaternions of soldiers;
the church praying by night; Peter asleep between two soldiers, bound with two chains; the angel of the Lord (white light,
a gold rim, no face) and a light in the cell, the chains fallen; the iron gate opening of its own accord; Mary's house,
Peter knocking at the door of the gate and Rhoda inside; the guards (12:19) told in words only over the empty cell; Herod
in royal apparel on his throne at Cæsarea making his oration; his death (12:23) in words only over the empty throne. The
church at Antioch fasting, the Holy Spirit's words in the Voice box, the hands laid on Barnabas and Saul; the first
journey on the map; the proconsul Sergius Paulus in his hall at Paphos, Elymas standing against them (no sorcery drawn; his
blindness told in words over the dark mist where he stood); the synagogue at Antioch of Pisidia; Paul's sermon beside his
face, with Samuel and Saul the son of Kish (1 Samuel's figures), David the shepherd-king, John at the Jordan; the Gentiles
glad; the dust shaken off at the gate. Built on act.art6."""
from act.art6 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
from mrk.art3 import palace_door
from mat.art3 import dust_gate

def agrippa(p, x, y, s, flip=False, up=None): return king_fig(p, x, y, s, cloth="#5A1A6A", bd="#2A1A10", flip=flip, up=up)
def mark_fig(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#8A7A4A", hr="#3A2214", flip=flip, up=up, kind="Tunic")
def sergius(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#5A4A3A", border="#6A1A5A", flip=flip, up=up)
def elymas(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#2A1A2A", head="#3A1A3A", cord="#E8B830", bd="#1A1210", flip=flip, up=up)
WHO.update({"agrippa": agrippa, "mark": mark_fig, "sergius": sergius, "elymas": elymas})

def herod_throne(p, w, h, seed, herod=True, crowd_=True):
    """Herod arrayed in royal apparel on the throne at Cæsarea: the throne on its high dais under a purple canopy between
    white columns, the people of Tyre and Sidon below with their hands raised, shouting; herod=False the throne empty, the
    canopy and the dais only (his death told in words)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2") if herod else sky(w, h, "#2A2A4A", "#8A6A7A")]
    for x in (0.08, 0.92):
        o.append(f'<rect x="{f(w * x - 18)}" y="{f(h * 0.06)}" width="36" height="{f(b)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    cx = w * 0.66 if crowd_ else w * 0.5
    dy = b - h * 0.22
    o.append(f'<path d="M{f(cx - w * 0.2)} {f(h * 0.12)} L {f(cx + w * 0.2)} {f(h * 0.12)} L {f(cx + w * 0.16)} {f(h * 0.24)} L {f(cx - w * 0.16)} {f(h * 0.24)} Z" fill="#5A1A6A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(cx - w * 0.2)} {f(h * 0.12)} L {f(cx + w * 0.2)} {f(h * 0.12)}" stroke="#E8B830" stroke-width="5"></path>')
    for k in range(3):
        o.append(f'<rect x="{f(cx - w * (0.2 - 0.03 * k))}" y="{f(dy + h * 0.07 * k)}" width="{f(w * (0.4 - 0.06 * k))}" height="{f(h * 0.07)}" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></rect>')
    k = max(0.5, h / 320)
    o.append(f'<path d="M{f(cx - 40 * k)} {f(dy)} L {f(cx - 40 * k)} {f(dy - 120 * k)} C {f(cx - 40 * k)} {f(dy - 140 * k)} {f(cx + 40 * k)} {f(dy - 140 * k)} {f(cx + 40 * k)} {f(dy - 120 * k)} L {f(cx + 40 * k)} {f(dy)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 48 * k)}" y="{f(dy - 50 * k)}" width="{f(96 * k)}" height="{f(14 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>')
    if herod:
        s2 = fit(dy, dy - min(dy * 0.7, 190 * k))
        o.append(glow(cx, dy - 120 * k, 120 * k, "#FFFFFF", 0.6, f"{p}h") + agrippa(p, cx, dy - 4, s2 * 0.9, flip=True, up=UP_BLESS))
    if crowd_:
        s = fit(b, max(h * 0.3, b - 200))
        o.append(crowd(p, w * 0.04, w * 0.42, b, b - 170 * s, 6, seed, flip=True, up=UP_HIGH if herod else None))
    return "".join(o)

def quaternions(p, w, h, seed):
    """Delivered to four quaternions of soldiers to guard him: the prison of the king at Jerusalem, its iron-bound door, and
    the soldiers standing guard before it with their spears, Peter led in between two of them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#8A6A7A"), f'<rect x="-10" y="{f(h * 0.14)}" width="{f(w + 20)}" height="{f(b - h * 0.14)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(8):
        y = h * 0.14 + (b - h * 0.14) * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#4A3E3A" stroke-width="2"></path>')
    o.append(f'<rect x="{f(w * 0.44)}" y="{f(h * 0.34)}" width="{f(w * 0.16)}" height="{f(b - h * 0.34)}" fill="#3A3A44" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(w * 0.44)} {f(h * 0.34 + (b - h * 0.34) * k / 4)} L {f(w * 0.6)} {f(h * 0.34 + (b - h * 0.34) * k / 4)}" stroke="#1A1A20" stroke-width="3"></path>' for k in (1, 2, 3)))
    s = fit(b, max(h * 0.3, b - 200))
    spear = '<path d="M24 -150 L 34 -250" stroke="#5A3A22" stroke-width="4"></path><path d="M34 -250 l -5 -14 l 9 3 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1"></path>'
    for x in (0.08, 0.18, 0.7, 0.8, 0.9):
        o.append(soldier_fig(p, w * x, b, s * 0.96, flip=x > 0.5, up=None) + "")
    o.append(soldier(p, w * 0.28, b, s) + peter(p, w * 0.36, b, s, flip=True))
    return "".join(o)

def asleep_chains(p, w, h, seed, angel_=False):
    """The same night Peter was sleeping between two soldiers, bound with two chains: the cell, Peter lying asleep on the
    straw, a soldier sitting asleep on either side, the chains from his wrists to theirs; angel_=True an angel of the Lord
    standing by him in a light that fills the cell (white light, gold rim, no face), the chains fallen off his hands, Peter
    rising."""
    bg, b = _prison(w, h, seed)
    o = [mk.defs(p, *ALL, *LIE), bg]
    if angel_:
        o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#FFF4C2" opacity="0.35"></rect>' + glow(w * 0.5, b - h * 0.3, w * 0.4, "#FFFFFF", 0.9, f"{p}l"))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(seated(w * 0.2, b, s * 0.8, "#A8281E", head=None, beard=None, bowed=True))
    o.append(seated(w * 0.8, b, s * 0.8, "#A8281E", head=None, beard=None, flip=True, bowed=True))
    if not angel_:
        o.append(lying(p, w * 0.5, b - 4, s * 0.8, cloth=ROBES["peter"]))
        o.append(f'<path d="M{f(w * 0.28)} {f(b - 40 * s)} C {f(w * 0.34)} {f(b - 10 * s)} {f(w * 0.4)} {f(b - 10 * s)} {f(w * 0.44)} {f(b - 30 * s)}" stroke="#8A8A90" stroke-width="{f(3 * s)}" stroke-dasharray="{f(5 * s)} {f(2 * s)}" fill="none"></path>'
                 f'<path d="M{f(w * 0.56)} {f(b - 30 * s)} C {f(w * 0.62)} {f(b - 10 * s)} {f(w * 0.68)} {f(b - 10 * s)} {f(w * 0.72)} {f(b - 40 * s)}" stroke="#8A8A90" stroke-width="{f(3 * s)}" stroke-dasharray="{f(5 * s)} {f(2 * s)}" fill="none"></path>')
    else:
        o.append(peter(p, w * 0.44, b, s, flip=True))
        o.append(angel(p, w * 0.6, b, s * 1.02, up=UP_CALL))
        for x in (0.36, 0.52):
            o.append(f'<path d="M{f(w * x)} {f(b - 4)} c {f(10 * s)} {f(-14 * s)} {f(24 * s)} {f(-14 * s)} {f(34 * s)} 0" stroke="#8A8A90" stroke-width="{f(3 * s)}" stroke-dasharray="{f(5 * s)} {f(2 * s)}" fill="none"></path>')
    return "".join(o)

def iron_gate(p, w, h, seed):
    """The iron gate that leadeth into the city, which opened to them of its own accord: the great gate of iron bars standing
    open at night, the angel of white light going before and Peter following, the street beyond in moonlight."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(30, w, h * 0.3, seed), houses(w, h, h * 0.7, seed, hmin=0.2, hmax=0.3, lit=True, stairs=False),
         pavement(w, h, h * 0.7, color="#4A4248", line="#3A3238")]
    gx = w * 0.16
    o.append(f'<rect x="-10" y="{f(h * 0.1)}" width="{f(gx + 10)}" height="{f(b)}" fill="#5A5054" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(7):
        o.append(f'<path d="M{f(gx + 6 * k)} {f(h * 0.2 + 3 * k)} L {f(gx + 6 * k)} {f(b - 4 * k)}" stroke="#2A2A30" stroke-width="5"></path>')
    o.append(f'<path d="M{f(gx)} {f(h * 0.3)} L {f(gx + 40)} {f(h * 0.33)} M{f(gx)} {f(h * 0.6)} L {f(gx + 40)} {f(h * 0.62)}" stroke="#2A2A30" stroke-width="5"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    o.append(glow(w * 0.62, b - 110 * s, 160 * s, "#FFFFFF", 0.8, f"{p}a") + angel(p, w * 0.62, b, s * 1.02, flip=True))
    o.append(peter(p, w * 0.42, b, s, flip=True))
    return "".join(o)

def rhoda_gate(p, w, h, seed, opened=False):
    """The house of Mary the mother of John Mark at night: the wall and the door of the gate; Peter outside knocking; inside
    the court, lamplight, Rhoda running in to tell them; opened=True the gate open, Peter within beckoning with his hand to
    hold their peace, the company amazed."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(30, w, h * 0.3, seed)]
    wx = w * 0.42
    o.append(f'<rect x="{f(wx)}" y="{f(h * 0.2)}" width="{f(w - wx + 10)}" height="{f(b)}" fill="#4A3A3A" stroke="{INK}" stroke-width="2"></rect>'
             + glow(w * 0.76, h * 0.5, h * 0.5, "#FFC14D", 0.5, f"{p}l") + A.lamp(w * 0.76, h * 0.34, max(0.6, h / 360)))
    o.append(f'<rect x="-10" y="{f(h * 0.3)}" width="{f(wx + 10)}" height="{f(b)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>')
    gx = wx - w * 0.1
    o.append(f'<rect x="{f(gx)}" y="{f(h * 0.42)}" width="{f(w * 0.1)}" height="{f(b - h * 0.42)}" fill="{"#FFC14D" if opened else "#5A3A22"}" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2228"></rect>')
    s = fit(b, max(h * 0.3, b - 200))
    if not opened:
        o.append(peter(p, gx - 40 * s, b, s, up=[(22, -158), (40, -170), (52, -180)]))
        o.append(woman_fig(p, w * 0.6, b, s * 0.84, "#C8A050", "#F3EFE6", up=UP_HIGH))
        for i, x in enumerate((0.76, 0.86, 0.95)):
            o.append(seated(w * x, b, s * 0.72, ["#6A4A3A", "#3A4A6A", "#5A3A4A"][i], head=None if i else "#3A3A4A", beard="#2A1A10", flip=True))
    else:
        o.append(peter(p, w * 0.5, b, s, flip=True, up=UP_HIGH))
        o.append(woman_fig(p, w * 0.62, b, s * 0.84, "#C8A050", "#F3EFE6", flip=True))
        for i, x in enumerate((0.72, 0.82, 0.92)):
            o.append(man_fig(p, w * x, b, s * 0.96, ["#6A4A3A", "#3A4A6A", "#5A3A4A"][i], hr="#2A1A10", bd="#2A1A10", up=UP_HIGH if i == 1 else None)
                     if i != 2 else woman_fig(p, w * x, b, s * 0.9, "#2A4A7A", "#3A6AA8"))
    return "".join(o)

def first_journey(w, h, legs=99, title="ACTS 13 – 14 · THE FIRST JOURNEY"):
    """The first journey, lit leg by leg (legs= how many): Antioch, Seleucia, Salamis, Paphos, Perga, Antioch of Pisidia,
    Iconium, Lystra, Derbe — and back by Lystra, Iconium, Antioch, Perga, Attalia to Antioch of Syria."""
    out = ["ANTIOCH", "SELEUCIA", (34.8, 35.6), "SALAMIS", (33.4, 35.1), "PAPHOS", (31.6, 35.8), "PERGA", "ANTIOCH OF PISIDIA", "ICONIUM", "LYSTRA", "DERBE"]
    back = ["DERBE", "LYSTRA", "ICONIUM", "ANTIOCH OF PISIDIA", "PERGA", "ATTALIA", (32.6, 36.0), (35.0, 35.9), "SELEUCIA", "ANTIOCH"]
    legs_out = [out[0:2], out[1:4], out[3:6], out[5:8], out[7:9], out[8:10], out[9:11], out[10:12]]
    rts = legs_out[:legs] + ([back] if legs > 8 else [])
    return geo.med_map(w, h, box=(29.6, 37.2, 34.2, 39.0), places=("ANTIOCH", "SELEUCIA", "SALAMIS", "PAPHOS", "PERGA", "ATTALIA", "ANTIOCH OF PISIDIA", "ICONIUM", "LYSTRA", "DERBE", "TARSUS"),
                       routes=rts, hi=tuple(q for r in rts for q in r if isinstance(q, str)), regions=("CYPRUS", "PAMPHYLIA", "PISIDIA", "LYCAONIA", "CILICIA", "SYRIA", "GALATIA"),
                       lit_routes=list(range(len(rts))), size=10, rsize=10, title=title)

def proconsul(p, w, h, seed, elymas_=True, mist=False):
    """The proconsul Sergius Paulus in his hall at Paphos (a white toga with a purple border), seated; Barnabas and Saul
    before him; Elymas standing against them (a dark robe, a band on his headcloth — no sorcery drawn); mist=True no Elymas,
    only a dark mist where he stood, and the proconsul risen, astonished."""
    bg, b = _hall(w, h, seed, "roman")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    st = b - 30 * s
    o.append(f'<rect x="{f(w * 0.7)}" y="{f(st)}" width="{f(w * 0.3)}" height="{f(b - st + 2)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    if mist:
        o.append(sergius(p, w * 0.84, st, s, up=UP_BLESS))
        r = random.Random(seed)
        o.append("".join(f'<ellipse cx="{f(w * 0.56 + r.uniform(-50, 50))}" cy="{f(b - r.uniform(20, 160) * s)}" rx="{f(r.uniform(30, 60) * s)}" ry="{f(r.uniform(16, 30) * s)}" fill="#1A1420" opacity="0.5"></ellipse>' for _ in range(10)))
    else:
        o.append(f'<rect x="{f(w * 0.8)}" y="{f(st - 60 * s)}" width="{f(70 * s)}" height="{f(60 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
        o.append(seated(w * 0.84, st, s * 0.84, "#F3EFE6", head=None, beard=None, flip=True))
        if elymas_: o.append(elymas(p, w * 0.58, b, s, up=UP_BLESS))
    o.append(barnabas(p, w * 0.14, b, s, flip=True) + paul(p, w * 0.26, b, s, flip=True, up=UP_BLESS if mist else None))
    return "".join(o)

def shake_dust(p, w, h, seed, who=("paul", "barnabas")):
    """They shook off the dust of their feet against them: Paul and Barnabas walking out of the town gate onto the open road,
    a puff of dust beaten from their sandals, the gate behind them on the right."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8A890", "#F3E8C8"), walls(w * 0.56, w + 10, h * 0.7, h * 0.4, seed, towers=2), ground(w, h, h * 0.7, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.28, b - 210))
    o.append(WHO[who[0]](p, w * 0.32, b, s) + WHO[who[1]](p, w * 0.18, b, s * 0.98))
    r = random.Random(seed)
    for _ in range(14):
        o.append(f'<circle cx="{f(w * 0.38 + r.uniform(0, w * 0.1))}" cy="{f(b - r.uniform(0, 30 * s))}" r="{f(r.uniform(3, 9) * s)}" fill="#D8C8A0" opacity="0.7"></circle>')
    return "".join(o)

def kings_of_israel(p, w, h, seed):
    """They asked for a king, and God gave unto them Saul the son of Kish: Samuel in midnight blue anointing Saul, a head taller
    (crimson, crowned), the people of Israel behind (1 Samuel's figures)."""
    from sa1.art import saul_fig, samuel_fig
    bg, b = _road(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 190))
    o.append(samuel_fig(p, w * 0.3, b, s, up=[(22, -158), (40, -186), (56, -206)]) + saul_fig(p, w * 0.44, b, s * 0.92, crown=True))
    o.append(crowd(p, w * 0.6, w * 0.96, b, b - 170 * s, 5, seed, flip=True))
    return "".join(o)
