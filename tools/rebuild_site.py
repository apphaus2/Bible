"""Rebuild the whole website in docs/ from the pages in manga/, in one step.

Usage (from the repo root):  python3 tools/rebuild_site.py [--thumbs]

It gathers each series' pages (manga/<series>/book-NN/*.dc.html) and its canvas.json
into one flat temp folder, runs tools/build_site.py, copies tools/site/* into docs/assets/,
and with --thumbs renders any missing thumbnail (needs node + Playwright + Pillow)."""
import json, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS, DOCS = ROOT / "tools", ROOT / "docs"

def main():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="manga-"))
    args = []
    for series in sorted(p for p in (ROOT / "manga").iterdir() if p.is_dir()):
        flat = tmp / series.name; flat.mkdir()
        shutil.copy(series / "canvas.json", flat / "canvas.json")
        for page in series.glob("book-*/*.dc.html"):
            shutil.copy(page, flat / page.name)
        args.append(f"{series.name}={flat}")
    subprocess.run([sys.executable, str(TOOLS / "build_site.py"), str(DOCS), *args], check=True)
    (DOCS / "assets").mkdir(exist_ok=True)
    for f in (TOOLS / "site").iterdir():
        shutil.copy(f, DOCS / "assets" / f.name)
    if "--thumbs" in sys.argv:
        from PIL import Image
        manifest = json.loads((DOCS / "manifest.json").read_text())
        pngs = tmp / "png"; pngs.mkdir()
        for s in manifest["series"]:
            canvas = json.loads((tmp / s["id"] / "canvas.json").read_text())
            for b in s["books"]:
                for pg in b["pages"]:
                    out = DOCS / pg["thumb"]
                    if out.exists():
                        continue
                    # find the page file whose slug matches this page's position in the book
                    src = page_file(tmp / s["id"], canvas, b, pg)
                    subprocess.run(["node", str(TOOLS / "shots.js"), str(pngs), str(src)], check=True)
                    Image.open(pngs / (src.name.replace(".dc.html", ".png"))).convert("RGB").resize((380, 540), Image.LANCZOS).save(out, quality=85)
                    print("thumb", out.relative_to(ROOT))
    shutil.rmtree(tmp, ignore_errors=True)

def page_file(flat, canvas, book, page):
    idx = book["pages"].index(page)
    prefix = book["id"]
    names = [n for n in canvas["order"] if (flat / n).exists()]
    # build_site.py matches pages to books with each book's `match`; reuse its SERIES config
    src = (TOOLS / "build_site.py").read_text()
    cfg = src[src.index("SERIES = ["):src.index("SERIES = [x for x")]
    ns = {}; exec(cfg, ns)
    series = next(x for x in ns["SERIES"] if x["id"] == flat.name)
    bk = next(x for x in series["books"] if x["dir"] == prefix)
    return flat / [n for n in names if bk["match"](n)][idx]

if __name__ == "__main__":
    main()
