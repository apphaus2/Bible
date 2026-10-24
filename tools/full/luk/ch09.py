"""Luke volume, Chapter 9 — Teach Us to Pray (Luke 11). Every verse, word for word from ref/eng-asv.
Praying in a certain place; the disciples' asking; the prayer over the field of wheat at sunrise. The friend at midnight at
the shut door, the loaves given for his importunity; ask, seek, knock; the loaf and the stone. The dumb man speaking, the
multitudes marvelling; by Beelzebub? — the finger of God, beside his face; the strong man's house; the waterless places and
the house swept and garnished (no spirit drawn); the woman in the multitude, Blessed is the womb that bare thee; the sign of
Jonah, the queen of the south, the men of Nineveh; the lamp on the stand and the lamp of the body. The Pharisee's dinner and
the washing; the outside of the cup and the platter; the tithe of mint and rue; the chief seats; the tombs which appear not;
the lawyers' burdens, the tombs of the prophets, the key of knowledge taken away; the scribes and Pharisees lying in wait."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art7 as A, ch08 as _prev
from luk.common import (K, Pages, D, F, Q, N, T, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        CROWD_WOMAN, LAWYER_STERN, PHARISEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C09-00-Title", "Chapter 9 · Teach Us to Pray", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A3A"></rect><g transform="translate(0 300)">{A.before_day("t9", 760, 780, 1101, found=True)}</g>'
    return title(9, "Teach Us to Pray", "Luke 11", svg, "#0B1A3A", v("11:1", frm="Lord, teach us to pray,", to="teach us to pray,"))


SEGS = [D([Q("11:1", "c", "said unto him,", "s")], lambda w, h: A.before_day("bd1", w, h, 1101, found=True), "#0B1A3A", head="Lord, Teach Us to Pray", sky=11, art_h=240),
        D([N("11:2", "said unto them,"), sy("11:3"), sy("11:4")], lambda w, h: A.prayer_field("pf1", w, h, 1102), "#FFD89A"),
        D([N("11:5", "said unto them,"), sy("11:6")], lambda w, h: A.midnight("md1", w, h, 1103), NIGHT, head="Friend, Lend Me Three Loaves"),
        D([sy("11:7"), sy("11:8")], lambda w, h: A.midnight("md2", w, h, 1104, opened=True), NIGHT),
        D([sy("11:9"), sy("11:10")], lambda w, h: A.door_knock("dk1", w, h, 1105), "#2A2050", head="Ask, and It Shall Be Given You"),
        D([sy("11:11"), sy("11:12"), sy("11:13")], lambda w, h: A.loaf_stone("ls1", w, h, 1106), "#8A6A4A"),
        D([cp("11:14")], lambda w, h: A.marvel("mv1", w, h, 1107), "#8FD0E2", head="The Finger of God"),
        D([N("11:15", "some of them said,"), cp("11:16")], lambda w, h: A.counsel("cs1", w, h, 1108), "#2A2A3A"),
        F([N("11:17", "said unto them,"), sy("11:18"), sy("11:19"), sy("11:20")], JESUS_STERN, bg=RED),
        D([sy("11:21"), sy("11:22"), sy("11:23")], lambda w, h: A.strong_house("sh1", w, h, 1109), "#5A4A44"),
        D([sy("11:24")], lambda w, h: A.waterless("wl1", w, h, 1110), "#1A1830"),
        D([sy("11:25"), sy("11:26")], lambda w, h: A.swept("sw1", w, h, 1111), "#B8987A"),
        F([N("11:27", "said unto him,")], CROWD_WOMAN, head="Blessed Are They That Hear"),
        F([N("11:28", "But he said,")], JESUS),
        D([N("11:29", "he began to say,"), sy("11:30")], lambda w, h: A.jonah_sign("jn1", w, h, 1112), "#0F4C68", head="A Greater Than Jonah"),
        D([sy("11:31")], lambda w, h: A.queen_south("qs1", w, h, 1113), "#E8C080"),
        D([sy("11:32")], lambda w, h: A.nineveh("nv1", w, h, 1114), "#8A7A6A"),
        D([sy("11:33")], lambda w, h: A.city_light("cl1", w, h, 1115), NIGHT, head="The Lamp of Thy Body"),
        D([sy("11:34"), sy("11:35"), sy("11:36")], lambda w, h: A.eye_lamp("el1", w, h, 1116), "#05050E"),
        D([cp("11:37"), cp("11:38")], lambda w, h: A.unwashed("uw1", w, h, 1117), "#B8987A", head="Woe unto You Pharisees"),
        D([N("11:39", "said unto him,"), sy("11:40"), sy("11:41")], lambda w, h: A.cup_platter("cp1", w, h, 1118), "#3A2A2A"),
        D([sy("11:42")], lambda w, h: A.gnat_camel("gc1", w, h, 1119), "#C8A878"),
        D([sy("11:43")], lambda w, h: A.moses_seat("ms1", w, h, 1120), "#C8B490"),
        D([sy("11:44")], lambda w, h: A.hidden_tombs("ht1", w, h, 1121), "#5A4A6A"),
        F([N("11:45", "saith unto him,")], LAWYER_STERN, bg=RED, head="Woe unto You Lawyers"),
        D([N("11:46", "And he said,")], lambda w, h: A.burdens("bu1", w, h, 1122), "#C8A878"),
        D([sy("11:47"), sy("11:48")], lambda w, h: A.prophets_tombs("pt1", w, h, 1123), "#8A7A6A"),
        F([sy("11:49"), sy("11:50"), sy("11:51")], JESUS_STERN, bg=RED),
        D([sy("11:52")], lambda w, h: A.key_knowledge("kk1", w, h, 1124), "#8A9AB0"),
        D([cp("11:53"), cp("11:54")], A.footed(lambda w, h: A.counsel("cs2", w, h, 1125), "#3A2A2A"), "#2A2A3A", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C09-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · CONSIDER THE LILIES")))
