"""Drawings for the 2 Corinthians volume, chapter 1 (2 Corinthians 1–5), and the letter's cast and helpers shared by the
later chapters (co2.art2, co2.art3 start `from co2.art import *`).

2 Corinthians starts from all of Acts' drawings (`from act.art16 import *`, which carries act.art … act.art15, Mark's and
Matthew's drawings) and from the epistle kit (epistle.py: the study, the sealed scroll, the still life, the letter's road,
the radiance, the technical plate), and adds its own. It does not import Romans' drawings (rom.art): the few it shares in
kind (the tables of stone, the heart) are drawn here.

People at a distance, on the kit silhouettes (epistle.robed): Paul only ever epistle.paul_fig; Timothy (timothy_fig) young,
beardless, bareheaded, light-brown hair, a grey-blue tunic, as Acts draws him; Titus (titus_fig) a Greek, bareheaded, short
black hair, clean-shaven, a sand tunic and a blue mantle; Moses (moses_fig) as Exodus draws him (brown robe, off-white
headcloth with a dark cord, black beard). God is never drawn (light, an empty seat); Satan is never drawn and no serpent is.
Every function takes (p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to the panel, names the figure defs."""
import sys, pathlib, math, random, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from act.art16 import *
from act.art import f, INK, soldier_fig
from epistle import (study, still_life, sealed_scroll, open_letter, reed_pen, inkpot, lamp_glow, letter_road, plate_bg, radiance, tag, dim, robed, paul_fig,
                     scribe_seated, low_table, mat as floor_mat, couch, pigeonholes, doorway, SEPIA, SEAL)
from genesis.art4 import clay_lamp
from genesis.art3 import label, node, route
from oba.minor import vista, halo, rays, starfield, bolt, rain, sea as sea_
from job.art import seated
from exo.art import MOSES_ROBE
from exo.art10 import MOSES_VEIL
import exodus4 as E4
import act.geo as geo

GOLD, CY = "#FFD23F", "#8FD0E2"

def plate_label(x, y, text, color=GOLD, size=10, anchor="middle", halo_="#0B1A2E"):
    """A label with a dark halo so it reads over a drawing."""
    return label(x, y, text, color, size, anchor).replace('stroke="#0B1A2E"', f'stroke="{halo_}"', 1)

# ---- the cast at a distance -----------------------------------------------------------------------------------------------
TIMOTHY_LOOK = dict(cloth="#7A8A9A", hair="#3A2214")
TITUS_LOOK = dict(cloth="#C8B080", hair="#1A1210", mantle="#2A4A7A")

