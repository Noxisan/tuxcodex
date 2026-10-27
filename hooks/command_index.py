"""MkDocs hook: replace <!-- COMMAND_INDEX --> with an alphabetical list of all commands.

The list is built from the command pages in docs/NN-chapter/*.en.md (all pages except
the chapter overviews), so new commands show up automatically. The name shown is the
page's first heading, so `git-commit.en.md` is listed as `git commit`.
"""

from pathlib import Path

PLACEHOLDER = "<!-- COMMAND_INDEX -->"


def title(path):
    return path.read_text().split("\n", 1)[0].removeprefix("# ").strip()


def on_page_markdown(markdown, page, config, files):
    if PLACEHOLDER not in markdown:
        return markdown
    docs = Path(config["docs_dir"])
    commands = sorted(
        ((title(path), path.name.split(".")[0], path.parent.name)
         for path in docs.glob("[0-9][0-9]-*/*.en.md")
         if not path.name.startswith(("index.", "basics."))),
        key=lambda item: item[0].lower(),
    )
    items = "\n".join(f"- [`{name}`]({chapter}/{slug}.md)" for name, slug, chapter in commands)
    block = f'<div class="tc-command-index" markdown>\n\n{items}\n\n</div>'
    return markdown.replace(PLACEHOLDER, block)
