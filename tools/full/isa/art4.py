"""Isaiah 13–16 drawings (on top of isa.art3): the burden of Babylon (the darkened sun, the Medes far off, Babylon's ruins
with the beasts of the desert), the day-star fallen, Sheol's empty thrones, the burden of Philistia (the fiery flying serpent
as a plate), the burden of Moab (a map of its towns, mourners on the housetops, the vine of Sibmah)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art3 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
import snake as SN

def ziggurat(cx, base, wd, ht, color="#B8865A", broken=0.0, seed=1):
    """A stepped temple-tower of Babylon: five stages and a stair; broken (0–1) knocks the upper stages away."""
    r = random.Random(seed); o = []
    for k in range(5):
        if broken and k >= 5 - int(broken * 4) - 1 and k > 1: break
        ww = wd * (1 - k * 0.17); hh = ht / 5
        y = base - (k + 1) * hh
        jag = "".join(f" L {f(cx - ww / 2 + i * ww / 6)} {f(y + (r.uniform(0, hh * 0.5) if broken and k > 0 else 0))}" for i in range(7))
        o.append(f'<path d="M{f(cx - ww / 2)} {f(base - k * hh)}{jag} L {f(cx + ww / 2)} {f(base - k * hh)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<path d="M{f(cx - wd * 0.06)} {f(base)} L {f(cx - wd * 0.03)} {f(base - ht * 0.6)} L {f(cx + wd * 0.03)} {f(base - ht * 0.6)} L {f(cx + wd * 0.06)} {f(base)} Z" fill="#8A5A3A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def dark_sun(p, w, h, seed):
    """The stars of heaven shall not give their light; the sun shall be darkened in its going forth, and the moon shall not
    cause its light to shine: a black sun with a thin ring of fire over Babylon's plain, people looking one at another."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#1A0A0A", "#6A2A1A"), f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.16)}" fill="#FF6A2A" opacity="0.5"></circle>',
         f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.14)}" fill="#0D0D0F"></circle>',
         f'<path d="M{f(w * 0.2)} {f(h * 0.22)} A {f(h * 0.06)} {f(h * 0.06)} 0 1 0 {f(w * 0.2)} {f(h * 0.34)}" fill="#3A2A2A" stroke="#5A4A4A" stroke-width="2"></path>',
         ground(w, h, h * 0.72, "#3A2018", dy=0), ziggurat(w * 0.2, h * 0.74, w * 0.2, h * 0.3, color="#5A3A2A", seed=seed)]
    s = fit(b, max(h * 0.55, b - 150))
    for i in range(4):
        o.append((man if i % 2 == 0 else woman)(p, w * (0.44 + i * 0.1), b, s * (1 - (i % 2) * 0.06), ["#5A3A3A", "#6A4A2A", "#4A3A4A", "#7A4A2A"][i], flip=i % 2 == 1))
    return "".join(o)

def scattered(w, h, seed):
    """As the chased roe, and as sheep that no man gathereth, they shall flee every man to his own land: sheep scattered
    across a plain under smoke, a roe leaping away."""
    r = random.Random(seed)
    o = [bg(w, h, "#5A4A5A", "#C8A080"), ground(w, h, h * 0.6, "#A88A60", dy=0), smoke(w * 0.1, h * 0.5, 8, seed, r0=h * 0.06, color="#3A3036", op=0.6)]
    s = min(0.6, h / 500)
    for _ in range(12):
        o.append(E.sheep(r.uniform(w * 0.2, w * 0.95), r.uniform(h * 0.66, h * 0.95), s * r.uniform(0.6, 1.0), flip=r.random() < 0.3))
    o.append(beast(w * 0.82, h * 0.7, s * 0.8, "wolf") if False else "")
    return "".join(o)

