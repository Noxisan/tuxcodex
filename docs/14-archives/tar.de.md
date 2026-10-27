# tar

> Packt Dateien und Verzeichnisse in ein Archiv und entpackt es wieder, mit Rechten, Besitzern und Datum. Zusammen mit einem Kompressor das Standardformat für Backups unter Linux.

![tar output](../assets/screenshots/14-archives/tar.png)

## Syntax

```bash
tar [OPTION]... [DATEI]...
```

Merk dir die Reihenfolge: `c` anlegen, `x` entpacken, `t` auflisten. Direkt nach `f` muss der Dateiname folgen.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-c` | Ein Archiv anlegen |
| `-x` | Ein Archiv entpacken |
| `-t` | Den Inhalt auflisten |
| `-f DATEI` | Die Archivdatei, immer nötig |
| `-v` | Die Dateien während der Arbeit auflisten |
| `-z`, `-j`, `-J`, `--zstd` | Mit gzip, bzip2, xz oder zstd komprimieren |
| `-C VERZ` | Erst in dieses Verzeichnis wechseln, z. B. um dorthin zu entpacken |
| `--exclude=MUSTER` | Passende Dateien überspringen |
| `-p` | Beim Entpacken die Rechte behalten (Standard für root) |

## Beispiele

**Ein Verzeichnis in ein komprimiertes Archiv packen:**

```bash
tar -czvf www.tar.gz -C /srv www
```

```text
www/
www/css/
www/css/style.css
www/img/
www/img/logo.png
www/index.html
```

**Den Inhalt eines Archivs anzeigen:**

```bash
tar -tzvf www.tar.gz
```

```text
drwxr-xr-x nox/nox           0 2026-10-26 10:15 www/
drwxr-xr-x nox/nox           0 2026-10-26 10:15 www/css/
-rw-r--r-- nox/nox        3092 2026-10-26 10:15 www/css/style.css
drwxr-xr-x nox/nox           0 2026-10-26 10:15 www/img/
-rw-r--r-- nox/nox       40000 2026-10-26 10:15 www/img/logo.png
-rw-r--r-- nox/nox       28893 2026-10-26 10:15 www/index.html
```

**In ein anderes Verzeichnis entpacken:**

```bash
mkdir -p /tmp/restore
tar -xzvf www.tar.gz -C /tmp/restore
```

```text
www/
www/css/
www/css/style.css
www/img/
www/img/logo.png
www/index.html
```

**Eine einzelne Datei entpacken:**

```bash
tar -xzvf www.tar.gz -C /tmp/restore www/css/style.css
```

```text
www/css/style.css
```

**Ein zstd-Archiv ohne die Bilder anlegen:**

```bash
tar --zstd -cf www.tar.zst --exclude=www/img -C /srv www
tar -tf www.tar.zst
```

```text
www/
www/css/
www/css/style.css
www/index.html
```

**Ein Archiv mit den Dateien auf der Platte vergleichen:**

```bash
tar -dzf www.tar.gz -C /srv
```

```text
www/index.html: Mod time differs
www/index.html: Size differs
```

`index.html` wurde nach dem Backup geändert.

## Wann brauche ich das?

- Für Backups von Verzeichnissen, etwa `/etc`, `/srv/www` oder einem Home-Verzeichnis
- Um ein Verzeichnis samt Rechten auf einen anderen Server zu bringen
- Um Software zu entpacken, die als `.tar.gz` oder `.tar.xz` verteilt wird

!!! tip "Relative Pfade im Archiv"
    Wechsle vor dem Archivieren mit `-C` oder `cd` in das übergeordnete Verzeichnis. Dann
    enthält das Archiv `www/...` statt `home/nox/srv/www/...`, und du kannst es überall
    entpacken.

!!! warning "Entpacken überschreibt"
    `tar -x` überschreibt vorhandene Dateien ohne Rückfrage. Prüfe den Inhalt vorher mit
    `tar -tf` und entpacke im Zweifel mit `-C` in ein leeres Verzeichnis.

## Verwandte Befehle

[gzip](gzip.md) · [zstd](zstd.md) · [zip](zip.md) · [rsync](../12-ssh/rsync.md) · [unzip](unzip.md) · [xz](xz.md) · [sha256sum](sha256sum.md)
