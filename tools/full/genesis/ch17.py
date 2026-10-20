"""Genesis volume, Chapter 17 — The Blessing of Jacob (Genesis 48–50), the last chapter of Genesis. Every verse,
word for word from ref/eng-asv. Jacob's blessing of the twelve (49:3–27) is set as two pages of cells, one per son,
each headed with his name (the words are Jacob's, spoken over his sons on his bed)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, egypt as EG
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from faces_ex import F
from genesis import G, art as X, art2 as Y, art3 as Z, art5 as K, art10 as T, art11 as U, art12 as V12
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE, LAMP
from genesis.ch12 import COURT
from genesis.ch14 import talk
from genesis.ch16 import ISRAEL_OLD, ISRAEL_DYING, LEAH_C, ZILPAH_C, RACHEL_C, BILHAH_C, goshen
from mk import defs, face

v, sp = G.v, G.span
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
EPHRAIM = F("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#1A1210", hl="#4A3A2E", collar=True, light="#FFE680")
MANASSEH = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#3A2214", hl="#6A5A4E", collar=True, light="#FFE680")
JOSEPH_OLD = F("adam", skin="#D9A27A", shadow="#8A5A5A", hair="#C8C2B6", hl="#8A867E", beard=True, beard_color="#C8C2B6", collar=True, kohl=True, light="#FFE680")
START = 251                                  # chapter 16 ends on page 250
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def bedside(p, w, h, seed, boys=True):
    """Israel sitting up on his bed; Joseph with his two sons before him."""
    b = h * 0.9
    bed = (f'<rect x="{w * 0.56:.0f}" y="{b - 40:.0f}" width="{w * 0.4:.0f}" height="30" rx="6" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></rect>'
           f'<rect x="{w * 0.92:.0f}" y="{b - 80:.0f}" width="20" height="70" rx="4" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')
    o = [J7_tent(w, h), Y.ground(w, h, b, "#2A1408", dy=0), bed, Z.E.kneel(w * 0.78, b - 34, round(h / 540, 3), color="#5A6E8A", skin=Y.SKIN, flip=True)]
    o.append(T.figure(p, "joseph_eg", w * 0.3, b, Y.fit(b, h * 0.36)))
    if boys:
        o.append(K.lad(p, w * 0.4, b, Y.fit(b, h * 0.56), cloth="#E8D8B0") + K.lad(p, w * 0.48, b, Y.fit(b, h * 0.6), cloth="#F3EFE6"))
    return "".join(o)

def J7_tent(w, h):
    from genesis import art7 as J7
    return J7.tent_inside(w, h, 0.3)

def crossed_hands(w, h):
    """Guiding his hands wittingly: two old hands crossed, the right upon the younger's head."""
    o = [J7_tent(w, h)]
    for x, c in [(0.3, "#3A2214"), (0.7, "#1A1210")]:
        o.append(f'<ellipse cx="{w * x:.0f}" cy="{h * 0.86:.0f}" rx="{w * 0.16:.0f}" ry="{h * 0.2:.0f}" fill="{c}" stroke="#0D0D0F" stroke-width="2.4"></ellipse>')
    for x0, x1 in [(0.1, 0.72), (0.9, 0.3)]:
        o.append(f'<path d="M{w * x0:.0f} {h * 0.1:.0f} L {w * x1:.0f} {h * 0.62:.0f}" stroke="#0D0D0F" stroke-width="38" stroke-linecap="round"></path>'
                 f'<path d="M{w * x0:.0f} {h * 0.1:.0f} L {w * x1:.0f} {h * 0.62:.0f}" stroke="#5A6E8A" stroke-width="32" stroke-linecap="round"></path>'
                 f'<ellipse cx="{w * x1:.0f}" cy="{h * 0.66:.0f}" rx="34" ry="22" fill="#C98E66" stroke="#0D0D0F" stroke-width="2.4"></ellipse>')
    o.append(Z.label(w * 0.7, h * 0.8, "EPHRAIM", "#FFD23F", 11) + Z.label(w * 0.3, h * 0.8, "MANASSEH", "#FFD23F", 11))
    return "".join(o)

