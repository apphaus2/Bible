"""Drawings for Revelation 15–18 (chapter 5 of the volume): the seven last plagues and the fall of Babylon. The bowls are
poured over land, sea, rivers, sun, the beast's empty throne, the dried Euphrates and the air — never over people drawn;
the unclean spirits like frogs are words only; Har-Magedon an empty plain. Babylon the great harlot: no woman is ever drawn —
the scarlet beast's heraldic plate with the golden cup, the seven mountains and kings as a chart, the city itself; her fall as
the smoke of the burning city seen far off by kings, merchants and shipmasters standing afar, the merchants' cargo as a
roll plate, the millstone cast into the sea, the city empty with no lamp.

    bowl_angels(p, w, h, seed, bowls=)    seven angels arrayed in white, golden girdles at their breasts (bowls= in hand)
    glass_fire(p, w, h, seed)             the sea of glass mingled with fire, the victors standing by it with harps
    tabernacle(p, w, h, seed, stage=)     the temple of the tabernacle of the testimony opened ("open" — the seven coming out;
                                          "bowls" — a living creature giving the seven golden bowls; "smoke" — filled with smoke)
    bowl(p, w, h, seed, which)            a bowl poured out: earth, sea, rivers, sun, throne, euphrates, air
    gathering(w, h, seed, empty=)         the kings gathered: camps and banners on a plain at dusk (empty= Har-Magedon, no one)
    city_split(w, h, seed)                the great city divided into three parts, the great hail
    great_city(cx, base, wd, hh, seed, state=)   Babylon: walls, the blue gate, the stepped tower (proud, burning, ruin, dark)
    many_waters(p, w, h, seed)            the angel and John by the many waters, the city far off
    seven_kings(w, h)                     the seven heads: seven mountains, seven kings — a chart
    ten_kings(w, h, seed)                 the ten horns, ten kings, and the Lamb that overcometh them: a plate
    waters_plate(w, h)                    the waters: peoples, and multitudes, and nations, and tongues
    babylon(p, w, h, seed, stage)         "glory" (an angel lightening the earth over the fallen city), "exodus" (come forth,
                                          my people), "proud", "burning", "kings", "merchants", "ships" (standing afar off),
                                          "empty" (no lamp), "millstone" (the strong angel casting it into the sea)
    cargo(w, h)                           the merchandise of 18:12–13 as a roll plate"""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rev.art4 import *
from rev.art import f, INK, GOLD, GOLD_L, WHITE, GIRDLE
from dan.art import ziggurat, bab_gate
from oba.minor import cup

GOLDEN_BOWL = '<path d="M-44 -92 C -42 -80 -20 -80 -18 -92 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'

def bowl_angels(p, w, h, seed, bowls=False):
    """The seven angels having the seven plagues (15:1, 15:6): arrayed with precious stone, pure and bright, golden girdles
    about their breasts; bowls= each holding a golden bowl."""
    o = [defs(p), sky(w, h, "#2A1440", "#8A4A6A"), halo(w * 0.5, h * 0.2, w * 0.6, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.15, 30, h * 0.08, w, "#FFFDF0", 0.3, 4)]
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.96)}" rx="{f(w * 0.5)}" ry="{f(h * 0.08)}" fill="#E8C8D8" opacity="0.4"></ellipse>')
    s = h * 0.78 / 205
    for i in range(7):
        x = w * (0.08 + 0.84 * i / 6)
        o.append(angel(p, x, h * 0.97 - (0 if i % 2 == 0 else h * 0.04), s * (1.0 if i % 2 == 0 else 0.92), flip=i >= 4,
                       extra=GIRDLE + (GOLDEN_BOWL if bowls else "")))
    return "".join(o)

