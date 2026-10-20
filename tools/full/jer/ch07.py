"""Jeremiah volume, Chapter 7 — The Earthen Bottle (Jeremiah 19–22). Every verse, word for word from ref/eng-asv.
The potter's earthen bottle carried to the gate Harsith over the valley of the son of Hinnom, and broken before the elders
(19:7–9, the siege and its distress, words over Topheth and the walls at night); Pashhur and the stocks in the upper gate of
Benjamin — Magor-missabib; thou hast persuaded me, and I was persuaded; a burning fire shut up in my bones; cursed be the day;
Zedekiah's embassy and the way of life and the way of death; go down to the house of the king; Shallum carried away; woe unto
him that buildeth his house by unrighteousness; the burial of an ass beyond the gates (words over the empty slope); Coniah,
the signet plucked off, a despised broken vessel; O earth, earth, earth."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art7 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PASHHUR, PRIEST, GOLDEN, COLD, RED, NIGHT
from jer import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W1, G1, S1, C1, A1 = (jer(1, "word"), GOLDEN), (jer(1, "grief"), COLD), (jer(1, "stern"), RED), (jer(1, "calm"), GOLDEN), (jer(1, "afraid"), COLD)
MAP = "#0B1A2E"


@P("JER-C07-00-Title", "Chapter 7 · The Earthen Bottle", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.bottle_gate("t7", 760, 780, 701, broken=True)}</g><rect x="0" y="0" width="760" height="302" fill="#5A3A4A"></rect>')
    return chapter_title(7, "第七話", "The Earthen Bottle", "Jeremiah 19 – 22", svg, "#5A3A4A", v("19:11", frm="Even so will I break", to="made whole again;"), "Jeremiah · Volume Twenty-Four")


SEGS = [S(cut("19:1", "Thus said Jehovah,") + [gd("19:2")], "19:1-2", a=("#5A3A4A", lambda w, h: K.bottle_gate("bg7", w, h, 702)), k=0.34, head="A Potter's Earthen Bottle", stamp=19),
        O("19:3-4", t=S1),
        O("19:5-6", a=("#1A0A12", lambda w, h: K.topheth(w, h, 703)), head="The Valley of Slaughter"),
        O("19:7-8", t=S1),
        O("19:9", a=("#0E0C1E", lambda w, h: K.siege_night(w, h, 704)), k=0.34),
        O("19:10-11", a=("#5A3A4A", lambda w, h: K.bottle_gate("bg7b", w, h, 705, broken=True)), k=0.38, head="Even So Will I Break This People"),
        O("19:12-13", a=("#14122A", lambda w, h: K.roofs_incense(w, h, 706))),
        S([cp("19:14"), gd("19:15")], "19:14-15", a=("#8FB0C8", lambda w, h: K.court_people("cp7", w, h, 707)))]


SEGS2 = [O("20:1-2", kind="cap", a=("#C8A878", lambda w, h: K.stocks("st7", w, h, 708)), k=0.26, head="The Stocks in the Gate of Benjamin", stamp=20),
         S(cut("20:3", "Then said Jeremiah unto him,", "cap", "say"), "20:3", t=S1),
         O("20:4", t=S1),
         O("20:5-6", a=("#5A4A5A", lambda w, h: K.captives("cp7b", w, h, 709, city="jerusalem"))),
         O("20:7-8", kind="say", t=G1, head="Thou Hast Persuaded Me"),
         O("20:9", kind="say", a=("#14080A", lambda w, h: K.fire_bones(w, h, 710)), k=0.3),
         O("20:10-11", kind="say", t=A1),
         O("20:12-13", kind="say", t=C1),
         O("20:14-16", kind="say", a=("#2A2A3A", lambda w, h: K.cursed_day(w, h, 711)), head="Cursed Be the Day"),
         O("20:17-18", kind="say", t=G1)]


SEGS3 = [S([cp("21:1"), say("21:2")], "21:1-2", t=(PRIEST, GOLDEN), head="Zedekiah Sent unto Him", stamp=21),
         S(cut("21:3", "Then said Jeremiah unto them,", "cap", "say") + [gd("21:4")], "21:3-4", a=("#5A4A5A", lambda w, h: K.siege_forts("sf7", w, h, 712))),
         O("21:5-6", t=S1),
         O("21:7", a=("#0E0C1E", lambda w, h: K.siege_night(w, h, 713))),
         O("21:8-9", a=("#5A4A5A", lambda w, h: K.two_ways(w, h, 714)), k=0.42, head="The Way of Life and the Way of Death"),
         O("21:10", a=("#2A0A0A", lambda w, h: K.burning_city(w, h, 715)), k=0.3),
         O("21:11-12", t=W1, head="O House of David"),
         O("21:13-14", a=("#2A0A0A", lambda w, h: K.forest_fire(w, h, 716)))]


SEGS4 = [S(cut("22:1", "Thus said Jehovah:") + [gd("22:2")], "22:1-2", a=("#8FB0C8", lambda w, h: K.palace("pa7", w, h, 717)), k=0.34, head="Go Down to the House of the King", stamp=22),
         O("22:3-4", t=W1),
         O("22:5-7", a=("#3A1A1A", lambda w, h: K.cedars_fire("cf7", w, h, 718))),
         O("22:8-9", a=("#8A8A9A", lambda w, h: K.passers("ps7", w, h, 719)), k=0.36),
         O("22:10-12", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "EGYPT", "NOPH"), hi=("EGYPT",), arrows=[("JERUSALEM", "NOPH")], box=(29.0, 38.5, 26.5, 34.5))), k=0.46,
           head="Weep Sore for Him That Goeth Away"),
         O("22:13-14", a=("#8FB0C8", lambda w, h: K.cedar_house("ch7", w, h, 720)), head="Woe unto Him That Buildeth His House by Unrighteousness"),
         O("22:15-17", t=S1),
         O("22:18-19", a=("#6A5A5A", lambda w, h: K.beyond_gates(w, h, 721)), head="The Burial of an Ass"),
         O("22:20-21", a=("#6A8AB0", lambda w, h: K.lebanon_nest(w, h, 722))),
         O("22:22-23", t=S1),
         O("22:24-25", a=("#1A1428", lambda w, h: K.signet(w, h, 723)), k=0.36, head="Coniah"),
         O("22:26-28", a=("#5A4A5A", lambda w, h: K.broken_vessel(w, h, 724))),
         O("22:29-30", a=("#5A3A2A", lambda w, h: K.empty_throne(w, h, 725)), k=0.3)]
PG.extend(pack(SEGS + SEGS2 + SEGS3 + SEGS4, "JER-C07-D", PG.next(), end=end_mark("NEXT · THE CUP OF THE WINE OF WRATH", "right: 10px; bottom: 34px")))