def medes(p, w, h, seed):
    """I will stir up the Medes against them, who shall not regard silver: a line of archers on a far ridge at dawn, bows
    bent, the plain of Babylon below."""
    o = [mk.defs(p, *ALL), bg(w, h, "#C86A3A", "#F3C890"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.36)} L {f(w * 0.7)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.7, "#B89A6A", dy=0), ziggurat(w * 0.16, h * 0.86, w * 0.16, h * 0.22, seed=seed)]
    s = min(0.4, h / 700)
    for i in range(10):
        x = w * (0.32 + i * 0.066); y = h * (0.38 + (i % 3) * 0.01)
        o.append(mk.person(p, round(x), round(y), round(s, 3), body="#1A1010", cloth="#2A1A1A", kind="Tunic", up=[(-22, -158), (-50, -160), (-74, -158)],
                           extra='<path d="M-74 -200 C -96 -170 -96 -140 -74 -116" stroke="#1A1010" stroke-width="5" fill="none"></path>'))
    return "".join(o)

def babylon_ruins(w, h, seed, pools=False):
    """Babylon, the glory of kingdoms, never inhabited: the broken temple-tower and fallen walls; ostriches, wild goats
    dancing on the rubble, jackals in the palaces (pools=True: pools of water and reeds, the porcupine, a broom laid on the stones)."""
    r = random.Random(seed)
    o = [bg(w, h, "#A87A5A", "#F3D8A0"), ground(w, h, h * 0.7, "#C8A070", dy=0), ziggurat(w * 0.66, h * 0.72, w * 0.36, h * 0.5, color="#B8865A", broken=0.6, seed=seed)]
    for i in range(8):
        x = w * (0.02 + i * 0.07); hh = h * r.uniform(0.08, 0.22)
        o.append(f'<path d="M{f(x)} {f(h * 0.74)} L {f(x)} {f(h * 0.74 - hh)} L {f(x + w * 0.03)} {f(h * 0.74 - hh * 0.7)} L {f(x + w * 0.065)} {f(h * 0.74 - hh * 0.9)} L {f(x + w * 0.065)} {f(h * 0.74)} Z" fill="#9A6A4A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for _ in range(14):
        x = r.uniform(0, w); y = r.uniform(h * 0.76, h * 0.96)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(r.uniform(10, 26))}" height="{f(r.uniform(6, 12))}" fill="#9A6A4A" stroke="#0D0D0F" stroke-width="1.2" transform="rotate({r.randint(-20, 20)} {f(x)} {f(y)})"></rect>')
    s = min(0.5, h / 560)
    if pools:
        o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.86)}" rx="{f(w * 0.16)}" ry="{f(h * 0.05)}" fill="#3A7A8A" stroke="#0D0D0F" stroke-width="2"></ellipse>' + E.reeds(w * 0.16, w * 0.44, h * 0.86, h * 0.16, 14, seed))
        o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.92)} L {f(w * 0.74)} {f(h * 0.86)}" stroke="#8A6A3A" stroke-width="4"></path>'
                 + "".join(f'<path d="M{f(w * 0.74)} {f(h * 0.86)} l {f(14 + k * 2)} {f(-8 + k * 4)}" stroke="#B89A4A" stroke-width="2"></path>' for k in range(5)))
        cx, cy = w * 0.86, h * 0.92
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy - 10 * s * 2)}" rx="{f(22 * s * 2)}" ry="{f(12 * s * 2)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 + "".join(f'<path d="M{f(cx + (k - 4) * 5 * s * 2)} {f(cy - 18 * s * 2)} l {f((k - 4) * 2 * s * 2)} {f(-16 * s * 2)}" stroke="#E8E2D6" stroke-width="1.6"></path>' for k in range(9)))
    else:
        for x, y in ((0.2, 0.88), (0.34, 0.84)):     # ostriches
            ox, oy = w * x, h * y; k = s * 2
            o.append(f'<ellipse cx="{f(ox)}" cy="{f(oy - 40 * k)}" rx="{f(24 * k)}" ry="{f(16 * k)}" fill="#1A1414" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
                     f'<path d="M{f(ox + 16 * k)} {f(oy - 48 * k)} C {f(ox + 22 * k)} {f(oy - 70 * k)} {f(ox + 18 * k)} {f(oy - 86 * k)} {f(ox + 26 * k)} {f(oy - 92 * k)}" stroke="#D8B8A0" stroke-width="{f(4 * k)}" fill="none"></path>'
                     f'<path d="M{f(ox - 6 * k)} {f(oy - 26 * k)} L {f(ox - 8 * k)} {f(oy)} M{f(ox + 6 * k)} {f(oy - 26 * k)} L {f(ox + 8 * k)} {f(oy)}" stroke="#D8B8A0" stroke-width="{f(3 * k)}"></path>')
        o.append(E.sheep(w * 0.52, h * 0.62, s * 0.8, wool="#8A6A4A", face="#3A2A1A") + E.sheep(w * 0.6, h * 0.5, s * 0.7, wool="#8A6A4A", face="#3A2A1A", flip=True))
        o.append(beast(w * 0.9, h * 0.9, s * 0.8, "wolf", flip=True))
    return "".join(o)

