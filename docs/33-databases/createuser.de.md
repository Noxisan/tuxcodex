# createuser

> Legt eine neue PostgreSQL-Rolle (Benutzer) an, auf Wunsch mit Passwort und dem Recht, Datenbanken anzulegen.

![createuser output](../assets/screenshots/33-databases/createuser.png)

## Syntax

```bash
createuser [-P] [-d] [-r] [-s] [-e] ROLLE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-P`, `--pwprompt` | Nach einem Passwort für die neue Rolle fragen |
| `-d` | Die Rolle darf Datenbanken anlegen |
| `-r` | Die Rolle darf andere Rollen anlegen |
| `-s` | Superuser: darf alles |
| `-e` | Das SQL zeigen, das an den Server geht |
| `--interactive` | Nach den Rechten fragen statt Standardwerte zu nehmen |

`createuser` ist eine Hülle um `CREATE ROLE … LOGIN`. Führ es als Linux-Benutzer `postgres` aus: `sudo -u postgres createuser …`. Rollen löschst du mit `dropuser`.

## Beispiele

**Eine Rolle mit Passwort für eine Anwendung:**

```bash
sudo -u postgres createuser --pwprompt app
```

```text
Enter password for new role:
Enter it again:
```

**Zeigen, was an den Server geht:**

```bash
sudo -u postgres createuser -e nox
```

```text
SELECT pg_catalog.set_config('search_path', '', false);
CREATE ROLE nox NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT LOGIN NOREPLICATION NOBYPASSRLS;
```

Ohne Optionen darf sich die Rolle anmelden, aber keine Datenbanken oder Rollen anlegen.

**Eine Rolle, die Datenbanken anlegen darf:**

```bash
sudo -u postgres createuser -d -P shopadmin
```

```text
Enter password for new role:
Enter it again:
```

**Die Rolle gibt es schon:**

```bash
sudo -u postgres createuser app
```

```text
createuser: error: creation of new role failed: ERROR:  role "app" already exists
```

Ein neues Passwort für eine vorhandene Rolle setzt du mit `sudo -u postgres psql -c '\password app'`.

**Das Ergebnis prüfen:**

```bash
sudo -u postgres psql -c '\du'
```

```text
                             List of roles
 Role name |                         Attributes
-----------+------------------------------------------------------------
 app       |
 nox       |
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS
 shopadmin | Create DB

```

## Wann brauche ich das?

- Für jede neue Anwendung, die eine eigene Datenbank bekommt
- Um einer Kollegin oder einem Kollegen einen eigenen Zugang zu geben, passend zum Linux-Benutzernamen für `peer`

!!! tip "Eine Rolle pro Linux-Benutzer"
    Eine Rolle mit demselben Namen wie ein Linux-Benutzer (`sudo -u postgres createuser nox`)
    kann sich lokal ohne Passwort anmelden. `nox` tippt dann einfach `psql -d shop`.

!!! warning "Kein Superuser für Anwendungen"
    Eine Anwendung mit `-s` kann jede Datenbank lesen, alles löschen und über `COPY … PROGRAM`
    Programme auf dem Server starten. Anwendungen bekommen eine normale Rolle, der ihre eigene
    Datenbank gehört.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `postgresql-client` | `postgresql-client` | `postgresql` | `postgresql-libs` |

## Verwandte Befehle

[createdb](createdb.md) · [psql](psql.md) · [pg_isready](pg_isready.md) · [useradd](../07-users-groups/useradd.md)
