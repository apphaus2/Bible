"""Drawings for Ezekiel 35–37: mount Seir made desolate; the mountains of Israel shooting forth their branches, tilled and
sown, the cities inhabited; clean water sprinkled; the land become like the garden of Eden; the flocks of Jerusalem in her
appointed feasts; the valley of dry bones — a field of white bones, the bones come together bone to its bone, the wind from
the four winds, and an exceeding great army standing upon their feet; the graves opened; the two sticks made one; and the
sanctuary in the midst of them for evermore."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art12 import *
from ezk.art12 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1

BONE = "#F3EFE6"

def seir(w, h, seed):
    """Mount Seir a perpetual desolation: red mountains of Edom, empty cities on their heights, smoke drifting."""
    o = [bg(f"sr{seed}", w, h, [(0, "#5A2A2A"), (1, "#E8A070")])]
    for layer, col in enumerate(("#A84A3A", "#8A3A2A", "#6A2A1A")):
        svg, pk = ridge(w, h, h * (0.42 + layer * 0.18), 3 + layer, seed + layer, h * 0.18, col)
        o.append(svg)
        if layer == 1:
            for px, py in pk: o.append(rubble(px - 20, px + 20, py + 10, 14, seed + int(px)))
    o.append(smoke(w * 0.3, h * 0.5, 6, seed, color="#3A2A2A", op=0.4, k=h / 400) + smoke(w * 0.72, h * 0.46, 6, seed + 1, color="#3A2A2A", op=0.4, k=h / 400))
    return "".join(o)

def tilled(p, w, h, seed):
    """Ye shall be tilled and sown, and the cities shall be inhabited: green mountains, furrowed fields, a ploughman with his
    oxen, the cities builded on the hills."""
    o = [mk.defs(p, *ALL), mountains(w, h, seed, "fruitful")]
    o.append(f'<path d="M-10 {f(h * 0.82)} L {f(w * 0.55)} {f(h * 0.8)} L {f(w * 0.55)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(8): o.append(f'<path d="M-10 {f(h * (0.84 + i * 0.022))} L {f(w * 0.55)} {f(h * (0.82 + i * 0.024))}" stroke="#5A4A2A" stroke-width="1.6"></path>')
    for i in range(3): o.append(house(w * (0.66 + i * 0.1), h * 0.72, w * 0.08, h * 0.1, color="#C8A878"))
    k = min(0.8, h / 300)
    o.append(S1.cow(w * 0.3, h * 0.9, k * 0.6) if hasattr(S1, "cow") else "")
    s = min(h * 0.4 / 200, 0.7)
    o.append(man(p, w * 0.14, h * 0.92, s, "#6A5A3A"))
    return "".join(o)

def sprinkle(w, h, seed):
    """I will sprinkle clean water upon you, and ye shall be clean: clear water falling in a bright arc of drops from a basin
    over the dry ground, the ground turning green where it falls."""
    r = random.Random(seed)
    o = [bg(f"sp{seed}", w, h, [(0, "#1A3A5A"), (1, "#8FD0E2")]), ground(w, h, h * 0.8, "#8A6A4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.82)} C {f(w * 0.45)} {f(h * 0.78)} {f(w * 0.75)} {f(h * 0.8)} {f(w * 0.95)} {f(h * 0.84)} L {f(w * 0.95)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#6AA04A"></path>')
    k = min(1.4, h / 240)
    o.append(P(f"M{f(w * 0.12)} {f(h * 0.4)} L {f(w * 0.26)} {f(h * 0.4)} L {f(w * 0.23)} {f(h * 0.5)} L {f(w * 0.15)} {f(h * 0.5)} Z", "#B87333", 2.2))
    for i in range(36):
        t = r.uniform(0, 1); x = w * (0.26 + 0.6 * t); y = h * (0.42 - 0.2 * math.sin(math.pi * t) + 0.36 * t) + r.uniform(-10, 10)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(2.4 * k)}" ry="{f(4 * k)}" fill="#E8F6FA" stroke="#2C9DB8" stroke-width="1"></ellipse>')
    return "".join(o)

def eden_land(w, h, seed):
    """This land that was desolate is become like the garden of Eden; and the waste cities are fenced and inhabited: green
    fields and trees, a walled city on its hill."""
    o = [mountains(w, h, seed, "fruitful")]
    o.append(J.city_hill(w * 0.74, h * 0.8, w * 0.24, h * 0.2, seed))
    for i in range(5): o.append(tree(w * (0.06 + i * 0.1), h * 0.96, h * 0.003, color="#2E8A3A", seed=seed + i))
    return "".join(o)

def feast_flocks(w, h, seed):
    """As the flock for sacrifice, as the flock of Jerusalem in her appointed feasts, so shall the waste cities be filled with
    flocks of men: Jerusalem by day, the flocks thronging up to the city."""
    o = [jerusalem("ff", w, h, seed, mode="day")]
    o.append(flock(w * 0.02, w * 0.98, h * 0.9, h * 0.99, 18, seed, cows=0.0))
    return "".join(o)

def bone(x, y, L, a, k=1.0):
    """One dry bone: a white shaft with knobbed ends."""
    dx, dy = math.cos(a) * L / 2, math.sin(a) * L / 2
    o = (f'<path d="M{f(x - dx)} {f(y - dy)} L {f(x + dx)} {f(y + dy)}" stroke="#0D0D0F" stroke-width="{f(6.5 * k)}" stroke-linecap="round"></path>'
         f'<path d="M{f(x - dx)} {f(y - dy)} L {f(x + dx)} {f(y + dy)}" stroke="{BONE}" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>')
    for s in (-1, 1):
        o += f'<circle cx="{f(x + s * dx)}" cy="{f(y + s * dy)}" r="{f(3.6 * k)}" fill="{BONE}" stroke="#0D0D0F" stroke-width="1.2"></circle>'
    return o

def valley_bones(p, w, h, seed, stage=0):
    """The valley full of bones, very many and very dry (stage 0, Ezekiel standing among them); the bones come together, bone
    to its bone (stage 1: frames of bones lying in rows); the wind from the four winds (stage 2: winds streaming in, light);
    an exceeding great army standing upon their feet (stage 3)."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(f"vb{seed}{stage}", w, h, [(0, "#3A3A5A" if stage < 3 else "#5A7AA8"), (1, "#C8A878" if stage < 3 else "#F3E0B0")])]
    o.append(P(f"M-10 {f(h * 0.5)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.56)} L -10 {f(h * 0.7)} Z", "#7A6A5A", 2))
    o.append(P(f"M{f(w + 10)} {f(h * 0.46)} L {f(w * 0.78)} {f(h * 0.28)} L {f(w * 0.62)} {f(h * 0.56)} L {f(w + 10)} {f(h * 0.7)} Z", "#7A6A5A", 2))
    o.append(ground(w, h, h * 0.56, "#B8A07A", dy=0))
    k = min(1.4, h / 300)
    if stage == 0:
        for _ in range(int(w / 8)):
            x = r.uniform(0, w); y = h * r.uniform(0.6, 0.99)
            o.append(bone(x, y, r.uniform(14, 30) * k * (0.6 + 0.6 * (y / h)), r.uniform(0, math.pi), k * (0.5 + 0.6 * y / h)))
        s = min(h * 0.5 / 200, 1.0)
        o.append(ezek_fig(p, w * 0.66, h * 0.9, s))
    elif stage in (1, 2):
        for row in range(3):
            for i in range(6):
                x = w * (0.08 + i * 0.16) + row * 16; y = h * (0.66 + row * 0.11)
                kk = k * (0.6 + row * 0.2)
                o.append(bone(x, y, 40 * kk, 0.05, kk * 0.8) + bone(x - 34 * kk, y + 2, 18 * kk, 0.2, kk * 0.7) + bone(x + 30 * kk, y - 4, 22 * kk, -0.6, kk * 0.6)
                         + bone(x + 30 * kk, y + 6, 22 * kk, 0.5, kk * 0.6) + f'<circle cx="{f(x - 50 * kk)}" cy="{f(y)}" r="{f(7 * kk)}" fill="{BONE}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
        if stage == 2:
            for a in range(4):
                ang = a * math.pi / 2 + math.pi / 4
                cx, cy = w * 0.5 + math.cos(ang) * w * 0.6, h * 0.5 + math.sin(ang) * h * 0.6
                o.append(f'<path d="M{f(cx)} {f(cy)} Q {f(w * 0.5 + math.cos(ang + 0.6) * w * 0.3)} {f(h * 0.5 + math.sin(ang + 0.6) * h * 0.3)} {f(w * 0.5)} {f(h * 0.6)}" stroke="#E8F0FF" stroke-width="3" fill="none" opacity="0.6" stroke-dasharray="14 8"></path>')
            o.append(glow(f"vbg{seed}", w * 0.5, h * 0.6, w * 0.4, h * 0.3, "#FFF4C2", 0.5))
        else:
            o.append(mk.speed(w * 0.5, h * 0.75, 30, w * 0.1, w * 0.7, seed, color="#3A2A1A", op=0.3))
    else:
        o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.98, h * 0.62, h * 0.99, 40, min(h * 0.2 / 200, 0.5), min(h * 0.4 / 200, 1.0)))
        o.append(V.rays(w * 0.5, -h * 0.1, 20, h * 0.1, h * 1.2, color="#FFF4C2", op=0.15))
    return "".join(o)

