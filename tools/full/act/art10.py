"""Drawings for Acts 17:16–18:28. Athens: the city full of idols — the Acropolis with its temple above the marketplace, the
statues of the gods on their pedestals (objects of stone and gold, as the verse names them); the marketplace and the Stoic
and Epicurean philosophers (white-bearded men in pale himations); the Areopagus, its rock and stone benches, Paul standing in
the midst; the altar inscribed TO AN UNKNOWN GOD. Corinth: Aquila (a sand headcloth) and Priscilla (a sea-blue veil) at
their tent-making, the goat-hair cloth on the frame; the house of Titus Justus hard by the synagogue; the vision by night
(the Lord not drawn: the light at the window); Gallio (a proconsul's toga) on the judgment-seat; what was done to Sosthenes
(18:17) told in words only over the empty judgment-seat; the harbour of Cenchreæ; the voyage by Ephesus to Cæsarea on the
map; Apollos of Alexandria in the synagogue at Ephesus. Built on act.art9."""
from act.art9 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
from act.art8 import jupiter_temple

def philosopher(p, x, y, s, i=0, flip=False, up=None):
    """A philosopher of Athens: a pale himation over one shoulder, bareheaded, a white or grey beard."""
    c = ["#E8E2D6", "#C8C0B0", "#D8D0E8", "#E0D8C0"][i % 4]
    bd = ["#E8E2D6", "#9A948A", "#C8C2B6", "#6A645E"][i % 4]
    drape = f'<path d="M-24 -160 C -6 -150 10 -110 18 -40 L 26 -42 C 20 -110 4 -156 -10 -166 Z" fill="{["#8A7A6A", "#5A6A7A", "#7A6A8A", "#6A7A5A"][i % 4]}" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#E3B08A", cloth=c, kind="Robe", sw=3, flip=flip, up=up, extra=drape + hair(bd) + beard(bd))
