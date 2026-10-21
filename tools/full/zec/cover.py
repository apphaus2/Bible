import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from zec import G
from oba.minor import cover_page
from zec import art as K

def cover():
    """The candlestick all of gold between the two olive-trees, glowing on the night grid of the visions (full-bleed)."""
    scene = f'<g transform="translate(0 300)">{K.lampstand("cvl", 760, 780, 38, spouts=True)}</g><rect x="0" y="0" width="760" height="302" fill="#0B0B2A"></rect>'
    return cover_page("Zechariah", "Volume Thirty-Eight", 38, "Chapters 1 – 14", "ゼカリヤ書", "ZEKARIYA-SHO", G.v("4:6", frm="Not by might"), scene,
                      bg="#0B0B2A", band="11,11,42")
