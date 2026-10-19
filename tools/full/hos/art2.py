"""Drawings for Hosea chapter 2 (Hosea 4–8): the land mourning, the high places under oaks and poplars and terebinths, the
stubborn heifer, the snare at Mizpah and the net upon Tabor (a map), the alarm at Gibeah, Ramah and Beth-aven (a map), the
moth and the rottenness, the lion, the latter rain, the morning cloud and the dew, the baker's oven and the cake not turned,
the silly dove between Egypt and Assyria with the net spread, the deceitful bow, the trumpet and the eagle over the house,
the calf of Samaria broken, the wind sown and the whirlwind reaped, the wild ass alone, the altars multiplied, the fire upon
the cities."""
from hos.art import *
from hos.art import f, K2
import random, math
import exodus5 as V5, joshua1 as J1x
from job.art4 import wild_ass_run
from job.art11 import desert_rain
from pro.art4 import flocks
FIELD = "#12102A"

def land_mourns(w, h, seed):
    """The land mourns: a parched field, withered stalks, the birds of the heavens flying away, the shore of the sea emptied."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#C8A880", "#F0D8B0"), sun(w * 0.2, h * 0.2, max(10, h * 0.05), color="#FFC14D", op=0.3),
         hills(w, h, h * 0.5, seed, "#B89A6A", amp=12, step=110), ground(w, h, h * 0.62, "#C8A070", dy=0)]
    for i in range(40):
        x = r.uniform(0, w); y = r.uniform(h * 0.66, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-4, 4))} {f(-r.uniform(8, 20))} l {f(r.uniform(2, 8))} {f(r.uniform(2, 6))}" stroke="#8A6A3A" stroke-width="1.8" fill="none"></path>')
    for i in range(7): o.append(bird(w * (0.5 + i * 0.07), h * (0.14 + (i % 3) * 0.05), 0.9, "#3A2A1A"))
    return "".join(o)

def oaks(p, w, h, seed):
    """Upon the tops of the mountains and on the hills, under oaks and poplars and terebinths, incense burning on altars."""
    o = [land(w, h, seed, tone="dusk", olives=0, horizon=0.4)]
    k = min(1.4, h / 260)
    for i, (x, kind, c) in enumerate(((0.12, "round", "#2E5A3A"), (0.34, "tall", "#3A6A3A"), (0.6, "round", "#2A4A2A"), (0.86, "tall", "#3A5A2A"))):
        o.append(tree(w * x, h * 0.74, k * 1.2, color=c, kind=kind, seed=seed + i))
        ax = w * (x + 0.08)
        o.append(f'<path d="M{f(ax - 12)} {f(h * 0.78)} L {f(ax - 8)} {f(h * 0.78 - 18 * k)} L {f(ax + 8)} {f(h * 0.78 - 18 * k)} L {f(ax + 12)} {f(h * 0.78)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + E.flame(ax, h * 0.78 - 18 * k, 6 * k, 12 * k, 1) + smoke(ax, h * 0.78 - 30 * k, 3, seed + i, color="#C8B8C8", op=0.5, k=k * 0.6))
    return "".join(o)

def heifer(w, h, seed, wind=True):
    """Israel like a stubborn heifer, braced in a large place; the wind wrapping it in its wings."""
    import samuel1 as S1x
    o = [land(w, h, seed, tone="grey", olives=0, horizon=0.42)]
    k = min(0.9, h / 320)
    o.append(S1x.cow(w * 0.5, h * 0.9, k, color="#8A5A3A", low=True))
    if wind:
        for i in range(6):
            y = h * (0.18 + i * 0.08)
            o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 20)} {f(w * 0.6)} {f(y + 20)} {f(w + 10)} {f(y - 10)}" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.6" stroke-dasharray="14 10"></path>')
    return "".join(o)

PL = {"MIZPAH": (0.36, 0.58), "TABOR": (0.56, 0.2), "GIBEAH": (0.42, 0.7), "RAMAH": (0.5, 0.58), "BETH-AVEN": (0.64, 0.46), "SAMARIA": (0.46, 0.4),
      "JERUSALEM": (0.5, 0.74), "GILGAL": (0.7, 0.6), "BETH-EL": (0.54, 0.54)}
def israel_map(w, h, places, icon="", title=""):
    """The land as a technical map, the Jordan on the east and the great sea on the west; places named; icon "net": a net and a
    snare at each place; "horn": a trumpet at each place."""
    o = [grid_bg(w, h),
         f'<path d="M-10 -10 L {f(w * 0.18)} -10 C {f(w * 0.22)} {f(h * 0.4)} {f(w * 0.16)} {f(h * 0.7)} {f(w * 0.12)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.8)} -10 C {f(w * 0.78)} {f(h * 0.3)} {f(w * 0.82)} {f(h * 0.5)} {f(w * 0.78)} {f(h * 0.7)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
         f'<ellipse cx="{f(w * 0.78)}" cy="{f(h * 0.86)}" rx="{f(w * 0.03)}" ry="{f(h * 0.12)}" fill="#2C9DB8"></ellipse>']
    for nm in places:
        x, y = PL[nm]
        o.append(node(w * x, h * y, nm, "#FFD23F", r=6, dy=-12, size=9))
        if icon == "net":
            o.append("".join(f'<path d="M{f(w * x - 16 + i * 8)} {f(h * y + 8)} L {f(w * x - 16 + i * 8 + 12)} {f(h * y + 28)}" stroke="#FF8A6A" stroke-width="1.2"></path>'
                             f'<path d="M{f(w * x - 16 + i * 8 + 12)} {f(h * y + 8)} L {f(w * x - 16 + i * 8)} {f(h * y + 28)}" stroke="#FF8A6A" stroke-width="1.2"></path>' for i in range(4)))
        if icon == "horn":
            o.append(J1x.shofar(w * x + 22, h * y + 10, 0.24, rot=-20))
    if title: o.append(label(w * 0.96, h * 0.08, title, "#F3EFE6", 9, anchor="end"))
    return "".join(o)

def moth(w, h):
    """I am unto Ephraim as a moth, and to the house of Judah as rottenness: a moth and a worm-eaten beam, as a plate."""
    o = [grid_bg(w, h)]
    k = min(1.4, h / 160)
    cx, cy = w * 0.3, h * 0.5
    for sx in (-1, 1):
        o.append(f'<path d="M{f(cx)} {f(cy)} C {f(cx + sx * 40 * k)} {f(cy - 40 * k)} {f(cx + sx * 70 * k)} {f(cy - 20 * k)} {f(cx + sx * 60 * k)} {f(cy + 4 * k)} C {f(cx + sx * 50 * k)} {f(cy + 30 * k)} {f(cx + sx * 20 * k)} {f(cy + 20 * k)} {f(cx)} {f(cy)} Z" fill="#B8A890" fill-opacity="0.5" stroke="#E8D8B0" stroke-width="2"></path>')
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(5 * k)}" ry="{f(20 * k)}" fill="#8A7A6A" stroke="#E8D8B0" stroke-width="1.6"></ellipse>' + label(cx, h * 0.9, "EPHRAIM · A MOTH", CYAN, 9))
    bx = w * 0.72
    o.append(f'<rect x="{f(bx - 80 * k)}" y="{f(cy - 14 * k)}" width="{f(160 * k)}" height="{f(28 * k)}" fill="#6A4A2A" fill-opacity="0.5" stroke="#C8A06A" stroke-width="2"></rect>')
    r = random.Random(3)
    o.append("".join(f'<circle cx="{f(bx + r.uniform(-74, 74) * k)}" cy="{f(cy + r.uniform(-10, 10) * k)}" r="{f(r.uniform(2, 5) * k)}" fill="#0B1A2E" stroke="#C8A06A" stroke-width="0.8"></circle>' for _ in range(22)))
    o.append(label(bx, h * 0.9, "JUDAH · ROTTENNESS", CYAN, 9))
    return "".join(o)

def lion_field(w, h, seed):
    """I will be unto Ephraim as a lion, and as a young lion to the house of Judah: two lions as emblems on the dark field."""
    o = [heraldic(w, h, seed)]
    k = min(h / 130, w / 380)
    import judges2 as JG
    k2 = min(h / 300, w / 700)
    o.append(JG.lion(w * 0.14, h * 0.92, k2, roar=True) + JG.lion(w * 0.86, h * 0.92, k2 * 0.8, flip=True, roar=False))
    o.append(label(w * 0.3, h * 0.14, "EPHRAIM · A LION", CYAN, 9) + label(w * 0.7, h * 0.14, "JUDAH · A YOUNG LION", CYAN, 9))
    return "".join(o)

def latter_rain(w, h, seed):
    """He will come unto us as the rain, as the latter rain that watereth the earth: rain sweeping over the green hills at dawn."""
    o = [land(w, h, seed, tone="dawn", olives=3)]
    r = random.Random(seed)
    o.append(f'<path d="M-10 -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h * 0.2)} C {f(w * 0.6)} {f(h * 0.3)} {f(w * 0.3)} {f(h * 0.16)} -10 {f(h * 0.26)} Z" fill="#6A7A8A" opacity="0.8"></path>')
    for i in range(70):
        x = r.uniform(0, w); y = r.uniform(h * 0.2, h * 0.8)
        o.append(f'<path d="M{f(x)} {f(y)} l -5 14" stroke="#C8E8F0" stroke-width="1.4" opacity="0.7"></path>')
    return "".join(o)

def morning_cloud(w, h, seed):
    """Your goodness is as a morning cloud, and as the dew that goeth early away: a thin cloud lifting off the hills at sunrise,
    the dew going up from the grass."""
    from job.art import clouds
    o = [dew_land(w, h, seed), clouds(w, h * 0.42, seed, n=4, color="#FFFFFF", op=0.6, ry=0.04)]
    return "".join(o)

def oven(w, h, seed, cake=False):
    """An oven heated by the baker: a clay oven glowing, the fire stirred; cake=True: a cake upon the coals, burnt on one side
    and raw on the other — a cake not turned."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>',
         f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4030" stroke="#0D0D0F" stroke-width="2"></rect>']
    cx, by = w * 0.5, h * 0.86
    rw, rh = min(w * 0.3, h * 0.7), h * 0.66
    o.append(f'<path d="M{f(cx - rw / 2)} {f(by)} C {f(cx - rw / 2)} {f(by - rh)} {f(cx + rw / 2)} {f(by - rh)} {f(cx + rw / 2)} {f(by)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="3"></path>'
             f'<path d="M{f(cx - rw * 0.2)} {f(by)} C {f(cx - rw * 0.2)} {f(by - rh * 0.4)} {f(cx + rw * 0.2)} {f(by - rh * 0.4)} {f(cx + rw * 0.2)} {f(by)} Z" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + E.blaze(cx, by, rw * 0.36, rh * 0.36, seed, n=4) + V.rays(cx, by - rh * 0.2, 16, 10, w * 0.5, color="#FFC14D", op=0.12))
    if cake:
        k = min(1.6, h / 200)
        x = w * 0.18; y = h * 0.6
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(46 * k)}" ry="{f(18 * k)}" fill="#E8D0A0" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<path d="M{f(x - 46 * k)} {f(y)} A {f(46 * k)} {f(18 * k)} 0 0 0 {f(x + 46 * k)} {f(y)} Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></path>'
                 + label(x, y - 28 * k, "A CAKE NOT TURNED", "#FFD23F", 9))
        x2 = w * 0.84
        o.append(f'<path d="M{f(x2 - 30 * k)} {f(y + 20 * k)} C {f(x2 - 30 * k)} {f(y - 40 * k)} {f(x2 + 30 * k)} {f(y - 40 * k)} {f(x2 + 30 * k)} {f(y + 20 * k)}" fill="none" stroke="#8A847A" stroke-width="2"></path>'
                 + "".join(f'<path d="M{f(x2 - 20 * k + i * 8 * k)} {f(y - 26 * k)} l {f(2 * k)} {f(-14 * k)}" stroke="#C8C2B6" stroke-width="1.6"></path>' for i in range(6))
                 + label(x2, y - 50 * k, "GRAY HAIRS HERE AND THERE", "#C8C2B6", 8))
    return "".join(o)

