"""Drawings for the Philemon volume, on Colossians' (`from col.art import *`: the prison study at Rome, the cast of the
prison letters, the Lycus valley, Paul's own hand) — Philemon's house at Colossæ (the church in thy house; Onesimus come home
with the letter; the lodging made ready), Onesimus serving Paul in his bonds, Onesimus and Tychicus on the road to Colossæ,
and Paul's fellow-workers about him at Rome. No beating and no chain on Onesimus is drawn: he is shown serving, walking,
arriving, a brother. Every function takes (p, w, h, seed, ...)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from col.art import *
from php.art import f, INK, _defs

def _house_front(w, h, b, seed, tone="day"):
    """Philemon's house at Colossæ: a courtyard wall of white plaster, the wide door of the house standing open, an upper room
    with its window over it, a vine; Mount Cadmus with snow on its top beyond the roofs."""
    day = tone == "day"
    o = [sky(w, h, "#8FD0E2", "#F3E8C8") if day else sky(w, h, "#2A2A5A", "#E8A060")]
    o.append(f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.2)} {f(h * 0.1)} L {f(w * 0.34)} {f(h * 0.16)} L {f(w * 0.46)} {f(h * 0.06)} L {f(w * 0.6)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.26)} L {f(w + 10)} {f(h * 0.4)} L -10 {f(h * 0.4)} Z" fill="#7A7A8A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.41)} {f(h * 0.1)} L {f(w * 0.46)} {f(h * 0.06)} L {f(w * 0.52)} {f(h * 0.13)} L {f(w * 0.48)} {f(h * 0.12)} L {f(w * 0.46)} {f(h * 0.14)} L {f(w * 0.43)} {f(h * 0.12)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.2"></path>')
    wall = "#E8DCC4" if day else "#C8A888"
    o.append(f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w * 0.72)}" height="{f(b - h * 0.3)}" fill="{wall}" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M-14 {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.2)} L {f(w * 0.74)} {f(h * 0.3)} Z" fill="#A8483A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(w * 0.7)}" y="{f(h * 0.44)}" width="{f(w * 0.34)}" height="{f(b - h * 0.44)}" fill="{wall}" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(w * 0.28)}" y="{f(h * 0.34)}" width="{f(w * 0.12)}" height="{f(h * 0.1)}" fill="{"#3A2214" if day else "#FFC14D"}" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.34)} {f(h * 0.34)} L {f(w * 0.34)} {f(h * 0.44)}" stroke="{INK}" stroke-width="2"></path>')
    dx, dw = w * 0.4, min(w * 0.16, h * 0.34)                  # the door standing open on the lit court
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.5)}" width="{f(dw)}" height="{f(b - h * 0.5)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(dx)} {f(h * 0.5)} L {f(dx - dw * 0.3)} {f(h * 0.53)} L {f(dx - dw * 0.3)} {f(b + 2)} L {f(dx)} {f(b)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for k in range(int(w * 0.7 / 22)):
        o.append(f'<circle cx="{f(k * 22 + r.uniform(-3, 3))}" cy="{f(h * 0.46 + r.uniform(-3, 4))}" r="{f(max(5, h * 0.028))}" fill="#4A8A3A" stroke="{INK}" stroke-width="1.1"></circle>')
    o.append(ground(w, h, b, "#C8B080" if day else "#8A7058", dy=0))
    return "".join(o), dx, dw

def philemon_house(p, w, h, seed, stage="church"):
    """Philemon's house at Colossæ. stage "church" (Phm 2, 4–7): Philemon (grey beard, off-white headcloth) at his open door
    with Apphia (dark-blue veil) and Archippus (charcoal headcloth), the saints coming in to the church in thy house;
    "arrive" (the end of the road, 10–17): Onesimus come home, standing before Philemon with the letter held out, Apphia in the
    doorway; "read": Philemon reading the letter, Onesimus standing by."""
    b = h * 0.94
    bg, dx, dw = _house_front(w, h, b, seed, "dusk" if stage == "arrive" else "day")
    o = [_defs(p), bg]
    s = fit(b, b - min(h * 0.68, 200))
    if stage == "church":
        o.append(philemon(p, dx - w * 0.08, b, s, flip=True, up=[(-22, -158), (-46, -150), (-66, -156)]))
        o.append(apphia(p, dx + dw * 0.5, b, s) + archippus(p, dx + dw + w * 0.05, b, s))
        for i, x in enumerate((0.08, 0.18)):
            o.append(saint(p, w * x, b, s * 0.98, [0, 1][i], flip=True))
        for i, x in enumerate((0.8, 0.9)):
            o.append(saint(p, w * x, b, s * 0.97, [4, 6][i]))
        return "".join(o)
    letter = sealed_scroll(-70, -150, 0.3, rot=12)
    if stage == "arrive":
        o.append(apphia(p, dx + dw + w * 0.07, b, s * 0.98))
        o.append(philemon(p, dx + dw * 0.55, b, s, up=[(-22, -158), (-42, -148), (-60, -150)]))
        o.append(onesimus(p, dx - w * 0.1, b, s, flip=True, up=[(-22, -158), (-42, -146), (-62, -146)], extra=letter))
        return "".join(o)
    o.append(philemon(p, dx + dw * 0.5, b, s, up=[(-22, -158), (-40, -150), (-58, -160)], extra=open_letter(-92, -196, 40, 52, rows=6, seed=seed)))
    o.append(onesimus(p, dx - w * 0.1, b, s, flip=True))
    return "".join(o)

def onesimus_serves(p, w, h, seed):
    """I beseech thee for my child, whom I have begotten in my bonds, Onesimus … my very heart (10–12): Paul's room at Rome,
    Paul sitting chained to the soldier, his free hand on the shoulder of Onesimus, who stands before him with a cup of
    water he has brought; the lamp, the window on Rome."""
    b = h * 0.94
    o = [_defs(p), room(w, h, b, wall="#5E4A3C", floor="#3A2E26"), lamp_glow(w * 0.55, b - h * 0.3, max(w, h) * 0.55, f"{p}lg", op=0.45),
         rome_window(w * 0.62, h * 0.12, min(w * 0.16, h * 0.4), h * 0.3, True, seed)]
    s = fit(b, b - min(h * 0.72, 300))
    gx, px = w * 0.1, w * 0.32
    o.append(EP._shield(w * 0.0, b, s) + guard_r(p, gx, b, s) + bench(px - 52 * s, b, 110 * s, s))
    o.append(paul_fig(p, px, b, s, flip=True, pose="sit", seat=None, up=[(-22, -158), (-52, -160), (-82, -166)]))
    o.append(chain(*guard_hand(gx, b, s), *robed_hand(px, b, s, flip=True, pose="sit"), s=s * 0.8))
    cup = '<path d="M-74 -150 L -58 -150 L -60 -134 L -72 -134 Z" fill="#B85A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(onesimus(p, px + 120 * s, b, s, up=[(-22, -158), (-46, -150), (-66, -148)], extra=cup))
    o.append(clay_lamp(w * 0.86, b - 52 * s, s * 0.8) + low_table(w * 0.8, b, 50 * s, s))
    return "".join(o)

def road_to_colossae(p, w, h, seed):
    """Perhaps he was therefore parted from thee for a season, that thou shouldest have him for ever; no longer as a servant,
    but more than a servant, a brother beloved (15–16): Onesimus and Tychicus on the road up the Lycus valley in the morning,
    Onesimus carrying the letter, Colossæ at the foot of snowy Mount Cadmus ahead of them."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFE6B0")]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.56)} {f(h * 0.14)} L {f(w * 0.66)} {f(h * 0.2)} L {f(w * 0.76)} {f(h * 0.1)} L {f(w * 0.96)} {f(h * 0.34)} L {f(w + 10)} {f(h * 0.5)} Z" fill="#7A7A8A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.72)} {f(h * 0.15)} L {f(w * 0.76)} {f(h * 0.1)} L {f(w * 0.81)} {f(h * 0.17)} L {f(w * 0.78)} {f(h * 0.16)} L {f(w * 0.76)} {f(h * 0.18)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(hills(w, h, h * 0.46, seed, color="#8A9A6A", amp=10, step=80) + town_hill(w * 0.8, h * 0.54, w * 0.1, h * 0.1, seed, color="#8A8A6A")
             + ground(w, h, h * 0.56, "#B8B07A", dy=0))
    o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.56)} L {f(w * 0.78)} {f(h * 0.56)} L {f(w * 1.0)} {f(h + 10)} L {f(-w * 0.1)} {f(h + 10)} Z" fill="#B8A890" stroke="{INK}" stroke-width="1.6"></path>')
    s = fit(b, b - min(h * 0.7, 206))
    o.append(tychicus(p, w * 0.3, b, s, flip=True, pose="walk"))
    o.append(onesimus(p, w * 0.46, b, s, flip=True, pose="walk", up=[(-22, -158), (-36, -132), (-52, -124)], extra=sealed_scroll(-58, -124, 0.26, rot=-20)))
    return "".join(o)

