"""Drawings for the James volume, and the cast of the general letters that are not Paul's. James starts from all of
Galatians' drawings (`from gal.art import *`, which carries Acts', Mark's and Matthew's drawings and the epistle kit: the
study, robed(), the sealed scroll, the plate ground) and adds its own; 1 Peter, 2 Peter and Jude start from these
(`from jas.art import *`).

The writers at a distance, on the kit silhouettes (epistle.robed), each the same in every volume (their faces are in
jas.common):
    james_fig    James the Lord's brother: a stone-grey robe, the white headcloth with a cord, a grey beard, a grey mantle
    peter_fig    Peter old: ntcast's brown robe, bareheaded, grey hair and beard, a darker mantle
    jude_fig     Jude, brother of James: a grey-olive robe, a dark slate headcloth with a cord, a grey-brown beard
    silvanus_fig Silvanus (Acts' Silas): a blue robe and headcloth with a cord, a black beard
    mark_r       Mark: an olive-khaki robe, bareheaded, dark-brown hair and a short beard
Paul is never drawn in these letters. God is never drawn (light); angels are figures of white light with a gold rim and
no face (gal.art.light_fig); Satan and demons are never drawn. Every function takes (p, w, h, seed, ...) or (w, h, ...);
p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from gal.art import *
from gal.art import art, plate_label, light_fig, _defs
from act.art import f, INK, _synagogue, _street, _road
from epistle import (study, still_life, sealed_scroll, open_letter, reed_pen, inkpot, lamp_glow, letter_road, plate_bg, radiance, tag, dim, robed,
                     scribe_seated, mat as floor_mat, low_table, stool, bench, doorway, SEPIA, SEAL)
from oba.minor import vista, halo, rays, starfield, walls, olive, fig_tree, vines, grain, sea as sea_, cup
from genesis.art2 import fit, ground, hills, SKIN, bird
from genesis.art3 import label, sun
from genesis.art4 import clay_lamp
from sa2.art import sky
from mat.art import room, temple, houses
from job.art import clouds, smoke
from jas.common import JAMES_LOOK, PETER_LOOK, JUDE_LOOK, SILVANUS_LOOK, MARK_LOOK
import mk, exodus as E
from num.art import ALL
from act import geo

GOLD, CY = "#FFD23F", "#8FD0E2"
UP_HEAVEN = [(-22, -158), (-34, -196), (-40, -232)]          # an arm lifted to heaven (reaching left as drawn)
UP_OUT = [(-22, -158), (-48, -150), (-72, -156)]              # an arm held out, speaking
UP_GIVE = [(-22, -158), (-42, -140), (-64, -132)]             # an arm reaching down and forward, giving

def D_(p): return mk.defs(p, *ALL, "ManUp", "WomanUp")

# ---- the writers and the people at a distance ----------------------------------------------------------------------------
def james_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    L = JAMES_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], belt="#6A5A3A", flip=flip, up=up,
                 extra=extra, pose=pose, seat=seat)
def peter_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    L = PETER_LOOK
    return robed(p, x, y, s, L["cloth"], hair=L["hair"], beard=L["beard"], mantle=L["mantle"], belt=L["belt"], flip=flip, up=up, extra=extra, pose=pose, seat=seat)
def jude_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    L = JUDE_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], belt="#2A2A2A", flip=flip, up=up,
                 extra=extra, pose=pose, seat=seat)
def silvanus_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    L = SILVANUS_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle="#1F3550", flip=flip, up=up, extra=extra, pose=pose, seat=seat)
def mark_r(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    L = MARK_LOOK
    return robed(p, x, y, s, L["cloth"], hair=L["hair"], beard=L["beard"], mantle=L["mantle"], belt="#4A3A1A", flip=flip, up=up, extra=extra, pose=pose, seat=seat)

ELDERS = [("#4A4A5A", "#E8E2D6", "#8A847A"), ("#5A4A3A", "#2A3A4A", "#3A2A1A"), ("#3A4A3A", "#D8D0C0", "#C8C2B6"), ("#5A3A3A", "#1F2F3A", "#6A645E")]
def elder_r(p, x, y, s, i=0, flip=False, up=None, extra="", pose="stand"):
    """An elder of the church (Jas 5:14, Acts 15): a plain robe, a cool or off-white headcloth, a beard."""
    c, hd, bd = ELDERS[i % 4]
    return robed(p, x, y, s, c, head=hd, cord="#2A1A10", beard=bd, flip=flip, up=up, extra=extra, pose=pose)
FOLK = [("#6A5A4A", None, "#2A1A10", "#2A1A10"), ("#4A5A6A", "#2A3A4A", None, "#3A2A1A"), ("#7A6A52", "#3A4A3A", None, "#5A4A3A"), ("#5A4A5A", None, "#1A1210", None)]
def man_r(p, x, y, s, i=0, flip=False, up=None, extra="", pose="stand", cloth=None, mantle=None):
    """A man of the people: a plain robe, bareheaded or a cool headcloth."""
    c, hd, hr, bd = FOLK[i % 4]
    return robed(p, x, y, s, cloth or c, head=hd, hair=None if hd else hr, beard=bd, mantle=mantle, flip=flip, up=up, extra=extra, pose=pose)
WOMEN = [("#5A6A8A", "#2A3A5A"), ("#6A5A6A", "#2A2A3A"), ("#7A6A5A", "#E8E2D6"), ("#4A6A6A", "#1F3A3A")]
def woman_r(p, x, y, s, i=0, flip=False, up=None, extra="", pose="stand"):
    c, vl = WOMEN[i % 4]
    return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, flip=flip, up=up, extra=extra, pose=pose)
def abraham_r(p, x, y, s, flip=False, up=None, extra=""):
    """Abraham in his old age (Genesis 22): a white robe, grey hair and beard (Genesis' look)."""
    return robed(p, x, y, s, "#E8E2D6", hair="#A8A296", beard="#B8B2A6", mantle="#B8B4C8", belt="#5A6A8A", flip=flip, up=up, extra=extra)
def angel_r(p, x, y, s, flip=False, up=None, extra="", glow=True):
    """An angel: a figure of white light with a gold rim and no face (the kit silhouette in white, outlined in gold, a soft
    light about it); no wings unless the text gives them."""
    return ((halo(x, y - 110 * s, 130 * s, "#FFF4C2", 0.4) if glow else "")
            + robed(p, x, y, s, "#FFFFFF", skin="#FFFDF0", line="#E8B830", flip=flip, up=up, extra=extra))
def isaac_r(p, x, y, s, flip=False, up=None, extra=""):
    """Isaac a lad (Genesis' look: brown curls, a plain tunic)."""
    return robed(p, x, y, s, "#C8A060", hair="#5A3A22", belt="#6A4A2A", flip=flip, up=up, extra=extra)

# ---- the study at Jerusalem ------------------------------------------------------------------------------------------------
JSCRIBE = dict(cloth="#5A6A72", head="#E8E2D6", cord="#5A4A3A")                 # a young scribe of the church at Jerusalem

def jerusalem_window(x, y, ww, hh, night, seed):
    """A window on Jerusalem: the city's roofs, and on its hill the house of God with its gold (mat.art.temple)."""
    sky_ = ("#0B0B2A", "#2A2050") if night else ("#8FD0E2", "#F3E8C8")
    uid = f"jw{seed}"
    o = [f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}"></rect></clipPath>'
         f'<linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky_[0]}"></stop><stop offset="1" stop-color="{sky_[1]}"></stop></linearGradient></defs>',
         f'<g clip-path="url(#{uid})"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="url(#{uid}g)"></rect>']
    if night: o.append(f'<g transform="translate({f(x)} {f(y)})">' + mk.stars(int(ww * hh / 900) + 6, ww, hh * 0.4, seed) + '</g>')
    o.append(f'<path d="M{f(x - 4)} {f(y + hh * 0.74)} C {f(x + ww * 0.3)} {f(y + hh * 0.56)} {f(x + ww * 0.7)} {f(y + hh * 0.54)} {f(x + ww + 4)} {f(y + hh * 0.66)} '
             f'L {f(x + ww + 4)} {f(y + hh + 4)} L {f(x - 4)} {f(y + hh + 4)} Z" fill="{"#2A2440" if night else "#9A8A6A"}" stroke="{INK}" stroke-width="1.4"></path>')
    t = temple(x + ww * 0.52, y + hh * 0.64, ww * 0.62, lit=night)
    o.append(t)
    r = random.Random(seed); xx = x - 6
    while xx < x + ww:
        bw = ww * r.uniform(0.16, 0.26); bh = hh * r.uniform(0.12, 0.22)
        o.append(f'<rect x="{f(xx)}" y="{f(y + hh - bh)}" width="{f(bw)}" height="{f(bh + 4)}" fill="{"#3A3050" if night else "#E8D8B0"}" stroke="{INK}" stroke-width="1.2"></rect>')
        if night and r.random() < 0.6: o.append(f'<rect x="{f(xx + bw * 0.4)}" y="{f(y + hh - bh * 0.7)}" width="{f(bw * 0.18)}" height="{f(bh * 0.26)}" fill="#FFC14D"></rect>')
        xx += bw
    o.append('</g>' + f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(x + ww / 2)} {f(y)} L {f(x + ww / 2)} {f(y + hh)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<rect x="{f(x - 8)}" y="{f(y + hh)}" width="{f(ww + 16)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def _elder_fig(i):
    return lambda p, x, y, s, flip=False, up=None, extra="": elder_r(p, x, y, s, i, flip=flip, up=up, extra=extra)

def study_james(p, w, h, seed, stage="dictate", fig_h=None, elders=2):
    """James writing to the twelve tribes: the study at Jerusalem by lamplight (epistle.study), James standing, his hand
    out, a young scribe of the church writing on his mat, the temple through the window, elders of the church listening."""
    return study(p, w, h, seed, stage=stage, scribe=JSCRIBE, writer=james_fig, window=jerusalem_window, fig_h=fig_h,
                 others=tuple(_elder_fig(i) for i in range(elders)))

# ---- James 1 ----------------------------------------------------------------------------------------------------------------
BABYLON = (44.42, 32.54)
def dispersion(w, h):
    """To the twelve tribes which are of the Dispersion: Acts' map from Italy to Babylon, rings spreading out from
    Jerusalem, the lands where the Jews were scattered (Acts 2:9–11) named."""
    return geo.med_map(w, h, box=(12.0, 48.0, 28.0, 43.5), places=("JERUSALEM", "ROME", "ALEXANDRIA", "ANTIOCH", "CYRENE", "EPHESUS", "CORINTH", "DAMASCUS", "TARSUS"),
                       hi=("JERUSALEM",), regions=("ITALY", "ACHAIA", "ASIA", "PONTUS", "CAPPADOCIA", "EGYPT", "LIBYA", "MESOPOTAMIA", "MEDIA", "ARABIA", "SYRIA"),
                       title="JAMES 1:1 · THE TWELVE TRIBES WHICH ARE OF THE DISPERSION", rings="JERUSALEM")

def surge(w, h, seed):
    """He that doubteth is like the surge of the sea driven by the wind and tossed: a storm sky, wind streaks, and the
    great waves heaving and breaking, the spray torn from their crests."""
    r = random.Random(seed)
    o = [sky(w, h, "#141826", "#4A5A6E"), clouds(w, h * 0.12, seed, n=7, color="#2A3040", op=0.9, ry=0.07, h=h)]
    for i in range(9):                                             # the wind
        y = h * r.uniform(0.08, 0.5); x = w * r.uniform(-0.1, 0.7); L = w * r.uniform(0.2, 0.4)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + L * 0.4)} {f(y - 6)} {f(x + L * 0.7)} {f(y + 4)} {f(x + L)} {f(y - 2)}" fill="none" stroke="#C8D8E8" stroke-width="2" opacity="0.5" stroke-linecap="round"></path>')
    for k, (y0, col, amp) in enumerate(((0.5, "#1F4A6A", 0.08), (0.64, "#1F6F9A", 0.12), (0.8, "#0F4C68", 0.16))):
        yb = h * y0; A = h * amp; n = 3 + k
        d = f"M-20 {f(h + 10)} L -20 {f(yb)}"
        for j in range(n):
            x0 = -20 + (w + 40) * j / n; x1 = -20 + (w + 40) * (j + 1) / n; cx = x0 + (x1 - x0) * 0.62
            d += (f" C {f(x0 + (x1 - x0) * 0.3)} {f(yb - A * 0.2)} {f(cx - (x1 - x0) * 0.12)} {f(yb - A)} {f(cx)} {f(yb - A)}"
                  f" C {f(cx + (x1 - x0) * 0.1)} {f(yb - A * 0.9)} {f(cx + (x1 - x0) * 0.06)} {f(yb - A * 0.5)} {f(x1)} {f(yb)}")
        o.append(f'<path d="{d} L {f(w + 20)} {f(h + 10)} Z" fill="{col}" stroke="{INK}" stroke-width="2"></path>')
        for j in range(n):                                         # the foam on each crest, blown off to the right
            x0 = -20 + (w + 40) * j / n; x1 = -20 + (w + 40) * (j + 1) / n; cx = x0 + (x1 - x0) * 0.62
            o.append(f'<path d="M{f(cx - (x1 - x0) * 0.1)} {f(yb - A * 0.85)} C {f(cx)} {f(yb - A * 1.08)} {f(cx + (x1 - x0) * 0.1)} {f(yb - A * 0.9)} {f(cx + (x1 - x0) * 0.08)} {f(yb - A * 0.55)}" '
                     f'fill="none" stroke="#E8F6FA" stroke-width="{f(3 + k)}" stroke-linecap="round"></path>')
            for q in range(5):
                o.append(f'<circle cx="{f(cx + (x1 - x0) * r.uniform(0.04, 0.3))}" cy="{f(yb - A * r.uniform(0.9, 1.4))}" r="{f(r.uniform(1.4, 3.2))}" fill="#E8F6FA" opacity="0.8"></circle>')
    o.append(plate_label(w * 0.5, h * 0.1, "THE SURGE OF THE SEA · DRIVEN BY THE WIND AND TOSSED", "#E8F6FA", 10, halo_="#141826"))
    return "".join(o)