def graves_open(p, w, h, seed):
    """I will open your graves, and cause you to come up out of your graves, O my people: rock-hewn tombs on a hillside, their
    stones rolled away and light within, a road leading off toward the hills of Israel."""
    o = [mk.defs(p, *ALL), bg(f"go{seed}", w, h, [(0, "#3A4A7A"), (1, "#F8C890")])]
    o.append(P(f"M-10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.26)} {f(w * 0.5)} {f(h * 0.34)} {f(w * 0.62)} {f(h * 0.5)} L {f(w * 0.62)} {f(h + 10)} L -10 {f(h + 10)} Z", "#8A7A6A", 2.4))
    for i in range(3):
        x = w * (0.1 + i * 0.17); y = h * (0.66 + (i % 2) * 0.08); R = min(w * 0.06, h * 0.12)
        o.append(f'<path d="M{f(x - R)} {f(y + R)} L {f(x - R)} {f(y)} A {f(R)} {f(R)} 0 0 1 {f(x + R)} {f(y)} L {f(x + R)} {f(y + R)} Z" fill="#FFE8A0" stroke="{INK}" stroke-width="2"></path>'
                 + glow(f"gog{seed}{i}", x, y + R * 0.4, R * 1.6, R * 1.2, "#FFE680", 0.6)
                 + f'<circle cx="{f(x + R * 1.7)}" cy="{f(y + R * 0.4)}" r="{f(R * 0.9)}" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></circle>')
    o.append(ground(w, h, h * 0.92, "#A8906A", dy=0))
    o.append(f'<path d="M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.8)} {f(h * 0.7)} L {f(w * 0.86)} {f(h * 0.7)} L {f(w * 0.66)} {f(h + 10)} Z" fill="#D8C8A0"></path>')
    o.append(hills(w * 0.4, h, h * 0.68, seed, "#6A8A5A", amp=8, step=40).replace('<path ', f'<path transform="translate({f(w * 0.62)} 0)" ', 1))
    return "".join(o)

