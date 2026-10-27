# crontab

> Zeigt und bearbeitet die Cronjobs eines Benutzers: Befehle, die regelmäßig zu festen Zeiten laufen.

![crontab output](../assets/screenshots/16-scheduling/crontab.png)

## Syntax

```bash
crontab [OPTION]... [DATEI]
```

Die Zeitsyntax mit ihren fünf Feldern erklären die [Grundlagen](basics.md).

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-l` | Die Crontab anzeigen |
| `-e` | Die Crontab im Editor bearbeiten |
| `-r` | Die ganze Crontab löschen |
| `-u BENUTZER` | Die Crontab eines anderen Benutzers (root) |
| `DATEI`, `-` | Eine Crontab aus einer Datei oder der Standardeingabe installieren |

## Beispiele

**Die eigene Crontab anzeigen:**

```bash
crontab -l
```

```text
# m h dom mon dow command
*/5 * * * * /usr/local/bin/check-disk.sh
30 3 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```

**Ein Benutzer ohne Crontab:**

```bash
crontab -l -u alice
```

```text
no crontab for alice
```

**Die Crontab bearbeiten:**

```bash
crontab -e
```

```text
crontab: installing new crontab
```

Nach dem Speichern und Schließen des Editors ist die neue Crontab sofort aktiv.

**Ein Fehler in den Zeitfeldern:**

```bash
crontab -e
```

```text
crontab: installing new crontab
"/tmp/crontab.dIi22M/crontab":2: bad minute
errors in crontab file, can't install.
Do you want to retry the same edit? (y/n) y
```

`61` ist keine gültige Minute. `crontab` verweigert die fehlerhafte Fassung und lässt dich sie
korrigieren.

## Wann brauche ich das?

- Um ein Skript regelmäßig auszuführen, etwa jede Nacht ein Backup
- Um zu prüfen, welche Jobs ein Benutzer eingeplant hat
- Wenn ein Job nicht läuft: Steht die Zeile da, und ist sie richtig?

!!! tip "Den Editor wählen"
    `crontab -e` nutzt den Editor aus `$EDITOR`. Mit `EDITOR=nano crontab -e` wählst du ihn für
    diesen einen Aufruf.

!!! danger "`-r` löscht ohne Rückfrage"
    `-r` liegt auf der Tastatur direkt neben `-e` und löscht sofort die ganze Crontab. Sichere
    sie regelmäßig: `crontab -l > ~/crontab.backup`.

## Verwandte Befehle

[run-parts](run-parts.md) · [anacron](anacron.md) · [at](at.md) · [flock](flock.md)