def silly_dove(w, h, seed):
    """Ephraim like a silly dove, without understanding, fluttering toward Egypt and toward Assyria; a net spread above it."""
    o = [grid_bg(w, h)]
    o.append(node(w * 0.1, h * 0.7, "EGYPT", "#FFD23F", r=6, dy=-12, size=9) + node(w * 0.9, h * 0.3, "ASSYRIA", "#FFD23F", r=6, dy=-12, size=9))
    o.append(route([(w * 0.46, h * 0.56), (w * 0.14, h * 0.68)], color="#8FD0E2") + route([(w * 0.54, h * 0.48), (w * 0.86, h * 0.32)], color="#8FD0E2"))
    k = min(1.4, h / 180)
    o.append(sdove(w * 0.5, h * 0.56, k * 0.9))
    for i in range(9):
        x = w * (0.3 + i * 0.05)
        o.append(f'<path d="M{f(x)} {f(h * 0.08)} L {f(x + w * 0.06)} {f(h * 0.3)}" stroke="#FF8A6A" stroke-width="1.2"></path><path d="M{f(x + w * 0.06)} {f(h * 0.08)} L {f(x)} {f(h * 0.3)}" stroke="#FF8A6A" stroke-width="1.2"></path>')
    o.append(label(w * 0.5, h * 0.06, "I WILL SPREAD MY NET UPON THEM", "#FF8A6A", 8))
    return "".join(o)

