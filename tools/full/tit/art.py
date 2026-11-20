"""Drawings for the Titus volume. Titus starts from all of 2 Timothy's drawings (`from ti2.art import *`, which carries 1
Timothy's, Galatians', Acts' and the Corinthian letters' drawings and the epistle kit), and adds its own: Crete — the island
on Acts' map with the letter's road to it, the window on its sea and mountains, the island at dawn — Titus receiving the
letter, the elders in every city, the household plates (aged men, aged women, young women, younger men, servants), Titus
an ensample to the younger men, the road to Nicopolis for the winter, Zenas the lawyer and Apollos setting out.

Titus at a distance: ti1.art.titus_fig_ — a Greek, bareheaded, short black hair, clean-shaven, a sand tunic and a blue
mantle (2 Corinthians' and Galatians' Titus). God is never drawn (light)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from ti2.art import *
from ti1.art import _defs, _sheet, _person_mark
from co1.art import apollos_r
from act.art15 import grain_ship

# Nicopolis (3:12) and two cities of Crete are not on Acts' map: named here for this letter's maps (lon, lat)
for _nm, _ll in (("NICOPOLIS", (20.73, 39.0)), ("GORTYNA", (24.95, 35.06)), ("CNOSSUS", (25.16, 35.3))):
    geo.PLACES.setdefault(_nm, _ll)
MAP_LABELS = {"NICOPOLIS": (-8, 4, "end"), "GORTYNA": (0, 16, "middle"), "CNOSSUS": (0, -10, "middle")}
for _nm, _at in MAP_LABELS.items(): geo.LABEL_AT.setdefault(_nm, _at)

def crete_road(w, h):
    """For this cause left I thee in Crete: the letter's road from Macedonia down through Achaia and across the sea to Crete,
    on Acts' map — the island with Fair Havens and Phœnix (Acts 27) and its old cities Cnossus and Gortyna; Nicopolis,
    where Paul has determined to winter (3:12), marked on the coast of Epirus."""
    rt = ["THESSALONICA", (22.6, 39.6), (23.2, 38.6), "CORINTH", (23.4, 37.2), (24.4, 36.2), "CNOSSUS"]
    return letter_road(w, h, rt, title="TITUS 1:5 · LEFT IN CRETE", box=(19.6, 28.6, 34.4, 41.2),
                       places=("THESSALONICA", "CORINTH", "ATHENS", "CNOSSUS", "GORTYNA", "NICOPOLIS", "EPHESUS"),
                       hi=("CNOSSUS", "GORTYNA"), regions=("MACEDONIA", "ACHAIA", "ASIA", ("CRETE", 23.4, 35.0)))

def crete_window(x, y, ww, hh, night, seed):
    """A window on Crete: the sea below, the bare ridge of the mountains behind, a white town on the shore."""
    sky_ = ("#0B0B2A", "#2A2050") if night else ("#8FD0E2", "#F3E8C8")
    uid = f"cw{seed}"
    o = [f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}"></rect></clipPath>'
         f'<linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky_[0]}"></stop><stop offset="1" stop-color="{sky_[1]}"></stop></linearGradient></defs>',
         f'<g clip-path="url(#{uid})"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="url(#{uid}g)"></rect>']
    o.append(f'<path d="M{f(x - 4)} {f(y + hh * 0.5)} L {f(x + ww * 0.3)} {f(y + hh * 0.22)} L {f(x + ww * 0.5)} {f(y + hh * 0.36)} L {f(x + ww * 0.72)} {f(y + hh * 0.18)} L {f(x + ww + 4)} {f(y + hh * 0.44)} '
             f'L {f(x + ww + 4)} {f(y + hh * 0.62)} L {f(x - 4)} {f(y + hh * 0.62)} Z" fill="{"#3A3450" if night else "#A89A80"}" stroke="{INK}" stroke-width="1.4"></path>'
             f'<rect x="{f(x - 4)}" y="{f(y + hh * 0.62)}" width="{f(ww + 8)}" height="{f(hh)}" fill="{"#1A2A4A" if night else "#3A8AB0"}"></rect>')
    for i in range(4):
        bx = x + ww * (0.1 + i * 0.12)
        o.append(f'<rect x="{f(bx)}" y="{f(y + hh * 0.54)}" width="{f(ww * 0.1)}" height="{f(hh * 0.08)}" fill="{"#5A5070" if night else "#F3EFE6"}" stroke="{INK}" stroke-width="1"></rect>')
    o.append('</g>' + f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(x + ww / 2)} {f(y)} L {f(x + ww / 2)} {f(y + hh)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<rect x="{f(x - 8)}" y="{f(y + hh)}" width="{f(ww + 16)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def titus_receives(p, w, h, seed):
    """To Titus, my true child after a common faith: Titus's room in a city of Crete by day, the window on the sea and the
    mountains; the brother come with the letter standing in the open doorway with the sealed roll, Titus reaching to take it."""
    return study(p, w, h, seed, stage="give", scribe=False, writer=titus_fig_, bearer=messenger, window=crete_window, night=False, fig_h=min(h * 0.72, w * 0.34))

def titus_reads(p, w, h, seed, night=True, x=0.58, tx=0.3):
    """Titus reading the letter by his lamp in Crete (ti1.art.timothy_reads' room, the window on the Cretan sea)."""
    b = h * 0.95
    k = fig_k(w, h, 0.42)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E" if night else "#D8C098", floor="#3A2A20" if night else "#8A6A4A")]
    if night: o.append(lamp_glow(w * 0.42, b - 70 * k, max(w, h) * 0.55, f"{p}tr", op=0.5))
    o.append(crete_window(w * 0.06, b - 205 * k, min(w * 0.2, 120 * k), min(h * 0.38, 92 * k), night, seed))
    tx = w * tx
    o.append(low_table(tx, b, 60 * k, k) + clay_lamp(tx + 18 * k, b - 31 * k, k * 0.55) + sealed_scroll(tx + 46 * k, b - 32 * k, 0.32 * k, rot=-8))
    o.append(titus_fig_(p, w * x, b, k, up=READ_UP, extra=_sheet(-74, -132, 46, 34, rot=-8), pose="sit"))
    return "".join(o)

CRETE = [(23.52, 35.29), (23.6, 35.6), (23.75, 35.52), (23.85, 35.53), (24.03, 35.51), (24.15, 35.6), (24.28, 35.56), (24.25, 35.46), (24.47, 35.38),
         (24.7, 35.42), (25.0, 35.41), (25.13, 35.34), (25.4, 35.33), (25.62, 35.3), (25.72, 35.19), (25.8, 35.3), (26.0, 35.25), (26.3, 35.3),
         (26.3, 35.1), (26.18, 34.98), (26.0, 34.98), (25.74, 35.0), (25.5, 35.0), (25.2, 34.95), (24.9, 34.93), (24.75, 34.92), (24.4, 35.07),
         (24.2, 35.17), (23.9, 35.23), (23.7, 35.22)]

def island(w, h, cx, cy, sc, fill="#1C2C34", line=CY):
    """Crete in outline (a finer coast than Acts' map's), centred at (cx, cy), sc px per degree."""
    pts = CRETE
    mx = sum(p_[0] for p_ in pts) / len(pts); my = sum(p_[1] for p_ in pts) / len(pts)
    k = math.cos(math.radians(35.2))
    P = lambda lon, lat: (cx + (lon - mx) * k * sc, cy - (lat - my) * sc)
    return P, f'<path d="M' + " L ".join(f"{f(a)} {f(b)}" for a, b in (P(*q) for q in pts)) + f' Z" fill="{fill}" stroke="{line}" stroke-width="2"></path>'

def elders_crete(p, w, h):
    """Appoint elders in every city: a plate — the island of Crete in outline, its cities marked, and at each city an elder
    standing (an outlined figure), the gold title AN ELDER IN EVERY CITY."""
    o = [plate_bg(w, h, "TITUS 1:5 · ELDERS IN EVERY CITY"), mk.defs("gp", *ALL)]
    sc = min((w - 40) / (2.8 * 0.82), (h - 60) / 0.9)
    P, path = island(w, h, w * 0.5, 40 + (h - 40) * 0.56, sc)
    o.append(path)
    towns = [("CNOSSUS", 25.16, 35.3), ("GORTYNA", 24.95, 35.08), ("LASEA", 24.8, 34.97), ("PHŒNIX", 24.1, 35.24), ("KYDONIA", 24.03, 35.47),
             ("LYTTOS", 25.38, 35.2), ("HIERAPYTNA", 25.74, 35.03), ("ELEUTHERNA", 24.68, 35.33)]
    fs = min(0.22, sc / 900)
    for nm, lon, lat in towns:
        x, y = P(lon, lat)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="4" fill="{GOLD}" stroke="{INK}" stroke-width="1"></circle>')
        o.append(_person_mark(x, y - 6, fs, "#24506E", head=True))
        o.append(label(x, y + 16, nm, CY, 8.5))
    return "".join(o)

def steward_plate(p, w, h):
    """The bishop must be blameless, as God's steward (1:6–9): a plate — an elder of Crete with the keys of a steward at his
    girdle at the left, his qualities at the right."""
    def fig(pp, x, y, s):
        keys = ('<path d="M10 -104 L 14 -84" stroke="#C8963E" stroke-width="2"></path><circle cx="15" cy="-80" r="4" fill="none" stroke="#C8963E" stroke-width="2"></circle>'
                '<path d="M17 -78 L 22 -66 L 26 -68" fill="none" stroke="#C8963E" stroke-width="2"></path>')
        return elder(pp, x, y, s, 1, extra=keys)
    items = [("BLAMELESS", False), ("THE HUSBAND OF ONE WIFE", False), ("CHILDREN THAT BELIEVE", False), ("NOT SELF-WILLED", True), ("NOT SOON ANGRY", True),
             ("NO BRAWLER", True), ("NO STRIKER", True), ("NOT GREEDY OF FILTHY LUCRE", True), ("GIVEN TO HOSPITALITY", False), ("A LOVER OF GOOD", False),
             ("SOBER-MINDED", False), ("JUST", False), ("HOLY", False), ("SELF-CONTROLLED", False), ("HOLDING TO THE FAITHFUL WORD", False)]
    return qualities(p, w, h, "TITUS 1:6–9 · AS GOD'S STEWARD", items, fig, cols=2)

def household_plate(people, title):
    """Household plates (Titus 2): a plate on cream paper of figures standing in cells, each with a name over it and one line
    of what the letter asks of them under it (labels: the ASV's words). people = [(fig(p, x, y, s), NAME, LINE), …]."""
    def draw(p, w, h):
        o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{CREAM}"></rect>', f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="{PAPER_INK}" stroke-width="1.4"></rect>',
             title_bar_cream(w, title), mk.defs(p, *ALL, "ManUp", "WomanUp")]
        n = len(people); cw = (w - 16) / n
        top, foot = 44, h - 64                                     # the lines under the figures kept clear of the verse badge
        s = min((foot - top - 26) / 210, cw * 0.62 / 70)
        for i, (fig, name, line) in enumerate(people):
            x0 = 8 + i * cw
            if i: o.append(f'<path d="M{f(x0)} {f(top)} L {f(x0)} {f(h - 8)}" stroke="{PAPER_INK}" stroke-width="1" stroke-dasharray="4 4"></path>')
            o.append(f'<ellipse cx="{f(x0 + cw / 2)}" cy="{f(foot)}" rx="{f(cw * 0.36)}" ry="5" fill="#D8C8A0"></ellipse>')
            o.append(fig(p, x0 + cw / 2, foot, s))
            o.append(label(x0 + cw / 2, top + 14, name, "#7A4A10", 10.5))
            o.append(two_lines(x0 + cw / 2, foot + 2, line, PAPER_INK, max(7.5, min(9, cw / 26))))
        return "".join(o)
    return draw

