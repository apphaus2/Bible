"""Drawings for Acts 8–9. Devout men burying Stephen; the scattering on the map; Saul laying waste the church (a night street,
a door broken open, Saul and the officers — no one dragged or struck is drawn); Philip in the city of Samaria; Simon the
sorcerer drawn only as a man among the crowd (no sorcery is drawn: his arts are words); the baptisms in the stream; the
hands laid on; the money offered. The desert road to Gaza, the angel of the Lord (white light, no face) beside Philip; the
Ethiopian's chariot (dark skin, an off-white turban with a gold band, a green robe edged with gold, the scroll of Isaiah
open on his knees); the water by the way; the chariot going on alone. The Damascus road: the light out of heaven poured
down on the road, Saul fallen to the earth (lying), the men with him standing speechless — Jesus is not drawn: his words
come from the light. Saul led by the hand into Damascus; three days blind; Ananias' vision in his house (the light at the
window — the Lord is not drawn); the house of Judas in the street called Straight, Ananias' hands on Saul and the scales
falling; the basket let down by night over the wall; Barnabas bringing Saul to the apostles; Æneas rising from his bed at
Lydda; Dorcas in the upper chamber at Joppa, the widows holding up the coats she made, and raised alive; the tanner's
house by the sea. Built on act.art4."""
from act.art4 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
import exodus3 as E3

ETH_ROBE, ETH_HEAD, ETH_SKIN = "#2A5A3A", "#F3EFE6", "#5A3A2A"

def ethiopian(p, x, y, s, flip=False, up=None):
    """The Ethiopian eunuch at a distance: dark skin, an off-white turban with a gold band, a green robe."""
    return mk.person(p, round(x), round(y), round(s, 3), body=ETH_SKIN, cloth=ETH_ROBE, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(ETH_HEAD, cord="#E8B830") + '<path d="M-24 -40 L 24 -40" stroke="#E8B830" stroke-width="4"></path>')
