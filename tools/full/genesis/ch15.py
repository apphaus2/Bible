"""Genesis volume, Chapter 15 — I Am Joseph (Genesis 44–45). Every verse, word for word from ref/asv.
Judah's plea (44:18–34) is kept in full across three pages: it retells the story, but it is the turning point.
Reuses the digest's "I am Joseph" close-up."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art10 as T, art11 as U, art12 as V12
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from genesis.ch12 import COURT
from genesis.ch14 import talk, BENJAMIN, STEWARD, ISRAEL
from mk import defs, face

v, sp = G.v, G.span
B5 = "digest/genesis/book-05/"
Jos, = (panels(B5 + n + ".dc.html") for n in ["B5-P08-Joseph"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
START = 229                                  # chapter 14 ends on page 228
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cup(w, h, seed):
    """The silver cup in the mouth of the youngest's sack."""
    import ruth1 as R
    return (f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#12113A"></rect>' + Z.V.rays(w * 0.5, h * 0.5, 30, 20, w, color="#C8C8D0", op=0.2)
            + R.sack(w * 0.5, h * 0.92, h / 80)
            + f'<path d="M{w * 0.42:.0f} {h * 0.3:.0f} L {w * 0.58:.0f} {h * 0.3:.0f} L {w * 0.54:.0f} {h * 0.46:.0f} L {w * 0.52:.0f} {h * 0.48:.0f} L {w * 0.52:.0f} {h * 0.56:.0f} '
              f'L {w * 0.56:.0f} {h * 0.58:.0f} L {w * 0.44:.0f} {h * 0.58:.0f} L {w * 0.48:.0f} {h * 0.56:.0f} L {w * 0.48:.0f} {h * 0.48:.0f} L {w * 0.46:.0f} {h * 0.46:.0f} Z" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="2.4"></path>')

def sacks_opened(p, w, h, seed):
    """They took down every man his sack, and he searched from the eldest to the youngest: the cup found in Benjamin's sack."""
    import ruth1 as R
    b = h * 0.88
    o = [Z.sun(w * 0.9, h * 0.2, 14, op=0.25), Y.ground(w, h, b, "#C8A06A", dy=0)]
    for i in range(11):
        x = w * (0.05 + i * 0.09)
        o.append(R.sack(x, b + 4, 1.1))
    o.append(f'<path d="M{w * 0.95 - 10:.0f} {b - 54:.0f} l 20 0 l -4 14 l -12 0 Z" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="1.6"></path>' + Z.V.rays(w * 0.95, b - 50, 16, 8, 40, color="#FFF4C2", op=0.6))
    o.append(T.figure(p, ("egypt", "#E8D8B0"), w * 0.8, b - 30, Y.fit(b - 30, h * 0.2), flip=True, pose="point"))
    return "".join(o)

def cause_out(p, w, h, seed):
    """Cause every man to go out from me: the Egyptians leaving the hall, Joseph alone with the eleven."""
    b = h * 0.9
    return T.stage(p, w, h, seed, "palace", [("joseph_eg", 0.5, 0.3)] + [(("egypt", "#F3EFE6"), x, 0.46, x > 0.5) for x in (0.08, 0.16, 0.86, 0.94)]
                   + [(("man", c), 0.28 + i * 0.03, 0.56) for i, c in enumerate(U.BROS[:4])] + [(("man", c), 0.64 + i * 0.03, 0.56, True) for i, c in enumerate(U.BROS[2:6])])

def embrace(p, w, h, seed):
    """He fell upon his brother Benjamin's neck, and wept."""
    b = h * 0.9; s = Y.fit(b, h * 0.36); arm = [(-22, -158), (2, -150), (22, -164)]
    return (T.stage(p, w, h, seed, "palace", [("joseph_eg", 0.46, 0.36, False, arm), ("benjamin", 0.56, 0.38, True, arm)])
            + "".join(T.figure(p, ("man", c), w * x, b, Y.fit(b, h * 0.42), flip=x > 0.5) for x, c in [(0.18, U.BROS[0]), (0.26, U.BROS[1]), (0.74, U.BROS[2]), (0.82, U.BROS[3])]))

