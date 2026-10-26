# visudo

> Bearbeitet die `sudo`-Konfiguration sicher: sperrt die Datei und prüft die Syntax vor dem Speichern.

![visudo output](../assets/screenshots/07-users-groups/visudo.png)

## Syntax

```bash
visudo [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | `/etc/sudoers` bearbeiten |
| `-f DATEI` | Eine andere Datei bearbeiten, z. B. in `/etc/sudoers.d/` |
| `-c`, `--check` | Nur die Syntax prüfen, nicht bearbeiten |
| `-s`, `--strict` | Strenge Prüfung, warnt auch vor ungenutzten Aliasen und ähnlichen Fehlern |

Eine Regel im `sudoers`-Format:

```text
deploy ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx
  │     │    │       │        └ erlaubter Befehl (mit vollem Pfad)
  │     │    │       └ kein Passwort nötig
  │     │    └ als welcher Benutzer
  │     └ auf welchen Hosts
  └ Benutzer (oder %gruppe)
```

## Beispiele

**Die Hauptkonfiguration bearbeiten:**

```bash
sudo visudo
```

```text
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
```

`visudo` öffnet `/etc/sudoers` in dem Editor aus `$EDITOR` (oder dem Systemstandard).

**Eine eigene Regel als separate Datei anlegen:**

```bash
sudo visudo -f /etc/sudoers.d/deploy
sudo cat /etc/sudoers.d/deploy
```

```text
deploy ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx
```

Diese Zeile erlaubt dem Benutzer `deploy`, nginx ohne Passwort neu zu starten, und sonst
nichts.

**Alle `sudo`-Dateien prüfen:**

```bash
sudo visudo -c
```

```text
/etc/sudoers: parsed OK
/etc/sudoers.d/README: parsed OK
/etc/sudoers.d/deploy: parsed OK
```

**Eine Regel mit Syntaxfehler:**

```bash
sudo visudo -c -f /etc/sudoers.d/deploy
```

```text
/etc/sudoers.d/deploy:1:60: syntax error
deploy ALL=(root) NOPASSWD /usr/bin/systemctl restart nginx
                                                           ^
```

Hinter `NOPASSWD` fehlt der Doppelpunkt. Speicherst du im Editor eine Datei mit Fehler,
fragt `visudo` `What now?`: `e` bearbeitet erneut, `x` beendet ohne zu speichern.

**Einen anderen Editor verwenden:**

```bash
sudo EDITOR=nano visudo
```

```text
#
# This file MUST be edited with the 'visudo' command as root.
```

## Wann brauche ich das?

- Um einem Benutzer oder einer Gruppe `sudo`-Rechte zu geben
- Um einem Deploy- oder Monitoring-Benutzer genau einen oder zwei Befehle ohne Passwort zu
  erlauben
- Um die Konfiguration nach Änderungen oder nach dem Kopieren von Dateien nach
  `/etc/sudoers.d/` zu prüfen

!!! tip "Eigene Regeln in `/etc/sudoers.d/`"
    Ändere nicht `/etc/sudoers` selbst. Leg deine Regeln in eigenen Dateien in
    `/etc/sudoers.d/` ab. Paket-Updates überschreiben sie dann nie, und eine einzelne Datei
    lässt sich leicht wieder entfernen.

!!! warning "Dateinamen in `/etc/sudoers.d/`"
    Dateien, deren Name einen `.` enthält oder auf `~` endet, werden ignoriert, zum
    Beispiel `deploy.conf`. Nimm Namen ohne Punkt, wie `deploy`.

!!! danger "`/etc/sudoers` nie mit einem normalen Editor bearbeiten"
    Ein Syntaxfehler in `/etc/sudoers` legt `sudo` komplett lahm, und ohne Root-Passwort
    kannst du es nicht mehr reparieren. `visudo` weigert sich, eine kaputte Datei zu
    speichern.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Admin-Regel in `/etc/sudoers` | `%sudo ALL=(ALL:ALL) ALL` | `%sudo ALL=(ALL:ALL) ALL` | `%wheel ALL=(ALL) ALL` | `%wheel ALL=(ALL:ALL) ALL`, auskommentiert |
| Standard-Editor | `nano` (über `editor`) | `nano` (über `editor`) | `vi` | `vi` |

## Verwandte Befehle

[sudo](sudo.md) · [su](su.md)
