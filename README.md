# Bible Manga

The Bible as a full-color manga in a 1980s cyberpunk-manga style, in the words of the
American Standard Version (1901). GitHub Actions builds the website and deploys it to
GitHub Pages on every push to `main`.

- **Full edition** (`volumes/`): one volume per book of the Bible, every scene and every line of
  dialogue word for word. In progress, starting with Genesis.
- **Digest edition** (`digest/`): the first drafts, short books of highlights from Genesis to 2 Samuel.
  Legacy; being replaced by the full edition.

## Build

```
python3 tools/full/build_volume.py genesis     # write volumes/genesis/ and check every line against ref/asv
python3 tools/site/rebuild_site.py --thumbs    # local preview in _site/ (needs node + Playwright + Pillow)
```

Text source: `ref/asv/` (USFM from eBible.org, public domain). See `CLAUDE.md` for the full working notes.