def glass_fire(p, w, h, seed):
    """A sea of glass mingled with fire, and them that came off victorious standing by it, having harps of God (15:2–3)."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#1A1440", "#6A3A6A"), halo(w * 0.5, h * 0.3, w * 0.5, "#FFF4C2", 0.6)]
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.58)}" rx="{f(w * 0.56)}" ry="{f(h * 0.22)}" fill="#C8ECF8" stroke="#8FD0E2" stroke-width="2.4"></ellipse>')
    for _ in range(16):
        x, y = w * r.uniform(0.1, 0.9), h * r.uniform(0.44, 0.7)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(14, 40))}" ry="{f(r.uniform(4, 9))}" fill="{r.choice(["#FF8A2E", "#FFB02E", "#D7261E"])}" opacity="0.55"></ellipse>')
    o.append(f'<ellipse cx="{f(w * 0.42)}" cy="{f(h * 0.52)}" rx="{f(w * 0.16)}" ry="{f(h * 0.03)}" fill="#FFFFFF" opacity="0.6"></ellipse>')
    s = h * 0.36 / 205
    for i in range(11):
        x = w * (0.05 + 0.9 * i / 10); b = h * 0.98
        o.append(robed(p, x, b, s, "#FFFFFF", skin=r.choice(["#C98E66", "#D9A27A", "#A8704E", "#8A5A3A"]), hair=r.choice(["#1A1210", "#3A2214", "#5A3A22"]),
                       woman=r.random() < 0.4, flip=x > w * 0.5, line="#3A3A4A", up=UP_HARP, extra=harp(-50, -112, 0.9)))
    return "".join(o)

def temple_front_heaven(cx, base, wd, hh, open_=True):
    """The temple of the tabernacle of the testimony in heaven: a white front, its doors open on light."""
    o = [f'<rect x="{f(cx - wd / 2)}" y="{f(base - hh)}" width="{f(wd)}" height="{f(hh)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.6"></rect>',
         f'<path d="M{f(cx - wd / 2 - 16)} {f(base - hh)} L {f(cx)} {f(base - hh - hh * 0.22)} L {f(cx + wd / 2 + 16)} {f(base - hh)} Z" fill="#D8CCB0" stroke="{INK}" stroke-width="2.6"></path>']
    for k in range(6):
        x = cx - wd * 0.44 + wd * 0.88 * k / 5
        if abs(x - cx) < wd * 0.16: continue
        o.append(f'<rect x="{f(x - wd * 0.03)}" y="{f(base - hh * 0.92)}" width="{f(wd * 0.06)}" height="{f(hh * 0.92)}" fill="#F3EEE0" stroke="{INK}" stroke-width="1.6"></rect>')
    dw, dh = wd * 0.26, hh * 0.72
    o.append(f'<rect x="{f(cx - dw / 2)}" y="{f(base - dh)}" width="{f(dw)}" height="{f(dh)}" fill="{"#FFF8DC" if open_ else "#6A4A2A"}" stroke="{INK}" stroke-width="2"></rect>')
    if open_: o.append(halo(cx, base - dh * 0.5, dh * 0.8, WHITE, 0.9))
    return "".join(o)

def tabernacle(p, w, h, seed, stage="open"):
    """The temple of the tabernacle of the testimony in heaven opened (15:5–8). "open": the seven angels coming out of it,
    golden girdles at their breasts; "bowls": one of the four living creatures (a medallion of light) and the seven golden
    bowls set out before the seven; "smoke": the temple filled with smoke from the glory of God (no one able to enter)."""
    o = [defs(p), sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.5, h * 0.4, w * 0.5, "#FFF4C2", 0.6)]
    o.append(f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(temple_front_heaven(w * 0.5, h * 0.9, w * 0.5, h * 0.62))
    if stage == "open":
        s = h * 0.5 / 205
        for i in range(7):
            x = w * (0.06 + 0.88 * i / 6)
            if abs(x - w * 0.5) < w * 0.08: x = w * 0.5
            o.append(angel(p, x, h * 0.98, s * (1.0 if abs(x - w * 0.5) > w * 0.2 else 0.85), flip=x > w * 0.5, extra=GIRDLE))
    if stage == "bowls":
        o.append(creature(w * 0.16, h * 0.4, h * 0.14, 1))
        for i in range(7):
            x = w * (0.32 + 0.06 * i)
            o.append(f'<path d="M{f(x - 14)} {f(h * 0.94)} C {f(x - 12)} {f(h * 0.94 + 12)} {f(x + 12)} {f(h * 0.94 + 12)} {f(x + 14)} {f(h * 0.94)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(smoke(w * 0.5, h * 0.5, 8, seed, color="#E8E2F0", op=0.5, k=h / 300))
    if stage == "smoke":
        o.append(smoke(w * 0.5, h * 0.7, 12, seed, color="#E8E2F0", op=0.75, k=h / 220) + smoke(w * 0.36, h * 0.8, 10, seed + 1, color="#D8D2E8", op=0.6, k=h / 260)
                 + smoke(w * 0.64, h * 0.8, 10, seed + 2, color="#D8D2E8", op=0.6, k=h / 260))
    return "".join(o)

def pourer(p, x, y, s, flip=False):
    """An angel in the sky pouring out a golden bowl (the bowl tipped at his outstretched hand, a stream falling)."""
    ex = ('<path d="M-70 -150 C -66 -136 -48 -138 -44 -150 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4" transform="rotate(60 -58 -146)"></path>'
          '<path d="M-66 -136 C -70 -100 -64 -60 -72 0" fill="none" stroke="#6A3A6A" stroke-width="5" opacity="0.7"></path>')
    return angel(p, x, y, s, up=[(-22, -158), (-44, -150), (-58, -148)], flip=flip, extra=ex)

def bowl(p, w, h, seed, which="earth"):
    """A bowl poured out (16:2–21), the angel in the sky at the left: "earth" (a dark land, no one in it), "sea" (the sea
    turned dark crimson, empty), "rivers" (the rivers and fountains darkened), "sun" (the sun scorching a cracked land),
    "throne" (darkness upon the empty throne of the beast), "euphrates" (the river dried, the way open, kings far off at the
    sunrising), "air" (lightnings, thunders and the great earthquake)."""
    r = random.Random(seed)
    tones = {"earth": ("#2A1A2A", "#6A4A4A"), "sea": ("#2A0A10", "#6A2A2A"), "rivers": ("#2A1A20", "#6A3A3A"), "sun": ("#C8501A", "#FFD8A0"),
             "throne": ("#05050A", "#1A1418"), "euphrates": ("#3A2A5A", "#F3B880"), "air": ("#14141E", "#4A4A5E")}
    o = [defs(p), sky(w, h, *tones[which])]
    hz = h * 0.62
    if which == "earth":
        o.append(hills(w, h, hz - h * 0.04, seed, color="#3A2A2A", amp=14, step=80) + ground(w, h, hz, "#4A3A2A", dy=0) + houses(w * 0.5, w * 0.95, hz + h * 0.04, h * 0.1, seed))
    elif which == "sea":
        o.append(sea(w, h, hz, seed, color="#6A0E16", deep="#2A0408"))
    elif which == "rivers":
        o.append(hills(w, h, hz - h * 0.04, seed, color="#3A2A2A", amp=14, step=80) + ground(w, h, hz, "#4A3A2A", dy=0) + river(w, hz + h * 0.14, h * 0.1, color="#6A0E16", foam="#8A3A3A", seed=seed))
        for fx in (0.2, 0.84): o.append(f'<ellipse cx="{f(w * fx)}" cy="{f(h * 0.9)}" rx="{f(w * 0.07)}" ry="{f(h * 0.03)}" fill="#6A0E16" stroke="{INK}" stroke-width="1.6"></ellipse>')
    elif which == "sun":
        o.append(halo(w * 0.62, h * 0.22, h * 0.5, "#FFF4C2", 0.9) + f'<circle cx="{f(w * 0.62)}" cy="{f(h * 0.22)}" r="{f(h * 0.12)}" fill="#FFF4C2" stroke="#FF8A2E" stroke-width="3"></circle>'
                 + rays(w * 0.62, h * 0.22, 24, h * 0.14, h * 0.6, "#FFE680", 0.6, 3))
        o.append(ground(w, h, hz, "#C88A4A", dy=0))
        for _ in range(16):
            x, y = r.uniform(0, w), r.uniform(hz + 6, h)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-30, 30))} {f(r.uniform(6, 16))} l {f(r.uniform(-20, 20))} {f(r.uniform(6, 14))}" fill="none" stroke="#7A4A2A" stroke-width="2"></path>')
        for k in range(5): o.append(f'<path d="M{f(w * (0.1 + 0.2 * k))} {f(hz - 4)} q 8 -12 0 -24 q -8 -12 0 -24" fill="none" stroke="#FFE6A0" stroke-width="2" opacity="0.5"></path>')
    elif which == "throne":
        o.append(darkness(w * 0.6, h * 0.5, w * 0.4, h * 0.5, seed, 0.8))
        cx, b, s = w * 0.62, h * 0.9, h / 300
        o.append(f'<path d="M{f(cx - 44 * s)} {f(b)} L {f(cx - 44 * s)} {f(b - 150 * s)} C {f(cx - 40 * s)} {f(b - 172 * s)} {f(cx + 40 * s)} {f(b - 172 * s)} {f(cx + 44 * s)} {f(b - 150 * s)} L {f(cx + 44 * s)} {f(b)} Z" fill="#1A1418" stroke="#4A3A3A" stroke-width="2.4"></path>'
                 f'<rect x="{f(cx - 56 * s)}" y="{f(b - 60 * s)}" width="{f(112 * s)}" height="{f(14 * s)}" fill="#2A2024" stroke="#4A3A3A" stroke-width="2"></rect>')
    elif which == "euphrates":
        o.append(halo(w * 0.86, hz, h * 0.4, "#FFE6A0", 0.8))
        o.append(ground(w, h, hz, "#B8905A", dy=0))
        o.append(f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.82)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h * 0.9)} C {f(w * 0.7)} {f(h * 0.98)} {f(w * 0.3)} {f(h * 0.86)} -10 {f(h * 0.9)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></path>')
        for _ in range(14):
            x, y = r.uniform(0, w), r.uniform(h * 0.74, h * 0.9)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-14, 14))} 4 l {f(r.uniform(-10, 10))} 4" fill="none" stroke="#5A4A2A" stroke-width="1.6"></path>')
        for k in range(30):
            x = w * (0.66 + 0.3 * k / 29)
            o.append(f'<path d="M{f(x)} {f(hz + 2)} L {f(x)} {f(hz - h * 0.035)}" stroke="#2A1A14" stroke-width="1.4"></path>')
        o.append(label(w * 0.04, h * 0.96, "EUPHRATES", "#F3EFE6", max(9, min(12, h / 22)), anchor="start"))
    elif which == "air":
        for i in range(6): o.append(bolt(w * (0.1 + 0.16 * i), 0, h * 0.6, seed + i, sw=3))
        o.append(hills(w, h, hz - h * 0.04, seed, color="#2A2A36", amp=14, step=80) + ground(w, h, hz, "#2E2A2E", dy=0))
        for k in range(6):
            x0 = w * r.uniform(0.05, 0.9)
            o.append(f'<path d="M{f(x0)} {f(hz + 4)} L {f(x0 + 14)} {f(hz + h * 0.1)} L {f(x0 + 4)} {f(hz + h * 0.2)} L {f(x0 + 20)} {f(h + 10)}" fill="none" stroke="#0D0D0F" stroke-width="3"></path>')
    if which != "throne":
        o.append(pourer(p, w * 0.2, h * 0.5, h * 0.42 / 205, flip=True))
    else:
        o.append(pourer(p, w * 0.16, h * 0.56, h * 0.46 / 205, flip=True))
    return "".join(o)

def gathering(w, h, seed, empty=False):
    """To gather them together unto the war of the great day (16:14, 16:16): the kings' camps and banners far off on a great
    plain at dusk; empty=True: the place which is called in Hebrew Har-Magedon — the plain empty, no one in it."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A1A2A", "#C8784A"), halo(w * 0.24, h * 0.6, h * 0.4, "#FF8A3D", 0.5)]
    hz = h * 0.6
    o.append(hills(w, h, hz - h * 0.04, seed, color="#4A3A3A", amp=16, step=100) + ground(w, h, hz, "#6A5A3A", dy=0))
    if not empty:
        for k in range(14):
            x = w * (0.08 + 0.84 * k / 13) + r.uniform(-8, 8); y = hz + h * r.uniform(0.04, 0.2); s = h / 400
            o.append(f'<path d="M{f(x - 14 * s)} {f(y)} L {f(x)} {f(y - 20 * s)} L {f(x + 14 * s)} {f(y)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="1.2"></path>'
                     f'<path d="M{f(x)} {f(y - 20 * s)} L {f(x)} {f(y - 40 * s)}" stroke="{INK}" stroke-width="1.4"></path>'
                     f'<path d="M{f(x)} {f(y - 40 * s)} L {f(x + 14 * s)} {f(y - 35 * s)} L {f(x)} {f(y - 30 * s)} Z" fill="{r.choice(["#B5281E", "#3A5A8A", "#E8B830", "#5A3A6A"])}"></path>')
    else:
        o.append(label(w * 0.5, h * 0.92, "HAR-MAGEDON", "#F3D8A0", max(10, min(14, h / 18))))
    return "".join(o)

