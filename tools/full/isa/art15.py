"""Isaiah 52–55 drawings (on top of isa.art14). The servant of 52:13–53:12 is never drawn: a root out of a dry ground, a lamb
silent before its shearers, sheep gone astray, an empty grave hewn in the rock among the rich man's tombs, a portion divided
with the great. Also: Zion shaking herself from the dust, the feet of him that bringeth good tidings on the mountains, the
watchmen singing, the vessels borne out, the barren woman's tent enlarged, the waters of Noah and the bow, the stones in fair
colors (a plate), the smith at his coals, ho every one that thirsteth, the rain and the snow, the trees clapping their hands."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art14 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def zion_rise(p, w, h, seed):
    """Awake, awake, put on thy strength, O Zion; shake thyself from the dust; arise, sit on thy throne, O Jerusalem: loose
    thyself from the bonds of thy neck: a woman rising from the dust at dawn, broken bonds at her feet, a bright garment held
    up, the city on its hill behind her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#6A7ABA", "#FFE0A8"), V.rays(w * 0.7, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.35),
         J.city_hill(w * 0.72, h * 0.66, w * 0.26, h * 0.3, seed), K1.temple_front(w * 0.72, h * 0.42, min(w * 0.1, h * 0.24), seed), ground(w, h, h * 0.7, "#C8A878", dy=0)]
    s = fit(b, max(h * 0.4, b - 210))
    o.append(woman(p, w * 0.32, b, s, "#F3EFE6", up=[(-22, -158), (-30, -190), (-24, -222)]))
    o.append(J2.fetters(w * 0.2, b, min(0.8, h / 360)))
    for _ in range(8):
        r = random.Random(seed + _)
        o.append(f'<circle cx="{f(w * 0.32 + r.uniform(-50, 50))}" cy="{f(b - r.uniform(0, 40))}" r="{f(r.uniform(2, 4))}" fill="#C8A878" opacity="0.7"></circle>')
    return "".join(o)

def good_tidings(p, w, h, seed):
    """How beautiful upon the mountains are the feet of him that bringeth good tidings; the voice of thy watchmen, together do
    they sing: a runner coming over the mountain-tops at sunrise, watchmen on the city wall below lifting their voices."""
    o = [mk.defs(p, *ALL), bg(w, h, "#5A6ABA", "#FFD8A0"), sun(w * 0.2, h * 0.22, min(26, h * 0.07), color="#FFF4C2", op=0.45),
         f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.16)} {f(h * 0.24)} L {f(w * 0.34)} {f(h * 0.46)} L {f(w * 0.5)} {f(h * 0.32)} L {f(w * 0.62)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A8A" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(h * 0.26, h * 0.1)
    o.append(S4.runner(p, w * 0.17, h * 0.26, s, cloth="#F3EFE6"))
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(h * 0.64)}" width="{f(w * 0.46)}" height="{f(h * 0.4)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(w * 0.56 + i * w * 0.06)}" y="{f(h * 0.6)}" width="{f(w * 0.03)}" height="{f(h * 0.05)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(8)))
    ws = fit(h * 0.6, h * 0.42)
    for i in range(3):
        o.append(man(p, w * (0.66 + i * 0.1), h * 0.6, ws, ["#5A6A8A", "#6A5A3A", "#4A5A4A"][i], flip=True, up=[(-22, -158), (-30, -190), (-24, -222)] if i != 1 else None))
    o.append(S3.notes(w * 0.82, h * 0.34, 4, seed, color="#3A2A6A"))
    return "".join(o)

