"""Isaiah 46–48 drawings (on top of isa.art12): Bel and Nebo bowed upon the beasts, the idol borne upon the shoulder, the
ravenous bird from the east, the virgin daughter of Babylon in the dust at the millstones, the star-gazers on the tower,
the furnace of affliction, peace as a river and righteousness as the waves of the sea, the going forth from Babylon, and the
water out of the rock."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art12 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds

def idol_fig(x, y, s, col="#E8B830", rot=0, crown=True):
    """A cast idol on its base (about 120 units tall at s=1); rot tips it over."""
    o = (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})">'
         '<rect x="-24" y="-14" width="48" height="14" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<path d="M-16 -14 L -18 -80 C -18 -92 18 -92 18 -80 L 16 -14 Z" fill="{col}" stroke="#0D0D0F" stroke-width="2"></path>'
         f'<circle cx="0" cy="-98" r="14" fill="{col}" stroke="#0D0D0F" stroke-width="2"></circle>'
         '<path d="M-18 -70 L -30 -50 M18 -70 L 30 -50" stroke="#0D0D0F" stroke-width="2"></path>')
    if crown: o += f'<path d="M-12 -110 L -12 -122 L -6 -114 L 0 -126 L 6 -114 L 12 -122 L 12 -110 Z" fill="#B87333" stroke="#0D0D0F" stroke-width="1.6"></path>'
    return o + '</g>'

def bel_nebo(w, h, seed):
    """Bel boweth down, Nebo stoopeth; their idols are upon the beasts, and upon the cattle; a burden to the weary beast; they
    are gone into captivity: two oxen plodding along a road out of Babylon, each with a great idol lashed on its back, the
    idols tipped and bowed, the beasts' heads hanging."""
    o = [bg(w, h, "#C88A5A", "#F3D8A8"), ziggurat(w * 0.88, h * 0.62, w * 0.2, h * 0.3, color="#B8865A", broken=0.4, seed=seed), ground(w, h, h * 0.62, "#C8A070", dy=0)]
    k = min(0.6, h / 460)
    for i, (x, col, nm) in enumerate(((0.26, "#E8B830", "BEL"), (0.58, "#C8C8D0", "NEBO"))):
        cx, b = w * x, h * 0.94
        o.append(S1.cow(cx, b, k, color="#8A6A4A", patch="#C8A87A", low=True))
        o.append(idol_fig(cx + 10 * k, b - 104 * k, k * 0.9, col=col, rot=-60 if i == 0 else -48))
        o.append(f'<path d="M{f(cx - 40 * k)} {f(b - 96 * k)} L {f(cx + 50 * k)} {f(b - 110 * k)}" stroke="#5A3A22" stroke-width="2"></path>')
        o.append(label(cx, b - 150 * k, nm, "#3A2A1A", 10))
    return "".join(o)

