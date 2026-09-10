(function () {
  'use strict';
  const mobile = window.matchMedia('(max-width: 779px)');
  const pairs = [
    ['top', 'mobile-top'], ['desktop-start', 'mobile-top'],
    ['services', 'mobile-services'], ['faq', 'mobile-questions'],
    ['consult', 'mobile-consult'], ['consult-form', 'mobile-consult-form'],
    ['path', 'mobile-consult']
  ];
  let observer, timer, frame;
  function stop() {
    if (observer) observer.disconnect();
    clearTimeout(timer);
    cancelAnimationFrame(frame);
  }
  function target() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return null; }
    const pair = pairs.find(p => p.includes(id));
    if (pair) id = pair[mobile.matches ? 1 : 0];
    return document.getElementById(id);
  }
  function start() {
    stop();
    const element = target();
    if (!element) return;
    // Correct late image/font layout changes, but never fight a user's scrolling.
    function align() {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(function () {
        if (!element.getClientRects().length) return;
        const root = document.documentElement;
        const previous = root.style.scrollBehavior;
        root.style.scrollBehavior = 'auto';
        window.scrollTo(0, Math.max(0, element.getBoundingClientRect().top + window.scrollY - 16));
        root.style.scrollBehavior = previous;
      });
    }
    observer = new ResizeObserver(align);
    document.querySelectorAll('main, main section, main img').forEach(e => observer.observe(e));
    align();
    timer = setTimeout(stop, 10000);
  }
  ['wheel', 'touchstart', 'pointerdown', 'keydown'].forEach(type =>
    window.addEventListener(type, stop, { passive: true }));
  window.addEventListener('hashchange', start);
  mobile.addEventListener('change', start);
  // A repeat click on the current fragment does not emit hashchange.
  document.addEventListener('click', function (event) {
    const link = event.target.closest && event.target.closest('a[href^="#"]');
    if (link && link.getAttribute('href') === location.hash) start();
  });
  start();
}());
