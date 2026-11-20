"""Ephesians volume, Chapter 2 — The Whole Armor of God (Ephesians 4–6). Every verse, word for word from ref/eng-asv.
Ephesians 4: Paul standing in his chain beseeching them to walk worthily, the soldier by him (4:1–3); the seven "ones" as an
emblem plate, the one God and Father of all a medallion of light (4:4–6); "he led captivity captive" in a song box over a
road of light, the fetters broken, gifts of light falling to men (4:7–8); the parenthesis beside Paul's face (4:9–10); the
gifts as a plate with the measuring rod of the fullgrown man (4:11–13); a little boat tossed by wind and wave (4:14); the body
fitly framed, its joints and bands, under the head of light (4:15–16); the vanity of the Gentiles in words over Ephesus' dark,
empty street, the temple of Diana red with torches far off (4:17–19); the old man put away and the new put on as two garments
(4:20–24); the sun going down over the harbour (4:25–28); "grieve not the Holy Spirit" beside Paul's face (4:29–32).
Ephesians 5: incense rising in a column of light (5:1–2); 5:3–7 in words over a dark, empty street; children of light
walking at sunrise (5:8–10); "Awake, thou that sleepest" in a song box over the sleeper and the dawn at the door (5:11–14);
"look carefully how ye walk" beside Paul's face (5:15–17); psalms and hymns by lamplight, one sitting with a lyre (5:18–21);
wives and husbands as a plain household at the door (5:22–24); Christ and the church beside Paul's face in white light
(5:25–27); "the two shall become one flesh" in a song box over the bridal emblem, a veil and a lamp (5:28–33).
Ephesians 6: "Honor thy father and mother" in song boxes over a father sitting with his son at the roll (6:1–4); servants and
masters as a plain household scene (6:5–8); "forbear threatening" beside Paul's stern face (6:9); Paul and the soldier he is
chained to, face to face (6:10–11); the spiritual hosts of wickedness in words over darkness only (6:12); THE WHOLE ARMOR OF
GOD as a plate of the Roman soldier, each piece labelled, the fiery darts struck out in the shield (6:13–17); Paul in his chain
praying, an ambassador in chains (6:18–20); Paul giving the sealed letter to Tychicus at the door (6:21–22); the benediction
over the light (6:23–24)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from eph import G, art as A, art2 as A2, ch01 as _prev
from eph.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, v, title, fin, PAUL, PAUL_LAMP, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG,
                        JOY_BG, STERN_BG)
from eph.art import art
from epistle import clipped

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("EPH-C02-00-Title", "Chapter 2 · The Whole Armor of God", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect>'
           f'<g transform="translate(20 380)">{clipped(lambda w, h: A2.armour_plate("t02", w, h))(720, 560)}</g>')
    return title(2, "The Whole Armor of God", "Ephesians 4–6", svg, "#0B1A2E", v("6:11", to="the whole armor of God,"))


SEGS = [
    # Ephesians 4 — walk worthily; one body; the gifts; the new man
    D(lp("4:1-3"), art(A.prison, "pr3", 5201, sit=False), "#3A2418", head="Walk Worthily", sky=4, art_h=300),
    D(lp("4:4-6"), art(A2.seven_ones), "#0B1A2E", head="One Body, and One Spirit", art_h=340),
    D([lt("4:7"), lt("4:8", to="saith,"), sg("4:8", frm="When he ascended"), ltj("4:9-10")], art(A2.captivity, "cc1", 5208), "#2A1E5A",
      head="He Led Captivity Captive", art_h=300),
    D(lp("4:11-13"), art(A2.gifts), "#0B1A2E", head="Some to Be Apostles", art_h=320),
    D([lt("4:14")], art(A2.tossed, 5214), "#2A3040", head="Tossed to and Fro", art_h=270),
    D(lp("4:15-16"), art(A2.body_plate), "#0B1A2E", head="Fitly Framed and Knit Together", art_h=340),
    D(lp("4:17-19"), art(A2.ephesus_night, 5217), "#05050E", head="The Vanity of Their Mind", art_h=230),
    D(lp("4:20-24"), art(A2.garments), "#0B1A2E", head="Put On the New Man", art_h=290),
    D(lp("4:25-28"), art(A2.sundown, 5225), "#2A1E4A", head="Let Not the Sun Go Down", art_h=250),
    F(lp("4:29-32"), PAUL),
    # Ephesians 5 — walk in love; children of light; husbands and wives
    D(lp("5:1-2"), art(A2.sweet_smell, 5301), "#1A1028", head="An Odor of a Sweet Smell", sky=5, art_h=300),
    D(lp("5:3-7"), art(A.dark_street, 5303), "#05050E", head="Let It Not Even Be Named", art_h=210),
    D(lp("5:8-10"), art(A2.children_light, "cl1", 5308), "#8FD0E2", head="Children of Light", art_h=290),
    D([lt("5:11"), lt("5:12"), lt("5:13"), lt("5:14", to="saith,"), sg("5:14", frm="Awake")], art(A2.awake, "aw1", 5311), "#14101E",
      head="Awake, Thou That Sleepest", art_h=280),
    F(lp("5:15-17"), PAUL),
    D(lp("5:18-21"), art(A2.hymns, "hy1", 5318), "#5A3E2E", head="Psalms and Hymns and Spiritual Songs", art_h=300),
    D(lp("5:22-24"), art(A2.household, "hh1", 5322), "#8FD0E2", head="Wives and Husbands", art_h=280),
    F(lp("5:25-27"), PAUL_JOY, bg=JOY_BG),
    D([*lp("5:28-30"), sg("5:31"), lt("5:32"), lt("5:33")], art(A2.bridal, 5328), "#E8C878", head="This Mystery Is Great", art_h=280),
    # Ephesians 6 — children and fathers; servants and masters; the whole armor of God
    D([lt("6:1"), sg("6:2", to="mother"), lt("6:2", frm="(which"), sg("6:3"), lt("6:4")], art(A2.father_son, "fs1", 5401), "#8FD0E2",
      head="Children, Obey Your Parents", sky=6, art_h=230),
    D(lp("6:5-8"), art(A2.servant_master, "sm1", 5405), "#8FD0E2", head="Servants and Masters", art_h=220),
    F([lt("6:9")], PAUL_STERN, bg=STERN_BG),
    D(lp("6:10-11"), art(A2.two_faces, 5410), "#A8603A", head="The Whole Armor of God", art_h=380),
    D([lt("6:12")], art(A2.hosts_dark, 5412), "#020206", art_h=230),
    D(lp("6:13-17"), lambda w, h: A2.armour_plate("ap1", w, h), "#0B1A2E", art_h=600),
    D(lp("6:18-20"), art(A.prison, "pr4", 5418, sit=False, up=A.PRAY, scribe=False), "#3A2418", head="An Ambassador in Chains", art_h=210),
    D(lp("6:21-22"), art(A.prison, "pr5", 5421, stage="prison_give", scribe=False), "#3A2418", head="Tychicus, the Beloved Brother", art_h=230),
    glory([lt("6:23"), lt("6:24")], h=900, head="Grace Be with All"),
]
PG.extend(K.pack(SEGS, "EPH-C02-D", PG.next(), end=fin("END OF EPHESIANS · NEXT · PHILIPPIANS")))
