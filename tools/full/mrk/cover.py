import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mrk import G
from oba.minor import cover_page
from mrk import art as K

def cover():
    """The sea of Galilee: Simon and Andrew casting their net from the boat, Jesus on the shore calling them (full-bleed)."""
    scene = (f'<g transform="translate(0 380)">{K.fishers("cv", 760, 700, 4101)}</g>'
             f'<rect x="0" y="0" width="760" height="382" fill="#0E2840"></rect>')
    return cover_page("Mark", "Volume Forty-One", 41, "Chapters 1 – 16", "マルコによる福音書", "MARUKO NI YORU FUKUINSHO",
                      G.v("1:17", frm="Come ye after me"), scene, bg="#0E2840", band="14,40,64")
