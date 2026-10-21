"""Ezekiel volume, Chapter 4 — Stuff for Removing (Ezekiel 12–14). Every verse, word for word from ref/asv.
The prophet a sign: stuff for removing brought out by day, the wall digged through in the dark and the face covered; the
prince in Jerusalem and the net spread upon him (a map: he shall not see the land of the Chaldeans); bread eaten with
quaking; the days are prolonged, and every vision faileth — the word shall be performed; the foolish prophets like foxes in
the waste places; the wall daubed with untempered mortar, the shower, the hailstones and the stormy wind, and the wall
fallen; the women that sew pillows (the things only); the elders with idols in their heart; and though Noah, Daniel and
Job were in it — the four sore judgments (a plate) — and the remnant that shall comfort you."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art4 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, ELDER, ELDER2,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C04-00-Title", "Chapter 4 · Stuff for Removing", title=True)
def title(n):
    svg = title_art(lambda w, h: K.removing("t4", w, h, 401, night=True), "#05051A")
    return chapter_title(4, "第四話", "Stuff for Removing", "Ezekiel 12 – 14", svg, "#05051A", v("12:11", to="I am your sign:"), "Ezekiel · Volume Twenty-Six")


OV = {"12:7": "c", "14:1": "c"}
SEGS = run(12, 1, 28, arts={3: ("#6AB0D8", lambda w, h: K.removing("rm4", w, h, 402)), 7: ("#05051A", lambda w, h: K.removing("rm4b", w, h, 403, night=True)),
                            12: ("#05051A", lambda w, h: K.removing("rm4c", w, h, 404, night=True)), 13: (MAP, lambda w, h: K.snare(w, h)),
                            18: ("#2A2A3A", lambda w, h: K.quaking("qk4", w, h, 405)), 20: ("#6A6A7A", lambda w, h: K.jerusalem("j4", w, h, 406, mode="empty")),
                            25: ("#1A1A2A", lambda w, h: K.sealed_vision(w, h, 407))},
           faces=FZ, ov=OV, generic=[("#2A1A3A", lambda w, h: K.jerusalem("j4g", w, h, 415, mode="dusk"))], heads={1: "Prepare Thee Stuff for Removing", 8: "I Am Your Sign", 17: "Bread with Quaking", 21: "Every Vision Faileth"})
SEGS += run(13, 1, 23, arts={4: ("#5A4A6A", lambda w, h: K.foxes(w, h, 408)), 10: ("#8FB0C8", lambda w, h: K.daubed(w, h, 409, 0)), 11: ("#1A1A2A", lambda w, h: K.daubed(w, h, 410, 1)),
                             14: ("#1A1A2A", lambda w, h: K.daubed(w, h, 411, 2)), 18: ("#1A1020", lambda w, h: K.pillows(w, h, 412))},
            faces=FZ, generic=[("#8FB0C8", lambda w, h: K.daubed(w, h, 416, 0)), ("#6A6A7A", lambda w, h: K.jerusalem("j4h", w, h, 417, mode="empty"))], heads={1: "Foxes in the Waste Places", 10: "Untempered Mortar", 17: "Woe to the Women That Sew Pillows"})
SEGS += run(14, 1, 23, arts={1: ("#3A2A2A", lambda w, h: K.elders_house("eh4", w, h, 413)), 13: (MAP, lambda w, h: K.three_men("tm4", w, h)),
                             22: ("#5A4A5A", lambda w, h: K.KK2.captives("cp4", w, h, 414, city="jerusalem"))},
            faces=FZ, ov=OV, generic=[("#3A2A2A", lambda w, h: K.elders_house("eh4b", w, h, 418)), ("#3A2A4A", lambda w, h: K.mountains(w, h, 419, "idols")),
                                       ("#6A6A7A", lambda w, h: K.jerusalem("j4i", w, h, 420, mode="empty"))], heads={1: "Idols in Their Heart", 12: "Noah, Daniel, and Job", 21: "Yet There Shall Be Left a Remnant"})
PG.extend(pack(SEGS, "EZK-C04-D", PG.next(), end=end_mark("NEXT · THE VINE AND THE FOUNDLING", "right: 10px; bottom: 34px")))
