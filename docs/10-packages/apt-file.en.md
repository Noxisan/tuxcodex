# apt-file

> Searches all packages in the Debian and Ubuntu repositories for a file, also packages that are not installed. Answers the question: which package do I need for this command?

![apt-file output](../assets/screenshots/10-packages/apt-file.png)

## Syntax

```bash
apt-file [OPTION]... COMMAND PATTERN
```

## Options

| Option | Description |
|--------|-------------|
| `update` | Download the file lists of the repositories |
| `search PATTERN` | Find packages that contain a file matching `PATTERN` |
| `list PACKAGE` | List the files of a package, also if it isn't installed |
| `-x`, `--regexp` | Treat the pattern as a regular expression |

## Examples

**Find out which package contains a command:**

```bash
apt-file search --regexp "/usr/bin/dig$"
```

```text
bind9-dnsutils: /usr/bin/dig
```

`dig` is missing on the server? Install it with `sudo apt install bind9-dnsutils`.

**Download the file lists first:**

```bash
sudo apt-file update
```

```text
Hit:1 http://deb.debian.org/debian trixie InRelease
Hit:2 http://deb.debian.org/debian trixie-updates InRelease
Hit:3 http://deb.debian.org/debian-security trixie-security InRelease
Get:4 http://deb.debian.org/debian trixie/main amd64 Contents (deb) [12.7 MB]
Get:5 http://deb.debian.org/debian trixie/main all Contents (deb) [38.2 MB]
Get:6 http://deb.debian.org/debian trixie-updates/main all Contents (deb) [9071 B]
Fetched 50.9 MB in 4s (12.2 MB/s)
Reading package lists...
```

**Search for several commands at once:**

```bash
apt-file search -x "bin/(ip|ss)$"
```

```text
iproute2: /usr/bin/ip
iproute2: /usr/bin/ss
iproute2: /usr/sbin/ip
```

**List the files of a package that isn't installed:**

```bash
apt-file list htop
```

```text
htop: /usr/bin/htop
htop: /usr/share/applications/htop.desktop
htop: /usr/share/doc/htop/AUTHORS
htop: /usr/share/doc/htop/README.md.gz
htop: /usr/share/doc/htop/changelog.Debian.gz
```

## When do I need it?

- When a command is missing and you don't know which package provides it
- When software needs a library or header file, for example during a build
- To see what a package would install before you install it

!!! tip "Search exactly"
    Without `--regexp`, `apt-file search bin/dig` also finds `digikam`, `digitemp` and
    many more. With a full path and `$` at the end, you get exactly the file you are
    looking for.

!!! warning "Not installed by default"
    Install it with `sudo apt install apt-file` and run `sudo apt-file update` once. The
    file lists are about 50 MB in size.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Which package provides a file? | `apt-file search` | `apt-file search` | `dnf provides '*/bin/dig'` | `pacman -F dig` (after `pacman -Fy`) |

## Related commands

[apt](apt.md) · [dpkg](dpkg.md) · [which](../02-navigation/which.md)
