# git stash

> Legt nicht committete Änderungen beiseite, damit du etwas anderes erledigen kannst, und holt sie später zurück.

![git-stash output](../assets/screenshots/18-git/git-stash.png)

## Syntax

```bash
git stash [push [-u] [-m "NACHRICHT"]]
git stash list | show | pop | apply | drop
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `push`, (keine) | Die Änderungen beiseitelegen; das Arbeitsverzeichnis ist danach sauber |
| `-m NACHRICHT` | Beschreibung des Stash |
| `-u`, `--include-untracked` | Auch neue, nicht verfolgte Dateien beiseitelegen |
| `list` | Alle Stashes auflisten |
| `show [-p]` | Zeigen, was ein Stash enthält; mit `-p` den vollständigen Diff |
| `pop` | Den neuesten Stash zurückholen und aus der Liste entfernen |
| `apply` | Einen Stash zurückholen, aber in der Liste behalten |
| `drop`, `clear` | Einen Stash löschen oder alle |

## Beispiele

**Änderungen beiseitelegen:**

```bash
git stash -m "Backup success message"
git status -s
```

```text
Saved working directory and index state On main: Backup success message
```

`git status -s` zeigt nichts mehr: Das Arbeitsverzeichnis ist sauber.

**Die Stashes auflisten:**

```bash
git stash list
```

```text
stash@{0}: On main: Backup success message
stash@{1}: WIP on main: fcdca2b Add service check
```

**Sehen, was ein Stash enthält:**

```bash
git stash show -p stash@{0}
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
```

**Trotz lokaler Änderungen pullen:**

```bash
git stash
git pull -q
git stash pop
```

```text
Saved working directory and index state WIP on main: fcdca2b Add service check
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   backup.sh

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (3aa763307131275684a45b04398b6790a46878c4)
```

## Wann brauche ich das?

- Wenn mitten in der Arbeit eine dringende Korrektur ansteht
- Wenn `git pull` oder `git switch` wegen lokaler Änderungen abbricht
- Um schnell etwas auszuprobieren und danach zum vorherigen Stand zurückzukehren

!!! tip "Neue Dateien nicht vergessen"
    Ohne `-u` nimmt `git stash` nur Änderungen an Dateien mit, die Git schon verfolgt.
    Neue Dateien bleiben im Arbeitsverzeichnis.

!!! warning "Ein Stash ist kein Backup"
    Stashes gibt es nur in deinem lokalen Repository, sie werden nie gepusht. Änderungen,
    die du behalten willst, gehören in einen Commit, notfalls in einem eigenen Branch.

## Verwandte Befehle

[git restore](git-restore.md) · [git switch](git-switch.md) · [git pull](git-pull.md) · [git commit](git-commit.md)