def timothy_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Timothy: young, beardless, bareheaded, light-brown hair, a grey-blue tunic (Acts' colours)."""
    return robed(p, x, y, s, TIMOTHY_LOOK["cloth"], hair=TIMOTHY_LOOK["hair"], belt="#3A4A5A", flip=flip, up=up, extra=extra)

def titus_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Titus, a Greek: bareheaded, short black hair, clean-shaven, a sand tunic and a blue mantle."""
    return robed(p, x, y, s, TITUS_LOOK["cloth"], hair=TITUS_LOOK["hair"], mantle=TITUS_LOOK["mantle"], belt="#6A4A2A", flip=flip, up=up, extra=extra)

def moses_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Moses as Exodus draws him: a brown robe, an off-white headcloth with a dark cord, a black beard."""
    return robed(p, x, y, s, MOSES_ROBE, head="#E2D8C4", cord="#3A2214", beard="#2A1A10", flip=flip, up=up, extra=extra)

def brother(p, x, y, s, i=0, flip=False, up=None, extra=""):
    """One of the brethren (the saints at Corinth, the churches of Macedonia): men in cool or off-white headcloths, women
    veiled, each look fixed by i."""
    looks = [dict(cloth="#4A5A6A", head="#2A3A4A", beard="#2A1A10"), dict(cloth="#6A5A4A", head="#E8E2D6", beard="#7A746A"),
             dict(cloth="#3A5A4A", woman=True, veil="#1F3A5A"), dict(cloth="#5A4A5A", head="#3A3A4A", beard="#3A2A1A"),
             dict(cloth="#8A7A5A", hair="#2A1A10"), dict(cloth="#4A4A6A", woman=True, veil="#2A2A3A"),
             dict(cloth="#6A6A5A", head="#F3EFE6", beard="#B8B2A8"), dict(cloth="#5A6A7A", hair="#1A1210", beard="#1A1210")]
    lk = dict(looks[i % len(looks)])
    woman = lk.pop("woman", False)
    return robed(p, x, y, s * (0.94 if woman else 1), lk.pop("cloth"), woman=woman, cord="#1A1210", flip=flip, up=up, extra=extra, **lk)

_HD, _CD = "#010203", "#040506"

def scribe_bare(x, y, s, cloth, hair, flip=False, stage="write"):
    """epistle.scribe_seated, bareheaded: the headcloth swapped for short hair (Timothy writing the letter, 1:1)."""
    svg = scribe_seated(x, y, s, cloth=cloth, head=_HD, cord=_CD, flip=flip, stage=stage)
    hx, hy = (6, -118) if stage == "write" else (2, -122)
    hp = (f'<path d="M{hx - 13} {hy + 5} C {hx - 17} {hy - 10} {hx - 8} {hy - 17} {hx + 1} {hy - 15} C {hx + 9} {hy - 14} {hx + 14} {hy - 9} {hx + 13} {hy - 3} '
          f'C {hx + 7} {hy - 8} {hx} {hy - 8} {hx - 4} {hy - 4} C {hx - 6} {hy} {hx - 8} {hy + 5} {hx - 9} {hy + 9} Z" fill="{hair}" stroke="{INK}" stroke-width="1.6"></path>')
    svg = re.sub(r'<path d="[^"]*" fill="%s"[^>]*></path>' % _HD, hp, svg)
    return re.sub(r'<path d="[^"]*" fill="none" stroke="%s"[^>]*></path>' % _CD, "", svg)

def study2(p, w, h, seed, stage="dictate", scribe=True, bearer=False, night=True, window="city", fig_h=None):
    """The letter written in Macedonia: epistle.study with this letter's people — Timothy (bareheaded) writing as Paul
    dictates (1:1: "Paul … and Timothy our brother"); bearer=True Titus: standing at the right listening (dictate, read),
    or taking the sealed scroll at the door (give: 8:16–23)."""
    b = h * 0.95; s = (fig_h or h * 0.72) / 205; k = s
    o = [study(p, w, h, seed, stage=stage, scribe=False, bearer=None, night=night, window=window, fig_h=fig_h)]
    tl = TIMOTHY_LOOK
    if stage == "give":
        if scribe: o.append(scribe_bare(w * 0.12, b - 4 * k, k, tl["cloth"], tl["hair"], stage="write"))
        if bearer:
            dx, dw = w * 0.68, min(w * 0.22, 120 * k)
            o.append(titus_fig(p, dx + dw * 0.5, b, s, up=[(-22, -158), (-42, -146), (-62, -146)], extra=sealed_scroll(-70, -150, 0.3, rot=12)))
        return "".join(o)
    if scribe:
        sx = w * 0.56
        tx = (w * 0.24 + 76 * k + sx - 78 * k) / 2 - 26 * k
        o.append(low_table(tx, b, 52 * k, k) + clay_lamp(tx + 18 * k, b - 31 * k, k * 0.5) + inkpot(tx + 42 * k, b - 30 * k, k * 0.5))
        o.append(scribe_bare(sx, b - 4 * k, k, tl["cloth"], tl["hair"], flip=True, stage="write" if stage == "dictate" else "read"))
    if bearer: o.append(titus_fig(p, w * 0.9, b, s, flip=True))
    return "".join(o)

# ---- small things ---------------------------------------------------------------------------------------------------------
def tablets(cx, cy, s, op=1.0):
    """The two tables of stone, round-topped, with rows of writing (no words)."""
    o = []
    for side in (-1, 1):
        x = cx + side * 34 * s
        o.append(f'<path d="M{f(x - 30 * s)} {f(cy + 60 * s)} L {f(x - 30 * s)} {f(cy - 40 * s)} C {f(x - 30 * s)} {f(cy - 74 * s)} {f(x + 30 * s)} {f(cy - 74 * s)} {f(x + 30 * s)} {f(cy - 40 * s)} '
                 f'L {f(x + 30 * s)} {f(cy + 60 * s)} Z" fill="#B8B0A0" stroke="{INK}" stroke-width="2.4" opacity="{op}"></path>')
        for k in range(5):
            yy = cy - 34 * s + k * 18 * s
            o.append(f'<path d="M{f(x - 20 * s)} {f(yy)} L {f(x + 20 * s)} {f(yy)}" stroke="#4A4038" stroke-width="{f(2.4 * s)}" stroke-dasharray="{f(6 * s)} {f(3 * s)}" opacity="{op}"></path>')
    return "".join(o)

def heart(cx, cy, R, fill="#C8202A", writing=True, glow_=True):
    """A heart (of flesh), rows of writing on it in light."""
    d = (f"M{f(cx)} {f(cy + R)} C {f(cx - R * 1.4)} {f(cy)} {f(cx - R * 1.1)} {f(cy - R * 1.1)} {f(cx)} {f(cy - R * 0.45)} "
         f"C {f(cx + R * 1.1)} {f(cy - R * 1.1)} {f(cx + R * 1.4)} {f(cy)} {f(cx)} {f(cy + R)} Z")
    o = [halo(cx, cy, R * 1.8, "#FF8A6A", 0.45) if glow_ else "", f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="2.6"></path>']
    if writing:
        for k in range(4):
            yy = cy - R * 0.36 + k * R * 0.24; hw = R * (0.62 - abs(k - 1.2) * 0.12)
            o.append(f'<path d="M{f(cx - hw)} {f(yy)} L {f(cx + hw)} {f(yy)}" stroke="#FFE6A0" stroke-width="{f(max(1.6, R * 0.05))}" stroke-dasharray="{f(R * 0.12)} {f(R * 0.05)}"></path>')
    return "".join(o)

def signet(x, y, s=1.0, rot=0):
    """A signet ring: a gold band, the bezel an oval stone cut with a mark."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})">'
            f'<ellipse cx="0" cy="14" rx="22" ry="26" fill="none" stroke="{INK}" stroke-width="10"></ellipse>'
            f'<ellipse cx="0" cy="14" rx="22" ry="26" fill="none" stroke="#E8B830" stroke-width="6.5"></ellipse>'
            f'<ellipse cx="0" cy="-14" rx="17" ry="12" fill="#B8820E" stroke="{INK}" stroke-width="2.4"></ellipse>'
            f'<ellipse cx="0" cy="-15" rx="12" ry="8" fill="#5A1A2A" stroke="{INK}" stroke-width="1.6"></ellipse>'
            '<path d="M-6 -15 L 0 -21 L 6 -15 L 0 -9 Z" fill="none" stroke="#E8B830" stroke-width="1.4"></path></g>')

def jar(x, base, s, uid, glow_=True, lie=False, crack=True):
    """An earthen vessel: a plain storage jar of red clay with two handles, (x, base) the middle of its foot (about 150
    units tall at s = 1); glow_=True light shining from within it — out of its mouth and through the hairline cracks;
    lie=True the jar knocked over on its side, unbroken, the light spilling from its mouth."""
    body = ("M-14 0 C -40 -6 -52 -40 -50 -74 C -48 -104 -34 -122 -18 -128 L -16 -138 L 16 -138 L 18 -128 C 34 -122 48 -104 50 -74 "
            "C 52 -40 40 -6 14 0 Z")
    rot = f' rotate(-84 0 -70)' if lie else ""
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)}){rot}">']
    if glow_:
        o.append(halo(0, -100, 150, "#FFE680", 0.5) + rays(0, -146, 14, 20, 120, "#FFF4C2", 0.35, 4, a0=200, a1=340))
    o.append(f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7A3A1E"></stop><stop offset="0.45" stop-color="#C8682E"></stop>'
             f'<stop offset="1" stop-color="#6A2E16"></stop></linearGradient></defs>'
             f'<path d="M-18 -112 C -40 -114 -46 -96 -44 -84" fill="none" stroke="{INK}" stroke-width="9"></path><path d="M-18 -112 C -40 -114 -46 -96 -44 -84" fill="none" stroke="#A8582A" stroke-width="5"></path>'
             f'<path d="M18 -112 C 40 -114 46 -96 44 -84" fill="none" stroke="{INK}" stroke-width="9"></path><path d="M18 -112 C 40 -114 46 -96 44 -84" fill="none" stroke="#A8582A" stroke-width="5"></path>'
             f'<path d="{body}" fill="url(#{uid})" stroke="{INK}" stroke-width="3"></path>'
             '<path d="M-44 -92 C -10 -98 10 -98 44 -92 M-48 -56 C -10 -62 10 -62 48 -56" fill="none" stroke="#5A2410" stroke-width="1.6" opacity="0.7"></path>'
             f'<ellipse cx="0" cy="-138" rx="17" ry="5" fill="{"#FFF4C2" if glow_ else "#2A140A"}" stroke="{INK}" stroke-width="2.2"></ellipse>')
    if glow_ and crack:
        o.append('<path d="M-30 -34 L -22 -46 L -26 -58 L -16 -72" fill="none" stroke="#0D0D0F" stroke-width="4"></path>'
                 '<path d="M-30 -34 L -22 -46 L -26 -58 L -16 -72" fill="none" stroke="#FFE680" stroke-width="2"></path>'
                 '<path d="M26 -20 L 32 -34 L 28 -44" fill="none" stroke="#0D0D0F" stroke-width="4"></path>'
                 '<path d="M26 -20 L 32 -34 L 28 -44" fill="none" stroke="#FFE680" stroke-width="2"></path>')
    return "".join(o) + "</g>"

def tomb_mon(x, base, s, kind=0, color="#C8B898"):
    """A tomb by the roadside (the roads out of a Roman city were lined with them): kind 0 a small shrine-tomb with a
    pediment and a dark niche, 1 a drum tomb with a cone roof, 2 a plain altar-tomb on steps. (x, base) its foot."""
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)})">',
         f'<rect x="-34" y="-12" width="68" height="12" fill="#9A8A70" stroke="{INK}" stroke-width="2"></rect>']
    if kind == 0:
        o.append(f'<rect x="-24" y="-82" width="48" height="70" fill="{color}" stroke="{INK}" stroke-width="2.2"></rect>'
                 f'<path d="M-30 -82 L 0 -104 L 30 -82 Z" fill="{color}" stroke="{INK}" stroke-width="2.2"></path>'
                 f'<path d="M-10 -20 L -10 -56 C -10 -66 10 -66 10 -56 L 10 -20 Z" fill="#2A2020" stroke="{INK}" stroke-width="1.6"></path>')
    elif kind == 1:
        o.append(f'<rect x="-30" y="-64" width="60" height="52" fill="{color}" stroke="{INK}" stroke-width="2.2"></rect>'
                 f'<ellipse cx="0" cy="-64" rx="30" ry="7" fill="#D8CCB0" stroke="{INK}" stroke-width="2"></ellipse>'
                 f'<path d="M-28 -66 L 0 -100 L 28 -66 Z" fill="#8A7A60" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M-30 -40 L 30 -40" stroke="#8A7A60" stroke-width="2"></path>')
    else:
        o.append(f'<rect x="-28" y="-24" width="56" height="12" fill="#B8A888" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="-18" y="-60" width="36" height="36" fill="{color}" stroke="{INK}" stroke-width="2.2"></rect>'
                 f'<rect x="-22" y="-66" width="44" height="8" fill="#D8CCB0" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o) + "</g>"

def straight_road(w, h, hz, vx, x0, x1, color="#B8946A", joints=8):
    """A road running from the bottom of the panel (x0 … x1) to a vanishing point (vx) on the horizon hz."""
    o = [f'<path d="M{f(vx - 5)} {f(hz)} L {f(vx + 5)} {f(hz)} L {f(x1)} {f(h + 10)} L {f(x0)} {f(h + 10)} Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>']
    for i in range(1, joints + 1):
        t = (i / (joints + 1)) ** 1.7; y = hz + (h + 10 - hz) * t
        a, b = vx - 5 + (x0 - vx + 5) * t, vx + 5 + (x1 - vx - 5) * t
        o.append(f'<path d="M{f(a)} {f(y)} L {f(b)} {f(y)}" stroke="#8A6A4A" stroke-width="{f(0.8 + 1.4 * t)}"></path>')
    return "".join(o)

# ---- 2 Corinthians 1 ------------------------------------------------------------------------------------------------------
def letter_to_corinth(w, h):
    """The letter's road: from Philippi in Macedonia by Thessalonica and Berœa, down through Greece to Corinth in Achaia."""
    rt = ["PHILIPPI", "AMPHIPOLIS", "APOLLONIA", "THESSALONICA", "BERŒA", (22.3, 39.6), (22.7, 38.7), (22.6, 38.2), "CORINTH"]
    return letter_road(w, h, rt, title="2 CORINTHIANS 1:1 · FROM MACEDONIA TO CORINTH", box=(19.6, 28.4, 36.9, 41.7),
                       places=("PHILIPPI", "THESSALONICA", "BERŒA", "ATHENS", "CORINTH", "TROAS", "EPHESUS"), hi=("PHILIPPI", "CORINTH"),
                       regions=("MACEDONIA", "ACHAIA", "ASIA"))

def asia_road(w, h, seed):
    """The affliction which befell us in Asia: the road out of a city at dusk, lined with tombs as the Roman roads were,
    the hills bare beyond it — no one on it (the sentence of death told in words)."""
    hz = h * 0.48
    o = [sky(w, h, "#1E1430", "#D8784A"), sun(w * 0.7, hz - h * 0.05, max(14, h * 0.06), color="#FF8A3D", op=0.35),
         hills(w, h, hz - h * 0.07, seed, color="#4A2A3A", amp=16, step=90), hills(w, h, hz, seed + 1, color="#6A3A30", amp=10, step=70),
         ground(w, h, hz + h * 0.01, "#6A4030", dy=0)]
    vx = w * 0.58
    o.append(straight_road(w, h, hz + h * 0.01, vx, w * 0.24, w * 0.86))
    r = random.Random(seed)
    for t in (0.1, 0.2, 0.34, 0.52, 0.78, 1.04):
        y = hz + (h - hz) * t; k = max(0.12, (h / 300) * t * 1.05)
        xl = vx - 5 + (w * 0.24 - vx) * t - 46 * k; xr = vx + 5 + (w * 0.86 - vx) * t + 46 * k
        o.append(tomb_mon(xl, y, k, r.randint(0, 2), color=r.choice(["#C8B898", "#B8A888", "#D0C0A0"])))
        o.append(tomb_mon(xr, y, k, r.randint(0, 2), color=r.choice(["#C8B898", "#B8A888", "#D0C0A0"])))
    o.append(birds(3, w * 0.62, w * 0.86, h * 0.1, h * 0.3, seed, color="#1E1430"))
    return "".join(o)

def purposed(w, h):
    """I was minded to come first unto you, and by you to pass into Macedonia, and again from Macedonia to come unto you,
    and of you to be set forward on my journey unto Judæa: the journey purposed, leg by leg, on the map."""
    return geo.med_map(w, h, box=(20.6, 36.4, 30.8, 42.0), places=("EPHESUS", "CORINTH", "PHILIPPI", "THESSALONICA", "TROAS", "JERUSALEM"),
                       routes=[["EPHESUS", (25.0, 37.6), "CORINTH"], ["CORINTH", (22.7, 38.7), (22.3, 39.6), "THESSALONICA", "PHILIPPI"],
                               ["PHILIPPI", (24.3, 40.2), (24.0, 38.6), (23.4, 37.6), "CORINTH"], ["CORINTH", (24.5, 36.4), (29.0, 34.4), (34.0, 32.6), "CÆSAREA", "JERUSALEM"]],
                       hi=("CORINTH",), regions=("MACEDONIA", "ACHAIA", "ASIA", "JUDÆA", "THE GREAT SEA"), lit_routes=[0, 1, 2, 3], size=10,
                       title="2 CORINTHIANS 1:15–16 · THE JOURNEY PURPOSED")

def seal_earnest(w, h):
    """He sealed us, and gave us the earnest of the Spirit in our hearts: a plate — the signet and the letter sealed with it
    at the left (a seal marks what is the owner's); at the right the heart with the light in it, the earnest (the first part
    given, a pledge of the whole)."""
    import exo.art8 as B
    o = [plate_bg(w, h, "2 CORINTHIANS 1:21–22 · SEALED · THE EARNEST OF THE SPIRIT")]
    k = min(w / 560, (h - 40) / 230); cy = h * 0.56
    o.append(f'<path d="M{f(w * 0.5)} 34 L {f(w * 0.5)} {f(h - 10)}" stroke="#2C5A7A" stroke-width="1.6" stroke-dasharray="6 5"></path>')
    o.append(sealed_scroll(w * 0.25, cy + 20 * k, 1.5 * k, rot=-6) + signet(w * 0.25 + 70 * k, cy - 54 * k, 1.0 * k, rot=18))
    o.append(heart(w * 0.75, cy, 54 * k, writing=False) + halo(w * 0.75, cy - 6 * k, 70 * k, "#FFF4C2", 0.7)
             + rays(w * 0.75, cy - 6 * k, 18, 30 * k, 110 * k, "#FFF4C2", 0.4, 3))
    ly = min(cy + 82 * k, h - 12)
    o.append(label(w * 0.25, ly, "WHO ALSO SEALED US", CY, 10) + label(w * 0.75, ly, "THE EARNEST OF THE SPIRIT IN OUR HEARTS", GOLD, 10))
    B._W[0] = w
    o.append(tag(w * 0.25 + 70 * k, cy - 74 * k, "THE SIGNET", w * 0.25 + 150 * k, cy - 96 * k, color=CY))
    return "".join(o)

# ---- 2 Corinthians 2 ------------------------------------------------------------------------------------------------------
def tear_stained(w, h, seed):
    """I wrote unto you with many tears: the open sheet of the letter on the table by lamplight, the reed pen laid by, the
    ink spotted where the tears fell."""
    o = [still_life(w, h, seed, sealed=False, night=True)]
    ty = h * 0.62; r = random.Random(seed)
    x0, y0, ww, hh = w * 0.18, ty + h * 0.04, w * 0.42, h * 0.26
    for _ in range(7):
        x, y = x0 + ww * r.uniform(0.1, 0.9), y0 + hh * r.uniform(0.15, 0.85); rr = max(3.0, h * r.uniform(0.012, 0.02))
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr * 1.3)}" ry="{f(rr)}" fill="#9AB8D0" opacity="0.55" stroke="#5A7A9A" stroke-width="0.8" transform="rotate(-3 {f(w * 0.4)} {f(ty)})"></ellipse>')
    return "".join(o)

