# ln

> Legt Links an: Symbolische Links zeigen auf einen Pfad, harte Links sind ein zweiter Name für dieselbe Datei.

![ln output](../assets/screenshots/03-files/ln.png)

## Syntax

```bash
ln [OPTION]... ZIEL LINKNAME
ln [OPTION]... ZIEL... VERZEICHNIS
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-s`, `--symbolic` | Symbolischen statt harten Link anlegen |
| `-f`, `--force` | Vorhandenen Link oder Datei mit gleichem Namen ersetzen |
| `-n`, `--no-dereference` | Vorhandenen Link auf ein Verzeichnis als Datei behandeln (mit `-f`) |
| `-r`, `--relative` | Symbolischen Link mit relativem Pfad anlegen |
| `-v`, `--verbose` | Jeden angelegten Link anzeigen |

| | Symbolischer Link (`ln -s`) | Harter Link (`ln`) |
|---|-----------------------------|--------------------|
| Zeigt auf | einen Pfad | die Daten selbst (gleicher Inode) |
| Für Verzeichnisse | ja | nein |
| Über Dateisysteme hinweg | ja | nein |
| Ziel gelöscht | Link ist kaputt | Daten bleiben erreichbar |

## Beispiele

**Eine nginx-Site mit einem symbolischen Link aktivieren:**

```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
ls -l /etc/nginx/sites-enabled/
```

```text
total 0
lrwxrwxrwx 1 root root 34 Sep 12 10:05 default -> /etc/nginx/sites-available/default
lrwxrwxrwx 1 root root 38 Oct 26 10:42 example.com -> /etc/nginx/sites-available/example.com
```

**Einen Link anlegen und anzeigen:**

```bash
ln -sv releases/2026-10-20 current
```

```text
'current' -> 'releases/2026-10-20'
```

**Einen vorhandenen Link auf ein neues Ziel zeigen lassen:**

```bash
ln -sfn releases/2026-10-26 current
ls -l current
```

```text
lrwxrwxrwx 1 nox nox 19 Oct 26 10:42 current -> releases/2026-10-26
```

**Einen harten Link anlegen:**

```bash
ln notes.txt notes-hard.txt
ls -li notes*.txt
```

```text
1048602 -rw-r--r-- 2 nox nox 812 Oct 26 09:15 notes-hard.txt
1048602 -rw-r--r-- 2 nox nox 812 Oct 26 09:15 notes.txt
```

Beide Namen haben dieselbe Inode-Nummer (`1048602`), und der Linkzähler steht auf `2`.

**Ein kaputter symbolischer Link:**

```bash
ln -s /etc/app.conf app.conf
cat app.conf
```

```text
cat: app.conf: No such file or directory
```

Der Link existiert, sein Ziel `/etc/app.conf` aber nicht.

## Wann brauche ich das?

- Um Sites und Module in nginx und Apache zu aktivieren (`sites-enabled`, `mods-enabled`)
- Für Deployments: `current` zeigt auf das aktive Release, und das Umstellen des Links
  rollt eine Version in einem Schritt aus oder zurück
- Um ein Programm oder Skript in `/usr/local/bin` verfügbar zu machen, ohne es zu kopieren
- Um eine Konfiguration in einem Git-Repository zu pflegen und sie an die Stelle zu
  verlinken, an der der Dienst sie erwartet

!!! tip "Prüfen, wohin ein Link zeigt"
    `ls -l` zeigt das Ziel hinter `->`. [`realpath`](../02-navigation/realpath.md) folgt
    der ganzen Kette von Links bis zur echten Datei.

!!! warning "Relative Ziele gelten relativ zum Link"
    `ln -s ../config/app.conf /etc/app.conf` speichert `../config/app.conf` wörtlich. Der
    Pfad wird vom Verzeichnis des **Links** (`/etc`) aus aufgelöst, nicht von dort, wo du
    den Befehl ausgeführt hast. Nimm absolute Pfade oder `-r`, um kaputte Links zu vermeiden.

!!! warning "Einen Link auf ein Verzeichnis ersetzen"
    Ohne `-n` ersetzt `ln -sf releases/2026-10-26 current` den Link `current` nicht, wenn
    er auf ein Verzeichnis zeigt. Stattdessen entsteht ein neuer Link **in** diesem
    Verzeichnis. Nimm zum Umstellen solcher Links immer `ln -sfn`.

## Verwandte Befehle

[cp](cp.md) · [realpath](../02-navigation/realpath.md)
