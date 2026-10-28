# pg_isready

> Prüft, ob ein PostgreSQL-Server Verbindungen annimmt, und meldet es als Exit-Code: ideal für Skripte und Monitoring.

![pg_isready output](../assets/screenshots/33-databases/pg_isready.png)

## Syntax

```bash
pg_isready [-h HOST] [-p PORT] [-d DB] [-U BENUTZER] [-t SEKUNDEN] [-q]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-h HOST`, `-p PORT` | Server und Port, Standard lokaler Socket und 5432 |
| `-d DB`, `-U BENUTZER` | Datenbank und Rolle für die Prüfung (nur fürs Log) |
| `-t SEKUNDEN` | Zeitlimit, Standard 3 |
| `-q` | Keine Ausgabe, nur der Exit-Code |

Exit-Codes: `0` nimmt Verbindungen an, `1` lehnt ab (z. B. beim Starten), `2` keine Antwort, `3` kein Versuch (falsche Parameter). `pg_isready` meldet sich nicht an und braucht deshalb kein Passwort.

## Beispiele

**Ist der lokale Server bereit:**

```bash
pg_isready
```

```text
/var/run/postgresql:5432 - accepting connections
```

**Einen Server über das Netz prüfen:**

```bash
pg_isready -h 192.0.2.22 -p 5432
```

```text
192.0.2.22:5432 - accepting connections
```

**Der Server ist gestoppt:**

```bash
pg_isready; echo $?
```

```text
/var/run/postgresql:5432 - no response
2
```

**Still, für Skripte:**

```bash
pg_isready -q && echo ok || echo down
```

```text
ok
```

## Wann brauche ich das?

- In Skripten, die warten müssen, bis die Datenbank läuft, z. B. nach einem Neustart
- Als Health Check in Docker Compose oder einem Monitoring-System
- Um von einem Anwendungsserver aus schnell zu prüfen, ob die Datenbank erreichbar ist

!!! tip "Auf die Datenbank warten"
    `until pg_isready -q -h db01; do sleep 1; done` wartet in einem Deploy-Skript, bis die
    Datenbank Verbindungen annimmt, und startet erst dann die Migration.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `postgresql-client` | `postgresql-client` | `postgresql` | `postgresql-libs` |

## Verwandte Befehle

[psql](psql.md) · [pg_lsclusters](pg_lsclusters.md) · [systemctl](../09-systemd/systemctl.md) · [docker compose](../19-docker/docker-compose.md)
