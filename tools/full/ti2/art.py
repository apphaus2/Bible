"""Drawings for the 2 Timothy volume. 2 Timothy starts from all of 1 Timothy's drawings (`from ti1.art2 import *`, which carries
Galatians', Acts' and the Corinthian letters' drawings and the epistle kit), and adds its own: Paul's cell at Rome, darker
and barer than the hired house of the earlier prison letters (Acts 28:30) — stone walls, one high barred window, one lamp,
the soldier and the chain, Luke alone with him (4:11) — Lois and Eunice, the gift stirred up, the deposit, the soldier,
the athlete and the husbandman, the word not bound, the workman, the foundation and its seal, the vessels of a great house,
Jannes and Jambres before Pharaoh's gate, the three gates of Antioch, Iconium and Lystra, the finish line and the crown of
righteousness, the cloak and the parchments, the brethren scattered on the map.

God is never drawn (light); Satan never drawn (2:26 words only); Paul's death is never drawn: "I am already being offered"
(4:6) is his face in a grave gold light, then the finished course and the crown laid up."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from ti1.art2 import *
from ti1.art import _sheet, _defs, _eph_window
from ti1.art2 import _hair_cap
from epistle import roman_guard, guard_hand, robed_hand, chain, scribe_seated, mat as floor_mat, bench, _shield
from co2.art import moses_fig
from exo.art2 import magician, palace_gate
from co1.art3 import athlete
from ti1.common import TIMOTHY_LOOK, LUKE_LOOK, LOIS_LOOK, EUNICE_LOOK

OLD_BEARD = "#4A2E1A"                                            # Timothy's short beard in 2 Timothy

def stone_wall(w, h, b, seed, color="#3A3238", line="#2A2430"):
    """A prison wall of dressed stone, course on course, and the floor of beaten earth below b."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(b + 10)}" fill="{color}"></rect>']
    r = random.Random(seed)
    ch_ = max(22, h * 0.07); y = 0; row = 0
    while y < b:
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="{line}" stroke-width="2"></path>')
        x = (row % 2) * 30 - 30
        while x < w:
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(min(b, y + ch_))}" stroke="{line}" stroke-width="2"></path>')
            x += r.uniform(56, 84)
        y += ch_; row += 1
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#241E22" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def barred_window(x, y, ww, hh, night=True):
    """A small window high in the wall, three iron bars across it, the night (or the day) beyond."""
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="{"#1A2050" if night else "#8FD0E2"}" stroke="{INK}" stroke-width="3"></rect>'
            + "".join(f'<path d="M{f(x + ww * t)} {f(y)} L {f(x + ww * t)} {f(y + hh)}" stroke="#4A4A54" stroke-width="{f(max(3, ww * 0.06))}"></path>' for t in (0.25, 0.5, 0.75))
            + (f'<circle cx="{f(x + ww * 0.36)}" cy="{f(y + hh * 0.3)}" r="1.6" fill="#F3EFE6"></circle><circle cx="{f(x + ww * 0.62)}" cy="{f(y + hh * 0.6)}" r="1.2" fill="#F3EFE6"></circle>' if night else ""))

def _vignette(w, h, uid, cx=0.45, cy=0.6, op=0.6):
    """The dark of the cell closing in round the lamp's light."""
    return (f'<defs><radialGradient id="{uid}" cx="{cx}" cy="{cy}" r="0.75"><stop offset="0.35" stop-color="#000000" stop-opacity="0"></stop>'
            f'<stop offset="1" stop-color="#000000" stop-opacity="{op}"></stop></radialGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>')

def luke_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    """Luke the physician: a short grey beard, an off-white headcloth, a plain grey-brown robe and a slate mantle."""
    l = LUKE_LOOK
    return robed(p, x, y, s, l["cloth"], head=l["head"], cord=l["cord"], beard=l["beard"], mantle=l["mantle"], flip=flip, up=up, extra=extra, pose=pose, seat=seat)

def cell(p, w, h, seed, stage="dictate", scribe=True, visitor=None, guard=True):
    """Paul's cell at Rome near his end, darker and barer than the hired house of Acts 28: walls of dressed stone, one small
    barred window high up, one clay lamp in a niche, the floor of beaten earth; the soldier standing at the left with his
    spear, chained wrist to wrist to Paul sitting on a plain bench; Luke alone with him (4:11), cross-legged on a mat with the
    roll. stage "dictate" Paul's hand out, Luke writing; "read" Luke reading it back; "alone" Paul sitting with his hands at
    rest and no scribe; visitor= a figure function fig(p, x, y, s, flip=, up=, extra=) standing in the open door at the right
    (Onesiphorus come with bread, 1:16–17)."""
    b = h * 0.95
    k = fig_k(w, h, 0.3)
    s = k
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), stone_wall(w, h, b, seed)]
    o.append(barred_window(w * 0.44, b - 220 * k, min(w * 0.1, 60 * k), min(h * 0.18, 46 * k)))
    nx = w * 0.56                                                    # the lamp's niche
    o.append(f'<path d="M{f(nx - 18 * k)} {f(b - 110 * k)} L {f(nx - 18 * k)} {f(b - 136 * k)} C {f(nx - 18 * k)} {f(b - 150 * k)} {f(nx + 18 * k)} {f(b - 150 * k)} {f(nx + 18 * k)} {f(b - 136 * k)} L {f(nx + 18 * k)} {f(b - 110 * k)} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>')
    o.append(lamp_glow(nx, b - 120 * k, max(w, h) * 0.5, f"{p}cl", op=0.5) + clay_lamp(nx - 12 * k, b - 110 * k, k * 0.5))
    if visitor:
        dx, dw = w * 0.8, min(w * 0.16, 90 * k)
        o.append(f'<rect x="{f(dx)}" y="{f(b - 196 * k)}" width="{f(dw)}" height="{f(196 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<path d="M{f(dx + dw)} {f(b - 196 * k)} L {f(dx + dw + 18 * k)} {f(b - 186 * k)} L {f(dx + dw + 18 * k)} {f(b + 4)} L {f(dx + dw)} {f(b)} Z" fill="#3A2A20" stroke="{INK}" stroke-width="2"></path>')
    gx, px = w * 0.12, w * 0.31
    if guard: o.append(_shield(w * 0.0, b, k * 0.9))
    arm = [(-22, -158), (-50, -146), (-76, -150)] if stage == "dictate" else None
    o.append(bench(px - 52 * k, b, 110 * k, k, color="#4A3A2A"))
    if guard: o.append(roman_guard(p, gx, b, s))
    o.append(paul_fig(p, px, b, s, flip=True, up=arm, pose="sit", seat=None))
    if guard:
        hx_, hy_ = robed_hand(px, b, s, flip=True, pose="sit")
        o.append(chain(*guard_hand(gx, b, s), hx_, hy_, s=k * 0.8))
    if scribe and stage != "alone":
        sx = w * 0.6
        o.append(floor_mat(w * 0.48, b, 120 * k, k, color="#5A4A30") + scribe_seated(sx, b - 4 * k, k, cloth=LUKE_LOOK["cloth"], head=LUKE_LOOK["head"], cord=LUKE_LOOK["cord"],
                                                                                    beard=LUKE_LOOK["beard"], flip=True, stage="read" if stage == "read" else "write"))
    if visitor:
        loaf = '<ellipse cx="-70" cy="-148" rx="10" ry="6" fill="#D8A060" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
        o.append(visitor(p, dx + dw * 0.5, b, s, flip=False, up=[(-22, -158), (-44, -150), (-64, -150)], extra=loaf))
    o.append(_vignette(w, h, f"{p}vg", cx=0.5, cy=0.62))
    return "".join(o)

