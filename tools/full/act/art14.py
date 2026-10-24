"""Drawings for Acts 25–26. Festus (greying, clean-shaven, a toga with a purple border) going up to Jerusalem and on the
judgment-seat at Cæsarea; the chief priests about Paul; I appeal unto Cæsar; king Agrippa (Agrippa II: a gold diadem, black
stubble, a royal purple robe) and Bernice (a deep blue veil with a gold band) arriving with great pomp, the chief captains
and the principal men of the city entering the place of hearing; Paul standing before them in his chain, his hand stretched
forth; the Damascus road told again (the light from heaven, Jesus not drawn); the king and the governor and Bernice rising.
Built on act.art13."""
from act.art13 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math

def festus(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#8A7A6A", border="#5A1A6A", flip=flip, up=up)
def agrippa2(p, x, y, s, flip=False, up=None): return king_fig(p, x, y, s, cloth="#4A1A6A", bd=None, flip=flip, up=up)
def bernice(p, x, y, s, flip=False, up=None): return woman_fig(p, x, y, s * 0.94, "#2A3A6A", "#2A3A6A", flip=flip, up=up, extra=band())
WHO.update({"festus": festus, "agrippa2": agrippa2, "bernice": bernice})

def festus_jerusalem(p, w, h, seed):
    """Festus at Jerusalem: the governor standing in the court of the palace with his soldiers, the chief priests and the
    principal men before him, asking."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.34, b - 190))
    o.append(soldier(p, w * 0.9, b, s, flip=True) + festus(p, w * 0.78, b, s, flip=True, up=UP_BLESS))
    for i, x in enumerate((0.16, 0.28, 0.4, 0.52)):
        o.append(high_priest(p, w * x, b, s) if i == 0 else man_fig(p, w * x, b, s * (1 - 0.02 * i), ["#E8E2D6", "#3A2A4A", "#6A2A3A", "#E8E2D6"][i], head=["#F3EFE6", "#3A2A4A", "#6A2A3A", "#F3EFE6"][i],
                                                                     cord="#E8B830", bd=["#3A2A1A", "#7A746A", "#1A1210", "#9A948A"][i], up=UP_BLESS if i == 2 else None))
    return "".join(o)

def pomp(p, w, h, seed):
    """Agrippa and Bernice came with great pomp into the place of hearing: the hall hung with red, the king in purple with his
    gold diadem and the queen in deep blue walking in under the canopy, the chief captains in their cloaks and the principal
    men of the city following, Festus rising to meet them."""
    bg, b = _hall(w, h, seed, "roman")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.36, b - 190))
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.14)} L {f(w * 0.48)} {f(h * 0.14)} L {f(w * 0.44)} {f(h * 0.24)} L {f(w * 0.12)} {f(h * 0.24)} Z" fill="#5A1A6A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.08)} {f(h * 0.14)} L {f(w * 0.48)} {f(h * 0.14)}" stroke="#E8B830" stroke-width="5"></path>')
    o.append(agrippa2(p, w * 0.26, b, s) + bernice(p, w * 0.36, b, s))
    o.append(lysias(p, w * 0.12, b, s * 0.96) + lysias(p, w * 0.03, b, s * 0.94))
    o.append(festus(p, w * 0.62, b, s, flip=True, up=UP_BLESS))
    o.append(toga_fig(p, w * 0.76, b, s * 0.96, hr="#6A645E", border="#E8B830", flip=True) + toga_fig(p, w * 0.88, b, s * 0.96, hr="#2A1A10", border="#E8B830", flip=True))
    return "".join(o)

def hearing(p, w, h, seed, stage="speak"):
    """The place of hearing: Agrippa and Bernice on their seats on the dais, Festus beside them, the chief captains and
    principal men standing along the wall; Paul standing in the midst in his chain, a soldier by him. stage "speak" — his
    hand stretched forth; "rise" — the king and the governor and Bernice risen from their seats, going out."""
    bg, b = _hall(w, h, seed, "roman")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.36, b - 190))
    st = b - 40 * s
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(st)}" width="{f(w * 0.46)}" height="{f(b - st + 2)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    if stage == "rise":
        o.append(festus(p, w * 0.62, st, s * 0.96) + agrippa2(p, w * 0.74, st, s * 0.96) + bernice(p, w * 0.86, st, s * 0.96))
    else:
        o.append(festus(p, w * 0.64, st, s * 0.94, flip=True))
        for x in (0.76, 0.88):
            o.append(f'<rect x="{f(w * x - 30 * s)}" y="{f(st - 60 * s)}" width="{f(60 * s)}" height="{f(60 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>')
        o.append(seated(w * 0.76, st - 40 * s, s * 0.8, "#4A1A6A", head="#1A1210", beard=None, flip=True, band=True) + seated(w * 0.88, st - 40 * s, s * 0.8, "#2A3A6A", head="#2A3A6A", beard=None, flip=True, band=True))
    o.append(lysias(p, w * 0.04, b, s * 0.94) + toga_fig(p, w * 0.14, b, s * 0.94, hr="#6A645E", border="#E8B830"))
    o.append(soldier(p, w * 0.28, b, s) + paul(p, w * 0.4, b, s, flip=True, up=UP_BLESS if stage == "speak" else None))
    o.append(f'<path d="M{f(w * 0.31)} {f(b - 96 * s)} C {f(w * 0.34)} {f(b - 80 * s)} {f(w * 0.37)} {f(b - 80 * s)} {f(w * 0.4)} {f(b - 96 * s)}" stroke="#8A8A90" stroke-width="{f(3 * s)}" stroke-dasharray="{f(5 * s)} {f(2 * s)}" fill="none"></path>')
    return "".join(o)

def light_gentiles(p, w, h, seed):
    """To open their eyes, that they may turn from darkness to light: the night lifting from the land, the dawn breaking over
    the cities of the nations on the hills."""
    o = [sky(w, h, "#14123A", "#FFC890"), glow(w * 0.7, h * 0.6, h * 0.6, "#FFF4C2", 0.8, f"{p}d"), sun(w * 0.7, h * 0.62, max(14, h * 0.06), color="#FFE680", op=0.5),
         hills(w, h, h * 0.62, seed, color="#3A3A5A", amp=16, step=90)]
    for i, x in enumerate((0.12, 0.4, 0.86)):
        o.append(hill_town(w * x, h * 0.7, w * 0.14, h * 0.12, seed + i, hill="#4A4A6A"))
    o.append(ground(w, h, h * 0.72, "#2A2A44", dy=0))
    return "".join(o)