def great_city(cx, base, wd, hh, seed, state="proud"):
    """Babylon the great: the long wall, the blue gate with its beasts, the stepped tower behind; state "proud" (lit at
    night), "burning", "ruin", "dark" (no lamp)."""
    o = []
    dark = state in ("dark", "ruin", "burning")
    o.append(ziggurat(cx - wd * 0.2, base - hh * 0.3, wd * 0.4, hh * 0.9, dark=dark))
    o.append(houses(cx - wd / 2, cx + wd / 2, base - hh * 0.3, hh * 0.3, seed, lit=state == "proud",
                    colors=("#5A4A4A", "#4A3E40", "#6A5A54") if dark else ("#E8D8B8", "#D8C8A0", "#E0CCA8")))
    o.append(f'<rect x="{f(cx - wd / 2)}" y="{f(base - hh * 0.3)}" width="{f(wd)}" height="{f(hh * 0.3)}" fill="{"#4A3E40" if dark else "#C8A878"}" stroke="{INK}" stroke-width="2"></rect>')
    o.append(bab_gate(cx + wd * 0.22, base, wd * 0.24, hh * 0.42))
    if state == "ruin": o.append(ruin(cx - wd / 2, cx + wd / 2, base, hh * 0.3, seed, color="#6A5A54"))
    if state == "burning":
        o.append(fires(cx - wd / 2, cx + wd / 2, base - hh * 0.2, hh * 0.5, seed, n=6))
        o.append(smokes([cx - wd * 0.3, cx, cx + wd * 0.3], base - hh * 0.4, seed, k=hh / 160, color="#2A2024", op=0.65, n=10))
    return "".join(o)

