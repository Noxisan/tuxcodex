# grep

> Searches files or the output of other commands for lines that match a pattern, and shows only those lines.

![grep output](../assets/screenshots/05-text-processing/grep.png)

## Syntax

```bash
grep [OPTION]... PATTERN [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-i`, `--ignore-case` | Ignore upper and lower case |
| `-v`, `--invert-match` | Show lines that do **not** match |
| `-c`, `--count` | Only print the number of matching lines |
| `-n`, `--line-number` | Show the line number in front of each match |
| `-w`, `--word-regexp` | Only match whole words |
| `-x`, `--line-regexp` | Only match whole lines |
| `-o`, `--only-matching` | Only print the matching part, not the whole line |
| `-E`, `--extended-regexp` | Use extended regular expressions (`+`, `?`, `|`, `()`) |
| `-F`, `--fixed-strings` | Search for the exact text, no regular expression |
| `-r`, `--recursive` | Search all files in a directory and its subdirectories |
| `-R`, `--dereference-recursive` | Like `-r`, but also follow symbolic links |
| `-l`, `--files-with-matches` | Only print the names of files that contain a match |
| `-A N` / `-B N` / `-C N` | Also show `N` lines after / before / around each match |
| `-q`, `--quiet` | Print nothing, only return the exit status (for scripts) |
| `--include=GLOB` | With `-r`: only search files matching `GLOB` (e.g. `'*.conf'`) |

The most important parts of regular expressions:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `^` | Beginning of the line | `^#` lines starting with `#` |
| `$` | End of the line | `;$` lines ending with `;` |
| `.` | Any single character | `h.t` matches `hat`, `hot` |
| `*` | The previous character any number of times | `ab*c` matches `ac`, `abbc` |
| `[...]` | One of the characters in the brackets | `[0-9]` a digit |
| `+` | The previous character at least once (`-E`) | `[0-9]+` a number |
| `a|b` | `a` or `b` (`-E`) | `error|warn` |
| `\s` | A space or tab | `^\s*$` empty line |

## Examples

**Find all failed requests (404) in a log:**

```bash
grep ' 404 ' /var/log/nginx/access.log
```

```text
192.0.2.77 - - [26/Oct/2026:10:02:19 +0100] "GET /wp-login.php HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.0.2.77 - - [26/Oct/2026:10:02:20 +0100] "GET /.env HTTP/1.1" 404 153 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:10:41:12 +0100] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0"
```

**Count the matches:**

```bash
grep -c ' 404 ' /var/log/nginx/access.log
```

```text
3
```

**Show everything except successful requests:**

```bash
grep -v ' 200 ' /var/log/nginx/access.log
```

```text
198.51.100.23 - - [26/Oct/2026:09:15:51 +0100] "POST /login HTTP/1.1" 302 0 "-" "Mozilla/5.0"
192.0.2.77 - - [26/Oct/2026:10:02:19 +0100] "GET /wp-login.php HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.0.2.77 - - [26/Oct/2026:10:02:20 +0100] "GET /.env HTTP/1.1" 404 153 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:10:41:12 +0100] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0"
```

**Search for several patterns at once:**

```bash
grep -E ' (302|404) ' /var/log/nginx/access.log | cut -d' ' -f1,7,9
```

```text
198.51.100.23 /login 302
192.0.2.77 /wp-login.php 404
192.0.2.77 /.env 404
198.51.100.23 /favicon.ico 404
```

**Show a match together with the lines around it:**

```bash
grep -C1 'POST' /var/log/nginx/access.log
```

```text
198.51.100.23 - - [26/Oct/2026:09:15:44 +0100] "GET /login HTTP/1.1" 200 2841 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:09:15:51 +0100] "POST /login HTTP/1.1" 302 0 "-" "Mozilla/5.0"
192.0.2.77 - - [26/Oct/2026:10:02:19 +0100] "GET /wp-login.php HTTP/1.1" 404 153 "-" "Mozilla/5.0"
```

**Extract only the IP addresses:**

```bash
grep -oE '^[0-9.]+' /var/log/nginx/access.log | sort -u
```

```text
192.0.2.10
192.0.2.55
192.0.2.77
198.51.100.23
```

**Show a configuration without comments and empty lines:**

```bash
grep -vE '^\s*(#|$)' /etc/hosts
```

```text
127.0.0.1       localhost
127.0.1.1       tuxcodex-srv.example.com        tuxcodex-srv
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

**Find out which configuration file contains a setting:**

```bash
grep -rl 'example.com' /etc/nginx/
```

```text
/etc/nginx/sites-available/example.com
```

**Search for an exact IP address:**

```bash
grep '192.0.2.1' ips.txt
grep -Fw '192.0.2.1' ips.txt
```

```text
192.0.2.1 - a
192.0.2.10 - b
192.0.2.155 - c
192.0.2.1 - a
```

In a regular expression, `.` stands for any character, and `192.0.2.1` also matches
`192.0.2.10`. `-F` searches for the exact text, `-w` only for the whole word.

**Check in a script whether something exists:**

```bash
grep -q '^nox:' /etc/passwd && echo "user exists"
```

```text
user exists
```

## When do I need it?

- To find errors, IP addresses, user names or URLs in logs
- To find out in which configuration file a setting is defined (`grep -r`)
- To filter the output of other commands: `ps aux | grep nginx`,
  `dpkg -l | grep openssh`
- To show only the active lines of a configuration, without comments
- In scripts, to check whether a line, a user or a setting exists (`grep -q`)

!!! tip "Search compressed logs with `zgrep`"
    `zgrep` works like `grep`, but also searches `.gz` files:
    `zgrep ' 500 ' /var/log/nginx/access.log*` searches all rotated logs at once.

!!! tip "Colour and context"
    On Debian, `grep` is an alias for `grep --color=auto` in interactive shells, and the
    match is highlighted. Combined with `-C 3`, you see each match together with its
    surroundings.

!!! warning "`-r` doesn't follow symbolic links"
    `grep -r` skips links inside the directory. In `/etc/nginx/sites-enabled/`, all sites
    are links, so `grep -r` finds nothing there. Use `grep -R` or search
    `sites-available` instead.

!!! warning "Quote the pattern"
    Always put the pattern in single quotes: `grep -E 'a|b'`. Without quotes, the shell
    interprets characters like `|`, `*` or `$` itself, before `grep` sees them.

## Related commands

[cut](cut.md) · [wc](wc.md) · [less](../04-viewing-files/less.md) · [sed](sed.md)
