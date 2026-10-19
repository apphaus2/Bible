"""Jeremiah volume, Chapter 19 — The Fall of Jerusalem (Jeremiah 52), the last chapter of Jeremiah. Every verse, word for word
from ref/asv. The fall retold: Zedekiah's reign; the forts built round about; the famine sore in the city; the breach and the
flight by the gate between the two walls; Riblah (52:10–11 and 52:24–27 words over the empty plain and the map); the house of
Jehovah and every great house burned (words over the burning city, no one drawn); the walls broken down; the captives; the
brass of the pillars, the sea and the bases broken and carried to Babylon, and Jachin and Boaz measured as a blueprint; the
people carried away, a tally board; and in the seven and thirtieth year Evil-merodach lifted up the head of Jehoiachin, changed
his prison garments, and he did eat bread before him continually all the days of his life. (Reuses 2 Kings' drawings: kg2.art
siege_forts, burning_city, captives, brass_carried, prison_garments.)"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art13 as K, art7 as K7
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, ZEDEKIAH, JEHOIACHIN, NEBUZARADAN, GOLDEN, COLD, RED, NIGHT
from jer import ch18 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
INK = "#0B1A2E"
RIBLAH = (MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "RIBLAH", "HAMATH", "DAMASCUS"), hi=("RIBLAH",), arrows=[("JERUSALEM", "RIBLAH")], box=(33.0, 39.0, 30.8, 35.6)))


@P("JER-C19-00-Title", "Chapter 19 · The Fall of Jerusalem", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.burning_city(760, 780, 1901)}</g><rect x="0" y="0" width="760" height="302" fill="#2A0A0A"></rect>')
    return chapter_title(19, "第十九話", "The Fall of Jerusalem", "Jeremiah 52", svg, "#2A0A0A", v("52:13", to="burned he with fire."), "Jeremiah · Volume Twenty-Four")


SEGS = [O("52:1-3", kind="cap", t=(ZEDEKIAH, COLD), head="Zedekiah Rebelled against the King of Babylon", stamp=52),
        O("52:4-5", kind="cap", a=("#5A4A5A", lambda w, h: K.siege_forts("sf19", w, h, 1902)), k=0.3, head="They Built Forts against It"),
        O("52:6", kind="cap", a=("#0E0C1E", lambda w, h: K7.siege_night(w, h, 1903)), k=0.24),
        O("52:7", kind="cap", a=("#0E0C1E", lambda w, h: K.flight("fl19", w, h, 1904)), k=0.3),
        O("52:8-9", kind="cap", a=RIBLAH, k=0.3),
        O("52:10-11", kind="cap", a=("#2A1A2A", lambda w, h: K.riblah(w, h, 1905)), k=0.3, head="Riblah in the Land of Hamath"),
        O("52:12-13", kind="cap", a=("#2A0A0A", lambda w, h: K.burning_city(w, h, 1906)), k=0.3, head="He Burned the House of Jehovah"),
        O("52:14", kind="cap", a=("#5A4A5A", lambda w, h: K.wall_breach(w, h, 1907)), k=0.24),
        O("52:15-16", kind="cap", a=("#5A4A5A", lambda w, h: K.captives("cp19", w, h, 1908, city="jerusalem")), k=0.3),
        O("52:17-19", kind="cap", a=("#5A3A2A", lambda w, h: K.brass_carried("bc19", w, h, 1909)), k=0.36, head="The Brass of Them to Babylon"),
        O("52:20-23", kind="cap", a=(INK, lambda w, h: K.pillar_elev(w, h, names=True)), k=0.42),
        O("52:24-25", kind="cap", t=(NEBUZARADAN, GOLDEN)),
        O("52:26-27", kind="cap", a=RIBLAH, k=0.24),
        O("52:28-30", kind="cap", a=("#1A1430", lambda w, h: K.tally(w, h, [("YEAR SEVEN", "3,023", "#FFD23F"), ("YEAR EIGHTEEN", "832", "#8FD0E2"),
                                                                              ("YEAR TWENTY-THREE", "745", "#FF8A6A")], "ALL THE PERSONS WERE FOUR THOUSAND AND SIX HUNDRED")), k=0.34,
          head="The People Whom Nebuchadrezzar Carried Away"),
        O("52:31", kind="cap", t=(JEHOIACHIN, GOLDEN), head="He Lifted Up the Head of Jehoiachin"),
        O("52:32-34", kind="cap", a=("#5A3A2A", lambda w, h: K.prison_garments("pg19", w, h, 1910)), k=0.3)]
PG.extend(pack(SEGS, "JER-C19-D", PG.next(), end=end_mark("END OF JEREMIAH · NEXT · LAMENTATIONS", "right: 10px; bottom: 34px", ch="完")))
