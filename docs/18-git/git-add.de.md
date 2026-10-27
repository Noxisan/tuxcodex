# git add

> Merkt Änderungen für den nächsten Commit vor, indem es sie in den Staging-Bereich legt.

![git-add output](../assets/screenshots/18-git/git-add.png)

## Syntax

```bash
git add [OPTIONEN] PFAD...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `PFAD` | Datei oder Verzeichnis; `.` heißt alles im aktuellen Verzeichnis und darunter |
| `-A`, `--all` | Alle Änderungen im ganzen Repository, auch gelöschte Dateien |
| `-u`, `--update` | Nur Dateien, die Git schon verfolgt, keine neuen |
| `-p`, `--patch` | Stück für Stück auswählen, welche Änderungen hinzukommen |
| `-n`, `--dry-run` | Nur anzeigen, was hinzugefügt würde |
| `-f`, `--force` | Auch eine Datei hinzufügen, die `.gitignore` ausschließt |

## Beispiele

**Eine Datei hinzufügen und das Ergebnis prüfen:**

```bash
git add check-disk.sh
git status -s
```

```text
M  check-disk.sh
 M backup.sh
?? notes.txt
```

`check-disk.sh` ist jetzt vorgemerkt (linke Spalte), `backup.sh` ist geändert, aber nicht vorgemerkt.

**Sehen, was git add . tun würde:**

```bash
git add -n .
```

```text
add 'backup.sh'
add 'notes.txt'
```

**Nur einen Teil der Änderungen hinzufügen:**

```bash
git add -p backup.sh
```

```text
diff --git a/backup.sh b/backup.sh
index 8791eb2..895c5d1 100644
--- a/backup.sh
+++ b/backup.sh
@@ -1,3 +1,4 @@
 #!/usr/bin/env bash
 set -euo pipefail
 nice -n 10 tar --zstd -cf "/mnt/backup/www-$(date +%F).tar.zst" -C /srv www
+echo "backup done"
(1/1) Stage this hunk [y,n,q,a,d,e,p,?]? y
```

**Alle Änderungen an verfolgten Dateien hinzufügen:**

```bash
git add -u
git status -s
```

```text
M  backup.sh
M  check-disk.sh
?? notes.txt
```

## Wann brauche ich das?

- Vor jedem Commit, um genau festzulegen, was hineinkommt
- Um mehrere Änderungen in einer Datei mit `-p` auf getrennte Commits aufzuteilen
- Um neue Dateien ins Repository aufzunehmen

!!! tip "Saubere Commits mit -p"
    `git add -p` zeigt jeden geänderten Block und fragt `y` (hinzufügen) oder `n`
    (überspringen). So enthält ein Commit nur, was zusammengehört.

!!! warning "Vor git add . prüfen"
    `git add .` nimmt auch neue Dateien mit, die du vielleicht nicht im Repository haben
    willst, etwa Logdateien oder eine `.env` mit Passwörtern. Schau vorher in `git status`
    oder nutze `-n`.

## Verwandte Befehle

[git status](git-status.md) · [git commit](git-commit.md) · [git restore](git-restore.md) · [git diff](git-diff.md)
