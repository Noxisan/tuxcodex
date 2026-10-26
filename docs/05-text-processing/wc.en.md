# wc

> Counts lines, words and bytes in files or in the output of other commands.

![wc output](../assets/screenshots/05-text-processing/wc.png)

## Syntax

```bash
wc [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-l`, `--lines` | Count lines |
| `-w`, `--words` | Count words |
| `-c`, `--bytes` | Count bytes |
| `-m`, `--chars` | Count characters (differs from bytes for umlauts and other UTF-8 characters) |
| `-L`, `--max-line-length` | Show the length of the longest line |

## Examples

**Count lines, words and bytes:**

```bash
wc /var/log/nginx/access.log
```

```text
  9 108 850 /var/log/nginx/access.log
```

The three numbers are lines, words and bytes.

**Only count lines:**

```bash
wc -l /var/log/nginx/access.log
```

```text
9 /var/log/nginx/access.log
```

**Count several files at once:**

```bash
wc -l /var/log/nginx/access.log users.csv
```

```text
  9 /var/log/nginx/access.log
  4 users.csv
 13 total
```

**Count the results of another command:**

```bash
grep ' 404 ' /var/log/nginx/access.log | wc -l
```

```text
3
```

**Only print the number, without the file name:**

```bash
wc -l < users.csv
```

```text
4
```

## When do I need it?

- To find out how big a log is or how many requests a server got
- To count matches together with `grep`, for example errors, logins or 404 requests
- To count files, users or processes: `ls /etc/nginx/sites-enabled | wc -l`
- In scripts that need a number to compare, for example "more than 100 errors"

!!! tip "Number only for scripts"
    With `wc -l < FILE`, `wc` reads from standard input and prints only the number. That
    is easier to use in scripts than the output with the file name.

!!! warning "The last line needs a line break"
    `wc -l` counts line breaks, not lines. If the last line of a file has no line break at
    the end, it is not counted.

## Related commands

[cat](../04-viewing-files/cat.md) · [sort](sort.md) · [grep](grep.md)
