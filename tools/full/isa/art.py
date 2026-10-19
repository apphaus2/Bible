"""Drawings for the Isaiah volume (chapter by chapter, added below), on top of 2 Chronicles' (chr2.art, which carries
chr1.art, kg2.art, kg1.art and 2 Samuel's drawings as K2). The images of the prophecy: the vineyard, the mountain of
Jehovah's house, the seraphim (God never drawn: light, smoke and an empty throne), the nations as technical maps, ruins and
empty cities for the judgments, the desert blossoming, the highway, the shepherd, the potter, the new heavens."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
import exodus2 as E2
from genesis.art2 import fit, ground, hills
from genesis.art3 import man, woman, sun, label, grid_bg, node, route
from jos.art import crowd_at, night

GOLD, CYAN, RED_C, INK = "#FFD23F", "#8FD0E2", "#D7261E", "#0D0D0F"

def bg(w, h, top, bot):
    return K2.sky(w, h, top, bot)

def rect(w, h, color):
    return f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{color}"></rect>'

def smoke(x, y, n, seed, r0=14, spread=18, color="#5A5060", op=0.7, rise=0.9):
    """A column of smoke rising from (x, y): n puffs growing and fading upward."""
    r = random.Random(seed); o = []
    for i in range(n):
        rr = r0 * (1 + i * 0.35)
        o.append(f'<circle cx="{f(x + r.uniform(-spread, spread) + i * 4)}" cy="{f(y - i * rr * rise)}" r="{f(rr)}" fill="{color}" opacity="{max(0.12, op - i * 0.05):.2f}"></circle>')
    return "".join(o)

def thorns(x0, x1, y, seed, n=14, s=1.0, color="#4A3A22"):
    """Briers and thorns: tangles of spiky strokes along a line."""
    r = random.Random(seed); o = []
    for _ in range(n):
        x = r.uniform(x0, x1); hh = r.uniform(18, 40) * s
        d = f"M{f(x)} {f(y)} " + " ".join(f"L {f(x + r.uniform(-14, 14) * s)} {f(y - hh * k / 4)}" for k in range(1, 5))
        o.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{f(2.2 * s)}"></path>')
        for k in range(3):
            yy = y - hh * (k + 1) / 4; xx = x + r.uniform(-8, 8) * s
            o.append(f'<path d="M{f(xx)} {f(yy)} l {f(6 * s)} {f(-5 * s)} M{f(xx)} {f(yy)} l {f(-6 * s)} {f(-4 * s)}" stroke="{color}" stroke-width="{f(1.6 * s)}"></path>')
    return "".join(o)

def tower(x, base, tw, th, color="#C8B48A", broken=False):
    """A watch-tower of stones: a tapering block with a crenellated top and a door."""
    top = base - th
    o = [f'<path d="M{f(x - tw / 2)} {f(base)} L {f(x - tw * 0.42)} {f(top)} L {f(x + tw * 0.42)} {f(top)} L {f(x + tw / 2)} {f(base)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>']
    if broken:
        o.append(f'<path d="M{f(x - tw * 0.42)} {f(top)} L {f(x - tw * 0.1)} {f(top + th * 0.2)} L {f(x + tw * 0.15)} {f(top + th * 0.08)} L {f(x + tw * 0.42)} {f(top + th * 0.3)} L {f(x + tw * 0.42)} {f(top - 2)} L {f(x - tw * 0.42)} {f(top - 2)} Z" fill="#8FD0E2" stroke="none"></path>')
    else:
        for i in range(4):
            o.append(f'<rect x="{f(x - tw * 0.42 + i * tw * 0.24)}" y="{f(top - th * 0.08)}" width="{f(tw * 0.12)}" height="{f(th * 0.08)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    o.append(f'<path d="M{f(x - tw * 0.1)} {f(base)} L {f(x - tw * 0.1)} {f(base - th * 0.24)} Q {f(x)} {f(base - th * 0.32)} {f(x + tw * 0.1)} {f(base - th * 0.24)} L {f(x + tw * 0.1)} {f(base)} Z" fill="#2A1E16"></path>')
    for k in range(1, 5):
        o.append(f'<path d="M{f(x - tw * 0.44)} {f(base - th * k / 5)} L {f(x + tw * 0.44)} {f(base - th * k / 5)}" stroke="#8A7656" stroke-width="1.4"></path>')
    return "".join(o)

def vines(x0, x1, y0, y1, seed, rows=4, wild=False, grapes=True):
    """Rows of vines on stakes across a slope from (x0, y0) to (x1, y1); wild=True: small dark wild grapes, leaves sparse."""
    r = random.Random(seed); o = []
    for k in range(rows):
        t = k / max(1, rows - 1)
        ya, yb = y0 + (y1 - y0) * t * 0.0 + t * 40, y1 + t * 40
        n = 9 + k * 2
        for i in range(n):
            u = i / (n - 1); x = x0 + (x1 - x0) * u; y = y0 + (y1 - y0) * u + t * 46 + k * 4
            sc = 0.6 + t * 0.5
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 22 * sc)}" stroke="#5A3A22" stroke-width="{f(2.4 * sc)}"></path>')
            lc = r.choice(["#3F8A44", "#2E6A32", "#5E8F26"]) if not wild else r.choice(["#5A6A2A", "#6A5A22", "#4A4A22"])
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y - 24 * sc)}" rx="{f(12 * sc)}" ry="{f(8 * sc)}" fill="{lc}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
            if grapes and r.random() < 0.6:
                gx, gy = x + r.uniform(-6, 6) * sc, y - 16 * sc
                col, rr = ("#5A1A6E", 2.6) if not wild else ("#2A1A1A", 1.6)
                for j in range(4):
                    o.append(f'<circle cx="{f(gx + (j % 2) * 3 * sc)}" cy="{f(gy + j * 2.4 * sc)}" r="{f(rr * sc + 0.6)}" fill="{col}"></circle>')
    return "".join(o)

# ---- Isaiah 1–5 ----------------------------------------------------------------------------------------------------------
def vineyard(p, w, h, seed, state="good"):
    """My wellbeloved had a vineyard in a very fruitful hill: the slope planted with the choicest vine, a tower in the midst,
    a winepress hewn out, a stone wall about it. state 'wild': the hedge taken away, the wall broken down, briers and thorns,
    wild grapes, no rain."""
    wild = state == "wild"
    o = [bg(w, h, "#8FD0E2" if not wild else "#A8A08A", "#F3E8C8" if not wild else "#C8B89A"),
         hills(w, h, h * 0.42, seed, color="#8AA06A" if not wild else "#9A8A6A", amp=10, step=80),
         f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.4)} {f(w + 10)} {f(h * 0.36)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" '
         f'fill="{"#7A9A4A" if not wild else "#8A7A4A"}" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(vines(w * 0.04, w * 0.96, h * 0.74, h * 0.46, seed, rows=4, wild=wild))
    o.append(tower(w * 0.62, h * 0.62, min(w * 0.08, h * 0.2), min(h * 0.34, w * 0.14), broken=wild))
    o.append(J1.winepress(w * 0.3, h * 0.9, min(w * 0.14, h * 0.36), min(h * 0.08, w * 0.04)))
    # the wall of stones along the foot of the hill
    seg_ = 26
    for i in range(int(w / seg_) + 1):
        if wild and (i % 5 in (2, 3)): continue
        o.append(f'<rect x="{f(i * seg_)}" y="{f(h * 0.94 - 10)}" width="{seg_ - 2}" height="12" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    if wild:
        o.append(thorns(0, w, h * 0.96, seed, n=int(w / 28), s=min(1.2, h / 260)))
        o.append(thorns(w * 0.1, w * 0.9, h * 0.66, seed + 1, n=int(w / 50), s=min(0.8, h / 380)))
    return "".join(o)

def heavens_earth(p, w, h, seed):
    """Hear, O heavens, and give ear, O earth: the hills of Judah under a wide sky; the ox at his owner's crib, the ass at
    his master's."""
    b = h * 0.92
    o = [bg(w, h, "#3A5A9A", "#F3E0B0"), V.rays(w * 0.5, -h * 0.2, 30, 20, max(w, h) * 1.4, color="#FFF4C2", op=0.2),
         hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=12, step=70), hills(w, h, h * 0.62, seed + 1, color="#A8A070", amp=8, step=90), ground(w, h, h * 0.76, "#C8A86A", dy=0)]
    s = min(0.9, h / 360)
    cx = w * 0.58
    o.append(f'<path d="M{f(cx - 60 * s)} {f(b - 40 * s)} L {f(cx + 60 * s)} {f(b - 40 * s)} L {f(cx + 48 * s)} {f(b - 14 * s)} L {f(cx - 48 * s)} {f(b - 14 * s)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(cx - 44 * s)} {f(b - 14 * s)} L {f(cx - 44 * s)} {f(b)} M{f(cx + 44 * s)} {f(b - 14 * s)} L {f(cx + 44 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>'
             f'<path d="M{f(cx - 50 * s)} {f(b - 42 * s)} C {f(cx - 20 * s)} {f(b - 56 * s)} {f(cx + 20 * s)} {f(b - 54 * s)} {f(cx + 50 * s)} {f(b - 42 * s)}" stroke="#D8B860" stroke-width="{f(6 * s)}" fill="none"></path>')
    o.append(S1.cow(cx - 70 * s, b, s * 0.9, color="#8A5A30", patch="#E8D8B0"))
    o.append(N.ass(cx + 150 * s, b, s * 0.85, flip=True))
    return "".join(o)

