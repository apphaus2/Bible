"""Drawings for Jeremiah chapter 10 (Jeremiah 29–31), on top of jer.art: the letter to the captivity, the exiles building and
planting by the rivers of Babylon, Babylon's walls, the book written, the yoke broken off, the virgin of Israel dancing, the
great company returning, Rachel weeping in Ramah, the waymarks, the new covenant, and the measuring line of the city."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from ezr.art import letter_scroll
from jer.art8 import seventy, figs, flock, tempest
from jer.art9 import yoke_bar

def palm(x, y, s=1.0):
    return J1.palm(x, y, s)

def babylon(w, h, seed, dusk=False, burning=False, broken=False):
    """Babylon on the Euphrates: great walls of blue-glazed brick with gold beasts, the gate, the stepped tower behind, palms on
    the river bank (burning=True: fire and smoke over it; broken=True: the walls thrown down)."""
    o = [K2.sky(w, h, "#2A1A3A" if dusk or burning else "#8FB0C8", "#E8803A" if dusk or burning else "#F3E0B0")]
    zx, zb = w * 0.62, h * 0.56
    for k in range(5):
        tw = w * (0.3 - k * 0.05); th = h * 0.07
        o.append(f'<rect x="{f(zx - tw / 2)}" y="{f(zb - th * (k + 1))}" width="{f(tw)}" height="{f(th)}" fill="{["#C8A070", "#D8B080", "#C8A070", "#D8B080", "#E8C890"][k]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(zx - w * 0.02)}" y="{f(zb - h * 0.42)}" width="{f(w * 0.04)}" height="{f(h * 0.07)}" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></rect>')
    if broken:
        o.append(wall(-10, w + 10, h * 0.5, h * 0.78, seed, color="#2A5A9A", towers=5, breach=(w * 0.2, w * 0.6)))
    else:
        o.append(wall(-10, w + 10, h * 0.46, h * 0.78, seed, color="#2A5A9A", towers=5, gate=w * 0.36))
        for k in range(6):
            x = w * (0.08 + k * 0.16)
            if abs(x - w * 0.36) < w * 0.06: continue
            o.append(f'<path d="M{f(x - 12)} {f(h * 0.66)} l 6 -8 l 14 0 l 4 -6 l 4 6 l -4 4 l 0 6 l -4 0 l -2 -4 l -10 0 l -2 4 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.22)}" fill="#2C7A9A"></rect>'
             f'<path d="M-10 {f(h * 0.84)} ' + " ".join(f"q {f(w / 20)} -6 {f(w / 10)} 0" for _ in range(11)) + '" fill="none" stroke="#E8F6FA" stroke-width="1.6"></path>')
    o.append(ground(w, h, h * 0.78, "#C8A870", dy=0).replace(f'{f(h + 10)} L -10', f'{f(h * 0.8)} L -10'))
    for k in range(3): o.append(palm(w * (0.06 + k * 0.42), h * 0.82, min(0.8, h / 380)))
    if burning:
        o += [E.blaze(w * (0.14 + i * 0.24), h * 0.6, w * 0.14, h * 0.3, seed + i, n=6) for i in range(4)]
        o.append(smoke(w * 0.4, h * 0.3, 9, seed, w=0.9) + smoke(w * 0.7, h * 0.24, 8, seed + 2, w=0.8))
    return "".join(o)

def letter(w, h, seed):
    """The words of the letter that Jeremiah sent from Jerusalem unto the elders of the captivity: a sealed scroll."""
    return letter_scroll(w, h, seed, seal="#1F3A7A", text_lines=8)

def exile_home(p, w, h, seed):
    """Build ye houses, and dwell in them; plant gardens: exiles building a house of mud brick and planting a garden by a river
    of Babylon, palms on the bank."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), f'<rect x="-10" y="{f(h * 0.52)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#2C7A9A"></rect>',
         ground(w, h, h * 0.6, "#C8B07A", dy=0), palm(w * 0.9, h * 0.62, min(0.8, h / 380)), palm(w * 0.06, h * 0.62, min(0.7, h / 420))]
    hx = w * 0.56
    o.append(f'<rect x="{f(hx)}" y="{f(h * 0.62)}" width="{f(w * 0.24)}" height="{f(h * 0.3)}" fill="#C8986A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(hx)} {f(h * (0.66 + k * 0.05))} L {f(hx + w * 0.24)} {f(h * (0.66 + k * 0.05))}" stroke="#8A5A3A" stroke-width="1.2"></path>' for k in range(5))
             + f'<rect x="{f(hx + w * 0.1)}" y="{f(h * 0.78)}" width="{f(w * 0.05)}" height="{f(h * 0.14)}" fill="#3A2214"></rect>')
    for k in range(6):
        o.append(f'<path d="M{f(w * (0.08 + k * 0.05))} {f(b)} l 0 -14 m -6 4 l 6 -4 l 6 4" stroke="#3E7A3A" stroke-width="3" fill="none"></path>')
    s = fit(b, max(h * 0.4, b - 220))
    o.append(man(p, w * 0.46, b, s, "#6A5A3A", up=[(-22, -158), (-26, -190), (-10, -206)]) + R1.sack(w * 0.46 - 6 * s, b - 196 * s, 0.5 * s))
    o.append(woman(p, w * 0.36, b, s * 0.94, "#8A5A6A", up=[(-22, -158), (-46, -130), (-60, -104)]))
    return "".join(o)

