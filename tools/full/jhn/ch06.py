"""John volume, Chapter 6 — Lazarus, Come Forth (John 11–12). Every verse, word for word from ref/eng-asv.
Lazarus sick on his bed at Bethany, his sisters by him; the messenger; the road back into Judæa, Thomas — let us also go;
Martha on the road, I am the resurrection, and the life; Mary fallen at his feet; Jesus wept, beside his face; the cave and
the stone (four days dead is words only, no decay drawn); the stone taken away and his eyes lifted up; Lazarus come forth,
a standing figure bound in white grave-clothes, his face bound about with a napkin, in the tomb door. The council and
Caiaphas; Ephraim near the wilderness. The supper at Bethany, Martha serving and Lazarus at the table, Mary with the pound
of nard and her hair, the house filled with the odour; Judas and the bag. The branches of the palm trees and the young ass;
the Greeks who would see Jesus; the grain of wheat in the earth; Now is my soul troubled; the voice out of heaven in the
Voice box over the sky (God never drawn; "the prince of this world," 12:31, is words only); the light going down on the
road; Isaiah's words in song boxes; Jesus crying out in the temple."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art6 as A, ch05 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        JESUS_GRIEF, JEW, CROWD, PETER, ANDREW, JOHN, JUDAS, CAIAPHAS, MARTHA, MARTHA_GRIEF, MARYB_GRIEF, NICODEMUS_DAY)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C06-00-Title", "Chapter 6 · Lazarus, Come Forth", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#5A6A9A"></rect><g transform="translate(0 180)">{A.tomb_cave("t6", 760, 720, 1101, stage="forth")}</g>'
           '<rect x="0" y="899" width="760" height="181" fill="#7A6A4A"></rect>')
    return title(6, "Lazarus, Come Forth", "John 11 – 12", svg, "#5A6A9A", v("11:43", frm="Lazarus, come forth."))


SEGS = [D([cp("11:1"), cp("11:2")], lambda w, h: A.sick_bed("sb1", w, h, 1102), "#B89A78", head="Lazarus of Bethany", sky=11, art_h=240),
        D([cp("11:3", to="saying,"), sy("11:3", frm="Lord,")], lambda w, h: A.messenger("me1", w, h, 1103), "#8FD0E2"),
        F([cp("11:4", to="he said,"), sy("11:4", frm="This sickness"), cp("11:5"), cp("11:6")], JESUS),
        F([said("11:7", "to the disciples,", "Let us go")], JESUS_TEACH),
        F([said("11:8", "say unto him,", "Rabbi,")], PETER),
        F([said("11:9", "Jesus answered,", "Are there not"), sy("11:10")], JESUS_TEACH),
        F([cp("11:11", to="saith unto them,"), sy("11:11", frm="Our friend")], JESUS),
        F([said("11:12", "said unto him,", "Lord,"), cp("11:13")], ANDREW),
        F([cp("11:14", to="plainly,"), sy("11:14", frm="Lazarus is dead."), sy("11:15")], JESUS_GRIEF, bg=COLD),
        D([cp("11:16", to="fellow-disciples,"), sy("11:16", frm="Let us also")], lambda w, h: A.road_judaea("rj1", w, h, 1104), "#8FD0E2", art_h=240),
        D([cp("11:17"), cp("11:18"), cp("11:19"), cp("11:20")], lambda w, h: A.martha_road("mr1", w, h, 1105), "#8FD0E2", head="I Am the Resurrection", art_h=240),
        F([said("11:21", "said unto Jesus,", "Lord,"), sy("11:22")], MARTHA_GRIEF, bg=COLD),
        F([said("11:23", "saith unto her,", "Thy brother")], JESUS),
        F([said("11:24", "saith unto him,", "I know")], MARTHA),
        F([said("11:25", "said unto her,", "I am the resurrection"), sy("11:26")], JESUS_TEACH),
        F([said("11:27", "She saith unto him,", "Yea, Lord:")], MARTHA),
        D([cp("11:28", to="secretly, saying,"), sy("11:28", frm="The Teacher"), cp("11:29"), cp("11:30"), cp("11:31")], lambda w, h: A.messenger("me2", w, h, 1106), "#8FD0E2"),
        D([cp("11:32", to="saying unto him,"), sy("11:32", frm="Lord,")], lambda w, h: A.mary_feet("mf1", w, h, 1107), "#3A2A5A", art_h=240),
        F([cp("11:33"), cp("11:34", to="and said,"), sy("11:34", frm="Where have ye", to="laid him?")], JESUS_GRIEF, bg=COLD, head="Jesus Wept"),
        F([cp("11:34", frm="They say unto him,", to="unto him,"), sy("11:34", frm="Lord, come")], MARYB_GRIEF, bg=COLD),
        F([cp("11:35")], JESUS_GRIEF, bg=COLD),
        F([said("11:36", "therefore said,", "Behold"), cp("11:37", to="some of them said,"), sy("11:37", frm="Could not")], CROWD, bg=COLD),
        D([cp("11:38"), cp("11:39", to="Jesus saith,"), sy("11:39", frm="Take ye away", to="the stone."), cp("11:39", frm="Martha,", to="saith unto him,"),
           sy("11:39", frm="Lord, by this time")], lambda w, h: A.tomb_cave("tc1", w, h, 1108), "#5A4A6A", art_h=260),
        F([said("11:40", "saith unto her,", "Said I not")], JESUS_TEACH),
        D([cp("11:41", to="and said,"), sy("11:41", frm="Father,"), sy("11:42")], lambda w, h: A.tomb_cave("tc2", w, h, 1109, stage="taken"), "#5A6A9A",
          head="Lazarus, Come Forth", art_h=260),
        D([cp("11:43", to="loud voice,"), sy("11:43", frm="Lazarus, come forth."), cp("11:44", to="saith unto them,"), sy("11:44", frm="Loose him,")],
          lambda w, h: A.tomb_cave("tc3", w, h, 1110, stage="forth"), "#5A6A9A", art_h=320),
        D([cp("11:45"), cp("11:46"), cp("11:47", to="and said,"), sy("11:47", frm="What do we?"), sy("11:48")], lambda w, h: A.priests_court("pc1", w, h, 1111), "#0B0B2A",
          head="It Is Expedient"),
        F([cp("11:49", to="said unto them,"), sy("11:49", frm="Ye know nothing"), sy("11:50")], CAIAPHAS, bg=RED),
        F([cp("11:51"), cp("11:52"), cp("11:53")], CAIAPHAS, bg=RED),
        D([cp("11:54")], lambda w, h: A.ephraim("ep1", w, h, 1112), "#5A3A5A"),
        D([cp("11:55"), cp("11:56", to="in the temple,"), sy("11:56", frm="What think ye?"), cp("11:57")], lambda w, h: A.city_gate_stirred("cg1", w, h, 1113), "#8FD0E2"),
        # John 12
        D([cp("12:1"), cp("12:2")], lambda w, h: A.supper_bethany("su1", w, h, 1201), "#C8A878", head="The Odor of the Ointment", sky=12, art_h=240),
        D([cp("12:3")], lambda w, h: A.supper_bethany("su2", w, h, 1202, stage="anoint"), "#C8A878", art_h=280),
        F([cp("12:4"), sy("12:5"), cp("12:6")], JUDAS, bg=RED),
        F([said("12:7", "Jesus therefore said,", "Suffer her"), sy("12:8")], JESUS),
        D([cp("12:9"), cp("12:10"), cp("12:11")], lambda w, h: A.bethany("be1", w, h, 1203), "#3A2A5A"),
        D([cp("12:12"), cp("12:13", to="and cried out,"), sy("12:13", frm="Hosanna:")], lambda w, h: A.entry("en1", w, h, 1204), "#8FD0E2", head="Hosanna", art_h=260),
        D([cp("12:14", to="as it is written,"), sg("12:15")], lambda w, h: A.bethphage("bp1", w, h, 1205), "#8FD0E2"),
        F([cp("12:16")], JOHN),
        D([cp("12:17"), cp("12:18"), cp("12:19", to="among themselves,"), sy("12:19", frm="Behold")], lambda w, h: A.city_gate_stirred("cg2", w, h, 1206), "#8FD0E2"),
        D([cp("12:20"), cp("12:21", to="saying,"), sy("12:21", frm="Sir,"), cp("12:22")], lambda w, h: A.greeks("gk1", w, h, 1207), "#8FD0E2", head="We Would See Jesus",
          art_h=240),
        F([said("12:23", "saying,", "The hour is come,")], JESUS_TEACH),
        D([sy("12:24")], lambda w, h: A.grain_wheat("gw1", w, h, 1208), "#8FD0E2", art_h=280),
        F([sy("12:25"), sy("12:26")], JESUS),
        F([sy("12:27"), sy("12:28", to="glorify thy name.")], JESUS_GRIEF, bg=COLD, head="The Voice out of Heaven"),
        D([cp("12:28", frm="There came", to="saying,"), gd("12:28", frm="I have both")], lambda w, h: A.voice_sky("vs1", w, h, 1209), "#2A2A5A", art_h=280),
        F([cp("12:29", to="others said,"), sy("12:29", frm="An angel")], CROWD),
        F([said("12:30", "answered and said,", "This voice"), sy("12:31"), sy("12:32"), cp("12:33")], JESUS_TEACH),
        F([said("12:34", "answered him,", "We have heard")], CROWD),
        D([said("12:35", "said unto them,", "Yet a little"), sy("12:36", to="sons of light."), cp("12:36", frm="These things spake")],
          lambda w, h: A.dusk_road("dr1", w, h, 1210), "#0B0B2A", head="Walk While Ye Have the Light", art_h=240),
        D([cp("12:37"), cp("12:38", to="which he spake,"), sg("12:38", frm="Lord, who hath")], lambda w, h: A.scriptures("sc1", w, h, 1211), "#3A2A2A"),
        D([cp("12:39"), sg("12:40"), cp("12:41")], lambda w, h: A.prophecy("pr1", w, h, 1212), "#1A1630"),
        F([cp("12:42"), cp("12:43")], NICODEMUS_DAY),
        F([said("12:44", "cried and said,", "He that believeth"), sy("12:45"), sy("12:46")], JESUS_TEACH, head="I Am Come a Light"),
        D([sy("12:47"), sy("12:48")], lambda w, h: A.word_light("wl1", w, h, 1213, "world"), "#05051A"),
        F([sy("12:49"), sy("12:50")], JESUS)]
PG.extend(K.pack(SEGS, "JHN-C06-D", PG.next(), end=nxt("NEXT · THE WASHING OF FEET")))
