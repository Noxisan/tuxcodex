# git push

> Schickt deine lokalen Commits auf den Server.

![git-push output](../assets/screenshots/18-git/git-push.png)

## Syntax

```bash
git push [-u] [REMOTE [BRANCH]]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-u`, `--set-upstream` | Den Server-Branch merken, damit später ein einfaches `git push` und `git pull` reicht |
| `--follow-tags` | Auch annotierte Tags senden, die zu den gepushten Commits gehören |
| `--tags` | Alle Tags senden |
| `-d`, `--delete BRANCH` | Einen Branch auf dem Server löschen |
| `--force-with-lease` | Den Server-Branch überschreiben, aber nur, wenn niemand sonst inzwischen gepusht hat |
| `-n`, `--dry-run` | Nur anzeigen, was gesendet würde |

## Beispiele

**Neue Commits auf den Server schicken:**

```bash
git push
```

```text
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 318 bytes | 318.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
To git.example.com:nox/scripts.git
   fcdca2b..599c398  main -> main
```

**Einen neuen Branch veröffentlichen:**

```bash
git push -u origin nginx-tls
```

```text
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 297 bytes | 297.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: To create a merge request for nginx-tls, visit:
remote:   https://git.example.com/nox/scripts/-/merge_requests/new?merge_request%5Bsource_branch%5D=nginx-tls
remote:
To git.example.com:nox/scripts.git
 * [new branch]      nginx-tls -> nginx-tls
branch 'nginx-tls' set up to track 'origin/nginx-tls'.
```

Die Zeilen mit `remote:` kommen vom Server, hier einer GitLab-Instanz.

**Der Server hat neuere Commits:**

```bash
git push
```

```text
To git.example.com:nox/scripts.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'git.example.com:nox/scripts.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

**Einen Branch auf dem Server löschen:**

```bash
git push origin --delete nginx-tls
```

```text
To git.example.com:nox/scripts.git
 - [deleted]         nginx-tls
```

## Wann brauche ich das?

- Nach dem Committen, damit die Änderungen sicher auf dem Server liegen und andere sie holen können
- Um einen neuen Branch zu veröffentlichen, etwa für einen Merge Request
- Um nicht mehr benötigte Branches auf dem Server aufzuräumen

!!! tip "Abgelehnt? Erst pullen"
    Hat der Server Commits, die du noch nicht hast, lehnt Git den Push ab. Führe
    `git pull` (oder `git pull --rebase`) aus und pushe erneut.

!!! danger "Kein --force"
    `git push --force` überschreibt den Branch auf dem Server und löscht Commits, die andere
    gepusht haben. Musst du wirklich überschreiben, nimm `--force-with-lease`: Es verweigert,
    wenn sich der Server seit deinem letzten Fetch geändert hat.

## Verwandte Befehle

[git pull](git-pull.md) · [git remote](git-remote.md) · [git commit](git-commit.md) · [git tag](git-tag.md)
