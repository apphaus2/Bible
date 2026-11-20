"""Drawings for the Hebrews volume, chapter 4 (Hebrews 11–13): the cloud of witnesses, the race, Sinai and mount Zion, the
strangers at Mamre, without the gate, the great shepherd, Timothy set at liberty, they of Italy.

Hebrews 11 is drawn as a long run of scenes, each in the look the earlier volumes give its people, every figure on the kit
figure (epistle.robed), never the old blob shapes: Abel (a shepherd's fleece-coloured tunic, brown hair) at his altar, Cain's
altar of fruits beside it with its smoke beaten down — no one slain; Enoch's road going up into the light, his footprints
stopping (he is not drawn); the ark on dry ground under the coming storm; Abraham's road on Acts' map, and the tents of
Abraham, Isaac and Jacob under the stars with the city that hath the foundations faint in the sky; Sarah with the child
(Romans' drawing); the pilgrims greeting the promises from afar; Moriah — the altar and the wood, Abraham and Isaac
standing together and the ram caught in the thicket (Isaac is never bound in the drawing); Jacob old, leaning on the top of
his staff, his hands on the heads of Joseph's two sons; Joseph's coffin borne out of Egypt on poles; Moses' mother holding
the child by lamplight, his father at the shut door; Moses in the white linen and red-and-white headcloth of Pharaoh's
house turning from the palace to his brethren at the brick-kilns; the bush that burned (Exodus' drawing); the passover —
a street of shut doors at midnight, lamplight under them (the blood in words only, the destroyer not drawn); the dry path
through the sea (Exodus' drawing); Jericho's wall fallen flat; Rahab's window and its scarlet line (Joshua's drawing);
Gideon, Barak, Samson, Jephthah, David and Samuel in a strip of faces; the lions lying still in the den and the furnace
with no one in it (Daniel's drawings, no one drawn); and 11:35–38 words only over the deserts and mountains and caves and
the holes of the earth, empty."""
from heb.art import *
from heb.art import art, plate_label, _defs, f, INK, defs_up, face_cell, cloud_bank, throne_of_light, angel_fig, GOLD, CY, CREAM, brother_fig, risen_fig
from heb.art2 import altar_fire, tent_plan
from rom.art2 import abraham, sarah_old
import mk

def strip(people, w, h, lights=None, rows=None):
    """Portrait cells in a strip (one row, or two when the panel is narrow or tall): people = [(face token, name)]."""
    n = len(people)
    rows = rows or (2 if (w / n < 110 or h > w * 0.62) else 1)
    per = (n + rows - 1) // rows
    cw, ch = w / per, h / rows
    lights = lights or ["#FFE680", "#FFC14D", "#FFF4C2", "#CFE0FF", "#FFB04A", "#FFE680"]
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#1A1028"></rect>']
    for i, (tok, nm) in enumerate(people):
        o.append(face_cell(tok, (i % per) * cw, (i // per) * ch, cw, ch, f"st{i}{n}", light=lights[i % len(lights)], name=nm))
    return "".join(o)

def city_of_light(cx, cb, wd, hh, k=1.0, op=1.0):
    """A city of light: walls and towers of white and gold on their foundations, gates of gold; (cx, cb) the middle of its
    foot, wd wide, the towers up to hh tall."""
    o = [f'<g opacity="{op}">']
    for i in range(9):
        x = cx - wd * 0.45 + i * wd * 0.1125; th = hh * (1.0 if i % 2 else 0.7) * (1.15 if i == 4 else 1)
        o.append(f'<rect x="{f(x - wd * 0.035)}" y="{f(cb - th)}" width="{f(wd * 0.07)}" height="{f(th)}" fill="#FFFBEA" stroke="#C8962A" stroke-width="1.6"></rect>'
                 f'<path d="M{f(x - wd * 0.035)} {f(cb - th)} L {f(x)} {f(cb - th - 12 * k)} L {f(x + wd * 0.035)} {f(cb - th)}" fill="#FFE9A8" stroke="#C8962A" stroke-width="1.2"></path>')
    o.append(f'<rect x="{f(cx - wd / 2)}" y="{f(cb - hh * 0.46)}" width="{f(wd)}" height="{f(hh * 0.46)}" fill="#FFF4D0" stroke="#C8962A" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(cx + d * wd * 0.15 - 10 * k)} {f(cb)} L {f(cx + d * wd * 0.15 - 10 * k)} {f(cb - 22 * k)} A {f(10 * k)} {f(10 * k)} 0 0 1 {f(cx + d * wd * 0.15 + 10 * k)} {f(cb - 22 * k)} L {f(cx + d * wd * 0.15 + 10 * k)} {f(cb)} Z" fill="#FFE680" stroke="#C8962A" stroke-width="1.2"></path>' for d in (-2, -1, 0, 1, 2))
             + "".join(f'<rect x="{f(cx - wd / 2 - 6 * k * (j + 1))}" y="{f(cb + 6 * k * j)}" width="{f(wd + 12 * k * (j + 1))}" height="{f(6 * k)}" fill="#E8D49A" stroke="#C8962A" stroke-width="1"></rect>' for j in range(3)))
    o.append('</g>')
    return "".join(o)

# ---- Hebrews 11: the elders -----------------------------------------------------------------------------------------------
def abel(p, w, h, seed):
    """By faith Abel offered unto God a more excellent sacrifice than Cain: two altars of field stones on the hillside at
    evening — Abel standing by his, his hands lifted, his flock behind him, its smoke going straight up into the light; Cain's
    altar of the fruits of the ground at the right, its smoke beaten down along the ground (no one slain, no beast on the
    altar drawn)."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#3A2A5A", "#FFC890"), halo(w * 0.36, 0, h * 0.5, "#FFF4C2", 0.6), hills(w, h, h * 0.6, seed, color="#6A5A4A", amp=12, step=90),
         ground(w, h, h * 0.68, "#9A8A5A", dy=0)]
    k = min(1.0, h / 300)
    def stones(x, base):
        return "".join(f'<ellipse cx="{f(x + dx * k)}" cy="{f(base - dy * k)}" rx="{f(16 * k)}" ry="{f(10 * k)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.6"></ellipse>'
                       for dx, dy in ((-28, 8), (0, 8), (28, 8), (-14, 24), (14, 24), (0, 40)))
    ax = w * 0.44
    o.append(f'<path d="M{f(ax)} {f(b - 54 * k)} C {f(ax - 10 * k)} {f(h * 0.5)} {f(ax + 10 * k)} {f(h * 0.25)} {f(ax)} -10" fill="none" stroke="#F3EFE6" stroke-width="{f(18 * k)}" opacity="0.55" stroke-linecap="round"></path>')
    o.append(stones(ax, b) + "".join(f'<path d="M{f(ax + (i - 2) * 9 * k - 6 * k)} {f(b - 50 * k)} C {f(ax + (i - 2) * 9 * k - 6 * k)} {f(b - 66 * k)} {f(ax + (i - 2) * 9 * k)} {f(b - 70 * k)} {f(ax + (i - 2) * 9 * k)} {f(b - 76 * k)} C {f(ax + (i - 2) * 9 * k + 4 * k)} {f(b - 66 * k)} {f(ax + (i - 2) * 9 * k + 6 * k)} {f(b - 60 * k)} {f(ax + (i - 2) * 9 * k + 6 * k)} {f(b - 50 * k)} Z" fill="{["#FF6A2A", "#FFC14D", "#FFE680"][i % 3]}"></path>' for i in range(5)))
    cx = w * 0.82
    o.append(f'<path d="M{f(cx - 10 * k)} {f(b - 54 * k)} C {f(cx - 60 * k)} {f(b - 70 * k)} {f(cx - 140 * k)} {f(b - 50 * k)} {f(cx - 220 * k)} {f(b - 60 * k)}" fill="none" stroke="#5A5060" stroke-width="{f(16 * k)}" opacity="0.6" stroke-linecap="round"></path>')
    o.append(stones(cx, b) + "".join(f'<circle cx="{f(cx + dx * k)}" cy="{f(b - 52 * k)}" r="{f(7 * k)}" fill="{c}" stroke="{INK}" stroke-width="1"></circle>' for dx, c in ((-14, "#C8302A"), (0, "#E8B830"), (14, "#7AB04A"))))
    for i in range(4):
        o.append(f'<ellipse cx="{f(w * (0.04 + 0.06 * i))}" cy="{f(b - 12 * k - (i % 2) * 6 * k)}" rx="{f(18 * k)}" ry="{f(11 * k)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></ellipse>'
                 f'<circle cx="{f(w * (0.04 + 0.06 * i) + 16 * k)}" cy="{f(b - 18 * k - (i % 2) * 6 * k)}" r="{f(6 * k)}" fill="#3A3A3A"></circle>')
    s = fit(b, max(h * 0.25, b - 220))
    staff = '<path d="M26 -150 L 40 4" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, w * 0.3, b, s, "#C8B898", hair="#3A2214", belt="#6A4A2A", flip=True, up=[(-22, -158), (-34, -186), (-36, -212)], extra=staff))
    o.append(plate_label(ax, h * 0.1, "ABEL", "#7A4A10", 10, halo_="#FFE6C0") + plate_label(cx, h * 0.46, "CAIN", "#4A3A3A", 10, halo_="#FFC890"))
    return "".join(o)

def enoch(p, w, h, seed):
    """By faith Enoch was translated that he should not see death; and he was not found: a road climbing the bare hill into a
    great light, a line of footprints going up it, and where the light begins the footprints stop — no one drawn."""
    o = [sky(w, h, "#3A3A7A", "#FFE6C0"), glow(w * 0.8, h * 0.2, h * 0.7, "#FFFFFF", 0.9, f"{p}g"), rays(w * 0.8, h * 0.2, 40, h * 0.1, max(w, h), "#FFF4C2", 0.3, 4)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.5)} {f(w * 0.86)} {f(h * 0.32)} L {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A5A7A" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(w * 0.02)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.55)} {f(h * 0.64)} {f(w * 0.8)} {f(h * 0.42)} L {f(w * 0.84)} {f(h * 0.44)} C {f(w * 0.6)} {f(h * 0.68)} {f(w * 0.36)} {f(h * 0.88)} {f(w * 0.16)} {f(h + 10)} Z" fill="#B8A8B8" opacity="0.7"></path>')
    k = min(1.0, h / 300)
    for i in range(11):                                                       # the footprints, stopping
        t = i / 12; x = w * (0.1 + 0.6 * t) + (6 * k if i % 2 else -6 * k); y = h * (0.94 - 0.44 * t)
        sc = k * (1 - 0.5 * t)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(6 * sc)}" ry="{f(3.4 * sc)}" fill="#3A2A3A" transform="rotate(-30 {f(x)} {f(y)})"></ellipse>')
    return "".join(o)

def ark_ready(p, w, h, seed):
    """By faith Noah, being warned of God concerning things not seen as yet … prepared an ark to the saving of his house: the
    ark on dry ground, its door open and the ramp let down, the storm not yet come but black on the horizon (Genesis'
    drawing, under a sky)."""
    from genesis.art2 import ark_ramp
    return sky(w, h, "#4A4A5E", "#C8B890") + cloud_bank(w, h * 0.12, seed, "#2A2A36", 0.9, k=min(1.0, h / 260)) + mk.defs(p, *ALL) + ark_ramp(p, w, h, seed)

def abraham_road(w, h):
    """By faith Abraham, when he was called, obeyed to go out … and he went out, not knowing whither he went: the map from Ur of
    the Chaldæans up to Haran and into the land of Canaan (Acts' map of Abraham's road)."""
    from act import geo
    return geo.med_map(w, h, box=(31, 48, 28.5, 38.5), places=("UR", "HARAN", "SHECHEM", "JERUSALEM", "DAMASCUS", "MEMPHIS"),
                       routes=[("UR", (44.4, 33.2), (40.3, 35.6), "HARAN"), ("HARAN", (37.2, 35.8), "DAMASCUS", "SHECHEM")], hi=("UR", "HARAN", "SHECHEM"),
                       regions=("MESOPOTAMIA", "CHALDÆA", "CANAAN", "EGYPT", "SYRIA"), lit_routes=[0, 1], size=10, rsize=10,
                       title="HEBREWS 11:8 · NOT KNOWING WHITHER HE WENT")

def sojourners(p, w, h, seed):
    """He became a sojourner in the land of promise … dwelling in tents, with Isaac and Jacob … for he looked for the city which
    hath the foundations, whose builder and maker is God: three black tents under the stars, Abraham at the door of the first,
    and faint in the sky above the hills the walls and gates of a city of light."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#05051A", "#2A2050"), starfield(w, h, seed, 80, 0.7)]
    cx = w * 0.6                                                              # the city of light in the sky
    o.append(halo(cx, h * 0.3, h * 0.34, "#FFE680", 0.3) + city_of_light(cx, h * 0.42, w * 0.5, h * 0.24, min(1.0, h / 320), op=0.8))
    o.append(hills(w, h, h * 0.66, seed, color="#14142E", amp=12, step=90) + ground(w, h, h * 0.74, "#1E1A30", dy=0))
    k = min(1.0, h / 300)
    for i, x in enumerate((0.36, 0.62, 0.86)):
        o.append(black_tent(w * x, b - 4 * k * (i % 2), 150 * k, 70 * k, lit=True))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(abraham(p, w * 0.14, b, s, flip=True, up=[(-22, -158), (-30, -190), (-30, -218)]))
    return "".join(o)

