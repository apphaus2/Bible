"""Drawings for Acts 27, the voyage and the shipwreck. Julius the centurion of the Augustan band (Matthew's and Mark's Roman
helmet with the red crest, dark stubble); the voyage on the map leg by leg (Sidon, the lee of Cyprus, Myra, Cnidus, the lee
of Crete, Fair Havens, Cauda, the sea of Adria, Melita); the ship of Alexandria — a great grain ship, its square mainsail
and small foresail, the swan's-neck stern and the steering oars; the harbour of Fair Havens and Paul's warning; the
tempestuous wind Euraquilo — the ship driven under a black sky, undergirded with cables, the freight and the tackling cast
out; the angel of God standing by Paul in the night (white light, a gold rim, no face); the sounding and the four anchors
from the stern; the boat cut away; the bread broken on the deck before the dawn; the wheat thrown into the sea; and the
bay with a beach — the foreship stuck fast where two seas met, the stern breaking up in the surf, and all coming safe to
the land on planks and pieces of the ship (no one is drawn drowning). Built on act.art14."""
from act.art14 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
from oba.minor import bolt, rain

def julius(p, x, y, s, flip=False, up=None): return centurion(p, x, y, s, flip=flip, up=up)
WHO.update({"julius": julius})

VOYAGE = [["CÆSAREA", (34.4, 33.0), "SIDON"], ["SIDON", (34.6, 35.9), (32.4, 36.2), "MYRA"], ["MYRA", (28.6, 36.3), "CNIDUS"], ["CNIDUS", (26.6, 35.9), "SALMONE"],
          ["SALMONE", (25.6, 34.9), "FAIR HAVENS"], ["FAIR HAVENS", (24.3, 34.95)], [(24.3, 34.95), "CAUDA", (22.0, 35.2), (19.0, 35.6), (16.4, 35.8), "MELITA"],
          ["MELITA", "SYRACUSE", "RHEGIUM", "PUTEOLI", "MARKET OF APPIUS", "THREE TAVERNS", "ROME"]]

def voyage(w, h, legs=7, lit=None, title="ACTS 27 · THE VOYAGE FOR ITALY", box=(12.0, 36.0, 32.6, 42.2)):
    rts = VOYAGE[:legs]
    names = [q for r in rts for q in r if isinstance(q, str)]
    return geo.med_map(w, h, box=box, places=tuple(dict.fromkeys(names)), routes=rts, hi=tuple(q for q in rts[-1] if isinstance(q, str)),
                       regions=("CRETE", "CYPRUS", "LYCIA", "SICILY", ("ADRIA", 18.6, 37.4), "ITALY", "ACHAIA"), lit_routes=lit if lit is not None else [len(rts) - 1],
                       size=10, rsize=10, title=title)