def reading_letter(p, w, h, seed, age=2):
    """Zephaniah the priest read this letter in the ears of Jeremiah the prophet."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A880", "#F3E0B0"), temple_front(w * 0.7, h * 0.66, w * 0.4, seed), ground(w, h, h * 0.66, "#D8C8A0", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(priest(p, w * 0.56, b, s, flip=True, up=[(22, -158), (40, -150), (60, -140)]))
    o.append(f'<rect x="{f(w * 0.56 - 80 * s)}" y="{f(b - 156 * s)}" width="{f(30 * s)}" height="{f(36 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(jer_fig(p, w * 0.3, b, s, age=age))
    return "".join(o)

def book_writing(w, h, seed):
    """Write thee all the words that I have spoken unto thee in a book: an open roll on a table, a reed pen and an inkhorn."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', glow(w * 0.5, h * 0.4, min(w, h) * 0.6, color="#FFE680", op=0.25, uid=f"bw{seed}"),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.24)}" y="{f(h * 0.5)}" width="{f(w * 0.48)}" height="{f(h * 0.26)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<ellipse cx="{f(w * 0.24)}" cy="{f(h * 0.63)}" rx="{f(w * 0.025)}" ry="{f(h * 0.14)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
         f'<ellipse cx="{f(w * 0.72)}" cy="{f(h * 0.63)}" rx="{f(w * 0.025)}" ry="{f(h * 0.14)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    r = random.Random(seed)
    for k in range(5):
        y = h * (0.55 + k * 0.04); x = w * 0.28; end = w * (0.68 if k < 4 else 0.46)
        while x < end:
            L = w * r.uniform(0.02, 0.05)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(min(L, end - x))} 0" stroke="#3A2A1A" stroke-width="2"></path>'); x += L + w * 0.01
    o.append(f'<path d="M{f(w * 0.48)} {f(h * 0.7)} L {f(w * 0.62)} {f(h * 0.36)}" stroke="#C8A060" stroke-width="4" stroke-linecap="round"></path>'
             f'<rect x="{f(w * 0.78)}" y="{f(h * 0.5)}" width="{f(w * 0.05)}" height="{f(h * 0.12)}" rx="4" fill="#3A3A3A" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def trembling(p, w, h, seed):
    """Wherefore do I see every man with his hands on his loins, as a woman in travail, and all faces turned into paleness?:
    men standing bent in a pale street."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A6A7A", "#C8C8C8"), empty_city(w, h * 0.96, seed)]
    s = fit(b, max(h * 0.44, b - 210))
    for i in range(4):
        o.append(man(p, w * (0.2 + i * 0.2), b, s * (0.96 + (i % 2) * 0.04), ["#5A5A6A", "#6A5A4A", "#4A4A5A", "#6A6A5A"][i], flip=i % 2 == 1,
                     up=[(-22, -158), (-30, -126), (-14, -100)], body="#B8A8A0"))
    return "".join(o)

def yoke_off(w, h, seed):
    """I will break his yoke from off thy neck, and will burst thy bonds: a yoke snapped in two, its thongs burst, in light."""
    o = [K2.sky(w, h, "#3A3A7A", "#FFE0A0"), V.rays(w * 0.5, h * 0.5, 30, 10, max(w, h), color="#FFF4C2", op=0.3), ground(w, h, h * 0.8, "#8A7A5A", dy=0)]
    s = min(2.0, h / 140)
    o.append(f'<g transform="rotate(-18 {f(w * 0.36)} {f(h * 0.7)})"><rect x="{f(w * 0.2)}" y="{f(h * 0.7)}" width="{f(w * 0.16)}" height="{f(10 * s)}" rx="4" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2.4"></rect></g>'
             f'<g transform="rotate(22 {f(w * 0.62)} {f(h * 0.7)})"><rect x="{f(w * 0.62)}" y="{f(h * 0.7)}" width="{f(w * 0.16)}" height="{f(10 * s)}" rx="4" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2.4"></rect></g>'
             f'<path d="M{f(w * 0.36)} {f(h * 0.62)} l 6 -16 l 6 10 l 8 -14 M{f(w * 0.6)} {f(h * 0.62)} l -4 -14 l -8 8" stroke="#FFE680" stroke-width="3" fill="none"></path>')
    return "".join(o)

def city_rebuilt(p, w, h, seed):
    """The city builded upon its own hill, and the palace inhabited; thanksgiving and the voice of them that make merry."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FC0E0", "#FFF0C8"), jerusalem(w * 0.3, w * 0.98, h * 0.7, h * 0.2, seed, color="#E8D8A8"), ground(w, h, h * 0.7, "#C8B880", dy=0)]
    s = fit(b, max(h * 0.5, b - 180))
    for i in range(3):
        o.append(S3.musician(p, w * (0.08 + i * 0.12), b, s, kind=("timbrel", "harp", "cymbals")[i], cloth=["#C2456A", "#3A6A8A", "#E8B830"][i], woman=i != 1, seed=seed + i))
    return "".join(o)

