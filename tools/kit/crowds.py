"""Crowd and procession drawings first written for the digest books (exodus_book3, joshua_book1, judges_book1,
judges_book2), kept here so the volumes no longer depend on the digest writers."""
import random
import exodus as E, exodus4 as Z, joshua1 as J, judges1 as G, judges2 as S
from mk import person

WAR = ("#8A3A1E", "#5A2A16", "#3A2214", "#5A6E8A")

def crowd(p, n, x0, x1, y0, y1, seed, smin, smax, flock=0.0, body=("#2A140C", "#3A2214", "#4A2A1A"), cloth=("#C9A86A", "#B8A27A", "#8A6A4A", "#5A6E8A", "#C2456A")):
    """n people (and, with flock, sheep) scattered between y0 and y1, larger toward the bottom."""
    r = random.Random(seed); items = []
    for _ in range(n):
        y = r.uniform(y0, y1); k = (y - y0) / max(1, y1 - y0)
        items.append((y, r.uniform(x0, x1), smin + (smax - smin) * k, r.random()))
    items.sort()
    out = []
    for y, x, s, q in items:
        if q < flock:
            out.append(E.sheep(x, y, s * 0.9, flip=r.random() < 0.5))
        else:
            out.append(person(p, f"{x:.0f}", f"{y:.0f}", f"{s:.2f}", body=r.choice(body), cloth=r.choice(cloth), kind=r.choice(["Robe", "Tunic"]), sw=4, woman=r.random() < 0.4))
    return "".join(out)

def procession(p, x0, x1, y, s, seed, flip=False):
    """Men of war, then seven priests with trumpets, then the ark, marching to the right (or left when flipped)."""
    r = random.Random(seed); o = []; x = x0; step = 46 * s
    for i in range(6):
        o.append(person(p, round(x), y + r.randint(-3, 3), round(s, 3), body="#2A140C", cloth=r.choice(WAR), kind="Tunic", sw=4, flip=flip, extra=Z.SPEAR)); x += step
    for i in range(7):
        o.append(J.trumpeter(p, x, y + r.randint(-3, 3), s, flip=flip)); x += step
    o.append(J.ark_borne(p, x + 120 * s, y, s, f"pr{seed}", gap=110 * s, glow=False))
    return "".join(o)

def midian_camp(n, x0, x1, y0, y1, seed):
    """The camp of Midian: dark tents and camels, scattered and scaled by depth."""
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1), r.random()) for _ in range(n)); o = []
    for y, x, q in items:
        k = (y - y0) / max(1, y1 - y0)
        if q < 0.3:
            o.append(G.camel(x, y, 0.2 + 0.25 * k, flip=q < 0.15, color="#8A6A4A"))
        else:
            w = 30 + 50 * k; o.append(Z.tent(x, y, w, w * 0.7, color=r.choice(["#2A1A2E", "#3A2A3E", "#4A2A1A"])))
    return "".join(o)

def samson_both(x, y, s, left, right, uid, locks=True, stroke="#0D0D0F", cloth="#8A3A1E"):
    """Samson with both arms free (wrestling, pushing the pillars)."""
    return (Z.figure_both(x, y, s, "#3A1E14", cloth, left, right, uid, stroke=stroke)
            .replace("</g>", (f'<g>{S.LOCKS_FIG}</g>' if locks else "") + "</g>", 1)
            .replace(f'fill="{cloth}" stroke="{stroke}" stroke-width="3"', f'fill="{cloth}" stroke="{stroke}" stroke-width="3"'))
