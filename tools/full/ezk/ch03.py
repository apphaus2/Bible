"""Ezekiel volume, Chapter 3 — The Glory Departs (Ezekiel 8–11). Every verse, word for word from ref/asv.
The elders of Judah in Ezekiel's house; a likeness as the appearance of fire, and the Spirit lifting him between earth and
heaven to Jerusalem; the image of jealousy at the north gate; the hole in the wall, and the chamber of imagery with the
seventy elders and their censers; the women weeping for Tammuz; the five and twenty men worshipping the sun toward the
east; the six men with their weapons and the man in linen with the inkhorn — the mark upon the foreheads; the slaughter
(9:5–7) words over the empty court, no one drawn; Ah Lord Jehovah!; the coals of fire scattered over the city from
between the cherubim; the glory over the threshold, then over the cherubim at the east gate; the five and twenty at the
east gate — this city is the caldron; Pelatiah's death words only; one heart and a new spirit; and the glory going up to
the mountain on the east side of the city. The glory is light and fire, never a figure."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from ezk import G, art3 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_FIRE, EZEKIEL_AWE, EZEKIEL_STERN, EZEKIEL_GRIEF,
                        EZEKIEL_TEAR, PELATIAH, ELDER, AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, VS = "#0B1A2E", "#1A0E1A"
C = "c"


@P("EZK-C03-00-Title", "Chapter 3 · The Glory Departs", title=True)
def title(n):
    svg = title_art(lambda w, h: K.threshold("t3", w, h, 301, east=True), "#2A2A4A")
    return chapter_title(3, "第三話", "The Glory Departs", "Ezekiel 8 – 11", svg, "#2A2A4A", v("10:18"), "Ezekiel · Volume Twenty-Six")


OV = {"8:1": C, "8:2": C, "8:3": C, "8:4": C, "8:5": (("c", None), ("g", "Son of man,"), ("c", "So I lifted")), "8:7": C,
      "8:8": (("c", None), ("g", "Son of man,"), ("c", "and when I had")), "8:10": C, "8:11": C, "8:14": C, "8:16": C,
      "9:1": (("c", None), ("g", "Cause ye")), "9:2": C, "9:3": C, "9:4": (("c", None), ("g", "Go through")),
      "9:5": (("c", None), ("g", "Go ye through")), "9:6": (("g", None), ("c", "Then they began")),
      "9:7": (("c", None), ("g", "Defile the house"), ("c", "And they went forth")), "9:8": (("c", None), ("s", "Ah Lord Jehovah!")),
      "9:11": (("c", None), ("s", "I have done")),
      "10:1": C, "10:2": (("c", None), ("g", "Go in between"), ("c", "And he went in")), "10:3": C, "10:4": C, "10:5": C,
      "10:6": (("c", None), ("g", "Take fire"), ("c", "that he went in")), **{f"10:{n}": C for n in range(7, 23)},
      "11:1": C, "11:5": (("c", None), ("g", "Speak, Thus")), "11:13": (("c", None), ("s", "Ah Lord Jehovah!")), **{f"11:{n}": C for n in range(22, 26)}}

SEGS = [drawn(wl("8:1", ov=OV), "EZEK 8:1", lambda w, h: K.elders_house("eh3", w, h, 302), "#3A2A2A", head="As I Sat in My House", stamp=8),
        drawn(wl("8:2-3", ov=OV), "EZEK 8:2–3", lambda w, h: K.lifted("lf3", w, h, 303), "#1A1A3A"),
        drawn(wl("8:4-6", ov=OV), "EZEK 8:4–6", lambda w, h: K.jealousy("jl3", w, h, 304), "#4A3A5A", head="The Image of Jealousy"),
        drawn(wl("8:7-9", ov=OV), "EZEK 8:7–9", lambda w, h: K.hole_wall("hw3", w, h, 305, door=True), "#2A2A3A", head="A Hole in the Wall"),
        drawn(wl("8:10-11", ov=OV), "EZEK 8:10–11", lambda w, h: K.imagery("im3", w, h, 306), "#1A1010"),
        fz("8:12-13", EZEKIEL_AWE, AMBER),
        drawn(wl("8:14-15", ov=OV), "EZEK 8:14–15", lambda w, h: K.tammuz("tz3", w, h, 307), "#5A4A6A", head="Weeping for Tammuz"),
        drawn(wl("8:16", ov=OV), "EZEK 8:16", lambda w, h: K.sun_worship("sw3", w, h, 308), "#3A4A7A", head="Their Faces toward the East"),
        fz("8:17-18", EZEKIEL_STERN, RED),
        drawn(wl("9:1-2", ov=OV), "EZEK 9:1–2", lambda w, h: K.six_men("sm3", w, h, 309), "#3A3A5A", head="The Man Clothed in Linen", stamp=9),
        drawn(wl("9:3-4", ov=OV), "EZEK 9:3–4", lambda w, h: K.marking("mk3", w, h, 310), "#4A4A6A"),
        drawn(wl("9:5-7", ov=OV), "EZEK 9:5–7", lambda w, h: K.empty_court(w, h, 311), "#2A1A2A"),
        drawn(wl("9:8-9", ov=OV), "EZEK 9:8–9", lambda w, h: K.fallen_court("fc3", w, h, 312), "#2A1A2A", head="Ah Lord Jehovah!"),
        face(wl("9:10-11", ov=OV), "EZEK 9:10–11", EZEKIEL_GRIEF, bg=COLD),
        drawn(wl("10:1-3", ov=OV), "EZEK 10:1–3", lambda w, h: K.coals("co3", w, h, 313), "#1A1A2A", head="Coals of Fire", stamp=10),
        drawn(wl("10:4-5", ov=OV), "EZEK 10:4–5", lambda w, h: K.threshold("th3", w, h, 314), "#2A2A4A"),
        drawn(wl("10:6-8", ov=OV), "EZEK 10:6–8", lambda w, h: K.coals("co3b", w, h, 315), "#1A1A2A"),
        drawn(wl("10:9-13", ov=OV), "EZEK 10:9–13", lambda w, h: K.vision("vw3", w, h, 316, stage="wheels"), VS, head="The Whirling Wheels"),
        drawn(wl("10:14-17", ov=OV), "EZEK 10:14–17", lambda w, h: K.creature_plan(w, h), MAP),
        drawn(wl("10:18-19", ov=OV), "EZEK 10:18–19", lambda w, h: K.threshold("th3b", w, h, 317, east=True), "#2A2A4A", head="At the Door of the East Gate"),
        drawn(wl("10:20-22", ov=OV), "EZEK 10:20–22", lambda w, h: K.vision("vl3", w, h, 318, stage="lifted"), VS),
        drawn(wl("11:1-3", ov=OV), "EZEK 11:1–3", lambda w, h: K.caldron(w, h, 319), "#2A1A2A", head="This City Is the Caldron", stamp=11),
        fz("11:4-6", EZEKIEL_STERN, RED, ov=OV),
        fz("11:7-10", EZEKIEL, GOLDEN),
        fz("11:11-12", EZEKIEL_STERN, RED),
        drawn(wl("11:13", ov=OV), "EZEK 11:13", lambda w, h: K.fallen_court("fc3b", w, h, 320), "#2A1A2A"),
        fz("11:14-16", EZEKIEL, GOLDEN, head="A Sanctuary for a Little While"),
        fz("11:17-18", EZEKIEL, GOLDEN),
        drawn(wl("11:19-21"), "EZEK 11:19–21", lambda w, h: K.hearts(w, h), MAP, head="A Heart of Flesh"),
        drawn(wl("11:22-23", ov=OV), "EZEK 11:22–23", lambda w, h: K.glory_mountain(w, h, 321), "#0B0B2A", head="The Glory Went Up"),
        drawn(wl("11:24-25", ov=OV), "EZEK 11:24–25", lambda w, h: K.speaking_captives("sc3", w, h, 322), "#2A2A5A")]
PG.extend(pack(SEGS, "EZK-C03-D", PG.next(), end=end_mark("NEXT · STUFF FOR REMOVING", "right: 10px; bottom: 34px")))
