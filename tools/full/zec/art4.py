"""Drawings for Zechariah 12–14 (chapter 4 of the volume), on zec.art: Jerusalem a cup of reeling and a burdensome stone
amid the camps of the nations; horses in terror; a pan of fire among wood, a torch among sheaves; the tents of Judah; the
great mourning, every family apart, in the valley of Megiddon; a fountain opened; the idols cut off and the hairy mantle
laid aside; the shepherd smitten and the sheep scattered, the third refined as silver; the day of Jehovah: the mount of
Olives cleft east and west (light in the cleft, God never drawn), at evening time there shall be light, living waters to the
eastern and western seas, Jerusalem lifted up (a plan of her gates), the camps of the nations empty, the feast of
tabernacles, and the bells of the horses. Restraint: 13:3, 13:8, 14:2 and 14:12–15 are words over empty places."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from zec.art import *
from zec.art import f, vision, GOLD, CY, G
import numbers1 as N1

def camps_round(w, h, seed, stone=False):
    """Jerusalem a cup of reeling unto all the peoples round about (stone=True: a burdensome stone): the city on its hill
    ringed by the camps of the nations, a great cup (or stone) glowing over it."""
    o = [sky(w, h, "#2A1A3A", "#C8805A"), mount_zion(w * 0.5, h * 0.8, w * 0.22, h * 0.36, seed, color="#7A6A5A"), ground(w, h, h * 0.8, "#5A4030", dy=0)]
    r = random.Random(seed)
    for i in range(10):
        x = w * (0.04 + i * 0.1) + r.uniform(-8, 8); y = h * (0.86 + (i % 2) * 0.06)
        if abs(x - w * 0.5) < w * 0.16: continue
        o.append(A.black_tent(x, y, w * 0.08, h * 0.08, color="#2A2230", lit="#FF8A3D"))
    k = min(1.0, h / 300)
    if stone:
        o.append(f'<path d="M{f(w * 0.5 - 50 * k)} {f(h * 0.3)} L {f(w * 0.5 - 40 * k)} {f(h * 0.3 - 60 * k)} L {f(w * 0.5 + 44 * k)} {f(h * 0.3 - 64 * k)} L {f(w * 0.5 + 54 * k)} {f(h * 0.3)} Z" fill="#8A8478" stroke="{GOLD}" stroke-width="2.4"></path>'
                 + halo(w * 0.5, h * 0.26, 80 * k, "#FFE680", 0.4))
    else:
        o.append(halo(w * 0.5, h * 0.24, 80 * k, "#FFE680", 0.4) + cup(w * 0.5, h * 0.36, k * 0.8, color="#E8B830", spill=True))
    return "".join(o)

def terror(w, h, seed):
    """I will smite every horse with terror, and his rider with madness, and every horse of the peoples with blindness:
    horses rearing and scattering under a white flash, riderless."""
    o = [sky(w, h, "#F3EFE6", "#8A8AA0"), halo(w * 0.5, h * 0.2, h * 0.7, "#FFFFFF", 0.7), ground(w, h, h * 0.72, "#6A5A4A", dy=0)]
    k = min(0.8, h / 320)
    for i, (x, fl, rot) in enumerate(((0.2, False, -18), (0.5, True, 14), (0.8, False, -10))):
        o.append(f'<g transform="rotate({rot} {f(w * x)} {f(h * 0.9)})">{E3.horse(w * x, h * 0.9, k, color=["#3A2214", "#5A3A22", "#1A1210"][i], flip=fl)}</g>'
                 + mk.speed(w * x, h * 0.7, 8, 20 * k, 60 * k, seed + i, color="#0D0D0F", op=0.5))
    return "".join(o)

def pan_torch(w, h, seed):
    """I will make the chieftains of Judah like a pan of fire among wood, and like a flaming torch among sheaves: a brazier
    blazing in a woodpile, a torch thrown into sheaves of grain."""
    o = [sky(w, h, "#1A0A0A", "#6A2A1A"), ground(w, h, h * 0.7, "#3A2014", dy=0)]
    k = min(1.2, h / 260)
    for i in range(7):
        x = w * (0.06 + i * 0.05)
        o.append(f'<path d="M{f(x)} {f(h * 0.94)} L {f(x + w * 0.2)} {f(h * 0.86 - (i % 3) * 10)}" stroke="#6A4A2A" stroke-width="{f(10 * k)}" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.82)} L {f(w * 0.32)} {f(h * 0.82)} L {f(w * 0.28)} {f(h * 0.88)} L {f(w * 0.16)} {f(h * 0.88)} Z" fill="#3A3A44" stroke="#0D0D0F" stroke-width="2"></path>'
             + E.blaze(w * 0.22, h * 0.82, w * 0.22, h * 0.4, seed, n=6))
    for i in range(5):
        x = w * (0.56 + i * 0.09)
        o.append(f'<path d="M{f(x - 16)} {f(h * 0.94)} L {f(x - 6)} {f(h * 0.94 - 60 * k)} L {f(x + 6)} {f(h * 0.94 - 60 * k)} L {f(x + 16)} {f(h * 0.94)} Z" fill="#E8C060" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(E.blaze(w * 0.74, h * 0.9, w * 0.3, h * 0.4, seed + 3, n=6))
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.72)}" stroke="#8A5A30" stroke-width="{f(8 * k)}"></path>' + E.blaze(w * 0.62, h * 0.5, 30 * k, 50 * k, seed + 5, n=3))
    return "".join(o)

def tents_judah(w, h, seed):
    """Jehovah also shall save the tents of Judah first: tents of Judah in the open country at dawn, the walls of Jerusalem
    behind, a guarding light over them."""
    o = [sky(w, h, "#3A3A6A", "#FFC890"), halo(w * 0.5, h * 0.3, h * 0.5, "#FFF4C2", 0.4), walls(w * 0.5, w * 1.04, h * 0.5, h * 0.2, seed, towers=2),
         hills(w, h, h * 0.54, seed, color="#8A7A5A", amp=10), ground(w, h, h * 0.6, "#B8A070", dy=0)]
    for i in range(5):
        o.append(A.black_tent(w * (0.12 + i * 0.18), h * (0.86 + (i % 2) * 0.06), w * 0.14, h * 0.14, color="#4A3A2A"))
    return "".join(o)

def mourning(p, w, h, seed):
    """The land shall mourn, every family apart, and their wives apart, as the mourning of Hadadrimmon in the valley of
    Megiddon: small groups of mourners standing apart across the valley, heads covered, men and women apart."""
    o = [mk.defs(p, *ALL), sky(w, h, "#4A4A5A", "#B8A8A0"), hills(w, h, h * 0.42, seed, color="#5A5A5A", amp=20), ground(w, h, h * 0.5, "#7A7060", dy=0)]
    r = random.Random(seed)
    groups = [(0.1, 0.62, "man"), (0.28, 0.66, "woman"), (0.48, 0.6, "man"), (0.66, 0.64, "woman"), (0.84, 0.62, "man"),
              (0.18, 0.92, "woman"), (0.4, 0.96, "man"), (0.62, 0.94, "woman"), (0.84, 0.96, "man")]
    for gx, gy, kind in groups:
        b = h * gy; s = fit(b, b - h * (0.16 if gy < 0.8 else 0.26))
        for j in range(3):
            x = w * gx + (j - 1) * 14 * s * 3
            o.append((man if kind == "man" else woman)(p, x, b, s, "#3A3A44" if kind == "man" else "#4A3A4A", flip=j == 2)
                     + f'<path d="M{f(x - 15 * s)} {f(b - 190 * s)} C {f(x - 16 * s)} {f(b - 214 * s)} {f(x + 16 * s)} {f(b - 214 * s)} {f(x + 15 * s)} {f(b - 190 * s)} L {f(x + 19 * s)} {f(b - 150 * s)} L {f(x - 19 * s)} {f(b - 150 * s)} Z" fill="#2A2A32" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(label(w * 0.96, h * 0.08, "THE VALLEY OF MEGIDDON", "#F3EFE6", 9, anchor="end"))
    return "".join(o)

def fountain(w, h, seed):
    """In that day there shall be a fountain opened to the house of David and to the inhabitants of Jerusalem, for sin and for
    uncleanness: a spring of light breaking from the rock under the city wall, its water running clear."""
    o = [sky(w, h, "#2A3A6A", "#E8F6FA"), walls(-10, w + 10, h * 0.34, h * 0.24, seed, towers=3), f'<path d="M-10 {f(h * 0.34)} L {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>']
    cx, cy = w * 0.5, h * 0.5
    o.append(f'<path d="M{f(cx - 30)} {f(cy + 20)} Q {f(cx)} {f(cy - 30)} {f(cx + 30)} {f(cy + 20)} Z" fill="#1A1A2A" stroke="#0D0D0F" stroke-width="2"></path>' + halo(cx, cy, h * 0.3, "#E8F6FA", 0.7))
    o.append(f'<path d="M{f(cx - 20)} {f(cy + 18)} C {f(cx - 30)} {f(h * 0.7)} {f(cx - 80)} {f(h * 0.86)} {f(cx - 160)} {f(h + 10)} L {f(cx + 160)} {f(h + 10)} C {f(cx + 80)} {f(h * 0.86)} {f(cx + 30)} {f(h * 0.7)} {f(cx + 20)} {f(cy + 18)} Z" fill="#5AB8D8" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(cx + dx)} {f(cy + 30)} C {f(cx + dx * 1.5)} {f(h * 0.7)} {f(cx + dx * 3)} {f(h * 0.86)} {f(cx + dx * 6)} {f(h)}" stroke="#E8F6FA" stroke-width="2.4" fill="none"></path>' for dx in (-12, 0, 12)))
    return "".join(o)

def idols_mantle(w, h, seed):
    """I will cut off the names of the idols out of the land; the prophets shall be ashamed, neither shall they wear a hairy
    mantle to deceive — I am a tiller of the ground: broken idols in the dust, a hairy mantle cast down, a plow in the
    furrow."""
    o = [sky(w, h, "#8FB8D8", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=12), ground(w, h, h * 0.56, "#A88A5A", dy=0)]
    for k in range(5):
        y = h * (0.62 + k * 0.07)
        o.append(f'<path d="M{f(w * 0.5)} {f(y)} L {f(w + 10)} {f(y + 6)}" stroke="#6A4A2A" stroke-width="3"></path>')
    k = min(1.0, h / 280)
    o.append(f'<g transform="translate({f(w * 0.74)} {f(h * 0.72)}) scale({f(k)})"><path d="M-60 0 L 30 -10 L 70 -40" stroke="#6A4A2A" stroke-width="8" fill="none" stroke-linecap="round"></path><path d="M30 -10 L 44 14 L 20 10 Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.96)} C {f(w * 0.1)} {f(h * 0.82)} {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.36)} {f(h * 0.96)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(w * (0.1 + i * 0.025))} {f(h * 0.94)} l 4 -12" stroke="#3A2A1A" stroke-width="1.6"></path>' for i in range(10)))
    o.append(f'<g transform="rotate(70 {f(w * 0.44)} {f(h * 0.94)})"><path d="M{f(w * 0.44 - 8 * k)} {f(h * 0.94)} L {f(w * 0.44 - 10 * k)} {f(h * 0.94 - 50 * k)} L {f(w * 0.44 + 10 * k)} {f(h * 0.94 - 50 * k)} L {f(w * 0.44 + 8 * k)} {f(h * 0.94)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def scattered_refine(w, h, seed):
    """Smite the shepherd, and the sheep shall be scattered; the third part brought into the fire and refined as silver: the
    sheep scattered on the hills at left, a crucible in the furnace at right, the silver bright in it."""
    o = [sky(w, h, "#3A2A3A", "#C8806A"), hills(w, h, h * 0.5, seed, color="#5A4A4A", amp=18), ground(w, h, h * 0.58, "#7A6050", dy=0)]
    r = random.Random(seed)
    for i in range(7):
        o.append(E.sheep(w * r.uniform(0.04, 0.5), h * r.uniform(0.62, 0.96), min(0.4, h / 700), flip=r.random() < 0.5))
    k = min(1.2, h / 260); x, y = w * 0.76, h * 0.92
    o.append(f'<path d="M{f(x - 70 * k)} {f(y)} L {f(x - 60 * k)} {f(y - 90 * k)} L {f(x + 60 * k)} {f(y - 90 * k)} L {f(x + 70 * k)} {f(y)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(x - 30 * k)} {f(y)} L {f(x - 30 * k)} {f(y - 40 * k)} Q {f(x)} {f(y - 60 * k)} {f(x + 30 * k)} {f(y - 40 * k)} L {f(x + 30 * k)} {f(y)} Z" fill="#FF8A3D"></path>'
             + E.blaze(x, y - 86 * k, 90 * k, 50 * k, seed, n=5)
             + f'<path d="M{f(x - 30 * k)} {f(y - 100 * k)} L {f(x + 30 * k)} {f(y - 100 * k)} L {f(x + 20 * k)} {f(y - 70 * k)} L {f(x - 20 * k)} {f(y - 70 * k)} Z" fill="#3A3A44" stroke="#0D0D0F" stroke-width="2"></path>'
             + f'<ellipse cx="{f(x)}" cy="{f(y - 100 * k)}" rx="{f(28 * k)}" ry="{f(6 * k)}" fill="#F3F3FF" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' + halo(x, y - 100 * k, 30 * k, "#FFFFFF", 0.6))
    return "".join(o)

def spoil_gate(w, h, seed):
    """A day of Jehovah cometh, when thy spoil shall be divided in the midst of thee; the city shall be taken: the city gate
    under smoke, its doors thrown down, spoil scattered in the gateway (no one drawn)."""
    o = [sky(w, h, "#3A1A1A", "#A85A3A"), walls(-10, w + 10, h * 0.76, h * 0.56, seed, color="#8A7060", towers=2),
         smokes([w * 0.2, w * 0.5, w * 0.8], h * 0.3, seed, k=max(0.6, h / 300), color="#2A1A1E"), ground(w, h, h * 0.76, "#5A4030", dy=0)]
    r = random.Random(seed)
    for i in range(8):
        x, y = w * r.uniform(0.3, 0.7), h * r.uniform(0.8, 0.96)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="9" ry="4" fill="{r.choice(["#E8B830", "#C8C8D0", "#7A3A5A"])}" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.96)} L {f(w * 0.48)} {f(h * 0.84)} L {f(w * 0.5)} {f(h * 0.86)} L {f(w * 0.38)} {f(h * 0.98)} Z" fill="#5A3A1E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def olives_cleft(w, h, seed, flee=False):
    """His feet shall stand in that day upon the mount of Olives, and the mount of Olives shall be cleft in the midst thereof
    toward the east and toward the west, a very great valley; half toward the north and half toward the south: the mountain
    split in two, light pouring through the cleft (no figure), people fleeing through the valley (flee=True)."""
    o = [sky(w, h, "#1A1030", "#5A4A7A"), halo(w * 0.5, h * 0.4, h * 0.6, "#FFF4C2", 0.6), rays(w * 0.5, h * 0.4, 28, h * 0.1, max(w, h), "#FFF4C2", 0.25, 4)]
    o.append(f'<path d="M-10 {f(h * 0.86)} L {f(w * 0.14)} {f(h * 0.36)} L {f(w * 0.3)} {f(h * 0.26)} L {f(w * 0.42)} {f(h * 0.34)} L {f(w * 0.44)} {f(h * 0.86)} Z" fill="#4A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.56)} {f(h * 0.86)} L {f(w * 0.58)} {f(h * 0.3)} L {f(w * 0.72)} {f(h * 0.22)} L {f(w * 0.88)} {f(h * 0.34)} L {f(w + 10)} {f(h * 0.86)} Z" fill="#4A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(12):
        x = r.choice([r.uniform(w * 0.06, w * 0.4), r.uniform(w * 0.6, w * 0.96)]); y = h * r.uniform(0.5, 0.82)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(h * 0.025)}" fill="#7A8A5A" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    o.append(f'<path d="M{f(w * 0.44)} {f(h * 0.86)} L {f(w * 0.5)} {f(h * 0.3)} L {f(w * 0.56)} {f(h * 0.86)} Z" fill="#FFF4C2" opacity="0.8"></path>'
             + ground(w, h, h * 0.86, "#3A3A2A", dy=0)
             + label(w * 0.14, h * 0.8, "← NORTH", "#F3EFE6", 9) + label(w * 0.86, h * 0.8, "SOUTH →", "#F3EFE6", 9))
    if flee:
        for i in range(6):
            x = w * (0.47 + (i % 2) * 0.04); y = h * (0.62 + i * 0.04)
            o.append(f'<path d="M{f(x - 3)} {f(y)} L {f(x)} {f(y - 14 - i * 2)} L {f(x + 3)} {f(y)} Z" fill="#2A1E2A"></path>')
    return "".join(o)

def evening_light(w, h, seed):
    """There shall not be light; it shall be one day, not day, and not night; but at evening time there shall be light: a
    sky half dark, half grey, and on the horizon at evening a band of clear light."""
    o = [sky(w, h, "#0B0B14", "#4A4A5A"), f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#FFF4C2" opacity="0.85"></rect>',
         halo(w * 0.5, h * 0.6, h * 0.3, "#FFF4C2", 0.6), hills(w, h, h * 0.66, seed, color="#1A1A24", amp=14), ground(w, h, h * 0.72, "#14141C", dy=0)]
    return "".join(o)

def living_waters(w, h):
    """Living waters shall go out from Jerusalem, half toward the eastern sea, half toward the western sea, in summer and in
    winter; all the land made like the Arabah: a technical map with the two streams."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.12)} -10 C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.08)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             f'<ellipse cx="{f(w * 0.82)}" cy="{f(h * 0.6)}" rx="{f(w * 0.05)}" ry="{f(h * 0.26)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    cx, cy = w * 0.5, h * 0.5
    o.append(f'<path d="M{f(cx)} {f(cy)} C {f(cx - w * 0.14)} {f(cy + 20)} {f(w * 0.24)} {f(cy - 10)} {f(w * 0.1)} {f(cy + 10)}" stroke="#5AC8E8" stroke-width="5" fill="none"></path>'
             f'<path d="M{f(cx)} {f(cy)} C {f(cx + w * 0.12)} {f(cy - 10)} {f(w * 0.68)} {f(cy + 30)} {f(w * 0.77)} {f(cy + 20)}" stroke="#5AC8E8" stroke-width="5" fill="none"></path>')
    o += [node(cx, cy, "JERUSALEM", color=GOLD, r=7), label(w * 0.14, h * 0.2, "THE WESTERN SEA", CY, 9, anchor="start"), label(w * 0.94, h * 0.26, "THE EASTERN SEA", CY, 9, anchor="end"),
          node(w * 0.4, h * 0.36, "GEBA", color=CY, r=4), node(w * 0.56, h * 0.82, "RIMMON", color=CY, r=4)]
    return "".join(o)

def gates_plan(w, h):
    """She shall be lifted up, and shall dwell in her place, from Benjamin's gate unto the place of the first gate, unto the
    corner gate, and from the tower of Hananel unto the king's winepresses: a plan of the city's wall and gates."""
    o = [grid_bg(w, h, bg="#0B1A2E")]
    pts = [(0.3, 0.2), (0.7, 0.16), (0.84, 0.46), (0.74, 0.84), (0.34, 0.86), (0.18, 0.52)]
    d = "M" + " L ".join(f"{f(w * x)} {f(h * y)}" for x, y in pts) + " Z"
    o.append(f'<path d="{d}" fill="#12385A" stroke="{GOLD}" stroke-width="3"></path>')
    names = [("BENJAMIN'S GATE", 0.7, 0.16, "start"), ("THE FIRST GATE", 0.84, 0.46, "start"), ("THE CORNER GATE", 0.3, 0.2, "end"),
             ("TOWER OF HANANEL", 0.18, 0.52, "end"), ("THE KING'S WINEPRESSES", 0.74, 0.84, "start")]
    for n, x, y, an in names:
        o.append(node(w * x, h * y, "", color=GOLD, r=5) + label(w * x + (10 if an == "start" else -10), h * y + 4, n, CY, 9, anchor=an))
    o.append(halo(w * 0.5, h * 0.5, h * 0.2, "#FFE680", 0.4) + label(w * 0.5, h * 0.52, "JERUSALEM", GOLD, 11))
    return "".join(o)

def empty_camps(w, h, seed):
    """The plague wherewith Jehovah will smite all the peoples that have warred against Jerusalem; a great tumult among them;
    the plague of the horse, the mule, the camel and the ass: the camps of the nations deserted under a grey sky, tents
    sagging, standards fallen (no one drawn)."""
    o = [sky(w, h, "#3A3A3A", "#9A9080"), hills(w, h, h * 0.5, seed, color="#5A5248", amp=12), ground(w, h, h * 0.56, "#6A6050", dy=0)]
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.08 + i * 0.14); y = h * (0.7 + (i % 3) * 0.1)
        o.append(f'<g transform="rotate({r.randint(-12, 12)} {f(x)} {f(y)})">' + A.black_tent(x, y, w * 0.12, h * 0.12, color="#3A3434", lit="#1A1414") + '</g>')
    for i in range(3):
        x = w * (0.2 + i * 0.3); y = h * 0.96
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + 60)} {f(y - 20)}" stroke="#5A3A22" stroke-width="4"></path><path d="M{f(x + 60)} {f(y - 20)} L {f(x + 64)} {f(y - 44)} L {f(x + 84)} {f(y - 30)} Z" fill="#7A1A2A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def tabernacles(p, w, h, seed):
    """Every one that is left of all the nations shall go up from year to year to worship the King, Jehovah of hosts, and to
    keep the feast of tabernacles: booths of green branches on the roofs and in the streets, and the nations coming up."""
    o = [mk.defs(p, *ALL), sky(w, h, "#5A7AB8", "#FFE6A0"), mount_zion(w * 0.74, h * 0.62, w * 0.24, h * 0.4, seed, color="#8A7A6A"), ground(w, h, h * 0.62, "#C8B080", dy=0)]
    for i in range(4):
        x = w * (0.08 + i * 0.12); y = h * 0.8
        o.append(f'<path d="M{f(x - 30)} {f(y)} L {f(x - 30)} {f(y - 50)} M{f(x + 30)} {f(y)} L {f(x + 30)} {f(y - 50)}" stroke="#6A4A2A" stroke-width="4"></path>'
                 + "".join(f'<ellipse cx="{f(x - 30 + j * 15)}" cy="{f(y - 54)}" rx="14" ry="8" fill="#3F7A34" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for j in range(5)))
    o.append(crowd(p, w * 0.08, w * 0.6, h * 0.97, h * 0.66, 6, seed, colors=("#B5421E", "#E8B830", "#2E6B3A", "#6A1A5A", "#1F5FAD"), flip=True))
    return "".join(o)

def no_rain(w, h, seed):
    """Upon them there shall be no rain; if the family of Egypt go not up: the Nile low between cracked banks, the sky
    cloudless and white."""
    r = random.Random(seed)
    o = [sky(w, h, "#F3E8C8", "#E8C890"), sun(w * 0.8, h * 0.16, max(14, h * 0.07), color="#FFF4C2", op=0.6), ground(w, h, h * 0.5, "#D8B07A", dy=0),
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.72)}" stroke="#4A8AA8" stroke-width="{f(h * 0.02)}" fill="none"></path>']
    for i in range(30):
        x, y = r.uniform(0, w), r.uniform(h * 0.52, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-16, 16))} {f(r.uniform(4, 10))}" stroke="#8A6A3A" stroke-width="1.4"></path>')
    for x in (0.2, 0.62):
        o.append(f'<path d="M{f(w * x - 40)} {f(h * 0.5)} L {f(w * x)} {f(h * 0.3)} L {f(w * x + 40)} {f(h * 0.5)} Z" fill="#E8C890" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def bells(w, h, seed):
    """Upon the bells of the horses, HOLY UNTO JEHOVAH; the pots in Jehovah's house like the bowls before the altar: a horse's
    harness with its gold bell engraved, and a row of pots made holy."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>', halo(w * 0.36, h * 0.44, h * 0.5, "#FFE680", 0.4)]
    k = min(1.6, h / 220); x, y = w * 0.36, h * 0.5
    o.append(f'<path d="M{f(x - 160 * k)} {f(y - 70 * k)} C {f(x - 60 * k)} {f(y - 40 * k)} {f(x + 60 * k)} {f(y - 40 * k)} {f(x + 160 * k)} {f(y - 70 * k)}" stroke="#7A3A1E" stroke-width="{f(8 * k)}" fill="none"></path>'
             f'<path d="M{f(x)} {f(y - 46 * k)} L {f(x)} {f(y - 30 * k)}" stroke="#7A3A1E" stroke-width="{f(4 * k)}"></path>'
             f'<path d="M{f(x - 40 * k)} {f(y + 40 * k)} C {f(x - 40 * k)} {f(y - 10 * k)} {f(x - 24 * k)} {f(y - 30 * k)} {f(x)} {f(y - 30 * k)} C {f(x + 24 * k)} {f(y - 30 * k)} {f(x + 40 * k)} {f(y - 10 * k)} {f(x + 40 * k)} {f(y + 40 * k)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<circle cx="{f(x)}" cy="{f(y + 48 * k)}" r="{f(8 * k)}" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></circle>'
             + label(x, y + 74 * k, G.v("14:20", frm="HOLY UNTO JEHOVAH", to="HOLY UNTO JEHOVAH"), GOLD, 11))
    for i in range(4):
        px = w * (0.66 + i * 0.09); py = h * 0.86
        o.append(f'<path d="M{f(px - 20 * k * 0.6)} {f(py - 30 * k * 0.6)} C {f(px - 26 * k * 0.6)} {f(py)} {f(px + 26 * k * 0.6)} {f(py)} {f(px + 20 * k * 0.6)} {f(py - 30 * k * 0.6)} Z" fill="#8A6A4A" stroke="{GOLD}" stroke-width="2"></path>')
    return "".join(o)