def day_star(w, h, seed, mount=False):
    """How art thou fallen from heaven, O day-star, son of the morning!: a bright star falling in a long streak from the top
    of the sky down to the ground at dawn (mount=True: the mount of congregation in the uttermost parts of the north, its
    peaks above the clouds, the star high over it)."""
    r = random.Random(seed)
    o = [bg(w, h, "#0B0B2A", "#C86A4A"), mk.stars(50, w, h * 0.6, seed)]
    if mount:
        o.append(f'<path d="M-10 {f(h + 10)} L {f(w * 0.3)} {f(h * 0.3)} L {f(w * 0.42)} {f(h * 0.42)} L {f(w * 0.56)} {f(h * 0.16)} L {f(w * 0.74)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2448" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(w * 0.52)} {f(h * 0.22)} L {f(w * 0.56)} {f(h * 0.16)} L {f(w * 0.6)} {f(h * 0.22)} Z" fill="#E8E8F8"></path>')
        for k in range(3):
            o.append(f'<ellipse cx="{f(w * (0.2 + k * 0.3))}" cy="{f(h * (0.6 + k * 0.05))}" rx="{f(w * 0.18)}" ry="{f(h * 0.05)}" fill="#E8D8E0" opacity="0.6"></ellipse>')
        o.append(N.star(w * 0.56, h * 0.08, min(w, h) * 0.05, color="#FFF4C2"))
    else:
        o.append(f'<path d="M{f(w * 0.86)} {f(-10)} L {f(w * 0.36)} {f(h * 0.82)}" stroke="#FFF4C2" stroke-width="{f(max(3, h * 0.02))}" opacity="0.5"></path>'
                 f'<path d="M{f(w * 0.7)} {f(h * 0.26)} L {f(w * 0.36)} {f(h * 0.82)}" stroke="#FFFFFF" stroke-width="{f(max(2, h * 0.01))}"></path>'
                 + N.star(w * 0.36, h * 0.82, min(w, h) * 0.06, color="#FFD23F"))
        o.append(ground(w, h, h * 0.86, "#2A1A1A", dy=0) + ziggurat(w * 0.12, h * 0.88, w * 0.14, h * 0.2, color="#3A2A2A", broken=0.6, seed=seed))
    return "".join(o)