def funeral(p, w, h, seed):
    """Chariots and horsemen, a very great company, going up out of Egypt with the bier."""
    import exodus3 as E3
    b = h * 0.86
    bier = (f'<rect x="{w * 0.42:.0f}" y="{b - 60:.0f}" width="{w * 0.16:.0f}" height="26" rx="4" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
            + "".join(T.figure(p, ("man", c), w * x, b, Y.fit(b, h * 0.62)) for x, c in [(0.42, "#5A3A22"), (0.5, "#7A3A2A"), (0.58, "#3A5A6A")]))
    return (Z.sun(w * 0.86, h * 0.2, 14, color="#FFE680", op=0.25) + Y.ground(w, h, b, "#C8A06A", dy=0)
            + E3.chariot(w * 0.14, b + 2, 0.5, color="#E8B830", driver="#F3EFE6") + E3.chariot(w * 0.82, b + 2, 0.5, color="#E8B830", driver="#F3EFE6", flip=True)
            + bier + "".join(T.figure(p, ("egypt", "#F3EFE6"), w * x, b, Y.fit(b, h * 0.6)) for x in (0.28, 0.34, 0.66, 0.72)))

def atad(p, w, h, seed):
    """The threshing-floor of Atad beyond the Jordan: the mourners in a ring, heads covered."""
    b = h * 0.88
    o = [Z.sun(w * 0.8, b - 10, h * 0.2, color="#C2456A", op=0.2), Y.hills(w, h, b - h * 0.1, seed, color="#3A2A3E", amp=6), Y.ground(w, h, b, "#8A7A5A", dy=0),
         Z.A4.threshing_floor(w * 0.5, b - 4, w * 0.6)]
    o += [Z.E.kneel(w * (0.26 + i * 0.07), b - (8 if i % 2 else 0), round(h / 560, 3), color=c, skin=Y.SKIN, flip=i > 3) for i, c in enumerate(U.BROS + ["#F3EFE6", "#E8D8B0"])]
    o.append(Z.label(w * 0.5, b + 22, "ABEL-MIZRAIM", "#12113A", 10))
    return "".join(o)

def coffin(w, h, seed):
    """He was put in a coffin in Egypt: a painted wooden coffin in the dark, a lamp, the end."""
    b = h * 0.8
    return (f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#12090A"></rect>' + f'<circle cx="{w * 0.5:.0f}" cy="{b - 60:.0f}" r="{h * 0.4:.0f}" fill="#FFC14D" opacity="0.14"></circle>'
            + f'<path d="M{w * 0.2:.0f} {b:.0f} L {w * 0.24:.0f} {b - 70:.0f} C {w * 0.3:.0f} {b - 100:.0f} {w * 0.7:.0f} {b - 100:.0f} {w * 0.76:.0f} {b - 70:.0f} L {w * 0.8:.0f} {b:.0f} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="3"></path>'
            + "".join(f'<path d="M{w * (0.26 + i * 0.06):.0f} {b - 80:.0f} L {w * (0.26 + i * 0.06):.0f} {b:.0f}" stroke="#1F5FAD" stroke-width="5"></path>' for i in range(9))
            + Y.ground(w, h, b, "#2A1A14", dy=0))


@P("GEN-C17-00-Title", "Chapter 17 · The Blessing of Jacob")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2214"></rect>' + crossed_hands(760, 1080)
    return chapter_title(17, "第十七話", "The Blessing of Jacob", "Genesis 48 – 50", svg, NIGHT,
                         v("50:20", frm="ye meant evil", to="for good,"), "Genesis · Volume One")


