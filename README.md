# Bible Manga

The Bible as a full-color manga in a 1980s cyberpunk-manga style, in the words of the
American Standard Version (1901). The website is published from `docs/` with GitHub Pages.

- **Full edition** (`volumes/`): one volume per book of the Bible, every scene and every line of
  dialogue word for word. In progress, starting with Genesis.
- **Digest edition** (`digest/`): the first drafts, short books of highlights from Genesis to 2 Samuel.
  Legacy; being replaced by the full edition.

## Build

```
python3 tools/full/build_volume.py genesis     # write volumes/genesis/ and check every line against ref/asv
python3 tools/site/rebuild_site.py --thumbs    # rebuild docs/ (needs node + Playwright + Pillow for thumbnails)
```

Text source: `ref/asv/` (USFM from eBible.org, public domain). See `CLAUDE.md` for the full working notes.
