"""Hebrews volume, Chapter 4 — So Great a Cloud of Witnesses (Hebrews 11–13). Every verse, word for word from ref/eng-asv.
Hebrews 11: the worlds framed by the word of God (Romans' night giving way to dawn); then the elders one by one, each in the
look their own volume gives them — Abel at his altar and Cain's smoke beaten down; Enoch's footprints stopping at the
light; the ark ready under the coming storm; Abraham's road on the map; the tents of Abraham, Isaac and Jacob and the city
that hath the foundations in the sky; Sarah with the child; the pilgrims greeting the promises from afar; Moriah and the ram
in the thicket (11:18 in the Voice box); Jacob leaning on the top of his staff, blessing Joseph's sons; Joseph's coffin
borne out of Egypt; Moses hid by his parents; Moses turning from Pharaoh's house to his brethren; the bush that burned;
the passover street at midnight, every door shut; the Red sea; Jericho's wall fallen flat; Rahab's scarlet line; Gideon,
Barak, Samson, Jephthah, David and Samuel in a strip of faces; the lions' den and the furnace with no one drawn; and the
sufferings of 11:35–38 in words over the empty deserts, mountains, caves and holes of the earth; the company of the
faithful on the ridge at evening. Hebrews 12: the race in the stadium (12:1–2); the empty track (12:3–4, words only); a
household at its door (12:5–8, Proverbs in song boxes; no blow drawn); the vineyard's peaceable fruit; the burdens
lifted; the root of bitterness; Esau's pottage and his tears; Sinai burning, the camp kept back by the bounds (12:18–21, the
word enjoined in the Voice box, Moses' words in a song box); mount Zion, the city of light and the hosts of angels
(12:22–24); the earth and the heaven shaken (12:25–26); the pillar of fire over the tabernacle, a consuming fire
(12:27–29). Hebrews 13: the three men at Mamre, white with gold rims, no faces (13:1–2); a shut door (13:3–4); the loaf and
the purse set aside (13:5–6); yesterday, to-day and for ever (13:7–8); the fire without the camp (13:9–11); the gate and the
far hill of the three crosses (13:12–14); the company praising at sunrise; the shepherds watching by night; the
benediction over the light (13:20–21); Timothy walking out of the open prison door; they of Italy on the quay."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from heb import G, art4 as A, ch03 as _prev
from heb.art import art
from heb.common import K, Pages, D, lt, lp, ltj, lj, sg, gd, sy, gj, sj, v, title, glory, fin

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("HEB-C04-00-Title", "Chapter 4 · So Great a Cloud of Witnesses", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 380)">{A.witnesses("t04", 760, 560, 6101)}</g>'
    return title(4, "So Great a Cloud of Witnesses", "Hebrews 11–13", svg, "#14123A", v("12:1", frm="seeing we are compassed", to="cloud of witnesses"))


def creation(w, h):
    from rom.art import creation as c
    return c(w, h, 6102)

SEGS = [
    # Hebrews 11 — by faith
    D(lp("11:1-3"), art(creation), "#0B0B2A", head="By Faith", sky=11, art_h=200),
    D([lt("11:4")], art(A.abel, "ab1", 6104), "#3A2A5A", art_h=220),
    D(lp("11:5-6"), art(A.enoch, "en1", 6105), "#3A3A7A", art_h=200),
    D([lt("11:7")], art(A.ark_ready, "ar1", 6107), "#4A4A5E", art_h=210),
    D([lt("11:8")], art(A.abraham_road), "#0B1A2E", head="Abraham", art_h=210),
    D(lp("11:9-10"), art(A.sojourners, "sj1", 6109), "#05051A", art_h=220),
    D(lp("11:11-12"), art(A.promise_child, "pc1", 6111), "#8FD0E2", art_h=210),
    D(lp("11:13-16"), art(A.afar, "af1", 6113), "#2A1A3A", head="Strangers and Pilgrims", art_h=220),
    D([lt("11:17"), lt("11:18", to="it was said,"), gd("11:18", frm="In Isaac"), lt("11:19")], art(A.moriah, "mo1", 6117), "#5A7AB0", art_h=230),
    D([lt("11:20"), lt("11:21")], art(A.jacob_blessing, "jb1", 6120), "#3A2A1E", art_h=220),
    D([lt("11:22")], art(A.bones, "bn1", 6122), "#3A3A7A", art_h=210),
    D([lt("11:23")], art(A.moses_hid, "mh1", 6123), "#3A2418", head="Moses", art_h=210),
    D(lp("11:24-26"), art(A.moses_turns, "mt1", 6124), "#5AB0D8", art_h=220),
    D([lt("11:27")], art(A.bush, 6127), "#0B0B2A", art_h=200),
    D([lt("11:28")], art(A.passover, 6128), "#05051A", art_h=200),
    D([lt("11:29")], art(A.red_sea, "rs1", 6129), "#0F4C68", art_h=200),
    D([lt("11:30")], art(A.jericho, 6130), "#8FD0E2", art_h=200),
    D([lt("11:31")], art(A.rahab, 6131), "#8FD0E2", art_h=200),
    D([lt("11:32")], art(A.judges), "#1A1028", head="What Shall I More Say?", art_h=200),
    D(lp("11:33-34"), art(A.lions_fire, "lf1", 6133), "#1E1824", art_h=210),
    D(lp("11:35-38"), art(A.caves, 6135), "#2A1A3A", art_h=200),
    D(lp("11:39-40"), art(A.witnesses, "wt1", 6139), "#14123A", art_h=220),
    # Hebrews 12 — the race; mount Zion
    D(lp("12:1-2"), art(A.race, "rc1", 6201), "#8FD0E2", head="So Great a Cloud of Witnesses", sky=12, art_h=230),
    D(lp("12:3-4"), art(A.empty_track, 6203), "#2A1A3A", art_h=200),
    D([lt("12:5", to="as with sons,"), sg("12:5", frm="My son"), sg("12:6")] + lp("12:7-8"), art(A.household, "hh1", 6205), "#8FD0E2",
      head="The Chastening of the Lord", art_h=210),
    D(lp("12:9-11"), art(A.fruit_vines, 6209), "#8FD0E2", art_h=200),
    D(lp("12:12-13"), art(A.burdens, "bu1", 6212), "#8FD0E2", art_h=200),
    D(lp("12:14-15"), art(A.bitter_root, 6214), "#8FD0E2", art_h=210),
    D(lp("12:16-17"), art(A.esau), "#2A1A1A", art_h=210),
    D(lp("12:18-19") + [lt("12:20", to="enjoined,"), gd("12:20", frm="If even"), lt("12:21", to="Moses said,"), sg("12:21", frm="I exceedingly")],
      art(A.sinai, "si1", 6218), "#05050E", head="Not unto a Mount That Might Be Touched", art_h=220),
    D(lp("12:22-24"), art(A.zion, "zi1", 6222), "#3A2A6A", head="Unto Mount Zion", art_h=260),
    D([lt("12:25"), lt("12:26", to="saying,"), gd("12:26", frm="Yet once more")], art(A.shaken, 6225), "#14123A", art_h=210),
    D(lp("12:27-29"), art(A.pillar_fire, "pf1", 6227), "#05050E", head="A Consuming Fire", art_h=230),
    # Hebrews 13 — love of the brethren; without the gate; the great shepherd
    D(lp("13:1-2"), art(A.mamre, "mm1", 6301), "#8FD0E2", head="Entertaining Angels Unawares", sky=13, art_h=230),
    D(lp("13:3-4"), art(A.shut_door, 6303), "#8FD0E2", art_h=200),
    D([lt("13:5", to="hath said,"), gd("13:5", frm="I will in no wise"), lt("13:6", to="we say,"), sg("13:6", frm="The Lord is my helper")], art(A.content, 6305), "#4A3424", art_h=200),
    D(lp("13:7-8"), art(A.always, 6307), "#2A2A6A", head="The Same Yesterday and To-day", art_h=200),
    D(lp("13:9-11"), art(A.without_camp, 6309), "#2A1A3A", art_h=200),
    D(lp("13:12-14"), art(A.without_gate, "wg1", 6312), "#3A2A3A", head="Without the Gate", art_h=220),
    D(lp("13:15-16"), art(A.praise, "pr1", 6315), "#3A2A5A", art_h=200),
    D(lp("13:17-19"), art(A.watch, "wa1", 6317), "#05051A", art_h=200),
    glory([lt("13:20"), lt("13:21")], head="The Great Shepherd of the Sheep", seed=6320),
    D([lt("13:22"), lt("13:23")], art(A.timothy_free, "tf1", 6322), "#8FD0E2", art_h=220),
    D([lt("13:24"), lt("13:25")], art(A.italy, "it1", 6324), "#8FD0E2", art_h=220),
]
PG.extend(K.pack(SEGS, "HEB-C04-D", PG.next(), end=fin("END OF HEBREWS · NEXT · JAMES")))