def welcomed(p, w, h, seed):
    """Forgive him and comfort him … confirm your love toward him: in the house where the church meets, the brethren
    standing, an elder holding out his hand to the man come back to the door."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#C8A878", floor="#8A6A4A"), lamp_glow(w * 0.4, b - h * 0.5, max(w, h) * 0.4, f"{p}lg", op=0.3)]
    s = fit(b, max(h * 0.24, b - 210))
    dx, dw = w * 0.76, min(w * 0.17, 150 * s)
    o.append(doorway(dx, b - 220 * s, dw, b, seed, night=False))
    o.append(brother(p, dx + dw * 0.5, b, s * 0.98, 3, flip=True))
    o.append(brother(p, w * 0.58, b, s, 6, up=[(-22, -158), (-46, -138), (-70, -128)], flip=True))
    for i, (x, j) in enumerate(((0.1, 0), (0.22, 2), (0.34, 4), (0.45, 1))):
        o.append(brother(p, w * x, b, s * (0.97 + 0.03 * (i % 2)), j, flip=True))
    return "".join(o)

def troas_door(p, w, h, seed):
    """When I came to Troas … a door was opened unto me in the Lord, and I had no relief … because I found not Titus: the
    door of a house at Troas open on the harbour, Paul in it looking out over the sea toward Macedonia, a ship under sail."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp"), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3A30"></rect>']
    dx0, dx1, dt = w * 0.3, w * 0.94, h * 0.08
    uid = f"{p}td"
    o.append(f'<defs><clipPath id="{uid}"><rect x="{f(dx0)}" y="{f(dt)}" width="{f(dx1 - dx0)}" height="{f(b - dt)}"></rect></clipPath></defs><g clip-path="url(#{uid})">'
             + sky(w, h, "#8FD0E2", "#FFE6B0") + sun(w * 0.8, h * 0.3, max(12, h * 0.05), color="#FFE680", op=0.4)
             + f'<path d="M{f(dx0)} {f(h * 0.46)} C {f(w * 0.5)} {f(h * 0.42)} {f(w * 0.7)} {f(h * 0.44)} {f(dx1)} {f(h * 0.42)} L {f(dx1)} {f(h * 0.5)} L {f(dx0)} {f(h * 0.5)} Z" fill="#7A8A9A" stroke="{INK}" stroke-width="1.4"></path>'
             + sea_(w, h, h * 0.5, seed, color="#1F6F9A", deep="#0F4C68") + ship(w * 0.7, h * 0.64, min(0.9, h / 360))
             + f'<rect x="{f(dx0)}" y="{f(h * 0.82)}" width="{f(dx1 - dx0)}" height="{f(h)}" fill="#A8987A" stroke="{INK}" stroke-width="2"></rect>'
             + '</g>')
    o.append(f'<rect x="{f(dx0 - 18)}" y="{f(dt - 16)}" width="{f(dx1 - dx0 + 36)}" height="16" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(x)}" y="{f(dt)}" width="18" height="{f(b - dt)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>' for x in (dx0 - 18, dx1)))
    o.append(f'<path d="M{f(dx0)} {f(dt)} L {f(dx0 - w * 0.2)} {f(dt + h * 0.06)} L {f(dx0 - w * 0.2)} {f(b + h * 0.02)} L {f(dx0)} {f(b)} Z" fill="#7A5A34" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(dx0 - w * 0.2 * t)} {f(dt + h * 0.06 * t)} L {f(dx0 - w * 0.2 * t)} {f(b + h * 0.02 * t)}" stroke="#5A3E22" stroke-width="2"></path>' for t in (0.33, 0.66)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2A20" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.2, b - 230))
    o.append(paul_fig(p, w * 0.42, b, s, flip=True))
    return "".join(o)

def censer(x, base, s, seed, uid):
    """A tripod censer at the roadside, incense smoke rising from its bowl in sweet gold curls."""
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)})">',
         f'<path d="M-16 0 L -6 -46 M16 0 L 6 -46 M0 2 L 0 -46" stroke="{INK}" stroke-width="5"></path><path d="M-16 0 L -6 -46 M16 0 L 6 -46 M0 2 L 0 -46" stroke="#B8860E" stroke-width="3"></path>',
         f'<path d="M-18 -48 C -16 -60 16 -60 18 -48 Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>', '</g>']
    r = random.Random(seed)
    pts = [(x, base - 60 * s)]
    for i in range(6):
        px, py = pts[-1]; pts.append((px + r.uniform(-14, 14) * s, py - 26 * s))
    d = "M" + " ".join(f"{f(a)} {f(b)}" for a, b in pts[:1]) + "".join(f" Q {f(pts[i][0] + (12 if i % 2 else -12) * s)} {f(pts[i][1] - 13 * s)} {f(pts[i + 1][0])} {f(pts[i + 1][1])}" for i in range(len(pts) - 1))
    o.append(f'<path d="{d}" fill="none" stroke="#FFF4C2" stroke-width="{f(9 * s)}" stroke-linecap="round" opacity="0.45"></path>'
             f'<path d="{d}" fill="none" stroke="#FFE680" stroke-width="{f(3 * s)}" stroke-linecap="round" opacity="0.8"></path>')
    return "".join(o)