def onesiphorus_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Onesiphorus of Ephesus: a slate headcloth, a brown beard, a traveller's dun cloak."""
    return robed(p, x, y, s, "#7A6A54", head="#3A4A5A", cord="#1A1210", beard="#5A4A3A", mantle="#5A4A3A", belt="#3A2A1A", flip=flip, up=up, extra=extra)

def onesiphorus_cell(p, w, h, seed):
    """He oft refreshed me, and was not ashamed of my chain; but, when he was in Rome, he sought me diligently, and found me:
    the cell door open, Onesiphorus standing in it with a loaf in his hand, Paul chained on his bench turning to him."""
    return cell(p, w, h, seed, stage="alone", visitor=onesiphorus_fig)

# ---- 2 Timothy 1 -----------------------------------------------------------------------------------------------------------
def three_faith(w, h):
    """The unfeigned faith that is in thee; which dwelt first in thy grandmother Lois, and thy mother Eunice; and … in thee
    also: a plate — three framed portraits in a row, Lois (old, grey hair, a dark-blue veil), Eunice (a grey-green veil),
    Timothy (a short beard now), joined by a gold line of light."""
    from ti1.common import LOIS, EUNICE, TIMOTHY_OLD
    o = [plate_bg(w, h, "2 TIMOTHY 1:5 · THE UNFEIGNED FAITH")]
    top = 44
    side = min((w - 80) / 3.4, h - top - 46)
    gap = (w - 3 * side) / 4
    for i, (tok, name, light) in enumerate(((LOIS, "LOIS", "#FFE6A0"), (EUNICE, "EUNICE", "#FFE6A0"), (TIMOTHY_OLD, "TIMOTHY", "#FFF4C2"))):
        x = gap + i * (side + gap)
        o.append(_portrait(tok, x, top + 4, side, side, f"tf{i}", light=light))
        o.append(label(x + side / 2, top + side + 22, name, GOLD, 11))
        if i < 2:
            o.append(f'<path d="M{f(x + side + 6)} {f(top + side / 2)} L {f(x + side + gap - 6)} {f(top + side / 2)}" stroke="{GOLD}" stroke-width="3" stroke-dasharray="6 4"></path>'
                     f'<path d="M{f(x + side + gap - 14)} {f(top + side / 2 - 6)} L {f(x + side + gap - 6)} {f(top + side / 2)} L {f(x + side + gap - 14)} {f(top + side / 2 + 6)}" fill="none" stroke="{GOLD}" stroke-width="3"></path>')
    o.append(label(gap + side * 0.5, top + side + 38, "THY GRANDMOTHER", CY, 9) + label(gap * 2 + side * 1.5, top + side + 38, "THY MOTHER", CY, 9)
             + label(gap * 3 + side * 2.5, top + side + 38, "IN THEE ALSO", CY, 9))
    return "".join(o)

from gal.art import _portrait

