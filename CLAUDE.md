# CLAUDE.md — Bible Manga

Context for Claude (and humans) working in this repo.

## What this is

A manga adaptation of the Bible, book by book, drawn as vector pages in a dense
black-and-white 1980s cyberpunk-manga style. Genesis is first.

- **Book One — Genesis 1–3** (Creation → Eden → the Fall): done, `manga/genesis/book-01/`
- Live canvas (private Claude Design artifact): https://claude.ai/artifact/UGXs4gFgPqfSp92tykHmT3

## Repo layout

```
manga/
  genesis/
    book-01/          Genesis 1–3
      canvas.json     canvas index: artboard positions, order, titles
      Main.dc.html    00 · Cover
      P01-…P07-….dc.html   one file per manga page
```

New books go in `manga/<book>/book-NN/` and keep the same file conventions.

## File format

Each page is a self-contained **Design Component** (`.dc.html`) for the Claude
Design canvas:

- Keep `<script src="./support.js"></script>` in `<head>` exactly as written.
- All markup sits inside `<x-dc>…</x-dc>`. Fonts come from one Google Fonts
  `<link>` in `<helmet>`.
- End each file with a `<script type="text/x-dc" data-dc-script data-props='…'>`
  block containing `class Component extends DCLogic { renderVals() {…} }`.
  `$preview` is `{"width":760,"height":1080}`.
- `{{hole}}` only does a dotted lookup, never an expression.
- Close every element and quote every attribute. Use inline `style=""`, since
  that's what the editor edits.
- Art is inline SVG plus CSS gradients. Don't use images, emoji, scripts that
  build the DOM, or iframes.
- Give SVG `id`s a page prefix (`dk`, `fm`, `ld`, `lf`, `ed`, `sv`, `ex`, …) so
  `<defs>`/`<use>` never collide.

`canvas.json`: pages are 760×1080, in rows of 4. Frames are 80 px apart in a row
and 120 px apart between rows (y = 0, 1200, 2400…). Every page needs a `boards`
entry and an `order` slot. Keep `createdOnFiles` unchanged.

## Visual style guide

**Influences:** 1980s Japanese cyberpunk manga in general. That means precise
linework, technical annotation labels, flying debris, radial speed lines,
screentone, and big cinematic splash panels.
**Never** use Akira's characters, logo or title treatment, the red motorcycle,
pill or capsule imagery, Neo-Tokyo, or the white-dome explosion. Use the
general style only, not a recreation of that work.

| Token | Value | Use |
|---|---|---|
| Paper | `#F3EFE6` | page ground, captions |
| Ink | `#0D0D0F` | lines, black panels |
| Red | `#D7261E` | sparingly: day stamps, forbidden fruit, serpent eye, flaming sword |
| Muted | `#8A867E` / `#6B6862` | verse refs, page numbers |

**Fonts:** Anton (God's voice, titles), IBM Plex Mono (narration captions, labels),
Archivo Narrow 700 (speech balloons), Noto Sans JP 900 (sound effects).

**Page:** 760×1080. Padding `28px 26px 30px`. The CSS grid has explicit
`grid-template-rows` and 12 px gaps. Panels have a 3 px ink border and
`overflow:hidden`. The page number goes centered at the bottom as `— NN —`.

**Recurring components** (copy the inline styles from existing pages):
- **Narration caption:** a paper box with a 2 px ink border, mono 600 at 11 px,
  uppercase.
- **Voice of God:** a black box with an inner paper rule
  (`box-shadow: inset 0 0 0 4px ink, inset 0 0 0 5.5px paper`), Anton, uppercase.
  No speaker is ever drawn.
- **Speech balloon:** a white ellipse (`border-radius:50%`) with a 2.5 px border
  and an SVG triangle tail placed *before* the balloon in the DOM. The serpent
  gets a black balloon with a double paper outline.
- **SFX:** Japanese katakana with a romanized tag underneath, e.g. ドン / DOOOM,
  ゴゴゴ / GOGOGO.
- **Day stamp:** a red-outlined rotated box with kanji over English
  (第一日 / THE FIRST DAY).
- **Verse ref:** tiny mono `GEN 1:3` in a corner.
- **Speed lines:** layered `repeating-conic-gradient` (focus) or thin tapered
  SVG wedges (horizontal). Screentone is a `radial-gradient` dot grid.
- **People:** a shared standing-silhouette `<path>` (feet at 0,0, ~199 units
  tall). Eve adds a hair path. Rotate −90° for a reclining figure.

## Text rules

- Use the **American Standard Version (1901)** (public domain) only. Trim with
  `…`; don't paraphrase. Keep ASV specifics: "Jehovah God", "waste and void",
  "great sea-monsters", "as God", Pishon, "the Cherubim".
- **Don't** quote the NASB, NAB (the Vatican site's translation) or any other
  copyrighted translation. If someone asks for one, offer the ASV or the World
  English Bible (also public domain) instead.
- Captions carry narration and balloons carry dialogue. God's words always use
  the Voice box.

## Roadmap

- Book Two: Genesis 4–9 (Cain and Abel → the Flood)
- Book Three: Genesis 11–22 (Babel, Abraham)
- Possible option: right-to-left reading order
