(function () {
  var doc = document.documentElement;
  var article = document.querySelector(".article-main");
  var toc = document.querySelector(".toc");
  var progress = document.createElement("div");
  var progressBar = document.createElement("span");
  progress.className = "reading-progress";
  progress.setAttribute("aria-hidden", "true");
  progressBar.dataset.readingProgress = "true";
  progress.appendChild(progressBar);
  document.body.prepend(progress);

  function syncMobileQuickCheck() {
    if (!article) return;

    var existing = article.querySelector(".mobile-quick-check-panel");
    if (window.innerWidth > 980) {
      if (existing) existing.remove();
      return;
    }

    if (existing || !toc) return;

    var sourceQuickCheck = toc.querySelector(".quick-check");
    if (!sourceQuickCheck) return;

    var title = sourceQuickCheck.querySelector("h2");
    var list = sourceQuickCheck.querySelector("ul");
    if (!title || !list) return;

    var panel = document.createElement("section");
    panel.className = "quick-check mobile-quick-check-panel";
    panel.dataset.mobileQuickCheck = "true";

    var label = sourceQuickCheck.getAttribute("aria-label");
    if (label) panel.setAttribute("aria-label", label);

    panel.appendChild(title.cloneNode(true));
    panel.appendChild(list.cloneNode(true));

    var anchor = article.querySelector(".answer-card");
    if (anchor) {
      anchor.insertAdjacentElement("afterend", panel);
    } else {
      article.prepend(panel);
    }
  }

  var tocLinks = toc ? Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]')) : [];
  var tocTargets = tocLinks
    .map(function (link) {
      var id = decodeURIComponent(link.getAttribute("href").slice(1));
      var target = document.getElementById(id);
      return target ? { link: link, target: target } : null;
    })
    .filter(Boolean);

  function updateProgress() {
    var max = doc.scrollHeight - window.innerHeight;
    var value = max > 0 ? window.scrollY / max : 0;
    progressBar.style.transform = "scaleX(" + Math.max(0, Math.min(1, value)) + ")";

    if (tocTargets.length) {
      var active = tocTargets[0];
      tocTargets.forEach(function (item) {
        if (item.target.getBoundingClientRect().top <= 130) active = item;
      });
      tocTargets.forEach(function (item) {
        item.link.classList.toggle("is-active", item === active);
      });
    }
  }

  var askLink = document.querySelector('a[href^="/ask/"]');
  var topicLink = document.querySelector('a[href^="/topics/"]');
  var bar = null;
  if (askLink || topicLink) {
    bar = document.createElement("nav");
    bar.className = "mobile-action-bar";
    bar.setAttribute("aria-label", "文章快捷操作");

    if (askLink) {
      var ask = document.createElement("a");
      ask.href = askLink.href;
      ask.textContent = "先问 AI";
      bar.appendChild(ask);
    }

    if (topicLink) {
      var topic = document.createElement("a");
      topic.href = topicLink.href;
      topic.textContent = "提交情况";
      bar.appendChild(topic);
    }

    document.body.appendChild(bar);
  }

  function updateActionBar() {
    if (!bar) return;
    var footer = document.querySelector(".site-footer");
    var footerVisible = footer ? footer.getBoundingClientRect().top < window.innerHeight - 40 : false;
    bar.classList.toggle("is-visible", window.scrollY > 360 && !footerVisible);
  }

  function updateUi() {
    syncMobileQuickCheck();
    updateProgress();
    updateActionBar();
  }

  window.addEventListener("scroll", updateUi, { passive: true });
  window.addEventListener("resize", updateUi);
  updateUi();
})();