def aquila(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#8A6A3A", head="#C8B080", cord="#6A4A2A", bd="#3A2214", flip=flip, up=up)
def priscilla(p, x, y, s, flip=False, up=None): return woman_fig(p, x, y, s * 0.94, "#5A6A8A", "#3A6A8A", flip=flip, up=up)
def apollos(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#E8D8B0", hr="#1A1210", bd="#1A1210", body="#A8704E", flip=flip, up=up)
def gallio(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#4A3A2A", border="#6A1A5A", flip=flip, up=up)
WHO.update({"aquila": aquila, "priscilla": priscilla, "apollos": apollos, "gallio": gallio,
            "philosopher": lambda p, x, y, s, flip=False, up=None: philosopher(p, x, y, s, 0, flip, up)})

def statue(x, base, s, kind=0, color="#E8E0D0"):
    """An idol on its pedestal: a standing figure of stone (or gilded) on a block — an object, no face drawn."""
    k = s
    o = [f'<rect x="{f(x - 20 * k)}" y="{f(base - 40 * k)}" width="{f(40 * k)}" height="{f(40 * k)}" fill="#C8C0B0" stroke="{INK}" stroke-width="1.6"></rect>']
    body = {0: "M-12 0 L -14 -70 C -16 -90 -6 -96 0 -96 C 6 -96 16 -90 14 -70 L 12 0 Z", 1: "M-14 0 L -10 -60 L -22 -80 L -8 -84 L -4 -96 L 4 -96 L 8 -84 L 22 -80 L 10 -60 L 14 0 Z",
            2: "M-10 0 L -12 -66 L -24 -96 L -14 -98 L 0 -76 L 14 -98 L 24 -96 L 12 -66 L 10 0 Z"}[kind % 3]
    o.append(f'<g transform="translate({f(x)} {f(base - 40 * k)}) scale({f(k)})"><path d="{body}" fill="{color}" stroke="{INK}" stroke-width="2"></path>'
             f'<circle cx="0" cy="-108" r="12" fill="{color}" stroke="{INK}" stroke-width="2"></circle></g>')
    return "".join(o)

def athens(p, w, h, seed, paul_=True, idols=True):
    """Athens full of idols: the Acropolis on its rock with the great temple above, the marketplace below lined with statues
    of the gods on their pedestals; Paul standing among them, looking."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<path d="M{f(w * 0.38)} {f(h * 0.5)} L {f(w * 0.46)} {f(h * 0.28)} L {f(w * 0.9)} {f(h * 0.26)} L {f(w * 0.98)} {f(h * 0.5)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>',
         jupiter_temple(w * 0.68, h * 0.27, w * 0.36), hills(w, h, h * 0.5, seed, color="#A89A7A", amp=8, step=90), pavement(w, h, h * 0.56, color="#D8D0C0")]
    k = max(0.5, h / 340)
    if idols:
        for i, x in enumerate((0.06, 0.2, 0.52, 0.66, 0.8, 0.94)):
            o.append(statue(w * x, b - 6, k * (0.9 + 0.1 * (i % 2)), kind=i, color="#E8B830" if i == 3 else ("#C8C8D0" if i == 1 else "#E8E0D0")))
    s = fit(b, max(h * 0.3, b - 200))
    if paul_: o.append(paul(p, w * 0.36, b, s, flip=True))
    return "".join(o)

def stoa(p, w, h, seed, mock=False):
    """The marketplace of Athens and the Stoa: the long colonnade, the philosophers of the Epicureans and the Stoics standing
    about Paul disputing; mock=True some turning away laughing with their hands thrown up."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(paul(p, w * 0.42, b, s, up=UP_BLESS))
    for i, x in enumerate((0.1, 0.22, 0.6, 0.74, 0.88)):
        o.append(philosopher(p, w * x, b, s * (1 - 0.02 * (i % 2)), i, flip=x > 0.5, up=(UP_HIGH if mock and i in (0, 3) else (UP_BLESS if i == 2 else None))))
    return "".join(o)

def areopagus(p, w, h, seed, speaking=True, altar_=False):
    """The Areopagus: the bare rock of Mars' hill below the Acropolis, the stone benches where the council sits; Paul standing
    in the midst, the Athenians seated about him in their himations; altar_=True an altar of stone in the foreground with
    its inscription TO AN UNKNOWN GOD."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"),
         f'<path d="M{f(w * 0.5)} {f(h * 0.46)} L {f(w * 0.58)} {f(h * 0.2)} L {f(w * 0.96)} {f(h * 0.18)} L {f(w + 10)} {f(h * 0.46)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>',
         jupiter_temple(w * 0.78, h * 0.19, w * 0.28),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.6)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#A8987A" stroke="{INK}" stroke-width="2.4"></path>']
    s = fit(b, max(h * 0.3, b - 200))
    for i, x in enumerate((0.06, 0.18, 0.66, 0.78, 0.9)):
        o.append(f'<rect x="{f(w * x - 40 * s)}" y="{f(b - 30 * s)}" width="{f(80 * s)}" height="{f(30 * s)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>')
        o.append(seated(w * x, b - 30 * s, s * 0.74, ["#E8E2D6", "#C8C0B0", "#D8D0E8", "#E0D8C0", "#E8E2D6"][i], head=None, beard=["#E8E2D6", "#9A948A", "#C8C2B6", "#6A645E", "#B8B2A6"][i], flip=x > 0.5))
    o.append(paul(p, w * 0.42, b, s, up=UP_HIGH if speaking else None))
    if altar_:
        k = s
        ax = w * 0.26
        o.append(f'<rect x="{f(ax - 60 * k)}" y="{f(b - 80 * k)}" width="{f(120 * k)}" height="{f(80 * k)}" fill="#D8D0C0" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<rect x="{f(ax - 70 * k)}" y="{f(b - 92 * k)}" width="{f(140 * k)}" height="{f(14 * k)}" fill="#C8C0B0" stroke="{INK}" stroke-width="2"></rect>'
                 + label(ax, b - 50 * k, "TO AN UNKNOWN GOD", "#3A2A1A", max(7, 9 * k), weight=700, ls=0.04)
                 + f'<path d="M{f(ax - 50 * k)} {f(b - 36 * k)} L {f(ax + 50 * k)} {f(b - 36 * k)}" stroke="#8A7A6A" stroke-width="1.4"></path>')
    return "".join(o)

def tentmakers(p, w, h, seed):
    """Aquila and Priscilla, tentmakers: their workshop in Corinth, a length of dark goat-hair cloth on the frame, a tent
    half-sewn, the awls and thread; Paul at work with them."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    k = max(0.5, h / 340)
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.36)} {f(b - 150 * k)} L {f(w * 0.7)} {f(b - 160 * k)} L {f(w * 0.76)} {f(b)}" fill="none" stroke="#5A3A22" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(w * 0.37)} {f(b - 146 * k)} L {f(w * 0.69)} {f(b - 156 * k)} L {f(w * 0.68)} {f(b - 50 * k)} L {f(w * 0.39)} {f(b - 46 * k)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(w * 0.38)} {f(b - (140 - 18 * j) * k)} L {f(w * 0.68)} {f(b - (150 - 18 * j) * k)}" stroke="#5A4A3A" stroke-width="1.4"></path>' for j in range(5)))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(seated(w * 0.18, b, s * 0.8, "#8A6A3A", head="#C8B080", beard="#3A2214") + priscilla(p, w * 0.86, b, s, flip=True, up=UP_TOUCH))
    o.append(seated(w * 0.52, b, s * 0.8, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A", flip=True))
    return "".join(o)

def judgment_bema(p, w, h, seed, gallio_=True, accusers=True, paul_=True):
    """Gallio on the judgment-seat at Corinth: the raised stone bema in the forum, the proconsul in his toga on the curule
    chair, the Jews accusing Paul below; gallio_=False the bema empty (what was done to Sosthenes told in words)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.56, seed, hmin=0.2, hmax=0.3, stairs=False), pavement(w, h, h * 0.56, color="#D8D0C0")]
    bx = w * 0.7
    st = b - h * 0.2
    o.append(f'<rect x="{f(bx - w * 0.18)}" y="{f(st)}" width="{f(w * 0.36)}" height="{f(b - st + 4)}" fill="#E8E0D0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(bx - w * 0.2)}" y="{f(st - 10)}" width="{f(w * 0.4)}" height="12" fill="#D8D0C0" stroke="{INK}" stroke-width="2"></rect>')
    k = max(0.5, (st - h * 0.1) / 260)
    o.append(f'<path d="M{f(bx - 30 * k)} {f(st - 10)} L {f(bx - 20 * k)} {f(st - 60 * k)} L {f(bx + 20 * k)} {f(st - 60 * k)} L {f(bx + 30 * k)} {f(st - 10)} M{f(bx - 30 * k)} {f(st - 60 * k)} L {f(bx + 30 * k)} {f(st - 10)} M{f(bx + 30 * k)} {f(st - 60 * k)} L {f(bx - 30 * k)} {f(st - 10)}" stroke="#8A6A2A" stroke-width="{f(4 * k)}" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    if gallio_:
        s2 = fit(st - 10, max(h * 0.06, st - 10 - 170 * s / 1.0))
        o.append(gallio(p, bx, st - 10, min(s2, s * 0.9), flip=True, up=UP_BLESS))
    if paul_: o.append(paul(p, w * 0.42, b, s))
    if accusers:
        for i, x in enumerate((0.1, 0.2, 0.3)):
            o.append(man_fig(p, w * x, b, s * (1 - 0.02 * i), ["#E8E2D6", "#3A4A6A", "#6A5A3A"][i], head=["#F3EFE6", "#3A4A6A", "#E8E2D6"][i], cord="#E8B830",
                             bd=["#9A948A", "#2A1A10", "#4A3A2A"][i], flip=True, up=UP_BLESS if i == 1 else None))
    return "".join(o)

def cenchreae(p, w, h, seed):
    """Cenchreæ, the port of Corinth: the quay and the ship for Syria, Paul with his head shorn for his vow going aboard
    with Priscilla and Aquila."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sea_(w, h, h * 0.5, seed), ship(w * 0.74, h * 0.62, max(0.45, h / 520)),
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w * 0.6)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.3, b - 200))
    o.append(aquila(p, w * 0.14, b, s) + priscilla(p, w * 0.25, b, s)
             + man_fig(p, w * 0.4, b, s, ROBES["paul"], hr="#3A2A1A", bd="#3A2A1A").replace(hair("#3A2A1A"), '<path d="M-13 -190 C -12 -200 12 -200 13 -190 Z" fill="#6A4A3A" opacity="0.5"></path>'))
    return "".join(o)

