"""Drawings for the 1 John volume (and, by `from jn1.art import *`, for 2 and 3 John). 1 John starts from Galatians'
drawings (`from gal.art import *`, which carries Acts', Mark's and Matthew's drawings and the epistle kit) and adds its own.

People at a distance are drawn on the kit silhouettes (epistle.robed): John the elder only ever jn1.common.john_fig; Jesus
as ntcast draws him (jesus_fig) and, risen, co1.art5.risen_fig. God is never drawn ("God is light" is light; the Father's
throne is empty, filled with light); the evil one, the devil and antichrist are never drawn. Every function takes
(p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from gal.art import *
from gal.art import _defs, _portrait
from epistle import study, robed, stool, bench, low_table, inkpot, reed_pen, open_letter, sealed_scroll, lamp_glow, plate_bg, tag, dim, doorway, radiance
from co1.art import _eph_window
from co1.art5 import risen_fig
from act.art11 import diana_temple
from genesis.art4 import clay_lamp
from mat.art import dove_light, UP_BLESS, UP_HIGH, UP_TOUCH, UP_CALL
from ezk.art2 import idol as small_idol
from jer.art4 import idol as tall_idol
from dan.art import cup as gold_cup
import faces
from jn1.common import john_fig, john_writer, JOHN_LOOK, LADY_LOOK, GAIUS_LOOK, DIOTREPHES_LOOK, DEMETRIUS_LOOK, WHITE

GOLD, CY = "#FFD23F", "#8FD0E2"
SCRIBE_LOOK = dict(cloth="#4A5A6A", hair="#2A1A10")        # the young scribe at Ephesus: bareheaded, beardless, a slate robe

def believer(p, x, y, s, i=0, flip=False, up=None, pose="stand"):
    """One of the church at Ephesus: men in plain robes with cool or off-white headcloths or bareheaded, women in cool veils."""
    looks = [("#4A5A6A", "#2A3A4A", None, "#2A1A10", False, None), ("#6A5A7A", None, "#2A3A5A", None, True, None),
             ("#6A5A4A", "#E8E2D6", None, "#6A645E", False, None), ("#5A7A6A", None, "#1F3A3A", None, True, None),
             ("#7A6A5A", None, None, "#3A2A1A", False, "#2A1A10"), ("#8A7A9A", None, "#E8E2D6", None, True, None),
             ("#3A4A3A", "#1F2F2A", None, "#3A2A1A", False, None), ("#7A5A5A", None, "#3A3A5A", None, True, None)]
    c, hd, vl, bd, wo, hr = looks[i % len(looks)]
    if wo: return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, flip=flip, up=up, pose=pose, seat=None if pose == "sit" else "stool")
    return robed(p, x, y, s, c, head=hd, beard=bd, hair=hr, flip=flip, up=up, pose=pose, seat=None if pose == "sit" else "stool")

def child(p, x, y, s, i=0, flip=False, up=None, pose="stand"):
    """A child (about two-thirds of a grown figure's height): a boy bareheaded, or a girl in a light veil."""
    c, hr, vl = [("#C8A060", "#2A1A10", None), ("#7A9AB0", None, "#E8E2D6"), ("#8A6A9A", "#3A2214", None), ("#9AB08A", None, "#2A3A5A")][i % 4]
    if vl: return robed(p, x, y, s * 0.66, c, woman=True, veil=vl, flip=flip, up=up, pose=pose)
    return robed(p, x, y, s * 0.68, c, hair=hr, belt="#6A4A2A", flip=flip, up=up, pose=pose)

def study_john(p, w, h, seed, stage="dictate", night=True, fig_h=None, others=(), bearer=None):
    """The letter written at Ephesus (epistle.study): John standing with his staff, dictating, the young scribe cross-legged
    on the mat writing, the window on Ephesus (the theatre in the hill, Diana's temple far off on the plain)."""
    return study(p, w, h, seed, stage=stage, scribe=SCRIBE_LOOK, writer=john_writer, window=_eph_window, night=night, fig_h=fig_h,
                 others=others, bearer=bearer)

def _vignette(fn, x, y, wd, hh, uid, label_, tone="#F3E2B8"):
    """A memory: drawing fn(w, h) in a framed inset, warmed toward sepia, its label on a strip above it."""
    return (f'<defs><clipPath id="{uid}c"><rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}"></rect></clipPath></defs>'
            f'<g clip-path="url(#{uid}c)"><g transform="translate({f(x)} {f(y + 22)})">{fn(wd, hh - 22)}</g>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}" fill="{tone}" opacity="0.22"></rect></g>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="22" fill="#2A1A10"></rect>'
            + plate_label(x + wd / 2, y + 15, label_, "#F3E2B8", 10, halo_="#2A1A10"))

from ntcast import JESUS_SKIN, JESUS_TUNIC, JESUS_MANTLE, _HAIR_FIG, _BEARD_FIG

def jesus_r(p, x, y, s, flip=False, up=None, extra="", pose="stand", glow_=True):
    """Jesus as ntcast draws him (olive-brown skin, dark hair to the shoulders, a short dark beard, the undyed robe and the
    blue-grey mantle, a soft gold glow, no halo), on the kit silhouette (epistle.robed) as the letters draw people."""
    g = f'<circle cx="{f(x)}" cy="{f(y - 150 * s)}" r="{f(70 * s)}" fill="#FFE680" opacity="0.2"></circle>' if glow_ else ""
    return g + robed(p, x, y, s, JESUS_TUNIC, skin=JESUS_SKIN, mantle=JESUS_MANTLE, flip=flip, up=up, extra=_HAIR_FIG + _BEARD_FIG + extra, pose=pose,
                     seat=None if pose == "sit" else "stool")

def john_young(p, x, y, s, flip=False, up=None, pose="stand"):
    """The beloved disciple as the Gospels draw him: young, beardless, dark hair, his rust robe (ntcast ROBES["john"])."""
    return robed(p, x, y, s, ROBES["john"], hair="#2A1A10", belt="#6A2A1A", flip=flip, up=up, pose=pose, seat=None if pose == "sit" else "stool")

def peter_r(p, x, y, s, flip=False, up=None, pose="stand"):
    return robed(p, x, y, s, ROBES["peter"], hair="#2A2420", beard="#4A4440", mantle="#4A3420", flip=flip, up=up, pose=pose, seat=None if pose == "sit" else "stool")

def thomas_r(p, x, y, s, flip=False, up=None):
    return robed(p, x, y, s, ROBES["thomas"], head="#5A4A6A", cord="#2A1A10", beard="#2A1A10", flip=flip, up=up)

def _heard(p, w, h, seed):
    """Heard: Jesus sitting on a stone by the sea teaching, his hand out; the young John and Peter sitting at his feet."""
    b = h * 0.9
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.36, seed, color="#7A8A6A", amp=10, step=70), lake(w, h, h * 0.42, seed, n=6),
         shore(w, h, h * 0.62, color="#C8B080")]
    s = fit(b, b - h * 0.7)
    o.append(f'<path d="M{f(w * 0.56)} {f(b)} C {f(w * 0.56)} {f(b - 50 * s)} {f(w * 0.9)} {f(b - 54 * s)} {f(w * 0.92)} {f(b)} Z" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></path>')
    o.append(jesus_r(p, w * 0.74, b, s, flip=False, up=[(-22, -158), (-46, -150), (-66, -158)], pose="sit"))
    for x in (0.2, 0.44):
        o.append(rock_seat(w * x, b, s * 0.62))
    o.append(peter_r(p, w * 0.2, b, s * 0.62, flip=True, pose="sit") + john_young(p, w * 0.44, b, s * 0.62, flip=True, pose="sit"))
    return "".join(o)

def rock_seat(x, b, s, color="#9A8A7A"):
    """A low stone to sit on, its top at a seated robed() figure's seat (SEAT_Y·s), (x, b) the figure's place on the ground."""
    return (f'<path d="M{f(x - 34 * s)} {f(b)} C {f(x - 34 * s)} {f(b - 46 * s)} {f(x - 20 * s)} {f(b - 52 * s)} {f(x)} {f(b - 52 * s)} '
            f'C {f(x + 24 * s)} {f(b - 52 * s)} {f(x + 38 * s)} {f(b - 44 * s)} {f(x + 38 * s)} {f(b)} Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>')

