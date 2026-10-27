# debsums

> On Debian and Ubuntu: compares installed files with the checksums of their packages and reports changed files.

![debsums output](../assets/screenshots/23-security-scanning/debsums.png)

## Syntax

```bash
debsums [OPTIONS] [PACKAGE...]
```

## Options

| Option | Description |
|--------|-------------|
| (none) | Check all packages and show every file |
| `-s`, `--silent` | Only report errors |
| `-c`, `--changed` | Only list changed files |
| `-e`, `--config` | Only check configuration files |
| `-a`, `--all` | Also check configuration files (they are skipped by default) |
| `PACKAGE` | Only these packages |

On RHEL, `rpm -Va` does the same, on Arch `pacman -Qkk`.

## Examples

**Report only changed files:**

```bash
sudo debsums -s
```

```text
debsums: changed file /usr/bin/which.debianutils (from debianutils package)
```

A system program that differs from the package. Unless you changed it yourself, that's a serious finding.

**Configuration files changed by hand:**

```bash
sudo debsums -ce
```

```text
/etc/ssh/sshd_config
/etc/nginx/nginx.conf
/etc/default/rkhunter
```

**Check a single package:**

```bash
debsums coreutils | head -4
```

```text
/usr/bin/[                                                                    OK
/usr/bin/arch                                                                 OK
/usr/bin/b2sum                                                                OK
/usr/bin/base32                                                               OK
```

**The same on RHEL:**

```bash
sudo rpm -Va | grep -v '^.......T'
```

```text
S.5....T.  c /etc/ssh/sshd_config
S.5....T.    /usr/bin/which
```

`S` size, `5` checksum, `T` time changed; `c` marks configuration files.

## When do I need it?

- To check whether system programs were changed outside the package manager
- After an incident, as a quick check without a prepared database
- To find configuration files that were changed by hand (`-ce`)

!!! tip "No preparation needed"
    Unlike AIDE, debsums needs no database of its own: the checksums come with the packages.
    That makes it the first quick check on a server you just took over.

!!! warning "Same system, same risk"
    A rootkit with root rights can also fake the checksum files in `/var/lib/dpkg/info/`. For
    a reliable check, compare against freshly downloaded packages (`debsums --generate`) or
    check from a rescue system.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Command | `debsums` | `debsums` | `rpm -Va` (built in) | `pacman -Qkk` (built in) |

## Related commands

[aide](aide.md) · [rkhunter](rkhunter.md) · [dpkg](../10-packages/dpkg.md) · [rpm](../10-packages/rpm.md)