def vessels_out(p, w, h, seed):
    """Depart ye, go ye out from thence, touch no unclean thing; cleanse yourselves, ye that bear the vessels of Jehovah; ye shall
    not go out in haste: priests in white walking out of the city gate in good order, carrying the gold vessels."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#C88A5A", "#F3D8A8"), f'<rect x="{f(w * 0.6)}" y="{f(h * 0.14)}" width="{f(w * 0.42)}" height="{f(h * 0.66)}" fill="#A87A5A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.72)} {f(h * 0.8)} L {f(w * 0.72)} {f(h * 0.44)} Q {f(w * 0.8)} {f(h * 0.32)} {f(w * 0.88)} {f(h * 0.44)} L {f(w * 0.88)} {f(h * 0.8)} Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.8, "#C8A878", dy=0)]
    s = fit(b, max(h * 0.4, b - 200))
    for i in range(4):
        x = w * (0.1 + i * 0.13)
        o.append(K1.priest(p, x, b, s * (1 - (3 - i) * 0.03), up=[(-22, -158), (-6, -140), (14, -140)]))
        o.append(f'<path d="M{f(x + 10 * s)} {f(b - 150 * s)} L {f(x + 30 * s)} {f(b - 150 * s)} L {f(x + 26 * s)} {f(b - 128 * s)} L {f(x + 14 * s)} {f(b - 128 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def dry_root(w, h, seed):
    """He grew up before him as a tender plant, and as a root out of a dry ground: he hath no form nor comeliness: a single small
    green shoot coming up out of cracked dry earth in a bare land (no one drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#C8A880", "#F3E0B8"), ground(w, h, h * 0.5, "#B8986A", dy=0)]
    for _ in range(26):
        x = r.uniform(0, w); y = r.uniform(h * 0.54, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 30))} {f(r.uniform(-6, 6))} l {f(r.uniform(6, 20))} {f(r.uniform(-8, 8))}" stroke="#6A4A2A" stroke-width="1.6" fill="none"></path>')
    s = min(1.6, h / 200); cx, b = w * 0.5, h * 0.8
    o.append(f'<path d="M{f(cx)} {f(b)} C {f(cx - 4 * s)} {f(b - 20 * s)} {f(cx + 4 * s)} {f(b - 34 * s)} {f(cx)} {f(b - 50 * s)}" stroke="#4E8A2A" stroke-width="{f(4 * s)}" fill="none"></path>'
             f'<path d="M{f(cx)} {f(b - 40 * s)} C {f(cx - 20 * s)} {f(b - 50 * s)} {f(cx - 24 * s)} {f(b - 40 * s)} {f(cx - 22 * s)} {f(b - 34 * s)} C {f(cx - 14 * s)} {f(b - 34 * s)} {f(cx - 6 * s)} {f(b - 36 * s)} {f(cx)} {f(b - 40 * s)} Z" fill="#7AC04A" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<path d="M{f(cx)} {f(b - 50 * s)} C {f(cx + 18 * s)} {f(b - 62 * s)} {f(cx + 24 * s)} {f(b - 54 * s)} {f(cx + 22 * s)} {f(b - 48 * s)} C {f(cx + 14 * s)} {f(b - 46 * s)} {f(cx + 6 * s)} {f(b - 48 * s)} {f(cx)} {f(b - 50 * s)} Z" fill="#7AC04A" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<path d="M{f(cx)} {f(b)} C {f(cx - 10 * s)} {f(b + 10 * s)} {f(cx - 20 * s)} {f(b + 14 * s)} {f(cx - 30 * s)} {f(b + 24 * s)} M{f(cx)} {f(b)} C {f(cx + 10 * s)} {f(b + 12 * s)} {f(cx + 16 * s)} {f(b + 20 * s)} {f(cx + 24 * s)} {f(b + 30 * s)}" stroke="#8A6A3A" stroke-width="2" fill="none"></path>')
    return "".join(o)