def beach(p, w, h, seed):
    """We have beheld and bear witness (4:14): Jesus on the beach at daybreak, the boat on the water (as the memory's "seen")."""
    return _seen(p, w, h, seed)

def _seen(p, w, h, seed):
    """Seen with our eyes: Jesus standing on the beach at daybreak, the boat far out on the grey-gold water, the net over its side."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#3A3A7A", "#FFD8A0"), halo(w * 0.7, h * 0.4, h * 0.6, "#FFF4C2", 0.6), hills(w, h, h * 0.38, seed, color="#5A5A7A", amp=8, step=70),
         lake(w, h, h * 0.44, seed, color="#6A7AA0", deep="#3A4A7A", n=10), shore(w, h, h * 0.74, color="#C8B080")]
    o.append(boat(p, w * 0.62, h * 0.54, min(0.5, w / 600), crew=((-30, "#6A4A2A"), (0, "#B85A3A"), (30, "#5A6A8A")), net=True))
    s = fit(b, b - h * 0.6)
    o.append(jesus_r(p, w * 0.24, b, s, flip=True))
    return "".join(o)

def _handled(p, w, h, seed):
    """Our hands handled: the room with its door shut, the risen Lord in white light, his hands held open (no wound drawn),
    Thomas reaching out his hand to him, the young John beside."""
    b = h * 0.92
    o = [_defs(p), room(w, h, b, wall="#5A4A4A", floor="#3A2E2A"), f'<rect x="{f(w * 0.84)}" y="{f(h * 0.34)}" width="{f(w * 0.14)}" height="{f(b - h * 0.34)}" fill="#4A2A1A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, b - h * 0.66)
    o.append(risen_fig(p, w * 0.32, b, s, flip=True, up=[(-22, -158), (-44, -134), (-62, -126)]))
    o.append(thomas_r(p, w * 0.64, b, s * 0.96, up=[(-22, -158), (-46, -142), (-68, -136)]) + john_young(p, w * 0.84, b, s * 0.94))
    return "".join(o)

def memory(w, h, seed=1):
    """That which we have heard, which we have seen with our eyes, that which we beheld, and our hands handled: three
    memories of the Gospel in framed insets on the dark of the old man's remembering — Jesus sitting by the sea teaching,
    the young John and Peter at his feet (heard); Jesus standing on the beach at daybreak, the boat on the water (seen); the
    risen Lord in the shut room, his hands held open, Thomas reaching out to him (handled)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E140E"></rect>', halo(w * 0.5, h * 0.5, max(w, h) * 0.6, "#5A3A22", 0.5)]
    pad, gap = 12, 10
    vw = (w - 2 * pad - 2 * gap) / 3; vh = h - 2 * pad
    shots = [(lambda ww, hh: _heard(f"mm{seed}a", ww, hh, seed), "WHICH WE HAVE HEARD"),
             (lambda ww, hh: _seen(f"mm{seed}b", ww, hh, seed + 1), "SEEN WITH OUR EYES"),
             (lambda ww, hh: _handled(f"mm{seed}c", ww, hh, seed + 2), "OUR HANDS HANDLED")]
    for i, (fn, lab) in enumerate(shots):
        o.append(_vignette(fn, pad + i * (vw + gap), pad, vw, vh, f"mm{seed}{i}", lab))
    return "".join(o)

def god_light(w, h, seed=1):
    """God is light, and in him is no darkness at all: light only — a white heart of light filling the panel, gold and then
    flame toward the edges, rays going out on every side, and no darkness left anywhere in it (no figure)."""
    uid = f"gl{seed}"
    cx, cy = w * 0.5, h * 0.52
    return (f'<defs><radialGradient id="{uid}" cx="0.5" cy="0.52" r="0.75"><stop offset="0" stop-color="#FFFFFF"></stop><stop offset="0.28" stop-color="#FFF8DC"></stop>'
            f'<stop offset="0.55" stop-color="#FFE680"></stop><stop offset="0.8" stop-color="#FFC14D"></stop><stop offset="1" stop-color="#FF8A3D"></stop></radialGradient></defs>'
            f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>'
            + rays(cx, cy, 48, min(w, h) * 0.12, max(w, h) * 1.2, "#FFFFFF", 0.35, 4)
            + halo(cx, cy, min(w, h) * 0.5, "#FFFFFF", 0.95))

def walk_light(p, w, h, seed):
    """If we walk in the light, as he is in the light, we have fellowship one with another: four of the brethren walking
    together on the road out of the night at the left into the morning light at the right, one with his hand on another's
    shoulder."""
    b = h * 0.92
    o = [_defs(p), f'<defs><linearGradient id="{p}wl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B0B2A"></stop><stop offset="0.35" stop-color="#3A2A5A"></stop>'
         f'<stop offset="0.7" stop-color="#F3C890"></stop><stop offset="1" stop-color="#FFF8DC"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}wl)"></rect>', mk.stars(18, w * 0.3, h * 0.5, seed),
         halo(w * 0.96, h * 0.42, max(w, h) * 0.4, "#FFFFFF", 0.8), rays(w * 0.96, h * 0.42, 22, h * 0.08, max(w, h) * 0.6, "#FFF4C2", 0.3, 4),
         hills(w, h, h * 0.62, seed, color="#6A5A6A", amp=10, step=90), ground(w, h, h * 0.7, "#8A7A62", dy=0),
         f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.7)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h * 0.96)} C {f(w * 0.6)} {f(h * 0.98)} {f(w * 0.3)} {f(h)} -10 {f(h + 4)} Z" fill="#C8B080" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.18, b - 220))
    for i, x in enumerate((0.34, 0.46, 0.58, 0.7)):
        o.append(believer(p, w * x, b - i * 2, s * (0.96 + 0.01 * i), i, flip=True, pose="walk"))
    return "".join(o)

def _throne(x, base, s, color="#FFF4C2"):
    """An empty throne of light on its steps (God is never drawn): the seat, the high back, the arms, three steps."""
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)})">']
    for k in range(3):
        o.append(f'<rect x="{-90 + k * 16}" y="{-16 - k * 16}" width="{180 - k * 32}" height="16" fill="#FFF8DC" stroke="#E8B830" stroke-width="2"></rect>')
    o.append('<path d="M-40 -48 L -40 -150 C -40 -176 40 -176 40 -150 L 40 -48 Z" fill="#FFFDF0" stroke="#E8B830" stroke-width="2.6"></path>'
             '<rect x="-52" y="-92" width="104" height="14" fill="#FFF8DC" stroke="#E8B830" stroke-width="2"></rect>'
             '<path d="M-52 -92 L -52 -48 M52 -92 L 52 -48" stroke="#E8B830" stroke-width="5"></path>')
    return "".join(o) + "</g>"

