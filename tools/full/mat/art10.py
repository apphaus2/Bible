"""Drawings for Matthew 26: the court of Caiaphas at night; the house of Simon the leper and the alabaster cruse; the thirty
pieces of silver weighed; the guest-chamber made ready; the last supper — the twelve at the table, the bread and the cup; the
mount of Olives by moonlight; Gethsemane — Jesus fallen on his face alone in the light among the olive trees, the three
asleep; the torches and staves coming into the garden; the sword dropped (the blow told in words only); the garden empty; the
hall of Caiaphas; the mocking told in words over the shut door; the fire in the court and the maid; the cock crowing at dawn.
Built on mat.art9."""
from mat.art9 import *
from mat.art9 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from ecc.art import loaf
import exodus as E

def jesus_kneel(x, y, s, flip=False):
    """Jesus kneeling in prayer, bowed to the ground (exodus.kneel in his colours)."""
    return E.kneel(x, y, s, color=JESUS_TUNIC, skin=JESUS_SKIN, flip=flip)

def torch(x, y, s=1.0, uid="tc"):
    return (f'<path d="M{f(x)} {f(y)} L {f(x + 4 * s)} {f(y - 60 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>'
            + glow(x + 4 * s, y - 70 * s, 50 * s, "#FFC14D", 0.8, uid) + E.flame(x + 4 * s, y - 58 * s, 12 * s, 30 * s, 0.1))

def priests_court(p, w, h, seed):
    """The court of the high priest by night: a colonnade lit by lamps, the chief priests and elders gathered in council, one
    in white and gold at their head."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#2A1A3A")]
    for x in (0.06, 0.3, 0.7, 0.94):
        o.append(f'<rect x="{f(w * x - 16)}" y="{f(h * 0.1)}" width="32" height="{f(b - h * 0.1)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#4A3A34" stroke="{INK}" stroke-width="2"></rect>')
    for x in (0.18, 0.82):
        o.append(glow(w * x, h * 0.3, h * 0.2, "#FFC14D", 0.6, f"{p}l{int(x * 10)}") + A.lamp(w * x, h * 0.3, max(0.6, h / 360)))
    o.append(pavement(w, h, b - h * 0.04, color="#4A3A34", line="#3A2A24"))
    s = fit(b, max(h * 0.26, b - 220))
    o.append(scribe_fig(p, w * 0.5, b, s * 1.02, white=True))
    for i, x in enumerate((0.36, 0.42, 0.58, 0.64, 0.72)):
        o.append(scribe_fig(p, w * x, b, s * 0.94, white=i % 2 == 1, flip=x > 0.5))
    return "".join(o)

def anointing(p, w, h, seed):
    """In the house of Simon the leper at Bethany: Jesus reclining at meat, a woman standing behind him pouring the ointment
    from an alabaster cruse upon his head, the disciples about the table looking on."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.84, w * 0.08)), A.lamp(w * 0.12, h * 0.3, max(0.6, h / 300))]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(b - 36 * s)}" width="{f(w * 0.76)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(5): o.append(loaf(w * (0.5 + 0.08 * i), b - 40 * s, s * 0.6))
    o.append(jesus_seated(w * 0.36, b, s * 0.82))
    cruse = '<path d="M-70 -196 C -80 -186 -78 -170 -68 -166 L -56 -166 C -48 -172 -48 -186 -58 -196 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(woman_fig(p, w * 0.36 + 90 * s, b, s * 0.94, "#8A2A3A", "#C2456A", flip=True, up=[(-22, -158), (-46, -184), (-62, -190)], extra=cruse))
    o.append(f'<path d="M{f(w * 0.36 + 90 * s - 62 * s * 0.94)} {f(b - 168 * s * 0.94)} q -10 20 -20 40" stroke="#E8C060" stroke-width="3" fill="none"></path>')
    for i, x in enumerate((0.66, 0.76, 0.86)):
        o.append(disciple_seated(w * x, b, s * 0.74, i + 4, flip=True))
    o.append(disciple_seated(w * 0.14, b, s * 0.74, 6))
    return "".join(o)

