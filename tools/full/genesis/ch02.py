"""Genesis volume, Chapter 2 — Cain to the Flood (Genesis 4–9). Every verse, word for word from ref/asv.
Genesis 5 (the book of the generations of Adam) is set as two 'scroll' pages: every verse in full, with a
lifespan bar per patriarch."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V, exodus2 as E2, faces
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y
from mk import defs, face

v, sp = G.v, G.span
B2 = "digest/genesis/book-02/"
Off, Fld, Mrk, Gen, Ark, Del, Dov, Cov = (panels(B2 + n + ".dc.html") for n in
    ["B2-P01-Offerings", "B2-P02-Field", "B2-P03-Mark", "B2-P04-Generations", "B2-P05-Ark", "B2-P06-Deluge", "B2-P07-Dove", "B2-P08-Covenant"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
NIGHT = "linear-gradient(180deg, #05050A 0%, #12113A 60%, #2A1A5E 100%)"
STORM = "linear-gradient(180deg, #0B0F2A 0%, #1E2A5A 60%, #2C5A7A 100%)"
DUSK = "linear-gradient(180deg, #12113A 0%, #4A1D55 45%, #FF8A3D 100%)"
SKY = "linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)"
GREY = "linear-gradient(180deg, #5E6E8A 0%, #A9B8C8 100%)"
DAWN = "linear-gradient(180deg, #2A1A5E 0%, #C2456A 55%, #FFC14D 100%)"
T = faces.tokens()
START = 17                                   # chapter 1 ends on page 16
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def rows(*hs):
    """Row template and the panel heights inside it (row minus the 3px borders). None = the rest of the page."""
    rest = 1022 - 12 * (len(hs) - 1) - sum(h for h in hs if h)
    return " ".join(f"{h}px" if h else "minmax(0, 1fr)" for h in hs), [(h or rest) - 6 for h in hs]

W1, W2, W3 = 702, 342, 222
def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)

def entry(name, years, beget, text, ref, accent="#FFD23F", note=None, size=11):
    """One patriarch on the scroll: name, a lifespan bar (years of 1000; the tick is the year he begat), the verses."""
    bar = (f'<svg viewBox="0 0 1000 12" preserveAspectRatio="none" style="display: block; width: 100%; height: 10px">'
           f'<rect x="0" y="0" width="1000" height="12" fill="#2A2A4A"></rect><rect x="0" y="0" width="{years}" height="12" fill="{accent}"></rect>'
           + (f'<rect x="{beget - 3}" y="0" width="6" height="12" fill="#D7261E"></rect>' if beget else "") + '</svg>')
    return (f'\n    <div style="position: relative; min-height: 0; border: 3px solid #0D0D0F; background: #12113A; color: #F3EFE6; padding: 8px 11px 10px; display: flex; flex-direction: column; gap: 6px">'
            f'\n      <div style="display: flex; justify-content: space-between; align-items: baseline"><span data-label style="font-family: Anton, sans-serif; font-size: 24px; line-height: 1; letter-spacing: 0.04em; text-transform: uppercase; color: {accent}">{name}</span>'
            f'<span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.18em">{note or f"{years} YEARS"} · {ref}</span></div>'
            f'\n      {bar}'
            f'\n      <div style="font-size: {size}px; font-weight: 600; line-height: 1.5; letter-spacing: 0.03em; text-transform: uppercase">{text}</div>\n    </div>')

def grid(cells, tmpl_rows, ncol=2):
    return f'\n  <div style="display: grid; grid-template-columns: repeat({ncol}, minmax(0, 1fr)); grid-template-rows: {tmpl_rows}; gap: 12px; min-height: 0">' + "".join(cells) + "\n  </div>"


@P("GEN-C02-00-Title", "Chapter 2 · Cain to the Flood")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B0F2A"></rect>' + Y.rain(760, 1080, 3) + E2.bolt(560, 120, 520, 7, w=1.6)
           + Y.sea(760, 1080, 760, 5, color="#12305A", deep="#05101F", foam="#8FB8D8", amp=22) + Y.ark_afloat(150, 742, 330, "tt"))
    return chapter_title(2, "第二話", "Cain to the Flood", "Genesis 4 – 9", svg, STORM,
                         v("6:8"), "Genesis · Volume One · The Full Edition")


@P("GEN-C02-P01-Offerings", "17 · The Offerings")
def p01():
    t, h = rows(200, 250, 300, None)
    r1 = cols(new(DUSK, W2, h[0], defs("c21a", *ALL) + Y.eve_with_cain("c21a", W2, h[0]),
                  cap(v("4:1", to="bare Cain,"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 4:1")),
              new("radial-gradient(circle at 30% 40%, #FFF4C2 0 30px, #FFC14D 140px, #C2456A 330px)", W2, h[0], Y.mother_and_child(W2, h[0], baby_xy=(250, 160)),
                  cap(v("4:1", frm="and said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("4:1", frm="I have"), "right: 8px; top: 44px", 200, size=12.5, pad="16px 20px")))
    r2 = use(Off[0], over=cap(v("4:2"), "left: 12px; bottom: 12px", size=11, maxw=420) + vref("GEN 4:2", "right: 12px; bottom: 12px"))
    r3 = use(Off[1], over=cap(v("4:3"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + cap(v("4:4"), "right: 12px; top: 12px", size=10.5, maxw=300)
             + cap(v("4:5", to="not respect."), "left: 12px; bottom: 14px", size=11, maxw=420) + vref("GEN 4:3–5", "right: 12px; bottom: 12px"))
    r4 = cols(use(Off[2], over=cap(v("4:5", frm="And Cain was"), "right: 8px; bottom: 8px", size=11, maxw=170) + sfx("ギリッ", "GIRI", "left: 14px; top: 10px", size=34, fill="#D7261E", stroke="#F3EFE6", rot=-8)),
              new(NIGHT, W2, h[3], cosmic(W2, h[3]),
                  cap(v("4:6", to="unto Cain,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("4:6", frm="Why"), "left: 8px; top: 48px", size=19, maxw=310) + vref("GEN 4:6")))
    return page("Genesis 4:1–6 — The Offerings", t, r1 + r2 + r3 + r4, START + 0)


@P("GEN-C02-P02-Field", "18 · In the Field")
def p02():
    t, h = rows(290, 200, 300, None)
    r1 = cols(new(NIGHT, W2, h[0], cosmic(W2, h[0]),
                  god(v("4:7"), "left: 8px; top: 8px", size=16, maxw=320) + vref("GEN 4:7")),
              use(Off[3], over=sfx("ゴロ…", "GORO", "right: 14px; top: 14px", size=30, fill="#D7261E", stroke="#0D0D0F", rot=4)))
    r2 = use(Fld[0], over=cap(v("4:8", to="in the field,"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 4:8", "right: 12px; bottom: 12px"))
    r3 = use(Fld[1], over=cap(v("4:8", frm="that Cain"), "left: 12px; bottom: 14px", size=13, maxw=420)
             + sfx("ドッ", "DOH", "left: 30px; top: 20px", size=64, fill="#0D0D0F", stroke="#F3EFE6", rot=-6))
    r4 = cols(new(NIGHT, W2, h[3], cosmic(W2, h[3]),
                  cap(v("4:9", to="unto Cain,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("4:9", frm="Where", to="brother?"), "left: 8px; top: 48px", size=24, maxw=300) + vref("GEN 4:9")),
              use(Fld[2], over=cap(v("4:9", frm="And he said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("4:9", frm="I know"), "right: 8px; top: 44px", 170, size=12, pad="16px 16px")))
    return page("Genesis 4:7–9 — In the Field", t, r1 + r2 + r3 + r4, START + 1)


@P("GEN-C02-P03-Fugitive", "19 · A Fugitive and a Wanderer")
def p03():
    t, h = rows(300, 250, None)
    r1 = cols(use(Fld[3], over=cap(v("4:10", to="said,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("4:10", frm="What"), "left: 8px; top: 46px", size=17, maxw=320) + vref("GEN 4:10")),
              new(NIGHT, W2, h[0], cosmic(W2, h[0]),
                  god(v("4:11") + " " + v("4:12"), "left: 8px; top: 8px", size=14.5, maxw=320) + vref("GEN 4:11–12")))
    r2 = use(Mrk[0], over=cap(v("4:13", to="Jehovah,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("4:13", frm="My punishment"), "left: 14px; top: 46px", 230, size=13, pad="18px 22px")
             + balloon(v("4:14"), "right: 10px; top: 8px", 430, size=11.5, pad="26px 50px") + vref("GEN 4:13–14", "left: 12px; bottom: 12px"))
    r3 = use(Mrk[1], over=cap(v("4:15", to="unto him,"), "right: 12px; top: 12px", size=10.5)
             + god(v("4:15", frm="Therefore", to="sevenfold."), "right: 12px; top: 48px", size=17, maxw=320)
             + cap(v("4:15", frm="And Jehovah appointed"), "right: 12px; bottom: 16px", size=11.5, maxw=320)
             + sfx("キィン", "KIIN", "left: 40px; bottom: 30px", size=40, fill="#FFD23F", stroke="#0D0D0F", rot=-4) + vref("GEN 4:15", "left: 12px; top: 12px"))
    return page("Genesis 4:10–15 — A Fugitive and a Wanderer", t, r1 + r2 + r3, START + 2)


@P("GEN-C02-P04-City", "20 · The City, the Harp and the Forge")
def p04():
    t, h = rows(270, 230, None)
    r1 = use(Mrk[2], over=cap(v("4:16"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("4:17"), "right: 12px; bottom: 14px", size=10.5, maxw=330) + vref("GEN 4:16–17", "left: 12px; bottom: 12px"))
    r2 = cols(new("linear-gradient(180deg, #FFC14D 0%, #E8A35A 100%)", W2, h[1], defs("c24a", *ALL) + Y.line_of_cain("c24a", W2, h[1], 241),
                  cap(v("4:18"), "left: 8px; top: 8px", size=10, maxw=320) + vref("GEN 4:18", "right: 8px; bottom: 8px")),
              new(DUSK, W2, h[1], defs("c24b", *ALL) + Y.lamech_wives("c24b", W2, h[1]),
                  cap(v("4:19"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 4:19", "right: 8px; bottom: 8px")))
    r3 = cols(new(SKY, W3, h[2], Y.tents_cattle(W3, h[2], 242),
                  cap(v("4:20"), "left: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 4:20", "right: 8px; bottom: 8px")),
              new("linear-gradient(180deg, #4A1D55 0%, #C2456A 100%)", W3, h[2], Y.harp_pipe(W3, h[2], 243),
                  cap(v("4:21"), "left: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 4:21", "right: 8px; bottom: 8px")),
              new("linear-gradient(180deg, #2A0A0A 0%, #5A1A16 100%)", W3, h[2], Y.forge(W3, h[2], 244),
                  cap(v("4:22"), "left: 8px; top: 8px", size=10.5, maxw=200)
                  + sfx("カン", "KAN", "right: 14px; top: 200px", size=36, fill="#FFD23F", stroke="#0D0D0F", rot=8) + vref("GEN 4:22", "right: 8px; bottom: 8px")))
    return page("Genesis 4:16–22 — The City, the Harp and the Forge", t, r1 + r2 + r3, START + 3)


@P("GEN-C02-P05-Seth", "21 · Then Began Men to Call")
def p05():
    t, h = rows(380, 300, None)
    r1 = new("repeating-conic-gradient(from 0deg at 30% 50%, #5A0A0A 0deg 4deg, #8A1A16 4deg 8deg)", W1, h[0],
             defs("c25a", *ALL) + face(Y.LAMECH, -40, -10, 1.0) + Y.wife("c25a", 618, 364, 0.78, "#C2456A", flip=True) + Y.wife("c25a", 668, 366, 0.74, "#7A3BA8", flip=True),
             cap(v("4:23", to="wives:"), "left: 300px; top: 14px", size=11)
             + balloon(v("4:23", frm="Adah and Zillah") + " " + v("4:24"), "left: 262px; top: 50px", 330, size=12.5, pad="34px 42px")
             + vref("GEN 4:23–24", "left: 12px; bottom: 12px"))
    r2 = new("radial-gradient(circle at 30% 40%, #FFF4C2 0 30px, #FFC14D 160px, #FF8A3D 400px)", W1, h[1], Y.mother_and_child(W1, h[1], baby_xy=(300, 230)),
             cap(v("4:25", to="Seth:"), "right: 12px; top: 12px", size=11, maxw=300)
             + cap(v("4:25", frm="For, said", to="she,"), "right: 12px; top: 90px", size=10.5)
             + balloon(v("4:25", frm="God hath"), "right: 14px; top: 130px", 280, size=13, pad="22px 28px") + vref("GEN 4:25", "left: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], defs("c25c", *ALL) + Y.call_upon("c25c", W1, h[2], 251),
             cap(v("4:26", to="Enosh."), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("4:26", frm="Then began"), "right: 12px; top: 12px", size=13, maxw=300) + vref("GEN 4:26", "left: 12px; bottom: 12px"))
    return page("Genesis 4:23–26 — Then Began Men to Call", t, r1 + r2 + r3, START + 4)


@P("GEN-C02-P06-Scroll", "22 · The Book of the Generations of Adam")
def p06():
    t, h = rows(230, None)
    r1 = new(NIGHT, W1, h[0], Y.generations(W1, h[0], 261, hi=0),
             cap(v("5:1"), "left: 12px; top: 12px", size=11, maxw=420)
             + cap(v("5:2"), "right: 12px; bottom: 14px", size=10.5, maxw=330) + vref("GEN 5:1–2", "left: 12px; bottom: 12px"))
    cells = [entry("Adam", 930, 130, sp("5:3-5"), "GEN 5:3–5", size=12.5),
             entry("Seth", 912, 105, sp("5:6-8"), "GEN 5:6–8", size=12.5),
             entry("Enosh", 905, 90, sp("5:9-11"), "GEN 5:9–11", size=12.5),
             entry("Kenan", 910, 70, sp("5:12-14"), "GEN 5:12–14", size=12.5),
             entry("Mahalalel", 895, 65, sp("5:15-17"), "GEN 5:15–17", size=12.5),
             entry("Jared", 962, 162, sp("5:18-20"), "GEN 5:18–20", size=12.5)]
    return page("Genesis 5:1–20 — The Book of the Generations of Adam", t, r1 + grid(cells, "1.25fr 1fr 1fr"), START + 5)


@P("GEN-C02-P07-Enoch", "23 · Enoch Walked with God")
def p07():
    t, h = rows(300, 140, 270, None)
    r1 = new("linear-gradient(180deg, #FFF4C2 0%, #C8B8D8 50%, #5A4A6E 100%)", W1, h[0], defs("c27a", *ALL) + Y.enoch("c27a", W1, h[0], 271),
             f'    <span data-label style="position: absolute; left: 14px; top: 10px; font-family: Anton, sans-serif; font-size: 34px; letter-spacing: 0.04em; text-transform: uppercase; color: #12113A">Enoch</span>\n'
             + cap(sp("5:21-23"), "left: 12px; top: 58px", size=10.5, maxw=330)
             + cap(v("5:24"), "right: 12px; bottom: 14px", size=14, maxw=300) + vref("GEN 5:21–24", "left: 12px; bottom: 12px"))
    r2 = grid([entry("Methuselah", 969, 187, sp("5:25-27"), "GEN 5:25–27", accent="#FF8A3D")], "minmax(0, 1fr)", ncol=1)
    r3 = cols(new(DAWN, W2, h[2], defs("c27c", *ALL) + Y.lamech_noah("c27c", W2, h[2]),
                  cap(v("5:28") + " " + v("5:29", to="saying,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("5:29", frm="This same"), "right: 6px; bottom: 6px", 236, size=10.5, pad="20px 26px") + vref("GEN 5:28–29", "left: 8px; bottom: 8px")),
              grid([entry("Lamech", 777, 182, sp("5:30-31"), "GEN 5:30–31", accent="#C2456A")], "minmax(0, 1fr)", ncol=1))
    r4 = new(DAWN, W1, h[3], defs("c27d", *ALL) + Y.noah_and_sons("c27d", W1, h[3]),
             f'    <span data-label style="position: absolute; left: 14px; top: 10px; font-family: Anton, sans-serif; font-size: 34px; letter-spacing: 0.04em; text-transform: uppercase; color: #F3EFE6; text-shadow: 3px 3px 0 #0D0D0F">Noah</span>\n'
             + cap(v("5:32"), "right: 12px; top: 12px", size=13, maxw=330) + vref("GEN 5:32", "left: 12px; bottom: 12px"))
    return page("Genesis 5:21–32 — Enoch Walked with God", t, r1 + r2 + r3 + r4, START + 6)


@P("GEN-C02-P08-Nephilim", "24 · The Nephilim")
def p08():
    t, h = rows(330, 200, None)
    r1 = new("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", W1, h[0], defs("c28a", *ALL) + Y.multitude("c28a", W1, h[0], 281),
             cap(v("6:1"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("6:2"), "right: 12px; top: 12px", size=11, maxw=320) + vref("GEN 6:1–2", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("6:3", to="said,"), "left: 12px; top: 12px", size=11)
             + god(v("6:3", frm="My Spirit"), "left: 12px; top: 48px", size=18, maxw=640) + vref("GEN 6:3"))
    r3 = new("linear-gradient(180deg, #2A0A1A 0%, #8A2A2A 60%, #FF8A3D 100%)", W1, h[2], defs("c28c", *ALL) + Y.nephilim("c28c", W1, h[2], 282),
             cap(v("6:4"), "left: 12px; top: 12px", size=12, maxw=330) + vref("GEN 6:4", "right: 12px; top: 12px"))
    return page("Genesis 6:1–4 — The Nephilim", t, r1 + r2 + r3, START + 7)


@P("GEN-C02-P09-Grieved", "25 · It Grieved Him at His Heart")
def p09():
    t, h = rows(320, 250, None)
    r1 = use(Gen[0], over=cap(v("6:5"), "left: 12px; top: 12px", size=12, maxw=420)
             + sfx("ザワザワ", "ZAWA ZAWA", "right: 18px; top: 16px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=4) + vref("GEN 6:5", "left: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("6:6"), "left: 12px; top: 12px", size=11, maxw=640)
             + cap(v("6:7", to="said,"), "left: 12px; top: 58px", size=10.5)
             + god(v("6:7", frm="I will"), "left: 12px; top: 92px", size=15, maxw=660) + vref("GEN 6:6–7"))
    r3 = cols(use(Gen[1], over=cap(v("6:8"), "right: 8px; bottom: 10px", size=13, maxw=230) + vref("GEN 6:8", "left: 8px; top: 8px")),
              new(DAWN, W2, h[2], defs("c29b", *ALL) + Y.noah_and_sons("c29b", W2, h[2], top=0.5),
                  cap(v("6:9"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + cap(v("6:10"), "left: 8px; top: 130px", size=10.5, maxw=320) + vref("GEN 6:9–10", "right: 8px; bottom: 8px")))
    return page("Genesis 6:5–10 — It Grieved Him at His Heart", t, r1 + r2 + r3, START + 8)


@P("GEN-C02-P10-Pattern", "26 · Make Thee an Ark")
def p10():
    t, h = rows(210, 230, 300, None)
    r1 = new("linear-gradient(180deg, #12090A 0%, #4A1A16 100%)", W1, h[0], Y.violence(W1, h[0], 301),
             cap(v("6:11"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("6:12"), "right: 12px; top: 12px", size=10.5, maxw=320) + vref("GEN 6:11–12", "left: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], Y.noah_kneels("c30b", W1, h[1]),
             cap(v("6:13", to="Noah,"), "left: 12px; top: 12px", size=10.5)
             + god(v("6:13", frm="The end"), "left: 12px; top: 46px", size=15, maxw=420) + vref("GEN 6:13", "right: 12px; top: 12px"))
    r3 = use(Ark[0], over=god(v("6:14") + " " + v("6:15"), "left: 12px; top: 12px", size=14, maxw=400) + vref("GEN 6:14–15", "right: 12px; top: 12px"))
    r4 = new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", W1, h[3],
             Y.ground(W1, h[3], h[3] * 0.9, "#8A9A5A", dy=0) + Y.ark_hull(240, h[3] * 0.9, 440, h[3] * 0.5, "p30", open_=True),
             god(v("6:16"), "left: 12px; top: 12px", size=13, maxw=230) + vref("GEN 6:16", "right: 12px; top: 12px"))
    return page("Genesis 6:11–16 — Make Thee an Ark", t, r1 + r2 + r3 + r4, START + 9)


@P("GEN-C02-P11-Covenant", "27 · Two of Every Sort")
def p11():
    t, h = rows(200, 220, 240, None)
    r1 = new(STORM, W1, h[0], Y.storm_land(W1, h[0], 311),
             god(v("6:17"), "left: 12px; top: 12px", size=15, maxw=520) + vref("GEN 6:17", "right: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("c31b", *ALL) + V.rays(W1 * 0.8, h[1], 30, 30, W1, color="#FFF4C2", op=0.3)
             + Y.ground(W1, h[1], h[1] * 0.88, "#2A3A1E", dy=0) + Y.family8("c31b", 390, 670, round(h[1] * 0.88), Y.fit(h[1] * 0.88, h[1] * 0.22)),
             god(v("6:18"), "left: 12px; top: 12px", size=15, maxw=330) + vref("GEN 6:18", "right: 12px; top: 12px"))
    r3 = new(SKY, W1, h[2], Y.pairs("c31c", W1, h[2], 313),
             god(v("6:19") + " " + v("6:20"), "left: 12px; top: 12px", size=12.5, maxw=640) + vref("GEN 6:19–20", "right: 12px; bottom: 12px"))
    r4 = cols(new("linear-gradient(180deg, #FFC14D 0%, #E8A35A 100%)", W2, h[3], Y.provisions(W2, h[3], 314),
                  god(v("6:21"), "left: 8px; top: 8px", size=14, maxw=320) + vref("GEN 6:21", "right: 8px; bottom: 8px")),
              use(Ark[1], over=cap(v("6:22"), "left: 8px; bottom: 8px", size=11, maxw=320)
                  + sfx("カンカン", "KAN KAN", "right: 14px; top: 14px", size=30, fill="#0D0D0F", stroke="#F3EFE6", rot=6) + vref("GEN 6:22", "right: 8px; bottom: 8px")))
    return page("Genesis 6:17–22 — Two of Every Sort", t, r1 + r2 + r3 + r4, START + 10)


@P("GEN-C02-P12-Come", "28 · Come Thou into the Ark")
def p12():
    t, h = rows(250, 250, 230, None)
    r1 = cols(new("radial-gradient(circle at 30% 40%, #FFF4C2 0 30px, #8FD0E2 160px, #12113A 360px)", W2, h[0], face(Y.NOAH_AWE, -50, -10, 0.72),
                  cap(v("7:1", to="unto Noah,"), "right: 8px; top: 8px", size=10.5, maxw=150) + vref("GEN 7:1", "left: 8px; bottom: 8px")),
              new(NIGHT, W2, h[0], cosmic(W2, h[0]),
                  god(v("7:1", frm="Come"), "left: 8px; top: 8px", size=17, maxw=320)))
    r2 = new(SKY, W1, h[1], Y.clean_sevens(W1, h[1], 321),
             god(v("7:2") + " " + v("7:3"), "left: 12px; top: 12px", size=13.5, maxw=500) + vref("GEN 7:2–3", "right: 12px; bottom: 12px"))
    r3 = new(STORM, W1, h[2], Y.storm_land(W1, h[2], 322),
             god(v("7:4"), "left: 12px; top: 12px", size=15, maxw=500) + vref("GEN 7:4", "right: 12px; bottom: 12px"))
    r4 = new(SKY, W1, h[3], Y.ark_ramp("c32d", W1, h[3], 323),
             cap(v("7:5"), "left: 12px; top: 12px", size=12, maxw=300) + vref("GEN 7:5", "left: 12px; bottom: 12px"))
    return page("Genesis 7:1–5 — Come Thou into the Ark", t, r1 + r2 + r3 + r4, START + 11)


@P("GEN-C02-P13-Fountains", "29 · The Fountains of the Great Deep")
def p13():
    t, h = rows(250, 210, None, 150)
    r1 = cols(new("radial-gradient(circle at 70% 40%, #FFF4C2 0 20px, #A9B8C8 160px, #2A3A6A 360px)", W2, h[0], face(Y.NOAH_GRAVE, 392, -10, 0.72, flip=True),
                  cap(v("7:6"), "left: 8px; top: 8px", size=10.5, maxw=160) + vref("GEN 7:6", "right: 8px; bottom: 8px")),
              use(Ark[2], over=cap(v("7:7"), "left: 8px; top: 8px", size=10, maxw=320) + vref("GEN 7:7", "right: 8px; bottom: 8px")))
    r2 = new(GREY, W1, h[1], Y.pairs("c33b", W1, h[1], 332),
             cap(v("7:8") + " " + v("7:9"), "left: 12px; top: 12px", size=11, maxw=520) + vref("GEN 7:8–9", "right: 12px; top: 12px"))
    r3 = use(Del[0], over=cap(v("7:10"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("7:11"), "left: 12px; bottom: 14px", size=11.5, maxw=440)
             + sfx("ドドドド", "DODODODO", "right: 18px; top: 20px", size=52, fill="#F3EFE6", stroke="#0D0D0F", rot=-4) + vref("GEN 7:10–11", "right: 12px; bottom: 12px"))
    days = "".join(f'<span data-label style="padding: 4px 8px; border: 2px solid {"#D7261E" if d == 40 else "#CFEFFF"}; color: {"#D7261E" if d == 40 else "#CFEFFF"}; font-family: Anton, sans-serif; font-size: 22px; letter-spacing: 0.06em">DAY {d:02d}</span>' for d in (1, 10, 20, 30, 40))
    r4 = new(STORM, W1, h[3], Y.rain(W1, h[3], 334),
             f'    <div style="position: absolute; left: 12px; right: 12px; bottom: 12px; display: flex; justify-content: space-between">{days}</div>\n'
             + cap(v("7:12"), "left: 12px; top: 12px", size=12) + vref("GEN 7:12", "right: 12px; top: 12px"))
    return page("Genesis 7:6–12 — The Fountains of the Great Deep", t, r1 + r2 + r3 + r4, START + 12)


@P("GEN-C02-P14-ShutIn", "30 · Jehovah Shut Him In")
def p14():
    t, h = rows(260, 200, 270, None)
    r1 = new(STORM, W1, h[0], defs("c34a", *ALL) + Y.rain(W1, h[0], 341) + Y.ground(W1, h[0], h[0] * 0.9, "#4A5A3A", dy=0)
             + Y.ark_hull(300, h[0] * 0.9, 480, h[0] * 0.5, "p34", open_=True) + Y.family8("c34a", 40, 290, round(h[0] * 0.9), Y.fit(h[0] * 0.9, h[0] * 0.42)),
             cap(v("7:13"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 7:13", "right: 12px; top: 12px"))
    r2 = new(GREY, W1, h[1], Y.pairs("c34b", W1, h[1], 342),
             cap(v("7:14"), "left: 12px; top: 12px", size=10.5, maxw=560) + vref("GEN 7:14", "right: 12px; bottom: 12px"))
    r3 = cols(new(STORM, W2, h[2], Y.rain(W2, h[2], 343) + V.rays(W2 * 0.7, -30, 26, 20, h[2] * 1.4, color="#FFF4C2", op=0.3)
                  + Y.ark_hull(-60, h[2] * 0.95, 420, h[2] * 0.55, "p34c", open_=True),
                  cap(v("7:15"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + cap(v("7:16", to="commanded him:"), "left: 8px; top: 96px", size=10.5, maxw=320) + vref("GEN 7:15–16", "right: 8px; bottom: 8px")),
              use(Ark[3], over=cap(v("7:16", frm="and Jehovah shut"), "left: 8px; bottom: 10px", size=15, maxw=280)
                  + sfx("ズゥゥン", "ZUUUN", "right: 12px; top: 16px", size=40, fill="#FFD23F", stroke="#0D0D0F", rot=6)))
    r4 = use(Del[1], over=cap(v("7:17"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 7:17", "right: 12px; bottom: 12px"))
    return page("Genesis 7:13–17 — Jehovah Shut Him In", t, r1 + r2 + r3 + r4, START + 13)


@P("GEN-C02-P15-Prevailed", "31 · The Waters Prevailed")
def p15():
    t, h = rows(250, 290, 220, None)
    r1 = new(GREY, W1, h[0], Y.high_waters(W1, h[0], 351),
             cap(v("7:18"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + cap(v("7:19") + " " + v("7:20"), "right: 12px; top: 12px", size=10.5, maxw=320) + vref("GEN 7:18–20", "right: 12px; bottom: 12px"))
    r2 = new("#0F3A5A", W1, h[1], Y.under_the_flood(W1, h[1], 352),
             cap(v("7:21") + " " + v("7:22"), "left: 12px; bottom: 14px", size=11, maxw=500) + vref("GEN 7:21–22", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], Y.lone_ark(W1, h[2], 353),
             cap(v("7:23", to="from the earth:"), "left: 12px; top: 12px", size=10.5, maxw=440)
             + cap(v("7:23", frm="and Noah only"), "right: 12px; bottom: 14px", size=13, maxw=300) + vref("GEN 7:23", "left: 12px; bottom: 12px"))
    r4 = new(GREY, W1, h[3], Y.sea(W1, h[3], h[3] * 0.5, 354, amp=6) + Y.ark_afloat(W1 * 0.1, h[3] * 0.5 - 4, 160, "p35d"),
             f'    <span data-label style="position: absolute; right: 16px; top: 12px; padding: 4px 10px; border: 2px solid #D7261E; background: #F3EFE6; color: #D7261E; font-family: Anton, sans-serif; font-size: 26px; letter-spacing: 0.06em">DAY 150</span>\n'
             + cap(v("7:24"), "left: 12px; top: 12px", size=12.5, maxw=380) + vref("GEN 7:24", "right: 12px; bottom: 12px"))
    return page("Genesis 7:18–24 — The Waters Prevailed", t, r1 + r2 + r3 + r4, START + 14)


@P("GEN-C02-P16-Remembered", "32 · God Remembered Noah")
def p16():
    t, h = rows(230, 230, 300, None)
    r1 = use(Dov[0], over=cap(v("8:1"), "left: 12px; bottom: 12px", size=11, maxw=470)
             + sfx("ヒュオオ", "HYUOO", "right: 18px; top: 14px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("GEN 8:1", "right: 12px; bottom: 12px"))
    r2 = new(GREY, W1, h[1], Y.parting(W1, h[1], 362),
             cap(v("8:2"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + cap(v("8:3"), "right: 12px; bottom: 14px", size=10.5, maxw=320) + vref("GEN 8:2–3", "left: 12px; bottom: 12px"))
    r3 = use(Dov[1], over=cap(v("8:4"), "right: 12px; top: 12px", size=12, maxw=250) + vref("GEN 8:4", "right: 12px; bottom: 12px"))
    r4 = new("linear-gradient(180deg, #FFC14D 0%, #8FD0E2 100%)", W1, h[3], Y.peaks(W1, h[3], 364),
             cap(v("8:5"), "left: 12px; top: 12px", size=11, maxw=500) + vref("GEN 8:5", "right: 12px; bottom: 12px"))
    return page("Genesis 8:1–5 — God Remembered Noah", t, r1 + r2 + r3 + r4, START + 15)


@P("GEN-C02-P17-Raven", "33 · The Raven and the Dove")
def p17():
    t, h = rows(290, 250, 260, None)
    r1 = new("#7A4A26", W1, h[0], Y.ark_window(W1, h[0]),
             cap(v("8:6"), "left: 12px; top: 12px", size=11, maxw=140) + vref("GEN 8:6", "right: 12px; bottom: 12px"))
    r2 = cols(use(Dov[2], over=cap(v("8:7"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("GEN 8:7", "right: 8px; top: 8px")),
              new(SKY, W2, h[1], Y.dove_out(W2, h[1], 372),
                  cap(v("8:8"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("GEN 8:8", "right: 8px; top: 8px")))
    r3 = new(SKY, W1, h[2], Y.hand_dove(W1, h[2], 373),
             cap(v("8:9"), "right: 12px; bottom: 12px", size=10.5, maxw=430) + vref("GEN 8:9", "right: 12px; top: 12px"))
    r4 = new(DAWN, W1, h[3], Y.sea(W1, h[3], h[3] * 0.62, 374, color="#2C7DA0", amp=4) + Y.ark_afloat(W1 * 0.06, h[3] * 0.62 - 2, 200, "p37d") + Y.dove(W1 * 0.3, h[3] * 0.36, 0.8),
             cap(v("8:10"), "right: 12px; top: 12px", size=11.5, maxw=360) + vref("GEN 8:10", "left: 12px; bottom: 12px"))
    return page("Genesis 8:6–10 — The Raven and the Dove", t, r1 + r2 + r3 + r4, START + 16)


@P("GEN-C02-P18-OliveLeaf", "34 · An Olive-Leaf Plucked Off")
def p18():
    t, h = rows(290, 210, 290, None)
    r1 = cols(use(Dov[3], over=cap(v("8:11", to="plucked off:"), "left: 8px; bottom: 8px", size=11, maxw=320) + vref("GEN 8:11", "right: 8px; top: 8px")),
              new("radial-gradient(circle at 30% 40%, #FFF4C2 0 30px, #9FE0FF 160px, #2C7DA0 360px)", W2, h[0], face(Y.NOAH_AWE, -50, 0, 0.74),
                  cap(v("8:11", frm="so Noah knew"), "right: 8px; bottom: 8px", size=11, maxw=170)))
    r2 = new(SKY, W1, h[1], Y.dove_away(W1, h[1], 382),
             cap(v("8:12"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 8:12", "right: 12px; bottom: 12px"))
    r3 = new("linear-gradient(180deg, #FFE3B8 0%, #8FD0E2 100%)", W1, h[2], defs("c38c", *ALL) + Y.ark_roof("c38c", W1, h[2], 383),
             cap(v("8:13"), "left: 12px; top: 12px", size=11, maxw=400) + vref("GEN 8:13", "right: 12px; top: 12px"))
    r4 = cols(new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", W2, h[3], Y.dry_ground(W2, h[3], 384),
                  cap(v("8:14"), "left: 8px; top: 8px", size=10.5, maxw=230) + vref("GEN 8:14", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[3], cosmic(W2, h[3]),
                  cap(v("8:15"), "left: 8px; top: 8px", size=10)
                  + god(v("8:16"), "left: 8px; top: 44px", size=15, maxw=320) + vref("GEN 8:15–16", "right: 8px; bottom: 8px")))
    return page("Genesis 8:11–16 — An Olive-Leaf Plucked Off", t, r1 + r2 + r3 + r4, START + 17)


@P("GEN-C02-P19-Altar", "35 · Seedtime and Harvest")
def p19():
    t, h = rows(250, 230, 250, None)
    r1 = new(SKY, W1, h[0], V.rays(W1 / 2, -40, 36, 40, W1, color="#FFF4C2", op=0.3) + Y.pairs("c39a", W1, h[0], 391),
             god(v("8:17"), "left: 12px; top: 12px", size=13.5, maxw=560) + vref("GEN 8:17", "right: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #FFE3B8 0%, #8FD0E2 100%)", W1, h[1], defs("c39b", *ALL) + Y.go_forth("c39b", W1, h[1], 392),
             cap(v("8:18"), "right: 12px; top: 12px", size=10.5, maxw=300)
             + cap(v("8:19"), "left: 12px; bottom: 12px", size=10.5, maxw=360) + vref("GEN 8:18–19", "right: 12px; bottom: 12px"))
    r3 = new("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", W1, h[2], defs("c39c", *ALL) + Y.noah_altar("c39c", W1, h[2], 393),
             cap(v("8:20"), "left: 12px; top: 12px", size=11.5, maxw=330) + vref("GEN 8:20", "left: 12px; bottom: 12px"))
    r4 = cols(new(NIGHT, W2, h[3], cosmic(W2, h[3]),
                  cap(v("8:21", to="in his heart,"), "left: 8px; top: 8px", size=9.5, maxw=320)
                  + god(v("8:21", frm="I will not"), "left: 8px; top: 62px", size=12.5, maxw=320) + vref("GEN 8:21", "right: 8px; bottom: 8px")),
              new("#12113A", W2, h[3], Y.seasons(W2, h[3], 394),
                  god(v("8:22"), "left: 8px; top: 8px", size=14, maxw=320) + vref("GEN 8:22", "right: 8px; bottom: 8px")))
    return page("Genesis 8:17–22 — Seedtime and Harvest", t, r1 + r2 + r3 + r4, START + 18)


@P("GEN-C02-P20-Blessed", "36 · Be Fruitful, and Multiply")
def p20():
    t, h = rows(210, 240, 280, None)
    r1 = new(DAWN, W1, h[0], defs("c40a", *ALL) + V.rays(W1 / 2, -30, 36, 30, W1, color="#FFF4C2", op=0.35)
             + Y.ground(W1, h[0], h[0] * 0.9, "#2A3A1E", dy=0) + Y.family8("c40a", 420, 680, round(h[0] * 0.9), Y.fit(h[0] * 0.9, h[0] * 0.2)),
             cap(v("9:1", to="unto them,"), "left: 12px; top: 12px", size=10.5, maxw=340)
             + god(v("9:1", frm="Be fruitful"), "left: 12px; top: 72px", size=17, maxw=340) + vref("GEN 9:1", "right: 12px; top: 12px"))
    r2 = new(SKY, W1, h[1], Y.dominion(W1, h[1], 402),
             god(v("9:2"), "left: 12px; top: 12px", size=13.5, maxw=640) + vref("GEN 9:2", "right: 12px; bottom: 12px"))
    r3 = cols(new(SKY, W2, h[2], Y.green_herb(W2, h[2], 403),
                  god(v("9:3"), "left: 8px; top: 8px", size=15, maxw=320) + vref("GEN 9:3", "right: 8px; bottom: 8px")),
              new("#2A0A0A", W2, h[2], Y.blood_drop(W2, h[2]),
                  god(v("9:4"), "left: 8px; top: 8px", size=15, maxw=320) + vref("GEN 9:4", "right: 8px; bottom: 8px")))
    r4 = cols(new(NIGHT, W2, h[3], cosmic(W2, h[3]),
                  god(v("9:5"), "left: 8px; top: 8px", size=12.5, maxw=320) + vref("GEN 9:5", "right: 8px; bottom: 8px")),
              new("#2A1A2E", W2, h[3], defs("c40d", *ALL) + Y.image_of_god("c40d", W2, h[3]),
                  god(v("9:6"), "left: 8px; top: 8px", size=13, maxw=320) + vref("GEN 9:6", "right: 8px; bottom: 8px")))
    return page("Genesis 9:1–6 — Be Fruitful, and Multiply", t, r1 + r2 + r3 + r4, START + 19)


@P("GEN-C02-P21-Token", "37 · The Token of the Covenant")
def p21():
    t, h = rows(230, 230, 250, None)
    r1 = new("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", W1, h[0], defs("c41a", *ALL) + Y.multitude("c41a", W1, h[0], 411),
             god(v("9:7"), "left: 12px; top: 12px", size=15, maxw=380) + vref("GEN 9:7", "right: 12px; top: 12px"))
    r2 = new(NIGHT, W1, h[1], defs("c41b", *ALL) + cosmic(W1, h[1]) + Y.ground(W1, h[1], h[1] * 0.9, "#1A1430", dy=0)
             + Y.family8("c41b", 420, 680, round(h[1] * 0.9), Y.fit(h[1] * 0.9, h[1] * 0.2)),
             cap(v("9:8"), "left: 12px; top: 12px", size=10.5, maxw=360)
             + god(v("9:9"), "left: 12px; top: 72px", size=16, maxw=360) + vref("GEN 9:8–9", "right: 12px; top: 12px"))
    r3 = new(SKY, W1, h[2], Y.pairs("c41c", W1, h[2], 413),
             god(v("9:10"), "left: 12px; top: 12px", size=13.5, maxw=600) + vref("GEN 9:10", "right: 12px; bottom: 12px"))
    r4 = cols(new(STORM, W2, h[3], Y.sea(W2, h[3], h[3] * 0.7, 414, amp=6),
                  god(v("9:11"), "left: 8px; top: 8px", size=13, maxw=320) + vref("GEN 9:11", "right: 8px; bottom: 8px")),
              new(GREY, W2, h[3], Y.covenant_sky(W2, h[3] * 0.62, 415),
                  cap(v("9:12", to="said,"), "left: 8px; top: 8px", size=10)
                  + god(v("9:12", frm="This is"), "left: 8px; bottom: 8px", size=12.5, maxw=320) + vref("GEN 9:12", "right: 8px; bottom: 8px")))
    return page("Genesis 9:7–12 — The Token of the Covenant", t, r1 + r2 + r3 + r4, START + 20)


@P("GEN-C02-P22-Bow", "38 · My Bow in the Cloud")
def p22():
    t, h = rows(600, None)
    r1 = use(Cov[0], over=god(v("9:13"), "left: 50%; top: 18px; transform: translateX(-50%)", size=22, maxw=520)
             + god(v("9:14"), "right: 12px; top: 300px", size=13, maxw=230) + vref("GEN 9:13–14", "left: 12px; bottom: 12px"))
    r2 = cols(new(GREY, W2, h[1], defs("c42b", *ALL) + Y.all_flesh("c42b", W2, h[1], 422),
                  god(v("9:15"), "left: 8px; top: 8px", size=14, maxw=320) + vref("GEN 9:15", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[1], cosmic(W2, h[1]),
                  god(v("9:16"), "left: 8px; top: 8px", size=13.5, maxw=320)
                  + cap(v("9:17", to="Noah,"), "left: 8px; top: 196px", size=10)
                  + god(v("9:17", frm="This is"), "left: 8px; top: 232px", size=13.5, maxw=320) + vref("GEN 9:16–17", "right: 8px; bottom: 8px")))
    return page("Genesis 9:13–17 — My Bow in the Cloud", t, r1 + r2, START + 21)


@P("GEN-C02-P23-Vineyard", "39 · A Vineyard")
def p23():
    t, h = rows(230, 230, 250, None)
    r1 = new(DAWN, W1, h[0], defs("c43a", *ALL) + Y.noah_and_sons("c43a", W1, h[0]),
             cap(v("9:18"), "right: 12px; top: 12px", size=10.5, maxw=320)
             + cap(v("9:19"), "right: 12px; bottom: 14px", size=10.5, maxw=320) + vref("GEN 9:18–19", "left: 12px; top: 12px"))
    r2 = new(SKY, W1, h[1], defs("c43b", *ALL) + Y.vineyard("c43b", W1, h[1], 432),
             cap(v("9:20"), "left: 12px; top: 12px", size=12, maxw=360) + vref("GEN 9:20", "right: 12px; top: 12px"))
    r3 = new(NIGHT, W1, h[2], Y.tent_night(W1, h[2], 433),
             cap(v("9:21"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("9:22"), "left: 12px; bottom: 14px", size=11, maxw=300) + vref("GEN 9:21–22", "right: 12px; top: 12px"))
    r4 = new(NIGHT, W1, h[3], defs("c43d", *ALL) + Y.garment_backward("c43d", W1, h[3], 434),
             cap(v("9:23"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 9:23", "left: 12px; top: 12px"))
    return page("Genesis 9:18–23 — A Vineyard", t, r1 + r2 + r3 + r4, START + 22)


@P("GEN-C02-P24-Days", "40 · All the Days of Noah")
def p24():
    t, h = rows(330, 290, None)
    r1 = new("radial-gradient(circle at 25% 50%, #FFC14D 0 20px, #B5421E 200px, #2A0A0A 460px)", W1, h[0], face(Y.NOAH_WAKE, -30, -20, 0.92),
             cap(v("9:24"), "left: 330px; top: 14px", size=11, maxw=340)
             + cap(v("9:25", to="said,"), "left: 330px; top: 92px", size=10.5)
             + balloon(v("9:25", frm="Cursed"), "left: 330px; top: 130px", 300, size=14, pad="24px 30px") + vref("GEN 9:24–25", "right: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("c44b", *ALL) + V.rays(W1 * 0.24, h[1] * 0.4, 30, 30, W1, color="#FFF4C2", op=0.3)
             + Y.ground(W1, h[1], h[1] * 0.88, "#2A3A1E", dy=0) + Y.noah("c44b", 170, round(h[1] * 0.88), round(Y.fit(h[1] * 0.88, h[1] * 0.14) * 200 / 250, 3), up=[(-22, -158), (-10, -200), (10, -236)]),
             cap(v("9:26", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("9:26", frm="Blessed"), "left: 290px; top: 46px", 210, size=12.5, pad="18px 22px")
             + balloon(v("9:27"), "right: 12px; top: 120px", 220, size=12.5, pad="18px 22px") + vref("GEN 9:26–27", "right: 12px; top: 12px"))
    r3 = new(DUSK, W1, h[2], Y.cairn_sunset(W1, h[2], 443),
             cap(v("9:28"), "left: 12px; top: 12px", size=12, maxw=360)
             + cap(v("9:29"), "left: 12px; top: 74px", size=14, maxw=360)
             + end_mark("NEXT · THE NATIONS AND BABEL", "right: 14px; bottom: 12px") + vref("GEN 9:28–29", "left: 12px; bottom: 12px"))
    return page("Genesis 9:24–29 — All the Days of Noah", t, r1 + r2 + r3, START + 23)
