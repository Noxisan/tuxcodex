# delgroup

> Löscht unter Debian eine Gruppe oder entfernt einen Benutzer aus einer Gruppe.

![delgroup output](../assets/screenshots/07-users-groups/delgroup.png)

## Syntax

```bash
delgroup [OPTION]... GRUPPE
delgroup BENUTZER GRUPPE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--only-if-empty` | Die Gruppe nur löschen, wenn sie keine Mitglieder hat |
| `--system` | Die Gruppe nur löschen, wenn sie eine Systemgruppe ist |
| `--verbose` | Jeden Schritt anzeigen |

## Beispiele

**Eine Gruppe löschen:**

```bash
sudo delgroup --verbose developers
```

```text
info: Removing group `developers' ...
```

**Eine Gruppe nur löschen, wenn niemand darin ist:**

```bash
sudo delgroup --only-if-empty developers
```

```text
fatal: The group `developers' is not empty!
```

Die Gruppe hat noch Mitglieder und bleibt bestehen.

**Einen Benutzer aus einer Gruppe entfernen:**

```bash
sudo delgroup alice developers
getent group developers
```

```text
developers:x:1005:bob,nox
```

**Prüfen, ob die Gruppe weg ist:**

```bash
getent group developers
echo $?
```

```text
2
```

## Wann brauche ich das?

- Um Team- oder Projektgruppen aufzuräumen, die nicht mehr gebraucht werden
- Um Gruppen deinstallierter Dienste zu entfernen
- Um einen Benutzer mit den Debian-Werkzeugen aus einer Gruppe zu entfernen

!!! tip "`--only-if-empty` beim Aufräumen"
    In Aufräumskripten verhindert `--only-if-empty`, dass du eine Gruppe löschst, die noch
    benutzt wird.

!!! warning "Dateien behalten die GID"
    Dateien, die der gelöschten Gruppe gehörten, behalten ihre GID. `ls -l` zeigt dann eine
    Zahl statt eines Namens. Finde sie vor dem Löschen mit
    `sudo find / -xdev -group developers`.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| `delgroup` | installiert | nicht vorhanden |
| Alternative | `groupdel` | `groupdel developers`, `gpasswd -d alice developers` |

## Verwandte Befehle

[addgroup](addgroup.md) · [gpasswd](gpasswd.md)
