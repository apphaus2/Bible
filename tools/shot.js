const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const [,, src, out] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 760, height: 1080 } });
  let html = fs.readFileSync(src, 'utf8').replace('<script src="./support.js"></script>', '').replace(/\{\{accent\}\}/g, '#D7261E');
  await p.setContent(html, { waitUntil: 'load' });
  await p.waitForTimeout(400);
  await p.screenshot({ path: out });
  await b.close();
})();
