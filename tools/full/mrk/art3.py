"""Drawings for Mark 5:1–6:29. The tombs of the Gerasenes with no one in them, only the broken chains and fetters on the
rocks (the man's torment is told in words; the unclean spirits are never drawn); the empty sea under the steep; the man
sitting clothed at Jesus' feet; the road through the ten cities; Jairus at his feet by the sea; the damsel risen from her
bed; the twelve anointing the sick; the doorway of Herod's palace with no one in it; the prison door shut and barred.
Built on mrk.art2."""
from mrk.art2 import *
from mrk.art2 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette
import random, math

GER_C = "#E8E0CC"                                  # the Gerasene's clean undyed robe

def gerasene_fig(p, x, y, s, flip=False, up=None):
    """The man of the Gerasenes, healed: a clean undyed robe, dark curls and a short black beard."""
    hair = '<path d="M-14 -186 C -18 -204 16 -206 14 -186 L 14 -178 L -14 -178 Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=GER_C, kind="Robe", sw=3, flip=flip, up=up, extra=hair + A.BLACK_BEARD)

def chains(x, y, k, seed, n=2):
    """Broken chains and a fetter lying on a rock: links in iron grey, the snapped ends apart."""
    r = random.Random(seed); o = []
    for c in range(n):
        x0 = x + c * 70 * k; y0 = y + r.uniform(-6, 6) * k; a = r.uniform(-0.3, 0.3)
        for i in range(6):
            cx = x0 + i * 13 * k * math.cos(a); cy = y0 + i * 13 * k * math.sin(a) + (3 * k if i % 2 else 0)
            o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(8 * k)}" ry="{f(4.5 * k)}" fill="none" stroke="#6A6A72" stroke-width="{f(3 * k)}" '
                     f'transform="rotate({f(math.degrees(a) + (90 if i % 2 else 0) * 0.3)} {f(cx)} {f(cy)})"></ellipse>')
        o.append(f'<path d="M{f(x0 + 80 * k * math.cos(a))} {f(y0 + 80 * k * math.sin(a) - 4 * k)} l {f(6 * k)} {f(-6 * k)}" stroke="#6A6A72" stroke-width="{f(3 * k)}"></path>')
    o.append(f'<path d="M{f(x - 30 * k)} {f(y + 8 * k)} a {f(12 * k)} {f(9 * k)} 0 1 1 {f(20 * k)} {f(4 * k)}" fill="none" stroke="#5A5A62" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(x - 6 * k)} {f(y + 6 * k)} l {f(6 * k)} {f(3 * k)}" stroke="#5A5A62" stroke-width="{f(4 * k)}"></path>')
    return "".join(o)

def empty_tombs(p, w, h, seed, night=True):
    """The tombs in the mountain side over the sea, their doors dark, no one in them; on the rocks before them the chains
    rent asunder and the fetters broken in pieces (night and day he was crying out — told in words only)."""
    b = h * 0.94
    top, bot = ("#0B0B2A", "#3A2A5A") if night else ("#6A6A8A", "#E8C8A0")
    o = [sky(w, h, top, bot), mk.stars(30, w, h * 0.3, seed) if night else "", moon(w * 0.86, h * 0.14, max(8, h * 0.04)) if night else "",
         lake(w, h, h * 0.56, seed, color="#1A3A5A" if night else "#1F6F9A", n=6, op=0.4),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.12)} {f(w * 0.7)} {f(h * 0.14)} {f(w * 0.86)} {f(h * 0.4)} L {f(w * 0.96)} {f(h + 10)} Z" '
         f'fill="{"#4A4048" if night else "#8A7A6A"}" stroke="{INK}" stroke-width="2.4"></path>']
    for i in range(5):
        x = w * (0.1 + 0.17 * i); y = h * (0.34 + 0.06 * (i % 2)) + (h * 0.06 if i in (0, 4) else 0)
        dw, dh = w * 0.04, h * 0.12
        o.append(f'<path d="M{f(x - dw)} {f(y + dh)} L {f(x - dw)} {f(y)} Q {f(x)} {f(y - dh * 0.5)} {f(x + dw)} {f(y)} L {f(x + dw)} {f(y + dh)} Z" fill="#0A0808" stroke="{INK}" stroke-width="2"></path>'
                 f'<circle cx="{f(x + dw * 1.7)}" cy="{f(y + dh * 0.62)}" r="{f(dh * 0.4)}" fill="{"#6A6060" if night else "#9A8A7A"}" stroke="{INK}" stroke-width="1.8"></circle>')
    k = max(0.6, h / 300)
    for x, y in ((0.14, 0.86), (0.52, 0.9), (0.72, 0.8)):
        o.append(f'<ellipse cx="{f(w * x + 30 * k)}" cy="{f(h * y + 10 * k)}" rx="{f(60 * k)}" ry="{f(16 * k)}" fill="{"#5A5058" if night else "#A89A8A"}" stroke="{INK}" stroke-width="2"></ellipse>')
        o.append(chains(w * x, h * y, k, seed + int(x * 100)))
    return "".join(o)

