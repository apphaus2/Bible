"""Drawings for the Habakkuk volume, on the minor prophets' kit (oba.minor). Habakkuk at a distance: an indigo robe and
headcloth, white beard (hab_fig). The Chaldeans are an army and horsemen; the watchtower; the vision written plain upon
tablets; the woes over the house set on high, the stone crying out of the wall, Lebanon's cedars felled, the dumb idol and
the holy temple. The prayer of chapter 3 is light over Teman and Paran, the tents of Cushan, the rivers and the sea, the
sun and moon standing still, the heap of mighty waters — God never drawn, only his brightness — and the barren fig-tree and
the hinds on the high places."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from jos.art import warrior, WAR
from sng.art import roe, leopard
import exodus2 as E2

HAB_C = "#2A2A5A"

def hab_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=HAB_C, sw=3, flip=flip, up=up, extra=A.headcloth(HAB_C) + WHITE_BEARD)

def strife(p, w, h, seed):
    """Strife and contention rise up; the law is slacked, justice goeth forth perverted: men quarrelling at the city gate,
    the judges' seat empty, scales overturned."""
    from ecc.art import scales
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#6A3A3A", "#E8A880"), walls(-10, w + 10, h * 0.62, h * 0.4, seed, color="#A8906A", towers=3), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    r = random.Random(seed)
    for i in range(5):
        x = w * (0.1 + i * 0.12)
        up = [(22, -158), (40, -176), (58, -196)] if i % 2 else None
        o.append(man(p, x, b - r.uniform(0, 8), fit(b, h * 0.5), r.choice(["#6A2A2A", "#3A4A6A", "#6A5A3A", "#4A3A5A"]), flip=i % 2 == 1, up=up))
    k = min(0.8, h / 360)
    o.append(f'<g transform="rotate(70 {f(w * 0.82)} {f(b)})">{scales(w * 0.82, b, k, tilt=0)}</g>')
    return "".join(o)