def _aged_man(p, x, y, s): return elder(p, x, y, s, 2, extra='<path d="M-40 -186 L -34 4" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M-40 -186 L -34 4" stroke="#8A6A3A" stroke-width="4.5" stroke-linecap="round"></path>', up=[(-22, -158), (-34, -124), (-38, -100)])
def _aged_woman(p, x, y, s): return woman(p, x, y, s, 0, old=True)
def _young_woman(p, x, y, s):
    jar = '<path d="M-58 -150 C -68 -160 -66 -184 -54 -190 L -42 -190 C -30 -184 -28 -160 -38 -150 Z" fill="#B85A32" stroke="#0D0D0F" stroke-width="1.6"></path>'
    return woman(p, x, y, s, 1, up=[(-22, -158), (-40, -176), (-46, -186)], extra=jar)
def _young_man(p, x, y, s): return young_man(p, x, y, s, 0)
def _servant(p, x, y, s):
    return robed(p, x, y, s, "#8A7A5A", hair="#2A1A10", belt="#5A3A22", up=[(-22, -158), (-40, -132), (-56, -118)],
                 extra='<path d="M-74 -118 L -40 -118 L -44 -96 L -70 -96 Z" fill="#B8884A" stroke="#0D0D0F" stroke-width="1.6"></path>')