def embers(w, h, seed):
    """Stir up the gift of God, which is in thee: a brazier on its tripod in a dark room, the coals glowing red under the ash
    and fanned up into flame, sparks going up; a fan of reeds laid on its rim."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1014"></rect>', halo(w * 0.5, h * 0.56, max(w, h) * 0.5, "#FF8A2A", 0.45)]
    k = min(w / 520, h / 260)
    cx, cy = w * 0.5, h * 0.66
    o.append(f'<path d="M{f(cx - 60 * k)} {f(cy + 10 * k)} L {f(cx - 80 * k)} {f(h + 10)} M{f(cx + 60 * k)} {f(cy + 10 * k)} L {f(cx + 80 * k)} {f(h + 10)} M{f(cx)} {f(cy + 20 * k)} L {f(cx)} {f(h + 10)}" stroke="#3A2A20" stroke-width="{f(7 * k)}"></path>')
    o.append(f'<path d="M{f(cx - 96 * k)} {f(cy - 12 * k)} C {f(cx - 90 * k)} {f(cy + 30 * k)} {f(cx + 90 * k)} {f(cy + 30 * k)} {f(cx + 96 * k)} {f(cy - 12 * k)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(22):                                              # the coals
        x = cx + r.uniform(-80, 80) * k; y = cy - 12 * k + r.uniform(-6, 6) * k
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(8, 14) * k)}" ry="{f(r.uniform(5, 8) * k)}" fill="{r.choice(["#D7261E", "#FF6A2A", "#8A1A10", "#5A4A4A"])}" stroke="{INK}" stroke-width="1"></ellipse>')
    for i, (dx, hh) in enumerate(((-40, 70), (-6, 110), (30, 86), (60, 50), (-64, 44))):     # the flames fanned up
        x = cx + dx * k; t = cy - 16 * k - hh * k
        o.append(f'<path d="M{f(x - 18 * k)} {f(cy - 14 * k)} C {f(x - 22 * k)} {f(cy - 40 * k)} {f(x - 4 * k)} {f(t + 30 * k)} {f(x)} {f(t)} C {f(x + 6 * k)} {f(t + 30 * k)} {f(x + 22 * k)} {f(cy - 40 * k)} {f(x + 18 * k)} {f(cy - 14 * k)} Z" '
                 f'fill="#FF8A2A" stroke="#D7261E" stroke-width="1.6"></path>'
                 f'<path d="M{f(x - 8 * k)} {f(cy - 14 * k)} C {f(x - 8 * k)} {f(cy - 30 * k)} {f(x - 2 * k)} {f(t + 40 * k)} {f(x)} {f(t + 24 * k)} C {f(x + 4 * k)} {f(t + 40 * k)} {f(x + 8 * k)} {f(cy - 30 * k)} {f(x + 8 * k)} {f(cy - 14 * k)} Z" fill="#FFE680"></path>')
    for i in range(24):                                              # sparks
        x = cx + r.uniform(-120, 120) * k; y = r.uniform(h * 0.06, cy - 60 * k)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.2, 2.6))}" fill="#FFD23F" opacity="{r.uniform(0.5, 1):.2f}"></circle>')
    fx = cx + 120 * k                                                # the fan of reeds on the rim
    o.append(f'<path d="M{f(fx - 24 * k)} {f(cy - 8 * k)} L {f(fx + 40 * k)} {f(cy - 50 * k)} L {f(fx + 56 * k)} {f(cy - 26 * k)} Z" fill="#C8A060" stroke="{INK}" stroke-width="1.6"></path>'
             + "".join(f'<path d="M{f(fx - 24 * k)} {f(cy - 8 * k)} L {f(fx + 40 * k + 16 * k * t)} {f(cy - 50 * k + 24 * k * t)}" stroke="#8A6A3A" stroke-width="1.2"></path>' for t in (0.25, 0.5, 0.75)))
    o.append(plate_label(w * 0.5, h * 0.1, "STIR UP THE GIFT", "#FFD23F", 11, halo_="#1A1014"))
    return "".join(o)

def deposit(w, h):
    """He is able to guard that which I have committed unto him against that day: a plate — a coffer bound with iron, tied
    with a cord and sealed with red clay, standing in light; tags: THAT WHICH I HAVE COMMITTED UNTO HIM · THE SEAL · AGAINST
    THAT DAY."""
    o = [plate_bg(w, h, "2 TIMOTHY 1:12–14 · THAT WHICH IS COMMITTED")]
    k = min((h - 60) / 200, w / 600)
    cx, base = w * 0.3, min(h - 24, 40 + (h - 40) * 0.5 + 70 * k)
    o.append(halo(cx, base - 80 * k, 170 * k, "#FFE680", 0.35))
    bw, bh = 170 * k, 104 * k
    o.append(f'<rect x="{f(cx - bw / 2)}" y="{f(base - bh)}" width="{f(bw)}" height="{f(bh)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<path d="M{f(cx - bw / 2 - 6 * k)} {f(base - bh)} C {f(cx - bw / 2)} {f(base - bh - 34 * k)} {f(cx + bw / 2)} {f(base - bh - 34 * k)} {f(cx + bw / 2 + 6 * k)} {f(base - bh)} Z" fill="#7A5A3A" stroke="{INK}" stroke-width="2.6"></path>')
    for t in (0.18, 0.82):
        o.append(f'<rect x="{f(cx - bw / 2 + bw * t - 6 * k)}" y="{f(base - bh - 26 * k)}" width="{f(12 * k)}" height="{f(bh + 26 * k)}" fill="#5A5A64" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<path d="M{f(cx)} {f(base - bh - 28 * k)} L {f(cx)} {f(base - bh * 0.4)}" stroke="#C8A060" stroke-width="{f(3 * k)}"></path>'
             f'<path d="M{f(cx - bw / 2)} {f(base - bh * 0.55)} L {f(cx + bw / 2)} {f(base - bh * 0.55)}" stroke="#C8A060" stroke-width="{f(3 * k)}"></path>'
             f'<circle cx="{f(cx)}" cy="{f(base - bh * 0.55)}" r="{f(15 * k)}" fill="#B5121B" stroke="{INK}" stroke-width="1.8"></circle>'
             f'<circle cx="{f(cx)}" cy="{f(base - bh * 0.55)}" r="{f(8 * k)}" fill="none" stroke="#7A0A10" stroke-width="1.6"></circle>')
    tx = cx + bw / 2 + 60 * k
    o.append(tag(cx + bw * 0.3, base - bh * 0.8, "THAT WHICH I HAVE COMMITTED", tx, base - bh - 24 * k, color=GOLD, size=10))
    o.append(tag(cx + 12 * k, base - bh * 0.55, "THE SEAL", tx, base - bh * 0.45, size=10))
    o.append(tag(cx + bw / 2, base - 10 * k, "AGAINST THAT DAY", tx, base - 6 * k, size=10))
    return "".join(o)

# ---- 2 Timothy 2 -----------------------------------------------------------------------------------------------------------
def three_callings(p, w, h, seed):
    """A good soldier, the athlete crowned, the husbandman that laboreth: three cells — a soldier on service standing to his
    post with spear and shield at the frontier fort; a runner at the games, the victor's wreath held out over the finish;
    the husbandman in his orchard at harvest, the first fig in his hand and the full basket at his feet."""
    def soldier(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - min(ch * 0.7, 230))
        o = [_defs(pp), sky(cw, ch, "#8FD0E2", "#F3E8C8"), walls(-10, cw + 10, ch * 0.66, ch * 0.24, seed, towers=2, color="#B8A07A", houses=False),
             ground(cw, ch, ch * 0.7, "#B8A06A", dy=0)]
        o.append(_shield(cw * 0.6, b, s) + roman_guard(pp, cw * 0.46, b, s))
        return "".join(o)
    def games(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - min(ch * 0.7, 230)) * 0.92
        o = [sky(cw, ch, "#5AB0D8", "#F3E8C8"), f'<path d="M-4 {f(ch * 0.5)} C {f(cw * 0.3)} {f(ch * 0.4)} {f(cw * 0.7)} {f(ch * 0.4)} {f(cw + 4)} {f(ch * 0.5)} L {f(cw + 4)} {f(ch * 0.62)} L -4 {f(ch * 0.62)} Z" fill="#8A9A6A" stroke="{INK}" stroke-width="1.6"></path>',
             f'<rect x="-4" y="{f(ch * 0.62)}" width="{f(cw + 8)}" height="{f(ch)}" fill="#E8C890" stroke="{INK}" stroke-width="2"></rect>']
        o += [f'<path d="M-4 {f(ch * (0.7 + 0.08 * i))} L {f(cw + 4)} {f(ch * (0.7 + 0.08 * i))}" stroke="#F3EFE6" stroke-width="2"></path>' for i in range(3)]
        px_ = cw * 0.8
        o.append(f'<rect x="{f(px_)}" y="{f(ch * 0.28)}" width="{f(cw * 0.03)}" height="{f(b - ch * 0.28)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<circle cx="{f(px_ + cw * 0.015)}" cy="{f(ch * 0.24)}" r="{f(ch * 0.06)}" fill="none" stroke="#2E6B3A" stroke-width="{f(max(4, ch * 0.025))}"></circle>')
        o.append(athlete(cw * 0.42, b, s, "run_a"))
        return "".join(o)
    def orchard(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - min(ch * 0.7, 230))
        o = [_defs(pp), sky(cw, ch, "#FFC890", "#FFF0C8"), ground(cw, ch, ch * 0.62, "#9CCB5E", dy=0)]
        tx = cw * 0.78
        o.append(f'<path d="M{f(tx)} {f(b)} C {f(tx - 6)} {f(ch * 0.6)} {f(tx + 4)} {f(ch * 0.4)} {f(tx)} {f(ch * 0.3)}" stroke="#5A3A22" stroke-width="{f(max(8, cw * 0.04))}" fill="none"></path>'
                 f'<ellipse cx="{f(tx)}" cy="{f(ch * 0.24)}" rx="{f(cw * 0.26)}" ry="{f(ch * 0.16)}" fill="#2E6B3A" stroke="{INK}" stroke-width="2"></ellipse>'
                 + "".join(f'<circle cx="{f(tx + cw * dx)}" cy="{f(ch * dy)}" r="{f(max(3, cw * 0.016))}" fill="#6A2A5A" stroke="{INK}" stroke-width="1"></circle>' for dx, dy in ((-0.12, 0.22), (0.06, 0.18), (0.14, 0.27), (-0.04, 0.3), (0.2, 0.2))))
        basket = ('<path d="M-70 -6 L -30 -6 L -36 22 L -64 22 Z" fill="#B8884A" stroke="#0D0D0F" stroke-width="1.6"></path>')
        fig_ = '<circle cx="-62" cy="-150" r="5" fill="#6A2A5A" stroke="#0D0D0F" stroke-width="1"></circle>'
        o.append(robed(pp, cw * 0.4, b, s, "#8A7A5A", head="#E8E2D6", cord="#5A4A3A", beard="#4A3A2A", belt="#5A3A22", up=[(-22, -158), (-40, -150), (-58, -152)], extra=fig_))
        o.append(f'<path d="M{f(cw * 0.12)} {f(b)} L {f(cw * 0.3)} {f(b)} L {f(cw * 0.27)} {f(b - ch * 0.1)} L {f(cw * 0.15)} {f(b - ch * 0.1)} Z" fill="#B8884A" stroke="{INK}" stroke-width="1.6"></path>'
                 + "".join(f'<circle cx="{f(cw * (0.17 + 0.03 * i))}" cy="{f(b - ch * 0.11)}" r="{f(max(3, cw * 0.016))}" fill="#6A2A5A" stroke="{INK}" stroke-width="1"></circle>' for i in range(4)))
        return "".join(o)
    o = [cells(p, w, h, [soldier, games, orchard])]
    o += [plate_label(w * (i + 0.5) / 3, h * 0.08, t, "#12113A", 9, halo_="#F3EFE6") for i, t in enumerate(("A GOOD SOLDIER", "CONTENDED LAWFULLY", "THE HUSBANDMAN"))]
    return "".join(o)

def not_bound(p, w, h, seed):
    """I suffer hardship unto bonds, as a malefactor; but the word of God is not bound: two cells — in the cell, close, Paul's
    wrist in its iron with the chain going to the ring in the wall, his hand on the roll by the lamp (IN BONDS); and out on
    the road at sunrise a brother walking away with the sealed letter in his hand, the road running on into the light (THE
    WORD OF GOD IS NOT BOUND)."""
    def bonds(pp, cw, ch):
        b = ch * 0.78
        o = [stone_wall(cw, ch, b, seed), lamp_glow(cw * 0.7, b - ch * 0.2, ch * 0.7, f"{pp}bl", op=0.55)]
        o.append(f'<rect x="-4" y="{f(b)}" width="{f(cw + 8)}" height="{f(ch)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>')
        k = ch / 260
        o.append(open_letter(cw * 0.2, b + 8 * k, cw * 0.5, ch * 0.12, rows=3, seed=seed) + clay_lamp(cw * 0.72, b + 2, k * 0.8))
        ax, ay = cw * 0.44, b + ch * 0.1                                    # the forearm in its sleeve, the hand on the roll
        o.append(f'<path d="M-10 {f(ay - 30 * k)} L {f(ax)} {f(ay - 6 * k)}" stroke="{INK}" stroke-width="{f(34 * k)}" stroke-linecap="round"></path>'
                 f'<path d="M-10 {f(ay - 30 * k)} L {f(ax)} {f(ay - 6 * k)}" stroke="{ROBES["paul"]}" stroke-width="{f(29 * k)}" stroke-linecap="round"></path>'
                 f'<ellipse cx="{f(ax + 22 * k)}" cy="{f(ay)}" rx="{f(22 * k)}" ry="{f(12 * k)}" fill="{SKIN}" stroke="{INK}" stroke-width="1.6"></ellipse>'
                 f'<rect x="{f(ax - 12 * k)}" y="{f(ay - 24 * k)}" width="{f(14 * k)}" height="{f(32 * k)}" rx="3" fill="#5A5A64" stroke="{INK}" stroke-width="1.6" transform="rotate(-24 {f(ax - 5 * k)} {f(ay - 8 * k)})"></rect>')
        o.append(chain(ax - 4 * k, ay - 20 * k, cw * 0.16, b - ch * 0.42, s=k, sag=0.3)
                 + f'<circle cx="{f(cw * 0.16)}" cy="{f(b - ch * 0.46)}" r="{f(9 * k)}" fill="none" stroke="#5A5A64" stroke-width="{f(4 * k)}"></circle>')
        return "".join(o)
    def road(pp, cw, ch):
        hz = ch * 0.5
        o = [_defs(pp), sky(cw, ch, "#6A8AC0", "#FFE0A8"), halo(cw * 0.78, hz, ch * 0.5, "#FFF4C2", 0.6), hills(cw, ch, hz - ch * 0.04, seed, color="#8A8A6A", amp=8, step=60),
             ground(cw, ch, hz, "#C8B07A", dy=0),
             f'<path d="M{f(cw * 0.1)} {f(ch + 4)} L {f(cw * 0.74)} {f(hz)} L {f(cw * 0.82)} {f(hz)} L {f(cw * 0.7)} {f(ch + 4)} Z" fill="#E8D8B0" stroke="{INK}" stroke-width="1.6"></path>']
        b = ch * 0.92; s = fit(b, b - min(ch * 0.62, 200))
        o.append(messenger(pp, cw * 0.48, b, s, flip=True, up=[(-22, -158), (-36, -130), (-42, -112)], extra=sealed_scroll(-42, -112, 0.34, rot=30)))
        return "".join(o)
    o = [cells(p, w, h, [bonds, road])]
    o.append(plate_label(w * 0.25, h * 0.08, "UNTO BONDS", "#FFD23F", 10) + plate_label(w * 0.75, h * 0.08, "THE WORD OF GOD IS NOT BOUND", "#12113A", 10, halo_="#FFF4C2"))
    return "".join(o)

def workman(p, w, h, seed):
    """A workman that needeth not to be ashamed, handling aright the word of truth: a stonecutter's yard in the morning, the
    mason standing at a block on its trestles, cutting it true along the line he has chalked, his square laid by; the
    finished stones squared and stacked behind him."""
    b = h * 0.92
    s = fit(b, b - min(h * 0.7, 220))
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.6, seed, hmin=0.12, hmax=0.2), ground(w, h, h * 0.6, "#D8C098", dy=0)]
    bx, by, bw, bh = w * 0.44, b - 92 * s, 160 * s, 50 * s               # the block on its trestles
    o.append(f'<path d="M{f(bx + 10 * s)} {f(by + bh)} L {f(bx)} {f(b)} M{f(bx + 30 * s)} {f(by + bh)} L {f(bx + 40 * s)} {f(b)} M{f(bx + bw - 30 * s)} {f(by + bh)} L {f(bx + bw - 40 * s)} {f(b)} M{f(bx + bw - 10 * s)} {f(by + bh)} L {f(bx + bw)} {f(b)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>'
             f'<rect x="{f(bx)}" y="{f(by)}" width="{f(bw)}" height="{f(bh)}" fill="#D8D0C0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(bx + bw * 0.55)} {f(by - 2)} L {f(bx + bw * 0.55)} {f(by + bh + 2)}" stroke="#D7261E" stroke-width="{f(2.2 * s)}" stroke-dasharray="{f(5 * s)} {f(3 * s)}"></path>'
             f'<path d="M{f(bx + bw * 0.55 + 4 * s)} {f(by)} L {f(bx + bw)} {f(by)} L {f(bx + bw)} {f(by + bh)} L {f(bx + bw * 0.55 + 4 * s)} {f(by + bh)}" fill="#C8C0B0" stroke="{INK}" stroke-width="1.4"></path>')
    mallet = ('<path d="M-74 -128 L -80 -156" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path><path d="M-74 -128 L -80 -156" stroke="#8A6A3A" stroke-width="3.5" stroke-linecap="round"></path>'
              '<rect x="-94" y="-170" width="26" height="16" rx="3" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6" transform="rotate(-12 -81 -162)"></rect>')
    o.append(robed(p, bx - 40 * s, b, s, "#8A7A5A", hair="#3A2A1A", beard="#3A2A1A", belt="#5A3A22", flip=True, up=[(-22, -158), (-48, -146), (-74, -128)], extra=mallet))
    o.append(f'<path d="M{f(bx + 12 * s)} {f(by - 4 * s)} L {f(bx + 40 * s)} {f(by - 4 * s)} L {f(bx + 40 * s)} {f(by - 14 * s)}" fill="none" stroke="#8A6A3A" stroke-width="{f(3 * s)}"></path>')
    for i in range(3):                                               # squared stones stacked
        o.append(f'<rect x="{f(w * 0.8 + (i % 2) * 18 * s)}" y="{f(b - (i + 1) * 34 * s)}" width="{f(80 * s)}" height="{f(34 * s)}" fill="#E0D8C8" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def foundation(w, h):
    """The firm foundation of God standeth, having this seal: a technical plate — the great foundation stone set on the rock,
    a seal cut into its face like a signet's impression, and the two inscriptions of the seal tagged on it (labels: the ASV's
    words)."""
    o = [plate_bg(w, h, "2 TIMOTHY 2:19 · THE FIRM FOUNDATION OF GOD")]
    k = min((h - 60) / 200, w / 640)
    base = min(h - 22, 40 + (h - 40) * 0.5 + 90 * k)            # the stone in the middle of a tall plate, not sunk to its foot
    cx = w * 0.32
    o.append(f'<path d="M-10 {f(base)} C {f(w * 0.2)} {f(base - 18 * k)} {f(w * 0.5)} {f(base - 10 * k)} {f(w + 10)} {f(base - 20 * k)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A4A54" stroke="{CY}" stroke-width="1.6"></path>')
    sw_, sh_ = 260 * k, 110 * k
    o.append(halo(cx, base - sh_ / 2, 200 * k, "#FFE680", 0.2))
    o.append(f'<rect x="{f(cx - sw_ / 2)}" y="{f(base - 14 * k - sh_)}" width="{f(sw_)}" height="{f(sh_)}" fill="#D8D0C0" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<path d="M{f(cx - sw_ / 2)} {f(base - 14 * k - sh_)} L {f(cx - sw_ / 2 + 24 * k)} {f(base - 34 * k - sh_)} L {f(cx + sw_ / 2 + 24 * k)} {f(base - 34 * k - sh_)} L {f(cx + sw_ / 2)} {f(base - 14 * k - sh_)} Z" fill="#E8E2D6" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(cx + sw_ / 2)} {f(base - 14 * k - sh_)} L {f(cx + sw_ / 2 + 24 * k)} {f(base - 34 * k - sh_)} L {f(cx + sw_ / 2 + 24 * k)} {f(base - 34 * k)} L {f(cx + sw_ / 2)} {f(base - 14 * k)} Z" fill="#B8B0A0" stroke="{INK}" stroke-width="2.2"></path>')
    sx, sy = cx, base - 14 * k - sh_ / 2
    o.append(f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(36 * k)}" fill="#C8C0B0" stroke="{INK}" stroke-width="2"></circle>'
             f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(28 * k)}" fill="none" stroke="#8A8278" stroke-width="2"></circle>'
             f'<path d="M{f(sx - 14 * k)} {f(sy)} L {f(sx + 14 * k)} {f(sy)} M{f(sx)} {f(sy - 14 * k)} L {f(sx)} {f(sy + 14 * k)}" stroke="#8A8278" stroke-width="{f(3 * k)}"></path>')
    tx = cx + sw_ / 2 + 50 * k
    o.append(tag(sx + 28 * k, sy - 18 * k, "THE LORD KNOWETH THEM THAT ARE HIS", tx, sy - 46 * k, color=GOLD, size=10))
    o.append(tag(sx + 28 * k, sy + 18 * k, "DEPART FROM UNRIGHTEOUSNESS", tx, sy + 30 * k, color=GOLD, size=10))
    o.append(tag(sx - 30 * k, sy - 18 * k, "THE SEAL", cx - sw_ / 2 - 20 * k, base - 14 * k - sh_ - 30 * k, size=10))
    return "".join(o)

def great_house(w, h):
    """In a great house there are not only vessels of gold and of silver, but also of wood and of earth: a plate on cream paper —
    a shelf of four vessels, a gold cup, a silver ewer, a wooden bowl and an earthen pot, tagged; the gold cup lit, set apart
    for the master's use."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{CREAM}"></rect>', f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="{PAPER_INK}" stroke-width="1.4"></rect>',
         title_bar_cream(w, "2 TIMOTHY 2:20–21 · VESSELS IN A GREAT HOUSE")]
    k = min((h - 80) / 160, w / 640)
    sy = 40 + (h - 40) * 0.7
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(sy)}" width="{f(w * 0.88)}" height="{f(12 * k)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>')
    xs = [w * (0.16 + 0.23 * i) for i in range(4)]
    o.append(halo(xs[0], sy - 50 * k, 90 * k, "#FFE680", 0.6))
    gx = xs[0]                                                         # the gold cup on its stem
    o.append(f'<path d="M{f(gx - 34 * k)} {f(sy - 100 * k)} C {f(gx - 32 * k)} {f(sy - 60 * k)} {f(gx + 32 * k)} {f(sy - 60 * k)} {f(gx + 34 * k)} {f(sy - 100 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(gx - 4 * k)} {f(sy - 66 * k)} L {f(gx - 4 * k)} {f(sy - 14 * k)} L {f(gx - 24 * k)} {f(sy)} L {f(gx + 24 * k)} {f(sy)} L {f(gx + 4 * k)} {f(sy - 14 * k)} L {f(gx + 4 * k)} {f(sy - 66 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>')
    sx = xs[1]                                                         # the silver ewer
    o.append(f'<path d="M{f(sx - 26 * k)} {f(sy)} C {f(sx - 40 * k)} {f(sy - 50 * k)} {f(sx - 20 * k)} {f(sy - 80 * k)} {f(sx - 8 * k)} {f(sy - 100 * k)} L {f(sx - 22 * k)} {f(sy - 116 * k)} L {f(sx + 14 * k)} {f(sy - 112 * k)} L {f(sx + 8 * k)} {f(sy - 100 * k)} '
             f'C {f(sx + 20 * k)} {f(sy - 80 * k)} {f(sx + 40 * k)} {f(sy - 50 * k)} {f(sx + 26 * k)} {f(sy)} Z" fill="#C8C8D0" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(sx + 12 * k)} {f(sy - 92 * k)} C {f(sx + 50 * k)} {f(sy - 90 * k)} {f(sx + 46 * k)} {f(sy - 40 * k)} {f(sx + 28 * k)} {f(sy - 30 * k)}" fill="none" stroke="{INK}" stroke-width="{f(5 * k)}"></path>')
    wx = xs[2]                                                         # the wooden bowl
    o.append(f'<path d="M{f(wx - 46 * k)} {f(sy - 40 * k)} C {f(wx - 40 * k)} {f(sy + 2)} {f(wx + 40 * k)} {f(sy + 2)} {f(wx + 46 * k)} {f(sy - 40 * k)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(wx - 30 * k)} {f(sy - 24 * k)} C {f(wx - 10 * k)} {f(sy - 16 * k)} {f(wx + 10 * k)} {f(sy - 16 * k)} {f(wx + 30 * k)} {f(sy - 24 * k)}" fill="none" stroke="#5A3A1A" stroke-width="1.4"></path>')
    ex = xs[3]                                                         # the earthen pot
    o.append(f'<path d="M{f(ex - 22 * k)} {f(sy)} C {f(ex - 44 * k)} {f(sy - 30 * k)} {f(ex - 40 * k)} {f(sy - 70 * k)} {f(ex - 16 * k)} {f(sy - 84 * k)} L {f(ex + 16 * k)} {f(sy - 84 * k)} C {f(ex + 40 * k)} {f(sy - 70 * k)} {f(ex + 44 * k)} {f(sy - 30 * k)} {f(ex + 22 * k)} {f(sy)} Z" fill="#B85A32" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(ex - 6 * k)} {f(sy - 70 * k)} L {f(ex + 4 * k)} {f(sy - 44 * k)} L {f(ex - 4 * k)} {f(sy - 30 * k)}" fill="none" stroke="#5A2A12" stroke-width="1.6"></path>')
    for x, t in zip(xs, ("GOLD", "SILVER", "WOOD", "EARTH")):
        o.append(label(x, sy + 12 * k + 18, t, PAPER_INK, 10))
    o.append(label(xs[0], 40 + (h - 40) * 0.14, "UNTO HONOR · MEET FOR THE MASTER'S USE", "#7A4A10", 9.5, anchor="start"))
    return "".join(o)

def last_days(w, h, seed):
    """In the last days grievous times shall come: a street of a city at night, every door shut, the windows dark, a cup
    overturned on the paving — no one in it (Galatians' dark street)."""
    return dark_street(w, h, seed)

# ---- 2 Timothy 3 -----------------------------------------------------------------------------------------------------------
def aaron_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Aaron as Exodus draws him: a grey beard, a blue headcloth, a dark robe (on the kit silhouette)."""
    return robed(p, x, y, s, "#4A4A6A", head="#2A4A8A", cord="#1A1210", beard="#A8A296", flip=flip, up=up, extra=extra)

ROD = '<path d="M-66 -176 L -60 6" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M-66 -176 L -60 6" stroke="#6A4A2A" stroke-width="4.5" stroke-linecap="round"></path>'

ROD_UP = '<path d="M-64 -250 L -54 -170" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M-64 -250 L -54 -170" stroke="#6A4A2A" stroke-width="4.5" stroke-linecap="round"></path>'
_STRIPES = ''.join(f'<path d="M-15 {y} L 15 {y}" stroke="#0D0D0F" stroke-width="2.6"></path>' for y in (-200, -192, -184))

def magus(p, x, y, s, flip=False, up=None, extra=""):
    """A magician of Egypt (Exodus' look on the kit silhouette): a white linen robe, a white headcloth banded in black, dark
    skin, a rod in the hand."""
    return robed(p, x, y, s, "#E8E2D6", skin="#8A4A2E", head="#F3EFE6", cord="#0D0D0F", mantle="#C8C2B6", flip=flip, up=up, extra=_STRIPES + extra)

def jannes_jambres(p, w, h, seed):
    """As Jannes and Jambres withstood Moses: before Pharaoh's pylon gate at noon (Exodus' palace gate), the two magicians of
    Egypt at the right in their white robes and striped headcloths, rods in hand; Moses and Aaron at the left facing them,
    Aaron's rod lifted."""
    b = h * 0.88
    s = fig_k(w, h, 0.3, 0.66)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#8FD0E2", "#FFF0C8"), palace_gate(p, w, h, seed)]
    o.append(moses_fig(p, w * 0.14, b, s, flip=True) + aaron_fig(p, w * 0.27, b, s, flip=True, up=[(-22, -158), (-44, -180), (-56, -210)],
                                                                                              extra='<path d="M-60 -250 L -52 -170" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M-60 -250 L -52 -170" stroke="#6A4A2A" stroke-width="4.5" stroke-linecap="round"></path>'))
    o.append(magus(p, w * 0.73, b, s, up=[(-22, -158), (-44, -178), (-58, -200)], extra=ROD_UP) + magus(p, w * 0.86, b, s * 0.98, extra=ROD))
    o.append(plate_label(w * 0.8, b - 236 * s, "JANNES AND JAMBRES", "#12113A", 10, halo_="#FFF4C2") + plate_label(w * 0.2, b - 236 * s, "MOSES AND AARON", "#12113A", 10, halo_="#FFF4C2"))
    return "".join(o)

def three_gates(p, w, h, seed):
    """What things befell me at Antioch, at Iconium, at Lystra: three cells — the gates of the three towns of the first
    journey at evening, shut and empty, no one before them (Acts 13:50, 14:5–6, 14:19 are words only)."""
    def gate(i, name):
        def draw(pp, cw, ch):
            tones = (("#4A2A5A", "#FFB07A"), ("#3A2A5A", "#E8907A"), ("#2A2448", "#C87A6A"))[i]
            o = [sky(cw, ch, *tones), hills(cw, ch, ch * 0.5, seed + i, color="#5A4A5A", amp=8, step=50)]
            o.append(walls(-10, cw + 10, ch * 0.86, ch * 0.42, seed + i, towers=2, color=("#B89A7A", "#A88A6A", "#988A7A")[i]))
            o.append(ground(cw, ch, ch * 0.86, "#7A6A5A", dy=0))
            return "".join(o)
        return draw
    o = [cells(p, w, h, [gate(0, "ANTIOCH"), gate(1, "ICONIUM"), gate(2, "LYSTRA")])]
    o += [plate_label(w * (i + 0.5) / 3, h * 0.1, t, "#F3EFE6", 10, halo_="#2A1A3A") for i, t in enumerate(("ANTIOCH", "ICONIUM", "LYSTRA"))]
    return "".join(o)

def from_a_babe(p, w, h, seed):
    """From a babe thou hast known the sacred writings: the house at Lystra by lamplight, the boy Timothy sitting on the mat
    with the roll open across his knees, his mother Eunice beside him, his grandmother Lois on her stool pointing to the
    line."""
    b = h * 0.95
    k = fig_k(w, h, 0.3)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - 60 * k, max(w, h) * 0.55, f"{p}fb", op=0.5)]
    o.append(night_window(w * 0.7, b - 200 * k, min(w * 0.14, 90 * k), min(h * 0.3, 70 * k), seed))
    o.append(low_table(w * 0.62, b, 50 * k, k) + clay_lamp(w * 0.62 + 24 * k, b - 31 * k, k * 0.55))
    o.append(robed(p, w * 0.26, b, k, LOIS_LOOK["cloth"], woman=True, veil=LOIS_LOOK["veil"], hair=LOIS_LOOK["hair"], flip=True, pose="sit",
                   up=[(-22, -158), (-46, -140), (-68, -124)]))
    o.append(floor_mat(w * 0.34, b, 120 * k, k))
    o.append(scribe_seated(w * 0.46, b - 4 * k, k * 0.72, cloth=TIMOTHY_LOOK["cloth"], head=None, hair=TIMOTHY_LOOK["hair"], flip=False, stage="read"))
    o.append(robed(p, w * 0.58, b, k * 0.94, EUNICE_LOOK["cloth"], woman=True, veil=EUNICE_LOOK["veil"], flip=False))
    o.append(plate_label(w * 0.26, b - 186 * k, "LOIS", "#FFD23F", 10, halo_="#2A1A10") + plate_label(w * 0.47, b - 120 * k, "TIMOTHY", "#FFD23F", 10, halo_="#2A1A10")
             + plate_label(w * 0.58, b - 222 * k, "EUNICE", "#FFD23F", 10, halo_="#2A1A10"))
    return "".join(o)