def withering(w, h, seed):
    """The flower of the grass: at the left the grass green and the wild flowers open in the morning; at the right the
    sun risen with the scorching wind, the grass withered and the flowers fallen."""
    r = random.Random(seed)
    hz = h * 0.42
    o = [f'<defs><linearGradient id="wg{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9AD0E8"></stop><stop offset="0.45" stop-color="#F3E8C8"></stop>'
         f'<stop offset="1" stop-color="#FF9A3D"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#wg{seed})"></rect>',
         halo(w * 0.86, h * 0.2, h * 0.5, "#FFE680", 0.6), f'<circle cx="{f(w * 0.86)}" cy="{f(h * 0.2)}" r="{f(max(14, h * 0.09))}" fill="#FFF4C2" stroke="#FF8A3D" stroke-width="3"></circle>',
         rays(w * 0.86, h * 0.2, 20, h * 0.12, h * 0.5, "#FFC14D", 0.4, 3)]
    for i in range(6):                                              # the scorching wind
        y = h * r.uniform(0.18, 0.4); x = w * r.uniform(0.5, 0.8)
        o.append(f'<path d="M{f(x)} {f(y)} c {f(-w * 0.06)} -6 {f(-w * 0.1)} 6 {f(-w * 0.16)} 0" fill="none" stroke="#C8501A" stroke-width="2.4" opacity="0.6" stroke-linecap="round"></path>')
    o.append(f'<defs><linearGradient id="wf{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6A9A3A"></stop><stop offset="0.45" stop-color="#9AAA4A"></stop>'
             f'<stop offset="0.6" stop-color="#C8A050"></stop><stop offset="1" stop-color="#A87A3A"></stop></linearGradient></defs>'
             f'<path d="M-10 {f(hz)} L {f(w + 10)} {f(hz)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="url(#wf{seed})" stroke="{INK}" stroke-width="2"></path>')
    for i in range(int(w / 7)):
        x = r.uniform(-5, w + 5); y = r.uniform(hz + 6, h + 4); t = x / w
        L = r.uniform(18, 36) * (h / 260); dry = t > 0.55
        lean = r.uniform(-4, 4) + (14 if dry else 0)
        col = "#3A7A2A" if t < 0.45 else ("#7A8A3A" if t < 0.58 else "#8A6A2A")
        o.append(f'<path d="M{f(x)} {f(y)} q {f(lean * 0.3)} {f(-L * 0.6)} {f(lean)} {f(-L if not dry else -L * 0.7)}" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round"></path>')
    for i in range(16):                                             # the flowers: open at the left, fallen at the right
        t = (i + r.random()) / 16; x = w * t; y = r.uniform(hz + 20, h * 0.92)
        if t < 0.5:
            c = r.choice(("#D7261E", "#E8B830", "#C2456A", "#F3EFE6"))
            o.append(f'<path d="M{f(x)} {f(y + 22)} L {f(x)} {f(y)}" stroke="#3A7A2A" stroke-width="2"></path>'
                     + "".join(f'<circle cx="{f(x + 5 * math.cos(a))}" cy="{f(y + 5 * math.sin(a))}" r="3.6" fill="{c}" stroke="{INK}" stroke-width="0.8"></circle>' for a in (0, 1.26, 2.51, 3.77, 5.03))
                     + f'<circle cx="{f(x)}" cy="{f(y)}" r="2.4" fill="#E8B830"></circle>')
        else:
            o.append(f'<path d="M{f(x)} {f(y + 20)} q 6 -8 14 -6" stroke="#8A6A2A" stroke-width="2" fill="none"></path>'
                     + "".join(f'<ellipse cx="{f(x + 18 + k * 6)}" cy="{f(y + 22 + (k % 2) * 3)}" rx="3" ry="1.6" fill="#8A4A2A" opacity="0.8"></ellipse>' for k in range(3)))
    o.append(plate_label(w * 0.22, h * 0.12, "THE FLOWER OF THE GRASS", "#2A4A2A", 10, halo_="#E8F2E8")
             + plate_label(w * 0.6, h * 0.12, "THE SCORCHING WIND", "#7A2A0A", 10, halo_="#FFE6C0"))
    return "".join(o)

