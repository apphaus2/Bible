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
  var x0 = null;
  document.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 70) go(dx < 0 ? 'next' : 'prev');
  }, { passive: true });
})();
