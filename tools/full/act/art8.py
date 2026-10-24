"""Drawings for Acts 14–15. Iconium divided; Lystra: the town gate and, before the city, the temple of Jupiter (a small
Greek temple of white columns); the cripple sitting, then leaping up; the priest of Jupiter bringing oxen with garlands to
the gates; Barnabas and Paul rending their garments among the multitude; Paul stoned (14:19) told in words only over the
empty gate with the stones lying before it; the disciples standing round him and Paul risen among them; the elders
appointed; the return voyage on the map. The council at Jerusalem: the apostles and elders seated in the upper room, James
the Lord's brother (grey beard, an off-white headcloth) presiding; the letter (Ezra's letter-scroll); the epistle read at
Antioch; Judas and Silas (a blue headcloth and robe); and the parting at Seleucia — Barnabas and Mark going down to the
ship for Cyprus, Paul and Silas setting out by road. Built on act.art7."""
from act.art7 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
import samuel1 as S1
from ezr.art import letter_scroll

def james_lord(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#B8B0A0", head="#F3EFE6", cord="#6A5A3A", bd="#A8A296", flip=flip, up=up)
def judas_bars(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#5A6A7A", head="#E8E2D6", bd="#5A4A3A", flip=flip, up=up)
WHO.update({"james_lord": james_lord, "judas_bars": judas_bars})

def jupiter_temple(x, base, wd):
    """The temple of Jupiter before the city: a small Greek temple, steps, six white columns and a pediment."""
    u = wd / 100
    o = [f'<rect x="{f(x - 50 * u)}" y="{f(base - 8 * u)}" width="{f(100 * u)}" height="{f(8 * u)}" fill="#D8D0C0" stroke="{INK}" stroke-width="1.8"></rect>',
         f'<rect x="{f(x - 46 * u)}" y="{f(base - 14 * u)}" width="{f(92 * u)}" height="{f(6 * u)}" fill="#E8E0D0" stroke="{INK}" stroke-width="1.6"></rect>']
    for k in range(6):
        cx = x - 40 * u + k * 16 * u
        o.append(f'<rect x="{f(cx - 3 * u)}" y="{f(base - 54 * u)}" width="{f(6 * u)}" height="{f(40 * u)}" fill="#F8F4EC" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="{f(x - 46 * u)}" y="{f(base - 60 * u)}" width="{f(92 * u)}" height="{f(6 * u)}" fill="#E8E0D0" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(x - 48 * u)} {f(base - 60 * u)} L {f(x)} {f(base - 78 * u)} L {f(x + 48 * u)} {f(base - 60 * u)} Z" fill="#E8E0D0" stroke="{INK}" stroke-width="1.8"></path>')
    return "".join(o)

def lystra(p, w, h, seed, stage="sit"):
    """Lystra: the town gate on the right, the temple of Jupiter before the city on the left. stage: "sit" — the cripple
    sitting on the ground, Paul speaking with his hand lifted; "leap" — the man leaping up, the multitude lifting their hands;
    "oxen" — the priest of Jupiter (white, a wreath) bringing two garlanded oxen to the gates; "rent" — Barnabas and Paul
    rushing among the people with their garments rent; "stoned" — the gate empty and the stones lying on the ground before it
    (told in words only); "rose" — the disciples standing round about Paul, and Paul risen, standing among them."""
    b = h * 0.94
    tone = ("#C8A890", "#F3E8C8") if stage != "stoned" else ("#3A2A3A", "#B8604A")
    o = [mk.defs(p, *ALL), sky(w, h, *tone), hills(w, h, h * 0.46, seed, color="#A89A7A" if stage != "stoned" else "#4A3A3A", amp=14, step=100),
         jupiter_temple(w * 0.18, h * 0.62, w * 0.28), walls(w * 0.6, w + 10, h * 0.66, h * 0.38, seed, towers=2),
         ground(w, h, h * 0.62, "#C8B07A" if stage != "stoned" else "#6A5040", dy=0)]
    s = fit(b, max(h * 0.3, b - 200))
    r = random.Random(seed)
    if stage == "sit":
        o.append(seated(w * 0.5, b, s * 0.82, "#7A7A60", head="#6A5A3A", beard="#3A2A1A", flip=True))
        o.append(paul(p, w * 0.34, b, s, flip=True, up=UP_BLESS) + barnabas(p, w * 0.24, b, s))
        o.append(crowd(p, w * 0.62, w * 0.94, b, b - 170 * s, 4, seed, flip=True))
    elif stage == "leap":
        o.append(glow(w * 0.5, b - 130 * s, 130 * s, "#FFF4C2", 0.6, f"{p}l") + man_fig(p, w * 0.5, b - 26 * s, s, "#7A7A60", head="#6A5A3A", bd="#3A2A1A", up=UP_HIGH))
        o.append(paul(p, w * 0.34, b, s, flip=True) + barnabas(p, w * 0.24, b, s))
        o.append(crowd(p, w * 0.62, w * 0.96, b, b - 170 * s, 5, seed, flip=True, up=UP_HIGH))
    elif stage == "oxen":
        wreath = '<path d="M-14 -200 C -8 -208 8 -208 14 -200" stroke="#4A8A3A" stroke-width="5" fill="none"></path>'
        o.append(toga_fig(p, w * 0.3, b, s, hr="#8A847A", border="#E8E2D6", extra=wreath, up=UP_BLESS, flip=True))
        for i, x in enumerate((0.48, 0.66)):
            k = s * 0.9
            o.append(S1.cow(w * x, b, k * 0.9, color=["#E8E2D6", "#C9A27A"][i], patch="#F3EFE6"))
            o.append("".join(f'<circle cx="{f(w * x + (40 + 9 * j) * k)}" cy="{f(b - (70 - 3 * j) * k)}" r="{f(5 * k)}" fill="{["#E8B830", "#C2456A", "#F3EFE6"][j % 3]}" stroke="{INK}" stroke-width="1"></circle>' for j in range(5)))
        o.append(crowd(p, w * 0.78, w * 0.98, b, b - 170 * s, 2, seed, flip=True, up=UP_HIGH))
    elif stage == "rent":
        o.append(paul(p, w * 0.42, b, s, up=UP_HIGH) + barnabas(p, w * 0.3, b, s, flip=True, up=UP_HIGH))
        o.append(f'<path d="M{f(w * 0.42 - 4 * s)} {f(b - 150 * s)} L {f(w * 0.42 + 6 * s)} {f(b - 110 * s)} L {f(w * 0.42 - 2 * s)} {f(b - 80 * s)}" stroke="{INK}" stroke-width="2.4" fill="none"></path>'
                 f'<path d="M{f(w * 0.3 + 4 * s)} {f(b - 150 * s)} L {f(w * 0.3 - 6 * s)} {f(b - 110 * s)} L {f(w * 0.3 + 2 * s)} {f(b - 80 * s)}" stroke="{INK}" stroke-width="2.4" fill="none"></path>')
        o.append(crowd(p, w * 0.54, w * 0.96, b, b - 170 * s, 5, seed, flip=True))
        o.append(S1.cow(w * 0.12, b, s * 0.8, color="#E8E2D6", patch="#F3EFE6"))
    elif stage == "stoned":
        for _ in range(26):
            x = r.uniform(w * 0.3, w * 0.98); y = r.uniform(h * 0.7, h * 0.98); k = r.uniform(0.6, 1.4) * max(0.6, h / 300)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(10 * k)} {f(-6 * k)} l {f(12 * k)} {f(4 * k)} l {f(-4 * k)} {f(6 * k)} Z" fill="#9A8A7A" stroke="{INK}" stroke-width="1.2"></path>')
    elif stage == "rose":
        o.append(glow(w * 0.42, b - 110 * s, 120 * s, "#FFF4C2", 0.5, f"{p}r") + paul(p, w * 0.42, b, s))
        for i, x in enumerate((0.22, 0.3, 0.54, 0.62, 0.7)):
            o.append(man_fig(p, w * x, b, s * 0.96, ["#3A6A3A", "#6A4A3A", "#3A4A6A", "#7A7A60", "#5A3A4A"][i], head=["#3A6A3A", None, "#3A4A6A", "#6A5A3A", None][i],
                             hr="#2A1A10", bd=["#4A2A1A", "#2A1A10", None, "#3A2A1A", None][i], flip=x < 0.42))
    return "".join(o)

def iconium(p, w, h, seed, divided=False):
    """Iconium: the synagogue court in the city; Paul and Barnabas speaking, the multitude of Jews and Greeks; divided=True
    the people split into two parties, one holding with the apostles, one turning away with the rulers."""
    bg, b = _gate(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(paul(p, w * 0.14, b, s, flip=True, up=UP_BLESS) + barnabas(p, w * 0.24, b, s, flip=True))
    if divided:
        o.append(crowd(p, w * 0.34, w * 0.52, b, b - 170 * s, 3, seed, flip=True))
        o.append(crowd(p, w * 0.66, w * 0.94, b, b - 170 * s, 4, seed + 1, flip=False, up=UP_HIGH))
        o.append(man_fig(p, w * 0.96, b, s, "#E8E2D6", head="#F3EFE6", cord="#E8B830", bd="#9A948A", up=UP_BLESS))
    else:
        o.append(crowd(p, w * 0.34, w * 0.96, b, b - 170 * s, 8, seed, flip=True))
    return "".join(o)

def council_jerusalem(p, w, h, seed, speaker=None):
    """The apostles and the elders gathered together: the upper room, James the Lord's brother presiding in the midst, the
    apostles and elders seated along the walls, Paul and Barnabas among them; speaker= "peter", "james_lord", "paul" — that
    one standing up to speak."""
    bg, b = _upper(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    seats = [(0.08, "#E8E2D6", "#F3EFE6", "#9A948A"), (0.18, "#3A4A6A", "#3A4A6A", "#2A1A10"), (0.28, ROBES["peter"], None, "#4A4440"), (0.38, ROBES["john"], None, None),
             (0.62, "#3A6A3A", "#3A6A3A", "#4A2A1A"), (0.72, ROBES["paul"], "#5A4A3A", "#3A2A1A"), (0.82, "#6A5A3A", "#E8E2D6", "#6A645E"), (0.92, "#4A3A5A", "#4A3A5A", "#2A1A10")]
    skip = {"peter": 2, "paul": 5}.get(speaker)
    for i, (x, c, hd, bd) in enumerate(seats):
        if i == skip: continue
        o.append(seated(w * x, b, s * 0.76, c, head=hd, beard=bd, flip=x > 0.5))
    if speaker == "james_lord":
        o.append(james_lord(p, w * 0.5, b, s, up=UP_BLESS))
    else:
        o.append(f'<rect x="{f(w * 0.44)}" y="{f(b - 60 * s)}" width="{f(w * 0.12)}" height="{f(60 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
        o.append(seated(w * 0.5, b - 34 * s, s * 0.76, "#B8B0A0", head="#F3EFE6", beard="#A8A296", flip=True))
        if speaker == "peter": o.append(peter(p, w * 0.28, b, s, flip=True, up=UP_BLESS))
        if speaker == "paul": o.append(paul(p, w * 0.72, b, s, up=UP_BLESS))
    return "".join(o)

def letter(p, w, h, seed):
    """The letter of the apostles and the elders: an unrolled scroll, written and sealed (Ezra's letter-scroll)."""
    return letter_scroll(w, h, seed, seal="#B5121B", text_lines=9)

def parting(p, w, h, seed):
    """They parted asunder one from the other: the harbour of Seleucia, Barnabas and Mark going down to the ship that sails
    for Cyprus; Paul and Silas on the road going the other way, inland."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sea_(w, h, h * 0.5, seed), ship(w * 0.3, h * 0.6, max(0.4, h / 560)),
         f'<path d="M{f(w * 0.46)} {f(h * 0.5)} C {f(w * 0.6)} {f(h * 0.56)} {f(w * 0.7)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.48)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#C8B07A" stroke="{INK}" stroke-width="2"></path>',
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w * 0.5)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.3, b - 200))
    o.append(barnabas(p, w * 0.32, b, s, flip=False) + mark_fig(p, w * 0.22, b, s * 0.94))
    o.append(paul(p, w * 0.7, b, s, flip=True) + silas(p, w * 0.8, b, s, flip=True))
    return "".join(o)

SECOND = [["ANTIOCH", "TARSUS", "DERBE"], ["DERBE", "LYSTRA", "ICONIUM", (31.4, 39.2)], [(31.4, 39.2), (29.0, 40.0), "TROAS"], ["TROAS", "SAMOTHRACE", "NEAPOLIS", "PHILIPPI"],
          ["PHILIPPI", "AMPHIPOLIS", "APOLLONIA", "THESSALONICA"], ["THESSALONICA", "BERŒA"], ["BERŒA", (23.2, 38.6), "ATHENS"], ["ATHENS", "CORINTH"],
          ["CORINTH", "CENCHREÆ", (25.4, 37.6), "EPHESUS"], ["EPHESUS", (30.0, 35.8), (33.8, 33.6), "CÆSAREA", "JERUSALEM", (35.8, 34.6), "ANTIOCH"]]

def second_journey(w, h, legs=99, title="ACTS 15:40 – 18:22 · THE SECOND JOURNEY", box=(21.0, 37.0, 31.4, 42.0), lit=None):
    """The second journey, leg by leg (legs= how many are drawn; the last drawn is lit red unless lit= lists others):
    Antioch through Cilicia to Derbe and Lystra, Phrygia and Galatia, Troas, Samothrace, Neapolis, Philippi, Amphipolis,
    Apollonia, Thessalonica, Berœa, Athens, Corinth, Cenchreæ, Ephesus, Cæsarea, Jerusalem, Antioch."""
    rts = SECOND[:legs]
    names = [q for r in rts for q in r if isinstance(q, str)]
    return geo.med_map(w, h, box=box, places=tuple(dict.fromkeys(names + ["ANTIOCH", "JERUSALEM"])), routes=rts, hi=tuple(q for q in rts[-1] if isinstance(q, str)),
                       regions=("SYRIA", "CILICIA", "GALATIA", "PHRYGIA", "ASIA", "MYSIA", "MACEDONIA", "ACHAIA"), lit_routes=lit if lit is not None else [len(rts) - 1],
                       size=10, rsize=10, title=title)
