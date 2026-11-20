"""Hebrews volume, Chapter 1 — Better than the Angels (Hebrews 1–4). Every verse, word for word from ref/eng-asv.
The letter on its way to the city on its hill (the title page). Hebrews 1: the prophets of old in a strip of faces (Moses,
Elijah, Isaiah, Jeremiah, Ezekiel, Daniel, Hosea, Amos); the effulgence of his glory over the worlds and the throne standing
empty in light (1:2–3); the angels, figures of white light, worshipping toward the throne (1:4–6, God's words in the Voice
box); his angels winds and his ministers a flame of fire (1:7, a song box); the throne and the sceptre and the oil of
gladness (1:8–9); the heavens rolled up as a mantle over the foundation of the earth (1:10–12); the heaven a throne and the
earth a footstool (1:13); ministering spirits going down to a town at dusk (1:14). Hebrews 2: a loosed boat drifting out of
the harbour (2:1–4); a man under the moon and the stars (2:5–8, Psalm 8 in song boxes); Jesus crowned with glory and honor —
risen in white light, the hill of the three crosses far below (2:9); Jesus risen among his brethren (2:10–13, his words in
balloons); a chain broken (2:14–16; the devil in words only); the mercy-seat (2:17–18). Hebrews 3: Moses before the
tabernacle (3:1–4) and the house plate (3:5–6); the wilderness and the forty years (3:7–11, the Voice box); neighbours met at
a door at sunrise (3:12–15); the empty desert (3:16–19). Hebrews 4: the land beyond Jordan (4:1–3); the sabbath camp (4:4–6);
Joshua over the land (4:7–10); the two-edged sword as a plate (4:11–13); the throne of grace (4:14–16)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from heb import G, art as A
from heb.art import art
from heb.common import K, Pages, D, lt, lp, ltj, lj, sg, gd, sy, gj, sj, v, title, nxt

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("HEB-C01-00-Title", "Chapter 1 · Better than the Angels", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A5A"></rect><g transform="translate(0 300)">{A.letter_road("t01", 760, 640, 5811)}</g>'
    return title(1, "Better than the Angels", "Hebrews 1–4", svg, "#2A2A5A", v("1:2", to="spoken unto us in his Son"))


SEGS = [
    # Hebrews 1 — the Son, better than the angels
    D([lt("1:1")], art(A.prophets), "#1A1028", head="God Hath Spoken", sky=1, art_h=190),
    D(lp("1:2-4"), art(A.majesty, "mj1", 5802), "#05051A", art_h=230),
    D([lt("1:5", to="at any time,"), gd("1:5", frm="Thou art my Son", to="begotten thee?"), lt("1:5", frm="and again,", to="and again,"),
       gd("1:5", frm="I will be to him"), lt("1:6", to="he saith,"), gd("1:6", frm="And let all")],
      art(A.angels_worship, "aw1", 5804), "#1A1440", head="Better than the Angels", art_h=220),
    D([lt("1:7", to="he saith,"), sg("1:7", frm="Who maketh")], art(A.wind_fire, "wf1", 5807), "#2A1A3A", art_h=200),
    D([lt("1:8", to="he saith,"), gd("1:8", frm="Thy throne"), gd("1:9")], art(A.sceptre_plate), "#0B1A2E", art_h=210),
    D([lt("1:10", to="And,"), gj(("1:10", "Thou, Lord"), "1:11", "1:12")], art(A.rolled_heavens, "rh1", 5810), "#FFF8DC", art_h=220),
    D([lt("1:13", to="at any time,"), gd("1:13", frm="Sit thou")], art(A.throne_footstool, "tf1", 5813), "#2A3A7A", art_h=200),
    D([lt("1:14")], art(A.ministering, "mn1", 5814), "#1A1440", art_h=200),
    # Hebrews 2 — so great a salvation; Jesus crowned
    D(lp("2:1-4"), art(A.drift, "dr1", 5821), "#1F4A6A", head="So Great a Salvation", sky=2, art_h=190),
    D([lt("2:5"), lt("2:6", to="saying,"), sg("2:6", frm="What is man"), sg("2:7")], art(A.what_is_man, "wm1", 5825), "#05051A", art_h=210),
    D([sg("2:8", to="under his feet."), lt("2:8", frm="For in that"), lt("2:9")], art(A.crowned, "cr1", 5829), "#3A2A4A", head="Crowned with Glory and Honor", art_h=280),
    D(lp("2:10-11"), art(A.many_sons, "ms1", 5830), "#3A3A7A", art_h=200),
    D([lt("2:12", to="saying,"), sy("2:12", frm="I will declare"), lt("2:13", to="And again,"), sy("2:13", frm="I will put", to="in him."),
       lt("2:13", frm="And again,", to="And again,", after="in him."), sy("2:13", frm="Behold, I")], art(A.brethren, "bt1", 5832), "#8FD0E2", art_h=230),
    D(lp("2:14-16"), art(A.chains_broken, 5814), "#3A3A7A", art_h=200),
    D(lp("2:17-18"), art(A.high_priest_mercy), "#0B1A2E", head="A Merciful and Faithful High Priest", art_h=220),
    # Hebrews 3 — Moses and Christ; to-day
    D(lp("3:1-4"), art(A.moses_tent, "mt1", 5831), "#8FD0E2", head="Moses in All His House", sky=3, art_h=220),
    D(lp("3:5-6"), art(A.house_plate), "#0B1A2E", art_h=230),
    D([lt("3:7", to="saith,"), gj(("3:7", "To-day"), "3:8", "3:9"), gj("3:10", "3:11")], art(A.wilderness_years, "wy1", 5837), "#FFE6A0",
      head="To-day If Ye Shall Hear His Voice", art_h=210),
    D(lp("3:12-14") + [lt("3:15", to="it is said,"), gd("3:15", frm="To-day")], art(A.to_day, "td1", 5842), "#3A3A7A", art_h=220),
    D(lp("3:16-19"), art(A.desert_fallen, 5846), "#FFE6A0", art_h=200),
    # Hebrews 4 — a sabbath rest; the word of God; the throne of grace
    D(lp("4:1-2"), art(A.land_of_rest, 5851), "#2A2A5A", head="A Promise of Entering into His Rest", sky=4, art_h=200),
    D([lt("4:3", to="he hath said,"), gd("4:3", frm="As I sware", to="my rest:"), lj(("4:3", "although"), ("4:4", None, "on this wise,")), sg("4:4", frm="And God rested")],
      art(A.sabbath, 5854), "#2A1A3A", art_h=190),
    D([lt("4:5", to="again,"), gd("4:5", frm="They shall not"), lj("4:6", ("4:7", None, "said before),")), gd("4:7", frm="To-day if")], art(A.david_harp, 5856), "#3A2418", art_h=190),
    D(lp("4:8-10"), art(A.joshua_land, "jl1", 5857), "#5AB0D8", art_h=200),
    D(lp("4:11-13"), art(A.sword_plate), "#0B1A2E", head="Sharper than Any Two-edged Sword", art_h=220),
    D(lp("4:14-16"), art(A.throne_grace, "tg1", 5864), "#1A1440", head="The Throne of Grace", art_h=220),
]
PG.extend(K.pack(SEGS, "HEB-C01-D", PG.next(), end=nxt("NEXT · A PRIEST FOR EVER")))
