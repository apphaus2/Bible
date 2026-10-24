"""Luke volume, Chapter 10 — Consider the Lilies (Luke 12–13). Every verse, word for word from ref/eng-asv.
The many thousands treading one upon another; the leaven of the Pharisees; proclaimed upon the housetops; five sparrows
for two pence; the man who would have his brother divide the inheritance; the rich fool's fields and greater barns, and
the night his soul was required — God's words in the Voice box (God never drawn); the ravens and the lilies; fear not,
little flock; purses which wax not old; loins girded and lamps burning at the door in the night; the thief; the faithful
steward; fire upon the earth; five in one house divided; the cloud in the west and the south wind; the adversary and the
magistrate. The Galilæans whose blood Pilate mingled told in words over the empty altar court, and the tower in Siloam a
heap of fallen stones with no one drawn under them; the barren fig tree spared a year; the woman bowed together eighteen
years made straight (no spirit drawn), the ruler's indignation; the mustard seed and the leaven; the narrow door shut;
that fox Herod; O Jerusalem, Jerusalem, the hen and her brood."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art8 as A, ch09 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, CROWD_MAN, RULER, PHARISEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C10-00-Title", "Chapter 10 · Consider the Lilies", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.lilies_field("t10", 760, 780, 1201)}</g>'
    return title(10, "Consider the Lilies", "Luke 12 – 13", svg, "#3A6A2A", v("12:27", frm="Consider the lilies,", to="how they grow:"))


SEGS = [D([N("12:1", "his disciples first of all,"), sy("12:2"), sy("12:3")], lambda w, h: A.housetops("ht1", w, h, 1201), "#5A6A9A", head="The Leaven of the Pharisees", sky=12),
        F([sy("12:4"), sy("12:5")], JESUS_STERN, bg=RED),
        D([sy("12:6"), sy("12:7")], lambda w, h: A.sparrows("sp1", w, h, 1202), "#C8A878"),
        F([sy("12:8"), sy("12:9"), sy("12:10"), sy("12:11"), sy("12:12")], JESUS_TEACH),
        F([N("12:13", "said unto him,")], CROWD_MAN, bg=COLD, head="Take Heed of Covetousness"),
        F([N("12:14", "said unto him,"), N("12:15", "said unto them,")], JESUS),
        D([N("12:16", "a parable unto them, saying,")], lambda w, h: A.rich_fool("rf1", w, h, 1203), "#8FD0E2"),
        D([sy("12:17"), sy("12:18"), sy("12:19")], lambda w, h: A.rich_fool("rf2", w, h, 1204, stage="build"), "#8FD0E2"),
        D([Q("12:20", "s", "said unto him,", "g"), sy("12:21")], lambda w, h: A.rich_fool("rf3", w, h, 1205, stage="night"), NIGHT, art_h=240),
        F([N("12:22", "said unto his disciples,"), sy("12:23")], JESUS_TEACH, head="Consider the Ravens"),
        D([sy("12:24"), sy("12:25"), sy("12:26")], lambda w, h: A.birds_heaven("bh1", w, h, 1206), "#5AB0D8"),
        D([sy("12:27"), sy("12:28")], lambda w, h: A.lilies_field("lf1", w, h, 1207), "#8FD0E2", head="Consider the Lilies", art_h=220),
        F([sy("12:29"), sy("12:30"), sy("12:31")], JESUS),
        D([sy("12:32")], lambda w, h: A.little_flock("lk1", w, h, 1208), "#5A6A9A", head="Fear Not, Little Flock"),
        D([sy("12:33"), sy("12:34")], lambda w, h: A.treasures("tr1", w, h, 1209), "#2A2228"),
        D([sy("12:35"), sy("12:36")], lambda w, h: A.watching("wt1", w, h, 1210), NIGHT, head="Your Lamps Burning"),
        D([sy("12:37"), sy("12:38")], lambda w, h: A.watching("wt2", w, h, 1211, lord=True), NIGHT),
        D([sy("12:39"), sy("12:40")], lambda w, h: A.thief("th1", w, h, 1212), NIGHT),
        F([N("12:41", "And Peter said,")], PETER, head="The Faithful and Wise Steward"),
        D([N("12:42", "And the Lord said,"), sy("12:43"), sy("12:44")], lambda w, h: A.steward("st1", w, h, 1213), "#B8987A"),
        D([sy("12:45"), sy("12:46")], lambda w, h: A.steward("st2", w, h, 1214, evil=True), "#5A3A3A"),
        F([sy("12:47"), sy("12:48")], JESUS_STERN, bg=RED),
        D([sy("12:49"), sy("12:50")], lambda w, h: A.fire_earth("fe1", w, h, 1215), "#2A1A3A", head="Fire upon the Earth"),
        D([sy("12:51"), sy("12:52"), sy("12:53")], lambda w, h: A.divided("dv1", w, h, 1216), "#A88A6A"),
        D([N("12:54", "to the multitudes also,"), sy("12:55"), sy("12:56"), sy("12:57")], lambda w, h: A.red_sky("rs1", w, h, 1217), "#4A2A5A"),
        D([sy("12:58"), sy("12:59")], lambda w, h: A.prison_door("pd1", w, h, 1218), "#2A2228"),
        # Luke 13
        D([cp("13:1")], lambda w, h: A.altar_court("ac1", w, h, 1301), "#6A6A8A", head="Except Ye Repent", sky=13),
        F([N("13:2", "said unto them,"), sy("13:3")], JESUS_STERN, bg=RED),
        D([sy("13:4"), sy("13:5")], lambda w, h: A.siloam("sl1", w, h, 1302), "#8A9AB0"),
        D([N("13:6", "this parable;"), sy("13:7")], lambda w, h: A.fig_by_way("fg1", w, h, 1303), "#8FD0E2", head="The Barren Fig Tree"),
        D([sy("13:8"), sy("13:9")], lambda w, h: A.vineyard("vy1", w, h, 1304, tone="day", hire=False), "#8FD0E2"),
        D([cp("13:10"), cp("13:11"), N("13:12", "said to her,")], lambda w, h: A.bowed("bw1", w, h, 1305), "#C8B490", head="Thou Art Loosed", art_h=220),
        D([cp("13:13")], lambda w, h: A.bowed("bw2", w, h, 1306, straight=True), "#C8B490"),
        F([N("13:14", "said to the multitude,")], RULER, bg=RED),
        F([N("13:15", "and said,"), sy("13:16"), cp("13:17")], JESUS_STERN, bg=RED),
        D([N("13:18", "He said therefore,"), sy("13:19")], lambda w, h: A.mustard("ms1", w, h, 1307), "#8FD0E2", head="Like a Grain of Mustard Seed"),
        D([N("13:20", "again he said,"), sy("13:21")], lambda w, h: A.leaven("lv1", w, h, 1308), "#B8987A"),
        F([cp("13:22"), Q("13:23", "c", "said unto him,", "s", "that are saved?", "c")], CROWD_MAN, bg=COLD, head="The Narrow Door"),
        D([sy("13:24")], lambda w, h: A.narrow_door("nd1", w, h, 1309), "#4A3A6A"),
        D([sy("13:25"), sy("13:26"), sy("13:27")], lambda w, h: A.narrow_door("nd2", w, h, 1310, shut=True), NIGHT),
        D([sy("13:28"), sy("13:29"), sy("13:30")], lambda w, h: A.wedding_hall("wh1", w, h, 1311, guests=True), "#5A3A2A"),
        F([N("13:31", "saying to him,")], PHARISEE, bg=RED, head="Go and Say to That Fox"),
        D([N("13:32", "said unto them,"), sy("13:33")], lambda w, h: A.foxes("fx1", w, h, 1312), "#4A2A5A"),
        D([sy("13:34"), sy("13:35")], A.footed(lambda w, h: A.hen_chickens("hc1", w, h, 1313), "#5A4A3A"), "#C8A878", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C10-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE PRODIGAL SON")))
