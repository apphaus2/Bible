"""Drawings for Daniel chapter 2 (Daniel 3–4): the image of gold on the plain of Dura, the instruments of the herald's decree,
the burning fiery furnace (the three walking loose in the fire, the fourth only a shape of light), the great tree, the
watcher, the stump with its band of iron and brass, the king on the roof of his palace, the field wet with dew."""
from dan.art import *
from dan.art import f, K2, GREY_BEARD
import random, math

def dura(p, w, h, seed, stage="stand"):
    """The image of gold set up in the plain of Dura: a tall gilded figure on a stepped base, far taller than the crowd.
    stage "stand": the satraps and rulers standing before it; "bow": all the peoples fallen down, three men left standing."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E0B0"), hills(w, h, h * 0.66, seed, "#C8A878", amp=6, step=120), ground(w, h, h * 0.7, "#D8B880", dy=0)]
    cx, top = w * 0.7, h * 0.04
    base = h * 0.74
    ht = base - top
    wd = ht / 10 * 1.6
    o.append(f'<rect x="{f(cx - wd * 1.4)}" y="{f(base - ht * 0.08)}" width="{f(wd * 2.8)}" height="{f(ht * 0.08)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(cx - wd * 1.0)}" y="{f(base - ht * 0.14)}" width="{f(wd * 2)}" height="{f(ht * 0.06)}" fill="#B08A5A" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = (ht * 0.86) / 200
    gold = mk.person(p, round(cx), round(base - ht * 0.14), round(s, 3), body="#E8B830", cloth="#FFD23F", sw=2.4, extra=TIARA.replace("#E8B830", "#FFE680") + A.BLACK_BEARD.replace("#2A1A10", "#C8962E"))
    o.append(gold + V.rays(cx, top + ht * 0.2, 24, 8, ht * 0.5, color="#FFF4C2", op=0.25))
    r = random.Random(seed)
    sf = fit(b, b - h * 0.2)
    if stage == "stand":
        for i in range(26):
            x = r.uniform(0.02, 0.56) * w; y = h * 0.74 + r.uniform(0, 0.2) * h
            o.append(prince(p, x, y, sf * (0.6 + (y - h * 0.74) / h * 2), PRINCE[i % 7], flip=False))
    else:
        for i in range(24):
            x = r.uniform(0.02, 0.56) * w; y = h * 0.76 + r.uniform(0, 0.18) * h
            o.append(N.prostrate(x, y, sf * (0.6 + (y - h * 0.74) / h * 2) * 0.8, color=PRINCE[i % 7], skin="#C98E66"))
        for i in range(3):
            o.append(three_fig(p, w * (0.2 + i * 0.07), b, sf * 1.2, i))
    return "".join(o)

INSTR = [("CORNET", "horn"), ("FLUTE", "flute"), ("HARP", "harp"), ("SACKBUT", "sack"), ("PSALTERY", "psal"), ("DULCIMER", "dulc")]
def _instr(kind, x, y, k):
    st = 'stroke="#FFD23F" stroke-width="2" fill="none"'
    if kind == "horn": return f'<path d="M{f(x - 30 * k)} {f(y + 10 * k)} C {f(x - 10 * k)} {f(y + 8 * k)} {f(x + 10 * k)} {f(y - 10 * k)} {f(x + 26 * k)} {f(y - 28 * k)} L {f(x + 34 * k)} {f(y - 18 * k)} C {f(x + 16 * k)} {f(y + 2 * k)} {f(x - 6 * k)} {f(y + 18 * k)} {f(x - 30 * k)} {f(y + 16 * k)} Z" {st}></path>'
    if kind == "flute": return f'<rect x="{f(x - 32 * k)}" y="{f(y - 3 * k)}" width="{f(64 * k)}" height="{f(6 * k)}" {st}></rect>' + "".join(f'<circle cx="{f(x + d * k)}" cy="{f(y)}" r="{f(1.6 * k)}" fill="#FFD23F"></circle>' for d in (-14, -6, 2, 10, 18))
    if kind == "harp": return f'<path d="M{f(x - 20 * k)} {f(y + 26 * k)} L {f(x - 20 * k)} {f(y - 30 * k)} C {f(x + 10 * k)} {f(y - 30 * k)} {f(x + 24 * k)} {f(y - 4 * k)} {f(x + 20 * k)} {f(y + 26 * k)} Z" {st}></path>' + "".join(f'<path d="M{f(x - 20 * k + i * 7 * k)} {f(y + 26 * k)} L {f(x - 20 * k + i * 7 * k)} {f(y - 26 * k + i * 4 * k)}" stroke="#FFD23F" stroke-width="1"></path>' for i in range(1, 6))
    if kind == "sack": return f'<path d="M{f(x - 24 * k)} {f(y + 22 * k)} L {f(x + 18 * k)} {f(y - 26 * k)} M{f(x - 14 * k)} {f(y + 26 * k)} L {f(x + 26 * k)} {f(y - 20 * k)}" {st}></path><path d="M{f(x - 24 * k)} {f(y + 22 * k)} C {f(x - 34 * k)} {f(y + 30 * k)} {f(x - 22 * k)} {f(y + 36 * k)} {f(x - 14 * k)} {f(y + 26 * k)}" {st}></path>'
    if kind == "psal": return f'<path d="M{f(x - 30 * k)} {f(y + 20 * k)} L {f(x + 30 * k)} {f(y + 20 * k)} L {f(x)} {f(y - 26 * k)} Z" {st}></path>' + "".join(f'<path d="M{f(x - 30 * k + i * 10 * k)} {f(y + 20 * k)} L {f(x - 30 * k + i * 10 * k + (30 - i * 10) * k * 0.0)} {f(y + 20 * k - min(i, 6 - i) * 14 * k)}" stroke="#FFD23F" stroke-width="1"></path>' for i in range(1, 6))
    return f'<rect x="{f(x - 32 * k)}" y="{f(y - 14 * k)}" width="{f(64 * k)}" height="{f(28 * k)}" {st}></rect>' + "".join(f'<path d="M{f(x - 30 * k)} {f(y - 10 * k + i * 5 * k)} L {f(x + 30 * k)} {f(y - 10 * k + i * 5 * k)}" stroke="#FFD23F" stroke-width="1"></path>' for i in range(5))

def instruments(w, h):
    """The herald's decree as a technical plate: the cornet, flute, harp, sackbut, psaltery and dulcimer, and all kinds of
    music, each drawn in outline with its name."""
    o = [grid_bg(w, h)]
    k = min(1.3, h / 160, w / 520)
    for i, (nm, kind) in enumerate(INSTR):
        x = w * (0.09 + i * 0.164); y = h * 0.42
        o.append(f'<rect x="{f(x - w * 0.07)}" y="{f(h * 0.1)}" width="{f(w * 0.14)}" height="{f(h * 0.66)}" fill="none" stroke="#1E5A7A" stroke-width="1.4"></rect>')
        o.append(_instr(kind, x, y, k) + label(x, h * 0.86, nm, CYAN, max(8, min(11, 9 * k))))
    return "".join(o)

def furnace(p, w, h, seed, stage="heat"):
    """The burning fiery furnace: a great kiln of brick with an arched mouth full of fire. stage "heat": the fire heated seven
    times more, men feeding it; "cast": only the mouth roaring, smoke and flame (no one drawn); "four": four men loose walking
    in the midst of the fire, the fourth a shape of white light; "out": the three come forth, the king and his counsellors
    before the mouth."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A1A2A", "#8A3A1A"), ground(w, h, h * 0.84, "#5A3A2A", dy=0)]
    fx, fw = w * 0.58, w * 0.62
    top = h * 0.06
    o.append(f'<path d="M{f(fx - fw / 2)} {f(h * 0.86)} L {f(fx - fw / 2)} {f(top + h * 0.2)} C {f(fx - fw * 0.3)} {f(top)} {f(fx + fw * 0.3)} {f(top)} {f(fx + fw / 2)} {f(top + h * 0.2)} L {f(fx + fw / 2)} {f(h * 0.86)} Z" fill="#7A3A22" stroke="#0D0D0F" stroke-width="3"></path>')
    for i in range(1, 9):
        y = top + h * 0.1 * i
        o.append(f'<path d="M{f(fx - fw / 2)} {f(y)} L {f(fx + fw / 2)} {f(y)}" stroke="#4A2214" stroke-width="1.4"></path>')
    mw, mt = fw * 0.56, h * 0.3
    mouth = f'M{f(fx - mw / 2)} {f(h * 0.86)} L {f(fx - mw / 2)} {f(mt + mw * 0.25)} A {f(mw / 2)} {f(mw / 2)} 0 0 1 {f(fx + mw / 2)} {f(mt + mw * 0.25)} L {f(fx + mw / 2)} {f(h * 0.86)} Z'
    o.append(f'<defs><linearGradient id="{p}fg" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.5" stop-color="#FFC14D"></stop><stop offset="1" stop-color="#FF6A2A"></stop></linearGradient></defs>'
             f'<path d="{mouth}" fill="url(#{p}fg)" stroke="#0D0D0F" stroke-width="3"></path>')
    o.append(f'<clipPath id="{p}mc"><path d="{mouth}"></path></clipPath>')
    inner = [E.blaze(fx + d * mw, h * 0.86, mw * 0.4, h * 0.42, seed + i, n=6) for i, d in enumerate((-0.3, 0.0, 0.3))]
    if stage == "four":
        s = (h * 0.84 - (mt + mw * 0.32)) * 0.8 / 200
        figs = "".join(three_fig(p, fx + d * mw, h * 0.84, s * 0.96, i, cloth=THREE_C[i][0]) for i, d in enumerate((-0.33, -0.11, 0.33)))
        inner.append(figs + glow_fig(fx + 0.11 * mw, h * 0.84, s))
    o.append(f'<g clip-path="url(#{p}mc)">{"".join(inner)}</g>')
    o.append(E.blaze(fx, mt + 10, mw * 0.5, h * 0.24, seed + 9, n=5) if stage in ("heat", "cast") else "")
    o.append(smoke(fx - fw * 0.2, top, 6, seed, color="#5A4A4A", op=0.6, k=min(1.6, h / 260)) + smoke(fx + fw * 0.2, top, 6, seed + 3, color="#5A4A4A", op=0.6, k=min(1.6, h / 260)))
    sf = fit(b, b - h * 0.36)
    if stage == "heat":
        for i in range(3):
            o.append(man(p, w * (0.06 + i * 0.09), b, sf, "#5A3A2A", up=[(-22, -158), (-6, -150), (12, -150)]))
    if stage == "out":
        o.append(neb(p, w * 0.1, b, sf * 1.08) + prince(p, w * 0.2, b - 4, sf, PRINCE[0]) + prince(p, w * 0.27, b, sf, PRINCE[1]))
        for i in range(3): o.append(three_fig(p, w * (0.33 + i * 0.065), b - (i % 2) * 4, sf * 1.02, i, flip=True))
    if stage == "four":
        o.append(neb(p, w * 0.1, b, sf * 1.08, up=[(-22, -158), (-44, -170), (-66, -184)]))
    return "".join(o)

