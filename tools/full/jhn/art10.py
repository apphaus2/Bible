"""Drawings for John 20–21. The garden tomb while it was yet dark, the stone taken away and Mary Magdalene before it; Peter
and the other disciple running, the other disciple ahead; within the tomb the linen cloths lying on the shelf and the
napkin rolled up in a place by itself, no one there; the two angels in white sitting one at the head and one at the feet
where the body had lain — figures of white light with a gold rim, no face; Mary weeping at the door; Jesus risen in white
light standing in the garden among the trees, and Mary turning to him — Rabboni; the disciples behind the shut and barred
doors, and Jesus risen standing in the midst (no wound drawn: his hands open in the light); Thomas kneeling. John 21: the
boat on the sea of Tiberias by night with its empty net; daybreak, Jesus on the beach; the net on the right side full of
fishes; Peter in the sea swimming to land; the fire of coals with fish laid on it and bread, the net drawn up with its
hundred and fifty and three; breaking their fast about the fire; Jesus and Peter walking by the water — lovest thou me?;
the beloved disciple following; and the books the world itself would not contain. Built on jhn.art9."""
from jhn.art9 import *
from jhn.art9 import f, INK, HEB, TWELVE, P, _loaf, LIE
import random, math
from mrk.art9 import light_seated, mourners

MAG_C, MAG_VEIL = ROBES["magdalene"], "#C2456A"

def magdalene_fig(p, x, y, s, flip=False, up=None):
    return woman_fig(p, x, y, s, MAG_C, MAG_VEIL, flip=flip, up=up)

def garden_tomb(w, h, b, seed, tone="dark", open_=True):
    """The garden and the new tomb hewn in the rock; the round stone taken away and lying aside."""
    top, bot = {"dark": ("#0B0B2A", "#3A3A6A"), "dawn": ("#3A3A7A", "#FFC890"), "day": ("#8FD0E2", "#FFF4C2")}[tone]
    o = [sky(w, h, top, bot)]
    if tone == "dark": o.append(mk.stars(30, w, h * 0.3, seed))
    o += [f'<path d="M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.44)} {f(h * 0.24)} C {f(w * 0.6)} {f(h * 0.14)} {f(w * 0.84)} {f(h * 0.16)} {f(w + 10)} {f(h * 0.24)} L {f(w + 10)} {f(h + 10)} Z" fill="{"#5A5260" if tone == "dark" else "#8A7A6A"}" stroke="{INK}" stroke-width="2.4"></path>',
          f'<path d="M{f(w * 0.56)} {f(b - h * 0.04)} L {f(w * 0.56)} {f(h * 0.5)} Q {f(w * 0.64)} {f(h * 0.4)} {f(w * 0.72)} {f(h * 0.5)} L {f(w * 0.72)} {f(b - h * 0.04)} Z" fill="#14100E" stroke="{INK}" stroke-width="2"></path>',
          ground(w, h, b - h * 0.04, "#2E3A2A" if tone == "dark" else "#5A6A3A", dy=0)]
    cx, cy, r = w * 0.88, b - h * 0.04 - h * 0.15, h * 0.15
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{"#6A6470" if tone == "dark" else "#A89A8A"}" stroke="{INK}" stroke-width="2.6"></circle>')
    for i, x in enumerate((0.06, 0.24)):
        o.append(olive(w * x, b, h / 380, seed=seed + i).replace("#7A8A5A", "#3A4A3A" if tone == "dark" else "#7A8A5A"))
    return "".join(o)

