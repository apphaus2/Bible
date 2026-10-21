"""Drawings for Ezekiel 26–28: Tyre on her rock in the sea (by day, besieged from the mainland, a bare rock for the spreading
of nets); the ship of Tyre as a blueprint plate (Ezekiel 27: the planks of Senir, the cedar mast, the oars of Bashan, the
linen sail of Egypt, the blue and purple awning) and the ship broken by the east wind; Tyre's traffickers as a map; the
mariners lamenting on the shore; the prince of Tyre's seat in the midst of the seas; the stones of Eden (a plate); the fire
brought forth from the midst; Sidon."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art9 import *
from ezk.art9 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1

SEA, SEA_D = "#1F6F9A", "#0F4C68"

def waves(w, y, seed, color="#E8F6FA", n=12, amp=6):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(x)} {f(y + r.uniform(-4, 8))} q 10 -{amp} 20 0 q 10 {amp} 20 0" stroke="{color}" stroke-width="2" fill="none" opacity="0.8"></path>'
                   for x in [r.uniform(-20, w) for _ in range(n)])

def galley(x, y, s=1.0, sail="#F3EFE6", broken=False, flip=False):
    """A merchant ship of Tarshish: a long hull, one mast with a square sail, a row of oars."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">',
         P("M-120 -10 C -100 14 100 14 130 -16 L 140 -36 L 110 -20 L -100 -20 L -128 -40 Z", "#8A5A30", 2.4),
         '<path d="M-100 -12 L 110 -12" stroke="#5A3A1A" stroke-width="2"></path>']
    o += [f'<path d="M{-90 + i * 22} -6 L {-100 + i * 22} 22" stroke="#5A3A1A" stroke-width="3"></path>' for i in range(9)]
    if broken:
        o.append('<path d="M0 -20 L 30 -110" stroke="#0D0D0F" stroke-width="7"></path><path d="M0 -20 L 30 -110" stroke="#B5793A" stroke-width="4"></path>'
                 + P("M30 -104 L 90 -70 L 70 -40 L 18 -60 Z", sail, 2, ' opacity="0.9"'))
    else:
        o.append('<path d="M0 -20 L 0 -150" stroke="#0D0D0F" stroke-width="7"></path><path d="M0 -20 L 0 -150" stroke="#B5793A" stroke-width="4"></path>'
                 + P("M-50 -140 L 50 -140 L 56 -50 L -56 -50 Z", sail, 2.2)
                 + '<path d="M-56 -50 L 56 -50 M-52 -110 L 52 -110 M-54 -80 L 54 -80" stroke="#7A3BA8" stroke-width="2" opacity="0.7"></path>'
                 + P("M60 -30 L 100 -30 L 104 -22 L 56 -22 Z", "#3A3A8A", 1.6))
    return "".join(o) + "</g>"

