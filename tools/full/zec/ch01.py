"""Zechariah volume, Chapter 1 — The Night Visions (Zechariah 1–4). Every verse, word for word from ref/asv.
The word in the eighth month (1:1 in a caption) and return unto me, beside Zechariah's face; the fathers' tombs; then the
night visions as glowing plates: I the horses among the myrtle-trees (the rider a shape of light), the line stretched over
Jerusalem; II the four horns and the four smiths; III the man with the measuring line and the wall of fire, the road home
from the land of the north, Zion in the light; IV Joshua the high priest (the adversary never drawn: words only), the filthy
garments taken away and the clean mitre, the stone of seven eyes; V the candlestick of gold and the two olive-trees, the
great mountain become a plain, the plummet in Zerubbabel's hand. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, nxt, NIGHT
from zec import G, art as A
from zec.common import K, cp, gd, sg, sy, gds, sgs, ZECHARIAH, ZECH_NIGHT, ZECH_AWE, ZECH_GOLD, ZERUBBABEL, JESHUA, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
VN = "#0B0B2A"


@P("ZEC-C01-00-Title", "Chapter 1 · The Night Visions", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 200)">{A.bare(A.myrtle_horses, "tm", 760, 700, 101)}</g>'
    return title(1, "The Night Visions", "Zechariah 1 – 4", svg, "#0B0B2A", v("1:8", to="among the myrtle-trees that were in the bottom;"), "Zechariah · Volume Thirty-Eight")


SEGS = [K.face([cp("1:1"), gd("1:2"), gd("1:3")], ZECHARIAH, head="Return unto Me", stamp=1),
        K.drawn(gds("1:4-6"), lambda w, h: A.fathers(w, h, 102), "#2A1A3A"),
        K.drawn([cp("1:7"), cp("1:8")], lambda w, h: A.myrtle_horses("mh1", w, h, 103), VN, head="Among the Myrtle-trees", h=440),
        K.face([cp("1:9", to="Then said I,"), sy("1:9", frm="O my lord", to="what are these?"), cp("1:9", frm="And the angel", to="said unto me,"), sy("1:9", frm="I will show")], ZECH_NIGHT, bg=COLD),
        K.drawn([cp("1:10", to="answered and said,"), sy("1:10", frm="These are"), cp("1:11", to="and said,"), sy("1:11", frm="We have walked"),
                 cp("1:12", to="answered and said,"), sy("1:12", frm="O Jehovah of hosts"), cp("1:13")], lambda w, h: A.myrtle_horses("mh2", w, h, 104), VN),
        K.drawn([cp("1:14", to="said unto me,"), sy("1:14", frm="Cry thou,", to="saying,"), gd("1:14", frm="Thus saith"), gd("1:15"), gd("1:16"), gd("1:17")],
                lambda w, h: A.line_jerusalem(w, h, 106), "#2A2A5A"),
        K.drawn([cp("1:18"), cp("1:19", to="talked with me,"), sy("1:19", frm="What are these?", to="What are these?"), cp("1:19", frm="And he answered me,", to="answered me,"),
                 sy("1:19", frm="These are the horns")], lambda w, h: A.horns("hr1", w, h, 107), VN, head="Four Horns and Four Smiths"),
        K.drawn([cp("1:20"), cp("1:21", to="Then said I,"), sy("1:21", frm="What come", to="to do?"), cp("1:21", frm="And he spake,", to="saying,"), sy("1:21", frm="These are the horns")],
                lambda w, h: A.horns("hr2", w, h, 108, smiths=True), VN)]
PG.extend(K.paged([SEGS[0:2], SEGS[2:4], SEGS[4:6], SEGS[6:8]], "ZEC-C01-D", PG.next()))
SEGS2 = [K.drawn([cp("2:1"), cp("2:2", to="Then said I,"), sy("2:2", frm="Whither", to="goest thou?"), cp("2:2", frm="And he said", to="unto me,"), sy("2:2", frm="To measure")],
                 lambda w, h: A.measuring("ms1", w, h, 109), VN, head="A Man with a Measuring Line", stamp=2),
         K.drawn([cp("2:3"), cp("2:4", to="said unto him,"), sy("2:4", frm="Run,"), gd("2:5")], lambda w, h: A.wall_fire("wf1", w, h, 110), VN),
         K.drawn(gds("2:6-9"), lambda w, h: A.flee_north(w, h), "#0B1A2E"),
         K.drawn([gd("2:10"), gd("2:11"), sg("2:12"), sg("2:13")], lambda w, h: A.zion_dwell(w, h, 111), "#2A2A5A", head="Sing and Rejoice, O Daughter of Zion")]
PG.extend(K.pack(SEGS2, "ZEC-C01-E", PG.next()))
SEGS3 = [K.drawn([cp("3:1"), cp("3:2", to="unto Satan,"), gd("3:2", frm="Jehovah rebuke")], lambda w, h: A.joshua_trial("jt1", w, h, 112), VN, head="Joshua the High Priest", stamp=3),
         K.drawn([cp("3:3"), cp("3:4", to="saying,"), sy("3:4", frm="Take the filthy", to="from off him."), cp("3:4", frm="And unto him he said,", to="he said,"), sy("3:4", frm="Behold, I have")],
                 lambda w, h: A.joshua_trial("jt2", w, h, 113, clean=True), VN),
         K.drawn([cp("3:5", to="And I said,"), sy("3:5", frm="Let them set", to="upon his head."), cp("3:5", frm="So they set")], lambda w, h: A.joshua_trial("jt3", w, h, 114, mitre=True), VN),
         K.face([cp("3:6"), gd("3:7"), gd("3:8")], JESHUA),
         K.drawn(gds("3:9-10"), lambda w, h: A.seven_eyes("se1", w, h, 115), VN)]
PG.extend(K.pack(SEGS3, "ZEC-C01-F", PG.next()))
SEGS4 = [K.drawn([cp("4:1"), cp("4:2", to="said unto me,"), sy("4:2", frm="What seest", to="seest thou?"), cp("4:2", frm="And I said,", to="And I said,"), sy("4:2", frm="I have seen"), sy("4:3")],
                 lambda w, h: A.lampstand("ls1", w, h, 116), VN, head="A Candlestick All of Gold", stamp=4),
         K.face([cp("4:4", to="saying,"), sy("4:4", frm="What are these"), cp("4:5", to="said unto me,"), sy("4:5", frm="Knowest", to="these are?"),
                 cp("4:5", frm="And I said,", to="And I said,"), sy("4:5", frm="No, my lord.")], ZECH_AWE, bg=COLD),
         K.drawn([cp("4:6", to="unto me, saying,"), sy("4:6", frm="This is the word", to="Zerubbabel, saying,"), gd("4:6", frm="Not by might"), gd("4:7")],
                 lambda w, h: A.mountain_plain(w, h, 117), "#3A3A6A", head="Not by Might, nor by Power"),
         K.drawn([cp("4:8"), gd("4:9"), gd("4:10")], lambda w, h: A.plummet("pl1", w, h, 118), "#8FD0E2"),
         K.face([cp("4:11", to="said unto him,"), sy("4:11", frm="What are these"), cp("4:12", to="said unto him,"), sy("4:12", frm="What are these")], ZECH_NIGHT, bg=COLD),
         K.drawn([cp("4:13", to="and said,"), sy("4:13", frm="Knowest", to="these are?"), cp("4:13", frm="And I said,", to="And I said,"), sy("4:13", frm="No, my lord."),
                  cp("4:14", to="Then said he,"), sy("4:14", frm="These are")], lambda w, h: A.lampstand("ls2", w, h, 119, spouts=True), VN)]
PG.extend(K.pack(SEGS4, "ZEC-C01-G", PG.next(), end=nxt("NEXT · THE FOUR CHARIOTS")))
