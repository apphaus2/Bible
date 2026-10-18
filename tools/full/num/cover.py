import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus3 as E3, exodus5 as V, numbers1 as N
from num import G, art as K
from genesis.art2 import ground, hills

def cover():
    """The camp by night: the pillar of fire over the tabernacle, the tents of the twelve tribes and their standards."""
    w, h = 760, 1080
    svg = (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; display: block">'
           f'<rect x="0" y="0" width="{w}" height="{h}" fill="#0B0B2A"></rect>' + mk.stars(160, w, 640, 41)
           + V.rays(380, 620, 36, 60, 900, color="#FFC14D", op=0.10)
           + hills(w, h, 700, 43, color="#1A1430", amp=18) + ground(w, h, 760, "#2A1E2A", dy=0)
           + N.camp(16, 0, 300, 770, 900, 44, color=("#3A2A3A", "#4A3226", "#2A1E22")) + N.camp(16, 460, 760, 770, 900, 45, color=("#3A2A3A", "#4A3226", "#2A1E22"))
           + V.tabernacle(380, 860, 300, uid="cvtb") + E3.pillar_fire(400, 790, 420, 40, 46)
           + "".join(K.standard(x, 1000, 1.6, K.TRIBE_C[n], pole=110) for x, n in ((70, "JUDAH"), (230, "REUBEN"), (540, "EPHRAIM"), (680, "DAN")))
           + '</svg>')
    svg += '<div style="position: absolute; left: 0; right: 0; top: 0; height: 420px; background: linear-gradient(180deg, rgba(11,11,42,0.95) 0%, rgba(11,11,42,0.7) 60%, rgba(11,11,42,0) 100%)"></div>'
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Fourth Book of Moses</span>
  </div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 128px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">NUMBERS</h1>
  <div style="position: absolute; top: 250px; left: 38px; width: 300px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 266px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Four</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 36</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; margin-top: 30px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>民</span><span>数</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">MINSŪKI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 340px; padding: 8px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 14px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 330px; line-height: 1.45">{G.v("6:24")} {G.v("6:25")} {G.v("6:26")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 4</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #0B0B2A; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Numbers — Volume Four", None, body, root_style=root)
