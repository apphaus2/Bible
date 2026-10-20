"""The website's downloads: every volume as an EPUB and a reading PDF, by book.

Usage (from the repo root):  python3 tools/book/downloads.py [--lang en] [volume ...]

Writes _book/download/<lang>/ (git-ignored; rebuild_site.py copies it to the site as download/<lang>/):
  <vol>.epub                      fixed-layout EPUB (tools/book/export_book.py)
  <vol>.pdf  or  <vol>-1.pdf …    the reading PDF at page size; a book whose PDF would pass 24 MB is split at chapter
                                  boundaries, because Cloudflare serves no single file over 25 MiB
  index.json                      {vol: {"epub": {file, size}, "pdf": [{file, size, range, pages}]}} for build_site.py
  .sources.json                   a hash of each volume's pages and the exporter: unchanged volumes are not rebuilt
The language is a folder so that other editions (Spanish first) can sit beside English; today every volume is English."""
import sys, json, hashlib, pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent

def source_hash(vol):
    h = hashlib.sha1()
    for f in [HERE / "export_book.py", HERE / "render.js", *sorted((ROOT / "volumes" / vol).rglob("*"))]:
        if f.is_file(): h.update(f.name.encode()); h.update(f.read_bytes())
    return h.hexdigest()

def main():
    args = sys.argv[1:]
    lang = args[args.index("--lang") + 1] if "--lang" in args else "en"
    only = [a for a in args if not a.startswith("--") and a != lang]
    out = ROOT / "_book" / "download" / lang; out.mkdir(parents=True, exist_ok=True)
    state_f, index_f = out / ".sources.json", out / "index.json"
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    index = json.loads(index_f.read_text()) if index_f.exists() else {}
    vols = [p.name for p in sorted((ROOT / "volumes").glob("*")) if (p / "volume.json").exists()]
    for vol in vols:
        if only and vol not in only: continue
        h = source_hash(vol)
        files = [index.get(vol, {}).get("epub", {}).get("file")] + [x["file"] for x in index.get(vol, {}).get("pdf", [])]
        if state.get(vol) == h and all(f and (out / f).exists() for f in files):
            continue
        for f in out.glob(f"{vol}*"):                 # the old files, including parts that may no longer exist
            if f.name == f"{vol}.epub" or f.name.startswith(f"{vol}.") or f.name.startswith(f"{vol}-"): f.unlink()
        subprocess.run([sys.executable, str(HERE / "export_book.py"), vol, "--screen", "--out", str(out.relative_to(ROOT))], check=True)
        pdfs = json.loads((out / f"{vol}.pdfs.json").read_text()); (out / f"{vol}.pdfs.json").unlink()
        index[vol] = {"epub": {"file": f"{vol}.epub", "size": (out / f"{vol}.epub").stat().st_size}, "pdf": pdfs}
        state[vol] = h
        index_f.write_text(json.dumps(index, indent=1)); state_f.write_text(json.dumps(state, indent=1))
    for vol in list(index):                           # volumes that no longer exist
        if vol not in vols: index.pop(vol); state.pop(vol, None)
    index_f.write_text(json.dumps(index, indent=1)); state_f.write_text(json.dumps(state, indent=1))
    print(f"downloads ({lang}): {len(index)} volumes in {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
