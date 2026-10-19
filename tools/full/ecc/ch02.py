"""Ecclesiastes volume, Chapter 2 — Two Are Better than One (Ecclesiastes 4–6). Every verse, word for word from ref/asv.
The tears of the oppressed in the brick field (no blow drawn); a handful with quietness; one that is alone at his table of
silver; two on the road, the one lifting up his fellow; the threefold cord; the poor wise youth come out of prison and the old
king on his throne; keep thy foot when thou goest to the house of God; the vow before the altar; the king served by the
field; the laborer's sweet sleep and the rich man awake; naked shall he go again; an alien eateth it; do not all go to one
place (the roads to one gate at dusk); and a man's days as a shadow."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from ecc import G, art as K
from ecc.common import (pack, paged, face, drawn, PREACHER, PREACHER_GOLD, PREACHER_WARM, PREACHER_STERN, PREACHER_NIGHT, COLD, GOLDEN, DUSK, RED)
from ecc import ch01 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ECC-C02-00-Title", "Chapter 2 · Two Are Better than One", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{K.two_better("t2", 760, 780, 201)}</g>')
    return chapter_title(2, "第二話", "Two Are Better than One", "Ecclesiastes 4 – 6", svg, "#4A6A8A", v("4:12", frm="and a threefold cord"), "Ecclesiastes · Volume Twenty-One")


PAGE = [[drawn("4:1-3", lambda w, h: K.oppressed("op2", w, h, 202), "#4A2A3A", head="The Tears of the Oppressed", stamp=4)],
        [drawn("4:4-6", lambda w, h: K.handful(w, h, 203), "linear-gradient(90deg, #2A4A6A 0%, #3A5A7A 48%, #6A4A3A 52%, #8A5A3A 100%)"),
         drawn("4:7-8", lambda w, h: K.alone("al2", w, h, 204), "#1A1430")],
        [drawn("4:9-11", lambda w, h: K.two_better("tb2", w, h, 205), "#8FD0E2", head="Two Are Better than One"),
         drawn("4:12", lambda w, h: K.threefold(w, h, 206), "#0B1A2E", h=330)],
        [drawn("4:13-16", lambda w, h: K.youth_king("yk2", w, h, 207), "linear-gradient(90deg, #2A1E2A 0%, #2A1E2A 42%, #8FD0E2 42%, #8FD0E2 100%)")],
        [drawn("5:1-3", lambda w, h: K.house_of_god("hg2", w, h, 208), "#8FD0E2", head="Keep Thy Foot", stamp=5)],
        [drawn("5:4-7", lambda w, h: K.vow("vw2", w, h, 209), "#3A2A4A")],
        [drawn("5:8-9", lambda w, h: K.field_king("fk2", w, h, 210), "#8FD0E2"),
         drawn("5:10-12", lambda w, h: K.sleep_two("st2", w, h, 211), "linear-gradient(90deg, #14123A 0%, #14123A 50%, #5A3A2A 50%, #5A3A2A 100%)")],
        [drawn("5:13-17", lambda w, h: K.naked_road("nr2", w, h, 212), "#4A2A4A", head="A Grievous Evil"),
         face("5:18-20", PREACHER_GOLD)],
        [drawn("6:1-2", lambda w, h: K.alien_eats("ae2", w, h, 213), "#8A4A26", head="An Evil Disease", stamp=6),
         drawn("6:3-6", lambda w, h: K.one_place("on2", w, h, 214), "#2A1A3A")],
        [face("6:7-9", PREACHER_NIGHT, bg=COLD),
         drawn("6:10-12", lambda w, h: K.shadow("sh2", w, h, 215), "#5A2A4A")]]
PG.extend(paged(PAGE, "ECC-C02-", PG.next(), end=end_mark("NEXT · A GOOD NAME", "right: 10px; bottom: 34px")))