def triumph(p, w, h, seed):
    """God always leadeth us in triumph in Christ, and maketh manifest through us the savor of his knowledge in every
    place: a triumph passing under the arch of a Roman city — the standards and the laurel, the street strewn, and the
    censers burning on either side, the sweet savour going up."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#5AB0D8", "#FFF4C2"), houses(w, h, h * 0.62, seed, hmin=0.2, hmax=0.3, stairs=False)]
    ax, aw, at = w * 0.5, min(w * 0.42, h * 1.1), h * 0.1
    o.append(f'<rect x="{f(ax - aw / 2)}" y="{f(at)}" width="{f(aw)}" height="{f(b - at)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(ax - aw / 2 - 8)}" y="{f(at - 14)}" width="{f(aw + 16)}" height="18" fill="#D8CCB0" stroke="{INK}" stroke-width="2.2"></rect>'
             f'<path d="M{f(ax - aw * 0.28)} {f(b)} L {f(ax - aw * 0.28)} {f(at + (b - at) * 0.42)} C {f(ax - aw * 0.28)} {f(at + (b - at) * 0.1)} {f(ax + aw * 0.28)} {f(at + (b - at) * 0.1)} {f(ax + aw * 0.28)} {f(at + (b - at) * 0.42)} L {f(ax + aw * 0.28)} {f(b)} Z" fill="#8FC0D8" stroke="{INK}" stroke-width="2.4"></path>')
    for side in (-1, 1):
        o.append(f'<path d="M{f(ax + side * aw * 0.38)} {f(at + 12)} L {f(ax + side * aw * 0.38)} {f(b)}" stroke="#B8AC90" stroke-width="{f(max(3, aw * 0.03))}"></path>')
    o.append(f'<path d="M{f(ax - aw * 0.4)} {f(at + 26)} C {f(ax - aw * 0.2)} {f(at + 46)} {f(ax)} {f(at + 46)} {f(ax)} {f(at + 30)} C {f(ax)} {f(at + 46)} {f(ax + aw * 0.2)} {f(at + 46)} {f(ax + aw * 0.4)} {f(at + 26)}" '
             f'fill="none" stroke="#2E6B3A" stroke-width="6"></path>')
    o.append(pavement(w, h, b - h * 0.02, color="#D8D0C0"))
    s = fit(b, max(h * 0.22, b - 200))
    for i, x in enumerate((0.32, 0.42, 0.52, 0.62)):
        std = (f'<path d="M30 -150 L 30 -250" stroke="#5A3A22" stroke-width="5"></path><circle cx="30" cy="-256" r="9" fill="#E8B830" stroke="{INK}" stroke-width="2"></circle>'
               f'<path d="M18 -236 L 42 -236 L 40 -214 L 20 -214 Z" fill="#B5121B" stroke="{INK}" stroke-width="1.6"></path>') if i % 2 == 0 else \
              (f'<path d="M30 -150 L 36 -224" stroke="#2E6B3A" stroke-width="4"></path>' + "".join(f'<ellipse cx="{36 + (5 if j % 2 else -5)}" cy="{-220 + j * 10}" rx="6" ry="3" fill="#4A8A3A" stroke="{INK}" stroke-width="1"></ellipse>' for j in range(5)))
        o.append(soldier_fig(p, w * x, b, s * 0.92, flip=True))
        o.append(f'<g transform="translate({f(w * x)} {f(b)}) scale({f(-s * 0.92)} {f(s * 0.92)})">{std}</g>')
    for x in (0.08, 0.2, 0.8, 0.92):
        o.append(censer(w * x, b, max(0.5, s * 0.9), seed + int(x * 100), f"{p}c{int(x * 100)}"))
    return "".join(o)

# ---- 2 Corinthians 3 ------------------------------------------------------------------------------------------------------
def hearts_of_flesh(w, h):
    """Ye are our epistle … written not with ink, but with the Spirit of the living God; not in tables of stone, but in
    tables that are hearts of flesh: a plate — the ink and reed pen, and the tables of stone, set back in the dark; the heart
    of flesh in the light, the writing on it shining."""
    o = [plate_bg(w, h, "2 CORINTHIANS 3:3 · AN EPISTLE OF CHRIST")]
    k = min(w / 600, (h - 40) / 230); cy = h * 0.56
    for x in (w * 0.34, w * 0.62):
        o.append(f'<path d="M{f(x)} 34 L {f(x)} {f(h - 10)}" stroke="#2C5A7A" stroke-width="1.6" stroke-dasharray="6 5"></path>')
    o.append(f'<g opacity="0.62">{inkpot(w * 0.12, cy + 40 * k, 1.8 * k)}{reed_pen(w * 0.24, cy + 44 * k, 1.4 * k, rot=24)}</g>')
    o.append(f'<g opacity="0.62">{tablets(w * 0.48, cy, 0.9 * k)}</g>')
    o.append(halo(w * 0.81, cy - 80 * k, 110 * k, "#FFF4C2", 0.55) + rays(w * 0.81, cy - 110 * k, 12, 10 * k, 80 * k, "#FFF4C2", 0.4, 3, a0=60, a1=120))
    o.append(heart(w * 0.81, cy + 4 * k, 58 * k))
    ly = min(cy + 86 * k, h - 12)
    o.append(label(w * 0.17, ly, "NOT WITH INK", CY, 10) + label(w * 0.48, ly, "NOT IN TABLES OF STONE", CY, 10)
             + label(w * 0.81, ly, "IN TABLES THAT ARE HEARTS OF FLESH", GOLD, 10))
    return "".join(o)

def moses_shining(p, w, h, seed):
    """The children of Israel could not look stedfastly upon the face of Moses for the glory of his face: Moses come down
    from the mount with the two tables in his arms, light about his face; the people before him turning their eyes away,
    some bowed to the ground. (The light is the glory on Moses' face; God is not drawn.)"""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#3A2A5A", "#E8A06A"), E4.sinai(w * 0.24, h * 0.6, w * 0.5, h * 0.52, seed, fire=False),
         ground(w, h, h * 0.6, "#8A6A4A", dy=0)]
    s = fit(b, max(h * 0.22, b - 210))
    mx = w * 0.3
    hy = b - 186 * s
    o.append(halo(mx, hy, 90 * s, "#FFFFFF", 0.85) + rays(mx, hy, 22, 22 * s, 120 * s, "#FFF4C2", 0.45, 3))
    tab = (f'<g transform="translate(-34 -120)">' + tablets(0, 0, 0.42) + '</g>')
    o.append(moses_fig(p, mx, b, s, flip=True, up=[(-22, -158), (-40, -136), (-34, -116)], extra=tab))
    o.append(halo(mx + 6 * s, hy, 34 * s, "#FFFFFF", 0.7))
    for i, x in enumerate((0.58, 0.7, 0.82, 0.93)):
        if i % 2 == 0: o.append(brother(p, w * x, b, s * 0.96, [1, 2, 3, 5][i], up=[(-22, -158), (-32, -176), (-22, -190)]))
        else: o.append(E.kneel(w * x, b, s * 0.95, color=["#5A3A22", "#4A3A6A", "#6A5A3A", "#3A4A3A"][i], flip=True))
    return "".join(o)

