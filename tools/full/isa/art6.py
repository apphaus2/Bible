"""Isaiah 21–23 drawings (on top of isa.art5): the watchman on his tower by night, whirlwinds in the South, the Dedanites'
caravans, the valley of vision (Jerusalem's housetops, the valleys full of chariots, a plan of the breaches and the two
pools), Shebna's sepulchre on high, the key and the nail, Tyre on its rock and the ships of Tarshish."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art5 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower

def watch_tower(p, w, h, seed, troop=False, dawn=False):
    """The watchman set on his watch-tower: a stone tower in the night, a figure on top with a hand to his brow; troop=True:
    far off a troop of horsemen in pairs, asses and camels; dawn=True: the first light on the edge of the sky."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(w, h, "#05051A", "#2A2050" if not dawn else "#C86A4A"), mk.stars(50, w, h * 0.5, seed)]
    if dawn: o.append(f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#FF8A3D" opacity="0.4"></rect>')
    o.append(J.moon(w * 0.82, h * 0.14, min(16, h * 0.05)))
    o.append(hills(w, h, h * 0.62, seed, color="#14102A", amp=10) + ground(w, h, h * 0.7, "#1A1630", dy=0))
    tw, th = min(w * 0.14, h * 0.34), h * 0.62
    o.append(tower(w * 0.2, b, tw, th, color="#4A4058"))
    s = fit(b - th, b - th - h * 0.16)
    o.append(mk.person(p, round(w * 0.2), round(b - th - th * 0.04), round(s, 3), body="#6A4A3A", cloth="#5A6A8A", kind="Tunic", sw=2, up=[(-22, -158), (-6, -176), (12, -184)]))
    if troop:
        k = min(0.36, h / 900)
        for i in range(3):
            x = w * (0.56 + i * 0.1); y = h * 0.74
            o.append(E3.horse(x, y, k, color="#0D0D12") + E3.horse(x + 16, y + 4, k, color="#14141A"))
        o.append(J1.camel(w * 0.9, h * 0.8, k * 1.2, color="#2A2026") + N.ass(w * 0.48, h * 0.8, k * 1.2, color="#2A2830"))
    return "".join(o)

def whirlwind(w, h, seed):
    """As whirlwinds in the South sweep through, it cometh from the wilderness, from a terrible land: columns of whirling sand
    crossing a desert plain under a hot sky."""
    r = random.Random(seed)
    o = [bg(w, h, "#C86A3A", "#F3C890"), ground(w, h, h * 0.66, "#D8A870", dy=0)]
    for k in range(3):
        cx = w * (0.2 + k * 0.3); b = h * 0.9
        for i in range(10):
            y = b - i * h * 0.07; rx = w * (0.02 + i * 0.012)
            o.append(f'<ellipse cx="{f(cx + math.sin(i * 0.8 + k) * w * 0.02)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(h * 0.02)}" fill="none" stroke="#8A5A3A" stroke-width="2" opacity="{0.8 - i * 0.05:.2f}"></ellipse>')
    return "".join(o)

def dedanites(p, w, h, seed):
    """In the forest in Arabia shall ye lodge, O ye caravans of Dedanites; the inhabitants of Tema met the fugitives with
    their bread: camels couched among the thickets at evening, travellers by a small fire, a woman bringing water."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#3A2A4A", "#C87A4A"), ground(w, h, h * 0.66, "#8A6A4A", dy=0)]
    for i in range(9):
        x = w * (0.04 + i * 0.12); y = h * 0.7
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.16)}" stroke="#3A2A1A" stroke-width="3"></path><circle cx="{f(x)}" cy="{f(y - h * 0.2)}" r="{f(h * 0.06)}" fill="#3A4A2A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    k = min(0.5, h / 600)
    o.append(J1.camel(w * 0.2, b, k, color="#B5844A") + J1.camel(w * 0.36, b - 6, k * 0.9, color="#A8743A", flip=True))
    o.append(E.blaze(w * 0.56, b, w * 0.04, h * 0.1, seed, n=4))
    s = fit(b, max(h * 0.55, b - 140))
    o.append(man(p, w * 0.5, b, s, "#6A4A3A") + man(p, w * 0.62, b, s * 0.96, "#4A4A5A", flip=True))
    o.append(woman(p, w * 0.8, b, s * 0.94, "#2E6B8A", flip=True, up=[(-22, -158), (-36, -150), (-50, -152)]))
    return "".join(o)

def valley_vision(p, w, h, seed):
    """What aileth thee now, that thou art wholly gone up to the housetops?: Jerusalem's flat roofs crowded with people looking
    out over the valley, a tumultuous city at dusk."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(w, h, "#5A4A7A", "#E8A06A")]
    x = -10; s = min(0.34, h / 700)
    while x < w:
        bw = r.uniform(70, 120); top = h * r.uniform(0.46, 0.62)
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(bw)}" height="{f(h - top + 10)}" fill="{r.choice(["#C8A88A", "#B89878", "#D8B898"])}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.4)}" y="{f(top + 30)}" width="12" height="18" fill="#2A1E1A"></rect>')
        for k in range(r.randint(2, 3)):
            o.append((man if r.random() < 0.6 else woman)(p, x + bw * (0.2 + k * 0.3), top, s, r.choice(["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#7A6A2A", "#C2456A"]), flip=r.random() < 0.5,
                                                         up=[(-22, -158), (-30, -190), (-24, -222)] if r.random() < 0.3 else None))
        x += bw
    return "".join(o)

