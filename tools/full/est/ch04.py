"""Esther volume, Chapter 4 — The Days of Purim (Esther 8–10), the last chapter of Esther. Every verse, word for word from
ref/eng-asv. The house of Haman given to Esther and the king's ring to Mordecai; Esther at the king's feet and the golden sceptre
again — how can I endure to see the evil that shall come unto my people?; the writing in the king's name that no man may
reverse; the scribes in the month Sivan and the posts on swift steeds; Mordecai in royal apparel of blue and white and a great
crown of gold, and the Jews had light and gladness; the thirteenth day of Adar (9:1–16: the slaying words only, over the map of
the provinces and over the city of Shushan at dusk; the hanging of Haman's ten sons, 9:14, words over the gallows far off);
the days of rest, feasting and gladness, of sending portions one to another and gifts to the poor (a strip of the days of
Adar); the letters of Mordecai and the second letter of Purim; and Mordecai the Jew next unto king Ahasuerus."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from jos.art import below
from est import G, art as K
from est.common import (pack, cp, say, says, caps, drawn, face, joined, tshade as shade, AHASUERUS, ESTHER_GRIEF, ESTHER_QUEEN, ESTHER_RESOLVE, MORDECAI_ROYAL,
                        COLD, GOLDEN, RED)
from est import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT, DARK = "#0B1A2E", "#0F0E2A", "#1A0E14"


@P("EST-C04-00-Title", "Chapter 4 · The Days of Purim", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.going_forth("t4", 760, 820, 801)}</g><rect x="0" y="0" width="760" height="262" fill="#FFE680"></rect>')
    return chapter_title(4, "第四話", "The Days of Purim", "Esther 8 – 10", svg, "#8A6A2A", v("8:16"), "Esther · Volume Seventeen")


SEGS = [drawn([caps("8:1-2")], "ESTH 8:1–2", below(lambda w, h: K.ring_mordecai("rm8", w, h, 802), 0.24), "#C8B08A", head="The House of Haman", stamp=8),
        drawn([caps("8:3-4")], "ESTH 8:3–4", below(lambda w, h: K.inner_court("ic8", w, h, 803, stage="kneel", mirror=True), 0.3), "#C8B08A"),
        face([cp("8:5", to="And she said,"), say("8:5", frm="If it please"), says("8:6")], "ESTH 8:5–6", ESTHER_GRIEF, bg=COLD, head="How Can I Endure"),
        face([cp("8:7", to="to Mordecai the Jew,"), say("8:7", frm="Behold, I have given"), says("8:8")], "ESTH 8:7–8", AHASUERUS),
        drawn([caps("8:9")], "ESTH 8:9", below(lambda w, h: K.scribes("sc8", w, h, 804, ring=True), 0.42), "#C8B08A", head="In the King's Name"),
        drawn([caps("8:10")], "ESTH 8:10", below(lambda w, h: K.posts("po8", w, h, 805), 0.2), "#8FD0E2"),
        drawn([caps("8:11-12")], "ESTH 8:11–12", below(lambda w, h: K.pur_wheel(w, h, note="UPON ONE DAY · THE THIRTEENTH DAY OF ADAR"), 0.3), DARK),
        drawn([caps("8:13-14")], "ESTH 8:13–14", below(lambda w, h: K.empire_map(w, h, posts=True), 0.3), MAP),
        drawn([caps("8:15-16")], "ESTH 8:15–16", below(lambda w, h: K.going_forth("gf8", w, h, 806), 0.2), "#FFE680", head="Light and Gladness"),
        drawn([caps("8:17")], "ESTH 8:17", below(lambda w, h: K.feast_town("ft8", w, h, 807), 0.2), "#FFB04A")]
PG.extend(pack(SEGS, "EST-C04-D", PG.next()))
SEGS2 = [drawn([caps("9:1-2")], "ESTH 9:1–2", below(lambda w, h: K.empire_map(w, h, seed=9), 0.36), MAP, head="The Thirteenth Day of Adar", stamp=9),
         drawn([caps("9:3-4")], "ESTH 9:3–4", below(lambda w, h: K.mordecai_great("mg9", w, h, 901), 0.24), "#C8B08A"),
         drawn([caps("9:5-10")], "ESTH 9:5–10", below(lambda w, h: K.shushan(w, h, 902, tone="dusk", smoke=True), 0.4), "#3A2A5A", head="In Shushan the Palace"),
         drawn([caps("9:11"), cp("9:12", to="unto Esther the queen,"), say("9:12", frm="The Jews have slain")], "ESTH 9:11–12",
               below(lambda w, h: K.inner_court("ic9", w, h, 903, mirror=True), 0.46), "#C8B08A"),
         face([cp("9:13", to="Then said Esther,"), say("9:13", frm="If it please")], "ESTH 9:13", ESTHER_RESOLVE),
         drawn([caps("9:14")], "ESTH 9:14", below(lambda w, h: K.gallows_far(w, h, 904), 0.2), "#2A1A3A"),
         drawn([caps("9:15-16")], "ESTH 9:15–16", below(lambda w, h: K.shushan(w, h, 905, tone="night"), 0.36), NIGHT),
         drawn([caps("9:17-19")], "ESTH 9:17–19", below(lambda w, h: K.adar_days(w, h), 0.4), DARK, head="Feasting and Gladness"),
         drawn([caps("9:20-22")], "ESTH 9:20–22", below(lambda w, h: K.feast_town("ft9", w, h, 906, portions=True), 0.4), "#FFB04A"),
         drawn([caps("9:23-25")], "ESTH 9:23–25", below(lambda w, h: K.pur_wheel(w, h, note="PUR · THE LOT"), 0.4), DARK, head="Purim"),
         drawn([caps("9:26-28")], "ESTH 9:26–28", below(lambda w, h: K.every_year(w, h), 0.46), DARK),
         drawn([caps("9:29-32")], "ESTH 9:29–32", below(lambda w, h: K.second_letter("sl9", w, h, 907), 0.46), "#C8B08A")]
PG.extend(pack(SEGS2, "EST-C04-E", PG.next()))
SEGS3 = [drawn([caps("10:1")], "ESTH 10:1", below(lambda w, h: K.empire_map(w, h, isles=True, seed=10), 0.16), MAP, head="Next unto King Ahasuerus", stamp=10),
         drawn([caps("10:2")], "ESTH 10:2", below(lambda w, h: K.chronicles(w, h, 1001, names=("AHASUERUS", "MORDECAI", "MEDIA AND PERSIA")), 0.24), "#2A1A2A"),
         face([caps("10:3")], "ESTH 10:3", MORDECAI_ROYAL, bg=GOLDEN)]
PG.extend(pack(SEGS3, "EST-C04-F", PG.next(), end=end_mark("END OF ESTHER · NEXT · JOB", "right: 10px; bottom: 34px", ch="完")))
