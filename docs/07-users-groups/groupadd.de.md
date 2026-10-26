# groupadd

> Legt eine neue Gruppe mit einem einzigen Befehl an, das Low-Level-Werkzeug, das auf jeder Distribution gleich funktioniert.

![groupadd output](../assets/screenshots/07-users-groups/groupadd.png)

## Syntax

```bash
groupadd [OPTION]... GRUPPE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-g GID`, `--gid` | Diese GID verwenden |
| `-r`, `--system` | Eine Systemgruppe (GID unter 1000) anlegen |
| `-f`, `--force` | Kein Fehler, wenn die Gruppe schon existiert |

## Beispiele

**Eine Gruppe anlegen:**

```bash
sudo groupadd developers
getent group developers
```

```text
developers:x:1005:
```

**Eine Gruppe mit fester GID anlegen:**

```bash
sudo groupadd -g 2000 backup-admins
getent group backup-admins
```

```text
backup-admins:x:2000:
```

**Eine Systemgruppe für einen Dienst anlegen:**

```bash
sudo groupadd -r myapp
getent group myapp
```

```text
myapp:x:996:
```

**Versuchen, eine Gruppe anzulegen, die schon existiert:**

```bash
sudo groupadd developers
```

```text
groupadd: group 'developers' already exists
```

**Eine vorhandene Gruppe in einem Skript ignorieren:**

```bash
sudo groupadd -f developers
echo $?
```

```text
0
```

## Wann brauche ich das?

- In Skripten und Automatisierung, die auf beliebigen Distributionen Gruppen anlegen
- Um Gruppen mit derselben GID auf mehreren Servern anzulegen, etwa für NFS-Freigaben
- Um Systemgruppen für Dienste anzulegen

!!! tip "Dieselbe GID auf jedem Server"
    Bei gemeinsamem Speicher wie NFS werden Rechte als Zahlen gespeichert. Lege solche
    Gruppen mit `-g` und derselben GID auf jedem Server an, sonst gehören die Dateien auf
    jeder Maschine einer anderen Gruppe.

!!! tip "Gruppen umbenennen oder löschen"
    `groupmod -n NEU ALT` benennt eine Gruppe um, `groupdel GRUPPE` löscht sie. Eine
    Gruppe, die noch primäre Gruppe eines Benutzers ist, lässt sich nicht löschen.

## Verwandte Befehle

[addgroup](addgroup.md) · [getent](getent.md)
