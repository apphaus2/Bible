"""Numbers volume, Chapter 11 — Balaam (Numbers 22–24). Every verse, word for word from ref/asv.
Balak and the elders of Moab and Midian; Balaam at Pethor; God's word by night; the ass, the angel of Jehovah and the
narrow path (the digest's panels); the seven altars on the high places of Baal, on Pisgah and on Peor; and the four
parables in song boxes over the camp of Israel, ending with the star out of Jacob (the digest's star)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, numbers1 as N
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import art as A
from exo.kit import talk, song
from num import G, art as K, art11 as K11
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import COLD, EMBER
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED, BLUE
from num import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
B1 = "reference/numbers/book-01/"
D7, D8 = (panels(B1 + n + ".dc.html") for n in ["NU1-P07-Ass", "NU1-P08-Star"])
VISTA = "#E8C88A"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())
def parable(h, lead_ref, lead_to, refs_text, ref_label, size=17, seed=1, extra=""):
    return new(VISTA, W1, h, K11.vista(W1, h, seed), cap(v(lead_ref, to=lead_to), "left: 12px; top: 12px", size=11)
               + song(refs_text, "left: 12px; top: 50px", size=size, maxw=600, color="#7A3BA8") + vref(ref_label, "right: 12px; bottom: 12px") + extra)


@P("NUM-C11-00-Title", "Chapter 11 · Balaam", title=True)
def title(n):
    a = D7[1]
    svg = f'<g transform="translate(-380 300) scale(1.9)">{a.svg}</g>'
    return chapter_title(11, "第十一話", "Balaam", "Numbers 22 – 24", svg, a.bg, v("24:17", frm="There shall come forth", to="out of Israel,"), "Numbers · Volume Four")


@P("NUM-C11-P01-Moab", "Moab Was Sore Afraid")
def p01(n):
    t, h = rows(220, None)
    r1 = new(DUSK, W1, h[0], K.wilderness_camp("u1a", W1, h[0], 1111, dusk=True, sinai=False), cap(v("22:1"), "left: 12px; top: 12px", size=12.5, maxw=500) + mk.stamp(22, "right: 14px; top: 12px") + vref("NUM 22:1", "right: 12px; bottom: 12px"))
    r2 = new("#E8B880", W1, h[1], K11.moab_walls("u1b", W1, h[1], 1112), cap(v("22:2") + " " + v("22:3"), "left: 12px; top: 12px", size=12, maxw=420)
             + cap(v("22:4", to="And Moab said unto the elders of Midian,"), "right: 12px; top: 130px", size=11, maxw=300)
             + balloon(v("22:4", frm="Now will this", to="field."), "right: 16px; top: 190px", 300, size=13, pad="18px 22px") + cap(v("22:4", frm="And Balak the son"), "left: 12px; bottom: 30px", size=11, maxw=360) + vref("NUM 22:2–4", "right: 12px; bottom: 12px"))
    return page("Numbers 22:1–4 — Moab Was Sore Afraid", t, r1 + r2, n)


@P("NUM-C11-P02-Curse", "Curse Me This People")
def p02(n):
    t, h = rows(None, 280)
    r1 = talk(K11.BALAK, h[0], EMBER, [("cap", v("22:5", to="to call him, saying,")), ("say", after("22:5", "to call him, saying,") + " " + v("22:6"))], ref="NUM 22:5–6", size=16)
    r2 = new(SKY, W1, h[1], K11.messengers("u2b", W1, h[1], 1122), cap(v("22:7"), "left: 12px; top: 12px", size=12, maxw=500) + vref("NUM 22:7", "right: 12px; bottom: 12px"))
    return page("Numbers 22:5–7 — Curse Me This People", t, r1 + r2, n)


@P("NUM-C11-P03-Pethor", "What Men Are These with Thee?")
def p03(n):
    t, h = rows(240, None, 230)
    r1 = new(SKY, W1, h[0], K11.messengers("u3a", W1, h[0], 1131, arrived=True), cap(v("22:8", to="said unto them,"), "left: 12px; top: 12px", size=11)
             + balloon(v("22:8", frm="Lodge here", to="unto me:"), "left: 18px; top: 50px", 360, size=13, pad="16px 22px") + cap(v("22:8", frm="and the princes"), "right: 12px; bottom: 30px", size=11) + vref("NUM 22:8", "right: 12px; bottom: 8px"))
    r2 = night(h[1], cap(v("22:9", to="and said,"), "left: 12px; top: 12px", size=11) + god(v("22:9", frm="What men"), "left: 12px; top: 50px", size=19, maxw=500)
               + cap(v("22:10", to="said unto God,"), "right: 12px; top: 120px", size=11) + balloon(after("22:10", "said unto God,") + " " + v("22:11"), "right: 16px; top: 160px", 400, size=13, pad="20px 28px") + vref("NUM 22:9–11", "right: 12px; bottom: 12px"))
    r3 = night(h[2], cap(v("22:12", to="unto Balaam,"), "left: 12px; top: 12px", size=11) + god(after("22:12", "unto Balaam,"), "left: 12px; top: 50px", size=21, maxw=600) + vref("NUM 22:12", "right: 12px; bottom: 12px"))
    return page("Numbers 22:8–12 — What Men Are These with Thee?", t, r1 + r2 + r3, n)


@P("NUM-C11-P04-Refuseth", "Balaam Refuseth to Come with Us")
def p04(n):
    t, h = rows(240, 200, None)
    r1 = talk(K11.BALAAM, h[0], DUSK, [("cap", v("22:13", to="the princes of Balak,")), ("say", after("22:13", "the princes of Balak,"))], ref="NUM 22:13", size=15)
    r2 = talk(K11.ELDER_MOAB, h[1], EMBER, [("cap", v("22:14", to="and said,")), ("say", after("22:14", "and said,"))], ref="NUM 22:14", size=17, flip=True)
    r3 = new(SKY, W1, h[2], K11.messengers("u4c", W1, h[2], 1143, arrived=True), cap(v("22:15") + " " + v("22:16", to="said to him,"), "left: 12px; top: 12px", size=11.5, maxw=440)
             + balloon(after("22:16", "said to him,") + " " + v("22:17"), "left: 18px; top: 100px", 420, size=13, pad="22px 28px") + vref("NUM 22:15–17", "right: 12px; bottom: 12px"))
    return page("Numbers 22:13–17 — Balaam Refuseth to Come with Us", t, r1 + r2 + r3, n)


@P("NUM-C11-P05-HouseFull", "His House Full of Silver and Gold")
def p05(n):
    t, h = rows(None, 280)
    r1 = talk(K11.BALAAM, h[0], DUSK, [("cap", v("22:18", to="the servants of Balak,")), ("say", after("22:18", "the servants of Balak,") + " " + v("22:19"))], ref="NUM 22:18–19", size=17)
    r2 = night(h[1], cap(v("22:20", to="said unto him,"), "left: 12px; top: 12px", size=11) + god(after("22:20", "said unto him,"), "left: 12px; top: 50px", size=21, maxw=620) + vref("NUM 22:20", "right: 12px; bottom: 12px"))
    return page("Numbers 22:18–20 — His House Full of Silver and Gold", t, r1 + r2, n)


@P("NUM-C11-P06-Way", "The Angel of Jehovah in the Way")
def p06(n):
    t, h = rows(294, 394, None)
    r1 = use(D7[0], over=cap(v("22:21") + " " + v("22:22"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("NUM 22:21–22", "right: 12px; bottom: 12px"))
    r2 = use(D7[1], over=cap(v("22:23"), "left: 12px; top: 12px", size=11.5, maxw=360) + sfx("バシッ", "BASHI!", "left: 40px; bottom: 30px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("NUM 22:23", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], K11.narrow("u6c", W1, h[2], 1163), cap(v("22:24") + " " + v("22:25") + " " + v("22:26"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("NUM 22:24–26", "right: 12px; bottom: 12px"))
    return page("Numbers 22:21–26 — The Angel of Jehovah in the Way", t, r1 + r2 + r3, n)


@P("NUM-C11-P07-Ass", "What Have I Done unto Thee?")
def p07(n):
    t, h = rows(294, 254, None)
    r1 = cols(use(D7[2], over=cap(v("22:27"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("NUM 22:27", "right: 8px; bottom: 8px")),
              use(D7[3], over=cap(v("22:28", to="said unto Balaam,"), "left: 8px; top: 8px", size=10.5, maxw=320) + balloon(after("22:28", "said unto Balaam,"), "left: 10px; top: 64px", 200, size=12, pad="18px 20px") + vref("NUM 22:28", "right: 8px; bottom: 8px")))
    r2 = use(D8[0], over=cap(v("22:29", to="unto the ass,"), "left: 120px; top: 12px", size=11) + balloon(after("22:29", "unto the ass,"), "right: 20px; top: 40px", 340, size=15, pad="18px 26px") + vref("NUM 22:29", "right: 12px; bottom: 12px"))
    r3 = new(GOLDEN, W1, h[2], f'<g transform="translate({W1 * 0.3:.0f} {h[2] * 0.92:.0f})">{N.ass(0, 0, min(1.6, h[2] / 180))}</g>',
             cap(v("22:30", to="unto Balaam,"), "right: 12px; top: 12px", size=11) + balloon(v("22:30", frm="Am not I", to="unto thee?"), "right: 16px; top: 52px", 380, size=15, pad="22px 28px")
             + cap(v("22:30", frm="and he said,"), "right: 12px; bottom: 30px", size=11.5) + vref("NUM 22:30", "left: 12px; bottom: 12px"))
    return page("Numbers 22:27–30 — What Have I Done unto Thee?", t, r1 + r2 + r3, n)


@P("NUM-C11-P08-Eyes", "Then Jehovah Opened the Eyes of Balaam")
def p08(n):
    t, h = rows(434, None)
    r1 = use(D8[1], over=cap(v("22:31"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("NUM 22:31", "right: 12px; bottom: 12px"))
    r2 = new("radial-gradient(circle at 70% 40%, #FFF8E0 0%, #FFD23F 40%, #E8886A 100%)", W1, h[1], mk.defs("u8b", *K.ALL) + N.angel("u8b", W1 * 0.8, h[1] * 0.96, h[1] / 240),
             cap(v("22:32", to="said unto him,"), "left: 12px; top: 12px", size=11) + god(after("22:32", "said unto him,") + " " + v("22:33"), "left: 12px; top: 50px", size=19, maxw=440) + vref("NUM 22:32–33", "right: 12px; bottom: 12px"))
    return page("Numbers 22:31–33 — Then Jehovah Opened the Eyes of Balaam", t, r1 + r2, n)


@P("NUM-C11-P09-Sinned", "I Have Sinned")
def p09(n):
    t, h = rows(None, 280)
    r1 = talk(K11.BALAAM_AWE, h[0], GOLDEN, [("cap", v("22:34", to="angel of Jehovah,")), ("say", after("22:34", "angel of Jehovah,"))], ref="NUM 22:34", size=18)
    r2 = new("radial-gradient(circle at 70% 40%, #FFF8E0 0%, #FFD23F 40%, #E8886A 100%)", W1, h[1], mk.defs("u9b", *K.ALL) + N.angel("u9b", W1 * 0.82, h[1] * 0.96, h[1] / 250),
             cap(v("22:35", to="unto Balaam,"), "left: 12px; top: 12px", size=11) + god(v("22:35", frm="Go with the men;", to="thou shalt speak."), "left: 12px; top: 50px", size=19, maxw=440)
             + cap(v("22:35", frm="So Balaam went"), "left: 12px; bottom: 12px", size=11.5) )
    return page("Numbers 22:34–35 — I Have Sinned", t, r1 + r2, n)


@P("NUM-C11-P10-Balak", "Did I Not Earnestly Send unto Thee?")
def p10(n):
    t, h = rows(260, 240, None)
    r1 = talk(K11.BALAK, h[0], EMBER, [("cap", v("22:36") + " " + v("22:37", to="unto Balaam,")), ("say", after("22:37", "unto Balaam,"))], ref="NUM 22:36–37", size=14)
    r2 = talk(K11.BALAAM, h[1], DUSK, [("cap", v("22:38", to="unto Balak,")), ("say", after("22:38", "unto Balak,"))], ref="NUM 22:38", size=15, flip=True)
    r3 = new("#E8B880", W1, h[2], K11.altars7("u10c", W1, h[2], 11103, "baal"), cap(v("22:39") + " " + v("22:40") + " " + v("22:41"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 22:39–41", "right: 12px; bottom: 12px"))
    return page("Numbers 22:36–41 — Did I Not Earnestly Send unto Thee?", t, r1 + r2 + r3, n)


@P("NUM-C11-P11-SevenAltars", "Build Me Here Seven Altars")
def p11(n):
    t, h = rows(220, None, 260)
    r1 = talk(K11.BALAAM, h[0], DUSK, [("cap", v("23:1", to="unto Balak,")), ("say", after("23:1", "unto Balak,"))], ref="NUM 23:1", size=17)
    r1 = r1[: r1.rfind("</div>")] + mk.stamp(23, "right: 14px; bottom: 12px") + "</div>"
    r2 = new("#E8B880", W1, h[1], K11.altars7("u11b", W1, h[1], 1112, "baal"), cap(v("23:2"), "left: 12px; top: 12px", size=12, maxw=520)
             + cap(v("23:3", to="And Balaam said unto Balak,"), "left: 12px; top: 74px", size=11) + balloon(v("23:3", frm="Stand by", to="I will tell thee."), "left: 18px; top: 110px", 400, size=13, pad="18px 24px")
             + vref("NUM 23:2–3", "right: 12px; bottom: 12px"))
    r3 = new("#2A2458", W1, h[2], K11.bare_height("u11c", W1, h[2], 1113), cap(v("23:3", frm="And he went"), "left: 12px; top: 12px", size=12)
             + cap(v("23:4"), "right: 12px; top: 56px", size=11.5, maxw=330) + cap(v("23:5", to="and said,"), "left: 12px; top: 90px", size=11, maxw=300) + god(after("23:5", "and said,"), "left: 12px; bottom: 12px", size=16, maxw=360) + vref("NUM 23:3–5", "right: 12px; bottom: 12px"))
    return page("Numbers 23:1–5 — Build Me Here Seven Altars", t, r1 + r2 + r3, n)


@P("NUM-C11-P12-Parable1", "How Shall I Curse?")
def p12(n):
    t, h = rows(180, None)
    r1 = new("#E8B880", W1, h[0], K11.altars7("u12a", W1, h[0], 1121, "baal"), cap(v("23:6"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 23:6", "right: 12px; bottom: 12px"))
    r2 = parable(h[1], "23:7", "and said,", after("23:7", "and said,") + " " + sp("23:8-10"), "NUM 23:7–10", size=21, seed=1122)
    return page("Numbers 23:6–10 — How Shall I Curse?", t, r1 + r2, n)


@P("NUM-C11-P13-Pisgah", "Unto the Top of Pisgah")
def p13(n):
    t, h = rows(260, None)
    r1 = cols(talk(K11.BALAK_ANGRY, h[0], RED, [("cap", v("23:11", to="unto Balaam,")), ("say", after("23:11", "unto Balaam,"))], w=W2, ref="NUM 23:11", size=12),
              talk(K11.BALAAM, h[0], DUSK, [("cap", v("23:12", to="and said,")), ("say", after("23:12", "and said,"))], w=W2, ref="NUM 23:12", size=12, flip=True))
    r2 = new("#8FD0E2", W1, h[1], K11.altars7("u13b", W1, h[1], 1132, "pisgah"), cap(v("23:13", to="unto him,"), "left: 12px; top: 12px", size=11)
             + balloon(after("23:13", "unto him,"), "left: 18px; top: 50px", 380, size=13, pad="20px 26px") + cap(v("23:14"), "right: 12px; top: 12px", size=11.5, maxw=280)
             + cap(v("23:15", to="unto Balak,"), "right: 12px; top: 160px", size=11) + balloon(after("23:15", "unto Balak,"), "right: 16px; top: 196px", 280, size=13, pad="16px 20px") + vref("NUM 23:13–15", "left: 12px; bottom: 12px"))
    return page("Numbers 23:11–15 — Unto the Top of Pisgah", t, r1 + r2, n)


@P("NUM-C11-P14-Parable2", "God Is Not a Man, That He Should Lie")
def p14(n):
    t, h = rows(230, None)
    r1 = new("#2A2458", W1, h[0], K11.bare_height("u14a", W1, h[0], 1141), cap(v("23:16", to="and said,"), "left: 12px; top: 12px", size=11, maxw=380) + god(after("23:16", "and said,"), "left: 12px; top: 80px", size=15, maxw=380)
             + cap(v("23:17", to="with him."), "right: 12px; top: 12px", size=11, maxw=230) + cap(v("23:17", frm="And Balak said"), "right: 12px; bottom: 12px", size=11, maxw=230))
    r2 = parable(h[1], "23:18", "and said,", after("23:18", "and said,") + " " + sp("23:19-24"), "NUM 23:16–24", size=17, seed=1142)
    return page("Numbers 23:16–24 — God Is Not a Man, That He Should Lie", t, r1 + r2, n)


@P("NUM-C11-P15-Peor", "Unto the Top of Peor")
def p15(n):
    t, h = rows(250, None)
    r1 = cols(talk(K11.BALAK_ANGRY, h[0], RED, [("cap", v("23:25", to="unto Balaam,")), ("say", after("23:25", "unto Balaam,"))], w=W2, ref="NUM 23:25", size=13),
              talk(K11.BALAAM, h[0], DUSK, [("cap", v("23:26", to="unto Balak,")), ("say", after("23:26", "unto Balak,"))], w=W2, ref="NUM 23:26", size=12, flip=True))
    r2 = new("#E8886A", W1, h[1], K11.altars7("u15b", W1, h[1], 1152, "peor"), cap(v("23:27", to="unto Balaam,"), "left: 12px; top: 12px", size=11)
             + balloon(after("23:27", "unto Balaam,"), "left: 18px; top: 50px", 360, size=13, pad="20px 26px") + cap(v("23:28"), "right: 12px; top: 12px", size=11.5, maxw=280)
             + cap(v("23:29", to="unto Balak,"), "right: 12px; top: 110px", size=11) + balloon(after("23:29", "unto Balak,"), "right: 16px; top: 146px", 280, size=12.5, pad="16px 20px")
             + cap(v("23:30"), "left: 12px; top: 200px", size=11.5, maxw=320) + vref("NUM 23:27–30", "left: 12px; bottom: 12px"))
    return page("Numbers 23:25–30 — Unto the Top of Peor", t, r1 + r2, n)


@P("NUM-C11-P16-Tents", "How Goodly Are Thy Tents, O Jacob")
def p16(n):
    t, h = rows(294, None)
    r1 = cols(new(VISTA, W2, h[0], K11.vista(W2, h[0], 1161, tribes=False), mk.stamp(24, "right: 10px; top: 10px") + cap(v("24:1") + " " + v("24:2"), "left: 8px; bottom: 8px", size=10.5, maxw=320)),
              use(D8[2], over=vref("NUM 24:5", "right: 8px; bottom: 8px")))
    r2 = parable(h[1], "24:3", "and said,", after("24:3", "and said,") + " " + sp("24:4-9"), "NUM 24:1–9", size=16, seed=1162)
    return page("Numbers 24:1–9 — How Goodly Are Thy Tents, O Jacob", t, r1 + r2, n)


@P("NUM-C11-P17-Flee", "Flee Thou to Thy Place")
def p17(n):
    t, h = rows(500, None)
    r1 = talk(K11.BALAK_ANGRY, h[0], RED, [("cap", v("24:10", to="Balak said unto Balaam,")), ("say", after("24:10", "Balak said unto Balaam,") + " " + v("24:11"))], ref="NUM 24:10–11", size=16)
    r2 = talk(K11.BALAAM, h[1], DUSK, [("cap", v("24:12", to="unto Balak,")), ("say", after("24:12", "unto Balak,") + " " + v("24:13") + " " + v("24:14"))], ref="NUM 24:12–14", size=15, flip=True)
    return page("Numbers 24:10–14 — Flee Thou to Thy Place", t, r1 + r2, n)


@P("NUM-C11-P18-Star", "A Star out of Jacob")
def p18(n):
    t, h = rows(None, 294)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), cap(v("24:15", to="and said,"), "left: 12px; top: 12px", size=11)
             + song(after("24:15", "and said,") + " " + v("24:16") + " " + v("24:17") + " " + v("24:18") + " " + v("24:19"), "left: 12px; top: 50px", size=19, maxw=640, color="#7A3BA8") + vref("NUM 24:15–19", "right: 12px; bottom: 12px"))
    r2 = cols(use(D8[3], over=""), new(VISTA, W2, h[1], K11.vista(W2, h[1], 1182, tribes=False), ""))
    return page("Numbers 24:15–19 — A Star out of Jacob", t, r1 + r2, n)


@P("NUM-C11-P19-Amalek", "Amalek Was the First of the Nations")
def p19(n):
    t, h = rows(None, 230)
    r1 = new(DUSK, W1, h[0], X.cosmic(W1, h[0]), cap(v("24:20", to="and said,"), "left: 12px; top: 12px", size=11) + song(after("24:20", "and said,"), "left: 12px; top: 50px", size=18, maxw=600, color="#7A3BA8")
             + cap(v("24:21", to="and said,"), "left: 12px; top: 160px", size=11) + song(after("24:21", "and said,") + " " + v("24:22"), "left: 12px; top: 198px", size=18, maxw=600, color="#7A3BA8")
             + cap(v("24:23", to="and said,"), "left: 12px; top: 330px", size=11) + song(after("24:23", "and said,") + " " + v("24:24"), "left: 12px; top: 368px", size=18, maxw=600, color="#7A3BA8")
             + vref("NUM 24:20–24", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], K11.messengers("u19b", W1, h[1], 1192), cap(v("24:25"), "left: 12px; top: 12px", size=13, maxw=500)
             + vref("NUM 24:25", "left: 12px; bottom: 12px") + end_mark("NEXT · PHINEHAS", "right: 10px; bottom: 10px"))
    return page("Numbers 24:20–25 — Amalek Was the First of the Nations", t, r1 + r2, n)
