# ssh-keyscan

> Fetches the public host keys of SSH servers without logging in. Useful to check fingerprints and to fill `known_hosts` in advance.

![ssh-keyscan output](../assets/screenshots/12-ssh/ssh-keyscan.png)

## Syntax

```bash
ssh-keyscan [OPTION]... HOST...
```

## Options

| Option | Description |
|--------|-------------|
| `-t TYPE` | Only this key type, e.g. `ed25519` |
| `-p PORT` | SSH port of the server |
| `-H` | Hash the host names, like `known_hosts` usually does |
| `-T SECONDS` | Timeout per host |

## Examples

**Fetch the host key of a server:**

```bash
ssh-keyscan -t ed25519 192.0.2.10
```

```text
# 192.0.2.10:22 SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
192.0.2.10 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFgCVsGZOlwwWrxgxW+pqtbBN5Au8Sc1XK8G0B0nzz2N
```

The line starting with `#` comes from standard error and shows the SSH version of the
server. The second line has the format of `known_hosts`.

**Show the fingerprint of the host key:**

```bash
ssh-keyscan -t ed25519 192.0.2.10 2>/dev/null | ssh-keygen -lf -
```

```text
256 SHA256:3qrz2WaaPN7BZOUbSTXHRndWQcm8gTxZgtaniXKLSGs 192.0.2.10 (ED25519)
```

Compare it with the fingerprint SSH shows on the first connection, or with the one the
administrator of the server tells you.

**Add a server to `known_hosts` in advance:**

```bash
ssh-keyscan -H -t ed25519 192.0.2.10 >> ~/.ssh/known_hosts
```

```text
# 192.0.2.10:22 SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
```

Only the comment line ends up on the screen, the key goes into the file. After that,
the first connection no longer asks.

**Check the SSH versions of several servers:**

```bash
ssh-keyscan 192.0.2.10 192.0.2.20 198.51.100.7 2>&1 >/dev/null | sort -u
```

```text
# 192.0.2.10:22 SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
# 192.0.2.20:22 SSH-2.0-OpenSSH_9.9
# 198.51.100.7:22 SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.14
```

## When do I need it?

- Before the first connection, to compare the fingerprint over a second, trusted way
- In automation, to add new servers to `known_hosts` without a question
- To get a quick overview of the SSH versions in a network

!!! tip "Check fingerprints on the server"
    On the server itself, `ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub` shows the
    real fingerprint. If it matches the fetched one, nobody sits in between.

!!! warning "`ssh-keyscan` trusts the network"
    The tool takes whatever key the network delivers. Adding keys blindly with
    `ssh-keyscan >> known_hosts` skips exactly the check that protects you from
    man-in-the-middle attacks. Compare the fingerprint at least once.

## Related commands

[ssh-keygen](ssh-keygen.md) · [ssh](ssh.md) · [sshd](sshd.md)
