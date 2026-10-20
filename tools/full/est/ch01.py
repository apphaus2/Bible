"""Esther volume, Chapter 1 — Vashti and Esther (Esther 1–2). Every verse, word for word from ref/eng-asv.
Ahasuerus who reigned from India even unto Ethiopia (a map of the hundred and seven and twenty provinces); the feast of a
hundred and fourscore days and the feast of seven days in the court of the garden — hangings of white, green and blue, a
pavement of red, white, yellow and black marble, vessels of gold diverse one from another; Vashti's feast for the women; the
seven chamberlains, and the queen who refused to come; the seven princes and the word of Memucan; letters into every province;
then the fair young virgins gathered to Shushan; Mordecai the Benjamite and Hadassah, that is, Esther; Hegai keeper of the
women; the twelve months of purification; the royal crown set upon Esther's head and Esther's feast; and Mordecai in the
king's gate — Bigthan and Teresh (2:23 words over the threshold and the book of the chronicles)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from est.common import tshade as shade
from jos.art import below
from est import G, art as K
from est.common import (pack, cp, say, says, caps, drawn, face, joined, AHAS_WROTH, VASHTI, MEMUCAN, SERVANT, MORDECAI, ESTHER, ESTHER_QUEEN, HEGAI,
                        COLD, GOLDEN, RED)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT = "#0B1A2E", "#0F0E2A"


@P("EST-C01-00-Title", "Chapter 1 · Vashti and Esther", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.crowning("t1", 760, 820, 101)}</g><rect x="0" y="0" width="760" height="262" fill="#6A3A1E"></rect>')
    return chapter_title(1, "第一話", "Vashti and Esther", "Esther 1 – 2", svg, "#4A1A6A", v("2:17", frm="he set the royal crown"), "Esther · Volume Seventeen")


SEGS = [drawn([caps("1:1-2")], "ESTH 1:1–2", below(lambda w, h: K.empire_map(w, h), 0.24), MAP, head="Ahasuerus", stamp=1),
        drawn([caps("1:3-4")], "ESTH 1:3–4", below(lambda w, h: K.throne_hall("th1", w, h, 102), 0.3), "#C8B08A", head="The Feast in Shushan"),
        drawn([caps("1:5-6")], "ESTH 1:5–6", below(lambda w, h: K.garden_feast("gf1", w, h, 103), 0.3), "#8FD0E2"),
        drawn([caps("1:7-8")], "ESTH 1:7–8", below(lambda w, h: K.vessels(w, h, 104), 0.36), "#3A1A2A"),
        drawn([caps("1:9")], "ESTH 1:9", below(lambda w, h: K.women_feast("wf1", w, h, 105), 0.2), "#C88A9A", head="Vashti the Queen"),
        drawn([caps("1:10-11")], "ESTH 1:10–11", below(lambda w, h: K.seven("sv1", w, h, 106), 0.36), "#C8B08A"),
        face([caps("1:12")], "ESTH 1:12", VASHTI, bg=RED),
        drawn([caps("1:13-14"), says("1:15")], "ESTH 1:13–15", below(lambda w, h: K.seven("sp1", w, h, 107, who="princes"), 0.46), "#C8B08A", head="The Seven Princes"),
        face([cp("1:16", to="the princes,"), say("1:16", frm="Vashti the queen hath"), says("1:17")], "ESTH 1:16–17", MEMUCAN, head="The Word of Memucan"),
        face([says("1:18-20")], "ESTH 1:18–20", MEMUCAN),
        drawn([caps("1:21-22")], "ESTH 1:21–22", below(lambda w, h: K.scribes("sc1", w, h, 108), 0.36), "#C8B08A")]
PG.extend(pack(SEGS, "EST-C01-D", PG.next()))
SEGS2 = [face([caps("2:1"), cp("2:2", to="unto him,"), say("2:2", frm="Let there be"), says("2:3"), say("2:4", to="instead of Vashti."), cp("2:4", frm="And the thing")],
              "ESTH 2:1–4", SERVANT, head="Fair Young Virgins", stamp=2),
         face([caps("2:5-7")], "ESTH 2:5–7", MORDECAI, head="Mordecai and Hadassah"),
         drawn([caps("2:8-9")], "ESTH 2:8–9", below(lambda w, h: K.womens_house("wh2", w, h, 201), 0.36), "#8FD0E2", head="Hegai, Keeper of the Women"),
         drawn([caps("2:10-11")], "ESTH 2:10–11", below(lambda w, h: K.womens_house("wh2b", w, h, 202, mordecai_out=True), 0.24), "#8FD0E2"),
         drawn([caps("2:12-14")], "ESTH 2:12–14", below(lambda w, h: K.perfumes(w, h, 203), 0.46), "#3A2A3A"),
         face([caps("2:15-16")], "ESTH 2:15–16", ESTHER, head="Esther"),
         drawn([caps("2:17")], "ESTH 2:17", below(lambda w, h: K.crowning("cr2", w, h, 204), 0.2), "#C8B08A", head="Queen instead of Vashti"),
         drawn([caps("2:18")], "ESTH 2:18", below(lambda w, h: K.esther_feast("ef2", w, h, 205), 0.2), "#C8B08A"),
         drawn([caps("2:19-20")], "ESTH 2:19–20", below(lambda w, h: K.kings_gate("kg2", w, h, 206), 0.3), "#8FD0E2", head="In the King's Gate"),
         drawn([caps("2:21-22")], "ESTH 2:21–22", below(lambda w, h: K.threshold("tr2", w, h, 207), 0.3), NIGHT),
         drawn([caps("2:23")], "ESTH 2:23", below(lambda w, h: K.chronicles(w, h, 208), 0.2), "#2A1A2A")]
PG.extend(pack(SEGS2, "EST-C01-E", PG.next(), end=end_mark("NEXT · FOR SUCH A TIME AS THIS", "right: 10px; bottom: 34px")))
