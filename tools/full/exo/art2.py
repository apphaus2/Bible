"""New drawings for Exodus chapter 2 (Exodus 5–8): straw and stubble, the officers beaten, the Nile and the river of blood,
frogs in Pharaoh's bedchamber, the heaps of frogs, the land of Goshen set apart from the swarms of flies."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, judges1 as G1, egypt as EG
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, city, SKIN
from genesis.art3 import sun, label, man, woman
from exo import art as A
def f(v): return f"{v:.1f}"

OFFICER = F("adam", skin="#B98A6E", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A5A3A", cord=True, brow="sorrow", sweat=True, light="#FFC14D")
OFFICER_ANGRY = F("adam", skin="#B98A6E", shadow="#5E3A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A5A3A", cord=True, brow="scowl", light="#FF6A4A")
MAGICIAN, MAGICIAN_FEAR = A.tok("MAGICIAN"), A.tok("MAGICIAN_FEAR")

def officer(p, x, y, s, flip=False, up=None):
    """An officer of the children of Israel: a Hebrew set over the brick-makers, olive headcloth."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#6A5A3A", sw=3, flip=flip, up=up, extra=A.headcloth("#8A7A4A", cord="#2A1A10") + A.BLACK_BEARD)

def magician(p, x, y, s, flip=False, up=None):
    """A magician of Egypt: black-and-white striped headcloth, white robe, a rod."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth="#E8E2D6", sw=3, flip=flip, up=up,
                     extra=T.NEMES_BLUE.replace("#E8B830", "#F3EFE6").replace("#1F5FAD", "#0D0D0F"))

def beaten(p, w, h, seed):
    """The officers were beaten: two officers bowed under the taskmaster's rod among the drying bricks."""
    r = random.Random(seed); b = h * 0.88
    o = [sun(w * 0.86, h * 0.16, 16, color="#FFF4C2", op=0.3), ground(w, h, b, "#C8A06A", dy=0)]
    for row in range(3):
        for i in range(10):
            x = w * 0.04 + i * w * 0.042 + (row % 2) * 8; y = b - 12 - row * 13
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.036)}" height="11" fill="#A85A32" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(E.kneel(w * 0.58, b, 0.62, color="#6A5A3A", skin="#8A5A3E") + E.kneel(w * 0.7, b + 4, 0.56, color="#5A3A22", skin="#8A5A3E"))
    o.append(A.taskmaster(p, w * 0.86, b, fit(b, h * 0.36), flip=True, up=[(-22, -158), (-4, -196), (14, -230)]))
    return "".join(o)

def stubble(p, w, h, seed):
    """Gather stubble for straw: the people scattered over a reaped field, bent double, bundles on their backs."""
    r = random.Random(seed); b = h * 0.62
    o = [sun(w * 0.82, h * 0.18, 14, op=0.3), ground(w, h, b, "#C8A06A", dy=0)]
    o += [f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-3, 3))} -9" stroke="#8A6A3A" stroke-width="1.6"></path>' for x, y in [(r.uniform(0, w), r.uniform(b + 4, h)) for _ in range(160)]]
    for i in range(7):
        x, y = r.uniform(w * 0.04, w * 0.96), r.uniform(b + 20, h * 0.98)
        o.append(E.kneel(x, y, 0.2 + 0.3 * (y - b) / (h - b), color=r.choice(A.HEBREW), skin="#8A5A3E", flip=r.random() < 0.5))
    return "".join(o)

def palace_gate(p, w, h, seed, cast=()):
    """Before Pharaoh's palace: a pylon gate with banners, a paved way."""
    b = h * 0.88
    o = [sun(w * 0.9, h * 0.16, 14, op=0.25)]
    for x in (0.36, 0.64):
        o.append(f'<path d="M{f(w * x - w * 0.12)} {f(b)} L {f(w * x - w * 0.1)} {f(h * 0.14)} L {f(w * x + w * 0.1)} {f(h * 0.14)} L {f(w * x + w * 0.12)} {f(b)} Z" fill="#D8B878" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<path d="M{f(w * x - w * 0.1)} {f(h * 0.22)} L {f(w * x + w * 0.1)} {f(h * 0.22)}" stroke="#1F5FAD" stroke-width="6"></path>')
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(h * 0.3)}" width="{f(w * 0.08)}" height="{f(b - h * 0.3)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, b, "#C8B080", dy=0))
    return "".join(o) + "".join(T.figure(p, c[0], w * c[1], b, fit(b, h * c[2]), flip=c[3] if len(c) > 3 else False, pose=c[4] if len(c) > 4 else None) for c in cast)

