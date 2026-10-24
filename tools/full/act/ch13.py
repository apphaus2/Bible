"""Acts volume, Chapter 13 — Before Felix (Acts 22:30–24:27). Every verse, word for word from ref/eng-asv.
The council: Paul beside his face; Ananias the high priest beside his; the blow on the mouth (23:2) told in words only;
God shall smite thee, thou whited wall; the law in a song box; the Pharisees and Sadducees divided, the scribes standing up;
the soldiers taking Paul into the castle; the night following — the light standing by Paul in the castle (the Lord not
drawn), his words in a speech box; the forty under a curse; Paul's sister's son and the chief captain; the escort by night,
Paul set on a horse; Lysias' letter over Ezra's letter-scroll; the road to Antipatris and Cæsarea on the map; Felix in
Herod's palace. Tertullus beside his face, accusing; Paul's defence beside his face and before the governor's seat; Felix
deferring; Felix and Drusilla hearing Paul of righteousness, and self-control, and the judgment to come; Felix terrified,
beside his face; the two years in bonds, and Porcius Festus."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art13 as A, ch12 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_STERN, PAUL_COLD, HIGH_PRIEST, LYSIAS, NEPHEW,
                        CENTURION, TERTULLUS, FELIX, FELIX_AFRAID, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C13-00-Title", "Chapter 13 · Before Felix", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#C8B8A0"></rect><g transform="translate(0 300)">{A.praetorium("t13", 760, 780, 2424, queen="drusilla", accusers=False, paul_speak=True)}</g>'
    return title(13, "Before Felix", "Acts 22:30 – 24:27", svg, "#5A3A3A", v("24:25", frm="righteousness, and self-control,", to="the judgment to come,"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)

SEGS = [D([cp("22:30")], lambda w, h: A.council("cn1", w, h, 2230, accused=("paul",)), "#4A3A44", head="The Council", art_h=220),
        F([cp("23:1", to="said,"), sy("23:1", frm="Brethren, I have lived")], PAUL, h=220),
        F([cp("23:2")], HIGH_PRIEST, bg=RED, h=200),
        F([cp("23:3", to="Then said Paul unto him,"), sy("23:3", frm="God shall smite thee,")], PAUL_STERN, bg=RED),
        D([cp("23:4", to="And they that stood by said,"), sy("23:4", frm="Revilest thou"), cp("23:5", to="And Paul said,"), sy("23:5", frm="I knew not,", to="for it is written,"),
           sg("23:5", frm="Thou shalt not speak evil")], lambda w, h: A.council("cn2", w, h, 2304, accused=("paul",)), "#4A3A44", sky=(23, "left"), art_h=260),
        F([cp("23:6", to="he cried out in the council,"), sy("23:6", frm="Brethren, I am a Pharisee,")], PAUL),
        D([cp("23:7"), cp("23:8"), cp("23:9", to="and strove, saying,"), sy("23:9", frm="We find no evil")], lambda w, h: A.council_divided("cd1", w, h, 2307), "#4A3A44", art_h=220),
        D([cp("23:10")], lambda w, h: A.council_divided("cd2", w, h, 2310, taken=True), "#4A3A44", art_h=220),
        D([cp("23:11", to="and said,"), sy("23:11", frm="Be of good cheer:")], lambda w, h: A.castle_night("cs1", w, h, 2311), "#3A3238", head="Be of Good Cheer", art_h=240),
        D([cp("23:12"), cp("23:13"), cp("23:14", to="and said,"), sy("23:14", frm="We have bound ourselves"), sy("23:15")], lambda w, h: A.forty("fy1", w, h, 2312), "#1E1420",
          head="The Forty", art_h=220),
        D([cp("23:16"), cp("23:17", to="and said,"), sy("23:17", frm="Bring this young man")], lambda w, h: A.nephew_told("nt1", w, h, 2316), "#B8A07A"),
        D([cp("23:18", to="and saith,"), sy("23:18", frm="Paul the prisoner"), cp("23:19", to="asked him privately,"), sy("23:19", frm="What is it")],
          lambda w, h: A.nephew_told("nt2", w, h, 2318, captain=True), "#B8A07A"),
        F([cp("23:20", to="And he said,"), sy("23:20", frm="The Jews have agreed"), sy("23:21")], NEPHEW),
        F([cp("23:22", to="charging him,"), sy("23:22", frm="Tell no man"), cp("23:23", to="and said,"), sy("23:23", frm="Make ready two hundred"), cp("23:24")], LYSIAS, bg=RED),
        D([cp("23:25"), sy("23:26"), sy("23:27"), sy("23:28")], lambda w, h: A.letter("lt1", w, h, 2325), "#2A1A2A", head="Unto the Most Excellent Governor Felix"),
        D([sy("23:29"), sy("23:30")], lambda w, h: A.letter("lt2", w, h, 2329), "#2A1A2A"),
        D([cp("23:31"), cp("23:32")], lambda w, h: A.escort("es1", w, h, 2331), "#05051A", art_h=240),
        D([cp("23:33"), cp("23:34"), sy("23:35", to="are come:"), cp("23:35", frm="and he commanded")], A.to_caesarea, "#0B1A2E", art_h=240),
        # Acts 24
        D([cp("24:1"), cp("24:2", to="saying,"), sy("24:2", frm="Seeing that by thee")], lambda w, h: A.praetorium("pr1", w, h, 2401, orator="tertullus"), "#C8B8A0",
          head="Tertullus", sky=(24, "left"), art_h=280),
        F([sy("24:3"), sy("24:4"), sy("24:5"), sy("24:6"), sy("24:8"), cp("24:9")], TERTULLUS, bg=RED),
        F([cp("24:10", to="Paul answered,"), sy("24:10", frm="Forasmuch as I know"), sy("24:11"), sy("24:12"), sy("24:13")], PAUL, head="Paul's Defence before Felix"),
        F([sy("24:14"), sy("24:15"), sy("24:16")], PAUL),
        D([sy("24:17"), sy("24:18"), sy("24:19")], lambda w, h: A.temple_vow("tv1", w, h, 2417), "#8FD0E2"),
        F([sy("24:20"), sy("24:21")], PAUL_STERN, bg=RED),
        D([cp("24:22", to="deferred them, saying,"), sy("24:22", frm="When Lysias"), cp("24:23")], lambda w, h: A.praetorium("pr2", w, h, 2422, accusers=False), "#C8B8A0"),
        D([cp("24:24")], lambda w, h: A.praetorium("pr3", w, h, 2424, queen="drusilla", accusers=False, paul_speak=True), "#C8B8A0", head="Felix and Drusilla", art_h=220),
        F([cp("24:25", to="answered,"), sy("24:25", frm="Go thy way")], FELIX_AFRAID, bg=COLD),
        D([cp("24:26"), cp("24:27")], lambda w, h: A.two_years("ty1", w, h, 2426), "#D8C098", art_h=220)]
PG.extend(K.pack(SEGS, "ACT-C13-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · BEFORE AGRIPPA")))
