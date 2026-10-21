import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mal import G
from oba.minor import cover_page
from mal import art as K

def cover():
    """The sun of righteousness rising over the hills, its rays spread as wings, calves leaping in the field (full-bleed)."""
    scene = f'<rect x="0" y="0" width="760" height="1080" fill="#3A4A8A"></rect><g transform="translate(0 300)">{K.sun_wings(760, 780, 39)}</g>'
    return cover_page("Malachi", "Volume Thirty-Nine", 39, "Chapters 1 – 4", "マラキ書", "MARAKI-SHO", G.v("4:2", frm="shall the sun of righteousness", to="in its wings;"), scene,
                      bg="#3A4A8A", band="42,42,90")
