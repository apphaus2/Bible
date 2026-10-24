"""John volume, Chapter 8 — That They May Be One (John 15–17). Every verse, word for word from ref/eng-asv.
The last discourse and the prayer, Jesus' faces alternating with drawings of what he names: the true vine on its terrace at
first light (the husbandman, the Father, never drawn — the vine only), the withered branches burning by the wall; the
eleven walking with him by night past the vineyards; the synagogue door shut on them; the Comforter promised, a soft light
in the upper room ("the prince of this world," 16:11, words only); a little while; the mother at dawn with her new-born
child in her arms, her sorrow turned into joy — nothing of the travail drawn; the eleven scattered along the dark roads and
Jesus alone in the light; I have overcome the world. The prayer: Jesus on the hillside by night with his eyes and hands
lifted up to heaven, the eleven about him, the city across the valley; that they may be one — the eleven gathered close in
the light; the roads going out into all the world; the glory ("the evil one," 17:15, words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art8 as A, ch07 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        JESUS_GRIEF, PETER, ANDREW, THOMAS)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C08-00-Title", "Chapter 8 · That They May Be One", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#5A6A9A"></rect><g transform="translate(0 200)">{A.true_vine("t8", 760, 720, 1501)}</g>'
           '<rect x="0" y="899" width="760" height="181" fill="#A89A8A"></rect>')
    return title(8, "That They May Be One", "John 15 – 17", svg, "#5A6A9A", v("15:5", frm="I am the vine, ye are the branches:", to="the branches:"))


W = lambda kind, seed: (lambda w, h: A.word_light(f"wl{seed}", w, h, seed, kind))
SEGS = [D([sy("15:1"), sy("15:2")], lambda w, h: A.true_vine("tv1", w, h, 1502), "#5A6A9A", head="I Am the True Vine", sky=15, art_h=280),
        F([sy("15:3"), sy("15:4")], JESUS_TEACH),
        D([sy("15:5")], lambda w, h: A.true_vine("tv2", w, h, 1503), "#5A6A9A", art_h=260),
        D([sy("15:6")], lambda w, h: A.true_vine("tv3", w, h, 1504, stage="fire"), "#2A1A2A", art_h=220),
        F([sy("15:7"), sy("15:8")], JESUS),
        F([sy("15:9"), sy("15:10"), sy("15:11")], JESUS_TEACH, head="Abide in My Love"),
        D([sy("15:12"), sy("15:13"), sy("15:14")], lambda w, h: A.night_walk("nw1", w, h, 1505), "#05051A", art_h=240),
        F([sy("15:15"), sy("15:16"), sy("15:17")], JESUS),
        F([sy("15:18"), sy("15:19")], JESUS_GRIEF, bg=COLD, head="If the World Hateth You"),
        D([sy("15:20"), sy("15:21")], lambda w, h: A.shut_door("sd1", w, h, 1506), "#2A2228"),
        F([sy("15:22"), sy("15:23"), sy("15:24")], JESUS_STERN),
        D([sy("15:25", to="in their law,"), sg("15:25", frm="They hated me"), sy("15:26"), sy("15:27")], lambda w, h: A.comforter("cf1", w, h, 1507), "#4A3438"),
        # John 16
        D([sy("16:1"), sy("16:2"), sy("16:3")], lambda w, h: A.found_him("fh1", w, h, 1601), "#5A4A7A", head="It Is Expedient for You", sky=16),
        F([sy("16:4"), sy("16:5"), sy("16:6")], JESUS_GRIEF, bg=COLD),
        D([sy("16:7"), sy("16:8"), sy("16:9"), sy("16:10"), sy("16:11")], lambda w, h: A.comforter("cf2", w, h, 1602), "#4A3438"),
        F([sy("16:12"), sy("16:13")], JESUS_TEACH),
        F([sy("16:14"), sy("16:15")], JESUS),
        D([sy("16:16")], lambda w, h: A.night_walk("nw2", w, h, 1603), "#05051A", head="A Little While", art_h=240),
        F([cp("16:17", to="one to another,"), sy("16:17", frm="What is this")], THOMAS),
        F([cp("16:18", to="They said therefore,"), sy("16:18", frm="What is this")], ANDREW),
        F([cp("16:19", to="said unto them,"), sy("16:19", frm="Do ye inquire"), sy("16:20")], JESUS_GRIEF, bg=COLD),
        D([sy("16:21")], lambda w, h: A.newborn("nb1", w, h, 1604), "#C8A878", art_h=260),
        F([sy("16:22"), sy("16:23"), sy("16:24")], JESUS),
        F([sy("16:25"), sy("16:26"), sy("16:27"), sy("16:28")], JESUS_TEACH),
        F([said("16:29", "His disciples say,", "Lo,"), sy("16:30")], PETER),
        F([said("16:31", "Jesus answered them,", "Do ye now")], JESUS_GRIEF, bg=COLD),
        D([sy("16:32")], lambda w, h: A.scattered("sc1", w, h, 1605), "#05051A", art_h=260),
        D([sy("16:33")], lambda w, h: A.world_light("wl1", w, h, 1606), "#3A4A8A", head="I Have Overcome the World", art_h=260),
        # John 17
        D([cp("17:1", to="he said,"), sy("17:1", frm="Father,"), sy("17:2"), sy("17:3")], lambda w, h: A.prayer("pr1", w, h, 1701), "#0B0B2A",
          head="Father, the Hour Is Come", sky=17, art_h=260),
        F([sy("17:4"), sy("17:5")], JESUS_TEACH),
        F([sy("17:6"), sy("17:7"), sy("17:8")], JESUS),
        D([sy("17:9"), sy("17:10"), sy("17:11")], lambda w, h: A.prayer("pr2", w, h, 1702, one=True), "#0B0B2A", head="That They May Be One", art_h=240),
        F([sy("17:12"), sy("17:13")], JESUS_GRIEF, bg=COLD),
        F([sy("17:14"), sy("17:15"), sy("17:16")], JESUS_TEACH),
        D([sy("17:17"), sy("17:18"), sy("17:19")], lambda w, h: A.everywhere("ev1", w, h, 1703), "#8FD0E2"),
        D([sy("17:20"), sy("17:21")], lambda w, h: A.world_light("wl2", w, h, 1704), "#3A4A8A"),
        F([sy("17:22"), sy("17:23")], JESUS),
        D([sy("17:24")], W("glory", 1705), "#FFC14D"),
        F([sy("17:25"), sy("17:26")], JESUS_TEACH)]
PG.extend(K.pack(SEGS, "JHN-C08-D", PG.next(), end=nxt("NEXT · IT IS FINISHED")))