def grain_ship(p, x, y, s, sail="full", tilt=0, crew=(), broken=False, anchors=False, girded=False, mast=True, boat_=True):
    """A ship of Alexandria, (x, y) the waterline amidships (about 420 units long at s=1): a deep hull with a swan's-neck
    stern, twin steering oars, the tall mast with a great square mainsail (sail="full", "reefed" or "none") and a small
    foresail on a raking foremast; crew= x positions of figures on the deck (cloth colours, or "paul"); broken=True the
    stern broken away; anchors=True four cables from the stern; girded=True cables passed under the hull."""
    o = [f'<g transform="translate({f(x)} {f(y)}) rotate({f(tilt)}) scale({f(s)})">']
    if mast:
        o.append('<path d="M-10 -40 L -10 -300" stroke="#4A2A1A" stroke-width="8"></path><path d="M-120 -280 L 100 -280" stroke="#4A2A1A" stroke-width="5"></path>'
                 '<path d="M150 -40 L 200 -190" stroke="#4A2A1A" stroke-width="6"></path>')
        if sail == "full":
            o.append('<path d="M-118 -276 L 98 -276 C 110 -200 104 -130 96 -80 L -112 -80 C -122 -130 -126 -200 -118 -276 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="3"></path>'
                     '<path d="M-118 -230 L 100 -230 M-120 -180 L 104 -180 M-118 -130 L 100 -130" stroke="#C8B080" stroke-width="2"></path>'
                     '<path d="M172 -170 L 212 -190 L 220 -120 L 176 -110 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></path>')
        elif sail == "reefed":
            o.append('<path d="M-118 -276 L 98 -276 L 96 -250 L -116 -250 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></path>'
                     '<path d="M172 -170 L 212 -190 L 216 -150 L 176 -140 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for cx in crew:
        who, dx = (cx if isinstance(cx, tuple) else ("#6A5A4A", cx))
        if who == "paul": o.append(paul(p, dx, -44, 0.5))
        elif who == "soldier": o.append(soldier(p, dx, -44, 0.5))
        elif who == "julius": o.append(julius(p, dx, -44, 0.5))
        elif who == "angel": o.append(angel(p, dx, -44, 0.52))
        else: o.append(man_fig(p, dx, -44, 0.5, who, hr="#2A1A10", kind="Tunic"))
    hull = ('M-220 -60 L 200 -60 C 230 -60 250 -80 262 -110 L 270 -100 C 256 -50 236 -10 190 0 L -170 0 C -210 -10 -236 -40 -240 -70 '
            'C -250 -100 -262 -130 -250 -160 C -244 -170 -230 -168 -232 -156 C -240 -126 -232 -96 -220 -60 Z')
    if broken:
        o.append('<clipPath id="%sbk"><path d="M-80 -200 L 300 -200 L 300 40 L -40 40 L -70 -10 L -50 -40 L -90 -70 Z"></path></clipPath>' % p)
        o.append(f'<path d="{hull}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="3" clip-path="url(#{p}bk)"></path>')
        r = random.Random(int(x))
        for _ in range(7):
            px, py = -200 + r.uniform(0, 140), -20 + r.uniform(-30, 30)
            o.append(f'<rect x="{f(px)}" y="{f(py)}" width="{f(r.uniform(40, 90))}" height="10" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="1.6" transform="rotate({r.randint(-30, 30)} {f(px)} {f(py)})"></rect>')
    else:
        o.append(f'<path d="{hull}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="3"></path>'
                 '<path d="M-226 -46 L 216 -46 M-200 -24 L 220 -24" stroke="#3A2414" stroke-width="2.4"></path>'
                 '<path d="M-196 -50 L -230 30" stroke="#3A2414" stroke-width="7"></path><path d="M-232 22 L -226 46 L -214 42 Z" fill="#3A2414"></path>')
    if girded:
        o.append("".join(f'<path d="M{dx} -62 C {dx - 8} -20 {dx - 4} 0 {dx + 4} 6" stroke="#C8A878" stroke-width="5" fill="none"></path>' for dx in (-120, -20, 80, 160)))
    if anchors:
        o.append("".join(f'<path d="M-236 -60 L {-300 - 20 * k} {60 + 10 * k}" stroke="#C8A878" stroke-width="3"></path>' for k in range(4)))
    if boat_ and not broken:
        o.append('<path d="M-150 -70 L -60 -70 C -64 -56 -76 -50 -100 -50 C -126 -50 -142 -56 -150 -70 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append("</g>")
    return "".join(o)

def harbour(p, w, h, seed, warn=False, tone="day"):
    """A haven of Crete: the bay under the bare hills, the ship of Alexandria at anchor with her sail furled; warn=True on the
    quay Paul admonishing the centurion Julius, the master and the owner of the ship."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2" if tone == "day" else "#5A6A8A", "#F3E8C8"), hills(w, h, h * 0.42, seed, color="#A89A7A", amp=20, step=110),
         sea_(w, h, h * 0.5, seed), grain_ship(p, w * 0.68, h * 0.68, min(w * 0.42 / 500, h / 560), sail="reefed"),
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w * 0.5)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.34, b - 190))
    if warn:
        o.append(paul(p, w * 0.12, b, s, flip=True, up=UP_BLESS) + julius(p, w * 0.26, b, s) + man_fig(p, w * 0.36, b, s, "#1F5A6A", head="#E8E2D6", bd="#6A645E")
                 + man_fig(p, w * 0.45, b, s * 0.98, "#8A6A2A", hr="#2A1A10", bd="#2A1A10", kind="Tunic"))
    return "".join(o)

def tempest(p, w, h, seed, stage="driven"):
    """The tempestuous wind Euraquilo: a black sky, the sea in great waves, the ship driven before the wind; stage "driven"
    — the sail lowered, the ship heeling; "girded" — the crew passing cables under the hull; "freight" — sacks and the
    tackling thrown overboard; "dark" — neither sun nor stars for many days, the ship small in the dark sea."""
    o = [sky(w, h, "#05050E", "#2A2A3A"), rain(w, h, seed, n=90, color="#8A9AB0", op=0.5)]
    r = random.Random(seed)
    if stage != "dark":
        o.append(bolt(w * r.uniform(0.6, 0.9), 0, h * 0.4, seed))
    o.append(mk.defs(p, *ALL))
    o.append(sea_(w, h, h * 0.56, seed, color="#0F3A52", deep="#05101A", foam="#CFEFFF", rough=True))
    k = min(w * 0.62 / 500, h / 520) * (0.6 if stage == "dark" else 1.0)
    crew = [("julius", -60), ("#6A5A4A", 40), ("paul", 120)] if stage in ("driven", "dark") else [("#6A5A4A", -120), ("#4A5A6A", -40), ("#5A4A3A", 60)]
    o.append(grain_ship(p, w * 0.5, h * 0.7, k, sail="reefed" if stage != "freight" else "none", tilt=-8 if stage != "dark" else 4, crew=crew, girded=stage == "girded", mast=True))
    if stage == "freight":
        for i in range(5):
            x = w * (0.82 + 0.035 * i); y = h * (0.5 + 0.08 * (i % 3))
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(26 * k)}" height="{f(16 * k)}" rx="{f(6 * k)}" fill="#C8A878" stroke="{INK}" stroke-width="1.6" transform="rotate({r.randint(-30, 30)} {f(x)} {f(y)})"></rect>')
    o.append("".join(f'<path d="M{f(x - 60)} {f(h * 0.72 + dy)} C {f(x - 20)} {f(h * 0.6 + dy)} {f(x + 20)} {f(h * 0.6 + dy)} {f(x + 60)} {f(h * 0.72 + dy)}" stroke="#CFEFFF" stroke-width="4" fill="none"></path>'
                     for x, dy in ((w * 0.12, 30), (w * 0.86, 40), (w * 0.4, 70))))
    return "".join(o)

def angel_deck(p, w, h, seed):
    """There stood by me this night an angel of the God whose I am: the deck at night in the storm, Paul standing, and beside
    him an angel of white light with a gold rim, no face."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#05050E", "#1A1A3A"), rain(w, h, seed, n=60, color="#8A9AB0", op=0.4),
         f'<path d="M-10 {f(b)} L {f(w + 10)} {f(b - h * 0.04)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.8)} {f(b)} L {f(w * 0.8)} -10" stroke="#3A2414" stroke-width="10"></path>']
    s = fit(b, max(h * 0.34, b - 190))
    o.append(glow(w * 0.52, b - 110 * s, 180 * s, "#FFFFFF", 0.9, f"{p}a") + angel(p, w * 0.52, b, s * 1.04, flip=True, up=UP_BLESS))
    o.append(paul(p, w * 0.32, b, s))
    return "".join(o)

