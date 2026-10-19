"""Isaiah 63–66 drawings (on top of isa.art17): the winepress trodden alone (an empty winepress running red at sunset, Bozrah far
off: no one drawn), the cattle going down into the valley, Zion a wilderness, rend the heavens (fire on the mountains), the
polluted garment and the fading leaf, the graves and the gardens at night, the new wine in the cluster, Sharon a fold of
flocks, a table for Fortune and Destiny, new heavens and a new earth, houses built and vineyards planted, heaven a throne and
the earth a footstool (an empty throne in the sky over the earth), a land born in one day, the nations bringing your brethren
on horses and litters and dromedaries, and the valley outside the city where the fire is not quenched (66:24 words only)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art17 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def winepress_alone(w, h, seed):
    """I have trodden the winepress alone; and of the peoples there was no man with me: a great rock-hewn winepress under a red
    evening sky, its vat brimming and the red running over its lip into the trough; the road from Edom and Bozrah's crags far
    off; no one drawn."""
    o = [bg(w, h, "#3A0A14", "#E8603A"), sun(w * 0.8, h * 0.3, min(30, h * 0.08), color="#FFB04A", op=0.35),
         f'<path d="M{f(w * 0.6)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.34)} L {f(w * 0.78)} {f(h * 0.44)} L {f(w * 0.88)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.48)} L {f(w + 10)} {f(h * 0.56)} L {f(w * 0.6)} {f(h * 0.56)} Z" fill="#8A2A1A" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.56, "#6A3A2A", dy=0), f'<path d="M{f(w * 0.64)} {f(h * 0.56)} L {f(w * 0.68)} {f(h * 0.56)} L {f(w * 0.5)} {f(h + 10)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#8A5A3A" opacity="0.6"></path>']
    s = min(1.4, h / 240); cx, cy = w * 0.3, h * 0.78
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(110 * s)}" ry="{f(34 * s)}" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="2.6"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - 2)}" rx="{f(96 * s)}" ry="{f(26 * s)}" fill="#7A0A1A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
             f'<ellipse cx="{f(cx - 20 * s)}" cy="{f(cy - 8 * s)}" rx="{f(40 * s)}" ry="{f(8 * s)}" fill="#B5121B" opacity="0.7"></ellipse>'
             f'<path d="M{f(cx + 100 * s)} {f(cy + 4)} C {f(cx + 130 * s)} {f(cy + 20 * s)} {f(cx + 150 * s)} {f(cy + 40 * s)} {f(cx + 200 * s)} {f(cy + 44 * s)}" stroke="#7A0A1A" stroke-width="{f(10 * s)}" fill="none" stroke-linecap="round"></path>'
             f'<rect x="{f(cx + 190 * s)}" y="{f(cy + 34 * s)}" width="{f(80 * s)}" height="{f(24 * s)}" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(cx + 194 * s)}" y="{f(cy + 38 * s)}" width="{f(72 * s)}" height="{f(10 * s)}" fill="#7A0A1A"></rect>')
    return "".join(o)

def cattle_valley(w, h, seed):
    """As the cattle that go down into the valley, the Spirit of Jehovah caused them to rest: cattle going down a slope into a green
    valley with water at evening."""
    o = [bg(w, h, "#7A8AC8", "#FFE0B0"), f'<path d="M-10 {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.8)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7AA04A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.88)}" rx="{f(w * 0.2)}" ry="{f(h * 0.05)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1.6"></ellipse>']
    k = min(0.5, h / 520)
    for i in range(4):
        t = i / 4; x = w * (0.08 + t * 0.34); y = h * (0.5 + t * 0.32)
        o.append(S1.cow(x, y, k * (0.6 + t * 0.5), color=["#8A5A30", "#C9A27A", "#6A4A2A", "#B88A5A"][i], low=True))
    return "".join(o)

def look_down(w, h, seed):
    """Look down from heaven, and behold from the habitation of thy holiness and of thy glory: a vast sky of cloud with a shaft of
    light breaking through, the small walled city below (no one drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#2A3A6A", "#C8B8C8")]
    for _ in range(12):
        o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h * 0.5))}" rx="{f(w * r.uniform(0.1, 0.2))}" ry="{f(h * r.uniform(0.05, 0.1))}" fill="#4A5A8A" opacity="0.7"></ellipse>')
    o.append(f'<path d="M{f(w * 0.46)} -10 L {f(w * 0.54)} -10 L {f(w * 0.62)} {f(h * 0.8)} L {f(w * 0.38)} {f(h * 0.8)} Z" fill="#FFF4C2" opacity="0.3"></path>')
    o.append(hills(w, h, h * 0.82, seed, color="#5A5A6A", amp=8) + J.city_hill(w * 0.5, h * 0.9, w * 0.14, h * 0.1, seed))
    return "".join(o)