def bow_plate(w, h):
    """They are like a deceitful bow: a bow warped and twisted, its arrow falling short."""
    o = [grid_bg(w, h)]
    k = min(1.6, h / 160)
    cx, cy = w * 0.4, h * 0.5
    o.append(f'<path d="M{f(cx - 10 * k)} {f(cy - 60 * k)} C {f(cx + 40 * k)} {f(cy - 40 * k)} {f(cx - 20 * k)} {f(cy + 10 * k)} {f(cx + 30 * k)} {f(cy + 60 * k)}" fill="none" stroke="#C8783A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(cx - 10 * k)} {f(cy - 60 * k)} L {f(cx + 30 * k)} {f(cy + 60 * k)}" stroke="#E8E2D6" stroke-width="1.4"></path>'
             + route([(cx + 20 * k, cy), (w * 0.6, h * 0.66), (w * 0.7, h * 0.86)], color="#FF8A6A") + label(w * 0.72, h * 0.94, "A DECEITFUL BOW", CYAN, 9))
    return "".join(o)

def eagle(x, y, s=1.0, color="#4A3A2A"):
    """An eagle with its wings spread, seen from below as it stoops ((x, y) = its body)."""
    d = ("M-8 0 C -30 -6 -60 -20 -92 -18 L -80 -10 L -88 -4 L -74 0 L -80 6 L -60 6 C -40 8 -20 10 -10 14 L -14 34 L 0 28 L 14 34 L 10 14 "
         "C 20 10 40 8 60 6 L 80 6 L 74 0 L 88 -4 L 80 -10 L 92 -18 C 60 -20 30 -6 8 0 C 8 -10 4 -16 0 -16 C -4 -16 -8 -10 -8 0 Z")
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="{f(2 / s)}" stroke-linejoin="round"></path>'
            '<circle cx="0" cy="-18" r="7" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-3 -14 L 0 -6 L 3 -14 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.8"></path>'
            + "".join(f'<path d="M{sx * a} -8 L {sx * (a + 6)} 2" stroke="#0D0D0F" stroke-width="1" opacity="0.6"></path>' for sx in (-1, 1) for a in (30, 46, 62, 76)) + '</g>')