def soundings(p, w, h, seed, anchors=True, boat=False):
    """About midnight in the sea of Adria: the ship lying in the dark with a lantern, a sailor letting down the sounding-lead
    over the side; anchors=True four anchors let go from the stern; boat=True the ship's boat lowered into the sea, the
    soldiers at the side cutting the ropes and the boat falling off."""
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#14143A"), mk.stars(20, w, h * 0.3, seed), sea_(w, h, h * 0.58, seed, color="#0F2A4A", deep="#05101A")]
    k = min(w * 0.56 / 500, h / 600)
    o.append(grain_ship(p, w * 0.56, h * 0.74, k, sail="none", crew=[("#6A5A4A", 160), ("soldier", -120), ("soldier", -170)] if boat else [("#6A5A4A", 160), ("paul", 0)],
                        anchors=anchors, boat_=not boat))
    o.append(glow(w * 0.56, h * 0.46, h * 0.1, "#FFC14D", 0.6, f"{p}ln"))
    o.append(f'<path d="M{f(w * 0.56 + 190 * k)} {f(h * 0.74 - 50 * k)} L {f(w * 0.56 + 200 * k)} {f(h * 0.98)}" stroke="#C8A878" stroke-width="2" stroke-dasharray="6 4"></path>')
    if boat:
        o.append(f'<g transform="translate({f(w * 0.24)} {f(h * 0.82)}) rotate(14) scale({f(k * 1.4)})"><path d="M-60 0 L 60 0 C 54 18 36 24 0 24 C -36 24 -54 18 -60 0 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path></g>'
                 f'<path d="M{f(w * 0.56 - 170 * k)} {f(h * 0.74 - 60 * k)} L {f(w * 0.3)} {f(h * 0.78)}" stroke="#C8A878" stroke-width="2" stroke-dasharray="10 6"></path>')
    return "".join(o)