def zion_wilderness(w, h, seed):
    """Thy holy cities are become a wilderness, Zion is become a wilderness; our holy and beautiful house is burned with fire: the
    hill of Zion overgrown, its walls broken, the house a blackened shell, smoke still rising (no one drawn)."""
    return K3.burning_city(w, h, seed)

def rend_heavens(w, h, seed):
    """Oh that thou wouldest rend the heavens, that thou wouldest come down, that the mountains might quake at thy presence, as when
    fire kindleth the brushwood: the sky torn open with light, fire running over the mountains, the brushwood burning (no one
    drawn)."""
    o = [rect(w, h, "#14102A"), f'<path d="M{f(w * 0.3)} -10 L {f(w * 0.46)} {f(h * 0.3)} L {f(w * 0.54)} {f(h * 0.22)} L {f(w * 0.7)} -10 Z" fill="#FFF4C2"></path>',
         V.rays(w * 0.5, h * 0.1, 30, 20, max(w, h), color="#FFE680", op=0.25),
         f'<path d="M-10 {f(h + 10)} L {f(w * 0.2)} {f(h * 0.5)} L {f(w * 0.4)} {f(h * 0.7)} L {f(w * 0.6)} {f(h * 0.44)} L {f(w * 0.84)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(5):
        o.append(E.blaze(w * (0.1 + i * 0.2), h * (0.92 - (i % 2) * 0.1), w * 0.12, h * 0.24, seed + i, n=5))
    return "".join(o)

def fading_leaf(w, h, seed):
    """All our righteousnesses are as a polluted garment: and we all do fade as a leaf; and our iniquities, like the wind, take us
    away: a stained garment cast on the ground, dead leaves blown away across the field by the wind."""
    r = random.Random(seed)
    o = [bg(w, h, "#6A6A7A", "#C8B8A0"), ground(w, h, h * 0.7, "#8A7A5A", dy=0)]
    s = min(1.2, h / 260)
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.9)} C {f(w * 0.14)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.36)} {f(h * 0.82)} C {f(w * 0.38)} {f(h * 0.88)} {f(w * 0.3)} {f(h * 0.94)} {f(w * 0.12)} {f(h * 0.9)} Z" fill="#8A8070" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<ellipse cx="{f(w * r.uniform(0.16, 0.32))}" cy="{f(h * r.uniform(0.82, 0.9))}" rx="{f(6 * s)}" ry="{f(3 * s)}" fill="#4A3A2A"></ellipse>' for _ in range(5)))
    for _ in range(16):
        x = r.uniform(w * 0.4, w); y = r.uniform(h * 0.2, h * 0.8)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(8 * s)}" ry="{f(4 * s)}" fill="{r.choice(["#A8783A", "#8A6A2A", "#C8984A"])}" transform="rotate({r.randint(0, 180)} {f(x)} {f(y)})"></ellipse>')
    for k in range(5):
        y = h * (0.2 + k * 0.12)
        o.append(f'<path d="M{f(w * 0.36)} {f(y)} C {f(w * 0.56)} {f(y - 14)} {f(w * 0.76)} {f(y + 14)} {f(w + 10)} {f(y)}" stroke="#E8E2D6" stroke-width="1.6" fill="none" opacity="0.5"></path>')
    return "".join(o)