def booth(p, w, h, seed):
    """Your country is desolate; your cities are burned with fire: smoke over far hills, and the daughter of Zion left as a
    booth in a vineyard, a lodge in a garden of cucumbers."""
    r = random.Random(seed)
    o = [bg(w, h, "#6A5A6A", "#E8C8A0"), hills(w, h, h * 0.46, seed, color="#8A7A6A", amp=12, step=70)]
    for i, x in enumerate((0.16, 0.42, 0.82)):
        cx, cy = w * x, h * 0.46
        o.append(f'<path d="M{f(cx - 24)} {f(cy)} L {f(cx - 24)} {f(cy - 14)} L {f(cx - 12)} {f(cy - 8)} L {f(cx - 4)} {f(cy - 18)} L {f(cx + 10)} {f(cy - 10)} L {f(cx + 22)} {f(cy - 16)} L {f(cx + 24)} {f(cy)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="1.6"></path>')
        o.append(smoke(cx, cy - 16, 7, seed + i, r0=min(10, h * 0.04), color="#4A4048", op=0.6))
    o.append(ground(w, h, h * 0.62, "#B8A070", dy=0))
    for k in range(4):
        y = h * (0.7 + k * 0.08)
        for i in range(14):
            x = w * (0.04 + i * 0.07) + (k % 2) * 12
            o.append(f'<path d="M{f(x - 10)} {f(y)} C {f(x - 4)} {f(y - 6)} {f(x + 4)} {f(y - 6)} {f(x + 10)} {f(y)}" stroke="#4E7A3A" stroke-width="2.4" fill="none"></path>'
                     f'<ellipse cx="{f(x + 2)}" cy="{f(y - 1)}" rx="5" ry="2.6" fill="#7AA040" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    s = min(1.0, h / 300); x, b = w * 0.66, h * 0.82
    o.append(f'<path d="M{f(x - 50 * s)} {f(b)} L {f(x - 50 * s)} {f(b - 50 * s)} L {f(x + 50 * s)} {f(b - 50 * s)} L {f(x + 50 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(5 * s)}" fill="none"></path>'
             f'<path d="M{f(x - 64 * s)} {f(b - 48 * s)} L {f(x)} {f(b - 84 * s)} L {f(x + 64 * s)} {f(b - 48 * s)} Z" fill="#8A7A3A" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(x - 60 * s + i * 12 * s)} {f(b - 50 * s)} L {f(x - 52 * s + i * 10 * s)} {f(b - 70 * s)}" stroke="#5A6A2A" stroke-width="2"></path>' for i in range(10)))
    return "".join(o)

