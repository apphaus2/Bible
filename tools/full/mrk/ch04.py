"""Mark volume, Chapter 4 — It Is I (Mark 6:30–7:37). Every verse, word for word from ref/eng-asv.
The apostles come back; the boat to a desert place and the people running round the shore on foot; sheep not having a
shepherd, the multitude on the hillside; the disciples' word and the two hundred shillings' worth; the companies on the
green grass in ranks by hundreds and by fifties, seen from the hill; the loaves blessed and broken; twelve basketfuls.
The mountain at nightfall; the boat distressed in rowing, Jesus walking on the sea in the fourth watch, the cry of a ghost,
It is I; the calm; Gennesaret and the sick laid in the marketplaces. The Pharisees and the scribes from Jerusalem over the
disciples at bread; the cups and pots and brasen vessels of the washings; Isaiah's words in song boxes beside Jesus' stern
face; Moses' commandment in the Voice box; Corban; the things that defile, beside his face. The borders of Tyre and Sidon:
the house that could not be hid; the Syrophœnician woman (Matthew's Canaanitish woman's looks) and the little dogs under
the table; the child found laid upon the bed, at peace (the demon is never drawn). The deaf man taken aside — Ephphatha."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art4 as A, ch03 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, ANDREW, PHILIP, PHARISEE, SCRIBE_STERN, CANAANITE, DEAF, CROWD_MAN)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C04-00-Title", "Chapter 4 · It Is I", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 300)">{A.on_the_sea("t4", 760, 780, 648)}</g>'
    return title(4, "It Is I", "Mark 6:30 – 7:37", svg, "#0B0B2A", v("6:50", frm="Be of good cheer:"))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [F([cp("6:30"), cp("6:31", to="saith unto them,"), sy("6:31", frm="Come ye"), cp("6:31", frm="For there were")], JESUS, head="Sheep Not Having a Shepherd"),
        D([cp("6:32"), cp("6:33")], lambda w, h: A.desert_place("dp1", w, h, 632), "#8FD0E2"),
        D([cp("6:34")], lambda w, h: A.hillside("hs1", w, h, 634), "#8FD0E2"),
        F([cp("6:35", to="and said,"), sy("6:35", frm="The place is desert,"), sy("6:36")], ANDREW, head="Five Loaves, and Two Fishes"),
        F([cp("6:37", to="said unto them,"), sy("6:37", frm="Give ye them", to="to eat."), cp("6:37", frm="And they say", to="unto him,"), sy("6:37", frm="Shall we go")],
          JESUS, h=320),
        F([cp("6:38", to="saith unto them,"), sy("6:38", frm="How many", to="go and see."), cp("6:38", frm="And when they knew,", to="they say,"), sy("6:38", frm="Five,")],
          PHILIP, h=300),
        D([cp("6:39"), cp("6:40")], lambda w, h: A.companies("cm1", w, h, 639), "#5A7AB0", head="By Hundreds, and by Fifties", art_h=280),
        D([cp("6:41")], lambda w, h: A.five_loaves("fl1", w, h, 641), "#5A3A6A", art_h=240),
        D([cp("6:42"), cp("6:43"), cp("6:44")], lambda w, h: A.baskets("bk1", w, h, 642), "#3A2A5A"),
        D([cp("6:45"), cp("6:46"), cp("6:47")], lambda w, h: A.mount_alone("ma1", w, h, 645), NIGHT, head="Be Not Afraid"),
        D([cp("6:48"), cp("6:49")], lambda w, h: A.on_the_sea("os1", w, h, 648), "#0B0B2A", art_h=240),
        F([cp("6:50", to="saith unto them,"), sy("6:50", frm="Be of good cheer:")], JESUS, bg=COLD),
        D([cp("6:51"), cp("6:52")], lambda w, h: A.on_the_sea("os2", w, h, 651, calm=True), "#2A2A6A"),
        D([cp("6:53"), cp("6:54"), cp("6:55"), cp("6:56")], lambda w, h: A.gennesaret("gn1", w, h, 653), "#8FD0E2", art_h=220),
        # Mark 7
        D([cp("7:1"), cp("7:2")], lambda w, h: A.unwashed("uw1", w, h, 701), "#8FD0E2", head="The Tradition of the Elders", stamp=7),
        D([cp("7:3"), cp("7:4")], lambda w, h: A.cups_pots("cu1", w, h, 703), "#C8B490"),
        F([cp("7:5", to="ask him,"), sy("7:5", frm="Why walk not")], PHARISEE, bg=RED),
        F([cp("7:6", to="as it is written,"), sg("7:6", frm="This people"), sg("7:7"), sy("7:8")], JESUS_STERN, bg=RED),
        F([cp("7:9", to="said unto them,"), sy("7:9", frm="Full well"), sy("7:10", to="Moses said,"), gd("7:10", frm="Honor thy father"), sy("7:11"), sy("7:12"), sy("7:13")],
          JESUS_STERN, bg=RED),
        F([cp("7:14", to="said unto them,"), sy("7:14", frm="Hear me"), sy("7:15")], JESUS_TEACH, head="That Which Proceedeth out of the Man"),
        F([cp("7:17"), cp("7:18", to="saith unto them,"), sy("7:18", frm="Are ye so"), sy("7:19", to="into the draught?"), cp("7:19", frm="This he said,")], JESUS_TEACH),
        F([cp("7:20", to="And he said,"), sy("7:20", frm="That which"), sy("7:21"), sy("7:22"), sy("7:23")], JESUS_STERN, bg=RED),
        D([cp("7:24")], lambda w, h: A.house_tyre("ht1", w, h, 724), "#4A3A6A", head="Even the Dogs under the Table"),
        D([cp("7:25"), cp("7:26")], lambda w, h: A.tyre("ty1", w, h, 725), "#8FD0E2"),
        F([cp("7:27", to="said unto her,"), sy("7:27", frm="Let the children")], JESUS),
        D([cp("7:28", to="saith unto him,"), sy("7:28", frm="Yea, Lord;")], lambda w, h: A.crumbs("cr1", w, h, 728), "#C8A878"),
        F([cp("7:29", to="said unto her,"), sy("7:29", frm="For this saying")], JESUS),
        D([cp("7:30")], lambda w, h: A.child_bed("cb1", w, h, 730), "#C8A08A"),
        D([cp("7:31"), cp("7:32")], lambda w, h: A.decapolis("dc1", w, h, 731, jesus_=True), "#8FD0E2", head="Ephphatha"),
        D([cp("7:33"), cp("7:34", to="saith unto him,"), sy("7:34", frm="Ephphatha,", to="Ephphatha,"), cp("7:34", frm="that is,", to="that is,"), sy("7:34", frm="Be opened.")],
          lambda w, h: A.ephphatha("ep1", w, h, 733), "#8FD0E2", art_h=240),
        F([cp("7:35")], DEAF),
        D([cp("7:36"), cp("7:37", to="saying,"), sy("7:37", frm="He hath done")], lambda w, h: A.multitudes("mt1", w, h, 736, sick=False), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MRK-C04-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THOU ART THE CHRIST")))
