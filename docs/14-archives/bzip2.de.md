# bzip2

> Komprimiert Dateien stärker als gzip, aber langsamer. Heute vor allem in älteren Archiven zu finden.

![bzip2 output](../assets/screenshots/14-archives/bzip2.png)

## Syntax

```bash
bzip2 [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-k` | Die Originaldatei behalten |
| `-d`, `bunzip2` | Entpacken |
| `-v` | Den Kompressionsgrad zeigen |
| `-t` | Eine komprimierte Datei prüfen |
| `-1` … `-9` | Blockgröße, Standard `9` |

## Beispiele

**Eine Datei komprimieren:**

```bash
bzip2 -v db.sql
```

```text
  db.sql:  6.012:1,  1.331 bits/byte, 83.37% saved, 432013312 in, 71857104 out.
```

**Eine komprimierte Datei prüfen:**

```bash
bzip2 -tv db.sql.bz2
```

```text
  db.sql.bz2: ok
```

**Ein altes `.tar.bz2`-Archiv entpacken:**

```bash
tar -xjvf site-2019.tar.bz2
```

```text
site-2019/
site-2019/index.php
site-2019/config.php
```

## Wann brauche ich das?

- Um ältere Archive und Downloads im `.bz2`-Format zu entpacken
- Wenn ein vorhandenes Skript oder System bzip2 erwartet

!!! tip "Bessere Alternativen"
    Für neue Archive ist `zstd` bei ähnlicher Größe viel schneller, und `xz` komprimiert noch
    stärker. bzip2 hat heute selten einen Vorteil.

## Verwandte Befehle

[gzip](gzip.md) · [xz](xz.md) · [zstd](zstd.md) · [tar](tar.md)
