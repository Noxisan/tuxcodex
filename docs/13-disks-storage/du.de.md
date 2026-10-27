# du

> Zeigt, wie viel Platz Dateien und Verzeichnisse belegen. Das Werkzeug, um herauszufinden, was eine Platte füllt.

![du output](../assets/screenshots/13-disks-storage/du.png)

## Syntax

```bash
du [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-s` | Nur die Summe pro Argument |
| `-h` | Lesbare Größen |
| `-d N`, `--max-depth=N` | Nur Verzeichnisse bis zur Tiefe `N` zeigen |
| `-x` | Auf diesem Dateisystem bleiben, anderen Einhängungen nicht folgen |
| `-a` | Auch Dateien auflisten, nicht nur Verzeichnisse |
| `--apparent-size` | Größe des Inhalts statt des belegten Platzes auf der Platte |

## Beispiele

**Größe eines Verzeichnisses:**

```bash
sudo du -sh /var/log
```

```text
1.3G    /var/log
```

**Die größten Verzeichnisse finden, sortiert:**

```bash
sudo du -h -d 1 -x /var | sort -h
```

```text
4.0K    /var/local
4.0K    /var/opt
16K     /var/tmp
1.1M    /var/spool
48M     /var/backups
402M    /var/cache
612M    /var/lib
1.3G    /var/log
2.3G    /var
```

**Die fünf größten Unterverzeichnisse der Logs:**

```bash
sudo du -h -d 1 /var/log | sort -rh | sed -n '2,6p'
```

```text
812M    /var/log/nginx
214M    /var/log/journal
98M     /var/log/postgresql
41M     /var/log/apt
12M     /var/log/installer
```

`sed -n '2,6p'` überspringt die erste Zeile, die Summe von `/var/log` selbst.

**Die größten einzelnen Dateien:**

```bash
sudo du -ah /var/log/nginx | sort -rh | sed -n '2,3p'
```

```text
4.0G    /var/log/nginx/access.log.1
1.0G    /var/log/nginx/access.log
```

## Wann brauche ich das?

- Wenn `df` eine volle Platte zeigt: Welches Verzeichnis ist schuld?
- Um große Logdateien oder vergessene Backups zu finden
- Vor einem Umzug, um zu wissen, wie viele Daten verschoben werden müssen

!!! tip "Mit `sort -h` kombinieren"
    `du -h | sort -h` sortiert lesbare Größen richtig: `4.0K` vor `1.2M` vor `3.4G`. Die
    größten Einträge stehen am Ende.

!!! warning "Langsam bei großen Verzeichnissen"
    `du` liest jede Datei. Bei Verzeichnissen mit Millionen Dateien kann das Minuten dauern
    und die Platte belasten. Begrenze es mit `-d 1` und `-x`.

## Verwandte Befehle

[df](df.md) · [ncdu](ncdu.md) · [sort](../05-text-processing/sort.md) · [find](../02-navigation/find.md)
