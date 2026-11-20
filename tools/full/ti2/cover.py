import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ti2 import G
from oba.minor import cover_page
from ti2 import art as A

def cover():
    """The letter from the cell at Rome: the stone wall by night, the barred window with the moon beyond, the lamp burning in
    its niche, the chain hanging from its ring, and on the bench the letter rolled and sealed (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#241E22"></rect>'
             f'<g transform="translate(0 300)">{A.cell_night(760, 780, 5501)}</g>')
    return cover_page("2 Timothy", "Volume Fifty-Five", 55, "Chapters 1 – 4", "テモテへの第二の手紙", "TEMOTE E NO DAINI NO TEGAMI",
                      G.v("4:7"), scene, bg="#241E22", band="36,30,34")
