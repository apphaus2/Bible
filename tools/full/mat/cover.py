import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mat import G
from oba.minor import cover_page
from mat import art as K

def cover():
    """The star standing over Bethlehem at night, the wise-men's camels on the road below (full-bleed)."""
    scene = (f'<g transform="translate(0 380)">{K.star_road("cv", 760, 700, 4001)}</g>'
             f'<rect x="0" y="0" width="760" height="382" fill="#0B0B2A"></rect>')
    return cover_page("Matthew", "Volume Forty", 40, "Chapters 1 – 28", "マタイによる福音書", "MATAI NI YORU FUKUINSHO",
                      G.v("2:2", frm="we saw his star"), scene, bg="#0B0B2A", band="11,11,42")