def altar_refused(p, w, h, seed):
    """To what purpose is the multitude of your sacrifices?: the altar in the court heaped with burnt-offerings, its smoke
    blown down and dark; the new moon over the house; the people spreading forth their hands."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#2A2040", "#8A5A6A"), J.moon(w * 0.84, h * 0.18, min(18, h * 0.08)),
         ground(w, h, h * 0.72, "#8A7A6A", dy=0)]
    o.append(K1.temple_front(w * 0.24, h * 0.72, w * 0.32, seed))
    o.append(smoke(w * 0.56, h * 0.66, 9, seed, r0=min(12, h * 0.05), spread=30, color="#3A3040", op=0.75, rise=0.5))
    o.append(horned_altar(w * 0.56, h * 0.86, min(0.8, h / 380), fire=True, seed=seed))
    s = fit(b, max(h * 0.5, b - 180))
    for i in range(5):
        x = w * (0.72 + i * 0.06)
        o.append((man if i % 2 == 0 else woman)(p, x, b - (i % 2) * 4, s * (0.9 + (i % 3) * 0.05), ["#5A4A6A", "#6A3A2A", "#3A4A6A", "#7A5A3A", "#4A5A4A"][i], flip=True,
                                                 up=[(-22, -158), (-36, -186), (-30, -214)]))
    return "".join(o)

def scarlet_snow(w, h, seed):
    """Though your sins be as scarlet, they shall be as white as snow; though they be red like crimson, they shall be as
    wool: a split plate, scarlet cloth on the left, snow and wool on the right."""
    o = [rect(w, h, "#F3EFE6"),
         f'<path d="M-10 -10 L {f(w * 0.56)} -10 L {f(w * 0.44)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B5121B"></path>',
         f'<path d="M-10 -10 L {f(w * 0.56)} -10 L {f(w * 0.44)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="url(#ss{seed})" opacity="0.5"></path>',
         f'<defs><linearGradient id="ss{seed}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF4A3A"></stop><stop offset="1" stop-color="#5A0A10"></stop></linearGradient></defs>']
    for i in range(7):
        y = h * (0.12 + i * 0.13)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.14)} {f(y - 18)} {f(w * 0.3)} {f(y + 18)} {f(w * 0.5 - i * 0.017 * w)} {f(y - 6)}" stroke="#7A0A12" stroke-width="3" fill="none" opacity="0.7"></path>')
    r = random.Random(seed)
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.95)} L {f(w * 0.7)} {f(h * 0.42)} L {f(w * 0.8)} {f(h * 0.56)} L {f(w * 0.9)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#E8F0F8" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for _ in range(14):
        x = r.uniform(w * 0.56, w * 0.98); y = r.uniform(h * 0.66, h * 0.92)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(10, 20) * min(1, h / 300))}" fill="#FFFFFF" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    for _ in range(40):
        o.append(f'<circle cx="{f(r.uniform(w * 0.5, w))}" cy="{f(r.uniform(0, h * 0.6))}" r="{f(r.uniform(1.4, 3))}" fill="#FFFFFF" stroke="#8FA8C8" stroke-width="0.6"></circle>')
    o.append(label(w * 0.2, h * 0.9, "SCARLET · CRIMSON", "#F3EFE6", 11) + label(w * 0.8, h * 0.2, "SNOW · WOOL", "#0B1A2E", 11))
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.6)} {f(h * 0.5)}" stroke="#0D0D0F" stroke-width="4"></path><path d="M{f(w * 0.6)} {f(h * 0.5 - 10)} L {f(w * 0.64)} {f(h * 0.5)} L {f(w * 0.6)} {f(h * 0.5 + 10)} Z" fill="#0D0D0F"></path>')
    return "".join(o)

def refiner(w, h, seed):
    """I will thoroughly purge away thy dross: a crucible in the furnace, the dross skimmed off, the silver bright (a plate)."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.62; s = min(1.2, h / 260)
    o.append(E.blaze(cx, h * 0.98, 160 * s, 70 * s, seed, n=8))
    o.append(f'<path d="M{f(cx - 70 * s)} {f(cy - 30 * s)} L {f(cx + 70 * s)} {f(cy - 30 * s)} L {f(cx + 52 * s)} {f(cy + 40 * s)} L {f(cx - 52 * s)} {f(cy + 40 * s)} Z" fill="#6A6A72" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - 30 * s)}" rx="{f(70 * s)}" ry="{f(12 * s)}" fill="#E8ECF4" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(cx + 24 * s)}" cy="{f(cy - 32 * s)}" rx="{f(22 * s)}" ry="{f(5 * s)}" fill="#5A4A3A"></ellipse>')
    o.append(route([(cx + 40 * s, cy - 40 * s), (w * 0.82, h * 0.24)], color="#FF8A6A") + label(w * 0.84, h * 0.2, "THE DROSS · THE TIN", "#FF8A6A", 10)
             + route([(cx - 40 * s, cy - 40 * s), (w * 0.18, h * 0.24)], color=GOLD) + label(w * 0.16, h * 0.2, "SILVER", GOLD, 10))
    return "".join(o)

def faded_oak(w, h, seed):
    """Ye shall be as an oak whose leaf fadeth, and as a garden that hath no water; the strong as tow, his work as a spark."""
    r = random.Random(seed)
    o = [bg(w, h, "#C8A880", "#F3D8A0"), ground(w, h, h * 0.8, "#B8986A", dy=0)]
    s = min(1.1, h / 280)
    o.append(f'<g transform="translate({f(w * 0.3)} {f(h * 0.84)}) scale({f(s)})"><path d="M-14 0 C -10 -60 -16 -110 -30 -150 L -10 -150 C 0 -120 6 -110 14 -150 L 30 -150 C 16 -110 12 -60 16 0 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<circle cx="{f(r.uniform(-70, 70))}" cy="{f(r.uniform(-230, -150))}" r="{f(r.uniform(26, 44))}" fill="{r.choice(["#A8783A", "#8A6A2A", "#C8984A"])}" stroke="#0D0D0F" stroke-width="2"></circle>' for _ in range(10))
             + '</g>')
    for _ in range(12):
        x = r.uniform(w * 0.1, w * 0.5); y = r.uniform(h * 0.6, h * 0.95)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="5" ry="2.6" fill="#A8783A" transform="rotate({r.randint(0, 180)} {f(x)} {f(y)})"></ellipse>')
    for i in range(7):
        x = w * (0.58 + i * 0.055)
        o.append(f'<path d="M{f(x)} {f(h * 0.86)} C {f(x - 6)} {f(h * 0.78)} {f(x + 6)} {f(h * 0.74)} {f(x)} {f(h * 0.68)}" stroke="#8A7A4A" stroke-width="2.4" fill="none"></path>'
                 f'<path d="M{f(x)} {f(h * 0.7)} l -8 4 M{f(x)} {f(h * 0.74)} l 8 3" stroke="#8A7A4A" stroke-width="1.8"></path>')
    for k in range(5):
        x0 = w * 0.55
        o.append(f'<path d="M{f(x0 + k * 30)} {f(h * 0.92)} l {f(26)} {f(-4)}" stroke="#2A1E1A" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.9)} q {f(w * 0.08)} {f(-14)} {f(w * 0.2)} 0" stroke="#5A4A3A" stroke-width="2" fill="none"></path>'
             f'<path d="M{f(w * 0.9)} {f(h * 0.6)} L {f(w * 0.92)} {f(h * 0.56)} L {f(w * 0.94)} {f(h * 0.6)} L {f(w * 0.92)} {f(h * 0.64)} Z" fill="#FFD23F" stroke="#D7261E" stroke-width="1.4"></path>')
    return "".join(o)