def advocate(p, w, h, seed):
    """We have an Advocate with the Father, Jesus Christ the righteous: the empty throne on its steps at the right, filled
    with light (the Father never drawn); Jesus risen in white light standing before it at the left, his hand held out toward
    it; and below, the dark curve of the whole world with the lamps of its towns."""
    b = h * 0.78
    o = [_defs(p), sky(w, h, "#2A2060", "#C8A0D8"), halo(w * 0.74, h * 0.4, max(w, h) * 0.55, "#FFFFFF", 0.8),
         rays(w * 0.74, h * 0.4, 30, h * 0.1, max(w, h), "#FFF4C2", 0.3, 4)]
    o.append(_throne(w * 0.74, b, min(1.4, h / 300)))
    o.append(f'<path d="M-20 {f(b)} L {f(w + 20)} {f(b)}" stroke="#FFF4C2" stroke-width="3" opacity="0.7"></path>')
    o.append(f'<path d="M-40 {f(h + 10)} C {f(w * 0.2)} {f(h * 0.82)} {f(w * 0.8)} {f(h * 0.82)} {f(w + 40)} {f(h + 10)} Z" fill="#0F2A3A" stroke="{INK}" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for _ in range(int(w / 26)):
        xx = r.uniform(w * 0.05, w * 0.95); yy = h * 0.9 + abs(xx - w / 2) / w * h * 0.12 + r.uniform(0, h * 0.06)
        o.append(f'<circle cx="{f(xx)}" cy="{f(yy)}" r="{f(r.uniform(1.4, 2.6))}" fill="#FFC14D"></circle>')
    s = fit(b, max(h * 0.06, b - h * 0.62))
    o.append(risen_fig(p, w * 0.36, b, s, flip=True, up=[(-22, -158), (-46, -150), (-70, -156)]))
    return "".join(o)

def dawn_ephesus(w, h, seed, sun_x=0.84):
    """The darkness is passing away, and the true light already shineth: dawn over Ephesus — the night with its last stars
    drawing off to the left, the sun coming up out of the sea at the right (at sun_x of the width), the harbour and the city
    on its hills, the theatre in the hillside and Diana's temple on the plain still in shadow."""
    uid = f"de{seed}"
    sx = w * sun_x
    o = [f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="1" y2="0.4"><stop offset="0" stop-color="#0B0B2A"></stop><stop offset="0.4" stop-color="#3A2A6A"></stop>'
         f'<stop offset="0.72" stop-color="#E8906A"></stop><stop offset="1" stop-color="#FFE6A0"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>', mk.stars(30, w * 0.42, h * 0.5, seed),
         halo(sx, h * 0.6, max(w, h) * 0.45, "#FFF4C2", 0.7), rays(sx, h * 0.6, 26, h * 0.08, max(w, h) * 0.9, "#FFF4C2", 0.26, 4, a0=180, a1=360),
         f'<circle cx="{f(sx)}" cy="{f(h * 0.6)}" r="{f(max(12, h * 0.07))}" fill="#FFF8DC"></circle>',
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h * 0.42)}" fill="#3A4A7A"></rect>',
         f'<path d="M{f(sx - w * 0.2)} {f(h * 0.6)} L {f(sx + w * 0.2)} {f(h * 0.6)} C {f(sx + w * 0.08)} {f(h * 0.63)} {f(sx - w * 0.08)} {f(h * 0.63)} {f(sx - w * 0.2)} {f(h * 0.6)} Z" fill="#FFE6A0" opacity="0.7"></path>']
    r = random.Random(seed)
    for k in range(10):
        yy = h * (0.63 + 0.035 * k); xx = sx + r.uniform(-w * 0.06, w * 0.06)
        o.append(f'<path d="M{f(xx - w * 0.05)} {f(yy)} L {f(xx + w * 0.05)} {f(yy)}" stroke="#FFF4C2" stroke-width="2" opacity="0.6"></path>')
    o.append(f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.14)} {f(h * 0.3)} {f(w * 0.3)} {f(h * 0.32)} {f(w * 0.46)} {f(h * 0.5)} C {f(w * 0.52)} {f(h * 0.62)} {f(w * 0.56)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.76)} '
             f'L {f(w * 0.6)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2440" stroke="{INK}" stroke-width="2"></path>')
    cx, cy, rw = w * 0.22, h * 0.56, w * 0.11                                   # the theatre in the hillside
    for k in range(4):
        r_ = rw * (1 - k * 0.2)
        o.append(f'<path d="M{f(cx - r_)} {f(cy)} A {f(r_)} {f(r_ * 0.55)} 0 0 1 {f(cx + r_)} {f(cy)}" fill="none" stroke="#6A6080" stroke-width="2.4"></path>')
    o.append(houses(w, h, h * 0.84, seed, x0=-10, x1=w * 0.58, hmin=0.07, hmax=0.12, lit=True, color=("#4A4060", "#3E3656", "#52486A", "#463E5E")))
    o.append(diana_temple(w * 0.52, h * 0.79, w * 0.09).replace("#F3EFE6", "#6A6080").replace("#D8D0C0", "#5A5070"))
    o.append(f'<path d="M-10 {f(h * 0.84)} L {f(w * 0.6)} {f(h * 0.84)} L {f(w * 0.62)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1E1A30" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def dark_road(p, w, h, seed):
    """He that hateth his brother is in the darkness, and walketh in the darkness, and knoweth not whither he goeth: a road
    by night under no moon, a man feeling his way along it with his hand out, a stone in the way before his feet; far off
    at the right a lit doorway, two brethren meeting in its light (he that loveth his brother abideth in the light)."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#05050E", "#141428"), hills(w, h, h * 0.56, seed, color="#0E0E1C", amp=10, step=80), ground(w, h, h * 0.66, "#141420", dy=0)]
    dx, dw = w * 0.8, max(36, w * 0.07)
    o.append(f'<rect x="{f(dx - dw * 1.4)}" y="{f(h * 0.4)}" width="{f(dw * 2.8)}" height="{f(h * 0.27)}" fill="#2A2438" stroke="{INK}" stroke-width="1.6"></rect>'
             + glow(dx, h * 0.6, h * 0.34, "#FFC14D", 0.5, f"{p}dg")
             + f'<rect x="{f(dx - dw / 2)}" y="{f(h * 0.5)}" width="{f(dw)}" height="{f(h * 0.17)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>')
    s2 = h * 0.15 / 200                                              # small, in the doorway far off
    o.append(believer(p, dx - dw * 0.18, h * 0.67, s2, 2, flip=True, up=UP_BLESS) + believer(p, dx + dw * 0.18, h * 0.67, s2, 0, up=UP_BLESS))
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(b - 4)}" rx="{f(w * 0.04)}" ry="{f(h * 0.03)}" fill="#3A3640" stroke="{INK}" stroke-width="1.6"></ellipse>')
    s = fit(b, max(h * 0.16, b - 230))
    o.append(robed(p, w * 0.18, b, s, "#3A3A48", head="#22222E", cord="#0D0D0F", beard="#1A1210", flip=True, up=UP_TOUCH, pose="walk"))
    o.append(f'<rect x="-10" y="-10" width="{f(w * 0.5)}" height="{f(h + 20)}" fill="#05050E" opacity="0.25"></rect>')
    return "".join(o)

def _cell_ground(x, y, wd, hh, top, bot, uid):
    return (f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"></stop><stop offset="1" stop-color="{bot}"></stop></linearGradient>'
            f'<clipPath id="{uid}c"><rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}"></rect></clipPath></defs>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}" fill="url(#{uid})"></rect>')

def three_ages(p, w, h):
    """I write unto you, my little children … fathers … young men: a plate of three cells — the little children (a boy and
    a girl), the fathers (two old men, grey and white), the young men (two standing upright, strong) — each named."""
    o = [_defs(p), plate_bg(w, h, "1 JOHN 2:12–14 · I WRITE UNTO YOU")]
    top = 34; pad = 10; cw = (w - 4 * pad) / 3; ch = h - top - pad
    cells = [("LITTLE CHILDREN", "#8FD0E2", "#F3E8C8"), ("FATHERS", "#C8A0D8", "#F3E2C8"), ("YOUNG MEN", "#9CCB5E", "#F3EAC8")]
    for i, (name, t, bt) in enumerate(cells):
        x = pad + i * (cw + pad); y = top
        o.append(_cell_ground(x, y, cw, ch, t, bt, f"{p}ta{i}"))
        b = y + ch - 6
        s = fit(b, max(y + 34, b - min(ch * 0.74, 230)))
        o.append(f'<g clip-path="url(#{p}ta{i}c)"><rect x="{f(x)}" y="{f(b - 4)}" width="{f(cw)}" height="{f(ch)}" fill="#C8B07A"></rect>')
        if i == 0:
            o.append(child(p, x + cw * 0.36, b, s, 0, flip=True) + child(p, x + cw * 0.64, b, s, 1))
        elif i == 1:
            o.append(robed(p, x + cw * 0.34, b, s, "#6A5A4A", head="#E8E2D6", cord="#5A4A3A", beard="#C8C2B6", mantle="#4A5A6A", flip=True)
                     + robed(p, x + cw * 0.68, b, s, "#4A5A6A", hair="#E8E2D6", beard="#E8E2D6", mantle="#6A5A4A"))
        else:
            o.append(robed(p, x + cw * 0.34, b, s, "#5A7A4A", hair="#2A1A10", belt="#3A2A1A", flip=True, up=UP_HIGH)
                     + robed(p, x + cw * 0.68, b, s, "#3A5A7A", head="#1F3A4A", cord="#0D1A20", beard="#2A1A10", belt="#2A1A10"))
        o.append('</g>' + f'<rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="{f(ch)}" fill="none" stroke="{GOLD}" stroke-width="2"></rect>'
                 f'<rect x="{f(x)}" y="{f(y)}" width="{f(cw)}" height="24" fill="#0B1A2E"></rect>'
                 + plate_label(x + cw / 2, y + 16, name, GOLD, 11))
    return "".join(o)

def _stall(x, base, wd, hh, awning, wares, seed):
    """A market stall: posts, a striped awning, a counter with its wares (cloth, jars, gold, fine robes hanging)."""
    r = random.Random(seed); o = []
    o.append(f'<path d="M{f(x)} {f(base)} L {f(x)} {f(base - hh)} M{f(x + wd)} {f(base)} L {f(x + wd)} {f(base - hh)}" stroke="#4A2A14" stroke-width="4"></path>')
    o.append(f'<path d="M{f(x - wd * 0.06)} {f(base - hh)} L {f(x + wd * 1.06)} {f(base - hh)} L {f(x + wd * 0.98)} {f(base - hh * 0.8)} L {f(x + wd * 0.02)} {f(base - hh * 0.8)} Z" fill="{awning[0]}" stroke="{INK}" stroke-width="1.8"></path>'
             + "".join(f'<path d="M{f(x + wd * k / 6)} {f(base - hh)} L {f(x + wd * (0.02 + k / 6.4))} {f(base - hh * 0.8)}" stroke="{awning[1]}" stroke-width="{f(wd / 16)}"></path>' for k in range(1, 6, 2)))
    o.append(f'<rect x="{f(x)}" y="{f(base - hh * 0.36)}" width="{f(wd)}" height="{f(hh * 0.36)}" fill="#8A5A30" stroke="{INK}" stroke-width="1.8"></rect>')
    cy = base - hh * 0.36
    if wares == "cloth":
        for k in range(4):
            c = ["#B5121B", "#1F5FAD", "#E8B830", "#5A2A7A"][k]
            o.append(f'<rect x="{f(x + wd * (0.06 + 0.22 * k))}" y="{f(cy - hh * 0.12)}" width="{f(wd * 0.2)}" height="{f(hh * 0.12)}" fill="{c}" stroke="{INK}" stroke-width="1.2"></rect>')
            o.append(f'<path d="M{f(x + wd * (0.1 + 0.22 * k))} {f(base - hh * 0.78)} L {f(x + wd * (0.1 + 0.22 * k))} {f(base - hh * 0.5)}" stroke="{c}" stroke-width="{f(wd * 0.12)}"></path>')
    elif wares == "jars":
        for k in range(5):
            jx = x + wd * (0.12 + 0.19 * k); jh = hh * r.uniform(0.14, 0.2)
            o.append(f'<path d="M{f(jx - wd * 0.06)} {f(cy)} C {f(jx - wd * 0.08)} {f(cy - jh * 0.7)} {f(jx - wd * 0.03)} {f(cy - jh)} {f(jx)} {f(cy - jh)} C {f(jx + wd * 0.03)} {f(cy - jh)} {f(jx + wd * 0.08)} {f(cy - jh * 0.7)} {f(jx + wd * 0.06)} {f(cy)} Z" '
                     f'fill="{["#C8682E", "#E8D8B0", "#4A6A8A"][k % 3]}" stroke="{INK}" stroke-width="1.2"></path>')
    else:
        for k in range(6):
            o.append(f'<circle cx="{f(x + wd * (0.12 + 0.15 * k))}" cy="{f(cy - hh * 0.05)}" r="{f(hh * 0.045)}" fill="{GOLD if k % 2 else "#E8E2D6"}" stroke="{INK}" stroke-width="1.2"></circle>')
        o.append(gold_cup(x + wd * 0.5, cy - hh * 0.1, hh / 140))
    return "".join(o)

def world_passing(p, w, h, seed):
    """The world passeth away, and the lust thereof: a market street of the city — stalls of dyed cloth, jars, gold and
    silver, buyers among them — and at the right everything thinning into a pale haze and gone, stalls, wares and street."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#C8906A", "#F3D8A8"), houses(w, h, h * 0.58, seed, hmin=0.14, hmax=0.24), ground(w, h, h * 0.58, "#B89A6A", dy=0)]
    sw = w * 0.2
    for i, ware in enumerate(("cloth", "gold", "jars", "cloth", "gold")):
        o.append(_stall(w * 0.02 + i * sw * 1.04, h * 0.78, sw * 0.9, h * 0.4, [("#B5121B", "#F3E2B8"), ("#1F5FAD", "#F3E2B8"), ("#2E6B3A", "#F3E2B8")][i % 3], ware, seed + i))
    s = fit(b, max(h * 0.18, b - 200))
    o.append(robed(p, w * 0.2, b, s, "#7A1A4A", head="#1F2F5A", cord=GOLD, beard="#1A1210", mantle="#E8B830", flip=True, up=UP_BLESS)
             + believer(p, w * 0.36, b, s, 1) + robed(p, w * 0.56, b, s, "#2A4A8A", hair="#1A1210", beard="#1A1210", mantle="#B5121B", up=UP_TOUCH))
    o.append(f'<defs><linearGradient id="{p}fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F3E8D0" stop-opacity="0"></stop><stop offset="0.45" stop-color="#F3E8D0" stop-opacity="0"></stop>'
             f'<stop offset="0.82" stop-color="#F3E8D0" stop-opacity="0.92"></stop><stop offset="1" stop-color="#F8F2E4" stop-opacity="1"></stop></linearGradient></defs>'
             f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}fade)"></rect>')
    r = random.Random(seed)
    for _ in range(26):
        xx = r.uniform(w * 0.55, w); yy = r.uniform(h * 0.2, h * 0.9)
        o.append(f'<circle cx="{f(xx)}" cy="{f(yy)}" r="{f(r.uniform(1, 3))}" fill="#C8B080" opacity="{r.uniform(0.2, 0.6):.2f}"></circle>')
    return "".join(o)

