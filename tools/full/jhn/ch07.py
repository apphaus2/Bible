"""John volume, Chapter 7 — The Washing of Feet (John 13–14). Every verse, word for word from ref/eng-asv.
The upper room by night: the twelve at the low table under the lamps; the devil in the heart of Judas told in words only
beside his face; Jesus rising from supper, laying aside his garments, girded with the towel, pouring water into the basin;
stooping with the basin and towel at Peter's feet — restrained and warm; the basin and towel alone; Ye ought to wash one
another's feet. One of you shall betray me: the beloved disciple leaning on his breast, the sop given across the table;
"then entered Satan into him" words only beside Judas' face; the door open on the night — and it was night. A new
commandment; the cock on the wall. John 14: the many mansions of light on the height; Thomas; I am the way — the road up
into the light; Philip; the Comforter promised, a soft light come down into the room; Judas not Iscariot; Peace I leave
with you; "the prince of the world" words only; Arise, let us go hence."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art7 as A, ch06 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        JESUS_GRIEF, PETER, JOHN, JUDAS, THOMAS, PHILIP, JUDE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C07-00-Title", "Chapter 7 · The Washing of Feet", title=True)
def title_page(n):
    svg = A.basin_still("t7", 760, 1080, 1301)
    return title(7, "The Washing of Feet", "John 13 – 14", svg, "#3A2A2A", v("13:34", frm="that ye love one another;", to="love one another;"))


SEGS = [D([cp("13:1")], lambda w, h: A.washing("wa1", w, h, 1302), "#4A3438", head="He Loved Them unto the End", sky=13, art_h=260),
        F([cp("13:2")], JUDAS, bg=RED),
        D([cp("13:3"), cp("13:4"), cp("13:5")], lambda w, h: A.washing("wa2", w, h, 1303, stage="rise"), "#4A3438", head="The Washing of Feet", art_h=260),
        D([cp("13:6", to="He saith unto him,"), sy("13:6", frm="Lord,")], lambda w, h: A.washing("wa3", w, h, 1304, stage="wash"), "#4A3438", art_h=280),
        F([said("13:7", "said unto him,", "What I do")], JESUS),
        F([cp("13:8", to="saith unto him,"), sy("13:8", frm="Thou shalt never", to="my feet.")], PETER),
        F([cp("13:8", frm="Jesus answered him,", to="answered him,"), sy("13:8", frm="If I wash")], JESUS_TEACH),
        F([said("13:9", "saith unto him,", "Lord,")], PETER),
        F([said("13:10", "saith to him,", "He that is bathed"), cp("13:11", to="therefore said he,"), sy("13:11", frm="Ye are not")], JESUS_GRIEF, bg=COLD),
        D([cp("13:12", to="said unto them,"), sy("13:12", frm="Know ye")], lambda w, h: A.washing("wa4", w, h, 1305), "#4A3438"),
        F([sy("13:13")], JESUS_TEACH),
        D([sy("13:14"), sy("13:15")], lambda w, h: A.basin_still("bs1", w, h, 1306), "#3A2A2A", art_h=240),
        F([sy("13:16"), sy("13:17")], JESUS),
        F([sy("13:18", to="be fulfilled,"), sg("13:18", frm="He that eateth"), sy("13:19"), sy("13:20")], JESUS_GRIEF, bg=COLD),
        F([cp("13:21", to="and said,"), sy("13:21", frm="Verily,")], JESUS_GRIEF, bg=COLD, head="One of You Shall Betray Me"),
        D([cp("13:22"), cp("13:23"), cp("13:24", to="saith unto him,"), sy("13:24", frm="Tell us")], lambda w, h: A.washing("wa5", w, h, 1307), "#4A3438"),
        F([cp("13:25", to="saith unto him,"), sy("13:25", frm="Lord, who")], JOHN),
        D([cp("13:26", to="answereth,"), sy("13:26", frm="He it is,", to="give it him."), cp("13:26", frm="So when he had")],
          lambda w, h: A.washing("wa6", w, h, 1308, stage="sop"), "#4A3438", art_h=260),
        F([cp("13:27", to="entered Satan into him.")], JUDAS, bg=RED),
        F([cp("13:27", frm="Jesus therefore", to="saith unto him,"), sy("13:27", frm="What thou doest")], JESUS_STERN, bg=RED),
        F([cp("13:28"), cp("13:29")], JOHN),
        D([cp("13:30")], lambda w, h: A.washing("wa7", w, h, 1309, stage="door"), "#4A3438", art_h=280),
        D([cp("13:31", to="Jesus saith,"), sy("13:31", frm="Now is"), sy("13:32")], lambda w, h: A.word_light("wl1", w, h, 1311, "glory"), "#FFC14D", head="A New Commandment"),
        F([sy("13:33")], JESUS_GRIEF, bg=COLD),
        D([sy("13:34"), sy("13:35")], lambda w, h: A.washing("wa9", w, h, 1312, stage="eleven"), "#4A3438", art_h=220),
        F([cp("13:36", to="saith unto him,"), sy("13:36", frm="Lord, whither", to="goest thou?")], PETER),
        F([cp("13:36", frm="Jesus answered,", to="answered,"), sy("13:36", frm="Whither I go")], JESUS),
        F([said("13:37", "saith unto him,", "Lord, why")], PETER),
        D([cp("13:38", to="answereth,"), sy("13:38", frm="Wilt thou")], lambda w, h: A.cockcrow("cc1", w, h, 1310), "#1A1A3A", art_h=220),
        # John 14
        D([sy("14:1"), sy("14:2"), sy("14:3"), sy("14:4")], lambda w, h: A.mansions("mn1", w, h, 1401), "#5A6A9A", head="Many Mansions", sky=14, art_h=260),
        F([said("14:5", "saith unto him,", "Lord,")], THOMAS),
        D([said("14:6", "saith unto him,", "I am the way,"), sy("14:7")], lambda w, h: A.the_way("tw1", w, h, 1402), "#3A4A8A", head="I Am the Way", art_h=260),
        F([said("14:8", "saith unto him,", "Lord, show")], PHILIP),
        F([said("14:9", "saith unto him,", "Have I been"), sy("14:10"), sy("14:11")], JESUS_TEACH),
        F([sy("14:12"), sy("14:13"), sy("14:14")], JESUS),
        D([sy("14:15"), sy("14:16"), sy("14:17")], lambda w, h: A.comforter("cf1", w, h, 1403), "#4A3438", head="Another Comforter", art_h=240),
        F([sy("14:18"), sy("14:19"), sy("14:20")], JESUS),
        F([sy("14:21")], JESUS_TEACH),
        F([said("14:22", "saith unto him,", "Lord, what")], JUDE),
        F([said("14:23", "said unto him,", "If a man"), sy("14:24")], JESUS_TEACH),
        D([sy("14:25"), sy("14:26"), sy("14:27")], lambda w, h: A.comforter("cf2", w, h, 1404), "#4A3438", head="Peace I Leave with You"),
        F([sy("14:28"), sy("14:29"), sy("14:30")], JESUS_GRIEF, bg=COLD),
        D([sy("14:31")], lambda w, h: A.washing("wa8", w, h, 1405, stage="rising"), "#4A3438", art_h=280)]
PG.extend(K.pack(SEGS, "JHN-C07-D", PG.next(), end=nxt("NEXT · THAT THEY MAY BE ONE")))