def wagons(p, w, h, seed):
    """Joseph gave them wagons, and provision for the way; ten asses laden with the good things of Egypt."""
    import ruth1 as R, exodus3 as E3, numbers1 as N
    b = h * 0.86
    cart = lambda x: (f'<rect x="{x - 50:.0f}" y="{b - 46:.0f}" width="100" height="30" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
                      f'<circle cx="{x - 30:.0f}" cy="{b - 10:.0f}" r="14" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></circle><circle cx="{x + 30:.0f}" cy="{b - 10:.0f}" r="14" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></circle>'
                      + R.sack(x - 20, b - 46, 0.7) + R.sack(x + 14, b - 46, 0.6))
    return (Z.sun(w * 0.1, h * 0.24, 16, color="#FFE680", op=0.3) + Y.ground(w, h, b, "#C8A06A", dy=0)
            + cart(w * 0.2) + cart(w * 0.42) + "".join(N.ass(w * (0.58 + i * 0.07), b + 4, 0.16) + R.sack(w * (0.58 + i * 0.07) - 4, b - 24, 0.4) for i in range(6)))


@P("GEN-C15-00-Title", "Chapter 15 · I Am Joseph")
def title():
    burst = mk.speed(380, 640, 90, 120, 900, 15, color="#FFC14D", sw=2, op=0.5)
    return chapter_title(15, "第十五話", "I Am Joseph", "Genesis 44 – 45", burst + face(V12.JOSEPH_EG_WEEP, -60, 400, 1.5), NIGHT,
                         v("45:3", frm="I am Joseph;", to="yet live?"), "Genesis · Volume One")