def sheol_thrones(w, h, seed):
    """Sheol from beneath is moved for thee to meet thee; it hath raised up from their thrones all the kings of the nations:
    a dark vault under the earth, a row of stone thrones, pale shapes risen from them with dim crowns, no faces."""
    o = [rect(w, h, "#0A0812"), f'<path d="M-10 {f(h * 0.2)} Q {f(w * 0.5)} {f(-h * 0.2)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} -10 L -10 -10 Z" fill="#2A2026"></path>']
    n = 7; s = min(1.0, h / 300)
    for i in range(n):
        x = w * (0.08 + i * 0.84 / (n - 1)); b = h * 0.9
        o.append(f'<rect x="{f(x - 22 * s)}" y="{f(b - 60 * s)}" width="{f(44 * s)}" height="{f(60 * s)}" fill="#3A3440" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x - 22 * s)}" y="{f(b - 110 * s)}" width="{f(8 * s)}" height="{f(56 * s)}" fill="#3A3440" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        o.append(f'<path d="M{f(x - 12 * s)} {f(b - 60 * s)} C {f(x - 16 * s)} {f(b - 110 * s)} {f(x - 10 * s)} {f(b - 140 * s)} {f(x)} {f(b - 150 * s)} C {f(x + 10 * s)} {f(b - 140 * s)} {f(x + 16 * s)} {f(b - 110 * s)} {f(x + 12 * s)} {f(b - 60 * s)} Z" fill="#C8C8D8" opacity="0.35"></path>'
                 f'<path d="M{f(x - 8 * s)} {f(b - 150 * s)} L {f(x - 8 * s)} {f(b - 160 * s)} L {f(x - 3 * s)} {f(b - 154 * s)} L {f(x)} {f(b - 162 * s)} L {f(x + 3 * s)} {f(b - 154 * s)} L {f(x + 8 * s)} {f(b - 160 * s)} L {f(x + 8 * s)} {f(b - 150 * s)} Z" fill="#8A7A3A" opacity="0.6"></path>')
    o.append(ground(w, h, h * 0.9, "#1A1418", dy=0))
    return "".join(o)

def cast_out(w, h, seed):
    """Thou art cast forth away from thy sepulchre like an abominable branch: a royal sepulchre hewn in the rock standing open
    and empty, and on the stones before it a broken crown and a cast-off branch."""
    o = [bg(w, h, "#3A2A3A", "#A8887A"), f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.7)} {f(h * 0.26)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.2, h / 260); cx, b = w * 0.36, h * 0.8
    o.append(f'<path d="M{f(cx - 50 * s)} {f(b)} L {f(cx - 50 * s)} {f(b - 70 * s)} Q {f(cx)} {f(b - 110 * s)} {f(cx + 50 * s)} {f(b - 70 * s)} L {f(cx + 50 * s)} {f(b)} Z" fill="#1A1212" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 70 * s)}" y="{f(b - 130 * s)}" width="{f(140 * s)}" height="{f(16 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<circle cx="{f(cx + 90 * s)}" cy="{f(b - 30 * s)}" r="{f(40 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></circle>')
    o.append(ground(w, h, h * 0.84, "#6A5A4A", dy=0))
    o.append(S2.crown(w * 0.62, h * 0.9, 0.8 * s, rot=24) + f'<path d="M{f(w * 0.7)} {f(h * 0.94)} L {f(w * 0.92)} {f(h * 0.88)}" stroke="#4A3A22" stroke-width="{f(4 * s)}"></path>'
             + "".join(f'<path d="M{f(w * (0.74 + k * 0.04))} {f(h * 0.93 - k * 2)} l {f(8 * s)} {f(-10 * s)}" stroke="#4A3A22" stroke-width="2"></path>' for k in range(4)))
    return "".join(o)

