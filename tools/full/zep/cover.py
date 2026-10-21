import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from zep import G
from oba.minor import cover_page
from zep import art as K

def cover():
    """The day of darkness: black clouds rolling over the battlements, the ram's horn raised (full-bleed)."""
    scene = f'<rect x="0" y="0" width="760" height="1080" fill="#05050A"></rect><g transform="translate(0 300)">{K.day_dark(760, 780, 36)}</g>'
    return cover_page("Zephaniah", "Volume Thirty-Six", 36, "Chapters 1 – 3", "ゼパニヤ書", "ZEPANIYA-SHO", G.v("1:14", to="it is near and hasteth greatly,"), scene,
                      bg="#05050A", band="5,5,10")