def many_waters(p, w, h, seed):
    """Come hither, I will show thee the judgment of the great harlot that sitteth upon many waters (17:1): one of the seven
    angels and John on a height above many waters running together, the great city far off on them (no woman drawn)."""
    o = [defs(p), sky(w, h, "#2A2A5A", "#E8A880")]
    hz = h * 0.5
    o.append(sea(w, h, hz, seed, color="#2A5A8A", deep="#0F3050"))
    for k in range(4):
        o.append(f'<path d="M{f(w * (0.2 + 0.2 * k))} {f(h + 10)} C {f(w * (0.24 + 0.2 * k))} {f(h * 0.8)} {f(w * (0.4 + 0.1 * k))} {f(h * 0.6)} {f(w * 0.6)} {f(hz + 6)}" fill="none" stroke="#8FD0E2" stroke-width="3" opacity="0.6"></path>')
    o.append(great_city(w * 0.62, hz + 4, w * 0.4, h * 0.3, seed, "proud"))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} C {f(w * 0.12)} {f(h * 0.66)} {f(w * 0.26)} {f(h * 0.72)} {f(w * 0.34)} {f(h + 10)} Z" fill="#4A3A3A" stroke="{INK}" stroke-width="2.4"></path>')
    s = h * 0.32 / 205
    o.append(angel(p, w * 0.08, h * 0.74, s, up=[(-22, -158), (-46, -160), (-66, -166)], flip=True, extra=GIRDLE))
    o.append(john_fig(p, w * 0.19, h * 0.76, s * 0.94, flip=True))
    return "".join(o)

