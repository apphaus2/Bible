"""Drawings for Ezekiel 29–32: Pharaoh as the great monster lying in the midst of his rivers (a crocodile in the Nile, the
hooks in his jaws, the net spread over him); the staff of reed that broke; Egypt from Migdol to Syene as a map with her
cities; the land desolate, the pyramids standing over a dry river; the horn made to bud; the day of clouds; the ships to
Ethiopia; the arms of Pharaoh broken and the sword in the king of Babylon's hand (a plate — no wound drawn); the Assyrian
as a great cedar in Lebanon, then felled upon the mountains; the heavens covered and the stars made dark; and the pit with
the nations about it (a plate of graves round about, names only)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art10 import *
from ezk.art10 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1, SEA, SEA_D
import egypt as EG

NILE, NILE_D = "#2C7DA8", "#1A5A7A"

def croc(x, y, s=1.0, flip=False, hooks=False, fish=False):
    """The great monster that lieth in the midst of his rivers: a crocodile seen from the side, jaws a little open (hooks:
    hooks in the jaws with lines; fish: fish sticking to the scales)."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">',
         P("M-200 -6 C -150 -10 -100 -30 -40 -34 C 20 -38 70 -30 110 -22 L 190 -16 L 196 -8 L 120 -4 C 70 4 -20 8 -120 6 C -160 4 -190 2 -200 -6 Z", "#4A6A3A", 2.6),
         P("M110 -22 L 196 -26 L 200 -18 L 120 -14 Z", "#5A7A4A", 2),
         '<circle cx="104" cy="-34" r="7" fill="#C8C060" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="106" cy="-34" r="2.6" fill="#0D0D0F"></circle>']
    for i in range(12):
        bx = -120 + i * 18
        o.append(f'<path d="M{bx} -28 l 6 -10 l 6 10" fill="#3A5A2A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    for i in range(8):
        o.append(f'<path d="M{150 + i * 6} -18 l 2 6" stroke="#F3EFE6" stroke-width="2"></path>')
    o += [f'<path d="M{lx} 2 L {lx - 14} 22 L {lx - 2} 22" fill="none" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M{lx} 2 L {lx - 14} 22 L {lx - 2} 22" fill="none" stroke="#4A6A3A" stroke-width="4" stroke-linecap="round"></path>' for lx in (-60, 60)]
    if hooks:
        o.append('<path d="M170 -20 C 176 -6 190 -6 192 -18" fill="none" stroke="#C8C8D0" stroke-width="3"></path><path d="M182 -10 L 260 -120" stroke="#E8E2D6" stroke-width="1.6"></path>'
                 '<path d="M150 -12 C 154 0 166 0 168 -12" fill="none" stroke="#C8C8D0" stroke-width="3"></path><path d="M160 -2 L 240 -130" stroke="#E8E2D6" stroke-width="1.6"></path>')
    if fish:
        for i in range(6):
            fx = -110 + i * 34
            o.append(f'<path d="M{fx} -34 c 6 -8 18 -8 22 0 l 6 -5 l 0 10 l -6 -5 c -4 8 -16 8 -22 0 Z" fill="#9AB8C8" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o) + "</g>"

def nile_scene(w, h, seed, hooks=False, fish=False, net=False, desert=False):
    """The great monster in the midst of the Nile, the pyramids on the bank; hooks / fish / net spread over him; desert=True:
    cast forth into the wilderness, on the sand."""
    o = [bg(f"ns{seed}{hooks}{net}{desert}", w, h, [(0, "#E8A060" if not desert else "#C8803A"), (1, "#F3E0B0")])]
    o.append(EG.pyramid(w * 0.78, h * 0.5, w * 0.24, h * 0.24) + EG.pyramid(w * 0.92, h * 0.5, w * 0.14, h * 0.14))
    if desert:
        o.append(ground(w, h, h * 0.5, "#D8B07A", dy=0))
        o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.5)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.58)}" stroke="#B8905A" stroke-width="3" fill="none"></path>')
    else:
        o.append(f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#C8A86A" stroke="{INK}" stroke-width="2"></rect>')
        o.append(f'<rect x="-10" y="{f(h * 0.58)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="{NILE}" stroke="{INK}" stroke-width="2"></rect>' + waves(w, h * 0.68, seed, n=10) + waves(w, h * 0.9, seed + 1, n=10))
        o.append(E.reeds(-10, w * 0.25, h * 0.62, h * 0.12, 12, seed))
    k = min(w / 520, h / 160) * 0.9
    o.append(croc(w * 0.46, h * (0.8 if not desert else 0.84), k, hooks=hooks, fish=fish))
    if net:
        for i in range(-8, 9):
            o.append(f'<path d="M{f(w * 0.46 + i * w * 0.04)} {f(h * 0.56)} L {f(w * 0.46 + i * w * 0.04 + w * 0.12)} {f(h * 0.98)}" stroke="#E8E2D6" stroke-width="1.4" opacity="0.8"></path>'
                     f'<path d="M{f(w * 0.46 + i * w * 0.04)} {f(h * 0.56)} L {f(w * 0.46 + i * w * 0.04 - w * 0.12)} {f(h * 0.98)}" stroke="#E8E2D6" stroke-width="1.4" opacity="0.8"></path>')
    return "".join(o)

def reed_staff(w, h, seed):
    """A staff of reed to the house of Israel: a tall reed staff snapped in the middle, by the river."""
    o = [bg(f"rs{seed}", w, h, [(0, "#8AB0C8"), (1, "#F3E0B0")]), ground(w, h, h * 0.84, "#B8A07A", dy=0), E.reeds(-10, w + 10, h * 0.86, h * 0.14, 30, seed)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.86)} L {f(w * 0.44)} {f(h * 0.5)}" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M{f(w * 0.3)} {f(h * 0.86)} L {f(w * 0.44)} {f(h * 0.5)}" stroke="#C8B060" stroke-width="6" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.46)} {f(h * 0.5)} L {f(w * 0.68)} {f(h * 0.62)}" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M{f(w * 0.46)} {f(h * 0.5)} L {f(w * 0.68)} {f(h * 0.62)}" stroke="#C8B060" stroke-width="6" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.44)} {f(h * 0.5)} l -6 -10 m 8 6 l 4 -12 m 2 14 l 10 -6" stroke="#8A7A3A" stroke-width="2"></path>')
    return "".join(o)