def chaldeans(p, w, h, seed):
    """I raise up the Chaldeans, that bitter and hasty nation, that march through the breadth of the earth: a long column
    of spearmen across the plain, their banners."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8A5A3A", "#E8C090"), hills(w, h, h * 0.5, seed, color="#9A7A5A", amp=10), ground(w, h, h * 0.56, "#B8986A", dy=0)]
    for row, (y, k) in enumerate(((0.66, 0.5), (0.8, 0.7), (0.96, 0.9))):
        n = 7 + row * 2
        for i in range(n):
            x = w * (i + 0.5) / n + (row % 2) * 10
            o.append(warrior(p, x, h * y, fit(h * y, h * (y - 0.16 * k)), WAR[(i + row) % len(WAR)], flip=False))
    return "".join(o)

def horsemen(w, h, seed):
    """Their horses swifter than leopards, more fierce than the evening wolves; their horsemen fly as an eagle that
    hasteth to devour: horsemen galloping at dusk, an eagle stooping above them."""
    o = [sky(w, h, "#2A1A3A", "#E8803A"), ground(w, h, h * 0.7, "#5A3A2E", dy=0)]
    k = min(0.9, h / 300)
    for i in range(4):
        x = w * (0.16 + i * 0.22); y = h * (0.9 + (i % 2) * 0.05)
        o.append(E3.horse(x, y, k * 0.8, color=["#3A2214", "#5A3A22", "#1A1210", "#6A4A2A"][i]) + mk.speed(x - 60 * k, y - 40 * k, 6, 10 * k, 70 * k, seed + i, color="#E8C090", op=0.5)
                 + f'<path d="M{f(x - 4 * k)} {f(y - 80 * k)} L {f(x - 8 * k)} {f(y - 110 * k)} L {f(x + 8 * k)} {f(y - 112 * k)} L {f(x + 6 * k)} {f(y - 80 * k)} Z" fill="#7A2A1A" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y - 120 * k)}" r="{f(8 * k)}" fill="{SKIN}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    o.append(eagle(w * 0.7, h * 0.22, k * 1.1, color="#2A1A14"))
    return "".join(o)

def siege_ramp(w, h, seed):
    """He derideth every stronghold, for he heapeth up dust, and taketh it: an earth ramp heaped against a fortress wall."""
    o = [sky(w, h, "#6A5A5A", "#D8B898"), walls(w * 0.4, w * 1.05, h * 0.62, h * 0.5, seed, color="#9A8A7A", towers=2), ground(w, h, h * 0.62, "#9A7A5A", dy=0),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.92)} L {f(w * 0.46)} {f(h * 0.4)} L {f(w * 0.54)} {f(h * 0.44)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#B89A6A" stroke="#0D0D0F" stroke-width="2.2"></path>']
    for k in range(6):
        y = h * (0.5 + k * 0.08)
        o.append(f'<path d="M{f(w * (0.4 - k * 0.07))} {f(y)} L {f(w * (0.52 - k * 0.02))} {f(y + 4)}" stroke="#8A6A3A" stroke-width="2"></path>')
    o.append(wind_lines(w, h, seed, n=6, color="#F3E8C8", op=0.5, y0=0.1, y1=0.4))
    return "".join(o)

def net_fishes(w, h, seed):
    """He maketh men as the fishes of the sea; he catcheth them in his net, and burneth incense unto his drag: a great net
    hauled full of fish, a censer smoking before it."""
    o = [sky(w, h, "#5A6A8A", "#D8D0C0"), sea(w, h, h * 0.4, seed)]
    x0, x1, y0, y1 = w * 0.08, w * 0.68, h * 0.5, h * 0.94
    o.append(f'<path d="M{f(x0)} {f(y0)} C {f(x0 + 40)} {f(y1)} {f(x1 - 40)} {f(y1)} {f(x1)} {f(y0)}" fill="#1F4A6A" stroke="#C8B890" stroke-width="3"></path>')
    for i in range(12):
        t = i / 11
        o.append(f'<path d="M{f(x0 + (x1 - x0) * t)} {f(y0)} L {f(x0 + (x1 - x0) * (0.2 + 0.6 * t))} {f(y1 - 8)}" stroke="#C8B890" stroke-width="1.2" opacity="0.8"></path>')
    r = random.Random(seed)
    for i in range(10):
        x, y = r.uniform(x0 + 30, x1 - 30), r.uniform(y0 + 14, y1 - 20); s = r.uniform(10, 18) * min(1.0, h / 260)
        o.append(f'<path d="M{f(x - s)} {f(y)} C {f(x - s * 0.4)} {f(y - s * 0.5)} {f(x + s * 0.5)} {f(y - s * 0.5)} {f(x + s)} {f(y)} C {f(x + s * 0.5)} {f(y + s * 0.5)} {f(x - s * 0.4)} {f(y + s * 0.5)} {f(x - s)} {f(y)} Z M{f(x - s)} {f(y)} L {f(x - s * 1.5)} {f(y - s * 0.4)} L {f(x - s * 1.5)} {f(y + s * 0.4)} Z" fill="#9AB0C0" stroke="#0D0D0F" stroke-width="1.2"></path>')
    cx, cy, k = w * 0.84, h * 0.94, min(1.0, h / 300)
    o.append(f'<path d="M{f(cx - 24 * k)} {f(cy)} L {f(cx - 18 * k)} {f(cy - 40 * k)} L {f(cx + 18 * k)} {f(cy - 40 * k)} L {f(cx + 24 * k)} {f(cy)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             + smoke(cx, cy - 50 * k, 7, seed, color="#C8C0B8", op=0.5, k=k * 0.7))
    return "".join(o)

def watchtower(p, w, h, seed):
    """I will stand upon my watch, and set me upon the tower, and will look forth: Habakkuk on the top of a stone
    watchtower above the plain at dusk, looking out."""
    o = [mk.defs(p, *ALL), sky(w, h, "#1E1650", "#E8906A"), starfield(w, h, seed, 30, 0.3), hills(w, h, h * 0.66, seed, color="#3A2A4A", amp=14), ground(w, h, h * 0.74, "#2A1E2E", dy=0)]
    x = w * 0.3; top = h * 0.28
    o.append(f'<path d="M{f(x - w * 0.08)} {f(h + 10)} L {f(x - w * 0.06)} {f(top)} L {f(x + w * 0.06)} {f(top)} L {f(x + w * 0.08)} {f(h + 10)} Z" fill="#7A6A6A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<rect x="{f(x - w * 0.065 + i * w * 0.035)}" y="{f(top - h * 0.04)}" width="{f(w * 0.022)}" height="{f(h * 0.045)}" fill="#7A6A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(4))
             + "".join(f'<path d="M{f(x - w * 0.07)} {f(top + h * 0.12 * k)} L {f(x + w * 0.07)} {f(top + h * 0.12 * k)}" stroke="#5A4A4A" stroke-width="1.6"></path>' for k in range(1, 6)))
    s = fit(top, top - h * 0.2)
    o.append(hab_fig(p, x, top, s, up=[(22, -158), (40, -176), (60, -184)]))
    return "".join(o)

def tablets(w, h, seed):
    """Write the vision, and make it plain upon tablets, that he may run that readeth it: two great tablets with bold
    ruled writing, a runner's road beyond."""
    o = [sky(w, h, "#3A3A6A", "#FFD8A0"), ground(w, h, h * 0.72, "#A8906A", dy=0),
         route([(w * 0.6, h * 0.8), (w * 0.8, h * 0.76), (w + 10, h * 0.74)], color="#FFE680", dash="10 6")]
    k = min(1.4, h / 260)
    for i, x in enumerate((0.26, 0.46)):
        cx, cy = w * x, h * 0.86
        o.append(f'<path d="M{f(cx - 50 * k)} {f(cy)} L {f(cx - 50 * k)} {f(cy - 110 * k)} Q {f(cx)} {f(cy - 150 * k)} {f(cx + 50 * k)} {f(cy - 110 * k)} L {f(cx + 50 * k)} {f(cy)} Z" fill="#D8D0C0" stroke="#0D0D0F" stroke-width="2.6"></path>'
                 + "".join(f'<path d="M{f(cx - 36 * k)} {f(cy - (110 - j * 18) * k)} L {f(cx + (36 - (j % 3) * 8) * k)} {f(cy - (110 - j * 18) * k)}" stroke="#2A2A3A" stroke-width="{f(4 * k)}" stroke-dasharray="{f(12 * k)} {f(4 * k)}"></path>' for j in range(6)))
    o.append(halo(w * 0.36, h * 0.6, h * 0.4, "#FFE680", 0.35))
    return "".join(o)