@P("GEN-C17-P01-Sick", "251 · God Almighty Appeared unto Me at Luz")
def p01():
    t, h = rows(240, None)
    r1 = new("#3A2214", W1, h[0], defs("c171a", *ALL) + bedside("c171a", W1, h[0], 1711),
             cap(v("48:1") + " " + v("48:2"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 48:1–2", "right: 12px; top: 12px"))
    r2 = new(LAMP, W1, h[1], face(ISRAEL_OLD, -60, h[1] - 560, 1.4),
             cap(v("48:3", to="unto Joseph,"), "left: 330px; top: 16px", size=11)
             + balloon(v("48:3", frm="God Almighty") + " " + v("48:4") + " " + v("48:5") + " " + v("48:6") + " " + v("48:7"), "left: 280px; top: 56px", 420, size=12, pad="72px 54px")
             + vref("GEN 48:3–7", "left: 12px; bottom: 12px"))
    return page("Genesis 48:1–7 — God Almighty Appeared unto Me at Luz", t, r1 + r2, START + 0)


@P("GEN-C17-P02-Sons", "252 · Who Are These?")
def p02():
    t, h = rows(260, 260, None)
    r1 = cols(talk(ISRAEL_OLD, h[0], LAMP, [("cap", v("48:8", to="said,")), ("say", v("48:8", frm="Who are"))], w=W2, ref="GEN 48:8", size=13),
              talk(V12.JOSEPH_EG, h[0], COURT, [("cap", v("48:9", to="unto his father,")), ("say", v("48:9", frm="They are", to="given me here.")),
                                                ("cap", v("48:9", frm="And he said,", to="he said,")), ("say", v("48:9", frm="Bring them"))], w=W2, ref="GEN 48:9", size=11.5))
    r2 = new("#3A2214", W1, h[1], defs("c172b", *ALL) + bedside("c172b", W1, h[1], 1722),
             cap(v("48:10"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("GEN 48:10", "right: 12px; top: 12px"))
    r3 = talk(ISRAEL_OLD, h[2], LAMP, [("cap", v("48:11", to="unto Joseph,")), ("say", v("48:11", frm="I had not")), ("cap", v("48:12"))], ref="GEN 48:11–12")
    return page("Genesis 48:8–12 — Who Are These?", t, r1 + r2 + r3, START + 1)


@P("GEN-C17-P03-Hands", "253 · Guiding His Hands Wittingly")
def p03():
    t, h = rows(380, None)
    r1 = new("#3A2214", W1, h[0], crossed_hands(W1, h[0]),
             cap(v("48:13"), "left: 12px; top: 12px", size=10.5, maxw=330) + cap(v("48:14"), "right: 12px; top: 12px", size=10.5, maxw=330) + vref("GEN 48:13–14", "right: 12px; bottom: 34px"))
    r2 = new(LAMP, W1, h[1], fc(ISRAEL_OLD, h[1], w=W1),
             cap(v("48:15", to="and said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("48:15", frm="The God before") + " " + v("48:16"), "left: 270px; top: 46px", 410, size=13, pad="40px 42px") + vref("GEN 48:15–16", "left: 12px; bottom: 12px"))
    return page("Genesis 48:13–16 — Guiding His Hands Wittingly", t, r1 + r2, START + 2)


@P("GEN-C17-P04-Ephraim", "254 · He Set Ephraim before Manasseh")
def p04():
    t, h = rows(270, 260, None)
    r1 = talk(V12.JOSEPH_EG, h[0], COURT, [("cap", v("48:17")), ("cap", v("48:18", to="unto his father,")), ("say", v("48:18", frm="Not so"))], ref="GEN 48:17–18")
    r2 = talk(ISRAEL_OLD, h[1], LAMP, [("cap", v("48:19", to="and said,")), ("say", v("48:19", frm="I know it"))], ref="GEN 48:19")
    r3 = cols(new(GOLDEN, W2, h[2], fc(EPHRAIM, h[2]),
                  cap(v("48:20", to="saying,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("48:20", frm="In thee", to="Manasseh:"), "right: 8px; top: 64px", 210, size=11.5, pad="18px 18px")
                  + cap(v("48:20", frm="and he set"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("GEN 48:20", "left: 8px; bottom: 8px")),
              talk(ISRAEL_DYING, h[2], COLD, [("cap", v("48:21", to="unto Joseph,")), ("say", v("48:21", frm="Behold") + " " + v("48:22"))], w=W2, ref="GEN 48:21–22", size=11))
    return page("Genesis 48:17–22 — He Set Ephraim before Manasseh", t, r1 + r2 + r3, START + 3)


@P("GEN-C17-P05-Gather", "255 · Gather Yourselves Together")
def p05():
    t, h = rows(300, None)
    r1 = new("#3A2214", W1, h[0], defs("c175a", *ALL) + J7_tent(W1, h[0]) + Y.ground(W1, h[0], h[0] * 0.9, "#2A1408", dy=0)
             + "".join(T.figure("c175a", ("man", c), W1 * (0.06 + i * 0.075), h[0] * 0.9, Y.fit(h[0] * 0.9, h[0] * 0.5)) for i, c in enumerate((U.BROS * 2)[:12])),
             cap(v("49:1", to="and said:"), "left: 12px; top: 12px", size=11) + vref("GEN 49:1", "right: 12px; top: 12px"))
    r2 = new(LAMP, W1, h[1], face(ISRAEL_DYING, -60, h[1] - 560, 1.4),
             balloon(v("49:1", frm="Gather") + " " + v("49:2"), "left: 300px; top: 30px", 390, size=14.5, pad="40px 40px") + vref("GEN 49:1–2", "left: 12px; bottom: 12px"))
    return page("Genesis 49:1–2 — Gather Yourselves Together", t, r1 + r2, START + 4)


def tribes(items, title, num, head=None):
    cells = [clan(nm, txt, ref, c, size=sz) for nm, txt, ref, c, sz in items]
    body = grid(cells, "repeat(3, minmax(0, 1fr))")
    tag = (f'\n  <div data-label style="position: absolute; left: 26px; right: 26px; top: 8px; text-align: center; font-size: 9px; font-weight: 600; '
           f'letter-spacing: 0.24em; color: #6B6862">THE BLESSING OF JACOB · GENESIS 49</div>')
    return page(title, "minmax(0, 1fr)", body + tag, num)


@P("GEN-C17-P06-Tribes1", "256 · Reuben, Thou Art My First-born")
def p06():
    return tribes([("Reuben", v("49:3") + " " + v("49:4"), "GEN 49:3–4", LEAH_C, 13),
                   ("Simeon · Levi", v("49:5") + " " + v("49:6") + " " + v("49:7"), "GEN 49:5–7", LEAH_C, 11.5),
                   ("Judah", v("49:8") + " " + v("49:9"), "GEN 49:8–9", "#FFD23F", 12.5),
                   ("Judah", v("49:10") + " " + v("49:11") + " " + v("49:12"), "GEN 49:10–12", "#FFD23F", 12),
                   ("Zebulun", v("49:13"), "GEN 49:13", LEAH_C, 15),
                   ("Issachar", v("49:14") + " " + v("49:15"), "GEN 49:14–15", LEAH_C, 13.5)],
                  "Genesis 49:3–15 — Reuben, Thou Art My First-born", START + 5)


@P("GEN-C17-P07-Tribes2", "257 · Joseph Is a Fruitful Bough")
def p07():
    return tribes([("Dan", v("49:16") + " " + v("49:17") + " " + v("49:18"), "GEN 49:16–18", BILHAH_C, 13),
                   ("Gad · Asher · Naphtali", v("49:19") + " " + v("49:20") + " " + v("49:21"), "GEN 49:19–21", ZILPAH_C, 13),
                   ("Joseph", v("49:22") + " " + v("49:23") + " " + v("49:24"), "GEN 49:22–24", RACHEL_C, 12),
                   ("Joseph", v("49:25"), "GEN 49:25", RACHEL_C, 13),
                   ("Joseph", v("49:26"), "GEN 49:26", RACHEL_C, 13),
                   ("Benjamin", v("49:27"), "GEN 49:27", RACHEL_C, 14)],
                  "Genesis 49:16–27 — Joseph Is a Fruitful Bough", START + 6)


@P("GEN-C17-P08-Gathered", "258 · He Was Gathered unto His People")
def p08():
    t, h = rows(190, None, 220)
    r1 = new(NIGHT, W1, h[0], L_sons(W1, h[0]), cap(v("49:28"), "left: 12px; top: 12px", size=11, maxw=600) + vref("GEN 49:28", "right: 12px; bottom: 10px"))
    r2 = new(LAMP, W1, h[1], fc(ISRAEL_DYING, h[1], w=W1),
             cap(v("49:29", to="said unto them,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("49:29", frm="I am to be") + " " + v("49:30") + " " + v("49:31") + " " + v("49:32"), "left: 270px; top: 46px", 410, size=12.5, pad="40px 40px") + vref("GEN 49:29–32", "left: 12px; bottom: 12px"))
    r3 = new("#12090A", W1, h[2], J7_tent(W1, h[2]).replace('opacity="0.3"', 'opacity="0.08"')
             + f'<rect x="{W1 * 0.3:.0f}" y="{h[2] * 0.7:.0f}" width="{W1 * 0.5:.0f}" height="30" rx="6" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + f'<path d="M{W1 * 0.32:.0f} {h[2] * 0.7:.0f} C {W1 * 0.4:.0f} {h[2] * 0.6:.0f} {W1 * 0.7:.0f} {h[2] * 0.6:.0f} {W1 * 0.78:.0f} {h[2] * 0.7:.0f} Z" fill="#5A6E8A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + f'<circle cx="{W1 * 0.76:.0f}" cy="{h[2] * 0.66:.0f}" r="14" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></circle>',
             cap(v("49:33"), "left: 12px; top: 12px", size=12.5, maxw=500) + vref("GEN 49:33", "right: 12px; bottom: 12px"))
    return page("Genesis 49:28–33 — He Was Gathered unto His People", t, r1 + r2 + r3, START + 7)

def L_sons(w, h):
    from genesis import art8 as L
    return L.sons_ring(w, h, 1781, ["REUBEN", "SIMEON", "LEVI", "JUDAH", "DAN", "NAPHTALI", "GAD", "ASHER", "ISSACHAR", "ZEBULUN", "JOSEPH", "BENJAMIN"], hi=None)


@P("GEN-C17-P09-Embalmed", "259 · Threescore and Ten Days")
def p09():
    t, h = rows(300, None)
    r1 = new(COLD, W1, h[0], fc(V12.JOSEPH_EG_WEEP, h[0], w=W1),
             cap(v("50:1"), "left: 300px; top: 12px", size=11.5, maxw=380)
             + cap(v("50:2") + " " + v("50:3"), "left: 300px; top: 70px", size=10.5, maxw=380) + hud("70 DAYS", "right: 14px; bottom: 14px", size=22) + vref("GEN 50:1–3", "left: 12px; bottom: 12px"))
    r2 = talk(V12.JOSEPH_EG, h[1], COURT, [("cap", v("50:4", to="saying,")), ("say", v("50:4", frm="If now") + " " + v("50:5")),
                                            ("cap", v("50:6", to="Pharaoh said,")), ("say", v("50:6", frm="Go up"))], ref="GEN 50:4–6")
    return page("Genesis 50:1–6 — Threescore and Ten Days", t, r1 + r2, START + 8)


@P("GEN-C17-P10-Atad", "260 · A Very Great Company")
def p10():
    t, h = rows(280, 280, None)
    r1 = new(SAND, W1, h[0], defs("c1710a", *ALL) + funeral("c1710a", W1, h[0], 17101),
             cap(v("50:7") + " " + v("50:8") + " " + v("50:9"), "left: 12px; top: 12px", size=10.5, maxw=520) + vref("GEN 50:7–9", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], atad(None, W1, h[1], 17102),
             cap(v("50:10"), "left: 12px; top: 12px", size=10, maxw=330)
             + cap(v("50:11", to="they said,"), "right: 12px; top: 12px", size=10, maxw=310)
             + balloon(v("50:11", frm="This is", to="Egyptians:"), "right: 12px; top: 84px", 260, size=11.5, pad="14px 18px")
             + cap(v("50:11", frm="wherefore"), "left: 12px; top: 120px", size=10.5, maxw=300) + vref("GEN 50:10–11", "left: 12px; bottom: 12px"))
    r3 = new(GREEN, W1, h[2], K.machpelah(None, W1, h[2], 17103),
             cap(v("50:12") + " " + v("50:13"), "left: 12px; top: 12px", size=10.5, maxw=420) + cap(v("50:14"), "left: 12px; top: 120px", size=10, maxw=320) + vref("GEN 50:12–14", "left: 12px; bottom: 12px"))
    return page("Genesis 50:7–14 — A Very Great Company", t, r1 + r2 + r3, START + 9)


@P("GEN-C17-P11-Forgive", "261 · Forgive, I Pray Thee")
def p11():
    t, h = rows(300, 220, None)
    r1 = talk(U.BROTHER, h[0], RED, [("cap", v("50:15", to="they said,")), ("say", v("50:15", frm="It may be")), ("cap", v("50:16", to="saying,")),
                                       ("say", v("50:16", frm="Thy father") + " " + v("50:17", to="God of thy father."))], ref="GEN 50:15–17")
    r2 = new(COURT, W1, h[1], fc(V12.JOSEPH_EG_WEEP, h[1], w=W1), cap(v("50:17", frm="And Joseph wept"), "left: 300px; top: 30px", size=14) + vref("GEN 50:17", "left: 12px; bottom: 12px"))
    r3 = new(COURT, W1, h[2], defs("c1711c", *ALL) + T.stage("c1711c", W1, h[2], 17113, "palace", [("joseph_eg", 0.86, 0.36, True)],
                                                                 props="".join(Z.E.kneel(W1 * (0.08 + i * 0.07), h[2] * 0.9, round(h[2] / 560, 3), color=c, skin=Y.SKIN) for i, c in enumerate((U.BROS * 2)[:10]))),
             cap(v("50:18", to="they said,"), "left: 12px; top: 12px", size=10.5, maxw=380)
             + balloon(v("50:18", frm="Behold"), "left: 12px; top: 66px", 240, size=13, pad="14px 18px") + vref("GEN 50:18", "right: 12px; top: 12px"))
    return page("Genesis 50:15–18 — Forgive, I Pray Thee", t, r1 + r2 + r3, START + 10)


@P("GEN-C17-P12-MeantGood", "262 · God Meant It for Good")
def p12():
    t, h = rows(None)
    r1 = new("radial-gradient(circle at 70% 30%, #FFF4C2 0 40px, #FFC14D 260px, #8A4A3A 680px)", W1, h[0], face(V12.JOSEPH_EG, -60, h[0] - 560, 1.4),
             cap(v("50:19", to="unto them,"), "left: 330px; top: 16px", size=11.5)
             + balloon(v("50:19", frm="Fear not") + " " + v("50:20") + " " + v("50:21", to="little ones."), "left: 300px; top: 60px", 390, size=15, pad="56px 44px")
             + cap(v("50:21", frm="And he comforted"), "left: 330px; top: 520px", size=12, maxw=360) + vref("GEN 50:19–21", "left: 12px; bottom: 12px"))
    return page("Genesis 50:19–21 — God Meant It for Good", t, r1, START + 11)


@P("GEN-C17-P13-End", "263 · So Joseph Died")
def p13():
    t, h = rows(230, 280, None)
    r1 = new(GREEN, W1, h[0], defs("c1713a", *ALL) + goshen("c1713a", W1, h[0], 17131),
             cap(v("50:22"), "left: 12px; top: 12px", size=11, maxw=400) + cap(v("50:23"), "right: 12px; bottom: 34px", size=10.5, maxw=320)
             + hud("110", "left: 14px; bottom: 30px", size=26) + vref("GEN 50:22–23", "right: 12px; bottom: 10px"))
    r2 = talk(JOSEPH_OLD, h[1], GOLDEN, [("cap", v("50:24", to="unto his brethren,")), ("say", v("50:24", frm="I die;")), ("cap", v("50:25", to="saying,")), ("say", v("50:25", frm="God will"))], ref="GEN 50:24–25")
    r3 = new("#12090A", W1, h[2], coffin(W1, h[2], 17133),
             cap(v("50:26"), "left: 12px; top: 12px", size=13, maxw=520)
             + end_mark("END OF GENESIS · NEXT · EXODUS", "right: 14px; bottom: 12px", ch="完") + vref("GEN 50:26", "left: 12px; bottom: 12px"))
    return page("Genesis 50:22–26 — So Joseph Died", t, r1 + r2 + r3, START + 12)
