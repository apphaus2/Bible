"""Acts volume, Chapter 5 — The Road to Damascus (Acts 8–9). Every verse, word for word from ref/eng-asv.
Saul consenting, beside his face; the scattering on the map; devout men lamenting at Stephen's tomb; Saul laying waste the
church — a night street, a door broken in, Saul and the officers (the dragging told in words only). Philip in the city of
Samaria, a lame man leaping; Simon who used sorcery, a man on a step among the people (no sorcery drawn); the baptisms in
the stream; Peter and John laying on hands; the money offered; Thy silver perish with thee beside Peter's stern face. The
desert road to Gaza and the angel of the Lord (white light, no face); the Ethiopian in his chariot reading Isaiah; the
Spirit's words in the Voice box; the lamb before the shearer with the scroll (Isaiah's words in song boxes); the water by
the way; the chariot standing still; the map to Azotus and Cæsarea. The Damascus road: the light out of heaven poured on
the road and Saul fallen to the earth, the men with him speechless — Jesus is not drawn, his words come from the light in
speech boxes; Saul led by the hand; three days blind beside his face with the clouded eyes. Ananias' vision — the light
through the window, the Lord not drawn; the house in the street called Straight, the scales falling; Saul in the
synagogues; the basket let down over the wall by night; Barnabas bringing him to the apostles; the map to Tarsus; the
church at peace. Æneas rising at Lydda; Dorcas at Joppa among the widows and their coats, then raised alive; the tanner's
house by the sea."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art5 as A, ch04 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PETER, PETER_STERN, SAUL_PERSECUTOR, SAUL_BLIND,
                        PHILIP_EV, SIMON_MAGUS, SIMON_AFRAID, ETHIOPIAN, ANANIAS_DAM, BARNABAS, PAUL, WHITE_LIGHT)
from oba.minor import vista

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C05-00-Title", "Chapter 5 · The Road to Damascus", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5AB0D8"></rect><g transform="translate(0 260)">{A.damascus_road("t5", 760, 820, 903, fallen=True)}</g>'
    return title(5, "The Road to Damascus", "Acts 8 – 9", svg, "#2A4A7A", v("9:4", frm="Saul, Saul,"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)

SEGS = [F([cp("8:1", to="consenting unto his death.")], SAUL_PERSECUTOR, bg=RED, head="Scattered Abroad", h=220),
        D([cp("8:1", frm="And there arose")], A.scattered, "#0B1A2E", art_h=280, sky=(8, "left")),
        D([cp("8:2")], lambda w, h: A.mourners_tomb("mt1", w, h, 802), "#2A2A4A"),
        D([cp("8:3")], lambda w, h: A.laid_waste("lw1", w, h, 803), "#0B0B2A"),
        D([cp("8:4"), cp("8:5")], lambda w, h: A.philip_city("pc1", w, h, 804, healed=False), "#8FD0E2", head="Philip in Samaria"),
        D([cp("8:6"), cp("8:7"), cp("8:8")], lambda w, h: A.philip_city("pc2", w, h, 806), "#8FD0E2"),
        D([cp("8:9"), cp("8:10", to="saying,"), sy("8:10", frm="This man is"), cp("8:11")], lambda w, h: A.simon_crowd("sm1", w, h, 809), "#4A2A5A", head="Simon"),
        D([cp("8:12"), cp("8:13")], lambda w, h: A.stream("st1", w, h, 812), "#8FD0E2"),
        D([cp("8:14"), cp("8:15"), cp("8:16"), cp("8:17")], lambda w, h: A.hands_on("ho1", w, h, 814), "#D8C098", art_h=240),
        D([cp("8:18"), cp("8:19", to="saying,"), sy("8:19", frm="Give me also")], lambda w, h: A.hands_on("ho2", w, h, 818, money=True), "#D8C098", art_h=240),
        F([cp("8:20", to="But Peter said unto him,"), sy("8:20", frm="Thy silver"), sy("8:21"), sy("8:22"), sy("8:23")], PETER_STERN, bg=RED),
        F([cp("8:24", to="answered and said,"), sy("8:24", frm="Pray ye for me")], SIMON_AFRAID, bg=COLD),
        D([cp("8:25")], scene("rd1", 825, "road", [(0.3, "peter", {"flip": True}), (0.2, "john", {"flip": True})]), "#8FD0E2"),
        D([cp("8:26", to="saying,"), sy("8:26", frm="Arise, and go")], lambda w, h: A.desert_road("dr1", w, h, 826), "#5AB0D8", head="The Way unto Gaza"),
        D([cp("8:27"), cp("8:28")], lambda w, h: A.desert_road("dr2", w, h, 827, angel_=False, chariot_=True, philip_x=0.12), "#5AB0D8", art_h=240),
        D([cp("8:29", to="unto Philip,"), gd("8:29", frm="Go near,"), cp("8:30", to="and said,"), sy("8:30", frm="Understandest")],
          lambda w, h: A.desert_road("dr3", w, h, 829, angel_=False, chariot_=True, philip_x=0.4, running=True), "#5AB0D8"),
        F([cp("8:31", to="And he said,"), sy("8:31", frm="How can I,", to="guide me?"), cp("8:31", frm="And he besought")], ETHIOPIAN),
        D([cp("8:32", to="was this,"), sg("8:32", frm="He was led"), sg("8:33")], lambda w, h: A.lamb_scroll("ls1", w, h, 832), "#E8D8B8"),
        F([cp("8:34", to="and said,"), sy("8:34", frm="I pray thee,")], ETHIOPIAN),
        D([cp("8:35"), cp("8:36", to="the eunuch saith,"), sy("8:36", frm="Behold, here is water;")],
          lambda w, h: A.desert_road("dr4", w, h, 835, angel_=False, chariot_=True, philip_x=0.4, reading=False), "#5AB0D8"),
        D([cp("8:38")], lambda w, h: A.stream("st2", w, h, 838, who="eunuch", chariot_=True), "#8FD0E2", art_h=240),
        D([cp("8:39"), cp("8:40")], A.alone_road, "#0B1A2E", art_h=260),
        # Acts 9
        D([cp("9:1"), cp("9:2")], lambda w, h: A.council("hp1", w, h, 901, accused=("saul",)), "#4A3A44", head="The Road to Damascus"),
        D([cp("9:3")], lambda w, h: A.damascus_road("dm1", w, h, 903), "#5AB0D8", art_h=260, sky=9),
        D([cp("9:4", to="saying unto him,"), sy("9:4", frm="Saul, Saul,"), cp("9:5", to="And he said,"), sy("9:5", frm="Who art thou, Lord?", to="Who art thou, Lord?"),
           cp("9:5", frm="And he said,", to="And he said,", after="Lord?"), sy("9:5", frm="I am Jesus"), sy("9:6")],
          lambda w, h: A.damascus_road("dm2", w, h, 904, fallen=True), "#5AB0D8", art_h=260),
        D([cp("9:7"), cp("9:8")], lambda w, h: A.damascus_road("dm3", w, h, 907, lit=False, led=True), "#5AB0D8"),
        F([cp("9:9")], SAUL_BLIND, bg=COLD, h=220),
        D([cp("9:10", to="in a vision,"), sy("9:10", frm="Ananias.", to="Ananias."), cp("9:10", frm="And he said,", to="And he said,"), sy("9:10", frm="Behold, I am here")],
          lambda w, h: A.vision_house("vh1", w, h, 910), "#4A3A3A", art_h=240, head="Ananias"),
        D([cp("9:11", to="said unto him,"), sy("9:11", frm="Arise, and go"), sy("9:12")], lambda w, h: A.vision_house("vh2", w, h, 911, pray=False), "#4A3A3A", art_h=240),
        F([cp("9:13", to="But Ananias answered,"), sy("9:13", frm="Lord, I have heard"), sy("9:14")], ANANIAS_DAM),
        D([cp("9:15", to="said unto him,"), sy("9:15", frm="Go thy way:"), sy("9:16")], lambda w, h: A.vision_house("vh3", w, h, 915), "#4A3A3A", art_h=240),
        D([cp("9:17", to="on him said,"), sy("9:17", frm="Brother Saul,")], lambda w, h: A.scales("sc1", w, h, 917), "#D8C098", art_h=260, head="The Street Called Straight"),
        D([cp("9:18"), cp("9:19", to="was strengthened.")], lambda w, h: A.scales("sc2", w, h, 918), "#D8C098", art_h=260),
        D([cp("9:19", frm="And he was certain days"), cp("9:20"), cp("9:21", to="and said,"), sy("9:21", frm="Is not this he"), cp("9:22")],
          scene("sy1", 919, "synagogue", [(0.2, "paul", {"flip": True, "up": A.UP_BLESS}), (0.42, "seated", {"c": "#6A5A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True}),
                                          (0.56, "seated", {"c": "#3A4A6A", "v": "#3A4A6A", "flip": True}), (0.7, "man", {"c": "#5A2A4A", "v": "#2A2A3A", "bd": "#2A1A10", "flip": True}),
                                          (0.82, "man", {"c": "#8A6A2A", "v": "#E8E2D6", "bd": "#6A645E"})]), "#C8B490"),
        D([cp("9:23"), cp("9:24"), cp("9:25")], lambda w, h: A.basket_wall("bw1", w, h, 923), "#05051A", art_h=260, head="Let Down in a Basket"),
        D([cp("9:26"), cp("9:27")], scene("bn1", 926, "upper", [(0.12, "barnabas", {"flip": True, "up": A.UP_BLESS}), (0.24, "paul", {"flip": True}),
                                                                (0.5, ("apostle", 0)), (0.6, ("apostle", 1)), (0.7, ("apostle", 2)), (0.82, ("apostle", 4), {"flip": True})]), "#C8A878"),
        D([cp("9:28"), cp("9:29"), cp("9:30")], A.tarsus_road, "#0B1A2E", art_h=240),
        D([cp("9:31")], lambda w, h: vista(w, h, 931, tone="day", horizon=0.56, hills_n=2, trees=3, sheep=7, field="grain"), "#8FD0E2"),
        D([cp("9:32"), cp("9:33")], lambda w, h: A.aeneas("ae1", w, h, 932), "#D8C098", art_h=240, head="Æneas and Dorcas"),
        D([cp("9:34", to="said unto him,"), sy("9:34", frm="Aeneas,", to="make thy bed."), cp("9:34", frm="And straightway he arose."), cp("9:35")],
          lambda w, h: A.aeneas("ae2", w, h, 934, risen=True), "#D8C098", art_h=240),
        D([cp("9:36"), cp("9:37")], lambda w, h: A.dorcas("dc1", w, h, 936), "#C8A878", art_h=240),
        D([cp("9:38", to="entreating him,"), sy("9:38", frm="Delay not"), cp("9:39")], lambda w, h: A.dorcas("dc2", w, h, 938), "#C8A878", art_h=240),
        D([cp("9:40", to="he said,"), sy("9:40", frm="Tabitha, arise.", to="Tabitha, arise."), cp("9:40", frm="And she opened"), cp("9:41")], lambda w, h: A.dorcas("dc3", w, h, 940, raised=True), "#C8A878", art_h=240),
        D([cp("9:42"), cp("9:43")], lambda w, h: A.tanner("tn1", w, h, 942), "#8FD0E2")]
PG.extend(K.pack(SEGS, "ACT-C05-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · WHAT GOD HATH CLEANSED")))
