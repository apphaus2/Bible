"""John volume, Chapter 3 — The Bread of Life (John 5–6). Every verse, word for word from ref/eng-asv (5:4 has no text in
the ASV: the coverage lists it as omitted).
The pool of Bethesda by the sheep gate, the sick under its five porches; the man of thirty and eight years on his pallet,
Wouldest thou be made whole?, and then standing with his bed on his shoulder; the Jews stopping him in the street on the
sabbath; Jesus finding him in the temple. The discourse of the Son and the Father beside Jesus' faces, with the light, the
rock tombs at dawn (the dead that hear his voice are words only), John the lamp that burneth and shineth, the scrolls of
the scriptures and the tables of Moses. Then the mountain over the sea of Tiberias; Philip and Andrew; the lad's five
barley loaves and two fishes; the companies on the much grass, the loaves given out, the twelve baskets; the mountain
alone; the boat in the dark and the great wind, It is I, the boat at the land; the boats from Tiberias. The bread of life
beside his faces and over the loaf in a shaft of light, the manna round the tents, the broken loaf, and for his flesh and
his blood the bread and the cup only. The synagogue at Capernaum, the hard saying, the disciples going back along the road,
and the twelve: Lord, to whom shall we go?"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art3 as A, ch02 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        JESUS_GRIEF, LAME, HEALED, JEW, CROWD, PHILIP, ANDREW, PETER, JUDAS)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C03-00-Title", "Chapter 3 · The Bread of Life", title=True)
def title_page(n):
    svg = A.bread_heaven("t3", 760, 1080, 501)
    return title(3, "The Bread of Life", "John 5 – 6", svg, "#14122A", v("6:35", frm="I am the bread of life:", to="bread of life:"))


W = lambda kind, seed: (lambda w, h: A.word_light(f"wl{seed}", w, h, seed, kind))
SEGS = [D([cp("5:1"), cp("5:2"), cp("5:3")], lambda w, h: A.bethesda("bt1", w, h, 502), "#8FD0E2", head="The Pool of Bethesda", sky=5, art_h=260),
        D([cp("5:5"), said("5:6", "he saith unto him,", "Wouldest")], lambda w, h: A.bethesda("bt2", w, h, 503, stage="man"), "#8FD0E2", art_h=250),
        F([said("5:7", "answered him,", "Sir,")], LAME, bg=COLD),
        F([said("5:8", "saith unto him,", "Arise,")], JESUS),
        D([cp("5:9")], lambda w, h: A.bethesda("bt3", w, h, 504, stage="rise"), "#8FD0E2", art_h=270),
        D([said("5:10", "that was cured,", "It is the sabbath,"), said("5:11", "answered them,", "He that made")], lambda w, h: A.sabbath_street("ss1", w, h, 505),
          "#8FD0E2", head="It Is the Sabbath"),
        F([said("5:12", "They asked him,", "Who is the man")], JEW, bg=RED),
        D([cp("5:13"), said("5:14", "said unto him,", "Behold,")], lambda w, h: A.temple_found("tf1", w, h, 506), "#8FD0E2"),
        F([cp("5:15"), cp("5:16")], JEW, bg=RED),
        F([said("5:17", "answered them,", "My Father"), cp("5:18")], JESUS_STERN, bg=RED),
        F([said("5:19", "said unto them,", "Verily,"), sy("5:20")], JESUS_TEACH, head="The Son Giveth Life"),
        D([sy("5:21"), sy("5:22"), sy("5:23")], W("glory", 507), "#FFC14D"),
        F([sy("5:24")], JESUS),
        D([sy("5:25"), sy("5:26"), sy("5:27")], lambda w, h: A.tombs_light("tl1", w, h, 508), "#2A2A5A", art_h=220),
        F([sy("5:28"), sy("5:29"), sy("5:30")], JESUS_STERN),
        F([sy("5:31"), sy("5:32"), sy("5:33"), sy("5:34")], JESUS_TEACH, head="They Bear Witness of Me"),
        D([sy("5:35")], lambda w, h: A.lamp_shining("ls1", w, h, 509), "#1A1222"),
        D([sy("5:36"), sy("5:37"), sy("5:38")], W("glory", 510), "#FFC14D"),
        D([sy("5:39"), sy("5:40")], lambda w, h: A.scriptures("sc1", w, h, 511), "#3A2A2A"),
        F([sy("5:41"), sy("5:42"), sy("5:43"), sy("5:44")], JESUS_STERN),
        D([sy("5:45"), sy("5:46"), sy("5:47")], lambda w, h: A.tables_law("tw1", w, h, 512), "#12113A"),
        # John 6
        D([cp("6:1"), cp("6:2"), cp("6:3"), cp("6:4")], lambda w, h: A.mountain_sea("ms1", w, h, 601), "#8FD0E2", head="Five Barley Loaves", sky=6, art_h=240),
        F([cp("6:5", to="saith unto Philip,"), sy("6:5", frm="Whence"), cp("6:6")], JESUS),
        F([said("6:7", "answered him,", "Two hundred")], PHILIP),
        D([cp("6:8"), sy("6:9")], lambda w, h: A.lad_loaves("ll1", w, h, 602), "#8FD0E2", art_h=240),
        D([cp("6:10", to="Jesus said,"), sy("6:10", frm="Make the people", to="sit down."), cp("6:10", frm="Now there was")], lambda w, h: A.companies("cm1", w, h, 603),
          "#8FD0E2"),
        D([cp("6:11")], lambda w, h: A.five_loaves("fl1", w, h, 604), "#8FD0E2", art_h=240),
        D([cp("6:12", to="saith unto his disciples,"), sy("6:12", frm="Gather up"), cp("6:13")], lambda w, h: A.baskets("bk1", w, h, 605), "#8FD0E2"),
        D([cp("6:14", to="they said,"), sy("6:14", frm="This is of a truth"), cp("6:15")], lambda w, h: A.mount_alone("ma1", w, h, 606), "#0B0B2A"),
        D([cp("6:16"), cp("6:17"), cp("6:18")], lambda w, h: A.boat_dark("bd1", w, h, 607), "#05051A", head="It Is I", art_h=240),
        D([cp("6:19"), said("6:20", "saith unto them,", "It is I;")], lambda w, h: A.boat_dark("bd2", w, h, 608, jesus_=True), "#05051A", art_h=260),
        D([cp("6:21")], lambda w, h: A.boat_dark("bd3", w, h, 609, land=True), "#3A3A7A"),
        D([cp("6:22"), cp("6:23"), cp("6:24")], lambda w, h: A.boats_tiberias("bt4", w, h, 610), "#8FD0E2", head="The Bread out of Heaven"),
        F([said("6:25", "said unto him,", "Rabbi,")], CROWD),
        F([said("6:26", "answered them and said,", "Verily,"), sy("6:27")], JESUS_TEACH),
        F([said("6:28", "said therefore unto him,", "What must")], CROWD),
        F([said("6:29", "said unto them,", "This is the work")], JESUS),
        D([said("6:30", "said therefore unto him,", "What then"), sy("6:31", to="as it is written,"), sg("6:31", frm="He gave them")],
          lambda w, h: A.manna_camp("mc1", w, h, 611), "#3A2A5A"),
        F([said("6:32", "said unto them,", "Verily,"), sy("6:33")], JESUS_TEACH),
        F([said("6:34", "said therefore unto him,", "Lord,")], CROWD),
        D([said("6:35", "said unto them,", "I am the bread")], lambda w, h: A.bread_heaven("bh1", w, h, 612), "#14122A", head="I Am the Bread of Life", art_h=280),
        F([sy("6:36"), sy("6:37"), sy("6:38")], JESUS),
        F([sy("6:39"), sy("6:40")], JESUS_TEACH),
        F([cp("6:41"), said("6:42", "And they said,", "Is not this")], JEW, bg=RED),
        F([said("6:43", "said unto them,", "Murmur not"), sy("6:44")], JESUS_STERN),
        D([sy("6:45", to="in the prophets,"), sg("6:45", frm="And they shall", to="taught of God."), sy("6:45", frm="Every one"), sy("6:46")],
          lambda w, h: A.scriptures("sc2", w, h, 613), "#3A2A2A"),
        F([sy("6:47"), sy("6:48"), sy("6:49"), sy("6:50")], JESUS),
        D([sy("6:51")], lambda w, h: A.bread_heaven("bh2", w, h, 614, broken=True), "#14122A", art_h=240),
        F([said("6:52", "saying,", "How can")], JEW, bg=RED),
        D([said("6:53", "said unto them,", "Verily,"), sy("6:54"), sy("6:55"), sy("6:56")], lambda w, h: A.bread_heaven("bh3", w, h, 615, cup_=True, broken=True), "#14122A",
          art_h=220),
        F([sy("6:57"), sy("6:58")], JESUS_TEACH),
        D([cp("6:59"), said("6:60", "said,", "This is a hard")], lambda w, h: A.synagogue("sy1", w, h, 616), "#C8B490", head="To Whom Shall We Go?"),
        F([cp("6:61", to="said unto them,"), sy("6:61", frm="Doth this"), sy("6:62"), sy("6:63"), sy("6:64", to="believe not."), cp("6:64", frm="For Jesus knew")],
          JESUS_GRIEF, bg=COLD),
        F([said("6:65", "And he said,", "For this cause")], JESUS_GRIEF, bg=COLD),
        D([cp("6:66")], lambda w, h: A.went_back("wb1", w, h, 617), "#5A4A7A", art_h=240),
        F([said("6:67", "unto the twelve,", "Would ye")], JESUS_GRIEF, bg=COLD),
        F([said("6:68", "answered him,", "Lord,"), sy("6:69")], PETER),
        F([said("6:70", "answered them,", "Did not I")], JESUS_GRIEF, bg=COLD),
        F([cp("6:71")], JUDAS, bg=RED)]
PG.extend(K.pack(SEGS, "JHN-C03-D", PG.next(), end=nxt("NEXT · BEFORE ABRAHAM WAS")))
