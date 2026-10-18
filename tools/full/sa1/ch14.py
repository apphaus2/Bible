"""1 Samuel volume, Chapter 14 — Mount Gilboa (1 Samuel 30–31), the last chapter of 1 Samuel. Every verse, word for word from
ref/asv. Ziklag burnt and the wives taken; David strengthened himself in Jehovah his God; the ephod — Pursue; the brook
Besor; the Egyptian in the field; the Amalekites eating and dancing; all recovered; as his share is that goeth down to the
battle, so shall his share be that tarrieth by the baggage; the presents to the elders of Judah (roll cells). Then Gilboa
(the digest's panels): Saul's death is words over the mountain with his crown and spear (31:4–5, 31:8–10 nothing drawn), and
the men of Jabesh-gilead burying the bones under the tamarisk at Jabesh."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages
from deu.common import shade
from deu import art4 as D4
from jos import art as JA
from jdg import art as JG
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_WEEP, DAVID, DAVID_BOLD, DAVID_GRIEVED, RED, COLD, GOLDEN)
from sa1 import ch13 as _prev

v, sp = G.v, G.span
EGYPTIAN = F("adam", skin="#9A6A4A", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", egypt=("#E8E2D6", "#D7261E"), sweat=True, brow="sorrow", light="#FFC14D")
BASE = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1SA-C14-00-Title", "Chapter 14 · Mount Gilboa", title=True)
def title(n):
    bg, art = D("B10", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A3A"></rect><g transform="translate(0 280)">{art(760, 800)}</g>')
    return chapter_title(14, "第十四話", "Mount Gilboa", "1 Samuel 30 – 31", svg, "#2A1A3A", v("31:6"), "1 Samuel · Volume Nine")


SEGS = [drawn([caps("30:1-3")], "1SAM 30:1–3", lambda w, h: JA.burning(w, h, 1411, city="ziklag"), "#2A0A0A", head="Ziklag Burned with Fire", stamp=30),
        face([caps("30:4-6")], "1SAM 30:4–6", DAVID_GRIEVED, bg=COLD),
        drawn([cp("30:7", to="the son of Ahimelech,"), say("30:7", frm="I pray thee,", to="the ephod."), cp("30:7", frm="And Abiathar brought"), cp("30:8", to="saying,"), say("30:8", frm="If I pursue", to="overtake them?"),
               cp("30:8", frm="And he answered him,", to="And he answered him,"), gd("30:8", frm="Pursue;")], "1SAM 30:7–8", lambda w, h: K.ephod_inquire("ei14", w, h, 1412), "#2A1A3A"),
        drawn([caps("30:9-12")], "1SAM 30:9–12", lambda w, h: JG.fords("bs14", w, h, 1413), "#E8C88A", head="The Brook Besor"),
        face([cp("30:13", to="said unto him,"), say("30:13", frm="To whom", to="whence art thou?"), cp("30:13", frm="And he said,", to="And he said,"), ("say", v("30:13", frm="I am a young man") + " " + v("30:14"))],
             "1SAM 30:13–14", EGYPTIAN),
        face([cp("30:15", to="said to him,"), say("30:15", frm="Wilt thou", to="this troop?"), cp("30:15", frm="And he said,", to="And he said,"), say("30:15", frm="Swear unto me")], "1SAM 30:15", EGYPTIAN),
        drawn([caps("30:16-17")], "1SAM 30:16–17", lambda w, h: JG.midian(w, h, 1414, night_=True), "#14123A"),
        drawn([caps("30:18-19"), cp("30:20", to="and said,"), say("30:20", frm="This is")], "1SAM 30:18–20", lambda w, h: K.spoil_flocks(w, h, 1415), "#E8C88A", head="They Shall Share Alike"),
        face([caps("30:21"), cp("30:22", to="and said,"), say("30:22", frm="Because they went")], "1SAM 30:21–22", BASE, bg=RED),
        face([cp("30:23", to="Then said David,"), ("say", v("30:23", frm="Ye shall not") + " " + v("30:24")), caps("30:25")], "1SAM 30:23–25", DAVID_BOLD)]
PG.extend(pack(SEGS, "1SA-C14-D", PG.next()))
GIFTS = [("The Spoil of the Enemies of Jehovah", v("30:26"), "1SAM 30:26", "#FFD23F", "A Present for You"),
         ("Beth-el · Ramoth · Jattir", v("30:27"), "1SAM 30:27", "#FFB04A", None), ("Aroer · Siphmoth · Eshtemoa", v("30:28"), "1SAM 30:28", "#FFB04A", None),
         ("Racal · the Jerahmeelites · the Kenites", v("30:29"), "1SAM 30:29", "#FFB04A", None), ("Hormah · Bor-ashan · Athach", v("30:30"), "1SAM 30:30", "#FFB04A", None),
         ("Hebron", v("30:31"), "1SAM 30:31", "#FFB04A", None)]
PG.extend(roll_pages(GIFTS, "1SA-C14-R", PG.next(), "1 Samuel", "1SAM", tag="THE PRESENTS TO THE ELDERS OF JUDAH · 1 SAMUEL 30"))
SEGS2 = [over([caps("31:1-3")], "1SAM 31:1–3", "B10", 0, head="Mount Gilboa", stamp=31),
         over([cp("31:4", to="to his armorbearer,"), say("31:4", frm="Draw thy sword,", to="abuse me."), cp("31:4", frm="But his armorbearer"), caps("31:5-6")], "1SAM 31:4–6", "B10", 1),
         drawn([caps("31:7-10")], "1SAM 31:7–10", lambda w, h: JA.burning(w, h, 1416, city="beth-shan"), "#2A0A0A"),
         drawn([caps("31:11-13")], "1SAM 31:11–13", lambda w, h: K.tamarisk_alone(w, h, 1417), "#3A2A4A", head="Under the Tamarisk-tree in Jabesh")]
PG.extend(pack(SEGS2, "1SA-C14-E", PG.next(), end=end_mark("END OF 1 SAMUEL · NEXT · 2 SAMUEL", "right: 10px; bottom: 34px", ch="完")))
