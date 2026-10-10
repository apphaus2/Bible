"""Rebuild the whole website in docs/ from both editions, in one step.

Usage (from the repo root):  python3 tools/site/rebuild_site.py [--thumbs]

- Full edition: every volumes/<id>/ that has a volume.json (pages/ + canvas.json) is passed straight through.
- Digest edition: each digest/<series>/ is flattened (its book-*/ pages + the series canvas.json) into a temp folder.
It clears the generated folders in docs/ (keeping docs/thumbs/ as a cache), runs tools/site/build_site.py,
copies tools/site/assets/* into docs/assets/, renders any missing thumbnail with --thumbs
(needs node + Playwright + Pillow), and deletes thumbnails no page uses any more."""
import json, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE, DOCS = ROOT / "tools" / "site", ROOT / "docs"

def main():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="manga-"))
    args, keys = [], {}
    for vol in sorted(p for p in (ROOT / "volumes").glob("*") if (p / "volume.json").exists()):
        args.append(f"{vol.name}={vol}"); keys[vol.name] = vol / "pages"
    for series in sorted(p for p in (ROOT / "digest").iterdir() if p.is_dir()):
        flat = tmp / series.name; flat.mkdir()
        shutil.copy(series / "canvas.json", flat / "canvas.json")
        for page in series.glob("book-*/*.dc.html"):
            shutil.copy(page, flat / page.name)
        args.append(f"digest-{series.name}={flat}"); keys[f"digest-{series.name}"] = flat
    for d in DOCS.iterdir() if DOCS.exists() else []:
        if d.is_dir() and d.name not in ("thumbs", "assets"):
            shutil.rmtree(d)
    subprocess.run([sys.executable, str(SITE / "build_site.py"), str(DOCS), *args], check=True)
    (DOCS / "assets").mkdir(exist_ok=True)
    for f in (SITE / "assets").iterdir():
        shutil.copy(f, DOCS / "assets" / f.name)
    manifest = json.loads((DOCS / "manifest.json").read_text())
    wanted = {pg["thumb"] for s in manifest["series"] for b in s["books"] for pg in b["pages"]}
    if "--thumbs" in sys.argv:
        from PIL import Image
        pngs = tmp / "png"; pngs.mkdir()
        for s in manifest["series"]:
            for b in s["books"]:
                for pg in b["pages"]:
                    out = DOCS / pg["thumb"]
                    if out.exists():
                        continue
                    key, name = pg["src"].split("/", 1)
                    src = keys[key] / name
                    subprocess.run(["node", str(SITE / "shots.js"), str(pngs), str(src)], check=True)
                    Image.open(pngs / name.replace(".dc.html", ".png")).convert("RGB").resize((380, 540), Image.LANCZOS).save(out, quality=85)
                    print("thumb", out.relative_to(ROOT))
    for t in (DOCS / "thumbs").glob("*.jpg"):
        if f"thumbs/{t.name}" not in wanted:
            t.unlink(); print("removed unused", t.name)
    shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
