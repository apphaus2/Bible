import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mic import G
from oba.minor import cover_page
from mic import art as K

def cover():
    """The anvil: a sword beaten into a plowshare, sparks flying (full-bleed)."""
    scene = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A14"></rect><g transform="translate(0 300)">{K.plowshares(760, 780, 33)}</g>'
    return cover_page("Micah", "Volume Thirty-Three", 33, "Chapters 1 – 7", "ミカ書", "MIKA-SHO", G.v("4:3", frm="and they shall beat", to="pruning-hooks;"), scene,
                      bg="#2A1A14", band="42,26,20")