def mountain_house(p, w, h, seed):
    """The mountain of Jehovah's house established on the top of the mountains, exalted above the hills, and all nations
    flowing unto it: light on the summit, streams of people climbing from every side."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(w, h, "#5A7ABA", "#FFE8B0"), V.rays(w * 0.5, h * 0.12, 36, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.3),
         hills(w, h, h * 0.66, seed, color="#8A9A7A", amp=10, step=60),
         f'<path d="M{f(w * 0.08)} {f(h + 10)} L {f(w * 0.42)} {f(h * 0.22)} L {f(w * 0.5)} {f(h * 0.18)} L {f(w * 0.58)} {f(h * 0.22)} L {f(w * 0.92)} {f(h + 10)} Z" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="2.6"></path>',
         f'<path d="M{f(w * 0.42)} {f(h * 0.22)} L {f(w * 0.5)} {f(h * 0.18)} L {f(w * 0.58)} {f(h * 0.22)} L {f(w * 0.66)} {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.38)} Z" fill="#C8A87A" opacity="0.8"></path>']
    s = min(1.0, h / 380)
    o.append(K1.temple_front(w * 0.5, h * 0.2, min(w * 0.16, h * 0.4), seed))
    for side in (-1, 1):
        pts = [(w * 0.5 + side * w * (0.46 - k * 0.05), h * (0.98 - k * 0.12)) for k in range(7)]
        o.append(f'<path d="M{" L ".join(f"{f(x)} {f(y)}" for x, y in pts)}" stroke="#E8D8A8" stroke-width="{f(6 * s + 2)}" fill="none" stroke-linejoin="round"></path>')
        for k, (x, y) in enumerate(pts[:-1]):
            for j in range(3):
                t = (j + 1) / 4; xx = x + (pts[k + 1][0] - x) * t; yy = y + (pts[k + 1][1] - y) * t
                sc = (0.1 + 0.24 * (1 - k / 7)) * s * 1.2
                o.append((man if (k + j) % 2 else woman)(p, xx, yy, sc, r.choice(["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#7A6A2A", "#C2456A"]), flip=side > 0))
    return "".join(o)

def plowshares(w, h):
    """They shall beat their swords into plowshares, and their spears into pruning-hooks (a plate)."""
    o = [grid_bg(w, h)]
    s = min(1.0, h / 220); y1, y2 = h * 0.32, h * 0.72
    o.append(f'<path d="M{f(w * 0.06)} {f(y1)} L {f(w * 0.3)} {f(y1)} L {f(w * 0.33)} {f(y1 + 5)} L {f(w * 0.3)} {f(y1 + 10)} L {f(w * 0.06)} {f(y1 + 10)} Z" fill="#C8D0D8" stroke="#8FD0E2" stroke-width="1.6"></path>'
             f'<rect x="{f(w * 0.03)}" y="{f(y1 - 8)}" width="8" height="26" fill="#8FD0E2"></rect>')
    o.append(f'<path d="M{f(w * 0.04)} {f(y2 + 4)} L {f(w * 0.28)} {f(y2 + 4)}" stroke="#B87333" stroke-width="5"></path><path d="M{f(w * 0.28)} {f(y2 - 4)} L {f(w * 0.35)} {f(y2 + 4)} L {f(w * 0.28)} {f(y2 + 12)} Z" fill="#C8D0D8" stroke="#8FD0E2" stroke-width="1.6"></path>')
    o.append(route([(w * 0.4, y1 + 5), (w * 0.58, y1 + 5)], color=GOLD) + route([(w * 0.4, y2 + 4), (w * 0.58, y2 + 4)], color=GOLD))
    o.append(f'<path d="M{f(w * 0.66)} {f(y1 - 14 * s)} C {f(w * 0.74)} {f(y1 - 20 * s)} {f(w * 0.8)} {f(y1 + 6 * s)} {f(w * 0.86)} {f(y1 + 22 * s)} L {f(w * 0.8)} {f(y1 + 22 * s)} C {f(w * 0.76)} {f(y1 + 8 * s)} {f(w * 0.72)} {f(y1)} {f(w * 0.66)} {f(y1)} Z" fill="#C8D0D8" stroke="#FFD23F" stroke-width="1.8"></path>'
             f'<path d="M{f(w * 0.66)} {f(y1 - 6)} L {f(w * 0.94)} {f(y1 - 40 * s)}" stroke="#B87333" stroke-width="6"></path>')
    o.append(f'<path d="M{f(w * 0.64)} {f(y2 + 4)} L {f(w * 0.9)} {f(y2 + 4)}" stroke="#B87333" stroke-width="5"></path>'
             f'<path d="M{f(w * 0.9)} {f(y2 + 4)} C {f(w * 0.95)} {f(y2 - 6)} {f(w * 0.95)} {f(y2 + 22)} {f(w * 0.91)} {f(y2 + 22)}" stroke="#C8D0D8" stroke-width="5" fill="none"></path>')
    o.append(label(w * 0.18, y1 - 18, "SWORDS", CYAN, 10) + label(w * 0.8, y1 - 26 * s - 8, "PLOWSHARES", GOLD, 10)
             + label(w * 0.18, y2 - 14, "SPEARS", CYAN, 10) + label(w * 0.8, y2 - 14, "PRUNING-HOOKS", GOLD, 10))
    return "".join(o)

def lofty(w, h, seed):
    """A day of Jehovah upon all that is lifted up: the cedars of Lebanon, the oaks of Bashan, the high mountains, the lofty
    tower and the fortified wall, the ships of Tarshish — under a storm, lightning striking."""
    o = [bg(w, h, "#1A1830", "#5A4A6A"), f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.12)} {f(h * 0.2)} L {f(w * 0.24)} {f(h * 0.5)} L {f(w * 0.32)} {f(h * 0.3)} L {f(w * 0.44)} {f(h * 0.7)} Z" fill="#3A3448" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.7, "#3A3A30", dy=0)]
    s = min(0.8, h / 380)
    for i in range(4):
        x = w * (0.04 + i * 0.07); y = h * 0.74
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 120 * s)}" stroke="#3A2A1A" stroke-width="{f(5 * s)}"></path>'
                 + "".join(f'<path d="M{f(x - (40 - k * 8) * s)} {f(y - (30 + k * 22) * s)} L {f(x)} {f(y - (50 + k * 22) * s)} L {f(x + (40 - k * 8) * s)} {f(y - (30 + k * 22) * s)} Z" fill="#1F3A2A" stroke="#0D0D0F" stroke-width="1.4"></path>' for k in range(4)))
    o.append(tower(w * 0.56, h * 0.72, w * 0.08, h * 0.44, color="#6A6050"))
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.58)}" width="{f(w * 0.14)}" height="{f(h * 0.14)}" fill="#5A5444" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.74)} {f(h * 0.72)} L {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.74)} {f(h + 10)} Z" fill="#1F3A5A"></path>')
    o.append(K1.ship(w * 0.88, h * 0.78, min(0.7, h / 420)))
    o.append(E2.bolt(w * 0.3, 0, h * 0.5, seed) + E2.bolt(w * 0.86, 0, h * 0.5, seed + 1))
    return "".join(o)

def caves(p, w, h, seed):
    """Men going into the caves of the rocks and the holes of the earth; their idols of silver and gold cast away to the
    moles and to the bats."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(w, h, "#3A2A2A", "#8A5A4A"),
         f'<path d="M-10 {f(h * 0.1)} L {f(w * 0.3)} {f(h * 0.04)} L {f(w * 0.7)} {f(h * 0.12)} L {f(w + 10)} {f(h * 0.06)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.0, h / 320)
    holes = [(0.14, 0.4), (0.38, 0.3), (0.62, 0.46), (0.86, 0.32)]
    for i, (x, y) in enumerate(holes):
        cx, cy = w * x, h * y; rw, rh = 50 * s, 40 * s
        o.append(f'<path d="M{f(cx - rw)} {f(cy + rh)} C {f(cx - rw)} {f(cy - rh)} {f(cx + rw)} {f(cy - rh)} {f(cx + rw)} {f(cy + rh)} Z" fill="#1A1010" stroke="#0D0D0F" stroke-width="2"></path>')
        o.append(E.kneel(cx - 10 * s, cy + rh, 0.26 * s, color="#3A2A2A", flip=i % 2 == 1))
    gy = h * 0.88
    for i in range(5):
        x = w * (0.2 + i * 0.14)
        col = "#E8B830" if i % 2 else "#C8C8D0"
        o.append(f'<g transform="rotate({r.choice([-70, 80, -100, 95])} {f(x)} {f(gy)})"><rect x="{f(x - 7 * s)}" y="{f(gy - 30 * s)}" width="{f(14 * s)}" height="{f(30 * s)}" fill="{col}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(gy - 36 * s)}" r="{f(7 * s)}" fill="{col}" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')
    for i in range(6):
        x = r.uniform(w * 0.1, w * 0.9); y = r.uniform(h * 0.6, h * 0.76); sc = r.uniform(0.6, 1.0) * s
        o.append(f'<path d="M{f(x)} {f(y)} q {f(-8 * sc)} {f(-8 * sc)} {f(-18 * sc)} {f(-2 * sc)} q {f(4 * sc)} {f(4 * sc)} {f(2 * sc)} {f(8 * sc)} q {f(8 * sc)} {f(-4 * sc)} {f(16 * sc)} {f(-6 * sc)} '
                 f'q {f(8 * sc)} {f(2 * sc)} {f(16 * sc)} {f(6 * sc)} q {f(-2 * sc)} {f(-4 * sc)} {f(2 * sc)} {f(-8 * sc)} q {f(-10 * sc)} {f(-6 * sc)} {f(-18 * sc)} {f(2 * sc)} Z" fill="#1A1010"></path>')
    return "".join(o)

