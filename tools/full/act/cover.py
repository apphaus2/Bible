import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from act import G
from oba.minor import cover_page
from act import art as K

def cover():
    """Pentecost: the upper chamber, a tongue like as of fire resting over each head and the wind sweeping through (full-bleed)."""
    scene = (f'<g transform="translate(0 380)">{K.upper_chamber("cv", 760, 700, 4401, prayer=False, fire=True, wind=True)}</g>'
             f'<rect x="0" y="0" width="760" height="382" fill="#3A1E2A"></rect>')
    return cover_page("Acts", "Volume Forty-Four", 44, "Chapters 1 – 28", "使徒行伝", "SHITO GYŌDEN",
                      G.v("1:8", frm="ye shall be my witnesses"), scene, bg="#3A1E2A", band="58,30,42")
