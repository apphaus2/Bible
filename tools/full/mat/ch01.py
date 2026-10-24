"""Matthew volume, Chapter 1 — The Son of David (Matthew 1–4). Every verse, word for word from ref/eng-asv.
The book of the generation: the three fourteens as one chart over roll cells (every name and every word), then the three
runs of fourteen; Mary at Nazareth; Joseph's trouble beside his face; the angel of the Lord in his dream (white light, no
face); Immanuel in a song box over the prophet's scroll; the child born and named JESUS. The wise-men on their camels before
Jerusalem; Herod troubled; the chief priests and scribes in his hall, the prophecy of Bethlehem; the star standing over the
house; gold and frankincense and myrrh; the flight into Egypt by night. Herod's slaughter at Bethlehem is words only, over
the empty street with every door shut, and Rachel weeping over the bare hills of Ramah. The return to Nazareth. John the
Baptist in the wilderness and at the Jordan; the axe at the root; the fan and the threshing-floor; the heavens opened, the
Spirit as a dove of light and the Father's voice in the Voice box. The temptation: Jesus alone in every picture, the devil
never drawn, his words over the empty desert, the pinnacle and the mountain; angels of light ministering. Capernaum by the
sea, the great light; the fishers of men; the synagogues and the multitudes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from mat import G, art as A
from mat.common import (K, Pages, cp, gd, sg, sy, v, title, chart_roll, cell, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN,
                        BAPTIST, BAPTIST_HUMBLE, JOSEPH_TROUBLED, MAGUS, HEROD_TROUBLED, HEROD_GREAT, HEROD_WROTH, SCRIBE)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("MAT-C01-00-Title", "Chapter 1 · The Son of David", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 300)">{A.bethlehem(760, 780, 101)}</g>'
    return title(1, "The Son of David", "Matthew 1 – 4", svg, NIGHT, v("1:1"))


CAP1 = v("1:1")
GEN = [cell("From Abraham unto David", "1:2-6", "#FFD23F", to="David the king."),
       cell("From David unto the Carrying Away", "1:6-11", "#8FD0E2", frm="And David begat"),
       cell("From the Carrying Away unto the Christ", "1:12-16", "#F3EFE6")]
K.label()                                          # the genealogy's cuts are on the chart page, not the next panel's label


@P("MAT-C01-A-P01-TheBookOfTheGeneration", "The Book of the Generation")
def generations(n):
    return chart_roll(GEN, lambda w, h: A.generations(w, h, top=0.13), 470, "Matthew 1:1–16 — The Book of the Generation", n, cap=CAP1,
                      ref="MATT 1:1", tag="THE GENERATIONS · MATTHEW 1")


SEGS = [K.drawn([cp("1:17")], lambda w, h: A.fourteens(w, h), MAP, head="Fourteen Generations"),
        K.drawn([cp("1:18")], lambda w, h: A.mary_alone("ma1", w, h, 111), "#B8987A", head="Immanuel", stamp=1),
        K.face([cp("1:19")], JOSEPH_TROUBLED, bg=COLD),
        K.drawn([cp("1:20", to="saying,"), sy("1:20", frm="Joseph,"), sy("1:21")], lambda w, h: A.dream("dr1", w, h, 112), NIGHT),
        K.drawn([cp("1:22"), sg("1:23")], lambda w, h: A.prophecy("pp1", w, h, 113), "#1A1630"),
        K.drawn([cp("1:24")], lambda w, h: A.wedded("wd1", w, h, 114), "#5A3A6A", head="He Called His Name Jesus"),
        K.drawn([cp("1:25")], lambda w, h: A.born("bn1", w, h, 115), "#3A2E3A"),
        # Matthew 2
        K.drawn([cp("2:1")], lambda w, h: A.magi("mg1", w, h, 201, city=True), NIGHT, head="Wise-Men from the East", stamp=2),
        K.face([sy("2:2")], MAGUS, bg=GOLDEN),
        K.face([cp("2:3")], HEROD_TROUBLED, bg=COLD),
        K.drawn([cp("2:4")], lambda w, h: A.herod_hall("hh1", w, h, 202, who="scribes"), "#3A1A3A"),
        K.face([cp("2:5", to="said unto him,"), sy("2:5", frm="In Bethlehem"), sg("2:6")], SCRIBE),
        K.drawn([cp("2:7")], lambda w, h: A.herod_hall("hh2", w, h, 203), "#3A1A3A", head="Herod the King"),
        K.face([cp("2:8", to="and said,"), sy("2:8", frm="Go and search")], HEROD_GREAT, bg=RED),
        K.drawn([cp("2:9"), cp("2:10")], lambda w, h: A.star_road("sr1", w, h, 204), NIGHT, head="Exceeding Great Joy"),
        K.drawn([cp("2:11")], lambda w, h: A.gifts("gf1", w, h, 205), "#4A3438"),
        K.drawn([cp("2:12")], lambda w, h: A.magi("mg2", w, h, 206, star=False, home=True), "#3A3A6A"),
        K.drawn([cp("2:13", to="saying,"), sy("2:13", frm="Arise and take")], lambda w, h: A.dream("dr2", w, h, 207, flee=True), NIGHT, head="Out of Egypt"),
        K.drawn([cp("2:14"), cp("2:15", to="saying,"), sg("2:15", frm="Out of Egypt")], lambda w, h: A.flight("fl1", w, h, 208), NIGHT),
        K.face([cp("2:16", to="exceeding wroth,")], HEROD_WROTH, bg=RED, head="Rachel Weeping for Her Children"),
        K.drawn([cp("2:16", frm="and sent forth")], lambda w, h: A.empty_street("es1", w, h, 209), "#05050E"),
        K.drawn([cp("2:17"), sg("2:18")], lambda w, h: A.ramah("rm1", w, h, 210), NIGHT),
        K.drawn([cp("2:19"), sy("2:20")], lambda w, h: A.dream("dr3", w, h, 211, egypt=True), NIGHT, head="He Shall Be Called a Nazarene"),
        K.drawn([cp("2:21")], lambda w, h: A.flight("fl2", w, h, 212, back=True), "#5A6A9A"),
        K.drawn([cp("2:22"), cp("2:23")], lambda w, h: A.nazareth("nz1", w, h, 213), "#8FD0E2"),
        # Matthew 3
        K.drawn([cp("3:1"), sy("3:2"), cp("3:3", to="saying,"), sg("3:3", frm="The voice")], lambda w, h: A.wilderness("wl1", w, h, 301, crowd_n=6), "#FFD89A",
                head="The Voice in the Wilderness", stamp=3),
        K.face([cp("3:4")], BAPTIST, bg=GOLDEN),
        K.drawn([cp("3:5"), cp("3:6")], lambda w, h: A.jordan("jd1", w, h, 302), "#8FD0E2"),
        K.face([cp("3:7", to="he said unto them,"), sy("3:7", frm="Ye offspring"), sy("3:8"), sy("3:9")], BAPTIST, bg=RED, head="Fruit Worthy of Repentance"),
        K.drawn([sy("3:10")], lambda w, h: A.axe_root("ax1", w, h, 303), "#3A1A1A"),
        K.face([sy("3:11")], BAPTIST, bg=GOLDEN),
        K.drawn([sy("3:12")], lambda w, h: A.threshing("th1", w, h, 304), "#5A3A6A"),
        K.drawn([cp("3:13")], lambda w, h: A.jordan("jd2", w, h, 305, jesus_=True, crowd_n=4), "#8FD0E2", head="This Is My Beloved Son"),
        K.face([cp("3:14", to="saying,"), sy("3:14", frm="I have need")], BAPTIST_HUMBLE, bg=GOLDEN),
        K.face([cp("3:15", to="said unto him,"), sy("3:15", frm="Suffer it now", to="all righteousness."), cp("3:15", frm="Then he suffereth")], JESUS),
        K.drawn([cp("3:16"), cp("3:17", to="saying,"), gd("3:17", frm="This is my")], lambda w, h: A.heavens_opened("ho1", w, h, 306), "#2A2A6A"),
        # Matthew 4
        K.drawn([cp("4:1"), cp("4:2")], lambda w, h: A.alone("al1", w, h, 401), NIGHT, head="It Is Written", stamp=4),
        K.drawn([cp("4:3", to="said unto him,"), sy("4:3", frm="If thou art")], lambda w, h: A.stones_close("sc1", w, h, 402), "#5A3A5A"),
        K.face([cp("4:4", to="answered and said,"), sy("4:4", frm="It is written,")], JESUS_TEACH),
        K.drawn([cp("4:5"), cp("4:6", to="saith unto him,"), sy("4:6", frm="If thou art")], lambda w, h: A.pinnacle("pn1", w, h, 403), "#2A3A7A",
                head="The Pinnacle of the Temple"),
        K.face([cp("4:7", to="said unto him,"), sy("4:7", frm="Again it is")], JESUS),
        K.drawn([cp("4:8"), cp("4:9", to="said unto him,"), sy("4:9", frm="All these")], lambda w, h: A.high_mountain("hm1", w, h, 404), "#3A1A4A",
                head="An Exceeding High Mountain"),
        K.face([cp("4:10", to="unto him,"), sy("4:10", frm="Get thee hence")], JESUS_STERN, bg=RED),
        K.drawn([cp("4:11")], lambda w, h: A.ministered("mn1", w, h, 405), "#3A2A5A"),
        K.drawn([cp("4:12"), cp("4:13"), cp("4:14")], lambda w, h: A.galilee("gl1", w, h, 406), "#8FD0E2", head="A Great Light"),
        K.drawn([sg("4:15"), sg("4:16")], lambda w, h: A.galilee("gl2", w, h, 407, town=False, tone="dawn"), "#3A3A7A"),
        K.face([cp("4:17", to="and to say,"), sy("4:17", frm="Repent ye")], JESUS_TEACH),
        K.drawn([cp("4:18"), cp("4:19", to="saith unto them,"), sy("4:19", frm="Come ye"), cp("4:20")], lambda w, h: A.fishers("fs1", w, h, 408), "#8FD0E2",
                head="Fishers of Men"),
        K.drawn([cp("4:21")], lambda w, h: A.zebedee("zb1", w, h, 409), "#8FD0E2"),
        K.drawn([cp("4:22")], lambda w, h: A.zebedee("zb2", w, h, 410, leaving=True), "#8FD0E2"),
        K.drawn([cp("4:23")], lambda w, h: A.synagogue("sy1", w, h, 411), "#C8B490", head="Great Multitudes"),
        K.drawn([cp("4:24"), cp("4:25")], lambda w, h: A.multitudes("mt1", w, h, 412), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MAT-C01-D", PG.next(), end=nxt("NEXT · THE SERMON ON THE MOUNT")))
