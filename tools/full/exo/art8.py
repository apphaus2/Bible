"""Blueprints for Exodus chapter 8 (Exodus 25–27): the pattern of the tabernacle as technical drawings — cyan linework on
a navy grid, gold where the text says gold, dimension lines in cubits. Each function draws into a w x h panel.

Shared pieces: bp(w, h) (the grid), dim() (a dimension line with its label), box() (an oblique-projection box), tag()
(a small callout label). Cubit counts come from the verses on the same panel."""
import sys, pathlib, random, math, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus5 as V, samuel1 as S1
from genesis.art3 import label, grid_bg
def f(v): return f"{v:.1f}"

INK, CY, GOLD, SILVER, BRASS = "#0B1A2E", "#8FD0E2", "#E8B830", "#C8C8D0", "#B87333"
BLUE, PURPLE, SCARLET, LINEN = "#1F5FAD", "#6A3A9A", "#C8202A", "#F3EFE6"

_W = [702]                                   # the width of the panel being drawn (set by bp) so callouts stay inside it
def bp(w, h, step=24):
    _W[0] = w
    return grid_bg(w, h, color="#1E3A5A", step=step, bg=INK)

def dim(x1, y1, x2, y2, text, off=0, size=9, color=CY):
    """A dimension line between two points with arrowheads and a centred label."""
    a = math.atan2(y2 - y1, x2 - x1); nx, ny = -math.sin(a) * off, math.cos(a) * off
    x1, y1, x2, y2 = x1 + nx, y1 + ny, x2 + nx, y2 + ny
    ah = lambda x, y, d: f'<path d="M{f(x)} {f(y)} l {f(8 * math.cos(a + d * 2.7))} {f(8 * math.sin(a + d * 2.7))} M{f(x)} {f(y)} l {f(8 * math.cos(a - d * 2.7))} {f(8 * math.sin(a - d * 2.7))}" stroke="{color}" stroke-width="1.4"></path>'
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    rot = math.degrees(a); rot = rot - 180 if rot > 90 else (rot + 180 if rot < -90 else rot)
    return (f'<path d="M{f(x1)} {f(y1)} L {f(x2)} {f(y2)}" stroke="{color}" stroke-width="1.2" stroke-dasharray="5 3"></path>' + ah(x1, y1, -1) + ah(x2, y2, 1)
            + f'<g transform="translate({f(mx)} {f(my - 5)}) rotate({f(rot)})"><rect x="{f(-len(text) * size * 0.34)}" y="{f(-size)}" width="{f(len(text) * size * 0.68)}" height="{f(size + 4)}" fill="{INK}"></rect>'
            + label(0, 0, text, color, size) + '</g>')

def box(x, y, w, d, h, fill=GOLD, line="#0D0D0F", k=0.5, top=None, side=None):
    """An oblique box: front face w x h with its bottom-left at (x, y), depth d drawn up and to the right."""
    dx, dy = d * k, -d * k * 0.7
    top = top or fill; side = side or fill
    return (f'<path d="M{f(x)} {f(y - h)} L {f(x + dx)} {f(y - h + dy)} L {f(x + w + dx)} {f(y - h + dy)} L {f(x + w)} {f(y - h)} Z" fill="{top}" stroke="{line}" stroke-width="2"></path>'
            f'<path d="M{f(x + w)} {f(y)} L {f(x + w + dx)} {f(y + dy)} L {f(x + w + dx)} {f(y - h + dy)} L {f(x + w)} {f(y - h)} Z" fill="{side}" stroke="{line}" stroke-width="2" opacity="0.92"></path>'
            f'<rect x="{f(x)}" y="{f(y - h)}" width="{f(w)}" height="{f(h)}" fill="{fill}" stroke="{line}" stroke-width="2"></rect>')

def tag(x, y, text, tx, ty, color=CY, size=9):
    """A callout: a leader line from (x, y) to a label at (tx, ty)."""
    est = len(text) * size * 0.66; right = tx >= x
    if right and tx + 4 + est > _W[0] - 6: tx = _W[0] - 10 - est
    if not right and tx - 4 - est < 6: tx = 10 + est
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="{color}"></circle><path d="M{f(x)} {f(y)} L {f(tx)} {f(ty)}" stroke="{color}" stroke-width="1.2"></path>'
            + label(tx + (4 if right else -4), ty + 3, text, color, size, "start" if right else "end"))

def title_bar(w, text, y=18):
    return label(14, y, text, "#FFD23F", 11, "start", ls=0.2)

