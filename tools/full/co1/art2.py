"""Drawings for 1 Corinthians 5–7 (chapter 2 of the volume), on co1.art. Restraint governs these chapters: 5:1–13 are words
over a shut door and an empty house front at night, 5:5 (Satan) words only; 6:9–20 words over dark, empty streets and the
temple; 7 words over plain household scenes — a lamp at a table, a house door, a courtyard, a well — nothing sexual drawn,
7:5 (Satan) words only. The leaven and the unleavened bread with the passover lamb as an emblem (a lamb standing in light,
no slaughter); the law court at Corinth."""
from co1.art import *
from co1.art import f, INK, _seated_lap
from genesis.art5 import well
from mat.art import empty_street, woman_fig

# ---- 1 Corinthians 5 ---------------------------------------------------------------------------------------------------
def shut_house(w, h, seed, lamp=True):
    """A house front in Corinth at night, its door shut and barred, a thread of lamplight under it; the street empty."""
    b = h * 0.9
    o = [sky(w, h, "#05051A", "#1E1650"), mk.stars(30, w, h * 0.3, seed)]
    o.append(houses(w, h, b, seed, hmin=0.3, hmax=0.42, shut=True))
    hx, hw, ht = w * 0.34, w * 0.32, h * 0.12                   # the one house, near
    o.append(f'<rect x="{f(hx)}" y="{f(ht)}" width="{f(hw)}" height="{f(b - ht)}" fill="#4A3E3A" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(hx - 8)}" y="{f(ht - 10)}" width="{f(hw + 16)}" height="12" fill="#3A302C" stroke="{INK}" stroke-width="2"></rect>')
    dx, dw = hx + hw * 0.34, hw * 0.32
    o.append(f'<rect x="{f(dx)}" y="{f(b - h * 0.5)}" width="{f(dw)}" height="{f(h * 0.5)}" fill="#3A2214" stroke="{INK}" stroke-width="2.6"></rect>'
             + "".join(f'<path d="M{f(dx + dw * k / 4)} {f(b - h * 0.5)} L {f(dx + dw * k / 4)} {f(b)}" stroke="#24140A" stroke-width="1.6"></path>' for k in (1, 2, 3))
             + f'<rect x="{f(dx - 6)}" y="{f(b - h * 0.3)}" width="{f(dw + 12)}" height="{f(h * 0.04)}" fill="#1A1008" stroke="{INK}" stroke-width="1.6"></rect>')
    if lamp: o.append(f'<rect x="{f(dx)}" y="{f(b - 3)}" width="{f(dw)}" height="3" fill="#FFC14D"></rect>' + glow(dx + dw / 2, b, h * 0.12, "#FFC14D", 0.5, f"sh{seed}"))
    o.append(f'<rect x="{f(hx + hw * 0.08)}" y="{f(ht + h * 0.1)}" width="{f(hw * 0.14)}" height="{f(h * 0.1)}" fill="#14101A" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(hx + hw * 0.78)}" y="{f(ht + h * 0.1)}" width="{f(hw * 0.14)}" height="{f(h * 0.1)}" fill="#14101A" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(ground(w, h, b, "#2A2430", dy=0))
    return "".join(o)

def night_street(p, w, h, seed):
    """An empty street at night, every door shut and barred, no one in the way (Matthew's empty street)."""
    return empty_street(p, w, h, seed)

def leaven_passover(w, h, seed, labels=True):
    """A little leaven leaveneth the whole lump … Christ our passover: at the left the kneading-trough, the old lump swollen
    with leaven; at the right, on a clean cloth, the thin unleavened cakes; between them, high in a ring of light, the lamb
    standing (an emblem: no altar, no knife)."""
    o = [f'<defs><linearGradient id="lv{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3A2A22"></stop><stop offset="0.5" stop-color="#C8A06A"></stop>'
         f'<stop offset="1" stop-color="#F3E8C8"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#lv{seed})"></rect>']
    ty = h * 0.74
    o.append(f'<rect x="-10" y="{f(ty)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></rect>')
    k = min(w / 560, h / 240)
    tx = w * 0.18                                              # the trough and the leavened lump
    o.append(f'<path d="M{f(tx - 80 * k)} {f(ty - 34 * k)} L {f(tx + 80 * k)} {f(ty - 34 * k)} L {f(tx + 64 * k)} {f(ty)} L {f(tx - 64 * k)} {f(ty)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(tx - 76 * k)} {f(ty - 32 * k)} C {f(tx - 80 * k)} {f(ty - 110 * k)} {f(tx + 80 * k)} {f(ty - 120 * k)} {f(tx + 76 * k)} {f(ty - 32 * k)} Z" fill="#E8D4A8" stroke="{INK}" stroke-width="2.2"></path>')
    r = random.Random(seed)
    for _ in range(9):
        cx, cy = tx + r.uniform(-50, 50) * k, ty - r.uniform(50, 90) * k
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r.uniform(2, 5) * k)}" fill="none" stroke="#B89A6A" stroke-width="1.2"></circle>')
    cx = w * 0.8                                               # the unleavened cakes on a white cloth
    o.append(f'<path d="M{f(cx - 100 * k)} {f(ty + 2)} L {f(cx + 100 * k)} {f(ty + 2)} L {f(cx + 90 * k)} {f(ty - 14 * k)} L {f(cx - 90 * k)} {f(ty - 14 * k)} Z" fill="#F8F4EA" stroke="{INK}" stroke-width="1.8"></path>')
    for i in range(3):
        yy = ty - 18 * k - i * 9 * k
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(yy)}" rx="{f(64 * k)}" ry="{f(9 * k)}" fill="#E8C890" stroke="{INK}" stroke-width="1.8"></ellipse>'
                 + "".join(f'<circle cx="{f(cx + d * k)}" cy="{f(yy)}" r="{f(1.6 * k)}" fill="#8A5A2A"></circle>' for d in (-30, -10, 10, 30)))
    lx, ly = w * 0.5, ty - 6 * k                               # the lamb, in light
    o.append(halo(lx, ly - 50 * k, 110 * k, "#FFFFFF", 0.8) + rays(lx, ly - 50 * k, 18, 50 * k, 130 * k, "#FFF4C2", 0.4, 3))
    o.append(E.sheep(lx, ly, k * 1.1))
    if labels: o.append(plate_label(w * 0.18, h * 0.1, "THE OLD LEAVEN", "#FFF8E6", 11, halo_="#0D0D0F") + plate_label(w * 0.8, h * 0.1, "UNLEAVENED", "#12113A", 11, halo_="#F3EFE6")
             + plate_label(lx, h * 0.1, "OUR PASSOVER", "#7A4A2A", 11, halo_="#FFF8E6"))
    return "".join(o)