def sorrows_dusk(w, h, seed):
    """He was despised, and rejected of men; a man of sorrows, and acquainted with grief; as one from whom men hide their face: a
    road out of the city at dusk, empty, the gate behind it shut (no one drawn)."""
    o = [bg(w, h, "#2A2040", "#A86A6A"), J.city_hill(w * 0.24, h * 0.64, w * 0.24, h * 0.3, seed), ground(w, h, h * 0.62, "#6A5A5A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h * 0.62)} L {f(w * 0.36)} {f(h * 0.62)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.4"></path>']
    return "".join(o)

def stray_sheep(w, h, seed):
    """All we like sheep have gone astray; we have turned every one to his own way: sheep scattered in every direction over the
    hills, each going its own way, no fold."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FB0D8", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#9AA06A", amp=12), ground(w, h, h * 0.5, "#A8B070", dy=0)]
    s = min(0.6, h / 500)
    for i in range(11):
        a = i * math.pi * 2 / 11
        x = w * 0.5 + math.cos(a) * w * r.uniform(0.18, 0.42); y = h * 0.74 + math.sin(a) * h * r.uniform(0.1, 0.2)
        o.append(E.sheep(x, y, s * (0.6 + (y / h - 0.5)), flip=math.cos(a) < 0))
    return "".join(o)

def silent_lamb(w, h, seed):
    """As a lamb that is led to the slaughter, and as a sheep that before its shearers is dumb, so he opened not his mouth: a
    lamb standing quiet in a pen, shears laid on a stone beside it (no one drawn, nothing done)."""
    o = [bg(w, h, "#C8B8A8", "#F3E8D8"), ground(w, h, h * 0.66, "#B8A07A", dy=0)]
    for i in range(10):
        o.append(f'<path d="M{f(w * (0.08 + i * 0.09))} {f(h * 0.94)} L {f(w * (0.08 + i * 0.09))} {f(h * 0.62)}" stroke="#6A4A2A" stroke-width="4"></path>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.68)} L {f(w * 0.92)} {f(h * 0.68)} M{f(w * 0.06)} {f(h * 0.8)} L {f(w * 0.92)} {f(h * 0.8)}" stroke="#6A4A2A" stroke-width="3"></path>')
    o.append(E3.lamb(w * 0.44, h * 0.92, min(0.9, h / 260)))
    s = min(1.0, h / 300)
    o.append(f'<rect x="{f(w * 0.72)}" y="{f(h * 0.86)}" width="{f(80 * s)}" height="{f(24 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<path d="M{f(w * 0.74)} {f(h * 0.86)} L {f(w * 0.74 + 60 * s)} {f(h * 0.86 - 10 * s)} M{f(w * 0.74)} {f(h * 0.86 - 2)} L {f(w * 0.74 + 60 * s)} {f(h * 0.86 + 4 * s)}" stroke="#C8D0D8" stroke-width="{f(3 * s)}"></path>')
    return "".join(o)

def rich_grave(w, h, seed):
    """They made his grave with the wicked, and with a rich man in his death: a garden with a new tomb hewn in the rock, its stone
    rolled aside and the tomb empty, other tombs along the hillside (no one drawn)."""
    o = [bg(w, h, "#5A6ABA", "#FFE0B0"), V.rays(w * 0.8, h * 0.3, 24, 20, max(w, h), color="#FFF4C2", op=0.3),
         f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.24)} {f(w * 0.6)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.26)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#A89070" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.2, h / 260)
    for x in (0.14, 0.82):
        o.append(f'<path d="M{f(w * x - 20 * s)} {f(h * 0.6)} L {f(w * x - 20 * s)} {f(h * 0.44)} Q {f(w * x)} {f(h * 0.38)} {f(w * x + 20 * s)} {f(h * 0.44)} L {f(w * x + 20 * s)} {f(h * 0.6)} Z" fill="#3A2A22" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<circle cx="{f(w * x + 4 * s)}" cy="{f(h * 0.54)}" r="{f(22 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></circle>')
    cx = w * 0.46
    o.append(f'<path d="M{f(cx - 40 * s)} {f(h * 0.8)} L {f(cx - 40 * s)} {f(h * 0.56)} Q {f(cx)} {f(h * 0.46)} {f(cx + 40 * s)} {f(h * 0.56)} L {f(cx + 40 * s)} {f(h * 0.8)} Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<circle cx="{f(cx + 90 * s)}" cy="{f(h * 0.74)}" r="{f(44 * s)}" fill="#9A8A7A" stroke="#0D0D0F" stroke-width="2.4"></circle>')
    o.append(ground(w, h, h * 0.8, "#7A9A4A", dy=0))
    for i in range(5):
        o.append(f'<circle cx="{f(w * (0.06 + i * 0.2))}" cy="{f(h * 0.88)}" r="{f(16 * s)}" fill="#3E7A3A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

def portion(w, h, seed):
    """Therefore will I divide him a portion with the great, and he shall divide the spoil with the strong: the empty throne
    lifted up in light above the kneeling nations (no one on the throne)."""
    return davids_throne(w, h, seed).replace("THE THRONE OF DAVID", "A PORTION WITH THE GREAT")

def barren_tent(p, w, h, seed):
    """Sing, O barren; enlarge the place of thy tent, and let them stretch forth the curtains of thy habitations; lengthen thy
    cords, and strengthen thy stakes: a woman driving in a tent stake, her tent being widened with new curtains, children about."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C8"), hills(w, h, h * 0.5, seed, color="#9AA06A", amp=8), ground(w, h, h * 0.6, "#C8B080", dy=0)]
    o.append(J1.tent_big(w * 0.56, b - 4, min(w * 0.6, h * 1.2), h * 0.44, color="#7A3A5A", stripe="#E8B830", open_=True))
    o.append(f'<path d="M{f(w * 0.26)} {f(h * 0.6)} L {f(w * 0.06)} {f(b)}" stroke="#5A3A22" stroke-width="2"></path><path d="M{f(w * 0.06)} {f(b - 10)} L {f(w * 0.06)} {f(b + 6)}" stroke="#3A2414" stroke-width="5"></path>')
    s = fit(b, max(h * 0.45, b - 180))
    o.append(woman(p, w * 0.14, b, s, "#2E6B8A", up=[(-22, -158), (-40, -140), (-58, -120)]))
    for i in range(3):
        o.append(S1.boy(p, w * (0.32 + i * 0.07), b, s * 0.55))
    return "".join(o)