def tyre(w, h, seed, mode="day"):
    """Tyre that dwellest at the entry of the sea: the city on its rock in the sea, walls and towers, ships in the harbour.
    mode: day; siege (forts and a mound on the shore, the dust of horsemen, many nations coming up as the waves); ruin (a bare
    rock in the sea, fishers' nets spread to dry, no one drawn); burning; sidon (the city on the shore)."""
    r = random.Random(seed)
    skies = {"day": ("#6AB0D8", "#F3E8C8"), "siege": ("#5A4A5A", "#C8A080"), "ruin": ("#8A9AB0", "#E8E0D0"), "burning": ("#2A0A0A", "#C84A1A"), "sidon": ("#7AA8C8", "#F3E0C0")}
    o = [bg(f"ty{seed}{mode}", w, h, [(0, skies[mode][0]), (1, skies[mode][1])])]
    hy = h * 0.66
    o.append(f'<rect x="-10" y="{f(hy)}" width="{f(w + 20)}" height="{f(h - hy + 10)}" fill="{SEA}" stroke="{INK}" stroke-width="2"></rect>')
    o.append(waves(w, hy + h * 0.1, seed, n=14) + waves(w, hy + h * 0.24, seed + 1, n=14))
    if mode in ("siege",):
        o.append(f'<path d="M-10 {f(hy - 6)} L {f(w * 0.28)} {f(hy - 10)} L {f(w * 0.32)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8946A" stroke="{INK}" stroke-width="2"></path>')
        o.append(f'<path d="M{f(w * 0.18)} {f(hy)} L {f(w * 0.36)} {f(hy + h * 0.08)} L {f(w * 0.36)} {f(hy + h * 0.14)} L {f(w * 0.2)} {f(hy + h * 0.1)} Z" fill="#9A7A4A" stroke="{INK}" stroke-width="2"></path>')
        for fx in (0.06, 0.16): o.append(f'<path d="M{f(w * fx - 14)} {f(hy)} L {f(w * fx - 10)} {f(hy - h * 0.14)} L {f(w * fx + 10)} {f(hy - h * 0.14)} L {f(w * fx + 14)} {f(hy)} Z" fill="#7A6A4A" stroke="{INK}" stroke-width="2"></path>')
        o.append(smoke(w * 0.08, hy - h * 0.1, 6, seed, color="#C8A880", op=0.5, k=h / 400))
    cx = w * (0.62 if mode != "sidon" else 0.5)
    rock = f"M{f(cx - w * 0.26)} {f(hy + h * 0.06)} C {f(cx - w * 0.24)} {f(hy - h * 0.04)} {f(cx + w * 0.24)} {f(hy - h * 0.04)} {f(cx + w * 0.26)} {f(hy + h * 0.06)} Z"
    o.append(P(rock, "#8A7A6A", 2.4))
    if mode == "ruin":
        for i in range(5):
            x = cx - w * 0.16 + i * w * 0.08
            o.append(f'<path d="M{f(x)} {f(hy - h * 0.02)} L {f(x)} {f(hy - h * 0.16)} M{f(x + w * 0.08)} {f(hy - h * 0.02)} L {f(x + w * 0.08)} {f(hy - h * 0.16)}" stroke="#5A3A1A" stroke-width="3"></path>')
            o.append("".join(f'<path d="M{f(x)} {f(hy - h * (0.16 - j * 0.03))} L {f(x + w * 0.08)} {f(hy - h * (0.15 - j * 0.03))}" stroke="#C8C8B0" stroke-width="1.2"></path>' for j in range(5)))
        return "".join(o)
    x0, x1 = cx - w * 0.22, cx + w * 0.22
    for i in range(10):
        bx = x0 + r.uniform(0, x1 - x0 - 30); bh = h * r.uniform(0.12, 0.24)
        o.append(f'<rect x="{f(bx)}" y="{f(hy - h * 0.02 - bh)}" width="{f(r.uniform(22, 40))}" height="{f(bh)}" fill="{r.choice(["#D8C8A8", "#C8B898", "#E8D8B8"])}" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(hy - h * 0.08)}" width="{f(x1 - x0)}" height="{f(h * 0.08)}" fill="#B8A888" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(int((x1 - x0) / 16)):
        o.append(f'<rect x="{f(x0 + i * 16 + 2)}" y="{f(hy - h * 0.08 - 7)}" width="9" height="8" fill="#B8A888" stroke="{INK}" stroke-width="1.2"></rect>')
    for tx in (x0, cx, x1):
        o.append(f'<rect x="{f(tx - 12)}" y="{f(hy - h * 0.2)}" width="24" height="{f(h * 0.18)}" fill="#B8A888" stroke="{INK}" stroke-width="2"></rect>')
    if mode == "burning":
        for i in range(4): o.append(f'<g opacity="0.9">' + E.blaze(x0 + (i + 0.5) * (x1 - x0) / 4, hy - h * 0.08, w * 0.08, h * 0.2, seed + i, n=5) + '</g>')
        o.append(smoke(cx, hy - h * 0.3, 7, seed, color="#2A1A1A", op=0.6, k=h / 300))
    k = min(0.6, h / 600)
    if mode in ("day", "sidon"):
        o.append(galley(w * 0.18, hy + h * 0.16, k) + galley(w * 0.9, hy + h * 0.26, k * 0.8, sail="#E8D8A8", flip=True))
    return "".join(o)

def ship_plate(w, h):
    """The ship of Tyre as a blueprint plate: planks of fir-trees from Senir, a cedar from Lebanon for the mast, oars of the
    oaks of Bashan, benches of ivory inlaid in boxwood, a sail of fine linen with broidered work from Egypt, an awning of blue
    and purple from the isles of Elishah."""
    o = [bp(w, h), title_bar(w, "THE SHIP OF TYRE · PERFECT IN BEAUTY")]
    k = min(w / 520, h / 200)
    cx, base = w * 0.3, h * 0.86
    o.append(galley(cx, base - 10 * k, k))
    tx = w * 0.58
    rows = [("MAST · A CEDAR FROM LEBANON", cx, base - 120 * k), ("SAIL · FINE LINEN OF EGYPT", cx + 30 * k, base - 90 * k),
            ("AWNING · BLUE AND PURPLE · ELISHAH", cx + 80 * k, base - 36 * k), ("BENCHES · IVORY IN BOXWOOD", cx + 10 * k, base - 24 * k),
            ("PLANKS · FIR-TREES OF SENIR", cx - 60 * k, base - 16 * k), ("OARS · THE OAKS OF BASHAN", cx - 40 * k, base + 8 * k)]
    for i, (t, x, y) in enumerate(rows):
        o.append(tag(x, y, t, tx, h * (0.16 + i * 0.13), size=8))
    return "".join(o)

def shipwreck(w, h, seed):
    """Thy rowers have brought thee into great waters: the east wind hath broken thee in the heart of the seas — the ship
    breaking in a storm, the wares sinking (no one drawn)."""
    r = random.Random(seed)
    o = [bg(f"sw{seed}", w, h, [(0, "#1A1A2A"), (1, "#4A5A6A")]), clouds(w, h * 0.08, seed, n=8, color="#2A2A3A", op=0.95, ry=0.08)]
    o.append(f'<path d="M-10 {f(h * 0.6)} Q {f(w * 0.25)} {f(h * 0.4)} {f(w * 0.5)} {f(h * 0.62)} T {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{SEA_D}" stroke="{INK}" stroke-width="2.4"></path>')
    k = min(0.9, h / 360)
    o.append(f'<g transform="rotate(-18 {f(w * 0.5)} {f(h * 0.62)})">' + galley(w * 0.5, h * 0.66, k, broken=True) + '</g>')
    o.append(waves(w, h * 0.7, seed, n=16, amp=10) + waves(w, h * 0.86, seed + 1, n=16, amp=10))
    for _ in range(6):
        x = r.uniform(0.2, 0.8) * w; y = r.uniform(0.75, 0.95) * h
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(r.uniform(10, 24))}" height="{f(r.uniform(8, 14))}" fill="#8A5A30" stroke="{INK}" stroke-width="1.4" transform="rotate({r.uniform(-30, 30):.0f} {f(x)} {f(y)})"></rect>')
    o.append(wind_lines(w, h, seed, n=8, color="#C8D8E8", op=0.6, y0=0.1, y1=0.5))
    return "".join(o)

