"""Mark volume, Chapter 2 — Peace, Be Still (Mark 3–4). Every verse, word for word from ref/eng-asv.
The withered hand in the synagogue, the Pharisees watching along the wall, then the hand stretched forth; the Pharisees and
the Herodians taking counsel at dusk. The multitude from every country, drawn as a plan of the land with a road in from
each; the press on the beach and the little boat waiting; the unclean spirits' cry beside Jesus' stern face (never drawn).
The twelve on the mountain, named beneath their figures in Mark's order. The house where they could not eat bread; the
scribes from Jerusalem; a kingdom and a house divided beside his face; the strong man's house; his mother and his brethren
at the door. Then by the sea: the boat a little off shore, the sower and the four grounds, each ground again close up as he
expounds it; the lamp on the stand; the measure; the seed growing secretly from night to day, the blade, the ear and the
full grain, the sickle ready; the mustard tree; and the evening crossing — the great storm, Jesus asleep on the cushion in
the stern, then standing over the waves, then the great calm."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art2 as A, ch01 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        SCRIBE_STERN, PETER)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("MRK-C02-00-Title", "Chapter 2 · Peace, Be Still", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#14141E"></rect><g transform="translate(0 300)">{A.tempest("t2", 760, 780, 401, awake=True)}</g>'
    return title(2, "Peace, Be Still", "Mark 3 – 4", svg, "#14141E", v("4:39", frm="Peace, be still.", to="Peace, be still."))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("3:1"), cp("3:2")], lambda w, h: A.withered("wh1", w, h, 301), "#C8B490", head="Stretch Forth Thy Hand", sky=3),
        F([cp("3:3", to="hand withered,"), sy("3:3", frm="Stand forth."), cp("3:4", to="unto them,"), sy("3:4", frm="Is it lawful", to="or to kill?"),
           cp("3:4", frm="But they held")], JESUS_STERN, bg=RED),
        D([cp("3:5", to="unto the man,"), sy("3:5", frm="Stretch forth", to="thy hand."), cp("3:5", frm="And he stretched")], lambda w, h: A.withered("wh2", w, h, 302, restored=True),
          "#C8B490"),
        D([cp("3:6")], lambda w, h: A.counsel("cn1", w, h, 303), "#2A1A3A"),
        D([cp("3:7"), cp("3:8")], lambda w, h: A.whence(w, h, 304), MAP, head="A Great Multitude", art_h=300),
        D([cp("3:9"), cp("3:10"), cp("3:11", to="saying,"), sy("3:11", frm="Thou art the Son")], lambda w, h: A.gennesaret("gn1", w, h, 305), "#8FD0E2"),
        F([cp("3:12")], JESUS_STERN, bg=RED),
        D([cp("3:13"), cp("3:14"), cp("3:15"), cp("3:16"), cp("3:17"), cp("3:18"), cp("3:19", to="betrayed him.")], lambda w, h: A.twelve_mark("tw1", w, h, 306), MAP,
          head="He Appointed Twelve", art_h=300),
        D([cp("3:19", frm="And he cometh"), cp("3:20"), cp("3:21", to="for they said,"), sy("3:21", frm="He is beside")], lambda w, h: A.door_crowd("dc2", w, h, 307), "#8FD0E2",
          head="A House Divided"),
        F([cp("3:22", to="said,"), sy("3:22", frm="He hath Beelzebub")], SCRIBE_STERN, bg=RED),
        F([cp("3:23", to="in parables,"), sy("3:23", frm="How can Satan"), sy("3:24"), sy("3:25"), sy("3:26")], JESUS_STERN, bg=RED),
        D([sy("3:27")], lambda w, h: A.strong_house("sh1", w, h, 308), "#3A2A3A"),
        F([sy("3:28"), sy("3:29"), cp("3:30")], JESUS_STERN, bg=RED),
        D([cp("3:31"), cp("3:32", to="say unto him,"), sy("3:32", frm="Behold, thy mother")], lambda w, h: A.kindred("kd1", w, h, 309), "#C8A878", head="My Mother and My Brethren"),
        F([cp("3:33", to="and saith,"), sy("3:33", frm="Who is my"), cp("3:34", to="he saith,"), sy("3:34", frm="Behold, my mother"), sy("3:35")], JESUS),
        # Mark 4
        D([cp("4:1"), cp("4:2")], lambda w, h: A.boat_preach("bp1", w, h, 401), "#8FD0E2", head="Behold, the Sower Went Forth", stamp=4),
        D(S("4:3", 8), lambda w, h: A.sower("sw1", w, h, 402), "#8FD0E2", art_h=260),
        F([cp("4:9", to="And he said,"), sy("4:9", frm="Who hath ears")], JESUS),
        D([cp("4:10"), cp("4:11", to="said unto them,"), sy("4:11", frm="Unto you"), sy("4:12")], lambda w, h: A.eyes_ears("ee1", w, h, 403), "#4A2A5A"),
        F([cp("4:13", to="saith unto them,"), sy("4:13", frm="Know ye not"), sy("4:14")], JESUS_TEACH, head="The Sower Soweth the Word"),
        D([sy("4:15")], lambda w, h: A.ground_close("gw1", w, h, 404, "way"), "#8FD0E2"),
        D([sy("4:16"), sy("4:17")], lambda w, h: A.ground_close("gr1", w, h, 405, "rocky"), "#FFD89A"),
        D([sy("4:18"), sy("4:19")], lambda w, h: A.ground_close("gt1", w, h, 406, "thorns"), "#8FD0E2"),
        D([sy("4:20")], lambda w, h: A.ground_close("gg1", w, h, 407, "good"), "#8FD0E2"),
        D([cp("4:21", to="unto them,"), sy("4:21", frm="Is the lamp"), sy("4:22"), sy("4:23")], lambda w, h: A.city_light("cl1", w, h, 408), "#0B0B2A", head="The Lamp on the Stand"),
        F([cp("4:24", to="unto them,"), sy("4:24", frm="Take heed"), sy("4:25")], JESUS_TEACH),
        D([cp("4:26", to="And he said,"), sy("4:26", frm="So is the kingdom"), sy("4:27"), sy("4:28"), sy("4:29")], lambda w, h: A.seed_secretly("ss1", w, h, 409), "#5A4A8A",
          head="The Seed Should Spring Up", art_h=220),
        D([cp("4:30", to="And he said,"), sy("4:30", frm="How shall we"), sy("4:31"), sy("4:32")], lambda w, h: A.mustard("ms1", w, h, 410), "#8FD0E2"),
        F([cp("4:33"), cp("4:34")], JESUS_TEACH),
        D([cp("4:35", to="saith unto them,"), sy("4:35", frm="Let us go"), cp("4:36")], lambda w, h: A.galilee("gl1", w, h, 411, town=False, tone="dusk"), "#4A2A5A",
          head="Peace, Be Still"),
        D([cp("4:37"), cp("4:38", to="say unto him,"), sy("4:38", frm="Teacher, carest")], lambda w, h: A.tempest("tp1", w, h, 412), "#14141E", art_h=240),
        D([cp("4:39", to="unto the sea,"), sy("4:39", frm="Peace, be still.", to="be still."), cp("4:39", frm="And the wind ceased")], lambda w, h: A.tempest("tp2", w, h, 413, awake=True),
          "#14141E", art_h=240),
        F([cp("4:40", to="unto them,"), sy("4:40", frm="Why are ye")], JESUS),
        D([cp("4:41", to="one to another,"), sy("4:41", frm="Who then is this")], lambda w, h: A.tempest("tp3", w, h, 414, calm=True), "#5AB0D8", art_h=240)]
PG.extend(K.pack(SEGS, "MRK-C02-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · TALITHA CUMI")))
