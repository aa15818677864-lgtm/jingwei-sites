(function () {
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