def sheol_cup(w, h, seed):
    """Wine is treacherous; he enlargeth his desire as Sheol, and he is as death, and cannot be satisfied: an overflowing
    cup at the edge of a gaping pit."""
    o = [sky(w, h, "#2A1A2A", "#8A4A3A"), ground(w, h, h * 0.6, "#4A3028", dy=0),
         f'<ellipse cx="{f(w * 0.62)}" cy="{f(h * 0.8)}" rx="{f(w * 0.3)}" ry="{f(h * 0.14)}" fill="#05030A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>',
         f'<ellipse cx="{f(w * 0.62)}" cy="{f(h * 0.82)}" rx="{f(w * 0.22)}" ry="{f(h * 0.08)}" fill="#1A0A10" opacity="0.6"></ellipse>',
         cup(w * 0.18, h * 0.92, min(1.2, h / 260), spill=True)]
    return "".join(o)

def pledges(w, h, seed):
    """Woe to him that increaseth that which is not his, and ladeth himself with pledges: heaps of pledges — sealed bags,
    cloaks, vessels — piled in a storehouse, the door broken open."""
    from est.art import vessel
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>',
         f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.78)}" y="{f(h * 0.2)}" width="{f(w * 0.16)}" height="{f(h * 0.66)}" fill="#C8A060" opacity="0.5"></rect>',
         f'<path d="M{f(w * 0.94)} {f(h * 0.86)} L {f(w * 0.99)} {f(h * 0.9)} L {f(w * 0.99)} {f(h * 0.22)} L {f(w * 0.94)} {f(h * 0.2)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path>']
    r = random.Random(seed); k = min(1.0, h / 300)
    for i in range(14):
        x = w * (0.06 + (i % 7) * 0.1); y = h * (0.88 - (i // 7) * 0.14)
        kind = i % 3
        if kind == 0: o.append(f'<path d="M{f(x - 20 * k)} {f(y)} C {f(x - 26 * k)} {f(y - 30 * k)} {f(x - 10 * k)} {f(y - 44 * k)} {f(x)} {f(y - 46 * k)} C {f(x + 10 * k)} {f(y - 44 * k)} {f(x + 26 * k)} {f(y - 30 * k)} {f(x + 20 * k)} {f(y)} Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="{f(x)}" cy="{f(y - 40 * k)}" r="{f(4 * k)}" fill="#B5121B"></circle>')
        elif kind == 1: o.append(f'<path d="M{f(x - 24 * k)} {f(y)} L {f(x - 16 * k)} {f(y - 20 * k)} L {f(x + 18 * k)} {f(y - 24 * k)} L {f(x + 26 * k)} {f(y)} Z" fill="{r.choice(["#5A2A6A", "#2A5A6A", "#8A3A2A"])}" stroke="#0D0D0F" stroke-width="1.6"></path>')
        else: o.append(vessel(x, y, k * 0.6, r.choice(["cup", "amphora", "bowl"]), color=r.choice(["#E8B830", "#C8C8D0"])))
    return "".join(o)

def stone_cries(w, h, seed):
    """That he may set his nest on high — the stone shall cry out of the wall, and the beam out of the timber shall answer
    it: a high house on a crag, one stone of its wall and one beam glowing with lines of sound."""
    o = [sky(w, h, "#2A2A4A", "#C89A7A"), f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.3)} {f(h * 0.4)} L {f(w * 0.7)} {f(h * 0.36)} L {f(w * 0.82)} {f(h + 10)} Z" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="2.2"></path>']
    x0, x1, top = w * 0.32, w * 0.68, h * 0.08
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(h * 0.3)}" fill="#C8B090" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for row in range(4):
        y = top + h * 0.075 * row
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="#8A7A5A" stroke-width="1.4"></path>')
    sx, sy = w * 0.42, top + h * 0.15
    o.append(f'<rect x="{f(sx)}" y="{f(sy)}" width="{f(w * 0.06)}" height="{f(h * 0.075)}" fill="#FFE680" stroke="#0D0D0F" stroke-width="1.8"></rect>'
             + rays(sx + w * 0.03, sy + h * 0.04, 10, h * 0.06, h * 0.14, "#FFE680", 0.8, 2.4))
    o.append(f'<rect x="{f(x0 - 10)}" y="{f(top - 8)}" width="{f(x1 - x0 + 20)}" height="10" fill="#FFC14D" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    return "".join(o)

def glory_sea(w, h, seed):
    """The earth shall be filled with the knowledge of the glory of Jehovah, as the waters cover the sea: the wide sea under a
    sky full of golden light to every horizon."""
    o = [sky(w, h, "#FFD870", "#FFF4C2"), halo(w * 0.5, h * 0.3, max(w, h) * 0.6, "#FFF4C2", 0.6), rays(w * 0.5, h * 0.3, 36, h * 0.1, max(w, h), "#FFFFFF", 0.35, 3),
         sea(w, h, h * 0.52, seed, color="#3A9AC8", deep="#1F6F9A", foam="#FFF4C2")]
    return "".join(o)

def lebanon_felled(w, h, seed):
    """The violence done to Lebanon shall cover thee, and the destruction of the beasts: cedars cut down on the slopes, their
    stumps, a stag fleeing; the cup of Jehovah's right hand."""
    o = [sky(w, h, "#5A6A8A", "#D8D0C0"), hills(w, h, h * 0.4, seed, color="#6A7A8A", amp=30, step=100), ground(w, h, h * 0.56, "#6A6A4A", dy=0)]
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.06 + i * 0.14); y = h * r.uniform(0.66, 0.9)
        o.append(f'<rect x="{f(x - 8)}" y="{f(y - 16)}" width="16" height="16" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></rect><ellipse cx="{f(x)}" cy="{f(y - 16)}" rx="8" ry="3" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.96)} L {f(w * 0.6)} {f(h * 0.9)}" stroke="#5A3A22" stroke-width="{f(h * 0.04)}" stroke-linecap="round"></path>')
    o.append(roe(w * 0.8, h * 0.8, min(0.7, h / 360), flip=False, hart=True, pose="leap", color="#8A5A2A"))
    return "".join(o)