def serpents_root(w, h, seed):
    """Out of the serpent's root shall come forth an adder, and his fruit shall be a fiery flying serpent: three stages on a
    plate — the root, the adder, the fiery flying serpent."""
    o = [grid_bg(w, h)]
    s = min(1.0, h / 220); y = h * 0.62
    o.append(f'<path d="M{f(w * 0.1)} {f(y)} C {f(w * 0.12)} {f(y + 30 * s)} {f(w * 0.16)} {f(y + 40 * s)} {f(w * 0.2)} {f(y + 50 * s)} M{f(w * 0.14)} {f(y + 20 * s)} C {f(w * 0.1)} {f(y + 30 * s)} {f(w * 0.08)} {f(y + 44 * s)} {f(w * 0.06)} {f(y + 50 * s)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}" fill="none"></path>'
             f'<path d="M{f(w * 0.06)} {f(y)} L {f(w * 0.22)} {f(y)}" stroke="#4A7A9A" stroke-width="1.6"></path>')
    o.append(SN.snake([(w * 0.36, y + 10 * s), (w * 0.42, y - 10 * s), (w * 0.48, y + 10 * s), (w * 0.54, y - 6 * s)], 7 * s, f"sr{seed}a", head_scale=0.6))
    o.append(N.fiery([(w * 0.7, y + 20 * s), (w * 0.76, y - 10 * s), (w * 0.84, y), (w * 0.92, y - 40 * s)], 8 * s, f"sr{seed}b", head_scale=0.7))
    for side in (-1, 1):
        o.append(f'<path d="M{f(w * 0.8)} {f(y - 6 * s)} C {f(w * 0.8 + side * 20 * s)} {f(y - 50 * s)} {f(w * 0.8 + side * 50 * s)} {f(y - 60 * s)} {f(w * 0.8 + side * 60 * s)} {f(y - 40 * s)} C {f(w * 0.8 + side * 40 * s)} {f(y - 36 * s)} {f(w * 0.8 + side * 20 * s)} {f(y - 20 * s)} {f(w * 0.8)} {f(y - 6 * s)} Z" fill="#FF8A3D" stroke="#D7261E" stroke-width="1.6" opacity="0.8"></path>')
    o.append(route([(w * 0.24, y), (w * 0.32, y)], color=GOLD) + route([(w * 0.58, y), (w * 0.66, y)], color=GOLD))
    o.append(label(w * 0.14, y + 74 * s, "THE SERPENT'S ROOT", CYAN, 9) + label(w * 0.45, y + 74 * s, "AN ADDER", CYAN, 9) + label(w * 0.8, y + 74 * s, "A FIERY FLYING SERPENT", "#FF8A6A", 9))
    return "".join(o)

MOAB = [("AR", 0.36, 0.66), ("KIR", 0.5, 0.78), ("DIBON", 0.44, 0.5), ("NEBO", 0.34, 0.24), ("MEDEBA", 0.46, 0.32), ("HESHBON", 0.48, 0.18), ("ELEALEH", 0.58, 0.14),
        ("JAHAZ", 0.66, 0.44), ("ZOAR", 0.2, 0.92), ("LUHITH", 0.26, 0.82), ("HORONAIM", 0.36, 0.88), ("EGLAIM", 0.6, 0.62), ("BEER-ELIM", 0.78, 0.36), ("JAZER", 0.62, 0.06), ("SIBMAH", 0.42, 0.12)]
def moab_map(w, h, hi=()):
    """The burden of Moab as a technical map: the Dead Sea on the west, the Arnon cutting across, the towns of the lament from
    Heshbon and Elealeh down to Zoar, and the cry going round the borders to Eglaim and Beer-elim."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.06)} -10 C {f(w * 0.14)} {f(h * 0.3)} {f(w * 0.08)} {f(h * 0.6)} {f(w * 0.14)} {f(h * 0.86)} L {f(w * 0.2)} {f(h * 0.86)} C {f(w * 0.24)} {f(h * 0.6)} {f(w * 0.26)} {f(h * 0.3)} {f(w * 0.22)} -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.17, h * 0.46, "SALT SEA", "#4A8AAA", 8))
    o.append(f'<path d="M{f(w * 0.22)} {f(h * 0.56)} C {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.54)} {f(w * 0.86)} {f(h * 0.6)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>' + label(w * 0.8, h * 0.66, "THE ARNON", "#4A8AAA", 8))
    o.append(f'<path d="M{f(w * 0.3)} -10 L {f(w * 0.86)} {f(h * 0.2)} L {f(w * 0.9)} {f(h * 0.7)} L {f(w * 0.56)} {f(h * 0.98)} L {f(w * 0.24)} {f(h + 10)}" stroke="#FF8A6A" stroke-width="1.6" stroke-dasharray="6 6" fill="none"></path>')
    for nm, x, y in MOAB:
        o.append(node(w * x, h * y, nm, "#D7261E" if nm in hi else "#8FD0E2", r=5 if nm in hi else 4, dy=-10, size=8.5))
    return "".join(o)

def housetops(p, w, h, seed):
    """On their housetops, and in their broad places, every one waileth: the flat roofs of a Moabite town at dusk, figures
    in sackcloth on every roof, heads bowed and covered."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(w, h, "#4A3A5A", "#C88A6A")]
    x = -10; s = min(0.32, h / 700)
    while x < w:
        bw = r.uniform(80, 130); top = h * r.uniform(0.4, 0.6)
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(bw)}" height="{f(h - top + 10)}" fill="{r.choice(["#A88A6A", "#9A7A5A", "#B89A7A"])}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.3)}" y="{f(top + 30)}" width="14" height="20" fill="#2A1E1A"></rect>')
        for k in range(r.randint(1, 2)):
            o.append(E.kneel(x + bw * (0.3 + k * 0.4), top, s, color="#5A5040", skin="#5A5040", flip=r.random() < 0.5))
        x += bw
    return "".join(o)