def moses_veiled(w, h, seed):
    """Moses, who put a veil upon his face … and unto this day, whensoever Moses is read, a veil lieth upon their heart:
    at the left Moses' face veiled (Exodus' face); at the right the reading of the old covenant — the scroll open on the
    reading-desk in a dim synagogue, a veil of cloth lying across it."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2A3A"></rect>']
    uid = f"mv{seed}"
    o.append(f'<defs><radialGradient id="{uid}" cx="0.3" cy="0.4" r="0.6"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.5" stop-color="#C89A6A"></stop>'
             f'<stop offset="1" stop-color="#3A2A3A"></stop></radialGradient></defs><rect x="0" y="0" width="{f(w * 0.46)}" height="{f(h)}" fill="url(#{uid})"></rect>')
    s = min(w * 0.46 / 320, (h + 10) / 380)
    o.append(mk.face(MOSES_VEIL, f(w * 0.23 - 165 * s), f(h - 380 * s + 6), round(s, 3)))
    o.append(f'<path d="M{f(w * 0.46)} 0 L {f(w * 0.46)} {f(h)}" stroke="{INK}" stroke-width="3"></path>')
    # the synagogue: the reading-desk, the scroll open on it, the veil across it, a lamp
    x0 = w * 0.46; cx = x0 + (w - x0) * 0.5; b = h * 0.94
    o.append(f'<rect x="{f(x0)}" y="0" width="{f(w - x0)}" height="{f(h)}" fill="#3A2E2A"></rect>' + lamp_glow(cx + (w - x0) * 0.3, h * 0.3, h * 0.6, f"{uid}l", op=0.4)
             + "".join(f'<rect x="{f(x0 + (w - x0) * t - 12)}" y="{f(h * 0.06)}" width="24" height="{f(b - h * 0.06)}" fill="#5A4A3E" stroke="{INK}" stroke-width="1.6"></rect>' for t in (0.12, 0.88))
             + f'<rect x="{f(x0)}" y="{f(b)}" width="{f(w - x0)}" height="{f(h)}" fill="#2A2018" stroke="{INK}" stroke-width="2"></rect>')
    dw, dh = (w - x0) * 0.44, h * 0.34
    o.append(f'<path d="M{f(cx - dw * 0.3)} {f(b)} L {f(cx - dw * 0.2)} {f(b - dh)} L {f(cx + dw * 0.2)} {f(b - dh)} L {f(cx + dw * 0.3)} {f(b)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(cx - dw * 0.6)} {f(b - dh - 4)} L {f(cx + dw * 0.6)} {f(b - dh - 4)} L {f(cx + dw * 0.5)} {f(b - dh + 8)} L {f(cx - dw * 0.5)} {f(b - dh + 8)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2"></path>')
    sw = dw * 0.9
    o.append(open_letter(cx - sw / 2, b - dh - 4 - sw * 0.34, sw, sw * 0.32, rows=4, seed=seed)
             + f'<ellipse cx="{f(cx - sw / 2)}" cy="{f(b - dh - 4 - sw * 0.18)}" rx="7" ry="{f(sw * 0.18)}" fill="#D8C49A" stroke="{INK}" stroke-width="1.6"></ellipse>'
             + f'<ellipse cx="{f(cx + sw / 2)}" cy="{f(b - dh - 4 - sw * 0.18)}" rx="7" ry="{f(sw * 0.18)}" fill="#D8C49A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    vy = b - dh - 4 - sw * 0.36
    o.append(f'<path d="M{f(cx - sw * 0.56)} {f(vy)} C {f(cx - sw * 0.2)} {f(vy - 10)} {f(cx + sw * 0.2)} {f(vy - 10)} {f(cx + sw * 0.56)} {f(vy)} L {f(cx + sw * 0.6)} {f(vy + sw * 0.44)} '
             f'C {f(cx + sw * 0.3)} {f(vy + sw * 0.38)} {f(cx - sw * 0.3)} {f(vy + sw * 0.5)} {f(cx - sw * 0.6)} {f(vy + sw * 0.42)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2" opacity="0.94"></path>'
             + "".join(f'<path d="M{f(cx + sw * t)} {f(vy)} L {f(cx + sw * t * 1.05)} {f(vy + sw * 0.42)}" stroke="#C8C2B6" stroke-width="1.6"></path>' for t in (-0.3, 0, 0.3)))
    return "".join(o)

def mirror(w, h, seed):
    """We all, with unveiled face beholding as in a mirror the glory of the Lord, are transformed … from glory to glory:
    a hand-mirror of polished bronze lying on a cloth, the light from above caught in it and shining back; beside it a
    veil laid aside. (No face is drawn: the light is the glory.)"""
    uid = f"mr{seed}"
    o = [f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF8DC"></stop><stop offset="0.5" stop-color="#C8904A"></stop>'
         f'<stop offset="1" stop-color="#3A2418"></stop></linearGradient>'
         f'<radialGradient id="{uid}m" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#FFFFFF"></stop><stop offset="0.35" stop-color="#FFE680"></stop><stop offset="1" stop-color="#B8820E"></stop></radialGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>',
         rays(w * 0.5, -h * 0.2, 26, h * 0.2, h * 1.2, "#FFFFFF", 0.22, 6, a0=55, a1=125)]
    ty = h * 0.7
    o.append(f'<path d="M-10 {f(ty)} L {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A2A4A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M-10 {f(ty + 10)} L {f(w + 10)} {f(ty + 10)}" stroke="#E8B830" stroke-width="2"></path>')
    k = min(w / 600, h / 260)
    mx, my, R = w * 0.44, ty - 30 * k, 64 * k
    o.append(halo(mx, my, R * 2.6, "#FFFFFF", 0.7) + rays(mx, my, 20, R * 1.1, R * 3.2, "#FFF4C2", 0.45, 4))
    o.append(f'<path d="M{f(mx + R * 0.7)} {f(my + R * 0.7)} L {f(mx + R * 2.0)} {f(my + R * 1.4)}" stroke="{INK}" stroke-width="{f(18 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(mx + R * 0.7)} {f(my + R * 0.7)} L {f(mx + R * 2.0)} {f(my + R * 1.4)}" stroke="#8A5A1E" stroke-width="{f(12 * k)}" stroke-linecap="round"></path>'
             f'<ellipse cx="{f(mx)}" cy="{f(my)}" rx="{f(R)}" ry="{f(R * 0.62)}" fill="#B8820E" stroke="{INK}" stroke-width="3"></ellipse>'
             f'<ellipse cx="{f(mx)}" cy="{f(my - 2 * k)}" rx="{f(R * 0.84)}" ry="{f(R * 0.5)}" fill="url(#{uid}m)" stroke="#8A5A1E" stroke-width="2"></ellipse>')
    vx = w * 0.7
    o.append(f'<path d="M{f(vx - 70 * k)} {f(ty + 30 * k)} C {f(vx - 40 * k)} {f(ty - 4 * k)} {f(vx + 30 * k)} {f(ty - 8 * k)} {f(vx + 80 * k)} {f(ty + 24 * k)} '
             f'C {f(vx + 60 * k)} {f(ty + 46 * k)} {f(vx - 20 * k)} {f(ty + 52 * k)} {f(vx - 70 * k)} {f(ty + 30 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(vx + t * k)} {f(ty + 2 * k)} C {f(vx + (t + 6) * k)} {f(ty + 20 * k)} {f(vx + (t - 4) * k)} {f(ty + 34 * k)} {f(vx + t * k)} {f(ty + 44 * k)}" fill="none" stroke="#C8C2B6" stroke-width="1.6"></path>' for t in (-34, -6, 22, 48)))
    o.append(plate_label(vx, ty - 22 * k, "THE VEIL IS TAKEN AWAY", "#FFF4C2", 10, halo_="#3A1A2A"))
    return "".join(o)

# ---- 2 Corinthians 4 ------------------------------------------------------------------------------------------------------
def veiled_city(w, h, seed):
    """Even if our gospel is veiled, it is veiled in them that perish … that the light … should not dawn upon them: a town
    under a low, heavy sky at the end of night, every door shut and every window dark, the dawn held back behind the cloud
    on the horizon. (The god of this world is words only.)"""
    hz = h * 0.62
    o = [sky(w, h, "#05050E", "#2A2440"), halo(w * 0.72, hz, max(w, h) * 0.28, "#FFB07A", 0.25)]
    r = random.Random(seed)
    for i in range(5):
        y = h * (0.14 + 0.1 * i); cx = w * r.uniform(0.1, 0.9)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(y)}" rx="{f(w * r.uniform(0.3, 0.5))}" ry="{f(h * 0.07)}" fill="#1A1828" opacity="0.92"></ellipse>')
    o.append(f'<rect x="-10" y="{f(hz - h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#14121E" opacity="0.9"></rect>')
    o.append(hills(w, h, hz, seed, color="#14101A", amp=14, step=80))
    o.append(houses(w, h, h * 0.94, seed, hmin=0.24, hmax=0.4, shut=True, color=("#3A3448", "#2E2A3A", "#342E40", "#3A3444"), stairs=True))
    o.append(ground(w, h, h * 0.94, "#14101A", dy=0))
    return "".join(o)

def first_light(w, h, seed):
    """God, that said, Light shall shine out of darkness, who shined in our hearts: the deep in darkness, and light breaking
    out of it from above, falling on the waters. (Light only.)"""
    hz = h * 0.66
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#05050E"></rect>',
         halo(w * 0.5, h * 0.18, max(w, h) * 0.5, "#FFE680", 0.55), rays(w * 0.5, h * 0.18, 30, h * 0.06, max(w, h) * 0.9, "#FFF4C2", 0.3, 5),
         halo(w * 0.5, h * 0.18, max(w, h) * 0.12, "#FFFFFF", 0.95)]
    o.append(sea_(w, h, hz, seed, color="#0F2A3A", deep="#05101A", foam="#8FB8C8", rough=True))
    o.append(f'<path d="M{f(w * 0.38)} {f(hz)} L {f(w * 0.62)} {f(hz)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#FFE680" opacity="0.28"></path>')
    return "".join(o)

def earthen_vessel(w, h, seed):
    """We have this treasure in earthen vessels: a plain clay jar on a stone ledge in a dark room, light shining from
    within it — out of its mouth and through its cracks."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E1418"></rect>']
    for i in range(int(h / 30) + 2):
        y = i * 30
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A1E22" stroke-width="2"></path>')
        for j in range(int(w / 80) + 2):
            x = j * 80 + (40 if i % 2 else 0)
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + 30)}" stroke="#2A1E22" stroke-width="1.4"></path>')
    ly = h * 0.86
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(ly)}" width="{f(w * 0.6)}" height="{f(h * 0.06)}" fill="#6A5A54" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.22)}" y="{f(ly + h * 0.06)}" width="{f(w * 0.56)}" height="{f(h)}" fill="#4A3E3A" stroke="{INK}" stroke-width="2"></rect>')
    s = min(1.6, (ly - h * 0.1) / 170)
    o.append(jar(w * 0.5, ly, s, f"ev{seed}"))
    return "".join(o)

