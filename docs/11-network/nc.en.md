# nc

> Netcat: opens TCP or UDP connections by hand. Ideal to test whether a port is reachable, or to talk to a service directly.

![nc output](../assets/screenshots/11-network/nc.png)

## Syntax

```bash
nc [OPTION]... HOST PORT
nc -l [OPTION]... PORT
```

## Options

| Option | Description |
|--------|-------------|
| `-z` | Only test whether the port is open, send no data |
| `-v` | Report the result |
| `-w SECONDS` | Timeout for the connection |
| `-u` | UDP instead of TCP |
| `-l` | Listen on a port instead of connecting |
| `-N` | Close the connection after the input ends |

## Examples

**Test whether a port is reachable:**

```bash
nc -zv 192.0.2.20 5432
```

```text
Connection to 192.0.2.20 5432 port [tcp/postgresql] succeeded!
```

**Nothing listens on the port:**

```bash
nc -zv 192.0.2.20 5433
```

```text
nc: connect to 192.0.2.20 port 5433 (tcp) failed: Connection refused
```

`Connection refused` means: the host is reachable, but no program listens on this port.

**No answer at all:**

```bash
nc -zv -w 3 198.51.100.7 22
```

```text
nc: connect to 198.51.100.7 port 22 (tcp) timed out: Operation now in progress
```

A timeout usually means a firewall drops the packets on the way.

**Talk to a web server by hand:**

```bash
printf 'HEAD / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n' | nc example.com 80
```

```text
HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Mon, 26 Oct 2026 09:42:17 GMT
Content-Type: text/html
Content-Length: 162
Connection: close
Location: https://example.com/
```

**Test a connection between two servers:**

```bash
nc -l 9000
```

```text
hello from tuxcodex-srv
```

On the first server, `nc -l 9000` waits for a connection. On the second,
`echo "hello from tuxcodex-srv" | nc -N 192.0.2.10 9000` sends a line. If it arrives,
the way between the servers is open, including all firewalls.

## When do I need it?

- To find out whether a firewall blocks a port, before you search for the error in the
  service
- To check whether a database or a mail server can be reached from the application
  server
- To talk to text based protocols like HTTP or SMTP directly

!!! tip "Refused or timeout?"
    `Connection refused` comes back immediately: the way is open, but the service isn't
    running. A timeout after a few seconds points to a firewall.

!!! warning "Different `nc` variants"
    There are several implementations with different options and messages. The examples
    show the OpenBSD variant of Debian and Ubuntu. On RHEL, `nc` is Ncat from the nmap
    project, see the table.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `netcat-openbsd` | `netcat-openbsd` (installed) | `nmap-ncat` | `openbsd-netcat` |
| Port test | `nc -zv HOST PORT` | `nc -zv HOST PORT` | `nc -zv HOST PORT` (message `Connected to …`) | `nc -zv HOST PORT` |

## Related commands

[ss](ss.md) · [curl](curl.md) · [ping](ping.md)