def tomb_morning(p, w, h, seed, stage="mary"):
    """mary: while it was yet dark, Mary Magdalene come to the tomb and standing before it, seeing the stone taken away.
    run: at first light Peter and the other disciple running along the garden path to the tomb, the other disciple ahead.
    weep: Mary standing without at the tomb weeping, stooping toward the door. gardener: in the garden at sunrise, Jesus
    risen standing among the trees in white light, and Mary turned to him, her arms held out."""
    b = h * 0.94
    tone = {"mary": "dark", "run": "dawn", "weep": "dawn", "gardener": "day"}[stage]
    o = [mk.defs(p, *ALL), garden_tomb(w, h, b, seed, tone=tone)]
    s = fit(b, max(h * 0.28, b - 230))
    if stage == "mary":
        o.append(magdalene_fig(p, w * 0.42, b, s, up=UP_BLESS))
    elif stage == "run":
        up_run = [(-22, -158), (-40, -140), (-54, -150)]
        o.append(disciple(p, w * 0.4, b, s, "john", flip=True, up=up_run) + disciple(p, w * 0.2, b - 4, s * 0.98, "peter", flip=True, up=up_run))
    elif stage == "weep":
        o.append(woman_fig(p, w * 0.48, b, s, MAG_C, MAG_VEIL, flip=True, up=[(-22, -158), (-26, -176), (-14, -186)]))
    elif stage == "gardener":
        o.append(jesus_risen(p, w * 0.22, b, s))
        o.append(magdalene_fig(p, w * 0.46, b, s * 0.96, up=UP_BLESS))
    return "".join(o)

def inside_tomb(p, w, h, seed, angels=False, look=False):
    """Within the tomb: the stone shelf cut in the rock, the linen cloths lying on it, and the napkin that was upon his head
    not lying with them but rolled up in a place by itself at the end; the morning light in the low doorway. angels=True:
    two angels in white sitting, one at the head and one at the feet where the body had lain — white light, a gold rim, no
    face; look=True: the other disciple stooping at the doorway, looking in."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A2220"),
         f'<path d="M{f(w * 0.04)} {f(h * 0.3)} L {f(w * 0.04)} {f(b)} L {f(w * 0.28)} {f(b)} L {f(w * 0.28)} {f(h * 0.4)} Q {f(w * 0.16)} {f(h * 0.2)} {f(w * 0.04)} {f(h * 0.3)} Z" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.28)} {f(b)} L {f(w * 0.04)} {f(b)} L {f(w * 0.4)} {f(h + 10)} L {f(w * 0.8)} {f(h + 10)} Z" fill="#FFE680" opacity="0.22"></path>',
         f'<rect x="{f(w * 0.36)}" y="{f(b - h * 0.24)}" width="{f(w * 0.6)}" height="{f(h * 0.12)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.36)}" y="{f(b - h * 0.12)}" width="{f(w * 0.6)}" height="{f(h * 0.12)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3E38"></rect>']
    k = max(0.6, h / 300); top = b - h * 0.24
    o.append(f'<path d="M{f(w * 0.46)} {f(top)} L {f(w * 0.48)} {f(top - 12 * k)} L {f(w * 0.78)} {f(top - 14 * k)} L {f(w * 0.8)} {f(top)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="1.8"></path>'
             + "".join(f'<path d="M{f(w * (0.5 + 0.06 * i))} {f(top - 12 * k)} L {f(w * (0.5 + 0.06 * i))} {f(top)}" stroke="#C8C0B0" stroke-width="1.4"></path>' for i in range(5))
             + f'<ellipse cx="{f(w * 0.9)}" cy="{f(top - 7 * k)}" rx="{f(14 * k)}" ry="{f(7 * k)}" fill="#F8F4EC" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(w * 0.9 - 10 * k)} {f(top - 7 * k)} q {f(10 * k)} -6 {f(20 * k)} 0" stroke="#C8C0B0" stroke-width="1.4" fill="none"></path>')
    s = fit(b, max(h * 0.24, b - 230))
    if angels:
        for x, fl in ((0.44, False), (0.86, True)):
            o.append(glow(w * x, top - 60 * s, 130 * s, "#FFFFFF", 0.9, f"{p}a{int(x * 100)}") + light_seated(w * x, top, s * 0.8, flip=fl))
    if look:
        o.append(f'<g transform="translate({f(w * 0.16)} {f(b)}) rotate(18) translate({f(-w * 0.16)} {f(-b)})">' + disciple(p, w * 0.16, b, s * 0.9, "john", flip=True) + '</g>')
    return "".join(o)

def shut_room(p, w, h, seed, stage="midst"):
    """When the doors were shut where the disciples were, for fear of the Jews: the room by lamplight, the door barred, the
    disciples sitting close. midst: Jesus risen come and standing in the midst in white light, his hands open (no wound
    drawn), the disciples rising glad; breathe: the same, a soft light going out from him over them; absent: the
    disciples telling Thomas, who stands apart by the door; thomas: Thomas kneeling before Jesus risen — My Lord and my God."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#5A4A4A", floor="#3A2E2A"), clay_lamp(w * 0.5, h * 0.2, min(1.1, max(0.5, h / 340))),
         f'<rect x="{f(w * 0.86)}" y="{f(h * 0.22)}" width="{f(w * 0.1)}" height="{f(b - h * 0.22)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.84)} {f(h * 0.56)} L {f(w * 0.98)} {f(h * 0.56)}" stroke="#2A1A10" stroke-width="8"></path>']
    s = fit(b, max(h * 0.24, b - 230))
    open_hands = [(-22, -158), (-40, -136), (-58, -128)]
    if stage in ("midst", "breathe"):
        if stage == "breathe": o.append(glow(w * 0.46, b - 120 * s, 300 * s, "#FFFDF0", 0.55, f"{p}b"))
        o.append(jesus_risen(p, w * 0.46, b, s, up=open_hands))
        for i, x in enumerate((0.12, 0.22, 0.32)):
            o.append(disciple_seated(w * x, b, s * 0.72, i))
        for i, x in enumerate((0.62, 0.72)):
            o.append(disciple(p, w * x, b, s * 0.94, ["john", "james"][i], flip=True, up=UP_BLESS if i == 0 else None))
    elif stage == "absent":
        for i, x in enumerate((0.12, 0.22, 0.32, 0.42, 0.52)):
            o.append(disciple_seated(w * x, b, s * 0.72, i, flip=True))
        o.append(disciple(p, w * 0.72, b, s * 0.96, "thomas", flip=True))
    elif stage == "thomas":
        o.append(jesus_risen(p, w * 0.36, b, s, up=open_hands))
        o.append(kneeler(w * 0.56, b, s * 0.84, ROBES["thomas"], flip=True))
        for i, x in enumerate((0.1, 0.2, 0.74)):
            o.append(disciple_seated(w * x, b, s * 0.72, i + 1, flip=x > 0.5))
    return "".join(o)