def promise_child(p, w, h, seed):
    """By faith even Sarah herself received power to conceive seed when she was past age: Sarah, grey-haired, at the tent door
    with the child Isaac in her arms, Abraham standing by (Romans' drawing)."""
    from rom.art4 import child_promise
    return child_promise(p, w, h, seed)

def afar(p, w, h, seed):
    """These all died in faith, not having received the promises, but having seen them and greeted them from afar … strangers
    and pilgrims on the earth … they desire a better country, that is, a heavenly: the pilgrims with their staves on a ridge at
    dusk — Abraham, Sarah, Isaac, Jacob — looking far off to a city of light on the edge of the sky, Abraham's hand lifted to
    it."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#2A1A3A", "#E8A06A"), starfield(w, h, seed, 20, 0.3)]
    cx = w * 0.82
    o.append(glow(cx, h * 0.46, h * 0.4, "#FFF4C2", 0.8, f"{p}c") + town_hill(cx, h * 0.56, w * 0.22, h * 0.16, seed, color="#FFE9A8", lit=True))
    o.append(hills(w, h, h * 0.62, seed, color="#3A2A3A", amp=12, step=90))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.78)} C {f(w * 0.2)} {f(h * 0.74)} {f(w * 0.4)} {f(h * 0.76)} {f(w * 0.56)} {f(h * 0.84)} L {f(w * 0.62)} {f(h + 10)} Z" fill="#4A3A3A" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.3, b - 210)) * 0.9
    staff = '<path d="M-26 -150 L -40 4" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, w * 0.08, b, s * 0.96, "#2C4A7A", hair="#2A1A10", beard="#2A1A10", flip=True, extra=staff))                       # Jacob
    o.append(robed(p, w * 0.19, b - 2, s * 0.98, "#8A6A4A", hair="#5A3A22", beard="#5A3A22", flip=True, extra=staff))                   # Isaac
    o.append(sarah_old(p, w * 0.3, b - 4, s, flip=True))
    o.append(abraham(p, w * 0.42, b - 6, s, flip=True, up=[(-22, -158), (-48, -162), (-72, -172)]))
    o.append(plate_label(cx, h * 0.12, "A BETTER COUNTRY · THAT IS, A HEAVENLY", "#7A4A10", 10, halo_="#FFE6C0"))
    return "".join(o)

def moriah(p, w, h, seed):
    """By faith Abraham, being tried, offered up Isaac … accounting that God is able to raise up, even from the dead; from
    whence he did also in a figure receive him back: the top of the mount in the land of Moriah in the morning, the altar
    of stones with the wood laid in order on it, Abraham and Isaac standing together beside it, Abraham's hand on his son's
    shoulder, and in the thicket behind them the ram caught by his horns."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#5A7AB0", "#FFE6B0"), halo(w * 0.7, h * 0.2, h * 0.4, "#FFF4C2", 0.6)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} Z" fill="#A89070" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.0, h / 300)
    ax = w * 0.5
    for dx, dy in ((-36, 10), (-12, 10), (12, 10), (36, 10), (-24, 28), (0, 28), (24, 28), (-12, 44), (12, 44)):
        o.append(f'<ellipse cx="{f(ax + dx * k)}" cy="{f(b - dy * k)}" rx="{f(15 * k)}" ry="{f(10 * k)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    for i in range(4):
        o.append(f'<rect x="{f(ax - 40 * k)}" y="{f(b - 60 * k - i * 7 * k)}" width="{f(80 * k)}" height="{f(6 * k)}" rx="{f(3 * k)}" fill="#8A5A2A" stroke="{INK}" stroke-width="1" transform="rotate({(-1) ** i * 4} {f(ax)} {f(b - 58 * k - i * 7 * k)})"></rect>')
    tx = w * 0.74                                                             # the thicket and the ram
    o.append("".join(f'<path d="M{f(tx + (i - 3) * 14 * k)} {f(b)} C {f(tx + (i - 3) * 18 * k)} {f(b - 40 * k)} {f(tx + (i - 3) * 10 * k)} {f(b - 70 * k)} {f(tx + (i - 3) * 22 * k)} {f(b - 96 * k)}" fill="none" stroke="#3A2A1A" stroke-width="2.4"></path>' for i in range(7)))
    o.append(f'<ellipse cx="{f(tx)}" cy="{f(b - 30 * k)}" rx="{f(34 * k)}" ry="{f(20 * k)}" fill="#E8E2D6" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<path d="M{f(tx - 20 * k)} {f(b - 14 * k)} L {f(tx - 22 * k)} {f(b)} M{f(tx + 18 * k)} {f(b - 14 * k)} L {f(tx + 20 * k)} {f(b)}" stroke="{INK}" stroke-width="{f(4 * k)}"></path>'
             f'<ellipse cx="{f(tx - 36 * k)}" cy="{f(b - 42 * k)}" rx="{f(12 * k)}" ry="{f(9 * k)}" fill="#3A3A3A" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(tx - 40 * k)} {f(b - 50 * k)} C {f(tx - 56 * k)} {f(b - 64 * k)} {f(tx - 30 * k)} {f(b - 76 * k)} {f(tx - 26 * k)} {f(b - 60 * k)}" fill="none" stroke="#C8B898" stroke-width="{f(5 * k)}"></path>')
    o.append("".join(f'<path d="M{f(tx + (i - 2) * 16 * k)} {f(b - 50 * k)} C {f(tx + (i - 2) * 12 * k)} {f(b - 70 * k)} {f(tx + (i - 2) * 20 * k)} {f(b - 84 * k)} {f(tx + (i - 2) * 14 * k)} {f(b - 104 * k)}" fill="none" stroke="#2A1A10" stroke-width="2"></path>' for i in range(5)))
    s = fit(b, max(h * 0.25, b - 220))
    o.append(abraham(p, w * 0.18, b, s, flip=True, up=[(-22, -158), (-46, -150), (-64, -140)]))
    o.append(robed(p, w * 0.29, b, s * 0.82, "#C8A060", hair="#5A3A22", belt="#6A4A2A", flip=True))
    return "".join(o)

def jacob_blessing(p, w, h, seed):
    """By faith Isaac blessed Jacob and Esau … By faith Jacob, when he was dying, blessed each of the sons of Joseph; and
    worshipped, leaning upon the top of his staff: in Egypt, Jacob old and white-haired in his slate-blue robe, bowed on the
    top of his staff, his hand on the heads of Joseph's two sons standing before him in white linen; Joseph in his collar
    beside them."""
    b = h * 0.95
    o = [defs_up(p), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', glow(w * 0.5, h * 0.3, h * 0.7, "#FFC14D", 0.45, f"{p}l")]
    k = min(1.0, h / 300)
    for x in (w * 0.08, w * 0.92):                                            # pillars of an Egyptian house
        o.append(f'<rect x="{f(x - 16 * k)}" y="-10" width="{f(32 * k)}" height="{f(b + 10)}" fill="#C8A060" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(x - 16 * k)} {f(h * 0.2)} L {f(x + 16 * k)} {f(h * 0.2)} M{f(x - 16 * k)} {f(h * 0.24)} L {f(x + 16 * k)} {f(h * 0.24)}" stroke="#1F5FAD" stroke-width="3"></path>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#6A5040"></rect>')
    s = fit(b, max(h * 0.25, b - 220))
    staff = '<path d="M-30 -132 L -40 4" stroke="#6A4A2A" stroke-width="6" stroke-linecap="round"></path><circle cx="-30" cy="-134" r="5" fill="#6A4A2A"></circle>'
    o.append(robed(p, w * 0.34, b, s, "#2C4A7A", hair="#E8E2D6", beard="#E8E2D6", mantle="#1F3A5A", flip=True, up=[(-22, -158), (-44, -156), (-62, -146)], extra=staff))
    for i, x in enumerate((0.48, 0.58)):
        o.append(robed(p, w * x, b, s * 0.66, "#F3EFE6", hair="#1A1210", belt="#E8B830", flip=False))
    o.append(robed(p, w * 0.74, b, s, "#F3EFE6", hair="#3A2214", belt="#E8B830", mantle="#1F5FAD", flip=False,
                   extra='<path d="M-22 -166 C -10 -150 10 -150 22 -166" fill="none" stroke="#E8B830" stroke-width="6"></path>'))
    return "".join(o)

def bones(p, w, h, seed):
    """By faith Joseph, when his end was nigh, made mention of the departure of the children of Israel; and gave commandment
    concerning his bones: the departure come — at first light, on the road out of Egypt with the pyramids behind, Joseph's
    painted coffin borne on poles on the shoulders of four men of Israel in the long file of the people."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#3A3A7A", "#FFC890"), halo(w * 0.86, h * 0.4, h * 0.3, "#FFE6A0", 0.55)]
    k = min(1.0, h / 300)
    for i, x in enumerate((0.08, 0.2)):
        o.append(f'<path d="M{f(w * x - 50 * k)} {f(h * 0.62)} L {f(w * x)} {f(h * 0.62 - 70 * k)} L {f(w * x + 50 * k)} {f(h * 0.62)} Z" fill="#D8B880" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(ground(w, h, h * 0.62, "#C8A878", dy=0))
    s = fit(b, max(h * 0.3, b - 200)) * 0.9
    for i in range(5):                                                        # the file of the people behind
        o.append(brother_fig(p, w * (0.04 + 0.08 * i), b - 30 * k, s * 0.7, i + 1, flip=True))
    cx0, cx1 = w * 0.48, w * 0.82                                             # the bearers and the coffin
    cy = b - 160 * s
    o.append(f'<path d="M{f(cx0 - 30 * k)} {f(cy)} L {f(cx1 + 30 * k)} {f(cy)}" stroke="#6A4A2A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(cx0 + 20 * k)} {f(cy - 4 * k)} L {f(cx0 + 30 * k)} {f(cy - 50 * k)} C {f(cx0 + 60 * k)} {f(cy - 64 * k)} {f(cx1 - 60 * k)} {f(cy - 64 * k)} {f(cx1 - 30 * k)} {f(cy - 50 * k)} L {f(cx1 - 20 * k)} {f(cy - 4 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(cx0 + 40 * k + i * (cx1 - cx0 - 80 * k) / 6)} {f(cy - 56 * k)} L {f(cx0 + 40 * k + i * (cx1 - cx0 - 80 * k) / 6)} {f(cy - 6 * k)}" stroke="#1F5FAD" stroke-width="{f(4 * k)}"></path>' for i in range(7)))
    for i, x in enumerate((cx0, cx0 + (cx1 - cx0) * 0.33, cx0 + (cx1 - cx0) * 0.66, cx1)):
        o.append(brother_fig(p, x, b, s, i, flip=True, up=[(-22, -158), (-14, -170), (-6, -168)]) if i % 2 == 0 else robed(p, x, b, s, ["#6A4A3A", "#4A5A6A"][i // 2], head="#E8E2D6", cord="#6A5A3A", beard="#2A1A10", flip=True, up=[(-22, -158), (-14, -170), (-6, -168)]))
    return "".join(o)

def moses_hid(p, w, h, seed):
    """By faith Moses, when he was born, was hid three months by his parents, because they saw he was a goodly child; and they
    were not afraid of the king's commandment: within a Hebrew house by lamplight, his mother sitting with the child in her
    arms, his father standing at the shut and barred door, the night window beyond."""
    b = h * 0.95
    o = [defs_up(p), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2418"></rect>', glow(w * 0.42, h * 0.4, h * 0.6, "#FFC14D", 0.5, f"{p}l")]
    k = min(1.0, h / 300)
    o.append(night_window(w * 0.66, h * 0.18, w * 0.12, h * 0.2, seed) + f'<rect x="{f(w * 0.82)}" y="{f(h * 0.2)}" width="{f(w * 0.12)}" height="{f(b - h * 0.2)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.8)}" y="{f(h * 0.56)}" width="{f(w * 0.16)}" height="{f(8 * k)}" fill="#3A2214" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#5A3A2A"></rect>')
    o.append(f'<path d="M{f(w * 0.46 - 16 * k)} {f(b - 70 * k)} L {f(w * 0.46 + 16 * k)} {f(b - 70 * k)} L {f(w * 0.46 + 10 * k)} {f(b - 60 * k)} L {f(w * 0.46 - 10 * k)} {f(b - 60 * k)} Z" fill="#A86A3A" stroke="{INK}" stroke-width="1.4"></path>'
             f'<path d="M{f(w * 0.46 + 12 * k)} {f(b - 72 * k)} c -3 -8 1 -14 1 -18 c 3 6 5 12 -1 18 Z" fill="#FFE680"></path>'
             f'<rect x="{f(w * 0.4)}" y="{f(b - 60 * k)}" width="{f(w * 0.12)}" height="{f(60 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(b, max(h * 0.25, b - 220))
    babe = '<ellipse cx="-30" cy="-112" rx="20" ry="9" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></ellipse><circle cx="-46" cy="-116" r="7" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.2"></circle>'
    o.append(robed(p, w * 0.24, b, s, "#5A6A8A", woman=True, veil="#2A3A5A", pose="sit", up=[(-22, -158), (-36, -126), (-44, -114)], extra=babe))
    o.append(robed(p, w * 0.72, b, s, "#6A4A3A", head="#E8E2D6", cord="#6A5A3A", beard="#2A1A10", up=[(-22, -158), (-6, -140), (14, -124)]))
    return "".join(o)

def moses_turns(p, w, h, seed):
    """By faith Moses, when he was grown up, refused to be called the son of Pharaoh's daughter; choosing rather to share ill
    treatment with the people of God …: at the left the gold-and-blue colonnade of Pharaoh's house; Moses in the white linen
    and red-and-white headcloth of the palace walking away from it to the right, toward his brethren at the brick-kilns under
    the taskmaster's sun."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#5AB0D8", "#FFF0C0"), ground(w, h, h * 0.72, "#D8B880", dy=0)]
    k = min(1.0, h / 300)
    for i in range(4):                                                        # Pharaoh's colonnade
        x = w * (0.02 + 0.07 * i)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.14)}" width="{f(26 * k)}" height="{f(b - h * 0.14)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(x)} {f(h * 0.24)} L {f(x + 26 * k)} {f(h * 0.24)} M{f(x)} {f(h * 0.28)} L {f(x + 26 * k)} {f(h * 0.28)}" stroke="#1F5FAD" stroke-width="3"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w * 0.3)}" height="{f(h * 0.07)}" fill="#1F5FAD" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(6):                                                        # the brick-kilns and the bricks drying
        x = w * (0.6 + 0.07 * i); y = h * (0.84 + 0.04 * (i % 2))
        o.append(f'<rect x="{f(x)}" y="{f(y - 14 * k)}" width="{f(24 * k)}" height="{f(14 * k)}" fill="#A8603A" stroke="{INK}" stroke-width="1.2"></rect>')
    o.append(f'<path d="M{f(w * 0.86)} {f(h * 0.72)} L {f(w * 0.86)} {f(h * 0.4)} L {f(w * 0.96)} {f(h * 0.4)} L {f(w * 0.96)} {f(h * 0.72)} Z" fill="#8A5A3A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.91)} {f(h * 0.4)} C {f(w * 0.86)} {f(h * 0.3)} {f(w * 0.96)} {f(h * 0.2)} {f(w * 0.9)} {f(h * 0.08)}" fill="none" stroke="#8A8080" stroke-width="{f(14 * k)}" opacity="0.6" stroke-linecap="round"></path>')
    s = fit(b, max(h * 0.25, b - 220))
    for i, x in enumerate((0.66, 0.76)):                                      # his brethren, bowed under their loads
        o.append(robed(p, w * x, b - 6 * k, s * 0.86, ["#8A7A5A", "#6A5A4A"][i], hair="#1A1210", beard="#1A1210", belt="#4A3A2A",
                       up=[(-22, -158), (-10, -190), (6, -196)], extra='<rect x="-6" y="-214" width="34" height="18" fill="#A8603A" stroke="#0D0D0F" stroke-width="1.6"></rect>'))
    o.append(robed(p, w * 0.42, b, s, "#F3EFE6", head="#F3EFE6", cord="#D7261E", belt="#E8B830", flip=True, pose="walk",
                   extra='<path d="M-22 -166 C -10 -150 10 -150 22 -166" fill="none" stroke="#E8B830" stroke-width="5"></path>'))
    return "".join(o)

