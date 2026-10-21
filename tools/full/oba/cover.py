import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba import G
from oba.minor import cover_page
from oba import art as K

def cover():
    """The red rock of Edom by night, its dwellings cut in the cliff and an eagle's nest among the stars (full-bleed)."""
    scene = f'<g transform="translate(0 300)">{K.clefts(760, 780, 31)}</g><rect x="0" y="0" width="760" height="302" fill="#05051A"></rect>'
    return cover_page("Obadiah", "Volume Thirty-One", 31, "Chapter 1", "オバデヤ書", "OBADEYA-SHO", G.v("1:4", to="I will bring thee down from thence,"), scene,
                      bg="#05051A", band="5,5,26")
