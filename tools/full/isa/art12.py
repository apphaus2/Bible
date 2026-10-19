"""Isaiah 43–45 drawings (on top of isa.art11): through the waters and through the fire, the four winds giving up the sons
and daughters, the nations assembled as witnesses, a way in the sea (the chariot and horse lying in the deep), rivers in the
desert with the jackals and ostriches drinking, the smith and the carpenter (a plate of the idol's making), the one tree
half burned and half a god, the thick cloud blotted out, the heavens and the mountains singing, the doors of brass broken
before Cyrus, light and darkness, the heavens distilling righteousness, the nations coming over, and every knee bowing."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art11 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def waters_fire(p, w, h, seed):
    """When thou passest through the waters, I will be with thee; when thou walkest through the fire, thou shalt not be
    burned: a lone traveller wading a river on the left and walking unharmed between flames on the right."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#8FC8E8"></rect>', f'<rect x="{f(w / 2)}" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#3A1A1A"></rect>']
    for k in range(4):
        y = h * (0.6 + k * 0.1)
        o.append(f'<path d="M-10 {f(y)} ' + " ".join(f"Q {f(x + 20)} {f(y - 8)} {f(x + 40)} {f(y)}" for x in range(-10, int(w / 2), 40)) + f' L {f(w / 2)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#2C7DA8", "#1F6F9A", "#1A5A80", "#144A6A"][k]}" stroke="#E8F6FA" stroke-width="1.4"></path>')
    s = fit(b, max(h * 0.5, b - 170))
    o.append(man(p, w * 0.24, b, s, "#5A4A6A"))
    y = h * 0.84
    o.append(f'<path d="M-10 {f(y)} ' + " ".join(f"Q {f(x + 20)} {f(y - 8)} {f(x + 40)} {f(y)}" for x in range(-10, int(w / 2), 40)) + f' L {f(w / 2)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" opacity="0.75"></path>')
    o.append(f'<rect x="{f(w / 2)}" y="{f(b)}" width="{f(w / 2 + 10)}" height="{f(h - b + 10)}" fill="#2A1414" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(E.blaze(w * 0.62, b, w * 0.1, h * 0.5, seed, n=6) + E.blaze(w * 0.92, b, w * 0.1, h * 0.5, seed + 1, n=6))
    o.append(man(p, w * 0.77, b, s, "#5A4A6A", flip=True))
    o.append(f'<path d="M{f(w / 2)} -10 L {f(w / 2)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="3"></path>')
    return "".join(o)

def four_winds(w, h):
    """I will bring thy seed from the east, and gather thee from the west; I will say to the north, Give up; and to the south,
    Keep not back: a compass of the four quarters with arrows from each coming in to Zion at the centre."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.54; r = min(w, h) * 0.38
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="#4A7A9A" stroke-width="1.6" stroke-dasharray="6 5"></circle>')
    for nm, a in (("THE NORTH · GIVE UP", -90), ("THE EAST", 0), ("THE SOUTH · KEEP NOT BACK", 90), ("THE WEST", 180)):
        ax, ay = cx + math.cos(math.radians(a)) * r, cy + math.sin(math.radians(a)) * r
        o.append(route([(ax, ay), (cx + math.cos(math.radians(a)) * 30, cy + math.sin(math.radians(a)) * 30)], color=GOLD))
        lx = ax + (math.cos(math.radians(a)) * 10); ly = ay + (math.sin(math.radians(a)) * 14) + (4 if a == 0 or a == 180 else 0)
        o.append(label(min(w - 8, max(8, lx)), max(14, min(h - 6, ly)), nm, CYAN, 9, "start" if a == 0 else "end" if a == 180 else "middle"))
    o.append(node(cx, cy, "ZION", GOLD, r=7, dy=-14, size=11))
    return "".join(o)

def witnesses(p, w, h, seed):
    """Let all the nations be gathered together, and let the peoples be assembled: who among them can declare this? Ye are my
    witnesses: a great assembly in an open place, the peoples in many colours on one side, Israel on the other, an empty seat
    of judgment between them in light."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FB0D8", "#F3E8C8"), V.rays(w * 0.5, h * 0.3, 24, 10, max(w, h), color="#FFF4C2", op=0.3), ground(w, h, h * 0.6, "#C8B088", dy=0)]
    o.append(f'<rect x="{f(w * 0.44)}" y="{f(h * 0.5)}" width="{f(w * 0.12)}" height="{f(h * 0.12)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.4, h * 0.64, b, 16, fit(b, b - 90) * 0.6, fit(b, b - 110)))
    for i in range(12):
        x = r.uniform(w * 0.6, w * 0.98); y = r.uniform(h * 0.64, b)
        o.append((man if r.random() < 0.6 else woman)(p, x, y, fit(b, b - 100) * (0.6 + (y - h * 0.64) / (b - h * 0.64) * 0.4), r.choice(["#7A2A6A", "#E8B830", "#1F5FAD", "#B5121B", "#2E8A5A", "#F3EFE6"]), flip=True))
    return "".join(o)

def sea_way(w, h, seed):
    """Jehovah, who maketh a way in the sea, and a path in the mighty waters; who bringeth forth the chariot and horse, the army
    and the mighty man (they lie down together, they shall not rise): the sea standing back from a dry path, and in the
    returned waters a broken chariot wheel and a spear lying under the surface."""
    o = [rect(w, h, "#8FC8E8"), E3.sea_corridor(w, h, (w * 0.5, h * 0.3), w * 0.3, w * 0.7, seed, uid=f"sw{seed}")]
    s = min(1.0, h / 300)
    o.append(f'<g opacity="0.7"><circle cx="{f(w * 0.12)}" cy="{f(h * 0.86)}" r="{f(28 * s)}" fill="none" stroke="#3A2214" stroke-width="{f(5 * s)}"></circle>'
             + "".join(f'<path d="M{f(w * 0.12)} {f(h * 0.86)} L {f(w * 0.12 + math.cos(a) * 28 * s)} {f(h * 0.86 + math.sin(a) * 28 * s)}" stroke="#3A2214" stroke-width="3"></path>' for a in [k * math.pi / 3 for k in range(6)])
             + f'<path d="M{f(w * 0.78)} {f(h * 0.94)} L {f(w * 0.98)} {f(h * 0.82)}" stroke="#5A5A6A" stroke-width="{f(4 * s)}"></path></g>')
    return "".join(o)

def desert_beasts(w, h, seed):
    """The beasts of the field shall honor me, the jackals and the ostriches; because I give waters in the wilderness, and
    rivers in the desert: a river winding through the desert, jackals and ostriches drinking at it."""
    o = [bg(w, h, "#E8A050", "#FFF0C8"), ground(w, h, h * 0.44, "#E0B878", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h * 0.44)} C {f(w * 0.2)} {f(h * 0.6)} {f(w * 0.7)} {f(h * 0.7)} {f(w * 0.4)} {f(h + 10)} L {f(w * 0.56)} {f(h + 10)} C {f(w * 0.86)} {f(h * 0.7)} {f(w * 0.34)} {f(h * 0.6)} {f(w * 0.36)} {f(h * 0.44)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>']
    k = min(0.7, h / 360)
    o.append(beast(w * 0.16, h * 0.9, k, "wolf") + beast(w * 0.86, h * 0.94, k * 0.9, "wolf", flip=True))
    o.append(ostrich(w * 0.66, h * 0.66, k * 1.1, drink=True) + ostrich(w * 0.76, h * 0.72, k, flip=True))
    return "".join(o)

def ostrich(x, y, s=1.0, flip=False, drink=False):
    """An ostrich standing (drink=True: its neck bent down to the water); (x, y) = the ground under it; ~130 units tall."""
    sx = -s if flip else s
    neck = "M14 -78 C 30 -70 40 -40 46 -6" if drink else "M14 -84 C 22 -100 16 -118 24 -130"
    head = (40, -6) if drink else (28, -132)
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-6 -50 L -10 0 M8 -50 L 12 0" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M-6 -50 L -10 0 M8 -50 L 12 0" stroke="#D8A890" stroke-width="4" stroke-linecap="round"></path>'
            '<path d="M-36 -64 C -40 -90 -10 -98 14 -88 C 30 -82 30 -60 14 -50 C -4 -42 -30 -46 -36 -64 Z" fill="#1A1414" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-36 -66 C -44 -70 -48 -60 -42 -54 C -38 -58 -36 -60 -36 -66 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<path d="{neck}" stroke="#0D0D0F" stroke-width="7" fill="none" stroke-linecap="round"></path><path d="{neck}" stroke="#D8A890" stroke-width="4" fill="none" stroke-linecap="round"></path>'
            f'<ellipse cx="{head[0]}" cy="{head[1]}" rx="7" ry="5" fill="#D8A890" stroke="#0D0D0F" stroke-width="1.6"></ellipse><path d="M{head[0] + 6} {head[1]} l 8 2" stroke="#0D0D0F" stroke-width="2"></path></g>')

def willows(w, h, seed):
    """I will pour water upon him that is thirsty, and streams upon the dry ground; they shall spring up among the grass, as
    willows by the watercourses: rain on dry ground, and willows springing up along a new stream."""
    r = random.Random(seed)
    o = [bg(w, h, "#7A9AC8", "#E8F0D8")]
    for _ in range(40):
        x = r.uniform(0, w); y = r.uniform(0, h * 0.4)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#4A6A9A" stroke-width="1.4" opacity="0.6"></path>')
    o.append(ground(w, h, h * 0.5, "#9CBB5E", dy=0) + f'<path d="M-10 {f(h * 0.76)} C {f(w * 0.3)} {f(h * 0.68)} {f(w * 0.6)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.74)}" stroke="#2C9DB8" stroke-width="{f(max(6, h * 0.03))}" fill="none"></path>')
    s = min(1.0, h / 300)
    for i in range(6):
        x = w * (0.08 + i * 0.17); y = h * (0.72 + (i % 2) * 0.06)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 70 * s)}" stroke="#5A4A2A" stroke-width="{f(5 * s)}"></path>'
                 + "".join(f'<path d="M{f(x)} {f(y - 70 * s)} C {f(x + (k - 3) * 10 * s)} {f(y - 80 * s)} {f(x + (k - 3) * 16 * s)} {f(y - 50 * s)} {f(x + (k - 3) * 18 * s)} {f(y - 24 * s)}" stroke="#6A9A3A" stroke-width="2.4" fill="none"></path>' for k in range(7)))
    return "".join(o)

