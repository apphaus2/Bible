"""Jonah volume, Chapter 2 — That Great City (Jonah 3–4). Every verse, word for word from ref/asv.
The word of Jehovah the second time; Nineveh, an exceeding great city of three days' journey; Jonah crying at the gate,
yet forty days; the people in sackcloth; the king in ashes beside his empty throne and his decree, the herds unfed; God
repented of the evil (words over the city at dawn); Jonah's anger beside his face; the booth on the east side of the city,
the gourd, the worm at dawn, the sultry east wind; and Nineveh at evening with its cattle. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, vista, NIGHT
from jon import G, art as A, ch01 as _prev
from jon.common import K, cp, gd, sy, JONAH, JONAH_ANGRY, JONAH_FAINT, KING_SACK, COLD, GOLDEN, RED

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JON-C02-00-Title", "Chapter 2 · That Great City", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A3A"></rect><g transform="translate(0 300)">{A.nineveh_great("tn", 760, 780, 201, jonah=False, dusk=True)}</g>'
    return title(2, "That Great City", "Jonah 3 – 4", svg, "#2A1A3A", v("3:4", frm="Yet forty days"), "Jonah · Volume Thirty-Two")


SEGS = [K.drawn([cp("3:1"), gd("3:2")], lambda w, h: vista(w, h, 202, tone="dawn", sun_at=(0.8, 0.5), hills_n=2, horizon=0.68, people=[(0.4, "prophet", A.JONAH_C)], p="jw2"),
                "#2A2A5A", head="The Second Time", stamp=3),
        K.drawn([cp("3:3")], lambda w, h: A.nineveh_great("ng1", w, h, 203), "#E8C890", head="An Exceeding Great City"),
        K.drawn([cp("3:4", to="and said,"), sy("3:4", frm="Yet forty days")], lambda w, h: A.nineveh_great("ng2", w, h, 204), "#E8C890"),
        K.drawn([cp("3:5")], lambda w, h: A.sackcloth("sc1", w, h, 205), "#6A6A7A", head="Sackcloth and Ashes"),
        K.drawn([cp("3:6")], lambda w, h: A.king_ashes("ka1", w, h, 206), "#3A2A2A"),
        K.drawn([cp("3:7", to="saying,"), sy("3:7", frm="Let neither")], lambda w, h: A.decree("dc1", w, h, 207), "#7A7A8A"),
        K.face([sy("3:8"), sy("3:9")], KING_SACK, bg=COLD),
        K.drawn([cp("3:10")], lambda w, h: A.nineveh_great("ng3", w, h, 208, jonah=False, sack=True), "#E8C890"),
        K.face([cp("4:1"), cp("4:2", to="and said,"), sy("4:2", frm="I pray thee"), sy("4:3")], JONAH_ANGRY, bg=RED, head="Doest Thou Well to Be Angry?", stamp=4),
        K.drawn([cp("4:4", to="said,"), gd("4:4", frm="Doest"), cp("4:5")], lambda w, h: A.booth("bt1", w, h, 209), "#8FD0E2"),
        K.drawn([cp("4:6")], lambda w, h: A.booth("bt2", w, h, 210, stage="gourd"), "#8FD0E2", head="The Gourd"),
        K.drawn([cp("4:7")], lambda w, h: A.worm_close(w, h, 211), "#5A4A7A"),
        K.drawn([cp("4:8", to="and said,"), sy("4:8", frm="It is better")], lambda w, h: A.booth("bt3", w, h, 212, stage="wind"), "#FFE680"),
        K.face([cp("4:9", to="to Jonah,"), gd("4:9", frm="Doest thou", to="for the gourd?"), cp("4:9", frm="And he said,", to="And he said,"), sy("4:9", frm="I do well")], JONAH_FAINT, bg=GOLDEN),
        K.drawn([cp("4:10", to="said,"), gd("4:10", frm="Thou hast"), gd("4:11")], lambda w, h: A.sixscore("sx1", w, h, 213), "#2A1A3A", head="Should Not I Have Regard for Nineveh?")]
PG.extend(K.pack(SEGS, "JON-C02-D", PG.next(), end=fin("END OF JONAH · NEXT · MICAH")))
