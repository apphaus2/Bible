"""Isaiah 24–27 drawings (on top of isa.art6): the earth made empty and reeling like a hammock, the city of confusion shut
up, the sun ashamed over Zion, the stronghold in the storm, the feast of fat things on the mountain and the veil lifted, the
strong city, the dew of herbs at dawn, the chambers shut, leviathan the swift serpent, the altar's stones as chalkstones,
and the great trumpet."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art6 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
import snake as SN

def earth_empty(p, w, h, seed):
    """Jehovah maketh the earth empty, and maketh it waste, and turneth it upside down: a tilted, cracked plain under a dim
    sky, its towns emptied, a few figures scattered far apart."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#4A4A5A", "#B8987A"),
         f'<path d="M-10 {f(h * 0.5)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></path>']
    for _ in range(9):
        x = r.uniform(0, w); y = r.uniform(h * 0.62, h * 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(14, 40))} {f(r.uniform(-6, 6))} l {f(r.uniform(10, 30))} {f(r.uniform(-8, 8))} l {f(r.uniform(10, 30))} {f(r.uniform(-6, 6))}" stroke="#3A2A1A" stroke-width="2" fill="none"></path>')
    for i in range(4):
        x = w * (0.1 + i * 0.25); y = h * (0.52 + i * 0.03)
        o.append(f'<path d="M{f(x - 20)} {f(y)} L {f(x - 20)} {f(y - 14)} L {f(x - 6)} {f(y - 8)} L {f(x + 2)} {f(y - 18)} L {f(x + 18)} {f(y - 10)} L {f(x + 18)} {f(y)} Z" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    s = fit(b, max(h * 0.6, b - 120))
    for x in (0.18, 0.52, 0.86):
        o.append(man(p, w * x, b - r.uniform(0, 20), s * r.uniform(0.7, 1.0), r.choice(["#4A4A5A", "#5A3A3A", "#3A4A3A"]), flip=r.random() < 0.5))
    return "".join(o)

def gate_smitten(w, h, seed):
    """The waste city is broken down; every house is shut up; in the city is left desolation, and the gate is smitten with
    destruction: a broken city gate, the street behind it of shut doors, a harp and a wine-cup lying in the dust."""
    o = [bg(w, h, "#5A5A6A", "#C8B098"), ground(w, h, h * 0.8, "#8A7A6A", dy=0)]
    for i in range(6):
        x = w * (0.02 + i * 0.16)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.36)}" width="{f(w * 0.15)}" height="{f(h * 0.44)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + w * 0.05)}" y="{f(h * 0.6)}" width="{f(w * 0.05)}" height="{f(h * 0.2)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<path d="M{f(x + w * 0.05)} {f(h * 0.66)} L {f(x + w * 0.1)} {f(h * 0.74)} M{f(x + w * 0.1)} {f(h * 0.66)} L {f(x + w * 0.05)} {f(h * 0.74)}" stroke="#2A1A10" stroke-width="2"></path>')
    s = min(1.0, h / 280)
    o.append(S2.harp(w * 0.3, h * 0.92, 0.5 * s, rot=-70) + f'<path d="M{f(w * 0.56)} {f(h * 0.9)} L {f(w * 0.6)} {f(h * 0.86)} L {f(w * 0.62)} {f(h * 0.9)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def earth_reels(w, h, seed):
    """The earth shall stagger like a drunken man, and shall sway to and fro like a hammock; the windows on high are opened,
    and the foundations of the earth tremble: a hut on poles swaying, the ground split, rain pouring from a rent sky."""
    r = random.Random(seed)
    o = [bg(w, h, "#1A1A2A", "#5A5A7A")]
    for _ in range(70):
        x = r.uniform(0, w); y = r.uniform(0, h * 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} l -6 18" stroke="#8FB0D8" stroke-width="1.4" opacity="0.6"></path>')
    o.append(f'<g transform="rotate(-6 {f(w / 2)} {f(h * 0.8)})">{ground(w, h, h * 0.7, "#4A3A2A", dy=0)}</g>')
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.78)} L {f(w * 0.36)} {f(h * 0.86)} L {f(w * 0.33)} {f(h * 0.92)} L {f(w * 0.4)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="4" fill="none"></path>')
    s = min(1.2, h / 260); x, b = w * 0.66, h * 0.76
    o.append(f'<g transform="rotate(10 {f(x)} {f(b)})"><path d="M{f(x - 40 * s)} {f(b)} L {f(x - 40 * s)} {f(b - 80 * s)} M{f(x + 40 * s)} {f(b)} L {f(x + 40 * s)} {f(b - 80 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>'
             f'<path d="M{f(x - 50 * s)} {f(b - 80 * s)} L {f(x)} {f(b - 116 * s)} L {f(x + 50 * s)} {f(b - 80 * s)} Z" fill="#8A7A3A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(x - 40 * s)} {f(b - 50 * s)} Q {f(x)} {f(b - 30 * s)} {f(x + 40 * s)} {f(b - 50 * s)}" stroke="#C8B080" stroke-width="{f(4 * s)}" fill="none"></path></g>')
    o.append(E2.bolt(w * 0.2, 0, h * 0.4, seed))
    return "".join(o)

def sun_moon_zion(w, h, seed):
    """The moon shall be confounded, and the sun ashamed; for Jehovah of hosts will reign in mount Zion: a pale sun and a
    pale moon dimmed in the sky, and below them Zion shining with a glory brighter than both."""
    o = [bg(w, h, "#2A2A4A", "#8A7AA0"), f'<circle cx="{f(w * 0.18)}" cy="{f(h * 0.2)}" r="{f(min(w, h) * 0.07)}" fill="#C8B888" opacity="0.6"></circle>',
         f'<circle cx="{f(w * 0.84)}" cy="{f(h * 0.18)}" r="{f(min(w, h) * 0.05)}" fill="#C8C8D8" opacity="0.5"></circle>',
         V.rays(w * 0.5, h * 0.6, 40, 20, max(w, h), color="#FFE680", op=0.3), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.56)}" r="{f(min(w, h) * 0.2)}" fill="#FFF4C2" opacity="0.5"></circle>',
         J.city_hill(w * 0.5, h * 0.92, w * 0.36, h * 0.3, seed), K1.temple_front(w * 0.5, h * 0.66, min(w * 0.14, h * 0.32), seed)]
    return "".join(o)

