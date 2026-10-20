"""Numbers volume, Chapter 8 — Korah (Numbers 15–17). Every verse, word for word from ref/eng-asv.
The offerings and drink-offerings, the first of the dough and sins of error as law cells; the man gathering sticks on
the sabbath (15:36 shown only as the heap of stones without the camp); the fringes; Korah, Dathan and Abiram; the ground
cleaving (16:31–33 as the tents going down, no bodies); the fire upon the two hundred and fifty (their censers only);
the censers beaten into plates; Aaron between the dead and the living; and Aaron's rod that budded."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art8 as B8
from exo.kit import talk, law_pages, set_book
from lev import art3 as L3, art8 as L8
from num import G, art as K, art8 as K8
from num.art7 import fallen
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND, hud
from genesis.ch04 import COLD, EMBER
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED, BLUE
from num import ch07 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = B8.INK
FIRE = "linear-gradient(180deg, #2A0A0A 0%, #8A1E16 60%, #FF8A3D 100%)"
SAY = "And Jehovah spake unto Moses, saying,"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C08-00-Title", "Chapter 8 · Korah", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A0A0A"></rect>' + f'<g transform="translate(0 360)">{K8.company("t8", 760, 720, 801, censers=True)}</g>'
    return chapter_title(8, "第八話", "Korah", "Numbers 15 – 17", svg, FIRE, v("16:3", frm="Ye take too much upon you,", to="every one of them,"), "Numbers · Volume Four")


LAWS = [
    ("WHEN YE ARE COME INTO THE LAND", "15:1-3", K8.pg_offering_fire, SAY, "When Ye Are Come into the Land"),
    ("FOR EACH LAMB", "15:4-5", K8.pg_lamb, "", None),
    ("FOR A RAM", "15:6-7", K8.pg_ram, "", None),
    ("FOR A BULLOCK", "15:8-10", K8.pg_bullock, "", None),
    ("ACCORDING TO THE NUMBER", "15:11-13", K8.pg_each, "", None),
    ("ONE LAW AND ONE ORDINANCE", "15:14-16", K8.pg_one_law, "", None),
    ("THE FIRST OF YOUR DOUGH", "15:17-21", K8.pg_bread, SAY, "The First of Your Dough"),
    ("IF YE SHALL ERR", "15:22-23", K8.pg_err, "", "If Ye Shall Err"),
    ("ALL THE CONGREGATION", "15:24", K8.pg_congregation, "", None),
    ("THEY SHALL BE FORGIVEN", "15:25-26", K8.pg_forgiven, "", None),
    ("IF ONE PERSON SIN UNWITTINGLY", "15:27-29", K8.pg_she_goat, "", None),
    ("WITH A HIGH HAND", "15:30-31", K8.pg_high_hand, "", None),
]
PG.extend(law_pages(LAWS, "NUM-C08-L", PG.next(), "When Ye Are Come into the Land", title_book="Numbers", carry=True))


@P("NUM-C08-P01-Sticks", "A Man Gathering Sticks upon the Sabbath Day")
def p01(n):
    t, h = rows(300, 280, None)
    r1 = new(SKY, W1, h[0], K8.sticks("k1a", W1, h[0], 811), cap(v("15:32") + " " + v("15:33"), "left: 12px; top: 12px", size=12.5, maxw=470) + vref("NUM 15:32–33", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], L8.ward("k1b", W1, h[1], 812), cap(v("15:34"), "left: 12px; top: 12px", size=12.5, maxw=420) + vref("NUM 15:34", "right: 12px; bottom: 12px"))
    r3 = new("#3A2A3E", W1, h[2], L8.heap_without("k1c", W1, h[2], 813), cap(v("15:35", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(after("15:35", "unto Moses,"), "left: 12px; top: 50px", size=16, maxw=460) + cap(v("15:36"), "right: 12px; bottom: 30px", size=11.5, maxw=330) + vref("NUM 15:35–36", "right: 12px; bottom: 8px"))
    return page("Numbers 15:32–36 — A Man Gathering Sticks upon the Sabbath Day", t, r1 + r2 + r3, n)


@P("NUM-C08-P02-Fringes", "A Cord of Blue")
def p02(n):
    t, h = rows(None, 330)
    r1 = night(h[0], cap(v("15:37"), "left: 12px; top: 12px", size=11) + god(sp("15:38-39"), "left: 12px; top: 50px", size=21, maxw=640) + vref("NUM 15:37–39", "right: 12px; bottom: 12px"))
    r2 = new("#E8E2D6", W1, h[1], K8.fringe(W1, h[1]), god(v("15:40") + " " + v("15:41"), "right: 12px; top: 12px", size=17, maxw=330) + vref("NUM 15:40–41", "right: 12px; bottom: 12px"))
    return page("Numbers 15:37–41 — A Cord of Blue", t, r1 + r2, n)


@P("NUM-C08-P03-Korah", "Ye Take Too Much upon You")
def p03(n):
    t, h = rows(330, None)
    r1 = new(SAND, W1, h[0], K8.company("k3a", W1, h[0], 831), mk.stamp(16, "right: 14px; top: 12px") + cap(v("16:1") + " " + v("16:2"), "left: 12px; top: 12px", size=12, maxw=470) + vref("NUM 16:1–2", "right: 12px; bottom: 12px"))
    r2 = talk(K8.KORAH, h[1], RED, [("cap", v("16:3", to="said unto them,")), ("say", after("16:3", "said unto them,"))], ref="NUM 16:3", size=19)
    return page("Numbers 16:1–3 — Ye Take Too Much upon You", t, r1 + r2, n)


@P("NUM-C08-P04-Censers", "Take You Censers")
def p04(n):
    t, h = rows(200, None)
    r1 = new("#3A2A3A", W1, h[0], fallen("k4a", W1, h[0], 841), cap(v("16:4"), "left: 12px; top: 12px", size=12.5, maxw=420) + vref("NUM 16:4", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_STERN, h[1], RED, [("cap", v("16:5", to="saying,")), ("say", after("16:5", "saying,") + " " + v("16:6") + " " + v("16:7"))], ref="NUM 16:5–7", size=18)
    return page("Numbers 16:4–7 — Take You Censers", t, r1 + r2, n)


@P("NUM-C08-P05-Priesthood", "Seek Ye the Priesthood Also?")
def p05(n):
    t, h = rows(None, 280)
    r1 = talk(A.MOSES_STERN, h[0], RED, [("cap", v("16:8", to="unto Korah,")), ("say", after("16:8", "unto Korah,") + " " + v("16:9") + " " + v("16:10"))], ref="NUM 16:8–10", size=17)
    r2 = talk(A.MOSES_STERN, h[1], RED, [("say", v("16:11"))], ref="NUM 16:11", size=19, flip=True)
    return page("Numbers 16:8–11 — Seek Ye the Priesthood Also?", t, r1 + r2, n)


@P("NUM-C08-P06-WeWillNotComeUp", "We Will Not Come Up")
def p06(n):
    t, h = rows(None, 260)
    r1 = talk(K8.DATHAN, h[0], RED, [("cap", v("16:12", to="and they said,")), ("say", after("16:12", "and they said,") + " " + v("16:13") + " " + v("16:14"))], ref="NUM 16:12–14", size=17)
    r2 = talk(A.MOSES_STERN, h[1], RED, [("cap", v("16:15", to="unto Jehovah,")), ("say", after("16:15", "unto Jehovah,"))], ref="NUM 16:15", size=17, flip=True)
    return page("Numbers 16:12–15 — We Will Not Come Up", t, r1 + r2, n)


@P("NUM-C08-P07-Door", "At the Door of the Tent of Meeting")
def p07(n):
    t, h = rows(250, None, 260)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("16:16", to="unto Korah,")), ("say", after("16:16", "unto Korah,") + " " + v("16:17"))], ref="NUM 16:16–17", size=15)
    r2 = new(GOLDEN, W1, h[1], K8.company("k7b", W1, h[1], 872, censers=True), cap(v("16:18") + " " + v("16:19"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 16:18–19", "right: 12px; bottom: 12px"))
    r3 = night(h[2], cap(v("16:20"), "left: 12px; top: 12px", size=11) + god(v("16:21"), "left: 12px; top: 50px", size=21, maxw=600) + vref("NUM 16:20–21", "right: 12px; bottom: 12px"))
    return page("Numbers 16:16–21 — At the Door of the Tent of Meeting", t, r1 + r2 + r3, n)


@P("NUM-C08-P08-GetYouUp", "Get You Up from about the Tabernacle of Korah")
def p08(n):
    t, h = rows(250, 230, None)
    r1 = new("#3A2A3A", W1, h[0], fallen("k8a", W1, h[0], 881), cap(v("16:22", to="and said,"), "left: 12px; top: 12px", size=11)
             + balloon(after("16:22", "and said,"), "right: 16px; top: 12px", 400, size=14, pad="20px 26px") + vref("NUM 16:22", "left: 12px; bottom: 12px"))
    r2 = night(h[1], cap(v("16:23"), "left: 12px; top: 12px", size=11) + god(v("16:24"), "left: 12px; top: 50px", size=21, maxw=600) + vref("NUM 16:23–24", "right: 12px; bottom: 12px"))
    r3 = new("#8FB0C8", W1, h[2], K8.cleft("k8c", W1, h[2], 883, stage=0), cap(v("16:25"), "left: 12px; top: 12px", size=12, maxw=400)
             + cap(v("16:26", to="saying,"), "left: 12px; top: 80px", size=11, maxw=300) + balloon(after("16:26", "saying,"), "left: 18px; top: 130px", 320, size=13, pad="18px 22px") + vref("NUM 16:25–26", "right: 12px; bottom: 12px"))
    return page("Numbers 16:22–26 — Get You Up from about the Tabernacle of Korah", t, r1 + r2 + r3, n)


@P("NUM-C08-P09-NewThing", "If Jehovah Make a New Thing")
def p09(n):
    t, h = rows(300, None)
    r1 = new("#8FB0C8", W1, h[0], K8.cleft("k9a", W1, h[0], 891, stage=0), cap(v("16:27"), "left: 12px; top: 12px", size=12.5, maxw=520) + vref("NUM 16:27", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_STERN, h[1], RED, [("cap", v("16:28", to="And Moses said,")), ("say", after("16:28", "Moses said,") + " " + v("16:29") + " " + v("16:30"))], ref="NUM 16:28–30", size=17)
    return page("Numbers 16:27–30 — If Jehovah Make a New Thing", t, r1 + r2, n)


@P("NUM-C08-P10-Clave", "The Ground Clave Asunder")
def p10(n):
    t, h = rows(None, 300)
    r1 = new("#3A1A1A", W1, h[0], K8.cleft("k10a", W1, h[0], 8101, stage=1), cap(v("16:31") + " " + v("16:32") + " " + v("16:33"), "left: 12px; top: 12px", size=13, maxw=520)
             + mk.sfx("ゴゴゴ", "GOGOGO", "right: 30px; top: 30px", size=52, fill="#FF6A2A", stroke="#0D0D0F", rot=6) + vref("NUM 16:31–33", "right: 12px; bottom: 12px"))
    r2 = cols(new("#3A1A1A", W2, h[1], K8.cleft("k10b", W2, h[1], 8102, stage=2), cap(v("16:34"), "left: 8px; top: 8px", size=11, maxw=320) + vref("NUM 16:34", "right: 8px; bottom: 8px")),
              new(FIRE, W2, h[1], L3.censers_fallen(W2, h[1], 8103), cap(v("16:35"), "left: 8px; top: 8px", size=12, maxw=320) + vref("NUM 16:35", "right: 8px; bottom: 8px")))
    return page("Numbers 16:31–35 — The Ground Clave Asunder", t, r1 + r2, n)


@P("NUM-C08-P11-Plates", "A Sign unto the Children of Israel")
def p11(n):
    t, h = rows(340, None)
    r1 = night(h[0], cap(v("16:36"), "left: 12px; top: 12px", size=11) + god(v("16:37") + " " + v("16:38"), "left: 12px; top: 50px", size=21, maxw=640) + vref("NUM 16:36–38", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K8.plates(W1, h[1]), cap(v("16:39") + " " + v("16:40"), "left: 12px; top: 34px", size=11.5, maxw=330) + vref("NUM 16:39–40", "right: 12px; bottom: 12px"))
    return page("Numbers 16:36–40 — A Sign unto the Children of Israel", t, r1 + r2, n)


@P("NUM-C08-P12-Murmured", "Ye Have Killed the People of Jehovah")
def p12(n):
    t, h = rows(250, None, 230)
    r1 = talk(A.HEBREW_ANGRY, h[0], RED, [("cap", v("16:41", to="saying,")), ("say", after("16:41", "saying,"))], ref="NUM 16:41", size=20)
    r2 = new(GOLDEN, W1, h[1], K8.company("k12b", W1, h[1], 8122), cap(v("16:42") + " " + v("16:43"), "left: 12px; top: 12px", size=12.5, maxw=520) + vref("NUM 16:42–43", "right: 12px; bottom: 12px"))
    r3 = night(h[2], cap(v("16:44"), "left: 12px; top: 12px", size=11) + god(v("16:45", to="in a moment."), "left: 12px; top: 50px", size=20, maxw=600)
               + cap(v("16:45", frm="And they fell"), "right: 12px; bottom: 30px", size=11) + vref("NUM 16:44–45", "right: 12px; bottom: 8px"))
    return page("Numbers 16:41–45 — Ye Have Killed the People of Jehovah", t, r1 + r2 + r3, n)


@P("NUM-C08-P13-Between", "Between the Dead and the Living")
def p13(n):
    t, h = rows(260, None)
    r1 = talk(A.MOSES_AFRAID, h[0], COLD, [("cap", v("16:46", to="unto Aaron,")), ("say", after("16:46", "unto Aaron,"))], ref="NUM 16:46", size=16)
    r2 = new("#1A1020", W1, h[1], K8.between("k13b", W1, h[1], 8132),
             cap(v("16:47"), "left: 12px; top: 12px", size=12, maxw=320) + cap(v("16:48"), "right: 12px; top: 12px", size=14, maxw=300)
             + cap(v("16:49") + " " + v("16:50"), "right: 12px; bottom: 40px", size=11.5, maxw=320) + hud("14,700", "left: 12px; bottom: 30px", size=30) + vref("NUM 16:47–50", "right: 12px; bottom: 12px"))
    return page("Numbers 16:46–50 — Between the Dead and the Living", t, r1 + r2, n)


@P("NUM-C08-P14-Rods", "Twelve Rods")
def p14(n):
    t, h = rows(400, None)
    r1 = night(h[0], mk.stamp(17, "right: 14px; top: 12px") + cap(v("17:1"), "left: 12px; top: 12px", size=11) + god(sp("17:2-5"), "left: 12px; top: 50px", size=19, maxw=640) + vref("NUM 17:1–5", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K8.rods(W1, h[1]), cap(v("17:6") + " " + v("17:7"), "right: 12px; top: 34px", size=11.5, maxw=300) + vref("NUM 17:6–7", "right: 12px; bottom: 12px"))
    return page("Numbers 17:1–7 — Twelve Rods", t, r1 + r2, n)


@P("NUM-C08-P15-Budded", "The Rod of Aaron Was Budded")
def p15(n):
    t, h = rows(None, 230, 270)
    r1 = new(INK, W1, h[0], K8.rods(W1, h[0], budded=True), cap(v("17:8") + " " + v("17:9"), "right: 12px; top: 34px", size=12.5, maxw=330) + vref("NUM 17:8–9", "right: 12px; bottom: 12px"))
    r2 = night(h[1], cap(v("17:10", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("17:10", "unto Moses,"), "left: 12px; top: 50px", size=17, maxw=640)
               + cap(v("17:11"), "right: 12px; bottom: 30px", size=11) + vref("NUM 17:10–11", "right: 12px; bottom: 8px"))
    r3 = talk(A.HEBREW_FEAR if hasattr(A, "HEBREW_FEAR") else A.SLAVE, h[2], COLD, [("cap", v("17:12", to="saying,")), ("say", after("17:12", "saying,") + " " + v("17:13"))], ref="NUM 17:12–13", size=16)
    r3 = r3[: r3.rfind("</div>")] + end_mark("NEXT · THE WATER FOR IMPURITY", "right: 10px; bottom: 10px") + "</div>"
    return page("Numbers 17:8–13 — The Rod of Aaron Was Budded", t, r1 + r2 + r3, n)