TRADE = {"TARSHISH": (0.04, 0.42), "JAVAN": (0.16, 0.14), "TUBAL": (0.4, 0.04), "MESHECH": (0.56, 0.06), "TOGARMAH": (0.66, 0.14), "DEDAN": (0.64, 0.92),
         "SYRIA": (0.5, 0.3), "JUDAH · ISRAEL": (0.36, 0.62), "DAMASCUS": (0.52, 0.42), "VEDAN": (0.56, 0.82), "ARABIA · KEDAR": (0.74, 0.7),
         "SHEBA · RAAMAH": (0.8, 0.94), "HARAN": (0.7, 0.3), "CANNEH · EDEN": (0.84, 0.42), "ASSHUR · CHILMAD": (0.88, 0.56), "PERSIA · LUD · PUT": (0.94, 0.8)}
def trade_map(w, h, hi=None):
    """Tyre, the merchant of the peoples unto many isles: her traffickers as a technical map, a line from each to Tyre."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 {f(h * 0.2)} C {f(w * 0.1)} {f(h * 0.3)} {f(w * 0.22)} {f(h * 0.4)} {f(w * 0.28)} {f(h * 0.56)} L {f(w * 0.24)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.1, h * 0.7, "THE GREAT SEA", "#4A7A9A", 9))
    T = (w * 0.3, h * 0.46)
    for nm, (x, y) in TRADE.items():
        on = hi is None or nm in hi
        o.append(route([(w * x, h * y), T], color="#FFD23F" if on else "#2A4A6A", sw=1.4, dash="4 5", arrow=False))
        o.append(node(w * x, h * y, nm, "#FFD23F" if on else "#4A7A9A", r=4, dy=-9, size=8 if on else 7))
    o.append(node(*T, "TYRE", "#D7261E", r=7, dy=-13, size=11))
    return "".join(o)

def mariners(p, w, h, seed):
    """The mariners and all the pilots of the sea come down from their ships and stand upon the land, casting dust upon
    their heads, girded with sackcloth, wailing."""
    o = [mk.defs(p, *ALL), bg(f"mr{seed}", w, h, [(0, "#4A4A6A"), (1, "#C8A890")])]
    o.append(f'<rect x="-10" y="{f(h * 0.4)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="{SEA}" stroke="{INK}" stroke-width="2"></rect>' + waves(w, h * 0.5, seed, n=10))
    k = min(0.5, h / 600)
    o.append(galley(w * 0.12, h * 0.5, k, sail="#C8B898") + galley(w * 0.9, h * 0.52, k * 0.9, flip=True))
    o.append(ground(w, h, h * 0.66, "#C8B080", dy=0))
    s = min(h * 0.84 / 200, 1.0)
    for i in range(6):
        x = w * (0.12 + i * 0.152)
        o.append(mk.person(p, round(x), round(h * 0.98), round(s, 3), body=SKIN, cloth=["#5A5248", "#4A4A3A", "#6A5A48"][i % 3], sw=2.6, flip=i % 2 == 1,
                           up=[(-22, -158), (-14, -196), (2, -206)] if i % 2 == 0 else None, extra=A.headcloth("#3A3A3A") + A.BLACK_BEARD))
        if i % 2 == 0: o.append(smoke(x, h * 0.98 - 210 * s, 3, seed + i, color="#C8B898", op=0.6, k=s * 0.4))
    return "".join(o)

def seat_of_god(w, h, seed):
    """Thou hast said, I am a god, I sit in the seat of God, in the midst of the seas: an empty golden throne on the rock of
    Tyre, treasures heaped about it, the sea all round (no one drawn)."""
    o = [tyre(w, h, seed, mode="day")]
    k = min(1.2, h / 300)
    cx, by = w * 0.62, h * 0.6
    o.append(glow(f"sg{seed}", cx, by - 40 * k, 80 * k, 60 * k, "#FFE680", 0.6))
    o.append(P(f"M{f(cx - 26 * k)} {f(by)} L {f(cx - 26 * k)} {f(by - 70 * k)} L {f(cx + 26 * k)} {f(by - 70 * k)} L {f(cx + 26 * k)} {f(by)} Z", "#E8B830", 2.2)
             + P(f"M{f(cx - 34 * k)} {f(by - 30 * k)} L {f(cx + 34 * k)} {f(by - 30 * k)} L {f(cx + 34 * k)} {f(by - 22 * k)} L {f(cx - 34 * k)} {f(by - 22 * k)} Z", "#C8963E", 2))
    o.append("".join(f'<circle cx="{f(cx + dx * k)}" cy="{f(by - 4 * k)}" r="{f(5 * k)}" fill="{c}" stroke="{INK}" stroke-width="1.2"></circle>' for dx, c in ((-50, "#E8B830"), (-40, "#C8C8D0"), (44, "#E8B830"), (54, "#D7261E"))))
    return "".join(o)

STONES = [("SARDIUS", "#C8202A"), ("TOPAZ", "#E8C840"), ("DIAMOND", "#E8F0F8"), ("BERYL", "#8FD8B8"), ("ONYX", "#3A3A44"), ("JASPER", "#4A8A5A"),
          ("SAPPHIRE", "#1F4FBF"), ("EMERALD", "#1F9A5A"), ("CARBUNCLE", "#B01A3A"), ("GOLD", "#E8B830")]
def eden_stones(w, h):
    """Thou wast in Eden, the garden of God; every precious stone was thy covering: a plate of the stones and the gold."""
    o = [bp(w, h), title_bar(w, "EVERY PRECIOUS STONE WAS THY COVERING")]
    cols = 5; cw = w / cols; rh = h * 0.36
    for i, (nm, c) in enumerate(STONES):
        r_, cc = divmod(i, cols)
        x = cw * (cc + 0.5); y = h * 0.3 + r_ * rh
        R = min(cw * 0.22, rh * 0.28)
        o.append(f'<path d="M{f(x)} {f(y - R)} L {f(x + R)} {f(y - R * 0.2)} L {f(x + R * 0.6)} {f(y + R)} L {f(x - R * 0.6)} {f(y + R)} L {f(x - R)} {f(y - R * 0.2)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.8"></path>'
                 f'<path d="M{f(x - R * 0.5)} {f(y - R * 0.3)} L {f(x)} {f(y - R * 0.7)}" stroke="#FFFFFF" stroke-width="2" opacity="0.7"></path>' + label(x, y + R + 14, nm, "#8FD0E2", 8))
    return "".join(o)

def fire_midst(w, h, seed):
    """I have brought forth a fire from the midst of thee; it hath devoured thee, and I have turned thee to ashes upon the
    earth: the rock of Tyre with its towers burning, ashes drifting over the sea."""
    return tyre(w, h, seed, mode="burning")

def gathered(w, h, seed):
    """They shall dwell securely therein, build houses and plant vineyards: the mountains of Israel green, houses and vines."""
    o = [mountains(w, h, seed, "fruitful")]
    for i in range(4): o.append(house(w * (0.56 + i * 0.1), h * 0.84, w * 0.08, h * 0.1, color="#C8A878"))
    return "".join(o)
