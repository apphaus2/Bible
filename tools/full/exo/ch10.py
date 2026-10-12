"""Exodus volume, Chapter 10 — The Golden Calf (Exodus 32–34). Every verse, word for word from ref/asv.
The digest's Exodus Book Five drawings are lifted for the calf, the broken tables, the cleft of the rock and the shining
face. The slaying of 32:27–28 is caption-only over an empty gate; 34:12–26 is two pages of law cells."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art5 as F5, art6 as S6, art7 as L7, art10 as K
from exo.kit import talk, law
from exo.ch02 import night
from exo.ch06 import MOUNT, pic
from exo.ch07 import laws
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from mk import defs, face

v, sp = G.v, G.span
MG, PL, BR, SI, GL, TN = [panels("digest/exodus/book-05/" + n + ".dc.html") for n in ["EX5-P03-MakeUsGods", "EX5-P04-Play", "EX5-P05-Broken", "EX5-P06-Side", "EX5-P07-Glory", "EX5-P08-Tabernacle"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
SHINE = "linear-gradient(180deg, #FFF4C2 0%, #FFD23F 60%, #FF8A3D 100%)"
START = 156                                  # chapter 9 ends on page 155
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("EXO-C10-00-Title", "Chapter 10 · The Golden Calf")
def title():
    a = MG[3]
    return chapter_title(10, "第十話", "The Golden Calf", "Exodus 32 – 34", f'<g transform="translate(-180 120) scale(1.6)">{a.svg}</g>', a.bg,
                         v("32:4", frm="These are thy gods,"), "Exodus · Volume Two")


@P("EXO-C10-P01-MakeUsGods", "156 · Up, Make Us Gods")
def p01():
    t, h = rows(330, 330, None)
    r1 = use(MG[0], over=cap(v("32:1", to="said unto him,"), "left: 12px; top: 12px", size=11, maxw=420) + balloon(v("32:1", frm="Up, make"), "right: 14px; top: 70px", 330, size=13, pad="24px 28px")
             + mk.stamp(32, "left: 14px; bottom: 14px") + vref("EX 32:1", "right: 12px; bottom: 12px"))
    r2 = cols(talk(K.AARON_PLEAD, h[1], EMBER, [("cap", v("32:2", to="unto them,")), ("say", v("32:2", frm="Break off"))], w=W2, ref="EX 32:2", size=12.5),
              new(DUSK, W2, h[1], defs("x101b", *ALL) + K.rings("x101b", W2, h[1], 1012), cap(v("32:3"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 32:3", "right: 8px; bottom: 8px")))
    r3 = use(MG[2], over=cap(v("32:4", to="a molten calf:"), "left: 12px; top: 12px", size=11, maxw=380) + vref("EX 32:4", "right: 12px; bottom: 12px"))
    return page("Exodus 32:1–4 — Up, Make Us Gods", t, r1 + r2 + r3, START + 0)


@P("EXO-C10-P02-Feast", "157 · These Are Thy Gods, O Israel")
def p02():
    t, h = rows(330, 220, None)
    r1 = use(MG[3], over=cap(v("32:4", frm="and they said,", to="they said,"), "left: 12px; top: 12px", size=11) + balloon(v("32:4", frm="These are"), "left: 20px; top: 50px", 330, size=14, pad="20px 26px")
             + sfx("キラッ", "KIRA!", "right: 30px; top: 30px", size=46, fill="#FFD23F", rot=-6) + vref("EX 32:4", "right: 12px; bottom: 12px"))
    r2 = talk(K.AARON_PLEAD, h[1], EMBER, [("cap", v("32:5", to="and said,")), ("say", v("32:5", frm="To-morrow"))], ref="EX 32:5", size=15)
    r3 = use(PL[0], over=cap(v("32:6"), "left: 12px; top: 12px", size=11.5, maxw=440) + sfx("ドンドン", "DON DON", "right: 20px; top: 20px", size=44, fill="#D7261E", rot=-6) + vref("EX 32:6", "right: 12px; bottom: 12px"))
    return page("Exodus 32:4–6 — These Are Thy Gods, O Israel", t, r1 + r2 + r3, START + 1)


@P("EXO-C10-P03-Stiffnecked", "158 · A Stiffnecked People")
def p03():
    t, h = rows(400, None)
    r1 = use(PL[1], over=cap(v("32:7", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("32:7", frm="Go, get") + " " + v("32:8"), "left: 12px; top: 48px", size=17, maxw=560) + vref("EX 32:7–8", "right: 12px; bottom: 12px"))
    r2 = new(MOUNT, W1, h[1], E4.sinai(W1 * 0.74, h[1], W1 * 0.6, h[1] * 0.92, 1032), over=cap(v("32:9", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("32:9", frm="I have seen") + " " + v("32:10"), "left: 12px; top: 48px", size=19, maxw=520) + vref("EX 32:9–10", "right: 12px; bottom: 12px"))
    return page("Exodus 32:7–10 — A Stiffnecked People", t, r1 + r2, START + 2)


@P("EXO-C10-P04-Remember", "159 · Remember Abraham, Isaac, and Israel")
def p04():
    t, h = rows(None, 200)
    r1 = talk(A.MOSES_OLD_PLEA, h[0], BLUE, [("cap", v("32:11", to="and said,")), ("say", v("32:11", frm="Jehovah, why") + " " + v("32:12")), ("say", v("32:13"))], ref="EX 32:11–13", size=14)
    r2 = new(NIGHT, W1, h[1], X.cosmic(W1, h[1]) + mk.stars(120, W1, h[1], 1042), cap(v("32:14"), "left: 50%; top: 50%; transform: translate(-50%, -50%)", size=13, maxw=520) + vref("EX 32:14", "right: 12px; bottom: 12px"))
    return page("Exodus 32:11–14 — Remember Abraham, Isaac, and Israel", t, r1 + r2, START + 3)


@P("EXO-C10-P05-Noise", "160 · The Noise of Them That Sing")
def p05():
    t, h = rows(290, 330, None)
    r1 = use(BR[0], over=cap(v("32:15") + " " + v("32:16"), "left: 12px; top: 12px", size=11, maxw=430) + vref("EX 32:15–16", "right: 12px; bottom: 12px"))
    r2 = cols(talk(F5.JOSHUA, h[1], RED, [("cap", v("32:17", to="unto Moses,")), ("say", v("32:17", frm="There is"))], w=W2, ref="EX 32:17", size=13),
              talk(A.MOSES_STERN, h[1], RED, [("cap", v("32:18", to="And he said,")), ("say", v("32:18", frm="It is not"))], w=W2, flip=True, ref="EX 32:18", size=12))
    r3 = use(PL[0], over=sfx("ワーッ", "WAAA", "left: 30px; top: 30px", size=44, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("EX 32:18", "right: 12px; bottom: 12px"))
    return page("Exodus 32:15–18 — The Noise of Them That Sing", t, r1 + r2 + r3, START + 4)


@P("EXO-C10-P06-Broken", "161 · He Brake Them beneath the Mount")
def p06():
    t, h = rows(None, 300)
    r1 = use(BR[3], over=cap(v("32:19"), "left: 12px; top: 12px", size=12, maxw=440) + sfx("ガシャーン", "GASHAAN", "right: 20px; bottom: 60px", size=54, fill="#F3EFE6", stroke="#0D0D0F", rot=-8) + vref("EX 32:19", "right: 12px; bottom: 12px"))
    r2 = use(SI[0], over=cap(v("32:20"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("EX 32:20", "right: 12px; bottom: 12px"))
    return page("Exodus 32:19–20 — He Brake Them beneath the Mount", t, r1 + r2, START + 5)


@P("EXO-C10-P07-ThisCalf", "162 · There Came Out This Calf")
def p07():
    t, h = rows(230, None)
    r1 = talk(A.MOSES_STERN, h[0], RED, [("cap", v("32:21", to="unto Aaron,")), ("say", v("32:21", frm="What did"))], ref="EX 32:21", size=16)
    r2 = talk(K.AARON_FEAR, h[1], EMBER, [("cap", v("32:22", to="And Aaron said,")), ("say", v("32:22", frm="Let not") + " " + v("32:23") + " " + v("32:24"))], ref="EX 32:22–24", size=15)
    return page("Exodus 32:21–24 — There Came Out This Calf", t, r1 + r2, START + 6)


@P("EXO-C10-P08-Side", "163 · Who Is on Jehovah's Side?")
def p08():
    t, h = rows(290, 300, None)
    r1 = use(SI[1], over=cap(v("32:25") + " " + v("32:26", to="and said,"), "left: 12px; top: 12px", size=11, maxw=380) + balloon(v("32:26", frm="Whoso is", to="unto me."), "right: 14px; top: 110px", 270, size=14, pad="20px 24px") + vref("EX 32:25–26", "left: 12px; bottom: 12px"))
    r2 = use(SI[2], over=cap(v("32:26", frm="And all the sons"), "left: 12px; top: 12px", size=11) + cap(v("32:27", to="And he said unto them,"), "left: 12px; top: 50px", size=11)
             + balloon(v("32:27", frm="Thus saith"), "right: 14px; top: 14px", 360, size=12.5, pad="24px 30px") + vref("EX 32:26–27", "left: 12px; bottom: 12px"))
    r3 = new("#3A0A10", W1, h[2], K.gate(W1, h[2], 1083), cap(v("32:28"), "left: 12px; top: 12px", size=12, maxw=420) + hud("3,000", "right: 14px; top: 14px", size=26)
             + cap(v("32:29", to="And Moses said,"), "left: 12px; bottom: 80px", size=11) + balloon(v("32:29", frm="Consecrate"), "left: 20px; bottom: 14px", 420, size=12.5, pad="14px 22px") + vref("EX 32:28–29", "right: 12px; bottom: 12px"))
    return page("Exodus 32:25–29 — Who Is on Jehovah's Side?", t, r1 + r2 + r3, START + 7)


@P("EXO-C10-P09-BlotMe", "164 · Blot Me, I Pray Thee, out of Thy Book")
def p09():
    t, h = rows(230, 280, None)
    r1 = talk(A.MOSES_STERN, h[0], GOLDEN, [("cap", v("32:30", to="unto the people,")), ("say", v("32:30", frm="Ye have"))], ref="EX 32:30", size=14)
    r2 = talk(A.MOSES_OLD_PLEA, h[1], BLUE, [("cap", v("32:31", to="and said,")), ("say", v("32:31", frm="Oh, this") + " " + v("32:32"))], ref="EX 32:31–32", size=15)
    r3 = new(MOUNT, W1, h[2], E4.sinai(W1 * 0.76, h[2], W1 * 0.5, h[2] * 0.9, 1093, fire=False), cap(v("32:33", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("32:33", frm="Whosoever") + " " + v("32:34"), "left: 12px; top: 48px", size=15, maxw=460) + cap(v("32:35"), "left: 12px; bottom: 14px", size=11, maxw=420) + vref("EX 32:33–35", "right: 12px; bottom: 12px"))
    return page("Exodus 32:30–35 — Blot Me, I Pray Thee, out of Thy Book", t, r1 + r2 + r3, START + 8)


@P("EXO-C10-P10-Ornaments", "165 · No Man Did Put On Him His Ornaments")
def p10():
    t, h = rows(300, 200, None)
    r1 = new(SAND, W1, h[0], defs("x1010a", *ALL) + L7.angel_before("x1010a", W1, h[0], 1101), cap(v("33:1", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("33:1", frm="Depart,") + " " + v("33:2") + " " + v("33:3"), "left: 12px; top: 48px", size=14, maxw=560) + mk.stamp(33, "right: 14px; bottom: 12px") + vref("EX 33:1–3", "left: 12px; bottom: 12px"))
    r2 = new("#3A3450", W1, h[1], defs("x1010b", *ALL) + K.mourning("x1010b", W1, h[1], 1102), cap(v("33:4"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("EX 33:4", "right: 12px; bottom: 12px"))
    r3 = new(MOUNT, W1, h[2], E4.sinai(W1 * 0.8, h[2], W1 * 0.4, h[2] * 0.9, 1103, fire=False), cap(v("33:5", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("33:5", frm="Say unto"), "left: 12px; top: 48px", size=15, maxw=460) + cap(v("33:6"), "left: 12px; bottom: 14px", size=11, maxw=420) + vref("EX 33:5–6", "right: 12px; bottom: 12px"))
    return page("Exodus 33:1–6 — No Man Did Put On Him His Ornaments", t, r1 + r2 + r3, START + 9)


@P("EXO-C10-P11-TentOfMeeting", "166 · Face to Face, As a Man Speaketh unto His Friend")
def p11():
    t, h = rows(320, 300, None)
    r1 = new(SKY, W1, h[0], defs("x1011a", *ALL) + K.tent_without("x1011a", W1, h[0], 1111), cap(v("33:7"), "left: 12px; top: 12px", size=11, maxw=440) + cap(v("33:8"), "right: 12px; bottom: 14px", size=10.5, maxw=300) + vref("EX 33:7–8", "left: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], defs("x1011b", *ALL) + K.tent_without("x1011b", W1, h[1], 1112, cloud=True, worship=True), cap(v("33:9") + " " + v("33:10"), "left: 12px; top: 12px", size=11, maxw=420) + vref("EX 33:9–10", "right: 12px; bottom: 12px"))
    r3 = cols(talk(A.MOSES_CALM, h[2], GOLDEN, [("cap", v("33:11", to="unto his friend."))], w=W2, ref="EX 33:11"),
              talk(F5.JOSHUA, h[2], GOLDEN, [("cap", v("33:11", frm="And he turned"))], w=W2, flip=True))
    return page("Exodus 33:7–11 — Face to Face, As a Man Speaketh unto His Friend", t, r1 + r2 + r3, START + 10)


@P("EXO-C10-P12-Presence", "167 · My Presence Shall Go with Thee")
def p12():
    t, h = rows(330, 170, None)
    r1 = talk(A.MOSES_OLD_PLEA, h[0], BLUE, [("cap", v("33:12", to="unto Jehovah,")), ("say", v("33:12", frm="See, thou") + " " + v("33:13"))], ref="EX 33:12–13", size=14)
    r2 = night(W1, h[1], cap(v("33:14", to="And he said,"), "left: 12px; top: 12px", size=11) + god(v("33:14", frm="My presence"), "left: 12px; top: 48px", size=22, maxw=600) + vref("EX 33:14", "right: 12px; bottom: 12px"))
    r3 = cols(talk(A.MOSES_OLD_PLEA, h[2], BLUE, [("cap", v("33:15", to="unto him,")), ("say", v("33:15", frm="If thy") + " " + v("33:16"))], w=W2, ref="EX 33:15–16", size=11.5),
              night(W2, h[2], cap(v("33:17", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + god(v("33:17", frm="I will do"), "left: 8px; top: 44px", size=15, maxw=320) + vref("EX 33:17", "right: 8px; bottom: 8px")))
    return page("Exodus 33:12–17 — My Presence Shall Go with Thee", t, r1 + r2 + r3, START + 11)


@P("EXO-C10-P13-Glory", "168 · Show Me, I Pray Thee, Thy Glory")
def p13():
    t, h = rows(260, 380, None)
    r1 = use(GL[0], over=cap(v("33:18", to="And he said,"), "left: 330px; top: 12px", size=11) + balloon(v("33:18", frm="Show me"), "left: 330px; top: 60px", 260, size=16, pad="20px 24px") + vref("EX 33:18", "left: 12px; bottom: 12px"))
    r2 = use(GL[1], over=cap(v("33:19", to="And he said,"), "left: 12px; top: 12px", size=11) + god(v("33:19", frm="I will make"), "left: 12px; top: 48px", size=17, maxw=500)
             + cap(v("33:20", to="And he said,"), "right: 12px; bottom: 90px", size=11) + god(v("33:20", frm="Thou canst"), "right: 12px; bottom: 14px", size=17, maxw=420) + vref("EX 33:19–20", "left: 12px; bottom: 12px"))
    r3 = use(GL[2], over=cap(v("33:21", to="And Jehovah said,"), "right: 12px; top: 12px", size=11) + god(v("33:21", frm="Behold,") + " " + v("33:22") + " " + v("33:23"), "right: 12px; top: 48px", size=14, maxw=430) + vref("EX 33:21–23", "left: 12px; bottom: 12px"))
    return page("Exodus 33:18–23 — Show Me, I Pray Thee, Thy Glory", t, r1 + r2 + r3, START + 12)


@P("EXO-C10-P14-Hew", "169 · Hew Thee Two Tables of Stone")
def p14():
    t, h = rows(300, 280, None)
    r1 = new(SKY, W1, h[0], defs("x1014a", *ALL) + K.hewing("x1014a", W1, h[0], 1141), cap(v("34:1", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("34:1", frm="Hew thee") + " " + v("34:2") + " " + v("34:3"), "left: 12px; top: 48px", size=14, maxw=640) + mk.stamp(34, "right: 14px; bottom: 12px") + vref("EX 34:1–3", "left: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("x1014b", *ALL) + K.climbing("x1014b", W1, h[1], 1142), cap(v("34:4"), "right: 12px; top: 12px", size=11, maxw=330) + vref("EX 34:4", "left: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], K.cloud_mount(W1, h[2], 1143), cap(v("34:5") + " " + v("34:6", to="and proclaimed,"), "left: 12px; top: 12px", size=11, maxw=500)
             + god(v("34:6", frm="Jehovah, Jehovah,") + " " + v("34:7"), "left: 12px; top: 76px", size=16, maxw=660) + vref("EX 34:5–7", "right: 12px; bottom: 12px"))
    return page("Exodus 34:1–7 — Hew Thee Two Tables of Stone", t, r1 + r2 + r3, START + 13)


@P("EXO-C10-P15-Covenant", "170 · Behold, I Make a Covenant")
def p15():
    t, h = rows(250, 230, None)
    r1 = new(NIGHT, W1, h[0], defs("x1015a", *ALL) + K.bowed("x1015a", W1, h[0], 1151), cap(v("34:8"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("EX 34:8", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_OLD_PLEA, h[1], BLUE, [("cap", v("34:9", to="And he said,")), ("say", v("34:9", frm="If now"))], ref="EX 34:9", size=14)
    r3 = new("#0B1A2E", W1, h[2], A.peoples_map(W1, h[2], 1153), cap(v("34:10", to="And he said,"), "right: 12px; top: 12px", size=11)
             + god(v("34:10", frm="Behold, I make") + " " + v("34:11"), "right: 12px; top: 48px", size=13.5, maxw=330) + vref("EX 34:10–11", "left: 12px; top: 12px"))
    return page("Exodus 34:8–11 — Behold, I Make a Covenant", t, r1 + r2 + r3, START + 14)


@P("EXO-C10-P16-Jealous", "171 · Whose Name Is Jealous")
def p16():
    return laws("Exodus 34:12–20 — Whose Name Is Jealous", START + 15,
                [("NO COVENANT WITH THEM", "34:12-13", L7.pg_idols), ("A JEALOUS GOD", "34:14", L7.pg_idols), ("THEIR DAUGHTERS", "34:15-16", L7.pg_dowry),
                 ("NO MOLTEN GODS", "34:17", L7.pg_idols), ("THE FEAST OF UNLEAVENED BREAD", "34:18", L7.pg_three), ("THE FIRSTLINGS", "34:19-20", L7.pg_firstfruits)])

@P("EXO-C10-P17-Feasts", "172 · Three Times in the Year")
def p17():
    return laws("Exodus 34:21–26 — Three Times in the Year", START + 16,
                [("IN PLOWING TIME AND IN HARVEST", "34:21", L7.pg_rest), ("WEEKS AND INGATHERING", "34:22", L7.pg_three), ("ALL THY MALES", "34:23", L7.pg_crowd),
                 ("NONE SHALL DESIRE THY LAND", "34:24", L7.pg_sojourner), ("THE SACRIFICE OF THE PASSOVER", "34:25", lambda p: L7.pg_three(p)), ("THE FIRST OF THE FIRST-FRUITS", "34:26", L7.pg_kid)])


@P("EXO-C10-P18-Shone", "173 · The Skin of His Face Shone")
def p18():
    t, h = rows(260, 300, None)
    r1 = new(NIGHT, W1, h[0], F5.book(W1, h[0], 1181), cap(v("34:27", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("34:27", frm="Write thou"), "left: 12px; top: 48px", size=15, maxw=420)
             + cap(v("34:28"), "right: 12px; bottom: 14px", size=11, maxw=380) + hud("40", "right: 14px; top: 14px", size=28) + vref("EX 34:27–28", "left: 12px; bottom: 12px"))
    r2 = use(TN[0], over=cap(v("34:29"), "left: 12px; top: 12px", size=11, maxw=440) + vref("EX 34:29", "right: 12px; bottom: 12px"))
    r3 = cols(use(TN[1], over=vref("EX 34:29", "left: 8px; bottom: 8px")),
              use(TN[2], over=cap(v("34:30"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("EX 34:30", "right: 8px; top: 8px")))
    return page("Exodus 34:27–30 — The Skin of His Face Shone", t, r1 + r2 + r3, START + 17)


@P("EXO-C10-P19-Veil", "174 · He Put a Veil on His Face")
def p19():
    t, h = rows(300, None)
    r1 = new(SAND, W1, h[0], defs("x1019a", *ALL) + K.shining("x1019a", W1, h[0], 1191), cap(v("34:31") + " " + v("34:32"), "left: 12px; top: 12px", size=11, maxw=440) + vref("EX 34:31–32", "right: 12px; bottom: 12px"))
    r2 = cols(new(SHINE, W2, h[1], fc(K.MOSES_VEIL, h[1]), cap(v("34:33"), "right: 8px; top: 8px", size=11, maxw=200) + vref("EX 34:33", "left: 8px; bottom: 8px")),
              new(SHINE, W2, h[1], fc(K.MOSES_SHINE, h[1], flip=True) + V.rays(W2 * 0.3, h[1] * 0.4, 24, 30, W2, color="#FFFFFF", op=0.4), cap(v("34:34") + " " + v("34:35"), "left: 8px; top: 8px", size=10.5, maxw=220)
                  + end_mark("NEXT · THE GLORY", "left: 8px; bottom: 8px") + vref("EX 34:34–35", "right: 8px; bottom: 8px")))
    return page("Exodus 34:31–35 — He Put a Veil on His Face", t, r1 + r2, START + 18)