def horn_oil(w, h, seed):
    """Ye have an anointing from the Holy One: a ram's horn of oil tipped in the light, the oil falling from it in a stream
    of gold drops (no hand drawn)."""
    k = min(w / 420, h / 260)
    cx, cy = w * 0.44, h * 0.36
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1440"></rect>', halo(w * 0.56, h * 0.7, max(w, h) * 0.5, "#FFE680", 0.55),
         rays(cx, cy, 28, 20 * k, max(w, h), "#FFF4C2", 0.2, 3)]
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) rotate(28) scale({f(k)})">'
             '<path d="M-110 -22 C -60 -40 0 -36 40 -18 C 60 -8 72 6 70 22 L 52 26 C 50 14 40 6 26 2 C -10 -8 -60 -6 -104 6 C -118 10 -126 -16 -110 -22 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="3"></path>'
             + "".join(f'<path d="M{-90 + 24 * i} {-24 + i} C {-86 + 24 * i} -10 {-86 + 24 * i} 0 {-90 + 24 * i} {6 - i}" fill="none" stroke="#B8A27A" stroke-width="2"></path>' for i in range(6))
             + '<ellipse cx="62" cy="24" rx="10" ry="5" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></ellipse></g>')
    tip_x, tip_y = cx + 62 * k * math.cos(math.radians(28)) - 24 * k * math.sin(math.radians(28)), cy + 62 * k * math.sin(math.radians(28)) + 24 * k * math.cos(math.radians(28))
    r = random.Random(seed)
    yy = tip_y + 10 * k
    while yy < h * 0.96:
        rr = r.uniform(3, 6) * k
        o.append(f'<path d="M{f(tip_x)} {f(yy - rr * 1.6)} C {f(tip_x + rr)} {f(yy - rr * 0.4)} {f(tip_x + rr)} {f(yy + rr)} {f(tip_x)} {f(yy + rr)} C {f(tip_x - rr)} {f(yy + rr)} {f(tip_x - rr)} {f(yy - rr * 0.4)} {f(tip_x)} {f(yy - rr * 1.6)} Z" '
                 f'fill="{GOLD}" stroke="#8A5A10" stroke-width="1"></path>')
        yy += rr * 3.4
    o.append(halo(tip_x, h * 0.96, 60 * k, "#FFFFFF", 0.7))
    return "".join(o)