def three_stand(p, w, h, seed):
    """Shadrach, Meshach and Abed-nego standing before the king on his throne in the plain, the image of gold far behind."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E0B0"), ground(w, h, h * 0.66, "#D8B880", dy=0)]
    gx = w * 0.5
    o.append(mk.person(p, round(gx), round(h * 0.66), round(h * 0.6 / 200, 3), body="#E8B830", cloth="#FFD23F", sw=2, extra=TIARA.replace("#E8B830", "#FFE680")))
    o.append(throne_k(p, w, h, w * 0.84, b, "neb"))
    s = fit(b, b - h * 0.5)
    for i in range(3): o.append(three_fig(p, w * (0.14 + i * 0.12), b, s, i))
    o.append(guard(p, w * 0.62, b, s * 0.96, cloth="#7A2A1A", flip=True))
    return "".join(o)

# ---- Daniel 4 ------------------------------------------------------------------------------------------------------------------
def great_tree(w, h, seed, stage=0):
    """The tree in the midst of the earth, whose height reached unto heaven: beasts in its shadow, birds in its branches.
    stage 1: a watcher, a holy one, coming down from heaven as a shaft of light; stage 2: the tree hewn down, the stump of its
    roots left in the tender grass, bound with a band of iron and brass, wet with the dew."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0F0E2A" if stage == 1 else "#5A8AC8", "#3A2A5A" if stage == 1 else "#CFE8F0")]
    if stage == 1: o.append(mk.stars(40, w, h * 0.5, seed))
    o.append(ground(w, h, h * 0.86, "#4A6A3A" if stage != 1 else "#2A3A2A", dy=0))
    cx = w * 0.5
    if stage == 2:
        o.append(f'<path d="M{f(cx - 34)} {f(h * 0.87)} L {f(cx - 28)} {f(h * 0.66)} L {f(cx + 28)} {f(h * 0.66)} L {f(cx + 34)} {f(h * 0.87)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<ellipse cx="{f(cx)}" cy="{f(h * 0.66)}" rx="28" ry="7" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<rect x="{f(cx - 32)}" y="{f(h * 0.72)}" width="64" height="9" fill="#8A9AA8" stroke="#0D0D0F" stroke-width="1.8"></rect>'
                 f'<rect x="{f(cx - 33)}" y="{f(h * 0.78)}" width="66" height="9" fill="#C8783A" stroke="#0D0D0F" stroke-width="1.8"></rect>')
        for i in range(5):
            x = cx + (i - 2) * w * 0.12 + 60 * (1 if i > 2 else -1)
            o.append(f'<path d="M{f(x)} {f(h * 0.86)} L {f(x + w * 0.1)} {f(h * 0.82 - i * 3)}" stroke="#6A4A2A" stroke-width="{f(10 - i)}" stroke-linecap="round"></path>')
        for i in range(30):
            o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.88, h))}" r="2" fill="#E8F6FA" opacity="0.8"></circle>')
        o.append(tag(cx + 34, h * 0.76, "A BAND OF IRON AND BRASS", w * 0.72, h * 0.5, color="#F3EFE6"))
        return "".join(o)
    tw = min(w * 0.06, h * 0.06)
    o.append(f'<path d="M{f(cx - tw * 1.6)} {f(h * 0.87)} C {f(cx - tw)} {f(h * 0.6)} {f(cx - tw * 0.6)} {f(h * 0.4)} {f(cx - tw * 0.4)} {f(h * 0.2)} L {f(cx + tw * 0.4)} {f(h * 0.2)} C {f(cx + tw * 0.6)} {f(h * 0.4)} {f(cx + tw)} {f(h * 0.6)} {f(cx + tw * 1.6)} {f(h * 0.87)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for i in range(14):
        a = r.uniform(-0.9, 0.9); ry = h * r.uniform(0.04, 0.5)
        x = cx + a * w * 0.42; y = ry
        o.append(f'<path d="M{f(cx)} {f(ry + h * 0.14)} L {f(x)} {f(y + h * 0.06)}" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>')
    for i in range(36):
        x = cx + r.uniform(-0.46, 0.46) * w; y = h * r.uniform(-0.02, 0.56)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(0.05, 0.1) * min(w, h * 1.6))}" fill="{r.choice(("#2E6B3A", "#3A7A3A", "#1F4A34"))}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    for i in range(14):
        x = cx + r.uniform(-0.4, 0.4) * w; y = h * r.uniform(0.04, 0.5)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="4" fill="#E8783A" stroke="#0D0D0F" stroke-width="1"></circle>')
    for i in range(8):
        x = cx + r.uniform(-0.4, 0.4) * w; y = h * r.uniform(0.0, 0.45)
        o.append(bird(x, y, 0.8, "#0D0D0F"))
    k = min(1.0, h / 520)
    from job.art11 import wild_ox_fig, hind
    o.append(wild_ox_fig(w * 0.2, h * 0.92, k * 0.7) + hind(w * 0.8, h * 0.92, k * 0.7, flip=True))
    if stage == 1:
        o.append(f'<path d="M{f(cx + w * 0.22)} -10 L {f(cx + w * 0.3)} -10 L {f(cx + w * 0.36)} {f(h * 0.86)} L {f(cx + w * 0.16)} {f(h * 0.86)} Z" fill="#FFF4C2" opacity="0.3"></path>'
                 + glow_fig(cx + w * 0.26, h * 0.62, h * 0.4 / 200))
    return "".join(o)