# ---- 2 Timothy 4 -----------------------------------------------------------------------------------------------------------
def preach(p, w, h, seed):
    """Preach the word; be urgent in season, out of season: Timothy, older now with a short beard, standing on the steps of a
    colonnade in Ephesus with the roll in his hand, his other hand out; a few hearers in the street below, some turning
    away."""
    b = h * 0.94
    s = fig_k(w, h, 0.3, 0.68)
    o = [_defs(p), colonnade(w, h, b, seed)]
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(b - 26 * s)}" width="{f(w * 0.4)}" height="{f(26 * s)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.04)}" y="{f(b - 13 * s)}" width="{f(w * 0.48)}" height="{f(13 * s)}" fill="#D8CCB0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(timothy_fig_(p, w * 0.26, b - 26 * s, s, flip=True, up=[(-22, -158), (-48, -156), (-74, -168)], extra=_sheet(-40, -128, 34, 24, rot=6), beard=OLD_BEARD))
    o.append(gentile(p, w * 0.6, b, s * 0.96, 0) + gentile(p, w * 0.7, b, s * 0.96, 2, woman=True) + elder(p, w * 0.8, b, s * 0.96, 1) + gentile(p, w * 0.92, b, s * 0.96, 1, flip=True))
    return "".join(o)

def finish_line(w, h, seed):
    """I have fought the good fight, I have finished the course, I have kept the faith: the stadium at evening, the games
    over and the crowds gone, the course running empty to the finishing post, the last light gold on the post and the line
    drawn across the track."""
    o = [sky(w, h, "#3A2A5A", "#FFB070"), halo(w * 0.8, h * 0.42, max(w, h) * 0.45, "#FFE6B0", 0.5)]
    o.append(f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.22)} {f(w * 0.7)} {f(h * 0.22)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.52)} L -10 {f(h * 0.52)} Z" fill="#6A5A6A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(5):                                                  # the empty tiers
        y = h * (0.32 + i * 0.04)
        o.append(f'<path d="M-10 {f(y + 2)} C {f(w * 0.3)} {f(y - 6)} {f(w * 0.7)} {f(y - 6)} {f(w + 10)} {f(y + 2)}" fill="none" stroke="#8A7A8A" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.52)}" width="{f(w + 20)}" height="{f(h)}" fill="#D8A868" stroke="{INK}" stroke-width="2"></rect>')
    vx = w * 0.8
    for t in (-0.6, -0.2, 0.2, 0.6, 1.0):                               # the lanes running to the post
        o.append(f'<path d="M{f(vx + (t - 0.2) * w * 0.12)} {f(h * 0.54)} L {f(vx + (t - 0.2) * w * 1.4)} {f(h + 10)}" stroke="#F3E8C8" stroke-width="2" opacity="0.8"></path>')
    ly = h * 0.6
    o.append(f'<path d="M{f(w * 0.54)} {f(ly)} L {f(w + 10)} {f(ly - 2)}" stroke="#F3EFE6" stroke-width="{f(max(4, h * 0.016))}"></path>')
    o.append(f'<rect x="{f(vx - 5)}" y="{f(h * 0.3)}" width="10" height="{f(ly - h * 0.3)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
             + halo(vx, h * 0.3, h * 0.12, "#FFE680", 0.7)
             + f'<circle cx="{f(vx)}" cy="{f(h * 0.26)}" r="{f(h * 0.05)}" fill="none" stroke="#E8B830" stroke-width="{f(max(4, h * 0.02))}"></circle>')
    o.append(plate_label(w * 0.3, h * 0.12, "THE COURSE FINISHED", "#F3EFE6", 11, halo_="#3A2A5A"))
    return "".join(o)

