# git restore

> Verwirft Änderungen im Arbeitsverzeichnis oder holt Dateien wieder aus dem Staging-Bereich heraus.

![git-restore output](../assets/screenshots/18-git/git-restore.png)

## Syntax

```bash
git restore [--staged] [--source=COMMIT] PFAD...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Die Datei im Arbeitsverzeichnis auf den vorgemerkten oder committeten Stand zurücksetzen |
| `--staged`, `-S` | Die Datei aus dem Staging-Bereich nehmen, die Änderung in der Datei bleibt |
| `--source=COMMIT`, `-s` | Die Datei so wiederherstellen, wie sie in diesem Commit, Branch oder Tag war |
| `-p`, `--patch` | Stück für Stück auswählen, welche Änderungen verworfen werden |
| `--worktree --staged` | Beides auf einmal: aus dem Staging nehmen und verwerfen |

## Beispiele

**Eine missglückte Änderung verwerfen:**

```bash
git status -s
git restore backup.sh
git status -s
```

```text
 M backup.sh
```

Das zweite `git status` zeigt nichts mehr: `backup.sh` ist wieder auf dem Stand des letzten Commits.

**Eine Datei aus dem Staging-Bereich nehmen:**

```bash
git restore --staged check-disk.sh
git status -s
```

```text
 M check-disk.sh
```

**Die Version aus einem älteren Commit zurückholen:**

```bash
git restore --source=v1.0 check-disk.sh
git diff
```

```text
diff --git a/check-disk.sh b/check-disk.sh
index f12cb8f..0478c3c 100644
--- a/check-disk.sh
+++ b/check-disk.sh
@@ -1,2 +1,2 @@
 #!/usr/bin/env bash
-df -hT / /srv/data /mnt/backup /var
+df -h / /srv/data /mnt/backup
```

Die alte Version ist jetzt eine normale Änderung im Arbeitsverzeichnis. Committe sie oder verwirf sie wieder mit `git restore check-disk.sh`.

**Eine gelöschte Datei zurückholen:**

```bash
rm rotate-logs.sh
git restore rotate-logs.sh
ls
```

```text
README.md  backup.sh  check-disk.sh  check-services.sh  rotate-logs.sh
```

## Wann brauche ich das?

- Wenn eine Änderung schiefging und du die letzte funktionierende Version zurückwillst
- Wenn du eine Datei versehentlich hinzugefügt hast
- Um eine ältere Version einer Konfigurationsdatei zurückzuholen, etwa die von vor einem Update

!!! tip "Ältere Befehle für dasselbe"
    Ältere Anleitungen nutzen `git checkout -- DATEI` statt `git restore DATEI` und
    `git reset HEAD DATEI` statt `git restore --staged DATEI`. Beides funktioniert weiterhin.

!!! danger "Verworfen ist weg"
    `git restore DATEI` überschreibt deine nicht committeten Änderungen in dieser Datei ohne
    Rückfrage. Git kann sie nicht zurückholen, weil sie nie in einem Commit waren.

## Verwandte Befehle

[git status](git-status.md) · [git diff](git-diff.md) · [git stash](git-stash.md) · [git log](git-log.md)
