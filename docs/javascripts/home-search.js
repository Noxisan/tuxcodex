// Home page search: searches the MkDocs search index and shows the results right below
// the search field. Only pages in the language of the current page are shown.
(function () {
  const MAX_RESULTS = 8;
  let entries = null;

  function config() {
    const node = document.getElementById("__config");
    return node ? JSON.parse(node.textContent) : { base: "." };
  }

  function escapeHtml(text) {
    return text.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
  }

  function plainText(html) {
    const div = document.createElement("div");
    div.innerHTML = html;
    return div.textContent.replace(/\s+/g, " ").trim();
  }

  function highlight(text, terms) {
    const parts = terms.filter(Boolean).map((t) => {
      const escaped = t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      // A single character is only highlighted at the beginning of the text
      return t.length < 2 ? "^" + escaped : escaped;
    });
    if (!parts.length) return escapeHtml(text);
    const pattern = new RegExp("(" + parts.join("|") + ")", "gi");
    return text.split(pattern).map((piece, i) =>
      i % 2 ? "<mark>" + escapeHtml(piece) + "</mark>" : escapeHtml(piece)).join("");
  }


  async function loadIndex(base) {
    if (entries) return entries;
    const response = await fetch(base + "/search/search_index.json");
    const data = await response.json();
    const german = document.documentElement.lang.startsWith("de");
    const pages = new Map();
    entries = [];
    for (const doc of data.docs) {
      if (german !== doc.location.startsWith("de/")) continue;
      if (doc.location === "" || doc.location === "de/") continue;  // skip the home page
      const [page, anchor] = doc.location.split("#");
      const item = { location: doc.location, page, anchor, title: doc.title, text: plainText(doc.text) };
      if (!anchor) pages.set(page, item);
      entries.push(item);
    }
    // Remember the page title and intro for section entries
    for (const item of entries) {
      const page = pages.get(item.page);
      item.pageTitle = page ? page.title : item.title;
      item.intro = page ? page.text : "";
    }
    return entries;
  }

  function search(query) {
    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    const results = new Map();
    for (const item of entries) {
      const title = item.pageTitle.toLowerCase();
      const haystack = (item.title + " " + item.text).toLowerCase();
      let score = 0;
      if (!item.anchor) {
        if (title === terms.join(" ")) score = 100;
        else if (title.startsWith(terms[0])) score = 60;
        else if (query.length > 1 && terms.every((t) => title.includes(t))) score = 40;
      }
      // Single characters only match command names, otherwise almost every page matches
      if (!score && query.length > 1 && terms.every((t) => haystack.includes(t))) score = item.anchor ? 5 : 10;
      if (!score) continue;
      const best = results.get(item.page);
      if (!best || score > best.score) results.set(item.page, { ...item, score });
    }
    return [...results.values()]
      .sort((a, b) => b.score - a.score || a.pageTitle.localeCompare(b.pageTitle))
      .slice(0, MAX_RESULTS);
  }

  function render(list, results, terms, base, emptyText) {
    if (!results.length) {
      list.innerHTML = '<li class="tc-search-empty">' + escapeHtml(emptyText) + "</li>";
      return;
    }
    list.innerHTML = results.map((r, i) => {
      const section = r.anchor ? ' <span class="tc-search-section">› ' + escapeHtml(r.title) + "</span>" : "";
      const snippet = (r.intro || r.text).slice(0, 160);
      return '<li><a href="' + base + "/" + r.location + '"' + (i === 0 ? ' class="tc-active"' : "") + ">" +
        '<span class="tc-search-title"><code>' + highlight(r.pageTitle, terms) + "</code>" + section + "</span>" +
        '<span class="tc-search-snippet">' + highlight(snippet, terms) + "</span></a></li>";
    }).join("");
  }

  function init() {
    const field = document.getElementById("tc-search-input");
    const list = document.getElementById("tc-search-results");
    if (!field || !list) return;
    const base = config().base;

    field.addEventListener("focus", () => loadIndex(base));
    field.addEventListener("input", async () => {
      await loadIndex(base);
      const query = field.value.trim();
      if (!query) {
        list.innerHTML = "";
        list.hidden = true;
        return;
      }
      render(list, search(query), query.toLowerCase().split(/\s+/), base, field.dataset.empty);
      if (list.hidden) {
        list.hidden = false;
        list.scrollIntoView({ block: "nearest", behavior: "smooth" });
      }
    });

    field.addEventListener("keydown", (event) => {
      const links = [...list.querySelectorAll("a")];
      const current = links.findIndex((a) => a.classList.contains("tc-active"));
      if (event.key === "Enter" && links[current]) {
        window.location.href = links[current].href;
      } else if (event.key === "Escape") {
        field.value = "";
        list.innerHTML = "";
        list.hidden = true;
      } else if ((event.key === "ArrowDown" || event.key === "ArrowUp") && links.length) {
        event.preventDefault();
        const next = (current + (event.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
        links.forEach((a, i) => a.classList.toggle("tc-active", i === next));
        links[next].scrollIntoView({ block: "nearest" });
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
