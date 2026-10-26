// Home page search field: opens the Material search and passes the focus on to it.
(function () {
  function openSearch(event) {
    const toggle = document.querySelector('input[data-md-toggle="search"]');
    const query = document.querySelector(".md-search__input");
    if (!toggle || !query) return;
    event.preventDefault();
    toggle.checked = true;
    toggle.dispatchEvent(new Event("change"));
    query.focus();
    event.target.blur();
  }

  function init() {
    const field = document.getElementById("tc-search-input");
    if (!field) return;
    field.addEventListener("focus", openSearch);
    field.addEventListener("mousedown", openSearch);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
