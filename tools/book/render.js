// Playwright helper for tools/book/export_book.py.
//   node tools/book/render.js pdf   <print.html> <out.pdf>     every .sheet becomes one PDF page (size from @page)
//   node tools/book/render.js cover <cover.html> <out.jpg>     the 760×1080 cover as a JPEG for e-reader libraries
const { chromium } = require('playwright');
const { pathToFileURL } = require('url');
(async () => {
  const [,, mode, src, out] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 760, height: 1080 } });
  await p.goto(pathToFileURL(src).href, { waitUntil: 'load' });
  try { await p.evaluate(() => document.fonts.ready); } catch (e) {}
  if (mode === 'pdf') {
    await p.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  } else {
    await p.screenshot({ path: out, type: 'jpeg', quality: 90 });
  }
  await b.close();
})();