AGED = household_plate([(_aged_man, "AGED MEN", "TEMPERATE, GRAVE, SOBER-MINDED"), (_aged_woman, "AGED WOMEN", "REVERENT, TEACHERS OF THAT WHICH IS GOOD")],
                       "TITUS 2:2–3 · AGED MEN · AGED WOMEN")
YOUNG = household_plate([(_young_woman, "YOUNG WOMEN", "TO LOVE THEIR HUSBANDS, THEIR CHILDREN"), (_aged_woman, "TRAINED BY THE AGED", "WORKERS AT HOME, KIND")],
                        "TITUS 2:4–5 · THE YOUNG WOMEN")
SERVANTS = household_plate([(_servant, "SERVANTS", "WELL-PLEASING, NOT GAINSAYING"), (lambda p, x, y, s: elder(p, x, y, s, 3), "THEIR OWN MASTERS", "SHOWING ALL GOOD FIDELITY")],
                           "TITUS 2:9–10 · SERVANTS")

def ensample(p, w, h, seed):
    """The younger men likewise exhort to be sober-minded: in all things showing thyself an ensample of good works: the
    courtyard of a house in Crete in the morning, Titus with the open roll teaching three younger men sitting on the bench;
    the sea beyond the wall."""
    b = h * 0.95
    s = fig_k(w, h)
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"), f'<rect x="-10" y="{f(h * 0.4)}" width="{f(w + 20)}" height="{f(h * 0.12)}" fill="#3A8AB0"></rect>',
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(b - h * 0.5)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8B07A" stroke="{INK}" stroke-width="2"></rect>']
    o.append(titus_fig_(p, w * 0.22, b, s, flip=True, up=[(-22, -158), (-48, -150), (-72, -156)], extra=_sheet(-40, -128, 36, 26, rot=6)))
    o.append(bench(w * 0.5, b, w * 0.36, s))
    for i, x in enumerate((0.56, 0.68, 0.8)):
        c, hr, bd = [("#8A7A5A", "#2A1A10", None), ("#4A5A6A", "#1A1210", "#1A1210"), ("#6A4A3A", "#3A2214", None)][i]
        o.append(robed(p, w * x, b, s, c, hair=hr, beard=bd, pose="sit", seat=None))
    return "".join(o)