def four_cells(w, h):
    """We are pressed on every side, yet not straitened; perplexed, yet not unto despair; pursued, yet not forsaken;
    smitten down, yet not destroyed: a plate of four cells, the clay jar in each with the light in it — pressed between
    two great stones, whole; at a fork of three roads in the dark; on a road with the storm behind it, a shaft of light on
    it; knocked over on its side, unbroken, the light spilling out. (The jar alone: no one is drawn.)"""
    o = [plate_bg(w, h, "2 CORINTHIANS 4:8–9 · YET NOT")]
    top, gap = 32, 10
    cw, ch = (w - 3 * gap) / 2, (h - top - 2 * gap) / 2
    cells = [("PRESSED ON EVERY SIDE", "YET NOT STRAITENED"), ("PERPLEXED", "YET NOT UNTO DESPAIR"),
             ("PURSUED", "YET NOT FORSAKEN"), ("SMITTEN DOWN", "YET NOT DESTROYED")]
    for i, (a, bb) in enumerate(cells):
        x, y = gap + (i % 2) * (cw + gap), top + (i // 2) * (ch + gap)
        uid = f"fc{i}"
        o.append(f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}"></rect></clipPath></defs>'
                 f'<g clip-path="url(#{uid})"><rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}" fill="#0B1A2E"></rect>')
        base = y + ch * 0.8; k = min(0.62, (ch * 0.62) / 160); cx = x + cw * 0.5
        o.append(f'<rect x="{f(x)}" y="{f(base)}" width="{f(cw)}" height="{f(ch)}" fill="#1E2A3A"></rect>')
        if i == 0:
            for side in (-1, 1):
                ex = cx + side * 62 * k
                o.append(f'<path d="M{f(ex)} {f(base)} L {f(ex + side * 4 * k)} {f(base - 120 * k)} L {f(ex + side * 60 * k)} {f(base - 140 * k)} L {f(ex + side * 120 * k)} {f(base - 90 * k)} '
                         f'L {f(ex + side * 130 * k)} {f(base)} Z" fill="#5A5A6A" stroke="{CY}" stroke-width="1.6"></path>')
            o.append(jar(cx, base, k * 0.86, f"{uid}j", crack=False))
        elif i == 1:
            for tx in (-0.46, 0.0, 0.46):
                o.append(f'<path d="M{f(cx)} {f(base)} L {f(cx + cw * tx)} {f(y + ch * 0.36)}" stroke="#2C4A6A" stroke-width="{f(12 * k)}" stroke-linecap="round"></path>')
            o.append(jar(cx, base + 6 * k, k * 0.8, f"{uid}j", crack=False))
        elif i == 2:
            o.append(f'<path d="M{f(x)} {f(base)} L {f(x + cw)} {f(base - 8)}" stroke="#2C4A6A" stroke-width="{f(10 * k)}"></path>'
                     + f'<path d="M{f(x)} {f(y)} L {f(x + cw * 0.36)} {f(y)} L {f(x + cw * 0.2)} {f(base)} L {f(x)} {f(base)} Z" fill="#05050E" opacity="0.7"></path>'
                     + bolt(x + cw * 0.12, y, base - ch * 0.2, 5, color=CY, sw=2)
                     + f'<path d="M{f(cx + cw * 0.16 - 18)} {f(y)} L {f(cx + cw * 0.16 + 18)} {f(y)} L {f(cx + 50 * k)} {f(base)} L {f(cx - 50 * k)} {f(base)} Z" fill="#FFF4C2" opacity="0.3"></path>')
            o.append(jar(cx, base, k * 0.8, f"{uid}j", crack=False))
        else:
            o.append(jar(cx - 10 * k, base - 4 * k, k * 0.8, f"{uid}j", lie=True, crack=False))
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}" fill="none" stroke="{CY}" stroke-width="1.4"></rect>'
                 + label(x + 10, y + 17, a, CY, 10, "start") + label(x + 10, y + 32, bb, GOLD, 10, "start") + '</g>')
    return "".join(o)

