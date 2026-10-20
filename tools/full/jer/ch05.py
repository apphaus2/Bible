"""Jeremiah volume, Chapter 5 — The Marred Girdle (Jeremiah 13–15). Every verse, word for word from ref/eng-asv.
The linen girdle bought and worn, hidden in a cleft of the rock by the Euphrates, and dug up marred, profitable for nothing;
every bottle filled with wine; the dark mountains; the king and the queen-mother (two crowns fallen before empty seats);
can the Ethiopian change his skin?; the drought — the gates sitting in black, the empty vessels at the cisterns, the cracked
ground, the hind forsaking her young; the prophets that prophesy lies; though Moses and Samuel stood before me; the four kinds
told in words over an empty plain; woe is me, my mother; thy words were found, and I did eat them; a fortified brazen wall."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art5 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PENITENT, GOLDEN, COLD, RED, NIGHT
from jer import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W1, G1, S1, C1, A1 = (jer(1, "word"), GOLDEN), (jer(1, "grief"), COLD), (jer(1, "stern"), RED), (jer(1, "calm"), GOLDEN), (jer(1, "afraid"), COLD)
DRY = "#E8A060"


@P("JER-C05-00-Title", "Chapter 5 · The Marred Girdle", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.euphrates("t5", 760, 780, 501, stage=1)}</g><rect x="0" y="0" width="760" height="302" fill="#8A8A9A"></rect>')
    return chapter_title(5, "第五話", "The Marred Girdle", "Jeremiah 13 – 15", svg, "#4A4A5A", v("13:7", frm="behold, the girdle was marred,"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([*cut("13:1", "Thus saith Jehovah unto me,"), cp("13:2")], "13:1-2", a=("#8A8A9A", lambda w, h: K.girdle_worn("gw5", w, h, 502)), k=0.32, head="A Linen Girdle", stamp=13),
        S([cp("13:3"), gd("13:4"), cp("13:5")], "13:3-5", a=(DRY, lambda w, h: K.euphrates("eu5", w, h, 503)), k=0.36, head="By the Euphrates"),
        S([*cut("13:6", "that Jehovah said unto me,"), cp("13:7")], "13:6-7", a=("#8A8A9A", lambda w, h: K.euphrates("eu5b", w, h, 504, stage=1)), k=0.4),
        S([cp("13:8"), gods("13:9-10")], "13:8-10", t=S1),
        O("13:11", t=W1),
        O("13:12", a=("#2A1A1A", lambda w, h: K.bottles(w, h, 505)), k=0.34, head="Every Bottle Shall Be Filled with Wine"),
        O("13:13-14", t=S1),
        S([gods("13:15-16"), say("13:17")], "13:15-17", a=("#0E0E18", lambda w, h: K.dark_mountains(w, h, 506))),
        O("13:18-19", a=("#5A3A2A", lambda w, h: K.crowns_down(w, h, 507)), head="Humble Yourselves, Sit Down"),
        O("13:20-22", t=S1),
        O("13:23-24", a=("#C8906A", lambda w, h: K.stubble_wind(w, h, 508)), k=0.3, head="Can the Ethiopian Change His Skin?"),
        O("13:25-27", t=S1)]
PG.extend(pack(SEGS, "JER-C05-D", PG.next()))

SEGS2 = [O("14:1-2", a=("#C89A6A", lambda w, h: K.gate_mourning("gm5", w, h, 509)), k=0.3, head="Concerning the Drought", stamp=14),
         O("14:3-4", a=(DRY, lambda w, h: K.dry_cistern("dc5", w, h, 510))),
         O("14:5-6", a=(DRY, lambda w, h: K.bare_beasts(w, h, 511)), k=0.36),
         O("14:7-9", kind="say", t=G1),
         S([gd("14:10"), *cut("14:11", "And Jehovah said unto me,"), gd("14:12")], "14:10-12", t=S1),
         S(cut("14:13", "Then said I,", "cap", "say") + cut("14:14", "Then Jehovah said unto me,"), "14:13-14", t=A1, head="The Prophets Prophesy Lies"),
         O("14:15-16", a=("#3A2A4A", lambda w, h: K.empty_city(w, h, 512, smoke_=True, dusk=True))),
         O("14:17-18", t=G1),
         O("14:19-20", kind="say", t=G1, head="Hast Thou Utterly Rejected Judah?"),
         O("14:21-22", kind="say", a=("#5A6A8A", lambda w, h: K.rain_clouds(w, h, 513)), k=0.36)]
PG.extend(pack(SEGS2, "JER-C05-E", PG.next()))

SEGS3 = [S([*cut("15:1", "Then said Jehovah unto me,"), gd("15:2")], "15:1-2", t=S1, head="Though Moses and Samuel Stood before Me", stamp=15),
         O("15:3-4", a=("#2A1A2A", lambda w, h: K.circling(w, h, 514))),
         O("15:5-6", t=S1),
         O("15:7", a=("#8FB0C8", lambda w, h: K.winnowing("wn5", w, h, 515)), k=0.3),
         O("15:8-9", a=("#1A1018", lambda w, h: K.noon_dark(w, h, 516))),
         S([say("15:10"), *cut("15:11", "Jehovah said,")], "15:10-11", t=G1, head="Woe Is Me, My Mother"),
         O("15:12-14", t=S1),
         O("15:15-17", kind="say", t=C1, head="Thy Words Were Found"),
         O("15:18", kind="say", a=(DRY, lambda w, h: K.dry_brook(w, h, 517)), k=0.28),
         O("15:19", t=W1),
         O("15:20-21", a=("#4A3A5A", lambda w, h: K.iron_pillar("ip5", w, h, 518, age=1)), head="A Fortified Brazen Wall")]
PG.extend(pack(SEGS3, "JER-C05-F", PG.next(), end=end_mark("NEXT · THE POTTER'S HOUSE", "right: 10px; bottom: 34px")))
