# addgroup

> Legt unter Debian eine neue Gruppe an oder fügt einen vorhandenen Benutzer einer Gruppe hinzu.

![addgroup output](../assets/screenshots/07-users-groups/addgroup.png)

## Syntax

```bash
addgroup [OPTION]... GRUPPE
addgroup BENUTZER GRUPPE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--system` | Eine Systemgruppe (GID unter 1000) für einen Dienst anlegen |
| `--gid ID` | Diese GID verwenden |
| `--verbose` | Jeden Schritt anzeigen |

## Beispiele

**Eine Gruppe anlegen und jeden Schritt anzeigen:**

```bash
sudo addgroup --verbose developers
```

```text
info: Selecting GID from range 1000 to 59999 ...
info: Adding group `developers' (GID 1005) ...
```

**Die neue Gruppe prüfen:**

```bash
getent group developers
```

```text
developers:x:1005:
```

Die Gruppe existiert, hat aber noch keine Mitglieder.

**Einen Benutzer der Gruppe hinzufügen:**

```bash
sudo addgroup alice developers
getent group developers
```

```text
developers:x:1005:alice
```

**Eine Systemgruppe für einen Dienst anlegen:**

```bash
sudo addgroup --system myapp
getent group myapp
```

```text
myapp:x:108:
```

**Versuchen, eine Gruppe anzulegen, die schon existiert:**

```bash
sudo addgroup developers
```

```text
fatal: The group `developers' already exists.
```

## Wann brauche ich das?

- Um eine Teamgruppe für ein gemeinsames Verzeichnis anzulegen, etwa `developers` oder `deploy`
- Um eine Gruppe für einen Dienst anzulegen, die sich mehrere Benutzer oder Dienste teilen
- Um einen Benutzer mit den Debian-Werkzeugen einer Gruppe hinzuzufügen

!!! tip "Dasselbe wie `adduser BENUTZER GRUPPE`"
    `addgroup alice developers` und `adduser alice developers` machen genau dasselbe. Nimm
    das, was du dir leichter merkst.

!!! warning "Mitglieder brauchen eine neue Anmeldung"
    Ein Benutzer, der einer Gruppe hinzugefügt wurde, bekommt die neuen Rechte erst in
    einer neuen Sitzung. Melde dich ab und wieder an oder öffne eine neue SSH-Verbindung.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| `addgroup` | installiert | nicht vorhanden |
| Alternative | `groupadd` | `groupadd developers`, `gpasswd -a alice developers` |

## Verwandte Befehle

[adduser](adduser.md) · [getent](getent.md)