def graves_gardens(w, h, seed):
    """Sacrificing in gardens, and burning incense upon bricks; that sit among the graves, and lodge in the secret places: a
    garden by night with incense smoking on a brick altar, tombs cut in the hillside behind (no one drawn)."""
    o = [bg(w, h, "#0B0B2A", "#2A2048"), mk.stars(30, w, h * 0.4, seed),
         f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.34)} {f(w * 0.6)} {f(h * 0.4)} {f(w + 10)} {f(h * 0.36)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2430" stroke="#0D0D0F" stroke-width="2"></path>']
    for x in (0.12, 0.3, 0.74, 0.9):
        o.append(f'<path d="M{f(w * x - 16)} {f(h * 0.58)} L {f(w * x - 16)} {f(h * 0.48)} Q {f(w * x)} {f(h * 0.42)} {f(w * x + 16)} {f(h * 0.48)} L {f(w * x + 16)} {f(h * 0.58)} Z" fill="#0A0810" stroke="#0D0D0F" stroke-width="1.6"></path>')
    s = min(1.0, h / 280); cx, b = w * 0.52, h * 0.88
    for k in range(3):
        for j in range(4 - k):
            o.append(f'<rect x="{f(cx - 40 * s + j * 20 * s + k * 10 * s)}" y="{f(b - (k + 1) * 12 * s)}" width="{f(20 * s)}" height="{f(12 * s)}" fill="#8A4A2A" stroke="#0D0D0F" stroke-width="1"></rect>')
    o.append(smoke(cx, b - 40 * s, 7, seed, r0=8 * s, color="#8A7A98", op=0.5) + E.blaze(cx, b - 36 * s, 16 * s, 16 * s, seed, n=3))
    for x in (0.2, 0.42, 0.66, 0.84):
        o.append(J.oak(w * x, h * 0.96, min(0.36, h / 700), seed=int(x * 100)).replace("#3F8A44", "#1F3A2A").replace("#2E6A32", "#1A2E22").replace("#5E8F26", "#2A3A1A"))
    return "".join(o)

def cluster(w, h, seed):
    """As the new wine is found in the cluster, and one saith, Destroy it not, for a blessing is in it: a vine stripped bare but for
    one great cluster of grapes left hanging, light on it."""
    o = [bg(w, h, "#C8B898", "#F3E8C8"), ground(w, h, h * 0.8, "#9A8A5A", dy=0)]
    s = min(1.4, h / 220)
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.3)} L {f(w * 0.9)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>'
             f'<path d="M{f(w * 0.2)} {f(h * 0.9)} C {f(w * 0.18)} {f(h * 0.6)} {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.3)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="{f(8 * s)}" fill="none"></path>')
    o.append(V.rays(w * 0.56, h * 0.5, 20, 10, w * 0.3, color="#FFF4C2", op=0.4) + N.grapes(w * 0.56, h * 0.3, 0.9 * s, seed))
    return "".join(o)