def bush(w, h, seed):
    """By faith he forsook Egypt … for he endured, as seeing him who is invisible: the bush that burned and was not consumed,
    at night on the mountain of God (Exodus' drawing; God is not drawn)."""
    from exo.art import burning
    return burning(w, h, seed)

def passover(w, h, seed):
    """By faith he kept the passover, and the sprinkling of the blood, that the destroyer of the firstborn should not touch
    them: a street of the Hebrews' houses in Goshen at midnight, every door shut, lamplight under each door and in the small
    windows, the moon high — no one in the street (the blood is in the words only; the destroyer is not drawn)."""
    o = [sky(w, h, "#05051A", "#1E1650"), starfield(w, h, seed, 60, 0.4), halo(w * 0.84, h * 0.14, h * 0.12, "#FFF4C2", 0.4),
         f'<circle cx="{f(w * 0.84)}" cy="{f(h * 0.14)}" r="{f(max(8, h * 0.04))}" fill="#FFF8DC"></circle>']
    b = h * 0.86; r = random.Random(seed); x = -10
    while x < w + 10:
        bw = w * r.uniform(0.16, 0.22); bh = h * r.uniform(0.46, 0.6)
        o.append(f'<rect x="{f(x)}" y="{f(b - bh)}" width="{f(bw)}" height="{f(bh + 10)}" fill="#3A3450" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.34)}" y="{f(b - bh * 0.5)}" width="{f(bw * 0.32)}" height="{f(bh * 0.5)}" fill="#2A1A14" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.3)}" y="{f(b - bh * 0.54)}" width="{f(bw * 0.4)}" height="{f(bh * 0.05)}" fill="#4A4060" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x + bw * 0.36)}" y="{f(b - 3)}" width="{f(bw * 0.28)}" height="3" fill="#FFC14D"></rect>'
                 f'<rect x="{f(x + bw * 0.4)}" y="{f(b - bh * 0.86)}" width="{f(bw * 0.18)}" height="{f(bh * 0.12)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.4"></rect>')
        x += bw
    o.append(ground(w, h, b, "#1E1A2A", dy=0))
    return "".join(o)