def seven_kings(w, h):
    """The seven heads are seven mountains … and they are seven kings (17:9–11): a chart — seven mountains in a row, each
    with its king's crown: five fallen, one is, the other not yet come; and the beast, an eighth, of the seven."""
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE SEVEN HEADS · SEVEN MOUNTAINS · SEVEN KINGS")]
    n = 7; cw = (w - 40) / 8
    for i in range(8):
        x = 20 + cw * (i + 0.5); b = h * 0.8
        if i < 7:
            o.append(f'<path d="M{f(x - cw * 0.42)} {f(b)} L {f(x)} {f(b - h * 0.34)} L {f(x + cw * 0.42)} {f(b)} Z" fill="#2A3A5A" stroke="#8FD0E2" stroke-width="1.4"></path>')
        st = "fallen" if i < 5 else "is" if i == 5 else "not" if i == 6 else "eighth"
        col = {"fallen": "#5A5A6A", "is": "#E8B830", "not": "none", "eighth": "#D7261E"}[st]
        cy = b - h * 0.42 if i < 7 else h * 0.5
        o.append(f'<path d="M{f(x - 14)} {f(cy)} L {f(x - 15)} {f(cy - 14)} L {f(x - 7)} {f(cy - 7)} L {f(x)} {f(cy - 18)} L {f(x + 7)} {f(cy - 7)} L {f(x + 15)} {f(cy - 14)} L {f(x + 14)} {f(cy)} Z" '
                 f'fill="{col}" stroke="{"#FFD23F" if col == "none" else "#0D0D0F"}" stroke-width="1.4" {"stroke-dasharray=\"3 2\"" if col == "none" else ""} '
                 f'{"transform=\"rotate(90 " + f(x) + " " + f(cy) + ")\"" if st == "fallen" else ""}></path>')
        o.append(label(x, h * 0.9, ("I", "II", "III", "IV", "V", "VI", "VII", "VIII")[i], "#FFD23F", 9))
    o.append(label(20 + cw * 2.5, h * 0.97, "FIVE ARE FALLEN", "#8FD0E2", 8) + label(20 + cw * 5.5, h * 0.97, "ONE IS", "#E8B830", 8)
             + label(20 + cw * 6.5, h * 0.24, "NOT YET COME", "#8FD0E2", 8) + label(20 + cw * 7.5, h * 0.4, "AN EIGHTH", "#FF6A4A", 8))
    return "".join(o)

