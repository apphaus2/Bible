"""Proverbs volume, Chapter 11 — A Worthy Woman (Proverbs 30–31). Every verse, word for word from ref/eng-asv.
The words of Agur beside his face: who hath ascended up into heaven? (over the stars and the deep, God never drawn); two
things have I asked of thee; then his numbered sayings as numbered signs on the blueprint grid — the generations, the four
never satisfied, the four too wonderful, the four the earth cannot bear, the four little and exceeding wise, the four
stately in going; the ravens of the valley drawn as birds over the valley only. The words of king Lemuel which his mother
taught him; then the worthy woman (31:10–31, in song boxes) over the scenes of her household: the house and her husband,
wool and flax and the merchant-ships, the vineyard, the lamp by night and the distaff, the household in scarlet in the
snow, her husband among the elders at the gate, her children rising up to call her blessed."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art5 as K
from pro.common import (pack, cp, say, sg, sgs, says, caps, face, drawn, joined, AGUR, AGUR_LOW, LEMUEL, QUEEN_MOTHER, WORTHY, HUSBAND,
                        COLD, GOLDEN, RED)
from pro import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C11-00-Title", "Chapter 11 · A Worthy Woman", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A3A6A"></rect><g transform="translate(0 360)">{K.blessed("t11", 760, 720, 1101)}</g>')
    return chapter_title(11, "第十一話", "A Worthy Woman", "Proverbs 30 – 31", svg, "#5A3A6A", v("31:10"), "Proverbs · Volume Twenty")


SEGS = [face([caps("30:1"), says("30:2-3")], "30:1-3", AGUR_LOW, bg=COLD, head="The Words of Agur", stamp=30),
        drawn(sgs("30:4"), "30:4", lambda w, h: K.founded(w, h, 1102), "#0B0B2A", full=True, h=300),
        face([says("30:5-6")], "30:5-6", AGUR),
        face([says("30:7-9")], "30:7-9", AGUR_LOW, bg=COLD, head="Two Things Have I Asked of Thee"),
        drawn(sgs("30:10"), "30:10", lambda w, h: K.emb_art("face_liar", w, h, 1103, k=min(2.4, h / 120)), "#1A1030"),
        drawn(sgs("30:11-14"), "30:11-14", lambda w, h: K.generations(w, h, 1104), "#14102A", h=380, head="There Is a Generation"),
        drawn(sgs("30:15-16"), "30:15-16", lambda w, h: K.never_satisfied(w, h, 1105), "#14102A", h=340),
        drawn(sgs("30:17"), "30:17", lambda w, h: K.ravens(w, h, 1106), "#2A1A2A"),
        drawn(sgs("30:18-20"), "30:18-20", lambda w, h: K.wonderful(w, h, 1107), "#0B1A2E", h=360, head="Three Things Too Wonderful"),
        drawn(sgs("30:21-23"), "30:21-23", lambda w, h: K.trembles(w, h, 1108), "#14102A", h=340),
        drawn(sgs("30:24-28"), "30:24-28", lambda w, h: K.little_wise(w, h, 1109), "#1A2A1A", h=380, head="Little upon the Earth"),
        drawn(sgs("30:29-31"), "30:29-31", lambda w, h: K.stately(w, h, 1110), "#14102A", h=340),
        face([says("30:32-33")], "30:32-33", AGUR),
        face([caps("31:1"), says("31:2-3")], "31:1-3", QUEEN_MOTHER, head="The Words of King Lemuel", stamp=31),
        drawn(sgs("31:4-7"), "31:4-7", lambda w, h: K.lemuel("lm11", w, h, 1111), "#3A1A2A", h=420),
        face([says("31:8-9")], "31:8-9", QUEEN_MOTHER, bg=COLD),
        drawn(sgs("31:10-12"), "31:10-12", lambda w, h: K.worthy_home("wh11", w, h, 1112), "#8FD0E2", h=400, head="A Worthy Woman Who Can Find?"),
        drawn(sgs("31:13-15"), "31:13-15", lambda w, h: K.wool_ships("ws11", w, h, 1113), "#1E1650", h=400),
        drawn(sgs("31:16-17"), "31:16-17", lambda w, h: K.vineyard_plant("vp11", w, h, 1114), "#8FD0E2", h=380),
        drawn(sgs("31:18-19"), "31:18-19", lambda w, h: K.lamp_distaff("ld11", w, h, 1115), "#2A1A14"),
        drawn(sgs("31:20-22"), "31:20-22", lambda w, h: K.snow_scarlet("ss11", w, h, 1116), "#8A9AB8", h=400),
        drawn(sgs("31:23-24"), "31:23-24", lambda w, h: K.gate_husband("gh11", w, h, 1117), "#C8B8A0"),
        face([joined("song", "31:25", "31:26", "31:27")], "31:25-27", WORTHY, head="Her Children Rise Up"),
        drawn([cp("31:28", to="praiseth her, saying:"), say("31:29")], "31:28-29", lambda w, h: K.blessed("bl11", w, h, 1118), "#5A3A6A", h=380),
        drawn(sgs("31:30-31"), "31:30-31", lambda w, h: K.worthy_home("wh11b", w, h, 1119), "#8FD0E2", h=340)]
PG.extend(pack(SEGS, "PRO-C11-D", PG.next(), end=end_mark("END OF PROVERBS · NEXT · ECCLESIASTES", "right: 10px; bottom: 34px", ch="完")))
