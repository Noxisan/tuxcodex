# pg_dump

> Writes a consistent backup of a PostgreSQL database while it keeps running, as SQL or in a compressed archive format.

![pg_dump output](../assets/screenshots/28-backup/pg_dump.png)

## Syntax

```bash
pg_dump [OPTIONS] DATABASE
pg_restore [OPTIONS] -d DATABASE FILE
```

## Options

| Option | Description |
|--------|-------------|
| `-Fc` | Custom format: compressed, restore selectively with `pg_restore` |
| `-f FILE` | Write to a file instead of standard output |
| `-t TABLE` | Only this table |
| `--schema-only`, `--data-only` | Only the structure, or only the data |
| `-U USER`, `-h HOST` | Connect as another user, to another server |
| `pg_dumpall --globals-only` | Roles and tablespaces, which `pg_dump` doesn't include |
| `pg_restore -d DB FILE` | Restore a custom-format dump; `-l` lists its content |

## Examples

**Dump a database in custom format:**

```bash
sudo -u postgres pg_dump -Fc -f /var/backups/db/statusdb-$(date +%F).dump statusdb
ls -lh /var/backups/db/
```

```text
total 4.2M
-rw-r--r-- 1 postgres postgres 4.2M Oct 26 02:30 statusdb-2026-10-26.dump
```

**What's in the dump:**

```bash
pg_restore -l /var/backups/db/statusdb-2026-10-26.dump | head -12
```

```text
;
; Archive created at 2026-10-26 02:30:01 CET
;     dbname: statusdb
;     TOC Entries: 11
;     Compression: gzip
;     Dump Version: 1.16-0
;     Format: CUSTOM
;     Integer: 4 bytes
;     Offset: 8 bytes
;     Dumped from database version: 17.6 (Debian 17.6-0+deb13u1)
;     Dumped by pg_dump version: 17.6 (Debian 17.6-0+deb13u1)
;
```

**Restore into a test database:**

```bash
sudo -u postgres createdb statusdb_test
sudo -u postgres pg_restore -d statusdb_test /var/backups/db/statusdb-2026-10-26.dump
sudo -u postgres psql -tA statusdb_test -c 'SELECT count(*) FROM checks'
```

```text
5000
```

The restore test: the number of rows matches the production database.

**Also back up the roles:**

```bash
sudo -u postgres pg_dumpall --globals-only > /var/backups/db/globals.sql
grep -c 'CREATE ROLE' /var/backups/db/globals.sql
```

```text
3
```

## When do I need it?

- Every night before the file backup, so the dump is part of it
- Before an upgrade of PostgreSQL or the application
- To copy a database to a test or staging system

!!! tip "Custom format for backups"
    `-Fc` is compressed, and `pg_restore` can restore single tables or the schema from it.
    A plain SQL dump (`.sql`) is easier to read but can only be restored completely.

!!! warning "Roles aren't in the dump"
    `pg_dump` contains one database, not the users and their passwords. Back them up with
    `pg_dumpall --globals-only` as well, otherwise the restore fails with missing roles.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `postgresql-client` | `postgresql-client` | `postgresql` | `postgresql` |

## Related commands

[mysqldump](mysqldump.md) · [restic](restic.md) · [docker exec](../19-docker/docker-exec.md) · [crontab](../16-scheduling/crontab.md)
