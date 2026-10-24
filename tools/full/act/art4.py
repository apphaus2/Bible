"""Drawings for Acts 7, Stephen's defence: his history of the fathers is drawn with the Old Testament volumes' own drawings
(Genesis: Joseph's caravan, the chariot, the famine, the granaries; Exodus: the bricks, the Nile, the wilderness, the bush
burning, the dry path through the sea, the tent of meeting; Hosea: the calf), and the maps of Acts for Abraham's road. New
here: the host of heaven; the heaven a throne and the earth a footstool; the heavens opened to Stephen — the glory as light
breaking out of the sky, and at its right hand the Son of man standing, a tall figure of white light with no face (God is
never drawn: the glory is the light alone); and the stoning (7:58–60) told in words only, over the city wall outside the
gate at evening, where the witnesses' garments lie heaped at the feet of a young man named Saul (Paul's dark-brown robe and
headcloth and black beard, as he is ever after); then the wall alone at dusk. Built on act.art3."""
from act.art3 import *
from act.art3 import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue
import random, math
import mk

def ot(fn, *a, **k):
    """An Old Testament volume's drawing fn(p, w, h, seed) with the figure defs it expects from its own page."""
    return lambda w, h: mk.defs(a[0], *ALL) + fn(a[0], w, h, *a[1:], **k)

def abraham_road(w, h):
    """The God of glory appeared unto our father Abraham in Mesopotamia: the map from Ur of the Chaldæans up the
    Euphrates to Haran, and from Haran into the land of Canaan."""
    return geo.med_map(w, h, box=(31, 48, 28.5, 38.5), places=("UR", "HARAN", "SHECHEM", "JERUSALEM", "DAMASCUS", "MEMPHIS"),
                       routes=[("UR", (44.4, 33.2), (40.3, 35.6), "HARAN"), ("HARAN", (37.2, 35.8), "DAMASCUS", "SHECHEM")], hi=("UR", "HARAN", "SHECHEM"),
                       regions=("MESOPOTAMIA", "CHALDÆA", "CANAAN", "EGYPT", "SYRIA"), lit_routes=[0, 1], size=10, rsize=10,
                       title="ACTS 7:2–4 · FROM THE LAND OF THE CHALDÆANS")

def sinai_road(w, h):
    """Moses fled into the land of Midian; and the wilderness of mount Sinai: the map of Egypt, the wilderness and Midian."""
    return geo.med_map(w, h, box=(29, 38, 26.5, 32.5), places=("MEMPHIS", "MOUNT SINAI", "JERUSALEM", "SHECHEM"),
                       routes=[("MEMPHIS", (32.6, 30.0), (34.4, 29.6), (35.0, 28.6))], hi=("MOUNT SINAI",), regions=("EGYPT", "MIDIAN", "CANAAN"),
                       lit_routes=[0], size=10, rsize=10, title="ACTS 7:29–30 · THE LAND OF MIDIAN")

def tent_sojourn(p, w, h, seed):
    """None inheritance in it, not so much as to set his foot on: Abraham's tent alone in the open land under the stars, his
    figure at the door (grey hair and beard, a slate-blue robe, as in Genesis)."""
    from genesis.art3 import abram
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#2A2050"), mk.stars(70, w, h * 0.6, seed), hills(w, h, h * 0.62, seed, color="#1A1A3A", amp=12, step=90),
         ground(w, h, h * 0.7, "#2A2440", dy=0)]
    k = max(0.5, h / 320)
    cx = w * 0.62
    o.append(f'<path d="M{f(cx - 110 * k)} {f(b)} L {f(cx - 70 * k)} {f(b - 90 * k)} L {f(cx + 70 * k)} {f(b - 96 * k)} L {f(cx + 120 * k)} {f(b)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(cx - 20 * k)} {f(b)} L {f(cx)} {f(b - 70 * k)} L {f(cx + 20 * k)} {f(b)} Z" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    o.append(abram(p, w * 0.36, b, s, staff=True))
    return "".join(o)

def host_of_heaven(p, w, h, seed):
    """Gave them up to serve the host of heaven: the night sky crowded with stars over the dark camp in the wilderness, the
    tents black under them."""
    b = h * 0.94
    o = [sky(w, h, "#05051A", "#1E1650"), mk.stars(120, w, h * 0.7, seed), halo(w * 0.7, h * 0.24, h * 0.1, "#FFE680", 0.5),
         f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.24)}" r="{f(max(4, h * 0.02))}" fill="#FFF4C2"></circle>',
         hills(w, h, h * 0.74, seed, color="#0D0D1E", amp=10, step=90), ground(w, h, h * 0.8, "#0B0B18", dy=0)]
    for i in range(7):
        x = w * (0.06 + 0.14 * i); k = max(0.4, h / 500)
        o.append(f'<path d="M{f(x - 40 * k)} {f(b)} L {f(x - 20 * k)} {f(b - 40 * k)} L {f(x + 26 * k)} {f(b - 44 * k)} L {f(x + 46 * k)} {f(b)} Z" fill="#1A1420" stroke="#2A2A3A" stroke-width="1.6"></path>')
    return "".join(o)

