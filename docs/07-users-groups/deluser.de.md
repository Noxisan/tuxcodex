# deluser

> Löscht unter Debian einen Benutzer, auf Wunsch samt Home-Verzeichnis, oder entfernt einen Benutzer aus einer Gruppe.

![deluser output](../assets/screenshots/07-users-groups/deluser.png)

## Syntax

```bash
deluser [OPTION]... BENUTZER
deluser BENUTZER GRUPPE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--remove-home` | Auch das Home-Verzeichnis und den Mail-Spool löschen |
| `--remove-all-files` | **Alle** Dateien des Benutzers im System löschen |
| `--backup` | Die Dateien vor dem Löschen in einem Archiv sichern |
| `--backup-to VERZ` | Verzeichnis für das Sicherungsarchiv |
| `--system` | Den Benutzer nur löschen, wenn er ein Systembenutzer ist |
| `--verbose` | Jeden Schritt anzeigen |

## Beispiele

**Einen Benutzer löschen, das Home-Verzeichnis behalten:**

```bash
sudo deluser --verbose alice
```

```text
info: Removing crontab ...
info: Removing user `alice' ...
```

`/home/alice` bleibt erhalten, so kannst du noch Dateien daraus sichern.

**Einen Benutzer samt Home-Verzeichnis löschen:**

```bash
sudo deluser --verbose --remove-home bob
```

```text
info: Looking for files to backup/remove ...
info: Removing files ...
info: Removing crontab ...
info: Removing user `bob' ...
```

**Einen Benutzer aus einer Gruppe entfernen:**

```bash
sudo deluser alice docker
groups alice
```

```text
alice : alice users sudo
```

Der Benutzer bleibt, nur die Mitgliedschaft in `docker` wird entfernt.

**Versuchen, einen Benutzer aus seiner primären Gruppe zu entfernen:**

```bash
sudo deluser alice alice
```

```text
fatal: You may not remove the user from their primary group.
```

## Wann brauche ich das?

- Wenn jemand das Team verlässt und sein Konto entfernt werden muss
- Um Zugriffsrechte zu entziehen, zum Beispiel `sudo` oder `docker` (`deluser BENUTZER GRUPPE`)
- Um Test- oder befristete Konten aufzuräumen

!!! tip "Erst sperren, später löschen"
    Statt ein Konto sofort zu löschen, sperre es mit `chage -E 1 BENUTZER` und prüfe ein
    paar Wochen lang, ob noch etwas davon abhängt: Cronjobs, Dateien, Dienste.

!!! warning "Dateien außerhalb des Home-Verzeichnisses bleiben"
    Selbst mit `--remove-home` bleiben Dateien des Benutzers in `/srv`, `/var/www` oder
    `/tmp` erhalten. Sie gehören dann einer UID ohne Namen. Finde sie vor dem Löschen mit
    `find / -xdev -user alice`.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| `deluser` | installiert | nicht vorhanden |
| Alternative | `userdel`, `gpasswd -d` | `userdel -r alice`, `gpasswd -d alice docker` |

## Verwandte Befehle

[adduser](adduser.md) · [usermod](usermod.md) · [userdel](userdel.md)