@P("GEN-C15-P01-Cup", "229 · My Cup, the Silver Cup")
def p01():
    t, h = rows(380, None)
    r1 = talk(V12.JOSEPH_EG, h[0], COURT, [("cap", v("44:1", to="saying,")), ("say", v("44:1", frm="Fill the") + " " + v("44:2", to="grain money.")),
                                            ("cap", v("44:2", frm="And he did"))], ref="GEN 44:1–2")
    r2 = cols(new("#12113A", W2, h[1], cup(W2, h[1], 1512), cap(v("44:3"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 44:3", "right: 8px; bottom: 8px")),
              talk(V12.JOSEPH_EG_STERN, h[1], COURT, [("cap", v("44:4", to="unto his steward,")), ("say", v("44:4", frm="Up, follow") + " " + v("44:5"))], w=W2, ref="GEN 44:4–5", size=11.5))
    return page("Genesis 44:1–5 — My Cup, the Silver Cup", t, r1 + r2, START + 0)


@P("GEN-C15-P02-Search", "230 · Found in Benjamin's Sack")
def p02():
    t, h = rows(300, 250, None)
    r1 = talk(U.BROTHER, h[0], RED, [("cap", v("44:6") + " " + v("44:7", to="unto him,")), ("say", v("44:7", frm="Wherefore") + " " + v("44:8") + " " + v("44:9"))], ref="GEN 44:6–9")
    r2 = talk(STEWARD, h[1], COURT, [("cap", v("44:10", to="he said,")), ("say", v("44:10", frm="Now also"))], ref="GEN 44:10")
    r3 = new(SAND, W1, h[2], defs("c152c", *ALL) + sacks_opened("c152c", W1, h[2], 1523),
             cap(v("44:11") + " " + v("44:12"), "left: 12px; top: 12px", size=11, maxw=440)
             + cap(v("44:13"), "left: 12px; top: 96px", size=10.5, maxw=360) + vref("GEN 44:11–13", "right: 12px; top: 12px"))
    return page("Genesis 44:6–13 — Found in Benjamin's Sack", t, r1 + r2 + r3, START + 1)


@P("GEN-C15-P03-Bondmen", "231 · We Are My Lord's Bondmen")
def p03():
    t, h = rows(210, 260, None)
    r1 = new(COURT, W1, h[0], defs("c153a", *ALL) + T.stage("c153a", W1, h[0], 1531, "palace", [("joseph_eg", 0.86, 0.32, True)],
                                                             props="".join(Z.E.kneel(W1 * (0.08 + i * 0.065), h[0] * 0.9, round(h[0] / 620, 3), color=c, skin=Y.SKIN) for i, c in enumerate((U.BROS * 2)[:11]))),
             cap(v("44:14"), "left: 12px; top: 12px", size=11, maxw=440) + vref("GEN 44:14", "right: 12px; bottom: 12px"))
    r2 = talk(V12.JOSEPH_EG_STERN, h[1], COURT, [("cap", v("44:15", to="unto them,")), ("say", v("44:15", frm="What deed")),
                                                ("cap", v("44:17", to="he said,")), ("say", v("44:17", frm="Far be"))], ref="GEN 44:15, 17")
    r3 = talk(U.JUDAH, h[2], RUST, [("cap", v("44:16", to="Judah said,")), ("say", v("44:16", frm="What shall"))], ref="GEN 44:16")
    return page("Genesis 44:14–17 — We Are My Lord's Bondmen", t, r1 + r2 + r3, START + 2)


def judah(refs, page_title, num):
    t, h = rows(None)
    lines = []
    for r in refs:
        if r == "44:18":
            lines += [("cap", v("44:18", to="and said,")), ("say", v("44:18", frm="Oh, my lord"))]
        else:
            lines += [("say", v(r))]
    merged, buf = [], []
    for k, tx in lines:
        if k == "say": buf.append(tx)
        else:
            if buf: merged.append(("say", " ".join(buf))); buf = []
            merged.append((k, tx))
    if buf: merged.append(("say", " ".join(buf)))
    r1 = new(RUST, W1, h[0], face(U.JUDAH, -80, h[0] - 560, 1.4),
             "".join(cap(tx, f"left: 330px; top: {16 + i * 56}px", size=11, maxw=360) if k == "cap" else
                     balloon(tx, f"left: 290px; top: {60 if i else 16}px", 410, size=13, pad="70px 52px") for i, (k, tx) in enumerate(merged))
             + vref(f"GEN {refs[0]}–{refs[-1].split(':')[1]}", "left: 12px; bottom: 12px"))
    return page(page_title, t, r1, num)


@P("GEN-C15-P04-Judah1", "232 · Oh, My Lord")
def p04():
    return judah(["44:18", "44:19", "44:20", "44:21", "44:22"], "Genesis 44:18–22 — Oh, My Lord", START + 3)


@P("GEN-C15-P05-Judah2", "233 · Ye Know That My Wife Bare Me Two Sons")
def p05():
    return judah(["44:23", "44:24", "44:25", "44:26", "44:27", "44:28", "44:29"], "Genesis 44:23–29 — Ye Know That My Wife Bare Me Two Sons", START + 4)


@P("GEN-C15-P06-Judah3", "234 · Let Thy Servant Abide instead of the Lad")
def p06():
    return judah(["44:30", "44:31", "44:32", "44:33", "44:34"], "Genesis 44:30–34 — Let Thy Servant Abide instead of the Lad", START + 5)


@P("GEN-C15-P07-IAmJoseph", "235 · I Am Joseph")
def p07():
    t, h = rows(250, 560, None)
    r1 = new(COURT, W1, h[0], defs("c157a", *ALL) + cause_out("c157a", W1, h[0], 1571),
             cap(v("45:1", to="and he cried,"), "left: 12px; top: 12px", size=10.5, maxw=380)
             + balloon(v("45:1", frm="Cause every", to="from me."), "right: 12px; top: 12px", 220, size=12.5, pad="14px 18px")
             + cap(v("45:1", frm="And there stood"), "right: 12px; top: 96px", size=10.5, maxw=260) + vref("GEN 45:1", "left: 12px; bottom: 12px"))
    r2 = new("repeating-conic-gradient(from 0deg at 40% 60%, #FFC14D 0deg 3deg, #E8705A 3deg 6deg)", W1, h[1],
             mk.speed(W1 * 0.4, h[1] * 0.6, 80, 100, 800, 1572, color="#FFF4C2", sw=1.6, op=0.4) + face(V12.JOSEPH_EG_WEEP, -40, h[1] - 520, 1.36),
             cap(v("45:2"), "left: 12px; top: 12px", size=12) + cap(v("45:3", to="unto his brethren,"), "left: 12px; top: 60px", size=11)
             + balloon(v("45:3", frm="I am Joseph;", to="yet live?"), "right: 12px; top: 220px", 300, size=17, pad="22px 28px")
             + sfx("ううっ", "UU", "right: 24px; top: 60px", size=60, fill="#F3EFE6", stroke="#7A3A3A", rot=-4) + vref("GEN 45:2–3", "left: 12px; bottom: 12px"))
    r3 = new(RED, W1, h[2], defs("c157c", *ALL) + T.stage("c157c", W1, h[2], 1573, "palace", [(("man", c), 0.12 + i * 0.12, 0.44, False) for i, c in enumerate(U.BROS)]),
             cap(v("45:3", frm="And his brethren"), "left: 12px; top: 12px", size=11.5, maxw=500) + vref("GEN 45:3", "right: 12px; top: 12px"))
    return page("Genesis 45:1–3 — I Am Joseph", t, r1 + r2 + r3, START + 6)


@P("GEN-C15-P08-SentMe", "236 · God Did Send Me before You")
def p08():
    t, h = rows(None)
    r1 = new(COURT, W1, h[0], face(V12.JOSEPH_EG_WEEP, -80, h[0] - 560, 1.4),
             cap(v("45:4", to="his brethren,"), "left: 330px; top: 16px", size=11, maxw=360)
             + balloon(v("45:4", frm="Come near", to="I pray you."), "left: 320px; top: 60px", 260, size=13, pad="16px 20px")
             + cap(v("45:4", frm="And they came near.", to="he said,"), "left: 330px; top: 140px", size=11, maxw=360)
             + balloon(v("45:4", frm="I am Joseph your") + " " + v("45:5") + " " + v("45:6") + " " + v("45:7") + " " + v("45:8"), "left: 300px; top: 200px", 390, size=13.5, pad="56px 44px")
             + vref("GEN 45:4–8", "left: 12px; bottom: 12px"))
    return page("Genesis 45:4–8 — God Did Send Me before You", t, r1, START + 7)


@P("GEN-C15-P09-Goshen", "237 · Thou Shalt Dwell in the Land of Goshen")
def p09():
    t, h = rows(None, 280)
    r1 = new(COURT, W1, h[0], fc(V12.JOSEPH_EG, h[0], w=W1),
             balloon(v("45:9") + " " + v("45:10") + " " + v("45:11") + " " + v("45:12") + " " + v("45:13"), "left: 260px; top: 20px", 420, size=13, pad="50px 44px")
             + vref("GEN 45:9–13", "left: 12px; bottom: 12px"))
    r2 = new(COURT, W1, h[1], defs("c159b", *ALL) + embrace("c159b", W1, h[1], 1592),
             cap(v("45:14"), "left: 12px; top: 12px", size=11, maxw=330) + cap(v("45:15"), "right: 12px; top: 12px", size=10.5, maxw=300) + vref("GEN 45:14–15", "right: 12px; bottom: 12px"))
    return page("Genesis 45:9–15 — Thou Shalt Dwell in the Land of Goshen", t, r1 + r2, START + 8)


@P("GEN-C15-P10-Wagons", "238 · Take You Wagons out of the Land of Egypt")
def p10():
    t, h = rows(None, 250)
    r1 = new(COURT, W1, h[0], fc(V12.PHARAOH, h[0], w=W1),
             cap(v("45:16", to="saying,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("45:16", frm="Joseph's brethren", to="are come:"), "left: 300px; top: 66px", 240, size=12.5, pad="14px 18px")
             + cap(v("45:16", frm="and it pleased") + " " + v("45:17", to="unto Joseph,"), "left: 320px; top: 140px", size=10.5, maxw=360)
             + balloon(v("45:17", frm="Say unto") + " " + v("45:18") + " " + v("45:19") + " " + v("45:20"), "left: 270px; top: 230px", 410, size=12.5, pad="40px 40px")
             + vref("GEN 45:16–20", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], wagons(None, W1, h[1], 15102),
             cap(v("45:21"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("GEN 45:21", "right: 12px; top: 12px"))
    return page("Genesis 45:16–21 — Take You Wagons out of the Land of Egypt", t, r1 + r2, START + 9)


@P("GEN-C15-P11-Revived", "239 · Joseph My Son Is Yet Alive")
def p11():
    t, h = rows(210, 220, None)
    r1 = new(SAND, W1, h[0], wagons(None, W1, h[0], 15111),
             cap(v("45:22") + " " + v("45:23"), "left: 12px; top: 12px", size=10.5, maxw=520) + hud("300", "right: 14px; top: 12px", size=24) + vref("GEN 45:22–23", "right: 12px; bottom: 12px"))
    r2 = talk(V12.JOSEPH_EG, h[1], COURT, [("cap", v("45:24", to="unto them,")), ("say", v("45:24", frm="See that")), ("cap", v("45:25"))], ref="GEN 45:24–25")
    r3 = talk(ISRAEL, h[2], GOLDEN, [("cap", v("45:26", to="saying,")), ("say", v("45:26", frm="Joseph is", to="land of Egypt.")), ("cap", v("45:26", frm="And his heart") + " " + v("45:27")),
                                      ("cap", v("45:28", to="Israel said,")), ("say", v("45:28", frm="It is enough"))], ref="GEN 45:26–28",
              extra=end_mark("NEXT · ISRAEL IN EGYPT", "right: 14px; bottom: 12px"))
    return page("Genesis 45:22–28 — Joseph My Son Is Yet Alive", t, r1 + r2 + r3, START + 10)
