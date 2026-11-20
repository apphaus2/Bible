"""Drawings for 1 Timothy 3–6 (ti1.art carries the cast and chapters 1–2): the bishop and the deacons as plates, the pillar
and ground of the truth, the palæstra and the lamp, Timothy before the elders and under their hands, the church as a
family, the widows, the cup of wine, food and covering, the root of all kinds of evil, the rich, the deposit guarded."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from ti1.art import *
from ti1.art import _sheet, _defs, _eph_window, _seated_lap
from co1.art3 import athlete
from co2.art2 import chest_open, bag
import exodus as EX

def _check(x, y, k, neg=False):
    """A gold tick, or a red bar for a 'not', at (x, y)."""
    if neg: return f'<path d="M{f(x - 6 * k)} {f(y)} L {f(x + 6 * k)} {f(y)}" stroke="#FF6A4A" stroke-width="{f(3 * k)}" stroke-linecap="round"></path>'
    return f'<path d="M{f(x - 6 * k)} {f(y)} L {f(x - 1 * k)} {f(y + 5 * k)} L {f(x + 7 * k)} {f(y - 6 * k)}" fill="none" stroke="{GOLD}" stroke-width="{f(2.6 * k)}" stroke-linecap="round" stroke-linejoin="round"></path>'

def qualities(p, w, h, title, items, fig, cols=2, foot=None):
    """A plate of qualifications: the title bar, at the left the man the office asks for (fig(p, x, y, s)), at the right his
    qualities in columns — a gold tick for what he must be, a red bar for what he must not be (labels: the ASV's words)."""
    o = [plate_bg(w, h, title), mk.defs(p, *ALL, "ManUp", "WomanUp")]
    b = h - 14
    s = (h - 60) / 215
    fx = min(w * 0.14, 80 * s + 20)
    o.append(halo(fx, b - 100 * s, 110 * s, "#FFE680", 0.25) + fig(p, fx, b, s))
    x0 = fx + 80 * s
    rows_ = math.ceil(len(items) / cols)
    top = 46
    lh = min(24, (h - top - 14 - (18 if foot else 0)) / rows_)
    cw = (w - x0 - 10) / cols
    size = max(8.5, min(11, lh * 0.5, cw / 26))
    for i, (txt, neg) in enumerate(items):
        c, r = divmod(i, rows_)
        x = x0 + c * cw; y = top + lh * (r + 0.6)
        o.append(_check(x + 8, y - 3, 1, neg) + label(x + 20, y + 1, txt, "#FFB0A0" if neg else "#F3EFE6", size, anchor="start"))
    if foot: o.append(label(x0 + (w - x0) / 2, h - 12, foot, CY, 9.5))
    return "".join(o)

def bishop_plate(p, w, h):
    """The bishop (3:2–4): a plate — an elder with his staff at the left, his qualities at the right."""
    def fig(pp, x, y, s): return elder(pp, x, y, s, 0, extra='<path d="M-40 -186 L -34 4" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M-40 -186 L -34 4" stroke="#8A6A3A" stroke-width="4.5" stroke-linecap="round"></path>', up=[(-22, -158), (-34, -124), (-38, -100)])
    items = [("WITHOUT REPROACH", False), ("THE HUSBAND OF ONE WIFE", False), ("TEMPERATE", False), ("SOBER-MINDED", False), ("ORDERLY", False),
             ("GIVEN TO HOSPITALITY", False), ("APT TO TEACH", False), ("NO BRAWLER", True), ("NO STRIKER", True), ("GENTLE", False),
             ("NOT CONTENTIOUS", True), ("NO LOVER OF MONEY", True), ("RULETH WELL HIS OWN HOUSE", False), ("NOT A NOVICE", True)]
    return qualities(p, w, h, "1 TIMOTHY 3:1–7 · THE OFFICE OF A BISHOP", items, fig, cols=2)

def deacon_plate(p, w, h):
    """The deacons (3:8–12): a plate — a deacon with a basket of bread at the left, his qualities at the right."""
    def fig(pp, x, y, s):
        basket = ('<path d="M-78 -116 L -44 -116 L -48 -94 L -74 -94 Z" fill="#B8884A" stroke="#0D0D0F" stroke-width="1.6"></path>'
                  '<ellipse cx="-68" cy="-118" rx="7" ry="5" fill="#D8A060" stroke="#0D0D0F" stroke-width="1"></ellipse><ellipse cx="-56" cy="-119" rx="7" ry="5" fill="#D8A060" stroke="#0D0D0F" stroke-width="1"></ellipse>')
        return young_man(pp, x, y, s, 1, up=[(-22, -158), (-40, -128), (-58, -116)], extra=basket)
    items = [("GRAVE", False), ("NOT DOUBLE-TONGUED", True), ("NOT GIVEN TO MUCH WINE", True), ("NOT GREEDY OF FILTHY LUCRE", True),
             ("A PURE CONSCIENCE", False), ("FIRST BE PROVED", False), ("BLAMELESS", False), ("HUSBANDS OF ONE WIFE", False),
             ("RULING THEIR CHILDREN WELL", False), ("WOMEN: GRAVE, NOT SLANDERERS", False), ("TEMPERATE", False), ("FAITHFUL IN ALL THINGS", False)]
    return qualities(p, w, h, "1 TIMOTHY 3:8–12 · DEACONS IN LIKE MANNER", items, fig, cols=2)

def pillar_plate(w, h):
    """The house of God, which is the church of the living God, the pillar and ground of the truth: a technical plate — the
    elevation of one great column standing on its stepped base and footing, bearing the beam of the house, the light
    falling on it; dimension lines and tags: THE PILLAR · THE GROUND (the stay that holds it) · THE TRUTH it bears up."""
    o = [plate_bg(w, h, "1 TIMOTHY 3:15 · THE PILLAR AND GROUND OF THE TRUTH")]
    cx = w * 0.42
    top, base = 74, h - 34
    ch = base - top
    cw = min(w * 0.12, ch * 0.16)
    o.append(halo(cx, top + ch * 0.2, ch * 0.7, "#FFE680", 0.22))
    # the beam of the house across the top, and its roof line
    o.append(f'<rect x="{f(cx - cw * 3.4)}" y="{f(top - 4)}" width="{f(cw * 6.8)}" height="{f(ch * 0.07)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(cx - cw * 3.6)} {f(top - 4)} L {f(cx)} {f(top - 4 - ch * 0.1)} L {f(cx + cw * 3.6)} {f(top - 4)} Z" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></path>')
    cap_y = top - 4 + ch * 0.07
    o.append(f'<path d="M{f(cx - cw * 0.95)} {f(cap_y)} L {f(cx + cw * 0.95)} {f(cap_y)} L {f(cx + cw * 0.62)} {f(cap_y + ch * 0.06)} L {f(cx - cw * 0.62)} {f(cap_y + ch * 0.06)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></path>'
             f'<circle cx="{f(cx - cw * 0.8)}" cy="{f(cap_y + ch * 0.03)}" r="{f(cw * 0.18)}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>'
             f'<circle cx="{f(cx + cw * 0.8)}" cy="{f(cap_y + ch * 0.03)}" r="{f(cw * 0.18)}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
    sh_t, sh_b = cap_y + ch * 0.06, base - ch * 0.16
    o.append(f'<path d="M{f(cx - cw * 0.55)} {f(sh_t)} L {f(cx + cw * 0.55)} {f(sh_t)} L {f(cx + cw * 0.62)} {f(sh_b)} L {f(cx - cw * 0.62)} {f(sh_b)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2.2"></path>')
    o += [f'<path d="M{f(cx + cw * d)} {f(sh_t + 3)} L {f(cx + cw * d * 1.12)} {f(sh_b - 3)}" stroke="#B8B0A0" stroke-width="1.4"></path>' for d in (-0.36, -0.12, 0.12, 0.36)]
    for i, (wd, hh) in enumerate(((0.8, 0.035), (1.0, 0.035), (1.3, 0.045))):          # the base mouldings and the stepped footing
        y = sh_b + ch * sum(x[1] for x in ((0.8, 0.035), (1.0, 0.035), (1.3, 0.045))[:i])
        o.append(f'<rect x="{f(cx - cw * wd)}" y="{f(y)}" width="{f(cw * wd * 2)}" height="{f(ch * hh)}" fill="#D8D0C0" stroke="{INK}" stroke-width="1.8"></rect>')
    gy = sh_b + ch * 0.115
    o.append(f'<rect x="{f(cx - cw * 2.6)}" y="{f(gy)}" width="{f(cw * 5.2)}" height="{f(base - gy)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(cx - cw * 2.6 + cw * 5.2 * t)} {f(gy)} L {f(cx - cw * 2.6 + cw * 5.2 * t)} {f(base)}" stroke="#6A5A4A" stroke-width="1.4"></path>' for t in (0.25, 0.5, 0.75)))
    o.append(f'<path d="M-10 {f(base)} L {f(w + 10)} {f(base)}" stroke="{CY}" stroke-width="1.6" stroke-dasharray="6 5"></path>')
    tx = cx + cw * 3.0
    o.append(tag(cx + cw * 0.6, (sh_t + sh_b) / 2, "THE PILLAR", tx, (sh_t + sh_b) / 2 - ch * 0.08, size=10))
    o.append(tag(cx + cw * 2.0, (gy + base) / 2, "THE GROUND", tx, (gy + base) / 2, size=10))
    o.append(tag(cx + cw * 2.6, top + ch * 0.01, "OF THE TRUTH", tx, top + ch * 0.12, color=GOLD, size=10))
    lx = max(16, cx - cw * 3.6 - 150)
    o.append(label(lx, top + ch * 0.36, "THE HOUSE OF GOD", CY, 10, anchor="start") + label(lx, top + ch * 0.36 + 16, "THE CHURCH OF THE", CY, 9, anchor="start")
             + label(lx, top + ch * 0.36 + 30, "LIVING GOD", CY, 9, anchor="start"))
    return "".join(o)

# ---- 1 Timothy 4 -----------------------------------------------------------------------------------------------------------
def palaestra(p, w, h, seed):
    """Bodily exercise is profitable for a little; but godliness is profitable for all things: two cells — the palæstra in
    the afternoon, two runners striding and a boxer at the post (BODILY EXERCISE); and Timothy at night reading the letter
    by his lamp (GODLINESS)."""
    def gym(pp, cw, ch):
        b = ch * 0.92
        o = [sky(cw, ch, "#E89A5A", "#FFE0A8"), f'<rect x="-4" y="{f(ch * 0.12)}" width="{f(cw + 8)}" height="{f(ch * 0.05)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>']
        for i in range(6):
            x = cw * (0.04 + i * 0.19)
            o.append(f'<rect x="{f(x)}" y="{f(ch * 0.17)}" width="{f(cw * 0.04)}" height="{f(b - ch * 0.17)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
        o.append(f'<rect x="-4" y="{f(b)}" width="{f(cw + 8)}" height="{f(ch)}" fill="#E8C890" stroke="{INK}" stroke-width="2"></rect>')
        s = fit(b, b - ch * 0.66) * 0.92
        o.append(athlete(cw * 0.22, b, s, "run_a") + athlete(cw * 0.5, b, s * 0.96, "run_b", skin="#B98A6E", cloth="#E8E2D6", hair="#3A2214") + athlete(cw * 0.8, b, s, "box", skin="#D9A27A", gloves=True))
        return "".join(o)
    def lamp(pp, cw, ch): return timothy_reads(pp, cw, ch, seed, window=night_window_)
    o = [cells(p, w, h, [gym, lamp])]
    o.append(plate_label(w * 0.25, h * 0.08, "BODILY EXERCISE · FOR A LITTLE", "#12113A", 9.5, halo_="#FFF4C2")
             + plate_label(w * 0.75, h * 0.08, "GODLINESS · FOR ALL THINGS", GOLD, 9.5))
    return "".join(o)

def night_window_(x, y, ww, hh, night, seed): return night_window(x, y, ww, hh, seed)

def church_room(w, h, b, seed, night=False):
    """The room where the church meets at Ephesus: plain plastered walls, a window on the city, a bench along the wall."""
    o = [room(w, h, b, wall="#D8C098" if not night else "#5A3E2E", floor="#8A6A4A" if not night else "#3A2A20")]
    o.append(_eph_window(w * 0.42, b - h * 0.62, min(w * 0.16, h * 0.4), min(h * 0.3, w * 0.12), night, seed))
    return "".join(o)

def youth(p, w, h, seed):
    """Let no man despise thy youth; but be thou an ensample to them that believe: the church at Ephesus gathered by day,
    Timothy young and beardless standing with the open roll and his hand out, teaching; the elders with their grey beards
    sitting on the bench and standing at the right, listening."""
    b = h * 0.95
    s = fig_k(w, h)
    o = [_defs(p), church_room(w, h, b, seed)]
    o.append(timothy_fig_(p, w * 0.2, b, s, flip=True, up=[(-22, -158), (-48, -150), (-72, -156)], extra=_sheet(-40, -128, 36, 26, rot=6)))
    o.append(bench(w * 0.56, b, w * 0.2, s))
    o.append(robed(p, w * 0.6, b, s, "#5A6A7A", head="#E8E2D6", beard="#C8C2B6", mantle="#3A4A5A", pose="sit", seat=None))
    o.append(robed(p, w * 0.72, b, s, "#6A5A4A", head="#2A3A4A", beard="#9A948A", mantle="#4A3A2A", pose="sit", seat=None))
    o.append(elder(p, w * 0.86, b, s, 2) + woman(p, w * 0.95, b, s, 0, old=True))
    return "".join(o)

def _hair_cap(cx, cy, r, color):
    """Short hair over the top of the kneeling figure's round head (exodus.kneel draws a bare head)."""
    return (f'<path d="M{f(cx - r)} {f(cy + r * 0.1)} A {f(r)} {f(r)} 0 0 1 {f(cx + r * 0.9)} {f(cy - r * 0.3)} Q {f(cx)} {f(cy - r * 0.5)} {f(cx - r * 0.5)} {f(cy + r * 0.2)} Z" '
            f'fill="{color}" stroke="{INK}" stroke-width="1.2"></path>')

def hands_laid(p, w, h, seed):
    """The gift that is in thee … given thee by prophecy, with the laying on of the hands of the presbytery: Timothy kneeling
    in the midst, the elders standing about him with their hands laid on his head, a soft light falling from the window
    above (no figure in it)."""
    b = h * 0.95
    s = fig_k(w, h)
    o = [_defs(p), church_room(w, h, b, seed)]
    o.append(f'<path d="M{f(w * 0.42)} {f(b - h * 0.62)} L {f(w * 0.36)} {f(b)} L {f(w * 0.66)} {f(b)} L {f(w * 0.58)} {f(b - h * 0.62)} Z" fill="#FFF4C2" opacity="0.35"></path>')
    kx = w * 0.5
    reach = [(-22, -158), (-46, -150), (-68, -140)]                 # the hand comes to rest on the kneeling man's head
    o.append(elder(p, kx - 200 * s, b, s * 0.98, 3, flip=True) + elder(p, kx - 90 * s, b, s, 1, flip=True, up=reach))
    o.append(EX.kneel(kx - 40 * s, b, s * 1.05, color=TIMOTHY_LOOK["cloth"], skin=SKIN)
             + _hair_cap(kx - 22.15 * s, b - 126 * s, 13.65 * s, TIMOTHY_LOOK['hair']))
    o.append(elder(p, kx + 50 * s, b, s, 0, up=reach) + elder(p, kx + 150 * s, b, s * 0.98, 2))
    return "".join(o)

# ---- 1 Timothy 5 -----------------------------------------------------------------------------------------------------------
def family(p, w, h, seed):
    """The elder as a father; the younger men as brethren: the elder women as mothers; the younger as sisters: the courtyard of
    the house where the church meets, Timothy in the midst; at the left an old man and two young men, at the right an old
    woman and two young women; tags over each."""
    b = h * 0.95
    s = fig_k(w, h, 0.32, 0.66)
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"), f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(b - h * 0.2)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#C8B088" stroke="{INK}" stroke-width="1.6"></rect>',
         f'<rect x="{f(w * 0.44)}" y="{f(h * 0.36)}" width="{f(w * 0.12)}" height="{f(b - h * 0.36)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8B07A" stroke="{INK}" stroke-width="2"></rect>']
    o.append(elder(p, w * 0.07, b, s, 0, flip=True) + young_man(p, w * 0.17, b, s * 0.98, 0, flip=True) + young_man(p, w * 0.27, b, s, 1, flip=True))
    o.append(timothy_fig_(p, w * 0.5, b, s, up=[(-22, -158), (-46, -150), (-68, -152)]))
    o.append(woman(p, w * 0.73, b, s, 2) + woman(p, w * 0.83, b, s, 1) + woman(p, w * 0.93, b, s, 0, old=True))
    ty = b - 228 * s
    o.append(plate_label(w * 0.07, ty, "AS A FATHER", "#12113A", 9, halo_="#F3EFE6") + plate_label(w * 0.22, ty - 14, "AS BRETHREN", "#12113A", 9, halo_="#F3EFE6")
             + plate_label(w * 0.78, ty - 14, "AS SISTERS", "#12113A", 9, halo_="#F3EFE6") + plate_label(w * 0.93, ty, "AS MOTHERS", "#12113A", 9, halo_="#F3EFE6"))
    return "".join(o)

def widow_prays(p, w, h, seed):
    """She that is a widow indeed, and desolate, hath her hope set on God, and continueth in supplications and prayers night
    and day: a bare room at night, the widow in her dark veil kneeling by the lamp, the moon at the small window."""
    b = h * 0.92
    o = [room(w, h, b, wall="#3E3242", floor="#2A2228"), lamp_glow(w * 0.4, b - h * 0.2, max(w, h) * 0.5, f"{p}wl", op=0.5)]
    o.append(night_window(w * 0.62, b - h * 0.7, min(w * 0.14, h * 0.3), min(h * 0.26, w * 0.12), seed))
    o.append(f'<circle cx="{f(w * 0.62 + min(w * 0.14, h * 0.3) * 0.7)}" cy="{f(b - h * 0.62)}" r="{f(h * 0.03)}" fill="#F3EFE6"></circle>')
    k = min(h, w * 0.5) / 300
    o.append(low_table(w * 0.24, b, 50 * k, k) + clay_lamp(w * 0.24 + 24 * k, b - 31 * k, k * 0.6))
    o.append(EX.kneel(w * 0.44, b, k * 1.1, color="#2A2A3A", skin="#1F2A4A"))                # veiled from head to foot
    return "".join(o)

def enrolled(w, h):
    """Let none be enrolled as a widow under threescore years old … well reported of for good works: a plate on cream paper —
    the church's roll open at the top (THREESCORE YEARS · THE WIFE OF ONE MAN), and under it five emblems of good works: a
    cradle (brought up children), an open door and a loaf (hospitality to strangers), a basin and a towel (washed the
    saints' feet), a cup held out (relieved the afflicted), a lamp (every good work)."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{CREAM}"></rect>', f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="{PAPER_INK}" stroke-width="1.4"></rect>',
         title_bar_cream(w, "1 TIMOTHY 5:9–10 · ENROLLED AS A WIDOW")]
    rw, rh = min(w * 0.6, 420), min(h * 0.16, 44)
    rx, ry = w / 2 - rw / 2, 44
    o.append(open_letter(rx, ry, rw, rh, rows=2, seed=3))
    o.append(label(w / 2, ry + rh + 16, "THREESCORE YEARS · THE WIFE OF ONE MAN", PAPER_INK, 10))
    cy = ry + rh + 30 + (h - ry - rh - 60) * 0.5
    k = min((h - ry - rh - 70) / 110, w / 760)
    xs = [w * (0.1 + 0.2 * i) for i in range(5)]
    def cradle(x, y): return (f'<path d="M{f(x - 34 * k)} {f(y)} C {f(x - 30 * k)} {f(y + 26 * k)} {f(x + 30 * k)} {f(y + 26 * k)} {f(x + 34 * k)} {f(y)} Z" fill="#B8884A" stroke="{INK}" stroke-width="1.8"></path>'
                              f'<path d="M{f(x - 40 * k)} {f(y + 30 * k)} C {f(x - 20 * k)} {f(y + 20 * k)} {f(x + 20 * k)} {f(y + 20 * k)} {f(x + 40 * k)} {f(y + 30 * k)}" fill="none" stroke="{INK}" stroke-width="3"></path>'
                              f'<path d="M{f(x - 30 * k)} {f(y - 2 * k)} C {f(x - 10 * k)} {f(y - 10 * k)} {f(x + 10 * k)} {f(y - 10 * k)} {f(x + 30 * k)} {f(y - 2 * k)}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.4"></path>')
    def door(x, y): return (f'<rect x="{f(x - 30 * k)}" y="{f(y - 40 * k)}" width="{f(30 * k)}" height="{f(70 * k)}" fill="#FFE6A0" stroke="{INK}" stroke-width="1.8"></rect>'
                            f'<path d="M{f(x)} {f(y - 40 * k)} L {f(x + 16 * k)} {f(y - 34 * k)} L {f(x + 16 * k)} {f(y + 36 * k)} L {f(x)} {f(y + 30 * k)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></path>'
                            f'<ellipse cx="{f(x + 30 * k)}" cy="{f(y + 22 * k)}" rx="{f(14 * k)}" ry="{f(8 * k)}" fill="#D8A060" stroke="{INK}" stroke-width="1.4"></ellipse>')
    def basin(x, y): return (f'<path d="M{f(x - 36 * k)} {f(y + 4 * k)} C {f(x - 30 * k)} {f(y + 30 * k)} {f(x + 30 * k)} {f(y + 30 * k)} {f(x + 36 * k)} {f(y + 4 * k)} Z" fill="#B85A32" stroke="{INK}" stroke-width="1.8"></path>'
                             f'<ellipse cx="{f(x)}" cy="{f(y + 4 * k)}" rx="{f(36 * k)}" ry="{f(7 * k)}" fill="#8FD0E2" stroke="{INK}" stroke-width="1.6"></ellipse>'
                             f'<path d="M{f(x - 10 * k)} {f(y - 30 * k)} L {f(x + 20 * k)} {f(y - 30 * k)} L {f(x + 26 * k)} {f(y - 6 * k)} L {f(x - 6 * k)} {f(y - 4 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></path>')
    def cup(x, y): return (f'<path d="M{f(x - 40 * k)} {f(y + 20 * k)} C {f(x - 20 * k)} {f(y + 8 * k)} {f(x - 12 * k)} {f(y + 6 * k)} {f(x - 4 * k)} {f(y + 8 * k)}" fill="none" stroke="{INK}" stroke-width="{f(10 * k)}" stroke-linecap="round"></path>'
                           f'<path d="M{f(x - 40 * k)} {f(y + 20 * k)} C {f(x - 20 * k)} {f(y + 8 * k)} {f(x - 12 * k)} {f(y + 6 * k)} {f(x - 4 * k)} {f(y + 8 * k)}" fill="none" stroke="{SKIN}" stroke-width="{f(7 * k)}" stroke-linecap="round"></path>'
                           f'<path d="M{f(x - 6 * k)} {f(y - 14 * k)} L {f(x + 22 * k)} {f(y - 14 * k)} L {f(x + 18 * k)} {f(y + 8 * k)} L {f(x - 2 * k)} {f(y + 8 * k)} Z" fill="#B85A32" stroke="{INK}" stroke-width="1.6"></path>')
    def lampk(x, y): return halo(x, y - 6 * k, 30 * k, "#FFE680", 0.6) + clay_lamp(x - 20 * k, y + 14 * k, k * 1.1)
    tags = ["BROUGHT UP CHILDREN", "HOSPITALITY TO STRANGERS", "WASHED THE SAINTS' FEET", "RELIEVED THE AFFLICTED", "EVERY GOOD WORK"]
    for x, fn, t in zip(xs, (cradle, door, basin, cup, lampk), tags):
        o.append(fn(x, cy))
        o.append(two_lines(x, min(h - 44, cy + 46 * k), t, PAPER_INK, max(7.5, min(9.5, w / 80))))
    return "".join(o)

def wine_cup(w, h, seed):
    """Be no longer a drinker of water, but use a little wine for thy stomach's sake: a still life on the low table by the
    window at morning — a jug of water and a cup, and beside them a small flask of wine and a little poured in a cup, a loaf."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A878"></rect>']
    ty = h * 0.6
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.08)}" width="{f(w * 0.26)}" height="{f(h * 0.4)}" fill="#8FD0E2" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(w * 0.73)} {f(h * 0.08)} L {f(w * 0.73)} {f(h * 0.48)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.38)} C {f(w * 0.66)} {f(h * 0.3)} {f(w * 0.78)} {f(h * 0.32)} {f(w * 0.86)} {f(h * 0.36)} L {f(w * 0.86)} {f(h * 0.48)} L {f(w * 0.6)} {f(h * 0.48)} Z" fill="#9A8A6A"></path>')
    o.append(f'<path d="M-10 {f(ty)} L {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></path>')
    k = min(w / 520, h / 240)
    def jug(x, y, s, col):
        return (f'<path d="M{f(x - 22 * s)} {f(y)} C {f(x - 34 * s)} {f(y - 40 * s)} {f(x - 20 * s)} {f(y - 70 * s)} {f(x - 10 * s)} {f(y - 80 * s)} L {f(x + 10 * s)} {f(y - 80 * s)} '
                f'C {f(x + 20 * s)} {f(y - 70 * s)} {f(x + 34 * s)} {f(y - 40 * s)} {f(x + 22 * s)} {f(y)} Z" fill="{col}" stroke="{INK}" stroke-width="2"></path>'
                f'<path d="M{f(x + 14 * s)} {f(y - 70 * s)} C {f(x + 40 * s)} {f(y - 70 * s)} {f(x + 40 * s)} {f(y - 40 * s)} {f(x + 24 * s)} {f(y - 34 * s)}" fill="none" stroke="{INK}" stroke-width="{f(4 * s)}"></path>')
    def cup_(x, y, s, fill):
        return (f'<path d="M{f(x - 16 * s)} {f(y - 30 * s)} L {f(x + 16 * s)} {f(y - 30 * s)} L {f(x + 12 * s)} {f(y)} L {f(x - 12 * s)} {f(y)} Z" fill="#B85A32" stroke="{INK}" stroke-width="1.8"></path>'
                f'<ellipse cx="{f(x)}" cy="{f(y - 30 * s)}" rx="{f(16 * s)}" ry="{f(4 * s)}" fill="{fill}" stroke="{INK}" stroke-width="1.4"></ellipse>')
    y = ty + h * 0.2
    o.append(jug(w * 0.16, y, k * 1.3, "#B85A32") + cup_(w * 0.3, y, k * 1.2, "#8FD0E2"))
    o.append(jug(w * 0.56, y, k * 0.8, "#5A2A3A") + cup_(w * 0.68, y, k * 1.2, "#7A1A2A"))
    o.append(f'<ellipse cx="{f(w * 0.86)}" cy="{f(y - 12 * k)}" rx="{f(46 * k)}" ry="{f(22 * k)}" fill="#C8884A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.86 - 30 * k)} {f(y - 20 * k)} L {f(w * 0.86 + 30 * k)} {f(y - 20 * k)}" stroke="#8A5A2A" stroke-width="2"></path>')
    o.append(plate_label(w * 0.23, ty + h * 0.32, "WATER", "#F3EFE6", 10, halo_="#3A1E0E") + plate_label(w * 0.62, ty + h * 0.32, "A LITTLE WINE", "#FFD23F", 10, halo_="#3A1E0E"))
    return "".join(o)