# ---- 25:1–9 ----------------------------------------------------------------------------------------------------
def offering(w, h):
    """The offering: swatches of every material named in 25:3–7, in a labelled grid."""
    o = [bp(w, h), title_bar(w, "THE OFFERING · MATERIALS")]
    items = [("GOLD", GOLD, "ingot"), ("SILVER", SILVER, "ingot"), ("BRASS", BRASS, "ingot"), ("BLUE", BLUE, "skein"), ("PURPLE", PURPLE, "skein"),
             ("SCARLET", SCARLET, "skein"), ("FINE LINEN", LINEN, "skein"), ("GOATS' HAIR", "#3A3430", "skein"), ("RAMS' SKINS RED", "#A8322A", "hide"),
             ("SEALSKINS", "#5A6A7A", "hide"), ("ACACIA WOOD", "#B5793A", "log"), ("OIL", "#C8B040", "jar"), ("SPICES", "#8A6A3A", "jar"), ("ONYX STONES", "#2A2A3A", "stone")]
    cols = 7; cw = (w - 20) / cols; ch = (h * 0.6 - 34) / 2
    for i, (nm, c, kind) in enumerate(items):
        x = 10 + (i % cols) * cw + cw / 2; y = 34 + (i // cols) * ch + ch * 0.48
        s = min(cw, ch) / 90
        if kind == "ingot": g = f'<path d="M{f(x - 26 * s)} {f(y + 10 * s)} L {f(x - 18 * s)} {f(y - 10 * s)} L {f(x + 18 * s)} {f(y - 10 * s)} L {f(x + 26 * s)} {f(y + 10 * s)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>'
        elif kind == "skein": g = "".join(f'<ellipse cx="{f(x)}" cy="{f(y + d * s)}" rx="{f(24 * s)}" ry="{f(8 * s)}" fill="none" stroke="{c}" stroke-width="{f(5 * s)}"></ellipse>' for d in (-8, 0, 8))
        elif kind == "hide": g = f'<path d="M{f(x - 26 * s)} {f(y - 16 * s)} C {f(x - 10 * s)} {f(y - 24 * s)} {f(x + 10 * s)} {f(y - 24 * s)} {f(x + 26 * s)} {f(y - 16 * s)} L {f(x + 22 * s)} {f(y + 18 * s)} C {f(x)} {f(y + 12 * s)} {f(x)} {f(y + 12 * s)} {f(x - 22 * s)} {f(y + 18 * s)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>'
        elif kind == "log": g = f'<rect x="{f(x - 28 * s)}" y="{f(y - 8 * s)}" width="{f(50 * s)}" height="{f(16 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></rect><ellipse cx="{f(x + 22 * s)}" cy="{f(y)}" rx="{f(6 * s)}" ry="{f(8 * s)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
        elif kind == "jar": g = f'<path d="M{f(x - 12 * s)} {f(y - 18 * s)} L {f(x + 12 * s)} {f(y - 18 * s)} C {f(x + 24 * s)} {f(y)} {f(x + 18 * s)} {f(y + 18 * s)} {f(x)} {f(y + 18 * s)} C {f(x - 18 * s)} {f(y + 18 * s)} {f(x - 24 * s)} {f(y)} {f(x - 12 * s)} {f(y - 18 * s)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>'
        else: g = "".join(f'<path d="M{f(x + dx * s)} {f(y - 10 * s)} l {f(10 * s)} {f(8 * s)} l {f(-4 * s)} {f(12 * s)} l {f(-12 * s)} 0 l {f(-4 * s)} {f(-12 * s)} Z" fill="{c}" stroke="{CY}" stroke-width="1.6"></path>' for dx in (-14, 8))
        o.append(f'<rect x="{f(x - cw / 2 + 4)}" y="{f(y - ch * 0.42)}" width="{f(cw - 8)}" height="{f(ch * 0.84)}" fill="none" stroke="#2C9DB8" stroke-width="1"></rect>' + g
                 + label(x, y + ch * 0.36, nm, CY, 7.5, ls=0.04))
    return "".join(o)

def sanctuary(w, h):
    """Let them make me a sanctuary: the tabernacle in its court, as an elevation with a scale bar."""
    return bp(w, h) + title_bar(w, "THE SANCTUARY · ELEVATION") + V.tabernacle(w * 0.5, h * 0.82, w * 0.82, uid="bp1") + dim(w * 0.09, h * 0.92, w * 0.91, h * 0.92, "100 CUBITS")

# ---- 25:10–22 -----------------------------------------------------------------------------------------------
def ark(w, h, staves=True, lid=False, testimony=False):
    """The ark of acacia wood overlaid with gold: 2½ x 1½ x 1½ cubits, a crown round about, four rings, two staves."""
    u = min(w / 7.5, h / 4.4)                          # pixels per cubit
    L, B, H_ = 2.5 * u, 1.5 * u, 1.5 * u
    x, y = w * 0.62 - L * 0.62, h * 0.84
    o = [bp(w, h), title_bar(w, "THE ARK OF THE TESTIMONY")]
    o.append(box(x, y, L, B, H_, fill=GOLD, top="#FFD23F", side="#C8981E"))
    o.append(f'<path d="M{f(x)} {f(y - H_ + 8)} L {f(x + L)} {f(y - H_ + 8)}" stroke="#FFF4C2" stroke-width="3"></path>')
    if staves:
        sy = y - H_ * 0.25
        o.append(f'<path d="M{f(x - u * 0.9)} {f(sy)} L {f(x + L + u * 0.9)} {f(sy)}" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path><path d="M{f(x - u * 0.9)} {f(sy)} L {f(x + L + u * 0.9)} {f(sy)}" stroke="{GOLD}" stroke-width="6" stroke-linecap="round"></path>')
        o += [f'<circle cx="{f(x + d)}" cy="{f(sy)}" r="7" fill="none" stroke="#0D0D0F" stroke-width="4"></circle><circle cx="{f(x + d)}" cy="{f(sy)}" r="7" fill="none" stroke="#FFD23F" stroke-width="2.4"></circle>' for d in (u * 0.3, L - u * 0.3)]
        o.append(tag(x + L + u * 0.9, sy, "STAVES · ACACIA, GOLD", x + L + u * 0.9, sy - u * 0.9))
        o.append(tag(x + u * 0.3, sy, "RINGS OF GOLD", x - u * 0.6, sy + u * 0.4))
    if testimony:
        o.append(V.tables(x + L * 0.5, y - H_ - u * 0.2, u / 120, uid="bpt", glow=False)
                 + f'<path d="M{f(x + L * 0.5)} {f(y - H_ - u * 0.1)} L {f(x + L * 0.5)} {f(y - H_ * 0.6)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="4 4"></path>')
    o.append(tag(x + L * 0.5, y - H_ - 2, "A CROWN OF GOLD ROUND ABOUT", x + L * 0.5, y - H_ - u * 0.8))
    o.append(dim(x, y + 12, x + L, y + 12, "2½ CUBITS") + dim(x - 14, y, x - 14, y - H_, "1½") + dim(x + L + 10, y + 6, x + L + 10 + B * 0.5, y + 6 - B * 0.35, "1½"))
    return "".join(o)

def cherub(x, y, s=1.0, flip=False):
    """A cherub of beaten gold kneeling at the end of the mercy-seat, wings spread on high toward the other, face toward the seat."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            # the far wing, behind the body
            '<path d="M-8 -58 C -40 -86 -40 -120 -14 -128 C 12 -134 52 -118 86 -92 C 56 -96 30 -90 10 -66 Z" fill="#C8981E" stroke="#0D0D0F" stroke-width="2"></path>'
            # kneeling body and bowed head, facing right
            '<path d="M-22 0 L 26 0 C 30 -6 28 -14 20 -16 C 8 -20 6 -34 8 -48 C 10 -58 4 -64 -4 -64 C -14 -62 -20 -52 -22 -40 C -26 -26 -28 -10 -22 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
            '<circle cx="8" cy="-74" r="11" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle><path d="M14 -76 l 5 3" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M6 -40 L 24 -30" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path><path d="M6 -40 L 24 -30" stroke="#E8B830" stroke-width="3.6" stroke-linecap="round"></path>'
            # the near wing, spread on high and forward over the mercy-seat
            '<path d="M-4 -60 C -28 -84 -26 -112 -4 -118 C 20 -124 58 -108 92 -80 C 62 -84 36 -80 14 -58 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M2 -104 C 24 -104 46 -98 66 -88 M-2 -90 C 18 -90 36 -86 52 -78 M2 -76 C 16 -76 28 -74 38 -70" stroke="#C8981E" stroke-width="1.6" fill="none"></path></g>')

def mercy_seat(w, h, grid=True, cx=0.56, scale=1.0):
    """The mercy-seat of pure gold, 2½ x 1½ cubits, with a cherub at each end, wings covering it, faces one to another."""
    u = min(w / 6.4, h / 4.0) * scale
    L, B, H_ = 2.5 * u, 1.5 * u, 1.5 * u
    x, y = w * cx - L * 0.62, h * 0.88
    o = [bp(w, h) if grid else "", title_bar(w, "THE MERCY-SEAT · TWO CHERUBIM OF GOLD") if grid else ""]
    o.append(V.rays(x + L * 0.62, y - H_ - u * 0.9, 24, 10, u * 2.6, color="#FFF4C2", op=0.25))
    o.append(box(x, y, L, B, H_, fill=GOLD, top="#FFD23F", side="#C8981E"))
    ty = y - H_ - B * 0.18; cs = u / 70
    o.append(cherub(x + u * 0.35 + B * 0.12, ty, cs) + cherub(x + L - u * 0.1 + B * 0.12, ty, cs, flip=True))
    if grid:
        o.append(dim(x, y + 12, x + L, y + 12, "2½ CUBITS") + dim(x + L + 10, y + 6, x + L + 10 + B * 0.5, y + 6 - B * 0.35, "1½"))
        o.append(tag(x + L * 0.62, y - H_ - u * 0.7, "FROM BETWEEN THE TWO CHERUBIM", x + L + u * 0.3, y - H_ - u * 1.4, color="#FFD23F"))
    return "".join(o)

# ---- 25:23–30 ----------------------------------------------------------------------------------------------
def table(w, h, bread=True, vessels=True):
    """The table of acacia overlaid with gold: 2 x 1 x 1½ cubits, a border of a handbreadth, rings at the feet, staves; the showbread."""
    u = min(w / 5.6, h / 4.4)
    L, B, H_ = 2 * u, 1 * u, 1.5 * u
    x, y = w * 0.58 - L * 0.6, h * 0.86; dx, dy = B * 0.5, -B * 0.35
    o = [bp(w, h), title_bar(w, "THE TABLE OF SHOWBREAD")]
    for lx, ly in ((x + dx + 4, y + dy), (x + L + dx - 10, y + dy), (x + 4, y), (x + L - 10, y)):   # the four feet, back pair first
        o.append(f'<rect x="{f(lx)}" y="{f(ly - H_)}" width="6" height="{f(H_)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(box(x, y - H_ + u * 0.22, L, B, u * 0.22, fill=GOLD, top="#FFD23F", side="#C8981E"))
    o.append(f'<path d="M{f(x)} {f(y - H_ + u * 0.06)} L {f(x + L)} {f(y - H_ + u * 0.06)}" stroke="#FFF4C2" stroke-width="2.4"></path>')
    sy = y - H_ * 0.45
    o.append(f'<path d="M{f(x - u * 0.6)} {f(sy)} L {f(x + L + u * 0.6)} {f(sy)}" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M{f(x - u * 0.6)} {f(sy)} L {f(x + L + u * 0.6)} {f(sy)}" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"></path>')
    if bread:
        for row in range(2):
            for i in range(6):
                bx = x + u * 0.18 + i * (L - u * 0.3) / 6 + row * dx * 0.5; by = y - H_ + u * 0.0 - row * 8 - 4
                o.append(f'<ellipse cx="{f(bx + 10)}" cy="{f(by)}" rx="{f(u * 0.13)}" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
        o.append(tag(x + L * 0.3, y - H_ - 6, "SHOWBREAD · BEFORE ME ALWAY", x + L * 0.1, y - H_ - u * 0.9, color="#FFD23F"))
    if vessels:
        vx = w * 0.84
        o.append(f'<ellipse cx="{f(vx)}" cy="{f(h * 0.4)}" rx="18" ry="6" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 f'<path d="M{f(vx - 10)} {f(h * 0.56)} L {f(vx + 10)} {f(h * 0.56)} L {f(vx + 6)} {f(h * 0.66)} L {f(vx - 6)} {f(h * 0.66)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 + label(vx, h * 0.34, "DISHES · SPOONS", CY, 8) + label(vx, h * 0.72, "FLAGONS · BOWLS", CY, 8))
    o.append(dim(x, y + 12, x + L, y + 12, "2 CUBITS") + dim(x - 16, y, x - 16, y - H_, "1½") + dim(x + L + 12, y - H_ + 6, x + L + 12 + dx, y - H_ + 6 + dy, "1"))
    return "".join(o)

# ---- 25:31–40 ----------------------------------------------------------------------------------------------
def lampstand(w, h, lit=True):
    """The candlestick of beaten gold: base, shaft, six branches, cups like almond-blossoms, knops and flowers, seven lamps."""
    s = min(w / 220, h / 190)
    x, y = w * 0.5, h * 0.92
    o = [bp(w, h), title_bar(w, "THE CANDLESTICK" if w < 400 else "THE CANDLESTICK · ONE BEATEN WORK OF PURE GOLD"), re.sub(r'<path d="M[^"]*" fill="none" stroke="#8A8478"[^>]*></path>', "", S1.lamp(x, y, s, lit=lit))]   # unlit: no smoke either
    o.append(tag(x - 66 * s, y - 128 * s, "CUPS LIKE ALMOND-BLOSSOMS", x - 100 * s, y - 160 * s))
    o.append(tag(x + 44 * s, y - 120 * s, "A KNOP AND A FLOWER", x + 90 * s, y - 150 * s))
    o.append(tag(x, y - 40 * s, "THE SHAFT", x + 60 * s, y - 50 * s))
    o.append(tag(x, y - 6 * s, "THE BASE", x - 60 * s, y - 14 * s))
    o.append(label(w - 14, h - 10, "7 LAMPS · 6 BRANCHES · 1 TALENT", CY, 9, "end"))
    return "".join(o)

def snuffers(w, h):
    """The snuffers and snuffdishes of pure gold, and the talent of gold it is made of."""
    o = [bp(w, h), title_bar(w, "VESSELS · A TALENT OF PURE GOLD")]
    cx = w * 0.3
    o.append(f'<path d="M{f(cx - 40)} {f(h * 0.5)} L {f(cx + 30)} {f(h * 0.6)} M{f(cx - 40)} {f(h * 0.6)} L {f(cx + 30)} {f(h * 0.5)}" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"></path>'
             f'<ellipse cx="{f(cx + 90)}" cy="{f(h * 0.6)}" rx="34" ry="10" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    tx = w * 0.76
    o.append(f'<path d="M{f(tx - 40)} {f(h * 0.7)} C {f(tx - 50)} {f(h * 0.4)} {f(tx + 50)} {f(h * 0.4)} {f(tx + 40)} {f(h * 0.7)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + label(tx, h * 0.8, "1 TALENT", "#FFD23F", 10))
    return "".join(o)

# ---- 26:1–14 -----------------------------------------------------------------------------------------------
def curtains(w, h, n=10, length="28", color=None, couple=(5, 5), clasps="GOLD", cherubim=True, loops=True, area=(0.18, 0.78)):
    """Curtains laid side by side in plan: n strips of length x 4 cubits, coupled in two sets, fifty loops and clasps between."""
    o = [bp(w, h)]
    x0, x1 = w * 0.08, w * 0.92; cw = (x1 - x0) / n; top, bot = h * area[0], h * area[1]
    cols = color or [BLUE, PURPLE, SCARLET, LINEN]
    for i in range(n):
        x = x0 + i * cw; c = cols[i % len(cols)] if isinstance(cols, list) else cols
        o.append(f'<rect x="{f(x + 1)}" y="{f(top)}" width="{f(cw - 2)}" height="{f(bot - top)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        if cherubim:
            o.append("".join(f'<path d="M{f(x + cw / 2)} {f(yy)} l -6 6 l 6 6 l 6 -6 Z" fill="none" stroke="#FFD23F" stroke-width="1.2" opacity="0.8"></path>' for yy in [top + (bot - top) * k / 5 for k in range(1, 5)]))
    jx = x0 + couple[0] * cw
    if loops:
        o.append("".join(f'<circle cx="{f(jx)}" cy="{f(top + (bot - top) * k / 12)}" r="3.4" fill="{"#FFD23F" if clasps == "GOLD" else "#B87333"}" stroke="#0D0D0F" stroke-width="1"></circle>' for k in range(1, 12)))
        o.append(tag(jx, top + (bot - top) * 0.5, f"50 LOOPS · 50 CLASPS OF {clasps}", jx + 30, top - 10))
    o.append(dim(x0, bot + 12, x0 + cw, bot + 12, "4", size=8) + dim(x1 + 12, top, x1 + 12, bot, f"{length} CUBITS"))
    o.append(label(x0 + couple[0] * cw / 2, bot + 30, f"{couple[0]} COUPLED", CY, 9) + label(jx + couple[1] * cw / 2, bot + 30, f"{couple[1]} COUPLED", CY, 9))
    return "".join(o)

def coverings(w, h):
    """The tent over the tabernacle in section: linen curtains, goats' hair, rams' skins dyed red, sealskins above."""
    o = [bp(w, h), title_bar(w, "THE COVERINGS · SECTION")]
    cx, base = w * 0.5, h * 0.9; bw, bh = w * 0.3, h * 0.42
    layers = [("SEALSKINS", "#5A6A7A", 30), ("RAMS' SKINS DYED RED", "#A8322A", 20), ("GOATS' HAIR · 11 CURTAINS", "#3A3430", 10), ("FINE TWINED LINEN · 10 CURTAINS", BLUE, 0)]
    for i, (nm, c, off) in enumerate(layers):
        o.append(f'<path d="M{f(cx - bw / 2 - off - 10)} {f(base - 10 + off * 0.3)} L {f(cx - bw / 2 - off)} {f(base - bh - off)} L {f(cx + bw / 2 + off)} {f(base - bh - off)} L {f(cx + bw / 2 + off + 10)} {f(base - 10 + off * 0.3)}" fill="none" stroke="{c}" stroke-width="8"></path>')
        o.append(tag(cx + bw / 2 + off + 6, base - bh * 0.4 - off * 0.4, nm, w * 0.78, h * (0.2 + i * 0.14), color=CY))
    o.append(f'<rect x="{f(cx - bw / 2)}" y="{f(base - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{GOLD}" opacity="0.35" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def overhang(w, h):
    """The half curtain over the back, and a cubit over each side: the tent of goats' hair in plan, folds marked."""
    o = [bp(w, h), title_bar(w, "THE TENT · OVERHANG")]
    x0, x1, top, bot = w * 0.16, w * 0.84, h * 0.22, h * 0.82
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(bot - top)}" fill="#3A3430" stroke="{CY}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(x0 + 30)}" y="{f(top + 20)}" width="{f(x1 - x0 - 60)}" height="{f(bot - top - 40)}" fill="none" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="6 4"></rect>')
    o.append(dim(x1 - 30, bot + 10, x1, bot + 10, "½", size=8) + label(x1 - 15, bot + 30, "OVER THE BACK", CY, 8))
    o.append(dim(x0 - 12, top, x0 - 12, top + 20, "1", size=8) + dim(x0 - 12, bot - 20, x0 - 12, bot, "1", size=8) + label(x0 - 18, (top + bot) / 2, "SIDES", CY, 8, "end"))
    o.append(label((x0 + x1) / 2, (top + bot) / 2, "THE TABERNACLE", "#FFD23F", 10))
    return "".join(o)

