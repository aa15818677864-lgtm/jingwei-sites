(function () {
  document.querySelectorAll('[data-photo-carousel]').forEach(function (root) {
    const slides = Array.from(root.querySelectorAll('.lh-photo-slides img'));
    const viewport = root.querySelector('.lh-photo-slides');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let index = 0;
    let paused = reducedMotion.matches;
    let visible = false;
    let hovering = false;
    let focused = false;
    let timer;
    function button(label, text, parent, action) {
      const node = document.createElement('button');
      node.type = 'button';
      node.setAttribute('aria-label', label);
      node.textContent = text;
      node.addEventListener('click', action);
      parent.appendChild(node);
      return node;
    }
    const dots = document.createElement('div');
    dots.className = 'lh-photo-dots';
    const dotButtons = slides.map(function (slide, i) {
      return button((i + 1) + ' / ' + slides.length + ' · ' + slide.alt, '', dots, function () { show(i); });
    });
    root.appendChild(dots);
    root.classList.add('lh-photo-ready');
    function show(next) {
      index = (next + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        slide.hidden = false;
        slide.classList.toggle('is-active', i === index);
        slide.setAttribute('aria-hidden', String(i !== index));
      });
      dotButtons.forEach(function (dot, i) { dot.setAttribute('aria-pressed', String(i === index)); });
      root.dataset.activeSlide = String(index + 1);
      updateTimer();
    }
    function updateTimer() {
      clearTimeout(timer);
      if (!paused && visible && !hovering && !focused && !document.hidden) {
        timer = setTimeout(function () { show(index + 1); }, 1500);
      }
    }
    root.addEventListener('mouseenter', function () { hovering = true; updateTimer(); });
    root.addEventListener('mouseleave', function () { hovering = false; updateTimer(); });
    root.addEventListener('focusin', function () { focused = true; updateTimer(); });
    root.addEventListener('focusout', function (event) { focused = root.contains(event.relatedTarget); updateTimer(); });
    document.addEventListener('visibilitychange', updateTimer);
    reducedMotion.addEventListener('change', function () { paused = reducedMotion.matches; updateTimer(); });
    let start;
    viewport.addEventListener('touchstart', function (event) {
      if (event.touches.length === 1) start = { x: event.touches[0].clientX, y: event.touches[0].clientY };
    }, { passive: true });
    viewport.addEventListener('touchend', function (event) {
      if (!start) return;
      const dx = event.changedTouches[0].clientX - start.x;
      const dy = event.changedTouches[0].clientY - start.y;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) show(index + (dx < 0 ? 1 : -1));
      start = null;
    }, { passive: true });
    viewport.addEventListener('touchcancel', function () { start = null; });
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) slides.forEach(function (slide) { slide.loading = 'eager'; });
      updateTimer();
    }, { threshold: 0.2 }).observe(root);
    show(0);
  });
})();