def tiberias(p, w, h, seed, stage="night"):
    """The sea of Tiberias. night: the boat far out on the dark water, the seven in it, the net hanging empty over the side.
    beach: day breaking over the hills, the boat out on the grey-gold water, and Jesus standing on the beach. net: the net
    cast on the right side of the boat, so full of fishes they cannot draw it; Peter: Peter in the sea swimming to land, the
    little boat coming behind dragging the net. fire: on the shore the fire of coals with fish laid on it and bread, Jesus
    standing by it, the net drawn up on the sand full of great fishes. meal: the disciples sitting about the fire, Jesus
    giving them the bread and the fish."""
    b = h * 0.94
    if stage == "night":
        o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(70, w, h * 0.4, seed), moon(w * 0.18, h * 0.14, max(8, h * 0.035)),
             hills(w, h, h * 0.4, seed, color="#14142E", amp=10, step=90), lake(w, h, h * 0.46, seed, color="#14304A", deep="#0A1A2A", foam="#6A8AA8", op=0.5)]
        s = fit(h * 0.74, h * 0.42)
        o.append(boat(p, w * 0.56, h * 0.72, s, crew=[(-52, ROBES["peter"]), (-14, ROBES["thomas"]), (24, ROBES["john"]), (60, "#2E5A5A")], mast=True, net=True))
        return "".join(o)
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A7A", "#FFC890"), sun(w * 0.7, h * 0.36, max(14, h * 0.05), color="#FFE680", op=0.5),
         hills(w, h, h * 0.36, seed, color="#5A4A6A", amp=12, step=90), lake(w, h, h * 0.42, seed, color="#4A6A9A", deep="#1A2A5A", foam="#FFD8A0"),
         f'<path d="M{f(w * 0.6)} {f(h * 0.43)} L {f(w * 0.8)} {f(h * 0.43)} L {f(w * 0.74)} {f(h * 0.64)} L {f(w * 0.66)} {f(h * 0.64)} Z" fill="#FFE680" opacity="0.3"></path>']
    if stage in ("beach", "net", "peter"):
        o.append(shore(w, h, h * 0.78, x0=-10, x1=w * 0.42, color="#B8A07A"))
        s = fit(b, max(h * 0.3, b - 220)); sb = max(fit(h * 0.62, h * 0.38), min(0.9, h / 420))
        crew = [(-52, ("up", ROBES["thomas"])), (-14, ("up", ROBES["john"])), (24, ROBES["james"]), (60, "#2E5A5A")] if stage == "net" else [(-30, ROBES["john"]), (20, ROBES["james"])]
        if stage != "peter": crew = [(-70, ROBES["peter"])] + crew
        o.append(boat(p, w * 0.72, h * 0.6, sb, crew=crew, mast=True, net=stage in ("net", "peter"), flip=True))
        if stage in ("net", "peter"):
            r = random.Random(seed)
            o.append(f'<path d="M{f(w * 0.72 - 96 * sb)} {f(h * 0.6)} C {f(w * 0.6)} {f(h * 0.62)} {f(w * 0.56)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.74)} C {f(w * 0.66)} {f(h * 0.76)} {f(w * 0.72)} {f(h * 0.72)} {f(w * 0.72 - 60 * sb)} {f(h * 0.62)}" fill="#C8C2D6" fill-opacity="0.35" stroke="#E8D8B0" stroke-width="1.6"></path>')
            for _ in range(14):
                fx, fy = w * r.uniform(0.58, 0.68), h * r.uniform(0.64, 0.73)
                o.append(f'<path d="M{f(fx - 8)} {f(fy)} c 4 -4 12 -4 16 0 c -4 4 -12 4 -16 0 Z" fill="#C8C2D6" stroke="{INK}" stroke-width="0.8"></path>')
        if stage == "peter":
            px, py = w * 0.5, h * 0.66
            o.append(f'<circle cx="{f(px)}" cy="{f(py - 8 * sb)}" r="{f(9 * sb + 2)}" fill="#B98A6E" stroke="{INK}" stroke-width="1.6"></circle>'
                     f'<path d="M{f(px - 12 * sb)} {f(py - 6 * sb)} C {f(px - 10 * sb)} {f(py + 4 * sb)} {f(px + 10 * sb)} {f(py + 4 * sb)} {f(px + 12 * sb)} {f(py - 6 * sb)}" fill="#4A4440" stroke="{INK}" stroke-width="1.2"></path>'
                     f'<path d="M{f(px - 40 * sb)} {f(py)} q {f(20 * sb)} -10 {f(30 * sb)} -2 M{f(px + 10 * sb)} {f(py - 2)} q {f(16 * sb)} -12 {f(34 * sb)} -4" stroke="#B98A6E" stroke-width="{f(5 * sb + 1)}" fill="none" stroke-linecap="round"></path>'
                     f'<path d="M{f(px - 50 * sb)} {f(py + 4)} q {f(50 * sb)} -8 {f(100 * sb)} 0" stroke="#FFE8C0" stroke-width="2" fill="none"></path>')
        o.append(jesus_risen(p, w * 0.16, b, s * 0.96) if stage != "beach" else jesus(p, w * 0.16, b, s * 0.96))
        return "".join(o)
    o.append(shore(w, h, h * 0.62, color="#B8A07A"))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(boat(p, w * 0.86, h * 0.56, fit(h * 0.56, h * 0.42), mast=True, flip=True))
    if stage == "fire":
        o.append(coals(w * 0.46, b - 8, s * 0.9, seed, fish=True, bread=True))
        r = random.Random(seed)
        o.append(f'<path d="M{f(w * 0.6)} {f(b - 4)} C {f(w * 0.66)} {f(b - 40 * s)} {f(w * 0.84)} {f(b - 40 * s)} {f(w * 0.92)} {f(b - 6)} Z" fill="#C8C2D6" fill-opacity="0.4" stroke="#B8A880" stroke-width="1.8"></path>')
        for _ in range(16):
            fx, fy = w * r.uniform(0.62, 0.9), b - r.uniform(4, 28 * s)
            o.append(f'<path d="M{f(fx - 10 * s)} {f(fy)} c {f(5 * s)} {f(-5 * s)} {f(15 * s)} {f(-5 * s)} {f(20 * s)} 0 c {f(-5 * s)} {f(5 * s)} {f(-15 * s)} {f(5 * s)} {f(-20 * s)} 0 Z" fill="#C8C2D6" stroke="{INK}" stroke-width="0.8"></path>')
        o.append(jesus_risen(p, w * 0.24, b, s, up=UP_BLESS))
        o.append(disciple(p, w * 0.56, b - 6, s * 0.96, "peter", flip=True, up=UP_TOUCH))
    elif stage == "meal":
        o.append(coals(w * 0.5, b - 8, s * 0.8, seed, fish=True))
        o.append(jesus_risen(p, w * 0.32, b, s, up=[(-22, -158), (-44, -140), (-60, -130)], flip=True))
        o.append(f'<ellipse cx="{f(w * 0.32 + 62 * s)}" cy="{f(b - 132 * s)}" rx="{f(14 * s)}" ry="{f(7 * s)}" fill="#D9A25A" stroke="{INK}" stroke-width="1.4"></ellipse>')
        for i, x in enumerate((0.1, 0.18, 0.62, 0.72, 0.82, 0.92)):
            o.append(disciple_seated(w * x, b, s * 0.72, [0, 5, 3, 2, 8, 9][i], flip=x > 0.5))
    return "".join(o)