def borne_idol(p, w, h, seed):
    """They bear it upon the shoulder, they carry it, and set it in its place, and it standeth; yea, one may cry unto it, yet can
    it not answer: two men carrying a gilded idol on poles, another setting its base in place, a man on his knees before an
    empty niche."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#4A3A3A"), f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(h * 0.7)}" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, h * 0.86, "#3A2A22", dy=0)]
    s = fit(b, max(h * 0.5, b - 170))
    o.append(man(p, w * 0.18, b, s, "#6A5A3A", up=[(-22, -158), (-10, -176), (6, -186)]) + man(p, w * 0.42, b, s, "#4A3A2A", up=[(-22, -158), (-10, -176), (6, -186)]))
    o.append(f'<path d="M{f(w * 0.12)} {f(b - 188 * s)} L {f(w * 0.48)} {f(b - 188 * s)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>' + idol_fig(w * 0.3, b - 188 * s, s * 0.9))
    o.append(f'<path d="M{f(w * 0.68)} {f(h * 0.86)} L {f(w * 0.68)} {f(h * 0.44)} Q {f(w * 0.76)} {f(h * 0.34)} {f(w * 0.84)} {f(h * 0.44)} L {f(w * 0.84)} {f(h * 0.86)} Z" fill="#2A1E1A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(E.kneel(w * 0.64, b, s * 0.9, color="#5A4A6A", skin="#8A5A3A", flip=True))
    return "".join(o)

def ravenous_bird(w, h):
    """Calling a ravenous bird from the east, the man of my counsel from a far country: an eagle's track drawn across the map
    from the far east to Babylon."""
    o = [nations_map(w, h, hi=("MEDIA", "BABYLON"), arrows=(("MEDIA", "BABYLON"),), lit="#FFD23F", show=["MEDIA", "ELAM", "BABYLON", "NINEVEH", "JERUSALEM", "DAMASCUS", "EGYPT"],
                     note="A RAVENOUS BIRD FROM THE EAST")]
    x, y, k = w * 0.84, h * 0.32, min(1.0, h / 260)
    o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 30 * k)} {f(y - 24 * k)} {f(x - 66 * k)} {f(y - 20 * k)} {f(x - 96 * k)} {f(y - 4 * k)} C {f(x - 70 * k)} {f(y)} {f(x - 40 * k)} {f(y + 6 * k)} {f(x - 6 * k)} {f(y + 8 * k)} Z" fill="#FFD23F" opacity="0.7"></path>'
             f'<path d="M{f(x)} {f(y)} C {f(x + 30 * k)} {f(y - 24 * k)} {f(x + 66 * k)} {f(y - 20 * k)} {f(x + 96 * k)} {f(y - 4 * k)} C {f(x + 70 * k)} {f(y)} {f(x + 40 * k)} {f(y + 6 * k)} {f(x + 6 * k)} {f(y + 8 * k)} Z" fill="#FFD23F" opacity="0.7"></path>')
    return "".join(o)

def daughter_dust(p, w, h, seed):
    """Come down, and sit in the dust, O virgin daughter of Babylon; sit on the ground without a throne; take the millstones,
    and grind meal: an empty gilded throne overturned on the steps of a palace at dusk, and below it a woman in a dark mantle
    sitting on the ground at a hand-mill."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#3A2A4A", "#C87A5A"), ziggurat(w * 0.8, h * 0.7, w * 0.3, h * 0.44, color="#8A5A3A", seed=seed), ground(w, h, h * 0.7, "#8A6A4A", dy=0)]
    s = min(1.0, h / 300)
    o.append(f'<g transform="rotate(-70 {f(w * 0.56)} {f(h * 0.86)})">{S3.throne(w * 0.56, h * 0.86, 0.5 * s)}</g>')
    qx = w * 0.34
    o.append(f'<ellipse cx="{f(qx)}" cy="{f(b - 8 * s)}" rx="{f(40 * s)}" ry="{f(12 * s)}" fill="#6A6A7A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(qx - 40 * s)} {f(b - 8 * s)} L {f(qx - 40 * s)} {f(b)} C {f(qx - 40 * s)} {f(b + 8 * s)} {f(qx + 40 * s)} {f(b + 8 * s)} {f(qx + 40 * s)} {f(b)} L {f(qx + 40 * s)} {f(b - 8 * s)}" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<ellipse cx="{f(qx)}" cy="{f(b - 20 * s)}" rx="{f(30 * s)}" ry="{f(9 * s)}" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(qx + 16 * s)} {f(b - 22 * s)} L {f(qx + 18 * s)} {f(b - 44 * s)}" stroke="#5A3A22" stroke-width="{f(4 * s)}"></path>'
             f'<path d="M{f(qx + 40 * s)} {f(b)} q {f(10 * s)} {f(2 * s)} {f(18 * s)} {f(-2 * s)}" stroke="#F3EFE6" stroke-width="{f(4 * s)}" fill="none"></path>')
    o.append(E.kneel(w * 0.2, b, fit(b, max(h * 0.5, b - 160)) * 0.85, color="#2A2030", skin="#C98E66"))
    return "".join(o)

def stargazers(p, w, h, seed):
    """Let now the astrologers, the star-gazers, the monthly prognosticators, stand up, and save thee: robed men on the top of a
    temple-tower at night pointing at the stars and the moon, a chart on a tablet."""
    o = [mk.defs(p, *ALL), bg(w, h, "#05051A", "#2A1E50"), mk.stars(70, w, h * 0.6, seed), J.moon(w * 0.8, h * 0.18, min(20, h * 0.07)),
         ziggurat(w * 0.4, h * 1.0, w * 0.7, h * 0.56, color="#4A3A4A", seed=seed)]
    top = h * 1.0 - h * 0.56 + h * 0.02
    s = fit(top, top - min(h * 0.26, 120))
    for i, x in enumerate((0.3, 0.4, 0.5)):
        o.append(man(p, w * x, top, s, ["#5A3A6A", "#2A4A6A", "#6A2A3A"][i], up=[(-22, -158), (-34, -190), (-46, -222)] if i != 1 else None))
    return "".join(o)

