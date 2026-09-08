(function () {
  const menu = document.querySelector('.mobile-nav-dropdown');
  if (menu) {
    menu.addEventListener('click', function (event) {
      if (event.target.closest('a')) menu.open = false;
    });
    document.addEventListener('click', function (event) {
      if (!menu.contains(event.target)) menu.open = false;
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && menu.open) {
        menu.open = false;
        menu.querySelector('summary').focus();
      }
    });
  }
  document.querySelectorAll(".mobile-v6 .accordion").forEach(function (group) {
    group.addEventListener("toggle", function (event) {
      const opened = event.target;
      if (!(opened instanceof HTMLDetailsElement) || !opened.open) {
        return;
      }
      group.querySelectorAll("details[open]").forEach(function (item) {
        if (item !== opened) {
          item.open = false;
        }
      });
    }, true);
  });
})();