def trumpet_eagle(w, h, seed):
    """Set the trumpet to thy mouth. As an eagle he cometh against the house of Jehovah: a trumpet of ram's horn raised on the
    hill, a great eagle stooping over the house."""
    o = [land(w, h, seed, tone="grey", olives=1)]
    k = min(1.4, h / 260)
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.5)}" width="{f(w * 0.24)}" height="{f(h * 0.26)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.58)}" y="{f(h * 0.46)}" width="{f(w * 0.28)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(eagle(w * 0.68, h * 0.26, k * 1.3))
    o.append(J1x.shofar(w * 0.22, h * 0.6, k * 0.6, rot=-30))
    return "".join(o)

def calf_broken(w, h, seed, broken=False):
    """The calf of Samaria on its pedestal (the workman made it, and it is no God); broken=True: broken in pieces."""
    o = [K2.sky(w, h, "#3A2A3A", "#8A6A5A"), ground(w, h, h * 0.82, "#5A4A3A", dy=0)]
    k = min(1.4, h / 300)
    if broken:
        o.append(V5.shards(w * 0.5, h * 0.84, k, seed).replace("#B8B2A6", "#E8B830") + f'<path d="M{f(w * 0.36)} {f(h * 0.84)} L {f(w * 0.64)} {f(h * 0.84)} L {f(w * 0.6)} {f(h * 0.76)} L {f(w * 0.4)} {f(h * 0.76)} Z" fill="#6B4A22" stroke="#0D0D0F" stroke-width="2"></path>')
        r = random.Random(seed)
        o.append("".join(f'<path d="M{f(w * 0.5 + r.uniform(-120, 120) * k)} {f(h * 0.82 - r.uniform(0, 20) * k)} l {f(r.uniform(10, 24) * k)} {f(r.uniform(-8, 8) * k)} l {f(r.uniform(-6, 6) * k)} {f(r.uniform(6, 12) * k)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>' for _ in range(14)))
    else:
        o.append(V.rays(w * 0.5, h * 0.5, 20, 10, w * 0.4, color="#FFE680", op=0.12) + V5.calf(w * 0.5, h * 0.84, k, uid=f"cb{seed}"))
    return "".join(o)

def whirlwind_field(w, h, seed):
    """They sow the wind, and they shall reap the whirlwind: a bare sown field, a whirlwind standing up over it, no standing grain."""
    from job.art import whirl
    o = [K2.sky(w, h, "#6A6A7A", "#C8B898"), hills(w, h, h * 0.56, seed, "#8A7A5A", amp=10, step=100), ground(w, h, h * 0.66, "#A88A5A", dy=0)]
    for i in range(7):
        y = h * (0.7 + i * 0.045)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 4)}" stroke="#7A5A3A" stroke-width="2"></path>')
    o.append(whirl(w * 0.6, h * 0.06, h * 0.9, w * 0.2, w * 0.03, seed, color="#C8B8A8", op=0.6))
    return "".join(o)

