# git commit

> Speichert die vorgemerkten Änderungen als neuen Commit im Verlauf des Repositorys.

![git-commit output](../assets/screenshots/18-git/git-commit.png)

## Syntax

```bash
git commit [-a] [-m "NACHRICHT"] [--amend]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-m NACHRICHT` | Commit-Nachricht auf der Kommandozeile, sonst öffnet sich der Editor |
| `-a`, `--all` | Alle geänderten verfolgten Dateien committen, ohne vorher `git add` (keine neuen Dateien) |
| `--amend` | Den letzten Commit ersetzen, etwa um eine vergessene Datei nachzureichen |
| `--no-edit` | Mit `--amend`: die Nachricht behalten |
| `-v`, `--verbose` | Beim Schreiben der Nachricht die Änderungen im Editor zeigen |

## Beispiele

**Die vorgemerkten Änderungen committen:**

```bash
git commit -m "Also check /mnt/backup"
```

```text
[main 3fcc96a] Also check /mnt/backup
 1 file changed, 1 insertion(+), 1 deletion(-)
```

`3fcc96a` ist der Anfang der Commit-ID (Hash), über die du ihn später ansprechen kannst.

**Alle geänderten Dateien in einem Schritt hinzufügen und committen:**

```bash
git commit -am "Run backup with lower priority"
```

```text
[main c31bfe7] Run backup with lower priority
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Eine vergessene Datei in den letzten Commit nachreichen:**

```bash
git add check-services.sh
git commit --amend --no-edit
```

```text
[main a41c7e2] Add service check
 Date: Mon Oct 26 10:12:40 2026 +0100
 2 files changed, 4 insertions(+)
 create mode 100755 check-services.sh
```

**Eine längere Nachricht im Editor schreiben:**

```bash
git commit
```

```text

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#       modified:   check-disk.sh
#
```

Schreib die Zusammenfassung in die erste Zeile, lass die zweite leer und ergänze darunter die Details. Speichern und schließen erzeugt den Commit.

## Wann brauche ich das?

- Nach jeder logischen Änderung, etwa einem behobenen Fehler oder einer neuen Einstellung
- Vor einer riskanten Änderung, damit du einen Stand hast, zu dem du zurückkannst
- Um den letzten Commit vor dem Pushen mit `--amend` zu korrigieren

!!! tip "Klein und oft"
    Ein Commit pro Änderung macht den Verlauf lesbar, und du kannst später genau eine
    Änderung zurücknehmen. Ein Commit kostet nichts.

!!! warning "--amend nur vor dem Pushen"
    `--amend` erzeugt einen neuen Commit und ersetzt den alten. Liegt der alte schon auf dem
    Server, passt dein Verlauf nicht mehr zu dem des Servers, und der nächste Push wird
    abgelehnt.

## Verwandte Befehle

[git add](git-add.md) · [git status](git-status.md) · [git log](git-log.md) · [git push](git-push.md)