def full_land(w, h, seed):
    """Their land is full of silver and gold, full of horses and chariots, full of idols: three cells of a plate."""
    o = [grid_bg(w, h)]
    s = min(1.5, h / 170)
    cw = w / 3
    for i, name in enumerate(("SILVER AND GOLD", "HORSES · CHARIOTS", "IDOLS")):
        x0 = i * cw
        o.append(f'<rect x="{f(x0 + 10)}" y="{f(h * 0.08)}" width="{f(cw - 20)}" height="{f(h * 0.84)}" fill="none" stroke="#4A7A9A" stroke-width="1.6"></rect>' + label(x0 + cw / 2, h * 0.08 + 16, name, GOLD, 10))
    cx = cw / 2; b = h * 0.84
    for k in range(4):
        for j in range(4 - k):
            col = "#E8B830" if (j + k) % 2 else "#C8C8D0"
            o.append(f'<path d="M{f(cx - 60 * s + j * 30 * s + k * 15 * s)} {f(b - k * 16 * s)} l {f(26 * s)} 0 l {f(-4 * s)} {f(-14 * s)} l {f(-18 * s)} 0 Z" fill="{col}" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(E3.horse(cw * 1.42, b, 0.5 * s, color="#5A3A22") + E3.chariot(cw * 1.62, b, 0.42 * s, color="#8A5A2A"))
    for j in range(3):
        x = cw * 2 + cw * (0.28 + j * 0.22); col = ["#E8B830", "#C8C8D0", "#8A6A4A"][j]
        o.append(f'<rect x="{f(x - 10 * s)}" y="{f(b - 70 * s)}" width="{f(20 * s)}" height="{f(56 * s)}" rx="{f(6 * s)}" fill="{col}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(b - 80 * s)}" r="{f(11 * s)}" fill="{col}" stroke="#0D0D0F" stroke-width="1.6"></circle>'
                 f'<rect x="{f(x - 16 * s)}" y="{f(b - 14 * s)}" width="{f(32 * s)}" height="{f(14 * s)}" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def stay_staff(w, h, seed):
    """The whole stay of bread, and the whole stay of water taken away: an empty basket, a cracked water-jar, a staff laid down."""
    o = [bg(w, h, "#5A4A3A", "#C8A070"), ground(w, h, h * 0.7, "#8A6A4A", dy=0)]
    s = min(1.2, h / 220); b = h * 0.86
    o.append(f'<path d="M{f(w * 0.2 - 50 * s)} {f(b - 40 * s)} L {f(w * 0.2 + 50 * s)} {f(b - 40 * s)} L {f(w * 0.2 + 40 * s)} {f(b)} L {f(w * 0.2 - 40 * s)} {f(b)} Z" fill="#B8904A" stroke="#0D0D0F" stroke-width="2.2"></path>'
             + "".join(f'<path d="M{f(w * 0.2 - 46 * s)} {f(b - (32 - k * 9) * s)} L {f(w * 0.2 + 46 * s)} {f(b - (32 - k * 9) * s)}" stroke="#7A5A2A" stroke-width="1.6"></path>' for k in range(4)))
    cx = w * 0.5
    o.append(f'<path d="M{f(cx - 16 * s)} {f(b - 90 * s)} L {f(cx + 16 * s)} {f(b - 90 * s)} L {f(cx + 12 * s)} {f(b - 78 * s)} C {f(cx + 44 * s)} {f(b - 60 * s)} {f(cx + 40 * s)} {f(b - 10 * s)} {f(cx + 16 * s)} {f(b)} L {f(cx - 16 * s)} {f(b)} C {f(cx - 40 * s)} {f(b - 10 * s)} {f(cx - 44 * s)} {f(b - 60 * s)} {f(cx - 12 * s)} {f(b - 78 * s)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(cx + 4 * s)} {f(b - 70 * s)} L {f(cx - 6 * s)} {f(b - 44 * s)} L {f(cx + 8 * s)} {f(b - 30 * s)} L {f(cx)} {f(b - 6 * s)}" stroke="#0D0D0F" stroke-width="2.2" fill="none"></path>'
             f'<path d="M{f(cx + 30 * s)} {f(b)} C {f(cx + 50 * s)} {f(b + 2)} {f(cx + 70 * s)} {f(b - 2)} {f(cx + 90 * s)} {f(b + 1)}" stroke="#4A3A2A" stroke-width="2" fill="none" opacity="0.6"></path>')
    o.append(f'<path d="M{f(w * 0.62)} {f(b - 4)} L {f(w * 0.95)} {f(b - 14 * s)}" stroke="#5A3A22" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.95)} {f(b - 14 * s)} c {f(10 * s)} {f(-4 * s)} {f(14 * s)} {f(-16 * s)} {f(4 * s)} {f(-18 * s)}" stroke="#5A3A22" stroke-width="{f(6 * s)}" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

ORN = ["ANKLETS", "CAULS", "CRESCENTS", "PENDANTS", "BRACELETS", "MUFFLERS", "HEADTIRES", "ANKLE CHAINS", "SASHES", "PERFUME-BOXES", "AMULETS",
       "RINGS", "NOSE-JEWELS", "FESTIVAL ROBES", "MANTLES", "SHAWLS", "SATCHELS", "HAND-MIRRORS", "FINE LINEN", "TURBANS", "VEILS"]
def _orn(i, x, y, s):
    g = "#FFD23F"; c = "#8FD0E2"
    k = i % 7
    if k == 0: return f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(14 * s)}" ry="{f(8 * s)}" fill="none" stroke="{g}" stroke-width="3"></ellipse>'
    if k == 1: return f'<path d="M{f(x - 14 * s)} {f(y + 6 * s)} C {f(x - 14 * s)} {f(y - 14 * s)} {f(x + 14 * s)} {f(y - 14 * s)} {f(x + 14 * s)} {f(y + 6 * s)} Z" fill="none" stroke="{c}" stroke-width="2"></path>'
    if k == 2: return f'<path d="M{f(x - 8 * s)} {f(y - 12 * s)} A {f(13 * s)} {f(13 * s)} 0 1 0 {f(x - 8 * s)} {f(y + 12 * s)} A {f(9 * s)} {f(9 * s)} 0 1 1 {f(x - 8 * s)} {f(y - 12 * s)} Z" fill="{g}"></path>'
    if k == 3: return f'<path d="M{f(x)} {f(y - 14 * s)} L {f(x)} {f(y - 2 * s)}" stroke="{g}" stroke-width="2"></path><path d="M{f(x)} {f(y - 2 * s)} C {f(x + 8 * s)} {f(y + 6 * s)} {f(x)} {f(y + 14 * s)} {f(x)} {f(y + 14 * s)} C {f(x)} {f(y + 14 * s)} {f(x - 8 * s)} {f(y + 6 * s)} {f(x)} {f(y - 2 * s)} Z" fill="{c}"></path>'
    if k == 4: return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(12 * s)}" fill="none" stroke="{g}" stroke-width="4" stroke-dasharray="4 2"></circle>'
    if k == 5: return f'<path d="M{f(x - 14 * s)} {f(y - 8 * s)} L {f(x + 14 * s)} {f(y - 8 * s)} L {f(x + 10 * s)} {f(y + 10 * s)} L {f(x - 10 * s)} {f(y + 10 * s)} Z" fill="none" stroke="{c}" stroke-width="2"></path>'
    return f'<path d="M{f(x)} {f(y - 13 * s)} L {f(x + 10 * s)} {f(y)} L {f(x)} {f(y + 13 * s)} L {f(x - 10 * s)} {f(y)} Z" fill="{g}" stroke="#0D0D0F" stroke-width="1"></path>'

def ornaments(w, h):
    """The Lord will take away the beauty of their anklets …: every ornament of Isaiah 3:18–23 on a plate, one cell each."""
    o = [grid_bg(w, h)]
    cols = 7; rows = 3
    cw, ch = w / cols, h / rows
    s = min(1.0, ch / 90)
    for i, nm in enumerate(ORN):
        r_, c_ = divmod(i, cols)
        x0, y0 = c_ * cw, r_ * ch
        o.append(f'<rect x="{f(x0 + 4)}" y="{f(y0 + 4)}" width="{f(cw - 8)}" height="{f(ch - 8)}" fill="#12203A" stroke="#4A7A9A" stroke-width="1.2"></rect>')
        o.append(_orn(i, x0 + cw / 2, y0 + ch * 0.42, s) + label(x0 + cw / 2, y0 + ch - 12, nm, CYAN, max(7, min(9, cw / 11))))
        o.append(f'<path d="M{f(x0 + 10)} {f(y0 + ch - 8)} L {f(x0 + cw - 10)} {f(y0 + 10)}" stroke="#D7261E" stroke-width="1.4" opacity="0.6"></path>')
    return "".join(o)

def gate_mourns(p, w, h, seed):
    """Her gates shall lament and mourn; and she shall be desolate and sit upon the ground: an empty gate, a woman in
    sackcloth sitting in the dust before it."""
    o = [bg(w, h, "#4A4A5A", "#A8A0A0"), ground(w, h, h * 0.8, "#8A7A6A", dy=0)]
    o.append(S4.gatehouse(w * 0.5, h * 0.8, min(w * 0.5, h * 1.2), h * 0.66))
    o.append(E.kneel(w * 0.3, h * 0.94, fit(h * 0.94, h * 0.6) * 0.8, color="#5A5040", skin="#8A5A3A"))
    o.append(smoke(w * 0.85, h * 0.3, 6, seed, r0=10, color="#6A6070", op=0.5))
    return "".join(o)

def seven_women(p, w, h, seed):
    """Seven women taking hold of one man in that day: a street of the city, the seven about him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8A7A8A", "#E8D8C0"), J.city_hill(w * 0.5, h * 0.6, w * 0.7, h * 0.3, seed), ground(w, h, h * 0.62, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.5, b - 150))
    cols = ["#7A3A5A", "#5A4A7A", "#8A5A3A", "#3A5A6A", "#6A3A3A", "#7A6A3A", "#4A5A3A"]
    o.append(man(p, w * 0.5, b, s, "#4A4A5A"))
    for i in range(7):
        side = -1 if i < 4 else 1
        x = w * 0.5 + side * w * (0.08 + (i % 4) * 0.08)
        o.append(woman(p, x, b - (i % 2) * 6, s * 0.92, cols[i], flip=side > 0, up=[(-22, -158), (-34, -150), (-48, -146)] if i in (0, 4) else None))
    return "".join(o)

def zion_canopy(p, w, h, seed):
    """Over the whole habitation of mount Zion a cloud and smoke by day, and the shining of a flaming fire by night; a
    pavilion for a shade: the city split between day and night."""
    o = [f'<defs><clipPath id="zd{seed}"><rect x="-10" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}"></rect></clipPath>'
         f'<clipPath id="zn{seed}"><rect x="{f(w / 2)}" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}"></rect></clipPath></defs>']
    city = J.city_hill(w * 0.5, h * 0.96, w * 0.56, h * 0.5, seed) + K1.temple_front(w * 0.5, h * 0.56, min(w * 0.18, h * 0.5), seed)
    o.append(f'<g clip-path="url(#zd{seed})">{bg(w, h, "#8FD0E2", "#F3E8C8")}{city}{E3.pillar_cloud(w * 0.3, h * 0.5, -10, w * 0.12, seed)}</g>')
    o.append(f'<g clip-path="url(#zn{seed})">{rect(w, h, "#0B0B2A")}{mk.stars(30, w, h * 0.5, seed)}{city}<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A" opacity="0.45"></rect>'
             f'{E3.pillar_fire(w * 0.7, h * 0.5, -10, w * 0.1, seed)}</g>')
    o.append(f'<path d="M{f(w / 2)} -10 L {f(w / 2)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="3"></path>')
    return "".join(o)

def empty_houses(w, h, seed):
    """Woe unto them that join house to house: great and fair houses side by side without inhabitant, their windows dark,
    the fields about them bare."""
    r = random.Random(seed)
    o = [bg(w, h, "#8A8AA0", "#E8D8B8"), ground(w, h, h * 0.84, "#A89A70", dy=0)]
    x = -10
    while x < w:
        bw = r.uniform(70, 120); bh = r.uniform(h * 0.32, h * 0.6)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.84 - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{r.choice(["#D8C8A8", "#C8B898", "#E0D0B0"])}" stroke="#0D0D0F" stroke-width="2"></rect>')
        for k in range(int(bh / 40)):
            for j in range(int(bw / 34)):
                o.append(f'<rect x="{f(x + 10 + j * 32)}" y="{f(h * 0.84 - bh + 12 + k * 38)}" width="12" height="18" fill="#1A1414"></rect>')
        x += bw
    return "".join(o)

def feast(p, w, h, seed):
    """The harp and the lute, the tabret and the pipe, and wine, are in their feasts: a table by lamplight, cups and a
    wine-jar, the instruments laid on the board — late into the night."""
    from genesis.art4 import clay_lamp
    o = [rect(w, h, "#2A1428"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(max(w, h) * 0.5)}" fill="#8A4A2A" opacity="0.35"></circle>']
    s = min(1.2, h / 240); b = h * 0.86
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(b - 30 * s)}" width="{f(w * 0.76)}" height="{f(16 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.16)}" y="{f(b - 14 * s)}" width="{f(10 * s)}" height="{f(h - b + 14 * s)}" fill="#5A3A1E"></rect><rect x="{f(w * 0.82)}" y="{f(b - 14 * s)}" width="{f(10 * s)}" height="{f(h - b + 14 * s)}" fill="#5A3A1E"></rect>')
    top = b - 30 * s
    o.append(S2.harp(w * 0.24, top, 0.5 * s) + S3.timbrel(w * 0.38, top - 10 * s, 0.6 * s))
    for i in range(4):
        x = w * (0.48 + i * 0.07)
        o.append(f'<path d="M{f(x - 8 * s)} {f(top - 20 * s)} L {f(x + 8 * s)} {f(top - 20 * s)} L {f(x + 3 * s)} {f(top - 6 * s)} L {f(x + 3 * s)} {f(top)} L {f(x - 3 * s)} {f(top)} L {f(x - 3 * s)} {f(top - 6 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(top - 19 * s)}" rx="{f(7 * s)}" ry="{f(2 * s)}" fill="#7A0A2A"></ellipse>')
    o.append(f'<path d="M{f(w * 0.8)} {f(top)} C {f(w * 0.76)} {f(top - 30 * s)} {f(w * 0.77)} {f(top - 60 * s)} {f(w * 0.79)} {f(top - 70 * s)} L {f(w * 0.83)} {f(top - 70 * s)} C {f(w * 0.85)} {f(top - 60 * s)} {f(w * 0.86)} {f(top - 30 * s)} {f(w * 0.82)} {f(top)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.6)} {f(top - 4)} L {f(w * 0.72)} {f(top - 14 * s)}" stroke="#C8A06A" stroke-width="{f(4 * s)}" stroke-linecap="round"></path>')
    o.append(clay_lamp(w * 0.1, top, 0.8 * s) + mk.stars(20, w, h * 0.3, seed))
    return "".join(o)

def stubble_fire(w, h, seed):
    """As the tongue of fire devoureth the stubble, and as the dry grass sinketh down in the flame."""
    r = random.Random(seed)
    o = [bg(w, h, "#3A1A1A", "#C8582A"), ground(w, h, h * 0.66, "#C8A060", dy=0)]
    for _ in range(int(w / 8)):
        x = r.uniform(0, w); y = r.uniform(h * 0.7, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-3, 3))} -10" stroke="#8A6A3A" stroke-width="1.6"></path>')
    for i in range(6):
        o.append(E.blaze(w * (0.08 + i * 0.17), h * 0.8 + (i % 2) * 8, w * 0.14, h * 0.4, seed + i, n=6))
    o.append(smoke(w * 0.5, h * 0.4, 6, seed, r0=h * 0.06, spread=w * 0.3, color="#2A1A1A", op=0.5, rise=0.6))
    return "".join(o)

def ensign(p, w, h, seed, sea=False):
    """He will lift up an ensign to the nations from far: a standard on a bare hill, and from the end of the earth a host
    coming with speed, horses' hoofs as flint, wheels as a whirlwind (sea=True: darkness and the roaring of the sea)."""
    o = [mk.defs(p, *ALL), bg(w, h, "#3A2A3A" if sea else "#C8A880", "#C87A4A" if sea else "#F3D8A0"), hills(w, h, h * 0.62, seed, color="#8A6A4A", amp=8)]
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.7)} Z" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.2)} {f(h * 0.06)}" stroke="#3A2A1A" stroke-width="4"></path>'
             f'<path d="M{f(w * 0.2)} {f(h * 0.06)} C {f(w * 0.26)} {f(h * 0.04)} {f(w * 0.3)} {f(h * 0.1)} {f(w * 0.36)} {f(h * 0.08)} L {f(w * 0.36)} {f(h * 0.18)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.26)} {f(h * 0.14)} {f(w * 0.2)} {f(h * 0.16)} Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.72, "#B89A6A", dy=0))
    s = min(0.5, h / 600)
    for i in range(5):
        x = w * (0.52 + i * 0.1); y = h * (0.8 + (i % 2) * 0.06)
        o.append(E3.chariot(x, y, s * (0.8 + i * 0.06), color="#3A2A1A", driver="#2A1A10"))
    o.append(f'<ellipse cx="{f(w * 0.98)}" cy="{f(h * 0.82)}" rx="{f(w * 0.2)}" ry="{f(h * 0.12)}" fill="#C8A87A" opacity="0.6"></ellipse>')
    if sea:
        o.append(f'<path d="M-10 {f(h * 0.94)} C {f(w * 0.2)} {f(h * 0.86)} {f(w * 0.3)} {f(h * 0.98)} {f(w * 0.5)} {f(h * 0.9)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F3A5A" stroke="#E8F6FA" stroke-width="2"></path>'
                 f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#0B0B1A" opacity="0.5"></rect>')
    return "".join(o)

# ---- Isaiah 6: the vision -------------------------------------------------------------------------------------------------
def wing(x, y, ang, L, wd, color="#FFF4C2", edge="#FF8A3D", n=7, mirror=False):
    """A broad feathered wing from its root (x, y), pointing at angle ang (degrees): a curved leading edge, then a row of
    long flight feathers back to the root, and a band of coverts. mirror=True puts the feathers on the other side."""
    m = -1 if mirror else 1
    lead = [(L * t, -m * wd * 0.55 * math.sin(math.pi * min(1, t * 1.1))) for t in [i / 10 for i in range(11)]]
    d = "M0 0 " + " ".join(f"L {f(px)} {f(py)}" for px, py in lead[1:])
    feath = []
    for i in range(n):
        t0 = 1 - i / n; t1 = 1 - (i + 1) / n
        x0, y0 = L * t0, m * wd * (0.15 + 0.7 * (1 - t0) ** 0.6) * (0.4 if i == 0 else 1)
        x1, y1 = L * t1, m * wd * (0.15 + 0.7 * (1 - t1) ** 0.6)
        tipx, tipy = (x0 + x1) / 2 + L * 0.04, max(y0, y1, key=abs) + m * wd * 0.35
        d += f" Q {f(tipx)} {f(tipy)} {f(x1)} {f(y1)}"
        feath.append(f'<path d="M{f(x1 + (x0 - x1) * 0.3)} {f(y1 * 0.3)} L {f(tipx - L * 0.02)} {f(tipy - m * wd * 0.12)}" stroke="{edge}" stroke-width="1.4" opacity="0.8"></path>')
    d += " Z"
    cov = "M0 0 " + " ".join(f"L {f(px)} {f(py * 0.6 + m * wd * 0.05)}" for px, py in lead[1:8]) + f" Q {f(L * 0.4)} {f(m * wd * 0.35)} 0 {f(m * wd * 0.12)} Z"
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(ang)})"><path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            + "".join(feath) + f'<path d="{cov}" fill="#FFFFFF" opacity="0.55"></path></g>')