def idol_temple(w, h, seed):
    """Woe unto him that saith to the wood, Awake; to the dumb stone, Arise! — overlaid with gold, no breath in it. But
    Jehovah is in his holy temple: let all the earth keep silence before him. A gilded idol dark on the left, the temple
    lit far off on the right."""
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#1A1418"></rect>',
         f'<g transform="translate({f(w * 0.5)} 0)">{sky(w * 0.5, h, "#2A3A6A", "#FFE6A0")}{halo(w * 0.25, h * 0.5, h * 0.5, "#FFF4C2", 0.6)}'
         f'{hills(w * 0.5, h, h * 0.7, seed, color="#5A4A6A", amp=10)}{temple_front(w * 0.25, h * 0.72, w * 0.2, seed)}{ground(w * 0.5, h, h * 0.72, "#6A5A5A", dy=0)}</g>',
         f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="3"></path>']
    k = min(1.2, h / 260); x, y = w * 0.24, h * 0.92
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><rect x="-40" y="-14" width="80" height="14" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></rect>'
             '<path d="M-20 -14 L -24 -90 C -24 -110 -14 -120 0 -120 C 14 -120 24 -110 24 -90 L 20 -14 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<circle cx="0" cy="-130" r="14" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></circle><path d="M-6 -132 L -2 -132 M4 -132 L 8 -132" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-24 -80 L -40 -50 M24 -80 L 40 -50" stroke="#C8962E" stroke-width="8" stroke-linecap="round"></path></g>')
    return "".join(o)

