import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jon import G
from oba.minor import cover_page
from jon import art as K

def cover():
    """The ship in the tempest above, the great fish in the deep below (full-bleed)."""
    scene = (f'{K.tempest("cvt", 760, 600, 32, crew=0)}'
             f'<g transform="translate(0 560)">{K.deep(760, 520, 33, inside=True)}</g>')
    return cover_page("Jonah", "Volume Thirty-Two", 32, "Chapters 1 – 4", "ヨナ書", "YONA-SHO", G.v("2:9", frm="Salvation is of Jehovah."), scene,
                      bg="#0B1A2E", band="11,11,26")
