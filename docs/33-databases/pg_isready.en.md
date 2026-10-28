# pg_isready

> Checks whether a PostgreSQL server accepts connections and reports it as an exit code: ideal for scripts and monitoring.

![pg_isready output](../assets/screenshots/33-databases/pg_isready.png)

## Syntax

```bash
pg_isready [-h HOST] [-p PORT] [-d DB] [-U USER] [-t SECONDS] [-q]
```

## Options

| Option | Description |
|--------|-------------|
| `-h HOST`, `-p PORT` | Server and port, default local socket and 5432 |
| `-d DB`, `-U USER` | Database and role for the check (only used in the log) |
| `-t SECONDS` | Timeout, default 3 |
| `-q` | No output, only the exit code |

Exit codes: `0` accepting connections, `1` rejecting (e.g. while starting), `2` no response, `3` no attempt (wrong parameters). `pg_isready` doesn't log in, so it needs no password.

## Examples

**Is the local server ready:**

```bash
pg_isready
```

```text
/var/run/postgresql:5432 - accepting connections
```

**Check a server over the network:**

```bash
pg_isready -h 192.0.2.22 -p 5432
```

```text
192.0.2.22:5432 - accepting connections
```

**The server is stopped:**

```bash
pg_isready; echo $?
```

```text
/var/run/postgresql:5432 - no response
2
```

**Silent, for scripts:**

```bash
pg_isready -q && echo ok || echo down
```

```text
ok
```

## When do I need it?

- In scripts that must wait until the database is up, e.g. after a restart
- As a health check in Docker Compose or a monitoring system
- To check quickly from an application server whether the database is reachable

!!! tip "Wait for the database"
    `until pg_isready -q -h db01; do sleep 1; done` waits in a deploy script until the database
    accepts connections, and only then starts the migration.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `postgresql-client` | `postgresql-client` | `postgresql` | `postgresql-libs` |

## Related commands

[psql](psql.md) · [pg_lsclusters](pg_lsclusters.md) · [systemctl](../09-systemd/systemctl.md) · [docker compose](../19-docker/docker-compose.md)