def patriarchs(p, w, h, seed):
    """I appeared unto Abraham, unto Isaac, and unto Jacob: three robed old men under the stars, each by his tent."""
    b = h * 0.88
    o = [mk.stars(70, w, h * 0.7, seed), hills(w, h, b - 8, seed, color="#1A1430", amp=8), ground(w, h, b, "#1A1430", dy=0)]
    for i, (x, c) in enumerate(((0.22, "#3A5A8A"), (0.5, "#7A4A2E"), (0.78, "#8A3A5A"))):
        o.append(A.black_tent(w * x - 40, b, w * 0.16, h * 0.18))
        o.append(mk.person(p, round(w * x + 30), round(b), fit(b, h * 0.42), body=SKIN, cloth=c, sw=3, extra=Y.WHITE_BEARD, up=T.POSES["raise"] if i == 0 else None))
        o.append(label(w * x + 30, b + 16 if b + 16 < h else h - 4, ["ABRAHAM", "ISAAC", "JACOB"][i], "#FFD23F", 9))
    return "".join(o)

def river(p, w, h, seed, blood=False, cast=(), dead=False, base=0.86):
    """The river of Egypt: the Nile between reed beds and palms, pyramids beyond; blood=True turns it red."""
    r = random.Random(seed); b = h * base; wy = h * 0.5
    water = ("#8A0E16", "#B5121B") if blood else ("#1F6F9A", "#2C9DB8")
    o = [sun(w * 0.86, h * 0.16, 14, op=0.25), EG.pyramid(w * 0.74, wy, w * 0.2, h * 0.2), EG.pyramid(w * 0.86, wy, w * 0.12, h * 0.12),
         f'<rect x="-10" y="{f(wy)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="{water[0]}"></rect>']
    o += [f'<path d="M{f(x)} {f(y)} l 30 0" stroke="{water[1]}" stroke-width="3"></path>' for x, y in [(r.uniform(0, w), r.uniform(wy + 6, wy + h * 0.18)) for _ in range(14)]]
    if dead: o += [E2.fish(r.uniform(w * 0.05, w * 0.95), r.uniform(wy + 8, wy + h * 0.17), r.uniform(0.5, 0.8), rot=r.choice([170, 190, 160])) for _ in range(8)]
    o.append(E.reeds(-10, w * 0.24, wy + h * 0.2, h * 0.2, 12, seed) + E.reeds(w * 0.6, w + 10, wy + h * 0.2, h * 0.18, 10, seed + 1))
    o.append(G1.palm(w * 0.08, wy + h * 0.18, h / 300))
    o.append(ground(w, h, wy + h * 0.2, "#C8A06A", dy=0))
    o += [T.figure(p, c[0], w * c[1], b, fit(b, h * c[2]), flip=c[3] if len(c) > 3 else False, pose=c[4] if len(c) > 4 else None) for c in cast]
    return "".join(o)

