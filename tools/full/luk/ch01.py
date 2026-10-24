"""Luke volume, Chapter 1 — Gabriel (Luke 1). Every verse, word for word from ref/eng-asv.
The preface to Theophilus over the writing-desk and its scroll; Zacharias and Elisabeth at their house in the hill country;
the multitude praying without at the hour of incense; within, the holy place, the golden candlestick and the altar of
incense, and the angel of the Lord on its right side — a figure of white light with a gold rim, no face, no wings; Gabriel's
words over the holy place (never beside a face), Zacharias' fear beside his; dumb, making signs on the porch; Elisabeth hid
five months. The sixth month: Mary in her house at Nazareth, Gabriel in the doorway of light, her trouble and her answer
beside her face; the angel departed. The hill country with haste; the visitation at Zacharias' door; Elisabeth's blessing
beside her face; the Magnificat in song boxes over the hills at morning and beside Mary's face. John born among the
neighbors and kinsfolk; the eighth day, the writing tablet — His name is John; his mouth opened; the sayings noised abroad;
the Benedictus in song boxes, the dayspring from on high over the hills of Judah; and the child in the deserts."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art as A
from luk.common import (K, Pages, D, F, Q, N, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, ZACHARIAS, ZACHARIAS_AFRAID, ZACHARIAS_SING,
                        ELISABETH, ELISABETH_JOY, MARY_AWE, MARY_SING, CROWD_MAN)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C01-00-Title", "Chapter 1 · Gabriel", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A2A"></rect><g transform="translate(0 300)">{A.holy_place("t1", 760, 780, 101, zach=False)}</g>'
    return title(1, "Gabriel", "Luke 1", svg, "#2A1A2A", v("1:19", frm="I am Gabriel,", to="presence of God;"))


SEGS = [D([cp("1:1"), cp("1:2"), cp("1:3"), cp("1:4")], lambda w, h: A.writing_desk("wd1", w, h, 101), "#2A2030", head="Most Excellent Theophilus", sky=1, art_h=220),
        D([cp("1:5"), cp("1:6"), cp("1:7")], lambda w, h: A.priest_home("ph1", w, h, 102), "#5A4A7A", head="Zacharias and Elisabeth"),
        D([cp("1:8"), cp("1:9"), cp("1:10")], lambda w, h: A.hour_incense("hi1", w, h, 103), "#8FD0E2", head="The Hour of Incense"),
        D([cp("1:11"), cp("1:12")], lambda w, h: A.holy_place("hp1", w, h, 104, afraid=True), "#2A1A2A", art_h=240),
        D([N("1:13", "said unto him,"), sy("1:14")], lambda w, h: A.holy_place("hp2", w, h, 105), "#2A1A2A"),
        D([sy("1:15"), sy("1:16"), sy("1:17")], lambda w, h: A.holy_place("hp3", w, h, 106, zach=False), "#2A1A2A"),
        F([N("1:18", "said unto the angel,")], ZACHARIAS_AFRAID, bg=COLD),
        D([N("1:19", "answering said unto him,"), sy("1:20")], lambda w, h: A.holy_place("hp4", w, h, 107, afraid=True), "#2A1A2A", head="I Am Gabriel"),
        D([cp("1:21"), cp("1:22")], lambda w, h: A.dumb_signs("ds1", w, h, 108), "#8FD0E2"),
        D([cp("1:23"), cp("1:24")], lambda w, h: A.hid_herself("hh1", w, h, 109), "#B8987A"),
        F([sy("1:25")], ELISABETH),
        D([cp("1:26"), cp("1:27")], lambda w, h: A.mary_alone("ma1", w, h, 110), "#B8987A", head="Hail, Thou That Art Highly Favored"),
        D([N("1:28", "and said,")], lambda w, h: A.annunciation("an1", w, h, 111), "#B8987A", art_h=260),
        F([cp("1:29")], MARY_AWE, bg=COLD),
        D([N("1:30", "said unto her,"), sy("1:31"), sy("1:32"), sy("1:33")], lambda w, h: A.annunciation("an2", w, h, 112), "#B8987A"),
        F([N("1:34", "said unto the angel,")], MARY_AWE),
        D([N("1:35", "said unto her,"), sy("1:36"), sy("1:37")], lambda w, h: A.annunciation("an3", w, h, 113), "#B8987A"),
        D([Q("1:38", "c", "And Mary said,", "s", "according to thy word.", "c")], lambda w, h: A.annunciation("an4", w, h, 114, departed=True), "#B8987A"),
        D([cp("1:39"), cp("1:40")], lambda w, h: A.hill_road("hr1", w, h, 115), "#8FD0E2", head="Blessed Art Thou among Women"),
        D([cp("1:41"), N("1:42", "and said,")], lambda w, h: A.visitation("vs1", w, h, 116), "#8FD0E2", art_h=240),
        F([sy("1:43"), sy("1:44"), sy("1:45")], ELISABETH_JOY),
        D([N("1:46", "And Mary said,", "n"), sg("1:47"), sg("1:48")], lambda w, h: A.magnify("mg1", w, h, 117), "#3A5AA8", head="My Soul Doth Magnify the Lord", art_h=240),
        F([sg("1:49"), sg("1:50"), sg("1:51"), sg("1:52")], MARY_SING),
        D([sg("1:53"), sg("1:54"), sg("1:55"), cp("1:56")], lambda w, h: A.hill_road("hr2", w, h, 118), "#8FD0E2"),
        D([cp("1:57"), cp("1:58")], lambda w, h: A.john_born("jb1", w, h, 119), "#A88A6A", head="His Name Is John"),
        D([cp("1:59"), Q("1:60", "c", "answered and said,", "s")], lambda w, h: A.john_born("jb2", w, h, 120), "#A88A6A"),
        F([N("1:61", "said unto her,"), cp("1:62")], CROWD_MAN, bg=COLD),
        D([Q("1:63", "c", "wrote, saying,", "s", "His name is John.", "c")], lambda w, h: A.tablet("tb1", w, h, 121), "#A88A6A", art_h=240),
        F([cp("1:64")], ZACHARIAS_SING),
        D([cp("1:65"), Q("1:66", "c", "saying,", "s", "this child be?", "c")], lambda w, h: A.housetops("ht1", w, h, 122), "#5A6A9A"),
        F([cp("1:67"), sg("1:68"), sg("1:69"), sg("1:70")], ZACHARIAS_SING, head="The Dayspring from on High"),
        D([sg("1:71"), sg("1:72"), sg("1:73"), sg("1:74"), sg("1:75")], lambda w, h: A.prophecy("pp1", w, h, 123), "#1A1630"),
        F([sg("1:76"), sg("1:77")], ZACHARIAS),
        D([sg("1:78"), sg("1:79")], lambda w, h: A.dayspring("dy1", w, h, 124), "#0B0B2A", art_h=260),
        D([cp("1:80")], lambda w, h: A.deserts("de1", w, h, 125), "#3A2A5A")]
PG.extend(K.pack(SEGS, "LUK-C01-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · GOOD TIDINGS OF GREAT JOY")))
