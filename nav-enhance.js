// nav-enhance.js
// 目标：
// 1) 手机端三横线菜单变“右侧抽屉”，不全屏
// 2) 提供关闭按钮 + 点击遮罩关闭 + ESC 关闭
// 3) 与原站 script.js 共存：不改原逻辑，只同步 body.nav-open 状态

document.addEventListener('DOMContentLoaded', function () {
  var menuToggle = document.getElementById('menuToggle');
  var navMenu = document.getElementById('navMenu');
  var navBackdrop = document.getElementById('navBackdrop');
  var navClose = document.getElementById('navClose');

  if (!menuToggle || !navMenu) return;

  function syncBodyState() {
    var isOpen = navMenu.classList.contains('active');
    document.body.classList.toggle('nav-open', isOpen);
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  }

  function closeMenu() {
    navMenu.classList.remove('active');
    menuToggle.classList.remove('active');
    syncBodyState();
  }

  // 原站脚本已绑定 click：这里再监听一次，用于同步 body.nav-open
  menuToggle.addEventListener('click', function () {
    // 等原站脚本先切换 class
    setTimeout(syncBodyState, 0);
  });

  // 键盘可访问：Enter/Space 打开
  menuToggle.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      menuToggle.click();
    }
  });

  if (navBackdrop) {
    navBackdrop.addEventListener('click', closeMenu);
  }

  if (navClose) {
    navClose.addEventListener('click', closeMenu);
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeMenu();
    }
  });

  // 点击导航链接后（手机端）关闭抽屉：原站已有逻辑，这里再兜底一次
  navMenu.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function () {
      if (window.innerWidth <= 768) closeMenu();
    });
  });

  // 初始同步
  syncBodyState();

  // 视口变化时同步
  window.addEventListener('resize', function () {
    if (window.innerWidth > 768) {
      document.body.classList.remove('nav-open');
    } else {
      syncBodyState();
    }
  });
});
