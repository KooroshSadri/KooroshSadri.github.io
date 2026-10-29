(function () {
  'use strict';
  var root = document.documentElement;
  var themeButton = document.querySelector('.theme-toggle');
  var themeMeta = document.getElementById('browser-theme-color');
  function syncTheme() {
    var dark = root.getAttribute('data-theme') !== 'light';
    var label = dark ? 'Switch to light mode' : 'Switch to dark mode';
    if (themeButton) { themeButton.setAttribute('aria-label', label); themeButton.title = label; }
    if (themeMeta) themeMeta.content = dark ? '#1d1f21' : '#ffffff';
  }
  if (themeButton) {
    themeButton.hidden = false;
    themeButton.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('ks-theme', next); } catch (e) {}
      syncTheme();
    });
  }
  syncTheme();
  window.addEventListener('storage', function (event) {
    if (event.key === 'ks-theme') { root.setAttribute('data-theme', event.newValue === 'light' ? 'light' : 'dark'); syncTheme(); }
  });
  var menuButton = document.querySelector('.menu-toggle');
  var header = document.querySelector('.site-header');
  var menu = document.getElementById('primary-menu');
  if (menuButton && header && menu) {
    menuButton.hidden = false;
    function closeMenu() {
      header.classList.remove('menu-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Open navigation');
    }
    menuButton.addEventListener('click', function () {
      var expanded = menuButton.getAttribute('aria-expanded') !== 'true';
      header.classList.toggle('menu-open', expanded);
      menuButton.setAttribute('aria-expanded', String(expanded));
      menuButton.setAttribute('aria-label', expanded ? 'Close navigation' : 'Open navigation');
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && header.classList.contains('menu-open')) { closeMenu(); menuButton.focus(); }
    });
    document.addEventListener('click', function (event) { if (!header.contains(event.target)) closeMenu(); });
    menu.addEventListener('click', function (event) { if (event.target.closest('a')) closeMenu(); });
    window.addEventListener('resize', function () { if (window.innerWidth > 760) closeMenu(); });
  }
  var followButton = document.querySelector('.author__urls-wrapper button');
  if (followButton) {
    followButton.setAttribute('aria-controls', 'author-links');
    followButton.setAttribute('aria-expanded', 'false');
    var followLinks = document.getElementById('author-links');
    function syncFollowVisibility() {
      if (!followLinks) return;
      var style = window.getComputedStyle(followLinks);
      var visible = style.display !== 'none' && style.visibility !== 'hidden';
      followButton.setAttribute('aria-expanded', String(visible));
    }
    function queueFollowSync() {
      // Let the legacy handler run, then wait for any queued fade animations.
      window.setTimeout(function () {
        if (followLinks && window.jQuery) {
          window.jQuery(followLinks).promise().done(syncFollowVisibility);
        } else {
          syncFollowVisibility();
        }
      }, 0);
    }
    followButton.addEventListener('click', queueFollowSync);
    window.addEventListener('resize', queueFollowSync);
    document.addEventListener('DOMContentLoaded', queueFollowSync);
    queueFollowSync();
  }
}());