def bread_deck(p, w, h, seed, wheat=False):
    """While the day was coming on: the deck in the grey of the morning, Paul standing with a loaf broken in his hands, giving
    thanks, the sailors and soldiers and prisoners sitting about him; wheat=True the wheat being thrown into the sea."""
    from ecc.art import loaf
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A5A", "#C8A890"), sea_(w, h, h * 0.5, seed, color="#3A5A6A", deep="#1A2A3A"),
         f'<path d="M-10 {f(b)} L {f(w + 10)} {f(b - h * 0.04)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.08)} -10" stroke="#3A2414" stroke-width="10"></path>']
    s = fit(b, max(h * 0.34, b - 190))
    if wheat:
        o.append(man_fig(p, w * 0.7, b, s, "#6A5A4A", hr="#2A1A10", kind="Tunic", up=UP_HIGH) + man_fig(p, w * 0.82, b, s, "#4A5A6A", hr="#2A1A10", kind="Tunic", up=UP_HIGH))
        r = random.Random(seed)
        o.append("".join(f'<circle cx="{f(w * r.uniform(0.84, 1.0))}" cy="{f(h * r.uniform(0.2, 0.5))}" r="2.4" fill="#E8C060"></circle>' for _ in range(60)))
        o.append(paul(p, w * 0.3, b, s) + julius(p, w * 0.42, b, s))
    else:
        o.append(paul(p, w * 0.24, b, s, flip=True, up=UP_HIGH) + loaf(w * 0.24 + 46 * s, b - 196 * s, s * 0.5))
        for i, x in enumerate((0.4, 0.52, 0.64, 0.76, 0.88)):
            o.append(seated(w * x, b, s * 0.76, ["#6A5A4A", "#A8281E", "#4A5A6A", "#5A4A3A", "#A8281E"][i], head=None, beard="#2A1A10" if i % 2 == 0 else None, flip=True))
    return "".join(o)

def aground(p, w, h, seed, stage="bay"):
    """The bay with a beach at daybreak: stage "bay" — the ship making for the beach under her foresail; "aground" — the
    foreship stuck fast on the bank where two seas met, the stern breaking up in the surf; "safe" — the broken ship in the
    breakers, men coming through the surf on planks and pieces of the ship, and all standing safe on the beach."""
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFC890"), hills(w, h, h * 0.42, seed, color="#8A9A6A", amp=16, step=100),
         sea_(w, h, h * 0.5, seed, color="#1F6F9A", rough=stage != "bay"),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.36)} {f(h * 0.6)} {f(w * 0.44)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#D8C090" stroke="{INK}" stroke-width="2"></path>']
    k = min(w * 0.5 / 500, h / 640)
    if stage == "bay":
        o.append(grain_ship(p, w * 0.78, h * 0.66, k, sail="reefed", crew=[("paul", 0), ("julius", 80), ("#6A5A4A", -100)]))
    else:
        o.append(grain_ship(p, w * 0.7, h * 0.7, k * 1.1, sail="none", tilt=6, broken=True, crew=[("#6A5A4A", 120)] if stage == "aground" else []))
        o.append("".join(f'<path d="M{f(w * x)} {f(h * 0.74 + d)} q 20 -18 40 0 t 40 0" stroke="#FFFFFF" stroke-width="4" fill="none"></path>' for x, d in ((0.52, 0), (0.6, 20), (0.86, 10), (0.44, 34))))
    if stage == "safe":
        b = h * 0.94
        s = fit(b, max(h * 0.4, b - 170))
        for i, x in enumerate((0.48, 0.56)):
            o.append(f'<rect x="{f(w * x - 40 * k * 2)}" y="{f(h * 0.78 + 12 * i)}" width="{f(80 * k * 2)}" height="{f(10 * k * 2)}" fill="#7A5A3A" stroke="{INK}" stroke-width="1.6"></rect>'
                     + man_fig(p, w * x, h * 0.78 + 12 * i + 4, s * 0.5, "#6A5A4A", hr="#2A1A10", kind="Tunic", up=UP_HIGH))
        o.append(paul(p, w * 0.12, b, s) + julius(p, w * 0.22, b, s) + soldier(p, w * 0.3, b, s * 0.96) + man_fig(p, w * 0.38, b, s * 0.96, "#4A5A6A", hr="#2A1A10", kind="Tunic", up=UP_HIGH))
    return "".join(o)