def crete_dawn(w, h, seed):
    """The grace of God hath appeared, bringing salvation to all men … looking for the blessed hope: dawn over the sea of
    Crete, the sun rising out of the water behind the long ridge of the island, its light laid across the sea."""
    hz = h * 0.56
    o = [sky(w, h, "#2A2A5A", "#FFC890"), halo(w * 0.6, hz, max(w, h) * 0.55, "#FFF4C2", 0.6), rays(w * 0.6, hz, 28, h * 0.1, max(w, h), "#FFF4C2", 0.2, 4, 180, 360),
         f'<circle cx="{f(w * 0.6)}" cy="{f(hz)}" r="{f(h * 0.08)}" fill="#FFF8DC"></circle>',
         f'<path d="M-10 {f(hz)} L {f(w * 0.1)} {f(hz - h * 0.08)} L {f(w * 0.22)} {f(hz - h * 0.05)} L {f(w * 0.36)} {f(hz - h * 0.16)} L {f(w * 0.46)} {f(hz - h * 0.04)} L {f(w * 0.5)} {f(hz)} Z" fill="#4A3A5A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.74)} {f(hz)} L {f(w * 0.84)} {f(hz - h * 0.06)} L {f(w * 0.94)} {f(hz - h * 0.1)} L {f(w + 10)} {f(hz - h * 0.04)} L {f(w + 10)} {f(hz)} Z" fill="#4A3A5A" stroke="{INK}" stroke-width="2"></path>',
         f'<rect x="-10" y="{f(hz)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A5A8A"></rect>',
         ] + [f'<path d="M{f(w * 0.6 - (w * 0.04 + (y_ - hz) * 0.32))} {f(y_)} L {f(w * 0.6 + (w * 0.04 + (y_ - hz) * 0.32))} {f(y_)}" stroke="#FFE6A0" stroke-width="{f(2 + (y_ - hz) / 40)}" '
              f'stroke-dasharray="{f(14 + (y_ - hz) / 6)} {f(8 + (y_ - hz) / 10)}" opacity="0.85"></path>' for y_ in [hz + (h - hz) * t_ for t_ in (0.04, 0.12, 0.22, 0.34, 0.48, 0.64, 0.82)]]
    r = random.Random(seed)
    for i in range(14):
        y = hz + (h - hz) * r.uniform(0.1, 0.95); x = w * r.uniform(0.0, 1.0); L = w * r.uniform(0.03, 0.08)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + L)} {f(y)}" stroke="#8FD0E2" stroke-width="2" opacity="0.6"></path>')
    return "".join(o)