def crown_of_life(w, h, seed):
    """The crown of life, which the Lord promised to them that love him: a victor's wreath of gold leaves on a stone
    under a falling light, the field of the contest dark around it."""
    r = random.Random(seed)
    cx, cy = w * 0.5, h * 0.52
    R = min(w * 0.18, h * 0.3)
    o = [sky(w, h, "#140E2A", "#3A2A50"), starfield(w, h, seed, 40, 0.6), halo(cx, cy, R * 2.6, "#FFE680", 0.45),
         rays(cx, -20, 14, 10, h * 1.2, "#FFF4C2", 0.18, 6, 60, 120)]
    o.append(f'<path d="M{f(cx - R * 1.3)} {f(h + 10)} L {f(cx - R * 1.1)} {f(cy + R * 0.7)} L {f(cx + R * 1.1)} {f(cy + R * 0.7)} L {f(cx + R * 1.3)} {f(h + 10)} Z" fill="#5A5060" stroke="{INK}" stroke-width="2.4"></path>')
    for side in (-1, 1):                                           # the wreath: two branches of leaves meeting at the top
        for k in range(11):
            a = math.radians(100 + side * (k * 15 + 8)) if side < 0 else math.radians(80 - (k * 15 + 8))
            a = math.radians(90 + side * (12 + k * 14.5))
            x, y = cx + R * math.cos(a), cy - R * 0.62 * math.sin(a)
            rot = math.degrees(a) + (90 if side > 0 else -90)
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(R * 0.16)}" ry="{f(R * 0.07)}" transform="rotate({f(-rot + 180)} {f(x)} {f(y)})" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(R)}" ry="{f(R * 0.62)}" fill="none" stroke="#A87A1A" stroke-width="{f(max(2, R * 0.05))}"></ellipse>')
    o.append(f'<path d="M{f(cx - 8)} {f(cy + R * 0.62)} l -10 {f(R * 0.3)} M{f(cx + 8)} {f(cy + R * 0.62)} l 10 {f(R * 0.3)}" stroke="#D7261E" stroke-width="4" stroke-linecap="round"></path>')
    o.append(plate_label(cx, h * 0.12, "THE CROWN OF LIFE", GOLD, 12, halo_="#140E2A"))
    return "".join(o)