def throne_footstool(p, w, h, seed):
    """The heaven is my throne, and the earth the footstool of my feet: the vault of the sky full of light over the whole
    round of the earth, mountains and sea and fields under it — no figure (God is never drawn)."""
    o = [sky(w, h, "#2A3A7A", "#FFF4C2"), rays(w * 0.5, -h * 0.1, 40, h * 0.1, max(w, h) * 1.2, color="#FFFDF0", op=0.25),
         glow(w * 0.5, 0, h * 0.6, "#FFFFFF", 0.8, f"{p}g"), clouds(w, h * 0.14, seed, n=6, color="#FFFDF0", op=0.8, h=h)]
    o.append(f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.2)} {f(h * 0.6)} {f(w * 0.8)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A8A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.68)} C {f(w * 0.7)} {f(h * 0.66)} {f(w * 0.9)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.7)} {f(h + 10)} Z" fill="#1F6F9A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.04)} {f(h * 0.66)} L {f(w * 0.14)} {f(h * 0.46)} L {f(w * 0.22)} {f(h * 0.56)} L {f(w * 0.3)} {f(h * 0.42)} L {f(w * 0.42)} {f(h * 0.64)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def son_of_man_light(x, y, s):
    """The Son of man standing, seen in the vision: a tall standing figure made only of white light, no face, no colour — the
    light of the glory about him (he is not otherwise drawn in a vision)."""
    return (f'<ellipse cx="{f(x)}" cy="{f(y - 110 * s)}" rx="{f(70 * s)}" ry="{f(140 * s)}" fill="#FFFFFF" opacity="0.6"></ellipse>'
            f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-26 0 C -30 -60 -28 -120 -22 -158 C -18 -170 18 -170 22 -158 C 28 -120 30 -60 26 0 Z" fill="#FFFFFF" stroke="#FFF4C2" stroke-width="3"></path>'
            '<circle cx="0" cy="-186" r="17" fill="#FFFFFF" stroke="#FFF4C2" stroke-width="3"></circle></g>')

def heavens_opened(p, w, h, seed, council_=False):
    """Behold, I see the heavens opened: the sky over the city torn open into a great depth of gold and white light (the
    glory of God — light only), and on the right of the glory the Son of man standing, a figure of white light without a
    face; council_=True Stephen below in the midst of the council, looking up, his face lit."""
    o = [sky(w, h, "#14123A", "#3A2A6A"), mk.stars(30, w, h * 0.5, seed)]
    cx, cy = w * 0.46, h * 0.28
    o.append(rays(cx, cy, 48, h * 0.1, max(w, h), color="#FFD23F", op=0.16, sw=5))
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.36)}" ry="{f(h * 0.22)}" fill="#FFE680" opacity="0.5"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.26)}" ry="{f(h * 0.16)}" fill="#FFF4C2" opacity="0.8"></ellipse>'
             + glow(cx, cy, h * 0.3, "#FFFFFF", 0.95, f"{p}gl"))
    s = fit(cy + h * 0.14, cy - h * 0.16)
    o.append(son_of_man_light(cx + w * 0.2, cy + h * 0.16, s))
    o.append(clouds(w, cy + h * 0.2, seed, n=7, color="#E8DCFF", op=0.6, h=h * 0.6))
    if council_:
        b = h * 0.96
        o.append(walls(-10, w + 10, b, h * 0.26, seed, towers=4, gate=False, lit=True))
        o.append(mk.defs(p, *ALL))
        ss = fit(b, b - h * 0.34)
        o.append(glow(w * 0.22, b - 120 * ss, 120 * ss, "#FFF4C2", 0.8, f"{p}st") + stephen(p, w * 0.22, b, ss, flip=True, up=UP_HIGH))
    return "".join(o)

def garments_wall(p, w, h, seed, dusk=False, saul_=True):
    """Outside the city: the great wall and its gate, the rocky ground, and the witnesses' garments laid down in a heap at
    the feet of a young man named Saul, who stands by them — the stoning is told in words only, nothing of it drawn.
    dusk=True: the evening after, the wall alone against the red sky, the garments taken up, a few stones lying."""
    b = h * 0.94
    top, bot = ("#2A1A3A", "#C8603A") if dusk else ("#5A6A9A", "#E8C890")
    o = [mk.defs(p, *ALL), sky(w, h, top, bot), walls(w * 0.36, w + 10, h * 0.6, h * 0.42, seed, towers=3, lit=dusk),
         ground(w, h, h * 0.6, "#8A7A5A" if not dusk else "#4A3A3A", dy=0)]
    r = random.Random(seed)
    for _ in range(14):
        x = r.uniform(0, w * 0.6); y = r.uniform(h * 0.66, h * 0.98); k = r.uniform(0.6, 1.4) * max(0.6, h / 300)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(10 * k)} {f(-6 * k)} l {f(12 * k)} {f(4 * k)} l {f(-4 * k)} {f(6 * k)} Z" fill="#9A8A7A" stroke="{INK}" stroke-width="1.2"></path>')
    s = fit(b, max(h * 0.3, b - 210))
    if not dusk:
        gx = w * 0.2
        for i, c in enumerate(("#6A4A3A", "#3A4A6A", "#8A6A3A", "#5A3A4A", "#4A5A3A")):
            o.append(f'<path d="M{f(gx - 50 * s + i * 8 * s)} {f(b - i * 7 * s)} C {f(gx - 20 * s)} {f(b - 20 * s - i * 7 * s)} {f(gx + 30 * s)} {f(b - 14 * s - i * 7 * s)} {f(gx + 54 * s - i * 6 * s)} {f(b - i * 6 * s)} Z" fill="{c}" stroke="{INK}" stroke-width="1.8"></path>')
        if saul_:
            o.append(paul(p, gx + 90 * s, b, s, flip=True))
    return "".join(o)
