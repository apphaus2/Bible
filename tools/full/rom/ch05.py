"""Romans volume, Chapter 5 — A Living Sacrifice (Romans 12–16). Every verse, word for word from ref/eng-asv.
A man before the altar with his hands lifted, presenting himself (12:1, no beast slain); the plates of one body and of the
gifts; the believers at table; "Vengeance belongeth unto me; I will recompense, saith the Lord" in the Voice box; bread,
water and a pan of coals on a doorstep (12:20). Romans 13: a Roman on the judgment-seat (Gallio, as Acts draws him) and the
plate of tribute and the sheathed sword; the commandments of 13:9 in the Voice box over the plate of the law summed up in
one heart; the armour of light by the window at dawn, 13:13's revelling and wantonness in words only. Romans 14: herbs and
meat at one table; the plate of the days; "As I live, saith the Lord" in the Voice box over the throne in light and every
knee bowed far below (God never drawn); meat and wine set aside. Romans 15: the psalms and Isaiah in song boxes, the root
of Jesse, the nations with hands lifted; the benedictions of 15:5–6, 15:13 and 15:33 as glory panels; the maps of the road
round unto Illyricum and on to Spain. Romans 16: Phoebe come to Rome with the letter; the greetings roll (epistle.greetings),
every saint a shaded profile face in a cool, dark or off-white headcloth or veil; 16:17–20 over Rome at evening, Satan
never drawn and no serpent (16:20 words only); the brethren at Corinth — Timothy and the kinsmen, then Tertius' own line
(16:22) beside his face with the tail toward him, Gaius, Erastus and Quartus; and the doxology of 16:25–27 over the burst
of light. 16:24 has no text in the ASV (the verse number is empty), so the coverage lists it as omitted."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rom import G, art5 as A, ch04 as _prev
from rom.common import (K, Pages, D, F, lt, lp, sg, gd, v, title, fin, glory, PAUL, PAUL_STERN, PAUL_JOY, PAUL_GRIEF, PAUL_LAMP, GOLD_BG, STERN_BG, JOY_BG,
                        GRIEF_BG, LAMP_BG, TERTIUS, AQUILA, PRISCILLA, EPAENETUS, MARY_ROME, ANDRONICUS, JUNIAS, AMPLIATUS, URBANUS, STACHYS, APELLES,
                        ARISTOBULUS_H, HERODION, NARCISSUS_H, TRYPHAENA, TRYPHOSA, PERSIS, RUFUS, RUFUS_MOTHER, ASYNCRITUS, HERMAS, PHILOLOGUS, JULIA, NEREUS,
                        OLYMPAS)
from epistle import greetings, face_portrait

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ROM-C05-00-Title", "Chapter 5 · A Living Sacrifice", title=True)
def title_page(n):
    svg = f'<g transform="translate(0 300)">{A.living_sacrifice("t05", 760, 780, 505)}</g><rect x="0" y="0" width="760" height="302" fill="#5A7AA8"></rect>'
    return title(5, "A Living Sacrifice", "Romans 12–16", svg, "#3A5A8A", v("12:1", frm="present your bodies a living sacrifice", to="acceptable to God,"))


def st(p, seed, **k): return lambda w, h: A.study(p, w, h, seed, **k)

SEGS = [
    # Romans 12
    D(lp("12:1-2"), lambda w, h: A.living_sacrifice("ls1", w, h, 1201), "#5A7AA8", head="A Living Sacrifice", sky=12, art_h=250),
    F([lt("12:3")], PAUL),
    D(lp("12:4-5"), lambda w, h: A.one_body(w, h), "#0B1A2E", head="One Body", art_h=250),
    D(lp("12:6-8"), lambda w, h: A.gifts_plate(w, h), "#0B1A2E", art_h=190),
    F(lp("12:9-12"), PAUL_JOY, bg=JOY_BG),
    D([lt("12:13")], lambda w, h: A.table_guests("tg1", w, h, 1213), "#4A3A3A", art_h=200),
    F(lp("12:14-18"), PAUL),
    D([lt("12:19", to="for it is written,"), gd("12:19", frm="Vengeance belongeth unto me"), lt("12:20"), lt("12:21")], lambda w, h: A.coals(w, h, 1219), "#3A2A2A",
      head="Overcome Evil with Good", art_h=210),
    # Romans 13
    D(lp("13:1-3"), lambda w, h: A.ruler_seat("rs1", w, h, 1301), "#8FD0E2", head="The Higher Powers", sky=13, art_h=210),
    D(lp("13:4-7"), lambda w, h: A.tribute(w, h), "#0B1A2E", art_h=210),
    F([lt("13:8")], PAUL),
    D([lt("13:9", to="For this,"), gd("13:9", frm="Thou shalt not commit adultery", to="Thou shalt not covet,"), lt("13:9", frm="and if there be any other", to="namely,"),
       gd("13:9", frm="Thou shalt love thy neighbor"), lt("13:10")], lambda w, h: A.law_love(w, h), "#0B1A2E", art_h=210),
    D(lp("13:11-14"), lambda w, h: A.armor_light(w, h, 1311), "#1E1828", head="The Armor of Light", art_h=250),
    # Romans 14
    D(lp("14:1-4"), lambda w, h: A.two_diners("dn1", w, h, 1401), "#C8A878", head="The Weak and the Strong", sky=14, art_h=230),
    D(lp("14:5-6"), lambda w, h: A.days_plate(w, h), "#0B1A2E", art_h=170),
    F(lp("14:7-9"), PAUL),
    D([lt("14:10"), lt("14:11", to="For it is written,"), gd("14:11", frm="As I live"), lt("14:12")], lambda w, h: A.knees_bow("kb1", w, h, 1410), "#2A3A7A",
      head="Every Knee Shall Bow", art_h=250),
    F(lp("14:13-16"), PAUL_STERN, bg=STERN_BG),
    F(lp("14:17-19"), PAUL_JOY, bg=JOY_BG),
    D(lp("14:20-23"), lambda w, h: A.meat_wine(w, h, 1420), "#4A3424", art_h=190),
    # Romans 15
    D([lt("15:1"), lt("15:2"), lt("15:3", to="as it is written,"), sg("15:3", frm="The reproaches"), lt("15:4")], st("st15", 1501), "#3A2418",
      head="We That Are Strong", sky=15, art_h=230),
    glory(lp("15:5-6"), seed=1505, h=300),
    D([lt("15:7"), lt("15:8"), lt("15:9", to="as it is written,"), sg("15:9", frm="Therefore will I give praise")], lambda w, h: A.nations_praise("np1", w, h, 1507),
      "#4A2A5A", head="Rejoice, Ye Gentiles", art_h=220),
    D([lt("15:10", to="And again he saith,"), sg("15:10", frm="Rejoice, ye Gentiles"), lt("15:11", to="And again,"), sg("15:11", frm="Praise the Lord"),
       lt("15:12", to="Isaiah saith,"), sg("15:12", frm="There shall be the root")], lambda w, h: A.jesse_root(w, h, 1510), "#5A7AA8", art_h=220),
    glory([lt("15:13")], seed=1513, h=240),
    F(lp("15:14-16"), PAUL, head="Unto Illyricum"),
    D(lp("15:17-19"), lambda w, h: A.illyricum(w, h), "#0B1A2E", art_h=260),
    D([lt("15:20"), lt("15:21", to="as it is written,"), sg("15:21", frm="They shall see"), lt("15:22")], st("st20", 1520, stage="read"), "#3A2418", art_h=220),
    D(lp("15:23-26"), lambda w, h: A.to_spain(w, h), "#0B1A2E", head="Unto Spain", art_h=260),
    F(lp("15:27-29"), PAUL_JOY, bg=JOY_BG),
    F(lp("15:30-32"), PAUL_GRIEF, bg=GRIEF_BG),
    glory([lt("15:33")], seed=1533, h=220),
    # Romans 16 — Phoebe
    D(lp("16:1-2"), lambda w, h: A.phoebe_rome("pr1", w, h, 1601), "#8FD0E2", head="I Commend unto You Phoebe", sky=16, art_h=300),
]
PG.extend(K.pack(SEGS, "ROM-C05-D", PG.next()))

fp = face_portrait
ITEMS = [("PRISCA & AQUILA", "16:3–5 · MY FELLOW-WORKERS", [lt("16:3"), lt("16:4"), lt("16:5", to="in their house.")], fp(AQUILA, PRISCILLA)),
         ("EPÆNETUS", "16:5 · THE FIRSTFRUITS OF ASIA", [lt("16:5", frm="Salute Epænetus")], fp(EPAENETUS)),
         ("MARY", "16:6 · MUCH LABOR ON YOU", [lt("16:6")], fp(MARY_ROME)),
         ("ANDRONICUS & JUNIAS", "16:7 · MY FELLOW-PRISONERS", [lt("16:7")], fp(ANDRONICUS, JUNIAS)),
         ("AMPLIATUS", "16:8 · MY BELOVED IN THE LORD", [lt("16:8")], fp(AMPLIATUS)),
         ("URBANUS & STACHYS", "16:9 · OUR FELLOW-WORKER", [lt("16:9")], fp(URBANUS, STACHYS)),
         ("APELLES", "16:10 · THE APPROVED IN CHRIST", [lt("16:10")], fp(APELLES, ARISTOBULUS_H)),
         ("HERODION", "16:11 · MY KINSMAN", [lt("16:11")], fp(HERODION, NARCISSUS_H)),
         ("TRYPHÆNA · TRYPHOSA · PERSIS", "16:12 · WHO LABOR IN THE LORD", [lt("16:12")], fp(TRYPHAENA, PERSIS)),
         ("RUFUS", "16:13 · THE CHOSEN IN THE LORD", [lt("16:13")], fp(RUFUS, RUFUS_MOTHER)),
         ("ASYNCRITUS · HERMAS", "16:14 · AND THE BRETHREN", [lt("16:14")], fp(ASYNCRITUS, HERMAS)),
         ("PHILOLOGUS & JULIA", "16:15 · ALL THE SAINTS", [lt("16:15")], fp(PHILOLOGUS, JULIA))]
K.label()                                                       # the greetings' verses are labelled by their cells, not the next panel
PG.extend(greetings(ITEMS, "ROM-C05-G", PG.next(), "Romans", "ROM", head="Salute", most=4))

SEGS2 = [
    D(lp("16:16-18"), lambda w, h: A.rome("re1", w, h, 1616), "#8FD0E2", head="The God of Peace", art_h=220),
    F(lp("16:19-20"), PAUL_JOY, bg=JOY_BG),
    D([lt("16:21")], lambda w, h: A.brethren("bt1", w, h, 1621), "#5A3E2E", head="I Tertius", art_h=260),
    F([lt("16:22")], TERTIUS, bg=LAMP_BG, flip=False),
    D([lt("16:23")], lambda w, h: A.brethren("bt2", w, h, 1623, stage="gaius"), "#5A3E2E", art_h=260),
    glory(lp("16:25-27"), seed=1625, head="To the Only Wise God", h=620),
]
PG.extend(K.pack(SEGS2, "ROM-C05-E", PG.next(), end=fin("END OF ROMANS · NEXT · 1 CORINTHIANS")))
