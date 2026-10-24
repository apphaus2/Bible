"""Luke volume, Chapter 2 — Good Tidings of Great Joy (Luke 2). Every verse, word for word from ref/eng-asv.
The decree of Cæsar Augustus, the enrolling at a town gate; Joseph leading the ass up the road to Bethlehem, Mary riding;
the stable by the inn, the ox-stall and the manger, the babe swaddled and small in a soft light (no face drawn). The
shepherds keeping watch by night; the angel of the Lord standing by them in white light, the glory shining round about —
the angel's words over the field (no face, no wings); the multitude of the heavenly host as figures of light filling the
sky, their song in a song box; the shepherds going with haste, kneeling at the manger, returning through Bethlehem with
their arms lifted; Mary pondering by the manger. The eighth day and the name JESUS; the presentation in the temple court
with the pair of turtledoves; Simeon taking the child up in his arms, his song in song boxes, his words to Mary beside his
face; Anna the prophetess, bent with age. Nazareth; the passover at twelve, the company on the road, the parents turning
back seeking; the boy among the teachers under the colonnade; his mother's words and his answer beside their faces; the
carpenter's house at Nazareth."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art as A, ch01 as _prev
from luk.common import (K, Pages, D, F, Q, N, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, SHEPHERD_JOY, SIMEON, MARY_GRIEF, JESUS_BOY)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C02-00-Title", "Chapter 2 · Good Tidings of Great Joy", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 300)">{A.field_night("t2", 760, 780, 201, host=True)}</g>'
    return title(2, "Good Tidings of Great Joy", "Luke 2", svg, "#0B0B2A", v("2:14"))


SEGS = [D([cp("2:1"), cp("2:2"), cp("2:3")], lambda w, h: A.enrolment("en1", w, h, 201), "#8FD0E2", head="All the World Should Be Enrolled", sky=(2, "left")),
        D([cp("2:4"), cp("2:5")], lambda w, h: A.to_bethlehem("tb1", w, h, 202), "#4A3A6A", art_h=240),
        D([cp("2:6"), cp("2:7")], lambda w, h: A.stable("st1", w, h, 203), "#2A2030", head="No Room for Them in the Inn", art_h=280),
        D([cp("2:8")], lambda w, h: A.field_night("fn1", w, h, 204), NIGHT, head="Good Tidings of Great Joy", art_h=260),
        D([cp("2:9")], lambda w, h: A.field_night("fn2", w, h, 205, angel_=True), NIGHT, art_h=260),
        D([N("2:10", "said unto them,"), sy("2:11"), sy("2:12")], lambda w, h: A.field_night("fn3", w, h, 206, angel_=True), NIGHT),
        D([cp("2:13"), sg("2:14")], lambda w, h: A.field_night("fn4", w, h, 207, host=True), NIGHT, head="Glory to God in the Highest", art_h=300),
        F([N("2:15", "said one to another,")], SHEPHERD_JOY, bg=COLD),
        D([cp("2:16")], lambda w, h: A.stable("st2", w, h, 208, shepherds=True), "#2A2030", art_h=260),
        D([cp("2:17"), cp("2:18")], lambda w, h: A.shepherds_tell("sh1", w, h, 209), "#5A6A9A"),
        D([cp("2:19")], lambda w, h: A.pondered("pd1", w, h, 210), "#1E1828", head="Pondering Them in Her Heart", art_h=260),
        D([cp("2:20")], lambda w, h: A.field_night("fn5", w, h, 211, gone=True), NIGHT),
        D([cp("2:21")], lambda w, h: A.born("bn1", w, h, 212), "#5A4048", head="His Name Was Called Jesus"),
        D([cp("2:22"), cp("2:23"), cp("2:24")], lambda w, h: A.presented("pr1", w, h, 213), "#8FD0E2", head="To Present Him to the Lord"),
        F([cp("2:25"), cp("2:26")], SIMEON, head="Simeon"),
        D([cp("2:27"), cp("2:28"), sg("2:29"), sg("2:30"), sg("2:31"), sg("2:32")], lambda w, h: A.presented("pr2", w, h, 214, simeon=True), "#8FD0E2", art_h=240),
        F([cp("2:33"), N("2:34", "said unto Mary his mother,"), sy("2:35")], SIMEON),
        D([cp("2:36"), cp("2:37"), cp("2:38")], lambda w, h: A.presented("pr3", w, h, 215, anna=True), "#8FD0E2", head="Anna the Prophetess"),
        D([cp("2:39"), cp("2:40")], lambda w, h: A.nazareth("nz1", w, h, 216), "#8FD0E2"),
        D([cp("2:41"), cp("2:42")], lambda w, h: A.passover_road("pv1", w, h, 217), "#8FD0E2", head="In My Father's House"),
        D([cp("2:43"), cp("2:44")], lambda w, h: A.passover_road("pv2", w, h, 218, boy=False), "#8FD0E2"),
        D([cp("2:45")], lambda w, h: A.passover_road("pv3", w, h, 219, seeking=True), "#8FD0E2"),
        D([cp("2:46"), cp("2:47")], lambda w, h: A.among_doctors("ad1", w, h, 220), "#C8B490", art_h=240),
        F([Q("2:48", "c", "said unto him,", "s")], MARY_GRIEF, bg=COLD),
        F([N("2:49", "said unto them,"), cp("2:50")], JESUS_BOY),
        D([cp("2:51"), cp("2:52")], lambda w, h: A.subject("sb1", w, h, 221), "#B8987A", art_h=240)]
PG.extend(K.pack(SEGS, "LUK-C02-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE VOICE IN THE WILDERNESS")))