def sharon_fold(w, h, seed):
    """Sharon shall be a fold of flocks, and the valley of Achor a place for herds to lie down in: a green plain with a sheepfold
    full of sheep, cattle lying down in the valley beyond."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FC8E8", "#F8F0D0"), hills(w, h, h * 0.44, seed, color="#8AB06A", amp=8), ground(w, h, h * 0.52, "#9CCB5E", dy=0)]
    k = min(0.5, h / 520)
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.8)}" rx="{f(w * 0.22)}" ry="{f(h * 0.12)}" fill="none" stroke="#B8A88A" stroke-width="{f(8 * k)}"></ellipse>')
    for _ in range(9):
        o.append(E.sheep(w * 0.3 + r.uniform(-w * 0.16, w * 0.16), h * 0.8 + r.uniform(-h * 0.06, h * 0.08), k * 0.6, flip=r.random() < 0.5))
    for i in range(3):
        o.append(S1.cow(w * (0.66 + i * 0.1), h * (0.66 + (i % 2) * 0.06), k * 0.7, color=["#8A5A30", "#C9A27A", "#6A4A2A"][i], low=True))
    return "".join(o)

def fortune_table(w, h, seed):
    """Ye that prepare a table for Fortune, and that fill up mingled wine unto Destiny: a table spread before two small idols in a
    dark room, wine-cups filled, lamps burning."""
    from genesis.art4 import clay_lamp
    o = [rect(w, h, "#2A1A24"), ground(w, h, h * 0.86, "#1A1214", dy=0)]
    s = min(1.2, h / 240); ty = h * 0.66
    o.append(f'<rect x="{f(w * 0.16)}" y="{f(ty)}" width="{f(w * 0.68)}" height="{f(14 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.2)}" y="{f(ty + 14 * s)}" width="{f(8 * s)}" height="{f(h * 0.86 - ty - 14 * s)}" fill="#5A3A1E"></rect><rect x="{f(w * 0.78)}" y="{f(ty + 14 * s)}" width="{f(8 * s)}" height="{f(h * 0.86 - ty - 14 * s)}" fill="#5A3A1E"></rect>')
    o.append(idol_fig(w * 0.34, ty, 0.6 * s, col="#E8B830") + idol_fig(w * 0.66, ty, 0.6 * s, col="#C8C8D0"))
    o.append(label(w * 0.34, ty - 100 * s, "FORTUNE", "#E8B830", 10) + label(w * 0.66, ty - 100 * s, "DESTINY", "#C8C8D0", 10))
    for x in (0.46, 0.54):
        o.append(f'<path d="M{f(w * x - 8 * s)} {f(ty - 20 * s)} L {f(w * x + 8 * s)} {f(ty - 20 * s)} L {f(w * x + 3 * s)} {f(ty - 6 * s)} L {f(w * x + 3 * s)} {f(ty)} L {f(w * x - 3 * s)} {f(ty)} L {f(w * x - 3 * s)} {f(ty - 6 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
                 f'<ellipse cx="{f(w * x)}" cy="{f(ty - 19 * s)}" rx="{f(7 * s)}" ry="{f(2 * s)}" fill="#7A0A2A"></ellipse>')
    o.append(clay_lamp(w * 0.22, ty, 0.6 * s) + clay_lamp(w * 0.78, ty, 0.6 * s))
    return "".join(o)

def new_heavens(w, h, seed):
    """Behold, I create new heavens and a new earth; and the former things shall not be remembered: a clear new sky at morning over
    a fresh green earth, rivers and hills, Jerusalem shining on its hill."""
    r = random.Random(seed)
    o = [bg(w, h, "#5AA8E8", "#FFF4D8"), V.rays(w * 0.5, h * 0.5, 48, 20, max(w, h) * 1.2, color="#FFFFFF", op=0.3), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.07)}" fill="#FFF8E0"></circle>',
         hills(w, h, h * 0.56, seed, color="#6AAA4A", amp=12, step=70), J.city_hill(w * 0.5, h * 0.62, w * 0.2, h * 0.16, seed),
         ground(w, h, h * 0.66, "#8ACB5E", dy=0), f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.88)} {f(w + 10)} {f(h * 0.78)}" stroke="#2C9DB8" stroke-width="{f(max(6, h * 0.025))}" fill="none"></path>']
    for _ in range(40):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.7, h))}" r="{f(r.uniform(2, 4))}" fill="{r.choice(["#E8406A", "#FFD23F", "#F3EFE6"])}"></circle>')
    return "".join(o)

def build_plant(p, w, h, seed):
    """They shall build houses, and inhabit them; and they shall plant vineyards, and eat the fruit of them: new houses with families
    at their doors, vineyards in fruit on the slope behind, an old man and a child together."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C8"), hills(w, h, h * 0.42, seed, color="#8AA05A", amp=8), vines(w * 0.04, w * 0.96, h * 0.56, h * 0.44, seed, rows=2),
         ground(w, h, h * 0.66, "#C8B888", dy=0)]
    for i in range(3):
        x = w * (0.08 + i * 0.3)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.5)}" width="{f(w * 0.18)}" height="{f(h * 0.3)}" fill="#E0D0B0" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + w * 0.07)}" y="{f(h * 0.62)}" width="{f(w * 0.04)}" height="{f(h * 0.18)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    s = fit(b, max(h * 0.5, b - 150))
    o.append(man(p, w * 0.32, b, s, "#F3EFE6") + S1.boy(p, w * 0.38, b, s * 0.55) + woman(p, w * 0.66, b, s, "#C2456A") + man(p, w * 0.9, b, s, "#2E6B8A", flip=True))
    return "".join(o)

def peace_mountain(p, w, h, seed):
    """The wolf and the lamb shall feed together, and the lion shall eat straw like the ox; and dust shall be the serpent's food.
    They shall not hurt nor destroy in all my holy mountain (the peaceable kingdom)."""
    return peaceable(p, w, h, seed)