# ---- 1 Corinthians 6 ---------------------------------------------------------------------------------------------------
def tribunal(p, w, h, seed, stage="sue"):
    """Brother goeth to law with brother, and that before unbelievers: the tribunal in the forum, a magistrate in a white
    toga with a purple border standing on the raised bema, and below it two brethren of the church — stage "sue": one
    pointing at the other, who throws up his hands; "wrong": the two turned away from each other, the seat empty."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8")]
    for k in range(7):
        x = w * (0.02 + k * 0.16)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.14)}" width="{f(w * 0.03)}" height="{f(b - h * 0.14)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(pavement(w, h, b, color="#D8D0C0"))
    bx, bw, bh = w * 0.06, w * 0.34, h * 0.2                   # the bema
    o.append(f'<rect x="{f(bx)}" y="{f(b - bh)}" width="{f(bw)}" height="{f(bh)}" fill="#C8BCA8" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(bx - 6)}" y="{f(b - bh - 8)}" width="{f(bw + 12)}" height="10" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(bx + bw + k * w * 0.02)} {f(b - bh * (1 - k / 4))} l {f(w * 0.02)} 0 l 0 {f(bh / 4)}" fill="none" stroke="{INK}" stroke-width="1.6"></path>' for k in range(4)))
    s = fit(b, b - min(h * 0.62, 170))
    if stage == "sue":
        o.append(robed(p, bx + bw * 0.5, b - bh - 4, s * 0.92, "#F3EFE6", skin="#E3B08A", hair="#4A3A2A", mantle="#6A1A5A", flip=True))
        o.append(folk(p, w * 0.56, b, s, 0, flip=True, up=[(-22, -158), (-46, -150), (-70, -150)]))
        o.append(folk(p, w * 0.78, b, s, 2, flip=True, up=[(-22, -158), (-34, -188), (-30, -214)]))
    else:
        o.append(f'<path d="M{f(bx + bw * 0.4)} {f(b - bh - 8)} L {f(bx + bw * 0.4)} {f(b - bh - 40 * s)} L {f(bx + bw * 0.62)} {f(b - bh - 40 * s)} L {f(bx + bw * 0.62)} {f(b - bh - 8)}" fill="none" stroke="{INK}" stroke-width="3"></path>')
        o.append(folk(p, w * 0.52, b, s, 0) + folk(p, w * 0.84, b, s, 2, flip=True))
    return "".join(o)

def washed(w, h, seed):
    """But ye were washed, but ye were sanctified, but ye were justified: dawn over still water, the light poured on it."""
    return vista(w, h, seed, tone="dawn", horizon=0.56, hills_n=1, sea_=True, glow_at=(0.5, 0.56, 0.7, "#FFFFFF"), sun_at=(0.5, 0.54), birds_=3)

def market_meats(p, w, h, seed):
    """Meats for the belly, and the belly for meats: the meat market (the shambles) under its awnings, the hooks and the
    joints hung up, the scales on the counter, the stalls left empty at evening."""
    b = h * 0.92
    o = [sky(w, h, "#E8905A", "#F3D8A0"), pavement(w, h, b, color="#C8B898")]
    n = 3
    for i in range(n):
        x0 = w * (0.03 + i * 0.33); sw_ = w * 0.3
        o.append(f'<rect x="{f(x0)}" y="{f(h * 0.3)}" width="{f(sw_)}" height="{f(b - h * 0.3)}" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(x0 - 8)} {f(h * 0.3)} L {f(x0 + sw_ + 8)} {f(h * 0.3)} L {f(x0 + sw_)} {f(h * 0.14)} L {f(x0)} {f(h * 0.14)} Z" fill="{["#B5121B", "#E8B830", "#1F5FAD"][i]}" stroke="{INK}" stroke-width="2"></path>'
                 + "".join(f'<path d="M{f(x0 + sw_ * k / 8)} {f(h * 0.14)} L {f(x0 - 8 + (sw_ + 16) * k / 8)} {f(h * 0.3)}" stroke="#F3EFE6" stroke-width="3" opacity="0.6"></path>' for k in range(1, 8, 2))
                 + f'<rect x="{f(x0 - 4)}" y="{f(b - h * 0.24)}" width="{f(sw_ + 8)}" height="{f(h * 0.24)}" fill="#C8A878" stroke="{INK}" stroke-width="2"></rect>'
                 + f'<path d="M{f(x0 + 6)} {f(h * 0.36)} L {f(x0 + sw_ - 6)} {f(h * 0.36)}" stroke="#2A1A10" stroke-width="3"></path>')
        for k in range(3):                                     # joints on hooks
            jx = x0 + sw_ * (0.2 + 0.3 * k)
            o.append(f'<path d="M{f(jx)} {f(h * 0.36)} l 0 {f(h * 0.05)}" stroke="#8A8A94" stroke-width="2"></path>'
                     f'<path d="M{f(jx - h * 0.04)} {f(h * 0.41)} C {f(jx - h * 0.06)} {f(h * 0.5)} {f(jx - h * 0.02)} {f(h * 0.6)} {f(jx)} {f(h * 0.6)} C {f(jx + h * 0.03)} {f(h * 0.58)} {f(jx + h * 0.05)} {f(h * 0.48)} {f(jx + h * 0.04)} {f(h * 0.41)} Z" '
                     f'fill="#A8402A" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(f'<path d="M{f(x0 + sw_ * 0.5)} {f(b - h * 0.24)} l 0 {f(-h * 0.08)} M{f(x0 + sw_ * 0.38)} {f(b - h * 0.32)} L {f(x0 + sw_ * 0.62)} {f(b - h * 0.32)}" stroke="#2A1A10" stroke-width="2.4"></path>'
                 f'<path d="M{f(x0 + sw_ * 0.34)} {f(b - h * 0.27)} q {f(sw_ * 0.04)} {f(h * 0.03)} {f(sw_ * 0.08)} 0 M{f(x0 + sw_ * 0.58)} {f(b - h * 0.27)} q {f(sw_ * 0.04)} {f(h * 0.03)} {f(sw_ * 0.08)} 0" stroke="#C8963E" stroke-width="2.4" fill="#C8963E"></path>')
    return "".join(o)

def city_night(p, w, h, seed):
    """Corinth by night under the Acrocorinth, the streets dark and empty, a few lamps in the windows (6:15–18)."""
    return corinth_view(p, w, h, seed, tone="night")

# ---- 1 Corinthians 7 ---------------------------------------------------------------------------------------------------
def lamp_table(w, h, seed, cups=2):
    """A plain room at night: a low table with a lamp burning, two cups and a loaf, the door of the house shut — no one
    drawn (7:1–5)."""
    b = h * 0.9
    o = [room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - h * 0.3, max(w, h) * 0.6, f"lt{seed}", op=0.5)]
    dx, dw = w * 0.72, w * 0.16
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.16)}" width="{f(dw)}" height="{f(b - h * 0.16)}" fill="#4A2A16" stroke="{INK}" stroke-width="2.6"></rect>'
             + "".join(f'<path d="M{f(dx + dw * k / 3)} {f(h * 0.16)} L {f(dx + dw * k / 3)} {f(b)}" stroke="#2A160A" stroke-width="1.6"></path>' for k in (1, 2))
             + f'<rect x="{f(dx - 10)}" y="{f(h * 0.12)}" width="{f(dw + 20)}" height="{f(h * 0.04)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>')
    k = min(w / 520, h / 240)
    tx = w * 0.3
    o.append(low_table_(tx, b, 150 * k, k) + clay_lamp(tx + 75 * k, b - 31 * k, k * 0.9))
    for i in range(cups):
        cx = tx + (30 + 90 * i) * k
        o.append(f'<path d="M{f(cx - 8 * k)} {f(b - 44 * k)} L {f(cx + 8 * k)} {f(b - 44 * k)} L {f(cx + 6 * k)} {f(b - 30 * k)} L {f(cx - 6 * k)} {f(b - 30 * k)} Z" fill="#B8784A" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(loaf(tx + 120 * k, b - 34 * k, k * 0.7))
    return "".join(o)

def low_table_(x, y, w, s=1.0):
    return EP.low_table(x, y, w, s)

def house_door(w, h, seed, open_=False, dusk=False):
    """A house door on a quiet street by day (or dusk): the door shut, or standing open on the courtyard, a jar by the step."""
    b = h * 0.9
    top = ("#3A2A5A", "#E8905A") if dusk else ("#8FD0E2", "#F3E8C8")
    o = [sky(w, h, *top), houses(w, h, b, seed, hmin=0.34, hmax=0.46)]
    hx, hw = w * 0.3, w * 0.4
    o.append(f'<rect x="{f(hx)}" y="{f(h * 0.1)}" width="{f(hw)}" height="{f(b - h * 0.1)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(hx - 8)}" y="{f(h * 0.06)}" width="{f(hw + 16)}" height="{f(h * 0.05)}" fill="#C8B088" stroke="{INK}" stroke-width="2"></rect>')
    dx, dw, dt = hx + hw * 0.36, hw * 0.28, b - h * 0.52
    if open_:
        o.append(f'<rect x="{f(dx)}" y="{f(dt)}" width="{f(dw)}" height="{f(b - dt)}" fill="#C8E0A0" stroke="{INK}" stroke-width="2.6"></rect>'
                 f'<path d="M{f(dx)} {f(b - h * 0.14)} L {f(dx + dw)} {f(b - h * 0.14)}" stroke="#8A9A5A" stroke-width="2"></path>'
                 f'<path d="M{f(dx)} {f(dt)} L {f(dx - dw * 0.4)} {f(dt + h * 0.04)} L {f(dx - dw * 0.4)} {f(b + h * 0.02)} L {f(dx)} {f(b)} Z" fill="#7A4A2A" stroke="{INK}" stroke-width="2.4"></path>')
    else:
        o.append(f'<rect x="{f(dx)}" y="{f(dt)}" width="{f(dw)}" height="{f(b - dt)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2.6"></rect>'
                 + "".join(f'<path d="M{f(dx + dw * k / 3)} {f(dt)} L {f(dx + dw * k / 3)} {f(b)}" stroke="#5A3418" stroke-width="1.6"></path>' for k in (1, 2))
                 + f'<circle cx="{f(dx + dw * 0.8)}" cy="{f(dt + (b - dt) * 0.55)}" r="3" fill="#C8963E"></circle>')
    k = min(1.0, h / 260)
    o.append(f'<path d="M{f(dx + dw + 24 * k)} {f(b)} C {f(dx + dw + 10 * k)} {f(b - 30 * k)} {f(dx + dw + 18 * k)} {f(b - 50 * k)} {f(dx + dw + 28 * k)} {f(b - 54 * k)} L {f(dx + dw + 40 * k)} {f(b - 54 * k)} '
             f'C {f(dx + dw + 50 * k)} {f(b - 50 * k)} {f(dx + dw + 58 * k)} {f(b - 30 * k)} {f(dx + dw + 44 * k)} {f(b)} Z" fill="#B8784A" stroke="{INK}" stroke-width="1.8"></path>')
    o.append(ground(w, h, b, "#C8B080", dy=0))
    return "".join(o)

def household(p, w, h, seed):
    """Else were your children unclean; but now are they holy: the courtyard of a house by day, a man and his wife at the
    door with their two children before them, a vine on the wall."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(b - h * 0.1)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.42)}" y="{f(h * 0.3)}" width="{f(w * 0.16)}" height="{f(b - h * 0.3)}" fill="#3A2214" stroke="{INK}" stroke-width="2.4"></rect>']
    for k in range(8):                                         # a vine along the wall
        x = w * (0.04 + k * 0.05)
        o.append(f'<circle cx="{f(x)}" cy="{f(h * 0.2 + (k % 2) * 8)}" r="{f(max(6, h * 0.04))}" fill="#4A8A3A" stroke="{INK}" stroke-width="1.2"></circle>')
    o.append(f'<path d="M{f(w * 0.02)} {f(b)} C {f(w * 0.04)} {f(h * 0.5)} {f(w * 0.02)} {f(h * 0.3)} {f(w * 0.06)} {f(h * 0.2)} L {f(w * 0.4)} {f(h * 0.2)}" stroke="#5A3A1A" stroke-width="4" fill="none"></path>')
    o.append(ground(w, h, b, "#C8B080", dy=0))
    s = fit(b, b - min(h * 0.74, 200))
    o.append(robed(p, w * 0.32, b, s, "#5A6A7A", head="#2A3A4A", cord="#0D1418", beard="#2A1A10", flip=True))
    o.append(robed(p, w * 0.68, b, s * 0.94, "#7A5A6A", woman=True, veil="#2A2A4A"))
    o.append(robed(p, w * 0.44, b, s * 0.58, "#C8A060", hair="#2A1A10", flip=True) + robed(p, w * 0.56, b, s * 0.5, "#8AA0B8", woman=True, veil="#E8E2D6"))
    return "".join(o)

