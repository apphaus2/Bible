"""John volume, Chapter 5 — The Good Shepherd (John 9–10). Every verse, word for word from ref/eng-asv.
The man blind from his birth sitting by the way; the disciples' question; the clay — Jesus' hand to his brow, nothing more;
the pool of Siloam, and he came seeing; the neighbours; before the Pharisees, his blind eyes closed and pale beside his
face before, open after; his father and mother afraid; whereas I was blind, now I see; cast out at the gate; Jesus finding
him by the shut synagogue door; Lord, I believe. The fold of the sheep: the thief's ladder against the wall in the night,
no one on it; the porter and the shepherd at the door, the sheep following him; the stranger they flee from; I am the door
— Jesus in the doorway; I am the good shepherd — a lamb on his shoulders; the hireling running and the wolf at the trees'
edge, no harm drawn; one flock, one shepherd. The feast of the dedication in winter in Solomon's porch; I and the Father
are one; the stones taken up and held; beyond the Jordan."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art5 as A, ch04 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        JESUS_GRIEF, JEW, CROWD, PHARISEE, SEEING, SEEING_BOLD, PARENT, MOTHER_BL)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C05-00-Title", "Chapter 5 · The Good Shepherd", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#5A4A7A"></rect><g transform="translate(0 180)">{A.good_shepherd("t5", 760, 720, 901)}</g>'
           '<rect x="0" y="899" width="760" height="181" fill="#8AAA4A"></rect>')
    return title(5, "The Good Shepherd", "John 9 – 10", svg, "#5A4A7A", v("10:11", frm="I am the good shepherd:", to="good shepherd:"))


SEGS = [D([cp("9:1"), said("9:2", "saying,", "Rabbi,")], lambda w, h: A.beggar_way("bw1", w, h, 902), "#8FD0E2", head="A Man Blind from His Birth", sky=9, art_h=240),
        F([said("9:3", "Jesus answered,", "Neither did"), sy("9:4"), sy("9:5")], JESUS_TEACH),
        D([cp("9:6"), cp("9:7", to="said unto him,"), sy("9:7", frm="Go, wash", to="Sent).")], lambda w, h: A.beggar_way("bw2", w, h, 903, stage="anoint"), "#8FD0E2",
          art_h=240),
        D([cp("9:7", frm="He went away")], lambda w, h: A.siloam("si1", w, h, 904, seeing=True), "#8FD0E2", art_h=260),
        D([cp("9:8", to="was a beggar, said,"), sy("9:8", frm="Is not this"), cp("9:9", to="Others said,"), sy("9:9", frm="It is he:", to="It is he:"),
           cp("9:9", frm="others said,", to="others said,"), sy("9:9", frm="No, but", to="like him."), cp("9:9", frm="He said,", to="He said,"), sy("9:9", frm="I am he.")],
          lambda w, h: A.beggar_way("bw3", w, h, 905, stage="neighbours"), "#8FD0E2", head="I Am He"),
        F([said("9:10", "unto him,", "How then")], CROWD),
        F([said("9:11", "He answered,", "The man")], SEEING),
        D([cp("9:12", to="said unto him,"), sy("9:12", frm="Where is he?", to="Where is he?"), cp("9:12", frm="He saith,", to="He saith,"), sy("9:12", frm="I know not.")],
          lambda w, h: A.beggar_way("bw4", w, h, 906, stage="neighbours"), "#8FD0E2"),
        D([cp("9:13"), cp("9:14")], lambda w, h: A.pharisees_court("pc1", w, h, 907), "#8FD0E2", head="Before the Pharisees"),
        F([cp("9:15", to="said unto them,"), sy("9:15", frm="He put clay")], SEEING),
        F([cp("9:16", to="Pharisees said,"), sy("9:16", frm="This man is not", to="the sabbath."), cp("9:16", frm="But others said,", to="others said,"),
           sy("9:16", frm="How can", to="such signs?"), cp("9:16", frm="And there was")], PHARISEE, bg=RED),
        F([cp("9:17", to="again,"), sy("9:17", frm="What sayest", to="thine eyes?")], PHARISEE, bg=RED),
        F([cp("9:17", frm="And he said,", to="And he said,"), sy("9:17", frm="He is a prophet.")], SEEING),
        D([cp("9:18"), cp("9:19", to="saying,"), sy("9:19", frm="Is this your son,")], lambda w, h: A.pharisees_court("pc2", w, h, 908, who="parents"), "#8FD0E2"),
        F([said("9:20", "answered and said,", "We know"), sy("9:21")], PARENT, bg=COLD),
        F([cp("9:22"), cp("9:23", to="his parents,"), sy("9:23", frm="He is of age;")], MOTHER_BL, bg=COLD),
        F([cp("9:24", to="said unto him,"), sy("9:24", frm="Give glory")], PHARISEE, bg=RED, head="Now I See"),
        F([said("9:25", "He therefore answered,", "Whether")], SEEING),
        F([said("9:26", "said therefore unto him,", "What did he")], PHARISEE, bg=RED),
        F([said("9:27", "He answered them,", "I told you")], SEEING_BOLD),
        F([said("9:28", "and said,", "Thou art his"), sy("9:29")], PHARISEE, bg=RED),
        F([said("9:30", "answered and said unto them,", "Why,"), sy("9:31"), sy("9:32"), sy("9:33")], SEEING_BOLD),
        D([cp("9:34", to="said unto him,"), sy("9:34", frm="Thou wast", to="teach us?"), cp("9:34", frm="And they cast")],
          lambda w, h: A.pharisees_court("pc3", w, h, 909, who="cast"), "#8FD0E2"),
        D([cp("9:35", to="he said,"), sy("9:35", frm="Dost thou")], lambda w, h: A.found_him("fh1", w, h, 910), "#5A4A7A", head="Lord, I Believe", art_h=240),
        F([said("9:36", "answered and said,", "And who")], SEEING),
        F([said("9:37", "said unto him,", "Thou hast both")], JESUS),
        D([cp("9:38", to="And he said,"), sy("9:38", frm="Lord, I believe.", to="I believe."), cp("9:38", frm="And he worshipped")],
          lambda w, h: A.found_him("fh2", w, h, 911, worship=True), "#5A4A7A", art_h=240),
        F([said("9:39", "And Jesus said,", "For judgment")], JESUS_TEACH),
        F([said("9:40", "said unto him,", "Are we also")], PHARISEE, bg=RED),
        F([said("9:41", "said unto them,", "If ye were")], JESUS_STERN, bg=RED),
        # John 10
        D([sy("10:1")], lambda w, h: A.sheepfold("sf1", w, h, 1001, stage="thief"), "#05051A", head="The Door of the Sheep", sky=10, art_h=260),
        D([sy("10:2"), sy("10:3")], lambda w, h: A.sheepfold("sf2", w, h, 1002, stage="door"), "#3A3A7A", art_h=260),
        D([sy("10:4")], lambda w, h: A.sheepfold("sf3", w, h, 1003, stage="lead"), "#8FD0E2", art_h=240),
        D([sy("10:5")], lambda w, h: A.sheepfold("sf4", w, h, 1004, stage="stranger"), "#8FD0E2", art_h=220),
        F([cp("10:6"), said("10:7", "said unto them again,", "Verily,")], JESUS_TEACH),
        D([sy("10:8"), sy("10:9")], lambda w, h: A.sheepfold("sf5", w, h, 1005, stage="jesus"), "#3A3A7A", art_h=260),
        F([sy("10:10")], JESUS),
        D([sy("10:11")], lambda w, h: A.good_shepherd("gs1", w, h, 1006), "#5A4A7A", head="I Am the Good Shepherd", art_h=300),
        D([sy("10:12"), sy("10:13")], lambda w, h: A.hireling("hl1", w, h, 1007), "#3A2A4A", art_h=240),
        F([sy("10:14"), sy("10:15")], JESUS_TEACH),
        D([sy("10:16")], lambda w, h: A.one_flock("of1", w, h, 1008), "#8FD0E2", art_h=260),
        F([sy("10:17"), sy("10:18")], JESUS_GRIEF, bg=COLD),
        F([cp("10:19"), said("10:20", "many of them said,", "He hath"), cp("10:21", to="Others said,"), sy("10:21", frm="These are not")], JEW, bg=RED),
        D([cp("10:22"), cp("10:23"), cp("10:24", to="said unto him,"), sy("10:24", frm="How long")], lambda w, h: A.solomons_porch("sp1", w, h, 1009), "#5A6A7A",
          head="I and the Father Are One", art_h=240),
        F([said("10:25", "Jesus answered them,", "I told you,"), sy("10:26")], JESUS_TEACH),
        D([sy("10:27"), sy("10:28")], lambda w, h: A.sheepfold("sf6", w, h, 1010, stage="lead"), "#8FD0E2", art_h=240),
        F([sy("10:29"), sy("10:30")], JESUS),
        D([cp("10:31"), said("10:32", "Jesus answered them,", "Many good")], lambda w, h: A.solomons_porch("sp2", w, h, 1011, stones_=True), "#5A6A7A", art_h=240),
        F([said("10:33", "answered him,", "For a good")], JEW, bg=RED),
        F([cp("10:34", to="answered them,"), sy("10:34", frm="Is it not written", to="I said,"), sg("10:34", frm="Ye are gods?"), sy("10:35"), sy("10:36")], JESUS_TEACH),
        F([sy("10:37"), sy("10:38")], JESUS),
        D([cp("10:39"), cp("10:40"), cp("10:41", to="and they said,"), sy("10:41", frm="John indeed"), cp("10:42")],
          lambda w, h: A.jordan("jd2", w, h, 1012, jesus_=True, john=False, crowd_n=7), "#8FD0E2", head="Beyond the Jordan", art_h=240)]
PG.extend(K.pack(SEGS, "JHN-C05-D", PG.next(), end=nxt("NEXT · LAZARUS, COME FORTH")))
