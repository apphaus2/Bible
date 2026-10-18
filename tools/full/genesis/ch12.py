"""Genesis volume, Chapter 12 — The Captain of the Guard (Genesis 39–40). Every verse, word for word from ref/asv.
39:7–18 is given in full; the drawings are faces, the empty doorway and the garment in her hand."""
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
from genesis.ch07 import LAMP, RED, BLUE
from mk import defs, face

v, sp = G.v, G.span
B5 = "reference/genesis/book-05/"
Pri, = (panels(B5 + n + ".dc.html") for n in ["B5-P04-Prison"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
NILE = "radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #E8B830 180px, #6A3A12 420px)"
COURT = "radial-gradient(circle at 70% 30%, #FFE680 0 20px, #5A8AC8 180px, #12305A 420px)"
CELL = "radial-gradient(circle at 70% 25%, #FFF4C2 0 20px, #6A5A4A 180px, #12090A 420px)"
START = 197                                  # chapter 11 ends on page 196
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("GEN-C12-00-Title", "Chapter 12 · The Captain of the Guard")
def title():
    return chapter_title(12, "第十二話", "The Captain of the Guard", "Genesis 39 – 40", f'<g transform="translate(-400 -60) scale(2.4)">{Pri[1].svg}</g>', NIGHT,
                         v("39:21", to="with Joseph,"), "Genesis · Volume One")


@P("GEN-C12-P01-Overseer", "197 · Jehovah Was with Joseph")
def p01():
    t, h = rows(250, 330, None)
    r1 = use(Pri[0], over=cap(v("39:1"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("GEN 39:1", "right: 12px; bottom: 12px"))
    r2 = new(V12.EGYPT_BG, W1, h[1], defs("c121b", *ALL) + V12.house_of_potiphar("c121b", W1, h[1], 1212),
             cap(v("39:2") + " " + v("39:3"), "left: 12px; top: 12px", size=10.5, maxw=400)
             + cap(v("39:4"), "right: 12px; bottom: 34px", size=10.5, maxw=300) + vref("GEN 39:2–4", "left: 12px; bottom: 12px"))
    r3 = cols(new(COURT, W2, h[2], fc(V12.POTIPHAR, h[2]), cap(v("39:5"), "right: 8px; top: 8px", size=9.5, maxw=210) + vref("GEN 39:5", "left: 8px; bottom: 8px")),
              new(GLOW, W2, h[2], fc(V12.JOSEPH, h[2]), cap(v("39:6"), "right: 8px; top: 8px", size=10, maxw=200) + vref("GEN 39:6", "left: 8px; bottom: 8px")))
    return page("Genesis 39:1–6 — Jehovah Was with Joseph", t, r1 + r2 + r3, START + 0)


@P("GEN-C12-P02-Refused", "198 · How Then Can I Do This Great Wickedness?")
def p02():
    t, h = rows(250, 380, None)
    r1 = new(EMBER, W1, h[0], fc(V12.WIFE, h[0], w=W1),
             cap(v("39:7", to="and she said,"), "left: 300px; top: 12px", size=11, maxw=380)
             + balloon(v("39:7", frm="Lie with"), "left: 290px; top: 100px", 200, size=14, pad="14px 18px") + vref("GEN 39:7", "left: 12px; bottom: 12px"))
    r2 = new(GLOW, W1, h[1], fc(V12.JOSEPH_FIRM, h[1], w=W1),
             cap(v("39:8", to="master's wife,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("39:8", frm="Behold") + " " + v("39:9"), "left: 260px; top: 46px", 420, size=12.5, pad="36px 42px") + vref("GEN 39:8–9", "left: 12px; bottom: 12px"))
    r3 = new("#5A3A22", W1, h[2], defs("c122c", *ALL) + V12.house_of_potiphar("c122c", W1, h[2], 1223, joseph_top=0.5),
             cap(v("39:10"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 39:10", "right: 12px; top: 12px"))
    return page("Genesis 39:7–10 — How Then Can I Do This Great Wickedness?", t, r1 + r2 + r3, START + 1)


@P("GEN-C12-P03-Garment", "199 · He Left His Garment in Her Hand")
def p03():
    t, h = rows(370, None)
    r1 = new("#5A3A22", W1, h[0], defs("c123a", *ALL) + V12.garment("c123a", W1, h[0], 1231),
             cap(v("39:11"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + cap(v("39:12", to="saying,"), "left: 12px; top: 96px", size=10.5)
             + balloon(v("39:12", frm="Lie with", to="with me:"), "left: 12px; top: 130px", 170, size=13, pad="12px 14px")
             + cap(v("39:12", frm="and he left"), "right: 12px; top: 12px", size=11, maxw=200)
             + sfx("バッ", "BAH", "right: 30px; bottom: 30px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("GEN 39:11–12", "left: 12px; bottom: 12px"))
    r2 = new(EMBER, W1, h[1], fc(V12.WIFE_SCHEME, h[1], w=W1),
             cap(v("39:13") + " " + v("39:14", to="saying,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("39:14", frm="See, he") + " " + v("39:15"), "left: 260px; top: 104px", 420, size=12.5, pad="32px 40px") + vref("GEN 39:13–15", "left: 12px; bottom: 12px"))
    return page("Genesis 39:11–15 — He Left His Garment in Her Hand", t, r1 + r2, START + 2)


@P("GEN-C12-P04-Prison", "200 · He Put Him into the Prison")
def p04():
    t, h = rows(210, 300, None)
    r1 = new("#5A3A22", W1, h[0], defs("c124a", *ALL) + V12.cried_out("c124a", W1, h[0], 1241),
             cap(v("39:16"), "right: 12px; top: 12px", size=11, maxw=320) + vref("GEN 39:16", "left: 12px; top: 12px"))
    r2 = new(EMBER, W1, h[1], fc(V12.WIFE_SCHEME, h[1], w=W1),
             cap(v("39:17", to="saying,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("39:17", frm="The Hebrew") + " " + v("39:18"), "left: 270px; top: 46px", 410, size=12.5, pad="30px 40px") + vref("GEN 39:17–18", "left: 12px; bottom: 12px"))
    r3 = cols(new(RED, W2, h[2], fc(V12.POTIPHAR_WROTH, h[2]),
                  cap(v("39:19", to="saying,"), "right: 8px; top: 8px", size=9.5, maxw=210)
                  + balloon(v("39:19", frm="After this", to="to me;"), "right: 8px; top: 110px", 200, size=12, pad="14px 16px")
                  + cap(v("39:19", frm="that his wrath"), "right: 8px; bottom: 8px", size=10.5) + vref("GEN 39:19", "left: 8px; bottom: 8px")),
              new(V12.JAIL, W2, h[2], defs("c124c", *ALL) + V12.prison("c124c", W2, h[2], 1243, figures=[("joseph_plain", 0.5, 0.4, False)]),
                  cap(v("39:20"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 39:20", "right: 8px; bottom: 8px")))
    return page("Genesis 39:16–20 — He Put Him into the Prison", t, r1 + r2 + r3, START + 3)


@P("GEN-C12-P05-Keeper", "201 · The Keeper of the Prison")
def p05():
    t, h = rows(380, None)
    r1 = use(Pri[1], over=cap(v("39:21"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 39:21", "right: 12px; bottom: 12px"))
    r2 = new(V12.JAIL, W1, h[1], defs("c125b", *ALL) + V12.prison("c125b", W1, h[1], 1252, figures=[("joseph_plain", 0.3, 0.42, False), (("eg", "#8A6A4A"), 0.5, 0.44, True)]
                                                                        + [(("shade", None), x, 0.5, x > 0.6) for x in (0.68, 0.78, 0.88)]),
             cap(v("39:22") + " " + v("39:23"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 39:22–23", "right: 12px; bottom: 12px"))
    return page("Genesis 39:21–23 — The Keeper of the Prison", t, r1 + r2, START + 4)


@P("GEN-C12-P06-Officers", "202 · Wherefore Look Ye So Sad To-day?")
def p06():
    t, h = rows(230, 320, None)
    r1 = new(COURT, W1, h[0], defs("c126a", *ALL) + T.stage("c126a", W1, h[0], 1261, "palace", [("pharaoh", 0.5, 0.36, True), (("egypt", "#F3EFE6"), 0.26, 0.44), (("egypt", "#E8D8B0"), 0.36, 0.44)]),
             cap(v("40:1") + " " + v("40:2"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 40:1–2", "right: 12px; bottom: 12px"))
    r2 = use(Pri[2], over=cap(v("40:3") + " " + v("40:4"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + cap(v("40:5"), "right: 12px; top: 12px", size=10, maxw=290) + vref("GEN 40:3–5", "right: 12px; bottom: 12px"))
    r3 = cols(new(CELL, W2, h[2], fc(V12.JOSEPH_PRISON, h[2]),
                  cap(v("40:6") + " " + v("40:7", to="saying,"), "right: 8px; top: 8px", size=9.5, maxw=210)
                  + balloon(v("40:7", frm="Wherefore"), "right: 8px; bottom: 10px", 200, size=12, pad="14px 16px") + vref("GEN 40:6–7", "left: 8px; bottom: 8px")),
              new(COLD, W2, h[2], fc(V12.BUTLER_SAD, h[2]),
                  cap(v("40:8", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("40:8", frm="We have", to="interpret it."), "right: 8px; top: 40px", 200, size=11.5, pad="16px 18px")
                  + cap(v("40:8", frm="And Joseph", to="unto them,"), "right: 8px; top: 146px", size=10, maxw=200)
                  + balloon(v("40:8", frm="Do not"), "right: 8px; bottom: 10px", 210, size=11.5, pad="16px 18px") + vref("GEN 40:8", "left: 8px; bottom: 8px")))
    return page("Genesis 40:1–8 — Wherefore Look Ye So Sad To-day?", t, r1 + r2 + r3, START + 5)


@P("GEN-C12-P07-Vine", "203 · Three Branches")
def p07():
    t, h = rows(370, None)
    r1 = new("#2A1A5E", W1, h[0], V12.vine(W1, h[0], 1271),
             cap(v("40:9", to="said to him,"), "left: 12px; top: 12px", size=10.5, maxw=500)
             + balloon(v("40:9", frm="In my dream") + " " + v("40:10") + " " + v("40:11"), "right: 12px; top: 60px", 330, size=11.5, pad="28px 36px") + vref("GEN 40:9–11", "left: 12px; bottom: 12px"))
    r2 = new(CELL, W1, h[1], fc(V12.JOSEPH_PRISON, h[1], w=W1),
             cap(v("40:12", to="unto him,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("40:12", frm="This is") + " " + v("40:13") + " " + v("40:14") + " " + v("40:15"), "left: 250px; top: 46px", 430, size=12, pad="38px 44px")
             + hud("3 DAYS", "right: 14px; bottom: 14px", size=22) + vref("GEN 40:12–15", "left: 12px; bottom: 12px"))
    return page("Genesis 40:9–15 — Three Branches", t, r1 + r2, START + 6)


@P("GEN-C12-P08-Baskets", "204 · Three Baskets")
def p08():
    t, h = rows(370, None)
    r1 = new("#3A1A1A", W1, h[0], V12.baskets(W1, h[0], 1281),
             cap(v("40:16", to="unto Joseph,"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + balloon(v("40:16", frm="I also") + " " + v("40:17"), "left: 12px; bottom: 14px", 300, size=11.5, pad="26px 32px") + vref("GEN 40:16–17", "right: 12px; bottom: 12px"))
    r2 = new(CELL, W1, h[1], fc(V12.JOSEPH_PRISON, h[1], w=W1),
             cap(v("40:18", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("40:18", frm="This is") + " " + v("40:19"), "left: 270px; top: 46px", 410, size=13, pad="34px 40px")
             + hud("3 DAYS", "right: 14px; bottom: 14px", size=22) + vref("GEN 40:18–19", "left: 12px; bottom: 12px"))
    return page("Genesis 40:16–19 — Three Baskets", t, r1 + r2, START + 7)


@P("GEN-C12-P09-Forgat", "205 · He Forgat Him")
def p09():
    t, h = rows(300, 200, None)
    r1 = new(COURT, W1, h[0], defs("c129a", *ALL) + V12.birthday("c129a", W1, h[0], 1291),
             cap(v("40:20"), "left: 12px; top: 12px", size=10.5, maxw=440)
             + cap(v("40:21"), "right: 12px; bottom: 30px", size=10.5, maxw=280) + vref("GEN 40:20–21", "left: 12px; bottom: 12px"))
    r2 = new("#3A1A1A", W1, h[1], V12.baskets(W1, h[1], 1292),
             cap(v("40:22"), "left: 12px; top: 12px", size=12) + vref("GEN 40:22", "right: 12px; bottom: 12px"))
    r3 = cols(new(COURT, W2, h[2], fc(V12.BUTLER, h[2]), cap(v("40:23"), "right: 8px; top: 8px", size=12, maxw=200) + vref("GEN 40:23", "left: 8px; bottom: 8px")),
              new(CELL, W2, h[2], fc(V12.JOSEPH_PRISON, h[2]), end_mark("NEXT · PHARAOH'S DREAMS", "right: 8px; bottom: 8px")))
    return page("Genesis 40:20–23 — He Forgat Him", t, r1 + r2 + r3, START + 8)