def ananias_dam(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#3A4A5A", head="#3A4A5A", cord="#1A1210", bd="#9A948A", flip=flip, up=up)
WHO.update({"ethiopian": ethiopian, "ananias_dam": ananias_dam})

def mourners_tomb(p, w, h, seed):
    """Devout men buried Stephen, and made great lamentation over him: the rock tomb with its stone rolled to at evening,
    the men standing before it with their heads bowed and their hands to their faces."""
    o = [new_tomb(p, w, h, seed)]
    b = h * 0.94
    s = fit(b, max(h * 0.3, b - 210))
    for i, x in enumerate((0.08, 0.17, 0.26, 0.35)):
        o.append(man_fig(p, w * x, b, s * (1 - 0.02 * i), ["#3A3A4A", "#4A3A3A", "#2A3A4A", "#4A4A3A"][i], head=["#E8E2D6", "#3A3A4A", None, "#6A5A3A"][i],
                         hr="#2A1A10", bd="#2A1A10", flip=True, up=[(22, -158), (14, -176), (8, -190)] if i % 2 else None))
    return "".join(o)

def scattered(w, h):
    """They were all scattered abroad throughout the regions of Judæa and Samaria: the map of the land, the roads out of
    Jerusalem lit red."""
    return geo.med_map(w, h, box=(33.6, 36.6, 30.8, 33.6), places=("JERUSALEM", "SAMARIA", "JOPPA", "LYDDA", "GAZA", "AZOTUS", "CÆSAREA", "DAMASCUS"),
                       routes=[("JERUSALEM", q) for q in ("SAMARIA", "JOPPA", "GAZA", "AZOTUS", (35.3, 31.2), (35.6, 31.9))], hi=("JERUSALEM",),
                       regions=(("JUDÆA", 35.1, 31.45), ("SAMARIA", 35.4, 32.5), ("GALILEE", 35.4, 32.95), ("THE GREAT SEA", 34.1, 32.6)),
                       lit_routes=list(range(6)), size=10, rsize=10, title="ACTS 8:1 · SCATTERED ABROAD")

def laid_waste(p, w, h, seed):
    """Saul laid waste the church, entering into every house: a street at night, a door broken in and hanging, a lamp
    overturned on the threshold; Saul with the officers of the high priest going on to the next door — the dragging and
    the prison told in words only."""
    bg, b = _street(w, h, seed, "night")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    k = s
    dx = w * 0.18
    o.append(f'<rect x="{f(dx)}" y="{f(b - 140 * k)}" width="{f(60 * k)}" height="{f(110 * k)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(dx)} {f(b - 140 * k)} L {f(dx - 34 * k)} {f(b - 120 * k)} L {f(dx - 34 * k)} {f(b - 20 * k)} L {f(dx)} {f(b - 30 * k)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2" transform="rotate(-8 {f(dx)} {f(b - 30 * k)})"></path>'
             + A.lamp(dx + 30 * k, b - 6 * k, k * 0.8).replace("<g transform", '<g opacity="0.9" transform', 1))
    o.append(paul(p, w * 0.46, b, s, up=UP_BLESS) + officer(p, w * 0.58, b, s) + officer(p, w * 0.7, b, s * 0.98))
    return "".join(o)

def philip_city(p, w, h, seed, healed=True):
    """Philip in the city of Samaria: the gate and its square, Philip preaching with his hand lifted, the multitudes
    listening, and among them a lame man leaping with his staff held high."""
    bg, b = _gate(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    o.append(philip_ev(p, w * 0.16, b, s, flip=True, up=UP_HIGH))
    o.append(crowd(p, w * 0.34, w * 0.94, b, b - 180 * s, 7, seed, flip=True))
    if healed:
        staff = '<path d="M-26 -230 L -40 -150" stroke="#5A3A22" stroke-width="5"></path>'
        o.append(glow(w * 0.32, b - 130 * s, 110 * s, "#FFF4C2", 0.6, f"{p}h") + man_fig(p, w * 0.32, b - 24 * s, s, "#7A7A60", head="#6A5A3A", bd="#3A2A1A", up=UP_HIGH, extra=staff))
    return "".join(o)

def simon_crowd(p, w, h, seed):
    """Simon, who used sorcery and amazed the people: the square of Samaria, a man in a violet headcloth with a band
    standing on a step, the people about him gazing — no sorcery drawn."""
    bg, b = _gate(w, h, seed, "dusk")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    st = b - 30 * s
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(st)}" width="{f(w * 0.2)}" height="{f(b - st + 4)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    o.append(man_fig(p, w * 0.5, st, s, "#3A1A4A", head="#4A1A5A", cord="#E8B830", bd="#1A1210", up=UP_HIGH))
    o.append(crowd(p, w * 0.04, w * 0.34, b, b - 170 * s, 4, seed + 1, flip=True) + crowd(p, w * 0.66, w * 0.96, b, b - 170 * s, 4, seed + 2))
    return "".join(o)

def stream(p, w, h, seed, who="philip", believers=3, chariot_=False):
    """A baptism in running water: a stream between grassy banks, the baptizer standing in the water with one being
    baptized; who="philip" (the people of Samaria waiting on the bank) or "eunuch" (Philip and the Ethiopian, the chariot
    standing still on the road above)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#8A9A6A", amp=14, step=90), ground(w, h, h * 0.54, "#9AAA5A", dy=0)]
    if chariot_:
        o.append(eth_chariot(p, w * 0.78, h * 0.6, max(0.3, h / 900), reading=False, empty=True))
    o.append(f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>')
    o.append(lake(w, h, h * 0.8, seed, color="#2C7DA8", deep="#1F5F8A", n=8))
    s = fit(b, max(h * 0.3, b - 210))
    if who == "philip":
        o.append(philip_ev(p, w * 0.42, b, s, flip=True, up=UP_HIGH) + man_fig(p, w * 0.54, b + 6, s * 0.94, "#F3EFE6", hr="#2A1A10", bd="#2A1A10"))
        for i in range(believers):
            o.append(man_fig(p, w * (0.08 + 0.1 * i), h * 0.72, s * 0.8, ["#6A4A3A", "#3A4A6A", "#5A6A3A"][i % 3], head=["#E8E2D6", None, "#6A5A3A"][i % 3], hr="#2A1A10", bd="#2A1A10", flip=True)
                     if i % 2 == 0 else woman_fig(p, w * (0.08 + 0.1 * i), h * 0.72, s * 0.78, "#6A4A5A", "#3A3A5A", flip=True))
    else:
        o.append(philip_ev(p, w * 0.36, b, s, flip=True, up=UP_HIGH) + ethiopian(p, w * 0.48, b + 6, s * 0.96))
    o.append(f'<rect x="-10" y="{f(b - 30 * s)}" width="{f(w + 20)}" height="{f(h)}" fill="#2C7DA8" opacity="0.7"></rect>')
    return "".join(o)

def hands_on(p, w, h, seed, money=False):
    """Peter and John laying their hands on the believers of Samaria as they kneel; money=True Simon standing by, holding
    out a purse of money to them."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    for i, (x, c) in enumerate(((0.42, "#6A4A3A"), (0.56, "#5A6A3A"))):
        o.append(E.kneel(w * x, b, s * 0.82, color=c, skin=SKIN, flip=True))
    o.append(peter(p, w * 0.3, b, s, flip=True, up=[(22, -158), (44, -150), (60, -134)]) + john_ap(p, w * 0.68, b, s, up=[(-22, -158), (-44, -150), (-60, -134)]))
    if money:
        purse = '<path d="M-74 -150 C -80 -134 -66 -128 -60 -134 C -54 -140 -60 -156 -70 -156 Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="1.6"></path>'
        o.append(man_fig(p, w * 0.86, b, s, "#3A1A4A", head="#4A1A5A", cord="#E8B830", bd="#1A1210", up=UP_BLESS, extra=purse))
    return "".join(o)

def eth_chariot(p, x, y, s, reading=True, empty=False, flip=False, philip_=False):
    """The Ethiopian's chariot on the road, (x, y) the ground under its wheel: a horse, a covered two-wheeled carriage in
    green and gold, the eunuch sitting in it with the scroll of Isaiah open (empty=True: he has gone down from it)."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">', E3.horse(120, 0, 1.0, "#E8E2D6"),
         '<path d="M80 -46 L 20 -56" stroke="#8A5A30" stroke-width="5"></path>']
    if not empty:
        o.append(f'<g transform="scale(1.0)">' + mk.person(p, -40, -40, 0.62, body=ETH_SKIN, cloth=ETH_ROBE, kind="Robe", sw=4,
                                                         extra=A.headcloth(ETH_HEAD, cord="#E8B830")) + '</g>')
        if reading:
            o.append('<rect x="-30" y="-130" width="44" height="26" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="2"></rect>'
                     '<rect x="-34" y="-134" width="8" height="34" rx="4" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                     '<rect x="12" y="-134" width="8" height="34" rx="4" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append('<path d="M-90 -40 L -90 -100 L 30 -100 L 40 -40 Z" fill="#2A5A3A" stroke="#0D0D0F" stroke-width="2.6" opacity="0.0"></path>'
             '<path d="M-96 -30 L -96 -92 L 28 -92 C 40 -70 40 -50 34 -30 Z" fill="#2A5A3A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             '<path d="M-92 -80 L 30 -80 M-92 -50 L 36 -50" stroke="#E8B830" stroke-width="3"></path>'
             '<path d="M-104 -150 C -60 -176 10 -176 44 -150 L 36 -140 C 10 -160 -60 -160 -96 -140 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-96 -142 L -96 -92 M36 -142 L 30 -92" stroke="#6A4A2A" stroke-width="3"></path>'
             '<circle cx="-30" cy="-20" r="30" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="3"></circle><circle cx="-30" cy="-20" r="20" fill="none" stroke="#E8B830" stroke-width="2"></circle>'
             '<path d="M-30 -50 L -30 10 M-60 -20 L 0 -20 M-51 -41 L -9 1 M-51 1 L -9 -41" stroke="#3A2414" stroke-width="2"></path>')
    o.append("</g>")
    return "".join(o)

def desert_road(p, w, h, seed, angel_=True, chariot_=False, philip_x=0.2, running=False, reading=True):
    """The way that goeth down from Jerusalem unto Gaza, the same is desert: the road across the sand hills at noon;
    angel_=True an angel of the Lord, white light and a gold rim, no face, beside Philip; chariot_=True the Ethiopian's
    chariot on the road; running=True Philip running up to it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5AB0D8", "#FFF4C2"), sun(w * 0.86, h * 0.18, 18, color="#FFE680", op=0.4),
         hills(w, h, h * 0.46, seed, color="#D8A868", amp=16, step=110), ground(w, h, h * 0.56, "#E8C88A", dy=0),
         f'<path d="M-10 {f(h * 0.96)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.62)}" stroke="#F3E2B8" stroke-width="{f(max(14, h * 0.1))}" fill="none"></path>']
    s = fit(b, max(h * 0.3, b - 210))
    if chariot_:
        o.append(eth_chariot(p, w * 0.62, b, s * 0.9, reading=reading))
    if angel_:
        o.append(angel(p, w * (philip_x + 0.12), b, s * 1.02, up=UP_CALL))
    o.append(philip_ev(p, w * philip_x, b, s, flip=True, up=UP_BLESS if running else None))
    return "".join(o)

def lamb_scroll(p, w, h, seed):
    """He was led as a sheep to the slaughter: the open scroll of Isaiah, and beside it a lamb standing still and dumb
    before the shearer's shears laid on the ground."""
    o = [bgr(w, h, "#E8D8B8"), f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8A878" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.5, h / 300)
    o.append(scroll(w * 0.3, h * 0.5, 260 * k, 120 * k, lines=6))
    o.append(E.sheep(w * 0.74, h * 0.78, k * 0.9))
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.86)} L {f(w * 0.68)} {f(h * 0.82)} M{f(w * 0.6)} {f(h * 0.82)} L {f(w * 0.68)} {f(h * 0.86)}" stroke="#6A6A74" stroke-width="{f(3 * k)}"></path>')
    return "".join(o)

