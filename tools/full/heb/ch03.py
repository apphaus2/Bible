"""Hebrews volume, Chapter 3 — The Way into the Holy Place (Hebrews 9–10). Every verse, word for word from ref/eng-asv.
Hebrews 9: the candlestick and the table with the showbread as Exodus' blueprints (9:1–2); the Holy of holies as a plate —
the golden altar of incense, the ark in section with the pot of manna, Aaron's rod that budded and the tables of the
covenant, the cherubim of glory over the mercy-seat (9:3–5); the high priest alone before the veil with the censer, once in
the year, no blood drawn (9:6–7); the tabernacle as an elevation, a figure for the time present (9:8–10); the greater
tabernacle not made with hands drawn in light among the stars (9:11–12); the ashes of the heifer, the water, the hyssop and
the scarlet wool (9:13–14); the testament sealed and of force (9:15–17); the altar and the twelve pillars under Sinai, the
sprinkling in words (9:18–21); Jesus risen going up the steps of light into heaven itself (9:22–24); year by year and once
at the end of the ages, a timeline (9:25–26); the dawn over the hillside of tombs (9:27–28). Hebrews 10: the shadow of the
tabernacle on the floor, not the very image (10:1–4); the roll of the book (10:5–7, Christ's words in balloons); the three
crosses far off, once for all (10:8–10); the priest standing at the altar and the throne above (10:11–14); the roll of
reckoning washed clean (10:15–18, the Voice box); the veil rent (10:19–22); the church assembled, the letter read aloud
(10:23–25); fire on an empty dark plain (10:26–29); the storm (10:30–31); the prison door at night (10:32–34); the traveller
on the long road at first light (10:35–39)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from heb import G, art3 as A, ch02 as _prev
from heb.art import art
from heb.common import K, Pages, D, lt, lp, ltj, lj, sg, gd, sy, gj, sj, v, title, nxt

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("HEB-C03-00-Title", "Chapter 3 · The Way into the Holy Place", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A10"></rect><g transform="translate(0 340)">{A.once_a_year("t03", 760, 600, 6001)}</g>'
    return title(3, "The Way into the Holy Place", "Hebrews 9–10", svg, "#2A1A10", v("10:20", frm="a new and living way", to="through the veil"))


SEGS = [
    # Hebrews 9 — the first tabernacle; the greater tabernacle
    D(lp("9:1-2"), art(A.holy_place), "#0B1A2E", head="The First Tabernacle", sky=9, art_h=230),
    D(lp("9:3-5"), art(A.ark_contents), "#0B1A2E", head="The Holy of Holies", art_h=270),
    D(lp("9:6-7"), art(A.once_a_year, "oy1", 6006), "#2A1A10", head="Once in the Year", art_h=230),
    D(lp("9:8-10"), art(A.first_tent), "#0B1A2E", art_h=200),
    D(lp("9:11-12"), art(A.not_made, 6011), "#05051A", head="Not Made with Hands", art_h=220),
    D(lp("9:13-14"), art(A.ashes, 6013), "#2A1E18", art_h=200),
    D(lp("9:15-17"), art(A.testament), "#0B1A2E", art_h=210),
    D(lp("9:18-19") + [lt("9:20", to="saying,"), sg("9:20", frm="This is the blood"), lt("9:21")], art(A.covenant_altar, "ca1", 6018), "#8A6A4A", art_h=200),
    D(lp("9:22-24"), art(A.heaven_itself, "hi1", 6022), "#1A1440", head="Into Heaven Itself", art_h=240),
    D(lp("9:25-26"), art(A.year_by_year), "#0B1A2E", art_h=200),
    D(lp("9:27-28"), art(A.second_time, 6027), "#2A2A5A", art_h=200),
    # Hebrews 10 — once for all; the new and living way
    D(lp("10:1-4"), art(A.shadow, 6031), "#3A2A22", head="A Shadow of the Good Things to Come", sky=10, art_h=210),
    D([lt("10:5", to="he saith,"), K.j("say", ("10:5", "Sacrifice and offering"), "10:6", "10:7")], art(A.roll_of_book, "rb1", 6035), "#3A2418",
      head="Lo, I Am Come", art_h=210),
    D([lj("10:8", ("10:9", None, "then hath he said,")), sy("10:9", frm="Lo, I am come", to="thy will."), lj(("10:9", "He taketh away"), "10:10")],
      art(A.once_for_all, 6038), "#0B0B12", art_h=200),
    D(lp("10:11-14"), art(A.standing_priest, "sp1", 6041), "#5A5A9A", art_h=220),
    D([lt("10:15"), gd("10:16", to="write them;"), lt("10:16", frm="then saith he,"), gd("10:17"), lt("10:18")], art(A.remember_no_more, 6045), "#2A1E30", art_h=200),
    D(lp("10:19-22"), art(A.rent_veil, "rv1", 6049), "#1A1018", head="A New and Living Way", art_h=250),
    D(lp("10:23-25"), art(A.assembling, "as1", 6053), "#3A2418", art_h=210),
    D(lp("10:26-29"), art(A.fire_field, 6056), "#05050E", art_h=200),
    D([lt("10:30", to="him that said,"), gd("10:30", frm="Vengeance", to="I will recompense."), lt("10:30", frm="And again,", to="And again,"),
       sg("10:30", frm="The Lord shall judge"), lt("10:31")], art(A.storm, 6060), "#14141E", art_h=200),
    D(lp("10:32-34"), art(A.bonds, "bd1", 6062), "#0B0B2A", head="Call to Remembrance the Former Days", art_h=210),
    D(lp("10:35-36") + [lt("10:37", to="little while,"), gd("10:37", frm="He that cometh"), gd("10:38"), lt("10:39")], art(A.endure, "en1", 6065), "#2A2A5A",
      head="My Righteous One Shall Live by Faith", art_h=220),
]
PG.extend(K.pack(SEGS, "HEB-C03-D", PG.next(), end=nxt("NEXT · SO GREAT A CLOUD OF WITNESSES")))