def ten_kings(w, h, seed):
    """The ten horns are ten kings … these shall war against the Lamb, and the Lamb shall overcome them (17:12–14): ten
    crowns in a row below, the Lamb in light above them, LORD OF LORDS AND KING OF KINGS."""
    o = [sky(w, h, "#1A1440", "#3A2A6A"), radiance(w, h, seed, cy=0.36)]
    o.append(lamb(w * 0.5 - 30 * h / 400, h * 0.5, h * 0.3 / 90))
    for i in range(10):
        x = w * (0.07 + 0.86 * i / 9); y = h * 0.88; s = h / 300
        o.append(f'<path d="M{f(x - 14 * s)} {f(y)} L {f(x - 15 * s)} {f(y - 14 * s)} L {f(x - 7 * s)} {f(y - 7 * s)} L {f(x)} {f(y - 18 * s)} L {f(x + 7 * s)} {f(y - 7 * s)} L {f(x + 15 * s)} {f(y - 14 * s)} L {f(x + 14 * s)} {f(y)} Z" '
                 f'fill="#8A7A5A" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(label(w * 0.5, h * 0.1, "LORD OF LORDS, AND KING OF KINGS", "#FFE680", max(9, min(12, h / 22))))
    return "".join(o)

def waters_plate(w, h):
    """The waters which thou sawest … are peoples, and multitudes, and nations, and tongues (17:15): a plate of waters with
    the four names upon them."""
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE WATERS WHICH THOU SAWEST")]
    for k in range(5):
        y = h * (0.3 + 0.14 * k)
        o.append(f'<path d="M20 {f(y)}' + "".join(f" q 22 {(-8 if j % 2 == 0 else 8)} 44 0" for j in range(int((w - 40) / 44))) + '" fill="none" stroke="#8FD0E2" stroke-width="2" opacity="0.7"></path>')
    for i, nm in enumerate(("PEOPLES", "MULTITUDES", "NATIONS", "TONGUES")):
        x = w * (0.14 + 0.24 * i)
        o.append(f'<rect x="{f(x - 60)}" y="{f(h * 0.5 - 14)}" width="120" height="26" fill="#12223A" stroke="#FFD23F" stroke-width="1.4"></rect>' + label(x, h * 0.5 + 4, nm, "#FFD23F", 10))
    return "".join(o)

def babylon(p, w, h, seed, stage="burning"):
    """Babylon the great (18), never a woman drawn. "glory": another angel coming down, the earth lightened with his glory,
    over the city fallen and haunted by birds; "exodus": come forth, my people — figures going out of her gate toward the
    light; "proud": the city lit at night; "burning": the city burning far off, its smoke going up; "kings", "merchants",
    "ships": standing afar off watching the smoke of her burning — the kings in crowns on a hill, the merchants with their
    laden beasts, the shipmasters on their decks; "empty": the city dark, no lamp, a broken harp and a cold millstone;
    "millstone": a strong angel casting a great millstone into the sea, the splash."""
    r = random.Random(seed)
    o = [defs(p)]
    if stage == "glory":
        o += [sky(w, h, "#3A2A4A", "#E8C8A0"), halo(w * 0.3, h * 0.2, w * 0.5, "#FFF4C2", 0.85), rays(w * 0.3, h * 0.2, 36, h * 0.08, w, "#FFFDF0", 0.4, 5)]
        o.append(great_city(w * 0.64, h * 0.92, w * 0.6, h * 0.5, seed, "ruin") + ground(w, h, h * 0.92, "#5A4A3A", dy=0))
        o.append(birds(9, w * 0.5, w * 0.95, h * 0.2, h * 0.5, seed, 0.7, 1.2))
        o.append(angel(p, w * 0.26, h * 0.62, h * 0.5 / 205, up=[(-22, -158), (-46, -170), (-66, -180)], flip=True))
        return "".join(o)
    if stage == "exodus":
        o += [sky(w, h, "#1A1028", "#5A3A4A"), halo(w * 0.08, h * 0.5, h * 0.6, "#FFF4C2", 0.8)]
        o.append(great_city(w * 0.66, h * 0.82, w * 0.64, h * 0.62, seed, "proud") + ground(w, h, h * 0.82, "#5A4A3A", dy=0))
        s = h * 0.3 / 205
        for i in range(6):
            x = w * (0.48 - 0.07 * i); b = h * 0.96 - i * 2
            o.append(robed(p, x, b, s * (1 - i * 0.03), r.choice(["#6A4A3A", "#3A4A6A", "#5A6A3A", "#7A3A3A", "#4A3A5A"]), head=r.choice(["#E8E2D6", "#3A3A3A"]) if i % 2 == 0 else None,
                           woman=i % 2 == 1, hair="#2A1A10" if i % 2 else None, beard="#2A1A10" if i % 2 == 0 else None, pose="walk"))
        return "".join(o)
    if stage in ("proud", "empty"):
        o += [sky(w, h, "#0B0B2A", "#2A1A3A"), starfield(w, h, seed, 50, 0.5)]
        o.append(great_city(w * 0.5, h * 0.84, w * 0.9, h * 0.66, seed, "proud" if stage == "proud" else "dark") + ground(w, h, h * 0.84, "#3A2A2A", dy=0))
        if stage == "empty":
            o.append(f'<g transform="translate({f(w * 0.2)} {f(h * 0.96)}) rotate(-70) scale({f(h / 260)})">' + harp(0, 0, 1.4).replace('translate(0.0 0.0) scale(1.4)', 'scale(1.4)') + '</g>')
            o.append(f'<circle cx="{f(w * 0.78)}" cy="{f(h * 0.94)}" r="{f(h * 0.06)}" fill="#6A6460" stroke="{INK}" stroke-width="2"></circle><circle cx="{f(w * 0.78)}" cy="{f(h * 0.94)}" r="{f(h * 0.012)}" fill="#1A1418"></circle>')
        return "".join(o)
    if stage == "millstone":
        o += [sky(w, h, "#2A2A4A", "#8A7A9A")]
        hz = h * 0.6
        o.append(sea(w, h, hz, seed, color="#2A4A6A", deep="#0F2A40", rough=True))
        sx, sy = w * 0.6, hz + h * 0.06
        o.append("".join(f'<path d="M{f(sx + d * k * 14)} {f(sy)} L {f(sx + d * (k * 26 + 20))} {f(sy - h * (0.24 - k * 0.04))}" stroke="#E8F4F8" stroke-width="{6 - k}" stroke-linecap="round"></path>' for d in (-1, 1) for k in range(4)))
        o.append(f'<ellipse cx="{f(sx)}" cy="{f(sy)}" rx="{f(w * 0.12)}" ry="{f(h * 0.03)}" fill="#E8F4F8" opacity="0.8"></ellipse>')
        o.append(f'<circle cx="{f(sx)}" cy="{f(sy - h * 0.06)}" r="{f(h * 0.08)}" fill="#7A746C" stroke="{INK}" stroke-width="2.4"></circle><circle cx="{f(sx)}" cy="{f(sy - h * 0.06)}" r="{f(h * 0.018)}" fill="#2A2420"></circle>')
        o.append(angel(p, w * 0.28, h * 0.62, h * 0.54 / 205, up=[(-22, -158), (-46, -176), (-70, -180)], flip=True))
        return "".join(o)
    # the burning city far off, and those standing afar
    o += [sky(w, h, "#1A0A10", "#8A3A2A")]
    hz = h * 0.56
    o.append(great_city(w * (0.66 if stage != "burning" else 0.5), hz, w * (0.44 if stage != "burning" else 0.8), h * (0.34 if stage != "burning" else 0.48), seed, "burning"))
    if stage == "ships":
        o.append(sea(w, h, hz, seed, color="#2A2A3A", deep="#14141E"))
        for i, (x, y, k) in enumerate(((0.16, 0.86, 1.0), (0.42, 0.76, 0.7), (0.86, 0.94, 0.9))):
            o.append(ship(w * x, h * y, h * k / 360, flip=i == 2))
            for d in (-1, 1):
                o.append(robed(p, w * x + d * 24 * h * k / 360, h * y - 14 * h * k / 360, h * k * 0.18 / 205, r.choice(["#3A4A6A", "#6A4A3A", "#4A5A3A"]), head="#E8E2D6", beard="#2A1A10",
                               up=[(-22, -158), (-14, -176), (-4, -190)]))
        return "".join(o)
    o.append(ground(w, h, hz, "#3A2A22", dy=0))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.74)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.36)} {f(h * 0.78)} {f(w * 0.46)} {f(h + 10)} Z" fill="#4A3A30" stroke="{INK}" stroke-width="2.4"></path>')
    if stage == "kings":
        s = h * 0.36 / 205
        crown = '<path d="M-12 -196 L -13 -208 L -6 -201 L 0 -211 L 6 -201 L 13 -208 L 12 -196 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
        for i, (x, col) in enumerate(((0.06, "#7A1A2A"), (0.15, "#3A2A6A"), (0.24, "#1F4A6A"), (0.33, "#5A3A1A"))):
            o.append(robed(p, w * x, h * 0.8 + i * 4, s, col, hair="#2A1A10", beard="#2A1A10", mantle="#E8B830" if i % 2 else None, flip=True, extra=crown,
                           up=[(-22, -158), (-14, -176), (-4, -190)] if i % 2 == 0 else None))
    elif stage == "merchants":
        s = h * 0.34 / 205
        o.append(E3.horse(w * 0.06, h * 0.86, h * 0.26 / 140, color="#8A6A4A"))
        for k in range(3):
            o.append(f'<rect x="{f(w * 0.02 + k * 18)}" y="{f(h * 0.62 + k * 4)}" width="22" height="16" fill="#C8A060" stroke="{INK}" stroke-width="1.4"></rect>')
        for i, (x, col) in enumerate(((0.2, "#6A3A1A"), (0.29, "#2A5A4A"), (0.38, "#7A5A2A"))):
            o.append(robed(p, w * x, h * 0.84 + i * 3, s, col, head="#E8D8B0", cord="#7A4A1A", beard="#2A1A10", flip=True,
                           up=[(-22, -158), (-14, -176), (-4, -190)] if i == 1 else None))
    return "".join(o)