def valley_chariots(w, h, seed):
    """Thy choicest valleys were full of chariots, and the horsemen set themselves in array at the gate: the valley below the
    walls filled with chariots, the city gate shut above."""
    r = random.Random(seed)
    o = [bg(w, h, "#6A5A7A", "#E8B88A"), f'<rect x="{f(w * 0.56)}" y="{f(h * 0.18)}" width="{f(w * 0.46)}" height="{f(h * 0.36)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(8):
        o.append(f'<rect x="{f(w * 0.56 + i * w * 0.06)}" y="{f(h * 0.14)}" width="{f(w * 0.03)}" height="{f(h * 0.05)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.54)} L {f(w * 0.72)} {f(h * 0.36)} Q {f(w * 0.77)} {f(h * 0.3)} {f(w * 0.82)} {f(h * 0.36)} L {f(w * 0.82)} {f(h * 0.54)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.56, "#9A7A5A", dy=0))
    k = min(0.42, h / 760)
    for i in range(10):
        o.append(E3.chariot(w * r.uniform(0.04, 0.9), h * r.uniform(0.66, 0.96), k * r.uniform(0.8, 1.1), flip=r.random() < 0.5, color="#3A2A1A", driver="#2A1A10"))
    return "".join(o)

def jerusalem_plan(w, h):
    """The breaches of the city of David were many; ye gathered together the waters of the lower pool, brake down houses to
    fortify the wall, and made a reservoir between the two walls for the water of the old pool (a plan)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.62)} {f(h * 0.12)} L {f(w * 0.66)} {f(h * 0.78)} L {f(w * 0.42)} {f(h * 0.9)} L {f(w * 0.28)} {f(h * 0.6)} Z" fill="none" stroke="#8FD0E2" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.24)} {f(h * 0.62)} L {f(w * 0.4)} {f(h * 0.96)} L {f(w * 0.46)} {f(h * 0.96)}" fill="none" stroke="#8FD0E2" stroke-width="2" stroke-dasharray="8 4"></path>')
    for x, y in ((0.31, 0.3), (0.64, 0.4), (0.6, 0.7), (0.33, 0.66)):
        o.append(f'<path d="M{f(w * x - 8)} {f(h * y - 8)} L {f(w * x + 8)} {f(h * y + 8)} M{f(w * x + 8)} {f(h * y - 8)} L {f(w * x - 8)} {f(h * y + 8)}" stroke="#D7261E" stroke-width="3"></path>')
    o.append(label(w * 0.47, h * 0.42, "THE CITY OF DAVID", "#8FD0E2", 10) + label(w * 0.66, h * 0.36, "THE BREACHES", "#FF8A6A", 9, "start"))
    o.append(f'<ellipse cx="{f(w * 0.36)}" cy="{f(h * 0.9)}" rx="{f(w * 0.05)}" ry="{f(h * 0.04)}" fill="#2C7DA8" stroke="#8FD0E2" stroke-width="1.6"></ellipse>' + label(w * 0.24, h * 0.95, "THE LOWER POOL", "#8FD0E2", 9))
    o.append(f'<ellipse cx="{f(w * 0.28)}" cy="{f(h * 0.72)}" rx="{f(w * 0.025)}" ry="{f(h * 0.04)}" fill="#2C7DA8" stroke="#FFD23F" stroke-width="1.6"></ellipse>' + label(w * 0.31, h * 0.74, "THE RESERVOIR BETWEEN THE TWO WALLS", "#FFD23F", 9, "start"))
    o.append(f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.36)}" rx="{f(w * 0.04)}" ry="{f(h * 0.04)}" fill="#2C7DA8" stroke="#8FD0E2" stroke-width="1.6"></ellipse>' + label(w * 0.2, h * 0.28, "THE OLD POOL", "#8FD0E2", 9)
             + route([(w * 0.22, h * 0.4), (w * 0.27, h * 0.66)], color="#8FD0E2"))
    for i in range(5):
        o.append(f'<rect x="{f(w * 0.72 + i * 14)}" y="{f(h * 0.6)}" width="10" height="10" fill="none" stroke="#FF8A6A" stroke-width="1.4"></rect>')
    o.append(label(w * 0.78, h * 0.68, "HOUSES BROKEN DOWN", "#FF8A6A", 9) + route([(w * 0.72, h * 0.62), (w * 0.66, h * 0.58)], color="#FF8A6A"))
    return "".join(o)

def sepulchre_high(p, w, h, seed):
    """That thou hast hewed thee out here a sepulchre on high, graving a habitation for himself in the rock: a tomb being
    cut high in a cliff, the treasurer's mason on a scaffold, Shebna below in his robes of office."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(w, h, "#8FB0D8", "#F3E0B0"), f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.36)} {f(h * 0.04)} L {f(w + 10)} -10 L {f(w + 10)} {f(h + 10)} Z" fill="#B8987A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.0, h / 300); cx, cy = w * 0.62, h * 0.3
    o.append(f'<path d="M{f(cx - 34 * s)} {f(cy + 40 * s)} L {f(cx - 34 * s)} {f(cy)} Q {f(cx)} {f(cy - 30 * s)} {f(cx + 34 * s)} {f(cy)} L {f(cx + 34 * s)} {f(cy + 40 * s)} Z" fill="#2A1E1A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 50 * s)}" y="{f(cy - 40 * s)}" width="{f(100 * s)}" height="{f(8 * s)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(cx - 70 * s)} {f(cy + 44 * s)} L {f(cx + 70 * s)} {f(cy + 44 * s)} M{f(cx - 60 * s)} {f(cy + 44 * s)} L {f(cx - 60 * s)} {f(b)} M{f(cx + 60 * s)} {f(cy + 44 * s)} L {f(cx + 60 * s)} {f(b)}" stroke="#6A4A2A" stroke-width="{f(4 * s)}"></path>')
    o.append(mk.person(p, round(cx + 20 * s), round(cy + 44 * s), round(0.24 * s, 3), body="#3A1E14", cloth="#8A7A5A", kind="Tunic", sw=2, up=[(-22, -158), (-40, -186), (-60, -200)]))
    o.append(ground(w, h, b, "#A88A6A", dy=0))
    o.append(mk.person(p, round(w * 0.14), round(b), round(fit(b, max(h * 0.55, b - 150)), 3), body="#3A1E14", cloth="#7A5A1A", sw=3, up=[(22, -158), (40, -186), (60, -210)]))
    return "".join(o)

def key_nail(w, h):
    """The key of the house of David upon his shoulder; a nail in a sure place, and upon it all the glory of his father's
    house, every small vessel, from the cups even to all the flagons (a plate)."""
    o = [grid_bg(w, h)]
    s = min(1.3, h / 220)
    kx, ky = w * 0.26, h * 0.56
    o.append(f'<path d="M{f(kx - 110 * s)} {f(ky)} L {f(kx + 60 * s)} {f(ky)}" stroke="#E8B830" stroke-width="{f(10 * s)}" stroke-linecap="round"></path>'
             f'<circle cx="{f(kx + 80 * s)}" cy="{f(ky)}" r="{f(24 * s)}" fill="none" stroke="#E8B830" stroke-width="{f(9 * s)}"></circle>'
             f'<path d="M{f(kx - 100 * s)} {f(ky)} L {f(kx - 100 * s)} {f(ky + 30 * s)} M{f(kx - 80 * s)} {f(ky)} L {f(kx - 80 * s)} {f(ky + 22 * s)}" stroke="#E8B830" stroke-width="{f(8 * s)}"></path>'
             + label(kx, ky + 60 * s, "THE KEY OF THE HOUSE OF DAVID", GOLD, 9))
    nx, ny = w * 0.7, h * 0.3
    o.append(f'<rect x="{f(nx - 120 * s)}" y="{f(ny - 30 * s)}" width="{f(240 * s)}" height="{f(14 * s)}" fill="#5A5A6A" stroke="#8FD0E2" stroke-width="1.4"></rect>'
             f'<path d="M{f(nx)} {f(ny - 16 * s)} L {f(nx)} {f(ny + 10 * s)}" stroke="#C8D0D8" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>')
    for i in range(5):
        x = nx + (i - 2) * 40 * s; y = ny + 20 * s + abs(i - 2) * 8 * s
        o.append(f'<path d="M{f(nx)} {f(ny + 6 * s)} L {f(x)} {f(y)}" stroke="#8FD0E2" stroke-width="1.2"></path>'
                 + (f'<path d="M{f(x - 10 * s)} {f(y)} L {f(x + 10 * s)} {f(y)} L {f(x + 6 * s)} {f(y + 18 * s)} L {f(x - 6 * s)} {f(y + 18 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>' if i % 2 == 0 else
                    f'<path d="M{f(x - 8 * s)} {f(y)} L {f(x + 8 * s)} {f(y)} C {f(x + 16 * s)} {f(y + 20 * s)} {f(x + 12 * s)} {f(y + 40 * s)} {f(x)} {f(y + 44 * s)} C {f(x - 12 * s)} {f(y + 40 * s)} {f(x - 16 * s)} {f(y + 20 * s)} {f(x - 8 * s)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.4"></path>'))
    o.append(label(nx, ny + 100 * s, "A NAIL IN A SURE PLACE · THE CUPS · THE FLAGONS", CYAN, 9))
    return "".join(o)

def tyre(w, h, seed, state="howl"):
    """Tyre, the stronghold of the sea: the walled city on its rock in the sea with the ships of Tarshish; state 'howl': ships
    turned away under a dark sky, smoke over the city; 'waste': the walls broken, no house, no entering in; 'trade': the
    city whole again, ships laden with merchandise."""
    r = random.Random(seed)
    dark = state != "trade"
    o = [bg(w, h, "#3A3A5A" if dark else "#8FC8E8", "#C88A6A" if dark else "#F8E8C0"),
         f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#1F5A7A"></rect>',
         f'<path d="M{f(w * 0.28)} {f(h * 0.62)} L {f(w * 0.3)} {f(h * 0.54)} L {f(w * 0.34)} {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.46)} L {f(w * 0.66)} {f(h * 0.48)} L {f(w * 0.7)} {f(h * 0.54)} L {f(w * 0.74)} {f(h * 0.62)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>'
         f'<path d="M{f(w * 0.3)} {f(h * 0.58)} L {f(w * 0.72)} {f(h * 0.58)}" stroke="#6A5A4A" stroke-width="2"></path>']
    x = w * 0.35
    while x < w * 0.65:
        bw = r.uniform(18, 34); bh = r.uniform(h * 0.08, h * 0.22)
        if state == "waste": bh *= 0.4
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.5 - bh)}" width="{f(bw)}" height="{f(bh)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 + (f'<rect x="{f(x + bw * 0.3)}" y="{f(h * 0.5 - bh * 0.7)}" width="{f(bw * 0.3)}" height="{f(bh * 0.18)}" fill="#2A1E1A"></rect>' if state != "waste" else ""))
        x += bw
    o.append(f'<rect x="{f(w * 0.33)}" y="{f(h * 0.47)}" width="{f(w * 0.36)}" height="{f(h * 0.04)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="1.6"></rect>' if state != "waste" else "")
    if state != "trade": o.append(smoke(w * 0.5, h * 0.42, 7, seed, r0=h * 0.04, color="#3A3036", op=0.6))
    for i, (sx, sy, fl) in enumerate(((0.12, 0.74, True), (0.86, 0.7, False), (0.8, 0.86, False), (0.2, 0.9, True))):
        o.append(K1.ship(w * sx, h * sy, min(0.6, h / 500) * (1.1 if sy > 0.8 else 0.9), flip=fl if state != "trade" else not fl))
    return "".join(o)