EGYPT = {"MIGDOL": (0.62, 0.14), "TEHAPHNEHES": (0.56, 0.2), "PI-BESETH": (0.48, 0.22), "AVEN": (0.44, 0.3), "ZOAN": (0.52, 0.12), "SIN": (0.66, 0.08),
         "MEMPHIS": (0.42, 0.38), "PATHROS": (0.4, 0.6), "NO": (0.46, 0.72), "SYENE": (0.5, 0.88), "ETHIOPIA": (0.56, 0.98)}
def egypt_map(w, h, hi=()):
    """Egypt as a technical map, from Migdol to Syene even unto the border of Ethiopia: the Nile, its delta, its cities;
    those in hi lit (with fire where the word sets a fire)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h * 0.05)} C {f(w * 0.7)} {f(h * 0.06)} {f(w * 0.3)} {f(h * 0.04)} -10 {f(h * 0.06)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.2, h * 0.04, "THE GREAT SEA", "#8FD0E2", 8))
    o.append(f'<path d="M{f(w * 0.52)} {f(h + 10)} C {f(w * 0.48)} {f(h * 0.7)} {f(w * 0.42)} {f(h * 0.5)} {f(w * 0.44)} {f(h * 0.32)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>'
             f'<path d="M{f(w * 0.44)} {f(h * 0.32)} L {f(w * 0.34)} {f(h * 0.08)} M{f(w * 0.44)} {f(h * 0.32)} L {f(w * 0.6)} {f(h * 0.08)} M{f(w * 0.44)} {f(h * 0.32)} L {f(w * 0.46)} {f(h * 0.08)}" stroke="#2C9DB8" stroke-width="2.6"></path>')
    o.append(label(w * 0.36, h * 0.82, "THE RIVER", "#4A7A9A", 8, "end"))
    for nm, (x, y) in EGYPT.items():
        on = nm in hi
        o.append(node(w * x, h * y, nm, "#FFD23F" if on else "#4A7A9A", r=5 if on else 3, dy=-9, size=9 if on else 7, anchor="start" if x > 0.5 else "end"))
        if on: o.append(E.flame(w * x, h * y - 2, 6, 14, 0))
    return "".join(o)

def egypt_waste(w, h, seed):
    """The land of Egypt a desolation and a waste: the pyramids over an empty land, the river dried to a bed of cracked mud,
    no foot of man nor beast."""
    r = random.Random(seed)
    o = [bg(f"ew{seed}", w, h, [(0, "#C8803A"), (1, "#F3D8A0")]), sun(w * 0.2, h * 0.3, max(12, h * 0.06), color="#FFD23F", op=0.3)]
    o.append(EG.pyramid(w * 0.66, h * 0.62, w * 0.3, h * 0.3) + EG.pyramid(w * 0.86, h * 0.62, w * 0.2, h * 0.2))
    o.append(ground(w, h, h * 0.62, "#D8B07A", dy=0))
    o.append(f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h * 0.86)} C {f(w * 0.6)} {f(h * 0.92)} {f(w * 0.3)} {f(h * 0.82)} -10 {f(h * 0.86)} Z" fill="#9A7A5A" stroke="{INK}" stroke-width="2"></path>')
    o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(h * r.uniform(0.75, 0.85))} l {f(r.uniform(-14, 14))} {f(r.uniform(-4, 4))} l {f(r.uniform(-10, 10))} {f(r.uniform(2, 6))}" stroke="#5A4A3A" stroke-width="1.4" fill="none"></path>' for _ in range(24)))
    return "".join(o)

def horn_bud(w, h, seed):
    """I will cause a horn to bud forth unto the house of Israel: a ram's horn with green shoots springing from it, at dawn."""
    o = [bg(f"hb{seed}", w, h, [(0, "#3A4A7A"), (1, "#F8C890")]), V.rays(w * 0.5, h * 0.7, 20, h * 0.1, h * 0.8, color="#FFF4C2", op=0.2)]
    k = min(2.4, h / 120)
    o.append(J.shofar(w * 0.42, h * 0.74, k, rot=-30))
    for i in range(4):
        x = w * 0.42 + (30 + i * 10) * k * 0.6; y = h * 0.74 - (34 + i * 6) * k * 0.6
        o.append(f'<path d="M{f(x)} {f(y)} q {f(-4 * k)} {f(-14 * k)} {f(6 * k)} {f(-20 * k)}" stroke="#3A7A2A" stroke-width="{f(1.6 * k)}" fill="none"></path>'
                 f'<path d="M{f(x + 6 * k)} {f(y - 20 * k)} c {f(-8 * k)} {f(-2 * k)} {f(-8 * k)} {f(-12 * k)} 0 {f(-12 * k)} c {f(6 * k)} {f(4 * k)} {f(4 * k)} {f(10 * k)} 0 {f(12 * k)} Z" fill="#6AB04A" stroke="#0D0D0F" stroke-width="1"></path>')
    return "".join(o)