def alone_road(w, h):
    """The eunuch saw him no more, for he went on his way rejoicing; and Philip was found at Azotus: the map, from the
    water on the desert road to Azotus and up the coast to Cæsarea."""
    return geo.med_map(w, h, box=(33.8, 36.0, 30.9, 32.8), places=("JERUSALEM", "GAZA", "AZOTUS", "JOPPA", "LYDDA", "CÆSAREA"),
                       routes=[("JERUSALEM", (34.9, 31.6), "GAZA"), ((34.7, 31.6), "AZOTUS", "JOPPA", "CÆSAREA")], hi=("AZOTUS", "CÆSAREA"),
                       regions=(("JUDÆA", 35.1, 31.4), ("THE GREAT SEA", 34.25, 32.4)), lit_routes=[1], size=10, rsize=10, title="ACTS 8:26–40 · GAZA TO CÆSAREA")

def damascus_road(p, w, h, seed, fallen=False, lit=True, led=False):
    """Near Damascus at noon: the road among the hills, the city far off; lit=True a light out of heaven, above the
    brightness of the sun, poured down on the road; fallen=True Saul lying upon the earth in the light, the men that
    journeyed with him standing speechless with their arms flung up; led=True the light gone, Saul led by the hand toward
    the city gate. Jesus is not drawn."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#5AB0D8", "#FFF4C2"), hills(w, h, h * 0.46, seed, color="#B8A07A", amp=14, step=100),
         walls(w * 0.62, w * 0.96, h * 0.54, h * 0.16, seed, towers=3), ground(w, h, h * 0.56, "#D8C090", dy=0),
         f'<path d="M-10 {f(h * 0.98)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.56)} {f(h * 0.64)} {f(w * 0.74)} {f(h * 0.56)}" stroke="#F0E0B8" stroke-width="{f(max(12, h * 0.09))}" fill="none"></path>']
    s = fit(b, max(h * 0.3, b - 210))
    if lit:
        o.append(f'<path d="M{f(w * 0.26)} -10 L {f(w * 0.5)} -10 L {f(w * 0.6)} {f(b + 10)} L {f(w * 0.06)} {f(b + 10)} Z" fill="#FFFFFF" opacity="0.55"></path>'
                 + glow(w * 0.36, b - h * 0.2, h * 0.6, "#FFFFFF", 0.95, f"{p}l") + rays(w * 0.38, -h * 0.1, 30, h * 0.1, h * 1.2, color="#FFFFFF", op=0.35, sw=4))
    if fallen:
        o.append(f'<g transform="translate({f(w * 0.3 + 90 * s * 1.3)} {f(b - 2)}) scale({f(-s * 1.3)} {f(s * 1.3)})" fill="{ROBES["paul"]}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
        for i, x in enumerate((0.66, 0.76, 0.86)):
            o.append(man_fig(p, w * x, b, s * (0.96 - 0.03 * i), ["#6A5A4A", "#4A4A5A", "#5A3A2A"][i], head=["#3A3A3A", "#6A5A3A", None][i], hr="#2A1A10",
                             bd="#2A1A10", kind="Tunic", up=UP_HIGH if i != 1 else None))
    elif led:
        o.append(man_fig(p, w * 0.36, b, s * 0.98, "#6A5A4A", head="#3A3A3A", bd="#2A1A10", kind="Tunic", flip=True, up=[(22, -158), (40, -140), (54, -132)]))
        o.append(paul(p, w * 0.24, b, s, flip=True, up=[(22, -158), (36, -150), (50, -146)]))
        o.append(man_fig(p, w * 0.12, b, s * 0.96, "#4A4A5A", head="#6A5A3A", bd="#2A1A10", kind="Tunic", flip=True))
    else:
        o.append(paul(p, w * 0.3, b, s, flip=True) + man_fig(p, w * 0.18, b, s * 0.96, "#6A5A4A", head="#3A3A3A", bd="#2A1A10", kind="Tunic", flip=True)
                 + man_fig(p, w * 0.08, b, s * 0.94, "#4A4A5A", head="#6A5A3A", bd="#2A1A10", kind="Tunic", flip=True))
    return "".join(o)

def vision_house(p, w, h, seed, who="ananias_dam", pray=True):
    """The Lord said unto him in a vision: within the house, a shaft of white light falling through the window onto the
    one kneeling in prayer (the Lord is not drawn — the words come from the light)."""
    bg, b = _house(w, h, seed, "night")
    o = [mk.defs(p, *ALL), bg]
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(h * 0.14)}" width="{f(w * 0.1)}" height="{f(h * 0.16)}" fill="#FFFFFF" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.66)} {f(h * 0.3)} L {f(w * 0.56)} {f(b)} L {f(w * 0.22)} {f(b)} Z" fill="#FFFFFF" opacity="0.4"></path>'
             + glow(w * 0.4, b - h * 0.2, h * 0.4, "#FFFFFF", 0.7, f"{p}v"))
    s = fit(b, max(h * 0.3, b - 210))
    c = {"ananias_dam": "#3A4A5A", "peter": ROBES["peter"], "cornelius": "#7A1A14", "paul": ROBES["paul"]}[who]
    if pray: o.append(E.kneel(w * 0.4, b, s * 0.9, color=c, skin=SKIN, flip=True))
    else: o.append(WHO[who](p, w * 0.4, b, s, flip=True, up=UP_HIGH))
    return "".join(o)

def scales(p, w, h, seed):
    """In the house of Judas in the street called Straight: Saul sitting, Ananias standing over him with his hands laid on his
    head, and there fall from his eyes as it were scales — small bright flakes — and light comes into the room."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg, glow(w * 0.5, b - h * 0.3, h * 0.4, "#FFF4C2", 0.6, f"{p}s")]
    s = fit(b, max(h * 0.3, b - 210))
    sx = w * 0.46
    o.append(seated(sx, b, s * 0.84, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A"))
    o.append(ananias_dam(p, sx + 130 * s, b, s, up=[(-22, -158), (-50, -160), (-86, -154)]))
    r = random.Random(seed)
    for _ in range(9):
        x = sx + r.uniform(6, 30) * s; y = b - r.uniform(30, 92) * s
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(3.2 * s)}" ry="{f(1.8 * s)}" fill="#F3EFE6" stroke="#8A867E" stroke-width="0.8" transform="rotate({r.randint(0, 180)} {f(x)} {f(y)})"></ellipse>')
    return "".join(o)

def basket_wall(p, w, h, seed):
    """His disciples took him by night and let him down through the wall in a basket: the great wall of Damascus under the
    stars, a window high in it, the basket going down on its rope with Saul in it, the brethren leaning out above."""
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(50, w, h * 0.5, seed), moon_(w * 0.86, h * 0.16, max(10, h * 0.04))]
    x0, x1 = w * 0.18, w * 0.82
    o.append(f'<rect x="{f(x0)}" y="{f(h * 0.1)}" width="{f(x1 - x0)}" height="{f(h)}" fill="#6A5A54" stroke="{INK}" stroke-width="2.4"></rect>')
    for k in range(12):
        y = h * 0.1 + h * k / 12
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="#4A3E3A" stroke-width="2"></path>')
    bw = max(10, h * 0.04)
    xx = x0
    while xx < x1 - bw:
        o.append(f'<rect x="{f(xx)}" y="{f(h * 0.1 - bw)}" width="{f(bw)}" height="{f(bw + 1)}" fill="#6A5A54" stroke="{INK}" stroke-width="1.6"></rect>'); xx += bw * 1.9
    s = max(0.4, h / 380)
    wx, wy = w * 0.5, h * 0.1 + 70 * s
    o.append(f'<rect x="{f(wx - 46 * s)}" y="{f(wy - 60 * s)}" width="{f(92 * s)}" height="{f(74 * s)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<clipPath id="{p}win"><rect x="{f(wx - 46 * s)}" y="{f(wy - 60 * s)}" width="{f(92 * s)}" height="{f(74 * s)}"></rect></clipPath>'
             f'<g clip-path="url(#{p}win)">' + mk.person(p, round(wx - 14 * s), round(wy + 60 * s), round(s * 0.5, 3), body=SKIN, cloth="#4A4A5A", kind="Tunic", sw=3,
                                                         up=[(-22, -158), (-28, -130), (-30, -100)], extra=A.BLACK_BEARD) + '</g>')
    by = h * 0.72
    o.append(f'<path d="M{f(wx)} {f(wy + 10)} L {f(wx)} {f(by - 60 * s)}" stroke="#C8A878" stroke-width="3"></path>')
    o.append(f'<g transform="translate({f(wx)} {f(by)})">' + mk.person(p, 0, 0, round(s, 3), body=SKIN, cloth=ROBES["paul"], kind="Robe", sw=3,
                                                                   extra=A.headcloth("#5A4A3A", cord="#2A1A10") + beard("#3A2A1A")) + '</g>')
    o.append(f'<path d="M{f(wx - 60 * s)} {f(by - 100 * s)} C {f(wx - 60 * s)} {f(by + 10 * s)} {f(wx + 60 * s)} {f(by + 10 * s)} {f(wx + 60 * s)} {f(by - 100 * s)} Z" fill="#B8904A" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(wx - 58 * s)} {f(by - 100 * s + 22 * s * j)} L {f(wx + 58 * s)} {f(by - 100 * s + 22 * s * j)}" stroke="#7A5A2A" stroke-width="2"></path>' for j in range(1, 5))
             + f'<path d="M{f(wx - 60 * s)} {f(by - 100 * s)} L {f(wx)} {f(by - 180 * s)} L {f(wx + 60 * s)} {f(by - 100 * s)}" stroke="#C8A878" stroke-width="2" fill="none"></path>')
    o.append(ground(w, h, h * 0.94, "#1A1A2A", dy=0))
    return "".join(o)