def furnace(w, h, seed):
    """Behold, I have refined thee, but not as silver; I have chosen thee in the furnace of affliction: a refiner's furnace,
    its mouth glowing white-hot."""
    o = [rect(w, h, "#1A0E0E"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" r="{f(h * 0.5)}" fill="#8A2A1A" opacity="0.4"></circle>']
    s = min(1.4, h / 200); cx, b = w * 0.5, h * 0.94
    o.append(f'<path d="M{f(cx - 110 * s)} {f(b)} L {f(cx - 90 * s)} {f(b - 120 * s)} Q {f(cx)} {f(b - 170 * s)} {f(cx + 90 * s)} {f(b - 120 * s)} L {f(cx + 110 * s)} {f(b)} Z" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - 40 * s)} {f(b)} L {f(cx - 40 * s)} {f(b - 50 * s)} Q {f(cx)} {f(b - 80 * s)} {f(cx + 40 * s)} {f(b - 50 * s)} L {f(cx + 40 * s)} {f(b)} Z" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="2"></path>'
             + E.blaze(cx, b, 60 * s, 50 * s, seed, n=6) + smoke(cx, b - 170 * s, 5, seed, r0=12 * s, color="#3A3036", op=0.5))
    return "".join(o)

def river_waves(w, h, seed):
    """Oh that thou hadst hearkened to my commandments! then had thy peace been as a river, and thy righteousness as the waves of
    the sea; thy seed as the sand: a broad river flowing out to the sea, waves rolling in on a long beach of sand."""
    r = random.Random(seed)
    o = [bg(w, h, "#7AB8E8", "#F3F0E0"), hills(w, h, h * 0.4, seed, color="#7AA04A", amp=8),
         f'<path d="M{f(w * 0.06)} {f(h * 0.4)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.1)} {f(h * 0.62)} {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.5)} {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.4)} {f(h * 0.5)} {f(w * 0.16)} {f(h * 0.4)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M-10 {f(h * 0.7)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A"></path>']
    for k in range(4):
        y = h * (0.7 + k * 0.07)
        o.append(f'<path d="M{f(w * 0.3)} {f(y)} ' + " ".join(f"Q {f(x + 25)} {f(y - 10)} {f(x + 50)} {f(y)}" for x in range(int(w * 0.3), int(w) + 50, 50)) + '" stroke="#E8F6FA" stroke-width="2" fill="none"></path>')
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.9)} {f(w * 0.6)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for _ in range(40):
        o.append(f'<circle cx="{f(r.uniform(0, w * 0.5))}" cy="{f(r.uniform(h * 0.9, h))}" r="1.2" fill="#B89A6A"></circle>')
    return "".join(o)

def rock_water(p, w, h, seed):
    """They thirsted not when he led them through the deserts; he caused the waters to flow out of the rock for them; he clave
    the rock also, and the waters gushed out: a cloven rock in the desert, water gushing, the people drinking."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#E8A050", "#FFF0C8"), ground(w, h, h * 0.6, "#E0B878", dy=0)]
    s = min(1.2, h / 280)
    o.append(E4.rock(w * 0.35, h * 0.86, w * 0.3, h * 0.44, color="#A86A4A", dark="#5A3A2A") + f'<path d="M{f(w * 0.5)} {f(h * 0.42)} L {f(w * 0.48)} {f(h * 0.6)} L {f(w * 0.52)} {f(h * 0.7)}" stroke="#0D0D0F" stroke-width="3" fill="none"></path>'
             + E4.gush(w * 0.5, h * 0.7, seed, scale=s) + f'<path d="M{f(w * 0.5)} {f(h * 0.86)} C {f(w * 0.6)} {f(h * 0.9)} {f(w * 0.8)} {f(h * 0.94)} {f(w + 10)} {f(h * 0.92)}" stroke="#2C9DB8" stroke-width="{f(8 * s)}" fill="none"></path>')
    fs = fit(b, max(h * 0.55, b - 140))
    o.append(E.kneel(w * 0.3, b, fs * 0.8, color="#5A4A6A", skin="#8A5A3A") + man(p, w * 0.08, b, fs, "#6A3A2A") + woman(p, w * 0.18, b, fs, "#C2456A"))
    return "".join(o)