def tablets(w, h):
    """The keeping of the commandments of God: the two tables of stone, standing in light on a plate."""
    o = [plate_bg(w, h, "1 CORINTHIANS 7:19 · THE COMMANDMENTS OF GOD")]
    k = min(w / 520, (h - 40) / 200); cx, cy = w * 0.5, h * 0.58
    o.append(halo(cx, cy, 120 * k, "#FFF4C2", 0.45))
    for side in (-1, 1):
        x = cx + side * 40 * k
        o.append(f'<path d="M{f(x - 34 * k)} {f(cy + 66 * k)} L {f(x - 34 * k)} {f(cy - 44 * k)} C {f(x - 34 * k)} {f(cy - 82 * k)} {f(x + 34 * k)} {f(cy - 82 * k)} {f(x + 34 * k)} {f(cy - 44 * k)} '
                 f'L {f(x + 34 * k)} {f(cy + 66 * k)} Z" fill="#B8B0A0" stroke="{INK}" stroke-width="2.4"></path>')
        for j in range(5):
            yy = cy - 38 * k + j * 20 * k
            o.append(f'<path d="M{f(x - 22 * k)} {f(yy)} L {f(x + 22 * k)} {f(yy)}" stroke="#4A4038" stroke-width="{f(2.6 * k)}" stroke-dasharray="{f(6 * k)} {f(3 * k)}"></path>')
    return "".join(o)

