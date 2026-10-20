"""Build the whole website, in one step.

Usage (from the repo root):  python3 tools/site/rebuild_site.py [--thumbs] [--out _site]

- Every volumes/<id>/ that has a volume.json (pages/ + canvas.json) is passed straight through. (digest/, the old first
  drafts, is not published: it stays in the repo only as a source of drawings that volume pages lift.)
- The ASV text: the per-book PDFs in _book/asv/ (tools/book/asv_pdf.py), if built, are copied to the site and linked from the
  home page, every chapter page and every page's "ASV" credit (the whole-Bible PDF is not published: it is large).
- The downloads: _book/download/<lang>/ (tools/book/downloads.py: each volume as an EPUB and a reading PDF), if built.
The output folder (default _site/, which is git-ignored) is cleared except for thumbs/ (a cache), then
tools/site/build_site.py writes the pages and tools/site/assets/* is copied in. With --thumbs, any thumbnail
that is missing or whose source page changed (tracked by a hash in thumbs/.sources.json) is rendered with
Playwright (needs node + the `playwright` package + Pillow); thumbnails no page uses any more are deleted.
GitHub Actions (.github/workflows/pages.yml) runs exactly this and deploys _site/ to Cloudflare (bible.apphaus.us) and GitHub Pages."""
import hashlib, json, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = ROOT / "tools" / "site"

def main():
    out = ROOT / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "_site")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="manga-"))
    args, keys = [], {}
    for vol in sorted(p for p in (ROOT / "volumes").glob("*") if (p / "volume.json").exists()):
        args.append(f"{vol.name}={vol}"); keys[vol.name] = vol / "pages"
    out.mkdir(exist_ok=True)
    for d in out.iterdir():
        if d.name == "thumbs": continue
        shutil.rmtree(d) if d.is_dir() else d.unlink()
    if (ROOT / "_book" / "asv" / "index.json").exists():       # the ASV text, one PDF per book (tools/book/asv_pdf.py)
        shutil.copytree(ROOT / "_book" / "asv", out / "asv")
    else: print("no _book/asv/: the site is built without the ASV text links (run tools/book/asv_pdf.py)")
    for idx in sorted((ROOT / "_book" / "download").glob("*/index.json")):   # the manga by book (tools/book/downloads.py)
        dst = out / "download" / idx.parent.name; dst.mkdir(parents=True, exist_ok=True)
        shutil.copy(idx, dst / "index.json")
        for v in json.loads(idx.read_text()).values():
            for f in [v["epub"]["file"], *(x["file"] for x in v["pdf"])]: shutil.copy(idx.parent / f, dst / f)
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
            for i in range(0, len(items), 150):     # batches: Windows caps a command line at 32,767 characters
                batch = items[i:i + 150]
                subprocess.run(["node", str(SITE / "shots.js"), str(pngs), *[str(s) for s, _, _, _ in batch]], check=True)
                for src, dst, h, t in batch:
                    Image.open(pngs / src.name.replace(".dc.html", ".png")).convert("RGB").resize((380, 540), Image.LANCZOS).save(dst, quality=85)
                    state[t] = h
                state_f.write_text(json.dumps({k: v for k, v in sorted(state.items()) if k in wanted}, indent=0))
            print(f"rendered {len(items)} thumbnails from {key}")
        state_f.write_text(json.dumps({k: v for k, v in sorted(state.items()) if k in wanted}, indent=0))
    for t in (out / "thumbs").glob("*.jpg"):
        if f"thumbs/{t.name}" not in wanted:
            t.unlink(); print("removed unused", t.name)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"site written to {out.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
