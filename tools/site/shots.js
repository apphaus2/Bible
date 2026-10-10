// Render .dc.html pages to 760×1080 PNGs with Playwright.
// Usage: node tools/site/shots.js <out_dir> page.dc.html …   (one browser for the whole batch)
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [,, outdir, ...srcs] = process.argv;
  fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 760, height: 1080 } });
  for (const src of srcs) {
    let html = fs.readFileSync(src, 'utf8').replace('<script src="./support.js"></script>', '').replace(/\{\{accent\}\}/g, '#D7261E');
    await p.setContent(html, { waitUntil: 'load' });
    try { await p.evaluate(() => document.fonts.ready); } catch (e) {}
    await p.waitForTimeout(150);
    const name = src.split('/').pop().replace('.dc.html', '.png');
    await p.screenshot({ path: outdir + '/' + name });
  }
  await b.close();
})();