def sticks(w, h, seed, joined=False):
    """Take thee one stick and write upon it, and another stick, and join them one to another into one stick: two rods marked
    with writing (joined=True: made one, bound together, shining)."""
    o = [bg(f"sk{seed}{joined}", w, h, [(0, "#2A2A3A"), (1, "#6A5A4A")])]
    k = min(1.6, h / 200)
    def rod(x0, y0, x1, y1):
        s_ = (f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#0D0D0F" stroke-width="{f(16 * k)}" stroke-linecap="round"></path>'
              f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#B8945A" stroke-width="{f(11 * k)}" stroke-linecap="round"></path>')
        for i in range(6):
            t = 0.2 + i * 0.1; x = x0 + (x1 - x0) * t; y = y0 + (y1 - y0) * t
            s_ += f'<path d="M{f(x - 4 * k)} {f(y - 3 * k)} l {f(5 * k)} {f(2 * k)} l {f(-3 * k)} {f(4 * k)}" stroke="#2A1A10" stroke-width="{f(1.6 * k)}" fill="none"></path>'
        return s_
    if joined:
        o.append(glow(f"skg{seed}", w * 0.5, h * 0.6, w * 0.4, h * 0.3, "#FFE680", 0.5))
        o.append(rod(w * 0.12, h * 0.62, w * 0.5, h * 0.6) + rod(w * 0.5, h * 0.6, w * 0.88, h * 0.58))
        o.append(f'<rect x="{f(w * 0.5 - 12 * k)}" y="{f(h * 0.6 - 12 * k)}" width="{f(24 * k)}" height="{f(24 * k)}" fill="none" stroke="#C8302A" stroke-width="{f(3 * k)}"></rect>')
    else:
        o.append(rod(w * 0.14, h * 0.5, w * 0.62, h * 0.44) + rod(w * 0.38, h * 0.8, w * 0.86, h * 0.74))
    return "".join(o)

def sanctuary_midst(p, w, h, seed):
    """My tabernacle also shall be with them, my sanctuary in the midst of them for evermore: the house standing in the midst
    of the tribes' tents, the glory as light upon it."""
    o = [mk.defs(p, *ALL), bg(f"sm{seed}", w, h, [(0, "#3A4A8A"), (1, "#F3E0B0")])]
    o.append(glory(f"smg{seed}", w * 0.5, h * 0.62, w * 0.12, h * 0.5, seed))
    o.append(K1.temple_front(w * 0.5, h * 0.7, w * 0.34, seed))
    o.append(ground(w, h, h * 0.7, "#C8B080", dy=0))
    o.append(N.camp(16, -10, w + 10, h * 0.76, h * 0.98, seed, color=("#5A3A22", "#6B4A2A", "#3A2214", "#7A5A3A")))
    return "".join(o)