def day_clouds(w, h, seed):
    """The day of Jehovah is near, a day of clouds: dark clouds over the Nile and the pyramids, the sun hidden."""
    o = [bg(f"dc{seed}", w, h, [(0, "#1A1A2A"), (1, "#6A5A4A")]), EG.pyramid(w * 0.7, h * 0.7, w * 0.26, h * 0.26, lit="#8A7A5A", dark="#5A4A3A")]
    o.append(f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="{NILE_D}" stroke="{INK}" stroke-width="2"></rect>')
    o.append(clouds(w, h * 0.12, seed, n=9, color="#2A2A3A", op=0.95, ry=0.09) + clouds(w, h * 0.3, seed + 1, n=7, color="#3A3A4A", op=0.9, ry=0.07))
    o.append(bolts(w, h, seed, 1, 0.2, 0.6))
    return "".join(o)

def ships_ethiopia(w, h, seed):
    """Messengers shall go forth from before me in ships to make the careless Ethiopians afraid: ships going up the Nile."""
    o = [bg(f"se{seed}", w, h, [(0, "#C8803A"), (1, "#F3D8A0")]), hills(w, h, h * 0.5, seed, "#A8805A", amp=8, step=90)]
    o.append(f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="{NILE}" stroke="{INK}" stroke-width="2"></rect>' + waves(w, h * 0.72, seed, n=10))
    k = min(0.6, h / 360)
    for i in range(3): o.append(galley(w * (0.2 + i * 0.3), h * (0.78 + (i % 2) * 0.06), k * (1 - i * 0.1), sail="#E8D8A8"))
    o.append(S1.palm(w * 0.9, h * 0.6, h / 500) + S1.palm(w * 0.06, h * 0.6, h / 520))
    return "".join(o)

def arms_plate(w, h):
    """I have broken the arm of Pharaoh king of Egypt, and I will strengthen the arms of the king of Babylon and put my sword
    in his hand: a plate — Pharaoh's curved sword broken and his sceptre fallen; Babylon's sword held up, straight and whole."""
    o = [bp(w, h), title_bar(w, "THE ARMS OF PHARAOH SHALL FALL DOWN · THE ARMS OF THE KING OF BABYLON HELD UP")]
    k = min(1.4, h / 240)
    ex, ey = w * 0.28, h * 0.66
    o.append(f'<g transform="translate({f(ex)} {f(ey)}) rotate(28) scale({f(k)})"><path d="M-60 0 L 0 0 C 30 0 44 -20 40 -40 C 30 -30 20 -14 0 -10 L -60 -10 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="2"></path>'
             '<rect x="-90" y="-9" width="30" height="8" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect></g>')
    o.append(f'<path d="M{f(ex - 10)} {f(ey - 40 * k)} l 10 14 l -6 6 l 12 12" stroke="#D7261E" stroke-width="3" fill="none"></path>')
    o.append(f'<path d="M{f(ex - 60 * k)} {f(ey + 40 * k)} L {f(ex + 60 * k)} {f(ey + 30 * k)}" stroke="#E8B830" stroke-width="{f(5 * k)}"></path><path d="M{f(ex + 60 * k)} {f(ey + 30 * k)} c 10 -6 14 -18 6 -24" stroke="#E8B830" stroke-width="{f(5 * k)}" fill="none"></path>')
    o.append(label(ex, h * 0.95, "PHARAOH · BROKEN", "#FF8A6A", 9))
    bx = w * 0.72
    o.append(f'<path d="M{f(bx)} {f(h * 0.88)} L {f(bx)} {f(h * 0.2)}" stroke="#0D0D0F" stroke-width="{f(12 * k)}"></path><path d="M{f(bx)} {f(h * 0.88)} L {f(bx)} {f(h * 0.2)}" stroke="#D8E0F0" stroke-width="{f(8 * k)}"></path>'
             f'<rect x="{f(bx - 22 * k)}" y="{f(h * 0.74)}" width="{f(44 * k)}" height="{f(7 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(glow("apg", bx, h * 0.3, 30 * k, 60 * k, "#FFFFFF", 0.6, core="#FFFFFF"))
    o.append(label(bx, h * 0.95, "BABYLON · THE SWORD", "#FFD23F", 9))
    return "".join(o)

def great_cedar(w, h, seed, felled=False):
    """The Assyrian was a cedar in Lebanon with fair branches, his top among the thick boughs, birds nesting in its boughs
    and the beasts under its branches, the waters at its root (felled=True: cut off and left upon the mountains, its branches
    broken in all the watercourses)."""
    r = random.Random(seed)
    o = [bg(f"gc{seed}{felled}", w, h, [(0, "#5A9AD0" if not felled else "#5A5A6A"), (1, "#E8E0C8" if not felled else "#A89A8A")]), hills(w, h, h * 0.7, seed, "#6A8A5A" if not felled else "#6A6A5A", amp=14, step=70)]
    o.append(f'<path d="M-10 {f(h * 0.94)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.6)} {f(h * 0.98)} {f(w + 10)} {f(h * 0.92)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>')
    k = min(h / 300, 1.3)
    if felled:
        o.append(f'<g transform="rotate(84 {f(w * 0.3)} {f(h * 0.9)})">' + cedar_tree(w * 0.3, h * 0.9, k * 0.9) + '</g>')
        o.append(f'<rect x="{f(w * 0.3 - 12 * k)}" y="{f(h * 0.9 - 20 * k)}" width="{f(24 * k)}" height="{f(20 * k)}" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></rect>')
        for _ in range(6):
            x = r.uniform(0.5, 0.95) * w
            o.append(vine_branch(x, h * 0.9, x + r.uniform(-40, 40), h * 0.84, seed + _, sw=5))
    else:
        o.append(cedar_tree(w * 0.5, h * 0.94, k * 1.1))
        for _ in range(8):
            x = w * 0.5 + r.uniform(-120, 120) * k; y = h * 0.94 - r.uniform(70, 230) * k
            o.append(f'<path d="M{f(x - 8)} {f(y)} q 8 -8 16 0 q -8 -4 -16 0" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="1.2"></path>')
        o.append(E.sheep(w * 0.38, h * 0.96, 0.5 * k) + E.sheep(w * 0.62, h * 0.97, 0.5 * k, flip=True))
    return "".join(o)

def darkened(w, h, seed):
    """I will cover the heavens, and make the stars thereof dark; I will cover the sun with a cloud, and the moon shall not
    give its light: a black sky, the sun's disc behind cloud, the moon dark, over the Nile."""
    o = [bg(f"dk{seed}", w, h, [(0, "#05050A"), (1, "#1A1A2A")])]
    o.append(f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.12)}" fill="#3A2A1A" stroke="#8A5A2A" stroke-width="3"></circle>' + clouds(w, h * 0.32, seed, n=6, color="#0B0B12", op=0.95, ry=0.06))
    o.append(f'<circle cx="{f(w * 0.76)}" cy="{f(h * 0.24)}" r="{f(min(w, h) * 0.07)}" fill="#1A1A22" stroke="#4A4A5A" stroke-width="2"></circle>')
    o.append(EG.pyramid(w * 0.6, h * 0.76, w * 0.24, h * 0.24, lit="#2A2A30", dark="#1A1A20", line="#0D0D0F"))
    o.append(f'<rect x="-10" y="{f(h * 0.76)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#0B1A2A" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

PIT = [("ASSHUR", "#FF8A6A"), ("ELAM", "#FFC14D"), ("MESHECH · TUBAL", "#8FD0E2"), ("EDOM", "#C8A06A"), ("THE PRINCES OF THE NORTH", "#B8B8D8"), ("THE SIDONIANS", "#8FB8A8")]
def pit_plate(w, h, hi=None):
    """Go down, and be thou laid with the uncircumcised: the pit as a plate — the nations' graves set round about in the
    uttermost parts of the pit, each with its name (no one drawn); EGYPT going down in the midst."""
    o = [bp(w, h), title_bar(w, "THE NETHER PARTS OF THE EARTH · THEIR GRAVES ROUND ABOUT")]
    cx, cy = w * 0.5, h * 0.58; rx, ry = w * 0.33, h * 0.3
    for i in range(4):
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx * (1 - i * 0.22))}" ry="{f(ry * (1 - i * 0.22))}" fill="none" stroke="#4A7A9A" stroke-width="1.4" stroke-dasharray="5 4"></ellipse>')
    for i, (nm, c) in enumerate(PIT):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(PIT)
        x, y = cx + math.cos(a) * rx, cy + math.sin(a) * ry
        on = hi is None or nm in hi
        o.append("".join(f'<rect x="{f(x - 22 + j * 12)}" y="{f(y - 6)}" width="9" height="12" rx="2" fill="{c if on else "#2A3A4A"}" stroke="#0D0D0F" stroke-width="1"></rect>' for j in range(4)))
        o.append(label(x, y - 12 if y < cy else y + 22, nm, c if on else "#4A7A9A", 9 if on else 8))
    o.append(node(cx, cy, "EGYPT", "#FFD23F", r=6, dy=-12, size=10))
    return "".join(o)