def moon_(x, y, r):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * 2.4)}" fill="#F3EFE6" opacity="0.12"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></circle>')

def tarsus_road(w, h):
    """They brought him down to Cæsarea, and sent him forth to Tarsus: the map, Jerusalem to Cæsarea, and by sea to Tarsus."""
    return geo.med_map(w, h, box=(31.5, 38.5, 30.8, 37.6), places=("JERUSALEM", "CÆSAREA", "TARSUS", "DAMASCUS", "ANTIOCH"),
                       routes=[("DAMASCUS", "JERUSALEM"), ("JERUSALEM", "CÆSAREA"), ("CÆSAREA", (34.2, 34.6), (34.6, 36.3), "TARSUS")], hi=("TARSUS",),
                       regions=("CILICIA", "SYRIA", "CYPRUS", "JUDÆA"), lit_routes=[1, 2], size=10, rsize=10, title="ACTS 9:26–30 · SENT FORTH TO TARSUS")

def aeneas(p, w, h, seed, risen=False):
    """Æneas at Lydda, who had kept his bed eight years: in his house, Peter standing over the bed; risen=True Æneas standing
    up beside it, rolling up his bed."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL, *LIE), bg]
    s = fit(b, max(h * 0.3, b - 210))
    if not risen:
        o.append(on_bed(p, w * 0.56, b - 30 * s, 230 * s, cloth="#8A9AAA"))
        o.append(peter(p, w * 0.26, b, s, flip=True, up=UP_BLESS))
    else:
        o.append(bedroll(w * 0.62, b - 12 * s, 120 * s, 18 * s))
        o.append(peter(p, w * 0.26, b, s, flip=True) + glow(w * 0.46, b - 110 * s, 130 * s, "#FFF4C2", 0.6, f"{p}a")
                 + man_fig(p, w * 0.46, b, s, "#8A9AAA", hr="#3A2A1A", bd="#3A2A1A", kind="Tunic", up=UP_HIGH))
    return "".join(o)

def dorcas(p, w, h, seed, raised=False):
    """The upper chamber at Joppa: Dorcas laid on the bed under a white linen cloth, the widows standing by weeping and
    holding up the coats and garments she made; raised=True Peter giving her his hand, Dorcas standing alive (a rose robe, a
    white veil) and the widows coming in at the door."""
    bg, b = _upper(w, h, seed)
    o = [mk.defs(p, *ALL, *LIE), bg]
    s = fit(b, max(h * 0.3, b - 210))
    if not raised:
        o.append(bedroll(w * 0.32, b - 40 * s, 230 * s, 16 * s) + f'<path d="M{f(w * 0.32 - 104 * s)} {f(b - 40 * s)} C {f(w * 0.32 - 90 * s)} {f(b - 66 * s)} {f(w * 0.32 + 80 * s)} {f(b - 70 * s)} {f(w * 0.32 + 108 * s)} {f(b - 40 * s)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="2"></path>')
        for i, x in enumerate((0.56, 0.68, 0.8, 0.92)):
            coat = (f'<path d="M-60 -150 L -40 -150 L -34 -96 L -66 -96 Z" fill="{["#C2456A", "#1F5FAD", "#E8B830", "#2E6B3A"][i]}" stroke="#0D0D0F" stroke-width="1.6"></path>' if i % 2 == 0 else "")
            o.append(woman_fig(p, w * x, b, s * 0.92, ["#3A3A4A", "#4A3A3A", "#2A3A4A", "#4A4A4A"][i], ["#2A2A3A", "#3A2A2A", "#1A2A3A", "#3A3A3A"][i],
                               up=[(-22, -158), (-40, -150), (-56, -150)] if i % 2 == 0 else [(-22, -158), (-14, -176), (-8, -190)], extra=coat))
        o.append(peter(p, w * 0.08, b, s, flip=True))
    else:
        o.append(bedroll(w * 0.4, b - 40 * s, 230 * s, 16 * s))
        o.append(peter(p, w * 0.22, b, s, flip=True, up=UP_BLESS) + glow(w * 0.36, b - 110 * s, 140 * s, "#FFF4C2", 0.7, f"{p}d")
                 + woman_fig(p, w * 0.36, b, s * 0.94, "#B85A6A", "#F3EFE6"))
        for i, x in enumerate((0.66, 0.78, 0.9)):
            o.append(woman_fig(p, w * x, b, s * 0.9, ["#3A3A4A", "#4A3A3A", "#2A3A4A"][i], ["#2A2A3A", "#3A2A2A", "#1A2A3A"][i], up=UP_HIGH if i == 0 else None))
    return "".join(o)

def tanner(p, w, h, seed):
    """With one Simon a tanner, at Joppa: a house by the sea-shore, hides stretched on frames to dry and vats beside it,
    the harbour of Joppa and a ship beyond; Peter at the door."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sea_(w, h, h * 0.5, seed), ship(w * 0.8, h * 0.58, max(0.4, h / 600)), shore(w, h, h * 0.64, color="#D8C090")]
    k = max(0.5, h / 340)
    hx = w * 0.14
    o.append(f'<rect x="{f(hx)}" y="{f(b - 170 * k)}" width="{f(170 * k)}" height="{f(170 * k)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx - 6)}" y="{f(b - 178 * k)}" width="{f(170 * k + 12)}" height="{f(10 * k)}" fill="#8A6A4A" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(hx + 60 * k)} {f(b)} L {f(hx + 60 * k)} {f(b - 60 * k)} C {f(hx + 60 * k)} {f(b - 84 * k)} {f(hx + 100 * k)} {f(b - 84 * k)} {f(hx + 100 * k)} {f(b - 60 * k)} L {f(hx + 100 * k)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="1.6"></path>')
    for i in range(3):
        fx = w * (0.48 + 0.12 * i)
        o.append(f'<path d="M{f(fx - 34 * k)} {f(b)} L {f(fx - 34 * k)} {f(b - 110 * k)} M{f(fx + 34 * k)} {f(b)} L {f(fx + 34 * k)} {f(b - 110 * k)}" stroke="#5A3A22" stroke-width="{f(4 * k)}"></path>'
                 f'<path d="M{f(fx - 30 * k)} {f(b - 104 * k)} C {f(fx - 20 * k)} {f(b - 110 * k)} {f(fx + 20 * k)} {f(b - 110 * k)} {f(fx + 30 * k)} {f(b - 104 * k)} L {f(fx + 26 * k)} {f(b - 40 * k)} C {f(fx + 10 * k)} {f(b - 30 * k)} {f(fx - 10 * k)} {f(b - 30 * k)} {f(fx - 26 * k)} {f(b - 40 * k)} Z" fill="{["#B8906A", "#A87A54", "#C8A07A"][i]}" stroke="{INK}" stroke-width="1.8"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    o.append(peter(p, hx + 130 * k + 30 * s, b, s, flip=True))
    return "".join(o)
