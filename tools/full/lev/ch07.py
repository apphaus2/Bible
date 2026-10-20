"""Leviticus volume, Chapter 7 — Holy unto Jehovah (Leviticus 19–22). Every verse, word for word from ref/eng-asv.
All law cells (lev/art7.py). The penalties of chapter 20 are drawn as the kinship charts of chapter 18 under a red penalty
bar; no executions are shown."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from exo import art8 as B8
from exo.kit import law_pages, set_book
from lev import G, art7 as K
from lev import ch06 as _prev

v, sp = G.v, G.span
set_book(G)
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"


@P("LEV-C07-00-Title", "Chapter 7 · Holy unto Jehovah")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2458"></rect>' + f'<g transform="translate(0 500) scale(2.375)">{mk.defs("t7", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic") + K.pg_love("t7")}</g>'
    return chapter_title(7, "第七話", "Holy unto Jehovah", "Leviticus 19 – 22", svg, "#2A2458", v("19:18", frm="thou shalt love"), "Leviticus · Volume Three")


LAWS = [
    ("YE SHALL BE HOLY", "19:1-2", K.pg_holy, SAY, "Ye Shall Be Holy"),
    ("MOTHER AND FATHER · MY SABBATHS", "19:3", K.pg_parents, "", None),
    ("NO MOLTEN GODS", "19:4", K.pg_idols, "", None),
    ("THE PEACE-OFFERINGS", "19:5-8", K.pg_peace, "", None),
    ("THE CORNERS OF THY FIELD", "19:9", K.pg_corners, "", "For the Poor and the Sojourner"),
    ("THY VINEYARD", "19:10", K.pg_vineyard, "", None),
    ("YE SHALL NOT STEAL", "19:11-12", K.pg_steal, "", None),
    ("THE WAGES OF A HIRED SERVANT", "19:13", K.pg_wages, "", None),
    ("THE DEAF AND THE BLIND", "19:14", K.pg_blind, "", None),
    ("IN RIGHTEOUSNESS", "19:15", K.pg_judgment, "", None),
    ("A TALEBEARER", "19:16", K.pg_tale, "", None),
    ("THOU SHALT LOVE THY NEIGHBOR", "19:17-18", K.pg_love, "", "Thou Shalt Love Thy Neighbor"),
    ("DIVERSE KINDS", "19:19", K.pg_diverse, "", None),
    ("A BONDMAID", "19:20-22", K.pg_bondmaid, "", None),
    ("THE FRUIT OF THE TREES", "19:23-25", K.pg_trees, "", None),
    ("NO ENCHANTMENTS", "19:26", K.pg_augury, "", None),
    ("THE CORNERS OF THY BEARD", "19:27-28", K.pg_cuttings, "", None),
    ("PROFANE NOT THY DAUGHTER", "19:29-30", K.pg_daughter, "", None),
    ("FAMILIAR SPIRITS", "19:31", K.pg_wizards, "", None),
    ("THE HOARY HEAD", "19:32", K.pg_hoary, "", "The Stranger and the Hoary Head"),
    ("THE STRANGER", "19:33-34", K.pg_stranger, "", None),
    ("JUST BALANCES", "19:35-37", K.pg_weights, "", None),
    ("MOLECH", "20:1-2", K.pg_molech, SAY, "I Will Set My Face against That Man"),
    ("I WILL SET MY FACE", "20:3-5", K.pg_face, "", None),
    ("FAMILIAR SPIRITS AND WIZARDS", "20:6", K.pg_spirits, "", None),
    ("SANCTIFY YOURSELVES", "20:7-8", K.pg_sanctify, "", None),
    ("HE THAT CURSETH", "20:9", K.pg_curse, "", "Their Blood Shall Be upon Them"),
    ("ANOTHER MAN'S WIFE", "20:10", K.pg_adultery, "", None),
    ("HIS FATHER'S WIFE", "20:11", K.pg_fwife, "", None),
    ("HIS DAUGHTER-IN-LAW", "20:12", K.pg_dil, "", None),
    ("ABOMINATION", "20:13", K.pg_mankind, "", None),
    ("A WIFE AND HER MOTHER", "20:14", K.pg_wife_mother, "", None),
    ("A BEAST", "20:15-16", K.pg_beast, "", None),
    ("HIS SISTER", "20:17", K.pg_sister, "", None),
    ("HER SICKNESS", "20:18", K.pg_sickness, "", None),
    ("THY MOTHER'S SISTER", "20:19", K.pg_aunt, "", None),
    ("HIS UNCLE'S WIFE", "20:20", K.pg_uncle_wife, "", None),
    ("HIS BROTHER'S WIFE", "20:21", K.pg_bwife, "", None),
    ("THAT THE LAND VOMIT YOU NOT OUT", "20:22-24", K.pg_land, "", "Ye Shall Inherit Their Land"),
    ("A DISTINCTION", "20:25", K.pg_distinction, "", None),
    ("I HAVE SET YOU APART", "20:26", K.pg_set_apart, "", None),
    ("A FAMILIAR SPIRIT", "20:27", K.pg_familiar, "", None),
    ("NONE SHALL DEFILE HIMSELF FOR THE DEAD", "21:1", K.pg_dead, "", "Speak unto the Priests"),
    ("EXCEPT FOR HIS KIN", "21:2-4", K.pg_kin, "", None),
    ("NO BALDNESS", "21:5-6", K.pg_baldness, "", None),
    ("THE BREAD OF THY GOD", "21:7-8", K.pg_wife, "", None),
    ("THE DAUGHTER OF ANY PRIEST", "21:9", K.pg_pdaughter, "", None),
    ("THE HIGH PRIEST", "21:10", K.pg_high, "", "The High Priest among His Brethren"),
    ("NOT FOR HIS FATHER", "21:11-12", K.pg_hp_dead, "", None),
    ("A VIRGIN OF HIS OWN PEOPLE", "21:13-15", K.pg_hp_wife, "", None),
    ("THAT HATH A BLEMISH", "21:16-17", K.pg_blemish, SAY, "Whosoever Hath a Blemish"),
    ("HE SHALL NOT APPROACH", "21:18-20", K.pg_blemish, "", None),
    ("HE SHALL NOT COME NIGH", "21:21", K.pg_veil, "", None),
    ("THE MOST HOLY AND THE HOLY", "21:22-23", K.pg_eat_holy, "", None),
    ("SO MOSES SPAKE", "21:24", K.pg_spake, "", None),
    ("SEPARATE THEMSELVES", "22:1-3", K.pg_separate, SAY, "The Holy Things"),
    ("A LEPER, OR AN ISSUE", "22:4-6", K.pg_leper_priest, "", None),
    ("WHEN THE SUN IS DOWN", "22:7-9", K.pg_sun_down, "", None),
    ("NO STRANGER", "22:10", K.pg_stranger_eat, "", None),
    ("BOUGHT WITH HIS MONEY", "22:11", K.pg_bought, "", None),
    ("A PRIEST'S DAUGHTER", "22:12-13", K.pg_pdaughter2, "", None),
    ("UNWITTINGLY", "22:14-16", K.pg_unwitting, "", None),
    ("A MALE WITHOUT BLEMISH", "22:17-19", K.pg_male, SAY, "That Ye May Be Accepted"),
    ("WHATSOEVER HATH A BLEMISH", "22:20-21", K.pg_no_blemish, "", None),
    ("BLIND, OR BROKEN", "22:22", K.pg_no_blemish, "", None),
    ("SUPERFLUOUS OR LACKING", "22:23-24", K.pg_freewill, "", None),
    ("FROM THE HAND OF A FOREIGNER", "22:25", K.pg_foreigner, "", None),
    ("SEVEN DAYS UNDER THE DAM", "22:26-28", K.pg_seven_dam, SAY, None),
    ("A SACRIFICE OF THANKSGIVING", "22:29-30", K.pg_thanks, "", None),
    ("I WILL BE HALLOWED", "22:31-33", K.pg_hallowed, "", None),
]
PAGES += law_pages(LAWS, "LEV-C07-L", START, "Holy unto Jehovah", end=end_mark("NEXT · THE SET FEASTS", "right: 10px; top: 10px"))
