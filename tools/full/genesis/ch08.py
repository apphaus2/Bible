"""Genesis volume, Chapter 8 — The Ladder (Genesis 28–30). Every verse, word for word from ref/eng-asv.
Reuses the digest's Book Four panels for the ladder, Bethel, the well and Jacob and Rachel. Jacob's sons are counted
on a running row of twelve nodes as each is born. Genesis 30:3–4, 9 and 14–16 are given in full; the drawings stay
with the women's faces, the tent door and the mandrake plant."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art6 as R6, art7 as J7, art8 as L
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import LAMP, RED, BLUE
from mk import defs, face

v, sp = G.v, G.span
B4 = "reference/genesis/book-04/"
Lad, Rach = (panels(B4 + n + ".dc.html") for n in ["B4-P05-Ladder", "B4-P06-Rachel"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
ROSE = "radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #E07A9A 180px, #5A1A3A 420px)"
OCHRE = "radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #7A8AD8 180px, #1A2050 420px)"
PASTURE = "linear-gradient(180deg, #9FD0E2 0%, #E8F0C8 100%)"
SONS = ["REUBEN", "SIMEON", "LEVI", "JUDAH", "DAN", "NAPHTALI", "GAD", "ASHER", "ISSACHAR", "ZEBULUN", "JOSEPH"]
START = 137                                  # chapter 7 ends on page 136
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)

def son(n, ref, frm, mother, accent, size=16):
    """A son's birth as a scroll cell: number, name, mother, the verse."""
    return clan(f"{n:02d} · {SONS[n - 1].title()}", frm, ref, accent, of=f"OF {mother}", size=size)

def sons_bar(n, hi, h=70):
    return new("#12113A", W1, h, L.sons_ring(W1, h, 800 + n, SONS[:n], hi=hi), "")


@P("GEN-C08-00-Title", "Chapter 8 · The Ladder")
def title():
    return chapter_title(8, "第八話", "The Ladder", "Genesis 28 – 30", f'<g transform="translate(-160 0) scale(1.7)">{Lad[0].svg}</g>', NIGHT,
                         v("28:17", frm="this is none other", to="gate of heaven."), "Genesis · Volume One")