def lovest(p, w, h, seed, follow=False):
    """Lovest thou me?: the shore in the morning, Jesus risen and Peter walking together by the water's edge, the others
    left sitting by the fire far behind; follow=True the beloved disciple coming after them along the sand."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.32, seed, color="#7A8A6A", amp=12, step=90), lake(w, h, h * 0.38, seed),
         shore(w, h, h * 0.6, color="#C8B080")]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(coals(w * 0.86, h * 0.7, fit(h * 0.7, h * 0.56) * 0.6, seed))
    for i, x in enumerate((0.78, 0.94)):
        o.append(disciple_seated(w * x, h * 0.72, fit(h * 0.72, h * 0.58) * 0.8, i + 2, flip=x > 0.86))
    o.append(jesus_risen(p, w * 0.26, b, s, flip=True))
    o.append(disciple(p, w * 0.44, b - 4, s * 0.98, "peter", flip=True))
    if follow:
        o.append(disciple(p, w * 0.64, b - 10, s * 0.86, "john", flip=True))
    return "".join(o)

def books(p, w, h, seed):
    """Even the world itself would not contain the books that should be written: scrolls and books heaped and stacked away
    over the hills to the horizon under the evening light."""
    r = random.Random(seed)
    o = [sky(w, h, "#3A2A5A", "#FFC890"), glow(w * 0.5, h * 0.3, h * 0.6, "#FFF4C2", 0.6, f"{p}g"), hills(w, h, h * 0.42, seed, color="#8A7A6A", amp=12, step=90)]
    for row in range(7):
        y = h * (0.46 + 0.08 * row); k = (0.3 + 0.18 * row) * max(0.6, h / 300)
        x = r.uniform(-20, 0)
        while x < w + 20:
            if r.random() < 0.55:
                o.append(f'<rect x="{f(x)}" y="{f(y - 14 * k)}" width="{f(40 * k)}" height="{f(14 * k)}" rx="{f(6 * k)}" fill="{r.choice(["#E8D8B0", "#D8C098", "#F3E8C8"])}" stroke="{INK}" stroke-width="1.2"></rect>'
                         f'<rect x="{f(x - 3 * k)}" y="{f(y - 16 * k)}" width="{f(6 * k)}" height="{f(18 * k)}" rx="{f(3 * k)}" fill="#8A6A3A" stroke="{INK}" stroke-width="1"></rect>')
            else:
                hh = r.uniform(10, 22) * k
                o.append(f'<rect x="{f(x)}" y="{f(y - hh)}" width="{f(30 * k)}" height="{f(hh)}" fill="{r.choice(["#7A2A2A", "#2A4A6A", "#4A5A2A", "#6A4A2A"])}" stroke="{INK}" stroke-width="1.2"></rect>')
            x += r.uniform(34, 52) * k
    return "".join(o)
