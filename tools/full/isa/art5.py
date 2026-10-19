"""Isaiah 17–20 drawings (on top of isa.art4): Damascus a ruinous heap, the gleanings of the olive-tree, the altars and
Asherim forsaken, the chaff before the storm, the vessels of papyrus, the pruned vine, the swift cloud over Egypt, the Nile
dried up, the altar in Egypt, the sackcloth and the shoe laid down (Isaiah's sign shown only so)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art4 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
import jos.art as JA
import egypt as EG

def heap_flocks(w, h, seed):
    """Damascus a ruinous heap at sunset; and the cities of Aroer forsaken, for flocks which lie down there."""
    o = [JA.ruin_heap(w, h, seed)]
    s = min(0.45, h / 600)
    for i in range(5):
        o.append(E.sheep(w * (0.5 + i * 0.09), h * (0.84 + (i % 2) * 0.05), s, flip=i % 2 == 1))
    return "".join(o)

def olive_gleaning(p, w, h, seed):
    """Gleanings, as the shaking of an olive-tree, two or three berries in the top of the uppermost bough: a beaten olive-tree
    almost bare, a few berries left at the top, a gleaner below in the valley of Rephaim, the harvest gone."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#C8B8A0", "#F3E0B8"), hills(w, h, h * 0.5, seed, color="#A89A6A", amp=8), ground(w, h, h * 0.66, "#C8A870", dy=0)]
    s = min(1.3, h / 260); cx = w * 0.62
    o.append(f'<path d="M{f(cx - 14 * s)} {f(b)} C {f(cx - 20 * s)} {f(b - 60 * s)} {f(cx + 10 * s)} {f(b - 80 * s)} {f(cx)} {f(b - 120 * s)} L {f(cx + 14 * s)} {f(b - 120 * s)} C {f(cx + 24 * s)} {f(b - 80 * s)} {f(cx)} {f(b - 60 * s)} {f(cx + 14 * s)} {f(b)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for a in (-1.0, -0.5, 0.0, 0.5, 1.0):
        x1 = cx + math.sin(a) * 110 * s; y1 = b - 120 * s - math.cos(a) * 70 * s
        o.append(f'<path d="M{f(cx + 6 * s)} {f(b - 118 * s)} L {f(x1)} {f(y1)}" stroke="#5A4A3A" stroke-width="{f(4 * s)}"></path>')
        for k in range(3):
            o.append(f'<ellipse cx="{f(x1 + r.uniform(-10, 10) * s)}" cy="{f(y1 + r.uniform(-6, 6) * s)}" rx="{f(7 * s)}" ry="{f(3 * s)}" fill="#7A8A5A" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    for k in range(4):
        o.append(f'<circle cx="{f(cx + (k - 1.5) * 9 * s)}" cy="{f(b - 192 * s + (k % 2) * 6)}" r="{f(3.4 * s)}" fill="#2A2A1A"></circle>')
    o.append(R1.gleaner(w * 0.26, b, fit(b, max(h * 0.55, b - 140)) / 1.0 * 0.9))
    return "".join(o)

def asherim(w, h, seed):
    """They shall not look to the altars, the work of their hands, either the Asherim, or the sun-images: an altar, a carved
    pole and a sun-disc on its pillar, forsaken on a hilltop, the strong city behind them empty."""
    o = [bg(w, h, "#8A8AA0", "#E8D8B8"), J.city_hill(w * 0.8, h * 0.6, w * 0.2, h * 0.3, seed), ground(w, h, h * 0.66, "#A8986A", dy=0)]
    s = min(1.2, h / 240); b = h * 0.9
    o.append(f'<rect x="{f(w * 0.16)}" y="{f(b - 40 * s)}" width="{f(70 * s)}" height="{f(40 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.4)} {f(b)} L {f(w * 0.4)} {f(b - 150 * s)}" stroke="#6A4A2A" stroke-width="{f(10 * s)}"></path>'
             + "".join(f'<path d="M{f(w * 0.4 - 12 * s)} {f(b - (40 + k * 30) * s)} L {f(w * 0.4 + 12 * s)} {f(b - (50 + k * 30) * s)}" stroke="#4A2E1A" stroke-width="2"></path>' for k in range(4)))
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(b - 100 * s)}" width="{f(12 * s)}" height="{f(100 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<circle cx="{f(w * 0.56 + 6 * s)}" cy="{f(b - 116 * s)}" r="{f(22 * s)}" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></circle>'
             + "".join(f'<path d="M{f(w * 0.56 + 6 * s + math.cos(a) * 24 * s)} {f(b - 116 * s + math.sin(a) * 24 * s)} L {f(w * 0.56 + 6 * s + math.cos(a) * 34 * s)} {f(b - 116 * s + math.sin(a) * 34 * s)}" stroke="#C8A040" stroke-width="3"></path>' for a in [i * math.pi / 4 for i in range(8)]))
    o.append(thorns(w * 0.1, w * 0.7, b + 6, seed, n=10, s=min(0.8, h / 300)))
    return "".join(o)

def chaff_storm(w, h, seed):
    """They shall be chased as the chaff of the mountains before the wind, and like the whirling dust before the storm: a
    storm over the mountains at eventide, chaff and dust whirling away."""
    r = random.Random(seed)
    o = [bg(w, h, "#2A2A40", "#8A6A5A"), f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.36)} L {f(w * 0.4)} {f(h * 0.6)} L {f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.86)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="2"></path>']
    for k in range(6):
        cy = h * r.uniform(0.2, 0.7); cx = w * r.uniform(0.1, 0.9)
        o.append(f'<path d="M{f(cx - 60)} {f(cy)} C {f(cx - 20)} {f(cy - 30)} {f(cx + 20)} {f(cy + 30)} {f(cx + 60)} {f(cy)}" stroke="#C8B8A0" stroke-width="2" fill="none" opacity="0.6"></path>')
    o.append(J1.chaff(60, w * 0.1, w * 0.95, h * 0.1, h * 0.8, seed))
    return "".join(o)

def papyrus_boats(p, w, h, seed):
    """That sendeth ambassadors by the sea, even in vessels of papyrus upon the waters: reed boats on the Nile beyond the
    rivers of Ethiopia, tall swift messengers standing in them, papyrus on the banks."""
    b = h * 0.8
    o = [mk.defs(p, *ALL), bg(w, h, "#E8A050", "#F8E0A0"), f'<path d="M-10 {f(h * 0.62)} L {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(E.reeds(-10, w * 0.2, h * 0.66, h * 0.3, 12, seed) + E.reeds(w * 0.84, w + 10, h * 0.64, h * 0.3, 10, seed + 1))
    s = fit(b, max(h * 0.5, b - 150))
    for i, x in enumerate((0.36, 0.64)):
        cx = w * x; yy = b - i * 10
        o.append(f'<path d="M{f(cx - 80 * s)} {f(yy - 30 * s)} C {f(cx - 60 * s)} {f(yy + 6 * s)} {f(cx + 60 * s)} {f(yy + 6 * s)} {f(cx + 80 * s)} {f(yy - 30 * s)} C {f(cx + 40 * s)} {f(yy - 10 * s)} {f(cx - 40 * s)} {f(yy - 10 * s)} {f(cx - 80 * s)} {f(yy - 30 * s)} Z" fill="#C8B060" stroke="#0D0D0F" stroke-width="2"></path>'
                 + "".join(f'<path d="M{f(cx - 70 * s + k * 14 * s)} {f(yy - 20 * s)} L {f(cx - 66 * s + k * 14 * s)} {f(yy - 4 * s)}" stroke="#8A7A3A" stroke-width="1.4"></path>' for k in range(10)))
        o.append(mk.person(p, round(cx), round(yy - 12 * s), round(s * 1.05, 3), body="#3A2014", cloth="#F3EFE6", kind="Tunic", sw=3))
        o.append(mk.person(p, round(cx + 40 * s), round(yy - 12 * s), round(s * 1.05, 3), body="#3A2014", cloth="#E8B830", kind="Tunic", sw=3, up=[(-22, -158), (-6, -150), (20, -160)],
                           extra='<path d="M20 -170 L 40 30" stroke="#5A3A22" stroke-width="5"></path>'))
    return "".join(o)

def pruned_vine(w, h, seed):
    """Before the harvest he will cut off the sprigs with pruning-hooks, and the spreading branches will he take away: a vine
    with its branches cut and laid on the ground, a pruning-hook on them, birds of prey circling high over the mountains."""
    from genesis.art2 import birds
    o = [bg(w, h, "#E8C878", "#F8F0D0"), hills(w, h, h * 0.5, seed, color="#9A8A5A", amp=12), ground(w, h, h * 0.7, "#B89A6A", dy=0)]
    s = min(1.2, h / 240); cx, b = w * 0.4, h * 0.92
    o.append(f'<path d="M{f(cx)} {f(b)} C {f(cx - 10 * s)} {f(b - 40 * s)} {f(cx + 10 * s)} {f(b - 60 * s)} {f(cx)} {f(b - 90 * s)}" stroke="#5A3A22" stroke-width="{f(8 * s)}" fill="none"></path>'
             f'<path d="M{f(cx - 40 * s)} {f(b - 90 * s)} L {f(cx + 40 * s)} {f(b - 90 * s)}" stroke="#6A5A3A" stroke-width="3"></path>')
    for k in range(5):
        x = w * (0.52 + k * 0.08)
        o.append(f'<path d="M{f(x)} {f(b - 4)} C {f(x + 20 * s)} {f(b - 14 * s)} {f(x + 40 * s)} {f(b - 6 * s)} {f(x + 50 * s)} {f(b - 12 * s)}" stroke="#5A4A2A" stroke-width="3" fill="none"></path>'
                 f'<ellipse cx="{f(x + 30 * s)}" cy="{f(b - 14 * s)}" rx="{f(9 * s)}" ry="{f(5 * s)}" fill="#6A8A3A" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.2)} {f(b - 6)}" stroke="#8A5A2A" stroke-width="4"></path><path d="M{f(w * 0.2)} {f(b - 6)} c -8 -6 -8 -18 2 -20" stroke="#C8D0D8" stroke-width="4" fill="none"></path>')
    o.append(birds(7, w * 0.5, w * 0.95, h * 0.08, h * 0.3, seed, smin=1.0, smax=1.6))
    return "".join(o)

def swift_cloud(w, h, seed):
    """Behold, Jehovah rideth upon a swift cloud, and cometh unto Egypt: and the idols of Egypt shall tremble: a great storm
    cloud driving over the Nile and the pyramids, lightning in it, the idols on their pedestals shaking (no one drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#2A2A4A", "#E8A060"), f'<path d="M-10 {f(h * 0.7)} L {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h * 0.86)} C {f(w * 0.6)} {f(h * 0.92)} {f(w * 0.3)} {f(h * 0.84)} -10 {f(h * 0.88)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="1.6"></path>',
         EG.pyramid(w * 0.2, h * 0.7, w * 0.2, h * 0.2), EG.pyramid(w * 0.34, h * 0.7, w * 0.14, h * 0.14)]
    for _ in range(14):
        o.append(f'<ellipse cx="{f(r.uniform(w * 0.3, w * 1.0))}" cy="{f(r.uniform(h * 0.05, h * 0.3))}" rx="{f(w * r.uniform(0.08, 0.16))}" ry="{f(h * r.uniform(0.06, 0.12))}" fill="{r.choice(["#3A3A5A", "#4A4A6A", "#2A2A48"])}" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(E2.bolt(w * 0.6, h * 0.3, h * 0.36, seed) + E2.bolt(w * 0.84, h * 0.26, h * 0.4, seed + 1))
    s = min(1.0, h / 300)
    for i in range(3):
        x = w * (0.56 + i * 0.12); b = h * 0.72
        o.append(f'<g transform="rotate({(-8, 6, -4)[i]} {f(x)} {f(b)})"><rect x="{f(x - 12 * s)}" y="{f(b - 70 * s)}" width="{f(24 * s)}" height="{f(60 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.8"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(b - 80 * s)}" r="{f(11 * s)}" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.8"></circle>'
                 f'<rect x="{f(x - 16 * s)}" y="{f(b - 12 * s)}" width="{f(32 * s)}" height="{f(12 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></rect></g>'
                 f'<path d="M{f(x - 22 * s)} {f(b - 60 * s)} l -6 -4 M{f(x + 22 * s)} {f(b - 50 * s)} l 6 -4" stroke="#FFD23F" stroke-width="2"></path>')
    return "".join(o)

def nile_dry(p, w, h, seed):
    """The river shall be wasted and become dry; the reeds and flags shall wither; the fishers shall lament: the bed of the
    Nile cracked and dry, withered reeds, a fisher sitting by his empty net, a broken pillar."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#E8A060", "#F8E0A8"), EG.pyramid(w * 0.86, h * 0.5, w * 0.16, h * 0.16), ground(w, h, h * 0.5, "#C8A06A", dy=0),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.58)} {f(w * 0.6)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.86)} C {f(w * 0.6)} {f(h * 0.92)} {f(w * 0.3)} {f(h * 0.84)} -10 {f(h * 0.9)} Z" fill="#B8925A" stroke="#0D0D0F" stroke-width="2"></path>']
    for _ in range(20):
        x = r.uniform(0, w); y = r.uniform(h * 0.64, h * 0.86)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(8, 20))} {f(r.uniform(-4, 4))} l {f(r.uniform(4, 12))} {f(r.uniform(-6, 6))}" stroke="#6A4A2A" stroke-width="1.4" fill="none"></path>')
    o.append(E.reeds(-10, w * 0.26, h * 0.62, h * 0.18, 10, seed, color="#9A8A4A", dark="#6A5A2A", lean=0.4))
    s = fit(b, max(h * 0.55, b - 140))
    o.append(E.kneel(w * 0.5, b, s * 0.9, color="#E8E2D6", skin="#8A5A3A"))
    o.append(f'<path d="M{f(w * 0.56)} {f(b)} C {f(w * 0.6)} {f(b - 10)} {f(w * 0.66)} {f(b - 6)} {f(w * 0.7)} {f(b)}" stroke="#5A4A3A" stroke-width="1.4" fill="none"></path>'
             + "".join(f'<path d="M{f(w * (0.56 + k * 0.02))} {f(b)} l 6 -8" stroke="#5A4A3A" stroke-width="1"></path>' for k in range(8)))
    o.append(f'<rect x="{f(w * 0.78)}" y="{f(b - 50 * s)}" width="{f(26 * s)}" height="{f(50 * s)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2"></rect><path d="M{f(w * 0.78)} {f(b - 50 * s)} l {f(10 * s)} {f(-10 * s)} l {f(8 * s)} {f(6 * s)} l {f(8 * s)} {f(-8 * s)} L {f(w * 0.78 + 26 * s)} {f(b - 50 * s)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.86)}" y="{f(b - 18 * s)}" width="{f(50 * s)}" height="{f(18 * s)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2" transform="rotate(8 {f(w * 0.86)} {f(b)})"></rect>')
    return "".join(o)

