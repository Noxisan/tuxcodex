# Git verstehen

Git speichert den Zustand eines Verzeichnisses als Folge von Schnappschüssen, den
**Commits**. Jeder Commit hält fest, wer was wann und warum geändert hat, und du kannst zu
jedem davon zurück. Für Admins heißt das: Skripte und Konfigurationsdateien mit
vollständigem Verlauf, Änderungen, die sich rückgängig machen lassen, und dieselben Dateien
auf mehreren Servern.

## Die drei Bereiche

```text
Arbeitsverzeichnis  ──git add──►  Staging-Bereich  ──git commit──►  Repository
        ▲                                                               │
        └────────────────── git restore / git switch ───────────────────┘
```

| Bereich | Was er ist |
|---------|------------|
| **Arbeitsverzeichnis** | Die Dateien, die du siehst und bearbeitest |
| **Staging-Bereich** (Index) | Die Änderungen, die du mit [`git add`](git-add.md) für den nächsten Commit vorgemerkt hast |
| **Repository** | Alle Commits, gespeichert im versteckten Verzeichnis `.git` |

Du entscheidest, was in einen Commit kommt: drei Dateien ändern, zwei davon hinzufügen,
committen. Die dritte Änderung bleibt im Arbeitsverzeichnis für einen späteren Commit.

## Git einmal einrichten

Jeder Commit trägt einen Namen und eine E-Mail-Adresse. Setze sie einmal pro Benutzer:

```text
$ git config --global user.name "Nox"
$ git config --global user.email nox@example.com
$ git config --global init.defaultBranch main
```

Die Einstellungen landen in `~/.gitconfig`, siehe [`git config`](git-config.md).

## Dateien ignorieren

Eine Datei `.gitignore` im Repository listet Dateien auf, die Git nie verfolgen soll:
Logs, temporäre Dateien und vor allem Geheimnisse.

```text
# Logs and temporary files
*.log
*.swp
tmp/

# Secrets never belong in a repository
.env
*.key
```

[`git status`](git-status.md) zeigt ignorierte Dateien nicht an, und `git add .` lässt
sie aus. Nimm `.gitignore` selbst ins Repository auf, damit sie überall gilt.

## SSH-Schlüssel für GitHub und GitLab

Git-Server wie GitHub, GitLab oder Gitea melden dich per SSH-Schlüssel an. Erzeuge einen
Schlüssel, siehe [`ssh-keygen`](../12-ssh/ssh-keygen.md), und hinterlege den öffentlichen
Schlüssel in deinem Konto: bei GitHub unter *Settings › SSH and GPG keys*, bei GitLab unter
*Preferences › SSH Keys*.

```text
$ ssh-keygen -t ed25519 -C "nox@tuxcodex-srv"
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK3vYf2mPqT8wZr5nB7dXc1hL0sQe9uJgN4aRtVy6oMp nox@tuxcodex-srv
$ ssh -T git@github.com
Hi nox! You've successfully authenticated, but GitHub does not provide shell access.
```

Repository-Adressen sehen dann so aus: `git@github.com:nox/scripts.git`. Die Beispiele in
diesem Kapitel nutzen den Git-Server `git.example.com`.

## Der tägliche Ablauf

```text
$ git pull                       # get the latest state from the server
$ vim check-disk.sh              # change something
$ git status                     # what has changed?
$ git diff                       # what exactly?
$ git add check-disk.sh          # mark the change for the commit
$ git commit -m "Also check /var"
$ git push                       # send it to the server
```

Größere Änderungen machst du besser in einem eigenen Branch, siehe
[`git switch`](git-switch.md) und [`git merge`](git-merge.md).

## Gute Commit-Nachrichten

| Gut | Schlecht |
|-----|----------|
| `Raise PHP memory limit to 256M` | `changes` |
| `Fix backup path for /srv/data` | `fix` |
| Eine logische Änderung pro Commit | Eine Woche Arbeit in einem einzigen Commit |

Die erste Zeile ist eine kurze Zusammenfassung (etwa 50 Zeichen, im Imperativ: „Add“,
„Fix“, „Remove“). Braucht es mehr Erklärung, folgt nach einer Leerzeile der Rest.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorinstalliert | nein | ja (Server-Installation) | nein | nein |
| Installation | `sudo apt install git` | `sudo apt install git` | `sudo dnf install git` | `sudo pacman -S git` |

!!! tip "/etc versionieren"
    Das Paket `etckeeper` legt `/etc` in ein Git-Repository und committet automatisch vor
    und nach jeder Paketinstallation. So siehst du genau, welche Konfigurationsdatei sich
    wann geändert hat.

!!! danger "Keine Passwörter oder Schlüssel in ein Repository"
    Was du committest, bleibt im Verlauf, auch wenn du die Datei später löschst. Ein
    Passwort, das einmal gepusht wurde, gilt als kompromittiert: Ändere es. Halte
    Geheimnisse mit `.gitignore` von Anfang an heraus.
