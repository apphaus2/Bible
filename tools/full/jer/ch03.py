"""Jeremiah volume, Chapter 3 — The Temple of Jehovah (Jeremiah 7–9). Every verse, word for word from ref/asv.
The prophet in the gate of Jehovah's house: trust ye not in lying words, the temple of Jehovah; a den of robbers; go ye unto
Shiloh (its stones thrown down); the cakes to the queen of heaven; Topheth in the valley of the son of Hinnom (altars and smoke,
no one drawn); the graves opened under the sun and moon (no bones drawn); the stork knoweth her appointed times; is there no
balm in Gilead?; oh that my head were waters; Jerusalem heaps, a dwelling-place of jackals; the mourning women; let him that
glorieth glory in this, that he knoweth me; the uncircumcised nations as a map."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PENITENT, GOLDEN, COLD, RED, NIGHT
from jer import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W1, G1, S1, C1 = (jer(1, "word"), GOLDEN), (jer(1, "grief"), COLD), (jer(1, "stern"), RED), (jer(1, "calm"), GOLDEN)
MAP = "#0B1A2E"
GATE = lambda seed: ("#8FB0C8", lambda w, h: K.temple_gate(f"tg{seed}", w, h, seed))


@P("JER-C03-00-Title", "Chapter 3 · The Temple of Jehovah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.temple_gate("t3", 760, 780, 301)}</g><rect x="0" y="0" width="760" height="302" fill="#8FB0C8"></rect>')
    return chapter_title(3, "第三話", "The Temple of Jehovah", "Jeremiah 7 – 9", svg, "#3A4A6A", v("7:4", frm="The temple of Jehovah,"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([cp("7:1"), gd("7:2")], "7:1-2", a=GATE(302), k=0.32, head="Stand in the Gate of Jehovah's House", stamp=7),
        O("7:3-5", t=W1),
        O("7:6-8", t=S1),
        O("7:9-11", a=GATE(303), head="A Den of Robbers"),
        O("7:12", a=("#8A9AA8", lambda w, h: K.shiloh_ruins(w, h, 304)), k=0.3, head="Go Ye Now unto Shiloh"),
        O("7:13-15", t=S1),
        O("7:16-17", t=G1),
        O("7:18-19", a=("#1A1430", lambda w, h: K.queen_heaven("qh3", w, h, 305)), head="The Queen of Heaven"),
        O("7:20", t=S1),
        O("7:21-23", t=W1),
        O("7:24-26", t=G1),
        O("7:27-28", a=GATE(306)),
        O("7:29", a=("#C8A880", lambda w, h: K.bare_heights(w, h, 307, weeping=True)), k=0.3),
        O("7:30-31", a=("#1A0A12", lambda w, h: K.topheth(w, h, 308)), head="The Valley of Slaughter"),
        O("7:32-33", t=S1),
        O("7:34", a=("#3A2A4A", lambda w, h: K.empty_city(w, h, 309, dusk=True)), k=0.34)]
PG.extend(pack(SEGS, "JER-C03-D", PG.next()))

SEGS2 = [O("8:1-2", a=("#1A1A3A", lambda w, h: K.open_tombs(w, h, 310)), head="Spread before the Sun", stamp=8),
         O("8:3-4", t=S1),
         O("8:5-6", t=W1),
         O("8:7", a=("#6A8AB0", lambda w, h: K.migrants(w, h, 311)), k=0.3, head="The Stork in the Heavens"),
         O("8:8-9", t=G1),
         O("8:10", t=S1),
         O("8:11-12", t=W1),
         O("8:13", a=("#C8A070", lambda w, h: K.withered(w, h, 312)), k=0.3),
         O("8:14-15", kind="say", t=(PENITENT, COLD)),
         O("8:16", a=("#3A3A4A", lambda w, h: K.whirlwind_chariots(w, h, 313)), k=0.34),
         O("8:17", a=("#8A6A4A", lambda w, h: K.adders(w, h, 314)), k=0.26),
         S([say("8:18"), say("8:19", to="is not her King in her?"), gd("8:19", after="is not her King in her?")], "8:18-19", t=G1, head="Is There No Balm in Gilead?"),
         O("8:20", kind="say", a=("#4A3A5A", lambda w, h: K.harvest_past(w, h, 315)), k=0.24),
         O("8:21-22", kind="say", a=("#7A9AB8", lambda w, h: K.gilead(w, h, 316)), k=0.3)]
PG.extend(pack(SEGS2, "JER-C03-E", PG.next()))

SEGS3 = [O("9:1", kind="say", t=G1, head="A Fountain of Tears", stamp=9),
         O("9:2", kind="say", a=("#3A2A4A", lambda w, h: K.lodging(w, h, 317)), k=0.3),
         O("9:3", a=("#2A1A2A", lambda w, h: K.bow_arrows(w, h, 318)), k=0.3),
         O("9:4-6", t=S1),
         O("9:7-9", t=W1),
         O("9:10", kind="say", a=("#E8A060", lambda w, h: K.wilderness(w, h, 319))),
         O("9:11", a=("#5A4A5A", lambda w, h: K.jackal_heaps(w, h, 320)), k=0.26),
         S([say("9:12"), *cut("9:13", "And Jehovah saith,"), gd("9:14")], "9:12-14", t=G1),
         O("9:15-16", a=("#3A3A3A", lambda w, h: K.wormwood(w, h, 321))),
         O("9:17-19", a=("#3A3A4A", lambda w, h: K.mourners("mw3", w, h, 322)), head="Call for the Mourning Women"),
         O("9:20-21", a=("#3A2A4A", lambda w, h: K.empty_city(w, h, 323, dusk=True))),
         O("9:22", a=("#5A4A5A", lambda w, h: K.handful(w, h, 324)), k=0.26),
         O("9:23-24", t=C1, head="Let Him That Glorieth"),
         O("9:25-26", a=(MAP, lambda w, h: K.near_east(w, h, ("EGYPT", "JUDAH", "EDOM", "AMMON", "MOAB", "ARABIA"), hi=("EGYPT", "JUDAH", "EDOM", "AMMON", "MOAB", "ARABIA"),
                                                         box=(29.5, 42.5, 26.6, 36.2))), k=0.4)]
PG.extend(pack(SEGS3, "JER-C03-F", PG.next(), end=end_mark("NEXT · THE BROKEN COVENANT", "right: 10px; bottom: 34px")))