def dimon(p, w, h, seed):
    """The waters of Dimon: a river at sunset, its waters dark red under a red sky, and on the far bank a lion standing."""
    o = [mk.defs(p, *ALL), bg(w, h, "#5A1A1A", "#E8784A"), hills(w, h, h * 0.5, seed, color="#5A3A3A", amp=10),
         f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.72)} {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h * 0.8)} C {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.3)} {f(h * 0.76)} -10 {f(h * 0.82)} Z" fill="#6A1418" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.86, "#5A3A2A", dy=0)]
    o.append(J2.lion(w * 0.74, h * 0.62, min(0.4, h / 640), roar=False, flip=True))
    return "".join(o)

def lambs_selah(p, w, h, seed):
    """Send ye the lambs for the ruler of the land from Selah to the wilderness, unto the mount of the daughter of Zion: a
    flock driven along the road from the rock-city toward Zion far off."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#C8A880", "#F3E0B0"), f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} L {f(w * 0.08)} {f(h * 0.2)} L {f(w * 0.2)} {f(h * 0.4)} L {f(w * 0.26)} {f(h + 10)} Z" fill="#B85A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         J.city_hill(w * 0.88, h * 0.56, w * 0.1, h * 0.14, seed), ground(w, h, h * 0.6, "#C8B080", dy=0)]
    s = min(0.5, h / 520)
    for i in range(10):
        o.append(E3.lamb(w * (0.3 + i * 0.05) + r.uniform(-10, 10), h * r.uniform(0.7, 0.9), s * r.uniform(0.8, 1.0)))
    o.append(man(p, w * 0.24, b, fit(b, max(h * 0.55, b - 150)), "#8A5A3A", up=[(-22, -158), (-10, -130), (16, -110)]))
    return "".join(o)

def arnon_fords(w, h, seed):
    """As wandering birds, as a scattered nest, so shall the daughters of Moab be at the fords of the Arnon: a river ford in a
    deep gorge, birds scattering up from it, an empty nest on the bank."""
    o = [bg(w, h, "#8FB0C8", "#E8D0A8"), f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9A5A3A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w + 10)} {f(h * 0.3)} L {f(w * 0.7)} {f(h * 0.5)} L {f(w * 0.7)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A4A2A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.86)} C {f(w * 0.45)} {f(h * 0.8)} {f(w * 0.55)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.84)} L {f(w * 0.7)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></path>']
    from genesis.art2 import birds
    o.append(birds(14, w * 0.3, w * 0.9, h * 0.1, h * 0.5, seed))
    o.append(f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.5)}" rx="{f(w * 0.04)}" ry="{f(h * 0.03)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def tent_throne(p, w, h, seed):
    """A throne shall be established in lovingkindness, in the tent of David: a royal tent at morning, its door open, a
    throne within and a lamp."""
    o = [bg(w, h, "#8FB0D8", "#F3E0B0"), ground(w, h, h * 0.74, "#C8B080", dy=0)]
    o.append(J1.tent_big(w * 0.5, h * 0.9, min(w * 0.5, h * 1.0), h * 0.6, color="#5A3A6A", stripe="#E8B830", open_=True, glow="#FFE680"))
    o.append(S3.throne(w * 0.5, h * 0.86, min(0.6, h / 500)))
    return "".join(o)

def sibmah(w, h, seed):
    """The fields of Heshbon languish, and the vine of Sibmah; its choice branches broken down; no treader shall tread out wine
    in the presses: broken vines trailing over the terraces toward the sea, an empty winepress, no one singing."""
    r = random.Random(seed)
    o = [bg(w, h, "#A88A6A", "#E8D0A8"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.4)} {f(h * 0.44)} L {f(w * 0.4)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C6A8A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.4)} {f(h * 0.44)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} Z" fill="#9A8A5A" stroke="#0D0D0F" stroke-width="2"></path>']
    for k in range(4):
        y = h * (0.52 + k * 0.12)
        o.append(f'<path d="M{f(w * 0.38 - k * 10)} {f(y)} L {f(w + 10)} {f(y - 10)}" stroke="#6A5A3A" stroke-width="3"></path>')
        x = w * 0.96
        d = f"M{f(x)} {f(y - 12)} " + " ".join(f"L {f(x - i * 40 - r.uniform(0, 12))} {f(y - 10 + r.uniform(-8, 8))}" for i in range(1, 10))
        o.append(f'<path d="{d}" stroke="#5A4A2A" stroke-width="3" fill="none"></path>')
        for i in range(6):
            o.append(f'<ellipse cx="{f(x - i * 60 - 20)}" cy="{f(y - 14)}" rx="8" ry="5" fill="#8A7A3A" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(J1.winepress(w * 0.74, h * 0.9, min(w * 0.18, h * 0.4), min(h * 0.1, w * 0.04)))
    return "".join(o)

def harp_lament(w, h, seed):
    """My heart soundeth like a harp for Moab: a harp alone, its strings sounding, against a darkening sky."""
    o = [bg(w, h, "#2A2040", "#8A5A6A"), V.rays(w * 0.5, h * 0.6, 24, 20, max(w, h), color="#E8C8F0", op=0.12)]
    o.append(S2.harp(w * 0.5, h * 0.92, min(1.6, h / 160)))
    o.append(S3.notes(w * 0.66, h * 0.4, 5, seed, color="#C8B8E8"))
    return "".join(o)

def cedars(w, h, seed):
    """The fir-trees rejoice at thee, and the cedars of Lebanon, saying, Since thou art laid low, no hewer is come up against
    us: the cedars standing tall and whole on the snowy mountains of Lebanon, at rest."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FB8E0", "#F3EFE0"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.6)} {f(h * 0.4)} L {f(w * 0.8)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A6A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.24)} {f(h * 0.18)} L {f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.36)} {f(h * 0.18)} Z M{f(w * 0.75)} {f(h * 0.26)} L {f(w * 0.8)} {f(h * 0.2)} L {f(w * 0.85)} {f(h * 0.26)} Z" fill="#F3EFE6"></path>',
         ground(w, h, h * 0.86, "#4A6A3A", dy=0)]
    s = min(1.0, h / 300)
    for i in range(9):
        x = w * (0.05 + i * 0.112) + r.uniform(-12, 12); y = h * (0.9 + (i % 2) * 0.04); k = s * r.uniform(0.8, 1.15)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 150 * k)}" stroke="#4A2E1A" stroke-width="{f(7 * k)}"></path>'
                 + "".join(f'<path d="M{f(x - (56 - j * 9) * k)} {f(y - (40 + j * 24) * k)} C {f(x - 20 * k)} {f(y - (52 + j * 24) * k)} {f(x + 20 * k)} {f(y - (52 + j * 24) * k)} {f(x + (56 - j * 9) * k)} {f(y - (40 + j * 24) * k)} L {f(x)} {f(y - (64 + j * 24) * k)} Z" fill="{["#1F4A34", "#2A5A3A", "#1F4A34", "#2E6A3E", "#1F4A34"][j]}" stroke="#0D0D0F" stroke-width="1.4"></path>' for j in range(5)))
    return "".join(o)