def seraph(x, y, s, flip=False):
    """A seraph: a burning figure of light with six wings — with twain he covered his face, with twain he covered his feet,
    and with twain he did fly. (x, y) = the middle of the figure; about 260 units tall at s=1. No face is drawn: the upper
    wings cross before it."""
    sx = -1 if flip else 1
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s * sx)} {f(s)})">',
         '<circle cx="0" cy="-10" r="120" fill="#FFD23F" opacity="0.18"></circle><circle cx="0" cy="-10" r="70" fill="#FFF4C2" opacity="0.25"></circle>']
    o.append(wing(10, -40, -18, 170, 46, color="#FFF4C2") + wing(-10, -40, 198, 170, 46, color="#FFF4C2", mirror=True))   # twain did fly
    o.append('<path d="M0 -96 C 22 -70 26 0 18 84 L -18 84 C -26 0 -22 -70 0 -96 Z" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M0 -80 C 14 -50 16 10 8 74 L -8 74 C -16 10 -14 -50 0 -80 Z" fill="#FFD23F"></path>'
             '<path d="M0 -60 C 6 -30 7 10 3 60 L -3 60 C -7 10 -6 -30 0 -60 Z" fill="#FFF4C2"></path>'
             '<circle cx="0" cy="-104" r="16" fill="#FFC14D" stroke="#0D0D0F" stroke-width="2"></circle>')
    o.append(wing(14, 40, 104, 96, 30, color="#FFC14D", mirror=True) + wing(-14, 40, 76, 96, 30, color="#FFC14D"))         # twain covered his feet
    o.append(wing(14, -70, -118, 86, 30, color="#FFE680") + wing(-14, -70, -62, 86, 30, color="#FFE680", mirror=True))     # twain covered his face
    o.append('</g>')
    return "".join(o)