def preaching(p, w, h, seed):
    """We also believe, and therefore also we speak: Paul standing in a house of the saints with his hand out, speaking,
    the brethren sitting on the floor before him, a lamp on its ledge."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#D8C098", floor="#9A7A52", window=(w * 0.62, min(w * 0.08, h * 0.24)))]
    o.append(clay_lamp(w * 0.86, h * 0.32, min(1.2, h / 260)) + f'<rect x="{f(w * 0.83)}" y="{f(h * 0.32)}" width="{f(w * 0.06)}" height="6" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4"></rect>')
    s = fit(b, max(h * 0.24, b - 220))
    o.append(paul_fig(p, w * 0.2, b, s, flip=True, up=[(-22, -158), (-46, -150), (-70, -160)]))
    for i, x in enumerate((0.4, 0.52, 0.64, 0.76, 0.88)):
        o.append(seated(w * x, b, s * 0.8, ["#4A5A6A", "#6A5A4A", "#3A5A4A", "#5A4A5A", "#8A7A5A"][i], head=["#2A3A4A", "#E8E2D6", "#1F3A5A", "#3A3A4A", None][i],
                        beard=["#2A1A10", "#7A746A", None, "#3A2A1A", "#2A1A10"][i], flip=True))
    return "".join(o)

def seen_unseen(w, h, seed):
    """We look not at the things which are seen, but at the things which are not seen: below, the things seen at dusk — an
    old house falling into ruin, a withered tree, its leaves going down the wind (temporal); above, the heavens opening
    into light and stars (eternal)."""
    sp = h * 0.44
    o = [sky(w, h, "#0B0B2A", "#2A2A6A"), starfield(w, sp, seed, 50, 1.0), halo(w * 0.5, h * 0.06, max(w, h) * 0.36, "#FFF4C2", 0.5),
         rays(w * 0.5, h * 0.04, 24, h * 0.05, max(w, h) * 0.45, "#FFF4C2", 0.25, 4, a0=10, a1=170)]
    o.append(f'<rect x="-10" y="{f(sp)}" width="{f(w + 20)}" height="{f(h - sp + 10)}" fill="#C8784A"></rect>' + halo(w * 0.86, sp + h * 0.1, h * 0.12, "#FF8A3D", 0.5)
             + hills(w, h, sp + h * 0.16, seed, color="#6A3A30", amp=10, step=70) + ground(w, h, sp + h * 0.24, "#5A3A2A", dy=0))
    o.append(f'<path d="M-10 {f(sp)} L {f(w + 10)} {f(sp)}" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="8 6"></path>')
    b = h * 0.96
    o.append(ruin(w * 0.06, w * 0.5, b, h * 0.34, seed, color="#9A8060"))
    tx = w * 0.72
    o.append(f'<path d="M{f(tx)} {f(b)} L {f(tx + 4)} {f(b - h * 0.22)} M{f(tx + 2)} {f(b - h * 0.14)} L {f(tx - 30)} {f(b - h * 0.26)} M{f(tx + 3)} {f(b - h * 0.18)} L {f(tx + 34)} {f(b - h * 0.3)} '
             f'M{f(tx + 4)} {f(b - h * 0.22)} L {f(tx + 10)} {f(b - h * 0.34)}" stroke="#3A2418" stroke-width="{f(max(3, h * 0.014))}" stroke-linecap="round" fill="none"></path>')
    r = random.Random(seed)
    for _ in range(8):
        x, y = w * r.uniform(0.6, 0.98), h * r.uniform(0.62, 0.92)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="5" ry="2.4" fill="#A8582A" stroke="{INK}" stroke-width="0.8" transform="rotate({r.randint(0, 180)} {f(x)} {f(y)})"></ellipse>')
    o.append(plate_label(w * 0.5, h * 0.44, "THE THINGS WHICH ARE NOT SEEN · ETERNAL", GOLD, 10.5, halo_="#0B0B2A")
             + plate_label(w * 0.24, sp + 18, "THE THINGS WHICH ARE SEEN · TEMPORAL", "#FFF4C2", 10, halo_="#5A2A1A"))
    return "".join(o)

# ---- 2 Corinthians 5 ------------------------------------------------------------------------------------------------------
def tent_house(w, h):
    """If the earthly house of our tabernacle be dissolved, we have a building from God, a house not made with hands,
    eternal, in the heavens: a plate — below, a tent being struck, its poles leaning, the cloth sagging, the pegs pulled up;
    above, among the clouds, a house drawn in lines of light."""
    o = [plate_bg(w, h, "2 CORINTHIANS 5:1 · NOT MADE WITH HANDS")]
    k = min(w / 520, (h - 40) / 190)
    gy = h - 34; tx = w * 0.25
    o.append(f'<path d="M14 {f(gy)} L {f(w - 14)} {f(gy)}" stroke="#2C5A7A" stroke-width="2"></path>')
    o.append(f'<path d="M{f(tx - 90 * k)} {f(gy)} L {f(tx - 40 * k)} {f(gy - 62 * k)} L {f(tx + 30 * k)} {f(gy - 50 * k)} L {f(tx + 96 * k)} {f(gy)} '
             f'C {f(tx + 60 * k)} {f(gy - 14 * k)} {f(tx - 40 * k)} {f(gy - 8 * k)} {f(tx - 90 * k)} {f(gy)} Z" fill="#3A3028" stroke="{CY}" stroke-width="1.8"></path>'
             f'<path d="M{f(tx - 44 * k)} {f(gy)} L {f(tx - 36 * k)} {f(gy - 70 * k)} M{f(tx + 40 * k)} {f(gy)} L {f(tx + 22 * k)} {f(gy - 58 * k)}" stroke="#C8A060" stroke-width="{f(4 * k)}"></path>'
             + "".join(f'<path d="M{f(tx + dx * k)} {f(gy - 2)} l {f(6 * k)} {f(-18 * k)}" stroke="#C8A060" stroke-width="{f(3 * k)}"></path>' for dx in (-120, -104, 118, 134)))
    o.append(label(tx, gy + 20, "THE EARTHLY HOUSE OF OUR TABERNACLE · DISSOLVED", CY, 9.5))
    hx, hy = w * 0.72, 44 + 112 * k
    o.append(halo(hx, hy - 50 * k, 130 * k, "#FFF4C2", 0.5)
             + "".join(f'<ellipse cx="{f(hx + dx * k)}" cy="{f(hy + dy * k)}" rx="{f(rx * k)}" ry="{f(12 * k)}" fill="#E8E2D6" opacity="0.3"></ellipse>'
                       for dx, dy, rx in ((-90, 6, 70), (40, 10, 90), (110, 0, 50))))
    hw = 150 * k
    o.append(f'<g fill="none" stroke="#FFE680" stroke-width="2.2">'
             f'<path d="M{f(hx - hw * 0.6)} {f(hy - 70 * k)} L {f(hx)} {f(hy - 112 * k)} L {f(hx + hw * 0.6)} {f(hy - 70 * k)} Z"></path>'
             f'<path d="M{f(hx - hw * 0.56)} {f(hy - 66 * k)} L {f(hx + hw * 0.56)} {f(hy - 66 * k)} M{f(hx - hw * 0.6)} {f(hy)} L {f(hx + hw * 0.6)} {f(hy)}"></path>'
             + "".join(f'<path d="M{f(hx + hw * t)} {f(hy - 64 * k)} L {f(hx + hw * t)} {f(hy - 2 * k)}"></path>' for t in (-0.48, -0.28, -0.08, 0.12, 0.32, 0.52))
             + '</g>')
    o.append(label(hx, hy + 24, "A BUILDING FROM GOD · ETERNAL, IN THE HEAVENS", GOLD, 9.5))
    return "".join(o)

def bema_light(w, h, seed):
    """We must all be made manifest before the judgment-seat of Christ: a raised judgment-seat of white stone on its steps,
    the seat upon it empty, in a great light. (No one is drawn on it.)"""
    o = [sky(w, h, "#1A1440", "#C8803A"), radiance(w, h, seed, cy=0.5)]
    b = h * 0.96; bx = w * 0.5; bw = min(w * 0.5, h * 1.2)
    for i in range(4):
        sw_ = bw * (1 - i * 0.14); y = b - (i + 1) * h * 0.07
        o.append(f'<rect x="{f(bx - sw_ / 2)}" y="{f(y)}" width="{f(sw_)}" height="{f(h * 0.07)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    top = b - 4 * h * 0.07; k = min(1.4, h / 260)
    o.append(f'<path d="M{f(bx - 40 * k)} {f(top)} L {f(bx - 30 * k)} {f(top - 70 * k)} L {f(bx + 30 * k)} {f(top - 70 * k)} L {f(bx + 40 * k)} {f(top)} '
             f'M{f(bx - 40 * k)} {f(top - 70 * k)} L {f(bx + 40 * k)} {f(top)} M{f(bx + 40 * k)} {f(top - 70 * k)} L {f(bx - 40 * k)} {f(top)}" stroke="#B8860E" stroke-width="{f(6 * k)}" fill="none"></path>'
             f'<rect x="{f(bx - 34 * k)}" y="{f(top - 76 * k)}" width="{f(68 * k)}" height="{f(10 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def new_creature(w, h, seed):
    """If any man is in Christ, he is a new creature: the old things are passed away; behold, they are become new: dawn
    over the hills in spring, an almond tree in white blossom, green shoots coming up through the old ground."""
    hz = h * 0.6
    o = [vista(w, h, seed, tone="dawn", horizon=0.6, hills_n=2, glow_at=(0.62, 0.6, 0.6, "#FFF4C2"), sun_at=(0.62, 0.58), birds_=4, ground_=False),
         ground(w, h, hz + h * 0.04, "#6A8A3A", dy=0)]
    r = random.Random(seed)
    for _ in range(40):
        x, y = w * r.uniform(0, 1), h * r.uniform(0.7, 0.98); s = h * r.uniform(0.02, 0.04)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - s * 0.4)} {f(y - s * 0.6)} {f(x - s * 0.3)} {f(y - s)} {f(x - s * 0.6)} {f(y - s * 1.3)} M{f(x)} {f(y)} C {f(x + s * 0.3)} {f(y - s * 0.6)} {f(x + s * 0.5)} {f(y - s)} {f(x + s * 0.7)} {f(y - s * 1.2)}" '
                 f'stroke="#9CCB5E" stroke-width="2" fill="none"></path>')
    tx, b = w * 0.24, h * 0.96; k = min(1.3, h / 260)
    o.append(f'<path d="M{f(tx)} {f(b)} C {f(tx - 6 * k)} {f(b - 60 * k)} {f(tx + 6 * k)} {f(b - 90 * k)} {f(tx)} {f(b - 120 * k)} M{f(tx)} {f(b - 80 * k)} L {f(tx - 50 * k)} {f(b - 140 * k)} '
             f'M{f(tx)} {f(b - 100 * k)} L {f(tx + 54 * k)} {f(b - 150 * k)} M{f(tx)} {f(b - 120 * k)} L {f(tx + 4 * k)} {f(b - 170 * k)}" stroke="#3A2418" stroke-width="{f(7 * k)}" stroke-linecap="round" fill="none"></path>')
    for _ in range(90):
        a = r.uniform(0, math.tau); d = r.uniform(0, 1) ** 0.5
        x, y = tx + math.cos(a) * 80 * k * d, b - 145 * k + math.sin(a) * 50 * k * d
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(4.2 * k)}" fill="{r.choice(["#FFFFFF", "#FCE8EC", "#F8D8E0"])}" stroke="#C8A0A8" stroke-width="0.8"></circle>')
    return "".join(o)

def ambassador(w, h):
    """We are ambassadors therefore on behalf of Christ, as though God were entreating by us: a plate — the envoy's
    credentials, the letter rolled and sealed with the king's seal, the signet beside it; and the word of reconciliation."""
    import exo.art8 as B
    o = [plate_bg(w, h, "2 CORINTHIANS 5:20 · AMBASSADORS ON BEHALF OF CHRIST")]
    k = min(w / 560, (h - 40) / 220); cy = h * 0.56
    o.append(halo(w * 0.42, cy, 140 * k, "#FFE680", 0.3))
    o.append(sealed_scroll(w * 0.42, cy, 2.1 * k, rot=-4) + signet(w * 0.72, cy + 10 * k, 1.2 * k, rot=-20))
    B._W[0] = w
    o.append(tag(w * 0.42, cy + 16 * k, "THE SEAL", w * 0.18, cy + 70 * k, color=CY) + tag(w * 0.72, cy - 10 * k, "THE SIGNET", w * 0.86, cy - 70 * k, color=CY))
    o.append(label(w * 0.5, min(cy + 104 * k, h - 12), "THE WORD OF RECONCILIATION", GOLD, 10.5))
    return "".join(o)