def dancers(p, w, h, seed):
    """Again shalt thou be adorned with thy tabrets, O virgin of Israel, and go forth in the dances; vineyards planted upon the
    mountains of Samaria."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FC0E0", "#FFF0C8"), hills(w, h, h * 0.46, seed, "#5A8A4A", amp=18, step=70)]
    for r_ in range(3):
        for c in range(10):
            o.append(f'<circle cx="{f(w * (0.04 + c * 0.1 + (r_ % 2) * 0.05))}" cy="{f(h * (0.52 + r_ * 0.05))}" r="{f(w * 0.014)}" fill="#3E6A3A" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    o.append(ground(w, h, h * 0.68, "#B8C07A", dy=0))
    s = fit(b, max(h * 0.4, b - 210))
    for i in range(4):
        o.append(S3.musician(p, w * (0.2 + i * 0.18), b, s, kind="timbrel", cloth=["#C2456A", "#E8B830", "#7A3BA8", "#2E8A8A"][i], woman=True, seed=seed + i))
    return "".join(o)

def ephraim_watch(p, w, h, seed):
    """The watchmen upon the hills of Ephraim shall cry, Arise ye, and let us go up to Zion: a watchman with the horn on a green
    hilltop at dawn."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A5A8A", "#FFD8A0"), sun(w * 0.8, h * 0.6, min(w, h) * 0.06, color="#FFE680", op=0.35), hills(w, h, h * 0.62, seed, "#4A6A3A", amp=14, step=80),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} C {f(w * 0.1)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.48)} {f(w * 0.46)} {f(h * 0.7)} L {f(w * 0.56)} {f(h + 10)} Z" fill="#3E6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(h * 0.52, h * 0.16)
    o.append(horn_man(p, w * 0.2, h * 0.52, s, flip=False, cloth="#5A6A3A") + J.blasts(w * 0.2 + 44 * s, h * 0.52 - 186 * s, s, n=4))
    return "".join(o)

