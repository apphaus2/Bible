"""Drawings for Ezekiel 33–34: the watchman seeing the sword come upon the land; the one that escaped out of Jerusalem;
the waste places of the land; the people sitting before the prophet as before a lovely song (a harp beside them); the
shepherds that feed themselves and the flock scattered upon the mountains; the sheep sought out and gathered into good
pasture (no shepherd drawn — the Lord's searching is the gathering itself); the fat sheep and the lean, the trodden
pasture and the fouled water; the one shepherd, my servant David, with the flock; the covenant of peace — showers in
their season, the trees yielding fruit."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art11 import *
from ezk.art11 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1
from neh.art import ruins
import samuel2 as S2

def watch_sword(p, w, h, seed):
    """When he seeth the sword come upon the land, he blow the trumpet: the watchman on the tower and, far off on the plain,
    the dust of a host coming."""
    o = [watchman(p, w, h, seed)]
    for i in range(8):
        x = w * (0.62 + i * 0.045); y = h * 0.74
        o.append(f'<path d="M{f(x)} {f(y)} l 0 -14" stroke="#2A1A1A" stroke-width="3"></path><path d="M{f(x)} {f(y - 14)} l -2 -6 l 4 0 Z" fill="#C8C8D0"></path>')
    o.append(smoke(w * 0.78, h * 0.72, 5, seed, color="#C8A880", op=0.5, k=h / 400))
    return "".join(o)

def waste_places(w, h, seed):
    """They that inhabit those waste places in the land of Israel: broken walls and a burned gate on the hills of Judah."""
    return ruins(w, h, seed)

def listeners(p, w, h, seed):
    """They sit before thee as my people, and thou art unto them as a very lovely song of one that hath a pleasant voice:
    Ezekiel seated speaking, the people seated before him, a harp leaning by the door."""
    b = h * 0.96
    o = [elders_house(p, w, h, seed)]
    k = min(1.2, h / 260)
    o.append(S2.harp(w * 0.92, b, k * 0.8) if hasattr(S2, "harp") else "")
    return "".join(o)

def scattered(w, h, seed, beast=True):
    """My sheep wandered through all the mountains, and upon every high hill: sheep scattered singly over the mountains, no
    shepherd, a lion watching from the rocks."""
    r = random.Random(seed)
    o = [mountains(w, h, seed, "desolate")]
    k = min(0.7, h / 360)
    for _ in range(9):
        o.append(E.sheep(r.uniform(0.05, 0.95) * w, h * r.uniform(0.66, 0.96), k * r.uniform(0.5, 0.9), flip=r.random() < 0.5))
    if beast: o.append(JJ2.lion(w * 0.78, h * 0.64, k * 0.8, flip=True, roar=False))
    return "".join(o)

def shepherds_feast(p, w, h, seed):
    """Ye eat the fat, and ye clothe you with the wool: the shepherds' tent with a fire and a pot, fleeces piled, the
    shepherds sitting at ease; the flock beyond, untended."""
    o = [mk.defs(p, *ALL), bg(f"sf{seed}", w, h, [(0, "#3A2A4A"), (1, "#E8A070")]), hills(w, h, h * 0.6, seed, "#8A7A5A", amp=10, step=80), ground(w, h, h * 0.68, "#A88A5A", dy=0)]
    o.append(A.black_tent(w * 0.3, h * 0.84, w * 0.3, h * 0.24))
    o.append(E.blaze(w * 0.56, h * 0.9, w * 0.06, h * 0.1, seed, n=4) + f'<path d="M{f(w * 0.53)} {f(h * 0.8)} C {f(w * 0.53)} {f(h * 0.86)} {f(w * 0.59)} {f(h * 0.86)} {f(w * 0.59)} {f(h * 0.8)} Z" fill="#3A3A44" stroke="{INK}" stroke-width="1.6"></path>')
    for i in range(3): o.append(f'<ellipse cx="{f(w * (0.08 + i * 0.05))}" cy="{f(h * 0.92 - i * 6)}" rx="{f(w * 0.04)}" ry="{f(h * 0.03)}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.4"></ellipse>')
    s = min(h * 0.6 / 135, 0.8)
    o.append(seated(w * 0.66, h * 0.96, s, "#7A2A2A", head="#7A2A2A", beard="#2A1A10", flip=True) + seated(w * 0.46, h * 0.96, s, "#5A3A6A", head="#5A3A6A", beard="#3A2A1A"))
    o.append(flock(w * 0.75, w * 0.98, h * 0.66, h * 0.76, 6, seed, cows=0.0))
    return "".join(o)

def fold(w, h, seed):
    """I will seek that which was lost, and bring back that which was driven away: the flock gathered in good pasture upon
    the mountains of Israel, by the watercourses, lying down in a fold."""
    o = [mountains(w, h, seed, "fruitful")]
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.98)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.5)} {f(h * 0.96)} {f(w * 0.7)} {f(h * 0.9)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.96)} L {f(w * 0.56)} {f(h * 0.8)} L {f(w * 0.96)} {f(h * 0.8)} L {f(w * 0.96)} {f(h * 0.96)}" stroke="#8A7A6A" stroke-width="8" fill="none"></path>')
    o.append(flock(w * 0.58, w * 0.94, h * 0.84, h * 0.96, 10, seed + 1, cows=0.0))
    return "".join(o)

def fat_lean(w, h, seed):
    """I will judge between the fat sheep and the lean: a fat ram thrusting with his horns, lean sheep pushed aside, the
    pasture trodden down and the water fouled with feet."""
    o = [bg(f"fl{seed}", w, h, [(0, "#6AA0C8"), (1, "#E8D8A0")]), ground(w, h, h * 0.5, "#8A9A5A", dy=0)]
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.86)} C {f(w * 0.7)} {f(h * 0.8)} {f(w * 0.86)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.56)} {f(h + 10)} Z" fill="#7A6A4A" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.6, h / 180)
    o.append(E.sheep(w * 0.3, h * 0.92, k * 1.1, wool="#F3EFE6"))
    o.append(f'<path d="M{f(w * 0.3 + 30 * k)} {f(h * 0.92 - 40 * k)} c {f(14 * k)} {f(-10 * k)} {f(20 * k)} {f(6 * k)} {f(6 * k)} {f(10 * k)}" stroke="#8A6A3A" stroke-width="{f(4 * k)}" fill="none"></path>')
    for i in range(3): o.append(E.sheep(w * (0.5 + i * 0.08), h * (0.9 + i * 0.03), k * 0.55, wool="#C8C2B6", flip=True))
    o.append("".join(f'<path d="M{f(w * (0.1 + i * 0.06))} {f(h * 0.74)} l 4 -8 l 4 8" stroke="#5A6A3A" stroke-width="2" fill="none"></path>' for i in range(8)))
    return "".join(o)

def david_shepherd(p, w, h, seed):
    """I will set up one shepherd over them, and he shall feed them, even my servant David: a shepherd-king in purple with a
    small gold crown and a staff among the flock on the green hills."""
    o = [mk.defs(p, *ALL), bg(f"ds{seed}", w, h, [(0, "#6AB0D8"), (1, "#F3E8C8")]), hills(w, h, h * 0.56, seed, "#7A9A5A", amp=12, step=80), ground(w, h, h * 0.64, "#8AAA5A", dy=0)]
    s = min(fit(h * 0.96, h * 0.3), 1.0)
    o.append(mk.person(p, round(w * 0.3), round(h * 0.96), round(s, 3), body=SKIN, cloth="#5A2A7A", sw=3, up=[(-22, -158), (-36, -150), (-44, -130)],
                       extra=A.BLACK_BEARD.replace("#2A1A10", "#7A3A1A") + '<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    o.append(f'<path d="M{f(w * 0.3 - 44 * s)} {f(h * 0.96 - 130 * s)} L {f(w * 0.3 - 50 * s)} {f(h * 0.96)}" stroke="#5A3A1A" stroke-width="{f(5 * s)}"></path>')
    o.append(flock(w * 0.42, w * 0.96, h * 0.7, h * 0.96, 11, seed, cows=0.0))
    return "".join(o)

def showers(w, h, seed):
    """I will cause the shower to come down in its season; there shall be showers of blessing; the tree of the field shall
    yield its fruit: rain falling from a bright cloud upon green hills and fruit trees."""
    r = random.Random(seed)
    o = [mountains(w, h, seed, "fruitful")]
    o.append(clouds(w, h * 0.08, seed, n=5, color="#E8E8F0", op=0.9, ry=0.06))
    o.append("".join(f'<path d="M{f(x)} {f(h * 0.12)} l -10 {f(h * 0.3)}" stroke="#8FD0E2" stroke-width="1.6" opacity="0.7"></path>' for x in range(20, int(w), 24)))
    return "".join(o)