def lodging(p, w, h, seed):
    """But withal prepare me also a lodging (22): the upper room of Philemon's house made ready — a bed spread with a clean
    blanket, a lamp on the stool, a basin and pitcher, the window open on the valley and the mountain; Apphia laying the
    blanket straight."""
    b = h * 0.94
    o = [_defs(p), room(w, h, b, wall="#E8DCC4", floor="#A88A6A")]
    wx, wy, ww, wh = w * 0.62, h * 0.14, min(w * 0.22, h * 0.5), h * 0.34
    o.append(f'<defs><clipPath id="{p}lw"><rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}"></rect></clipPath></defs><g clip-path="url(#{p}lw)">'
             f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#8FD0E2"></rect>'
             f'<path d="M{f(wx)} {f(wy + wh * 0.7)} L {f(wx + ww * 0.4)} {f(wy + wh * 0.2)} L {f(wx + ww * 0.7)} {f(wy + wh * 0.4)} L {f(wx + ww)} {f(wy + wh * 0.3)} L {f(wx + ww)} {f(wy + wh)} L {f(wx)} {f(wy + wh)} Z" fill="#7A7A8A"></path>'
             f'<path d="M{f(wx + ww * 0.32)} {f(wy + wh * 0.3)} L {f(wx + ww * 0.4)} {f(wy + wh * 0.2)} L {f(wx + ww * 0.5)} {f(wy + wh * 0.28)} Z" fill="#F3EFE6"></path>'
             f'<rect x="{f(wx)}" y="{f(wy + wh * 0.78)}" width="{f(ww)}" height="{f(wh)}" fill="#A8B87A"></rect></g>'
             f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>')
    s = fit(b, b - min(h * 0.7, 290))
    bx, bw = w * 0.4, min(w * 0.4, 280 * s)
    o.append(f'<rect x="{f(bx - bw / 2)}" y="{f(b - 46 * s)}" width="{f(bw)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(xx)}" y="{f(b - 32 * s)}" width="{f(8 * s)}" height="{f(32 * s)}" fill="#4A2A14" stroke="{INK}" stroke-width="1.6"></rect>' for xx in (bx - bw / 2 + 4 * s, bx + bw / 2 - 12 * s))
             + f'<rect x="{f(bx - bw / 2)}" y="{f(b - 58 * s)}" width="{f(bw)}" height="{f(12 * s)}" rx="{f(4 * s)}" fill="#3A5A7A" stroke="{INK}" stroke-width="2"></rect>'
             + f'<rect x="{f(bx - bw / 2 + 4 * s)}" y="{f(b - 66 * s)}" width="{f(40 * s)}" height="{f(10 * s)}" rx="{f(4 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(stool(w * 0.06, b, s) + clay_lamp(w * 0.06, b - 56 * s, s * 0.7))
    o.append(apphia(p, bx + bw / 2 + w * 0.05, b, s, up=[(-22, -158), (-40, -128), (-58, -112)]))
    o.append(f'<ellipse cx="{f(w * 0.92)}" cy="{f(b - 4)}" rx="{f(24 * s)}" ry="{f(7 * s)}" fill="#8A8478" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(w * 0.92 - 8 * s)} {f(b - 6)} L {f(w * 0.92 - 10 * s)} {f(b - 40 * s)} L {f(w * 0.92 + 10 * s)} {f(b - 40 * s)} L {f(w * 0.92 + 8 * s)} {f(b - 6)} Z" fill="#B85A3A" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def fellow_workers(p, w, h, seed):
    """Epaphras, my fellow-prisoner in Christ Jesus, saluteth thee; and so do Mark, Aristarchus, Demas, Luke, my
    fellow-workers (23–24): Paul's room at Rome, Paul sitting chained to the soldier, and the five standing with him."""
    return prison_study(p, w, h, seed, stage="prison", scribe=False, others=(luke, demas, aristarchus, mark, epaphras), up=False)
