"""Genesis volume, Chapter 1 — In the Beginning (Genesis 1–3). Every verse, word for word from ref/asv."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import use, new, vref, day_stamp, page, chapter_title, end_mark, cols, cap, god, tail, balloon, sfx
from reuse import panels
from genesis import G, art as X
from mk import defs, face

v, sp = G.v, G.span
D = {n: panels(f"digest/genesis/book-01/{n}.dc.html") for n in ["P01-Darkness", "P02-Firmament", "P03-Land", "P04-Life", "P05-Eden", "P06-Serpent", "P07-Exile"]}
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
NIGHT = "linear-gradient(180deg, #05050A 0%, #12113A 60%, #2A1A5E 100%)"
DUSK = "linear-gradient(180deg, #12113A 0%, #4A1D55 45%, #FF8A3D 100%)"
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("GEN-C01-00-Title", "Chapter 1 · In the Beginning")
def title():
    svg = (X.starfield(760, 1080, 7, 260) + V.rays(380, 640, 48, 20, 1200, color="#FFF4C2", op=0.16)
           + '<circle cx="380" cy="640" r="60" fill="#FFF4C2" opacity="0.25"></circle><circle cx="380" cy="640" r="14" fill="#FFF4C2"></circle>')
    return chapter_title(1, "第一話", "In the Beginning", "Genesis 1 – 3", svg, NIGHT,
                         v("1:1"), "Genesis · Volume One · The Full Edition")


@P("GEN-C01-P01-Light", "01 · Let There Be Light")
def p01():
    r1 = new(NIGHT, 702, 244, X.starfield(702, 244, 11) + '<circle cx="351" cy="150" r="3" fill="#FFF4C2"></circle>',
             cap(v("1:1"), "left: 50%; top: 50%; transform: translate(-50%, -50%)", size=19, center=True, maxw=520) + vref("GEN 1:1"))
    r2 = cols(use(D["P01-Darkness"][0], over=cap(v("1:2", to="deep:"), "left: 10px; top: 10px", size=11, maxw=300)),
              use(D["P01-Darkness"][1], over=cap(v("1:2", frm="and the Spirit"), "left: 10px; top: 10px", size=11, maxw=300) + vref("GEN 1:2")))
    r3 = use(D["P01-Darkness"][3],
             over=cap(v("1:3", to="said,"), "left: 14px; top: 14px", size=12)
                  + god(v("1:3", frm="Let", to="light:"), "left: 14px; top: 54px", size=40)
                  + cap(v("1:3", frm="and there"), "right: 14px; top: 150px", size=13)
                  + sfx("ドン", "DON", "right: 30px; top: 20px", size=56, fill="#D7261E", stroke="#F3EFE6", rot=6)
                  + cap(v("1:4"), "left: 14px; bottom: 16px", size=11.5, maxw=420) + vref("GEN 1:3–4"))
    return page("Genesis 1:1–4 — Let There Be Light", "250px 230px minmax(0, 1fr)", r1 + r2 + r3, 1)


@P("GEN-C01-P02-Firmament", "02 · The Firmament")
def p02():
    r1 = use(D["P02-Firmament"][0], over=cap(v("1:5", to="Night."), "left: 12px; top: 12px", size=12, maxw=320)
             + cap(v("1:5", frm="And there was"), "right: 12px; bottom: 12px", size=11, maxw=300) + day_stamp(1, "left: 16px; bottom: 14px") + vref("GEN 1:5", "right: 12px; top: 12px"))
    r2 = use(D["P02-Firmament"][1], over=cap(v("1:6", to="said,"), "left: 12px; top: 12px", size=11)
             + god(v("1:6", frm="Let"), "left: 12px; top: 46px", size=19, maxw=380)
             + cap(v("1:7"), "right: 12px; bottom: 14px", size=11, maxw=380) + vref("GEN 1:6–7", "left: 12px; bottom: 12px"))
    r3 = cols(use(D["P02-Firmament"][2]),
              use(D["P02-Firmament"][3], over=cap(v("1:8", to="Heaven."), "left: 10px; top: 10px", size=12)
                  + cap(v("1:8", frm="And there"), "left: 10px; bottom: 12px", size=10.5, maxw=260) + day_stamp(2, "right: 12px; top: 10px") + vref("GEN 1:8")),
              tmpl="minmax(0, 1fr) minmax(0, 1.5fr)")
    return page("Genesis 1:5–8 — The Firmament", "290px minmax(0, 1fr) 270px", r1 + r2 + r3, 2)


@P("GEN-C01-P03-Land", "03 · The Dry Land")
def p03():
    r1 = use(D["P03-Land"][0], over=cap(v("1:9", to="said,"), "left: 12px; top: 12px", size=11)
             + god(v("1:9", frm="Let", to="appear:"), "left: 12px; top: 46px", size=17, maxw=330)
             + cap(v("1:9", frm="and it was so."), "right: 12px; top: 12px", size=11)
             + cap(v("1:10"), "right: 12px; bottom: 12px", size=10.5, maxw=330) + vref("GEN 1:9–10", "left: 12px; bottom: 12px"))
    r2 = cols(use(D["P03-Land"][1], over=cap(v("1:11", to="said,"), "left: 8px; top: 8px", size=10)
                  + god(v("1:11", frm="Let"), "left: 8px; top: 40px", size=13.5, maxw=316) + vref("GEN 1:11")),
              use(D["P03-Land"][2], over=cap(v("1:12"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 1:12")))
    r3 = new("linear-gradient(180deg, #2A1A5E 0%, #C2456A 70%, #FF8A3D 100%)", 702, 154, X.evening(702, 154, 3),
             cap(v("1:13"), "left: 12px; top: 12px", size=12) + day_stamp(3, "right: 16px; top: 12px", rot=4) + vref("GEN 1:13", "left: 12px; bottom: 10px"))
    return page("Genesis 1:9–13 — The Dry Land", "340px minmax(0, 1fr) 160px", r1 + r2 + r3, 3)


@P("GEN-C01-P04-Lights", "04 · The Two Great Lights")
def p04():
    r1 = use(D["P03-Land"][3], over=cap(v("1:14", to="said,"), "left: 12px; top: 12px", size=11)
             + god(v("1:14", frm="Let") + " " + v("1:15", to="earth:"), "left: 12px; top: 46px", size=16, maxw=360)
             + cap(v("1:15", frm="and it was so."), "left: 12px; bottom: 12px", size=11) + vref("GEN 1:14–15", "right: 12px; bottom: 12px"))
    r2 = cols(new(NIGHT, 342, 284, X.starfield(342, 284, 41, 220) + '<circle cx="260" cy="70" r="22" fill="#E8E2D6"></circle><circle cx="250" cy="64" r="20" fill="#12113A"></circle>',
                  cap(v("1:16"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("GEN 1:16", "right: 8px; top: 8px")),
              new("linear-gradient(180deg, #FFC14D 0%, #8FD0E2 100%)", 342, 284,
                  V.rays(171, -20, 30, 30, 500, color="#FFF4C2", op=0.5) + '<path d="M-10 230 C 100 200 240 220 352 200 L 352 300 L -10 300 Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>',
                  cap(v("1:17") + " " + v("1:18"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 1:17–18")))
    r3 = new("linear-gradient(180deg, #2A1A5E 0%, #7A3BA8 70%, #FF8A3D 100%)", 702, 154, X.evening(702, 154, 4, sun="#FFD23F"),
             cap(v("1:19"), "left: 12px; top: 12px", size=12) + day_stamp(4, "right: 16px; top: 12px", rot=4) + vref("GEN 1:19", "left: 12px; bottom: 10px"))
    return page("Genesis 1:14–19 — The Two Great Lights", "minmax(0, 1fr) 290px 160px", r1 + r2 + r3, 4)


@P("GEN-C01-P05-Waters", "05 · The Waters Swarm")
def p05():
    r1 = use(D["P04-Life"][0], over=cap(v("1:20", to="said,"), "left: 12px; top: 12px", size=11)
             + god(v("1:20", frm="Let"), "left: 12px; top: 46px", size=16, maxw=380)
             + sfx("ザバァン", "ZABAAN", "right: 20px; top: 16px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("GEN 1:20", "right: 12px; bottom: 12px"))
    r2 = cols(new("linear-gradient(180deg, #2C9DB8 0%, #12305A 100%)", 342, 284, X.fish_swarm(342, 284, 51),
                  cap(v("1:21", to="good."), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 1:21")),
              use(D["P04-Life"][1], over=cap(v("1:22", to="saying,"), "left: 8px; top: 8px", size=10)
                  + god(v("1:22", frm="Be fruitful"), "left: 8px; bottom: 10px", size=14, maxw=320) + vref("GEN 1:22", "right: 8px; top: 8px")))
    r3 = new("linear-gradient(180deg, #2A1A5E 0%, #C2456A 70%, #FFC14D 100%)", 702, 164, X.evening(702, 164, 5, sun="#FF8A3D"),
             cap(v("1:23"), "left: 12px; top: 12px", size=12) + day_stamp(5, "right: 16px; top: 12px", rot=4) + vref("GEN 1:23", "left: 12px; bottom: 10px"))
    return page("Genesis 1:20–23 — The Waters Swarm", "minmax(0, 1fr) 330px 170px", r1 + r2 + r3, 5)


@P("GEN-C01-P06-Image", "06 · In Our Image")
def p06():
    r1 = new("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 264, defs("c6a", *ALL) + X.beasts(702, 264, 61),
             cap(v("1:24", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("1:24", frm="Let"), "left: 12px; top: 44px", size=13, maxw=340)
             + cap(v("1:25"), "right: 12px; top: 12px", size=10, maxw=300) + vref("GEN 1:24–25", "right: 12px; bottom: 10px"))
    r2 = new(NIGHT, 702, 254, X.cosmic(702, 254),
             cap(v("1:26", to="said,"), "left: 12px; top: 12px", size=11)
             + god(v("1:26", frm="Let"), "left: 12px; top: 46px", size=18, maxw=660) + vref("GEN 1:26"))
    r3 = cols(new("radial-gradient(circle at 50% 70%, #FFF4C2 0 40px, #FFC14D 160px, #FF8A3D 360px)", 342, 362,
                  defs("c6c", *ALL) + V.rays(171, 250, 36, 30, 500, color="#FFF4C2", op=0.6)
                  + '<path d="M-10 300 L 352 300 L 352 372 L -10 372 Z" fill="#7A9A4A" stroke="#0D0D0F" stroke-width="2"></path>' + mk.person("c6c", 171, 300, 1.1, body=X.SKIN),
                  cap(v("1:27", to="created he him;"), "left: 8px; top: 8px", size=11, maxw=320)),
              new("linear-gradient(180deg, #FFE3B8 0%, #FFC14D 100%)", 342, 362,
                  defs("c6b", *ALL) + V.rays(171, 260, 30, 30, 500, color="#FFF4C2", op=0.5)
                  + '<path d="M-10 300 L 352 300 L 352 372 L -10 372 Z" fill="#7A9A4A" stroke="#0D0D0F" stroke-width="2"></path>' + X.couple("c6b", 171, 300, 1.0, hands=False),
                  cap(v("1:27", frm="male and female"), "left: 8px; top: 8px", size=14) + vref("GEN 1:27")))
    return page("Genesis 1:24–27 — In Our Image", "270px 260px minmax(0, 1fr)", r1 + r2 + r3, 6)


@P("GEN-C01-P07-VeryGood", "07 · Very Good")
def p07():
    r1 = new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294,
             defs("c7a", *ALL) + '<path d="M-10 230 L 712 224 L 712 304 L -10 304 Z" fill="#7A9A4A" stroke="#0D0D0F" stroke-width="2"></path>'
             + X.couple("c7a", 560, 270, 0.62),
             cap(v("1:28", to="unto them,"), "left: 12px; top: 12px", size=11)
             + god(v("1:28", frm="Be fruitful"), "left: 12px; top: 46px", size=15, maxw=420) + vref("GEN 1:28", "right: 12px; top: 12px"))
    r2 = new("linear-gradient(180deg, #FFE3B8 0%, #C9A86A 100%)", 702, 294, X.harvest(702, 294, 71),
             cap(v("1:29", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("1:29", frm="Behold") + " " + v("1:30", to="for food:"), "left: 12px; top: 44px", size=13.5, maxw=420)
             + cap(v("1:30", frm="and it was so."), "right: 12px; bottom: 12px", size=11) + vref("GEN 1:29–30", "left: 12px; bottom: 12px"))
    r3 = new("linear-gradient(180deg, #FFF4C2 0%, #FFC14D 50%, #FF8A3D 100%)", 702, 384,
             V.rays(351, 384, 40, 60, 900, color="#FFF4C2", op=0.5) + '<circle cx="351" cy="384" r="120" fill="#FFF4C2"></circle>',
             cap(v("1:31", to="very good."), "left: 50%; top: 40px; transform: translateX(-50%)", size=22, center=True, maxw=520)
             + cap(v("1:31", frm="And there was"), "left: 12px; bottom: 14px", size=11) + day_stamp(6, "right: 16px; bottom: 14px", rot=4) + vref("GEN 1:31", "right: 12px; top: 12px"))
    return page("Genesis 1:28–31 — Very Good", "300px 300px minmax(0, 1fr)", r1 + r2 + r3, 7)


@P("GEN-C01-P08-Dust", "08 · The Dust of the Ground")
def p08():
    r1 = use(D["P05-Eden"][0], over=cap(sp("2:1-3"), "left: 12px; top: 12px", size=11, maxw=500) + day_stamp(7, "right: 16px; bottom: 14px") + vref("GEN 2:1–3", "left: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #E8C88A 0%, #FFE3B8 100%)", 702, 254, X.mist(702, 254, 81),
             cap(v("2:4"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("2:5") + " " + v("2:6"), "right: 12px; top: 12px", size=10, maxw=330) + vref("GEN 2:4–6", "left: 12px; bottom: 12px"))
    r3 = cols(use(D["P04-Life"][3], over=cap(v("2:7", to="ground,"), "left: 8px; top: 8px", size=12, maxw=320) + vref("GEN 2:7")),
              use(D["P04-Life"][4], over=cap(v("2:7", frm="and breathed"), "left: 8px; bottom: 10px", size=12, maxw=320)))
    return page("Genesis 2:1–7 — The Dust of the Ground", "330px 260px minmax(0, 1fr)", r1 + r2 + r3, 8)


@P("GEN-C01-P09-Eden", "09 · A Garden Eastward, in Eden")
def p09():
    r1 = use(D["P05-Eden"][1], over=cap(v("2:8"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("2:9"), "right: 12px; top: 12px", size=10, maxw=310)
             + cap(v("2:10"), "left: 12px; top: 150px", size=10.5, maxw=300) + vref("GEN 2:8–10", "right: 12px; bottom: 34px"))
    r2 = cols(new("linear-gradient(180deg, #8FD0E2 0%, #C8A06A 100%)", 342, 420, X.gems(342, 420),
                  cap(v("2:11") + " " + v("2:12"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 2:11–12")),
              new("#7A9A4A", 342, 420, X.four_rivers(342, 420),
                  cap(v("2:13") + " " + v("2:14"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("GEN 2:13–14", "right: 8px; top: 8px")))
    return page("Genesis 2:8–14 — A Garden Eastward, in Eden", "560px minmax(0, 1fr)", r1 + r2, 9)


@P("GEN-C01-P10-Names", "10 · The Man Gave Names")
def p10():
    r1 = cols(use(D["P05-Eden"][2], over=cap(v("2:15"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("GEN 2:15", "right: 8px; top: 8px")),
              new(NIGHT, 342, 374, X.cosmic(342, 374),
                  cap(v("2:16", to="saying,"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + god(v("2:16", frm="Of every") + " " + v("2:17"), "left: 8px; top: 64px", size=15, maxw=320) + vref("GEN 2:16–17")))
    r2 = new(DUSK, 702, 214, defs("c10a", *ALL) + '<path d="M-10 180 L 712 176 L 712 224 L -10 224 Z" fill="#1A1430"></path>' + mk.person("c10a", 140, 182, 0.7, body="#0D0D0F"),
             cap(v("2:18", to="said,"), "left: 250px; top: 12px", size=10.5)
             + god(v("2:18", frm="It is not"), "left: 250px; top: 44px", size=16, maxw=420) + vref("GEN 2:18"))
    r3 = new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 394, defs("c10b", *ALL) + X.naming("c10b", 702, 394, 101),
             cap(v("2:19"), "left: 12px; top: 12px", size=10.5, maxw=400)
             + cap(v("2:20"), "right: 12px; top: 150px", size=10.5, maxw=300) + vref("GEN 2:19–20", "left: 12px; bottom: 12px"))
    return page("Genesis 2:15–20 — The Man Gave Names", "380px 220px minmax(0, 1fr)", r1 + r2 + r3, 10)


@P("GEN-C01-P11-Woman", "11 · Bone of My Bones")
def p11():
    r1 = cols(use(D["P06-Serpent"][0], over=cap(v("2:21"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 2:21")),
              new("radial-gradient(circle at 50% 60%, #FFF4C2 0 40px, #FFC14D 160px, #C2456A 330px)", 342, 254,
                  defs("c11a", *ALL) + V.rays(171, 170, 30, 30, 400, color="#FFF4C2", op=0.5) + mk.person("c11a", 171, 244, 0.9, body=X.SKIN, woman=True, hair=True),
                  cap(v("2:22"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 2:22")))
    r2 = use(D["P06-Serpent"][1], over=cap(v("2:23", to="said,"), "right: 12px; top: 12px", size=11)
             + balloon(v("2:23", frm="This is now"), "right: 14px; top: 50px", 300, size=14, pad="22px 30px") + vref("GEN 2:23", "left: 12px; bottom: 12px"))
    r3 = new("linear-gradient(180deg, #12113A 0%, #C2456A 50%, #FFC14D 100%)", 702, 304, defs("c11b", *ALL) + X.dawn_couple("c11b", 702, 304),
             cap(v("2:24"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("2:25"), "right: 12px; top: 12px", size=11, maxw=280) + vref("GEN 2:24–25", "left: 12px; bottom: 12px"))
    return page("Genesis 2:21–25 — Bone of My Bones", "260px 320px minmax(0, 1fr)", r1 + r2 + r3, 11)


@P("GEN-C01-P12-Serpent", "12 · Yea, Hath God Said?")
def p12():
    r1 = use(D["P06-Serpent"][2], over=cap(v("3:1", to="had made."), "left: 12px; top: 12px", size=12, maxw=360)
             + sfx("シュルル", "SHURURU", "right: 20px; bottom: 20px", size=36, fill="#5E8F26", stroke="#F3EFE6", rot=-6) + vref("GEN 3:1", "left: 12px; bottom: 12px"))
    r2 = use(D["P06-Serpent"][3], over=cap(v("3:1", frm="And he said", to="woman,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("3:1", frm="Yea"), "right: 14px; top: 46px", 330, size=14, pad="18px 30px")
             + cap(v("3:2", to="serpent,"), "right: 12px; top: 150px", size=10.5)
             + balloon(v("3:2", frm="Of the fruit") + " " + v("3:3"), "right: 14px; top: 186px", 380, size=13, pad="22px 34px") + vref("GEN 3:1–3", "left: 12px; bottom: 12px"))
    r3 = use(D["P06-Serpent"][4], over=cap(v("3:4", to="woman,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("3:4", frm="Ye shall") + " " + v("3:5"), "right: 14px; top: 14px", 360, size=14, pad="22px 34px") + vref("GEN 3:4–5", "left: 12px; bottom: 12px"))
    return page("Genesis 3:1–5 — Yea, Hath God Said?", "260px 380px minmax(0, 1fr)", r1 + r2 + r3, 12)


@P("GEN-C01-P13-Eyes", "13 · Where Art Thou?")
def p13():
    a, b, c = D["P07-Exile"][0], D["P07-Exile"][1], D["P07-Exile"][2]
    r1 = cols(use(a, over=cap(v("3:6", to="wise,"), "left: 6px; top: 6px", size=9.5, maxw=210)),
              use(b, over=cap(v("3:6", frm="she took", to="did eat;"), "left: 6px; bottom: 6px", size=10, maxw=210)),
              use(c, over=cap(v("3:6", frm="and she gave"), "left: 6px; top: 6px", size=10, maxw=210) + vref("GEN 3:6")))
    r2 = use(D["P07-Exile"][3], over=cap(v("3:7", to="naked;"), "left: 12px; bottom: 10px", size=11.5, maxw=500) + vref("GEN 3:7", "right: 12px; top: 10px"))
    r3 = cols(new("linear-gradient(180deg, #2A3A1E 0%, #5E8F26 100%)", 342, 214, X.fig_leaves(342, 214, 131),
                  cap(v("3:7", frm="and they sewed"), "left: 8px; top: 8px", size=10.5, maxw=320)),
              new("linear-gradient(180deg, #8FD0E2 0%, #2A3A1E 100%)", 342, 214, X.walking_voice(342, 214, 132),
                  cap(v("3:8"), "left: 8px; top: 8px", size=9.5, maxw=320) + vref("GEN 3:8")))
    r4 = cols(new(NIGHT, 342, 224, X.cosmic(342, 224),
                  cap(v("3:9", to="unto him,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + god(v("3:9", frm="Where"), "left: 8px; top: 70px", size=30) + vref("GEN 3:9")),
              new("radial-gradient(circle at 30% 50%, #C8D0DE 0 20px, #2A3A6A 150px, #05050A 330px)", 342, 224, face(X.ADAM_AFRAID, -40, -10, 0.6),
                  cap(v("3:10", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("3:10", frm="I heard"), "right: 6px; bottom: 8px", 190, size=11.5, pad="16px 18px") + vref("GEN 3:10", "left: 8px; bottom: 8px")))
    return page("Genesis 3:6–10 — Where Art Thou?", "220px 190px 220px minmax(0, 1fr)", r1 + r2 + r3 + r4, 13)


@P("GEN-C01-P14-Curse", "14 · What Is This Thou Hast Done?")
def p14():
    r1 = new(NIGHT, 702, 184, X.cosmic(702, 184),
             cap(v("3:11", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("3:11", frm="Who told"), "left: 12px; top: 46px", size=18, maxw=660) + vref("GEN 3:11"))
    r2 = cols(new("radial-gradient(circle at 30% 50%, #C8D0DE 0 20px, #5A6E8A 150px, #12113A 330px)", 342, 244, face(X.ADAM_AFRAID, -50, -10, 0.66),
                  cap(v("3:12", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("3:12", frm="The woman"), "right: 6px; bottom: 8px", 190, size=11.5, pad="16px 18px") + vref("GEN 3:12", "left: 8px; bottom: 8px")),
              new("radial-gradient(circle at 70% 50%, #F3EFE6 0 20px, #C2456A 150px, #4A1D55 330px)", 342, 244, face(X.EVE_AFRAID, 392, -10, 0.66, flip=True),
                  cap(v("3:13", to="woman,"), "left: 8px; top: 8px", size=9.5, maxw=200)
                  + god(v("3:13", frm="What is", to="done?"), "left: 8px; top: 60px", size=13, maxw=190)
                  + cap(v("3:13", frm="And the woman said,"), "left: 8px; bottom: 8px", size=10, maxw=190) + vref("GEN 3:13", "right: 8px; top: 8px")))
    r3 = new("linear-gradient(180deg, #4A1D55 0%, #8A4A3A 100%)", 702, 294, X.serpent_dust(702, 294, 141),
             cap(v("3:14", to="serpent,"), "left: 12px; top: 12px", size=10.5)
             + god(v("3:14", frm="Because") + " " + v("3:15"), "left: 12px; top: 44px", size=13.5, maxw=660) + vref("GEN 3:14–15", "right: 12px; bottom: 12px"))
    r4 = new("radial-gradient(circle at 25% 50%, #F3EFE6 0 20px, #C2456A 160px, #2A0A1A 460px)", 702, 254, face(X.EVE_SORROW, -30, -30, 0.7),
             cap(v("3:16", to="said,"), "left: 300px; top: 12px", size=10.5)
             + god(v("3:16", frm="I will"), "left: 300px; top: 44px", size=14, maxw=380) + vref("GEN 3:16"))
    return page("Genesis 3:11–16 — What Is This Thou Hast Done?", "190px 250px 300px minmax(0, 1fr)", r1 + r2 + r3 + r4, 14)


@P("GEN-C01-P15-Thorns", "15 · Dust Thou Art")
def p15():
    r1 = new("radial-gradient(circle at 25% 50%, #C8D0DE 0 20px, #5A6E8A 200px, #12113A 460px)", 702, 404, face(X.ADAM_GRIEF, -40, 20, 0.86),
             cap(v("3:17", to="said,"), "left: 330px; top: 12px", size=10.5)
             + god(v("3:17", frm="Because"), "left: 330px; top: 44px", size=15, maxw=360) + vref("GEN 3:17"))
    r2 = new("linear-gradient(180deg, #4A1D55 0%, #8A6A4A 100%)", 702, 254, X.thorns(702, 254, 151),
             cap(v("3:18"), "left: 12px; top: 12px", size=13, maxw=420) + vref("GEN 3:18"))
    r3 = new("linear-gradient(180deg, #FFC14D 0%, #E8A35A 100%)", 702, 324, X.toil("c15", 702, 324, 152),
             god(v("3:19"), "left: 12px; top: 12px", size=17, maxw=420) + vref("GEN 3:19"))
    return page("Genesis 3:17–19 — Dust Thou Art", "minmax(0, 1fr) 260px 330px", r1 + r2 + r3, 15)


@P("GEN-C01-P16-East", "16 · East of Eden")
def p16():
    r1 = cols(new("radial-gradient(circle at 30% 50%, #FFF4C2 0 20px, #FFC14D 150px, #C2456A 330px)", 342, 284, face(X.EVE, -40, 0, 0.7),
                  cap(v("3:20"), "right: 8px; top: 8px", size=10.5, maxw=170) + vref("GEN 3:20", "left: 8px; bottom: 8px")),
              new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 342, 284, defs("c16a", *ALL) + X.skins("c16a", 342, 284),
                  cap(v("3:21"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 3:21")))
    r2 = new(NIGHT, 702, 214, X.cosmic(702, 214),
             cap(v("3:22", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("3:22", frm="Behold"), "left: 12px; top: 44px", size=16, maxw=660) + vref("GEN 3:22"))
    r3 = use(D["P07-Exile"][5], over=cap(v("3:23"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("3:24"), "right: 12px; top: 12px", size=10.5, maxw=300)
             + end_mark("NEXT · CAIN AND ABEL", "right: 14px; bottom: 12px") + vref("GEN 3:23–24", "left: 12px; bottom: 12px"))
    return page("Genesis 3:20–24 — East of Eden", "290px 220px minmax(0, 1fr)", r1 + r2 + r3, 16)