def great_company(p, w, h, seed):
    """A great company shall return hither, the blind and the lame, the woman with child: walking by rivers of waters in a
    straight way."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#FFE8C0"), hills(w, h, h * 0.5, seed, "#7A8A5A", amp=10, step=80), ground(w, h, h * 0.6, "#C8B880", dy=0),
         f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.64)}" stroke="#2C9DB8" stroke-width="{f(h * 0.03)}" fill="none"></path>']
    s = fit(b, max(h * 0.42, b - 210))
    cols = ["#6A5A3A", "#8A5A6A", "#3A5A6A", "#6A3A2A", "#5A6A3A", "#7A6A4A", "#5A4A6A"]
    for i in range(7):
        x = w * (0.08 + i * 0.13)
        if i == 2: o.append(man(p, x, b, s, cols[i], flip=True, up=[(22, -158), (40, -120), (60, -10)]) + f'<path d="M{f(x - 60 * s)} {f(b - 10 * s)} L {f(x - 40 * s)} {f(b - 120 * s)}" stroke="#5A3A1E" stroke-width="3"></path>')
        elif i % 2: o.append(woman(p, x, b, s * 0.94, cols[i], flip=True))
        else: o.append(man(p, x, b, s * (0.9 + (i % 3) * 0.05), cols[i], flip=True))
    return "".join(o)

def plenty(w, h, seed):
    """The grain, the new wine, the oil, the young of the flock and of the herd: their soul as a watered garden."""
    o = [K2.sky(w, h, "#8FC0E0", "#FFF0C8"), hills(w, h, h * 0.5, seed, "#5A8A4A", amp=12, step=80), ground(w, h, h * 0.62, "#9AB85A", dy=0),
         R1.field(-10, w * 0.4, h * 0.86, h * 0.24, seed, rows=2), jar(w * 0.5, h * 0.94, min(0.9, h / 260), color="#B8703A"), jar(w * 0.58, h * 0.94, min(0.8, h / 300), color="#C8A04A", stopper="#3A5A2A"),
         N.grapes(w * 0.66, h * 0.8, min(0.5, h / 600), seed)]
    s = min(0.7, h / 380)
    for i in range(3): o.append(E.sheep(w * (0.76 + i * 0.08), h * (0.9 - (i % 2) * 0.04), s))
    return "".join(o)

def rachel(p, w, h, seed):
    """A voice is heard in Ramah, Rachel weeping for her children: a woman seated alone on the hill by the road at night, a
    pillar on the grave behind her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14122A"), J.moon(w * 0.82, h * 0.2, min(w, h) * 0.05),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.6)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<rect x="{f(w * 0.62)}" y="{f(h * 0.4)}" width="{f(w * 0.04)}" height="{f(h * 0.2)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.5, b - 200))
    o.append(E.kneel(w * 0.38, b, s, color="#5A3A5A", skin="#9A7A6A"))
    return "".join(o)

