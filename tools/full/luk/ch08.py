"""Luke volume, Chapter 8 — The Good Samaritan (Luke 10). Every verse, word for word from ref/eng-asv.
The seventy sent two and two on the roads to every city; the harvest plenteous; lambs among wolves; peace to this house;
the dust wiped off; woe unto Chorazin, Bethsaida and Capernaum. The seventy returned with joy; I beheld Satan fallen as
lightning from heaven — the lightning only, Satan never drawn; serpents and scorpions trodden; I thank thee, O Father. The
lawyer beside his face; what is written in the law? The parable of the good Samaritan on the road down to Jericho: the man
who fell among robbers is never drawn — his garments thrown down at the road's edge, the priest and the Levite passing by
on the other side, the Samaritan kneeling with his oil and wine, the man set on his beast wrapped in the red cloak, the inn
and the two shillings; Go, and do thou likewise. Martha and Mary: Mary at the Lord's feet, Martha cumbered about much
serving — Mary hath chosen the good part."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art6 as A, ch07 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, LAWYER, LAWYER_STERN, MARTHA, MARY_BETHANY)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C08-00-Title", "Chapter 8 · The Good Samaritan", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.jericho_road("t8", 760, 780, 1001, stage="beast")}</g>'
    return title(8, "The Good Samaritan", "Luke 10", svg, "#6A3A2A", v("10:37", frm="Go, and do thou likewise."))


SEGS = [D([cp("10:1"), N("10:2", "said unto them,")], lambda w, h: A.seventy("sv1", w, h, 1001), "#8FD0E2", head="The Seventy", sky=10, art_h=220),
        D([sy("10:3"), sy("10:4")], lambda w, h: A.sheep_wolves("sw1", w, h, 1002), "#4A3A5A"),
        D([sy("10:5"), sy("10:6"), sy("10:7")], lambda w, h: A.door_knock("dk1", w, h, 1003), "#2A2050"),
        D([sy("10:8"), sy("10:9"), sy("10:10"), sy("10:11"), sy("10:12")], lambda w, h: A.dust_gate("dg1", w, h, 1004), "#C8A890"),
        D([sy("10:13"), sy("10:14"), sy("10:15"), sy("10:16")], lambda w, h: A.woe("wo1", w, h, 1005), "#2A2A3A", head="Woe unto Thee, Chorazin!"),
        D([N("10:17", "with joy, saying,")], lambda w, h: A.seventy("sv2", w, h, 1006, back=True), "#8FD0E2", head="Your Names Are Written in Heaven"),
        D([N("10:18", "said unto them,")], lambda w, h: A.lightning_sky("ls1", w, h, 1007), "#14141E", art_h=240),
        D([sy("10:19"), sy("10:20")], lambda w, h: A.tread("tr1", w, h, 1008), "#C8A878"),
        F([N("10:21", "and said,"), sy("10:22")], JESUS_TEACH),
        F([N("10:23", "said privately,"), sy("10:24")], JESUS),
        F([N("10:25", "saying,")], LAWYER, bg=COLD, head="Who Is My Neighbor?"),
        F([N("10:26", "said unto him,")], JESUS),
        F([N("10:27", "answering said,")], LAWYER, bg=GOLDEN),
        F([N("10:28", "said unto him,")], JESUS),
        F([N("10:29", "said unto Jesus,")], LAWYER_STERN, bg=RED),
        D([N("10:30", "answer and said,")], lambda w, h: A.jericho_road("jr1", w, h, 1009), "#8FD0E2", head="A Certain Man Was Going Down to Jericho", art_h=240),
        D([sy("10:31")], lambda w, h: A.jericho_road("jr2", w, h, 1010, stage="priest"), "#8FD0E2", art_h=300),
        D([sy("10:32")], lambda w, h: A.jericho_road("jr3", w, h, 1011, stage="levite"), "#8FD0E2", art_h=300),
        D([sy("10:33"), sy("10:34", to="oil and wine;")], lambda w, h: A.jericho_road("jr4", w, h, 1012, stage="mercy"), "#8FD0E2", art_h=320),
        D([sy("10:34", frm="and he set him")], lambda w, h: A.jericho_road("jr5", w, h, 1013, stage="beast"), "#8FD0E2", art_h=240),
        D([sy("10:35")], lambda w, h: A.inn("in1", w, h, 1014), "#5A6A9A"),
        F([sy("10:36")], JESUS_TEACH),
        F((q37 := Q("10:37", "c", "And he said,", "s", "mercy on him.", "c", "said unto him,", "s"))[:2], LAWYER, bg=GOLDEN),
        F(q37[2:], JESUS, ref="LUKE 10:37"),
        D([cp("10:38"), cp("10:39")], lambda w, h: A.martha_house("mh1", w, h, 1015), "#B8987A", head="Martha, Martha", art_h=240),
        D([Q("10:40", "c", "and said,", "s")], lambda w, h: A.martha_house("mh2", w, h, 1016, stage="cumbered"), "#B8987A"),
        F([N("10:41", "answered and said unto her,"), sy("10:42")], JESUS)]
PG.extend(K.pack(SEGS, "LUK-C08-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · TEACH US TO PRAY")))
