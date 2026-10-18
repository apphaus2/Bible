"""Drawings for the 1 Samuel volume (chapter by chapter, added below). The Joshua and Judges drawings are reused where they
fit (jos.art, jdg.art); the digest's panels come in through sa1.common.D."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J, samuel1 as S1, samuel2 as S2, samuel3 as S3
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from exo import art as A
from num.art import ALL, TRIBE_C
from jos.art import crowd_at, below, night, WAR

def f(v): return f"{v:.1f}"

# ---- 1 Samuel 1–2 -------------------------------------------------------------------------------------------------------
def flesh_hook(w, h, seed):
    """The priest's servant with a flesh-hook of three teeth struck into the caldron while the flesh was boiling."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2218"></rect>', ground(w, h, h * 0.8, "#2A1810", dy=0),
         E.blaze(w * 0.5, h * 0.92, w * 0.3, h * 0.2, seed, n=7)]
    cx, cy = w * 0.5, h * 0.66
    o.append(f'<path d="M{f(cx - w * 0.18)} {f(cy)} C {f(cx - w * 0.18)} {f(cy + h * 0.2)} {f(cx + w * 0.18)} {f(cy + h * 0.2)} {f(cx + w * 0.18)} {f(cy)} Z" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.18)}" ry="{f(h * 0.04)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for k in range(4):
        o.append(f'<path d="M{f(cx - 40 + k * 26)} {f(cy - 10)} C {f(cx - 46 + k * 26)} {f(cy - 40)} {f(cx - 30 + k * 26)} {f(cy - 60)} {f(cx - 36 + k * 26)} {f(cy - 90)}" fill="none" stroke="#E8E2D6" stroke-width="3" opacity="0.5"></path>')
    hx = cx + w * 0.06
    o.append(f'<path d="M{f(hx + w * 0.3)} {f(h * 0.2)} L {f(hx)} {f(cy - 6)}" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(hx - 12 + i * 12)} {f(cy - 14)} L {f(hx - 14 + i * 12)} {f(cy + 14)}" stroke="#C8C8D0" stroke-width="4"></path>' for i in range(3)))
    return "".join(o)

def little_robe(w, h, seed):
    """The little robe his mother made him and brought from year to year."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8D8B0"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, max(w, h), color="#FFF4C2", op=0.3)]
    cx, cy, s = w * 0.5, h * 0.52, min(w, h) / 300
    o.append(f'<path d="M{f(cx - 40 * s)} {f(cy - 80 * s)} L {f(cx + 40 * s)} {f(cy - 80 * s)} L {f(cx + 90 * s)} {f(cy - 50 * s)} L {f(cx + 70 * s)} {f(cy - 20 * s)} L {f(cx + 50 * s)} {f(cy - 36 * s)} '
             f'L {f(cx + 60 * s)} {f(cy + 90 * s)} L {f(cx - 60 * s)} {f(cy + 90 * s)} L {f(cx - 50 * s)} {f(cy - 36 * s)} L {f(cx - 70 * s)} {f(cy - 20 * s)} L {f(cx - 90 * s)} {f(cy - 50 * s)} Z" '
             f'fill="#2A6A5A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - 58 * s)} {f(cy + 76 * s)} L {f(cx + 58 * s)} {f(cy + 76 * s)}" stroke="#E8B830" stroke-width="{f(5 * s)}" stroke-dasharray="8 5"></path>')
    return "".join(o)