def church_read(p, w, h, seed, reader=True):
    """The church at Ephesus in a house by lamplight: one standing with the roll open, reading the letter aloud; the
    brethren sitting on the benches either side, listening, a child standing among them; the lamp on its stand."""
    b = h * 0.94
    lx = w * 0.06
    o = [_defs(p), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - h * 0.5, max(w, h) * 0.6, f"{p}lg", op=0.5)]
    o.append(f'<path d="M{f(lx)} {f(b)} L {f(lx)} {f(b - h * 0.5)}" stroke="#3A2A1A" stroke-width="4"></path>' + clay_lamp(lx, b - h * 0.5, max(0.6, h / 300)))
    s = fit(b, max(h * 0.1, b - min(h * 0.62, 240)))
    step = 120 * s
    x0 = w * 0.12 + 30 * s
    o.append(bench(x0 - 40 * s, b, step + 96 * s, s))
    for i in range(2):
        o.append(believer(p, x0 + i * step, b, s, i, flip=True, pose="sit"))
    if reader:
        scroll_ = '<rect x="-84" y="-160" width="34" height="26" fill="#EADBB4" stroke="#0D0D0F" stroke-width="1.6"></rect>'
        o.append(robed(p, w * 0.7, b, s, "#4A5A6A", head="#E8E2D6", cord="#5A4A3A", beard="#6A645E", mantle="#5A4A3A", up=[(-22, -158), (-46, -150), (-66, -150)], extra=scroll_))
    xr = w * 0.96 - 30 * s
    o.append(bench(xr - 56 * s, b, 96 * s, s) + believer(p, xr, b, s, 3, pose="sit"))
    o.append(child(p, x0 + 2 * step + 10 * s, b, s, 2, flip=True))
    return "".join(o)

# ---- 1 John 3–5 ---------------------------------------------------------------------------------------------------------------
def children_stars(p, w, h, seed):
    """Behold what manner of love the Father hath bestowed upon us, that we should be called children of God: the church —
    men, women and their children — on a hill at night under the whole sky of stars, a soft light falling on them from
    above (no figure in it), the children in front with their arms up, faces turned up."""
    b = h * 0.94
    o = [_defs(p), night(w, h, seed, n=120, top="#05051A", bot="#3A2A6A"), halo(w * 0.56, h * 0.12, h * 0.5, "#FFF4C2", 0.5),
         rays(w * 0.56, h * 0.12, 18, h * 0.08, h * 0.9, "#FFF4C2", 0.18, 6, a0=30, a1=150),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2440" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.16, b - 210))
    figs = [(0.14, 0, None, False), (0.25, 1, UP_HIGH, False), (0.62, 2, None, True), (0.73, 3, UP_HIGH, True), (0.84, 4, None, True)]
    for x, i, up, fl in figs:
        o.append(believer(p, w * x, b, s, i, flip=fl, up=up))
    o.append(child(p, w * 0.36, b, s, 0, up=UP_HIGH) + child(p, w * 0.45, b, s, 1, flip=True) + child(p, w * 0.52, b, s, 3, flip=True, up=UP_HIGH))
    o.append(f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.32)}" fill="#FFF4C2" opacity="0.06"></rect>')
    return "".join(o)