def idol_plate(w, h):
    """The smith maketh an axe, and worketh in the coals; the carpenter stretcheth out a line, he marketh it out with a pencil,
    he shapeth it with planes, and marketh it out with the compasses, and shapeth it after the figure of a man: a plate of the
    making — the tools set out, and a block of wood marked with the outline of a man."""
    o = [bp(w, h), title_bar(w, "THE SMITH · THE CARPENTER · THE FIGURE OF A MAN")]
    s = min(1.0, h / 220); b = h * 0.84
    tools = [("THE AXE", 0.1), ("THE COALS", 0.22), ("THE LINE", 0.34), ("THE PENCIL", 0.46), ("THE PLANES", 0.58), ("THE COMPASSES", 0.7)]
    for nm, x in tools:
        cx = w * x
        if nm == "THE AXE":
            o.append(f'<path d="M{f(cx - 20 * s)} {f(b - 10 * s)} L {f(cx + 20 * s)} {f(b - 60 * s)}" stroke="#8A5A2A" stroke-width="4"></path><path d="M{f(cx + 14 * s)} {f(b - 70 * s)} L {f(cx + 30 * s)} {f(b - 64 * s)} L {f(cx + 24 * s)} {f(b - 44 * s)} Z" fill="#C8D0D8"></path>')
        elif nm == "THE COALS":
            o.append("".join(f'<circle cx="{f(cx + (k - 2) * 8 * s)}" cy="{f(b - 14 * s - (k % 2) * 6 * s)}" r="{f(6 * s)}" fill="#FF6A2A" stroke="#D7261E" stroke-width="1"></circle>' for k in range(5)))
        elif nm == "THE LINE":
            o.append(f'<circle cx="{f(cx)}" cy="{f(b - 30 * s)}" r="{f(12 * s)}" fill="none" stroke="#E8D8A8" stroke-width="3"></circle><path d="M{f(cx + 12 * s)} {f(b - 30 * s)} L {f(cx + 36 * s)} {f(b - 6 * s)}" stroke="#E8D8A8" stroke-width="1.4"></path>')
        elif nm == "THE PENCIL":
            o.append(f'<path d="M{f(cx - 20 * s)} {f(b - 10 * s)} L {f(cx + 20 * s)} {f(b - 50 * s)}" stroke="#D7261E" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>')
        elif nm == "THE PLANES":
            o.append(f'<rect x="{f(cx - 22 * s)}" y="{f(b - 30 * s)}" width="{f(44 * s)}" height="{f(16 * s)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="1.4"></rect><path d="M{f(cx - 4 * s)} {f(b - 30 * s)} L {f(cx + 4 * s)} {f(b - 42 * s)}" stroke="#C8D0D8" stroke-width="3"></path>')
        else:
            o.append(f'<path d="M{f(cx)} {f(b - 56 * s)} L {f(cx - 16 * s)} {f(b - 6 * s)} M{f(cx)} {f(b - 56 * s)} L {f(cx + 16 * s)} {f(b - 6 * s)}" stroke="#C8D0D8" stroke-width="3"></path><circle cx="{f(cx)}" cy="{f(b - 58 * s)}" r="{f(4 * s)}" fill="#C8D0D8"></circle>')
        o.append(label(cx, b + 16 * s, nm, CYAN, 8))
    bx = w * 0.84
    o.append(f'<rect x="{f(bx - 30 * s)}" y="{f(b - 130 * s)}" width="{f(60 * s)}" height="{f(130 * s)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<g transform="translate({f(bx)} {f(b)}) scale({f(0.6 * s)})"><path d="{mk.FIG["MAN"]}" fill="none" stroke="#FFD23F" stroke-width="3" stroke-dasharray="6 4"></path></g>'
             + label(bx, b + 30 * s, "THE FIGURE OF A MAN", GOLD, 8))
    return "".join(o)