def noah_bow(w, h, seed):
    """For this is as the waters of Noah unto me; for as I have sworn that the waters of Noah shall no more go over the earth;
    the mountains may depart, but my covenant of peace shall not be removed: a rainbow over the mountains after rain, the
    waters going down."""
    o = [bg(w, h, "#6A8AB8", "#E8F0E0"), f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.4)} L {f(w * 0.4)} {f(h * 0.6)} L {f(w * 0.6)} {f(h * 0.36)} L {f(w * 0.84)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A5A" stroke="#0D0D0F" stroke-width="2"></path>']
    cx, cy, R = w * 0.5, h * 1.0, min(w * 0.46, h * 0.84)
    for i, col in enumerate(("#D7261E", "#FF8A3D", "#FFD23F", "#5E9F2A", "#2C7DA8", "#5A3A8A")):
        o.append(f'<path d="M{f(cx - R + i * 8)} {f(cy)} A {f(R - i * 8)} {f(R - i * 8)} 0 0 1 {f(cx + R - i * 8)} {f(cy)}" stroke="{col}" stroke-width="8" fill="none" opacity="0.8"></path>')
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="#E8F6FA" stroke-width="1.6"></path>')
    return "".join(o)

STONES = [("SAPPHIRES · THE FOUNDATIONS", "#1F5FAD"), ("RUBIES · THE PINNACLES", "#B5121B"), ("CARBUNCLES · THE GATES", "#D7461E"), ("PRECIOUS STONES · THE BORDER", "#2E8A5A")]
def fair_stones(w, h):
    """Behold, I will set thy stones in fair colors, and lay thy foundations with sapphires; and I will make thy pinnacles of
    rubies, and thy gates of carbuncles, and all thy border of precious stones (a plate)."""
    o = [bp(w, h), title_bar(w, "THY STONES IN FAIR COLORS")]
    s = min(1.0, h / 220); cw = w / 4; b = h * 0.6
    for i, (nm, col) in enumerate(STONES):
        cx = cw * (i + 0.5)
        o.append(f'<path d="M{f(cx)} {f(b - 50 * s)} L {f(cx + 30 * s)} {f(b - 26 * s)} L {f(cx + 20 * s)} {f(b + 14 * s)} L {f(cx - 20 * s)} {f(b + 14 * s)} L {f(cx - 30 * s)} {f(b - 26 * s)} Z" fill="{col}" stroke="#F3EFE6" stroke-width="2"></path>'
                 f'<path d="M{f(cx - 30 * s)} {f(b - 26 * s)} L {f(cx + 30 * s)} {f(b - 26 * s)} M{f(cx)} {f(b - 50 * s)} L {f(cx - 12 * s)} {f(b - 26 * s)} L {f(cx)} {f(b + 14 * s)} L {f(cx + 12 * s)} {f(b - 26 * s)} Z" stroke="#F3EFE6" stroke-width="1" fill="none" opacity="0.7"></path>'
                 + label(cx, b + 40 * s, nm, CYAN, 8))
    return "".join(o)

def smith_coals(p, w, h, seed):
    """Behold, I have created the smith that bloweth the fire of coals, and bringeth forth a weapon for his work; no weapon that
    is formed against thee shall prosper: a smith at his forge working the bellows, a blade glowing on the anvil."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#2A1A16"), f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.7)}" r="{f(h * 0.4)}" fill="#C8582A" opacity="0.3"></circle>', ground(w, h, h * 0.86, "#1A1210", dy=0)]
    s = min(1.0, h / 280)
    o.append(f'<path d="M{f(w * 0.14)} {f(b)} L {f(w * 0.16)} {f(b - 70 * s)} L {f(w * 0.44)} {f(b - 70 * s)} L {f(w * 0.46)} {f(b)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></path>' + E.blaze(w * 0.3, b - 66 * s, 70 * s, 50 * s, seed, n=6))
    o.append(f'<path d="M{f(w * 0.46)} {f(b - 40 * s)} L {f(w * 0.56)} {f(b - 50 * s)} L {f(w * 0.56)} {f(b - 30 * s)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(w * 0.66)}" y="{f(b - 40 * s)}" width="{f(60 * s)}" height="{f(40 * s)}" fill="#3A3A40" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.66 - 10 * s)} {f(b - 44 * s)} L {f(w * 0.66 + 70 * s)} {f(b - 44 * s)}" stroke="#FF6A2A" stroke-width="{f(5 * s)}"></path>')
    o.append(man(p, w * 0.86, b, fit(b, max(h * 0.5, b - 170)), "#4A3A2A", flip=True, up=[(-22, -158), (-36, -186), (-30, -210)]))
    return "".join(o)

def come_waters(p, w, h, seed):
    """Ho, every one that thirsteth, come ye to the waters, and he that hath no money; come ye, buy, and eat; buy wine and milk
    without money and without price: a spring flowing into a stone basin in a market-place, jars of wine and milk set out, no
    seller, people coming with empty hands."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C8"), ground(w, h, h * 0.6, "#D8C098", dy=0)]
    s = min(1.0, h / 300); cx = w * 0.5
    o.append(f'<rect x="{f(cx - 70 * s)}" y="{f(b - 50 * s)}" width="{f(140 * s)}" height="{f(50 * s)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<ellipse cx="{f(cx)}" cy="{f(b - 50 * s)}" rx="{f(70 * s)}" ry="{f(10 * s)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<rect x="{f(cx - 10 * s)}" y="{f(b - 130 * s)}" width="{f(20 * s)}" height="{f(80 * s)}" fill="#A89878" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(cx)} {f(b - 110 * s)} C {f(cx + 30 * s)} {f(b - 110 * s)} {f(cx + 34 * s)} {f(b - 80 * s)} {f(cx + 30 * s)} {f(b - 54 * s)}" stroke="#2C9DB8" stroke-width="{f(5 * s)}" fill="none"></path>')
    for i, col in enumerate(("#B5652E", "#F3EFE6", "#B5652E")):
        x = cx + (110 + i * 34) * s
        o.append(f'<path d="M{f(x - 12 * s)} {f(b)} C {f(x - 18 * s)} {f(b - 20 * s)} {f(x - 10 * s)} {f(b - 40 * s)} {f(x - 6 * s)} {f(b - 44 * s)} L {f(x + 6 * s)} {f(b - 44 * s)} C {f(x + 10 * s)} {f(b - 40 * s)} {f(x + 18 * s)} {f(b - 20 * s)} {f(x + 12 * s)} {f(b)} Z" fill="{col}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    fs = fit(b, max(h * 0.45, b - 180))
    o.append(man(p, w * 0.12, b, fs, "#6A5A3A", up=[(-22, -158), (-4, -140), (16, -144)]) + woman(p, w * 0.24, b, fs * 0.94, "#C2456A"))
    return "".join(o)

def rain_snow(w, h, seed):
    """As the rain cometh down and the snow from heaven, and returneth not thither, but watereth the earth, and maketh it bring
    forth and bud, and giveth seed to the sower and bread to the eater: snow on the far mountains, rain on the near fields, the
    grain springing up."""
    r = random.Random(seed)
    o = [bg(w, h, "#7A9AC8", "#E8F0E8"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.2)} {f(h * 0.2)} L {f(w * 0.4)} {f(h * 0.44)} L {f(w * 0.62)} {f(h * 0.16)} L {f(w * 0.86)} {f(h * 0.44)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A8A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.14)} {f(h * 0.28)} L {f(w * 0.2)} {f(h * 0.2)} L {f(w * 0.26)} {f(h * 0.28)} Z M{f(w * 0.56)} {f(h * 0.24)} L {f(w * 0.62)} {f(h * 0.16)} L {f(w * 0.68)} {f(h * 0.24)} Z" fill="#F3F6FA"></path>']
    for _ in range(40):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h * 0.3))}" r="2" fill="#FFFFFF"></circle>')
    for _ in range(40):
        x = r.uniform(0, w); y = r.uniform(h * 0.3, h * 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#4A6A9A" stroke-width="1.4" opacity="0.6"></path>')
    o.append(ground(w, h, h * 0.62, "#8A6A3A", dy=0) + R1.field(-10, w + 10, h * 0.8, h * 0.18, seed, rows=3, color="#9CCB5E"))
    return "".join(o)

def trees_clap(w, h, seed):
    """The mountains and the hills shall break forth before you into singing, and all the trees of the field shall clap their
    hands; instead of the thorn shall come up the fir-tree, and instead of the brier the myrtle-tree: a road through rejoicing
    hills, the trees swaying, firs and myrtles springing up where thorns had been."""
    o = [heavens_sing(w, h, seed)]
    o.append(f'<path d="M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.48)} {f(h * 0.7)} L {f(w * 0.52)} {f(h * 0.7)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(thorns(w * 0.02, w * 0.3, h * 0.99, seed, n=6, s=0.6).replace("#4A3A22", "#8A7A5A"))
    for x in (0.28, 0.7):
        o.append(f'<circle cx="{f(w * x)}" cy="{f(h * 0.86)}" r="{f(min(w, h) * 0.05)}" fill="#3E7A3A" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M{f(w * x)} {f(h * 0.9)} L {f(w * x)} {f(h * 0.99)}" stroke="#5A3A22" stroke-width="4"></path>')
    return "".join(o)