def see_him(p, w, h, seed):
    """If he shall be manifested, we shall be like him; for we shall see him even as he is: the morning, Jesus risen in
    white light on the hill, and the brethren below turned toward him, the light on their faces and their robes."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#3A3A7A", "#FFE6B0"), halo(w * 0.7, h * 0.36, max(w, h) * 0.6, "#FFFFFF", 0.8),
         rays(w * 0.7, h * 0.36, 32, h * 0.1, max(w, h) * 1.1, "#FFF8DC", 0.3, 4),
         f'<path d="M{f(w * 0.36)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.6)} {f(w * 0.62)} {f(h * 0.56)} {f(w * 0.72)} {f(h * 0.56)} C {f(w * 0.84)} {f(h * 0.56)} {f(w * 0.92)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} Z" fill="#A8987A" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, h * 0.84, "#8A7A5A", dy=0)]
    s2 = fit(h * 0.57, max(h * 0.04, h * 0.57 - h * 0.44))
    o.append(risen_fig(p, w * 0.72, h * 0.57, s2, flip=False))
    s = fit(b, max(h * 0.3, b - 170))
    for i, x in enumerate((0.08, 0.17, 0.27, 0.37)):
        o.append(believer(p, w * x, b, s, i + 1, flip=True, up=UP_BLESS if i == 2 else None))
    return "".join(o)

CAIN_FACE = faces.face("adam", skin="#C47A5A", shadow="#5A1A16", brow="scowl", sigil=True, light="#FF6A4A")   # Genesis' Cain, angry, the mark set on him

def _altar(x, base, s, smoke, seed):
    """A rough altar of field stones with its smoke: smoke="up" rising straight, "down" beaten back along the ground."""
    r = random.Random(seed); o = []
    for row in range(3):
        for k in range(3 - row):
            o.append(f'<rect x="{f(x + (-30 + row * 10 + k * 20) * s)}" y="{f(base - (row + 1) * 14 * s)}" width="{f(20 * s)}" height="{f(14 * s)}" rx="3" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    top = base - 42 * s
    if smoke == "up":
        d = f"M{f(x)} {f(top)} " + " ".join(f"C {f(x + r.uniform(-14, 14) * s)} {f(top - (k + 0.3) * 40 * s)} {f(x + r.uniform(-14, 14) * s)} {f(top - (k + 0.7) * 40 * s)} {f(x + r.uniform(-6, 6) * s)} {f(top - (k + 1) * 40 * s)}" for k in range(5))
        o.append(f'<path d="{d}" fill="none" stroke="#E8E2D6" stroke-width="{f(16 * s)}" stroke-linecap="round" opacity="0.7"></path>')
    else:
        d = f"M{f(x)} {f(top)} C {f(x + 30 * s)} {f(top - 20 * s)} {f(x + 60 * s)} {f(top + 10 * s)} {f(x + 100 * s)} {f(top + 16 * s)} C {f(x + 150 * s)} {f(top + 22 * s)} {f(x + 200 * s)} {f(top + 34 * s)} {f(x + 260 * s)} {f(base - 6 * s)}"
        o.append(f'<path d="{d}" fill="none" stroke="#5A5060" stroke-width="{f(18 * s)}" stroke-linecap="round" opacity="0.7"></path>')
    return "".join(o)

def cain_field(p, w, h, seed, night_=False, portrait=True):
    """Not as Cain was of the evil one, and slew his brother: the field at dusk, empty — two altars of field stones, the smoke
    of one going straight up and the smoke of the other beaten down along the ground, a mattock left lying in the furrow; and
    in a framed portrait, Genesis' Cain, angry, the mark set on him. Nothing of the deed drawn: no one in the field.
    night_=True: the same field by night, empty, without the portrait (3:13–15)."""
    b = h * 0.9
    o = [sky(w, h, "#0B0B2A", "#2A2050") if night_ else sky(w, h, "#3A1A2A", "#E8784A")]
    if night_: o.append(mk.stars(40, w, h * 0.5, seed))
    else: o.append(halo(w * 0.3, h * 0.6, max(w, h) * 0.4, "#FFB070", 0.5))
    o.append(hills(w, h, h * 0.6, seed, color="#1E1428" if night_ else "#4A2A3A", amp=10, step=90))
    o.append(ground(w, h, h * 0.68, "#2A2018" if night_ else "#6A4A2A", dy=0))
    for k in range(7):                                               # the furrows of the tilled field
        yy = h * (0.72 + 0.04 * k)
        o.append(f'<path d="M-10 {f(yy)} C {f(w * 0.3)} {f(yy - 4)} {f(w * 0.7)} {f(yy + 4)} {f(w + 10)} {f(yy)}" stroke="{"#1A140E" if night_ else "#4A3018"}" stroke-width="2" fill="none"></path>')
    k = min(1.4, h / 300)
    o.append(_altar(w * 0.18, h * 0.7, k, "up", seed) + _altar(w * 0.44, h * 0.72, k, "down", seed + 1))
    o.append(f'<path d="M{f(w * 0.66)} {f(b)} L {f(w * 0.76)} {f(b - 30 * k)}" stroke="#4A2A14" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.645)} {f(b + 6 * k)} L {f(w * 0.68)} {f(b - 8 * k)} L {f(w * 0.69)} {f(b + 2 * k)} Z" fill="#6A6A70" stroke="{INK}" stroke-width="1.4"></path>')
    if night_:
        o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#05050E" opacity="0.2"></rect>')
    elif portrait:
        pw = min(w * 0.26, h * 0.62); ph = pw * 1.18
        o.append(_portrait(CAIN_FACE, w * 0.97 - pw, h * 0.06, pw, ph, f"{p}cf", light="#FF8A5A", ground_=("#2A0E14", "#7A2A1A")))
    return "".join(o)

def shut_heart(p, w, h, seed):
    """Whoso hath the world's goods, and beholdeth his brother in need, and shutteth up his compassion from him: a rich man's
    house at dusk, its gilded door shut and barred, light and a feast's lamps in the windows above, the owner at his window
    looking down and turning away; below at the shut door a brother in a torn cloak, sitting with his hand out."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#3A2A5A", "#C88A6A"), houses(w, h, h * 0.5, seed, x0=-10, x1=w * 0.3, hmin=0.12, hmax=0.2, lit=True)]
    hx, hw = w * 0.34, w * 0.62
    top = h * 0.1
    o.append(f'<rect x="{f(hx)}" y="{f(top)}" width="{f(hw)}" height="{f(b - top)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx - 8)}" y="{f(top - 10)}" width="{f(hw + 16)}" height="12" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(3):                                                # the lit windows above
        wx = hx + hw * (0.12 + 0.3 * k)
        o.append(f'<rect x="{f(wx)}" y="{f(top + h * 0.08)}" width="{f(hw * 0.16)}" height="{f(h * 0.16)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>')
    s2 = h * 0.2 / 206 / 1.4                                          # the owner seen to the waist in his window
    wx = hx + hw * 0.42
    o.append(f'<clipPath id="{p}win"><rect x="{f(wx)}" y="{f(top + h * 0.08)}" width="{f(hw * 0.16)}" height="{f(h * 0.16)}"></rect></clipPath>'
             f'<g clip-path="url(#{p}win)">' + robed(p, wx + hw * 0.08, top + h * 0.3, s2 * 1.4, "#7A1A4A", head="#1F2F5A", cord=GOLD, beard="#1A1210", mantle="#E8B830") + '</g>')
    dx, dw = hx + hw * 0.38, hw * 0.24
    o.append(f'<rect x="{f(dx)}" y="{f(b - h * 0.36)}" width="{f(dw)}" height="{f(h * 0.36)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(dx - 6)}" y="{f(b - h * 0.37 - 8)}" width="{f(dw + 12)}" height="10" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(dx + dw / 2)} {f(b - h * 0.36)} L {f(dx + dw / 2)} {f(b)}" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(dx - dw * 0.1)}" y="{f(b - h * 0.2)}" width="{f(dw * 1.2)}" height="{f(h * 0.03)}" fill="#3A2A1A" stroke="{INK}" stroke-width="1.6"></rect>'
             + "".join(f'<circle cx="{f(dx + dw * c)}" cy="{f(b - h * 0.28)}" r="3" fill="{GOLD}"></circle>' for c in (0.3, 0.7)))
    o.append(ground(w, h, b, "#8A7A62", dy=0))
    s = fit(b, max(h * 0.2, b - 190))
    o.append(f'<path d="M{f(w * 0.2 - 34 * s)} {f(b)} L {f(w * 0.2 - 30 * s)} {f(b - 50 * s)} L {f(w * 0.2 + 32 * s)} {f(b - 52 * s)} L {f(w * 0.2 + 38 * s)} {f(b)} Z" fill="#9A8A72" stroke="{INK}" stroke-width="2"></path>')
    o.append(robed(p, w * 0.2, b, s, "#6A6050", hair="#3A2A1A", beard="#3A2A1A", mantle="#4A4038", flip=True, up=UP_BLESS, pose="sit", seat=None))
    o.append(f'<path d="M{f(w * 0.2 - 10 * s)} {f(b - 70 * s)} l {f(8 * s)} {f(12 * s)} l {f(-6 * s)} {f(8 * s)} M{f(w * 0.2 - 4 * s)} {f(b - 40 * s)} l {f(10 * s)} {f(6 * s)}" stroke="{INK}" stroke-width="1.6" fill="none"></path>')
    return "".join(o)

def assay(w, h):
    """Prove the spirits, whether they are of God: the assayer's tools as a plate — the black touchstone with two streaks
    drawn on it, one of true gold and one of brass; the balance; the crucible over the fire, the dross skimmed off."""
    o = [plate_bg(w, h, "1 JOHN 4:1 · PROVE THE SPIRITS")]
    k = min(w / 680, (h - 84) / 168)
    ym = (66 + h - 12) / 2                                       # the tools centred below the row of their names
    for x, name in ((0.2, "THE TOUCHSTONE"), (0.5, "THE BALANCE"), (0.77, "THE CRUCIBLE")):
        o.append(plate_label(w * x, 52, name, CY, 10))
    # the touchstone
    tx, ty = w * 0.2, ym
    o.append(f'<g transform="translate({f(tx)} {f(ty)}) scale({f(k)})"><path d="M-80 -40 L 70 -50 L 84 36 L -70 44 Z" fill="#1A1A1E" stroke="#8FD0E2" stroke-width="2"></path>'
             '<path d="M-56 -18 C -20 -24 20 -26 54 -30" stroke="#FFD23F" stroke-width="7" stroke-linecap="round"></path>'
             '<path d="M-52 16 C -16 12 20 10 58 6" stroke="#9A7A3A" stroke-width="7" stroke-linecap="round" opacity="0.8"></path></g>')
    o.append(tag(tx + 50 * k, ty - 28 * k, "TRUE GOLD", tx + 80 * k, ty - 90 * k) + tag(tx + 54 * k, ty + 6 * k, "BRASS", tx + 110 * k, ty + 50 * k))
    # the balance
    bx, by = w * 0.5, ym - 76 * k
    o.append(f'<g transform="translate({f(bx)} {f(by)}) scale({f(k)})"><path d="M0 0 L 0 150 M-30 150 L 30 150 M-80 10 L 80 -2" stroke="#E8E2D6" stroke-width="4"></path>'
             '<path d="M-80 10 L -100 70 M-80 10 L -60 70 M80 -2 L 60 58 M80 -2 L 100 58" stroke="#E8E2D6" stroke-width="1.6"></path>'
             '<path d="M-106 70 C -100 82 -60 82 -54 70 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M54 58 C 60 70 100 70 106 58 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<circle cx="-80" cy="66" r="8" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="80" cy="52" r="6" fill="#9A7A3A" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')
    # the crucible over the fire
    cx, cy = w * 0.77, ym + 4 * k
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(k)})"><path d="M-50 40 L 50 40 L 40 70 L -40 70 Z" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-30 40 C -20 10 -34 0 -16 -14 C -10 4 0 -4 4 -20 C 14 0 24 6 20 40 Z" fill="#FF8A3D" stroke="#B5121B" stroke-width="1.6"></path>'
             '<path d="M-36 -10 L 36 -10 L 26 -60 L -26 -60 Z" fill="#8A8A94" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<ellipse cx="0" cy="-60" rx="26" ry="6" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
             '<path d="M8 -64 C 30 -80 50 -78 60 -90" stroke="#6A6A70" stroke-width="4" fill="none" stroke-linecap="round"></path></g>')
    o.append(tag(cx + 58 * k, cy - 88 * k, "THE DROSS", cx + 84 * k, cy - 40 * k))
    return "".join(o)