def half_tree(p, w, h, seed):
    """He burneth part thereof in the fire; with part thereof he eateth flesh; he roasteth roast, and is satisfied; and the
    residue thereof he maketh a god, he falleth down unto it: a man by his fire with bread baking and the half-burned log, and
    beside it the other half carved into a god, the same man bowed before it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#2A1A20"), f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.7)}" r="{f(h * 0.4)}" fill="#C8582A" opacity="0.3"></circle>', ground(w, h, h * 0.86, "#1A1214", dy=0)]
    s = min(1.0, h / 280)
    o.append(f'<path d="M{f(w * 0.2)} {f(b)} L {f(w * 0.38)} {f(b - 8 * s)}" stroke="#4A2E1A" stroke-width="{f(12 * s)}" stroke-linecap="round"></path>' + E.blaze(w * 0.29, b - 4, w * 0.08, h * 0.24, seed, n=5)
             + f'<ellipse cx="{f(w * 0.29)}" cy="{f(b - 30 * s)}" rx="{f(22 * s)}" ry="{f(6 * s)}" fill="#C8904A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    fs = fit(b, max(h * 0.5, b - 170))
    o.append(man(p, w * 0.14, b, fs, "#6A5A3A", up=[(-22, -158), (2, -130), (26, -120)]))
    ix = w * 0.74
    o.append(f'<rect x="{f(ix - 16 * s)}" y="{f(b - 130 * s)}" width="{f(32 * s)}" height="{f(110 * s)}" rx="{f(10 * s)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<circle cx="{f(ix)}" cy="{f(b - 144 * s)}" r="{f(18 * s)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="2"></circle>'
             f'<rect x="{f(ix - 24 * s)}" y="{f(b - 20 * s)}" width="{f(48 * s)}" height="{f(20 * s)}" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(N.prostrate(w * 0.56, b, fs * 0.9, color="#6A5A3A"))
    return "".join(o)

def cloud_blotted(w, h, seed):
    """I have blotted out, as a thick cloud, thy transgressions, and, as a cloud, thy sins: a thick dark cloud breaking up and
    melting away into a clear blue sky over the hills."""
    r = random.Random(seed)
    o = [bg(w, h, "#5A9AD8", "#E8F4FA"), hills(w, h, h * 0.8, seed, color="#7AA04A", amp=10)]
    for i in range(16):
        x = w * (0.1 + i * 0.05) + r.uniform(-10, 10); y = h * 0.3 + r.uniform(-30, 30)
        op = max(0.08, 0.9 - i * 0.055)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(min(w, h) * r.uniform(0.07, 0.12))}" fill="#3A3A4A" opacity="{op:.2f}"></circle>')
    return "".join(o)

def heavens_sing(w, h, seed):
    """Sing, O ye heavens; shout, ye lower parts of the earth; break forth into singing, ye mountains, O forest, and every tree
    therein: mountains and forest under a bright sky, the trees swaying, notes rising from them."""
    o = [bg(w, h, "#5A9AD8", "#FFF0C8"), V.rays(w * 0.5, -h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.35),
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.56)} {f(h * 0.24)} L {f(w * 0.76)} {f(h * 0.5)} L {f(w * 0.9)} {f(h * 0.34)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A8A" stroke="#0D0D0F" stroke-width="2"></path>']
    s = min(0.8, h / 380)
    for i in range(11):
        x = w * (0.02 + i * 0.1); y = h * (0.94 + (i % 2) * 0.04)
        o.append(f'<g transform="rotate({(-6, 6)[i % 2]} {f(x)} {f(y)})"><path d="M{f(x)} {f(y)} L {f(x)} {f(y - 110 * s)}" stroke="#4A2E1A" stroke-width="{f(5 * s)}"></path>'
                 + "".join(f'<path d="M{f(x - (38 - j * 8) * s)} {f(y - (30 + j * 22) * s)} L {f(x)} {f(y - (60 + j * 22) * s)} L {f(x + (38 - j * 8) * s)} {f(y - (30 + j * 22) * s)} Z" fill="#2E6A3E" stroke="#0D0D0F" stroke-width="1.2"></path>' for j in range(4)) + '</g>')
    o.append(S3.notes(w * 0.3, h * 0.2, 6, seed, color="#1F3A7A") + S3.notes(w * 0.74, h * 0.16, 5, seed + 1, color="#1F3A7A"))
    return "".join(o)

def brass_doors(p, w, h, seed):
    """I will go before thee, and make the rough places smooth; I will break in pieces the doors of brass, and cut in sunder the
    bars of iron; I will give thee the treasures of darkness: the great gate of a city standing open, its brass doors broken
    and the iron bars cut, Cyrus' horsemen riding in, treasure glinting in the dark within."""
    o = [mk.defs(p, *ALL), bg(w, h, "#C86A3A", "#F8D8A0"), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.7)}" fill="#B8865A" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(14):
        o.append(f'<rect x="{f(i * w / 13 - 10)}" y="{f(h * 0.06)}" width="{f(w / 26)}" height="{f(h * 0.05)}" fill="#B8865A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    gx, gw = w * 0.36, w * 0.28
    o.append(f'<path d="M{f(gx)} {f(h * 0.8)} L {f(gx)} {f(h * 0.36)} Q {f(gx + gw / 2)} {f(h * 0.16)} {f(gx + gw)} {f(h * 0.36)} L {f(gx + gw)} {f(h * 0.8)} Z" fill="#1A1010" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for k in range(6):
        o.append(f'<circle cx="{f(gx + gw * (0.2 + k * 0.12))}" cy="{f(h * (0.66 + (k % 2) * 0.06))}" r="{f(min(w, h) * 0.012)}" fill="#E8B830"></circle>')
    o.append(f'<path d="M{f(gx)} {f(h * 0.36)} L {f(gx - w * 0.1)} {f(h * 0.42)} L {f(gx - w * 0.1)} {f(h * 0.84)} L {f(gx)} {f(h * 0.8)} Z" fill="#B87333" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(gx + gw)} {f(h * 0.36)} L {f(gx + gw + w * 0.06)} {f(h * 0.34)} L {f(gx + gw + w * 0.1)} {f(h * 0.6)} L {f(gx + gw + w * 0.04)} {f(h * 0.86)} L {f(gx + gw)} {f(h * 0.8)} Z" fill="#B87333" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(gx + gw + w * 0.04)} {f(h * 0.5)} L {f(gx + gw + w * 0.08)} {f(h * 0.56)} L {f(gx + gw + w * 0.05)} {f(h * 0.62)}" stroke="#0D0D0F" stroke-width="2.4" fill="none"></path>'
             f'<rect x="{f(w * 0.08)}" y="{f(h * 0.9)}" width="{f(w * 0.16)}" height="{f(h * 0.025)}" fill="#5A5A60" stroke="#0D0D0F" stroke-width="1.4" transform="rotate(-14 {f(w * 0.16)} {f(h * 0.9)})"></rect>'
             f'<rect x="{f(w * 0.72)}" y="{f(h * 0.92)}" width="{f(w * 0.14)}" height="{f(h * 0.025)}" fill="#5A5A60" stroke="#0D0D0F" stroke-width="1.4" transform="rotate(10 {f(w * 0.8)} {f(h * 0.92)})"></rect>')
    o.append(ground(w, h, h * 0.8, "#C8A070", dy=0))
    k = min(0.4, h / 700)
    o.append(E3.horse(w * 0.52, h * 0.96, k, color="#5A3A22", flip=True) + E3.horse(w * 0.66, h * 0.98, k, color="#3A2214", flip=True))
    return "".join(o)

def light_dark(w, h, seed):
    """I form the light, and create darkness; I make peace, and create evil; I am Jehovah, that doeth all these things: a plate
    split between the full light of day and the dark of night over the same hills."""
    o = [f'<defs><clipPath id="ld{seed}"><path d="M-10 -10 L {f(w * 0.56)} -10 L {f(w * 0.44)} {f(h + 10)} L -10 {f(h + 10)} Z"></path></clipPath></defs>',
         rect(w, h, "#05051A"), mk.stars(40, w, h * 0.6, seed), J.moon(w * 0.82, h * 0.2, min(18, h * 0.07)),
         f'<g clip-path="url(#ld{seed})">{bg(w, h, "#8FD0F0", "#FFF4C2")}{sun(w * 0.2, h * 0.24, min(30, h * 0.1), color="#FFF4C2", op=0.5)}</g>',
         hills(w, h, h * 0.7, seed, color="#3A4A3A", amp=12),
         f'<path d="M{f(w * 0.56)} -10 L {f(w * 0.44)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="3"></path>']
    return "".join(o)

def distil(w, h, seed):
    """Distil, ye heavens, from above, and let the skies pour down righteousness: let the earth open, that it may bring forth
    salvation, and let it cause righteousness to spring up together: soft rain falling from a bright cloud onto plowed earth,
    green shoots springing up in rows."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FB8E8", "#F8F0D0"), f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.16)}" rx="{f(w * 0.4)}" ry="{f(h * 0.1)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for _ in range(50):
        x = r.uniform(w * 0.12, w * 0.88); y = r.uniform(h * 0.26, h * 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} l 0 10" stroke="#5A8AC8" stroke-width="2" stroke-linecap="round"></path>')
    o.append(ground(w, h, h * 0.62, "#8A5A3A", dy=0))
    for k in range(5):
        y = h * (0.68 + k * 0.07)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y - 4)}" stroke="#5A3A22" stroke-width="2"></path>')
        for i in range(16):
            x = w * (0.03 + i * 0.062) + (k % 2) * 10
            o.append(f'<path d="M{f(x)} {f(y)} q -4 -10 -8 -12 M{f(x)} {f(y)} q 4 -10 8 -12" stroke="#5E9F2A" stroke-width="2" fill="none"></path>')
    return "".join(o)

def nations_come(w, h):
    """The labor of Egypt, and the merchandise of Ethiopia, and the Sabeans, men of stature, shall come over unto thee: arrows
    from Egypt, Ethiopia and Seba converging on Jerusalem (a map)."""
    return nations_map(w, h, hi=("EGYPT", "ETHIOPIA", "SEBA"), arrows=(("EGYPT", "JERUSALEM"), ("ETHIOPIA", "JERUSALEM"), ("SEBA", "JERUSALEM")), lit="#FFD23F",
                       show=["EGYPT", "ETHIOPIA", "SEBA", "JERUSALEM", "EDOM", "PHILISTIA", "BABYLON"])

def every_knee(p, w, h, seed):
    """Look unto me, and be ye saved, all the ends of the earth; unto me every knee shall bow, every tongue shall swear: people
    of every nation kneeling in rows on a wide plain toward the rising light."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(w, h, "#5A6ABA", "#FFE8B0"), V.rays(w * 0.5, h * 0.36, 40, 20, max(w, h), color="#FFF4C2", op=0.4),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.36)}" r="{f(h * 0.08)}" fill="#FFF4C2"></circle>', ground(w, h, h * 0.44, "#C8B088", dy=0)]
    for row in range(4):
        y = h * (0.56 + row * 0.12); s = fit(y, y - (40 + row * 26)) * 0.8
        for i in range(6 + row * 2):
            x = w * ((i + 0.5) / (6 + row * 2)) + r.uniform(-8, 8)
            o.append(E.kneel(x, y, s, color=r.choice(["#7A2A6A", "#E8B830", "#1F5FAD", "#B5121B", "#2E8A5A", "#F3EFE6", "#5A4A3A"]), skin=r.choice(["#5A3A2A", "#8A5A3A", "#B98A6E", "#3A2014"])))
    return "".join(o)
