"""2 Chronicles volume, Chapter 5 — Abijah and Asa (2 Chronicles 13–16). Every verse, word for word from ref/asv.
Abijah upon mount Zemaraim — hear me, O Jeroboam and all Israel; God is with us at our head; the ambushment behind and the
shout of Judah (a map; 13:17 words only); then Asa who sought Jehovah, the cities built while the land was quiet; Zerah the
Ethiopian with a thousand thousand — help us, O Jehovah our God, for we rely on thee (a map); Azariah the son of Oded —
Jehovah is with you while ye are with him; the covenant sworn with trumpets; Maacah removed; then Baasha and Ramah, the
silver sent to Ben-hadad, Hanani the seer — the eyes of Jehovah run to and fro throughout the whole earth — and the prison;
Asa diseased in his feet (words only); and the very great burning of spices."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, ABIJAH, ASA, ASA_OLD, AZARIAH_P, HANANI, COLD, GOLDEN, RED)
from chr2 import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT = "#0B1A2E", "#0F0E2A"


@P("2CH-C05-00-Title", "Chapter 5 · Abijah and Asa", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.zemaraim("t5", 760, 820, 501)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(5, "第五話", "Abijah and Asa", "2 Chronicles 13 – 16", svg, "#3A5A7A", v("13:12", to="at our head,"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("13:1-3")], "2CHR 13:1–3", below(lambda w, h: K.battle_map(w, h), 0.3), MAP, head="Abijah", stamp=13),
        drawn([cp("13:4", to="and said,"), say("13:4", frm="Hear me,"), says("13:5")], "2CHR 13:4–5", below(lambda w, h: K.zemaraim("zm5", w, h, 502), 0.36), "#8FD0E2",
              head="Upon Mount Zemaraim"),
        face([says("13:6-8")], "2CHR 13:6–8", ABIJAH),
        face([says("13:9-10")], "2CHR 13:9–10", ABIJAH),
        face([says("13:11-12")], "2CHR 13:11–12", ABIJAH, head="God Is with Us at Our Head"),
        drawn([caps("13:13-14")], "2CHR 13:13–14", below(lambda w, h: K.battle_map(w, h), 0.3), MAP),
        drawn([caps("13:15-18")], "2CHR 13:15–18", below(lambda w, h: K.battle_map(w, h, stage=1), 0.4), MAP),
        drawn([caps("13:19-22")], "2CHR 13:19–22", below(lambda w, h: K.K2.court("ct5", w, h, 503), 0.4), "#5A2A1E")]
PG.extend(pack(SEGS, "2CH-C05-D", PG.next()))
SEGS2 = [drawn([caps("14:1-5")], "2CHR 14:1–5", below(lambda w, h: K.asa_idol("ai5", w, h, 504), 0.4), "#3A2A3A", head="Asa", stamp=14),
         drawn([caps("14:6"), cp("14:7", to="unto Judah,"), say("14:7", frm="Let us build", to="every side."), cp("14:7", frm="So they built")], "2CHR 14:6–7",
               below(lambda w, h: K.judah_forts(w, h), 0.4), MAP),
         drawn([caps("14:8-10")], "2CHR 14:8–10", below(lambda w, h: K.zerah_map(w, h), 0.24), MAP, h=520, head="Zerah the Ethiopian"),
         face([cp("14:11", to="and said,"), say("14:11", frm="Jehovah, there is none")], "2CHR 14:11", ASA, bg=COLD),
         drawn([caps("14:12-13")], "2CHR 14:12–13", below(lambda w, h: K.zerah_map(w, h, pursuit=True), 0.4), MAP),
         drawn([caps("14:14-15")], "2CHR 14:14–15", below(lambda w, h: K.spoil("sp5", w, h, 505), 0.3), "#C8A878")]
PG.extend(pack(SEGS2, "2CH-C05-E", PG.next()))
SEGS3 = [face([caps("15:1"), cp("15:2", to="and said unto him,"), say("15:2", frm="Hear ye me,")], "2CHR 15:1–2", AZARIAH_P, head="If Ye Seek Him", stamp=15),
         face([says("15:3-7")], "2CHR 15:3–7", AZARIAH_P),
         drawn([caps("15:8-11")], "2CHR 15:8–11", below(lambda w, h: K.court_scene("cs5", w, h, 506, smoke=True, crowd=False), 0.3), "#8FD0E2"),
         drawn([caps("15:12-15")], "2CHR 15:12–15", below(lambda w, h: K.oath("oa5", w, h, 507), 0.4), "#FFB04A", head="With All Their Heart"),
         drawn([caps("15:16-19")], "2CHR 15:16–19", below(lambda w, h: K.asa_idol("ai5b", w, h, 508), 0.46), "#3A2A3A")]
PG.extend(pack(SEGS3, "2CH-C05-F", PG.next()))
SEGS4 = [drawn([caps("16:1"), cp("16:2", to="that dwelt at Damascus, saying,"), says("16:3")], "2CHR 16:1–3", below(lambda w, h: K.K3.silver_bags("sb5", w, h, 509), 0.44), "#5A3A2A",
               head="Baasha and Ramah", stamp=16),
         drawn([caps("16:4-6")], "2CHR 16:4–6", below(lambda w, h: K.ramah("rm5", w, h, 510), 0.36), "#8FD0E2"),
         face([cp("16:7", to="and said unto him,"), say("16:7", frm="Because thou")], "2CHR 16:7", HANANI, bg=COLD, head="Hanani the Seer"),
         face([says("16:8-9")], "2CHR 16:8–9", HANANI, bg=COLD),
         drawn([caps("16:10")], "2CHR 16:10", lambda w, h: K.prison(w, h, 511), "#3A3438"),
         face([caps("16:11-13")], "2CHR 16:11–13", ASA_OLD, bg=COLD),
         drawn([caps("16:14")], "2CHR 16:14", below(lambda w, h: K.spice_burning(w, h, 512), 0.24), "#3A2A4A")]
PG.extend(pack(SEGS4, "2CH-C05-G", PG.next(), end=end_mark("NEXT · JEHOSHAPHAT", "right: 10px; bottom: 34px")))
