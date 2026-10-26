# hostname

> Shows (or temporarily sets) the name of the machine you are on.

## Syntax

```bash
hostname [OPTION]... [NAME]
```

## Options

| Option | Description |
|--------|-------------|
| `-s`, `--short` | Print the short host name (cut at the first dot) |
| `-f`, `--fqdn`, `--long` | Print the fully qualified domain name (FQDN) |
| `-d`, `--domain` | Print the DNS domain name |
| `-I`, `--all-ip-addresses` | Print all configured IP addresses (no loopback, no IPv6 link-local) |
| `-i`, `--ip-address` | Print the address(es) the host name resolves to |
| `-A`, `--all-fqdns` | Print the FQDNs of all configured addresses |
| `-F`, `--file FILE` | Read the host name to set from `FILE` |

## Examples

**Show the host name:**

```bash
hostname
```

```text
tuxcodex-srv
```

**Show the fully qualified domain name:**

```bash
hostname -f
```

```text
tuxcodex-srv.example.com
```

**Show all IP addresses of the server:**

```bash
hostname -I
```

```text
192.0.2.10 2001:db8::10
```

**Show the address the host name resolves to:**

```bash
hostname -i
```

```text
127.0.1.1
```

**Set the host name until the next reboot:**

```bash
sudo hostname test-srv
hostname
```

```text
test-srv
```

<!-- SCREENSHOT: assets/screenshots/01-orientation/hostname.png -->

## When do I need it?

- To make sure you are on the right server before you change anything
- To quickly get the server's IP addresses with `hostname -I` without reading through
  the output of `ip address`
- To check that the FQDN is set correctly, which mail servers, certificates and some
  monitoring agents rely on
- In scripts and log messages that should include the machine name

!!! tip "Quick IP lookup"
    `hostname -I` is the fastest way to find out a server's addresses, for example
    when you are logged in on the console and need the IP for SSH.

!!! warning "`-i` shows `127.0.1.1` on Debian"
    `hostname -i` only resolves the host name, and Debian maps it to `127.0.1.1` in
    `/etc/hosts`. Use `hostname -I` for the real addresses.

!!! warning "Changes are not permanent"
    `hostname NAME` changes the name only until the next reboot. To change it
    permanently, use `hostnamectl hostname NAME` and adjust the entry in `/etc/hosts`.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| Package | `hostname` (always installed) | `inetutils` (not always installed) |
| `-I`, `-A` | available | not available |

On Arch, `hostname` may be missing on minimal systems. Use `hostnamectl` or
`cat /etc/hostname` instead, and `ip -brief address` for the IP addresses.

## Related commands

[hostnamectl](hostnamectl.md) · [uname](uname.md) · [whoami](whoami.md) · [id](id.md)
