"""Lamentations volume, Chapter 1 — How Doth the City Sit Solitary (Lamentations 1–2). Every verse, word for word from ref/asv,
each verse its own song line. The first lament: the city sitting solitary as a widow, weeping sore in the night; the ways of Zion
mourning; the sanctuary entered by the nations; is it nothing to you, all ye that pass by?; the yoke of my transgressions; the
winepress; Zion spreadeth forth her hands. The second: the daughter of Zion covered with a cloud; the tabernacle taken away as a
garden booth; the altar cast off; the line stretched over the wall; the gates sunk into the ground; the elders in the dust; thy
breach is great like the sea; all that pass by clap their hands; pour out thy heart like water. Restraint: 2:11–12 and 2:20–21
words over empty streets and a cold hearth; no one is drawn suffering."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from lam import G, art as K
from lam.common import pack, L, ZION, ZION_PLEA, MOURNER, MOURNER_HOPE, ELDER, GOLDEN, COLD, RED

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
Z, ZP, M = (ZION, COLD), (ZION_PLEA, GOLDEN), (MOURNER, COLD)
DUSK = "#2A2040"


@P("LAM-C01-00-Title", "Chapter 1 · How Doth the City Sit Solitary", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.widow_city("t1", 760, 780, 101, x=0.86)}</g><rect x="0" y="0" width="760" height="302" fill="#2A2040"></rect>')
    return chapter_title(1, "第一話", "How Doth the City Sit Solitary", "Lamentations 1 – 2", svg, DUSK, v("1:1", to="that was full of people!"), "Lamentations · Volume Twenty-Five")


SEGS = [L(1, 1, 2, d=(DUSK, lambda w, h: K.widow_city("wc1", w, h, 102)), k=0.42, head="How Doth the City Sit Solitary", stamp=1),
        L(1, 3, 4, d=("#6A6A7A", lambda w, h: K.ways_mourn(w, h, 103))),
        L(1, 5, 6, t=Z),
        L(1, 7, 8, d=("#8A8A9A", lambda w, h: K.passers_by("pb1", w, h, 104))),
        L(1, 9, 10, d=("#3A3040", lambda w, h: K.altar_alone(w, h, 105))),
        L(1, 11, t=ZP),
        L(1, 12, d=(DUSK, lambda w, h: K.widow_city("wc1b", w, h, 106)), k=0.36, head="Is It Nothing to You?"),
        L(1, 13, 14, d=("#1A1820", lambda w, h: K.yoke_iron(w, h, 107))),
        L(1, 15, 16, d=("#2A0A1A", lambda w, h: K.grape_tread(w, h, 108))),
        L(1, 17, 18, t=Z, head="Zion Spreadeth Forth Her Hands"),
        L(1, 19, 20, d=("#3A2A4A", lambda w, h: K.empty_streets(w, h, 109))),
        L(1, 21, 22, t=ZP),
        L(2, 1, 2, d=("#1A1A24", lambda w, h: K.cloud_city(w, h, 110)), head="Covered with a Cloud in His Anger", stamp=2),
        L(2, 3, 4, d=("#2A0A0A", lambda w, h: K.burning_city(w, h, 111))),
        L(2, 5, 6, d=("#8A7A6A", lambda w, h: K.booth_broken(w, h, 112))),
        L(2, 7, d=("#3A3040", lambda w, h: K.altar_alone(w, h, 113)), k=0.36),
        L(2, 8, d=("#5A4A5A", lambda w, h: K.line_stretched(w, h, 114)), k=0.36),
        L(2, 9, d=("#5A4A5A", lambda w, h: K.gates_sunk(w, h, 115)), k=0.36, head="Her Gates Are Sunk into the Ground"),
        L(2, 10, d=("#4A4048", lambda w, h: K.elders_dust("ed1", w, h, 116)), k=0.36),
        L(2, 11, 12, d=("#2A2420", lambda w, h: K.cold_hearth(w, h, 117))),
        L(2, 13, 14, d=("#4A5A7A", lambda w, h: K.breach_sea(w, h, 118)), head="Thy Breach Is Great like the Sea"),
        L(2, 15, 16, d=("#8A8A9A", lambda w, h: K.passers_by("pb1b", w, h, 119))),
        L(2, 17, 18, t=M),
        L(2, 19, d=("#14122A", lambda w, h: K.tears(w, h, 120)), k=0.36, head="Pour Out Thy Heart like Water"),
        L(2, 20, 21, d=("#3A2A4A", lambda w, h: K.empty_streets(w, h, 121))),
        L(2, 22, t=Z)]
PG.extend(pack(SEGS, "LAM-C01-D", PG.next(), end=end_mark("NEXT · HIS COMPASSIONS FAIL NOT", "right: 10px; bottom: 34px")))
