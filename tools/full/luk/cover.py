import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from luk import G
from oba.minor import cover_page
from luk import art as K

def cover():
    """The shepherds' field by night: the angel of the Lord in white light over them, the glory shining round about, the
    sheep, Bethlehem on its hill beyond (full-bleed)."""
    scene = (f'<g transform="translate(0 380)">{K.field_night("cv", 760, 700, 4201, angel_=True)}</g>'
             f'<rect x="0" y="0" width="760" height="382" fill="#0B0B2A"></rect>')
    return cover_page("Luke", "Volume Forty-Two", 42, "Chapters 1 – 24", "ルカによる福音書", "RUKA NI YORU FUKUINSHO",
                      G.v("2:10", frm="behold, I bring"), scene, bg="#0B0B2A", band="11,11,42")