def silver(p, w, h, seed):
    """They weighed unto him thirty pieces of silver: a balance on a table, the silver coins piled in one pan and scattered
    on the cloth beside it, a lamp — no one drawn."""
    r = random.Random(seed); b = h * 0.8
    o = [bgr(w, h, "#1A1630"), glow(w * 0.5, h * 0.4, h * 0.6, "#C8C8D8", 0.3, f"{p}g"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A2A1E" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.6, h / 200)
    cx = w * 0.42
    o.append(f'<path d="M{f(cx)} {f(b)} L {f(cx)} {f(b - 90 * k)} M{f(cx - 70 * k)} {f(b - 86 * k)} L {f(cx + 70 * k)} {f(b - 94 * k)}" stroke="#C8963E" stroke-width="{f(4 * k)}"></path>')
    for dx, dy in ((-70, -86), (70, -94)):
        o.append(f'<path d="M{f(cx + dx * k)} {f(b + dy * k)} L {f(cx + dx * k - 26 * k)} {f(b + dy * k + 40 * k)} M{f(cx + dx * k)} {f(b + dy * k)} L {f(cx + dx * k + 26 * k)} {f(b + dy * k + 40 * k)}" stroke="#8A6A3A" stroke-width="1.6"></path>'
                 f'<path d="M{f(cx + dx * k - 30 * k)} {f(b + dy * k + 40 * k)} Q {f(cx + dx * k)} {f(b + dy * k + 56 * k)} {f(cx + dx * k + 30 * k)} {f(b + dy * k + 40 * k)} Z" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></path>')
    for i in range(9):
        o.append(f'<ellipse cx="{f(cx - 70 * k + r.uniform(-16, 16) * k)}" cy="{f(b - 48 * k - i * 2 * k)}" rx="{f(7 * k)}" ry="{f(3 * k)}" fill="#D8D8E0" stroke="{INK}" stroke-width="1"></ellipse>')
    for _ in range(21):
        o.append(f'<ellipse cx="{f(w * 0.66 + r.uniform(0, w * 0.26))}" cy="{f(b + r.uniform(4, h * 0.14))}" rx="{f(7 * k)}" ry="{f(3 * k)}" fill="#D8D8E0" stroke="{INK}" stroke-width="1"></ellipse>')
    o.append(A.lamp(w * 0.12, b - 4, k * 0.8))
    return "".join(o)

def guest_chamber(p, w, h, seed):
    """They made ready the passover: an upper room, the low table set with unleavened bread, cups and the dish, lamps lit, two
    of the disciples laying the cloth."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#8A6A5A", floor="#5A4A3A", window=(w * 0.84, w * 0.08), night_=False)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<rect x="{f(w * 0.16)}" y="{f(b - 36 * s)}" width="{f(w * 0.6)}" height="{f(12 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(6): o.append(loaf(w * (0.2 + 0.1 * i), b - 40 * s, s * 0.5) + cup(w * (0.25 + 0.1 * i), b - 36 * s, s * 0.12))
    o.append(disciple(p, w * 0.1, b, s, "peter") + disciple(p, w * 0.86, b, s, "john", flip=True, up=UP_BLESS))
    o.append(A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300)))
    return "".join(o)

def supper(p, w, h, seed, bread=False, cupup=False):
    """He was sitting at meat with the twelve: the long low table at night under the lamps, Jesus in the midst, six of the
    twelve either side; bread=True: the loaf broken in his hands; cupup=True: the cup lifted."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#4A3438", floor="#3A2A2A", window=(w * 0.06, w * 0.08), night_=True, seed=seed)]
    for x in (0.3, 0.7): o.append(glow(w * x, h * 0.26, h * 0.2, "#FFC14D", 0.6, f"{p}l{int(x * 10)}") + A.lamp(w * x, h * 0.26, max(0.6, h / 360)))
    s = fit(b, max(h * 0.26, b - 220))
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(b - 32 * s)}" width="{f(w * 0.92)}" height="{f(12 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(6):
        o.append(disciple_seated(w * (0.06 + 0.07 * i), b, s * 0.66, i))
        o.append(disciple_seated(w * (0.94 - 0.07 * i), b, s * 0.66, i + 6, flip=True))
    o.append(jesus_seated(w * 0.5, b, s * 0.82))
    if bread:
        o.append(f'<g transform="translate({f(w * 0.5 + 40 * s)} {f(b - 70 * s)})">{loaf(-8 * s, 0, s * 0.6)}{loaf(10 * s, 4 * s, s * 0.5)}</g>')
    if cupup:
        o.append(glow(w * 0.5 + 44 * s, b - 90 * s, 30 * s, "#FFE680", 0.8, f"{p}c") + cup(w * 0.5 + 44 * s, b - 70 * s, s * 0.22))
    return "".join(o)

def olivet_night(p, w, h, seed):
    """When they had sung a hymn, they went out into the mount of Olives: the twelve and Jesus on the path under the moon,
    the city dark behind them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), jerusalem_far(w, h, seed, tone="night", lit=True), moon(w * 0.84, h * 0.16, max(8, h * 0.04)),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1E2A1E" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.4, b - 200))
    o.append(jesus(p, w * 0.2, b, s, glow=True))
    for i in range(6):
        o.append(disciple(p, w * (0.32 + 0.1 * i), b - (i % 2) * 4, s * 0.94, TWELVE[i]))
    return "".join(o)

def gethsemane(p, w, h, seed, sleeping=True, praying=True):
    """Gethsemane at night: the twisted olive trees under the moon; Jesus fallen on his face a little apart, alone, a soft
    cold light on him; Peter, James and John lying asleep under the trees."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, *LIE), night(w, h, seed, n=50, top="#05051A", bot="#1E1838"), moon(w * 0.2, h * 0.14, max(8, h * 0.04)),
         ground(w, h, h * 0.66, "#1E2A1E", dy=0)]
    for x in (0.06, 0.4, 0.64, 0.96):
        o.append(olive(w * x, h * 0.78, h / 300, seed=seed + int(x * 10)).replace("#7A8A5A", "#3A4A3A"))
    s = fit(b, max(h * 0.3, b - 220))
    if sleeping:
        for i, (x, c) in enumerate(((0.56, ROBES["peter"]), (0.72, ROBES["james"]), (0.86, ROBES["john"]))):
            o.append(f'<g transform="translate({f(w * x + 90 * s * 0.5)} {f(b - 2)}) scale({f(s * 0.5)})" fill="{c}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    if praying:
        o.append(glow(w * 0.24, b - 40 * s, 120 * s, "#9AA8C8", 0.7, f"{p}g") + jesus_kneel(w * 0.24, b, s * 0.9))
    return "".join(o)

def arrest(p, w, h, seed, sword=False, empty=False):
    """The multitude with swords and staves, from the chief priests: torches coming between the olive trees, men with staves
    and the high priest's servants, Judas at their head going to Jesus; sword=True: a sword lying dropped on the ground in
    the torchlight (the blow is told in words only); empty=True: the garden left empty, a torch dropped, the disciples
    fled."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, n=40, top="#05051A", bot="#2A1A1A"), ground(w, h, h * 0.66, "#1E2A1E", dy=0)]
    for x in (0.08, 0.92): o.append(olive(w * x, h * 0.78, h / 300, seed=seed + int(x * 10)).replace("#7A8A5A", "#3A4A3A"))
    s = fit(b, max(h * 0.3, b - 220))
    if empty:
        o.append(f'<g transform="rotate(70 {f(w * 0.5)} {f(b)})">' + torch(w * 0.5, b, s * 0.8, f"{p}t") + '</g>')
        return "".join(o)
    staff = '<path d="M30 -150 L 44 -230" stroke="#5A3A22" stroke-width="5"></path>'
    for i, x in enumerate((0.58, 0.68, 0.78, 0.88, 0.96)):
        o.append(man(p, w * x, b - (i % 2) * 6, s * 0.92, random.Random(seed + i).choice(["#3A3A4A", "#5A4A3A", "#4A3A3A"]), flip=True, extra=staff if i % 2 else ""))
        if i % 2 == 0: o.append(torch(w * x - 30 * s, b - 120 * s, s * 0.7, f"{p}t{i}"))
    o.append(mk.person(p, round(w * 0.44), round(b), round(s, 3), body="#B98A6E", cloth=ROBES["judas"], kind="Robe", sw=3, flip=True,
                       extra=A.headcloth(ROBES["judas"], cord="#3A2214") + A.BLACK_BEARD))
    o.append(jesus(p, w * 0.28, b, s))
    o.append(disciple(p, w * 0.12, b, s * 0.96, "peter"))
    if sword:
        o.append(f'<path d="M{f(w * 0.2)} {f(b + 2)} L {f(w * 0.36)} {f(b - 6)}" stroke="#C8C8D0" stroke-width="{f(4 * s)}"></path><path d="M{f(w * 0.2)} {f(b - 6)} L {f(w * 0.2)} {f(b + 10)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>')
    return "".join(o)

def caiaphas_hall(p, w, h, seed):
    """The house of Caiaphas: the high priest on his seat in the lamp-lit hall, the scribes and elders ranged on either side,
    Jesus standing bound before them, silent."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A1A2A")]
    for x in (0.06, 0.94):
        o.append(f'<rect x="{f(w * x - 16)}" y="-10" width="32" height="{f(b + 10)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>')
    o.append(glow(w * 0.5, h * 0.2, h * 0.3, "#FFC14D", 0.4, f"{p}g") + A.lamp(w * 0.5, h * 0.18, max(0.6, h / 360)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3A34" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.26, b - 220))
    o.append(f'<rect x="{f(w * 0.76)}" y="{f(b - 120 * s)}" width="{f(80 * s)}" height="{f(120 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(seated(w * 0.8, b - 50 * s, s * 0.84, "#E8E2D6", head="#F3EFE6", beard="#9A948A", band=True, flip=True))
    for i, x in enumerate((0.12, 0.2, 0.62, 0.68)):
        o.append(scribe_fig(p, w * x, b, s * 0.9, white=i % 2 == 0, flip=x > 0.5))
    o.append(jesus(p, w * 0.42, b, s, glow=False))
    o.append(f'<path d="M{f(w * 0.42 - 20 * s)} {f(b - 100 * s)} L {f(w * 0.42 + 20 * s)} {f(b - 96 * s)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}"></path>')
    return "".join(o)

def shut_door(p, w, h, seed):
    """The door of the high priest's house shut and barred at night, lamplight showing under it — what was done within is
    told in words only."""
    b = h * 0.94
    o = [bgr(w, h, "#2A2228")]
    for k in range(8):
        y = h * k / 7
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#3A3238" stroke-width="2"></path>')
    o.append(f'<rect x="{f(w * 0.34)}" y="{f(h * 0.12)}" width="{f(w * 0.32)}" height="{f(b - h * 0.12)}" fill="#5A3A22" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.5)}" stroke="#2A1A10" stroke-width="10"></path>'
             f'<rect x="{f(w * 0.34)}" y="{f(b - 4)}" width="{f(w * 0.32)}" height="6" fill="#FFC14D"></rect>'
             f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#1E1A20"></rect>')
    return "".join(o)

def court_fire(p, w, h, seed, maid=True, porch=False):
    """Peter sitting without in the court by the officers' fire at night, a maid standing over him pointing; porch=True: at
    the gate-porch, another maid and the bystanders."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), night(w, h, seed, n=40, top="#05051A", bot="#2A1A2A")]
    o.append(f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#3A3038" stroke="{INK}" stroke-width="2"></rect>')
    if porch:
        o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.7)} L {f(w * 0.6)} {f(h * 0.36)} Q {f(w * 0.72)} {f(h * 0.24)} {f(w * 0.84)} {f(h * 0.36)} L {f(w * 0.84)} {f(h * 0.7)} Z" fill="#0B0B1A" stroke="{INK}" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.7, "#2A2228", dy=0))
    s = fit(b, max(h * 0.3, b - 220))
    fx = w * 0.36
    o.append(glow(fx, b - 20 * s, 140 * s, "#FF8A3D", 0.6, f"{p}f") + E.blaze(fx, b, 60 * s, 70 * s, seed, n=4))
    o.append(seated(fx - 90 * s, b, s * 0.82, ROBES["peter"], head=None, beard="#4A4440"))
    o.append(seated(fx + 90 * s, b, s * 0.8, "#3A3A4A", head="#3A3A4A", beard="#1A1210", flip=True))
    if maid:
        o.append(woman_fig(p, w * (0.7 if not porch else 0.9), b, s * 0.9, "#5A6A4A", "#8A9A6A", flip=True, up=UP_BLESS))
    if porch:
        o.append(man(p, w * 0.66, b, s * 0.92, "#3A3A4A", flip=True) + man(p, w * 0.78, b, s * 0.9, "#5A4A3A", flip=True))
    return "".join(o)

def cockcrow(p, w, h, seed):
    """Straightway the cock crew: a cock on the wall of the court against the first grey light of dawn."""
    o = [sky(w, h, "#1A1A3A", "#C8906A"), f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#3A3038" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.6, h / 200)
    cx, cy = w * 0.5, h * 0.62
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(k)})">'
             '<path d="M-40 0 C -50 -30 -30 -50 -6 -50 C 4 -64 12 -80 22 -84 C 34 -86 40 -76 38 -66 L 50 -62 L 38 -58 C 38 -44 30 -24 20 -10 L 26 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-40 -6 C -70 -30 -66 -70 -44 -84 C -48 -60 -44 -40 -30 -26 Z" fill="#1F4A3A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M20 -86 l 4 -12 l 4 8 l 4 -10 l 2 12" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.2"></path>'
             '<path d="M36 -60 C 40 -50 36 -46 32 -48" fill="#D7261E" stroke="#0D0D0F" stroke-width="1"></path><circle cx="30" cy="-70" r="2" fill="#0D0D0F"></circle>'
             '<path d="M0 0 L -4 12 M10 0 L 12 12" stroke="#C8963E" stroke-width="3"></path></g>')
    o.append(f'<path d="M{f(cx + 52 * k)} {f(cy - 70 * k)} q 20 -6 30 -20 M{f(cx + 54 * k)} {f(cy - 60 * k)} q 26 0 40 -8" stroke="#F3EFE6" stroke-width="2" fill="none"></path>')
    return "".join(o)
