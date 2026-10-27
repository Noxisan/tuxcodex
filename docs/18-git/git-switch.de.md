# git switch

> Wechselt zu einem anderen Branch und bringt die Dateien im Arbeitsverzeichnis auf dessen Stand.

![git-switch output](../assets/screenshots/18-git/git-switch.png)

## Syntax

```bash
git switch [-c] BRANCH
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `BRANCH` | Zu diesem Branch wechseln; gibt es ihn nur auf dem Server, legt Git ihn lokal an |
| `-c NAME`, `--create` | Einen neuen Branch anlegen und zu ihm wechseln |
| `-` | Zurück zum vorherigen Branch |
| `--detach COMMIT` | Einen Commit oder Tag ohne Branch ansehen (Detached HEAD) |
| `--discard-changes` | Wechseln, auch wenn lokale Änderungen verloren gehen |

## Beispiele

**Einen neuen Branch anlegen und zu ihm wechseln:**

```bash
git switch -c rotate-logs
```

```text
Switched to a new branch 'rotate-logs'
```

**Zurück zu main:**

```bash
git switch main
```

```text
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

**An einem Branch arbeiten, den es bisher nur auf dem Server gibt:**

```bash
git switch nginx-tls
```

```text
Switched to a new branch 'nginx-tls'
branch 'nginx-tls' set up to track 'origin/nginx-tls'.
```

**Eine alte Version ansehen:**

```bash
git switch --detach v1.0
```

```text
HEAD is now at 3fcc96a Also check /mnt/backup
```

`git switch -` bringt dich zurück zu dem Branch, von dem du kamst.

**Nicht committete Änderungen im Weg:**

```bash
git switch fix-paths
```

```text
error: Your local changes to the following files would be overwritten by checkout:
        check-disk.sh
Please commit your changes or stash them before you switch branches.
Aborting
```

Committe die Änderung vorher oder leg sie mit [`git stash`](git-stash.md) beiseite.

## Wann brauche ich das?

- Um eine neue Änderung in einem eigenen Branch zu beginnen
- Um zwischen deiner Arbeit und `main` hin und her zu wechseln, etwa für eine dringende Korrektur
- Um eine alte Version anzusehen, zum Beispiel die mit einem Tag markierte

!!! tip "git checkout macht dasselbe"
    Ältere Anleitungen nutzen `git checkout BRANCH` und `git checkout -b NAME`.
    `git switch` ist der neuere Befehl und erledigt nur diese eine Aufgabe.

## Verwandte Befehle

[git branch](git-branch.md) · [git merge](git-merge.md) · [git stash](git-stash.md) · [git restore](git-restore.md)
