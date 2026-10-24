"""Luke volume, Chapter 6 — The Sower (Luke 8). Every verse, word for word from ref/eng-asv.
The twelve and the women who ministered of their substance on the road — Mary Magdalene, Joanna, Susanna. The sower and
the four grounds, each ground again close up as he expounds it; the lamp on its stand; his mother and brethren at the door.
The storm of wind on the lake, Jesus asleep, Master, master, we perish; the calm. The country of the Gerasenes, as Mark
tells it: the man is never drawn among the tombs; the cry, Legion, and the spirits' entreaties stand over the empty tombs,
the broken chains and the empty sea, never beside Jesus' face; the swine down the steep at a distance, the drowning in words
over the sea; the man sitting clothed and in his right mind at Jesus' feet; return to thy house. Jaïrus at his feet; the
woman in the press touching the border of his garment; Who is it that touched me?; Daughter, thy faith hath made thee
whole; Thy daughter is dead; the weeping; Maiden, arise."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art5 as A, ch05 as _prev
from luk.common import (K, Pages, D, F, Q, N, T, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, CROWD_MAN, JAIRUS_GLAD, RULER, ISSUE, ISSUE_HEALED, GERASENE_PLEAD)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C06-00-Title", "Chapter 6 · The Sower", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.sower("t6", 760, 780, 801)}</g>'
    return title(6, "The Sower", "Luke 8", svg, "#3A5A2A", v("8:5", frm="The sower went forth", to="his seed:"))


SEGS = [D([cp("8:1"), cp("8:2"), cp("8:3")], lambda w, h: A.women_follow("wf1", w, h, 801), "#8FD0E2", head="Certain Women Which Ministered", sky=8, art_h=220),
        D([cp("8:4"), sy("8:5")], lambda w, h: A.sower("sw1", w, h, 802), "#8FD0E2", head="The Sower Went Forth to Sow"),
        D([sy("8:6"), sy("8:7"), Q("8:8", "s", "a hundredfold.", "c", "he cried,", "s")], lambda w, h: A.sower("sw2", w, h, 803, ground_="all"), "#8FD0E2"),
        D([cp("8:9"), N("8:10", "And he said,")], lambda w, h: A.eyes_ears("ee1", w, h, 804), "#3A3A6A"),
        D([sy("8:11"), sy("8:12")], lambda w, h: A.ground_close("gw1", w, h, 805, "way"), "#C8B07A"),
        D([sy("8:13")], lambda w, h: A.ground_close("gr1", w, h, 806, "rocky"), "#C8B07A"),
        D([sy("8:14")], lambda w, h: A.ground_close("gt1", w, h, 807, "thorns"), "#8A9A5A"),
        D([sy("8:15")], lambda w, h: A.ground_close("gg1", w, h, 808, "good"), "#D8B860"),
        D([sy("8:16"), sy("8:17"), sy("8:18")], lambda w, h: A.city_light("cl1", w, h, 809), NIGHT, head="A Lamp on a Stand"),
        D([cp("8:19"), N("8:20", "it was told him,")], lambda w, h: A.kindred("kd1", w, h, 810), "#B8987A", head="My Mother and My Brethren"),
        F([N("8:21", "answered and said unto them,")]),
        D([Q("8:22", "c", "said unto them,", "s", "the other side of the lake:", "c"), cp("8:23")], lambda w, h: A.tempest("tp1", w, h, 811), "#14141E",
          head="Where Is Your Faith?", art_h=240),
        D([Q("8:24", "c", "awoke him, saying,", "s", "we perish.", "c")], lambda w, h: A.tempest("tp2", w, h, 812, awake=True), "#14141E", art_h=240),
        D([Q("8:25", "c", "said unto them,", "s", "Where is your faith?", "c", "one to another,", "s")], lambda w, h: A.tempest("tp3", w, h, 826, calm=True), "#5A8AC8"),
        D([cp("8:26"), cp("8:27")], lambda w, h: A.empty_tombs("et1", w, h, 813), NIGHT, head="What Is Thy Name?", art_h=220),
        D([N("8:28", "with a loud voice said,")], lambda w, h: A.tombs("tb1", w, h, 814, men=False), "#6A6A8A"),
        D([cp("8:29")], lambda w, h: A.empty_tombs("et2", w, h, 815, night=False), "#6A6A8A"),
        F((q30 := Q("8:30", "c", "asked him,", "s", "What is thy name?", "c", "And he said,", "s", "Legion;", "c"))[:2], JESUS_STERN, bg=RED),
        D([q30[2:], cp("8:31"), cp("8:32")], lambda w, h: A.tombs("tb2", w, h, 816, men=False, jesus_=False, swine=True), "#6A6A8A", ref="LUKE 8:30–32"),
        D([cp("8:33", to="into the swine:")], lambda w, h: A.swine_steep("sw3", w, h, 817), "#6A6A8A"),
        D([cp("8:33", frm="and the herd")], lambda w, h: A.empty_sea("es1", w, h, 818), "#5A5A7A"),
        D([cp("8:34")], lambda w, h: A.city_gate("cg1", w, h, 819, crowd_n=7), "#8FD0E2", head="Clothed, and in His Right Mind"),
        D([cp("8:35"), cp("8:36"), cp("8:37")], lambda w, h: A.gerasene_sitting("gs1", w, h, 820), "#8FD0E2", art_h=220),
        F([N("8:38", "sent him away, saying,"), Q("8:39", "s", "done for thee.", "c")], JESUS),
        D([cp("8:40"), cp("8:41"), cp("8:42")], lambda w, h: A.jairus_feet("jf1", w, h, 821), "#8FD0E2", head="Who Is It That Touched Me?"),
        D([cp("8:43"), cp("8:44")], lambda w, h: A.border("bd1", w, h, 822), "#8FD0E2"),
        F((q45 := Q("8:45", "c", "And Jesus said,", "s", "touched me?", "c", "with him,", "s"))[:2], JESUS),
        F(q45[2:], PETER, bg=COLD, ref="LUKE 8:45"),
        F([N("8:46", "Jesus said,")], JESUS),
        D([cp("8:47")], lambda w, h: A.border("bd2", w, h, 823), "#8FD0E2"),
        F([N("8:48", "said unto her,")], JESUS),
        F([N("8:49", "house, saying,")], CROWD_MAN, bg=COLD, head="Maiden, Arise"),
        F([N("8:50", "answered him,")], JESUS),
        D([cp("8:51"), N("8:52", "but he said,"), cp("8:53")], lambda w, h: A.ruler_house("rh1", w, h, 824), "#8FD0E2"),
        D([N("8:54", "called, saying,"), cp("8:55"), cp("8:56")], A.footed(lambda w, h: A.talitha("tl1", w, h, 825), "#8A6A4A"), "#C8A878", art_h=300)]
PG.extend(K.pack(SEGS, "LUK-C06-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THOU ART THE CHRIST")))
