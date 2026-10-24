"""Mark volume, Chapter 5 — Thou Art the Christ (Mark 8:1–9:29). Every verse, word for word from ref/eng-asv.
Four thousand on the hillside, the seven loaves, the seven baskets; the Pharisees asking a sign on the shore of Dalmanutha,
Jesus' deep sigh beside his face; one loaf in the boat, the leaven; the twelve baskets and the seven again, as he asks them.
The blind man of Bethsaida led out by the hand, the world first seen blurred — men as trees, walking — then all things
clearly. Cæsarea Philippi under the rock; Peter's confession beside his face; the Son of man must suffer; Get thee behind
me; the road to Jerusalem and the cross to take up. The transfiguration as Matthew's: Jesus in white light on the high
mountain, his garments glistering, Elijah and Moses beside him, the three below; the cloud of light and the Father's voice
in the Voice box, nothing drawn in the cloud; Jesus only. The way down; Elijah is come. The boy with the dumb spirit: the
multitude at the mountain's foot; the father's words beside his face; the fits and the tearing told in words only, over
the crowd standing in a ring with its back to us (the boy and the spirit are never drawn in it); I believe, help thou
mine unbelief; then the boy standing quiet beside his father."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art5 as A, ch04 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, PETER_GRIEF, ANDREW, JOHN, PHARISEE, FATHER_BOY, BETHSAIDA, BETHSAIDA_SEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C05-00-Title", "Chapter 5 · Thou Art the Christ", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A6A"></rect><g transform="translate(0 300)">{A.transfigured("t5", 760, 780, 902)}</g>'
    return title(5, "Thou Art the Christ", "Mark 8:1 – 9:29", svg, "#2A2A6A", v("8:29", frm="Thou art the Christ."))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [F([cp("8:1"), sy("8:2"), sy("8:3")], JESUS, head="Seven Loaves", stamp=8),
        D([cp("8:4", to="answered him,"), sy("8:4", frm="Whence shall"), cp("8:5", to="And he asked them,"), sy("8:5", frm="How many", to="have ye?"),
           cp("8:5", frm="And they said,", to="And they said,"), sy("8:5", frm="Seven.")], lambda w, h: A.hillside("hs1", w, h, 804), "#8FD0E2"),
        D([cp("8:6"), cp("8:7")], lambda w, h: A.five_loaves("fl1", w, h, 806), "#5A3A6A", art_h=220),
        D([cp("8:8"), cp("8:9")], lambda w, h: A.baskets_n("bk1", w, h, 808, n=7), "#3A2A5A"),
        D([cp("8:10"), cp("8:11")], lambda w, h: A.sign_asked("sa1", w, h, 810), "#8FD0E2", head="The Leaven of the Pharisees"),
        F([cp("8:12", to="and saith,"), sy("8:12", frm="Why doth"), cp("8:13")], JESUS_GRIEF, bg=COLD),
        D([cp("8:14"), cp("8:15", to="saying,"), sy("8:15", frm="Take heed,"), cp("8:16", to="saying,"), sy("8:16", frm="We have no bread.")],
          lambda w, h: A.no_bread("nb1", w, h, 814), "#8FD0E2"),
        F([cp("8:17", to="saith unto them,"), sy("8:17", frm="Why reason"), sy("8:18")], JESUS_STERN, bg=RED),
        D([sy("8:19", to="took ye up?"), cp("8:19", frm="They say unto him,", to="They say unto him,"), sy("8:19", frm="Twelve.")],
          lambda w, h: A.baskets("bk2", w, h, 819), "#3A2A5A"),
        D([sy("8:20", to="took ye up?"), cp("8:20", frm="And they say", to="unto him,"), sy("8:20", frm="Seven."), cp("8:21", to="said unto them,"), sy("8:21", frm="Do ye not")],
          lambda w, h: A.baskets_n("bk3", w, h, 820, n=7), "#3A2A5A"),
        D([cp("8:22"), cp("8:23", to="he asked him,"), sy("8:23", frm="Seest thou")], lambda w, h: A.bethsaida("bs1", w, h, 822), "#8FD0E2", head="I See Men, as Trees, Walking"),
        D([cp("8:24", to="and said,"), sy("8:24", frm="I see men;")], lambda w, h: A.men_as_trees("mt1", w, h, 824), "#C8D8E0", art_h=240),
        F([cp("8:25")], BETHSAIDA_SEE),
        F([cp("8:26", to="saying,"), sy("8:26", frm="Do not even")], JESUS),
        D([cp("8:27", to="saying unto them,"), sy("8:27", frm="Who do men"), cp("8:28", to="saying,"), sy("8:28", frm="John the Baptist;")],
          lambda w, h: A.caesarea("cs1", w, h, 827), "#8FD0E2", head="Thou Art the Christ"),
        F([cp("8:29", to="And he asked them,"), sy("8:29", frm="But who say", to="that I am?")], JESUS),
        F([cp("8:29", frm="Peter answereth", to="unto him,"), sy("8:29", frm="Thou art the Christ.")], PETER),
        F([cp("8:30"), cp("8:31"), cp("8:32", to="openly.")], JESUS_GRIEF, bg=COLD),
        F([cp("8:32", frm="And Peter took")], PETER_GRIEF, bg=COLD, head="Get Thee behind Me"),
        F([cp("8:33", to="and saith,"), sy("8:33", frm="Get thee behind")], JESUS_STERN, bg=RED),
        D([cp("8:34", to="said unto them,"), sy("8:34", frm="If any man"), sy("8:35")], lambda w, h: A.to_jerusalem("tj1", w, h, 834), "#4A2A5A", head="Take Up His Cross"),
        F([sy("8:36"), sy("8:37"), sy("8:38")], JESUS_GRIEF, bg=COLD),
        # Mark 9
        F([cp("9:1", to="said unto them,"), sy("9:1", frm="Verily")], JESUS_TEACH, stamp=9),
        D([cp("9:2"), cp("9:3"), cp("9:4")], lambda w, h: A.transfigured("tf1", w, h, 902), "#2A2A6A", head="He Was Transfigured", art_h=320),
        F([cp("9:5", to="saith to Jesus,"), sy("9:5", frm="Rabbi,"), cp("9:6")], PETER),
        D([cp("9:7", to="out of the cloud,"), gd("9:7", frm="This is my beloved")], lambda w, h: A.transfigured("tf2", w, h, 907, cloud=True), "#FFFDF0", art_h=280),
        D([cp("9:8")], lambda w, h: A.transfigured("tf3", w, h, 908, after=True), "#2A2A6A"),
        D([cp("9:9"), cp("9:10")], lambda w, h: A.coming_down("cd1", w, h, 909), "#3A2A5A", head="Elijah Is Come"),
        F([cp("9:11", to="saying,"), sy("9:11", frm="How is it")], JOHN),
        F([cp("9:12", to="said unto them,"), sy("9:12", frm="Elijah indeed"), sy("9:13")], JESUS_GRIEF, bg=COLD),
        D([cp("9:14"), cp("9:15"), cp("9:16", to="And he asked them,"), sy("9:16", frm="What question")], lambda w, h: A.foot_mountain("fm1", w, h, 914), "#8FD0E2",
          head="Help Thou Mine Unbelief"),
        F([cp("9:17", to="answered him,"), sy("9:17", frm="Teacher,"), sy("9:18")], FATHER_BOY, bg=COLD),
        F([cp("9:19", to="and saith,"), sy("9:19", frm="O faithless")], JESUS_STERN, bg=RED),
        D([cp("9:20")], lambda w, h: A.crowd_ring("cr1", w, h, 920, tone="grey"), "#6A6A7A"),
        F([cp("9:21", to="his father,"), sy("9:21", frm="How long", to="unto him?")], JESUS),
        F([cp("9:21", frm="And he said,", to="And he said,"), sy("9:21", frm="From a child."), sy("9:22")], FATHER_BOY, bg=COLD),
        F([cp("9:23", to="said unto him,"), sy("9:23", frm="If thou canst!")], JESUS),
        F([cp("9:24", to="and said,"), sy("9:24", frm="I believe;")], FATHER_BOY, bg=COLD),
        F([cp("9:25", to="saying unto him,"), sy("9:25", frm="Thou dumb")], JESUS_STERN, bg=RED),
        D([cp("9:26", to="part said,"), sy("9:26", frm="He is dead.")], lambda w, h: A.crowd_ring("cr2", w, h, 926), "#8FD0E2"),
        D([cp("9:27")], lambda w, h: A.boy_healed("bh1", w, h, 927, kneeling=False), "#8FD0E2"),
        F([cp("9:28", to="privately,"), sy("9:28", frm="How is it"), cp("9:29", to="said unto them,"), sy("9:29", frm="This kind")], JESUS_TEACH)]
PG.extend(K.pack(SEGS, "MRK-C05-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE LAST SHALL BE FIRST")))