# ---- the cover ------------------------------------------------------------------------------------------------------------
def corinth_dusk(w, h, seed):
    """Corinth at dusk: the great rock of the citadel with its temple against the evening sky, the city's walls and flat
    roofs below it, lamps coming on in the windows."""
    hz = h * 0.7
    o = [sky(w, h, "#1E1430", "#E8803A"), starfield(w, h * 0.4, seed, 30, 1.0), sun(w * 0.18, hz - h * 0.08, max(16, h * 0.04), color="#FF8A3D", op=0.35),
         hills(w, h, hz - h * 0.04, seed, color="#4A2A3A", amp=14, step=90)]
    o.append(f'<path d="M{f(w * 0.22)} {f(hz + 6)} L {f(w * 0.36)} {f(h * 0.34)} L {f(w * 0.46)} {f(h * 0.24)} L {f(w * 0.58)} {f(h * 0.2)} L {f(w * 0.7)} {f(h * 0.26)} '
             f'L {f(w * 0.82)} {f(h * 0.4)} L {f(w * 0.98)} {f(hz + 6)} Z" fill="#5A3A44" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.36)} {f(h * 0.34)} L {f(w * 0.44)} {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.5)} M{f(w * 0.7)} {f(h * 0.26)} L {f(w * 0.66)} {f(h * 0.4)} L {f(w * 0.7)} {f(h * 0.54)}" '
             f'stroke="#3A2430" stroke-width="2" fill="none"></path>')
    tx, ty, tw = w * 0.58, h * 0.2, w * 0.14
    o.append(f'<path d="M{f(tx - tw / 2 - 6)} {f(ty)} L {f(tx)} {f(ty - tw * 0.28)} L {f(tx + tw / 2 + 6)} {f(ty)} Z" fill="#C8B8A0" stroke="{INK}" stroke-width="1.8"></path>'
             f'<rect x="{f(tx - tw / 2)}" y="{f(ty)}" width="{f(tw)}" height="{f(tw * 0.08)}" fill="#B8A890" stroke="{INK}" stroke-width="1.4"></rect>'
             + "".join(f'<rect x="{f(tx - tw / 2 + tw * j / 6 - 3)}" y="{f(ty + tw * 0.08)}" width="6" height="{f(tw * 0.34)}" fill="#D8C8B0" stroke="{INK}" stroke-width="1"></rect>' for j in range(1, 6)))
    o.append(walls(w * 0.02, w * 0.98, hz + h * 0.06, h * 0.2, seed, color="#8A6A5A", lit=True, gate=True, towers=4))
    o.append(houses(w, h, h * 0.98, seed, hmin=0.12, hmax=0.2, lit=True, color=("#6A5060", "#5A4456", "#72586A", "#5E4A5C"), stairs=True))
    return "".join(o)