def egypt_altar(w, h, seed):
    """An altar to Jehovah in the midst of the land of Egypt, and a pillar at the border thereof: an altar of stones smoking
    by the Nile among palms, a standing pillar on the border far off, the pyramids beyond."""
    o = [bg(w, h, "#8FC8E0", "#F8E8B8"), EG.pyramid(w * 0.7, h * 0.56, w * 0.18, h * 0.18), EG.pyramid(w * 0.84, h * 0.56, w * 0.12, h * 0.12), ground(w, h, h * 0.56, "#D8B880", dy=0),
         f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.68)} L {f(w + 10)} {f(h * 0.76)} C {f(w * 0.6)} {f(h * 0.82)} {f(w * 0.3)} {f(h * 0.74)} -10 {f(h * 0.78)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="1.6"></path>']
    s = min(1.0, h / 280)
    o.append(J1.palm(w * 0.1, h * 0.92, s * 0.7) + J1.palm(w * 0.86, h * 0.95, s * 0.8))
    o.append(S4.altar(w * 0.42, h * 0.95, s * 0.9, fire=True, seed=seed))
    o.append(f'<rect x="{f(w * 0.58)}" y="{f(h * 0.36)}" width="{f(10 * s)}" height="{f(h * 0.2)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>' + label(w * 0.58, h * 0.32, "THE PILLAR AT THE BORDER", "#3A2A1A", 9))
    return "".join(o)

def highway(w, h):
    """A highway out of Egypt to Assyria; Israel the third, a blessing in the midst of the earth (the map, the road gold)."""
    return nations_map(w, h, hi=("EGYPT", "NINEVEH", "JERUSALEM"), arrows=(("EGYPT", "JERUSALEM"), ("JERUSALEM", "NINEVEH")), lit="#FFD23F",
                       show=["EGYPT", "JERUSALEM", "NINEVEH", "DAMASCUS", "ETHIOPIA", "BABYLON"], note="A HIGHWAY OUT OF EGYPT TO ASSYRIA")

def sackcloth(w, h, seed):
    """Go, and loose the sackcloth from off thy loins, and put thy shoe from off thy foot: the sackcloth laid down and a pair of
    sandals left on the road outside Jerusalem (the sign told in words only)."""
    o = [bg(w, h, "#C8A880", "#F3E0B0"), J.city_hill(w * 0.8, h * 0.56, w * 0.2, h * 0.24, seed), ground(w, h, h * 0.6, "#C8B080", dy=0)]
    s = min(1.4, h / 200); b = h * 0.86
    o.append(f'<path d="M{f(w * 0.2)} {f(b)} C {f(w * 0.22)} {f(b - 30 * s)} {f(w * 0.34)} {f(b - 36 * s)} {f(w * 0.42)} {f(b - 20 * s)} C {f(w * 0.44)} {f(b - 8 * s)} {f(w * 0.38)} {f(b + 4)} {f(w * 0.2)} {f(b)} Z" fill="#6A5A40" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(w * 0.24 + k * 10 * s)} {f(b - 4)} l {f(4 * s)} {f(-20 * s)}" stroke="#4A3A2A" stroke-width="1"></path>' for k in range(10)))
    o.append(E.sandal(w * 0.56, b, s * 0.9, -10) + E.sandal(w * 0.64, b + 4, s * 0.9, 14))
    return "".join(o)