# ---- 1 Timothy 6 -----------------------------------------------------------------------------------------------------------
def food_covering(w, h, seed):
    """We brought nothing into the world, for neither can we carry anything out; but having food and covering we shall be
    therewith content: a bare room by the light of the door — on the floor a mat, a loaf and a cup of water, a plain cloak
    folded, nothing more."""
    b = h * 0.86
    o = [room(w, h, b, wall="#C8A878", floor="#8A6A4A"),
         f'<path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.08)} {f(h * 0.18)} L {f(w * 0.24)} {f(h * 0.18)} L {f(w * 0.24)} {f(b)} Z" fill="#FFF4C2" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.24)} {f(b)} L {f(w * 0.6)} {f(h)} L {f(w * 0.08)} {f(h)} Z" fill="#FFF4C2" opacity="0.35"></path>']
    k = min(w / 600, h / 260)
    mx = w * 0.56
    o.append(f'<path d="M{f(mx - 120 * k)} {f(b + 6 * k)} L {f(mx + 140 * k)} {f(b + 6 * k)} L {f(mx + 160 * k)} {f(b + 36 * k)} L {f(mx - 140 * k)} {f(b + 36 * k)} Z" fill="#B8985A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<ellipse cx="{f(mx - 60 * k)}" cy="{f(b + 4 * k)}" rx="{f(36 * k)}" ry="{f(16 * k)}" fill="#C8884A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<path d="M{f(mx - 6 * k)} {f(b - 20 * k)} L {f(mx + 20 * k)} {f(b - 20 * k)} L {f(mx + 16 * k)} {f(b + 10 * k)} L {f(mx - 2 * k)} {f(b + 10 * k)} Z" fill="#B85A32" stroke="{INK}" stroke-width="1.8"></path>'
             f'<ellipse cx="{f(mx + 7 * k)}" cy="{f(b - 20 * k)}" rx="{f(13 * k)}" ry="{f(3.5 * k)}" fill="#8FD0E2" stroke="{INK}" stroke-width="1.2"></ellipse>')
    o.append(f'<path d="M{f(mx + 50 * k)} {f(b + 14 * k)} L {f(mx + 130 * k)} {f(b + 14 * k)} L {f(mx + 136 * k)} {f(b - 8 * k)} L {f(mx + 56 * k)} {f(b - 8 * k)} Z" fill="#6A6A5A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(mx + 54 * k)} {f(b)} L {f(mx + 132 * k)} {f(b)}" stroke="#4A4A3A" stroke-width="2"></path>')
    o.append(plate_label(mx - 40 * k, h * 0.2, "FOOD AND COVERING", "#3A1E0E", 10, halo_="#F3E8C8"))
    return "".join(o)