THIRD = [["ANTIOCH", "TARSUS", (33.0, 37.8), (32.4, 39.0)], [(32.4, 39.0), (30.2, 38.7), "EPHESUS"], ["EPHESUS", (26.6, 39.5), "TROAS", (24.8, 40.6), "NEAPOLIS", "PHILIPPI"],
         ["PHILIPPI", "THESSALONICA", "BERŒA", (22.4, 39.0), "CORINTH"], ["CORINTH", "ATHENS", (24.2, 39.0), "PHILIPPI"], ["PHILIPPI", "NEAPOLIS", "TROAS"],
         ["TROAS", "ASSOS", "MITYLENE", "CHIOS", "SAMOS", "TROGYLLIUM", "MILETUS"], ["MILETUS", "COS", "RHODES", "PATARA"], ["PATARA", (31.6, 34.6), "TYRE"],
         ["TYRE", "PTOLEMAIS", "CÆSAREA", "JERUSALEM"]]

def third_journey(w, h, legs=99, lit=None, title="ACTS 18:23 – 21:17 · THE THIRD JOURNEY", box=(21.0, 37.0, 31.4, 42.0)):
    """The third journey, leg by leg: through Galatia and Phrygia to Ephesus; Macedonia and Greece and back by Philippi to
    Troas; Assos, Mitylene, Chios, Samos, Trogyllium, Miletus; Cos, Rhodes, Patara; Tyre, Ptolemais, Cæsarea, Jerusalem."""
    rts = THIRD[:legs]
    names = [q for r in rts for q in r if isinstance(q, str)]
    return geo.med_map(w, h, box=box, places=tuple(dict.fromkeys(names)), routes=rts, hi=tuple(q for q in rts[-1] if isinstance(q, str)),
                       regions=("GALATIA", "PHRYGIA", "ASIA", "MACEDONIA", "ACHAIA", "SYRIA", "LYCIA"), lit_routes=lit if lit is not None else [len(rts) - 1],
                       size=10, rsize=10, title=title)