def empty_sea(p, w, h, seed):
    """And they were drowned in the sea: the steep falling into the water, the sea closing over, rings of foam spreading —
    nothing living drawn; the keepers' footprints running back up the slope."""
    r = random.Random(seed)
    o = [sky(w, h, "#5A5A7A", "#D8B8A0"), lake(w, h, h * 0.5, seed, color="#2A5A7A", n=10, op=0.5),
         f'<path d="M-10 {f(h * 0.16)} L {f(w * 0.24)} {f(h * 0.2)} C {f(w * 0.32)} {f(h * 0.32)} {f(w * 0.36)} {f(h * 0.5)} {f(w * 0.4)} {f(h * 0.62)} L {f(w * 0.4)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="2.4"></path>']
    for i in range(7):
        cx, cy = w * r.uniform(0.46, 0.94), h * r.uniform(0.56, 0.9); rx = w * r.uniform(0.03, 0.08)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(rx * 0.25)}" fill="none" stroke="#E8F6FA" stroke-width="2" opacity="0.8"></ellipse>'
                 f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx * 1.7)}" ry="{f(rx * 0.42)}" fill="none" stroke="#E8F6FA" stroke-width="1.2" opacity="0.5"></ellipse>')
    return "".join(o)

def gerasene_sitting(p, w, h, seed):
    """They behold him sitting, clothed and in his right mind: on the shore below the tombs the man sits at Jesus' feet in a
    clean robe, quiet; the people come out from the city stand off up the slope, afraid; the boat drawn up at the water."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), lake(w, h, h * 0.46, seed, n=6),
         f'<path d="M{f(w * 0.46)} {f(h + 10)} L {f(w * 0.52)} {f(h * 0.3)} C {f(w * 0.66)} {f(h * 0.18)} {f(w * 0.86)} {f(h * 0.16)} {f(w + 10)} {f(h * 0.22)} L {f(w + 10)} {f(h + 10)} Z" fill="#9A8A6A" stroke="{INK}" stroke-width="2.4"></path>',
         shore(w, h, h * 0.8, x0=-10, x1=w * 0.6)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(boat(p, w * 0.08, h * 0.8, s * 0.6, mast=False))
    o.append(jesus(p, w * 0.28, b, s))
    o.append(seated(w * 0.42, b, s * 0.8, GER_C, head="#1A1210", beard="#1A1210", flip=True))
    o.append(crowd(p, w * 0.66, w * 0.96, h * 0.62, h * 0.62 - 150 * s * 0.6, 6, seed, flip=True))
    o.append(disciple(p, w * 0.14, b, s * 0.94, "peter") + disciple(p, w * 0.54, b, s * 0.92, "john", flip=True))
    return "".join(o)

def decapolis(p, w, h, seed, jesus_=False):
    """He went his way, and began to publish in Decapolis: the road winding through the hills from town to town, the man in
    his clean robe on it, his arm raised as he tells it, people standing to hear at a town gate (jesus_=True: Jesus and
    the disciples on the road, the people coming out to him)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#9AAA7A", amp=14, step=90)]
    for i, (x, y) in enumerate(((0.1, 0.42), (0.3, 0.38), (0.52, 0.42), (0.74, 0.36), (0.92, 0.44))):
        o.append(hill_town(w * x, h * y, w * 0.1, h * 0.08, seed + i, hill="#A8B07A"))
    o.append(ground(w, h, h * 0.46, "#C8B07A", dy=0))
    o.append(f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.66)} {f(w * 0.74)} {f(h * 0.46)}" stroke="#E0D0A8" stroke-width="{f(max(6, h * 0.05))}" fill="none"></path>')
    o.append(walls(w * 0.62, w + 10, h * 0.7, h * 0.24, seed, towers=2))
    s = fit(b, max(h * 0.24, b - 230))
    if jesus_:
        o.append(jesus(p, w * 0.3, b, s) + disciple(p, w * 0.18, b, s * 0.96, "peter") + disciple(p, w * 0.08, b, s * 0.94, "john"))
    else:
        o.append(gerasene_fig(p, w * 0.34, b, s, up=UP_HIGH))
    o.append(crowd(p, w * 0.5, w * 0.9, b, b - 160 * s, 5, seed, flip=True))
    return "".join(o)

