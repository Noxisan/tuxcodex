# hexdump

> Zeigt die Bytes einer Datei hexadezimal an, inklusive aller Zeichen, die im Texteditor unsichtbar sind.

![hexdump output](../assets/screenshots/04-viewing-files/hexdump.png)

## Syntax

```bash
hexdump [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-C` | Kanonisches Format: Position, Hex-Bytes und lesbare Zeichen nebeneinander |
| `-n N` | Nur die ersten `N` Bytes lesen |
| `-s N` | Die ersten `N` Bytes überspringen |
| `-v` | Alle Zeilen zeigen, auch wiederholte (sonst als `*` zusammengefasst) |

## Beispiele

**Eine Byte Order Mark (BOM) in einer Konfigurationsdatei finden:**

```bash
hexdump -C config.json
```

```text
00000000  ef bb bf 7b 0a 20 20 22  6e 61 6d 65 22 3a 20 22  |...{.  "name": "|
00000010  61 70 70 22 0a 7d 0a                              |app".}.|
00000017
```

Die Bytes `ef bb bf` am Anfang sind eine UTF-8-BOM. Viele Programme stolpern darüber,
obwohl ein Editor sie nicht anzeigt.

| Spalte | Bedeutung |
|--------|-----------|
| `00000000` | Position (Offset) des ersten Bytes der Zeile, hexadezimal |
| `ef bb bf 7b …` | Die Bytes als Hexadezimalzahlen, 16 pro Zeile |
| `|...{.  "name": "|` | Dieselben Bytes als Zeichen, `.` für alles, was nicht druckbar ist |

**Windows-Zeilenenden in einem Skript finden:**

```bash
hexdump -C deploy.sh
```

```text
00000000  23 21 2f 62 69 6e 2f 62  61 73 68 0d 0a 65 63 68  |#!/bin/bash..ech|
00000010  6f 20 22 44 65 70 6c 6f  79 22 0d 0a              |o "Deploy"..|
0000001c
```

`0d 0a` ist ein Windows-Zeilenende (CR LF). Unter Linux endet eine Zeile nur mit `0a`.

**Nur den Anfang einer Datei ansehen:**

```bash
hexdump -C -n 16 backup/db-2026-10-20.sql.gz
```

```text
00000000  1f 8b 08 08 cc 57 d7 6a  00 03 64 62 2d 32 30 32  |.....W.j..db-202|
00000010
```

`1f 8b` ist die Signatur jeder gzip-Datei. So erkennt `file` Dateitypen.

**Eine Datei, die nur Nullen enthält:**

```bash
hexdump -C zero.bin
```

```text
00000000  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000400
```

Der `*` bedeutet: Die vorherige Zeile wiederholt sich bis Position `400` (1024 Bytes).

## Wann brauche ich das?

- Wenn eine Konfiguration oder ein Skript fehlschlägt, obwohl im Editor alles richtig
  aussieht: BOM, Windows-Zeilenenden, Tabs oder geschützte Leerzeichen werden sichtbar
- Um die Signatur einer Datei (gzip, PNG, ELF) zu prüfen und beschädigte oder falsch
  benannte Dateien zu finden
- Um zu prüfen, ob eine Platte oder Datei wirklich nur Nullen enthält, etwa nach dem Löschen

!!! tip "Immer `-C` nehmen"
    Ohne Optionen zeigt `hexdump` die Bytes in 2-Byte-Gruppen in einer verwirrenden
    Reihenfolge. `hexdump -C` ist das Format, das jeder erwartet. Unter Debian und Ubuntu
    ist `hd` eine Kurzform dafür.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `bsdextrautils` | `bsdextrautils` | `util-linux` (immer installiert) | `util-linux` (immer installiert) |

Fehlt `hexdump` unter Debian oder Ubuntu, installierst du es mit
`sudo apt install bsdextrautils`. Eine Alternative ist `xxd` aus dem gleichnamigen Paket
(unter RHEL Teil von `vim-common`).

## Verwandte Befehle

[file](../03-files/file.md) · [cat](cat.md) · [strings](strings.md)