def red_sea(p, w, h, seed):
    """By faith they passed through the Red sea as by dry land: the file of the people between the walls of water (Exodus'
    drawing)."""
    from exo.art4 import dry_walk
    return mk.defs(p, *ALL) + dry_walk(p, w, h, seed)

def jericho(w, h, seed):
    """By faith the walls of Jericho fell down, after they had been compassed about for seven days: the city wall fallen flat
    in a long heap of broken brick and stone, the dust still going up, the houses within standing open to the plain; seven
    marks of the days on the ground (no one drawn)."""
    o = [sky(w, h, "#8FD0E2", "#F3E0B0")]
    r = random.Random(seed)
    b = h * 0.8
    o.append(ground(w, h, h * 0.62, "#C8A06A", dy=0))
    for i in range(8):                                                        # the houses within
        x = w * (0.1 + 0.1 * i); hh = h * r.uniform(0.14, 0.22)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.62 - hh)}" width="{f(w * 0.08)}" height="{f(hh)}" fill="#E0C898" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x + w * 0.03)}" y="{f(h * 0.62 - hh * 0.5)}" width="{f(w * 0.02)}" height="{f(hh * 0.3)}" fill="#3A2A1A"></rect>')
    o.append(f'<path d="M-10 {f(b)} ' + " ".join(f'L {f(w * i / 24)} {f(b - h * r.uniform(0.08, 0.2))}' for i in range(25)) + f' L {f(w + 10)} {f(b)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8703A" stroke="{INK}" stroke-width="2.4"></path>')
    for i in range(40):
        x, y = w * r.random(), b - h * r.uniform(0, 0.14); s_ = r.uniform(6, 16)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(s_ * 1.6)}" height="{f(s_)}" fill="{r.choice(["#C8803A", "#A8603A", "#D89A5A"])}" stroke="{INK}" stroke-width="1" transform="rotate({r.uniform(-30, 30):.0f} {f(x)} {f(y)})"></rect>')
    for i in range(4):
        o.append(f'<ellipse cx="{f(w * r.uniform(0.1, 0.9))}" cy="{f(b - h * 0.22)}" rx="{f(w * 0.1)}" ry="{f(h * 0.08)}" fill="#E8D8B8" opacity="0.5"></ellipse>')
    for i in range(7):
        o.append(f'<path d="M{f(w * 0.06 + i * 14)} {f(h - 16)} l 0 -12" stroke="{INK}" stroke-width="3"></path>')
    return "".join(o)

def rahab(w, h, seed):
    """By faith Rahab the harlot perished not with them that were disobedient, having received the spies with peace: her
    window in the wall by day, the line of scarlet thread bound in it (Joshua's drawing)."""
    from jos.art import scarlet
    return scarlet(w, h, seed)

def judges(w, h):
    """Gideon, Barak, Samson, Jephthah; David and Samuel: a strip of faces as their volumes draw them — Gideon in his tan
    headcloth, Barak in slate-blue, Samson with his braided locks, Jephthah, David the king in his purple headcloth and gold
    band, Samuel old in midnight blue."""
    from jdg.common import GIDEON, BARAK, SAMSON
    from jdg.ch05 import JEPHTHAH
    from sa2.common import DAVID_KING
    from sa1.common import SAMUEL_OLD
    return strip([(GIDEON, "GIDEON"), (BARAK, "BARAK"), (SAMSON, "SAMSON"), (JEPHTHAH, "JEPHTHAH"), (DAVID_KING, "DAVID"), (SAMUEL_OLD, "SAMUEL")], w, h)

def lions_fire(p, w, h, seed):
    """Stopped the mouths of lions, quenched the power of fire: two cells — the den of lions, the lions lying still under the
    shaft of light from its mouth; and the furnace's mouth roaring with fire (Daniel's drawings, no one drawn)."""
    from dan.art import den
    from dan.art2 import furnace
    from co1.art5 import cells
    return cells(p, w, h, [lambda q, cw, hh: den(q, cw, hh, seed, daniel=False), lambda q, cw, hh: furnace(q, cw, hh, seed + 1, stage="cast")])

