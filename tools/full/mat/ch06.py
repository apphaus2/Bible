"""Matthew volume, Chapter 6 — Thou Art the Christ (Matthew 15–17). Every verse, word for word from ref/eng-asv.
The tradition of the elders over the disciples at bread; Isaiah's words in song boxes beside his stern face; the blind
leading the blind; the coast of Tyre and Sidon and the Canaanitish woman, the little dogs under the table; the sick laid at
his feet, the seven loaves and the seven baskets; the red sky; the boat without bread; the rock of Caesarea Philippi and
Peter's confession; the road to Jerusalem; the transfiguration — Jesus in white light, Moses and Elijah beside him, the
bright cloud with the Father's voice in the Voice box, then Jesus only; the boy healed (no demon drawn); the mountain
removed; the half-shekel and the fish with the shekel in its mouth."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art6 as A, ch05 as _prev
from mat.common import (K, Pages, drawn, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, ANDREW, JOHN, CANAANITE, FATHER_BOY, COLLECTOR)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C06-00-Title", "Chapter 6 · Thou Art the Christ", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A6A"></rect><g transform="translate(0 300)">{A.transfigured("t6", 760, 780, 1701)}</g>'
    return title(6, "Thou Art the Christ", "Matthew 15 – 17", svg, "#2A2A6A", v("16:16", frm="Thou art the Christ"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("15:1"), sy("15:2")], lambda w, h: A.unwashed("uw1", w, h, 1501), "#8FD0E2", head="The Tradition of the Elders", stamp=15),
        F([cp("15:3", to="said unto them,"), sy("15:3", frm="Why do ye"), sy("15:4"), sy("15:5"), sy("15:6")], JESUS_STERN, bg=RED),
        F([sy("15:7"), sg("15:8"), sg("15:9")], JESUS_STERN, bg=RED),
        F([cp("15:10", to="said unto them,"), sy("15:10", frm="Hear, and"), sy("15:11")]),
        F([cp("15:12", to="said unto him,"), sy("15:12", frm="Knowest thou")], ANDREW),
        D([cp("15:13", to="answered and said,"), sy("15:13", frm="Every plant"), sy("15:14")], lambda w, h: A.blind_pit("bp1", w, h, 1502), "#C8A890"),
        F([cp("15:15", to="said unto him,"), sy("15:15", frm="Declare")], PETER),
        F([cp("15:16", to="he said,"), sy("15:16", frm="Are ye also"), sy("15:17"), sy("15:18"), sy("15:19"), sy("15:20")]),
        D([cp("15:21"), cp("15:22", to="saying,"), sy("15:22", frm="Have mercy")], lambda w, h: A.tyre("ty1", w, h, 1503), "#8FD0E2", head="O Woman, Great Is Thy Faith"),
        F([cp("15:23", to="saying,"), sy("15:23", frm="Send her away;")], PETER),
        F([cp("15:24", to="answered and said,"), sy("15:24", frm="I was not")], JESUS),
        F([cp("15:25", to="saying,"), sy("15:25", frm="Lord, help me.")], CANAANITE, bg=COLD),
        D([cp("15:26", to="answered and said,"), sy("15:26", frm="It is not meet"), cp("15:27", to="she said,"), sy("15:27", frm="Yea, Lord:")], lambda w, h: A.crumbs("cr1", w, h, 1504),
          "#C8A878"),
        F([cp("15:28", to="said unto her,"), sy("15:28", frm="O woman,", to="as thou wilt."), cp("15:28", frm="And her daughter")], JESUS),
        D([cp("15:29"), cp("15:30"), cp("15:31")], lambda w, h: A.sick_laid("sl1", w, h, 1505), "#8FD0E2", head="Seven Loaves"),
        F([cp("15:32", to="and said,"), sy("15:32", frm="I have compassion")], JESUS),
        D([cp("15:33", to="say unto him,"), sy("15:33", frm="Whence"), cp("15:34", to="said unto them,"), sy("15:34", frm="How many", to="have ye?"),
           cp("15:34", frm="And they said,", to="And they said,"), sy("15:34", frm="Seven,"), cp("15:35"), cp("15:36")], lambda w, h: A.five_loaves("fl2", w, h, 1506), "#5A3A6A", art_h=240),
        D([cp("15:37"), cp("15:38"), cp("15:39")], lambda w, h: A.baskets_n("bk2", w, h, 1507, n=7), "#3A2A5A"),
        # Matthew 16
        D([cp("16:1"), cp("16:2", to="said unto them,"), sy("16:2", frm="When it is evening")], lambda w, h: A.red_sky("rs1", w, h, 1601), "#3A1A4A", head="The Signs of the Times", stamp=16),
        D([sy("16:3"), sy("16:4", to="the sign of Jonah."), cp("16:4", frm="And he left them")], lambda w, h: A.red_sky("rs2", w, h, 1602, morning=True), "#5A2A2A"),
        D([cp("16:5"), cp("16:6", to="said unto them,"), sy("16:6", frm="Take heed"), cp("16:7", to="saying,"), sy("16:7", frm="We took")], lambda w, h: A.no_bread("nb1", w, h, 1603), "#8FD0E2"),
        F([cp("16:8", to="perceiving it said,"), sy("16:8", frm="O ye of"), sy("16:9"), sy("16:10"), sy("16:11"), cp("16:12")]),
        D([cp("16:13", to="saying,"), sy("16:13", frm="Who do men"), cp("16:14", to="they said,"), sy("16:14", frm="Some say")], lambda w, h: A.caesarea("cs1", w, h, 1604), "#8FD0E2",
          head="Thou Art the Christ"),
        F([cp("16:15", to="unto them,"), sy("16:15", frm="But who say")], JESUS),
        F([cp("16:16", to="answered and said,"), sy("16:16", frm="Thou art the Christ")], PETER),
        F([cp("16:17", to="said unto him,"), sy("16:17", frm="Blessed art"), sy("16:18"), sy("16:19"), cp("16:20")]),
        D([cp("16:21")], lambda w, h: A.to_jerusalem("tj1", w, h, 1605), "#4A2A5A", head="Get Thee behind Me"),
        F([cp("16:22", to="saying,"), sy("16:22", frm="Be it far")], PETER, bg=COLD),
        F([cp("16:23", to="unto Peter,"), sy("16:23", frm="Get thee")], JESUS_STERN, bg=RED),
        F([cp("16:24", to="unto his disciples,"), sy("16:24", frm="If any man"), sy("16:25"), sy("16:26")], JESUS_GRIEF, bg=COLD),
        F([sy("16:27"), sy("16:28")]),
        # Matthew 17
        D([cp("17:1"), cp("17:2"), cp("17:3")], lambda w, h: A.transfigured("tf1", w, h, 1701), "#2A2A6A", head="He Was Transfigured", stamp=17, art_h=320),
        F([cp("17:4", to="said unto Jesus,"), sy("17:4", frm="Lord, it is good")], PETER),
        D([cp("17:5", to="saying,"), gd("17:5", frm="This is my beloved"), cp("17:6")], lambda w, h: A.transfigured("tf2", w, h, 1702, cloud=True), "#FFFDF0"),
        D([cp("17:7", to="and said,"), sy("17:7", frm="Arise,"), cp("17:8")], lambda w, h: A.transfigured("tf3", w, h, 1703, after=True), "#2A2A6A"),
        F([cp("17:9", to="saying,"), sy("17:9", frm="Tell the vision")], JESUS),
        F([cp("17:10", to="saying,"), sy("17:10", frm="Why then")], JOHN),
        F([cp("17:11", to="answered and said,"), sy("17:11", frm="Elijah indeed"), sy("17:12"), cp("17:13")], JESUS_GRIEF, bg=COLD),
        D([cp("17:14"), sy("17:15"), sy("17:16")], lambda w, h: A.boy_healed("bh1", w, h, 1704), "#8FD0E2", head="O Faithless and Perverse Generation"),
        F([cp("17:17", to="answered and said,"), sy("17:17", frm="O faithless")], JESUS_STERN, bg=RED),
        D([cp("17:18")], lambda w, h: A.boy_healed("bh2", w, h, 1705, kneeling=False), "#8FD0E2"),
        F([cp("17:19", to="and said,"), sy("17:19", frm="Why could")], ANDREW),
        D([cp("17:20", to="saith unto them,"), sy("17:20", frm="Because of")], lambda w, h: A.mountain_move("mm1", w, h, 1706), "#5A3A6A"),
        F([cp("17:22", to="said unto them,"), sy("17:22", frm="The Son of man"), sy("17:23", to="raised up."), cp("17:23", frm="And they were")], JESUS_GRIEF, bg=COLD),
        F([cp("17:24", to="and said,"), sy("17:24", frm="Doth not")], COLLECTOR),
        F([cp("17:25", to="He saith,"), sy("17:25", frm="Yea.", to="Yea.")], PETER),
        D([cp("17:25", frm="And when he came", to="saying,"), sy("17:25", frm="What thinkest"), cp("17:26", to="And when he said,"), sy("17:26", frm="From strangers,", to="From strangers,"), cp("17:26", frm="Jesus said unto him,", to="Jesus said unto him,"),
           sy("17:26", frm="Therefore the sons"), sy("17:27")], lambda w, h: A.hook_fish("hf1", w, h, 1708), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MAT-C06-D", PG.next(), most=4, lone=0.5, budget=1300, end=nxt("NEXT · THE FIRST SHALL BE LAST")))
