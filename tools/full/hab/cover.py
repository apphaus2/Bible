import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from hab import G
from oba.minor import cover_page
from hab import art as K

def cover():
    """Habakkuk on his watchtower at dusk, looking out (full-bleed)."""
    scene = f'<rect x="0" y="0" width="760" height="1080" fill="#1E1650"></rect><g transform="translate(0 400)">{K.watchtower("cvw", 760, 680, 35)}</g>'
    return cover_page("Habakkuk", "Volume Thirty-Five", 35, "Chapters 1 – 3", "ハバクク書", "HABAKUKU-SHO", G.v("2:4", frm="but the righteous"), scene,
                      bg="#1E1650", band="30,22,80")
