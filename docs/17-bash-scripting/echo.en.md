# echo

> Prints text and variables. The simplest way for a script to report what it is doing.

![echo output](../assets/screenshots/17-bash-scripting/echo.png)

## Syntax

```bash
echo [OPTION]... [TEXT]...
```

## Options

| Option | Description |
|--------|-------------|
| `-n` | No line break at the end |
| `-e` | Interpret escapes like `\n` (new line) and `\t` (tab) |
| `>&2` | Write to standard error instead of standard output |

## Examples

**Print text with a variable:**

```bash
echo "Hello, $USER"
```

```text
Hello, nox
```

**Several lines with `-e`:**

```bash
echo -e "line 1\nline 2"
```

```text
line 1
line 2
```

**Append a line to a file:**

```bash
echo "192.0.2.20 db01" | sudo tee -a /etc/hosts
```

```text
192.0.2.20 db01
```

`sudo echo ... >> /etc/hosts` doesn't work, because the redirection runs as your user. `tee -a`
with `sudo` does.

**An error message on standard error:**

```bash
echo "backup failed: disk full" >&2
```

```text
backup failed: disk full
```

## When do I need it?

- To report progress in a script
- To write a line into a file: `echo "text" >> file`
- To print error messages on standard error, where they don't mix with the output

!!! tip "Errors on standard error"
    `echo "error" >&2` writes to standard error. If someone redirects the output of your
    script into a file, the error messages still appear on the screen.

!!! warning "`echo` is not portable"
    `echo -e` and `echo -n` behave differently in other shells and with `/bin/sh`. For
    formatted or exact output, use [`printf`](printf.md).

## Related commands

[printf](printf.md) · [read](read.md) · [tee](../05-text-processing/tee.md)