def father_of_lights(w, h, seed):
    """Every good gift and every perfect gift is from above, coming down from the Father of lights: the lights of heaven
    (the sun, the moon, the stars) and from above them a light falling straight down on a sheaf of firstfruits standing in
    the field, which casts no shadow (1:17–18). No figure: God is never drawn."""
    cx = w * 0.5
    o = [sky(w, h, "#0B0B2A", "#3A3A7A"), starfield(w, h, seed, 70, 0.5),
         f'<circle cx="{f(w * 0.14)}" cy="{f(h * 0.2)}" r="{f(max(10, h * 0.05))}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.6"></circle>'
         f'<circle cx="{f(w * 0.14 + h * 0.02)}" cy="{f(h * 0.19)}" r="{f(max(10, h * 0.05))}" fill="#0B0B2A"></circle>',
         halo(w * 0.86, h * 0.22, h * 0.2, "#FFC14D", 0.6), f'<circle cx="{f(w * 0.86)}" cy="{f(h * 0.22)}" r="{f(max(12, h * 0.06))}" fill="#FFD23F" stroke="#FF8A3D" stroke-width="2"></circle>',
         f'<defs><linearGradient id="fl{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"></stop><stop offset="1" stop-color="#FFE680" stop-opacity="0.35"></stop></linearGradient></defs>',
         f'<path d="M{f(cx - w * 0.04)} -10 L {f(cx + w * 0.04)} -10 L {f(cx + w * 0.12)} {f(h * 0.86)} L {f(cx - w * 0.12)} {f(h * 0.86)} Z" fill="url(#fl{seed})"></path>',
         halo(cx, -10, h * 0.4, "#FFFFFF", 0.8),
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A4A2A" stroke="{INK}" stroke-width="2"></path>',
         grain(-10, w * 0.38, h * 0.86, h * 0.1, seed, color="#8A8A3A"), grain(w * 0.62, w + 10, h * 0.86, h * 0.1, seed + 1, color="#8A8A3A"),
         halo(cx, h * 0.8, h * 0.18, "#FFE680", 0.7)]
    k = h / 300                                                     # the sheaf of firstfruits, bound, standing upright
    sx, sy = cx, h * 0.88
    for i in range(-6, 7):
        o.append(f'<path d="M{f(sx + i * 2 * k)} {f(sy)} C {f(sx + i * 2.4 * k)} {f(sy - 30 * k)} {f(sx + i * 1.2 * k)} {f(sy - 50 * k)} {f(sx + i * 3.6 * k)} {f(sy - 80 * k)}" fill="none" stroke="#C8A040" stroke-width="{f(2.4 * k)}"></path>'
                 f'<ellipse cx="{f(sx + i * 3.6 * k)}" cy="{f(sy - 86 * k)}" rx="{f(2.6 * k)}" ry="{f(7 * k)}" fill="#E8C060" stroke="{INK}" stroke-width="1" transform="rotate({i * 5} {f(sx + i * 3.6 * k)} {f(sy - 86 * k)})"></ellipse>')
    o.append(f'<path d="M{f(sx - 12 * k)} {f(sy - 40 * k)} C {f(sx - 4 * k)} {f(sy - 36 * k)} {f(sx + 4 * k)} {f(sy - 36 * k)} {f(sx + 12 * k)} {f(sy - 40 * k)}" stroke="#8A5A1A" stroke-width="{f(4 * k)}" fill="none"></path>')
    o.append(plate_label(cx, h * 0.96, "FIRSTFRUITS · NO SHADOW CAST BY TURNING", GOLD, 9, halo_="#2A3A1A")
             + plate_label(w * 0.14, h * 0.32, "THE LIGHTS", "#E8E2D6", 9, halo_="#0B0B2A") + plate_label(w * 0.86, h * 0.36, "OF HEAVEN", "#FFE680", 9, halo_="#0B0B2A"))
    return "".join(o)

