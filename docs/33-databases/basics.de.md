# Datenbanken verstehen

Die meisten Anwendungen speichern ihre Daten in einer relationalen Datenbank. Auf
Linux-Servern sind zwei davon überall zu finden: **PostgreSQL** und **MariaDB** (der
Community-Fork von MySQL; beide nutzen dieselben Befehle und dasselbe Protokoll).

## PostgreSQL oder MariaDB?

| | PostgreSQL | MariaDB / MySQL |
|---|------------|-----------------|
| Client | `psql` | `mariadb` (auch als `mysql` aufrufbar) |
| Port | 5432 | 3306 |
| Admin-Konto | Linux-Benutzer `postgres` | MariaDB-Benutzer `root`, als Linux-`root` |
| Typischer Einsatz | Anwendungen mit komplexen Daten, GIS, viele aktuelle Frameworks | Klassisches Webhosting, WordPress, Nextcloud, viele PHP-Anwendungen |
| Backup | [`pg_dump`](../28-backup/pg_dump.md) | [`mysqldump`](../28-backup/mysqldump.md) |

## Pakete und Pfade

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| PostgreSQL-Paket | `postgresql` (17 in Debian 13) | `postgresql` (16 in 24.04) | `postgresql-server` | `postgresql` |
| Erster Datenbank-Cluster | bei der Installation angelegt und gestartet | bei der Installation angelegt und gestartet | `sudo postgresql-setup --initdb`, dann aktivieren | `sudo -u postgres initdb -D /var/lib/postgres/data`, dann aktivieren |
| PostgreSQL-Konfiguration | `/etc/postgresql/17/main/` | `/etc/postgresql/16/main/` | `/var/lib/pgsql/data/` | `/var/lib/postgres/data/` |
| MariaDB-Paket | `mariadb-server` (11.8 in Debian 13) | `mariadb-server` (10.11 in 24.04) | `mariadb-server` | `mariadb` |
| Erster Start | automatisch bei der Installation | automatisch bei der Installation | `systemctl enable --now mariadb` | `sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`, dann aktivieren |
| MariaDB-Konfiguration | `/etc/mysql/mariadb.conf.d/50-server.cnf` | `/etc/mysql/mariadb.conf.d/50-server.cnf` | `/etc/my.cnf.d/mariadb-server.cnf` | `/etc/my.cnf.d/server.cnf` |

Die Dienste heißen überall `postgresql` und `mariadb`. Unter Debian und Ubuntu läuft
PostgreSQL in *Clustern* wie `17/main`; `pg_lsclusters` listet sie auf.

## Wie die Anmeldung funktioniert

Bei lokalen Verbindungen über den Socket vertrauen beide Server dem **Linux-Benutzer**. Der
Admin braucht deshalb kein Datenbank-Passwort:

| | Lokale Admin-Anmeldung | Wie |
|---|------------------------|-----|
| PostgreSQL | `sudo -u postgres psql` | Methode `peer`: Der Linux-Benutzer muss so heißen wie die Datenbankrolle |
| MariaDB | `sudo mariadb` | Plugin `unix_socket`: Linux-`root` ist MariaDB-`root` |

Anwendungen verbinden sich meist per TCP (`-h localhost`) mit einem **Passwort**. In
PostgreSQL entscheidet die Datei `pg_hba.conf`, welche Methode für welche Verbindung gilt:

```text
# TYPE  DATABASE  USER  ADDRESS        METHOD
local   all       all                  peer
host    all       all   127.0.0.1/32   scram-sha-256
host    shop      app   192.0.2.0/24   scram-sha-256
```

Die Regeln werden von oben nach unten gelesen; die erste passende Zeile gilt.

## Benutzer, Datenbanken und Rechte

Eine Anwendung, eine Datenbank, ein Benutzer mit Rechten nur auf diese Datenbank:

```text
# PostgreSQL
$ sudo -u postgres createuser --pwprompt app
$ sudo -u postgres createdb -O app shop

# MariaDB
$ sudo mariadb
MariaDB [(none)]> CREATE DATABASE wiki CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
MariaDB [(none)]> CREATE USER 'wiki'@'localhost' IDENTIFIED BY 'secret';
MariaDB [(none)]> GRANT ALL PRIVILEGES ON wiki.* TO 'wiki'@'localhost';
```

In MariaDB besteht ein Benutzer immer aus Name **und Host**: `'wiki'@'localhost'` und
`'wiki'@'192.0.2.%'` sind zwei verschiedene Benutzer mit eigenen Passwörtern und Rechten.

## Zugriff von anderen Rechnern

Standardmäßig lauschen beide Server nur auf `localhost`. Für Zugriff aus dem Netz:

| | Einstellung | Zusätzlich |
|---|-------------|------------|
| PostgreSQL | `listen_addresses = '*'` in `postgresql.conf` | eine `host`-Zeile in `pg_hba.conf`, dann `systemctl reload postgresql` |
| MariaDB | `bind-address = 0.0.0.0` in der Server-Konfiguration | ein Benutzer mit passendem Host wie `'report'@'192.0.2.%'` |

Nach einer Änderung an `listen_addresses` oder `bind-address` braucht der Dienst einen
Neustart. Das Ergebnis prüfst du mit [`ss -tlnp`](../11-network/ss.md).

!!! tip "Die Datenbank neben der Anwendung lassen"
    Läuft die Anwendung auf demselben Server, lass die Datenbank auf `localhost`. Dann ist
    der Port von außen gar nicht erreichbar, und du brauchst keine Firewall-Regel.

!!! warning "Ports nur für einzelne Adressen öffnen"
    Die Ports 5432 und 3306 dürfen nie aus dem Internet erreichbar sein. Erlaube sie in der
    Firewall nur für die Anwendungsserver, etwa mit
    [`ufw`](../11-network/ufw.md): `sudo ufw allow from 192.0.2.21 to any port 5432 proto tcp`.
