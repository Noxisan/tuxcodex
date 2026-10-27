# Understanding scripts

A shell script is a text file with commands that Bash runs one after the other, exactly as
if you typed them. Anything you do more than twice by hand is a candidate for a script.

## The first lines

```bash
#!/usr/bin/env bash
set -euo pipefail
```

| Line | Meaning |
|------|---------|
| `#!/usr/bin/env bash` | The **shebang**: which program runs the script. Always the very first line |
| `set -euo pipefail` | Stop on errors and unset variables, see [`set`](set.md) |

Make the script executable and start it with its path:

```text
$ chmod +x backup.sh
$ ./backup.sh
```

`./` is needed because the current directory isn't in `PATH`. Scripts for everyone belong
in `/usr/local/bin/`, then they can be called by name.

## Variables

```text
$ name="tuxcodex-srv"
$ echo "Host: $name"
Host: tuxcodex-srv
```

No spaces around `=`. Read a variable with `$name` or `${name}`, and save the output of a
command with `$(command)`: `today=$(date +%F)`.

## Quoting

| Quotes | Effect | Example | Result |
|--------|--------|---------|--------|
| `"…"` | Variables are expanded, spaces stay together | `"Host: $name"` | `Host: tuxcodex-srv` |
| `'…'` | Everything stays literal | `'Host: $name'` | `Host: $name` |
| none | Words are split at spaces | `ls $file` with `file="old backup.tar.gz"` | `ls` gets two arguments |

Always put variables in double quotes: `"$file"`. That's the most common source of
errors in shell scripts.

## Arguments

| Variable | Content |
|----------|---------|
| `$0` | Name of the script |
| `$1`, `$2`, … | First, second, … argument |
| `$#` | Number of arguments |
| `"$@"` | All arguments, each one kept as it was given |
| `$?` | Exit code of the last command |

```text
$ ./greet.sh web01 "two words" 3
Script: ./greet.sh
First argument: web01
Number of arguments: 3
All arguments: web01 two words 3
```

## Exit codes

Every command ends with an exit code: `0` means success, everything else an error.
Conditions in Bash check exactly this code.

```text
$ grep -q root /etc/passwd; echo $?
0
$ grep -q nosuchuser /etc/passwd; echo $?
1
```

Scripts should end with a meaningful code too: `exit 0` for success, `exit 1` or higher
for errors, see [`exit`](exit.md).

## A complete example

`/usr/local/bin/backup-www`:

```bash
#!/usr/bin/env bash
# Back up a directory to /mnt/backup, keep 7 days.
set -euo pipefail

src="${1:-/srv/www}"
target="/mnt/backup/$(basename "$src")-$(date +%F).tar.zst"

log() {
    logger -t backup-www "$*"
    printf '%s %s\n' "$(date +%T)" "$*"
}

if [[ ! -d "$src" ]]; then
    log "Source $src does not exist"
    exit 1
fi

log "Starting backup of $src"
tar --zstd -cf "$target" -C "$(dirname "$src")" "$(basename "$src")"
log "Created $target ($(du -h "$target" | cut -f1))"

find /mnt/backup -name "$(basename "$src")-*.tar.zst" -mtime +7 -delete
log "Done"
```

```text
$ sudo backup-www
10:42:17 Starting backup of /srv/www
10:42:19 Created /mnt/backup/www-2026-10-26.tar.zst (48M)
10:42:19 Done
```

The pages of this chapter explain every building block of this script.

!!! tip "Check scripts with ShellCheck"
    [`shellcheck`](shellcheck.md) finds missing quotes, typos in variables and many other
    mistakes before the script ever runs.

!!! warning "`sh` is not `bash`"
    On Debian and Ubuntu, `/bin/sh` is `dash`, a smaller shell without `[[ ]]`, arrays and
    other Bash features. A script with `#!/bin/sh` that uses them fails with errors like
    `[[: not found`. Use `#!/usr/bin/env bash` for Bash scripts.