def throne_vision(p, w, h, seed, coal=False):
    """I saw the Lord sitting upon a throne, high and lifted up, and his train filled the temple: the temple in light,
    the throne lifted up in blinding glory (no one drawn), the train as falling folds of gold light, seraphim above,
    the house filled with smoke and the posts of the door shaking. coal=True: one seraph flying with the live coal."""
    r = random.Random(seed)
    o = [rect(w, h, "#14123A"), V.rays(w * 0.5, h * 0.18, 48, 20, max(w, h) * 1.3, color="#FFD23F", op=0.22),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.18)}" r="{f(min(w, h) * 0.16)}" fill="#FFF4C2" opacity="0.8"></circle>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.18)}" r="{f(min(w, h) * 0.09)}" fill="#FFFFFF"></circle>']
    # the posts of the door
    for x in (0.06, 0.94):
        o.append(f'<rect x="{f(w * x - w * 0.035)}" y="-10" width="{f(w * 0.07)}" height="{f(h + 20)}" fill="#3A3058" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 + "".join(f'<path d="M{f(w * x - w * 0.035)} {f(h * t)} l {f(w * 0.015)} {f(h * 0.015)} l {f(-w * 0.004)} {f(h * 0.02)} l {f(w * 0.018)} {f(h * 0.015)} l {f(-w * 0.006)} {f(h * 0.02)}" stroke="#0D0D0F" stroke-width="1.6" fill="none"></path>'
                           f'<path d="M{f(w * x - w * 0.045)} {f(h * t - 6)} l -8 -4 M{f(w * x + w * 0.045)} {f(h * t + 4)} l 8 -3" stroke="#FFD23F" stroke-width="2"></path>' for t in (0.3, 0.55, 0.8)))
    # the throne lifted up, on a high stepped dais, all but lost in the light
    ts = min(1.4, h / 300)
    for k in range(5):
        dw = w * (0.08 + k * 0.04); y0 = h * (0.36 + k * 0.035)
        o.append(f'<rect x="{f(w * 0.5 - dw)}" y="{f(y0)}" width="{f(dw * 2)}" height="{f(h * 0.035)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    o.append(S3.throne(w * 0.5, h * 0.36, ts * 0.8))
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.26)}" r="{f(min(w, h) * 0.13)}" fill="#FFFFFF" opacity="0.7"></circle>')
    # the train: folds of light falling from the throne to the floor of the temple
    for i in range(9):
        x0 = w * 0.5 + (i - 4) * w * 0.012; x1 = w * 0.5 + (i - 4) * w * 0.1
        o.append(f'<path d="M{f(x0)} {f(h * 0.36)} C {f(x0)} {f(h * 0.6)} {f(x1)} {f(h * 0.7)} {f(x1)} {f(h + 10)}" stroke="{["#FFD23F", "#FFC14D", "#FFE680"][i % 3]}" stroke-width="{f(w * 0.03)}" fill="none" opacity="0.5"></path>')
    # smoke filling the house
    for _ in range(26):
        x = r.choice([r.uniform(-20, w * 0.3), r.uniform(w * 0.7, w + 20)]); y = r.uniform(h * 0.3, h + 20)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(0.06, 0.12) * max(w, h) * 0.5)}" fill="#8A7AA8" opacity="0.35"></circle>')
    ss = min(0.9, h / 520)
    o.append(seraph(w * 0.24, h * 0.3, ss) + seraph(w * 0.76, h * 0.3, ss, flip=True))
    if coal:
        o.append(seraph(w * 0.62, h * 0.66, ss * 0.8, flip=True))
    return "".join(o)