def bronze_disc(x, y, r, uid, face=True):
    """A polished bronze hand mirror, its disc at (x, y), a dim face in it."""
    o = [f'<defs><radialGradient id="{uid}" cx="0.4" cy="0.35" r="0.8"><stop offset="0" stop-color="#F8E0A0"></stop><stop offset="0.6" stop-color="#C8903A"></stop>'
         f'<stop offset="1" stop-color="#7A4A1A"></stop></radialGradient></defs>',
         f'<rect x="{f(x - r * 0.16)}" y="{f(y + r * 0.9)}" width="{f(r * 0.32)}" height="{f(r * 1.2)}" rx="{f(r * 0.08)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>',
         f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="url(#{uid})" stroke="{INK}" stroke-width="3"></circle>']
    if face:
        o.append(f'<ellipse cx="{f(x + r * 0.05)}" cy="{f(y + r * 0.02)}" rx="{f(r * 0.36)}" ry="{f(r * 0.46)}" fill="#8A5A2A" opacity="0.45"></ellipse>'
                 f'<path d="M{f(x - r * 0.38)} {f(y - r * 0.18)} C {f(x - r * 0.3)} {f(y - r * 0.6)} {f(x + r * 0.4)} {f(y - r * 0.6)} {f(x + r * 0.42)} {f(y - r * 0.14)}" fill="#5A3A1A" opacity="0.4"></path>')
    o.append(f'<path d="M{f(x - r * 0.6)} {f(y - r * 0.5)} C {f(x - r * 0.4)} {f(y - r * 0.75)} {f(x - r * 0.1)} {f(y - r * 0.82)} {f(x + r * 0.15)} {f(y - r * 0.8)}" fill="none" stroke="#FFF4C2" stroke-width="2.4" opacity="0.8"></path>')
    return "".join(o)

def mirror_man(p, w, h, seed):
    """A man beholding his natural face in a mirror, and he goeth away, and straightway forgetteth: within a house, at
    the left the man holding the bronze mirror up before his face; at the right the same man gone out at the door into the
    street, the mirror left lying on the table behind him."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#C8B088", floor="#8A6A4A")]
    s = fit(b, max(h * 0.16, b - 230))
    dx, dw = w * 0.64, max(w * 0.14, 80 * s)                      # the open door onto the street
    o.append(doorway(dx, b - 196 * s, dw, b, seed, night=False))
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="#6A4A2A" stroke-width="3" stroke-dasharray="8 6" opacity="0.6"></path>')
    hx = w * 0.18
    o.append(man_r(p, hx, b, s, 0, flip=False, up=[(-22, -158), (-46, -164), (-58, -176)]))
    o.append(bronze_disc(hx - 70 * s, b - 190 * s, 15 * s, f"{p}bm", face=True))
    o.append(low_table(w * 0.56, b, 70 * s, s) + f'<g transform="translate({f(w * 0.56 + 35 * s)} {f(b - 32 * s)}) rotate(80)">' + bronze_disc(0, 0, 12 * s, f"{p}bm2", face=False) + '</g>')
    o.append(man_r(p, dx + dw * 0.55, b, s * 0.96, 0, flip=True, pose="walk"))
    o.append(plate_label(w * 0.25, h * 0.1, "HE BEHOLDETH HIMSELF", "#3A2A1A", 10, halo_="#E8D8B0")
             + plate_label(w * 0.75, h * 0.1, "AND GOETH AWAY", "#3A2A1A", 10, halo_="#E8D8B0"))
    return "".join(o)

def widows(p, w, h, seed):
    """To visit the fatherless and widows in their affliction: a poor house at the end of the street, a widow in a dark
    veil at her door with her two children, and a brother of the church come to them with a basket of bread and a jar."""
    bg, b = _street(w, h, seed, "dusk")
    s = fit(b, max(h * 0.16, b - 225))
    o = [D_(p), bg]
    hx, hw = w * 0.44, w * 0.36                                    # the widow's house: a low door, a lamp within
    o.append(f'<rect x="{f(hx)}" y="{f(b - 210 * s)}" width="{f(hw)}" height="{f(210 * s)}" fill="#B89A72" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx + hw * 0.2)}" y="{f(b - 150 * s)}" width="{f(hw * 0.26)}" height="{f(150 * s)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>')
    basket = ('<path d="M-82 -150 L -54 -150 L -58 -132 L -78 -132 Z" fill="#B8864A" stroke="#0D0D0F" stroke-width="1.6"></path>'
              '<circle cx="-72" cy="-152" r="5" fill="#D8A860" stroke="#0D0D0F" stroke-width="1"></circle><circle cx="-62" cy="-153" r="5" fill="#D8A860" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append(man_r(p, w * 0.3, b, s, 1, flip=True, up=[(-22, -158), (-46, -146), (-64, -142)], extra=basket))
    o.append(robed(p, hx + hw * 0.66, b, s * 0.94, "#3A3440", woman=True, veil="#1A1A22", flip=False))
    o.append(robed(p, hx + hw * 0.88, b, s * 0.62, "#8A7A5A", hair="#2A1A10", belt="#5A4A2A"))
    o.append(robed(p, hx + hw * 0.5, b, s * 0.5, "#6A7A8A", hair="#2A1A10", belt="#5A4A2A"))
    return "".join(o)
