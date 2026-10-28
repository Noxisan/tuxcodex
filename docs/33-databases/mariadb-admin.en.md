# mariadb-admin

> Administrative tasks for MariaDB and MySQL without SQL: check whether the server lives, show status, connections and variables.

![mariadb-admin output](../assets/screenshots/33-databases/mariadb-admin.png)

## Syntax

```bash
mariadb-admin [-u USER] [-p] [-h HOST] COMMAND...
```

## Options

| Command | Description |
|---------|-------------|
| `ping` | Is the server alive? Exit code `0` if yes |
| `status` | One line with uptime, threads, queries |
| `version` | Version, socket and status |
| `processlist` | Running connections and queries |
| `variables` | All server settings |
| `extended-status` | All status counters |
| `kill ID` | End a connection |
| `flush-privileges`, `reload` | Reload the user tables |

`mysqladmin` is an alias for `mariadb-admin`. On Debian and Ubuntu, `sudo mariadb-admin` logs in as `root` via the socket without a password.

## Examples

**Is the server alive:**

```bash
sudo mariadb-admin ping
```

```text
mysqld is alive
```

**Status in one line:**

```bash
sudo mariadb-admin status
```

```text
Uptime: 7834  Threads: 3  Questions: 18342  Slow queries: 0  Opens: 41  Open tables: 34  Queries per second avg: 2.341
```

**Version and connection:**

```bash
sudo mariadb-admin version
```

```text
mariadb-admin from 11.8.6-MariaDB, client 10.0 for debian-linux-gnu (x86_64)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Server version          11.8.6-MariaDB-0+deb13u1 from Debian
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /run/mysqld/mysqld.sock
Uptime:                 2 hours 10 min 34 sec

Threads: 3  Questions: 18342  Slow queries: 0  Opens: 41  Open tables: 34  Queries per second avg: 2.341
```

**Running connections:**

```bash
sudo mariadb-admin processlist
```

```text
+----+------+-----------+------+---------+------+----------+------------------+----------+
| Id | User | Host      | db   | Command | Time | State    | Info             | Progress |
+----+------+-----------+------+---------+------+----------+------------------+----------+
| 28 | wiki | localhost | wiki | Sleep   | 12   |          |                  | 0.000    |
| 29 | wiki | localhost | wiki | Sleep   | 3    |          |                  | 0.000    |
| 31 | root | localhost |      | Query   | 0    | starting | show processlist | 0.000    |
+----+------+-----------+------+---------+------+----------+------------------+----------+
```

**Selected settings:**

```bash
sudo mariadb-admin variables | grep -E '\| (bind_address|port|datadir|max_connections) ' | tr -s ' '
```

```text
| bind_address | 127.0.0.1 |
| datadir | /var/lib/mysql/ |
| max_connections | 151 |
| port | 3306 |
```

`bind_address 127.0.0.1`: the server is only reachable from the machine itself.

**The server doesn't run:**

```bash
sudo mariadb-admin ping
```

```text
mariadb-admin: connect to server at 'localhost' failed
error: 'Can't connect to local server through socket '/run/mysqld/mysqld.sock' (2)'
Check that mariadbd is running and that the socket: '/run/mysqld/mysqld.sock' exists!
```

## When do I need it?

- As a health check in scripts and monitoring (`ping`)
- To find out which settings the server really uses (`variables`)
- To spot a query that blocks everything (`processlist`, `kill`)

!!! tip "Watch the process list"
    `watch -n 2 sudo mariadb-admin processlist` shows every two seconds what the database is
    doing. Long `Time` values point to slow queries.

!!! warning "`shutdown` stops the server"
    `mariadb-admin shutdown` stops the server immediately, outside of systemd. Use
    `systemctl stop mariadb` instead, so systemd knows the state.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `mariadb-client` | `mariadb-client` | `mariadb` | `mariadb-clients` |

## Related commands

[mariadb](mariadb.md) · [mariadb-secure-installation](mariadb-secure-installation.md) · [systemctl](../09-systemd/systemctl.md) · [watch](../08-processes/watch.md)