# ---- 26:15–30 ----------------------------------------------------------------------------------------------
def board(w, h):
    """A board of acacia standing up: 10 cubits by 1½, two tenons below, each in a socket of silver."""
    u = h * 0.07
    x, y = w * 0.24, h * 0.86; bw, bh = 1.5 * u, 10 * u * 0.9
    o = [bp(w, h), title_bar(w, "A BOARD · TENONS · SOCKETS")]
    o.append(f'<rect x="{f(x)}" y="{f(y - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>')
    for k in (0.25, 0.75):
        tx = x + bw * k
        o.append(f'<rect x="{f(tx - 5)}" y="{f(y)}" width="10" height="16" fill="#B5793A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<path d="M{f(tx - 16)} {f(y + 30)} L {f(tx - 12)} {f(y + 6)} L {f(tx + 12)} {f(y + 6)} L {f(tx + 16)} {f(y + 30)} Z" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(dim(x - 14, y, x - 14, y - bh, "10 CUBITS") + dim(x, y - bh - 12, x + bw, y - bh - 12, "1½", size=8))
    o.append(tag(x + bw * 0.25, y + 8, "2 TENONS", x + bw + 30, y - 30) + tag(x + bw * 0.75, y + 22, "2 SOCKETS OF SILVER", x + bw + 30, y + 4))
    return "".join(o)

def frame_plan(w, h, bars=False, veil=False, furniture=False, screen=False, area=(0.24, 0.76)):
    """The tabernacle frame in plan: 20 boards south, 20 north, 6 at the hinder part westward and 2 at the corners;
    bars, the veil on four pillars, the furniture and the screen with five pillars as the verses add them."""
    o = [bp(w, h), title_bar(w, "THE TABERNACLE · PLAN")]
    x0, x1 = w * 0.1, w * 0.86; yN, yS = h * area[0], h * area[1]; bw = (x1 - x0) / 20
    for i in range(20):
        o.append(f'<rect x="{f(x0 + i * bw + 1)}" y="{f(yN - 6)}" width="{f(bw - 2)}" height="10" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1"></rect>'
                 f'<rect x="{f(x0 + i * bw + 1)}" y="{f(yS - 4)}" width="{f(bw - 2)}" height="10" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1"></rect>')
    wh = (yS - yN) / 8
    for i in range(8):
        o.append(f'<rect x="{f(x0 - 10)}" y="{f(yN + i * wh + 1)}" width="10" height="{f(wh - 2)}" fill="{"#FFD23F" if i in (0, 7) else GOLD}" stroke="#0D0D0F" stroke-width="1"></rect>')
    o += [label((x0 + x1) / 2, yN - 14, "NORTH · 20 BOARDS · 40 SOCKETS", CY, 9), label((x0 + x1) / 2, yS + 26, "SOUTH · 20 BOARDS · 40 SOCKETS", CY, 9),
          f'<g transform="translate({f(x0 - 24)} {f((yN + yS) / 2)}) rotate(-90)">' + label(0, 0, "WEST · 6 + 2 CORNER BOARDS", CY, 9) + '</g>',
          label(x1 + 30, (yN + yS) / 2 + 4, "EAST", CY, 9)]
    if bars:
        for k, yy in enumerate((yN - 12, yN + 10)):
            o.append(f'<path d="M{f(x0)} {f(yy)} L {f(x1)} {f(yy)}" stroke="#FFD23F" stroke-width="{3 if k else 2}" stroke-dasharray="{"" if k else "40 6"}"></path>')
        o.append(f'<path d="M{f(x0)} {f(yS - 10)} L {f(x1)} {f(yS - 10)}" stroke="#FFD23F" stroke-width="3"></path>' + label(x0 + 40, yS - 16, "THE MIDDLE BAR · END TO END", "#FFD23F", 8, "start"))
    if veil:
        vx = x0 + (x1 - x0) / 3
        o.append(f'<path d="M{f(vx)} {f(yN + 6)} L {f(vx)} {f(yS - 6)}" stroke="{SCARLET}" stroke-width="5"></path>'
                 + "".join(f'<circle cx="{f(vx)}" cy="{f(yN + (yS - yN) * k / 5)}" r="5" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></circle>' for k in range(1, 5))
                 + label((x0 + vx) / 2, yN + 26, "THE MOST HOLY", "#FFD23F", 9) + label((vx + x1) / 2, yN + 26, "THE HOLY PLACE", "#FFD23F", 9)
                 + label(vx, yS + 12, "THE VEIL · 4 PILLARS", SCARLET, 8))
    if furniture:
        cx = (x0 + vx) / 2
        o.append(f'<rect x="{f(cx - 22)}" y="{f((yN + yS) / 2 - 12)}" width="44" height="24" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>' + label(cx, (yN + yS) / 2 + 30, "ARK · MERCY-SEAT", CY, 8))
        hx = (vx + x1) / 2
        o.append(f'<rect x="{f(hx - 18)}" y="{f(yN + 40)}" width="36" height="18" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>' + label(hx, yN + 70, "TABLE · NORTH", CY, 8))
        o.append(f'<circle cx="{f(hx)}" cy="{f(yS - 44)}" r="10" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></circle>' + label(hx, yS - 20, "CANDLESTICK · SOUTH", CY, 8))
    if screen:
        o.append(f'<path d="M{f(x1 + 4)} {f(yN)} L {f(x1 + 4)} {f(yS)}" stroke="{BLUE}" stroke-width="5"></path>'
                 + "".join(f'<circle cx="{f(x1 + 4)}" cy="{f(yN + (yS - yN) * k / 4)}" r="5" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></circle>' for k in range(5)))
    return "".join(o)

def veil_elev(w, h):
    """The veil of blue, purple, scarlet and fine twined linen with cherubim, hung on four pillars upon four sockets of silver."""
    o = [bp(w, h), title_bar(w, "THE VEIL · ELEVATION")]
    x0, x1, top, bot = w * 0.12, w * 0.88, h * 0.18, h * 0.8; pw = 12
    bands = [BLUE, PURPLE, SCARLET, LINEN]
    for i in range(8):
        o.append(f'<rect x="{f(x0 + (x1 - x0) * i / 8)}" y="{f(top)}" width="{f((x1 - x0) / 8)}" height="{f(bot - top)}" fill="{bands[i % 4]}" stroke="#0D0D0F" stroke-width="1"></rect>')
    for k in range(1, 4):
        o.append(f'<g transform="translate({f(x0 + (x1 - x0) * k / 4)} {f((top + bot) / 2 + 20)}) scale({f(h / 500)})">{cherub(0, 0, 1.0)}</g>')
    for k in range(4):
        px = x0 + (x1 - x0) * k / 3 - pw / 2
        o.append(f'<rect x="{f(px)}" y="{f(top - 10)}" width="{pw}" height="{f(bot - top + 10)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<path d="M{f(px - 6)} {f(bot + 14)} L {f(px - 2)} {f(bot)} L {f(px + pw + 2)} {f(bot)} L {f(px + pw + 6)} {f(bot + 14)} Z" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def screen_elev(w, h, n=5, sockets="BRASS", label_="THE SCREEN FOR THE DOOR OF THE TENT"):
    """The screen of blue, purple, scarlet and fine twined linen, the work of the embroiderer, on n pillars."""
    o = [bp(w, h), title_bar(w, label_)]
    x0, x1, top, bot = w * 0.1, w * 0.9, h * 0.22, h * 0.8; pw = 10
    for i, c in enumerate([BLUE, PURPLE, SCARLET, LINEN] * 3):
        o.append(f'<rect x="{f(x0)}" y="{f(top + (bot - top) * i / 12)}" width="{f(x1 - x0)}" height="{f((bot - top) / 12 + 0.5)}" fill="{c}"></rect>')
    for k in range(n):
        px = x0 + (x1 - x0) * k / (n - 1) - pw / 2
        o.append(f'<rect x="{f(px)}" y="{f(top - 8)}" width="{pw}" height="{f(bot - top + 8)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 f'<path d="M{f(px - 6)} {f(bot + 12)} L {f(px - 2)} {f(bot)} L {f(px + pw + 2)} {f(bot)} L {f(px + pw + 6)} {f(bot + 12)} Z" fill="{BRASS if sockets == "BRASS" else SILVER}" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(label(w / 2, h - 8, f"{n} PILLARS · SOCKETS OF {sockets}", CY, 9))
    return "".join(o)

# ---- 27:1–8 ------------------------------------------------------------------------------------------------
def altar(w, h, grating=True, staves=True, vessels=False):
    """The altar of acacia overlaid with brass: five cubits long, five broad, foursquare, three high; horns on the corners,
    a grating of network halfway up, rings and staves; hollow with planks."""
    u = min(w / 15.0, h / 8.4)
    L, B, H_ = 5 * u, 5 * u, 3 * u
    x, y = w * 0.56 - L * 0.64, h * 0.88; dx, dy = B * 0.5, -B * 0.35
    o = [bp(w, h), title_bar(w, "THE ALTAR OF BURNT-OFFERING · BRASS")]
    o.append(box(x, y, L, B, H_, fill=BRASS, top="#D8935A", side="#8A5222"))
    for hx, hy in ((x, y - H_), (x + L, y - H_), (x + dx, y - H_ + dy), (x + L + dx, y - H_ + dy)):
        o.append(f'<path d="M{f(hx - 7)} {f(hy)} C {f(hx - 7)} {f(hy - 14)} {f(hx + 2)} {f(hy - 22)} {f(hx + 8)} {f(hy - 24)} C {f(hx + 4)} {f(hy - 14)} {f(hx + 7)} {f(hy - 6)} {f(hx + 7)} {f(hy)} Z" fill="#D8935A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    if grating:
        gy = y - H_ * 0.5
        o.append(f'<rect x="{f(x + 4)}" y="{f(gy)}" width="{f(L - 8)}" height="{f(H_ * 0.46)}" fill="url(#bpnet)" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 '<defs><pattern id="bpnet" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 0 L 10 10 M10 0 L 0 10" stroke="#5A2A10" stroke-width="1.4"></path></pattern></defs>')
        o.append(tag(x + L * 0.5, gy + H_ * 0.2, "A GRATING OF NETWORK OF BRASS", x + L + u * 0.6, gy + H_ * 0.5))
    if staves:
        sy = y - H_ * 0.52
        o.append(f'<path d="M{f(x - u * 1.0)} {f(sy)} L {f(x + L + u * 1.0)} {f(sy)}" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M{f(x - u * 1.0)} {f(sy)} L {f(x + L + u * 1.0)} {f(sy)}" stroke="{BRASS}" stroke-width="5" stroke-linecap="round"></path>')
    o.append(tag(x + L, y - H_ - 18, "THE HORNS · ONE PIECE WITH IT", x + L + u * 0.6, y - H_ - u * 0.8))
    if vessels:
        vx = w * 0.12
        o.append("".join(f'<g transform="translate({f(vx)} {f(h * (0.3 + i * 0.13))})"><path d="M-14 0 L 14 0 L 10 10 L -10 10 Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.4"></path></g>' for i in range(5))
                 + label(vx, h * 0.24, "POTS · SHOVELS · BASINS", CY, 7.5) + label(vx, h * 0.96, "FLESH-HOOKS · FIREPANS", CY, 7.5))
    o.append(dim(x, y + 12, x + L, y + 12, "5 CUBITS") + dim(x - 14, y, x - 14, y - H_, "3") + dim(x + L + 10, y + 6, x + L + 10 + dx, y + 6 + dy, "5"))
    return "".join(o)

# ---- 27:9–21 -----------------------------------------------------------------------------------------------
def court(w, h, show=("S", "N", "W", "E")):
    """The court of the tabernacle in plan: 100 x 50 cubits of fine twined linen; pillars 20, 20, 10; on the east two
    hangings of fifteen cubits with three pillars each and the gate's screen of twenty cubits with four."""
    o = [bp(w, h), title_bar(w, "THE COURT · PLAN · 100 x 50 CUBITS")]
    x0, x1, yN, yS = w * 0.08, w * 0.9, h * 0.22, h * 0.78
    o.append(f'<rect x="{f(x0)}" y="{f(yN)}" width="{f(x1 - x0)}" height="{f(yS - yN)}" fill="#F3EFE6" fill-opacity="0.06" stroke="#F3EFE6" stroke-width="3"></rect>')
    def posts(xa, ya, xb, yb, n, c=BRASS):
        return "".join(f'<circle cx="{f(xa + (xb - xa) * k / n)}" cy="{f(ya + (yb - ya) * k / n)}" r="3.6" fill="{c}" stroke="#0D0D0F" stroke-width="1"></circle>' for k in range(n + 1))
    if "S" in show: o.append(posts(x0, yS, x1, yS, 20) + label((x0 + x1) / 2, yS + 22, "SOUTH · 100 CUBITS · 20 PILLARS", CY, 9))
    if "N" in show: o.append(posts(x0, yN, x1, yN, 20) + label((x0 + x1) / 2, yN - 12, "NORTH · 100 CUBITS · 20 PILLARS", CY, 9))
    if "W" in show: o.append(posts(x0, yN, x0, yS, 10) + f'<g transform="translate({f(x0 - 14)} {f((yN + yS) / 2)}) rotate(-90)">' + label(0, 0, "WEST · 50 · 10 PILLARS", CY, 9) + '</g>')
    if "E" in show:
        g1, g2 = yN + (yS - yN) * 15 / 50, yN + (yS - yN) * 35 / 50
        o.append(f'<path d="M{f(x1)} {f(g1)} L {f(x1)} {f(g2)}" stroke="{BLUE}" stroke-width="6"></path><path d="M{f(x1)} {f(g1)} L {f(x1)} {f(g2)}" stroke="{SCARLET}" stroke-width="2" stroke-dasharray="6 6"></path>')
        o.append(posts(x1, yN, x1, g1, 3) + posts(x1, g2, x1, yS, 3) + posts(x1, g1, x1, g2, 3, c=GOLD))
        o.append(label(x1 + 8, (g1 + g2) / 2 - 4, "GATE", "#FFD23F", 9, "start") + label(x1 + 8, (g1 + g2) / 2 + 8, "20", "#FFD23F", 9, "start")
                 + label(x1 + 8, (yN + g1) / 2, "15", CY, 9, "start") + label(x1 + 8, (g2 + yS) / 2, "15", CY, 9, "start"))
    tx = x0 + (x1 - x0) * 0.3
    o.append(f'<rect x="{f(tx - (x1 - x0) * 0.15)}" y="{f(yN + (yS - yN) * 0.4)}" width="{f((x1 - x0) * 0.3)}" height="{f((yS - yN) * 0.2)}" fill="{GOLD}" opacity="0.5" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             + label(tx, yN + (yS - yN) * 0.53, "TABERNACLE", "#0D0D0F", 8))
    ax = x0 + (x1 - x0) * 0.72
    o.append(f'<rect x="{f(ax - 10)}" y="{f((yN + yS) / 2 - 10)}" width="20" height="20" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.4"></rect>' + label(ax, (yN + yS) / 2 + 24, "ALTAR", CY, 8))
    return "".join(o)

def court_elev(w, h, x0f=0.06):
    """A length of the court's hangings: fine twined linen five cubits high on pillars filleted with silver, sockets of brass, pins of brass."""
    o = [bp(w, h), title_bar(w, "THE HANGINGS · ELEVATION")]
    x0, x1, top, bot = w * x0f, w * 0.94, h * 0.3, h * 0.82; n = 8 if x0f < 0.3 else 5
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(bot - top)}" fill="{LINEN}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for k in range(n + 1):
        px = x0 + (x1 - x0) * k / n
        o.append(f'<rect x="{f(px - 5)}" y="{f(top - 12)}" width="10" height="{f(bot - top + 12)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 f'<rect x="{f(px - 6)}" y="{f(top - 14)}" width="12" height="6" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1"></rect>'
                 f'<path d="M{f(px - 9)} {f(bot + 10)} L {f(px - 5)} {f(bot)} L {f(px + 5)} {f(bot)} L {f(px + 9)} {f(bot + 10)} Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.2"></path>'
                 f'<path d="M{f(px)} {f(top - 10)} L {f(px + (x1 - x0) / n * 0.4)} {f(bot + 14)}" stroke="{CY}" stroke-width="0.8" opacity="0.6"></path>')
    o.append(dim(x1 + 0, bot, x1 + 0, top, "5 CUBITS", off=-14, size=8))
    o.append(tag(x0 + (x1 - x0) / n, top - 12, "FILLETS · HOOKS OF SILVER", x0 + (x1 - x0) * 0.3, h * 0.12) + tag(x0 + (x1 - x0) * 2 / n, bot + 6, "SOCKETS · PINS OF BRASS", x0 + (x1 - x0) * 0.5, h * 0.96))
    return "".join(o)

def olive_oil(w, h):
    """Pure olive oil beaten for the light: an olive branch, a press-stone, a jar, and the lamp burning continually."""
    o = [bp(w, h), title_bar(w, "PURE OLIVE OIL BEATEN · FOR THE LIGHT")]
    cx, cy = w * 0.26, h * 0.56
    o.append(f'<path d="M{f(cx - 70)} {f(cy + 40)} C {f(cx - 20)} {f(cy)} {f(cx + 20)} {f(cy - 20)} {f(cx + 70)} {f(cy - 40)}" stroke="#5A3A22" stroke-width="4" fill="none"></path>'
             + "".join(f'<ellipse cx="{f(cx + d)}" cy="{f(cy - d * 0.5 + (10 if k % 2 else -10))}" rx="14" ry="5" fill="#5E8F26" stroke="#0D0D0F" stroke-width="1.2" transform="rotate(-30 {f(cx + d)} {f(cy - d * 0.5)})"></ellipse>' for k, d in enumerate(range(-50, 60, 20)))
             + "".join(f'<ellipse cx="{f(cx + d)}" cy="{f(cy - d * 0.5 + 14)}" rx="5" ry="6" fill="#3A4A1A" stroke="#0D0D0F" stroke-width="1"></ellipse>' for d in (-30, 10, 40)))
    jx = w * 0.56
    o.append(f'<path d="M{f(jx - 14)} {f(h * 0.4)} L {f(jx + 14)} {f(h * 0.4)} C {f(jx + 30)} {f(h * 0.6)} {f(jx + 22)} {f(h * 0.8)} {f(jx)} {f(h * 0.8)} C {f(jx - 22)} {f(h * 0.8)} {f(jx - 30)} {f(h * 0.6)} {f(jx - 14)} {f(h * 0.4)} Z" fill="#C8B040" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(S1.lamp(w * 0.82, h * 0.9, min(0.7, h / 280)))
    return "".join(o)
