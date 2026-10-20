"""Leviticus volume, Chapter 9 — Blessing and Curse (Leviticus 26–27), the end of Leviticus. Every verse, word for word
from ref/eng-asv. All law cells (lev/art9.py): the blessings, the curses drawn as the land under judgment, and the estimations
of vows and tithes as charts. The volume ends with 完."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import chapter_title, end_mark
from exo import art8 as B8
from exo.kit import law_pages, set_book
from lev import G, art9 as K
from lev import ch08 as _prev

v, sp = G.v, G.span
set_book(G)
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"


@P("LEV-C09-00-Title", "Chapter 9 · Blessing and Curse")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A2458"></rect>' + V.rays(380, 520, 40, 30, 1100, color="#FFF4C2", op=0.2)
           + f'<g transform="translate(0 500) scale(2.375)">{mk.defs("t9", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic") + K.pg_tabernacle("t9")}</g>')
    return chapter_title(9, "第九話", "Blessing and Curse", "Leviticus 26 – 27", svg, "#2A2458", v("26:12"), "Leviticus · Volume Three")


LAWS = [
    ("NO IDOLS · MY SABBATHS", "26:1-2", K.pg_no_idols, "", "If Ye Walk in My Statutes"),
    ("RAINS IN THEIR SEASON", "26:3-4", K.pg_rain, "", None),
    ("UNTO THE VINTAGE", "26:5", K.pg_threshing, "", None),
    ("PEACE IN THE LAND", "26:6", K.pg_peace, "", None),
    ("FIVE OF YOU SHALL CHASE A HUNDRED", "26:7-8", K.pg_chase, "", None),
    ("FRUITFUL", "26:9-10", K.pg_fruitful, "", None),
    ("MY TABERNACLE AMONG YOU", "26:11-12", K.pg_tabernacle, "", None),
    ("THE BARS OF YOUR YOKE", "26:13", K.pg_yoke, "", None),
    ("IF YE WILL NOT HEARKEN", "26:14-15", K.pg_reject, "", "But If Ye Will Not Hearken"),
    ("TERROR · CONSUMPTION · FEVER", "26:16-17", K.pg_terror, "", None),
    ("HEAVEN AS IRON", "26:18-20", K.pg_iron, "", None),
    ("SEVEN TIMES MORE PLAGUES", "26:21-22", K.pg_beasts, "", None),
    ("I WILL SMITE YOU", "26:23-24", K.pg_seven_more, "", None),
    ("A SWORD UPON YOU", "26:25", K.pg_sword, "", None),
    ("YOUR STAFF OF BREAD", "26:26", K.pg_bread, "", None),
    ("IN WRATH", "26:27-29", K.pg_wrath, "", None),
    ("YOUR HIGH PLACES", "26:30", K.pg_high_places, "", None),
    ("YOUR CITIES A WASTE", "26:31-32", K.pg_waste, "", None),
    ("AMONG THE NATIONS", "26:33", K.pg_scatter, "", None),
    ("THE LAND SHALL ENJOY ITS SABBATHS", "26:34-35", K.pg_rest, "", "Then Shall the Land Enjoy Its Sabbaths"),
    ("A DRIVEN LEAF", "26:36-37", K.pg_leaf, "", None),
    ("THEY SHALL PINE AWAY", "26:38-39", K.pg_pine, "", None),
    ("THEY SHALL CONFESS", "26:40-41", K.pg_confess, "", None),
    ("I WILL REMEMBER MY COVENANT", "26:42-43", K.pg_remember, "", None),
    ("I WILL NOT REJECT THEM", "26:44-45", K.pg_not_reject, "", None),
    ("THE STATUTES AND ORDINANCES", "26:46", K.pg_sinai, "", None),
    ("WHEN A MAN SHALL ACCOMPLISH A VOW", "27:1-3", K.pg_20_60, SAY, "The Estimation of Persons"),
    ("A FEMALE", "27:4-5", K.pg_5_20, "", None),
    ("A MONTH OLD", "27:6", K.pg_child, "", None),
    ("SIXTY YEARS OLD AND UPWARD", "27:7", K.pg_60, "", None),
    ("IF HE BE POORER", "27:8", K.pg_poor, "", None),
    ("A BEAST", "27:9-10", K.pg_beast_vow, "", "Beasts, Houses and Fields"),
    ("AN UNCLEAN BEAST", "27:11-13", K.pg_unclean_beast, "", None),
    ("HIS HOUSE", "27:14-15", K.pg_house, "", None),
    ("A HOMER OF BARLEY", "27:16-17", K.pg_homer, "", None),
    ("AFTER THE JUBILEE", "27:18-19", K.pg_jubilee_field, "", None),
    ("A FIELD DEVOTED", "27:20-21", K.pg_devoted_field, "", None),
    ("A FIELD WHICH HE HATH BOUGHT", "27:22-24", K.pg_bought_field, "", None),
    ("TWENTY GERAHS", "27:25", K.pg_gerahs, "", None),
    ("THE FIRSTLING", "27:26-27", K.pg_firstling, "", "The Firstling, the Devoted, the Tithe"),
    ("NO DEVOTED THING", "27:28-29", K.pg_devoted, "", None),
    ("THE TITHE OF THE LAND", "27:30-31", K.pg_tithe, "", None),
    ("UNDER THE ROD", "27:32-33", K.pg_rod, "", None),
    ("IN MOUNT SINAI", "27:34", K.pg_commandments, "", None),
]
PAGES += law_pages(LAWS, "LEV-C09-L", START, "Blessing and Curse",
                   end=end_mark("END OF LEVITICUS · NEXT · NUMBERS", "right: 10px; top: 10px", ch="完"))