def altars(w, h, seed):
    """Ephraim hath multiplied altars for sinning: a hillside crowded with altars, smoke from each."""
    r = random.Random(seed)
    o = [land(w, h, seed, tone="dusk", olives=0, horizon=0.36)]
    k = min(1.2, h / 260)
    for i in range(9):
        x = w * (0.06 + i * 0.11); y = h * (0.66 + (i % 3) * 0.1)
        o.append(f'<path d="M{f(x - 14 * k)} {f(y)} L {f(x - 10 * k)} {f(y - 22 * k)} L {f(x + 10 * k)} {f(y - 22 * k)} L {f(x + 14 * k)} {f(y)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + E.flame(x, y - 22 * k, 6 * k, 14 * k, 1) + smoke(x, y - 36 * k, 3, seed + i, color="#9A8A9A", op=0.45, k=k * 0.5))
    return "".join(o)

def fire_cities(w, h, seed):
    """I will send a fire upon his cities, and it shall devour the castles thereof (no one drawn)."""
    o = [K2.sky(w, h, "#2A0A0A", "#8A2A1A"), J.city_hill(w * 0.3, h * 0.9, w * 0.3, h * 0.36, seed), J.city_hill(w * 0.76, h * 0.9, w * 0.24, h * 0.3, seed + 1),
         ground(w, h, h * 0.9, "#2A1A1A", dy=0)]
    o.append(E.blaze(w * 0.3, h * 0.56, w * 0.24, h * 0.3, seed, n=6) + E.blaze(w * 0.76, h * 0.62, w * 0.18, h * 0.24, seed + 2, n=5))
    o.append(smoke(w * 0.3, h * 0.3, 6, seed, color="#3A2A2A", op=0.6, k=min(1.6, h / 260)))
    return "".join(o)
