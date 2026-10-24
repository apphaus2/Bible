"""Contact sheets of a volume, for reviewing every page at a glance.

Usage (from the repo root):  python tools/site/sheets.py <volume id> <out_dir> [--from N] [--to M]

Renders the volume's pages in reading order (canvas.json) with tools/site/shots.js (Node + Playwright: NODE_PATH) into
<out_dir>/png/, then writes <out_dir>/sheet-01.png … : 20 pages a sheet (5 × 4), each tile labelled with its place in the
volume and its file name, so a page can be found again and opened full size from png/. --from/--to limit the pages
(by place, the cover is 0), e.g. to look again at a chapter after a fix. Needs Pillow."""
import sys, json, pathlib, subprocess, argparse
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[2]
TW, TH, COLS, ROWS = 240, 341, 5, 4

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("volume"); ap.add_argument("out"); ap.add_argument("--from", dest="frm", type=int, default=0); ap.add_argument("--to", type=int)
    a = ap.parse_args()
    vol, out = ROOT / "volumes" / a.volume, pathlib.Path(a.out)
    order = json.loads((vol / "canvas.json").read_text(encoding="utf-8"))["order"]
    places = list(range(len(order)))[a.frm:(a.to + 1 if a.to is not None else None)]
    pages = [str(vol / "pages" / order[i]) for i in places]
    for i in range(0, len(pages), 110):                    # batches: Windows caps a command line at 32,767 characters
        subprocess.run(["node", str(ROOT / "tools" / "site" / "shots.js"), str(out / "png"), *pages[i:i + 110]], check=True)
    for k in range(0, len(places), COLS * ROWS):
        sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 18)), "white"); d = ImageDraw.Draw(sheet)
        for j, place in enumerate(places[k:k + COLS * ROWS]):
            im = Image.open(out / "png" / order[place].replace(".dc.html", ".png")).convert("RGB").resize((TW - 6, TH - 6), Image.LANCZOS)
            x, y = (j % COLS) * TW, (j // COLS) * (TH + 18)
            sheet.paste(im, (x + 3, y + 18)); d.text((x + 4, y + 3), f"{place}  {order[place][:34]}", fill="black")
        sheet.save(out / f"sheet-{k // (COLS * ROWS) + 1:02d}.png")
    print(f"{len(places)} pages, {(len(places) + COLS * ROWS - 1) // (COLS * ROWS)} sheets in {out}")

if __name__ == "__main__":
    main()
