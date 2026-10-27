# git log

> Zeigt den Verlauf der Commits: wer was wann und warum geändert hat.

![git-log output](../assets/screenshots/18-git/git-log.png)

## Syntax

```bash
git log [OPTIONEN] [BEREICH] [-- PFAD...]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--oneline` | Eine Zeile pro Commit: kurze ID und Nachricht |
| `-N`, `-n N` | Nur die letzten N Commits |
| `--graph` | Branches und Merges als Graph zeichnen |
| `--all` | Alle Branches, nicht nur den aktuellen |
| `-p`, `--patch` | Die Änderungen jedes Commits zeigen |
| `--stat` | Die geänderten Dateien jedes Commits zeigen |
| `--since=DATUM`, `--until=DATUM` | Nur Commits in diesem Zeitraum, etwa `2026-10-24` oder `"2 weeks ago"` |
| `--author=NAME` | Nur Commits dieser Person |
| `--grep=TEXT` | Nur Commits, deren Nachricht den Text enthält |
| `-- PFAD` | Nur Commits, die diese Datei oder dieses Verzeichnis geändert haben |

## Beispiele

**Die letzten Commits zeigen:**

```bash
git log -2
```

```text
commit fcdca2b80d26c4bea3acde442420f133ff419929 (HEAD -> main, origin/main)
Author: Nox <nox@example.com>
Date:   Mon Oct 26 10:12:40 2026 +0100

    Add service check

commit 5f9cfeebdd686d7c7313eb0cb2b699699e2e9a5c
Author: Nox <nox@example.com>
Date:   Mon Oct 26 09:30:12 2026 +0100

    Check /var too
```

**Kompakter Verlauf mit Branches:**

```bash
git log --oneline --graph --all
```

```text
* fcdca2b (HEAD -> main, origin/main) Add service check
* 5f9cfee Check /var too
* 6e6f0af Show filesystem type
*   bdb6db4 Merge branch rotate-logs
|\
| * bfdf2d8 Add log rotation script
* | c31bfe7 Run backup with lower priority
|/
* 3fcc96a (tag: v1.0) Also check /mnt/backup
* 7f4bd56 Add README
* 0487470 Add backup and disk check scripts
```

**Die letzte Änderung an einer Datei, mit Diff:**

```bash
git log -p -1 check-disk.sh
```

```text
commit 5f9cfeebdd686d7c7313eb0cb2b699699e2e9a5c
Author: Nox <nox@example.com>
Date:   Mon Oct 26 09:30:12 2026 +0100

    Check /var too

diff --git a/check-disk.sh b/check-disk.sh
index 58ebc04..f12cb8f 100644
--- a/check-disk.sh
+++ b/check-disk.sh
@@ -1,2 +1,2 @@
 #!/usr/bin/env bash
-df -hT / /srv/data /mnt/backup
+df -hT / /srv/data /mnt/backup /var
```

**Commits seit einem Datum:**

```bash
git log --oneline --since=2026-10-24
```

```text
fcdca2b Add service check
5f9cfee Check /var too
6e6f0af Show filesystem type
bdb6db4 Merge branch rotate-logs
c31bfe7 Run backup with lower priority
```

**In den Commit-Nachrichten suchen:**

```bash
git log --oneline --grep=backup
```

```text
c31bfe7 Run backup with lower priority
3fcc96a Also check /mnt/backup
0487470 Add backup and disk check scripts
```

## Wann brauche ich das?

- Um herauszufinden, wann und warum eine Konfiguration geändert wurde
- Um einzugrenzen, seit wann ein Problem besteht: Welche Commits kamen nach dem letzten funktionierenden Stand?
- Um zu sehen, was jemand im Team in einem gemeinsamen Repository geändert hat

!!! tip "Den Pager mit q verlassen"
    Lange Ausgaben öffnen sich in einem Pager wie `less`. Blättern mit den Pfeiltasten,
    suchen mit `/`, beenden mit `q`.

## Verwandte Befehle

[git diff](git-diff.md) · [git tag](git-tag.md) · [git commit](git-commit.md) · [git branch](git-branch.md)
