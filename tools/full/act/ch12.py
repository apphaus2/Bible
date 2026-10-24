"""Acts volume, Chapter 12 — Bound in the Spirit (Acts 21:1–22:29). Every verse, word for word from ref/eng-asv.
The voyage to Tyre and the kneeling on the beach; Philip's house at Cæsarea and his four daughters; Agabus binding his own
feet and hands with Paul's girdle, the Holy Spirit's words in the Voice box; I am ready ... to die at Jerusalem, beside
Paul's face; the road up to Jerusalem; James and the elders, their counsel beside James' face; Paul in the temple with the
four men under their vow. The riot and the arrest: the court of the temple in uproar (the beating told in words only), the
doors shut; the chief captain and his soldiers running down the stairs of the castle; Paul bound with two chains; borne up
the stairs; Dost thou know Greek? beside Lysias' face; Paul on the stairs beckoning, the great silence. His defence beside
his face — at the feet of Gamaliel; the Damascus road and the light (Jesus not drawn); Ananias; the trance in the temple;
Stephen's garments by the wall; the crowd casting off their garments and throwing dust into the air; the thongs and the
centurion (the scourging threatened, told in words only); and a Roman born."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art12 as A, ch11 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_STERN, PAUL_GRIEF, AGABUS, JAMES_LORD, LYSIAS,
                        CENTURION, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C12-00-Title", "Chapter 12 · Bound in the Spirit", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.antonia("t12", 760, 780, 2140, stage="speak")}</g>'
    return title(12, "Bound in the Spirit", "Acts 21:1 – 22:29", svg, "#3A5A7A", v("21:13", frm="I am ready not to be bound only,", to="at Jerusalem"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)

SEGS = [D([cp("21:1"), cp("21:2"), cp("21:3")], A.up_to_jerusalem, "#0B1A2E", head="To Tyre", sky=(21, "left"), art_h=280),
        D([cp("21:4"), cp("21:5"), cp("21:6")], lambda w, h: A.beach_farewell("bf1", w, h, 2104), "#8FD0E2", art_h=220),
        D([cp("21:7"), cp("21:8"), cp("21:9")], lambda w, h: A.philip_house("ph1", w, h, 2107), "#D8C098", head="Agabus", art_h=220),
        D([cp("21:10"), cp("21:11", to="and said,"), gd("21:11", frm="Thus saith the Holy Spirit,")], lambda w, h: A.philip_house("ph2", w, h, 2110, agabus_=True), "#D8C098", art_h=240),
        F([cp("21:12"), cp("21:13", to="Then Paul answered,"), sy("21:13", frm="What do ye,")], PAUL_GRIEF, bg=COLD),
        D([cp("21:14", to="saying,"), sy("21:14", frm="The will of the Lord"), cp("21:15"), cp("21:16"), cp("21:17")],
          scene("rd1", 2114, "road", [(0.3, "paul", {"flip": True}), (0.2, "timothy", {"flip": True}), (0.1, "man", {"c": "#6A5A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True})]), "#8FD0E2"),
        D([cp("21:18"), cp("21:19")], lambda w, h: A.council_jerusalem("cj1", w, h, 2118, speaker="paul"), "#C8A878", head="James and the Elders"),
        F([cp("21:20", to="and they said unto him,"), sy("21:20", frm="Thou seest, brother,"), sy("21:21"), sy("21:22")], JAMES_LORD),
        F([sy("21:23"), sy("21:24"), sy("21:25")], JAMES_LORD),
        D([cp("21:26")], lambda w, h: A.temple_vow("tv1", w, h, 2126), "#8FD0E2", art_h=220),
        D([cp("21:27"), cp("21:28", to="crying out,"), sy("21:28", frm="Men of Israel, help:"), cp("21:29")], lambda w, h: A.temple_uproar("tu1", w, h, 2127), "#8FD0E2",
          head="The Uproar in the Temple", art_h=240),
        D([cp("21:30"), cp("21:31")], lambda w, h: A.temple_uproar("tu2", w, h, 2130), "#8FD0E2"),
        D([cp("21:32"), cp("21:33")], lambda w, h: A.antonia("an1", w, h, 2132, stage="run"), "#8FD0E2", head="The Castle", art_h=260),
        D([cp("21:34"), cp("21:35"), cp("21:36", to="crying out,"), sy("21:36", frm="Away with him.")], lambda w, h: A.antonia("an2", w, h, 2134, stage="borne"), "#8FD0E2", art_h=260),
        F([cp("21:37", to="he saith unto the chief captain,"), sy("21:37", frm="May I say something", to="unto thee?")], PAUL, h=220),
        F([cp("21:37", frm="And he said,", to="And he said,"), sy("21:37", frm="Dost thou know Greek?"), sy("21:38")], LYSIAS, bg=RED),
        F([cp("21:39", to="But Paul said,"), sy("21:39", frm="I am a Jew,")], PAUL),
        D([cp("21:40")], lambda w, h: A.antonia("an3", w, h, 2140, stage="speak"), "#8FD0E2", art_h=260),
        # Acts 22
        F([sy("22:1"), cp("22:2"), sy("22:3")], PAUL, head="Brethren and Fathers"),
        D([sy("22:4"), sy("22:5")], lambda w, h: A.gamaliel_feet("gf1", w, h, 2204), "#C8B490"),
        D([sy("22:6"), sy("22:7"), sy("22:8"), sy("22:9")], lambda w, h: A.damascus_road("dr1", w, h, 2206, fallen=True), "#5AB0D8", art_h=240, sky=22),
        D([sy("22:10"), sy("22:11")], lambda w, h: A.damascus_road("dr2", w, h, 2210, lit=False, led=True), "#5AB0D8"),
        D([sy("22:12"), sy("22:13"), sy("22:14")], lambda w, h: A.scales("sc1", w, h, 2212), "#D8C098", art_h=220),
        F([sy("22:15"), sy("22:16")], PAUL),
        D([sy("22:17"), sy("22:18")], lambda w, h: A.temple_trance("tt1", w, h, 2217), "#4A2A5A", art_h=220),
        D([sy("22:19"), sy("22:20"), sy("22:21")], lambda w, h: A.garments_wall("gw1", w, h, 2219), "#5A6A9A"),
        D([cp("22:22", to="and said,"), sy("22:22", frm="Away with such a fellow"), cp("22:23")], lambda w, h: A.antonia("an4", w, h, 2222, stage="dust"), "#8FD0E2",
          head="A Roman Born", art_h=260),
        D([cp("22:24"), cp("22:25", to="that stood by,"), sy("22:25", frm="Is it lawful"), cp("22:26", to="told him, saying,"), sy("22:26", frm="What art thou about to do?")],
          lambda w, h: A.thongs("th1", w, h, 2224), "#B8A07A", art_h=220),
        D([cp("22:27", to="and said unto him,"), sy("22:27", frm="Tell me,", to="a Roman?"), cp("22:27", frm="And he said,", to="And he said,"), sy("22:27", frm="Yea."),
           cp("22:28", to="answered,"), sy("22:28", frm="With a great sum", to="this citizenship."), cp("22:28", frm="And Paul said,", to="And Paul said,"),
           sy("22:28", frm="But I am a Roman born.")], lambda w, h: A.thongs("th2", w, h, 2227), "#B8A07A"),
        D([cp("22:29")], lambda w, h: A.antonia("an5", w, h, 2229, stage="bound"), "#8FD0E2")]
PG.extend(K.pack(SEGS, "ACT-C12-D", PG.next(), most=4, lone=1.5, end=nxt("NEXT · BEFORE FELIX")))
