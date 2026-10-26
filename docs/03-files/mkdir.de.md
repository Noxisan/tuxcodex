# mkdir

> Legt neue Verzeichnisse an, bei Bedarf samt aller fehlenden übergeordneten Verzeichnisse.

![mkdir output](../assets/screenshots/03-files/mkdir.png)

## Syntax

```bash
mkdir [OPTION]... VERZEICHNIS...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-p`, `--parents` | Fehlende übergeordnete Verzeichnisse mit anlegen, kein Fehler, wenn das Verzeichnis existiert |
| `-m`, `--mode=MODUS` | Rechte direkt setzen (z. B. `700`) |
| `-v`, `--verbose` | Für jedes angelegte Verzeichnis eine Meldung ausgeben |

## Beispiele

**Ein Verzeichnis anlegen:**

```bash
mkdir projects
ls -ld projects
```

```text
drwxr-xr-x 2 nox nox 4096 Oct 26 10:42 projects
```

**Eine verschachtelte Verzeichnisstruktur in einem Schritt anlegen:**

```bash
sudo mkdir -p /srv/www/example.com/{public,logs}
tree /srv/www
```

```text
/srv/www
└── example.com
    ├── logs
    └── public

3 directories, 0 files
```

**Anzeigen, welche Verzeichnisse angelegt wurden:**

```bash
mkdir -pv backup/2026/10
```

```text
mkdir: created directory 'backup/2026'
mkdir: created directory 'backup/2026/10'
```

`backup` gab es schon, deshalb wurden nur die beiden fehlenden Ebenen angelegt.

**Ein Verzeichnis anlegen, auf das nur du zugreifen kannst:**

```bash
mkdir -m 700 private
ls -ld private
```

```text
drwx------ 2 nox nox 4096 Oct 26 10:42 private
```

**Ein Verzeichnis anlegen, das schon existiert:**

```bash
mkdir projects
```

```text
mkdir: cannot create directory ‘projects’: File exists
```

## Wann brauche ich das?

- Um die Verzeichnisstruktur für eine neue Website, Anwendung oder ein Backup-Ziel
  anzulegen
- In Skripten und Deployments, wo `mkdir -p` sicherstellt, dass ein Verzeichnis
  existiert, ohne fehlzuschlagen, wenn es schon da ist
- Um Verzeichnisse mit eingeschränkten Rechten für Schlüssel oder Zugangsdaten
  anzulegen (`-m 700`)

!!! tip "`-p` in Skripten"
    `mkdir -p` schlägt nie fehl, weil ein Verzeichnis schon existiert. Damit kannst du
    ein Skript gefahrlos mehrmals ausführen.

!!! warning "Rechte außerhalb des Home-Verzeichnisses"
    Verzeichnisse wie `/srv`, `/opt` oder `/etc` gehören `root`. Ohne `sudo` bekommst du
    `mkdir: cannot create directory ‘/srv/www’: Permission denied`.

## Verwandte Befehle

[touch](touch.md) · [cd](../02-navigation/cd.md) · [tree](../02-navigation/tree.md) · [rmdir](rmdir.md)
