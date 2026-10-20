"""Judges volume, Chapter 2 — Deborah (Judges 3–5). Every verse, word for word from ref/eng-asv.
The nations left to prove Israel; Othniel; Ehud and Eglon king of Moab (3:21–22 are words over the locked doors of the cool
upper room: nothing within is drawn); Shamgar's ox-goad; Deborah under her palm-tree, Barak, mount Tabor and the river
Kishon (the digest's Deborah panels); Jael's tent (4:21 is the digest's silhouette at the tent door); and the Song of
Deborah in song boxes over Tabor, the stars, the Kishon, the tent and the lattice of Sisera's mother."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from discourse import seg
from deu.common import shade
from genesis import art as X
from jos import art as JA
from jos.art import below
from jdg import G, art as K
from jdg.common import (pack, say, gd, cp, sg, says, gods, caps, over, face, drawn, D, DEBORAH, BARAK, BARAK_BOLD, JAEL, KING_CANAAN, ISRAELITE,
                        RED, COLD, GOLDEN)
from jdg import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("JDG-C02-00-Title", "Chapter 2 · Deborah", title=True)
def title(n):
    bg, art = D("A1", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect><g transform="translate(0 360)">{art(760, 720)}</g>')
    return chapter_title(2, "第二話", "Deborah", "Judges 3 – 5", svg, "#F3D8A0", v("5:7", frm="Until that I Deborah arose,"), "Judges · Volume Seven")


SEGS = [drawn([caps("3:1-6")], "JDG 3:1–6", below(lambda w, h: K.nations_left(w, h), 0.5), MAP, head="The Nations Which Jehovah Left", stamp=3),
        drawn([caps("3:7-11")], "JDG 3:7–11", lambda w, h: JA.armed("ar2", w, h, 211, tribes=("JUDAH",)), "#F3D8A0", head="Othniel"),
        drawn([caps("3:12-16")], "JDG 3:12–16", lambda w, h: K.tribute("tr2", w, h, 212), "#6A2A3A", head="Ehud"),
        drawn([caps("3:17-18"), cp("3:19", to="and said,"), say("3:19", frm="I have a secret", to="O king."), cp("3:19", frm="And he said,", to="And he said,"),
               say("3:19", frm="Keep silence.", to="Keep silence."), cp("3:19", frm="And all that stood")], "JDG 3:17–19", lambda w, h: K.tribute("tr2b", w, h, 213), "#6A2A3A"),
        drawn([cp("3:20", to="And Ehud said,"), say("3:20", frm="I have a message", to="unto thee."), cp("3:20", frm="And he arose"), caps("3:21-23")], "JDG 3:20–23",
              lambda w, h: K.locked_door("ld2", w, h, 214, servants=False), "#C8A87A"),
        drawn([cp("3:24", to="and they said,"), say("3:24", frm="Surely he"), caps("3:25-26")], "JDG 3:24–26", lambda w, h: K.locked_door("ld2b", w, h, 215), "#C8A87A"),
        drawn([caps("3:27"), cp("3:28", to="And he said unto them,"), say("3:28", frm="Follow after me;", to="into your hand."), cp("3:28", frm="And they went down"),
               caps("3:29-30")], "JDG 3:27–30", lambda w, h: K.trumpet_hills("th2", w, h, 216), "#F3B86A"),
        drawn([caps("3:31")], "JDG 3:31", lambda w, h: K.ox_goad("og2", w, h, 217), "#F3D8A0", head="Shamgar"),
        drawn([caps("4:1-3")], "JDG 4:1–3", lambda w, h: JA.chariots("ch2", w, h, 218), "#8FD0E2", head="Deborah, a Prophetess", stamp=4),
        drawn([caps("4:4-5")], "JDG 4:4–5", lambda w, h: K.palm_judge("pj2", w, h, 219), "#F3D8A0"),
        face([cp("4:6", to="and said unto him,"), ("say", v("4:6", frm="Hath not") + " " + v("4:7"))], "JDG 4:6–7", DEBORAH),
        face([cp("4:8", to="And Barak said unto her,"), say("4:8", frm="If thou")], "JDG 4:8", BARAK, bg=COLD),
        over([cp("4:9", to="And she said,"), say("4:9", frm="I will surely", to="hand of a woman."), cp("4:9", frm="And Deborah arose")], "JDG 4:9", "A1", 3),
        drawn([caps("4:10-13")], "JDG 4:10–13", lambda w, h: JA.chariots("ch2b", w, h, 220), "#8FD0E2", head="Mount Tabor"),
        over([cp("4:14", to="And Deborah said unto Barak,"), say("4:14", frm="Up;", to="before thee?"), cp("4:14", frm="So Barak went down")], "JDG 4:14", "A2", 1),
        over([caps("4:15-16")], "JDG 4:15–16", "A2", 2),
        over([caps("4:17")], "JDG 4:17", "A3", 0, head="Jael"),
        face([cp("4:18", to="and said unto him,"), say("4:18", frm="Turn in,", to="fear not."), cp("4:18", frm="And he turned in")], "JDG 4:18", JAEL),
        over([cp("4:19", to="And he said unto her,"), say("4:19", frm="Give me", to="thirsty."), cp("4:19", frm="And she opened"),
              cp("4:20", to="And he said unto her,"), say("4:20", frm="Stand in")], "JDG 4:19–20", "A3", 2),
        over([caps("4:21")], "JDG 4:21", "A3", 3),
        face([cp("4:22", to="and said unto him,"), say("4:22", frm="Come,", to="whom thou seekest."), cp("4:22", frm="And he came"), caps("4:23-24")], "JDG 4:22–24", JAEL)]
PG.extend(pack(SEGS, "JDG-C02-D", PG.next()))

# ---- the Song of Deborah --------------------------------------------------------------------------------------------------
ARTS = [D("A2", 1), ("#0F0E2A", NIGHTA), ("#0F0E2A", lambda w, h: K.kishon(w, h, 221)), D("A3", 0), D("A1", 0), ("#7A5A4A", lambda w, h: K.lattice(w, h, 222))]
GROUPS = [(2, 5), (6, 9), (10, 13), (14, 16), (17, 20), (21, 23), (24, 26), (27, 29), (30, 31)]
def song_lines(a, b):
    out = []
    for n in range(a, b + 1):
        if n == 31:
            out += [sg("5:31", to="in his might."), cp("5:31", frm="And the land had rest")]
        else:
            out.append(sg(f"5:{n}"))
    return out
ART_FOR = {(2, 5): 0, (6, 9): 4, (14, 16): 0, (17, 20): 1, (21, 23): 2, (24, 26): 3, (27, 29): 5}
SONG = [face([cp("5:1")] + song_lines(2, 5), "JDG 5:1–5", DEBORAH, head="Then Sang Deborah and Barak", stamp=5)]
for a, b in GROUPS[1:]:
    ref = f"JDG 5:{a}–{b}"
    if (a, b) in ART_FOR:
        bg, art = ARTS[ART_FOR[(a, b)]]
        SONG.append(drawn(song_lines(a, b), ref, art, bg))
    else:
        SONG.append(face(song_lines(a, b), ref, DEBORAH if a != 10 else BARAK_BOLD, bg=GOLDEN))
PG.extend(pack(SONG, "JDG-C02-S", PG.next(), end=end_mark("NEXT · GIDEON", "right: 10px; bottom: 34px")))