# ---- the prayer of Habakkuk (3) ------------------------------------------------------------------------------------------
def teman_glory(w, h, seed):
    """God came from Teman, and the Holy One from mount Paran; his glory covered the heavens; he had rays coming forth;
    fiery bolts went forth: a blaze of light rising behind the desert mountains, rays spread over the sky (no figure)."""
    o = [sky(w, h, "#2A1A3A", "#FFB04A"), halo(w * 0.5, h * 0.62, max(w, h) * 0.6, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.62, 40, h * 0.1, max(w, h) * 1.2, "#FFF4C2", 0.35, 5),
         bolt(w * 0.16, h * 0.1, h * 0.6, seed, color="#FFD23F"), bolt(w * 0.86, h * 0.1, h * 0.56, seed + 1, color="#FFD23F"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.5)} L {f(w * 0.34)} {f(h * 0.64)} L {f(w * 0.5)} {f(h * 0.56)} L {f(w * 0.66)} {f(h * 0.66)} L {f(w * 0.84)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} Z" fill="#4A2A2A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         label(w * 0.2, h * 0.94, "TEMAN", "#FFE6A0", 10), label(w * 0.8, h * 0.94, "MOUNT PARAN", "#FFE6A0", 10)]
    return "".join(o)

def cushan(w, h, seed):
    """He stood, and measured the earth; the eternal mountains were scattered; I saw the tents of Cushan in affliction, the
    curtains of the land of Midian did tremble: black tents shaking under a stormy light, the hills breaking behind."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A2A3A", "#B88A6A"), halo(w * 0.5, 0, h * 0.6, "#FFF4C2", 0.4)]
    for i in range(5):
        x = w * (0.1 + i * 0.2)
        o.append(f'<path d="M{f(x - w * 0.12)} {f(h * 0.56)} L {f(x)} {f(h * r.uniform(0.22, 0.34))} L {f(x + w * 0.12)} {f(h * 0.56)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2" transform="rotate({r.randint(-8, 8)} {f(x)} {f(h * 0.56)})"></path>')
    o.append(ground(w, h, h * 0.56, "#B8986A", dy=0))
    for i in range(4):
        x = w * (0.14 + i * 0.24)
        o.append(f'<g transform="rotate({(-1) ** i * 4} {f(x)} {f(h * 0.9)})">' + A.black_tent(x, h * 0.9, w * 0.2, h * 0.22) + '</g>')
        o.append(mk.speed(x, h * 0.8, 6, w * 0.1, w * 0.13, seed + i, color="#F3EFE6", op=0.5))
    return "".join(o)

def waters_lift(w, h, seed):
    """Was thine anger against the rivers, thy wrath against the sea? the deep uttered its voice, and lifted up its hands on
    high; the mountains saw thee and were afraid: great waves rising like hands under lightning."""
    o = [sky(w, h, "#0B0B2A", "#3A4A6A"), bolt(w * 0.3, 0, h * 0.4, seed), bolt(w * 0.74, 0, h * 0.34, seed + 1),
         hills(w, h, h * 0.42, seed, color="#1A1A30", amp=30, step=100)]
    from jon.art import swell
    o.append(f'<g transform="translate(0 {f(h * 0.3)})">{E3.crash(w, h * 0.7, seed)}</g>')
    o.append(swell(w, h, h * 0.8, seed, color="#1F4A6A", n=2, amp=0.08))
    return "".join(o)

def sun_moon(w, h, seed):
    """The sun and moon stood still in their habitation, at the light of thine arrows as they went, at the shining of thy
    glittering spear: sun and moon both in the sky, shafts of light crossing it."""
    o = [sky(w, h, "#2A3A6A", "#D8B8A8"), sun(w * 0.22, h * 0.3, max(14, h * 0.07), color="#FFE680", op=0.5), J.moon(w * 0.8, h * 0.24, max(10, h * 0.05)),
         hills(w, h, h * 0.76, seed, color="#4A3A4A", amp=14), ground(w, h, h * 0.84, "#5A4A3A", dy=0)]
    r = random.Random(seed)
    for i in range(7):
        x0, y0 = w * r.uniform(-0.1, 0.4), h * r.uniform(0.0, 0.3)
        o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x0 + w * 0.6)} {f(y0 + h * 0.5)}" stroke="#FFF4C2" stroke-width="3" opacity="0.7"></path>'
                 f'<path d="M{f(x0 + w * 0.6)} {f(y0 + h * 0.5)} l -12 -2 l 4 -8 Z" fill="#FFF4C2"></path>')
    return "".join(o)

def sea_heap(w, h, seed):
    """Thou didst tread the sea with thy horses, the heap of mighty waters: the sea heaped up in two walls with a way of
    light through the midst."""
    o = [sky(w, h, "#1E1650", "#8FB8D8"), E3.sea_corridor(w, h, (w * 0.5, h * 0.36), w * 0.3, w * 0.7, seed, uid=f"sh{seed}"),
         halo(w * 0.5, h * 0.36, h * 0.3, "#FFF4C2", 0.6)]
    return "".join(o)

def barren(w, h, seed):
    """Though the fig-tree shall not flourish, neither shall fruit be in the vines, the labor of the olive fail, the fields
    yield no food, the flock cut off from the fold and no herd in the stalls."""
    o = [sky(w, h, "#8A7A6A", "#E8D8B8"), hills(w, h, h * 0.5, seed, color="#A8906A", amp=12), ground(w, h, h * 0.56, "#B8A07A", dy=0),
         vines(w * 0.36, w * 0.96, h * 0.66, h * 0.78, seed, rows=2, bare=True), fig_tree(w * 0.16, h * 0.96, min(1.1, h / 260), bare=True, seed=seed),
         grain(w * 0.3, w + 10, h * 0.98, h * 0.05, seed, color="#A89A6A")]
    x0 = w * 0.62
    o.append(f'<path d="M{f(x0)} {f(h * 0.96)} L {f(x0)} {f(h * 0.82)} L {f(w * 0.96)} {f(h * 0.82)} L {f(w * 0.96)} {f(h * 0.96)}" stroke="#8A7A6A" stroke-width="{f(h * 0.03)}" fill="none"></path>')
    return "".join(o)

def hinds(w, h, seed):
    """He maketh my feet like hinds' feet, and will make me to walk upon my high places: hinds leaping on the high crags at
    sunrise."""
    o = [sky(w, h, "#3A4A8A", "#FFD8A0"), sun(w * 0.8, h * 0.5, max(14, h * 0.07), color="#FFE680", op=0.5),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.34)} {f(h * 0.46)} L {f(w * 0.5)} {f(h * 0.2)} L {f(w * 0.64)} {f(h * 0.52)} L {f(w * 0.8)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A5A7A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    k = min(0.7, h / 380)
    o.append(roe(w * 0.22, h * 0.31, k, pose="leap", color="#B5743A") + roe(w * 0.5, h * 0.21, k * 0.9, pose="stand", color="#B5743A", flip=True))
    return "".join(o)
