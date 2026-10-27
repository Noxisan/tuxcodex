// Header: show the site title as "Tux" + "Dex" in two colours.
(function () {
  function init() {
    const title = document.querySelector(".md-header__topic:first-child .md-ellipsis");
    if (title && title.textContent.trim() === "TuxDex") {
      title.innerHTML = '<span class="tc-title-tux">Tux</span><span class="tc-title-dex">Dex</span>';
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
