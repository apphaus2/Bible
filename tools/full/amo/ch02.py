"""Amos volume, Chapter 2 — The Plumb-line (Amos 5–9), the last chapter of Amos. Every verse, word for word from ref/asv.
A lamentation over the house of Israel (a thousand, a hundred, ten); seek me, and ye shall live — not Beth-el, nor Gilgal,
nor Beer-sheba; him that maketh the Pleiades and Orion; the gate and the houses of hewn stone; seek good, and not evil;
wailing in the broad ways; the day of Jehovah darkness — the lion, the bear, the serpent; I hate your feasts — let justice
roll down as waters; the star of your god and captivity beyond Damascus; woe to them that are at ease in Zion (Calneh,
Hamath, Gath); beds of ivory; ten men in one house (6:9–10 words over the broken houses); horses upon the rock; then the
visions: the locusts after the king's mowings, the fire upon the great deep, and the plumb-line (a blueprint of the wall,
the line hanging, no hand drawn); Amaziah of Beth-el and the herdsman and dresser of sycomore-trees (7:17 words over
Beth-el); the basket of summer fruit; the songs of the temple turned to wailing (8:3 over the silent court); the false
ephah and shekel; the sun gone down at noon; a famine of hearing the words of Jehovah; the altar and its capitals (9:1, the
Lord never drawn); the sieve; and the tabernacle of David raised up, the plowman overtaking the reaper."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from amo import G, art2 as K
from dan.kit import refs_of
from amo.common import L, AMOS, AMOS_STERN, AMOS_GRIEF, AMOS_PRAY, AMAZIAH, COLD, GOLDEN, RED, NIGHT
from amo import ch01 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY, MAP, DUSK, GREY, BP = "#8FD0E2", "#0B1A2E", "#5A3A5A", "#8A8A9A", "#0B2A4A"


@P("AMO-C02-00-Title", "Chapter 2 · The Plumb-line", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B2A4A"></rect><g transform="translate(0 280)">{K.plumb(760, 800, labels=False)}</g>')
    return chapter_title(2, "第二話", "The Plumb-line", "Amos 5 – 9", svg, "#0B2A4A", v("7:8", frm="Behold, I will set a plumb-line", to="my people Israel;"), "Amos · Volume Thirty")


c, cs, s, ss, sl, A, T, Nt, gls, cut, sp2 = L.c, L.cs, L.s, L.ss, L.sl, L.A, L.T, L.N, L.gls, L.cut, L.split
am = lambda refs: ss(refs, "amos")

SEGS = [A([am("5:1-2")], "5:1-2", lambda w, h: K.fallen_virgin(w, h, 201), GREY, who="amos", head="A Lamentation", stamp=5),
        A([*cut("5:3", "For thus saith the Lord Jehovah:", poem=True)], "5:3", lambda w, h: K.thousand(w, h), MAP),
        A([*cut("5:4", "unto the house of Israel,", poem=True), *gls("5:5")], "5:4-5", lambda w, h: K.seek_map(w, h), MAP, head="Seek Ye Me, and Ye Shall Live"),
        A([am("5:6-7")], "5:6-7", lambda w, h: K.seek_map(w, h, fire=True), MAP, who="amos"),
        A([am("5:8-9")], "5:8-9", lambda w, h: K.constellations(w, h, 202), "#05051A", who="amos"),
        A([am("5:10-11")], "5:10-11", lambda w, h: K.judges_gate("jg2", w, h, 203), "#C8B8A0", who="amos"),
        T([am("5:12-13")], "5:12-13", AMOS_STERN, RED, who="amos"),
        A([am("5:14-15")], "5:14-15", lambda w, h: K.two_ways(w, h, 204), SKY, who="amos"),
        A([*cut("5:16", "the God of hosts, the Lord:", poem=True), *gls("5:17")], "5:16-17", lambda w, h: K.mourning_streets("ms2", w, h, 205), GREY),
        A([am("5:18-20")], "5:18-20", lambda w, h: K.flee_lion(w, h), K.FIELD, who="amos", head="Darkness, and Not Light"),
        A([*gls("5:21-23")], "5:21-23", lambda w, h: K.feast_hated(w, h, 206), DUSK, head="Let Justice Roll Down"),
        A([*gls("5:24")], "5:24", lambda w, h: K.mighty_stream(w, h, 207), SKY),
        A([*gls("5:25-27")], "5:25-27", lambda w, h: K.beyond_damascus(w, h), MAP)]
PG.extend(L.pack(SEGS, "AMO-C02-D", PG.next()))

SEGS2 = [A([am("6:1-3")], "6:1-3", lambda w, h: K.ease_map(w, h), MAP, who="amos", head="Woe to Them That Are at Ease in Zion", stamp=6),
         A([am("6:4-7")], "6:4-7", lambda w, h: K.ivory_beds(w, h, 208), "#5A3A3A", who="amos"),
         T([*sp2("6:8", "the God of hosts:", "amos", "god")], "6:8", AMOS_STERN, RED, who="amos"),
         A([am("6:9-10")], "6:9-10", lambda w, h: K.broken_house(w, h, 209), "#5A4A5A", who="amos"),
         A([am("6:11")], "6:11", lambda w, h: K.broken_house(w, h, 210), "#5A4A5A", who="amos"),
         A([am("6:12-14")], "6:12-14", lambda w, h: K.hamath_arabah(w, h), MAP, who="amos")]
PG.extend(L.pack(SEGS2, "AMO-C02-E", PG.next()))

SEGS3 = [A([am("7:1"), *sp2("7:2", "then I said,", "amos", "amos"), *sp2("7:3", "concerning this:", "amos", "god")], "7:1-3", lambda w, h: K.mowings(w, h, 211), SKY, who="amos",
           head="Thus the Lord Jehovah Showed Me", stamp=7),
         A([am("7:4"), am("7:5"), *sp2("7:6", "concerning this:", "amos", "god")], "7:4-6", lambda w, h: K.fire_deep(w, h, 212), "#3A1A1A", who="amos"),
         A([am("7:7"), s("7:8", "amos", to="Amos, what seest thou?"), s("7:8", "amos", frm="And I said, A plumb-line.", to="Then said the Lord,"), L.g("7:8", after="Then said the Lord,"), *gls("7:9")], "7:7-9", lambda w, h: K.plumb(w, h), BP, who="amos",
           head="A Plumb-line"),
         A([*sp2("7:10", "king of Israel, saying,", "cap", "amaziah"), ss("7:11", "amaziah")], "7:10-11", lambda w, h: K.kings_sanctuary("ks2", w, h, 213, amos=False), DUSK, who="amaziah",
           head="Amaziah the Priest of Beth-el"),
         T([*sp2("7:12", "Also Amaziah said unto Amos,", "cap", "amaziah"), ss("7:13", "amaziah")], "7:12-13", AMAZIAH, COLD, who="amaziah"),
         A([*sp2("7:14", "said to Amaziah,", "cap", "amos"), am("7:15")], "7:14-15", lambda w, h: K.sycomore("sy2", w, h, 214), "#9AB8D8", who="amos"),
         T([am("7:16-17")], "7:16-17", AMOS_STERN, RED, who="amos")]
PG.extend(L.pack(SEGS3, "AMO-C02-F", PG.next()))

SEGS4 = [A([am("8:1"), *sp2("8:2", "Then said Jehovah unto me,", "amos", "god")], "8:1-2", lambda w, h: K.summer_basket(w, h, 215), BP, who="amos", head="A Basket of Summer Fruit", stamp=8),
         A([*gls("8:3")], "8:3", lambda w, h: K.silent_court(w, h, 216), "#2A1A2A"),
         A([am("8:4-6")], "8:4-6", lambda w, h: K.false_measures(w, h), MAP, who="amos"),
         A([am("8:7-8"), *gls("8:9-10")], "8:7-10", lambda w, h: K.noon_dark(w, h, 217), "#1A1A2A", who="amos", head="The Sun to Go Down at Noon"),
         A([*gls("8:11-12")], "8:11-12", lambda w, h: K.famine_map(w, h), MAP, head="A Famine of Hearing"),
         T([*gls("8:13-14")], "8:13-14", AMOS_GRIEF, COLD)]
PG.extend(L.pack(SEGS4, "AMO-C02-G", PG.next()))

SEGS5 = [A([*sp2("9:1", "and he said,", "amos", "god")], "9:1", lambda w, h: K.altar_capitals(w, h, 218), "#2A1A2A", who="amos", head="Beside the Altar", stamp=9),
         A([*gls("9:2-4")], "9:2-4", lambda w, h: K.nowhere(w, h), MAP),
         A([am("9:5-6")], "9:5-6", lambda w, h: K.chambers(w, h, 219), "#3A4A6A", who="amos"),
         A([*gls("9:7")], "9:7", lambda w, h: K.exodus_peoples(w, h), MAP),
         A([*gls("9:8-10")], "9:8-10", lambda w, h: K.sieve(w, h), MAP),
         A([*gls("9:11-12")], "9:11-12", lambda w, h: K.tabernacle_david("td2", w, h, 220), "#9AB8D8", head="The Tabernacle of David"),
         A([*gls("9:13")], "9:13", lambda w, h: K.overtake("ov2", w, h, 221), SKY),
         A([*gls("9:14-15")], "9:14-15", lambda w, h: K.planted(w, h, 222), SKY)]
PG.extend(L.pack(SEGS5, "AMO-C02-H", PG.next(), end=end_mark("END OF AMOS · NEXT · OBADIAH", "right: 10px; bottom: 34px", ch="完")))
