"""Acts volume, Chapter 16 — Rome (Acts 28). Every verse, word for word from ref/eng-asv.
Melita: the barbarians' fire on the shore in the rain; the viper fastened on Paul's hand (snake.py) and shaken off into the
fire; the islanders watching, then saying he was a god; Publius and his father healed; the sick of the island cured; the
ship whose sign was the Twin Brothers; Syracuse, Rhegium and Puteoli on the map; the Appian Way, the Market of Appius and
the Three Taverns, the brethren coming to meet him; Rome on its hills; Paul in his own hired dwelling with the soldier that
guarded him; the chief of the Jews beside a face and in the room; Isaiah's words in song boxes; and the two whole years,
preaching the kingdom of God with all boldness, none forbidding him."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art16 as A, ch15 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, fin, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_COLD, PUBLIUS, JEW_ROME, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C16-00-Title", "Chapter 16 · Rome", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.rome("t16", 760, 780, 2816, paul_=True)}</g>'
    return title(16, "Rome", "Acts 28", svg, "#3A5A7A", v("28:14", frm="and so we came to Rome."))


vy = A.voyage
SEGS = [D([cp("28:1"), cp("28:2")], lambda w, h: A.melita_fire("mf1", w, h, 2801), "#3A4A5A", head="Melita", sky=(28, "left"), art_h=300),
        D([cp("28:3"), cp("28:4", to="they said one to another,"), sy("28:4", frm="No doubt this man")], lambda w, h: A.melita_fire("mf2", w, h, 2803, stage="viper"), "#3A4A5A", art_h=260),
        D([cp("28:5"), cp("28:6")], lambda w, h: A.melita_fire("mf3", w, h, 2805, stage="shaken"), "#3A4A5A", art_h=260),
        D([cp("28:7"), cp("28:8")], lambda w, h: A.publius_house("ph1", w, h, 2807), "#D8C098", head="Publius", art_h=240),
        D([cp("28:9"), cp("28:10")], lambda w, h: A.publius_house("ph2", w, h, 2809, crowd_=True), "#8FD0E2"),
        D([cp("28:11")], lambda w, h: A.twin_brothers("tb1", w, h, 2811), "#8FD0E2", head="And So We Came to Rome", art_h=240),
        D([cp("28:12"), cp("28:13"), cp("28:14")], lambda w, h: vy(w, h, legs=8, lit=[7], title="ACTS 28:11–16 · TO ROME", box=(11.6, 16.4, 35.4, 42.4)), "#0B1A2E", art_h=280),
        D([cp("28:15")], lambda w, h: A.appian_way("aw1", w, h, 2815), "#8FD0E2", art_h=260),
        D([cp("28:16")], lambda w, h: A.rome("rm1", w, h, 2816, paul_=True), "#8FD0E2", art_h=260),
        D([cp("28:17", to="he said unto them,"), sy("28:17", frm="I, brethren,")], lambda w, h: A.lodging("lg1", w, h, 2817), "#D8C098", head="The Hope of Israel", art_h=220),
        F([sy("28:18"), sy("28:19"), sy("28:20")], PAUL),
        F([cp("28:21", to="And they said unto him,"), sy("28:21", frm="We neither received"), sy("28:22")], JEW_ROME),
        D([cp("28:23"), cp("28:24")], lambda w, h: A.lodging("lg2", w, h, 2823), "#D8C098", art_h=220),
        F([cp("28:25", to="spoken one word,"), sy("28:25", frm="Well spake the Holy Spirit"), sg("28:26"), sg("28:27")], PAUL_COLD, bg=COLD),
        F([sy("28:28")], PAUL, h=220),
        D([cp("28:30"), cp("28:31")], lambda w, h: A.lodging("lg3", w, h, 2830, visitors="all"), "#D8C098", head="None Forbidding Him", art_h=280)]
PG.extend(K.pack(SEGS, "ACT-C16-D", PG.next(), most=4, lone=0.5, end=fin("END OF ACTS · NEXT · ROMANS")))
