# mysqldump

> Schreibt ein Backup von MySQL- und MariaDB-Datenbanken als SQL; unter MariaDB heißt dasselbe Werkzeug auch mariadb-dump.

![mysqldump output](../assets/screenshots/28-backup/mysqldump.png)

## Syntax

```bash
mysqldump [OPTIONEN] DATENBANK [TABELLE...]
mysqldump [OPTIONEN] --all-databases
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--single-transaction` | Konsistenter Dump von InnoDB-Tabellen, ohne sie zu sperren |
| `--all-databases` | Alle Datenbanken, auch die Benutzertabellen in `mysql` |
| `--routines`, `--events`, `--triggers` | Auch gespeicherte Prozeduren, geplante Events und Trigger |
| `--no-data` | Nur die Tabellenstruktur |
| `-u BENUTZER`, `-p`, `-h HOST` | Verbindung; Zugangsdaten besser in `~/.my.cnf` |
| `--result-file=DATEI` | In eine Datei schreiben |

Zurückspielen mit `mysql DATENBANK < dump.sql` (unter MariaDB auch `mariadb`).

## Beispiele

**Eine Datenbank komprimiert sichern:**

```bash
sudo mysqldump --single-transaction --routines shop | gzip > /var/backups/db/shop-$(date +%F).sql.gz
ls -lh /var/backups/db/shop-*
```

```text
-rw-r--r-- 1 root root 1.8M Oct 26 02:31 /var/backups/db/shop-2026-10-26.sql.gz
```

**Der Anfang eines Dumps:**

```bash
zcat /var/backups/db/shop-2026-10-26.sql.gz | head -6
```

```text
/*M!999999\- enable the sandbox mode */
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: shop
-- ------------------------------------------------------
-- Server version  11.8.3-MariaDB-0+deb13u1 from Debian
```

**Alle Datenbanken mit Benutzern und Routinen:**

```bash
sudo mysqldump --all-databases --single-transaction --routines --events | gzip > /var/backups/db/all-$(date +%F).sql.gz
ls -lh /var/backups/db/all-*
```

```text
-rw-r--r-- 1 root root 2.4M Oct 26 02:32 /var/backups/db/all-2026-10-26.sql.gz
```

**In eine Testdatenbank zurückspielen:**

```bash
sudo mysql -e 'CREATE DATABASE shop_test'
zcat /var/backups/db/shop-2026-10-26.sql.gz | sudo mysql shop_test
sudo mysql -e 'SELECT count(*) FROM shop_test.orders'
```

```text
count(*)
2
```

## Wann brauche ich das?

- Jede Nacht vor dem Datei-Backup, damit der Dump darin enthalten ist
- Vor Updates des Datenbankservers oder einer Webanwendung wie WordPress oder Nextcloud
- Um eine Datenbank auf einen anderen Server umzuziehen

!!! tip "Kein Passwort auf der Kommandozeile"
    Mit `-pGEHEIM` taucht das Passwort in `ps` und der Shell-History auf. Leg es in
    `/root/.my.cnf` mit den Rechten `600` ab (`[client]`, `user=`, `password=`), dann brauchen
    `mysqldump` und `mysql` keine Optionen.

!!! warning "Ohne --single-transaction"
    Ohne diese Option kann ein Dump einer belebten Datenbank Tabellen aus verschiedenen
    Zeitpunkten enthalten oder sie für die Dauer des Dumps sperren. Nimm für InnoDB immer
    `--single-transaction`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Datenbankserver | MariaDB | MySQL oder MariaDB | MySQL oder MariaDB | MariaDB |
| Paket mit dem Werkzeug | `mariadb-client` | `mysql-client` oder `mariadb-client` | `mysql` oder `mariadb` | `mariadb-clients` |

## Verwandte Befehle

[pg_dump](pg_dump.md) · [borg](borg.md) · [gzip](../14-archives/gzip.md) · [crontab](../16-scheduling/crontab.md)
