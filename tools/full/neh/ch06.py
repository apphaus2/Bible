"""Nehemiah volume, Chapter 6 — The Sealed Covenant (Nehemiah 10–11). Every verse, word for word from ref/asv.
They that sealed: Nehemiah the governor, the priests, the Levites and the chiefs of the people (roll cells under the
sealing of the covenant); the rest of the people entering into a curse and an oath — we will not give our daughters unto
the peoples of the land, nor buy on the sabbath; the third part of a shekel (a blueprint); the wood-offering by lot; the
first-fruits and the firstborn; the tithe of the tithes — we will not forsake the house of our God; then one of ten cast by
lot to dwell in Jerusalem the holy city (a lot board); the chiefs that dwelt in Jerusalem — Judah, Benjamin, the priests,
the Levites, the porters (a tally board over roll cells); and the villages of Judah and Benjamin (a map)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from neh import G, art as K
from neh.common import pack, cp, say, says, caps, drawn, face, COLD, GOLDEN, RED, plan_pages
from neh import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD, SKY = "#0B1A2E", "#1A1430", "#8FD0E2"
GOLD_C, CYAN_C, ROSE_C, LILAC = "#FFD23F", "#8FD0E2", "#FF8A6A", "#C8A0E8"


@P("NEH-C06-00-Title", "Chapter 6 · The Sealed Covenant", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.sealed_scroll(760, 640, 601)}</g><rect x="0" y="0" width="760" height="332" fill="#2A1A2A"></rect>'
                '<rect x="0" y="968" width="760" height="120" fill="#2A1A2A"></rect>')
    return chapter_title(6, "第六話", "The Sealed Covenant", "Nehemiah 10 – 11", svg, "#2A1A2A", v("10:39", frm="and we will not forsake"), "Nehemiah · Volume Sixteen")


SEALED = [("Those That Sealed", lambda w, h: K.sealing("sl6", w, h, 602), 300,
           [("Nehemiah the Governor and the Priests", "10:1-8", GOLD_C), ("The Levites", "10:9-13", CYAN_C), ("The Chiefs of the People", "10:14-27", ROSE_C)])]
PG.extend(plan_pages(SEALED, "NEH-C06-D", PG.next(), tag="THEY THAT SEALED · NEHEMIAH 10", stamp=10))
SEGS = [drawn([caps("10:28-29")], "NEH 10:28–29", below(lambda w, h: K.oath("oa6", w, h, 604), 0.4), "#FFB04A", head="A Curse and an Oath"),
        drawn([caps("10:30-31")], "NEH 10:30–31", below(lambda w, h: K.sabbath_gate("sg6", w, h, 605, shut=False), 0.36), "#3A2A5A"),
        drawn([caps("10:32-33")], "NEH 10:32–33", below(lambda w, h: K.shekel(w, h), 0.4), MAP, head="For the House of Our God"),
        drawn([caps("10:34")], "NEH 10:34", below(lambda w, h: K.wood_bearers("wb6", w, h, 606), 0.4), SKY),
        drawn([caps("10:35-37")], "NEH 10:35–37", below(lambda w, h: K.firstfruits("ff6", w, h, 607), 0.5), "#FFC890"),
        drawn([caps("10:38-39")], "NEH 10:38–39", below(lambda w, h: K.heaps("hp6", w, h, 608), 0.46), SKY)]
PG.extend(pack(SEGS, "NEH-C06-E", PG.next()))
DWELT = [("One of Ten", lambda w, h: K.lot_grid(w, h, ["JERUSALEM"] + ["THE OTHER CITIES"] * 9, lit=[0], cols=5), 240,
          [("One of Ten", "11:1-2", GOLD_C), ("The Children of Judah", "11:3-6", GOLD_C), ("The Children of Benjamin", "11:7-9", CYAN_C)]),
         ("They That Dwelt in Jerusalem", lambda w, h: K.tally_grid(w, h, [("THE SONS OF PEREZ", "468", GOLD_C), ("BENJAMIN", "928", CYAN_C), ("THE PRIESTS", "822", ROSE_C),
                                                                            ("CHIEFS OF FATHERS' HOUSES", "242", ROSE_C), ("MIGHTY MEN OF VALOR", "128", ROSE_C), ("THE LEVITES", "284", LILAC),
                                                                            ("THE PORTERS", "172", "#9CCB5E")], 4, "IN JERUSALEM THE HOLY CITY"), 260,
          [("The Priests", "11:10-14", ROSE_C), ("The Levites", "11:15-18", LILAC)]),
         ("The Porters and the Nethinim", lambda w, h: K.watch_night("wn6", w, h, 610), 240,
          [("The Porters and the Nethinim", "11:19-21", "#9CCB5E"), ("The Overseer of the Levites", "11:22-24", LILAC)]),
         ("The Villages", lambda w, h: K.villages_map(w, h), 380,
          [("The Villages of Judah", "11:25-30", GOLD_C), ("The Children of Benjamin", "11:31-36", CYAN_C)])]
PG.extend(plan_pages(DWELT, "NEH-C06-F", PG.next(), tag="THEY THAT DWELT · NEHEMIAH 11", stamp=11, end=end_mark("NEXT · THE DEDICATION OF THE WALL", "right: 10px; bottom: 34px")))