CARGO = [("GOLD", "#E8B830"), ("SILVER", "#C8CCD4"), ("PRECIOUS STONE", "#2E9A8A"), ("PEARLS", "#F3F0EA"), ("FINE LINEN", "#F3EEE0"), ("PURPLE", "#6A2A7A"),
         ("SILK", "#E8C8D8"), ("SCARLET", "#C8281E"), ("THYINE WOOD", "#8A5A30"), ("IVORY", "#F0E8D0"), ("PRECIOUS WOOD", "#6A3A1E"), ("BRASS", "#B5652E"),
         ("IRON", "#6A6A72"), ("MARBLE", "#E8E4DC"), ("CINNAMON", "#9A5A2A"), ("SPICE", "#C8783A"), ("INCENSE", "#D8C8B0"), ("OINTMENT", "#E8D8A0"),
         ("FRANKINCENSE", "#F0E0B0"), ("WINE", "#6A1A2A"), ("OIL", "#C8B040"), ("FINE FLOUR", "#F3EFE6"), ("WHEAT", "#D8B060"), ("CATTLE", "#7A5A3A"),
         ("SHEEP", "#E8E2D6"), ("HORSES", "#5A3A22"), ("CHARIOTS", "#8A6A4A"), ("SLAVES", "#4A3A3A"), ("SOULS OF MEN", "#F3EFE6")]

