# file

> Erkennt den Typ einer Datei anhand ihres Inhalts, egal was Dateiname oder Endung sagen.

![file output](../assets/screenshots/03-files/file.png)

## Syntax

```bash
file [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-b`, `--brief` | Nur den Typ ausgeben, ohne Dateinamen |
| `-i`, `--mime` | MIME-Typ und Zeichensatz ausgeben (z. B. `text/plain; charset=utf-8`) |
| `-L`, `--dereference` | Symbolischen Links folgen und das Ziel prüfen |
| `-z`, `--uncompress` | In komprimierte Dateien hineinschauen |
| `-s`, `--special-files` | Auch Blockgeräte und Partitionen lesen (z. B. `/dev/vda1`) |

## Beispiele

**Den Typ mehrerer Dateien prüfen:**

```bash
file notes.txt scripts/backup.sh
```

```text
notes.txt:         ASCII text
scripts/backup.sh: Bourne-Again shell script, ASCII text executable
```

**Prüfen, was in einem Backup steckt:**

```bash
file backup/*
```

```text
backup/db-2026-10-20.sql.gz:  gzip compressed data, was "db-2026-10-20.sql", last modified: Tue Oct 20 12:00:12 2026, from Unix, original size modulo 2^32 1073741824
backup/etc-2026-10-20.tar.gz: gzip compressed data, from Unix, original size modulo 2^32 432013312
```

**Ein Skript mit Windows-Zeilenenden finden:**

```bash
file deploy.sh
```

```text
deploy.sh: Bourne-Again shell script, ASCII text executable, with CRLF line terminators
```

**Herausfinden, worauf ein symbolischer Link zeigt:**

```bash
file /bin/sh
file -L /bin/sh
```

```text
/bin/sh: symbolic link to dash
/bin/sh: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4f6c1a2e9b3d8c7f5e0a1b2c3d4e5f6a7b8c9d0e, for GNU/Linux 3.2.0, stripped
```

**Eine Datei mit falscher Endung erkennen:**

```bash
file logo.txt
```

```text
logo.txt: PNG image data, 1254 x 1254, 8-bit/color RGB, non-interlaced
```

**MIME-Typ und Zeichensatz anzeigen:**

```bash
file -i notes.txt
```

```text
notes.txt: text/plain; charset=us-ascii
```

## Wann brauche ich das?

- Wenn ein Skript mit `/bin/bash^M: bad interpreter` abbricht: `file` zeigt
  `with CRLF line terminators`, die Datei wurde unter Windows gespeichert
- Um Uploads oder Downloads zu prüfen, deren Namen oder Endung du nicht traust
- Um herauszufinden, ob eine Datei Text oder binär ist, bevor du sie im Editor öffnest
- Um Backups und Archive vor dem Wiederherstellen zu prüfen

!!! tip "Windows-Zeilenenden korrigieren"
    Eine Datei mit CRLF-Zeilenenden wandelst du mit `sed -i 's/\r$//' deploy.sh` ins
    Linux-Format um. Das Paket `dos2unix` bietet dasselbe als eigenen Befehl.

!!! warning "Keine Sicherheitsprüfung"
    `file` schaut nur auf die ersten Bytes einer Datei und vergleicht sie mit bekannten
    Mustern. Das hilft bei der Orientierung, beweist aber nicht, dass eine hochgeladene
    Datei harmlos ist.

## Verwandte Befehle

[stat](stat.md) · [ln](ln.md)
