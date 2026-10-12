(function () {
  var sheet = document.getElementById('sheet');
  if (sheet) {
    var box = document.createElement('div'); box.className = 'box';
    sheet.parentNode.insertBefore(box, sheet); box.appendChild(sheet);
    var fit = function () {
      var w = Math.min(window.innerWidth - 24, 760);
      var s = w / 760;
      if (window.innerWidth >= 700) s = Math.min(s, (window.innerHeight - 120) / 1080);
      s = Math.max(s, 0.25);
      sheet.style.transform = 'scale(' + s + ')';
      box.style.width = (760 * s) + 'px'; box.style.height = (1080 * s) + 'px';
    };
    window.addEventListener('resize', fit); fit();
  }
  var go = function (rel) { var l = document.querySelector('link[rel="' + rel + '"]'); if (l) location.href = l.href; };
  document.addEventListener('keydown', function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (e.key === 'ArrowLeft') go('prev');
    if (e.key === 'ArrowRight') go('next');
  });
  // Swipe to turn the page: only a deliberate one-finger flick, never a pinch, never while zoomed in.
  //  - any second finger cancels the gesture (pinch-zoom), and touches are ignored for a moment after a pinch,
  //    because the fingers lift one at a time and the last one would otherwise look like a swipe;
  //  - nothing turns while the page is zoomed (visualViewport.scale > 1), so panning a zoomed page is safe,
  //    and a gesture during which the visual viewport moved or rescaled is a pan, not a swipe;
  //  - the flick must be long (a quarter of the screen, at least 90 px), mostly sideways and quick.
  var vv = window.visualViewport;
  var zoomed = function () { return vv ? vv.scale > 1.02 : (document.documentElement.clientWidth / window.innerWidth) > 1.02; };
  var view = function () { return vv ? [vv.scale, vv.pageLeft, vv.pageTop] : [1, window.scrollX, window.scrollY]; };
  var t0 = null, pinchUntil = 0;
  var cancel = function () { t0 = null; };
  document.addEventListener('touchstart', function (e) {
    if (e.touches.length > 1) { t0 = null; pinchUntil = Date.now() + 600; return; }
    if (Date.now() < pinchUntil || zoomed()) { t0 = null; return; }
    var t = e.touches[0];
    t0 = { x: t.clientX, y: t.clientY, at: Date.now(), view: view() };
  }, { passive: true });
  document.addEventListener('touchmove', function (e) {
    if (e.touches.length > 1) { t0 = null; pinchUntil = Date.now() + 600; }
  }, { passive: true });
  document.addEventListener('touchcancel', cancel, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (!t0) return;
    var s = t0; t0 = null;
    if (e.touches.length > 0 || Date.now() < pinchUntil || zoomed()) return;
    var v = view();
    if (Math.abs(v[0] - s.view[0]) > 0.01 || Math.abs(v[1] - s.view[1]) > 2 || Math.abs(v[2] - s.view[2]) > 2) return;
    var t = e.changedTouches[0], dx = t.clientX - s.x, dy = t.clientY - s.y;
    var far = Math.abs(dx) >= Math.max(90, window.innerWidth * 0.25);
    var flat = Math.abs(dx) > 2 * Math.abs(dy);
    var quick = Date.now() - s.at < 600;
    if (far && flat && quick) go(dx < 0 ? 'next' : 'prev');
  }, { passive: true });
})();
