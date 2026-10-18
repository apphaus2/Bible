"""1 Kings volume, Chapter 10 — Ahijah's Word (1 Kings 14–15). Every verse, word for word from ref/asv.
Abijah sick; Jeroboam's wife disguised at the door of the blind prophet at Shiloh — come in, thou wife of Jeroboam; heavy
tidings (the Voice box through Ahijah); at the threshold of Tirzah the child died (words only). Then the reigns as roll cells
(Judah gold, Israel red): Rehoboam and Shishak's plunder, the shields of brass; Abijam; Asa who cut down the Asherah and
carried away the stones of Ramah; Nadab and Baasha (15:27–29 in words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, JEROBOAM, AHIJAH, reign, reign_pages, RED, COLD, GOLDEN)
from kg1 import ch09 as _prev

v, sp = G.v, G.span
WIFE = F("eve", skin="#C98E66", shadow="#4A3A3A", hair="#3A3430", scarf="#4A4038", brow="sorrow", light="#9AA8C8")
JEROBOAM_SAD = F("adam", skin="#C47A5A", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2E6B3A", band=True, brow="sorrow", light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C10-00-Title", "Chapter 10 · Ahijah's Word", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A2A"></rect><g transform="translate(0 340)">{K.ahijah_door("t10", 760, 740, 1001)}</g>')
    return chapter_title(10, "第十話", "Ahijah's Word", "1 Kings 14 – 15", svg, "#3A2A2A", v("14:6", frm="Come in,", to="heavy tidings."), "1 Kings · Volume Eleven")


SEGS = [face([caps("14:1"), cp("14:2", to="to his wife,"), joined("say", ("14:2", "Arise,"), "14:3")], "1KGS 14:1–3", JEROBOAM_SAD, bg=COLD, head="Abijah Fell Sick", stamp=14),
        drawn([caps("14:4"), cp("14:5", to="said unto Ahijah,"), gd("14:5", frm="Behold,")], "1KGS 14:4–5", below(lambda w, h: K.ahijah_door("ad10", w, h, 1002), 0.4), "#3A2A2A"),
        face([cp("14:6", to="that he said,"), say("14:6", frm="Come in,"), say("14:7", to="Go, tell Jeroboam,"), joined("god", ("14:7", "Thus saith Jehovah,"), "14:8")], "1KGS 14:6–8", AHIJAH, bg=NIGHT,
             head="Heavy Tidings"),
        face([gods("14:9-10")], "1KGS 14:9–10", AHIJAH, bg=NIGHT),
        face([gods("14:11-13")], "1KGS 14:11–13", AHIJAH, bg=NIGHT),
        face([gods("14:14-16")], "1KGS 14:14–16", AHIJAH, bg=NIGHT),
        drawn([caps("14:17-18")], "1KGS 14:17–18", lambda w, h: K.threshold("th10", w, h, 1003), "#3A2A4A")]
PG.extend(pack(SEGS, "1KI-C10-D", PG.next()))
REIGNS = [reign("Jeroboam", "14:19-20", judah=False, head="The Kings of Judah and of Israel"),
          reign("Rehoboam, King of Judah", "14:21-24")]
PG.extend(reign_pages(REIGNS, "1KI-C10-R", PG.next()))
SEGS2 = [drawn([caps("14:25-26")], "1KGS 14:25–26", below(lambda w, h: K.shishak("sk10", w, h, 1004), 0.26), "#FFE680", head="Shishak King of Egypt"),
         drawn([caps("14:27-28")], "1KGS 14:27–28", below(lambda w, h: K.brass_shields(w, h, 1005), 0.3), "#3A2214")]
PG.extend(pack(SEGS2, "1KI-C10-E", PG.next()))
REIGNS2 = [reign("Rehoboam", "14:29-31"), reign("Abijam, King of Judah", "15:1-5"), reign("Abijam", "15:6-8"),
           reign("Asa, King of Judah", "15:9-12")]
PG.extend(reign_pages(REIGNS2, "1KI-C10-S", PG.next()))
SEGS3 = [drawn([caps("15:13-15")], "1KGS 15:13–15", below(lambda w, h: K.asa_idol("ai10", w, h, 1006), 0.3), "#3A2A3A"),
         drawn([caps("15:16-18"), says("15:19")], "1KGS 15:16–19", below(lambda w, h: __import__("sa2.art", fromlist=["x"]).vessels(w, h, 1007), 0.4), "#2A1A3A", head="Ramah"),
         drawn([caps("15:20-22")], "1KGS 15:20–22", below(lambda w, h: K.ramah("rm10", w, h, 1008), 0.3), "#8FD0E2")]
PG.extend(pack(SEGS3, "1KI-C10-F", PG.next()))
REIGNS3 = [reign("Asa", "15:23-24"), reign("Nadab, King of Israel", "15:25-26", judah=False), reign("Nadab", "15:27-30", judah=False),
           reign("Nadab", "15:31-32", judah=False), reign("Baasha, King of Israel", "15:33-34", judah=False)]
PG.extend(reign_pages(REIGNS3, "1KI-C10-T", PG.next()))
