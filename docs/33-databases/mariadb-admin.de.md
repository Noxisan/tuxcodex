# mariadb-admin

> Verwaltungsaufgaben für MariaDB und MySQL ohne SQL: prüfen, ob der Server lebt, Status, Verbindungen und Variablen anzeigen.

![mariadb-admin output](../assets/screenshots/33-databases/mariadb-admin.png)

## Syntax

```bash
mariadb-admin [-u BENUTZER] [-p] [-h HOST] BEFEHL...
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `ping` | Lebt der Server? Exit-Code `0`, wenn ja |
| `status` | Eine Zeile mit Laufzeit, Threads, Abfragen |
| `version` | Version, Socket und Status |
| `processlist` | Laufende Verbindungen und Abfragen |
| `variables` | Alle Server-Einstellungen |
| `extended-status` | Alle Statuszähler |
| `kill ID` | Eine Verbindung beenden |
| `flush-privileges`, `reload` | Die Benutzertabellen neu laden |

`mysqladmin` ist ein Alias für `mariadb-admin`. Unter Debian und Ubuntu meldet sich `sudo mariadb-admin` über den Socket ohne Passwort als `root` an.

## Beispiele

**Lebt der Server:**

```bash
sudo mariadb-admin ping
```

```text
mysqld is alive
```

**Status in einer Zeile:**

```bash
sudo mariadb-admin status
```

```text
Uptime: 7834  Threads: 3  Questions: 18342  Slow queries: 0  Opens: 41  Open tables: 34  Queries per second avg: 2.341
```

**Version und Verbindung:**

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

**Laufende Verbindungen:**

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

**Ausgewählte Einstellungen:**

```bash
sudo mariadb-admin variables | grep -E '\| (bind_address|port|datadir|max_connections) ' | tr -s ' '
```

```text
| bind_address | 127.0.0.1 |
| datadir | /var/lib/mysql/ |
| max_connections | 151 |
| port | 3306 |
```

`bind_address 127.0.0.1`: Der Server ist nur vom Rechner selbst aus erreichbar.

**Der Server läuft nicht:**

```bash
sudo mariadb-admin ping
```

```text
mariadb-admin: connect to server at 'localhost' failed
error: 'Can't connect to local server through socket '/run/mysqld/mysqld.sock' (2)'
Check that mariadbd is running and that the socket: '/run/mysqld/mysqld.sock' exists!
```

## Wann brauche ich das?

- Als Health Check in Skripten und im Monitoring (`ping`)
- Um herauszufinden, welche Einstellungen der Server wirklich nutzt (`variables`)
- Um eine Abfrage zu finden, die alles blockiert (`processlist`, `kill`)

!!! tip "Die Prozessliste beobachten"
    `watch -n 2 sudo mariadb-admin processlist` zeigt alle zwei Sekunden, was die Datenbank
    gerade tut. Lange `Time`-Werte deuten auf langsame Abfragen hin.

!!! warning "`shutdown` stoppt den Server"
    `mariadb-admin shutdown` stoppt den Server sofort, an systemd vorbei. Nimm stattdessen
    `systemctl stop mariadb`, damit systemd den Zustand kennt.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `mariadb-client` | `mariadb-client` | `mariadb` | `mariadb-clients` |

## Verwandte Befehle

[mariadb](mariadb.md) · [mariadb-secure-installation](mariadb-secure-installation.md) · [systemctl](../09-systemd/systemctl.md) · [watch](../08-processes/watch.md)