@P("GEN-C08-P01-Charge", "137 · Arise, Go to Paddan-aram")
def p01():
    t, h = rows(250, 330, None)
    r1 = new("#3A2214", W1, h[0], L.sending(None, W1, h[0], 811),
             cap(v("28:1", to="said unto him,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("28:1", frm="Thou shalt"), "right: 12px; top: 12px", 250, size=12, pad="18px 22px") + vref("GEN 28:1", "left: 12px; bottom: 12px"))
    r2 = new(LAMP, W1, h[1], fc(J7.ISAAC_OLD, h[1], w=W1),
             balloon(v("28:2") + " " + v("28:3") + " " + v("28:4"), "left: 260px; top: 20px", 420, size=12.5, pad="34px 42px") + vref("GEN 28:2–4", "left: 12px; bottom: 12px"))
    r3 = new(DAWN, W1, h[2], defs("c81c", *ALL) + L.setting_out("c81c", W1, h[2], 813),
             cap(v("28:5"), "right: 12px; top: 12px", size=11, maxw=360) + vref("GEN 28:5", "left: 12px; bottom: 12px"))
    return page("Genesis 28:1–5 — Arise, Go to Paddan-aram", t, r1 + r2 + r3, START + 0)


@P("GEN-C08-P02-Stone", "138 · A Certain Place")
def p02():
    t, h = rows(330, 170, None)
    r1 = new(SAND, W1, h[0], defs("c82a", *ALL) + L.esau_third("c82a", W1, h[0], 821),
             cap(v("28:6") + " " + v("28:7"), "left: 12px; top: 12px", size=10, maxw=290)
             + cap(v("28:8") + " " + v("28:9"), "right: 12px; top: 12px", size=10, maxw=270) + vref("GEN 28:6–9", "left: 12px; bottom: 12px"))
    r2 = new("#0B1A2E", W1, h[1], J7.flee_road(None, W1, h[1], 822), cap(v("28:10"), "right: 12px; bottom: 12px", size=12) + vref("GEN 28:10", "left: 12px; bottom: 12px"))
    r3 = new(DUSK, W1, h[2], defs("c82c", *ALL) + L.stone_pillow("c82c", W1, h[2], 823),
             cap(v("28:11"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 28:11", "right: 12px; top: 12px"))
    return page("Genesis 28:6–11 — A Certain Place", t, r1 + r2 + r3, START + 1)


@P("GEN-C08-P03-Ladder", "139 · The Gate of Heaven")
def p03():
    t, h = rows(640, None)
    r1 = use(Lad[0], over=cap(v("28:12"), "right: 12px; bottom: 14px", size=11.5, maxw=300)
             + cap(v("28:13", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + god(v("28:13", frm="I am Jehovah"), "left: 12px; top: 64px", size=14, maxw=240) + vref("GEN 28:12–13", "left: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             god(v("28:14") + " " + v("28:15"), "left: 12px; top: 12px", size=15, maxw=660) + vref("GEN 28:14–15"))
    return page("Genesis 28:12–15 — The Gate of Heaven", t, r1 + r2, START + 2)


@P("GEN-C08-P04-Bethel", "140 · Beth-el")
def p04():
    t, h = rows(370, 270, None)
    r1 = cols(use(Lad[1], over=cap(v("28:16", to="he said,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("28:16", frm="Surely"), "right: 8px; top: 60px", 200, size=12.5, pad="18px 18px")
                  + cap(v("28:17", to="said,"), "left: 8px; bottom: 120px", size=10)
                  + balloon(v("28:17", frm="How dreadful"), "right: 8px; bottom: 10px", 220, size=11.5, pad="22px 22px") + vref("GEN 28:16–17", "left: 8px; bottom: 8px")),
              use(Lad[2], over=cap(v("28:18") + " " + v("28:19"), "left: 8px; top: 8px", size=9.5, maxw=310) + vref("GEN 28:18–19", "right: 8px; bottom: 40px")))
    r2 = new(DAWN, W1, h[1], defs("c84b", *ALL) + L.oil_pillar("c84b", W1, h[1], 842),
             cap(v("28:20", to="saying,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("28:20", frm="If God") + " " + v("28:21"), "left: 12px; top: 46px", 330, size=12, pad="26px 32px") + vref("GEN 28:20–21", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], L.vow(W1, h[2], 843),
             balloon(v("28:22"), "left: 12px; top: 12px", 400, size=12.5, pad="24px 34px")
             + hud("1/10", "right: 14px; top: 12px", color="#FFD23F", size=24) + vref("GEN 28:22", "right: 12px; bottom: 12px"))
    return page("Genesis 28:16–22 — Beth-el", t, r1 + r2 + r3, START + 3)


@P("GEN-C08-P05-Well", "141 · Of Haran Are We")
def p05():
    t, h = rows(300, None, 240)
    r1 = new(PASTURE, W1, h[0], defs("c85a", *ALL) + L.three_flocks("c85a", W1, h[0], 851),
             cap(v("29:1") + " " + v("29:2"), "left: 12px; top: 12px", size=10, maxw=380)
             + cap(v("29:3"), "right: 12px; top: 12px", size=10, maxw=230) + vref("GEN 29:1–3", "right: 12px; bottom: 12px"))
    hh = h[1]
    r2 = cols(new(BLUE, W2, hh, fc(L.JACOB, hh),
                  cap(v("29:4", to="unto them,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:4", frm="My brethren", to="are ye?"), "right: 8px; top: 40px", 170, size=12, pad="14px 16px")
                  + cap(v("29:5", to="unto them,"), "right: 8px; top: 112px", size=10)
                  + balloon(v("29:5", frm="Know ye", to="Nahor?"), "right: 8px; top: 144px", 190, size=12, pad="14px 16px")
                  + cap(v("29:6", to="unto them,"), "right: 8px; top: 224px", size=10)
                  + balloon(v("29:6", frm="Is it well", to="him?"), "right: 8px; top: 256px", 150, size=12, pad="12px 14px") + vref("GEN 29:4–6", "left: 8px; bottom: 8px")),
              new(GREEN, W2, hh, defs("c85b", *ALL) + Y.ground(W2, hh, hh * 0.9, "#8AAA5A", dy=0)
                  + Z.man("c85b", W2 * 0.2, hh * 0.9, Y.fit(hh * 0.9, hh * 0.56), "#8A6A4A") + Z.man("c85b", W2 * 0.44, hh * 0.9, Y.fit(hh * 0.9, hh * 0.58), "#5A6A3A"),
                  cap(v("29:4", frm="And they said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:4", frm="Of Haran"), "right: 8px; top: 40px", 160, size=12, pad="14px 14px")
                  + cap(v("29:5", frm="And they said,", to="said,"), "right: 8px; top: 112px", size=10)
                  + balloon(v("29:5", frm="We know"), "right: 8px; top: 144px", 150, size=12, pad="12px 14px")
                  + cap(v("29:6", frm="And they said,", to="said,"), "right: 8px; top: 214px", size=10)
                  + balloon(v("29:6", frm="It is well:"), "right: 8px; top: 246px", 220, size=11, pad="16px 18px")))
    r3 = cols(new(BLUE, W2, h[2], fc(L.JACOB, h[2]),
                  cap(v("29:7", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:7", frm="Lo, it is"), "right: 8px; top: 40px", 220, size=11, pad="20px 20px") + vref("GEN 29:7", "left: 8px; bottom: 8px")),
              new(GREEN, W2, h[2], defs("c85c", *ALL) + Y.ground(W2, h[2], h[2] * 0.9, "#8AAA5A", dy=0)
                  + Z.man("c85c", W2 * 0.3, h[2] * 0.9, Y.fit(h[2] * 0.9, h[2] * 0.56), "#7A5A3A"),
                  cap(v("29:8", to="they said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:8", frm="We cannot"), "right: 8px; top: 40px", 220, size=11, pad="20px 20px") + vref("GEN 29:8", "left: 8px; bottom: 8px")))
    return page("Genesis 29:1–8 — Of Haran Are We", t, r1 + r2 + r3, START + 4)


@P("GEN-C08-P06-Rachel", "142 · Rachel Came with Her Father's Sheep")
def p06():
    t, h = rows(320, 380, None)
    r1 = use(Rach[0], over=cap(v("29:9") + " " + v("29:10"), "left: 12px; top: 12px", size=10.5, maxw=520)
             + sfx("ゴロッ", "GORO", "right: 30px; top: 70px", size=46, fill="#0D0D0F", stroke="#F3EFE6", rot=6) + vref("GEN 29:9–10", "left: 12px; bottom: 12px"))
    r2 = use(Rach[1], over=cap(v("29:11"), "left: 50%; bottom: 14px; transform: translateX(-50%)", size=12) + vref("GEN 29:11", "left: 12px; top: 12px"))
    r3 = cols(new(ROSE, W2, h[2], fc(L.RACHEL, h[2]),
                  cap(v("29:12"), "right: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 29:12", "left: 8px; bottom: 8px")),
              new(SAND, W2, h[2], defs("c86c", *ALL) + L.embrace("c86c", W2, h[2], 863),
                  cap(v("29:13"), "left: 8px; top: 8px", size=9.5, maxw=320) + vref("GEN 29:13", "right: 8px; bottom: 8px")))
    return page("Genesis 29:9–13 — Rachel Came with Her Father's Sheep", t, r1 + r2 + r3, START + 5)


@P("GEN-C08-P07-SevenYears", "143 · But a Few Days")
def p07():
    t, h = rows(300, 280, None)
    r1 = new(RUST, W1, h[0], fc(L.LABAN, h[0], w=W1),
             cap(v("29:14", to="said to him,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("29:14", frm="Surely", to="my flesh."), "left: 300px; top: 46px", 260, size=12.5, pad="18px 22px")
             + cap(v("29:14", frm="And he abode"), "left: 300px; top: 128px", size=10.5)
             + cap(v("29:15", to="unto Jacob,"), "left: 300px; top: 168px", size=10.5)
             + balloon(v("29:15", frm="Because"), "left: 290px; bottom: 10px", 390, size=11, pad="16px 30px") + vref("GEN 29:14–15", "left: 12px; bottom: 12px"))
    r2 = cols(new(OCHRE, W2, h[1], fc(L.LEAH, h[1]), cap(v("29:16"), "right: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 29:16", "left: 8px; bottom: 8px")),
              new(ROSE, W2, h[1], fc(L.RACHEL, h[1]), cap(v("29:17"), "right: 8px; top: 8px", size=11, maxw=200) + vref("GEN 29:17", "left: 8px; bottom: 8px")))
    r3 = cols(new(BLUE, W2, h[2], fc(L.JACOB, h[2]),
                  cap(v("29:18", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:18", frm="I will serve"), "right: 8px; top: 40px", 200, size=12, pad="20px 18px")
                  + cap(v("29:19", to="said,"), "right: 8px; top: 150px", size=10)
                  + balloon(v("29:19", frm="It is better"), "right: 8px; top: 182px", 220, size=11, pad="20px 20px") + vref("GEN 29:18–19", "left: 8px; bottom: 8px")),
              new("#7AA05A", W2, h[2], L.seven_years(W2, h[2], 873),
                  cap(v("29:20"), "left: 8px; top: 8px", size=11.5, maxw=320) + vref("GEN 29:20", "right: 8px; top: 120px")))
    return page("Genesis 29:14–20 — But a Few Days", t, r1 + r2 + r3, START + 6)


@P("GEN-C08-P08-Leah", "144 · Behold, It Was Leah")
def p08():
    t, h = rows(270, 270, None)
    r1 = cols(new(BLUE, W2, h[0], fc(L.JACOB_MAN, h[0]),
                  cap(v("29:21", to="unto Laban,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:21", frm="Give me"), "right: 8px; top: 40px", 200, size=12, pad="20px 18px") + vref("GEN 29:21", "left: 8px; bottom: 8px")),
              new("#2A1A14", W2, h[0], defs("c88a", *ALL) + L.wedding("c88a", W2, h[0], 881),
                  cap(v("29:22"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + cap(v("29:23"), "left: 8px; top: 74px", size=10, maxw=320) + vref("GEN 29:22–23", "right: 8px; bottom: 8px")))
    r2 = cols(new(OCHRE, W2, h[1], fc(L.LEAH_VEIL, h[1]), cap(v("29:24"), "right: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 29:24", "left: 8px; bottom: 8px")),
              new("radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #E8C08A 180px, #8A5A3A 420px)", W2, h[1], fc(L.LEAH, h[1]),
                  cap(v("29:25", to="it was Leah:"), "right: 8px; top: 8px", size=13, maxw=200)
                  + sfx("ハッ", "HA", "right: 20px; bottom: 30px", size=46, fill="#D7261E", stroke="#F3EFE6", rot=6) + vref("GEN 29:25", "left: 8px; bottom: 8px")))
    r3 = cols(new(RED, W2, h[2], fc(L.JACOB_ANGRY, h[2]),
                  cap(v("29:25", frm="and he said", to="to Laban,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:25", frm="What is this"), "right: 8px; top: 40px", 220, size=11, pad="22px 22px")),
              new(RUST, W2, h[2], fc(L.LABAN_SLY, h[2]),
                  cap(v("29:26", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("29:26", frm="It is not") + " " + v("29:27"), "right: 8px; top: 40px", 230, size=10.5, pad="24px 22px") + vref("GEN 29:26–27", "left: 8px; bottom: 8px")))
    return page("Genesis 29:21–27 — Behold, It Was Leah", t, r1 + r2 + r3, START + 7)


@P("GEN-C08-P09-Judah", "145 · This Time Will I Praise Jehovah")
def p09():
    t = "220px 70px minmax(0, 1fr) minmax(0, 1fr)"
    hh = 214
    r1 = cols(new(ROSE, W2, hh, fc(L.RACHEL_JOY, hh),
                  cap(v("29:28"), "right: 8px; top: 8px", size=10, maxw=200) + cap(v("29:29"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("GEN 29:28–29", "left: 8px; bottom: 8px")),
              new(OCHRE, W2, hh, fc(L.LEAH_SAD, hh),
                  cap(v("29:30"), "right: 8px; top: 8px", size=10, maxw=200) + cap(v("29:31"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("GEN 29:30–31", "left: 8px; bottom: 8px")))
    r2 = sons_bar(4, 3)
    r3 = cols(son(1, "GEN 29:32", v("29:32"), "LEAH", "#6A7AD8"), son(2, "GEN 29:33", v("29:33"), "LEAH", "#6A7AD8"))
    r4 = cols(son(3, "GEN 29:34", v("29:34"), "LEAH", "#6A7AD8"), son(4, "GEN 29:35", v("29:35"), "LEAH", "#6A7AD8"))
    return page("Genesis 29:28–35 — This Time Will I Praise Jehovah", t, r1 + r2 + r3 + r4, START + 8)


@P("GEN-C08-P10-Bilhah", "146 · Give Me Children, or Else I Die")
def p10():
    t = "270px 230px 70px minmax(0, 1fr)"
    r1 = cols(new(ROSE, W2, 264, fc(L.RACHEL_ENVY, 264),
                  cap(v("30:1", to="and she said unto Jacob,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("30:1", frm="Give me"), "right: 8px; bottom: 10px", 200, size=13, pad="16px 16px") + vref("GEN 30:1", "left: 8px; bottom: 8px")),
              new(RED, W2, 264, fc(L.JACOB_ANGRY, 264),
                  cap(v("30:2", to="he said,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("30:2", frm="Am I in"), "right: 8px; bottom: 10px", 220, size=11.5, pad="20px 20px") + vref("GEN 30:2", "left: 8px; bottom: 8px")))
    r2 = new(TENT, W1, 224, defs("c810b", *ALL) + L.handmaid("c810b", W1, 224, 8102),
             cap(v("30:3", to="she said,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("30:3", frm="Behold"), "left: 12px; top: 46px", 300, size=11.5, pad="20px 26px")
             + cap(v("30:4") + " " + v("30:5"), "right: 12px; top: 12px", size=10.5, maxw=200) + vref("GEN 30:3–5", "right: 12px; bottom: 12px"))
    r3 = sons_bar(6, 5)
    r4 = cols(son(5, "GEN 30:6", v("30:6"), "BILHAH", "#1F7A8C", size=16), son(6, "GEN 30:7–8", v("30:7") + " " + v("30:8"), "BILHAH", "#1F7A8C", size=15))
    return page("Genesis 30:1–8 — Give Me Children, or Else I Die", t, r1 + r2 + r3 + r4, START + 9)


@P("GEN-C08-P11-Mandrakes", "147 · My Son's Mandrakes")
def p11():
    t = "70px 210px 250px minmax(0, 1fr)"
    r1 = sons_bar(8, 7)
    r2 = cols(clan("07 · Gad", v("30:9") + " " + v("30:10") + " " + v("30:11"), "GEN 30:9–11", "#8A6AB8", of="OF ZILPAH", size=13),
              son(8, "GEN 30:12–13", v("30:12") + " " + v("30:13"), "ZILPAH", "#8A6AB8", size=13))
    r3 = new(SAND, W1, 244, defs("c811c", *ALL) + L.mandrakes("c811c", W1, 244, 8113),
             cap(v("30:14", to="his mother Leah."), "left: 12px; top: 12px", size=11, maxw=380)
             + cap(v("30:14", frm="Then Rachel", to="to Leah,"), "left: 12px; top: 92px", size=10.5)
             + balloon(v("30:14", frm="Give me, I pray"), "left: 12px; top: 126px", 300, size=12, pad="16px 22px") + vref("GEN 30:14", "right: 12px; top: 12px"))
    hh = 1022 - 36 - 70 - 210 - 250 - 6
    r4 = cols(new(OCHRE, W2, hh, fc(L.LEAH_SAD, hh),
                  cap(v("30:15", to="unto her,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("30:15", frm="Is it a small", to="mandrakes also?"), "right: 8px; top: 40px", 220, size=11, pad="20px 22px") + vref("GEN 30:15", "left: 8px; bottom: 8px")),
              new(ROSE, W2, hh, fc(L.RACHEL, hh),
                  cap(v("30:15", frm="And Rachel said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("30:15", frm="Therefore he"), "right: 8px; top: 40px", 210, size=11.5, pad="20px 20px")))
    return page("Genesis 30:9–15 — My Son's Mandrakes", t, r1 + r2 + r3 + r4, START + 10)


@P("GEN-C08-P12-Joseph", "148 · Jehovah Add to Me Another Son")
def p12():
    t = "230px 70px minmax(0, 1fr) 220px"
    r1 = new(DUSK, W1, 224, defs("c812a", *ALL) + Y.ground(W1, 224, 196, "#5A4A3A", dy=0) + Z.sun(W1 * 0.8, 190, 30, color="#FF8A3D", op=0.25)
             + L.leah("c812a", W1 * 0.36, 196, Y.fit(196, 224 * 0.36), up=[(-22, -158), (2, -150), (24, -164)]) + L.jacob_man("c812a", W1 * 0.54, 196, Y.fit(196, 224 * 0.32), flip=True, staff=True, up=L.HOLD_STAFF),
             cap(v("30:16", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=260)
             + balloon(v("30:16", frm="Thou must", to="mandrakes."), "right: 12px; top: 12px", 260, size=11, pad="20px 24px")
             + cap(v("30:16", frm="And he lay"), "right: 12px; bottom: 12px", size=10.5) + vref("GEN 30:16", "left: 12px; bottom: 12px"))
    r2 = sons_bar(11, 10)
    r3 = cols(son(9, "GEN 30:17–18", v("30:17") + " " + v("30:18"), "LEAH", "#6A7AD8", size=15),
              son(10, "GEN 30:19–20", v("30:19") + " " + v("30:20"), "LEAH", "#6A7AD8", size=15))
    r4 = cols(clan("Dinah", v("30:21"), "GEN 30:21", "#E07A9A", of="DAUGHTER OF LEAH", size=17),
              son(11, "GEN 30:22–24", v("30:22") + " " + v("30:23") + " " + v("30:24"), "RACHEL", "#C2456A", size=15))
    return page("Genesis 30:16–24 — Jehovah Add to Me Another Son", t, r1 + r2 + r3 + r4, START + 11)


@P("GEN-C08-P13-Wages", "149 · Appoint Me Thy Wages")
def p13():
    t, h = rows(300, 360, None)
    r1 = new(BLUE, W1, h[0], fc(L.JACOB_MAN, h[0], w=W1),
             cap(v("30:25", to="unto Laban,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("30:25", frm="Send me") + " " + v("30:26"), "left: 290px; top: 66px", 390, size=12.5, pad="28px 36px") + vref("GEN 30:25–26", "left: 12px; bottom: 12px"))
    r2 = cols(new(RUST, W2, h[1], fc(L.LABAN_SLY, h[1]),
                  cap(v("30:27", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("30:27", frm="If now"), "right: 8px; top: 40px", 220, size=11, pad="22px 22px")
                  + cap(v("30:28", to="he said,"), "right: 8px; top: 174px", size=10)
                  + balloon(v("30:28", frm="Appoint"), "right: 8px; top: 206px", 200, size=12, pad="16px 18px") + vref("GEN 30:27–28", "left: 8px; bottom: 8px")),
              new(BLUE, W2, h[1], fc(L.JACOB_MAN, h[1]),
                  cap(v("30:29", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("30:29", frm="Thou knowest") + " " + v("30:30"), "right: 8px; top: 40px", 240, size=10.5, pad="24px 24px") + vref("GEN 30:29–30", "left: 8px; bottom: 8px")))
    r3 = new(PASTURE, W1, h[2], defs("c813c", *ALL) + Y.ground(W1, h[2], h[2] * 0.8, "#8AAA5A", dy=0) + Z.flock(W1 * 0.3, W1 * 0.96, h[2] * 0.8, h[2] * 0.96, 14, 8133, cows=0.3, smin=0.22, smax=0.32)
             + L.laban("c813c", W1 * 0.1, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.4)) + L.jacob_man("c813c", W1 * 0.2, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.4), flip=True, staff=True, up=L.HOLD_STAFF),
             cap(v("30:31", to="he said,"), "left: 260px; top: 12px", size=10.5)
             + balloon(v("30:31", frm="What shall", to="give thee?"), "left: 250px; top: 46px", 200, size=12.5, pad="14px 18px")
             + cap(v("30:31", frm="And Jacob said,", to="Jacob said,"), "right: 12px; top: 120px", size=10.5)
             + balloon(v("30:31", frm="Thou shalt not"), "right: 12px; top: 154px", 380, size=12, pad="20px 30px") + vref("GEN 30:31", "left: 12px; top: 12px"))
    return page("Genesis 30:25–31 — Appoint Me Thy Wages", t, r1 + r2 + r3, START + 12)


@P("GEN-C08-P14-Speckled", "150 · Speckled and Spotted")
def p14():
    t, h = rows(330, 200, None)
    r1 = new(PASTURE, W1, h[0], L.speckled(None, W1, h[0], 8141, labels=False),
             balloon(v("30:32") + " " + v("30:33"), "left: 12px; top: 32px", 470, size=11.5, pad="30px 40px") + vref("GEN 30:32–33", "right: 12px; bottom: 12px"))
    r2 = new(RUST, W1, h[1], fc(L.LABAN_SLY, h[1], w=W1),
             cap(v("30:34", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("30:34", frm="Behold"), "left: 290px; top: 46px", 300, size=12.5, pad="18px 24px") + vref("GEN 30:34", "left: 12px; bottom: 12px"))
    r3 = new("#0E1A0A", W1, h[2], L.three_days(W1, h[2], 8143),
             cap(v("30:35"), "left: 12px; top: 12px", size=10.5, maxw=660)
             + cap(v("30:36"), "right: 12px; bottom: 14px", size=11, maxw=360) + vref("GEN 30:35–36", "left: 12px; bottom: 12px"))
    return page("Genesis 30:32–36 — Speckled and Spotted", t, r1 + r2 + r3, START + 13)


@P("GEN-C08-P15-Rods", "151 · The Man Increased Exceedingly")
def p15():
    t, h = rows(330, 260, None)
    r1 = new(PASTURE, W1, h[0], L.rods(None, W1, h[0], 8151),
             cap(v("30:37"), "left: 12px; top: 12px", size=10, maxw=300)
             + cap(v("30:38") + " " + v("30:39"), "right: 12px; top: 12px", size=10, maxw=300) + vref("GEN 30:37–39", "left: 12px; bottom: 12px"))
    r2 = new(PASTURE, W1, h[1], L.speckled(None, W1, h[1], 8152, labels=False),
             cap(v("30:40"), "left: 12px; top: 12px", size=10, maxw=300)
             + cap(v("30:41") + " " + v("30:42"), "right: 12px; top: 12px", size=10, maxw=300) + vref("GEN 30:40–42", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], defs("c815c", *ALL) + L.increase("c815c", W1, h[2], 8153),
             cap(v("30:43"), "right: 12px; top: 12px", size=12, maxw=380)
             + end_mark("NEXT · PENIEL", "right: 14px; bottom: 12px") + vref("GEN 30:43", "left: 12px; top: 12px"))
    return page("Genesis 30:37–43 — The Man Increased Exceedingly", t, r1 + r2 + r3, START + 14)
