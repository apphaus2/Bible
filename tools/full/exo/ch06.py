"""Exodus volume, Chapter 6 — Sinai (Exodus 19–21). Every verse, word for word from ref/asv.
The Ten Words get the digest's numbered panels; the ordinances of chapter 21 are pages of law cells (kit.law): God's
words in Voice boxes, each with a pictogram strip from art6."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art2 as B, art3 as C, art4 as D4, art5 as F5, art6 as S6
from exo.kit import talk, law
from exo.ch02 import night
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from mk import defs, face

v, sp = G.v, G.span
SI, IA, TW, AF = [panels("digest/exodus/book-04/" + n + ".dc.html") for n in ["EX4-P05-Sinai", "EX4-P06-IAm", "EX4-P07-TenWords", "EX4-P08-AfarOff"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
MOUNT = "linear-gradient(180deg, #1A0E2A 0%, #4A1D3A 55%, #C8682E 100%)"
WOMAN = A.tok("WOMAN")
START = 100                                  # chapter 5 ends on page 99
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def pic(fn, p):
    return defs(p, *ALL) + fn(p)

def ten(k, art, text, ref, pos="left: 12px; bottom: 12px", size=15, maxw=None):
    """A numbered commandment panel: the lifted digest art, the big kanji numeral, the Voice box."""
    return use(art, over=E4.numeral(k, "left: 10px; top: 6px", size=60) + god(text, pos, size=size, maxw=maxw) + vref(ref, "right: 8px; top: 8px"))


@P("EXO-C06-00-Title", "Chapter 6 · Sinai")
def title():
    a = SI[0]
    return chapter_title(6, "第六話", "Sinai", "Exodus 19 – 21", f'<g transform="translate(-30 0) scale(1.53)">{a.svg}</g>', a.bg,
                         v("19:18", to="in fire;"), "Exodus · Volume Two")


@P("EXO-C06-P01-Wings", "100 · On Eagles' Wings")
def p01():
    t, h = rows(230, 260, None)
    r1 = new("#0B1A2E", W1, h[0], A.exodus_map(W1, h[0], ["ELIM", "SINAI"], cur="SINAI", names=["THE RED SEA", "MARAH"]),
             cap(v("19:1") + " " + v("19:2"), "left: 12px; bottom: 12px", size=10.5, maxw=380) + mk.stamp(19, "right: 14px; top: 12px") + vref("EX 19:1–2", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], defs("x61b", *ALL) + S6.wings("x61b", W1, h[1], 1012),
             cap(v("19:3", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=440) + god(v("19:3", frm="Thus shalt") + " " + v("19:4"), "right: 12px; bottom: 12px", size=15, maxw=380) + vref("EX 19:3–4", "left: 12px; bottom: 12px"))
    r3 = new(MOUNT, W1, h[2], defs("x61c", *ALL) + S6.camp_before("x61c", W1, h[2], 1013), god(v("19:5") + " " + v("19:6"), "left: 12px; top: 12px", size=17, maxw=560) + vref("EX 19:5–6", "right: 12px; bottom: 12px"))
    return page("Exodus 19:1–6 — On Eagles' Wings", t, r1 + r2 + r3, START + 0)


@P("EXO-C06-P02-WeWillDo", "101 · All That Jehovah Hath Spoken We Will Do")
def p02():
    t, h = rows(240, 230, None)
    r1 = new(SAND, W1, h[0], defs("x62a", *ALL) + A.elders("x62a", W1, h[0], 1021, extra_cast=[(A.moses, 0.92, 0.42, True, "raise")]),
             cap(v("19:7") + " " + v("19:8", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=440) + balloon(v("19:8", frm="All that", to="we will do."), "left: 20px; top: 80px", 250, size=14, pad="14px 20px")
             + cap(v("19:8", frm="And Moses reported"), "right: 12px; top: 12px", size=10.5, maxw=180) + vref("EX 19:7–8", "right: 12px; bottom: 12px"))
    r2 = new(MOUNT, W1, h[1], E4.sinai(W1 * 0.6, h[1], W1 * 0.8, h[1] * 0.9, 1022, fire=False) + E3.pillar_cloud(W1 * 0.6, h[1] * 0.3, -20, W1 * 0.1, 1022),
             cap(v("19:9", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("19:9", frm="Lo, I come", to="for ever."), "left: 12px; top: 48px", size=15, maxw=380)
             + cap(v("19:9", frm="And Moses told"), "right: 12px; bottom: 14px", size=10.5, maxw=260) + vref("EX 19:9", "left: 12px; bottom: 12px"))
    r3 = new(MOUNT, W1, h[2], defs("x62c", *ALL) + S6.camp_before("x62c", W1, h[2], 1023, bounds=True),
             cap(v("19:10", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("19:10", frm="Go unto") + " " + v("19:11") + " " + v("19:12") + " " + v("19:13"), "left: 12px; top: 44px", size=13.5, maxw=660) + vref("EX 19:10–13", "right: 12px; bottom: 12px"))
    return page("Exodus 19:7–13 — All That Jehovah Hath Spoken We Will Do", t, r1 + r2 + r3, START + 1)


@P("EXO-C06-P03-ThirdDay", "102 · The Third Day")
def p03():
    t, h = rows(230, None)
    r1 = new(SKY, W1, h[0], defs("x63a", *ALL) + S6.washing("x63a", W1, h[0], 1031),
             cap(v("19:14"), "left: 12px; top: 12px", size=10.5, maxw=440) + cap(v("19:15", to="unto the people,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("19:15", frm="Be ready"), "right: 12px; top: 48px", 240, size=12.5, pad="14px 18px") + vref("EX 19:14–15", "right: 12px; bottom: 12px"))
    r2 = use(SI[0], over=cap(v("19:16"), "left: 12px; top: 12px", size=11.5, maxw=420) + sfx("ブオオオオ", "BUOOOO", "right: 20px; top: 20px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("EX 19:16", "right: 12px; bottom: 12px"))
    return page("Exodus 19:14–16 — The Third Day", t, r1 + r2, START + 2)


@P("EXO-C06-P04-Furnace", "103 · As the Smoke of a Furnace")
def p04():
    t, h = rows(300, 260, None)
    r1 = cols(use(SI[1], over=cap(v("19:17"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 19:17", "right: 8px; bottom: 8px")),
              use(SI[2], over=cap(v("19:18"), "left: 8px; top: 8px", size=10, maxw=320) + vref("EX 19:18", "right: 8px; bottom: 8px")))
    r2 = new(MOUNT, W1, h[1], E4.sinai(W1 * 0.5, h[1], W1 * 0.9, h[1] * 0.92, 1042) + E2.bolt(W1 * 0.2, 0, h[1] * 0.6, 1042) + E2.bolt(W1 * 0.82, 0, h[1] * 0.5, 1043, w=0.8),
             cap(v("19:19"), "left: 12px; top: 12px", size=11, maxw=420) + sfx("ブオオ", "BUOO", "right: 30px; top: 30px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-4) + vref("EX 19:19", "right: 12px; bottom: 12px"))
    r3 = use(SI[2], over=cap(v("19:20"), "left: 12px; top: 12px", size=11, maxw=420) + vref("EX 19:20", "right: 12px; bottom: 12px"))
    return page("Exodus 19:17–20 — As the Smoke of a Furnace", t, r1 + r2 + r3, START + 3)


@P("EXO-C06-P05-GoDown", "104 · Go, Get Thee Down")
def p05():
    t, h = rows(260, 220, None)
    r1 = new(MOUNT, W1, h[0], E4.sinai(W1 * 0.7, h[0], W1 * 0.6, h[0] * 0.9, 1051), cap(v("19:21", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("19:21", frm="Go down,") + " " + v("19:22"), "left: 12px; top: 48px", size=16, maxw=380) + vref("EX 19:21–22", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_FIRE, h[1], "linear-gradient(180deg, #1A0408 0%, #6A1A1E 50%, #FF6A2A 100%)", [("cap", v("19:23", to="unto Jehovah,")), ("say", v("19:23", frm="The people"))], ref="EX 19:23", size=14)
    r3 = new(MOUNT, W1, h[2], defs("x65c", *ALL) + S6.camp_before("x65c", W1, h[2], 1053, fire=True, bounds=True),
             cap(v("19:24", to="unto him,"), "left: 12px; top: 12px", size=11) + god(v("19:24", frm="Go, get"), "left: 12px; top: 48px", size=15, maxw=440)
             + cap(v("19:25"), "right: 12px; top: 12px", size=11, maxw=200) + vref("EX 19:24–25", "right: 12px; bottom: 12px"))
    return page("Exodus 19:21–25 — Go, Get Thee Down", t, r1 + r2 + r3, START + 4)


@P("EXO-C06-P06-TenWords1", "105 · And God Spake All These Words")
def p06():
    t, h = rows(290, 150, 300, None)
    r1 = use(IA[0], over=cap(v("20:1"), "left: 12px; top: 12px", size=11) + god(v("20:2"), "left: 12px; top: 50px", size=24, maxw=420) + mk.stamp(20, "right: 14px; bottom: 14px") + vref("EX 20:1–2", "left: 12px; bottom: 12px"))
    r2 = use(IA[1], over=E4.numeral(1, "left: 14px; top: 34px", size=70) + god(v("20:3"), "left: 120px; top: 44px", size=22) + vref("EX 20:3", "right: 12px; bottom: 12px"))
    r3 = use(IA[2], over=E4.numeral(2, "left: 14px; top: 20px", size=70) + god(v("20:4") + " " + v("20:5") + " " + v("20:6"), "left: 110px; top: 16px", size=14, maxw=560) + vref("EX 20:4–6", "right: 12px; bottom: 12px"))
    r4 = use(IA[3], over=E4.numeral(3, "left: 14px; top: 30px", size=70) + god(v("20:7"), "left: 120px; top: 30px", size=17, maxw=520) + vref("EX 20:7", "right: 12px; bottom: 12px"))
    return page("Exodus 20:1–7 — And God Spake All These Words", t, r1 + r2 + r3 + r4, START + 5)


@P("EXO-C06-P07-TenWords2", "106 · Remember the Sabbath Day")
def p07():
    t, h = rows(340, 236, None)
    r1 = cols(ten(4, TW[0], v("20:8") + " " + v("20:9") + " " + v("20:10") + " " + v("20:11"), "EX 20:8–11", pos="left: 8px; top: 74px", size=13, maxw=320),
              ten(5, TW[1], v("20:12"), "EX 20:12", size=14.5, maxw=320))
    r2 = ('\n  <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; min-height: 0">'
          + ten(6, TW[2], v("20:13"), "EX 20:13", size=16) + ten(7, TW[3], v("20:14"), "EX 20:14", size=16) + ten(8, TW[4], v("20:15"), "EX 20:15", size=16) + "\n  </div>")
    r3 = cols(ten(9, TW[5], v("20:16"), "EX 20:16", size=16, maxw=320), ten(10, TW[6], v("20:17"), "EX 20:17", size=14, maxw=320))
    return page("Exodus 20:8–17 — Remember the Sabbath Day", t, r1 + r2 + r3, START + 6)


@P("EXO-C06-P08-AfarOff", "107 · The People Stood Afar Off")
def p08():
    t, h = rows(320, 352, None)
    r1 = use(AF[0], over=cap(v("20:18"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("EX 20:18", "right: 12px; bottom: 12px"))
    r2 = cols(use(AF[1], over=cap(v("20:19", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + balloon(v("20:19", frm="Speak thou"), "right: 8px; top: 50px", 170, size=12.5, pad="20px 16px") + vref("EX 20:19", "left: 8px; bottom: 8px")),
              use(AF[2], over=cap(v("20:20", to="unto the people,"), "right: 8px; top: 8px", size=10.5) + balloon(v("20:20", frm="Fear not:"), "left: 8px; top: 50px", 180, size=12.5, pad="20px 16px") + vref("EX 20:20", "right: 8px; bottom: 8px")))
    r3 = use(AF[3], over=cap(v("20:21"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("EX 20:21", "right: 12px; bottom: 12px"))
    return page("Exodus 20:18–21 — The People Stood Afar Off", t, r1 + r2 + r3, START + 7)


@P("EXO-C06-P09-Altar", "108 · An Altar of Earth")
def p09():
    t, h = rows(300, None)
    r1 = cols(night(W2, h[0], cap(v("20:22", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + god(v("20:22", frm="Thus thou"), "left: 8px; top: 44px", size=15, maxw=320) + vref("EX 20:22", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[0], S6.idols_no(W2, h[0], 1092), god(v("20:23"), "left: 8px; top: 8px", size=14, maxw=320) + vref("EX 20:23", "right: 8px; bottom: 8px")))
    r2 = new(DUSK, W1, h[1], S6.altar_earth(W1, h[1], 1093), god(v("20:24") + " " + v("20:25") + " " + v("20:26"), "left: 12px; top: 12px", size=17, maxw=420) + vref("EX 20:24–26", "right: 12px; bottom: 12px"))
    return page("Exodus 20:22–26 — An Altar of Earth", t, r1 + r2, START + 8)


@P("EXO-C06-P10-Servant", "109 · These Are the Ordinances")
def p10():
    t, h = rows(150, None)
    r1 = new(MOUNT, W1, h[0], E4.sinai(W1 * 0.8, h[0], W1 * 0.4, h[0] * 0.9, 1101), god(v("21:1"), "left: 12px; top: 30px", size=22, maxw=460) + mk.stamp(21, "right: 14px; bottom: 12px") + vref("EX 21:1", "left: 12px; bottom: 12px"))
    cells = [law("THE HEBREW SERVANT", v("21:2") + " " + v("21:3"), "EX 21:2–3", pic(S6.pg_servant, "y1a"), cell=420),
             law("HIS WIFE AND CHILDREN", v("21:4"), "EX 21:4", pic(S6.pg_parents, "y1b"), cell=420),
             law("I WILL NOT GO OUT FREE", v("21:5") + " " + v("21:6"), "EX 21:5–6", pic(S6.pg_door, "y1c"), cell=420),
             law("THE MAID-SERVANT", v("21:7") + " " + v("21:8"), "EX 21:7–8", pic(S6.pg_maid, "y1d"), cell=420)]
    return page("Exodus 21:1–8 — These Are the Ordinances", t, r1 + grid(cells, "repeat(2, minmax(0, 1fr))"), START + 9)


@P("EXO-C06-P11-Refuge", "110 · A Place Whither He Shall Flee")
def p11():
    cells = [law("HIS SON'S WIFE", v("21:9") + " " + v("21:10") + " " + v("21:11"), "EX 21:9–11", pic(S6.pg_maid, "y2a")),
             law("HE THAT SMITETH A MAN", v("21:12") + " " + v("21:13") + " " + v("21:14"), "EX 21:12–14", pic(S6.pg_refuge, "y2b")),
             law("FATHER AND MOTHER", v("21:15") + " " + v("21:16") + " " + v("21:17"), "EX 21:15–17", pic(S6.pg_parents, "y2c")),
             law("IF MEN CONTEND", v("21:18") + " " + v("21:19"), "EX 21:18–19", pic(S6.pg_staff, "y2d"))]
    return page("Exodus 21:9–19 — A Place Whither He Shall Flee", "minmax(0, 1fr)", grid(cells, "repeat(2, minmax(0, 1fr))"), START + 10)


@P("EXO-C06-P12-EyeForEye", "111 · Eye for Eye")
def p12():
    cells = [law("A SERVANT SMITTEN", v("21:20") + " " + v("21:21"), "EX 21:20–21", pic(S6.pg_scales, "y3a")),
             law("AS THE JUDGES DETERMINE", v("21:22"), "EX 21:22", pic(S6.pg_scales, "y3b")),
             law("LIKE FOR LIKE", v("21:23") + " " + v("21:24") + " " + v("21:25"), "EX 21:23–25", pic(S6.pg_measure, "y3c")),
             law("FREE FOR HIS EYE'S SAKE", v("21:26") + " " + v("21:27"), "EX 21:26–27", pic(S6.pg_free, "y3d"))]
    return page("Exodus 21:20–27 — Eye for Eye", "minmax(0, 1fr)", grid(cells, "repeat(2, minmax(0, 1fr))"), START + 11)


@P("EXO-C06-P13-Ox", "112 · If an Ox Gore")
def p13():
    cells = [law("THE OX THAT GORETH", v("21:28"), "EX 21:28", pic(S6.pg_ox, "y4a"), cell=326),
             law("WONT TO GORE IN TIME PAST", v("21:29") + " " + v("21:30") + " " + v("21:31"), "EX 21:29–31", pic(lambda p: S6.pg_ox(p, rope=False), "y4b"), cell=326),
             law("A MAN-SERVANT OR A MAID-SERVANT", v("21:32"), "EX 21:32", pic(S6.pg_silver, "y4c"), cell=326),
             law("THE OPEN PIT", v("21:33") + " " + v("21:34"), "EX 21:33–34", pic(S6.pg_pit, "y4d"), cell=326),
             law("ONE MAN'S OX AND ANOTHER'S", v("21:35") + " " + v("21:36"), "EX 21:35–36", pic(S6.pg_two_oxen, "y4e"), cell=326)]
    end = (f'\n    <div style="position: relative; min-height: 0; border: 3px solid #0D0D0F; background: {MOUNT}; overflow: hidden">'
           f'<svg viewBox="0 0 342 300" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; width: 100%; height: 100%">{E4.sinai(171, 300, 300, 270, 1135)}</svg>'
           + end_mark("NEXT · THE BOOK OF THE COVENANT", "left: 10px; bottom: 10px") + '</div>')
    return page("Exodus 21:28–36 — If an Ox Gore", "minmax(0, 1fr)", grid(cells + [end], "repeat(3, minmax(0, 1fr))"), START + 12)
