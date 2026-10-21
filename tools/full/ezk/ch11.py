"""Ezekiel volume, Chapter 11 — Pharaoh King of Egypt (Ezekiel 29–32). Every verse, word for word from ref/asv.
Pharaoh the great monster in the midst of his rivers (a crocodile in the Nile): hooks in his jaws, cast forth into the
wilderness; the staff of reed; Egypt desolate from Migdol to Syene (a map), and gathered after forty years, the basest of
the kingdoms; Egypt given to Nebuchadrezzar for his service against Tyre; a horn to bud forth; the day of Jehovah, a day of
clouds; the ships to Ethiopia; the cities of Egypt set on fire (the map lit); the arms of Pharaoh broken and the sword in
the hand of the king of Babylon (a plate, no wound drawn); the Assyrian a cedar in Lebanon, felled and gone down to Sheol;
the lamentation over Pharaoh — the net spread, the heavens made dark; and the pit, the nations' graves round about it,
Asshur, Elam, Meshech and Tubal, Edom, the princes of the north and the Sidonians (a plate, names only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art11 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NILE = "#0B1A2E", "#E8A060"
CITIES = ("PATHROS", "ZOAN", "NO", "SIN", "MEMPHIS", "AVEN", "PI-BESETH", "TEHAPHNEHES")


@P("EZK-C11-00-Title", "Chapter 11 · Pharaoh King of Egypt", title=True)
def title(n):
    svg = title_art(lambda w, h: K.nile_scene(w, h, 1101), NILE)
    return chapter_title(11, "第十一話", "Pharaoh King of Egypt", "Ezekiel 29 – 32", svg, "#5A3A1A", v("29:3", frm="the great monster"), "Ezekiel · Volume Twenty-Six")


SEGS = run(29, 1, 21, arts={3: (NILE, lambda w, h: K.nile_scene(w, h, 1102)), 4: (NILE, lambda w, h: K.nile_scene(w, h, 1103, hooks=True, fish=True)),
                            5: ("#C8803A", lambda w, h: K.nile_scene(w, h, 1104, desert=True)), 6: ("#8AB0C8", lambda w, h: K.reed_staff(w, h, 1105)),
                            10: (MAP, lambda w, h: K.egypt_map(w, h, hi=("MIGDOL", "SYENE", "ETHIOPIA"))), 12: ("#C8803A", lambda w, h: K.egypt_waste(w, h, 1106)),
                            14: (MAP, lambda w, h: K.egypt_map(w, h, hi=("PATHROS",))), 18: ("#5A4A5A", lambda w, h: K.tyre(w, h, 1107, "siege")),
                            21: ("#3A4A7A", lambda w, h: K.horn_bud(w, h, 1108))},
           faces=FZ, heads={1: "The Great Monster", 6: "A Staff of Reed", 13: "At the End of Forty Years", 17: "His Recompense"})
SEGS += run(30, 1, 26, arts={2: ("#1A1A2A", lambda w, h: K.day_clouds(w, h, 1109)), 5: (MAP, lambda w, h: K.egypt_map(w, h, hi=("ETHIOPIA",))),
                             9: ("#C8803A", lambda w, h: K.ships_ethiopia(w, h, 1110)), 10: ("#5A4A5A", lambda w, h: K.army("ar11", w, h, 1111)),
                             12: ("#C8803A", lambda w, h: K.egypt_waste(w, h, 1112)), 14: (MAP, lambda w, h: K.egypt_map(w, h, hi=CITIES)),
                             21: (MAP, lambda w, h: K.arms_plate(w, h)), 24: ("#0B0B1A", lambda w, h: K.sword(w, h, 1113))},
            faces=FZ, heads={1: "Alas for the Day!", 10: "By the Hand of Nebuchadrezzar", 13: "I Will Set a Fire in Egypt", 20: "I Have Broken the Arm of Pharaoh"})
SEGS += run(31, 1, 18, arts={3: ("#5A9AD0", lambda w, h: K.great_cedar(w, h, 1114)), 7: ("#5A9AD0", lambda w, h: K.great_cedar(w, h, 1115)),
                             12: ("#5A5A6A", lambda w, h: K.great_cedar(w, h, 1116, felled=True)), 15: ("#05050A", lambda w, h: K.darkened(w, h, 1117)),
                             18: ("#5A5A6A", lambda w, h: K.great_cedar(w, h, 1118, felled=True))},
            faces=FZ, heads={1: "Whom Art Thou Like in Thy Greatness?", 10: "Because Thou Art Exalted in Stature", 15: "In the Day When He Went Down to Sheol"})
SEGS += run(32, 1, 32, arts={2: (NILE, lambda w, h: K.nile_scene(w, h, 1119)), 3: (NILE, lambda w, h: K.nile_scene(w, h, 1120, net=True)), 7: ("#05050A", lambda w, h: K.darkened(w, h, 1121)),
                             11: ("#0B0B1A", lambda w, h: K.sword(w, h, 1122)), 13: ("#C8803A", lambda w, h: K.egypt_waste(w, h, 1123)),
                             18: (MAP, lambda w, h: K.pit_plate(w, h, hi=())), 22: (MAP, lambda w, h: K.pit_plate(w, h, hi=("ASSHUR",))),
                             24: (MAP, lambda w, h: K.pit_plate(w, h, hi=("ELAM",))), 26: (MAP, lambda w, h: K.pit_plate(w, h, hi=("MESHECH · TUBAL",))),
                             29: (MAP, lambda w, h: K.pit_plate(w, h, hi=("EDOM",))), 30: (MAP, lambda w, h: K.pit_plate(w, h, hi=("THE PRINCES OF THE NORTH", "THE SIDONIANS"))),
                             32: (MAP, lambda w, h: K.pit_plate(w, h))},
            faces=FZ + [(EZEKIEL_GRIEF, COLD)], heads={1: "A Lamentation over Pharaoh", 11: "The Sword of the King of Babylon", 17: "Wail for the Multitude of Egypt",
                                                     22: "Asshur Is There", 24: "There Is Elam", 29: "There Is Edom"})
PG.extend(pack(SEGS, "EZK-C11-D", PG.next(), end=end_mark("NEXT · THE WATCHMAN AND THE SHEPHERDS", "right: 10px; bottom: 34px")))