def stronghold(p, w, h, seed):
    """A stronghold to the poor, a refuge from the storm, a shade from the heat, when the blast of the terrible ones is as a
    storm against the wall: a strong tower, rain driving against its wall, the poor sheltering on its lee side."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#2A2A3A", "#6A6A7A"), ground(w, h, h * 0.84, "#5A5A4A", dy=0)]
    for _ in range(60):
        x = r.uniform(0, w * 0.4); y = r.uniform(0, h * 0.84)
        o.append(f'<path d="M{f(x)} {f(y)} l 16 10" stroke="#8FB0D8" stroke-width="1.6" opacity="0.6"></path>')
    o.append(tower(w * 0.5, b, min(w * 0.22, h * 0.5), h * 0.72, color="#8A8070"))
    s = fit(b, max(h * 0.6, b - 120))
    for i in range(3):
        o.append(E.kneel(w * (0.68 + i * 0.08), b, s * 0.8, color=["#5A4A3A", "#4A4A5A", "#6A3A3A"][i], skin="#8A5A3A", flip=True))
    return "".join(o)

def feast_mountain(p, w, h, seed, veil=True):
    """In this mountain will Jehovah of hosts make unto all peoples a feast of fat things, a feast of wines on the lees; he
    will destroy the veil that is spread over all nations: a long table on the mountain-top in the morning, the peoples
    seated in many colours, and above them a dark veil drawn back and torn, light pouring through."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C0"), V.rays(w * 0.5, -h * 0.1, 40, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.35),
         f'<path d="M-10 {f(h + 10)} L {f(w * 0.2)} {f(h * 0.6)} L {f(w * 0.8)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A9A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    if veil:
        o.append(f'<path d="M-10 -10 L {f(w * 0.36)} -10 C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.06)} {f(h * 0.4)} L -10 {f(h * 0.44)} Z" fill="#2A2040" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(w + 10)} -10 L {f(w * 0.64)} -10 C {f(w * 0.7)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.3)} {f(w * 0.94)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.44)} Z" fill="#2A2040" stroke="#0D0D0F" stroke-width="2"></path>')
    tw = w * 0.56; ty = h * 0.7
    o.append(f'<rect x="{f(w * 0.5 - tw / 2)}" y="{f(ty)}" width="{f(tw)}" height="{f(h * 0.04)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.62, b - 110))
    for i in range(10):
        x = w * 0.5 - tw / 2 + (i + 0.5) * tw / 10
        o.append((man if i % 2 else woman)(p, x, b - (i % 2) * 6, s, r.choice(["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#7A6A2A", "#C2456A", "#E8B830"])))
    o.append(f'<rect x="{f(w * 0.5 - tw / 2)}" y="{f(ty)}" width="{f(tw)}" height="{f(h * 0.04)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(7):
        x = w * 0.5 - tw / 2 + (i + 0.5) * tw / 7
        o.append(f'<path d="M{f(x - 6)} {f(ty - 12)} L {f(x + 6)} {f(ty - 12)} L {f(x + 2)} {f(ty)} L {f(x - 2)} {f(ty)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path>'
                 if i % 2 else f'<ellipse cx="{f(x)}" cy="{f(ty - 4)}" rx="10" ry="5" fill="#C8862E" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    return "".join(o)

def strong_city(p, w, h, seed):
    """We have a strong city; salvation will he appoint for walls and bulwarks. Open ye the gates, that the righteous nation
    which keepeth faith may enter in: a walled city with its great gates open in the morning, people walking in."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C0"), V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         f'<rect x="-10" y="{f(h * 0.26)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(16):
        o.append(f'<rect x="{f(i * w / 15 - 10)}" y="{f(h * 0.22)}" width="{f(w / 30)}" height="{f(h * 0.05)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for x in (0.3, 0.7):
        o.append(f'<rect x="{f(w * x - w * 0.06)}" y="{f(h * 0.12)}" width="{f(w * 0.12)}" height="{f(h * 0.64)}" fill="#C8B890" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    o.append(f'<path d="M{f(w * 0.4)} {f(h * 0.76)} L {f(w * 0.4)} {f(h * 0.44)} Q {f(w * 0.5)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.44)} L {f(w * 0.6)} {f(h * 0.76)} Z" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.4)} {f(h * 0.44)} L {f(w * 0.34)} {f(h * 0.48)} L {f(w * 0.34)} {f(h * 0.8)} L {f(w * 0.4)} {f(h * 0.76)} Z M{f(w * 0.6)} {f(h * 0.44)} L {f(w * 0.66)} {f(h * 0.48)} L {f(w * 0.66)} {f(h * 0.8)} L {f(w * 0.6)} {f(h * 0.76)} Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.76, "#C8B080", dy=0))
    s = fit(b, max(h * 0.6, b - 120))
    for i in range(5):
        o.append((man if i % 2 == 0 else woman)(p, w * (0.44 + i * 0.03), b - i * h * 0.03, s * (1 - i * 0.12), ["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#C2456A"][i]))
    return "".join(o)

def night_seek(p, w, h, seed):
    """With my soul have I desired thee in the night: a figure kneeling by an open window at night, a lamp beside him, the
    stars outside."""
    from genesis.art4 import clay_lamp
    o = [rect(w, h, "#1A1428"), f'<rect x="{f(w * 0.56)}" y="{f(h * 0.12)}" width="{f(w * 0.3)}" height="{f(h * 0.5)}" fill="#0B0B2A" stroke="#0D0D0F" stroke-width="3"></rect>',
         f'<g transform="translate({f(w * 0.56)} {f(h * 0.12)})">{mk.stars(16, w * 0.3, h * 0.5, seed)}</g>', ground(w, h, h * 0.86, "#2A1E26", dy=0)]
    s = fit(h * 0.92, max(h * 0.5, h * 0.92 - 160))
    o.append(E.kneel(w * 0.44, h * 0.92, s, color="#4A3A6A", skin="#B98A6E"))
    o.append(clay_lamp(w * 0.22, h * 0.88, min(1.0, h / 300)) + f'<circle cx="{f(w * 0.22)}" cy="{f(h * 0.8)}" r="{f(h * 0.2)}" fill="#FFC14D" opacity="0.15"></circle>')
    return "".join(o)

def dew_dawn(w, h, seed):
    """Awake and sing, ye that dwell in the dust; for thy dew is as the dew of herbs: herbs heavy with dew on a hillside at
    dawn, the sun rising, tombs cut in the hill standing open and empty."""
    r = random.Random(seed)
    o = [bg(w, h, "#5A6ABA", "#FFD8A0"), V.rays(w * 0.7, h * 0.56, 30, 20, max(w, h), color="#FFF4C2", op=0.35), f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.56)}" r="{f(h * 0.08)}" fill="#FFF4C2"></circle>',
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.5)} {f(h * 0.52)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A9A5A" stroke="#0D0D0F" stroke-width="2"></path>']
    for x in (0.12, 0.3):
        o.append(f'<path d="M{f(w * x - 22)} {f(h * 0.62)} L {f(w * x - 22)} {f(h * 0.54)} Q {f(w * x)} {f(h * 0.46)} {f(w * x + 22)} {f(h * 0.54)} L {f(w * x + 22)} {f(h * 0.62)} Z" fill="#2A1E1A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<circle cx="{f(w * x + 40)}" cy="{f(h * 0.6)}" r="{f(h * 0.05)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    for _ in range(26):
        x = r.uniform(0, w); y = r.uniform(h * 0.7, h * 0.98)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 6)} {f(y - 14)} {f(x - 2)} {f(y - 22)} {f(x)} {f(y - 26)} C {f(x + 2)} {f(y - 22)} {f(x + 6)} {f(y - 14)} {f(x)} {f(y)} Z" fill="#3E8A3A" stroke="#0D0D0F" stroke-width="1"></path>'
                 f'<circle cx="{f(x + 2)}" cy="{f(y - 18)}" r="2.4" fill="#E8F6FA" stroke="#8FB0D8" stroke-width="0.8"></circle>')
    return "".join(o)

def chambers(w, h, seed):
    """Come, my people, enter thou into thy chambers, and shut thy doors about thee: houses with their doors shut at night,
    lamplight in the windows, a storm passing over."""
    o = [bg(w, h, "#14142A", "#3A3A5A"), ground(w, h, h * 0.86, "#2A2430", dy=0)]
    for i in range(5):
        x = w * (0.02 + i * 0.2)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.4)}" width="{f(w * 0.18)}" height="{f(h * 0.46)}" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + w * 0.06)}" y="{f(h * 0.62)}" width="{f(w * 0.06)}" height="{f(h * 0.24)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x + w * 0.02)}" y="{f(h * 0.48)}" width="{f(w * 0.03)}" height="{f(h * 0.06)}" fill="#FFC14D"></rect>')
    o.append(E2.bolt(w * 0.5, 0, h * 0.36, seed))
    return "".join(o)

def leviathan(w, h, seed):
    """Leviathan the swift serpent, and leviathan the crooked serpent, the monster that is in the sea: a great serpent coiling
    through dark storm waves, lightning over the sea (no one drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#0B1428", "#2A3A5A")]
    o.append(E2.bolt(w * 0.3, 0, h * 0.4, seed) + E2.bolt(w * 0.8, 0, h * 0.3, seed + 1))
    pts = [(w * 0.98, h * 0.8), (w * 0.84, h * 0.56), (w * 0.7, h * 0.78), (w * 0.56, h * 0.5), (w * 0.42, h * 0.72), (w * 0.28, h * 0.44), (w * 0.16, h * 0.36)]
    o.append(SN.snake(pts, min(w, h) * 0.07, f"lv{seed}", head_scale=1.6))
    for k in range(3):
        y = h * (0.66 + k * 0.12)
        d = f"M-10 {f(y)} " + " ".join(f"Q {f(x + 30)} {f(y - 18 + r.uniform(-6, 6))} {f(x + 60)} {f(y)}" for x in range(-10, int(w) + 60, 60))
        o.append(f'<path d="{d} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#1F4A6A", "#163A5A", "#102A48"][k]}" stroke="#E8F6FA" stroke-width="1.6" opacity="0.92"></path>')
    return "".join(o)

def chalkstones(p, w, h, seed):
    """He maketh all the stones of the altar as chalkstones that are beaten in sunder, so that the Asherim and the sun-images
    shall rise no more; the fortified city solitary, there shall the calf feed: white broken stones, a felled pole, a calf
    grazing by an empty wall."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#9AB0C8", "#F0E0C0"), f'<rect x="{f(w * 0.56)}" y="{f(h * 0.3)}" width="{f(w * 0.46)}" height="{f(h * 0.44)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.62)} {f(h * 0.26)} L {f(w * 0.7)} {f(h * 0.32)} L {f(w * 0.8)} {f(h * 0.24)} L {f(w + 10)} {f(h * 0.3)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.72, "#A8A06A", dy=0)]
    for _ in range(14):
        x = r.uniform(w * 0.06, w * 0.4); y = r.uniform(h * 0.8, h * 0.95)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 20))} {f(r.uniform(-8, -2))} l {f(r.uniform(6, 14))} {f(r.uniform(4, 10))} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(w * 0.1)} {f(b - 4)} L {f(w * 0.46)} {f(b - 14)}" stroke="#6A4A2A" stroke-width="{f(min(10, h * 0.03))}"></path>')
    o.append(S1.calf(w * 0.72, b, min(0.9, h / 300)))
    return "".join(o)

def great_trumpet(p, w, h, seed):
    """A great trumpet shall be blown; and they shall come that were ready to perish in the land of Assyria, and the outcasts
    in the land of Egypt, and worship in the holy mountain at Jerusalem: a trumpeter on Zion's height blowing the ram's horn,
    blasts of sound, people streaming up from both sides."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFE8B0"), f'<path d="M-10 {f(h + 10)} L {f(w * 0.5)} {f(h * 0.36)} L {f(w + 10)} {f(h + 10)} Z" fill="#9A8A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(h * 0.38, h * 0.14)
    o.append(J.trumpeter(p, w * 0.5, h * 0.38, s) + J.blasts(w * 0.5 + 60 * s, h * 0.38 - 150 * s, s * 1.4))
    for side in (-1, 1):
        for i in range(6):
            t = (i + 1) / 7; x = w * 0.5 + side * w * (0.46 - t * 0.36); y = b - t * (b - h * 0.46)
            o.append((man if i % 2 else woman)(p, x, y, fit(b, b - 110) * (1 - t * 0.6), r.choice(["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#7A6A2A", "#C2456A"]), flip=side > 0))
    o.append(label(w * 0.06, h * 0.96, "FROM ASSYRIA", "#3A2A1A", 9, "start") + label(w * 0.94, h * 0.96, "FROM EGYPT", "#3A2A1A", 9, "end"))
    return "".join(o)