from genesis.art2 import bird

def palace_roof(p, w, h, seed):
    """At the end of twelve months: the king walking on the roof of the royal palace, great Babylon spread below him."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), babylon(w, h * 0.86, seed, tone="day"),
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.22)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(int(w / 30) + 2):
        o.append(f'<rect x="{f(i * 30)}" y="{f(h * 0.76)}" width="16" height="{f(h * 0.05)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    s = fit(b, b - h * 0.5)
    o.append(neb(p, w * 0.8, b, s, flip=True, up=[(-22, -158), (-50, -170), (-80, -176)]))
    return "".join(o)

def dew_field(w, h, seed):
    """The field at dawn, wet with the dew of heaven: tall grass, oxen grazing far off (the king's madness told in words only)."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#9AB8D8", "#F3E8D8"), sun(w * 0.8, h * 0.42, max(10, h * 0.05), color="#FFE680", op=0.25),
         hills(w, h, h * 0.5, seed, "#6A8A6A", amp=10, step=90), ground(w, h, h * 0.58, "#7A9A4A", dy=0)]
    import samuel1 as S1x
    for i in range(3):
        o.append(S1x.cow(w * (0.18 + i * 0.2), h * 0.66 + i * 4, min(0.5, h / 600), flip=i == 1, color=("#C9A27A", "#8A6A4A", "#E8D8C0")[i], low=True))
    for i in range(int(w / 6)):
        x = r.uniform(-10, w + 10); y = r.uniform(h * 0.62, h + 4); hh = r.uniform(12, 30) * min(1.5, h / 300)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + 2)} {f(y - hh * 0.5)} {f(x + 6)} {f(y - hh)} {f(x + 8)} {f(y - hh)}" stroke="{r.choice(("#4A7A2A", "#5E8F26", "#3A6A2A"))}" stroke-width="2" fill="none"></path>')
        if r.random() < 0.25: o.append(f'<circle cx="{f(x + 8)}" cy="{f(y - hh)}" r="1.8" fill="#E8F6FA"></circle>')
    return "".join(o)

def restored(p, w, h, seed):
    """The king again upon his throne, his counsellors and lords come to seek unto him, the hall in glory."""
    b = h * 0.94
    o = [bab_hall(p, w, h, seed, floor=0.62), throne_k(p, w, h, w * 0.8, b, "neb"), V.rays(w * 0.8, h * 0.3, 24, 10, w * 0.5, color="#FFF4C2", op=0.15)]
    s = fit(b, max(h * 0.2, b - 250))
    for i in range(5): o.append(prince(p, w * (0.08 + i * 0.1), b - (i % 2) * 8, s * 0.94, PRINCE[i % 7]))
    return "".join(o)