def crown_laid(w, h, seed):
    """Henceforth there is laid up for me the crown of righteousness: on a plain stone table in a great light, a victor's
    wreath of gold laid up and waiting (no one drawn; the Lord, the righteous judge, is not drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2050"></rect>', radiance(w, h, seed, cy=0.42)]
    k = min(w / 520, h / 260)
    cx, ty = w * 0.5, h * 0.7
    o.append(f'<path d="M{f(cx - 150 * k)} {f(ty)} L {f(cx + 150 * k)} {f(ty)} L {f(cx + 130 * k)} {f(h + 10)} L {f(cx - 130 * k)} {f(h + 10)} Z" fill="#E8E2D6" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 160 * k)}" y="{f(ty - 10 * k)}" width="{f(320 * k)}" height="{f(12 * k)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    cy = ty - 40 * k
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(70 * k)}" ry="{f(26 * k)}" fill="none" stroke="#A8801E" stroke-width="{f(12 * k)}"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(70 * k)}" ry="{f(26 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(8 * k)}"></ellipse>')
    for i in range(18):                                                  # the leaves of the wreath
        a = math.radians(i * 20)
        x, y = cx + 70 * k * math.cos(a), cy + 26 * k * math.sin(a)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y - 4 * k)}" rx="{f(10 * k)}" ry="{f(4.5 * k)}" fill="#FFD23F" stroke="#8A6A10" stroke-width="1" transform="rotate({f(math.degrees(a) + 60)} {f(x)} {f(y - 4 * k)})"></ellipse>')
    o.append(plate_label(cx, h * 0.12, "THE CROWN OF RIGHTEOUSNESS", "#FFD23F", 11, halo_="#2A2050"))
    return "".join(o)

def scattered(w, h):
    """Demas forsook me … and went to Thessalonica; Crescens to Galatia, Titus to Dalmatia. Only Luke is with me … Tychicus I
    sent to Ephesus: the map of Acts — Rome lit, and the roads going out from it to Thessalonica, Galatia, Dalmatia and
    Ephesus, each tagged with the one who went; Troas, where the cloak was left."""
    regions = (("DALMATIA", 17.4, 43.6), ("GALATIA", 32.6, 39.6), "MACEDONIA", "ASIA", "ITALY",
               ("DEMAS", 21.4, 41.6), ("CRESCENS", 31.0, 40.4), ("TITUS", 16.8, 44.4), ("TYCHICUS", 25.6, 37.0), ("LUKE WITH ME", 12.5, 43.0))
    return geo.med_map(w, h, box=(10.5, 34.5, 36.0, 45.0), places=("ROME", "THESSALONICA", "EPHESUS", "TROAS", "CORINTH", "MILETUS"),
                       routes=[("ROME", (16.0, 41.2), (19.4, 41.2), "THESSALONICA"), ("ROME", (16.6, 42.6), (17.4, 43.4)), ("ROME", (18.0, 39.8), (22.0, 38.0), (26.0, 38.0), "EPHESUS"),
                               ("ROME", (18.0, 39.8), (24.0, 38.6), (29.0, 39.0), (32.4, 39.4))],
                       hi=("ROME",), regions=regions, lit_routes=[0, 1, 2, 3], size=9, rsize=10,
                       title="2 TIMOTHY 4:10–12 · ONLY LUKE IS WITH ME")

def cloak_books(w, h, seed):
    """The cloak that I left at Troas with Carpus, bring when thou comest, and the books, especially the parchments: a still
    life in a house at Troas — a heavy travelling cloak hung on a peg, and on the shelf below it the books (rolls tied up)
    and the parchments (a stack of skins and a bound packet of leaves)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A878"></rect>', lamp_glow(w * 0.7, h * 0.5, max(w, h) * 0.6, f"cb{seed}", op=0.4)]
    k = min(w / 520, h / 280)
    o.append(f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    px, py = w * 0.24, h * 0.12                                          # the peg and the cloak hanging from it
    bot = h * 0.8
    o.append(f'<path d="M{f(px - 12 * k)} {f(py + 4 * k)} C {f(px - 40 * k)} {f(py + 12 * k)} {f(px - 64 * k)} {f(py + 30 * k)} {f(px - 70 * k)} {f(py + 56 * k)} '
             f'C {f(px - 74 * k)} {f(py + 120 * k)} {f(px - 80 * k)} {f(bot - 40 * k)} {f(px - 86 * k)} {f(bot)} L {f(px + 86 * k)} {f(bot)} '
             f'C {f(px + 80 * k)} {f(bot - 40 * k)} {f(px + 74 * k)} {f(py + 120 * k)} {f(px + 70 * k)} {f(py + 56 * k)} C {f(px + 64 * k)} {f(py + 30 * k)} {f(px + 40 * k)} {f(py + 12 * k)} {f(px + 12 * k)} {f(py + 4 * k)} Z" '
             f'fill="#5A4A3E" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(px + d * k)} {f(py + 70 * k)} C {f(px + d * 1.1 * k)} {f(py + 140 * k)} {f(px + d * 1.2 * k)} {f(bot - 30 * k)} {f(px + d * 1.25 * k)} {f(bot)}" fill="none" stroke="#3A2E26" stroke-width="1.6"></path>' for d in (-44, -16, 16, 44))
             + f'<path d="M{f(px - 34 * k)} {f(py + 14 * k)} C {f(px - 40 * k)} {f(py + 50 * k)} {f(px - 20 * k)} {f(py + 74 * k)} {f(px)} {f(py + 78 * k)} C {f(px + 20 * k)} {f(py + 74 * k)} {f(px + 40 * k)} {f(py + 50 * k)} {f(px + 34 * k)} {f(py + 14 * k)} Z" fill="#4A3C32" stroke="{INK}" stroke-width="2"></path>'
             f'<circle cx="{f(px)}" cy="{f(py + 16 * k)}" r="{f(5 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="1.2"></circle>'
             f'<rect x="{f(px - 6 * k)}" y="{f(py - 6 * k)}" width="{f(12 * k)}" height="{f(12 * k)}" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect>')
    sy = h * 0.6                                                         # the shelf
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(sy)}" width="{f(w * 0.48)}" height="{f(12 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(3):                                                   # the books: rolls tied up
        o.append(sealed_scroll(w * (0.54 + 0.07 * i), sy - 10 * k - (i % 2) * 2, 0.5 * k, rot=-4 + 6 * i, seal="#7A5A3A"))
    o.append(f'<path d="M{f(w * 0.74)} {f(sy)} L {f(w * 0.9)} {f(sy)} L {f(w * 0.9)} {f(sy - 16 * k)} L {f(w * 0.74)} {f(sy - 16 * k)} Z" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.75)} {f(sy - 16 * k)} L {f(w * 0.89)} {f(sy - 16 * k)} L {f(w * 0.89)} {f(sy - 28 * k)} L {f(w * 0.75)} {f(sy - 28 * k)} Z" fill="#F3EAD0" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.76)} {f(sy - 28 * k)} L {f(w * 0.88)} {f(sy - 28 * k)} L {f(w * 0.88)} {f(sy - 38 * k)} L {f(w * 0.76)} {f(sy - 38 * k)} Z" fill="#E0D0B0" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.82)} {f(sy)} L {f(w * 0.82)} {f(sy - 38 * k)}" stroke="#8A3A2A" stroke-width="{f(2.4 * k)}"></path>')
    o.append(plate_label(px, h * 0.08, "THE CLOAK", "#3A1E0E", 10, halo_="#E8D0A0") + plate_label(w * 0.6, sy + 30 * k, "THE BOOKS", "#3A1E0E", 10, halo_="#E8D0A0")
             + plate_label(w * 0.82, sy + 30 * k, "THE PARCHMENTS", "#3A1E0E", 10, halo_="#E8D0A0"))
    return "".join(o)

def empty_court(p, w, h, seed):
    """At my first defence no one took my part, but all forsook me: the judgment-seat in the forum, empty, the scales beside it
    (Romans' drawing) — no one before it."""
    return judgment_seat(p, w, h, seed)

from rom.art import judgment_seat, oracles
from gal.art import dark_street, colonnade, gentile

def gentle(p, w, h, seed):
    """The Lord's servant must not strive, but be gentle towards all, apt to teach, forbearing, in meekness correcting them
    that oppose themselves: the room where the church meets, Timothy (his short beard now) sitting on the bench with the roll
    open on his knee and his hand open, a man standing over him with his arm flung out in dispute; two of the brethren
    listening at the door."""
    b = h * 0.95
    s = fig_k(w, h)
    o = [_defs(p), church_room(w, h, b, seed)]
    o.append(bench(w * 0.16, b, w * 0.2, s))
    o.append(timothy_fig_(p, w * 0.3, b, s, flip=True, pose="sit", seat=None, beard=OLD_BEARD, up=[(-22, -158), (-46, -150), (-66, -150)]))
    o.append(robed(p, w * 0.56, b, s, "#6A3A3A", head="#2A2A3A", cord="#1A1210", beard="#2A1A10", mantle="#3A2A2A", up=[(-22, -158), (-50, -170), (-74, -170)]))
    o.append(elder(p, w * 0.8, b, s * 0.98, 2) + young_man(p, w * 0.9, b, s * 0.98, 0))
    return "".join(o)

def cell_night(w, h, seed, chain_=True, scroll=True):
    """The cell at night with no one in it to see (the cover, an end panel): the stone wall, the barred window with the moon
    beyond, the lamp burning in its niche, the chain hanging from its ring, and the letter rolled and sealed on the bench."""
    b = h * 0.86
    o = [stone_wall(w, h, b, seed)]
    k = min(w / 520, h / 400)
    o.append(barred_window(w * 0.56, h * 0.14, 90 * k, 70 * k))
    o.append(f'<circle cx="{f(w * 0.56 + 62 * k)}" cy="{f(h * 0.14 + 22 * k)}" r="{f(9 * k)}" fill="#F3EFE6" opacity="0.9"></circle>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.14 + 70 * k)} L {f(w * 0.3)} {f(b)} L {f(w * 0.7)} {f(b)} L {f(w * 0.56 + 90 * k)} {f(h * 0.14 + 70 * k)} Z" fill="#AAB8E0" opacity="0.12"></path>')
    nx = w * 0.24
    o.append(f'<path d="M{f(nx - 26 * k)} {f(h * 0.5)} L {f(nx - 26 * k)} {f(h * 0.42)} C {f(nx - 26 * k)} {f(h * 0.36)} {f(nx + 26 * k)} {f(h * 0.36)} {f(nx + 26 * k)} {f(h * 0.42)} L {f(nx + 26 * k)} {f(h * 0.5)} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>')
    o.append(lamp_glow(nx, h * 0.47, max(w, h) * 0.55, f"cn{seed}", op=0.55) + clay_lamp(nx - 18 * k, h * 0.5, k * 0.8))
    if chain_:
        rx, ry = w * 0.84, h * 0.4
        o.append(f'<circle cx="{f(rx)}" cy="{f(ry)}" r="{f(10 * k)}" fill="none" stroke="#6A6A74" stroke-width="{f(4 * k)}"></circle>'
                 + chain(rx, ry + 10 * k, w * 0.9, b - 4, s=k, sag=0.1))
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(b - 46 * k)}" width="{f(w * 0.64)}" height="{f(16 * k)}" fill="#4A3A2A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.12)} {f(b - 30 * k)} L {f(w * 0.12)} {f(b)} M{f(w * 0.68)} {f(b - 30 * k)} L {f(w * 0.68)} {f(b)}" stroke="#3A2A1A" stroke-width="{f(10 * k)}"></path>')
    if scroll: o.append(sealed_scroll(w * 0.42, b - 52 * k, 0.9 * k, rot=-6))
    o.append(_vignette(w, h, f"cnv{seed}", cx=0.4, cy=0.5, op=0.55))
    return "".join(o)
