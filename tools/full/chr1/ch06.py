"""1 Chronicles volume, Chapter 6 — The Ark of God (1 Chronicles 13–16). Every verse, word for word from ref/eng-asv.
David consults with every leader — let us bring again the ark of our God; the new cart from the house of Abinadab (the
digest's panels); the threshing-floor of Chidon (13:10 words over the cart, no one drawn) and Perez-uzza; three months in
the house of Obed-edom; Hiram's cedars, David's sons, and Baal-perazim and the sound of marching in the tops of the
mulberry-trees; then none ought to carry the ark but the Levites, the singers appointed, the ark brought up with shouting
and David dancing, Michal at the window; and David's psalm of thanks in song boxes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from sa1 import art as KS1
from sa2.common import over as over2, D as D2
from chr1 import G, art as K
from chr1.common import (pack, cp, say, gd, sg, sgs, caps, drawn, face, cell, cells, roll, joined, DAVID_KING, DAVID_WRATH, DAVID_JOY, COLD, GOLDEN, RED)
from chr1 import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
TAG15, TAG16 = "THE LEVITES AND THE SINGERS · 1 CHRONICLES 15", "BEFORE THE ARK · 1 CHRONICLES 16"


@P("1CH-C06-00-Title", "Chapter 6 · The Ark of God", title=True)
def title(n):
    bg, art = D2("A4", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFB04A"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(6, "第六話", "The Ark of God", "1 Chronicles 13 – 16", svg, "#C8702A", v("15:28", to="with sound of the cornet,"), "1 Chronicles · Volume Thirteen")


SEGS = [face([caps("13:1"), cp("13:2", to="the assembly of Israel,"), joined("say", ("13:2", "If it seem"), "13:3")], "1CHR 13:1–3", DAVID_KING, head="The Ark of God", stamp=13),
        over2([caps("13:4-6")], "1CHR 13:4–6", "A3", 0),
        over2([caps("13:7-8")], "1CHR 13:7–8", "A3", 1),
        drawn([caps("13:9-10")], "1CHR 13:9–10", lambda w, h: K.K2.nacon("nc6", w, h, 601), "#2A2A4A", head="Perez-uzza"),
        face([caps("13:11"), cp("13:12", to="saying,"), say("13:12", frm="How shall")], "1CHR 13:11–12", DAVID_WRATH, bg=COLD),
        drawn([caps("13:13-14")], "1CHR 13:13–14", below(lambda w, h: K.K2.obed_edom("oe6", w, h, 602), 0.24), "#FFE680")]
PG.extend(pack(SEGS, "1CH-C06-D", PG.next()))
SEGS2 = [drawn([caps("14:1-2")], "1CHR 14:1–2", below(lambda w, h: K.lebanon("lb6", w, h, 603), 0.26), "#8FD0E2", head="Hiram King of Tyre", stamp=14),
         drawn([caps("14:3-7")], "1CHR 14:3–7", below(lambda w, h: K.branch(w, h, "DAVID", ["SHAMMUA", "SHOBAB", "NATHAN", "SOLOMON", "IBHAR", "ELISHUA", "ELPELET", "NOGAH",
                                                                                  "NEPHEG", "JAPHIA", "ELISHAMA", "BEELIADA", "ELIPHELET"], hi=("SOLOMON",), per=7), 0.24), MAP),
         drawn([caps("14:8-9")], "1CHR 14:8–9", lambda w, h: JA.armed("rp6", w, h, 604, tribes=()), "#F3D8A0", head="Baal-perazim"),
         drawn([cp("14:10", to="saying,"), say("14:10", frm="Shall I go up", to="into my hand?"), cp("14:10", frm="And Jehovah said unto him,", to="said unto him,"), gd("14:10", frm="Go up;")],
               "1CHR 14:10", lambda w, h: KS1.ephod_inquire("ei6", w, h, 605), "#2A1A3A"),
         drawn([cp("14:11", to="and David said,"), say("14:11", frm="God hath broken", to="breach of waters."), cp("14:11", frm="Therefore they called"), caps("14:12")], "1CHR 14:11–12",
               lambda w, h: K.K2.breach(w, h, 606), "#2A3A5A"),
         drawn([caps("14:13"), cp("14:14", to="said unto him,"), joined("god", ("14:14", "Thou shalt not"), "14:15"), caps("14:16-17")], "1CHR 14:13–17",
               lambda w, h: K.K2.mulberry("mb6", w, h, 607), "#14123A", head="The Tops of the Mulberry-trees")]
PG.extend(pack(SEGS2, "1CH-C06-E", PG.next()))
SEGS3 = [drawn([caps("15:1"), cp("15:2", to="Then David said,"), say("15:2", frm="None ought")], "1CHR 15:1–2", below(lambda w, h: K.K2.tent_ark("ta6", w, h, 608), 0.36), "#FFB04A",
               head="None Ought to Carry the Ark", stamp=15)]
SEGS3 += [face([caps("15:3-4")], "1CHR 15:3–4", DAVID_KING),
          drawn([caps("15:5-10")], "1CHR 15:5–10", below(lambda w, h: K.branch(w, h, "THE LEVITES", ["URIEL", "ASAIAH", "JOEL", "SHEMAIAH",
                                                                                           "ELIEL", "AMMINADAB"]), 0.3), MAP)]
PG.extend(pack(SEGS3, "1CH-C06-F", PG.next()))
SEGS4 = [face([caps("15:11"), cp("15:12", to="and said unto them,"), joined("say", ("15:12", "Ye are the heads"), "15:13")], "1CHR 15:11–13", DAVID_KING, head="Sanctify Yourselves"),
         drawn([caps("15:14-15")], "1CHR 15:14–15", below(lambda w, h: K.ark_up("au6", w, h, 609), 0.24), "#FFE680")]
PG.extend(pack(SEGS4, "1CH-C06-G", PG.next()))
R2 = cells(15, 16, 24, "The Singers", "#FFD23F", head="The Singers", budget=560)
PG.extend(roll(R2, "1CH-C06-S", PG.next(), TAG15))
SEGS5 = [over2([caps("15:25-26")], "1CHR 15:25–26", "A3", 2, head="With Joy"),
         over2([caps("15:27-28")], "1CHR 15:27–28", "A4", 0),
         over2([caps("15:29")], "1CHR 15:29", "A4", 1),
         drawn([caps("16:1-3")], "1CHR 16:1–3", below(lambda w, h: K.K2.tent_ark("ta6b", w, h, 610), 0.3), "#FFB04A", head="In the Midst of the Tent", stamp=16),
         drawn([caps("16:4-7")], "1CHR 16:4–7", below(lambda w, h: K.singers("sg6", w, h, 616, n=7, top=0.5), 0.3), "#FFB04A")]
PG.extend(pack(SEGS5, "1CH-C06-H", PG.next()))
SEGS6 = [drawn(sgs("16:8-14"), "1CHR 16:8–14", lambda w, h: K.singers("ps6", w, h, 611, n=8, top=0.72), "#FFB04A", head="O Give Thanks unto Jehovah"),
         drawn(sgs("16:15-22"), "1CHR 16:15–22", lambda w, h: K.K2.nathan_night(w, h, 612), "#0F0E2A"),
         drawn(sgs("16:23-29"), "1CHR 16:23–29", lambda w, h: K.K2.throne_glory(w, h, 613), "#14123A"),
         drawn(sgs("16:30-33"), "1CHR 16:30–33", lambda w, h: K.K2.waves(w, h, 614), "#0B1A2E"),
         drawn(sgs("16:34-35") + [sg("16:36", to="to everlasting."), cp("16:36", frm="And all the people")], "1CHR 16:34–36",
               lambda w, h: K.night_song("ns6", w, h, 615), "#0B0B2A")]
PG.extend(pack(SEGS6, "1CH-C06-U", PG.next()))
R4 = cells(16, 37, 42, "Before the Ark Continually", "#FFD23F", head="Before the Ark Continually", budget=620) + [cell("Every Man to His House", "16:43", "#FFB04A")]
PG.extend(roll(R4, "1CH-C06-V", PG.next(), TAG16, end=end_mark("NEXT · THY THRONE FOR EVER", "right: 40px; bottom: 50px")))
