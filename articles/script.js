(function () {
  var doc = document.documentElement;
  var progress = document.createElement("div");
  var progressBar = document.createElement("span");
  progress.className = "reading-progress";
  progress.setAttribute("aria-hidden", "true");
  progressBar.dataset.readingProgress = "true";
  progress.appendChild(progressBar);
  document.body.prepend(progress);

  function updateProgress() {
    var max = doc.scrollHeight - window.innerHeight;
    var value = max > 0 ? window.scrollY / max : 0;
    progressBar.style.transform = "scaleX(" + Math.max(0, Math.min(1, value)) + ")";
  }

  window.addEventListener("scroll", updateProgress, { passive: true });
  window.addEventListener("resize", updateProgress);
  updateProgress();

  var askLink = document.querySelector('a[href^="/ask/"]');
  var topicLink = document.querySelector('a[href^="/topics/"]');
  if (!askLink && !topicLink) return;

  var bar = document.createElement("nav");
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
})();
