---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-file-document-outline:{ .tc-hero-icon }

# Files

Creating, copying, moving, linking and deleting files and directories, and finding out
what a file really is.

</div>

## Create

<div class="grid cards" markdown>

-   :material-file-plus-outline:{ .lg .middle } **[touch](touch.md)**

    ---

    Create an empty file or update its timestamps.

-   :material-folder-plus-outline:{ .lg .middle } **[mkdir](mkdir.md)**

    ---

    Create directories, including missing parent directories.

</div>

## Working safely with files

Most mistakes with files happen in a second and can't be undone. These habits protect
you on every server:

| Habit | Example |
|-------|---------|
| Make a copy before you edit a configuration | `cp sshd_config{,.bak}` |
| Test wildcards with `ls` before using them with `rm` or `mv` | `ls *.log` → `rm *.log` |
| Let `cp`, `mv` and `rm` ask before overwriting or deleting | `cp -i`, `mv -i`, `rm -i` |
| Copy with permissions and timestamps | `cp -a` instead of `cp -r` |
| Check where you are before using relative paths | `pwd` |
| Use quotes for names with spaces | `rm "old backup.tar.gz"` |

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
