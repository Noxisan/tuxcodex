#!/usr/bin/env python3
"""Render terminal screenshots for command pages from their first example.

For every English command page that contains a placeholder like
    <!-- SCREENSHOT: assets/screenshots/<chapter>/<command>.png -->
the first ```bash / ```text pair under "## Examples" is rendered as a
terminal window PNG, and the placeholder is replaced by the image in both
language versions of the page.

Usage:
    python scripts/screenshots.py                 # all chapters, placeholders only
    python scripts/screenshots.py 01-orientation  # one chapter
    python scripts/screenshots.py --all           # also re-render embedded images
"""

import argparse
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DOCS = Path(__file__).resolve().parent.parent / "docs"

USER = "nox"
HOST = "tuxcodex-srv"

# Colours match docs/stylesheets/tuxcodex.css
BG = "#161a21"
TITLE_BG = "#1f242d"
BORDER = "#262b35"
TEXT = "#d4d7dd"
MUTED = "#8b919c"
ACCENT = "#7aa2f7"
DOTS = ("#ed8796", "#eed49f", "#a6da95")

SCALE = 2
FONT_SIZE = 15 * SCALE
LINE_HEIGHT = int(FONT_SIZE * 1.45)
PAD_X = 20 * SCALE
PAD_Y = 16 * SCALE
TITLE_H = 34 * SCALE
MIN_COLS = 72

PLACEHOLDER = re.compile(r"<!-- SCREENSHOT: assets/screenshots/(?P<path>[^ ]+\.png) -->")
EMBED = re.compile(r"!\[[^\]]*\]\(\.\./assets/screenshots/(?P<path>[^)]+\.png)\)")
BLOCK = re.compile(r"```bash\n(?P<cmd>.*?)```\s*```text\n(?P<out>.*?)```", re.S)


def font_file(pattern):
    result = subprocess.run(["fc-match", "-f", "%{file}", pattern],
                            capture_output=True, text=True, check=True)
    return result.stdout


class Fonts:
    """Monospace font with per-character fallback for symbols it lacks."""

    def __init__(self):
        self.regular = ImageFont.truetype(font_file("monospace:style=Regular"), FONT_SIZE)
        self.bold = ImageFont.truetype(font_file("monospace:style=Bold"), FONT_SIZE)
        self.cell = self.regular.getlength("M")
        self.fallbacks = {}

    def for_char(self, ch, bold=False):
        base = self.bold if bold else self.regular
        if ord(ch) < 0x2500:
            return base
        if ch not in self.fallbacks:
            path = font_file(f":charset={ord(ch):x}")
            self.fallbacks[ch] = ImageFont.truetype(path, FONT_SIZE) if path else base
        return self.fallbacks[ch]


def first_example(page):
    text = page.read_text()
    examples = text.split("## Examples", 1)[1]
    match = BLOCK.search(examples)
    return match["cmd"].rstrip("\n").split("\n"), match["out"].rstrip("\n").split("\n")


def render(commands, output, target, fonts):
    prompt = [(f"{USER}@{HOST}", ACCENT, True), (":", TEXT, False),
              ("~", ACCENT, False), ("$ ", TEXT, False)]
    lines = [prompt + [(cmd, TEXT, False)] for cmd in commands]
    lines += [[(line, TEXT, False)] for line in output]
    lines.append(prompt)

    cols = max(MIN_COLS, *(sum(len(t) for t, _, _ in line) for line in lines))
    width = int(cols * fonts.cell) + 2 * PAD_X
    height = TITLE_H + 2 * PAD_Y + len(lines) * LINE_HEIGHT

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, TITLE_H], fill=TITLE_BG)
    draw.line([0, TITLE_H, width, TITLE_H], fill=BORDER, width=SCALE)
    r = 6 * SCALE
    for i, colour in enumerate(DOTS):
        cx = PAD_X + r + i * 3.4 * r
        draw.ellipse([cx - r, TITLE_H / 2 - r, cx + r, TITLE_H / 2 + r], fill=colour)
    title = f"{USER}@{HOST}: ~"
    draw.text(((width - fonts.regular.getlength(title)) / 2, TITLE_H / 2), title,
              font=fonts.regular, fill=MUTED, anchor="lm")

    y = TITLE_H + PAD_Y
    for line in lines:
        col = 0
        for segment, colour, bold in line:
            for ch in segment:
                draw.text((PAD_X + col * fonts.cell, y), ch,
                          font=fonts.for_char(ch, bold), fill=colour)
                col += 1
        y += LINE_HEIGHT
    # Cursor after the final prompt
    cursor_x = PAD_X + sum(len(t) for t, _, _ in prompt) * fonts.cell
    draw.rectangle([cursor_x, y - LINE_HEIGHT + 3 * SCALE,
                    cursor_x + fonts.cell, y - LINE_HEIGHT + FONT_SIZE + 3 * SCALE], fill=MUTED)

    target.parent.mkdir(parents=True, exist_ok=True)
    img.save(target, optimize=True)


def embed(page_en, rel_path):
    name = Path(rel_path).stem
    image = f"![{name} output](../assets/screenshots/{rel_path})"
    for page in (page_en, page_en.with_name(page_en.name.replace(".en.md", ".de.md"))):
        if page.exists():
            text = page.read_text()
            page.write_text(text.replace(f"<!-- SCREENSHOT: assets/screenshots/{rel_path} -->", image))


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("chapters", nargs="*", help="chapter folders, e.g. 01-orientation")
    parser.add_argument("--all", action="store_true", help="also re-render images that are already embedded")
    args = parser.parse_args()

    chapters = [DOCS / c for c in args.chapters] or sorted(p for p in DOCS.iterdir() if p.is_dir() and p.name[:2].isdigit())
    fonts = Fonts()
    for chapter in chapters:
        for page in sorted(chapter.glob("*.en.md")):
            text = page.read_text()
            match = PLACEHOLDER.search(text) or (args.all and EMBED.search(text))
            if not match or "## Examples" not in text:
                continue
            commands, output = first_example(page)
            render(commands, output, DOCS / "assets/screenshots" / match["path"], fonts)
            embed(page, match["path"])
            print(f"rendered {match['path']}")


if __name__ == "__main__":
    main()
