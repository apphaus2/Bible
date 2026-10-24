"""Mark volume, Chapter 1 — The Beginning of the Gospel (Mark 1–2). Every verse, word for word from ref/eng-asv.
John crying in the wilderness, the prophets' words in song boxes; all Judæa going out to the Jordan; John's face, clothed
with camel's hair; Jesus coming down to the water; the heavens rent, the Spirit as a dove of light and the Father's voice
in the Voice box over the light. The forty days: Jesus alone in the night wilderness, the wild beasts dark on the ridges,
the angels of white light ministering (Satan never drawn: "tempted of Satan" is words only). Galilee and the time
fulfilled; Simon and Andrew casting a net, James and John leaving Zebedee in the boat. The synagogue at Capernaum: the
unclean spirit is never drawn — its cry stands over the synagogue, the rebuke beside Jesus' stern face, and then the man
quiet and whole before him. Simon's wife's mother raised and serving; the city at the door at sunset; the desert place a
great while before day; the leper kneeling. Then the house at Capernaum crowded to the door, the roof broken up and the bed
let down on its cords, the scribes reasoning, the man walking out with his bed; Levi at the place of toll and the publicans
at meat; the bridegroom; the wine-skins; the grainfields on the sabbath."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art as A
from mrk.common import (K, Pages, D, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, BAPTIST, PHARISEE,
                        SCRIBE_STERN)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C01-00-Title", "Chapter 1 · The Beginning of the Gospel", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 300)">{A.heavens_rent("t1", 760, 640, 101)}</g><rect x="0" y="936" width="760" height="144" fill="#2C6A98"></rect>'
    return title(1, "The Beginning of the Gospel", "Mark 1 – 2", svg, "#1E1650", v("1:1"))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("1:1"), cp("1:2", to="the prophet,"), sg("1:2", frm="Behold, I send"), sg("1:3")], lambda w, h: A.wilderness("wl1", w, h, 102), "#FFD89A",
          head="The Voice in the Wilderness", stamp=1),
        D([cp("1:4"), cp("1:5")], lambda w, h: A.jordan("jd1", w, h, 103), "#8FD0E2"),
        F([cp("1:6")], BAPTIST),
        F([cp("1:7", to="saying,"), sy("1:7", frm="There cometh"), sy("1:8")], BAPTIST, bg=RED),
        D([cp("1:9")], lambda w, h: A.jordan("jd2", w, h, 104, jesus_=True, crowd_n=4), "#8FD0E2", head="Thou Art My Beloved Son"),
        D([cp("1:10"), cp("1:11", to="out of the heavens,"), gd("1:11", frm="Thou art")], lambda w, h: A.heavens_rent("ho1", w, h, 105), "#2A2A6A", art_h=240),
        D([cp("1:12"), cp("1:13")], lambda w, h: A.with_beasts("wb1", w, h, 106), NIGHT, head="With the Wild Beasts", art_h=260),
        D([cp("1:14"), cp("1:15", to="and saying,"), sy("1:15", frm="The time is")], lambda w, h: A.multitudes("mt1", w, h, 107, sick=False), "#8FD0E2",
          head="The Kingdom of God Is at Hand"),
        D([cp("1:16"), cp("1:17", to="said unto them,"), sy("1:17", frm="Come ye"), cp("1:18")], lambda w, h: A.fishers("fs1", w, h, 108), "#8FD0E2", head="Fishers of Men"),
        D([cp("1:19")], lambda w, h: A.zebedee("zb1", w, h, 109), "#8FD0E2"),
        D([cp("1:20")], lambda w, h: A.zebedee("zb2", w, h, 110, leaving=True), "#8FD0E2"),
        D([cp("1:21"), cp("1:22")], lambda w, h: A.synagogue("sy1", w, h, 111), "#C8B490", head="As One Having Authority"),
        D([cp("1:23"), cp("1:24", to="saying,"), sy("1:24", frm="What have we")], lambda w, h: A.synagogue("sy2", w, h, 112, crowd_n=10), "#5A4A6A"),
        F([cp("1:25", to="saying,"), sy("1:25", frm="Hold thy peace"), cp("1:26")], JESUS_STERN, bg=RED),
        D([cp("1:27", to="saying,"), sy("1:27", frm="What is this?"), cp("1:28")], lambda w, h: A.synagogue_peace("sp1", w, h, 113), "#C8B490", art_h=300),
        D([cp("1:29"), cp("1:30"), cp("1:31")], lambda w, h: A.fever("fv1", w, h, 114), "#B8987A", head="He Took Her by the Hand"),
        D([cp("1:32"), cp("1:33"), cp("1:34")], lambda w, h: A.at_even("ae1", w, h, 115), "#4A2A5A"),
        D([cp("1:35"), cp("1:36"), cp("1:37", to="say unto him,"), sy("1:37", frm="All are")], lambda w, h: A.before_day("bd1", w, h, 116, found=True), "#0B1A3A",
          head="A Great While Before Day"),
        F([cp("1:38", to="unto them,"), sy("1:38", frm="Let us go"), cp("1:39")], JESUS_TEACH),
        D([cp("1:40", to="saying unto him,"), sy("1:40", frm="If thou wilt")], lambda w, h: A.leper("lp1", w, h, 117), "#8FD0E2", head="If Thou Wilt"),
        F([cp("1:41", to="saith unto him,"), sy("1:41", frm="I will;"), cp("1:42")], JESUS),
        F([cp("1:43"), cp("1:44", to="saith unto him,"), sy("1:44", frm="See thou")], JESUS_TEACH),
        D([cp("1:45")], lambda w, h: A.multitudes("mt2", w, h, 118), "#8FD0E2"),
        # Mark 2
        D([cp("2:1"), cp("2:2")], lambda w, h: A.door_crowd("dc1", w, h, 201), "#8FD0E2", head="Thy Sins Are Forgiven", stamp=2),
        D([cp("2:3"), cp("2:4")], lambda w, h: A.roof_opened("ro1", w, h, 202), "#8FD0E2", art_h=240),
        D([cp("2:5", to="sick of the palsy,"), sy("2:5", frm="Son, thy sins")], lambda w, h: A.let_down("ld1", w, h, 203), "#B89A70", art_h=240),
        F([cp("2:6"), sy("2:7")], SCRIBE_STERN, bg=RED),
        F([cp("2:8", to="saith unto them,"), sy("2:8", frm="Why reason"), sy("2:9"), sy("2:10", to="forgive sins"), cp("2:10", frm="(he saith"), sy("2:11")]),
        D([cp("2:12", to="saying,"), sy("2:12", frm="We never saw")], lambda w, h: A.bed_carried("bc1", w, h, 204, rise=True), "#8FD0E2"),
        D([cp("2:13"), cp("2:14", to="saith unto him,"), sy("2:14", frm="Follow me.", to="Follow me."), cp("2:14", frm="And he arose")], lambda w, h: A.toll("tl1", w, h, 205),
          "#8FD0E2", head="Levi the Son of Alphæus"),
        D([cp("2:15"), cp("2:16", to="unto his disciples,"), sy("2:16", frm="How is it")], lambda w, h: A.at_meat("am1", w, h, 206, pharisees=True), "#8A6A4A"),
        F([cp("2:17", to="saith unto them,"), sy("2:17", frm="They that")]),
        F([cp("2:18", to="say unto him,"), sy("2:18", frm="Why do John")], PHARISEE, bg=RED, head="The Bridegroom"),
        F([cp("2:19", to="said unto them,"), sy("2:19", frm="Can the sons"), sy("2:20")], JESUS),
        D([sy("2:21"), sy("2:22")], lambda w, h: A.wineskins("ws1", w, h, 207), "#E8D8B8"),
        D([cp("2:23"), cp("2:24", to="said unto him,"), sy("2:24", frm="Behold,")], lambda w, h: A.grainfield("gf1", w, h, 208), "#D8B860", head="Lord of the Sabbath"),
        F([cp("2:25", to="said unto them,"), sy("2:25", frm="Did ye"), sy("2:26"), cp("2:27", to="said unto them,"), sy("2:27", frm="The sabbath"), sy("2:28")])]
PG.extend(K.pack(SEGS, "MRK-C01-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · PEACE, BE STILL")))