def money_root(w, h):
    """The love of money is a root of all kinds of evil … and have pierced themselves through with many sorrows: a botanical
    plate on cream paper — a heap of coins and a burst money bag on the ground line, and under the ground the root going down
    from it and spreading, its branches tagged with the ASV's words (a temptation, a snare, foolish and hurtful lusts,
    destruction, perdition, many sorrows)."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{CREAM}"></rect>', f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="{PAPER_INK}" stroke-width="1.4"></rect>',
         title_bar_cream(w, "1 TIMOTHY 6:9–10 · A ROOT OF ALL KINDS OF EVIL")]
    gy = 40 + (h - 40) * 0.3
    o.append(f'<rect x="9" y="{f(gy)}" width="{f(w - 18)}" height="{f(h - gy - 9)}" fill="#E0D0B0"></rect><path d="M9 {f(gy)} L {f(w - 9)} {f(gy)}" stroke="{PAPER_INK}" stroke-width="2"></path>')
    cx = w * 0.5
    k = min(w / 700, h / 300)
    r = random.Random(7)
    for i in range(16):                                           # the heap of coins
        x = cx + r.uniform(-60, 60) * k; y = gy - 4 * k - r.uniform(0, 26) * k * (1 - abs(x - cx) / (70 * k))
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(9 * k)}" ry="{f(4 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></ellipse>')
    o.append(bag(cx + 80 * k, gy, k * 0.9))
    def root(x, y, ang, L, depth):
        if depth == 0 or L < 8 * k: return []
        x2 = x + L * math.cos(math.radians(ang)); y2 = y + L * math.sin(math.radians(ang))
        mx_, my_ = (x + x2) / 2 + r.uniform(-8, 8) * k, (y + y2) / 2 + r.uniform(-6, 6) * k
        out = [f'<path d="M{f(x)} {f(y)} Q {f(mx_)} {f(my_)} {f(x2)} {f(y2)}" fill="none" stroke="#3A2414" stroke-width="{f(max(1.2, depth * 1.8 * k))}" stroke-linecap="round"></path>']
        for d in (-26, 22):
            out += root(x2, y2, ang + d + r.uniform(-8, 8), L * 0.68, depth - 1)
        return out
    o += root(cx, gy, 90, (h - gy) * 0.34, 5)
    tags = [("A TEMPTATION", -0.32, 0.36), ("A SNARE", 0.3, 0.34), ("FOOLISH AND HURTFUL LUSTS", -0.3, 0.62), ("DESTRUCTION", 0.32, 0.6),
            ("PERDITION", -0.18, 0.86), ("MANY SORROWS", 0.22, 0.86)]
    for t, dx, dy in tags:
        x, y = cx + dx * w * 0.9, gy + (h - gy - 12) * dy
        o.append(f'<path d="M{f(cx + dx * w * 0.36)} {f(y - 4)} L {f(x - (len(t) * 3.5 + 6) * (1 if dx > 0 else -1))} {f(y - 4)}" stroke="{PAPER_INK}" stroke-width="1" stroke-dasharray="3 3"></path>')
        o.append(label(x, y, t, "#7A1A1A", 9.5))
    o.append(label(cx - 150 * k, gy - 10, "THE LOVE OF MONEY", PAPER_INK, 10))
    return "".join(o)

def rich_poor(p, w, h, seed):
    """Charge them that are rich … that they be not highminded, nor have their hope set on the uncertainty of riches … that
    they do good, that they be rich in good works, ready to distribute: two cells — a rich man's strongroom by lamplight,
    the chest open and full (THE UNCERTAINTY OF RICHES); and the same man at his gate in the morning giving bread into the
    hands of a poor man (RICH IN GOOD WORKS)."""
    rich = dict(cloth="#4A2A5A", head="#E8E2D6", cord="#C8981E", beard="#3A2A1A", mantle="#6A3A1A", belt="#C8981E")
    def vault(pp, cw, ch):
        b = ch * 0.9
        o = [room(cw, ch, b, wall="#3A3038", floor="#2A2228"), lamp_glow(cw * 0.5, b - ch * 0.3, ch * 0.7, f"{pp}vl", op=0.5)]
        k = ch / 260
        o.append(chest_open(cw * 0.5, b, k * 1.3) + bag(cw * 0.2, b, k) + bag(cw * 0.8, b, k * 0.9))
        return "".join(o)
    def gate(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - ch * 0.7)
        o = [_defs(pp), sky(cw, ch, "#8FD0E2", "#FFE6B0"), f'<rect x="{f(cw * 0.5)}" y="{f(ch * 0.12)}" width="{f(cw * 0.6)}" height="{f(b - ch * 0.12)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>',
             f'<rect x="{f(cw * 0.6)}" y="{f(ch * 0.3)}" width="{f(cw * 0.22)}" height="{f(b - ch * 0.3)}" fill="#3A2214" stroke="{INK}" stroke-width="2"></rect>',
             ground(cw, ch, b, "#C8B07A", dy=0)]
        loaf = '<ellipse cx="-74" cy="-150" rx="10" ry="6" fill="#D8A060" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
        o.append(robed(pp, cw * 0.66, b, s, rich["cloth"], head=rich["head"], cord=rich["cord"], beard=rich["beard"], mantle=rich["mantle"], belt=rich["belt"],
                       up=[(-22, -158), (-46, -150), (-70, -150)], extra=loaf))
        o.append(robed(pp, cw * 0.3, b, s * 0.94, "#8A7A5A", hair="#3A2A1A", beard="#3A2A1A", flip=True, up=[(-22, -158), (-44, -146), (-62, -146)]))
        return "".join(o)
    o = [cells(p, w, h, [vault, gate])]
    o.append(plate_label(w * 0.25, h * 0.08, "THE UNCERTAINTY OF RICHES", "#FFD23F", 9.5) + plate_label(w * 0.75, h * 0.08, "RICH IN GOOD WORKS", "#12113A", 9.5, halo_="#FFF4C2"))
    return "".join(o)

def guard_deposit(p, w, h, seed):
    """O Timothy, guard that which is committed unto thee: Timothy standing at night in his room at Ephesus, the sealed roll
    held close in his hand, the lamp on the table and the window on the city."""
    b = h * 0.95
    k = fig_k(w, h, 0.4)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - 80 * k, max(w, h) * 0.55, f"{p}gd", op=0.5)]
    o.append(_eph_window(w * 0.66, b - 205 * k, min(w * 0.2, 120 * k), min(h * 0.38, 92 * k), True, seed))
    o.append(low_table(w * 0.24, b, 60 * k, k) + clay_lamp(w * 0.24 + 30 * k, b - 31 * k, k * 0.6))
    o.append(timothy_fig_(p, w * 0.42, b, k, up=[(-22, -158), (-34, -128), (-20, -116)], extra=sealed_scroll(-16, -118, 0.42, rot=70)))
    return "".join(o)