def love_feast(p, w, h, seed):
    """That we should believe in the name of his Son Jesus Christ, and love one another: the brethren at supper together in
    a house by lamplight, sitting on the benches either side of the low table with the bread and the cup on it, one of them
    breaking the bread, a child standing by."""
    b = h * 0.94
    o = [_defs(p), room(w, h, b, wall="#6A4A34", floor="#3A2A20"), lamp_glow(w * 0.5, h * 0.2, max(w, h) * 0.6, f"{p}lg", op=0.5),
         f'<path d="M{f(w * 0.5)} {f(h * 0.1)} L {f(w * 0.5)} {f(h * 0.2)}" stroke="#2A1A10" stroke-width="2"></path>' + clay_lamp(w * 0.5, h * 0.22, max(0.6, h / 300))]
    s = fit(b, max(h * 0.1, b - min(h * 0.66, 250)))
    step = 118 * s
    xl = w * 0.5 - 100 * s - step                                    # two on the left bench facing right, two on the right facing left
    o.append(bench(xl - 40 * s, b, step + 96 * s, s) + bench(w * 0.5 + 100 * s - 56 * s, b, step + 96 * s, s))
    for i in range(2):
        o.append(believer(p, xl + i * step, b, s, i * 2, flip=True, pose="sit"))
    for i in range(2):
        o.append(believer(p, w * 0.5 + 100 * s + i * step, b, s, i * 2 + 1, pose="sit", up=[(-22, -158), (-44, -142), (-62, -138)] if i == 0 else None))
    tx = w * 0.5
    o.append(low_table(tx - 34 * s, b, 68 * s, s)
             + f'<ellipse cx="{f(tx - 12 * s)}" cy="{f(b - 34 * s)}" rx="{f(14 * s)}" ry="{f(5 * s)}" fill="#D8A860" stroke="{INK}" stroke-width="1.4"></ellipse>'
             + gold_cup(tx + 18 * s, b - 31 * s, s * 0.7, color="#B8A07A", fill="#5A1A2A"))
    o.insert(4, child(p, max(w * 0.04, xl - 50 * s), b, s, 1, flip=True))         # behind the bench, at the end of it
    return "".join(o)

def love_light(p, w, h, seed):
    """Beloved, let us love one another: for love is of God … God is love: a warm light falling from above on the
    brethren at a house door (no figure in the light) — two embracing at the threshold, a mother with her child, an old man
    with his hand on a young man's head in blessing."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#5A2A4A", "#FFD8A0"), halo(w * 0.5, h * 0.08, h * 0.55, "#FFFFFF", 0.7),
         rays(w * 0.5, h * 0.08, 22, h * 0.08, h * 0.9, "#FFF4C2", 0.28, 6, a0=20, a1=160),
         houses(w, h, h * 0.7, seed, hmin=0.18, hmax=0.3, lit=True), ground(w, h, h * 0.7, "#C8A878", dy=0)]
    s = fit(b, max(h * 0.16, b - 210))
    o.append(robed(p, w * 0.2, b, s * 0.94, "#5A7A6A", woman=True, veil="#1F3A3A", flip=True) + child(p, w * 0.27, b, s, 1))
    o.append(believer(p, w * 0.44, b, s, 2, flip=True, up=UP_BLESS) + believer(p, w * 0.52, b, s, 0, up=UP_BLESS))
    o.append(robed(p, w * 0.72, b, s, "#6A5A4A", hair="#E8E2D6", beard="#E8E2D6", mantle="#4A5A6A", flip=True, up=[(-22, -158), (-40, -168), (-58, -170)])
             + robed(p, w * 0.82, b + 2, s * 0.92, "#3A5A7A", hair="#2A1A10", belt="#2A1A10"))
    return "".join(o)

def no_fear(p, w, h, seed):
    """There is no fear in love: but perfect love casteth out fear: a night street, the shadows long, and a child running out
    of the dark into a lit doorway where its mother sits on the doorstep with her arms held out."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#05050E", "#1E1840"), mk.stars(20, w, h * 0.3, seed), houses(w, h, h * 0.64, seed, hmin=0.2, hmax=0.34, shut=True, color=("#2A2840", "#24223A", "#302E48", "#282640")),
         ground(w, h, h * 0.64, "#1A1828", dy=0)]
    dx, dw = w * 0.62, max(70, w * 0.16)
    o.append(f'<rect x="{f(dx - dw * 0.6)}" y="{f(h * 0.2)}" width="{f(dw * 2.2)}" height="{f(b - h * 0.2)}" fill="#3A3048" stroke="{INK}" stroke-width="2"></rect>'
             + glow(dx + dw / 2, b - h * 0.2, h * 0.7, "#FFC14D", 0.65, f"{p}g")
             + f'<rect x="{f(dx)}" y="{f(b - h * 0.6)}" width="{f(dw)}" height="{f(h * 0.6)}" fill="#FFD680" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(dx)} {f(b)} L {f(dx - w * 0.2)} {f(h + 10)} L {f(dx + dw + w * 0.1)} {f(h + 10)} L {f(dx + dw)} {f(b)} Z" fill="#FFC14D" opacity="0.3"></path>')
    s = fit(b, max(h * 0.16, b - 220))
    o.append(f'<rect x="{f(dx - 6)}" y="{f(b - 46 * s)}" width="{f(dw + 12)}" height="{f(46 * s)}" fill="#8A7A62" stroke="{INK}" stroke-width="2"></rect>')
    o.append(robed(p, dx + dw * 0.5, b, s * 0.94, "#5A6A8A", woman=True, veil="#1F2F5A", up=[(-22, -158), (-50, -136), (-74, -128)], pose="sit", seat=None))
    o.append(child(p, dx - dw * 0.5, b, s, 0, flip=True, up=[(-22, -158), (-46, -146), (-68, -146)], pose="walk"))
    for k in range(3):
        o.append(f'<path d="M{f(w * (0.02 + 0.1 * k))} {f(b)} L {f(w * (0.1 + 0.1 * k))} {f(h * 0.7)}" stroke="#05050E" stroke-width="{f(w * 0.04)}" opacity="0.5"></path>')
    return "".join(o)

