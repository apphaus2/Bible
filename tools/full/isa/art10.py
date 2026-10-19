"""Isaiah 36–39 drawings (on top of isa.art9; the story of Hezekiah and Sennacherib reuses 2 Kings' drawings carried in
kg2.art: upper_pool, letter_spread, silent_camp, nineveh, dial, treasures, lebanon, vine_fig): Hezekiah on his sickbed with
Isaiah standing by, the shepherd's tent and the weaver's loom of his writing, and the swallow and the crane."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art9 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds

def hezekiah_bed(p, w, h, seed, wall=False):
    """Hezekiah sick unto death upon his bed in the cedar chamber, Isaiah standing by (wall=True: the king turned to the wall,
    the prophet gone)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), K1.bed(w, h, w * 0.06, w * 0.56, b, cover="#1F3A7A", head="#C8A890", hair="#2A1A10")]
    if not wall:
        o.append(K1.prophet_fig(p, w * 0.76, b, fit(b, max(h * 0.4, b - 230)), "#4A3A6A", flip=True))
    return "".join(o)

def loom_tent(w, h, seed):
    """My dwelling is removed, and is carried away from me as a shepherd's tent: I have rolled up, like a weaver, my life; he
    will cut me off from the loom: a shepherd's tent being struck at evening, and beside it a loom with the web cut from it."""
    o = [bg(w, h, "#5A4A6A", "#E8A070"), hills(w, h, h * 0.56, seed, color="#6A5A4A", amp=10), ground(w, h, h * 0.66, "#A8885A", dy=0)]
    s = min(1.2, h / 260); b = h * 0.9
    o.append(f'<path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.2)} {f(b - 90 * s)} L {f(w * 0.3)} {f(b - 60 * s)} L {f(w * 0.36)} {f(b)} Z" fill="#3A2A22" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.2)} {f(b - 90 * s)} L {f(w * 0.24)} {f(b - 110 * s)}" stroke="#5A3A22" stroke-width="{f(4 * s)}"></path>')
    lx = w * 0.62
    o.append(f'<path d="M{f(lx - 70 * s)} {f(b)} L {f(lx - 60 * s)} {f(b - 140 * s)} M{f(lx + 70 * s)} {f(b)} L {f(lx + 60 * s)} {f(b - 140 * s)} M{f(lx - 66 * s)} {f(b - 130 * s)} L {f(lx + 66 * s)} {f(b - 130 * s)} M{f(lx - 64 * s)} {f(b - 40 * s)} L {f(lx + 64 * s)} {f(b - 40 * s)}" stroke="#6A4A2A" stroke-width="{f(5 * s)}"></path>'
             + "".join(f'<path d="M{f(lx - 56 * s + k * 8 * s)} {f(b - 128 * s)} L {f(lx - 56 * s + k * 8 * s)} {f(b - 90 * s)}" stroke="#E8D8B0" stroke-width="1.4"></path>' for k in range(15))
             + f'<rect x="{f(lx - 58 * s)}" y="{f(b - 92 * s)}" width="{f(116 * s)}" height="{f(10 * s)}" rx="{f(5 * s)}" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             + "".join(f'<path d="M{f(lx - 56 * s + k * 8 * s)} {f(b - 78 * s)} L {f(lx - 56 * s + k * 8 * s + 3)} {f(b - 48 * s)}" stroke="#E8D8B0" stroke-width="1.4" opacity="0.6"></path>' for k in range(15)))
    o.append(E.sheep(w * 0.88, b, min(0.5, h / 520)))
    return "".join(o)

def swallow_crane(w, h, seed):
    """Like a swallow or a crane, so did I chatter; I did moan as a dove; mine eyes fail with looking upward: swallows
    darting and cranes flying high over the city at dusk, a dove on the parapet."""
    o = [bg(w, h, "#3A3A6A", "#E89A7A"), J.city_hill(w * 0.5, h * 0.98, w * 0.6, h * 0.24, seed)]
    o.append(birds(9, w * 0.05, w * 0.95, h * 0.08, h * 0.5, seed, smin=0.8, smax=1.6))
    for i in range(3):
        x = w * (0.62 + i * 0.1); y = h * (0.18 + i * 0.04)
        o.append(f'<path d="M{f(x - 30)} {f(y)} L {f(x)} {f(y - 6)} L {f(x + 30)} {f(y)} M{f(x)} {f(y - 6)} L {f(x + 24)} {f(y - 10)}" stroke="#1A1414" stroke-width="2.4" fill="none"></path>')
    dx, dy = w * 0.2, h * 0.78
    o.append(f'<ellipse cx="{f(dx)}" cy="{f(dy)}" rx="16" ry="10" fill="#E8E2F0" stroke="#0D0D0F" stroke-width="1.6"></ellipse><circle cx="{f(dx + 14)}" cy="{f(dy - 8)}" r="6" fill="#E8E2F0" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    return "".join(o)

def fig_cake(w, h, seed):
    """Let them take a cake of figs, and lay it for a plaster upon the boil: a pressed cake of figs on a cloth, figs beside it."""
    o = [rect(w, h, "#3A2A2A"), V.rays(w * 0.5, h * 0.5, 20, 10, max(w, h), color="#E8C88A", op=0.1)]
    s = min(1.4, h / 200); cx, cy = w * 0.5, h * 0.6
    o.append(f'<path d="M{f(cx - 120 * s)} {f(cy + 30 * s)} L {f(cx + 120 * s)} {f(cy + 30 * s)} L {f(cx + 100 * s)} {f(cy - 10 * s)} L {f(cx - 100 * s)} {f(cy - 10 * s)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(60 * s)}" ry="{f(20 * s)}" fill="#6A3A4A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for k in range(5):
        x = cx + 80 * s + (k % 2) * 16 * s; y = cy - k * 6 * s
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 10 * s)} {f(y - 4 * s)} {f(x - 8 * s)} {f(y - 18 * s)} {f(x)} {f(y - 20 * s)} C {f(x + 8 * s)} {f(y - 18 * s)} {f(x + 10 * s)} {f(y - 4 * s)} {f(x)} {f(y)} Z" fill="#7A3A5A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)
