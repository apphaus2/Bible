"""John volume, Chapter 4 — Before Abraham Was (John 7–8). Every verse, word for word from ref/eng-asv; 7:53–8:11 kept
in full as the ASV prints it, in its brackets.
Galilee and his brethren; Jerusalem at the feast of tabernacles, its roofs and streets full of booths of branches, Jesus
going up in secret; the murmuring of the multitudes; teaching in the temple court; the officers sent to take him; the last
great day — rivers of living water, the dry hills greening under them; the division, the officers before the chief priests
(Never man so spake), Nicodemus. The woman taken in adultery: she only at a distance, veiled, set in the midst; Jesus
stooping and writing on the ground; the stones laid down as the accusers go out one by one; Neither do I condemn thee —
nothing more drawn. The light of the world: the golden lampstands of the court blazing over the night city; the treasury;
the long dispute beside the faces (the devil, 8:44, is words only); the broken fetters on the threshold of an open door;
Abraham under the stars; Before Abraham was born, I am; and the stones taken up in the porch as Jesus goes out of the
temple."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art4 as A, ch03 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        JESUS_GRIEF, JEW, CROWD, BROTHER, PHARISEE, OFFICER, NICODEMUS_DAY)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C04-00-Title", "Chapter 4 · Before Abraham Was", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 200)">{A.abraham_night("t4", 760, 700, 701)}</g>'
           '<rect x="0" y="899" width="760" height="181" fill="#14142E"></rect>')
    return title(4, "Before Abraham Was", "John 7 – 8", svg, "#05051A", v("8:58", frm="Before Abraham was born, I am."))


SEGS = [D([cp("7:1"), cp("7:2"), said("7:3", "said unto him,", "Depart hence,"), sy("7:4")], lambda w, h: A.brethren("br1", w, h, 702), "#8FD0E2", art_h=320,
          head="The Feast of Tabernacles", sky=7),
        F([cp("7:5"), said("7:6", "saith unto them,", "My time"), sy("7:7"), sy("7:8")], JESUS),
        D([cp("7:9"), cp("7:10")], lambda w, h: A.booths("bo1", w, h, 703, secret=True), "#8FD0E2", art_h=240),
        D([cp("7:11", to="and said,"), sy("7:11", frm="Where is he?"), cp("7:12", to="some said,"), sy("7:12", frm="He is a good man;", to="good man;"),
           cp("7:12", frm="others said,", to="others said,"), sy("7:12", frm="Not so,"), cp("7:13")], lambda w, h: A.booths("bo2", w, h, 704), "#8FD0E2"),
        D([cp("7:14"), said("7:15", "saying,", "How knoweth")], lambda w, h: A.temple_teach("tt1", w, h, 705), "#8FD0E2", head="My Teaching Is Not Mine"),
        F([said("7:16", "and said,", "My teaching"), sy("7:17"), sy("7:18")], JESUS_TEACH),
        F([sy("7:19")], JESUS_STERN, bg=RED),
        F([said("7:20", "The multitude answered,", "Thou hast")], CROWD, bg=RED),
        F([said("7:21", "said unto them,", "I did one"), sy("7:22"), sy("7:23"), sy("7:24")], JESUS_TEACH),
        F([said("7:25", "of Jerusalem said,", "Is not this"), sy("7:26"), sy("7:27")], CROWD),
        D([said("7:28", "teaching and saying,", "Ye both know"), sy("7:29")], lambda w, h: A.temple_teach("tt2", w, h, 706, stage="stand"), "#8FD0E2"),
        D([cp("7:30"), said("7:31", "and they said,", "When the Christ"), cp("7:32")], lambda w, h: A.temple_teach("tt3", w, h, 707, stage="officers"), "#8FD0E2",
          head="Officers to Take Him"),
        F([said("7:33", "Jesus therefore said,", "Yet a little"), sy("7:34")], JESUS_GRIEF, bg=COLD),
        F([said("7:35", "among themselves,", "Whither"), sy("7:36")], JEW, bg=RED),
        D([cp("7:37", to="cried, saying,"), sy("7:37", frm="If any man"), sy("7:38"), cp("7:39")], lambda w, h: A.living_water("lw1", w, h, 708), "#8FD0E2",
          head="Rivers of Living Water", art_h=260),
        F([cp("7:40", to="said,"), sy("7:40", frm="This is of a truth"), cp("7:41", to="Others said,"), sy("7:41", frm="This is the Christ.", to="the Christ."),
           cp("7:41", frm="But some said,", to="some said,"), sy("7:41", frm="What,"), sy("7:42")], CROWD),
        D([cp("7:43"), cp("7:44")], lambda w, h: A.temple_teach("tt4", w, h, 709, stage="officers"), "#8FD0E2"),
        F([cp("7:45", to="said unto them,"), sy("7:45", frm="Why did ye")], PHARISEE, bg=RED, head="Never Man So Spake"),
        F([said("7:46", "The officers answered,", "Never man")], OFFICER, bg=COLD),
        F([said("7:47", "answered them,", "Are ye also"), sy("7:48"), sy("7:49")], PHARISEE, bg=RED),
        F([cp("7:50"), sy("7:51")], NICODEMUS_DAY),
        F([said("7:52", "said unto him,", "Art thou also")], PHARISEE, bg=RED),
        D([cp("7:53"), cp("8:1")], lambda w, h: A.olivet_night("on1", w, h, 801), "#0B0B2A", head="Neither Do I Condemn Thee", sky=8),
        D([cp("8:2")], lambda w, h: A.temple_teach("tt5", w, h, 802), "#8FD0E2"),
        D([cp("8:3"), said("8:4", "they say unto him,", "Teacher,"), sy("8:5")], lambda w, h: A.taken_woman("tw1", w, h, 803), "#5A6A9A", art_h=260),
        D([cp("8:6")], lambda w, h: A.taken_woman("tw2", w, h, 804, stage="write"), "#5A6A9A", art_h=260),
        F([said("8:7", "said unto them,", "He that is without")], JESUS_TEACH),
        D([cp("8:8"), cp("8:9")], lambda w, h: A.taken_woman("tw3", w, h, 805, stage="gone"), "#5A6A9A", art_h=240),
        D([cp("8:10", to="said unto her,"), sy("8:10", frm="Woman,"), cp("8:11", to="And she said,"), sy("8:11", frm="No man, Lord.", to="No man, Lord."),
           cp("8:11", frm="And Jesus said,", to="And Jesus said,"), sy("8:11", frm="Neither do I")], lambda w, h: A.taken_woman("tw4", w, h, 806, stage="alone"), "#5A6A9A",
          art_h=260),
        D([said("8:12", "saying,", "I am the light")], lambda w, h: A.temple_lamps("tl1", w, h, 807), "#05051A", head="The Light of the World", art_h=300),
        F([said("8:13", "said unto him,", "Thou bearest")], PHARISEE, bg=RED),
        F([said("8:14", "said unto them,", "Even if"), sy("8:15"), sy("8:16")], JESUS_TEACH),
        F([sy("8:17"), sy("8:18")], JESUS),
        F([cp("8:19", to="said therefore unto him,"), sy("8:19", frm="Where is thy Father?", to="thy Father?")], PHARISEE, bg=RED),
        F([cp("8:19", frm="Jesus answered,", to="Jesus answered,"), sy("8:19", frm="Ye know neither")], JESUS_TEACH),
        D([cp("8:20")], lambda w, h: A.treasury("ty1", w, h, 808, widow=False, rich=False), "#C8B490"),
        F([said("8:21", "again unto them,", "I go away,")], JESUS_GRIEF, bg=COLD, head="I Am from Above"),
        F([said("8:22", "therefore said,", "Will he")], JEW, bg=RED),
        F([said("8:23", "said unto them,", "Ye are from"), sy("8:24")], JESUS_STERN, bg=RED),
        F([cp("8:25", to="unto him,"), sy("8:25", frm="Who art thou?", to="Who art thou?")], JEW, bg=RED),
        F([cp("8:25", frm="Jesus said", to="unto them,"), sy("8:25", frm="Even that"), sy("8:26")], JESUS_TEACH),
        F([cp("8:27"), said("8:28", "Jesus therefore said,", "When ye have"), sy("8:29")], JESUS_GRIEF, bg=COLD),
        D([cp("8:30"), said("8:31", "believed him,", "If ye abide"), sy("8:32")], lambda w, h: A.freed("fr1", w, h, 809), "#2A2228", head="The Truth Shall Make You Free"),
        F([said("8:33", "answered unto him,", "We are")], JEW, bg=RED),
        F([said("8:34", "answered them,", "Verily,"), sy("8:35"), sy("8:36")], JESUS),
        F([sy("8:37"), sy("8:38")], JESUS_STERN),
        F([cp("8:39", to="said unto him,"), sy("8:39", frm="Our father is Abraham.", to="is Abraham.")], JEW, bg=RED),
        F([cp("8:39", frm="Jesus saith", to="unto them,"), sy("8:39", frm="If ye were"), sy("8:40"), sy("8:41", to="your father.")], JESUS_TEACH),
        F([cp("8:41", frm="They said unto him,", to="unto him,"), sy("8:41", frm="We were not")], JEW, bg=RED),
        F([said("8:42", "said unto them,", "If God"), sy("8:43")], JESUS_TEACH),
        D([sy("8:44")], lambda w, h: A.wilderness("wn1", w, h, 812, john=False, tone="night"), "#0B0B2A", art_h=200),
        F([sy("8:45"), sy("8:46"), sy("8:47")], JESUS_STERN),
        F([said("8:48", "said unto him,", "Say we not")], JEW, bg=RED, head="Before Abraham Was"),
        F([said("8:49", "Jesus answered,", "I have not"), sy("8:50"), sy("8:51")], JESUS),
        F([said("8:52", "said unto him,", "Now we know"), sy("8:53")], JEW, bg=RED),
        F([said("8:54", "Jesus answered,", "If I glorify"), sy("8:55")], JESUS_TEACH),
        D([sy("8:56")], lambda w, h: A.abraham_night("an1", w, h, 810), "#05051A", art_h=260),
        F([said("8:57", "said unto him,", "Thou art not")], JEW, bg=RED),
        F([said("8:58", "said unto them,", "Verily,")], JESUS),
        D([cp("8:59")], lambda w, h: A.stones_up("su1", w, h, 811), "#5A4A6A", art_h=260)]
PG.extend(K.pack(SEGS, "JHN-C04-D", PG.next(), end=nxt("NEXT · THE GOOD SHEPHERD")))
