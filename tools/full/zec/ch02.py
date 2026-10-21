"""Zechariah volume, Chapter 2 — The Four Chariots (Zechariah 5–8). Every verse, word for word from ref/asv.
VI the flying roll, and the curse entering the house of the thief; VII the ephah with the talent of lead (the woman within it
in words only), carried to Shinar by two women with wings like a stork; VIII the four chariots between the
mountains of brass, going forth north and south; the crowns of silver and gold for Joshua, the man whose name is the Branch
(Joshua's face), and the crowns a memorial in the temple; the men of Bethel asking of the fast (Sharezer's face); the fast
in sackcloth; the widow and the sojourner at the gate; the whirlwind over the desolate land; then the city of truth: the
old and the children in the streets, the roads from east and west, the foundation, the seed of peace, truth in the gates,
the fasts become feasts, the peoples going up, and the ten men holding the skirt of a Jew. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, nxt, NIGHT
from zec import G, art2 as A, ch01 as _prev
from hag.art import rebuild, foundation_bless
from mic.art import mountain_house
from zec.common import K, cp, gd, sg, sy, gds, sgs, ZECHARIAH, ZECH_NIGHT, ZECH_AWE, ZECH_GOLD, JESHUA, SHAREZER, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
VN = "#0B0B2A"


@P("ZEC-C02-00-Title", "Chapter 2 · The Four Chariots", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 210)">{A.bare(A.chariots, "tc", 760, 760, 201)}</g>'
    return title(2, "The Four Chariots", "Zechariah 5 – 8", svg, "#0B0B2A", v("6:1", frm="there came four chariots"), "Zechariah · Volume Thirty-Eight")


K.ptr = len(G.cuts)
SEGS = [K.drawn([cp("5:1"), cp("5:2", to="said unto me,"), sy("5:2", frm="What seest", to="seest thou?"), cp("5:2", frm="And I answered,", to="I answered,"), sy("5:2", frm="I see a flying")],
                lambda w, h: A.flying_roll("fr1", w, h, 202), VN, head="A Flying Roll", stamp=5),
        K.drawn([cp("5:3", to="Then said he unto me,"), sy("5:3", frm="This is the curse"), gd("5:4")], lambda w, h: A.flying_roll("fr2", w, h, 203, houses=True), VN),
        K.drawn([cp("5:5", to="said unto me,"), sy("5:5", frm="Lift up"), cp("5:6", to="And I said,"), sy("5:6", frm="What is it?", to="What is it?"), cp("5:6", frm="And he said,", to="And he said,"),
                 sy("5:6", frm="This is the ephah", to="goeth forth.")], lambda w, h: A.ephah("ep1", w, h, 204), VN, head="The Ephah"),
        K.face([cp("5:6", frm="He said moreover,", to="moreover,"), sy("5:6", frm="This is their appearance"), sy("5:7"),
                cp("5:8", to="And he said,"), sy("5:8", frm="This is Wickedness:", to="Wickedness:"), cp("5:8", frm="and he cast her")], ZECH_NIGHT, bg=COLD),
        K.drawn([cp("5:9"), cp("5:10", to="talked with me,"), sy("5:10", frm="Whither"), cp("5:11", to="said unto me,"), sy("5:11", frm="To build")], lambda w, h: A.ephah("ep3", w, h, 206, carried=True), VN)]
PG.extend(K.pack(SEGS, "ZEC-C02-D", PG.next()))
SEGS2 = [K.drawn([cp("6:1"), cp("6:2"), cp("6:3")], lambda w, h: A.chariots("cr1", w, h, 207), VN, head="Four Chariots", stamp=6),
         K.drawn([cp("6:4", to="talked with me,"), sy("6:4", frm="What are these"), cp("6:5", to="said unto me,"), sy("6:5", frm="These are"), sy("6:6"),
                  cp("6:7", to="and he said,"), sy("6:7", frm="Get you hence", to="through the earth."), cp("6:7", frm="So they walked"), cp("6:8", to="saying,"), sy("6:8", frm="Behold,")],
                 lambda w, h: A.chariots("cr2", w, h, 208, going=True), VN),
         K.drawn([cp("6:9"), gd("6:10"), gd("6:11")], lambda w, h: A.crowns(w, h, 209), "#2A1E14", head="The Man Whose Name Is the Branch"),
         K.face([gd("6:12"), gd("6:13")], JESHUA),
         K.drawn([gd("6:14"), gd("6:15")], lambda w, h: A.crowns(w, h, 210, hung=True), "#5A7AB8")]
PG.extend(K.pack(SEGS2, "ZEC-C02-E", PG.next()))
SEGS3 = [K.face([cp("7:1"), cp("7:2"), cp("7:3", to="saying,"), sy("7:3", frm="Should I weep")], SHAREZER, head="Should I Weep in the Fifth Month?", stamp=7),
         K.drawn([cp("7:4"), *gds("7:5-7")], lambda w, h: A.fasting("fs1", w, h, 211), "#6A6A7A"),
         K.drawn([cp("7:8"), gd("7:9"), gd("7:10")], lambda w, h: A.widow_gate("wg1", w, h, 212), "#8FB8D8", head="Execute True Judgment"),
         K.drawn(gds("7:11-14"), lambda w, h: A.adamant(w, h, 213), "#3A3A4A")]
PG.extend(K.pack(SEGS3, "ZEC-C02-F", PG.next()))
SEGS4 = [K.drawn([cp("8:1"), gd("8:2"), gd("8:3")], lambda w, h: A.zion_dwell(w, h, 214), "#2A2A5A", head="The City of Truth", stamp=8),
         K.drawn(gds("8:4-5"), lambda w, h: A.streets_play("sp1", w, h, 215), "#8FD0E2"),
         K.drawn(gds("8:6-8"), lambda w, h: A.east_west(w, h), "#0B1A2E"),
         K.drawn(gds("8:9-10"), lambda w, h: rebuild("rb2", w, h, 216), "#8FD0E2", head="Let Your Hands Be Strong"),
         K.drawn(gds("8:11-13"), lambda w, h: foundation_bless(w, h, 217), "#5A7AB8"),
         K.drawn(gds("8:14-17"), lambda w, h: A.gate_truth("gt1", w, h, 218), "#8FB8D8"),
         K.drawn([cp("8:18"), gd("8:19")], lambda w, h: A.feasts("fe1", w, h, 219), VN, head="Joy and Gladness"),
         K.drawn(gds("8:20-22"), lambda w, h: mountain_house(w, h, 220), "#2A3A6A"),
         K.drawn(gds("8:23"), lambda w, h: A.ten_men("tm1", w, h, 221), "#5A7AB8")]
PG.extend(K.pack(SEGS4, "ZEC-C02-G", PG.next(), end=nxt("NEXT · THY KING COMETH")))
