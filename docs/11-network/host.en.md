# host

> Looks up names and addresses in DNS and prints the answer in a short, readable form.

![host output](../assets/screenshots/11-network/host.png)

## Syntax

```bash
host [OPTION]... NAME [SERVER]
```

## Options

| Option | Description |
|--------|-------------|
| `-t TYPE` | Only this record type: `A`, `AAAA`, `MX`, `TXT`, `NS`, `SOA` |
| `-a` | All records, in a detailed form like `dig` |
| `-4`, `-6` | Ask the DNS server over IPv4 or IPv6 |
| `SERVER` | Ask this DNS server instead of the configured one |

## Examples

**Look up a name:**

```bash
host example.com
```

```text
example.com has address 198.51.100.7
example.com has IPv6 address 2001:db8:1::7
example.com mail is handled by 10 mail.example.com.
```

Without a type, `host` shows the IPv4 and IPv6 addresses and the mail server in one go.

**Find the name of an IP address:**

```bash
host 192.0.2.10
```

```text
10.2.0.192.in-addr.arpa domain name pointer tuxdex-srv.example.com.
```

**Show the TXT records, for example SPF:**

```bash
host -t TXT example.com
```

```text
example.com descriptive text "v=spf1 mx -all"
```

**Ask a specific DNS server:**

```bash
host example.com 198.51.100.53
```

```text
Using domain server:
Name: 198.51.100.53
Address: 198.51.100.53#53
Aliases:

example.com has address 198.51.100.7
example.com has IPv6 address 2001:db8:1::7
example.com mail is handled by 10 mail.example.com.
```

**A name that doesn't exist:**

```bash
host nosuch.example.com
```

```text
Host nosuch.example.com not found: 3(NXDOMAIN)
```

## When do I need it?

- For a quick check whether a name resolves and to which address
- To check the reverse entry (PTR) of a mail server, which many receivers require
- When `dig` gives you more detail than you need

!!! tip "PTR records for mail servers"
    Mail servers without a matching reverse entry are often rejected as spam. `host` with
    the server's IP address must return its host name, and that name must point back to
    the same address.

!!! warning "`host` ignores `/etc/hosts` too"
    Like `dig`, `host` only asks DNS. Use `getent hosts NAME` to see the result
    including `/etc/hosts`.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `bind9-host` | `bind9-host` (installed) | `bind-utils` | `bind` |

## Related commands

[dig](dig.md) · [resolvectl](resolvectl.md) · [getent](../07-users-groups/getent.md)
