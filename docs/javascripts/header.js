// Header: show the site title as "Tux" + "Codex" in two colours.
(function () {
  function init() {
    const title = document.querySelector(".md-header__topic:first-child .md-ellipsis");
    if (title && title.textContent.trim() === "TuxCodex") {
      title.innerHTML = '<span class="tc-title-tux">Tux</span><span class="tc-title-codex">Codex</span>';
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