def jairus_feet(p, w, h, seed):
    """There cometh one of the rulers of the synagogue, Jaïrus by name, and falleth at his feet: on the beach by the sea,
    the ruler in his teal headcloth kneeling before Jesus, the great multitude about them, the boat at the water."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.42, seed, n=8),
         shore(w, h, h * 0.68)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(boat(p, w * 0.14, h * 0.66, s * 0.6, mast=True))
    o.append(crowd(p, w * 0.6, w * 0.98, b - 10 * s, b - 10 * s - 160 * s, 7, seed, flip=True))
    o.append(jesus(p, w * 0.32, b, s, flip=True, up=UP_TOUCH))
    o.append(E.kneel(w * 0.5, b, s * 0.9, color="#2A5A5A", flip=True, skin=SKIN))
    return "".join(o)

def talitha(p, w, h, seed, tall=None):
    """Talitha cumi — and straightway the damsel rose up, and walked: within the ruler's house, the girl of twelve risen from
    her bed in her white dress, her hand in Jesus' hand; her father and mother at the door; Peter, James and John
    (tall: the figures' height as a share of the panel, for a title page)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#C8A878", window=(w * 0.1, w * 0.08)), glow(w * 0.42, b - h * 0.3, h * 0.5, "#FFF4C2", 0.55, f"{p}g")]
    s = fit(b, b - h * tall) if tall else fit(b, max(h * 0.2, b - 240))
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(b - 40 * s)}" width="{f(w * 0.24)}" height="{f(22 * s)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.5)}" y="{f(b - 46 * s)}" width="{f(w * 0.24)}" height="{f(8 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    js, gs = s, s * 0.72
    jx = w * 0.3; gx = jx + 36 * js + 46 * gs
    o.append(jesus(p, jx, b, js, flip=True, up=[(-22, -158), (-30, -134), (-36, -124)]))
    o.append(woman(p, gx, b, gs, "#F3EFE6", up=[(-22, -158), (-36, -132), (-46, -122)]))
    o.append(man(p, w * 0.84, b, s * 0.96, "#2A5A5A", flip=True, kind="Robe", extra=A.headcloth("#2A5A5A", cord="#3A2214") + A.BLACK_BEARD)
             + woman_fig(p, w * 0.93, b, s * 0.9, "#6A3A5A", "#5A4A6A", flip=True))
    o.append(disciple(p, w * 0.15, b, s * 0.94, "peter", flip=True) + disciple(p, w * 0.07, b, s * 0.92, "james", flip=True))
    return "".join(o)

def anoint_sick(p, w, h, seed):
    """They anointed with oil many that were sick, and healed them: in a village street, one of the twelve kneeling by a
    sick man on his pallet, pouring oil from a horn; another raising a man to his feet; people at the doors."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.78, seed, hmin=0.3, hmax=0.46), pavement(w, h, h * 0.78)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(on_bed(p, w * 0.3, b - 16 * s, w * 0.24, cloth="#B8A88A"))
    horn = '<path d="M-60 -122 C -70 -130 -80 -128 -84 -118 L -70 -112 Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="1.4"></path>'
    o.append(E.kneel(w * 0.5, b, s * 0.86, color=ROBES["andrew"], flip=True, skin="#B98A6E"))
    o.append(disciple(p, w * 0.7, b, s, "thomas", flip=True, up=UP_TOUCH) + man(p, w * 0.8, b, s * 0.92, "#8A7A5A", flip=True))
    o.append(crowd(p, w * 0.04, w * 0.16, b - 30 * s, b - 30 * s - 140 * s, 2, seed))
    return "".join(o)

def palace_door(p, w, h, seed):
    """A doorway of Herod's palace at night: a curtained arch, lamplight from the hall beyond, a stair down to the women's
    rooms — no one drawn (what was asked and answered is told in words)."""
    b = h * 0.94
    o = [bgr(w, h, "#1E1420")]
    for k in range(9):
        y = h * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2E2230" stroke-width="2"></path>')
    ax, aw = w * 0.5, w * 0.26
    o.append(f'<path d="M{f(ax - aw / 2)} {f(b)} L {f(ax - aw / 2)} {f(h * 0.34)} Q {f(ax)} {f(h * 0.08)} {f(ax + aw / 2)} {f(h * 0.34)} L {f(ax + aw / 2)} {f(b)} Z" fill="#FFC14D" stroke="{INK}" stroke-width="3"></path>'
             + glow(ax, h * 0.6, h * 0.5, "#FFC14D", 0.4, f"{p}g")
             + f'<path d="M{f(ax - aw / 2)} {f(h * 0.34)} Q {f(ax - aw * 0.3)} {f(h * 0.6)} {f(ax - aw * 0.36)} {f(b)} L {f(ax - aw / 2)} {f(b)} Z" fill="#6A1A3A" stroke="{INK}" stroke-width="2"></path>'
             + f'<path d="M{f(ax + aw / 2)} {f(h * 0.34)} Q {f(ax + aw * 0.3)} {f(h * 0.6)} {f(ax + aw * 0.36)} {f(b)} L {f(ax + aw / 2)} {f(b)} Z" fill="#6A1A3A" stroke="{INK}" stroke-width="2"></path>')
    for x in (0.18, 0.82):
        o.append(f'<rect x="{f(w * x - 16)}" y="{f(h * 0.1)}" width="32" height="{f(b - h * 0.1)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2A2E"></rect>')
    return "".join(o)

def prison_shut(p, w, h, seed):
    """The prison at night: the iron-bound door in the stone wall shut and barred, a torch in its ring beside it, the light
    going out in the small grating — no one drawn (the beheading is told in words only)."""
    b = h * 0.94
    o = [bgr(w, h, "#2A2428")]
    r = random.Random(seed)
    for k in range(10):
        y = h * k / 9
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#3E363C" stroke-width="2"></path>')
        for m in range(7):
            x = w * (m + (0.5 if k % 2 else 0)) / 6
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + h / 9)}" stroke="#3E363C" stroke-width="2"></path>')
    dx, dw = w * 0.36, w * 0.28
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.14)}" width="{f(dw)}" height="{f(b - h * 0.14)}" fill="#4A3020" stroke="{INK}" stroke-width="3"></rect>')
    for k in range(1, 4):
        o.append(f'<path d="M{f(dx)} {f(h * 0.14 + (b - h * 0.14) * k / 4)} L {f(dx + dw)} {f(h * 0.14 + (b - h * 0.14) * k / 4)}" stroke="#2A2A2E" stroke-width="6"></path>')
    o.append(f'<rect x="{f(dx + dw * 0.36)}" y="{f(h * 0.22)}" width="{f(dw * 0.28)}" height="{f(h * 0.1)}" fill="#1A1010" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(dx + dw * (0.4 + 0.07 * k))} {f(h * 0.22)} L {f(dx + dw * (0.4 + 0.07 * k))} {f(h * 0.32)}" stroke="#6A6A72" stroke-width="2.4"></path>' for k in range(4))
             + f'<path d="M{f(dx - 20)} {f(h * 0.58)} L {f(dx + dw + 20)} {f(h * 0.58)}" stroke="#1A1A1E" stroke-width="12"></path>')
    o.append(torch(w * 0.8, h * 0.44, max(0.6, h / 300), uid=f"{p}tc"))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#1E1A1E"></rect>')
    return "".join(o)
