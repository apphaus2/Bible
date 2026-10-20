"""Genesis volume, Chapter 10 — Bethel Again (Genesis 34–36). Every verse, word for word from ref/eng-asv.
Genesis 34 is given in full; the drawings stay restrained (34:2 is a caption over the city; the sword at Shechem is
drawn as the city under smoke and two figures at the gate). 35:22 is caption-only. Genesis 36 (the generations of
Esau) is set as four scroll pages."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from genesis import G, art as X, art2 as Y, art3 as Z, art4 as Q, art7 as J7, art8 as L, art9 as M, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import LAMP, RED, BLUE
from genesis.ch08 import ROSE, OCHRE, PASTURE
from mk import defs, face

v, sp = G.v, G.span
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
TEAL = "radial-gradient(circle at 70% 30%, #FFE680 0 20px, #4A9A8A 180px, #12302A 420px)"
GRIEF = "radial-gradient(circle at 70% 30%, #CFE0FF 0 20px, #5A5A9A 180px, #12113A 420px)"
EDOM = "#C2452A"
START = 170                                  # chapter 9 ends on page 169
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)
BROTHERS = [(("man", c), x, 0.46, x > 0.5) for x, c in [(0.56, "#7A3A2A"), (0.66, "#5A3A22"), (0.76, "#3A5A6A"), (0.86, "#8A6A3A")]]


@P("GEN-C10-00-Title", "Chapter 10 · Bethel Again")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A1430"></rect>' + defs("tt10", *ALL) + L.vow(760, 1080, 101)
    return chapter_title(10, "第十話", "Bethel Again", "Genesis 34 – 36", svg, NIGHT,
                         v("35:3", frm="let us arise", to="unto God,"), "Genesis · Volume One")


@P("GEN-C10-P01-Dinah", "170 · Dinah the Daughter of Leah")
def p01():
    t, h = rows(230, 200, None)
    r1 = new(PASTURE, W1, h[0], defs("c101a", *ALL) + T.dinah_walk("c101a", W1, h[0], 1011),
             cap(v("34:1"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 34:1", "right: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #4A1D55 0%, #C2456A 100%)", W1, h[1], T.shechem_city(None, W1, h[1], 1012),
             cap(v("34:2"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 34:2", "right: 12px; bottom: 12px"))
    r3 = cols(new(TEAL, W2, h[2], fc(T.SHECHEM, h[2]),
                  cap(v("34:3"), "right: 8px; top: 8px", size=10, maxw=200)
                  + cap(v("34:4", to="saying,"), "right: 8px; top: 122px", size=10, maxw=200)
                  + balloon(v("34:4", frm="Get me"), "right: 8px; top: 186px", 190, size=12, pad="14px 16px") + vref("GEN 34:3–4", "left: 8px; bottom: 8px")),
              new(GRIEF, W2, h[2], fc(T.JACOB_GRIEVED, h[2]),
                  cap(v("34:5"), "right: 8px; top: 8px", size=10, maxw=210)
                  + cap(v("34:6"), "right: 8px; top: 140px", size=10, maxw=210) + vref("GEN 34:5–6", "left: 8px; bottom: 8px")))
    return page("Genesis 34:1–6 — Dinah the Daughter of Leah", t, r1 + r2 + r3, START + 0)


@P("GEN-C10-P02-Hamor", "171 · Give Her unto Him to Wife")
def p02():
    t, h = rows(230, 340, None)
    r1 = new(PASTURE, W1, h[0], defs("c102a", *ALL) + T.stage("c102a", W1, h[0], 1021, "field", BROTHERS + [("jacob", 0.18, 0.48)]),
             cap(v("34:7"), "left: 12px; top: 12px", size=10.5, maxw=470) + vref("GEN 34:7", "right: 12px; bottom: 12px"))
    r2 = new(TEAL, W1, h[1], fc(T.HAMOR, h[1], w=W1),
             cap(v("34:8", to="saying,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("34:8", frm="The soul") + " " + v("34:9") + " " + v("34:10"), "left: 270px; top: 46px", 410, size=12.5, pad="34px 42px") + vref("GEN 34:8–10", "left: 12px; bottom: 12px"))
    r3 = new(TEAL, W1, h[2], fc(T.SHECHEM, h[2], w=W1),
             cap(v("34:11", to="unto her brethren,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("34:11", frm="Let me find") + " " + v("34:12"), "left: 270px; top: 46px", 410, size=12.5, pad="30px 40px") + vref("GEN 34:11–12", "left: 12px; bottom: 12px"))
    return page("Genesis 34:7–12 — Give Her unto Him to Wife", t, r1 + r2 + r3, START + 1)


@P("GEN-C10-P03-Guile", "172 · With Guile")
def p03():
    t, h = rows(400, None)
    r1 = new(RED, W1, h[0], fc(T.SIMEON, h[0], w=W1),
             cap(v("34:13") + " " + v("34:14", to="unto them,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("34:14", frm="We cannot") + " " + v("34:15") + " " + v("34:16") + " " + v("34:17"), "left: 260px; top: 100px", 420, size=12, pad="36px 42px")
             + vref("GEN 34:13–17", "left: 12px; bottom: 12px"))
    r2 = cols(new(TEAL, W2, h[1], fc(T.HAMOR, h[1]), cap(v("34:18"), "right: 8px; top: 8px", size=11, maxw=200) + vref("GEN 34:18", "left: 8px; bottom: 8px")),
              new(TEAL, W2, h[1], fc(T.SHECHEM, h[1]), cap(v("34:19"), "right: 8px; top: 8px", size=10.5, maxw=210) + vref("GEN 34:19", "left: 8px; bottom: 8px")))
    return page("Genesis 34:13–19 — With Guile", t, r1 + r2, START + 2)


@P("GEN-C10-P04-Gate", "173 · Unto the Gate of Their City")
def p04():
    t, h = rows(400, None)
    r1 = new(TEAL, W1, h[0], fc(T.HAMOR, h[0], w=W1),
             cap(v("34:20"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("34:21") + " " + v("34:22") + " " + v("34:23"), "left: 260px; top: 84px", 420, size=12, pad="34px 42px") + vref("GEN 34:20–23", "left: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], defs("c104b", *ALL) + T.shechem_city(None, W1, h[1], 1042, gate=True)
             + "".join(Z.man("c104b", W1 * x, h[1] * 0.86, Y.fit(h[1] * 0.86, h[1] * 0.5), c, flip=x > 0.56)
                                                     for x, c in [(0.2, "#2A6A5A"), (0.28, "#5A3A22"), (0.36, "#8A6A3A"), (0.76, "#3A5A6A"), (0.84, "#7A5A3A"), (0.92, "#5A4A6A")]),
             cap(v("34:24"), "left: 12px; top: 12px", size=11, maxw=440) + vref("GEN 34:24", "right: 12px; top: 12px"))
    return page("Genesis 34:20–24 — Unto the Gate of Their City", t, r1 + r2, START + 3)


@P("GEN-C10-P05-Sword", "174 · With the Edge of the Sword")
def p05():
    t, h = rows(300, 210, None)
    r1 = new("#3A1A1A", W1, h[0], defs("c105a", *ALL) + T.shechem_city(None, W1, h[0], 1051, gate=True, smoke=True)
             + T.figure("c105a", ("sword", "#3A5A6A"), W1 * 0.18, h[0] * 0.86, Y.fit(h[0] * 0.86, h[0] * 0.4))
             + T.figure("c105a", ("sword", "#5A3A22"), W1 * 0.28, h[0] * 0.86, Y.fit(h[0] * 0.86, h[0] * 0.42)),
             cap(v("34:25") + " " + v("34:26"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("GEN 34:25–26", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], defs("c105b", *ALL) + Z.plunder("c105b", W1, h[1], 1052),
             cap(v("34:27") + " " + v("34:28") + " " + v("34:29"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 34:27–29", "right: 12px; top: 12px"))
    r3 = cols(new(GRIEF, W2, h[2], fc(T.JACOB_GRIEVED, h[2]),
                  cap(v("34:30", to="and Levi,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("34:30", frm="Ye have"), "right: 8px; top: 40px", 240, size=10, pad="22px 22px") + vref("GEN 34:30", "left: 8px; bottom: 8px")),
              new(RED, W2, h[2], fc(T.LEVI, h[2]),
                  cap(v("34:31", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("34:31", frm="Should he"), "right: 8px; top: 40px", 200, size=13, pad="18px 18px") + vref("GEN 34:31", "left: 8px; bottom: 8px")))
    return page("Genesis 34:25–31 — With the Edge of the Sword", t, r1 + r2 + r3, START + 4)


@P("GEN-C10-P06-ForeignGods", "175 · Put Away the Foreign Gods")
def p06():
    t, h = rows(180, 330, 250, None)
    r1 = new(NIGHT, W1, h[0], cosmic(W1, h[0]),
             cap(v("35:1", to="unto Jacob,"), "left: 12px; top: 10px", size=10.5)
             + god(v("35:1", frm="Arise"), "left: 12px; top: 42px", size=15, maxw=660) + vref("GEN 35:1"))
    r2 = new(BLUE, W1, h[1], fc(L.JACOB_MAN, h[1], w=W1),
             cap(v("35:2", to="with him,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("35:2", frm="Put away") + " " + v("35:3"), "left: 270px; top: 66px", 410, size=12.5, pad="32px 40px") + vref("GEN 35:2–3", "left: 12px; bottom: 12px"))
    r3 = new(PASTURE, W1, h[2], defs("c106c", *ALL) + T.foreign_gods("c106c", W1, h[2], 1063),
             cap(v("35:4"), "right: 12px; top: 12px", size=10.5, maxw=380) + vref("GEN 35:4", "right: 12px; bottom: 12px"))
    r4 = new("#2A1A3E", W1, h[3], defs("c106d", *ALL) + T.terror("c106d", W1, h[3], 1064),
             cap(v("35:5"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 35:5", "right: 12px; top: 12px"))
    return page("Genesis 35:1–5 — Put Away the Foreign Gods", t, r1 + r2 + r3 + r4, START + 5)


@P("GEN-C10-P07-ElBethel", "176 · Israel Shall Be Thy Name")
def p07():
    t, h = rows(240, 220, None)
    r1 = new(SKY, W1, h[0], defs("c107a", *ALL) + T.stage("c107a", W1, h[0], 1071, "rock", [("jacob", 0.82, 0.5, False, "raise")],
                                                              props=Z.A4.altar(W1 * 0.36, h[0] * 0.88, 0.5, seed=1071)),
             cap(v("35:6") + " " + v("35:7"), "left: 12px; top: 12px", size=10.5, maxw=420) + vref("GEN 35:6–7", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], T.allon_bacuth(None, W1, h[1], 1072),
             cap(v("35:8"), "left: 12px; top: 12px", size=11, maxw=440) + vref("GEN 35:8", "right: 12px; top: 12px"))
    r3 = new(NIGHT, W1, h[2], cosmic(W1, h[2]),
             cap(v("35:9"), "left: 12px; top: 12px", size=10.5)
             + cap(v("35:10", to="said unto him,"), "left: 12px; top: 50px", size=10.5)
             + god(v("35:10", frm="Thy name", to="Israel shall be thy name:"), "left: 12px; top: 84px", size=15, maxw=660)
             + cap(v("35:10", frm="and he called"), "right: 12px; top: 176px", size=10.5)
             + cap(v("35:11", to="said unto him,"), "left: 12px; top: 214px", size=10.5)
             + god(v("35:11", frm="I am God") + " " + v("35:12"), "left: 12px; top: 248px", size=14, maxw=660) + vref("GEN 35:9–12"))
    return page("Genesis 35:6–12 — Israel Shall Be Thy Name", t, r1 + r2 + r3, START + 6)


@P("GEN-C10-P08-BenOni", "177 · Ben-oni")
def p08():
    t, h = rows(220, 270, None)
    r1 = cols(new("#0B0B2A", W2, h[0], Q.going_up(W2, h[0], 1081), cap(v("35:13"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 35:13", "right: 8px; bottom: 8px")),
              new(DAWN, W2, h[0], defs("c108a", *ALL) + L.oil_pillar("c108a", W2, h[0], 1082),
                  cap(v("35:14") + " " + v("35:15"), "left: 8px; top: 8px", size=9.5, maxw=200) + vref("GEN 35:14–15", "left: 8px; bottom: 8px")))
    r2 = cols(new(GREY, W2, h[1], fc(T.RACHEL_DYING, h[1]),
                  cap(v("35:16"), "right: 8px; top: 8px", size=10, maxw=200)
                  + cap(v("35:18"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("GEN 35:16, 18", "left: 8px; bottom: 8px")),
              new(OCHRE, W2, h[1], fc(T.MIDWIFE, h[1]),
                  cap(v("35:17", to="said unto her,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("35:17", frm="Fear not"), "right: 8px; top: 80px", 200, size=12, pad="18px 18px") + vref("GEN 35:17", "left: 8px; bottom: 8px")))
    r3 = new(DUSK, W1, h[2], T.roadside_grave(None, W1, h[2], 1083),
             cap(v("35:19"), "left: 12px; top: 12px", size=11.5, maxw=400)
             + cap(v("35:20"), "left: 12px; top: 64px", size=11, maxw=400) + vref("GEN 35:19–20", "right: 12px; top: 12px"))
    return page("Genesis 35:13–20 — Ben-oni", t, r1 + r2 + r3, START + 7)


@P("GEN-C10-P09-Twelve", "178 · The Sons of Jacob Were Twelve")
def p09():
    t = "220px 70px minmax(0, 1fr) 230px"
    r1 = new(PASTURE, W1, 214, T.tower_eder(None, W1, 214, 1091),
             cap(v("35:21"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("35:22", to="Israel heard of it."), "left: 12px; top: 74px", size=10.5, maxw=300) + vref("GEN 35:21–22", "right: 12px; bottom: 12px"))
    r2 = new("#12113A", W1, 64, L.sons_ring(W1, 64, 1092, ["REUBEN", "SIMEON", "LEVI", "JUDAH", "DAN", "NAPHTALI", "GAD", "ASHER", "ISSACHAR", "ZEBULUN", "JOSEPH", "BENJAMIN"], hi=11), "")
    r3 = grid([clan("The Sons of Leah", v("35:22", frm="Now the sons") + " " + v("35:23"), "GEN 35:22–23", "#6A7AD8", size=12),
               clan("The Sons of Rachel", v("35:24"), "GEN 35:24", "#C2456A", size=15),
               clan("The Sons of Bilhah", v("35:25"), "GEN 35:25", "#1F7A8C", size=14),
               clan("The Sons of Zilpah", v("35:26"), "GEN 35:26", "#8A6AB8", size=12)], "minmax(0, 1fr) minmax(0, 1fr)")
    r4 = new(DUSK, W1, 224, defs("c109d", *ALL) + T.isaac_buried("c109d", W1, 224, 1094),
             cap(v("35:27"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + cap(v("35:28") + " " + v("35:29"), "left: 12px; top: 86px", size=10.5, maxw=330) + hud("180", "right: 14px; top: 12px", size=26) + vref("GEN 35:27–29", "right: 12px; bottom: 12px"))
    return page("Genesis 35:21–29 — The Sons of Jacob Were Twelve", t, r1 + r2 + r3 + r4, START + 8)


@P("GEN-C10-P10-Esau", "179 · The Generations of Esau")
def p10():
    t, h = rows(260, None)
    r1 = new(SAND, W1, h[0], defs("c1010a", *ALL) + T.seir("c1010a", W1, h[0], 10101),
             cap(v("36:1"), "left: 12px; top: 12px", size=15.5) + cap(v("36:6") + " " + v("36:7") + " " + v("36:8"), "left: 12px; top: 54px", size=10, maxw=330)
             + vref("GEN 36:1, 6–8", "right: 12px; bottom: 12px"))
    cells = [clan("The Wives of Esau", v("36:2") + " " + v("36:3"), "GEN 36:2–3", EDOM, size=16.5),
             clan("The Sons of Esau", v("36:4") + " " + v("36:5"), "GEN 36:4–5", EDOM, size=16.5),
             clan("In Mount Seir", v("36:9") + " " + v("36:10"), "GEN 36:9–10", EDOM, size=16.5),
             clan("Eliphaz · Reuel", v("36:11") + " " + v("36:12") + " " + v("36:13"), "GEN 36:11–13", EDOM, size=15.5)]
    return page("Genesis 36:1–13 — The Generations of Esau", t, r1 + grid(cells, "minmax(0, 1fr) minmax(0, 1fr)"), START + 9)


@P("GEN-C10-P11-Chiefs", "180 · The Chiefs of the Sons of Esau")
def p11():
    cells = [clan("Oholibamah", v("36:14"), "GEN 36:14", EDOM, size=16.5),
             clan("Chiefs of Eliphaz", v("36:15") + " " + v("36:16"), "GEN 36:15–16", EDOM, size=15.5),
             clan("Chiefs of Reuel", v("36:17"), "GEN 36:17", EDOM, size=15.5),
             clan("Chiefs of Oholibamah", v("36:18") + " " + v("36:19"), "GEN 36:18–19", EDOM, size=15.5),
             clan("Seir the Horite", v("36:20") + " " + v("36:21"), "GEN 36:20–21", "#C8A06A", size=15.5),
             clan("Lotan · Shobal", v("36:22") + " " + v("36:23"), "GEN 36:22–23", "#C8A06A", size=16)]
    return page("Genesis 36:14–23 — The Chiefs of the Sons of Esau", "minmax(0, 1fr)", grid(cells, "repeat(3, minmax(0, 1fr))"), START + 10)


@P("GEN-C10-P12-Horites", "181 · Anah Who Found the Hot Springs")
def p12():
    t, h = rows(200, None)
    r1 = new(SAND, W1, h[0], defs("c1012a", *ALL) + T.stage("c1012a", W1, h[0], 10121, "sand", [(("man", "#8A6A3A"), 0.3, 0.42)],
                                                                props=Z.N.ass(W1 * 0.5, h[0] * 0.9, 0.2) + Z.N.ass(W1 * 0.62, h[0] * 0.92, 0.18)
                                                                + "".join(f'<path d="M{W1 * x:.0f} {h[0] * 0.86:.0f} c -10 -20 10 -30 0 -50" fill="none" stroke="#F3EFE6" stroke-width="5" opacity="0.6"></path>' for x in (0.78, 0.84, 0.9))
                                                                + f'<ellipse cx="{W1 * 0.84:.0f}" cy="{h[0] * 0.9:.0f}" rx="60" ry="10" fill="#8FD0E2" stroke="#0D0D0F" stroke-width="2"></ellipse>'),
             cap(v("36:24"), "left: 12px; top: 12px", size=11, maxw=440) + vref("GEN 36:24", "right: 12px; top: 12px"))
    cells = [clan("Anah · Dishon", v("36:25") + " " + v("36:26"), "GEN 36:25–26", "#C8A06A", size=16.5),
             clan("Ezer · Dishan", v("36:27") + " " + v("36:28"), "GEN 36:27–28", "#C8A06A", size=16.5),
             clan("Chiefs of the Horites", v("36:29") + " " + v("36:30"), "GEN 36:29–30", "#C8A06A", size=16.5),
             clan("Kings of Edom", v("36:31") + " " + v("36:32") + " " + v("36:33"), "GEN 36:31–33", "#FFD23F", size=15.5)]
    return page("Genesis 36:24–33 — Anah Who Found the Hot Springs", t, r1 + grid(cells, "minmax(0, 1fr) minmax(0, 1fr)"), START + 11)


@P("GEN-C10-P13-Kings", "182 · The Kings That Reigned in Edom")
def p13():
    t, h = rows(150, None, 150)
    r1 = new("#12113A", W1, h[0], T.kings_of_edom(W1, h[0], 10131), vref("GEN 36:31–39", "right: 12px; top: 10px"))
    cells = [clan("Husham · Hadad", v("36:34") + " " + v("36:35"), "GEN 36:34–35", "#FFD23F", size=16),
             clan("Samlah · Shaul", v("36:36") + " " + v("36:37") + " " + v("36:38"), "GEN 36:36–38", "#FFD23F", size=16),
             clan("Hadar", v("36:39"), "GEN 36:39", "#FFD23F", size=16),
             clan("The Chiefs of Edom", v("36:40") + " " + v("36:41") + " " + v("36:42") + " " + v("36:43"), "GEN 36:40–43", EDOM, size=14)]
    r3 = new(SAND, W1, h[2], defs("c1013c", *ALL) + T.seir("c1013c", W1, h[2], 10133),
             end_mark("NEXT · THE DREAMER", "right: 14px; bottom: 12px"))
    return page("Genesis 36:34–43 — The Kings That Reigned in Edom", t, r1 + grid(cells, "minmax(0, 1fr) minmax(0, 1fr)") + r3, START + 12)
