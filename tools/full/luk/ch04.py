"""Luke volume, Chapter 4 — Launch Out into the Deep (Luke 5–6). Every verse, word for word from ref/eng-asv.
The lake of Gennesaret: the two boats drawn up and the nets washed; teaching the multitudes out of Simon's boat; put out
into the deep — Master, we toiled all night; the nets breaking and both boats filled so that they began to sink; Simon at
Jesus' knees among the fish — Depart from me; Fear not, from henceforth thou shalt catch men; the boats brought to land and
all left. The leper on his face, made clean; the deserts and prayer. The house where the Pharisees and doctors sat: the
palsied man let down through the tiles, Arise, the couch carried home. Levi at the place of toll and his great feast;
the bridegroom; the new patch and the new wine. The grainfields on the sabbath; the withered right hand restored, the
scribes filled with madness. All night on the mountain in prayer; the twelve named apostles in Luke's order. The level
place and the great multitude touching him; the blessings and the woes beside his face; love your enemies; the sun and the
rain on the unthankful; good measure running over; the blind leading the blind; the mote and the beam; the good tree and
the corrupt; the house on the rock and the house on the earth without a foundation."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art3 as A, ch03 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, PETER,
                        PETER_GRIEF, SCRIBE_STERN, PHARISEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C04-00-Title", "Chapter 4 · Launch Out into the Deep", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5A8AC8"></rect><g transform="translate(0 300)">{A.the_deep("t4", 760, 780, 501, stage="full")}</g>'
    return title(4, "Launch Out into the Deep", "Luke 5 – 6", svg, "#0F4C68", v("5:10", frm="Fear not;"))


SEGS = [D([cp("5:1"), cp("5:2")], lambda w, h: A.washing_nets("wn1", w, h, 501), "#8FD0E2", head="Put Out into the Deep", sky=5),
        D([cp("5:3")], lambda w, h: A.boat_preach("bp1", w, h, 502), "#8FD0E2"),
        D([N("5:4", "said unto Simon,")], lambda w, h: A.the_deep("dp1", w, h, 503), "#5A8AC8", art_h=240),
        F([N("5:5", "answered and said,")], PETER),
        D([cp("5:6"), cp("5:7")], lambda w, h: A.the_deep("dp2", w, h, 504, stage="full"), "#5A8AC8", art_h=260),
        F([Q("5:8", "c", "saying,", "s")], PETER_GRIEF, bg=COLD),
        D([cp("5:9"), Q("5:10", "c", "said unto Simon,", "s")], lambda w, h: A.the_deep("dp3", w, h, 505, stage="knees"), "#5A8AC8", head="Thou Shalt Catch Men", art_h=240),
        D([cp("5:11")], lambda w, h: A.left_all("la1", w, h, 506), "#8FD0E2", art_h=240),
        D([Q("5:12", "c", "saying,", "s")], lambda w, h: A.leper("lp1", w, h, 507), "#8FD0E2", head="Be Thou Made Clean"),
        F([Q("5:13", "c", "saying,", "s", "be thou made clean.", "c"), Q("5:14", "c", "tell no man:", "s")], JESUS),
        D([cp("5:15"), cp("5:16")], lambda w, h: A.before_day("bd1", w, h, 508), "#0B1A3A"),
        D([cp("5:17")], lambda w, h: A.door_crowd("dc1", w, h, 509), "#8FD0E2", head="Thy Sins Are Forgiven Thee"),
        D([cp("5:18"), cp("5:19")], lambda w, h: A.roof_opened("ro1", w, h, 510), "#8FD0E2", art_h=240),
        D([N("5:20", "he said,")], lambda w, h: A.let_down("ld1", w, h, 511), "#B89A70", art_h=240),
        F([N("5:21", "to reason, saying,")], SCRIBE_STERN, bg=RED),
        F([N("5:22", "answered and said unto them,"), sy("5:23"), Q("5:24", "s", "to forgive sins", "c", "palsied),", "s")]),
        D([cp("5:25"), N("5:26", "with fear, saying,")], lambda w, h: A.bed_carried("bc1", w, h, 512, rise=True), "#8FD0E2"),
        D([Q("5:27", "c", "said unto him,", "s"), cp("5:28")], lambda w, h: A.toll("tl1", w, h, 513), "#8FD0E2", head="Levi Made Him a Great Feast"),
        D([cp("5:29"), N("5:30", "disciples, saying,")], lambda w, h: A.at_meat("am1", w, h, 514, pharisees=True), "#8A6A4A"),
        F([N("5:31", "said unto them,"), sy("5:32")]),
        F([N("5:33", "said unto him,")], PHARISEE, bg=RED, head="The Bridegroom"),
        F([N("5:34", "said unto them,"), sy("5:35")], JESUS),
        D([Q("5:36", "c", "a parable unto them:", "s"), sy("5:37"), sy("5:38"), sy("5:39")], lambda w, h: A.wineskins("ws1", w, h, 515), "#E8D8B8"),
        # Luke 6
        D([cp("6:1"), N("6:2", "Pharisees said,")], lambda w, h: A.grainfield("gf1", w, h, 601), "#D8B860", head="Lord of the Sabbath", sky=6),
        F([N("6:3", "answering them said,"), sy("6:4"), N("6:5", "said unto them,")]),
        D([cp("6:6"), cp("6:7")], lambda w, h: A.withered("wt1", w, h, 602), "#C8B490", head="Stretch Forth Thy Hand"),
        F([Q("6:8", "c", "withered,", "s", "stand forth in the midst.", "c")], JESUS),
        F([N("6:9", "said unto them,")], JESUS_STERN, bg=RED),
        D([Q("6:10", "c", "said unto him,", "s", "Stretch forth thy hand.", "c"), cp("6:11")], lambda w, h: A.withered("wt2", w, h, 603, restored=True), "#C8B490"),
        D([cp("6:12")], lambda w, h: A.mount_alone("ma1", w, h, 604), NIGHT, head="Whom He Named Apostles", art_h=240),
        D([cp("6:13"), cp("6:14"), cp("6:15"), cp("6:16")], lambda w, h: A.twelve_luke("tw1", w, h, 605), "#0B1A2E", art_h=200),
        D([cp("6:17"), cp("6:18"), cp("6:19")], lambda w, h: A.level_place("lv1", w, h, 606, touching=True), "#8FD0E2", head="Blessed Are Ye Poor", art_h=220),
        D([N("6:20", "and said,"), sy("6:21"), sy("6:22"), sy("6:23")], lambda w, h: A.level_place("lv2", w, h, 607), "#8FD0E2"),
        F([sy("6:24"), sy("6:25"), sy("6:26")], JESUS_STERN, bg=RED),
        F([sy("6:27"), sy("6:28")], JESUS_TEACH, head="Love Your Enemies"),
        D([sy("6:29"), sy("6:30"), sy("6:31")], lambda w, h: A.two_miles("tm1", w, h, 608), "#8FD0E2"),
        D(S("6:32", 36), lambda w, h: A.sun_rain("sr1", w, h, 609), "#5A7AA8"),
        D([sy("6:37"), sy("6:38")], lambda w, h: A.measure("me1", w, h, 610), "#C8A060", head="Good Measure, Running Over", art_h=220),
        D([Q("6:39", "c", "a parable unto them,", "s"), sy("6:40")], lambda w, h: A.blind_pit("bl1", w, h, 611), "#8FD0E2"),
        D([sy("6:41"), sy("6:42")], lambda w, h: A.mote_beam("mb1", w, h, 612), "#B8987A"),
        D([sy("6:43"), sy("6:44"), sy("6:45")], lambda w, h: A.fruit_trees("ft1", w, h, 613), "#8FD0E2"),
        D([sy("6:46"), sy("6:47"), sy("6:48")], lambda w, h: A.house_storm("hs1", w, h, 614), "#14141E", head="A Foundation upon the Rock"),
        D([sy("6:49")], A.footed(lambda w, h: A.house_storm("hs2", w, h, 615, rock=False), "#3A5A7A"), "#14141E", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C04-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE WIDOW OF NAIN")))
