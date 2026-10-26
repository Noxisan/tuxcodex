# rmdir

> Deletes empty directories, and refuses as soon as a directory still contains something.

![rmdir output](../assets/screenshots/03-files/rmdir.png)

## Syntax

```bash
rmdir [OPTION]... DIRECTORY...
```

## Options

| Option | Description |
|--------|-------------|
| `-p`, `--parents` | Also delete the parent directories if they become empty |
| `-v`, `--verbose` | Show every deleted directory |
| `--ignore-fail-on-non-empty` | No error for directories that are not empty |

## Examples

**Delete an empty directory:**

```bash
rmdir -v private
```

```text
rmdir: removing directory, 'private'
```

**Try to delete a directory that is not empty:**

```bash
rmdir backup
```

```text
rmdir: failed to remove 'backup': Directory not empty
```

**Delete a path of empty directories from the inside out:**

```bash
rmdir -pv backup/2026/10
```

```text
rmdir: removing directory, 'backup/2026/10'
rmdir: removing directory, 'backup/2026'
rmdir: removing directory, 'backup'
rmdir: failed to remove directory 'backup': Directory not empty
```

`10` and `2026` were empty and are gone. `backup` still contains files and stays.

**Clean up without error messages:**

```bash
rmdir -p --ignore-fail-on-non-empty backup/2026/10
echo $?
```

```text
0
```

## When do I need it?

- To clean up empty directories after moving or deleting files
- In scripts, when a directory should only be removed if it is really empty
- As a safe alternative to `rm -r`: `rmdir` can never delete files by accident

!!! tip "Find all empty directories"
    To remove all empty directories below a path, combine `find` with `-empty`:
    `find /srv/backup -type d -empty -delete`. Check the list without `-delete` first.

!!! warning "Hidden files count too"
    If `rmdir` says `Directory not empty` although `ls` shows nothing, there are hidden
    files in it. Check with `ls -A`.

## Related commands

[rm](rm.md) · [mkdir](mkdir.md)
