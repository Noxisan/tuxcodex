# locate

> Findet Dateien anhand ihres Namens in Sekundenbruchteilen, über eine Datenbank aller Dateinamen statt einer Suche auf der Platte.

![locate output](../assets/screenshots/02-navigation/locate.png)

## Syntax

```bash
locate [OPTION]... MUSTER...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-i`, `--ignore-case` | Groß- und Kleinschreibung ignorieren |
| `-b`, `--basename` | Nur den Dateinamen vergleichen, nicht die Verzeichnisse im Pfad |
| `-c`, `--count` | Nur die Anzahl der Treffer ausgeben |
| `-l`, `--limit N` | Nach `N` Treffern aufhören |
| `-e`, `--existing` | Nur Dateien zeigen, die jetzt noch existieren |
| `-r`, `--regexp` | Muster als regulären Ausdruck behandeln |

Die Datenbank aktualisierst du mit `sudo updatedb`.

## Beispiele

**Eine Datei anhand ihres Namens finden:**

```bash
locate backup.sh
```

```text
/home/nox/scripts/backup.sh
```

**Alle Pfade finden, die einen Namen enthalten:**

```bash
locate sshd_config
```

```text
/etc/ssh/sshd_config
/etc/ssh/sshd_config.d
/usr/share/man/man5/sshd_config.5.gz
/usr/share/openssh/sshd_config
/usr/share/openssh/sshd_config.md5sum
```

**Nur Dateien mit genau diesem Namen finden:**

```bash
locate -b -r '^sshd_config$'
```

```text
/etc/ssh/sshd_config
/usr/share/openssh/sshd_config
```

**Ohne Unterscheidung von Groß- und Kleinschreibung suchen:**

```bash
locate -i NOTES
```

```text
/home/nox/notes.txt
```

**Die Treffer zählen:**

```bash
locate -c "*.conf"
```

```text
312
```

**Eine gerade angelegte Datei finden:**

```bash
sudo updatedb
locate report.pdf
```

```text
/home/nox/report.pdf
```

## Wann brauche ich das?

- Wenn du einen Dateinamen kennst, aber keine Ahnung hast, wo die Datei im System liegt
- Um Konfigurationsdateien, Manpages oder Beispieldateien eines Pakets schnell zu finden
- Wenn [`find /`](find.md) auf einem großen Dateisystem zu lange dauern würde

!!! tip "Nur Dateien, die du sehen darfst"
    `locate` zeigt nur Dateien in Verzeichnissen, auf die du Zugriff hast. Mit `sudo`
    findest du auch Dateien an geschützten Orten wie `/root`.

!!! warning "Die Datenbank ist nicht immer aktuell"
    Die Datenbank wird einmal am Tag aktualisiert. Seitdem angelegte Dateien fehlen,
    gelöschte tauchen noch auf. Führe vor der Suche nach neuen Dateien `sudo updatedb`
    aus, oder blende mit `locate -e` Dateien aus, die es nicht mehr gibt.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| Paket | `plocate` (nicht immer installiert) | `plocate` (nicht vorinstalliert) |
| Datenbank | wird bei der Installation angelegt | entsteht beim ersten `sudo updatedb` |
| Tägliche Aktualisierung | Timer automatisch aktiv | Timer selbst aktivieren |

Installation unter Debian:

```bash
sudo apt install plocate
```

Tägliche Aktualisierung unter Arch aktivieren:

```bash
sudo systemctl enable --now plocate-updatedb.timer
```

## Verwandte Befehle

[find](find.md) · [whereis](whereis.md)
