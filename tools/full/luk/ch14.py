"""Luke volume, Chapter 14 — Render unto Cæsar (Luke 20–21). Every verse, word for word from ref/eng-asv.
In the temple: by what authority?; the baptism of John, from heaven or from men?; the husbandmen of the vineyard — the
servants beaten and sent away empty and the beloved son cast forth and killed, told in words only over the empty vineyard;
the stone which the builders rejected; the spies and the denarius — render unto Cæsar the things that are Cæsar's, and unto
God the things that are God's; the Sadducees and the seven brethren, the God of the living, the Bush; David's son and
David's Lord; beware of the scribes in long robes. The poor widow's two mites at the treasury; not one stone upon another;
wars and tumults, signs from heaven; Jerusalem compassed with armies (no fighting drawn), the flight to the mountains; the
sun, the moon and the stars, the roaring of the sea, the Son of man coming in a cloud; the fig tree and all the trees;
watch ye at every season; by day in the temple, by night on Olivet."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art12 as A, ch13 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, PRIEST, SCRIBE, SCRIBE_STERN, SADDUCEE, SCRIBE_WISE, WITNESS)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C14-00-Title", "Chapter 14 · Render unto Cæsar", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A3A"></rect><g transform="translate(0 300)">{A.denarius("t14", 760, 780, 2001)}</g>'
    return title(14, "Render unto Cæsar", "Luke 20 – 21", svg, "#2A2A3A", v("20:25", frm="render unto Cæsar"))


SEGS = [D([cp("20:1"), N("20:2", "saying unto him,")], lambda w, h: A.temple_teaching("tt1", w, h, 2001), "#C8B490", head="By What Authority?", sky=20),
        F([N("20:3", "said unto them,"), sy("20:4")]),
        F([N("20:5", "with themselves, saying,"), sy("20:6"), cp("20:7")], PRIEST, bg=COLD),
        F([N("20:8", "said unto them,")], JESUS_STERN, bg=RED),
        D([Q("20:9", "c", "this parable:", "s")], lambda w, h: A.vineyard_hedged("vh1", w, h, 2002), "#8FD0E2", head="I Will Send My Beloved Son"),
        D([sy("20:10"), sy("20:11"), sy("20:12")], lambda w, h: A.vineyard_hedged("vh2", w, h, 2003, empty=True), "#8FD0E2"),
        D([sy("20:13"), sy("20:14")], lambda w, h: A.vineyard_hedged("vh3", w, h, 2004, tone="dusk"), "#4A2A5A"),
        D([sy("20:15"), Q("20:16", "s", "unto others.", "c", "they said,", "s")], lambda w, h: A.vineyard_hedged("vh4", w, h, 2005, tone="dusk", empty=True), "#4A2A5A"),
        D([N("20:17", "and said,"), sy("20:18")], lambda w, h: A.corner_stone("cs1", w, h, 2006), "#8FD0E2"),
        D([cp("20:19"), cp("20:20")], lambda w, h: A.counsel("cn1", w, h, 2007), "#2A2A3A", head="Render unto Cæsar"),
        F([N("20:21", "asked him, saying,"), sy("20:22")], WITNESS, bg=COLD),
        F([cp("20:23"), (q24 := Q("20:24", "s", "hath it?", "c", "And they said,", "s"))[0]], JESUS_STERN, bg=RED),
        D([q24[1:], N("20:25", "said unto them,"), cp("20:26")], lambda w, h: A.denarius("dn1", w, h, 2008), "#2A2A3A", ref="LUKE 20:24–26", art_h=240),
        F([cp("20:27"), N("20:28", "asked him, saying,")], SADDUCEE, bg=RED, head="The God of the Living"),
        D([sy("20:29"), sy("20:30"), sy("20:31"), sy("20:32"), sy("20:33")], lambda w, h: A.seven_tombs("st1", w, h, 2009), "#5A4A6A"),
        F([N("20:34", "said unto them,"), sy("20:35"), sy("20:36")], JESUS_TEACH),
        D([sy("20:37"), sy("20:38")], lambda w, h: A.the_bush("tb1", w, h, 2010), NIGHT),
        F([N("20:39", "answering said,"), cp("20:40")], SCRIBE_WISE),
        D([N("20:41", "said unto them,"), sy("20:42"), sy("20:43"), sy("20:44")], lambda w, h: A.psalm_scroll("ps1", w, h, 2011), "#1A1630", head="David's Son"),
        D([cp("20:45"), sy("20:46"), sy("20:47")], lambda w, h: A.moses_seat("ms1", w, h, 2012), "#C8B490", head="Beware of the Scribes"),
        # Luke 21
        D([cp("21:1"), cp("21:2"), N("21:3", "And he said,"), sy("21:4")], lambda w, h: A.treasury("tr1", w, h, 2101), "#C8B490", head="The Poor Widow", sky=21, art_h=220),
        D([cp("21:5"), sy("21:6")], lambda w, h: A.temple_stones("ts1", w, h, 2102), "#8FD0E2", head="Not One Stone upon Another"),
        F([N("21:7", "asked him, saying,")], PETER),
        F([N("21:8", "And he said,"), sy("21:9")], JESUS_STERN, bg=RED),
        D([N("21:10", "Then said he unto them,"), sy("21:11")], lambda w, h: A.wars_far("wf1", w, h, 2103), "#3A1A1A"),
        F([sy("21:12"), sy("21:13"), sy("21:14"), sy("21:15")], JESUS),
        F([sy("21:16"), sy("21:17"), sy("21:18"), sy("21:19")], JESUS_GRIEF, bg=COLD),
        D([sy("21:20")], lambda w, h: A.compassed("cm1", w, h, 2104), "#14141E", head="Jerusalem Compassed with Armies", art_h=240),
        D([sy("21:21"), sy("21:22"), sy("21:23")], lambda w, h: A.flee("fl1", w, h, 2105), "#8A7A6A"),
        D([sy("21:24")], lambda w, h: A.city_smoke("cs2", w, h, 2106), "#3A1A1A"),
        D([sy("21:25"), sy("21:26")], lambda w, h: A.darkened("dk1", w, h, 2107), "#05050E", head="Signs in Sun and Moon and Stars"),
        D([sy("21:27"), sy("21:28")], lambda w, h: A.clouds_glory("cg1", w, h, 2108), "#2A2A6A", art_h=240),
        D([N("21:29", "a parable:"), sy("21:30"), sy("21:31"), sy("21:32"), sy("21:33")], lambda w, h: A.fig_leaf("fg1", w, h, 2109), "#8FD0E2"),
        F([sy("21:34"), sy("21:35"), sy("21:36")], JESUS_TEACH, head="Watch Ye at Every Season"),
        D([cp("21:37"), cp("21:38")], A.footed(lambda w, h: A.olivet("ol1", w, h, 2110), "#3A3428"), "#4A2A5A", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C14-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THIS DO IN REMEMBRANCE OF ME")))
