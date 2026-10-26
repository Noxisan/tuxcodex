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

## Copy, move, delete

<div class="grid cards" markdown>

-   :material-content-copy:{ .lg .middle } **[cp](cp.md)**

    ---

    Copy files and directories.

-   :material-file-move-outline:{ .lg .middle } **[mv](mv.md)**

    ---

    Move or rename files and directories.

-   :material-delete-outline:{ .lg .middle } **[rm](rm.md)**

    ---

    Delete files and directories permanently.

-   :material-folder-remove-outline:{ .lg .middle } **[rmdir](rmdir.md)**

    ---

    Delete empty directories safely.

-   :material-shredder:{ .lg .middle } **[shred](shred.md)**

    ---

    Overwrite files securely before deleting them.

</div>

## Links

<div class="grid cards" markdown>

-   :material-link:{ .lg .middle } **[ln](ln.md)**

    ---

    Create symbolic and hard links.

</div>

## Inspect and change

<div class="grid cards" markdown>

-   :material-file-document-check-outline:{ .lg .middle } **[stat](stat.md)**

    ---

    Show all metadata: size, permissions, owner and timestamps.

-   :material-file-question-outline:{ .lg .middle } **[file](file.md)**

    ---

    Detect the file type from its content.

-   :material-content-cut:{ .lg .middle } **[truncate](truncate.md)**

    ---

    Empty, shorten or enlarge a file to an exact size.

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
