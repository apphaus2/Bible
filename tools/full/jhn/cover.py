import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jhn import G
from oba.minor import cover_page
from jhn import art as K

def scene(p, w, h, seed):
    """Dawn by the sea of Tiberias (21:4): the light breaking over the hills and the water, the boat far out with its net,
    and Jesus standing on the beach beside a fire of coals."""
    b = h * 0.9
    o = [K.mk.defs(p, *K.ALL), K.sky(w, h, "#1A1A4A", "#FFB07A"), K.rays(w * 0.66, h * 0.4, 40, 30, w * 1.2, color="#FFF4C2", op=0.2),
         K.glow(w * 0.66, h * 0.4, w * 0.5, "#FFE680", 0.7, f"{p}g"), f'<circle cx="{K.f(w * 0.66)}" cy="{K.f(h * 0.4)}" r="{K.f(w * 0.05)}" fill="#FFF4C2"></circle>',
         K.hills(w, h, h * 0.4, seed, color="#4A3A5A", amp=12, step=90), K.lake(w, h, h * 0.44, seed, color="#4A6A9A", deep="#1A2A5A", foam="#FFD8A0"),
         f'<path d="M{K.f(w * 0.56)} {K.f(h * 0.45)} L {K.f(w * 0.76)} {K.f(h * 0.45)} L {K.f(w * 0.72)} {K.f(h * 0.72)} L {K.f(w * 0.6)} {K.f(h * 0.72)} Z" fill="#FFE680" opacity="0.3"></path>',
         K.boat(p, w * 0.8, h * 0.56, 0.62, crew=[(-30, K.ROBES["peter"]), (20, K.ROBES["john"])], mast=True, net=True, flip=True),
         K.shore(w, h, h * 0.74, color="#8A7060")]
    s = K.fit(b, b - 250)
    o.append(K.coals(w * 0.6, b - 10, s * 0.8, seed, fish=True, bread=True))
    o.append(K.jesus(p, w * 0.34, b, s))
    return "".join(o)

def cover():
    svg = f'<g transform="translate(0 300)">{scene("cv", 760, 780, 4301)}</g><rect x="0" y="0" width="760" height="302" fill="#1A1A4A"></rect>'
    return cover_page("John", "Volume Forty-Three", 43, "Chapters 1 – 21", "ヨハネによる福音書", "YOHANE NI YORU FUKUINSHO",
                      G.v("1:1"), svg, bg="#1A1A4A", band="26,26,74")