def victory(w, h, seed):
    """This is the victory that hath overcome the world, even our faith: a victor's wreath of laurel lit gold, hanging in the
    morning light above the dark roofs of the city."""
    k = min(w / 420, h / 260)
    cx, cy = w * 0.5, h * 0.42
    o = [sky(w, h, "#2A2A6A", "#FFE6A0"), halo(cx, cy, cy * 0.95, "#FFFFFF", 0.6), rays(cx, cy, 30, 60 * k, cy * 0.95, "#FFF4C2", 0.26, 4),
         houses(w, h, h * 0.94, seed, hmin=0.12, hmax=0.22, color=("#3A3456", "#342E4E", "#403A5E", "#38324E"))]
    R = 78 * k
    for side in (-1, 1):                                              # two sprays of leaves up either side, open at the top
        for i in range(10):
            th = 250 - i * 14 if side < 0 else -70 + i * 14
            t = math.radians(th)
            for off, col in ((-6, "#2E6B3A"), (6, "#9CCB5E")):
                x, y = cx + (R + off * k) * math.cos(t), cy - (R + off * k) * math.sin(t)
                rot = (180 - th if side < 0 else -th) + off * 3
                o.append(f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(k)})"><path d="M0 0 C 7 -8 7 -20 0 -28 C -7 -20 -7 -8 0 0 Z" fill="{col}" stroke="#0D0D0F" stroke-width="1.4"></path></g>')
    o.append(f'<path d="M{f(cx)} {f(cy + R)} C {f(cx - 10 * k)} {f(cy + R + 8 * k)} {f(cx - 16 * k)} {f(cy + R + 16 * k)} {f(cx - 20 * k)} {f(cy + R + 26 * k)} '
             f'M{f(cx)} {f(cy + R)} C {f(cx + 10 * k)} {f(cy + R + 8 * k)} {f(cx + 16 * k)} {f(cy + R + 16 * k)} {f(cx + 20 * k)} {f(cy + R + 26 * k)}" stroke="{GOLD}" stroke-width="{f(5 * k)}" fill="none" stroke-linecap="round"></path>'
             f'<circle cx="{f(cx)}" cy="{f(cy + R)}" r="{f(6 * k)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

def three_witness(p, w, h):
    """There are three who bear witness, the Spirit, and the water, and the blood: and the three agree in one — an emblem
    plate of three medallions: the dove of light (the Spirit), the river's water poured from a pitcher (the water), the cup
    (the blood: the cup only, nothing drawn as blood); a gold line joining the three."""
    o = [plate_bg(w, h, "1 JOHN 5:6–8 · THREE WHO BEAR WITNESS")]
    top = 34; cy = top + 24 + (h - top - 24 - 30) * 0.5; r = min((w - 80) / 7.2, (h - top - 24 - 30) * 0.42)
    xs = (w * 0.2, w * 0.5, w * 0.8)
    names = ("THE SPIRIT", "THE WATER", "THE BLOOD")
    for i, x in enumerate(xs):
        uid = f"{p}tw{i}"
        o.append(f'<defs><radialGradient id="{uid}" cx="0.5" cy="0.4" r="0.7"><stop offset="0" stop-color="{["#FFFDF0", "#E8F6FA", "#FFF4E0"][i]}"></stop>'
                 f'<stop offset="1" stop-color="{["#C8A0D8", "#1F6F9A", "#7A2A3A"][i]}"></stop></radialGradient></defs>'
                 f'<circle cx="{f(x)}" cy="{f(cy)}" r="{f(r)}" fill="url(#{uid})" stroke="{GOLD}" stroke-width="3"></circle>')
        if i == 0: o.append(dove_light(x, cy - r * 0.1, r / 90, uid=f"{p}dv"))
        elif i == 1:
            k = r / 80
            o.append(f'<g transform="translate({f(x - 18 * k)} {f(cy - 30 * k)}) rotate(-40) scale({f(k)})"><path d="M-20 -30 C -24 -10 -24 20 -12 30 L 12 30 C 24 20 24 -10 20 -30 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                     '<path d="M-16 -30 L 16 -30 L 22 -40 L -10 -40 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path></g>'
                     f'<path d="M{f(x + 2 * k)} {f(cy - 36 * k)} C {f(x + 14 * k)} {f(cy - 20 * k)} {f(x + 16 * k)} {f(cy + 10 * k)} {f(x + 14 * k)} {f(cy + 40 * k)}" stroke="#E8F6FA" stroke-width="{f(7 * k)}" fill="none" stroke-linecap="round"></path>'
                     f'<path d="M{f(x - 40 * k)} {f(cy + 48 * k)} C {f(x - 20 * k)} {f(cy + 40 * k)} {f(x + 20 * k)} {f(cy + 56 * k)} {f(x + 44 * k)} {f(cy + 46 * k)}" stroke="#E8F6FA" stroke-width="{f(4 * k)}" fill="none"></path>')
        else:
            o.append(gold_cup(x, cy + r * 0.5, r / 34, fill="#5A1A2A"))
        o.append(plate_label(x, cy - r - 12, names[i], GOLD, 11))
    o.append(f'<path d="M{f(xs[0] + r)} {f(cy)} L {f(xs[1] - r)} {f(cy)} M{f(xs[1] + r)} {f(cy)} L {f(xs[2] - r)} {f(cy)}" stroke="{GOLD}" stroke-width="2"></path>')
    o.append(plate_label(w * 0.5, h - 14, "AND THE THREE AGREE IN ONE", "#E8E2D6", 10))
    return "".join(o)

def idols_cold(p, w, h, seed):
    """Little children, guard yourselves from idols: a colonnade of the city at dusk, images of gold and silver on their
    plinths between the columns, garlanded, and before them a stone altar, cold, its fire out and no one at it."""
    b = h * 0.9
    o = [sky(w, h, "#2A1E3A", "#B8785A"), f'<rect x="-10" y="{f(h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8BCA8" stroke="{INK}" stroke-width="2"></rect>']
    cols = 6
    for i in range(cols + 1):
        x = w * i / cols
        o.append(f'<rect x="{f(x - w * 0.018)}" y="{f(h * 0.18)}" width="{f(w * 0.036)}" height="{f(b - h * 0.18)}" fill="#D8CCB8" stroke="{INK}" stroke-width="1.8"></rect>'
                 + "".join(f'<path d="M{f(x - w * 0.008 + w * 0.008 * j)} {f(h * 0.2)} L {f(x - w * 0.008 + w * 0.008 * j)} {f(b - 4)}" stroke="#A89C88" stroke-width="1"></path>' for j in range(3)))
    o.append(ground(w, h, b, "#5A4A44", dy=0))
    k = min(1.2, h / 300)
    for i in range(cols):
        x = w * (i + 0.5) / cols
        o.append(f'<rect x="{f(x - 24 * k)}" y="{f(b - 40 * k)}" width="{f(48 * k)}" height="{f(40 * k)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.8"></rect>')
        if i % 2: o.append(tall_idol(x, b - 40 * k, 0.8 * k, decked=True))
        else: o.append(small_idol(x, b - 40 * k, 2.2 * k, color=["#E8B830", "#C8C8D0", "#C8A040"][i % 3]))
    o.append(f'<path d="M{f(w * 0.32)} {f(h + 10)} L {f(w * 0.36)} {f(b + h * 0.02)} L {f(w * 0.64)} {f(b + h * 0.02)} L {f(w * 0.68)} {f(h + 10)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.4)}" y="{f(b - h * 0.02)}" width="{f(w * 0.2)}" height="{f(h * 0.06)}" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></rect>'
             f'<ellipse cx="{f(w * 0.5)}" cy="{f(b - h * 0.02)}" rx="{f(w * 0.07)}" ry="{f(h * 0.012)}" fill="#4A4448"></ellipse>')
    return "".join(o)

def elder_desk(p, w, h, seed, stage="write", others=(), night=True):
    """John the elder seated at his low writing table by lamplight, the window on Ephesus behind him. stage "write" his hand
    on the sheet with the reed pen; "laid" the pen laid down beside the inkpot, the sheet unfinished, his hands in his lap
    (2 John 12, 3 John 13); "listen" turned toward brethren standing before him (others: figure functions). The table: a
    sheet of papyrus, the inkpot, the lamp."""
    b = h * 0.95
    s = h * 0.7 / 205
    o = [_defs(p), room(w, h, b, wall="#5A3E2E" if night else "#D8C098", floor="#3A2A20" if night else "#8A6A4A")]
    if night: o.append(lamp_glow(w * 0.48, b - 80 * s, max(w, h) * 0.55, f"{p}lg", op=0.45))
    o.append(_eph_window(w * 0.06, b - 200 * s, min(w * 0.2, 120 * s), min(h * 0.36, 90 * s), night, seed))
    jx = w * 0.3
    tx, tw = jx + 40 * s, 110 * s
    arm = [(-22, -158), (-50, -130), (-82, -118)] if stage == "write" else None
    o.append(john_fig(p, jx, b, s, flip=True, up=arm, pose="sit"))
    if stage == "write":
        o.append(f'<g transform="translate({f(jx)} {f(b)}) scale({f(-s)} {f(s)})">' + f'<g transform="translate(-84 {-118 + 48}) rotate(-30)"><path d="M0 0 L 3 -5 L 3 -40 L -3 -40 L -3 -5 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.4"></path></g></g>')
    o.append(low_table(tx, b, tw, s))
    ty = b - 31 * s
    o.append(f'<g transform="rotate(-4 {f(tx + tw * 0.4)} {f(ty)})">' + open_letter(tx + tw * 0.08, ty - 16 * s, tw * 0.5, 14 * s, rows=3, seed=seed) + '</g>')
    o.append(inkpot(tx + tw * 0.72, ty, s * 0.6) + clay_lamp(tx + tw * 0.9, ty - 1 * s, s * 0.55))
    if stage == "laid":
        o.append(reed_pen(tx + tw * 0.62, ty - 2 * s, s * 0.55, rot=84))
    for i, fig in enumerate(others):
        o.append(fig(p, w * (0.8 - 0.13 * i), b, s * (0.98 - 0.02 * i), flip=True))
    return "".join(o)