def live_coal(p, w, h, seed):
    """Then flew one of the seraphim unto me, having a live coal in his hand, taken with the tongs from off the altar: the
    altar's fire, the seraph flying, the coal glowing, the prophet bowed (his lips touched; nothing more drawn)."""
    o = [rect(w, h, "#1A1438"), V.rays(w * 0.2, h * 0.7, 30, 20, max(w, h), color="#FF8A3D", op=0.2)]
    o.append(horned_altar(w * 0.18, h * 0.96, min(0.9, h / 320), fire=True, seed=seed))
    ss = min(0.8, h / 420)
    o.append(seraph(w * 0.5, h * 0.42, ss, flip=True))
    cx, cy = w * 0.62, h * 0.5
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.44)} L {f(cx)} {f(cy)}" stroke="#5A5A6A" stroke-width="4"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.47)} L {f(cx)} {f(cy + 4)}" stroke="#5A5A6A" stroke-width="4"></path>'
             f'<circle cx="{f(cx + 6)}" cy="{f(cy + 2)}" r="{f(18 * ss)}" fill="#FF6A2A" opacity="0.5"></circle><circle cx="{f(cx + 6)}" cy="{f(cy + 2)}" r="{f(9 * ss)}" fill="#FFD23F" stroke="#D7261E" stroke-width="2"></circle>')
    o.append(E.kneel(w * 0.8, h * 0.96, fit(h * 0.96, h * 0.42) * 0.9, color="#4A3A6A", skin="#B98A6E", flip=True))
    return "".join(o)
