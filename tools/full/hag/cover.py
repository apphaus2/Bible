import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from hag import G
from oba.minor import cover_page
from hag import art as K

def cover():
    """The new walls of the house on the mount, the outline of the former glory over them in gold (full-bleed)."""
    scene = f'<rect x="0" y="0" width="760" height="1080" fill="#3A3A6A"></rect><g transform="translate(0 340)">{K.former_glory(760, 740, 37)}</g>'
    return cover_page("Haggai", "Volume Thirty-Seven", 37, "Chapters 1 – 2", "ハガイ書", "HAGAI-SHO", G.v("2:9", to="greater than the former,"), scene,
                      bg="#3A3A6A", band="58,58,106")
