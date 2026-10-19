"""Ezekiel volume, Chapter 10 â€” The Ship of Tyre (Ezekiel 26â€“28). Every verse, word for word from ref/asv.
Tyre that said Aha against Jerusalem: the city on her rock in the sea, Nebuchadrezzar's forts and horsemen on the shore,
the walls broken and the rock made bare for the spreading of nets (no one drawn); the princes of the sea come down from
their thrones; then the lamentation over Tyre (27:3â€“36) in song boxes, Tyre as a ship: the ship as a blueprint plate (the
planks of Senir, the cedar mast, the oars of Bashan, the linen sail of Egypt), her traffickers as a map, the ship broken
by the east wind in the heart of the seas, and the mariners lamenting on the shore; the prince of Tyre â€” I sit in the
seat of God, in the midst of the seas (an empty throne on the rock); the lamentation over the king of Tyre and the stones
of Eden (a plate); the fire from the midst; Sidon; and Israel dwelling securely."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art10 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, SKY = "#0B1A2E", "#6AB0D8"
T = lambda mode, seed: (SKY if mode == "day" else "#5A4A5A" if mode == "siege" else "#8A9AB0" if mode == "ruin" else "#2A0A0A", lambda w, h: K.tyre(w, h, seed, mode))


@P("EZK-C10-00-Title", "Chapter 10 Â· The Ship of Tyre", title=True)
def title(n):
    svg = title_art(lambda w, h: K.tyre(w, h, 1001, "day"), SKY)
    return chapter_title(10, "ç¬¬åè©±", "The Ship of Tyre", "Ezekiel 26 â€“ 28", svg, "#2A4A6A", v("27:3", frm="Thou, O Tyre,"), "Ezekiel Â· Volume Twenty-Six")


SEGS = run(26, 1, 21, arts={2: T("day", 1002), 7: T("siege", 1003), 10: T("siege", 1004), 12: T("burning", 1005), 14: T("ruin", 1006),
                            16: ("#4A4A6A", lambda w, h: K.mariners("mr10", w, h, 1007)), 19: T("ruin", 1008)},
           faces=FZ, heads={1: "Behold, I Am against Thee, O Tyre", 7: "Nebuchadrezzar King of Babylon", 15: "Shall Not the Isles Shake?"})
SEGS += run(27, 1, 36, arts={3: T("day", 1009), 5: (MAP, lambda w, h: K.ship_plate(w, h)), 10: T("day", 1010),
                             12: (MAP, lambda w, h: K.trade_map(w, h, hi=("TARSHISH", "JAVAN", "TUBAL", "MESHECH", "TOGARMAH", "DEDAN"))),
                             16: (MAP, lambda w, h: K.trade_map(w, h, hi=("SYRIA", "JUDAH Â· ISRAEL", "DAMASCUS", "VEDAN", "DEDAN"))),
                             21: (MAP, lambda w, h: K.trade_map(w, h, hi=("ARABIA Â· KEDAR", "SHEBA Â· RAAMAH", "HARAN", "CANNEH Â· EDEN", "ASSHUR Â· CHILMAD"))),
                             26: ("#1A1A2A", lambda w, h: K.shipwreck(w, h, 1011)), 29: ("#4A4A6A", lambda w, h: K.mariners("mr10b", w, h, 1012)),
                             33: (MAP, lambda w, h: K.trade_map(w, h)), 35: T("ruin", 1013)},
            faces=[(EZEKIEL_GRIEF, COLD), (EZEKIEL, GOLDEN)], ov={f"27:{n}": "n" for n in range(3, 37)}, budget=440,
            heads={1: "A Lamentation over Tyre", 5: "Perfect in Beauty", 12: "Thy Traffickers", 26: "Broken in the Heart of the Seas", 32: "Who Is There like Tyre?"})
SEGS += run(28, 1, 26, arts={2: ("#6AB0D8", lambda w, h: K.seat_of_god(w, h, 1014)), 7: T("siege", 1015), 12: (MAP, lambda w, h: K.eden_stones(w, h)),
                             16: ("#2A0A0A", lambda w, h: K.fire_midst(w, h, 1016)), 21: ("#7AA8C8", lambda w, h: K.tyre(w, h, 1017, "sidon")),
                             25: ("#6AB0D8", lambda w, h: K.gathered(w, h, 1018))},
            faces=FZ, heads={1: "The Prince of Tyre", 11: "The King of Tyre", 20: "Set Thy Face toward Sidon", 25: "They Shall Dwell Securely"})
PG.extend(pack(SEGS, "EZK-C10-D", PG.next(), end=end_mark("NEXT Â· PHARAOH KING OF EGYPT", "right: 10px; bottom: 34px")))