def calf_yoke(w, h, seed):
    """As a calf unaccustomed to the yoke: a young bullock straining against the yoke on its neck."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), ground(w, h, h * 0.66, "#B89A6A", dy=0)]
    s = min(1.6, h / 170)
    x, y = w * 0.46, h * 0.94
    o.append(S1.calf(x, y, s, flip=False, color="#8A5A30"))
    o.append(f'<rect x="{f(x + 10 * s)}" y="{f(y - 64 * s)}" width="{f(50 * s)}" height="{f(7 * s)}" rx="3" transform="rotate(-20 {f(x + 30 * s)} {f(y - 60 * s)})" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def waymarks(w, h, seed):
    """Set thee up waymarks, make thee guide-posts; set thy heart toward the highway: stone cairns along a road leading home."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), hills(w, h, h * 0.44, seed, "#8A8A5A", amp=12, step=80), ground(w, h, h * 0.54, "#C8B07A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.48)} {f(h * 0.54)} L {f(w * 0.52)} {f(h * 0.54)} L {f(w * 0.8)} {f(h + 10)} Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></path>']
    for i, (x, y, k) in enumerate(((0.24, 0.96, 1.0), (0.38, 0.72, 0.6), (0.44, 0.6, 0.36), (0.86, 0.96, 1.0), (0.66, 0.72, 0.6), (0.57, 0.6, 0.36))):
        s = min(1.0, h / 260) * k
        o.append(f'<path d="M{f(w * x - 20 * s)} {f(h * y)} L {f(w * x - 14 * s)} {f(h * y - 18 * s)} L {f(w * x - 8 * s)} {f(h * y - 30 * s)} L {f(w * x + 8 * s)} {f(h * y - 30 * s)} L {f(w * x + 14 * s)} {f(h * y - 18 * s)} L {f(w * x + 20 * s)} {f(h * y)} Z" fill="#A89A8A" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<rect x="{f(w * x - 3 * s)}" y="{f(h * y - 70 * s)}" width="{f(6 * s)}" height="{f(42 * s)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def sweet_sleep(w, h, seed):
    """Upon this I awaked, and beheld; and my sleep was sweet unto me: dawn over the hills of Judah, husbandmen and flocks."""
    o = [K2.sky(w, h, "#4A4A8A", "#FFD8A0"), sun(w * 0.5, h * 0.62, min(w, h) * 0.06, color="#FFE680", op=0.4), hills(w, h, h * 0.64, seed, "#5A7A4A", amp=12, step=80),
         ground(w, h, h * 0.74, "#9AB85A", dy=0)]
    s = min(0.6, h / 400)
    for i in range(5): o.append(E.sheep(w * (0.1 + i * 0.08), h * (0.9 - (i % 2) * 0.03), s))
    return "".join(o)

def sower(p, w, h, seed):
    """I will sow the house of Israel and the house of Judah with the seed of man, and with the seed of beast: a sower in a
    ploughed field."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), ground(w, h, h * 0.56, "#8A5A30", dy=0)]
    for k in range(8):
        o.append(f'<path d="M-10 {f(h * (0.6 + k * 0.05))} L {f(w + 10)} {f(h * (0.58 + k * 0.05))}" stroke="#6A4020" stroke-width="2"></path>')
    s = fit(b, max(h * 0.4, b - 220))
    o.append(man(p, w * 0.4, b, s, "#7A6A4A", up=[(-22, -158), (-50, -170), (-76, -160)], extra=A.headcloth("#7A6A4A")))
    r = random.Random(seed)
    o.append("".join(f'<circle cx="{f(w * 0.4 - 80 * s - r.uniform(0, 80))}" cy="{f(b - 150 * s + r.uniform(0, 120))}" r="2.4" fill="#E8C88A"></circle>' for _ in range(20)))
    for i in range(3): o.append(E.sheep(w * (0.7 + i * 0.09), h * 0.9, min(0.6, s)))
    return "".join(o)

def sour_grapes(w, h, seed):
    """The fathers have eaten sour grapes, and the children's teeth are set on edge: a cluster of green unripe grapes."""
    o = [K2.sky(w, h, "#C8B880", "#F3E8C8"), N.grapes(w * 0.5, h * 0.36, min(1.6, h / 150), seed).replace("#5A1A6E", "#8AAA3A").replace("#C8A0E0", "#E0F0A0")]
    return "".join(o)

def covenant_tables(w, h, seed, broken=False):
    """The covenant made with their fathers when he took them by the hand out of Egypt, which my covenant they brake: the two
    tables of stone (broken=True: the pieces)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1430"></rect>', V.rays(w * 0.5, h * 0.6, 24, 10, max(w, h), color="#FFD23F", op=0.12)]
    s = min(1.4, h / 220)
    o.append(V.shards(w * 0.5, h * 0.86, s, seed) if broken else V.tables(w * 0.5, h * 0.9, s, uid=f"ct{seed}"))
    return "".join(o)

def new_covenant(p, w, h, seed):
    """I will put my law in their inward parts, and in their heart will I write it; they shall all know me, from the least of
    them unto the greatest: a people in the morning light, young and old together."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A7A", "#FFE0A0"), V.rays(w * 0.5, h * 0.7, 30, 10, max(w, h), color="#FFF4C2", op=0.3), ground(w, h, h * 0.72, "#C8B880", dy=0)]
    s = fit(b, max(h * 0.42, b - 210))
    cols = ["#6A5A3A", "#8A5A6A", "#3A5A6A", "#6A3A2A", "#5A6A3A", "#7A6A4A"]
    for i in range(6):
        x = w * (0.1 + i * 0.16); k = [1.0, 0.94, 0.62, 1.0, 0.94, 0.7][i]
        o.append(man(p, x, b, s * k, cols[i], extra=A.headcloth(cols[i]) + (A.WHITE_BEARD if i == 3 else "")) if i % 3 == 0 else woman(p, x, b, s * k, cols[i]) if i % 3 == 1 else S1.boy(p, x, b, s * k))
    return "".join(o)