def bondservant(p, w, h, seed):
    """Wast thou called being a bondservant? A courtyard well: a bondservant in a short tunic drawing water for the house,
    the master's door behind him, the light of morning over the wall."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#FFB07A", "#F3E8C8"),
         f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(b - h * 0.2)}" fill="#D8C098" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.7)}" y="{f(h * 0.34)}" width="{f(w * 0.14)}" height="{f(b - h * 0.34)}" fill="#5A3418" stroke="{INK}" stroke-width="2.4"></rect>']
    o.append(ground(w, h, b, "#C8B080", dy=0))
    s = fit(b, b - min(h * 0.74, 200))
    fx = w * 0.28
    o.append(f'<path d="M{f(fx + 112 * s)} {f(b - 30 * s)} L {f(fx + 112 * s)} {f(b - 150 * s)} M{f(fx + 192 * s)} {f(b - 30 * s)} L {f(fx + 192 * s)} {f(b - 150 * s)} M{f(fx + 104 * s)} {f(b - 150 * s)} L {f(fx + 200 * s)} {f(b - 150 * s)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>'
             f'<path d="M{f(fx + 152 * s)} {f(b - 150 * s)} L {f(fx + 152 * s)} {f(b - 70 * s)}" stroke="#8A6A4A" stroke-width="{f(2 * s)}"></path>'
             f'<path d="M{f(fx + 142 * s)} {f(b - 70 * s)} L {f(fx + 162 * s)} {f(b - 70 * s)} L {f(fx + 158 * s)} {f(b - 54 * s)} L {f(fx + 146 * s)} {f(b - 54 * s)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(well(fx + 152 * s, b - 30 * s, s * 1.0))
    o.append(robed(p, fx, b, s, "#9A8A6A", hair="#2A1A10", belt="#5A3A1A", flip=True, up=[(-22, -158), (-50, -150), (-80, -150)],
                   extra='<path d="M-80 -150 L -152 -150" stroke="#8A6A4A" stroke-width="2"></path>'))
    return "".join(o)

def passing(w, h, seed):
    """The fashion of this world passeth away: the sun going down over the sea, the land darkening."""
    return vista(w, h, seed, tone="dusk", horizon=0.6, hills_n=2, sea_=True, sun_at=(0.62, 0.6), birds_=5)

def cares(p, w, h, seed):
    """Careful for the things of the Lord … careful for the things of the world: one panel in two rooms — at the left a man
    kneeling alone in prayer by a window; at the right a lamp-lit table of a household, the husband and the wife seated at
    their accounts and their bread."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "WomanUp"), room(w, h, b, wall="#6A4A3A", floor="#3A2A20"),
         f'<rect x="{f(w * 0.08)}" y="{f(h * 0.18)}" width="{f(w * 0.12)}" height="{f(h * 0.3)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="5"></path>',
         lamp_glow(w * 0.76, b - h * 0.36, h * 0.6, f"{p}cg", op=0.5)]
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.18)} L {f(w * 0.32)} {f(b)} L {f(w * 0.12)} {f(b)} Z" fill="#FFF4C2" opacity="0.3"></path>')
    s = fit(b, b - min(h * 0.74, 200))
    o.append(E.kneel(w * 0.26, b, s * 0.9, color="#5A6A7A", skin=SKIN))
    k = min(1.0, h / 240)
    tx = w * 0.62
    o.append(EP.low_table(tx, b, 110 * k, k) + clay_lamp(tx + 55 * k, b - 31 * k, k * 0.8) + loaf(tx + 90 * k, b - 34 * k, k * 0.6)
             + open_letter(tx + 10 * k, b - 40 * k, 30 * k, 10 * k, rows=2, seed=seed))
    o.append(seated(w * 0.56, b, s * 0.78, "#5A6A7A", head="#2A3A4A", beard="#2A1A10"))
    o.append(robed(p, w * 0.9, b, s * 0.92, "#7A5A6A", woman=True, veil="#2A2A4A", flip=True))
    return "".join(o)

