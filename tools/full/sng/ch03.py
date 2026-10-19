"""Song of Solomon volume, Chapter 3 — Love Is Strong as Death (Song of Solomon 6–8), the last chapter of the Song. Every
verse, word for word from ref/asv. Whither is thy beloved gone (the daughters' face); the beds of spices and the lilies;
fair as Tirzah, comely as Jerusalem, terrible as an army with banners; the likenesses again as cells; the queens and the
virgins without number and one dove; looking forth as the morning; the garden of nuts and the chariots; the two camps of
Mahanaim; then the likenesses of 7:1–9 as plates of cells only — sandals, jewels, a goblet, a heap of wheat set about with
lilies, fawns, the tower of ivory, the pools of Heshbon, the tower of Lebanon, Carmel, purple, the palm, the clusters, apples
and wine; the vineyards at dawn and the mandrakes; the mother's house; coming up from the wilderness under the apple-tree;
set me as a seal (the floods and a flame they cannot quench; God never drawn); the wall and the door; Solomon's vineyard at
Baal-hamon; and the hart upon the mountains of spices."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from sng import G, art as K
from sng.common import (paged, face, drawn, sg, sgs, BRIDE, BRIDE_GLAD, BRIDE_NIGHT, BELOVED, DAUGHTER, DAUGHTER2, COLD, GOLDEN, DUSK, ROSE, LEAF)
from sng import ch02 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
PLATE = "#1A1430"


def cells(*keys, cols=None, gap=False):
    """A plate of likeness cells; gap=True leaves an empty last cell (room for the chapter stamp)."""
    items = [(K.CELL[k], "") for k in keys] + ([("", "")] if gap else [])
    return lambda w, h: K.plate(w, h, items, cols=cols or len(items))


@P("SNG-C03-00-Title", "Chapter 3 · Love Is Strong as Death", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(0 280)">{K.seal_flame(760, 800, 301)}</g>')
    return chapter_title(3, "第三話", "Love Is Strong as Death", "Song of Solomon 6 – 8", svg, "#0B1A2E", v("8:7", to="drown it:"), "Song of Solomon · Volume Twenty-Two")


PAGE = [[face("6:1", DAUGHTER2, bg=ROSE, head="Whither Is Thy Beloved Gone", stamp=6),
         drawn("6:2-3", lambda w, h: K.spice_garden("sp3", w, h, 302), "#8FD0E2")],
        [drawn("6:4", lambda w, h: K.tirzah("tz3", w, h, 303), "#8FD0E2"),
         drawn("6:5-7", cells("gilead", "ewes", "scarlet"), PLATE)],
        [drawn("6:8-9", lambda w, h: K.queens("qn3", w, h, 304), "#E8D8B8"),
         drawn("6:10", lambda w, h: K.morning(w, h, 305), "#3A4A8A")],
        [drawn("6:11-12", lambda w, h: K.nut_garden(w, h, 306), "#8FD0E2"),
         drawn("6:13", lambda w, h: K.mahanaim("mh3", w, h, 307), "#3A2A5A")],
        [drawn("7:1-3", cells("sandals", "jewels", "goblet", "wheat", "fawns", gap=True), PLATE, head="How Beautiful Are Thy Feet", stamp=7),
         drawn("7:4-5", cells("ivory_tower", "pools", "leb_tower", "carmel", "purple"), PLATE)],
        [drawn("7:6-9", cells("palm", "clusters", "apples", "wine", cols=4), PLATE),
         drawn("7:10-13", lambda w, h: K.vineyard_dawn("vd3", w, h, 308), "#FFC890")],
        [face("8:1-4", BRIDE, bg=ROSE, stamp=8),
         drawn("8:5", lambda w, h: K.coming_up("cu3", w, h, 309), "#5A3A6A")],
        [drawn("8:6-7", lambda w, h: K.seal_flame(w, h, 310), "#0B1A2E", head="Set Me as a Seal"),
         drawn("8:8-10", lambda w, h: K.wall_door(w, h), "#0B1A2E")],
        [drawn("8:11-12", lambda w, h: K.baal_hamon("bh3", w, h, 311), "#8FD0E2"),
         drawn("8:13-14", lambda w, h: K.mountains_spices(w, h, 312), "#5A4A8A")]]
PG.extend(paged(PAGE, "SNG-C03-", PG.next(), end=end_mark("END OF THE SONG OF SOLOMON · NEXT · ISAIAH", "right: 10px; bottom: 34px", ch="完")))