def caves(w, h, seed):
    """Wandering in deserts and mountains and caves, and the holes of the earth: the wilderness at evening, bare mountains,
    the dark mouths of caves in the cliff and holes in the ground, a sheepskin left on a rock — no one in any of them (the
    sufferings of 11:35–38 are told in words only)."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A1A3A", "#C8803A")]
    o.append(f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.1)} {f(h * 0.3)} L {f(w * 0.22)} {f(h * 0.4)} L {f(w * 0.34)} {f(h * 0.18)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.78)} {f(h * 0.46)} L {f(w * 0.9)} {f(h * 0.24)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A4A3A" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.74)} {f(w * 0.7)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9A7A5A" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.0, h / 300)
    for x, y, sc in ((0.18, 0.56, 1.0), (0.42, 0.62, 0.8), (0.7, 0.58, 1.1), (0.88, 0.5, 0.7)):
        o.append(f'<path d="M{f(w * x - 30 * k * sc)} {f(h * y)} C {f(w * x - 30 * k * sc)} {f(h * y - 40 * k * sc)} {f(w * x + 30 * k * sc)} {f(h * y - 40 * k * sc)} {f(w * x + 30 * k * sc)} {f(h * y)} Z" fill="#140C0A" stroke="{INK}" stroke-width="1.6"></path>')
    for x in (0.3, 0.6):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * 0.88)}" rx="{f(30 * k)}" ry="{f(8 * k)}" fill="#1A100C"></ellipse>')
    o.append(f'<ellipse cx="{f(w * 0.82)}" cy="{f(h * 0.86)}" rx="{f(28 * k)}" ry="{f(12 * k)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(w * 0.8 - 20 * k)} {f(h * 0.84 - 10 * k)} C {f(w * 0.8)} {f(h * 0.84 - 18 * k)} {f(w * 0.84)} {f(h * 0.84 - 16 * k)} {f(w * 0.84 + 16 * k)} {f(h * 0.84 - 8 * k)} L {f(w * 0.84 + 10 * k)} {f(h * 0.84 + 2 * k)} L {f(w * 0.8 - 16 * k)} {f(h * 0.84 + 2 * k)} Z" fill="#E8DCC0" stroke="{INK}" stroke-width="1.4"></path>')
    return "".join(o)

def witnesses(p, w, h, seed):
    """These all, having had witness borne to them through their faith, received not the promise, God having provided some
    better thing concerning us: a great company of the faithful standing on a long ridge against the evening sky, men and
    women in their robes and headcloths, seen small and dark, the first stars over them."""
    b = h * 0.86
    o = [defs_up(p), sky(w, h, "#14123A", "#E8A06A"), starfield(w, h, seed, 40, 0.4)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(b)} C {f(w * 0.3)} {f(b - h * 0.06)} {f(w * 0.7)} {f(b - h * 0.04)} {f(w + 10)} {f(b - h * 0.08)} L {f(w + 10)} {f(h + 10)} Z" fill="#1A1424" stroke="{INK}" stroke-width="2"></path>')
    s = h * 0.24 / 205
    r = random.Random(seed)
    for i in range(22):
        x = w * (0.02 + 0.045 * i) + r.uniform(-4, 4); yb = b - (h * 0.06) * (x / w) + 2
        o.append(brother_fig(p, x, yb, s * r.uniform(0.9, 1.05), i, flip=r.random() < 0.5).replace('stroke="#0D0D0F"', 'stroke="#0D0D0F"'))
    o.append(f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#14123A" opacity="0.35"></rect>')
    return "".join(o)

# ---- Hebrews 12 -----------------------------------------------------------------------------------------------------------
def race(p, w, h, seed):
    """Let us run with patience the race that is set before us, looking unto Jesus: the stadium at the games, its banks of
    spectators (the cloud of witnesses), the runners stretched out down the track toward the post (1 Corinthians' drawing)."""
    from co1.art3 import race as r_
    return r_(p, w, h, seed)

def empty_track(w, h, seed):
    """Ye have not yet resisted unto blood, striving against sin: the stadium at evening, the stands empty, the track bare and
    raked, the turning-post standing alone (words only)."""
    o = [sky(w, h, "#2A1A3A", "#E8A06A")]
    sy_ = h * 0.5
    o.append(f'<path d="M-10 {f(sy_)} C {f(w * 0.3)} {f(sy_ - h * 0.16)} {f(w * 0.7)} {f(sy_ - h * 0.16)} {f(w + 10)} {f(sy_)} L {f(w + 10)} {f(h * 0.62)} L -10 {f(h * 0.62)} Z" fill="#6A5A4A" stroke="{INK}" stroke-width="2"></path>')
    for k in range(5):
        y = sy_ - h * 0.12 + k * h * 0.03
        o.append(f'<path d="M-10 {f(y + h * 0.12 - k * h * 0.012)} C {f(w * 0.3)} {f(y)} {f(w * 0.7)} {f(y)} {f(w + 10)} {f(y + h * 0.12 - k * h * 0.012)}" fill="none" stroke="#4A3A2E" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#D8B880" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(4):
        y = h * (0.68 + 0.08 * k)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#F3EFE6" stroke-width="2" opacity="0.7"></path>')
    o.append(f'<rect x="{f(w * 0.84)}" y="{f(h * 0.44)}" width="{f(8)}" height="{f(h * 0.5)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def household(p, w, h, seed):
    """My son, regard not lightly the chastening of the Lord … what son is there whom his father chasteneth not?: the
    courtyard of a house by day, a man and his wife at the door with their two children (1 Corinthians' drawing; no blow
    drawn)."""
    from co1.art2 import household as hh
    return hh(p, w, h, seed)

def fruit_vines(w, h, seed):
    """Afterward it yieldeth peaceable fruit unto them that have been exercised thereby, even the fruit of righteousness: a
    vineyard on the hillside, the vines pruned and heavy with fruit, under the sun."""
    return vista(w, h, seed, tone="day", horizon=0.48, sun_at=(0.82, 0.18), hills_n=2, field="vines", birds_=2)

def burdens(p, w, h, seed):
    """Lift up the hands that hang down, and the palsied knees; and make straight paths for your feet: on the road, a heavy
    bundle carried between two, and one lifting the sack from the back of a man bowed under it (Galatians' drawing)."""
    from gal.art import burdens as b_
    return b_(p, w, h, seed)

def bitter_root(w, h, seed):
    """Lest any root of bitterness springing up trouble you, and thereby the many be defiled: a field of young grain cut away
    in section, and under it the dark root of a bitter weed spreading through the soil among the roots of the grain, its
    thorny shoot breaking up into the field."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3E8C8")]
    gy = h * 0.42
    o.append(f'<rect x="-10" y="{f(gy)}" width="{f(w + 20)}" height="{f(h - gy + 10)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>')
    for k in range(3):
        o.append(f'<path d="M-10 {f(gy + h * (0.14 + 0.14 * k))} C {f(w * 0.3)} {f(gy + h * (0.12 + 0.14 * k))} {f(w * 0.6)} {f(gy + h * (0.16 + 0.14 * k))} {f(w + 10)} {f(gy + h * (0.14 + 0.14 * k))}" fill="none" stroke="#4A2E1A" stroke-width="1.6"></path>')
    o.append(grain(-10, w + 10, gy, h * 0.24, seed, color="#9CCB5E"))
    for i in range(14):                                                       # the grain's roots
        x = w * (0.04 + 0.07 * i)
        o.append(f'<path d="M{f(x)} {f(gy)} l -6 {f(h * 0.1)} M{f(x)} {f(gy)} l 4 {f(h * 0.12)} M{f(x)} {f(gy)} l 0 {f(h * 0.14)}" stroke="#C8A878" stroke-width="1.2" fill="none"></path>')
    rx = w * 0.56                                                             # the bitter root
    o.append(f'<path d="M{f(rx)} {f(gy - h * 0.2)} L {f(rx - 8)} {f(gy - h * 0.1)} L {f(rx + 6)} {f(gy - h * 0.06)} L {f(rx)} {f(gy)}" stroke="#2A1A10" stroke-width="4" fill="none"></path>'
             + "".join(f'<path d="M{f(rx + (i % 2 * 2 - 1) * 3)} {f(gy - h * 0.04 * i)} l {f((i % 2 * 2 - 1) * 12)} -6" stroke="#2A1A10" stroke-width="2"></path>' for i in range(1, 5)))
    for i in range(9):
        a = math.radians(r.uniform(10, 170)); L = h * r.uniform(0.2, 0.5)
        x2, y2 = rx + math.cos(a) * L * 1.6, gy + math.sin(a) * L
        o.append(f'<path d="M{f(rx)} {f(gy)} C {f(rx + (x2 - rx) * 0.3)} {f(gy + (y2 - gy) * 0.6)} {f(rx + (x2 - rx) * 0.7)} {f(y2 - 10)} {f(x2)} {f(y2)}" stroke="#1A100A" stroke-width="{f(r.uniform(2.4, 4.4))}" fill="none"></path>')
    o.append(plate_label(rx, h - 12, "A ROOT OF BITTERNESS SPRINGING UP", "#FFD08A", 10, halo_="#3A2214"))
    return "".join(o)

def esau(w, h):
    """Esau, who for one mess of meat sold his own birthright … he found no place for a change of mind in his father, though he
    sought it diligently with tears: two cells — the pot of red pottage on the fire in the tent (Genesis' drawing), and Esau's
    face, his red curls and stubble, weeping (Genesis)."""
    from genesis.art7 import pottage, ESAU_CRY
    cw = w / 2
    return (f'<defs><clipPath id="esc"><rect x="0" y="0" width="{f(cw)}" height="{f(h)}"></rect></clipPath></defs><g clip-path="url(#esc)">' + pottage(cw, h, 1612) + '</g>'
            + face_cell(ESAU_CRY, cw, 0, cw, h, "esf", light="#C8A0A0", ground=("#2A1A1A", "#7A4A3A"), name="ESAU · WITH TEARS")
            + f'<path d="M{f(cw)} -10 L {f(cw)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')

def sinai(p, w, h, seed):
    """Ye are not come unto a mount that might be touched, and that burned with fire, and unto blackness, and darkness, and
    tempest, and the sound of a trumpet: mount Sinai burning with fire in the black cloud, the lightning, and the camp of the
    tents below it kept back by the bounds (Exodus' drawing, under a dark sky)."""
    from exo.art6 import camp_before
    return sky(w, h, "#05050E", "#3A1A1A") + mk.defs(p, *ALL) + camp_before(p, w, h, seed, fire=True, bounds=True)

def zion(p, w, h, seed):
    """But ye are come unto mount Zion, and unto the city of the living God, the heavenly Jerusalem, and to innumerable hosts of
    angels, to the general assembly and church of the firstborn: the city of light standing on the clouds, its walls and gates
    and towers of white and gold, and the hosts of angels — figures of white light with gold rims, no faces — row upon row on
    the clouds before it."""
    o = [defs_up(p), sky(w, h, "#3A2A6A", "#FFF0D0"), rays(w * 0.5, h * 0.3, 44, 0, max(w, h), "#FFF4C2", 0.25, 4), glow(w * 0.5, h * 0.3, h * 0.6, "#FFFFFF", 0.8, f"{p}z")]
    k = min(1.0, h / 320)
    cx, cb = w * 0.5, h * 0.56
    o.append(city_of_light(cx, cb, w * 0.8, h * 0.26, k))
    o.append(cloud_bank(w, cb, seed, "#FFFDF4", 0.9, k=k))
    b = h * 0.97
    for row, (y0, sc, n) in enumerate(((h * 0.74, 0.5, 9), (h * 0.86, 0.68, 7), (b, 0.86, 6))):
        s = (h * 0.42 / 205) * sc
        for i in range(n):
            x = w * ((i + 0.5 + (row % 2) * 0.3) / n)
            o.append(angel_fig(p, x, y0, s, flip=i % 2 == 0, up=[(-22, -158), (-34, -190), (-40, -222)] if (i + row) % 3 == 0 else None))
    return "".join(o)

def shaken(w, h, seed):
    """Whose voice then shook the earth: but now he hath promised, saying, Yet once more will I make to tremble not the earth
    only, but also the heaven: the hills and the sky shaken — the land cracked open, rocks falling, the stars thrown out of
    their places, the horizon doubled with the trembling (no figure)."""
    r = random.Random(seed)
    o = [sky(w, h, "#14123A", "#5A3A6A")]
    for i in range(60):
        x, y = r.uniform(0, w), r.uniform(0, h * 0.5); L = r.uniform(4, 14)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(L)} {f(L * 0.5)}" stroke="#F3EFE6" stroke-width="1.4" opacity="0.7"></path><circle cx="{f(x + L)}" cy="{f(y + L * 0.5)}" r="1.6" fill="#FFF4C2"></circle>')
    for dy, op in ((0, 1), (-8, 0.35), (8, 0.35)):
        o.append(f'<path d="M-10 {f(h * 0.6 + dy)} L {f(w * 0.14)} {f(h * 0.44 + dy)} L {f(w * 0.3)} {f(h * 0.56 + dy)} L {f(w * 0.46)} {f(h * 0.4 + dy)} L {f(w * 0.64)} {f(h * 0.58 + dy)} L {f(w * 0.8)} {f(h * 0.42 + dy)} L {f(w + 10)} {f(h * 0.56 + dy)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2A3A" opacity="{op}" stroke="{INK}" stroke-width="2"></path>')
    for i in range(3):
        x = w * (0.2 + 0.3 * i)
        o.append(f'<path d="M{f(x)} {f(h * 0.62)} L {f(x + 12)} {f(h * 0.72)} L {f(x - 8)} {f(h * 0.8)} L {f(x + 16)} {f(h * 0.92)} L {f(x + 4)} {f(h + 10)}" fill="none" stroke="#FF8A3D" stroke-width="3"></path>')
    for i in range(10):
        x, y = w * r.random(), h * r.uniform(0.5, 0.9); s_ = r.uniform(6, 14)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(s_)}" height="{f(s_ * 0.8)}" fill="#6A5A5A" stroke="{INK}" stroke-width="1" transform="rotate({r.uniform(0, 90):.0f} {f(x)} {f(y)})"></rect>')
    for i in range(4):
        y = h * (0.1 + 0.1 * i)
        o.append(f'<path d="M{f(w * 0.02)} {f(y)} q 8 -6 16 0 t 16 0" fill="none" stroke="#C8B8E8" stroke-width="2" opacity="0.6"></path><path d="M{f(w * 0.94)} {f(y)} q 8 -6 16 0 t 16 0" fill="none" stroke="#C8B8E8" stroke-width="2" opacity="0.6"></path>')
    return "".join(o)

def pillar_fire(p, w, h, seed):
    """Receiving a kingdom that cannot be shaken … for our God is a consuming fire: the camp at night, the tents dark round the
    tabernacle, and over the tabernacle the pillar of fire standing up into the sky (God is not drawn: the fire only)."""
    r = random.Random(seed)
    o = [sky(w, h, "#05050E", "#2A0A0A"), starfield(w, h, seed, 30, 0.3)]
    k = min(w / 900, h / 330)
    cx = w * 0.5
    o.append(halo(cx, h * 0.4, h * 0.7, "#FF6A2A", 0.4))
    for i in range(7):
        x = cx + (i - 3) * 16 * k * 3;
    o.append(f'<path d="M{f(cx - 50 * k)} {f(h * 0.76)} C {f(cx - 80 * k)} {f(h * 0.4)} {f(cx - 30 * k)} {f(h * 0.2)} {f(cx - 40 * k)} -10 L {f(cx + 40 * k)} -10 C {f(cx + 30 * k)} {f(h * 0.2)} {f(cx + 80 * k)} {f(h * 0.4)} {f(cx + 50 * k)} {f(h * 0.76)} Z" fill="#FF6A2A" opacity="0.9"></path>'
             f'<path d="M{f(cx - 30 * k)} {f(h * 0.74)} C {f(cx - 50 * k)} {f(h * 0.4)} {f(cx - 10 * k)} {f(h * 0.2)} {f(cx - 20 * k)} -10 L {f(cx + 20 * k)} -10 C {f(cx + 10 * k)} {f(h * 0.2)} {f(cx + 50 * k)} {f(h * 0.4)} {f(cx + 30 * k)} {f(h * 0.74)} Z" fill="#FFC14D"></path>'
             f'<path d="M{f(cx - 10 * k)} {f(h * 0.72)} C {f(cx - 20 * k)} {f(h * 0.4)} {f(cx)} {f(h * 0.2)} {f(cx - 6 * k)} -10 L {f(cx + 6 * k)} -10 C {f(cx)} {f(h * 0.2)} {f(cx + 20 * k)} {f(h * 0.4)} {f(cx + 10 * k)} {f(h * 0.72)} Z" fill="#FFF4C2"></path>')
    o.append(ground(w, h, h * 0.8, "#1A0E0E", dy=0))
    o.append(tent_plan(cx, h * 0.84, k, color="#0D0D0F", fill="#3A2A2A", sw=2))
    for i in range(12):
        x = w * (0.04 + 0.08 * i); y = h * (0.92 + 0.03 * (i % 2)); kk = min(1.0, h / 400)
        if abs(x - cx) < w * 0.3: continue
        o.append(f'<path d="M{f(x - 26 * kk)} {f(y)} L {f(x - 12 * kk)} {f(y - 24 * kk)} L {f(x + 16 * kk)} {f(y - 26 * kk)} L {f(x + 28 * kk)} {f(y)} Z" fill="#140A0A" stroke="#3A2020" stroke-width="1.4"></path>')
    return "".join(o)

# ---- Hebrews 13 -----------------------------------------------------------------------------------------------------------
def mamre(p, w, h, seed):
    """Forget not to show love unto strangers: for thereby some have entertained angels unawares: the oaks of Mamre in the heat
    of the day, three men in white standing under the great oak — figures of white light with gold rims, no faces — Abraham
    before them with his hand out in welcome, Sarah at the door of the tent behind."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#8FD0E2", "#FFF0C0"), ground(w, h, h * 0.66, "#C8B878", dy=0)]
    k = min(1.0, h / 300)
    ox = w * 0.62                                                             # the oak
    o.append(f'<path d="M{f(ox - 14 * k)} {f(b)} C {f(ox - 10 * k)} {f(h * 0.6)} {f(ox - 20 * k)} {f(h * 0.4)} {f(ox - 6 * k)} {f(h * 0.3)} L {f(ox + 10 * k)} {f(h * 0.3)} C {f(ox + 18 * k)} {f(h * 0.5)} {f(ox + 12 * k)} {f(h * 0.7)} {f(ox + 18 * k)} {f(b)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>')
    for dx, dy, rr in ((-120, 0.2, 70), (-40, 0.1, 80), (60, 0.14, 76), (130, 0.24, 60), (0, 0.26, 70)):
        o.append(f'<circle cx="{f(ox + dx * k)}" cy="{f(h * dy)}" r="{f(rr * k)}" fill="#3A6A3A" stroke="{INK}" stroke-width="2"></circle>')
    o.append(black_tent(w * 0.14, b - 10 * k, 200 * k, 100 * k, lit=False))
    s = fit(b, max(h * 0.25, b - 220))
    o.append(sarah_old(p, w * 0.2, b - 8 * k, s * 0.86, flip=True))
    o.append(abraham(p, w * 0.38, b, s, flip=True, up=[(-22, -158), (-48, -146), (-70, -140)]))
    for i, x in enumerate((0.56, 0.68, 0.8)):
        o.append(angel_fig(p, w * x, b - (i % 2) * 4 * k, s))
    return "".join(o)

def shut_door(w, h, seed):
    """Remember them that are in bonds … let marriage be had in honor among all, and let the bed be undefiled: a house door on
    a quiet street, shut (1 Corinthians' drawing; words only)."""
    from co1.art2 import house_door
    return house_door(w, h, seed)

def content(w, h, seed):
    """Be ye free from the love of money; content with such things as ye have: on a plain table by the window in the morning, a
    loaf and a cup, a lamp, and the purse tied shut and pushed aside; the light falling on the bread."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3424"></rect>']
    k = min(w / 600, h / 260)
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.08)}" width="{f(w * 0.26)}" height="{f(h * 0.4)}" fill="#FFE6A0" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(w * 0.73)} {f(h * 0.08)} L {f(w * 0.73)} {f(h * 0.48)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.48)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.7)} {f(h * 0.7)} L {f(w * 0.86)} {f(h * 0.48)} Z" fill="#FFE6A0" opacity="0.25"></path>')
    b = h * 0.7
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(16 * k)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="-10" y="{f(b + 16 * k)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2818"></rect>')
    o.append(f'<ellipse cx="{f(w * 0.44)}" cy="{f(b - 16 * k)}" rx="{f(46 * k)}" ry="{f(20 * k)}" fill="#D9A25A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.42)} {f(b - 30 * k)} l {f(14 * k)} {f(10 * k)} M{f(w * 0.46)} {f(b - 32 * k)} l {f(14 * k)} {f(10 * k)}" stroke="#A8743A" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.6 - 16 * k)} {f(b)} L {f(w * 0.6 - 20 * k)} {f(b - 50 * k)} L {f(w * 0.6 + 20 * k)} {f(b - 50 * k)} L {f(w * 0.6 + 16 * k)} {f(b)} Z" fill="#9A5A3A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.12 - 24 * k)} {f(b)} C {f(w * 0.12 - 30 * k)} {f(b - 30 * k)} {f(w * 0.12 + 30 * k)} {f(b - 30 * k)} {f(w * 0.12 + 24 * k)} {f(b)} Z" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.12 - 8 * k)} {f(b - 24 * k)} L {f(w * 0.12 + 8 * k)} {f(b - 24 * k)}" stroke="#C8A060" stroke-width="{f(4 * k)}"></path>'
             f'<path d="M{f(w * 0.26 - 18 * k)} {f(b)} L {f(w * 0.26 - 6 * k)} {f(b - 18 * k)} L {f(w * 0.26 + 6 * k)} {f(b - 18 * k)} L {f(w * 0.26 + 18 * k)} {f(b)} Z" fill="#A86A3A" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.26 + 10 * k)} {f(b - 20 * k)} c -3 -8 1 -14 1 -18 c 3 6 5 12 -1 18 Z" fill="#FFE680"></path>')
    return "".join(o)

def always(w, h, seed):
    """Jesus Christ is the same yesterday and to-day, yea and for ever: one horizon running across three skies — the night of
    yesterday at the left with its stars, the day of to-day in the middle with the sun, and at the right the gold light of for
    ever — the land under them unbroken."""
    o = [f'<defs><linearGradient id="alw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B0B2A"></stop><stop offset="0.3" stop-color="#2A2A6A"></stop>'
         f'<stop offset="0.42" stop-color="#8FD0E2"></stop><stop offset="0.62" stop-color="#BFE4EE"></stop><stop offset="0.74" stop-color="#FFE6A0"></stop><stop offset="1" stop-color="#FFF8DC"></stop></linearGradient></defs>'
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#alw)"></rect>']
    r = random.Random(seed)
    o += [f'<circle cx="{f(r.uniform(0, w * 0.3))}" cy="{f(r.uniform(0, h * 0.6))}" r="{f(r.uniform(0.8, 2))}" fill="#F3EFE6"></circle>' for _ in range(40)]
    o.append(halo(w * 0.52, h * 0.3, h * 0.2, "#FFFFFF", 0.6) + f'<circle cx="{f(w * 0.52)}" cy="{f(h * 0.3)}" r="{f(h * 0.07)}" fill="#FFF4C2"></circle>')
    o.append(glow(w * 0.92, h * 0.4, h * 0.6, "#FFFFFF", 0.8, "alg") + rays(w * 0.92, h * 0.4, 30, h * 0.1, max(w, h) * 0.6, "#FFE680", 0.3, 3))
    o.append(hills(w, h, h * 0.72, seed, color="#3A4A3A", amp=10, step=90) + ground(w, h, h * 0.8, "#2A3A2A", dy=0))
    for x, t_ in ((w * 0.16, "YESTERDAY"), (w * 0.52, "TO-DAY"), (w * 0.8, "FOR EVER")):
        o.append(plate_label(x, h * 0.62, t_, GOLD, 11, halo_="#1A2A1A"))
    return "".join(o)

def without_camp(w, h, seed):
    """We have an altar … the bodies of those beasts whose blood is brought into the holy place by the high priest as an offering
    for sin, are burned without the camp: the camp of the tents round the tabernacle in the evening, and far outside it on the
    bare plain a fire with its smoke going up (no beast drawn)."""
    o = [sky(w, h, "#2A1A3A", "#E8A06A"), hills(w, h, h * 0.56, seed, color="#4A3A3A", amp=10, step=90), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    k = min(w / 900, h / 330)
    o.append(tent_plan(w * 0.34, h * 0.86, k, color="#0D0D0F", fill="#E8D8B0", sw=1.6))
    for i in range(14):
        x = w * (0.02 + 0.045 * i); y = h * (0.94 + 0.02 * (i % 2)); kk = min(1.0, h / 420)
        if abs(x - w * 0.34) < w * 0.22: continue
        o.append(f'<path d="M{f(x - 22 * kk)} {f(y)} L {f(x - 10 * kk)} {f(y - 20 * kk)} L {f(x + 12 * kk)} {f(y - 22 * kk)} L {f(x + 24 * kk)} {f(y)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="1.2"></path>')
    fx = w * 0.86                                                             # the fire without the camp
    o.append(f'<path d="M{f(fx)} {f(h * 0.7)} C {f(fx - 30)} {f(h * 0.5)} {f(fx + 30)} {f(h * 0.3)} {f(fx - 10)} -10" fill="none" stroke="#8A8090" stroke-width="{f(24 * k + 6)}" opacity="0.55" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(fx + (i - 2) * 9 - 7)} {f(h * 0.72)} C {f(fx + (i - 2) * 9 - 7)} {f(h * 0.66)} {f(fx + (i - 2) * 9)} {f(h * 0.64)} {f(fx + (i - 2) * 9)} {f(h * 0.6)} C {f(fx + (i - 2) * 9 + 3)} {f(h * 0.66)} {f(fx + (i - 2) * 9 + 7)} {f(h * 0.68)} {f(fx + (i - 2) * 9 + 7)} {f(h * 0.72)} Z" fill="{["#FF6A2A", "#FFC14D", "#FFE680"][i % 3]}"></path>' for i in range(5)))
    o.append(plate_label(fx, h * 0.8, "WITHOUT THE CAMP", "#FFE6A0", 9, halo_="#4A3020"))
    return "".join(o)

def without_gate(p, w, h, seed):
    """Wherefore Jesus also, that he might sanctify the people through his own blood, suffered without the gate. Let us
    therefore go forth unto him without the camp, bearing his reproach: the wall of the city and its gate standing open at the
    left, the road going out of it across the rocky ground to a bare hill far off, three crosses small on its top against a
    darkened sky (no nearer)."""
    o = [f'<defs><linearGradient id="{p}sk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5A4A5A"></stop><stop offset="1" stop-color="#1A1018"></stop></linearGradient></defs>'
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sk)"></rect>']
    k = min(1.0, h / 300)
    gx = w * 0.84                                                             # the far hill and the crosses
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.7)} C {f(w * 0.72)} {f(h * 0.56)} {f(w * 0.9)} {f(h * 0.52)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.76)} L {f(w * 0.6)} {f(h * 0.76)} Z" fill="#2A1E24" stroke="{INK}" stroke-width="2"></path>')
    for i, x in enumerate((gx - 22 * k, gx, gx + 22 * k)):
        top = h * 0.54 - (12 * k if i == 1 else 6 * k); bot = h * 0.56
        o.append(f'<path d="M{f(x)} {f(bot)} L {f(x)} {f(top - 20 * k)} M{f(x - 8 * k)} {f(top - 12 * k)} L {f(x + 8 * k)} {f(top - 12 * k)}" stroke="#0D0D0F" stroke-width="{f(3 * k)}"></path>')
    o.append(ground(w, h, h * 0.72, "#5A4A44", dy=0))
    o.append(f'<path d="M{f(w * 0.28)} {f(h * 0.94)} C {f(w * 0.46)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.78)} {f(w * 0.76)} {f(h * 0.72)} L {f(w * 0.78)} {f(h * 0.72)} C {f(w * 0.64)} {f(h * 0.8)} {f(w * 0.52)} {f(h * 0.9)} {f(w * 0.38)} {f(h + 10)} L {f(w * 0.26)} {f(h + 10)} Z" fill="#8A7A6A"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w * 0.34)}" height="{f(h * 0.84)}" fill="#A8987A" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(-10 + i * 30 * k)}" y="{f(h * 0.12)}" width="{f(18 * k)}" height="{f(h * 0.05)}" fill="#A8987A" stroke="{INK}" stroke-width="1.6"></rect>' for i in range(int(w * 0.34 / (30 * k)) + 1))
             + f'<path d="M{f(w * 0.14)} {f(h + 10)} L {f(w * 0.14)} {f(h * 0.5)} A {f(w * 0.07)} {f(w * 0.07)} 0 0 1 {f(w * 0.28)} {f(h * 0.5)} L {f(w * 0.28)} {f(h + 10)} Z" fill="#2A1E18" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(plate_label(w * 0.21, h * 0.08, "THE GATE", "#F3EFE6", 10, halo_="#3A2A2A"))
    return "".join(o)

def praise(p, w, h, seed):
    """Let us offer up a sacrifice of praise to God continually, that is, the fruit of lips which make confession to his name:
    a company seen from behind on a hill at sunrise, men and women in overlapping rows, many with an arm lifted (Romans'
    drawing)."""
    from rom.art5 import nations_praise
    return nations_praise(p, w, h, seed)

def watch(p, w, h, seed):
    """They watch in behalf of your souls, as they that shall give account: shepherds keeping watch by night over their flock in
    the field, the fire burning low (Luke's drawing, no angel)."""
    from luk.art import field_night
    return mk.defs(p, *ALL) + field_night(p, w, h, seed)

def timothy_free(p, w, h, seed):
    """Know ye that our brother Timothy hath been set at liberty; with whom, if he come shortly, I will see you: the prison's
    iron-bound door standing open in its stone wall in the morning, and Timothy (young, beardless, his grey-blue tunic, as Acts
    draws him) walking out of it into the light with his staff, the street beyond."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#8FD0E2", "#FFF0D0"), halo(w * 0.9, h * 0.2, h * 0.4, "#FFF4C2", 0.6)]
    k = min(1.0, h / 300)
    o.append(f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w * 0.46)}" height="{f(b - h * 0.1)}" fill="#8A8278" stroke="{INK}" stroke-width="2.4"></rect>')
    r = random.Random(seed)
    for row in range(10):
        y = h * 0.1 + row * (b - h * 0.1) / 10
        o.append(f'<path d="M-10 {f(y)} L {f(w * 0.36)} {f(y)}" stroke="#6A625A" stroke-width="1.4"></path>')
        for j in range(5):
            x = (j + (row % 2) * 0.5) * w * 0.09
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + (b - h * 0.1) / 10)}" stroke="#6A625A" stroke-width="1.4"></path>')
    dx, dw = w * 0.16, w * 0.13
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.36)}" width="{f(dw)}" height="{f(b - h * 0.36)}" fill="#14100E" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(dx + dw)} {f(h * 0.36)} L {f(dx + dw + w * 0.08)} {f(h * 0.4)} L {f(dx + dw + w * 0.08)} {f(b + 4)} L {f(dx + dw)} {f(b)} Z" fill="#4A3A2E" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(dx + dw)} {f(y)} L {f(dx + dw + w * 0.08)} {f(y + h * 0.02)}" stroke="#2A2A2A" stroke-width="{f(5 * k)}"></path>' for y in (h * 0.46, h * 0.66, h * 0.86)))
    o.append(ground(w, h, b, "#C8B898", dy=0) + f'<path d="M{f(w * 0.3)} {f(b)} L {f(w + 10)} {f(b)}" stroke="#A89878" stroke-width="2"></path>')
    s = fit(b, max(h * 0.25, b - 220))
    staff = '<path d="M30 -150 L 44 4" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, w * 0.56, b, s, "#7A8A9A", hair="#3A2214", belt="#3A4A5A", flip=True, pose="walk", extra=staff))          # Timothy, in Acts' colours
    return "".join(o)

def italy(p, w, h, seed):
    """Salute all them that have the rule over you, and all the saints. They of Italy salute you. Grace be with you all: a
    harbour of Italy in the morning — the quay with its arches and a Roman warehouse, a merchant ship making sail, and on the
    quay the brethren of Italy, men and women, lifting their hands in greeting after it."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#8FD0E2", "#FFF0D0"), halo(w * 0.84, h * 0.24, h * 0.3, "#FFF4C2", 0.6)]
    k = min(1.0, h / 300)
    sy_ = h * 0.56
    o.append(f'<rect x="-10" y="{f(sy_)}" width="{f(w + 20)}" height="{f(h - sy_ + 10)}" fill="#1F6F9A"></rect>')
    r = random.Random(seed)
    o += [f'<path d="M{f(r.uniform(w * 0.4, w))} {f(r.uniform(sy_, h))} l {f(r.uniform(10, 26))} 0" stroke="#5AA0C8" stroke-width="1.4"></path>' for _ in range(24)]
    from act.art15 import grain_ship
    o.append(grain_ship(p, w * 0.74, sy_ + h * 0.12, min(0.62, h / 480)))
    qx = w * 0.5                                                              # the quay and the warehouse
    o.append(f'<rect x="-10" y="{f(h * 0.7)}" width="{f(qx + 10)}" height="{f(h * 0.32)}" fill="#C8B898" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(x)} {f(h + 10)} L {f(x)} {f(h * 0.84)} A {f(14 * k)} {f(14 * k)} 0 0 1 {f(x + 28 * k)} {f(h * 0.84)} L {f(x + 28 * k)} {f(h + 10)} Z" fill="#1A3A4A" stroke="{INK}" stroke-width="1.4"></path>' for x in (w * 0.06, w * 0.2, w * 0.34)))
    o.append(f'<rect x="{f(w * 0.02)}" y="{f(h * 0.26)}" width="{f(w * 0.3)}" height="{f(h * 0.44)}" fill="#D8A878" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.0)} {f(h * 0.26)} L {f(w * 0.17)} {f(h * 0.16)} L {f(w * 0.34)} {f(h * 0.26)} Z" fill="#B8583A" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(x)} {f(h * 0.7)} L {f(x)} {f(h * 0.5)} A {f(12 * k)} {f(12 * k)} 0 0 1 {f(x + 24 * k)} {f(h * 0.5)} L {f(x + 24 * k)} {f(h * 0.7)} Z" fill="#5A3A2A" stroke="{INK}" stroke-width="1.4"></path>' for x in (w * 0.06, w * 0.15, w * 0.24)))
    s = (h * 0.34) / 205
    for i, x in enumerate((0.1, 0.2, 0.3, 0.42)):
        o.append(brother_fig(p, w * x, h * 0.72, s, i + 2, up=[(-22, -158), (-14, -190), (-6, -214)] if i % 2 == 0 else None, flip=False))
    o.append(plate_label(w * 0.17, h * 0.1, "ITALY", "#3A2A1A", 11, halo_="#FFF0D0"))
    return "".join(o)