def father_daughter(p, w, h, seed):
    """His virgin daughter: a father standing at the door of his house, his daughter beside him in a pale veil (7:36–38)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), house_door(w, h, seed, open_=True)]
    s = fit(b, b - min(h * 0.72, 196))
    o.append(robed(p, w * 0.22, b, s, "#6A5A4A", head="#E8E2D6", cord="#6A5A4A", beard="#8A847A", mantle="#4A3E34", flip=True))
    o.append(robed(p, w * 0.8, b, s * 0.94, "#C8B8D0", woman=True, veil="#E8E2D6"))
    return "".join(o)

def widow_door(p, w, h, seed):
    """A wife is bound for so long time as her husband liveth: a widow in a dark veil at the door of her house at dusk."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "WomanUp"), house_door(w, h, seed, open_=False, dusk=True)]
    s = fit(b, b - min(h * 0.72, 196))
    o.append(robed(p, w * 0.16, b, s * 0.94, "#3A3A4A", woman=True, veil="#1A1A2A", mantle="#2A2A3A", flip=True))
    return "".join(o)

def cords(w, h, seed):
    """Art thou bound unto a wife? seek not to be loosed. Art thou loosed from a wife? seek not a wife: an emblem in two
    halves — at the left a cord tied fast about a post in a knot; at the right the same cord loosed, lying slack."""
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#C8B490"></rect>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#C8B490"></rect>']
    b = h * 0.86; k = min(w / 600, h / 220)
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    for cx in (w * 0.25, w * 0.75):
        o.append(f'<rect x="{f(cx - 12 * k)}" y="{f(h * 0.16)}" width="{f(24 * k)}" height="{f(b - h * 0.16)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></rect>')
    cx = w * 0.25; ky = h * 0.46
    o.append(f'<path d="M{f(cx - 14 * k)} {f(ky - 8 * k)} C {f(cx)} {f(ky - 16 * k)} {f(cx + 18 * k)} {f(ky - 6 * k)} {f(cx + 14 * k)} {f(ky + 6 * k)} C {f(cx + 4 * k)} {f(ky + 14 * k)} {f(cx - 18 * k)} {f(ky + 8 * k)} {f(cx - 14 * k)} {f(ky - 8 * k)} Z" fill="none" stroke="#C8963E" stroke-width="{f(6 * k)}"></path>'
             f'<path d="M{f(cx + 14 * k)} {f(ky + 4 * k)} C {f(cx + 50 * k)} {f(ky + 20 * k)} {f(cx + 70 * k)} {f(ky + 40 * k)} {f(cx + 90 * k)} {f(b - 4)} L {f(cx + 150 * k)} {f(b - 4)}" fill="none" stroke="#C8963E" stroke-width="{f(6 * k)}"></path>'
             f'<circle cx="{f(cx + 14 * k)}" cy="{f(ky + 4 * k)}" r="{f(8 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></circle>')
    cx = w * 0.75
    o.append(f'<path d="M{f(cx - 40 * k)} {f(b - 4)} C {f(cx - 10 * k)} {f(b - 14 * k)} {f(cx + 20 * k)} {f(b + 2)} {f(cx + 50 * k)} {f(b - 10 * k)} C {f(cx + 80 * k)} {f(b - 20 * k)} {f(cx + 110 * k)} {f(b - 2)} {f(cx + 130 * k)} {f(b - 6 * k)}" fill="none" stroke="#C8963E" stroke-width="{f(6 * k)}"></path>')
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(w * 0.25, h * 0.1, "BOUND", "#12113A", 12, halo_="#F3EFE6") + plate_label(w * 0.75, h * 0.1, "LOOSED", "#12113A", 12, halo_="#F3EFE6"))
    return "".join(o)
