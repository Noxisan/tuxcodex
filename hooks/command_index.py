"""MkDocs hook: replace <!-- COMMAND_INDEX --> with an alphabetical list of all commands.

The list is built from the command pages in docs/NN-chapter/*.en.md (all pages except
the chapter overviews), so new commands show up automatically.
"""

from pathlib import Path

PLACEHOLDER = "<!-- COMMAND_INDEX -->"


def on_page_markdown(markdown, page, config, files):
    if PLACEHOLDER not in markdown:
        return markdown
    docs = Path(config["docs_dir"])
    commands = sorted(
        ((path.name.split(".")[0], path.parent.name)
         for path in docs.glob("[0-9][0-9]-*/*.en.md")
         if not path.name.startswith("index.")),
        key=lambda item: item[0].lower(),
    )
    items = "\n".join(f"- [`{name}`]({chapter}/{name}.md)" for name, chapter in commands)
    block = f'<div class="tc-command-index" markdown>\n\n{items}\n\n</div>'
    return markdown.replace(PLACEHOLDER, block)