def bedchamber(w, h, seed):
    """Into thy bedchamber, and upon thy bed, and into thine ovens: Pharaoh's gilded bed and the ovens, frogs on everything."""
    b = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1F3F7A"></rect>',
         E2.columns([w * 0.06, w * 0.94], -10, b, 34, color="#E8B830", band="#1F5FAD"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="40" fill="#8A6A4A"></rect>']
    o.append(f'<path d="M{f(w * 0.14)} {f(b)} L {f(w * 0.16)} {f(b - h * 0.3)} L {f(w * 0.6)} {f(b - h * 0.3)} L {f(w * 0.6)} {f(b)}" fill="none" stroke="#0D0D0F" stroke-width="5"></path>'
             f'<rect x="{f(w * 0.14)}" y="{f(b - h * 0.36)}" width="{f(w * 0.48)}" height="{f(h * 0.12)}" rx="8" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.12)} {f(b - h * 0.5)} L {f(w * 0.16)} {f(b - h * 0.24)}" stroke="#E8B830" stroke-width="10" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.7)} {f(b)} C {f(w * 0.7)} {f(b - h * 0.36)} {f(w * 0.9)} {f(b - h * 0.36)} {f(w * 0.9)} {f(b)} Z" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.76)} {f(b)} C {f(w * 0.76)} {f(b - h * 0.14)} {f(w * 0.84)} {f(b - h * 0.14)} {f(w * 0.84)} {f(b)} Z" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(E2.frogs(9, w * 0.16, w * 0.6, b - h * 0.36, b - h * 0.3, seed, smin=0.5, smax=0.8))
    o.append(E2.frogs(14, w * 0.02, w * 0.98, b + 6, h, seed + 1, smin=0.7, smax=1.2))
    o.append(E2.frogs(4, w * 0.7, w * 0.9, b - h * 0.36, b - h * 0.2, seed + 2, smin=0.5, smax=0.7))
    return "".join(o)

def frog_heaps(w, h, seed):
    """They gathered them together in heaps; and the land stank: grey heaps of dead frogs, a haze over the village."""
    r = random.Random(seed); b = h * 0.86
    o = [sun(w * 0.84, h * 0.2, 14, color="#E8D8A0", op=0.2), city(w * 0.7, b - 10, w * 0.5, h * 0.4, seed, color="#A88A5A", lit="#FFC14D", wall="#B89A6A"), ground(w, h, b, "#B8A06A", dy=0)]
    for x, s in ((0.22, 1.0), (0.5, 0.8), (0.8, 0.9)):
        o.append(f'<path d="M{f(w * x - 80 * s)} {f(b + 6)} C {f(w * x - 50 * s)} {f(b - 70 * s)} {f(w * x + 50 * s)} {f(b - 70 * s)} {f(w * x + 80 * s)} {f(b + 6)} Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
        o.append(E2.frogs(8, w * x - 60 * s, w * x + 60 * s, b - 46 * s, b, seed + int(x * 10), smin=0.4 * s, smax=0.6 * s).replace("#5E8F26", "#7A8A5A"))
    o += [f'<path d="M{f(x)} {f(b - 60)} c 8 -14 -8 -24 0 -40 c 8 -14 -6 -22 2 -34" fill="none" stroke="#8A9A5A" stroke-width="3" opacity="0.6"></path>' for x in (w * 0.2, w * 0.26, w * 0.5, w * 0.78, w * 0.84)]
    return "".join(o)

def goshen_divide(w, h, seed):
    """I will put a division between my people and thy people: Goshen green and clear, Egypt dark with swarms of flies."""
    b = h * 0.86; mid = w * 0.46
    o = [f'<rect x="-10" y="-10" width="{f(mid + 10)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>',
         f'<rect x="{f(mid)}" y="-10" width="{f(w - mid + 10)}" height="{f(h + 20)}" fill="#5A4A3A"></rect>',
         sun(w * 0.2, h * 0.2, 14, op=0.3), ground(w, h, b, "#9CCB5E", dy=0),
         f'<rect x="{f(mid)}" y="{f(b)}" width="{f(w - mid + 10)}" height="{f(h - b + 10)}" fill="#8A7A5A"></rect>',
         "".join(A.black_tent(w * x, b, w * 0.12, h * 0.14) for x in (0.1, 0.26)),
         Z.flock(w * 0.02, w * 0.42, b + 6, h * 0.98, 7, seed, cows=0.3, smin=0.14, smax=0.22),
         EG.pyramid(w * 0.8, b, w * 0.3, h * 0.36),
         E2.swarm(160, w * 0.74, h * 0.5, w * 0.26, h * 0.42, seed, smin=0.5, smax=1.1),
         f'<path d="M{f(mid)} -10 L {f(mid)} {f(h + 10)}" stroke="#FFD23F" stroke-width="4" stroke-dasharray="12 8"></path>',
         label(w * 0.23, h * 0.94, "GOSHEN", "#0D0D0F", 11), label(w * 0.73, h * 0.94, "EGYPT", "#F3EFE6", 11)]
    return "".join(o)

def clear_sky(p, w, h, seed):
    """There remained not one: the palace roofs under a clean sky, the last flies gone."""
    b = h * 0.86
    return (sun(w * 0.8, h * 0.22, 18, op=0.35) + city(w * 0.5, b, w * 0.9, h * 0.5, seed, color="#C8A06A", lit="#FFC14D", wall="#D8B878")
            + EG.pyramid(w * 0.14, b - h * 0.2, w * 0.14, h * 0.14) + ground(w, h, b, "#C8A06A", dy=0))
