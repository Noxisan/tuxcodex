# rm

> Deletes files and directories permanently, without a recycle bin.

![rm output](../assets/screenshots/03-files/rm.png)

## Syntax

```bash
rm [OPTION]... FILE...
```

## Options

| Option | Description |
|--------|-------------|
| `-r`, `-R`, `--recursive` | Delete directories with all their contents |
| `-f`, `--force` | Never ask, ignore files that don't exist |
| `-i` | Ask before every single file |
| `-I` | Ask once before deleting more than three files or deleting recursively |
| `-v`, `--verbose` | Show every deleted file |
| `-d`, `--dir` | Delete empty directories |
| `--` | End of options: everything after it is a file name |

## Examples

**Delete a file:**

```bash
rm -v notes-old.txt
```

```text
removed 'notes-old.txt'
```

**Delete a directory without `-r`:**

```bash
rm scripts-2026
```

```text
rm: cannot remove 'scripts-2026': Is a directory
```

**Delete a directory with all its contents:**

```bash
rm -rv scripts-2026
```

```text
removed 'scripts-2026/cleanup.sh'
removed 'scripts-2026/backup.sh'
removed directory 'scripts-2026'
```

**Ask once before deleting many files:**

```bash
rm -I *.log
```

```text
rm: remove 5 arguments?
```

**Delete a write-protected file:**

```bash
rm notes.txt
```

```text
rm: remove write-protected regular file 'notes.txt'?
```

`rm` asks because the file has no write permission. Answer `y` to delete it anyway.

**Delete a file whose name starts with `-`:**

```bash
rm -file.txt
rm ./-file.txt
```

```text
rm: invalid option -- 'l'
Try 'rm ./-file.txt' to remove the file '-file.txt'.
Try 'rm --help' for more information.
```

The first command fails because `rm` reads `-file.txt` as options. The second one works.

## When do I need it?

- To clean up old logs, backups, temporary files and leftovers of installations
- To remove a website, an application or a user's data after it is no longer needed
- To free up disk space when a partition is full

!!! tip "Safety net with `-I`"
    `rm -I` asks only once, but before large deletions. That is much less annoying than
    `-i` and still stops most accidents with wildcards.

!!! warning "There is no recycle bin"
    Files deleted with `rm` are gone. Only a backup can bring them back. Check wildcards
    with `ls` first: `ls *.log`, then `rm *.log`.

!!! danger "`rm -rf` with variables in scripts"
    If a variable is empty, `rm -rf "$DIR/"*` becomes `rm -rf /*` and deletes the whole
    system. Let Bash abort if the variable is empty:

    ```bash
    rm -rf "${DIR:?}/"*
    ```

    `rm` refuses to delete `/` itself (`--preserve-root` is the default), but `/*` is not
    protected.

## Related commands

[mv](mv.md) · [find](../02-navigation/find.md) · [rmdir](rmdir.md) · [truncate](truncate.md) · [shred](shred.md)
