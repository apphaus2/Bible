"""John volume, Chapter 1 — The Word Became Flesh (John 1–2). Every verse, word for word from ref/eng-asv.
The prologue with no figure in it: the Word in the beginning, one light in the void; all things made through him; the
life the light of men; the light shining in the darkness and the darkness not apprehending it. John sent from God to bear
witness of the light, on a rock at first light; the true light coming into the world over its sleeping towns; the doors of
his own shut, and the doors that open. Then the Word became flesh, and Jesus is seen for the first time, walking into a
village at sunrise. John's witness: the priests and Levites at Bethany beyond the Jordan; Behold, the Lamb of God; the
Spirit descending as a dove of light; the two following at the tenth hour; Andrew and Simon; Philip; Nathanael under the
fig tree; the heaven opened and the angels of light ascending and descending. Cana: the feast, the mother of Jesus, the six
waterpots of stone filled to the brim, the ruler of the feast tasting the good wine. The temple at the passover: the scourge
of cords, the sheep and oxen driven out, the tables overthrown, the doves let fly, no one struck; destroy this temple; the
temple forty and six years in building."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art as A
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, BAPTIST,
                        BAPTIST_HUMBLE, BAPTIST_STERN, LEVITE, PHARISEE, ANDREW, PHILIP, NATHANAEL, MARY, JOHN, JEW)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C01-00-Title", "Chapter 1 · The Word Became Flesh", title=True)
def title_page(n):
    svg = A.word_light("t1", 760, 1080, 101, "shineth")
    return title(1, "The Word Became Flesh", "John 1 – 2", svg, "#05050E", v("1:5"))


W = lambda kind, seed: (lambda w, h: A.word_light(f"wl{seed}", w, h, seed, kind))
SEGS = [D([cp("1:1"), cp("1:2")], W("void", 102), "#030308", head="In the Beginning Was the Word", stamp=1),
        D([cp("1:3")], W("made", 103), "#05051A"),
        D([cp("1:4")], W("life", 104), "#8FD0E2"),
        D([cp("1:5")], W("shineth", 105), "#05050E"),
        D([cp("1:6"), cp("1:7"), cp("1:8")], lambda w, h: A.witness("wt1", w, h, 106), "#2A2A5A", head="A Man Sent from God"),
        D([cp("1:9")], W("world", 107), "#05051A"),
        D([cp("1:10"), cp("1:11")], lambda w, h: A.shut_doors("sd1", w, h, 108), "#05051A"),
        D([cp("1:12"), cp("1:13")], lambda w, h: A.shut_doors("sd2", w, h, 109, open_=True), "#05051A"),
        D([cp("1:14")], lambda w, h: A.flesh("fl1", w, h, 110), "#5A6A9A", head="The Word Became Flesh", art_h=300),
        F([said("1:15", "saying,", "This was he")], BAPTIST),
        D([cp("1:16"), cp("1:17"), cp("1:18")], W("glory", 111), "#FFC14D"),
        D([said("1:19", "to ask him,", "Who art thou?")], lambda w, h: A.inquiry("iq1", w, h, 112), "#8FD0E2", head="Who Art Thou?"),
        F([said("1:20", "denied not; and he confessed,", "I am not the Christ.")], BAPTIST_HUMBLE),
        D([cp("1:21", to="asked him,"), sy("1:21", frm="What then?", to="Art thou Elijah?"), cp("1:21", frm="And he saith,", to="he saith,"),
           sy("1:21", frm="I am not.", to="I am not."), sy("1:21", frm="Art thou the prophet?", to="the prophet?"), cp("1:21", frm="And he answered,", to="answered,"),
           sy("1:21", frm="No."), said("1:22", "unto him,", "Who art thou?")], lambda w, h: A.inquiry("iq2", w, h, 113), "#8FD0E2"),
        F([said("1:23", "He said,", "I am the voice")], BAPTIST),
        F([cp("1:24"), said("1:25", "said unto him,", "Why then")], LEVITE, bg=RED),
        F([said("1:26", "saying,", "I baptize"), sy("1:27")], BAPTIST_HUMBLE),
        D([cp("1:28")], lambda w, h: A.jordan("jd1", w, h, 114, crowd_n=6), "#8FD0E2"),
        D([said("1:29", "and saith,", "Behold,")], lambda w, h: A.behold_lamb("bl1", w, h, 115), "#8FD0E2", head="Behold, the Lamb of God"),
        F([sy("1:30"), sy("1:31")], BAPTIST),
        D([said("1:32", "saying,", "I have beheld"), sy("1:33"), sy("1:34")], lambda w, h: A.heavens_opened("ho1", w, h, 116), "#2A2A6A"),
        D([cp("1:35"), said("1:36", "and saith,", "Behold,"), cp("1:37")], lambda w, h: A.behold_lamb("bl2", w, h, 117, two=True), "#8FD0E2", head="Come and See"),
        D([cp("1:38", to="saith unto them,"), sy("1:38", frm="What seek ye?", to="What seek ye?"), cp("1:38", frm="And they said", to="said unto him,"), sy("1:38", frm="Rabbi"),
           cp("1:39", to="saith unto them,"), sy("1:39", frm="Come,", to="ye shall see."), cp("1:39", frm="They came")],
          lambda w, h: A.where_abide("wa1", w, h, 118), "#5A3A6A"),
        F([cp("1:40"), said("1:41", "saith unto him,", "We have found")], ANDREW),
        D([cp("1:42", to="looked upon him,")], lambda w, h: A.brought("br1", w, h, 119), "#8FD0E2"),
        F([cp("1:42", frm="and said,", to="and said,"), sy("1:42", frm="Thou art Simon")], JESUS),
        D([said("1:43", "saith unto him,", "Follow me."), cp("1:44")], lambda w, h: A.follow_me("fm1", w, h, 120), "#8FD0E2", head="Under the Fig Tree"),
        F([said("1:45", "saith unto him,", "We have found him,")], PHILIP),
        D([cp("1:46", to="said unto him,"), sy("1:46", frm="Can any", to="Nazareth?"), cp("1:46", frm="Philip saith", to="unto him,"), sy("1:46", frm="Come and see.")],
          lambda w, h: A.under_fig("uf1", w, h, 121), "#8FD0E2"),
        F([said("1:47", "saith of him,", "Behold,")], JESUS),
        F([cp("1:48", to="saith unto him,"), sy("1:48", frm="Whence", to="me?")], NATHANAEL),
        F([cp("1:48", frm="Jesus answered", to="said unto him,"), sy("1:48", frm="Before Philip")], JESUS_TEACH),
        F([said("1:49", "answered him,", "Rabbi,")], NATHANAEL),
        F([said("1:50", "said unto him,", "Because")], JESUS),
        D([said("1:51", "saith unto him,", "Verily,")], lambda w, h: A.ladder_light("ll1", w, h, 122), "#05051A", art_h=280),
        # John 2
        D([cp("2:1"), cp("2:2")], lambda w, h: A.cana("cn1", w, h, 201), "#8FD0E2", head="The Marriage in Cana", sky=2, art_h=300),
        F([said("2:3", "saith unto him,", "They have")], MARY),
        F([said("2:4", "saith unto her,", "Woman,")], JESUS),
        F([said("2:5", "unto the servants,", "Whatsoever")], MARY),
        D([cp("2:6"), cp("2:7", to="saith unto them,"), sy("2:7", frm="Fill", to="with water."), cp("2:7", frm="And they filled")],
          lambda w, h: A.cana("cn2", w, h, 202, stage="pots"), "#8FD0E2", art_h=240),
        F([cp("2:8", to="saith unto them,"), sy("2:8", frm="Draw out", to="of the feast."), cp("2:8", frm="And they bare it.")], JESUS_TEACH),
        D([cp("2:9"), said("2:10", "and saith unto him,", "Every man")], lambda w, h: A.cana("cn3", w, h, 203, stage="wine"), "#8FD0E2", art_h=240),
        D([cp("2:11"), cp("2:12")], lambda w, h: A.galilee("gl1", w, h, 204), "#8FD0E2"),
        D([cp("2:13"), cp("2:14")], lambda w, h: A.temple_market("tc1", w, h, 205), "#8FD0E2", head="My Father's House", art_h=260),
        D([cp("2:15"), said("2:16", "he said,", "Take these")], lambda w, h: A.temple_market("cl1", w, h, 206, cleansed=True), "#8FD0E2", art_h=280),
        F([said("2:17", "it was written,", "Zeal", kind="song")], JOHN),
        F([said("2:18", "said unto him,", "What sign")], JEW, bg=RED),
        F([said("2:19", "said unto them,", "Destroy")], JESUS_STERN, bg=RED),
        D([said("2:20", "said,", "Forty"), cp("2:21"), cp("2:22")], lambda w, h: A.temple_building("tb1", w, h, 207), "#8FD0E2"),
        D([cp("2:23"), cp("2:24"), cp("2:25")], lambda w, h: A.passover_city("pc1", w, h, 208), "#8FD0E2")]
PG.extend(K.pack(SEGS, "JHN-C01-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · YE MUST BE BORN ANEW")))