def ordinances(w, h, seed):
    """Who giveth the sun for a light by day, and the moon and the stars for a light by night, who stirreth up the sea so that
    the waves thereof roar."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h * 0.6)}" fill="#8FC0E0"></rect>',
         mk.stars(30, w * 0.5, h * 0.5, seed), J.moon(w * 0.22, h * 0.2, min(w, h) * 0.05), sun(w * 0.78, h * 0.24, min(w, h) * 0.06),
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#1F6F9A"></rect>']
    for k in range(4):
        y = h * (0.66 + k * 0.08)
        o.append(f'<path d="M-10 {f(y)} ' + " ".join(f"q {f(w / 16)} -14 {f(w / 8)} 0" for _ in range(9)) + '" fill="none" stroke="#E8F6FA" stroke-width="2.4"></path>')
    return "".join(o)

CITY_M = [("THE TOWER OF HANANEL", 0.62, 0.12), ("THE GATE OF THE CORNER", 0.12, 0.3), ("THE HILL GAREB", 0.08, 0.62), ("GOAH", 0.24, 0.76),
          ("THE VALLEY OF THE DEAD BODIES AND OF THE ASHES", 0.46, 0.84), ("THE BROOK KIDRON", 0.9, 0.56), ("THE HORSE GATE", 0.78, 0.36)]
def measuring_line(w, h):
    """The city built to Jehovah from the tower of Hananel unto the gate of the corner; the measuring line onward to the hill
    Gareb and Goah; the valley of the dead bodies and of the ashes, the fields unto the brook Kidron, the horse gate — a plan."""
    o = [grid_bg(w, h)]
    pts = [(w * x, h * y) for _, x, y in CITY_M]
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.12)} L {f(w * 0.12)} {f(h * 0.3)} L {f(w * 0.08)} {f(h * 0.62)} L {f(w * 0.24)} {f(h * 0.76)} L {f(w * 0.46)} {f(h * 0.84)} L {f(w * 0.82)} {f(h * 0.66)} L {f(w * 0.78)} {f(h * 0.36)} Z" fill="#FFD23F" fill-opacity="0.12" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="10 6"></path>')
    o.append(f'<path d="M{f(w * 0.9)} {f(h * 0.06)} C {f(w * 0.88)} {f(h * 0.4)} {f(w * 0.92)} {f(h * 0.7)} {f(w * 0.86)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>')
    for (nm, x, y) in CITY_M:
        anchor = "start" if x < 0.3 else "end" if x > 0.7 else "middle"
        o.append(node(w * x, h * y, nm, "#FFD23F" if "VALLEY" not in nm else "#FF8A6A", r=4, dy=-10, anchor=anchor, size=8))
    o.append(label(w * 0.48, h * 0.5, "HOLY UNTO JEHOVAH", "#FFD23F", 12))
    return "".join(o)
