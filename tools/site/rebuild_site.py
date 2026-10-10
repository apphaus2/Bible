"""Build the whole website from both editions, in one step.

Usage (from the repo root):  python3 tools/site/rebuild_site.py [--thumbs] [--out _site]

- Full edition: every volumes/<id>/ that has a volume.json (pages/ + canvas.json) is passed straight through.
- Digest edition: each digest/<series>/ is flattened (its book-*/ pages + the series canvas.json) into a temp folder.
The output folder (default _site/, which is git-ignored) is cleared except for thumbs/ (a cache), then
tools/site/build_site.py writes the pages and tools/site/assets/* is copied in. With --thumbs, any thumbnail
that is missing or whose source page changed (tracked by a hash in thumbs/.sources.json) is rendered with
Playwright (needs node + the `playwright` package + Pillow); thumbnails no page uses any more are deleted.
GitHub Actions (.github/workflows/pages.yml) runs exactly this and deploys _site/ to GitHub Pages."""
import hashlib, json, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = ROOT / "tools" / "site"

def main():
    out = ROOT / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "_site")
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
    out.mkdir(exist_ok=True)
    for d in out.iterdir():
        if d.name == "thumbs": continue
        shutil.rmtree(d) if d.is_dir() else d.unlink()
    subprocess.run([sys.executable, str(SITE / "build_site.py"), str(out), *args], check=True)
    (out / "assets").mkdir(exist_ok=True)
    for f in (SITE / "assets").iterdir():
        shutil.copy(f, out / "assets" / f.name)
    manifest = json.loads((out / "manifest.json").read_text())
    pages = [pg for s in manifest["series"] for b in s["books"] for pg in b["pages"]]
    wanted = {pg["thumb"] for pg in pages}
    if "--thumbs" in sys.argv:
        from PIL import Image
        state_f = out / "thumbs" / ".sources.json"
        state = json.loads(state_f.read_text()) if state_f.exists() else {}
        todo = {}                                   # key -> [(source path, thumb path, hash)]
        for pg in pages:
            key, name = pg["src"].split("/", 1)
            src = keys[key] / name
            h = hashlib.sha1(src.read_bytes()).hexdigest()
            dst = out / pg["thumb"]
            if dst.exists() and state.get(pg["thumb"]) == h: continue
            todo.setdefault(key, []).append((src, dst, h, pg["thumb"]))
        for key, items in todo.items():             # one browser per source folder (file names repeat across folders)
            pngs = tmp / "png" / key
            subprocess.run(["node", str(SITE / "shots.js"), str(pngs), *[str(s) for s, _, _, _ in items]], check=True)
            for src, dst, h, t in items:
                Image.open(pngs / src.name.replace(".dc.html", ".png")).convert("RGB").resize((380, 540), Image.LANCZOS).save(dst, quality=85)
                state[t] = h
            print(f"rendered {len(items)} thumbnails from {key}")
        state_f.write_text(json.dumps({k: v for k, v in sorted(state.items()) if k in wanted}, indent=0))
    for t in (out / "thumbs").glob("*.jpg"):
        if f"thumbs/{t.name}" not in wanted:
            t.unlink(); print("removed unused", t.name)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"site written to {out.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
