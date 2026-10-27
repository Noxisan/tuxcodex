# xz

> Komprimiert Dateien sehr stark, mit den kleinsten Ergebnissen der üblichen Verfahren. Langsam beim Komprimieren, schnell beim Entpacken.

![xz output](../assets/screenshots/14-archives/xz.png)

## Syntax

```bash
xz [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-k` | Die Originaldatei behalten |
| `-d`, `unxz` | Entpacken |
| `-v` | Fortschritt und Verhältnis zeigen |
| `-l` | Angaben zu einer `.xz`-Datei zeigen |
| `-T0` | Alle CPU-Kerne nutzen |
| `-0` … `-9`, `-e` | Stufe, Standard `6`; `-e` noch stärker und langsamer |

## Beispiele

**Mit allen Kernen und Fortschritt komprimieren:**

```bash
xz -v -T0 db.sql
```

```text
db.sql (1/1)
  100 %        48.7 MiB / 412.0 MiB = 0.118    19 MiB/s       0:21
```

**Angaben zur Datei anzeigen:**

```bash
xz -l db.sql.xz
```

```text
Strms  Blocks   Compressed Uncompressed  Ratio  Check   Filename
    1      18     48.7 MiB    412.0 MiB  0.118  CRC64   db.sql.xz
```

**Ein Release als `.tar.xz` packen:**

```bash
tar -cJf app-2.4.1.tar.xz app-2.4.1
ls -lh app-2.4.1.tar.xz
```

```text
-rw-r--r-- 1 nox nox 3.1M Oct 26 10:42 app-2.4.1.tar.xz
```

## Wann brauche ich das?

- Für Dateien, die einmal komprimiert und oft heruntergeladen werden, etwa Software-Releases
- Wenn jedes Megabyte zählt, etwa für ein Archiv auf langsamem Speicher
- Um Quellcode- und Kernel-Archive zu entpacken, die oft `.tar.xz` sind

!!! warning "Hoher Speicherbedarf"
    Starke Stufen brauchen viel Arbeitsspeicher: `xz -9` nutzt mehrere hundert MB pro Kern.
    Mit `-T0` auf vielen Kernen kann das für einen kleinen Server zu viel sein.

## Verwandte Befehle

[zstd](zstd.md) · [gzip](gzip.md) · [tar](tar.md)