def apollos_synagogue(p, w, h, seed, taught=False):
    """Apollos of Alexandria, an eloquent man, mighty in the scriptures, speaking boldly in the synagogue at Ephesus; taught=True
    Priscilla and Aquila in their house, expounding to him the way of God more accurately."""
    if taught:
        bg, b = _house(w, h, seed)
        o = [mk.defs(p, *ALL), bg]
        s = fit(b, max(h * 0.3, b - 200))
        o.append(seated(w * 0.14, b, s * 0.8, "#E8D8B0", head=None, beard="#1A1210") + aquila(p, w * 0.36, b, s, flip=True, up=UP_BLESS) + priscilla(p, w * 0.47, b, s, flip=True))
        return "".join(o)
    bg, b = _synagogue(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(apollos(p, w * 0.3, b, s, flip=True, up=UP_HIGH))
    for i, x in enumerate((0.5, 0.62, 0.74)):
        o.append(seated(w * x, b, s * 0.78, ["#6A5A3A", "#3A4A6A", "#5A2A4A"][i], head=["#E8E2D6", "#3A4A6A", None][i], beard="#2A1A10", flip=True))
    o.append(aquila(p, w * 0.86, b, s, flip=True) + priscilla(p, w * 0.95, b, s, flip=True))
    return "".join(o)
