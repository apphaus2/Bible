"""Jeremiah volume, Chapter 6 — The Potter's House (Jeremiah 16–18). Every verse, word for word from ref/eng-asv.
Thou shalt not take thee a wife; enter not into the house of mourning, nor the house of feasting (the prophet passing alone
at night); from the land of the north; many fishers and many hunters; the sin of Judah written with a pen of iron; cursed is
the man that trusteth in man, like the heath in the desert, and blessed the man that trusteth in Jehovah, a tree by the
waters; the partridge on eggs she hath not laid; heal me, O Jehovah; the sabbath in the gates; then the potter's house — the
vessel marred in his hand, and made again; the snow of Lebanon; let us devise devices against Jeremiah; they have digged a pit."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art6 as K, art5 as K5
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PEOPLE, GOLDEN, COLD, RED, NIGHT
from jer import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W1, G1, S1, C1, A1 = (jer(1, "word"), GOLDEN), (jer(1, "grief"), COLD), (jer(1, "stern"), RED), (jer(1, "calm"), GOLDEN), (jer(1, "afraid"), COLD)
MAP = "#0B1A2E"
POT = "#7A5A3A"


@P("JER-C06-00-Title", "Chapter 6 · The Potter's House", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.potter("t6", 760, 820, 601, prophet=False)}</g><rect x="0" y="0" width="760" height="262" fill="#7A5A3A"></rect>')
    return chapter_title(6, "第六話", "The Potter's House", "Jeremiah 16 – 18", svg, "#5A3A22", v("18:6", frm="Behold, as the clay"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([cp("16:1"), gods("16:2-3")], "16:1-3", t=W1, head="Thou Shalt Not Take Thee a Wife", stamp=16),
        O("16:4", a=("#2A1A2A", lambda w, h: K5.circling(w, h, 602))),
        O("16:5-6", a=("#14122A", lambda w, h: K.two_doors("td6", w, h, 603)), head="The House of Mourning"),
        O("16:7-8", a=("#14122A", lambda w, h: K.two_doors("td6b", w, h, 604, feast=True))),
        O("16:9", t=S1),
        O("16:10-11", t=W1),
        O("16:12-13", t=S1),
        O("16:14-15", a=(MAP, lambda w, h: K.return_map(w, h)), k=0.42, head="From the Land of the North"),
        O("16:16-17", a=("#8FB0C8", lambda w, h: K.fishers_hunters("fh6", w, h, 605)), head="Many Fishers and Many Hunters"),
        O("16:18", t=S1),
        S([say("16:19"), say("16:20"), gd("16:21")], "16:19-21", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "EGYPT", "BABYLON", "TYRE", "ELAM", "ARABIA"), hi=(),
                                                                                                      arrows=[("EGYPT", "JERUSALEM"), ("BABYLON", "JERUSALEM"), ("ARABIA", "JERUSALEM"), ("TYRE", "JERUSALEM")],
                                                                                                      lit="#FFD23F", box=(29.5, 49.6, 25.6, 37.6))), k=0.46)]
PG.extend(pack(SEGS, "JER-C06-D", PG.next()))

SEGS2 = [O("17:1-2", a=("#2A2228", lambda w, h: K.iron_pen(w, h, 606)), k=0.34, head="With a Pen of Iron", stamp=17),
         O("17:3-4", t=S1),
         O("17:5-6", a=("#E8A060", lambda w, h: K.heath(w, h, 607)), k=0.36, head="Cursed Is the Man That Trusteth in Man"),
         O("17:7-8", a=("#8FC0E0", lambda w, h: K.tree_waters(w, h, 608)), k=0.34, head="Blessed Is the Man That Trusteth in Jehovah"),
         O("17:9-10", t=W1),
         O("17:11", a=("#C8A880", lambda w, h: K.partridge(w, h, 609)), k=0.28),
         O("17:12-13", kind="say", a=("#3A3A7A", lambda w, h: K.glorious_throne(w, h, 610)), k=0.36),
         O("17:14-16", kind="say", t=G1, head="Heal Me, O Jehovah"),
         O("17:17-18", kind="say", t=A1),
         S([*cut("17:19", "Thus said Jehovah unto me:"), gd("17:20")], "17:19-20", a=("#8FB0C8", lambda w, h: K.sabbath_gate("sg6", w, h, 611)), k=0.38, head="Hallow the Sabbath Day"),
         O("17:21-23", t=W1),
         O("17:24-25", a=("#8FB0C8", lambda w, h: K.sabbath_gate("sg6b", w, h, 612, kings=True))),
         O("17:26", a=("#FFC890", lambda w, h: K.offering_bearers("ob6", w, h, 613)), k=0.42),
         O("17:27", a=("#2A0A0A", lambda w, h: K.gates_fire(w, h, 614)), k=0.36)]
PG.extend(pack(SEGS2, "JER-C06-E", PG.next()))

SEGS3 = [S([cp("18:1"), gd("18:2")], "18:1-2", a=(POT, lambda w, h: K.potter("pt6", w, h, 615)), k=0.24, head="The Potter's House", stamp=18),
         O("18:3-4", kind="cap", a=(POT, lambda w, h: K.potter("pt6b", w, h, 616, marred=True)), k=0.26),
         S([cp("18:5"), gd("18:6")], "18:5-6", t=W1, head="As the Clay in the Potter's Hand"),
         O("18:7-10", t=S1),
         O("18:11", t=W1),
         S(cut("18:12", "But they say,", "cap", "say"), "18:12", t=(PEOPLE, RED)),
         O("18:13-15", a=("#6A9AC8", lambda w, h: K.lebanon_snow(w, h, 617))),
         O("18:16-17", a=("#C8906A", lambda w, h: K5.stubble_wind(w, h, 618)), k=0.36),
         S(cut("18:18", "Then said they,", "cap", "say"), "18:18", a=("#2A1A3A", lambda w, h: K.plotters("pl6", w, h, 619)), k=0.4, head="Let Us Devise Devices against Jeremiah"),
         O("18:19-20", kind="say", t=G1),
         O("18:21-22", kind="say", a=("#3A2A3A", lambda w, h: K.pit_snares(w, h, 620))),
         O("18:23", kind="say", t=S1)]
PG.extend(pack(SEGS3, "JER-C06-F", PG.next(), end=end_mark("NEXT · THE EARTHEN BOTTLE", "right: 10px; bottom: 34px")))