def cargo(w, h):
    """The merchandise of the merchants of the earth (18:12–13) as a roll plate: every ware named in its swatch, in the
    order John names them, the last — souls of men — set apart."""
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE MERCHANDISE · NO MAN BUYETH ANY MORE")]
    cols = 6; n = len(CARGO) - 1
    rows_ = math.ceil(n / cols)
    cw, ch = (w - 40) / cols, min((h - 84) / rows_, 46)
    for i, (nm, c) in enumerate(CARGO[:-1]):
        x = 20 + (i % cols) * cw; y = 34 + (i // cols) * ch
        o.append(f'<rect x="{f(x + 3)}" y="{f(y + 3)}" width="{f(ch * 0.5)}" height="{f(ch - 8)}" fill="{c}" stroke="#8FD0E2" stroke-width="1.2"></rect>'
                 + label(x + ch * 0.5 + 8, y + ch / 2 + 3, nm, "#F3EFE6", max(7, min(9, cw / 14)), anchor="start"))
    y = 34 + rows_ * ch + 6
    o.append(f'<rect x="{f(w / 2 - 110)}" y="{f(y)}" width="220" height="24" fill="#3A1A1A" stroke="#FF6A4A" stroke-width="1.6"></rect>' + label(w / 2, y + 16, "AND SOULS OF MEN", "#FF6A4A", 10))
    return "".join(o)

def city_split(w, h, seed):
    """The great city divided into three parts, the cities of the nations fallen, every island fled away, the great hail
    (16:19–21): the city broken by two chasms under a storm, hailstones falling (no one drawn)."""
    r = random.Random(seed)
    o = [sky(w, h, "#14141E", "#4A4A5E")]
    for i in range(3): o.append(bolt(w * (0.2 + 0.3 * i), 0, h * 0.5, seed + i, sw=3))
    hz = h * 0.7
    o.append(great_city(w * 0.5, hz, w * 0.9, h * 0.46, seed, "dark") + ground(w, h, hz, "#2A2226", dy=0))
    for x0 in (0.36, 0.64):
        o.append(f'<path d="M{f(w * x0 - 10)} {f(h * 0.2)} L {f(w * x0 + 14)} {f(h * 0.45)} L {f(w * x0 - 8)} {f(hz)} L {f(w * x0 + 18)} {f(h + 10)} L {f(w * x0 + 40)} {f(h + 10)} L {f(w * x0 + 20)} {f(hz)} L {f(w * x0 + 34)} {f(h * 0.45)} L {f(w * x0 + 12)} {f(h * 0.2)} Z" fill="#0A0608" stroke="{INK}" stroke-width="2"></path>')
    for _ in range(50):
        x, y = r.uniform(0, w), r.uniform(0, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(3, 6))}" fill="#E8F4F8" stroke="#6A8A9A" stroke-width="1"></circle>')
    return "".join(o)
