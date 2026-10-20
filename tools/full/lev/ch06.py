"""Leviticus volume, Chapter 6 — The Day of Atonement (Leviticus 16–18). Every verse, word for word from ref/eng-asv.
The Day of Atonement (16) as blueprint panels; the blood (17) and the forbidden degrees (18) as law cells, the kinship
laws drawn only as family-tree charts (lev/art6.py)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from exo import art8 as B8
from exo.kit import law_pages, set_book, blueprints
from lev import G, art6 as K
from lev import ch05 as _prev

v, sp = G.v, G.span
set_book(G)
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"
def g(refs): return [("god", sp(refs))]


@P("LEV-C06-00-Title", "Chapter 6 · The Day of Atonement")
def title():
    svg = f'<g transform="translate(0 280) scale(1.083)">{K.b_wilderness(702, 740, "t6")}</g>' + f'<rect x="0" y="0" width="760" height="300" fill="#C8A06A"></rect>'
    return chapter_title(6, "第六話", "The Day of Atonement", "Leviticus 16 – 18", svg, "#C8A06A", v("16:22", to="unto a solitary land:").rstrip(":"), "Leviticus · Volume Three")


DAY = [
    ("16:1–2", [("cap", v("16:1")), ("cap", v("16:2", to="unto Moses,")), ("god", v("16:2", frm="Speak unto"))], K.b_cloud, "That He Come Not at All Times"),
    ("16:3–4", g("16:3-4"), K.b_linen, None),
    ("16:5–6", g("16:5-6"), K.b_bullock, None),
    ("16:7–10", g("16:7-10"), lambda w, h: K.b_goats(w, h, lots=True), "One Lot for Jehovah, the Other for Azazel"),
    ("16:11–13", g("16:11-13"), K.b_censer, "Within the Veil"),
    ("16:14", g("16:14"), K.b_sprinkle, None),
    ("16:15–16", g("16:15-16"), K.b_sprinkle, None),
    ("16:17–19", g("16:17-19"), K.b_altar_blood, None),
    ("16:20–21", g("16:20-21"), K.b_confess, "The Live Goat"),
    ("16:22", g("16:22"), K.b_wilderness, None),
    ("16:23–25", g("16:23-25"), K.b_bathe, None),
    ("16:26–28", g("16:26-28"), K.b_without, None),
    ("16:29–31", g("16:29-31"), K.b_tenth, "A Statute for Ever"),
    ("16:32–34", g("16:32-34"), K.b_once, None),
]
PAGES += blueprints(DAY, "LEV-C06", START, "The Day of Atonement", book="Leviticus")
NEXT = START + len(PAGES) - 1

LAWS = [
    ("UNTO THE DOOR OF THE TENT", "17:1-4", K.pg_door_only, SAY, "The Life of the Flesh Is in the Blood"),
    ("IN THE OPEN FIELD", "17:5-6", K.pg_field, "", None),
    ("NO MORE UNTO THE HE-GOATS", "17:7", K.pg_he_goats, "", None),
    ("THE STRANGERS THAT SOJOURN", "17:8-9", K.pg_stranger, "", None),
    ("THE LIFE OF THE FLESH", "17:10-12", K.pg_life_blood, "", None),
    ("COVER IT WITH DUST", "17:13-14", K.pg_cover_dust, "", None),
    ("TORN OF BEASTS", "17:15-16", K.pg_torn_wash, "", None),
    ("I AM JEHOVAH YOUR GOD", "18:1-3", K.pg_egypt_canaan, SAY, "Ye Shall Not Do After Their Doings"),
    ("HE SHALL LIVE IN THEM", "18:4-5", K.pg_live, "", None),
    ("NEAR OF KIN", "18:6", K.pg_near_kin, "", None),
    ("THY MOTHER", "18:7", K.pg_k_parents, "", "None of You Shall Approach"),
    ("THY FATHER'S WIFE", "18:8", K.pg_k_fwife, "", None),
    ("THY SISTER", "18:9", K.pg_k_sister, "", None),
    ("THY SON'S DAUGHTER", "18:10", K.pg_k_grand, "", None),
    ("THY FATHER'S WIFE'S DAUGHTER", "18:11", K.pg_k_half, "", None),
    ("THY FATHER'S SISTER", "18:12", K.pg_k_aunts, "", None),
    ("THY MOTHER'S SISTER", "18:13", K.pg_k_maunt, "", None),
    ("THY FATHER'S BROTHER'S WIFE", "18:14", K.pg_k_uncle, "", None),
    ("THY DAUGHTER-IN-LAW", "18:15", K.pg_k_dil, "", None),
    ("THY BROTHER'S WIFE", "18:16", K.pg_k_bwife, "", None),
    ("A WOMAN AND HER DAUGHTER", "18:17", K.pg_k_wdaughter, "", None),
    ("TO HER SISTER", "18:18", K.pg_k_sisters, "", None),
    ("AS LONG AS SHE IS IMPURE", "18:19", K.pg_impure, "", None),
    ("THY NEIGHBOR'S WIFE", "18:20", K.pg_neighbor, "", None),
    ("MOLECH", "18:21", K.pg_molech, "", None),
    ("ABOMINATION", "18:22-23", K.pg_abomination, "", None),
    ("THE LAND IS DEFILED", "18:24-25", K.pg_vomit, "", "That the Land Vomit Not You Out"),
    ("KEEP MY STATUTES", "18:26-28", K.pg_keep, "", None),
    ("CUT OFF", "18:29-30", K.pg_keep, "", None),
]
PAGES += law_pages(LAWS, "LEV-C06-L", NEXT, "Ye Shall Not Do After Their Doings", end=end_mark("NEXT · HOLY UNTO JEHOVAH", "right: 10px; top: 10px"))
