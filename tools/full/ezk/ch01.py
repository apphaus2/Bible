"""Ezekiel volume, Chapter 1 — The Visions of God (Ezekiel 1–3). Every verse, word for word from ref/asv.
Among the captives by the river Chebar the heavens were opened; the stormy wind out of the north and the fire infolding
itself; the four living creatures (bronze figures in the fire, four wings) and a plate of their faces; the wheels with
their rims full of eyes; the firmament like the terrible crystal; the throne of sapphire, and above it only fire and
glowing metal and the bow round about (no figure drawn); Son of man, stand upon thy feet; the roll of a book (no hand
drawn) — eat this roll; the forehead made hard as adamant; the great rushing, and Tel-abib seven days; the watchman; the
plain, and shut thyself within thy house."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from ezk import G, art as K
from ezk.common import (title_art, pack, cp, say, gd, sg, says, gods, caps, drawn, face, joined, wl, fz, dz, run, label,
                        EZEKIEL, EZEKIEL_FIRE, EZEKIEL_AWE, EZEKIEL_STERN, EZEKIEL_GRIEF, NIGHT, AMBER, COLD, GOLDEN, RED)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
VS = "#1A0E1A"


@P("EZK-C01-00-Title", "Chapter 1 · The Visions of God", title=True)
def title(n):
    svg = title_art(lambda w, h: K.vision("t1", w, h, 101, stage="wheels"), "#0B0B1A")
    return chapter_title(1, "第一話", "The Visions of God", "Ezekiel 1 – 3", svg, "#0B0B1A", v("1:1", frm="the heavens were opened"), "Ezekiel · Volume Twenty-Six")


SEGS = [drawn([caps("1:1-3")], "EZEK 1:1–3", lambda w, h: K.chebar("cb1", w, h, 102), "#2A2A5A", k=0.3, head="By the River Chebar", stamp=1),
        drawn([caps("1:4")], "EZEK 1:4", lambda w, h: K.storm(w, h, 103), "#0B0B1A", k=0.24, head="A Stormy Wind out of the North"),
        drawn([caps("1:5-9")], "EZEK 1:5–9", lambda w, h: K.vision("vc1", w, h, 104), VS, k=0.28, head="Four Living Creatures"),
        drawn([caps("1:10-12")], "EZEK 1:10–12", lambda w, h: K.creature_plan(w, h), "#0B1A2E", k=0.3),
        drawn([caps("1:13-14")], "EZEK 1:13–14", lambda w, h: K.vision("vc2", w, h, 105), VS, k=0.2),
        drawn([caps("1:15-18")], "EZEK 1:15–18", lambda w, h: K.vision("vw1", w, h, 106, stage="wheels"), VS, k=0.3, head="A Wheel within a Wheel"),
        drawn([caps("1:19-21")], "EZEK 1:19–21", lambda w, h: K.vision("vl1", w, h, 107, stage="lifted"), VS, k=0.3),
        drawn([caps("1:22-25")], "EZEK 1:22–25", lambda w, h: K.vision("vf1", w, h, 108, stage="firmament"), VS, k=0.32, head="The Terrible Crystal"),
        drawn([caps("1:26-28")], "EZEK 1:26–28", lambda w, h: K.throne(w, h, 109, fall=True), "#05051A", k=0.3, head="The Likeness of the Glory of Jehovah"),
        face(wl("2:1-2", ov={"2:2": [cp("2:2")]}), "EZEK 2:1–2", EZEKIEL_AWE, bg=AMBER, head="Son of Man, Stand upon Thy Feet", stamp=2),
        fz("2:3-5", EZEKIEL_FIRE, AMBER),
        dz("2:6-7", lambda w, h: K.briers(w, h, 110), "#C88A5A", k=0.4),
        fz("2:8", EZEKIEL, GOLDEN),
        drawn([caps("2:9-10")], "EZEK 2:9–10", lambda w, h: K.roll(w, h, 111), "#1A1030", k=0.2, head="A Roll of a Book"),
        face(wl("3:1-3", ov={"3:2": [cp("3:2")], "3:3": [cp("3:3", to="And he said unto me,"), gd("3:3", frm="Son of man,", to="I give thee."), cp("3:3", frm="Then did I eat it;")]}),
             "EZEK 3:1–3", EZEKIEL_FIRE, bg=AMBER, stamp=3),
        fz("3:4-7", EZEKIEL, GOLDEN, head="Speak with My Words unto Them"),
        fz("3:8-9", EZEKIEL_STERN, RED),
        fz("3:10-11", EZEKIEL, GOLDEN),
        drawn([cp("3:12", to="saying,"), sg("3:12", frm="Blessed be"), caps("3:13-14")], "EZEK 3:12–14", lambda w, h: K.vision("vl3", w, h, 112, stage="lifted"), VS, k=0.34,
              head="The Voice of a Great Rushing"),
        drawn([caps("3:15")], "EZEK 3:15", lambda w, h: K.tel_abib("ta1", w, h, 113), "#4A3A6A", k=0.2),
        dz("3:16-19", lambda w, h: K.watchman("wm1", w, h, 114), "#1A1A3A", k=0.36, head="I Have Made Thee a Watchman"),
        fz("3:20-21", EZEKIEL_STERN, RED),
        drawn(wl("3:22-23", ov={"3:22": [cp("3:22", to="said unto me,"), gd("3:22", frm="Arise,")], "3:23": [cp("3:23")]}), "EZEK 3:22–23", lambda w, h: K.plain_glory("pg1", w, h, 115), "#2A2A4A", k=0.3, head="Go Forth into the Plain"),
        drawn(wl("3:24", ov={"3:24": [cp("3:24", to="said unto me,"), gd("3:24", frm="Go, shut")]}) + wl("3:25-27"), "EZEK 3:24–27", lambda w, h: K.shut_house("sh1", w, h, 116),
              "#1A1A3A", k=0.36)]
PG.extend(pack(SEGS, "EZK-C01-D", PG.next(), end=end_mark("NEXT · THE SIEGE ON A TILE", "right: 10px; bottom: 34px")))
