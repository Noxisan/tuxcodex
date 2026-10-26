# stat

> Zeigt alle Metadaten einer Datei: Größe, Rechte, Besitzer, Inode und alle Zeitstempel.

## Syntax

```bash
stat [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-c`, `--format=FORMAT` | Nur die angegebenen Felder ausgeben (siehe unten) |
| `-f`, `--file-system` | Informationen zum Dateisystem statt zur Datei anzeigen |
| `-L`, `--dereference` | Symbolischen Links folgen und das Ziel anzeigen |

Die wichtigsten Formatfelder für `-c`:

| Feld | Bedeutung | Beispiel |
|------|-----------|----------|
| `%n` | Dateiname | `notes.txt` |
| `%s` | Größe in Bytes | `812` |
| `%a` | Rechte als Oktalzahl | `644` |
| `%A` | Rechte als Text | `-rw-r--r--` |
| `%U` / `%G` | Besitzer / Gruppe | `nox` / `nox` |
| `%y` | Zeitpunkt der letzten Änderung | `2026-10-26 09:15:42.118273645 +0100` |
| `%i` | Inode-Nummer | `1048602` |

## Beispiele

**Alle Informationen zu einer Datei anzeigen:**

```bash
stat notes.txt
```

```text
  File: notes.txt
  Size: 812             Blocks: 8          IO Block: 4096   regular file
Device: 254,1   Inode: 1048602     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/     nox)   Gid: ( 1000/     nox)
Access: 2026-10-26 09:20:03.412345678 +0100
Modify: 2026-10-26 09:15:42.118273645 +0100
Change: 2026-10-26 09:15:42.118273645 +0100
 Birth: 2026-10-20 14:05:11.904123456 +0200
```

| Zeit | Bedeutung |
|------|-----------|
| `Access` | Letzter Lesezugriff auf den Inhalt |
| `Modify` | Letzte Änderung des Inhalts |
| `Change` | Letzte Änderung des Inhalts **oder** der Metadaten (Rechte, Besitzer) |
| `Birth` | Zeitpunkt, an dem die Datei angelegt wurde |

**Rechte und Besitzer in einer Zeile anzeigen:**

```bash
stat -c '%a %U:%G %n' /etc/ssh/sshd_config
```

```text
644 root:root /etc/ssh/sshd_config
```

**Nur die Größe in Bytes anzeigen:**

```bash
stat -c '%s' notes.txt
```

```text
812
```

**Den Zeitpunkt der letzten Änderung anzeigen:**

```bash
stat -c '%y' notes.txt
```

```text
2026-10-26 09:15:42.118273645 +0100
```

**Informationen zum Dateisystem anzeigen:**

```bash
stat -f /
```

```text
  File: /
    ID: 3f8a1c2b9d4e5f60 Namelen: 255     Type: ext2/ext3
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 5127839    Free: 3912044    Available: 3647812
Inodes: Total: 1310720    Free: 1201833
```

![stat output](../assets/screenshots/03-files/stat.png)

## Wann brauche ich das?

- Um sekundengenau herauszufinden, wann eine Konfigurationsdatei zuletzt geändert wurde
- Um Rechte als Zahl zu prüfen (`644`, `600`), die sich leichter vergleichen lässt als
  `-rw-r--r--`
- In Skripten, die Größe, Besitzer oder Alter einer Datei brauchen
- Um zu prüfen, ob Metadaten geändert wurden: Ist `Change` neuer als `Modify`, hat
  jemand Rechte oder Besitzer geändert, nicht den Inhalt

!!! tip "Rechte für `chmod`"
    `stat -c '%a' DATEI` gibt die Rechte genau in dem Format aus, das du für `chmod`
    brauchst. So lassen sich Rechte leicht von einer Datei auf eine andere übertragen.

!!! warning "Die Zugriffszeit ist nicht immer genau"
    Um Schreibzugriffe zu sparen, hängt Linux Dateisysteme meist mit `relatime` ein. Die
    Zugriffszeit wird dann nur in bestimmten Fällen aktualisiert. Verlass dich nicht
    darauf, um zu beweisen, wann eine Datei zuletzt gelesen wurde.

## Verwandte Befehle

[ls](../02-navigation/ls.md) · [touch](touch.md)