def throne_footstool(w, h, seed):
    """Heaven is my throne, and the earth is my footstool: what manner of house will ye build unto me?: the curve of the earth far
    below, and above it in the heavens an empty throne in blinding light (no one drawn)."""
    o = [rect(w, h, "#05050A"), mk.stars(80, w, h, seed), V.rays(w * 0.5, h * 0.36, 40, 20, max(w, h), color="#FFD23F", op=0.22)]
    cx, cy, R = w * 0.5, h + max(w, h) * 0.9, max(w, h) * 1.25
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#1F5A8A" stroke="#8FD0E2" stroke-width="3"></circle>')
    s = min(1.6, h / 200)
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.36)}" r="{f(min(w, h) * 0.18)}" fill="#FFF4C2" opacity="0.4"></circle>' + S3.throne(w * 0.5, h * 0.5, 0.7 * s))
    return "".join(o)

def land_born(p, w, h, seed):
    """Shall a land be born in one day? shall a nation be brought forth at once? for as soon as Zion travailed, she brought forth
    her children: Zion at sunrise with the new-born held up, a crowd of children pouring out of her gates."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#6A7ABA", "#FFE0A8"), V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.35)]
    o.append(S4.gatehouse(w * 0.5, h * 0.7, min(w * 0.6, h * 1.2), h * 0.54, lit=True))
    o.append(ground(w, h, h * 0.7, "#C8A878", dy=0))
    s = fit(b, max(h * 0.5, b - 150))
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.12 + i * 0.09); y = b - r.uniform(0, h * 0.12)
        o.append(S1.boy(p, x, y, s * 0.5 * (0.8 + (y - h * 0.7) / (b - h * 0.7) * 0.3)))
    return "".join(o)

def brethren_brought(p, w, h, seed):
    """They shall bring all your brethren out of all the nations for an oblation unto Jehovah, upon horses, and in chariots, and in
    litters, and upon mules, and upon swift beasts, to my holy mountain Jerusalem: a great procession winding up to the city —
    riders, a chariot, a litter borne on poles, mules and dromedaries."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FB0D8", "#FFE8B8"), J.city_hill(w * 0.88, h * 0.5, w * 0.14, h * 0.2, seed), K1.temple_front(w * 0.88, h * 0.32, min(w * 0.06, h * 0.14), seed),
         ground(w, h, h * 0.56, "#C8B080", dy=0)]
    k = min(0.42, h / 700)
    o.append(E3.horse(w * 0.12, b, k, color="#5A3A22") + E3.chariot(w * 0.3, b, k, color="#8A5A2A", driver="#1F5FAD"))
    s = fit(b, max(h * 0.5, b - 150))
    lx = w * 0.48
    o.append(man(p, lx - 40 * s, b, s, "#6A5A3A", up=[(-22, -158), (-6, -176), (6, -190)]) + man(p, lx + 40 * s, b, s, "#4A5A6A", up=[(-22, -158), (-6, -176), (6, -190)])
             + f'<rect x="{f(lx - 60 * s)}" y="{f(b - 230 * s)}" width="{f(120 * s)}" height="{f(40 * s)}" fill="#7A2A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(lx - 80 * s)} {f(b - 190 * s)} L {f(lx + 80 * s)} {f(b - 190 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>')
    o.append(N.ass(w * 0.66, b - 10, k * 1.2) + J1.camel(w * 0.78, b - 20, k * 1.1, color="#B5844A"))
    return "".join(o)

def outside_valley(w, h, seed):
    """They shall go forth, and look upon the dead bodies of the men that have transgressed against me: for their worm shall not
    die, neither shall their fire be quenched: the city wall above, and the deep valley outside it at dusk, a fire smouldering and
    smoke rising, nothing more drawn (66:24 told in words only)."""
    o = [bg(w, h, "#2A1A2A", "#8A4A3A"), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w * 0.5)}" height="{f(h * 0.3)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>']
    for i in range(7):
        o.append(f'<rect x="{f(i * w * 0.075)}" y="{f(h * 0.06)}" width="{f(w * 0.04)}" height="{f(h * 0.05)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<path d="M-10 {f(h * 0.4)} L {f(w * 0.36)} {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.86)} L {f(w * 0.66)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.44)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2420" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(E.blaze(w * 0.5, h * 0.88, w * 0.14, h * 0.16, seed, n=6) + smoke(w * 0.52, h * 0.7, 9, seed, r0=h * 0.04, spread=20, color="#2A1A1A", op=0.7))
    return "".join(o)
