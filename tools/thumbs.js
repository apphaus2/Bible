const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 760, height: 1080 } });
  for (const [src, out] of jobs) {
    let html = fs.readFileSync(src, 'utf8').replace('<script src="./support.js"></script>', '').replace(/\{\{accent\}\}/g, '#D7261E');
    await p.setContent(html, { waitUntil: 'load' }); await p.waitForTimeout(150);
    await p.screenshot({ path: out });
  }
  await b.close();
})();
