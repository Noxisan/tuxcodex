"""Generate docs/basics.{en,de}.md: all chapter basics, grouped by area, in nav order.

Run after adding a chapter: python3 scripts/basics_overview.py
Each card shows the title of the basics page and the description from the basics box
of the chapter overview.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
nav = (ROOT / "mkdocs.yml").read_text()
order = re.findall(r"^      - (\d\d-[a-z0-9-]+)/index\.md$", nav, re.M)

AREAS = {
    "en": [("Linux basics", ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "27", "28"]),
           ("Automation & DevOps", ["17", "18", "19", "20", "21", "22"]),
           ("Security", ["23", "24", "25", "26"])],
    "de": [("Linux-Grundlagen", None), ("Automatisierung & DevOps", None), ("Sicherheit", None)],
}
HEAD = {
    "en": ("Basics overview", "Every chapter starts with a basics page: the concepts, tables and workflows you need\nbefore the individual commands make sense. Here they are all in one place, in the order of\nthe handbook."),
    "de": ("Grundlagen im Überblick", "Jedes Kapitel beginnt mit einer Grundlagen-Seite: die Begriffe, Tabellen und Abläufe, die\ndu brauchst, bevor die einzelnen Befehle Sinn ergeben. Hier stehen sie alle an einem Ort,\nin der Reihenfolge des Handbuchs."),
}
LABEL = {"en": "**Basics:**", "de": "**Grundlagen:**"}

for lang in ("en", "de"):
    title, intro = HEAD[lang]
    out = ["---", "icon: material/school-outline", "hide:", "  - toc", "---", "",
           '<div class="tc-hero tc-hero--chapter tc-hero--basics" markdown>', "", ":material-school-outline:{ .tc-hero-icon }", "",
           f"# {title}", "", intro, "", "</div>", ""]
    for i, (area, nums) in enumerate(AREAS[lang]):
        nums = AREAS["en"][i][1]
        out += [f"## {area}", "", '<div class="grid cards tc-basics-cards" markdown>', ""]
        for ch in order:
            if ch[:2] not in nums:
                continue
            idx = (ROOT / "docs" / ch / f"index.{lang}.md").read_text()
            icon = re.search(r"^icon: material/(\S+)", idx, re.M).group(1)
            basics = (ROOT / "docs" / ch / f"basics.{lang}.md").read_text()
            name = re.search(r"^# (.+)$", basics, re.M).group(1)
            desc = re.search(re.escape(LABEL[lang]) + r" (.*?) :material-arrow-right", idx).group(1)
            chapter = re.search(r"^# (.+)$", idx, re.M).group(1)
            # Some summaries repeat the page title; keep only what they add
            if desc.lower().startswith(name.lower()):
                desc = desc[len(name):].lstrip(" ,:")
            desc = f"{chapter}: {desc}" if desc else chapter
            out += [f"-   :material-{icon}:{{ .lg .middle }} **[{name}]({ch}/basics.md)**", "", "    ---", "", f"    {desc}", ""]
        out += ["</div>", ""]
    (ROOT / "docs" / f"basics.{lang}.md").write_text("\n".join(out))
print(len(order), "chapters")