def nicopolis(w, h):
    """When I shall send Artemas unto thee, or Tychicus, give diligence to come unto me to Nicopolis: for there I have
    determined to winter: the map — from Crete over the sea and up the coast to Nicopolis on the gulf of Epirus, lit."""
    rt = ["CNOSSUS", (23.6, 36.0), (22.0, 36.6), (21.2, 37.4), (21.0, 38.4), "NICOPOLIS"]
    return letter_road(w, h, rt, title="TITUS 3:12 · TO NICOPOLIS FOR THE WINTER", box=(19.6, 27.0, 34.6, 40.6),
                       places=("CNOSSUS", "GORTYNA", "CORINTH", "ATHENS", "NICOPOLIS"), hi=("CNOSSUS", "NICOPOLIS"),
                       regions=("MACEDONIA", "ACHAIA", ("CRETE", 24.9, 35.62), ("EPIRUS", 20.9, 39.7)))

def zenas_apollos(p, w, h, seed):
    """Set forward Zenas the lawyer and Apollos on their journey diligently, that nothing be wanting unto them: a haven of
    Crete in the morning (Acts' harbour), the ship at the quay; Zenas with his rolls of the law under his arm and Apollos
    (as Acts draws him) going down to it, Titus seeing them off with a basket of bread and a skin of water for the way."""
    b = h * 0.94
    s = fig_k(w, h, 0.28, 0.66)
    o = [_defs(p), harbour(p, w, h, seed)]
    rolls = ''.join(f'<rect x="{-30 + 6 * i}" y="{-132 + 4 * i}" width="30" height="7" rx="3" fill="#EADBB4" stroke="#0D0D0F" stroke-width="1.2" transform="rotate(-20 -15 -128)"></rect>' for i in range(3))
    o.append(robed(p, w * 0.5, b, s, "#3A4A6A", head="#E8E2D6", cord="#3A2A1A", beard="#5A5A5A", mantle="#2A3A4A", flip=True, extra=rolls))
    o.append(apollos_r(p, w * 0.62, b, s, flip=True))
    gift = ('<path d="M-76 -140 L -40 -140 L -44 -116 L -72 -116 Z" fill="#B8884A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<ellipse cx="-66" cy="-142" rx="7" ry="5" fill="#D8A060" stroke="#0D0D0F" stroke-width="1"></ellipse><ellipse cx="-52" cy="-143" rx="7" ry="5" fill="#D8A060" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(titus_fig_(p, w * 0.82, b, s, up=[(-22, -158), (-44, -144), (-62, -140)], extra=gift))
    o.append(plate_label(w * 0.5, b - 222 * s, "ZENAS", "#12113A", 10, halo_="#F3EFE6") + plate_label(w * 0.62, b - 236 * s, "APOLLOS", "#12113A", 10, halo_="#F3EFE6")
             + plate_label(w * 0.82, b - 222 * s, "TITUS", "#12113A", 10, halo_="#F3EFE6"))
    return "".join(o)

from act.art15 import harbour
from co2.art2 import basin_water
from co1.art2 import washed
from rom.art5 import ruler_seat
