---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-shield-lock-outline:{ .tc-hero-icon }

# Rechte

Wer darf eine Datei lesen, ändern oder ausführen? Besitzer, Gruppen, Rechte, ACLs und
Attribute, und wie du herausfindest, warum etwas „Permission denied“ meldet.

</div>

## Grundrechte

<div class="grid cards" markdown>

-   :material-lock-open-variant-outline:{ .lg .middle } **[chmod](chmod.md)**

    ---

    Ändert Rechte als Zahl oder mit Buchstaben.

-   :material-account-key-outline:{ .lg .middle } **[chown](chown.md)**

    ---

    Ändert Besitzer und Gruppe von Dateien.

-   :material-account-group-outline:{ .lg .middle } **[chgrp](chgrp.md)**

    ---

    Ändert nur die Gruppe von Dateien.

-   :material-shield-account-outline:{ .lg .middle } **[umask](umask.md)**

    ---

    Legt die Standardrechte für neue Dateien fest.

</div>

## Fehlersuche

<div class="grid cards" markdown>

-   :material-folder-search-outline:{ .lg .middle } **[namei](namei.md)**

    ---

    Zeigt die Rechte jedes Verzeichnisses entlang eines Pfads.

</div>

## Zugriffslisten (ACLs)

<div class="grid cards" markdown>

-   :material-playlist-check:{ .lg .middle } **[getfacl](getfacl.md)**

    ---

    Zeigt zusätzliche Rechte für einzelne Benutzer und Gruppen.

-   :material-playlist-edit:{ .lg .middle } **[setfacl](setfacl.md)**

    ---

    Gibt einzelnen Benutzern oder Gruppen zusätzliche Rechte.

</div>

## Dateiattribute

<div class="grid cards" markdown>

-   :material-tag-search-outline:{ .lg .middle } **[lsattr](lsattr.md)**

    ---

    Zeigt besondere Attribute wie unveränderlich oder nur anhängen.

-   :material-tag-edit-outline:{ .lg .middle } **[chattr](chattr.md)**

    ---

    Schützt Dateien mit Attributen wie unveränderlich.

</div>

## Rechte verstehen

Jede Datei hat einen Besitzer, eine Gruppe und drei Sätze von Rechten. `ls -l` zeigt sie:

```text
-rwxr-x--- 1 nox www-data 1200 Oct 22 18:40 backup.sh
 └┬┘└┬┘└┬┘     │   │
  │  │  │      │   └ Gruppe
  │  │  │      └ Besitzer
  │  │  └ andere: keine Rechte
  │  └ Gruppe: lesen und ausführen
  └ Besitzer: lesen, schreiben und ausführen
```

| Recht | Bei einer Datei | Bei einem Verzeichnis | Wert |
|-------|-----------------|-----------------------|------|
| `r` lesen | Inhalt lesen | Namen der enthaltenen Dateien auflisten | 4 |
| `w` schreiben | Inhalt ändern | Dateien darin anlegen, umbenennen und löschen | 2 |
| `x` ausführen | Als Programm oder Skript starten | Mit `cd` betreten und auf Dateien darin zugreifen | 1 |

Die Werte werden pro Gruppe addiert: `rwx` = 4+2+1 = 7, `r-x` = 5, `r--` = 4.
Häufige Kombinationen:

| Zahl | Text | Typische Verwendung |
|------|------|---------------------|
| `644` | `rw-r--r--` | Normale Dateien, Konfigurationsdateien |
| `600` | `rw-------` | Private Dateien: SSH-Schlüssel, Passwörter |
| `640` | `rw-r-----` | Dateien, die eine Dienstgruppe lesen darf, z. B. TLS-Schlüssel |
| `755` | `rwxr-xr-x` | Verzeichnisse, Programme und Skripte |
| `750` | `rwxr-x---` | Verzeichnisse, die nur Besitzer und Gruppe betreten dürfen |
| `700` | `rwx------` | Private Verzeichnisse wie `~/.ssh` |

Sonderrechte:

| Bit | Wert | Anzeige | Bedeutung | Beispiel |
|-----|------|---------|-----------|----------|
| SUID | `4000` | `rws` beim Besitzer | Ein Programm läuft mit den Rechten seines Besitzers | `/usr/bin/passwd` |
| SGID | `2000` | `rws` bei der Gruppe | Neue Dateien in einem Verzeichnis bekommen dessen Gruppe | Gemeinsame Projektverzeichnisse |
| Sticky Bit | `1000` | `rwt` bei den anderen | Nur der Besitzer darf seine Dateien löschen | `/tmp` |

!!! tip "„Permission denied“ Schritt für Schritt"
    1. Wer bin ich? `id` zeigt deinen Benutzer und deine Gruppen.
    2. Was erlaubt die Datei? `ls -l DATEI` zeigt Besitzer, Gruppe und Rechte.
    3. Komme ich überhaupt an die Datei? `namei -l /voller/pfad/DATEI` zeigt die Rechte
       jedes Verzeichnisses auf dem Weg. Jedes Verzeichnis braucht `x`.
    4. Gibt es ACLs (`+` hinter den Rechten bei `ls -l`) oder Attribute wie `i`?

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
