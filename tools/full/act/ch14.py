"""Acts volume, Chapter 14 — Before Agrippa (Acts 25–26). Every verse, word for word from ref/eng-asv.
Festus at Jerusalem among the chief priests; the judgment-seat at Cæsarea, the Jews standing round about Paul; Festus'
question and Paul's answer beside their faces — I appeal unto Cæsar; Agrippa the king and Bernice; Festus laying the case
before the king beside his face; the great pomp and the place of hearing; Paul's defence before Agrippa beside his face,
with the Damascus road told again (the light from heaven above the brightness of the sun; Jesus not drawn, his words in
speech boxes from the light) and the dawn of light to the Gentiles; Paul, thou art mad, beside Festus' face; With but
little persuasion beside Agrippa's; except these bonds; the king and the governor and Bernice rising."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art14 as A, ch13 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_STERN, FESTUS, FESTUS_LOUD, AGRIPPA2, BERNICE,
                        HIGH_PRIEST, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C14-00-Title", "Chapter 14 · Before Agrippa", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#C8B8A0"></rect><g transform="translate(0 300)">{A.hearing("t14", 760, 780, 2601)}</g>'
    return title(14, "Before Agrippa", "Acts 25 – 26", svg, "#4A2A5A", v("26:28", frm="With but little persuasion"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)

SEGS = [D([cp("25:1"), cp("25:2"), cp("25:3"), cp("25:4"), sy("25:5")], lambda w, h: A.festus_jerusalem("fj1", w, h, 2501), "#8FD0E2", head="Festus", sky=(25, "left"), art_h=280),
        D([cp("25:6"), cp("25:7"), cp("25:8", to="in his defence,"), sy("25:8", frm="Neither against")], lambda w, h: A.praetorium("pr1", w, h, 2506, governor="festus"), "#C8B8A0",
          art_h=240),
        F([cp("25:9", to="answered Paul and said,"), sy("25:9", frm="Wilt thou go up")], FESTUS, h=220),
        F([cp("25:10", to="But Paul said,"), sy("25:10", frm="I am standing"), sy("25:11")], PAUL_STERN, bg=RED, head="I Appeal unto Cæsar"),
        F([cp("25:12", to="answered,"), sy("25:12", frm="Thou hast appealed")], FESTUS, h=220),
        D([cp("25:13")], lambda w, h: A.pomp("pm1", w, h, 2513), "#C8B8A0", head="Agrippa the King", art_h=240),
        F([cp("25:14", to="saying,"), sy("25:14", frm="There is a certain man"), sy("25:15"), sy("25:16")], FESTUS),
        F([sy("25:17"), sy("25:18"), sy("25:19")], FESTUS),
        F([sy("25:20"), sy("25:21")], FESTUS),
        F([cp("25:22", to="And Agrippa said unto Festus,"), sy("25:22", frm="I also could wish", to="the man myself.")], AGRIPPA2, h=220),
        F([sy("25:22", frm="To-morrow, saith he,")], FESTUS, h=200),
        D([cp("25:23")], lambda w, h: A.pomp("pm2", w, h, 2523), "#C8B8A0", art_h=260),
        F([cp("25:24", to="And Festus saith,"), sy("25:24", frm="King Agrippa,"), sy("25:25"), sy("25:26"), sy("25:27")], FESTUS),
        # Acts 26
        D([cp("26:1", to="And Agrippa said unto Paul,"), sy("26:1", frm="Thou art permitted", to="for thyself."), cp("26:1", frm="Then Paul stretched")],
          lambda w, h: A.hearing("hg1", w, h, 2601), "#C8B8A0", head="Paul before Agrippa", sky=(26, "left"), art_h=280),
        F([sy("26:2"), sy("26:3"), sy("26:4"), sy("26:5")], PAUL),
        F([sy("26:6"), sy("26:7"), sy("26:8")], PAUL),
        F([sy("26:9"), sy("26:10"), sy("26:11")], PAUL_STERN, bg=RED),
        D([sy("26:12"), sy("26:13")], lambda w, h: A.damascus_road("dr1", w, h, 2612), "#5AB0D8", art_h=240),
        D([sy("26:14"), sy("26:15"), sy("26:16")], lambda w, h: A.damascus_road("dr2", w, h, 2614, fallen=True), "#5AB0D8", art_h=200),
        D([sy("26:17"), sy("26:18")], lambda w, h: A.light_gentiles("lg1", w, h, 2617), "#14123A", art_h=220),
        F([sy("26:19"), sy("26:20"), sy("26:21")], PAUL),
        F([sy("26:22"), sy("26:23")], PAUL),
        F([cp("26:24", to="with a loud voice,"), sy("26:24", frm="Paul, thou art mad;")], FESTUS_LOUD, bg=RED, h=220, head="Almost Thou Persuadest"),
        F([cp("26:25", to="But Paul saith,"), sy("26:25", frm="I am not mad,"), sy("26:26"), sy("26:27")], PAUL),
        F([cp("26:28", to="And Agrippa said unto Paul,"), sy("26:28", frm="With but little")], AGRIPPA2, h=220),
        F([cp("26:29", to="And Paul said,"), sy("26:29", frm="I would to God,")], PAUL),
        D([cp("26:30"), cp("26:31", to="saying,"), sy("26:31", frm="This man doeth"), cp("26:32", to="And Agrippa said unto Festus,"), sy("26:32", frm="This man might")],
          lambda w, h: A.hearing("hg2", w, h, 2630, stage="rise"), "#C8B8A0", art_h=220)]
PG.extend(K.pack(SEGS, "ACT-C14-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE SHIPWRECK")))
