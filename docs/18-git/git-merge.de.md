# git merge

> Führt die Änderungen eines anderen Branches in den aktuellen Branch zusammen.

![git-merge output](../assets/screenshots/18-git/git-merge.png)

## Syntax

```bash
git merge [OPTIONEN] BRANCH
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `BRANCH` | Der Branch, dessen Commits in den aktuellen übernommen werden |
| `--ff-only` | Nur zusammenführen, wenn kein Merge-Commit nötig ist (Fast-Forward), sonst abbrechen |
| `--no-ff` | Immer einen Merge-Commit erzeugen, auch wenn ein Fast-Forward möglich wäre |
| `--squash` | Alle Änderungen des Branches zu einem einzigen neuen Commit zusammenfassen |
| `-m NACHRICHT` | Nachricht des Merge-Commits |
| `--abort` | Einen Merge mit Konflikten abbrechen und den vorherigen Stand wiederherstellen |

## Beispiele

**Einen fertigen Branch in main zusammenführen:**

```bash
git switch main
git merge rotate-logs
```

```text
Switched to branch 'main'
Merge made by the 'ort' strategy.
 rotate-logs.sh | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 rotate-logs.sh
```

**Ein Fast-Forward ohne Merge-Commit:**

```bash
git merge fix-paths
```

```text
Updating 6e6f0af..5f9cfee
Fast-forward
 check-disk.sh | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Ein Konflikt: Beide Branches haben dieselbe Zeile geändert:**

```bash
git merge fix-paths
cat check-disk.sh
```

```text
Auto-merging check-disk.sh
CONFLICT (content): Merge conflict in check-disk.sh
Automatic merge failed; fix conflicts and then commit the result.
#!/usr/bin/env bash
<<<<<<< HEAD
df -hT / /srv/data /mnt/backup
=======
df -h / /srv/data /mnt/backup /var
>>>>>>> fix-paths
```

Über `=======` steht die Version des aktuellen Branches, darunter die aus `fix-paths`. Bearbeite die Datei so, dass nur die richtige Zeile übrig bleibt, ohne die Marken.

**Den Merge nach dem Lösen des Konflikts abschließen:**

```bash
git add check-disk.sh
git commit --no-edit
```

```text
[main 8d2f6a1] Merge branch 'fix-paths'
```

**Den Merge stattdessen abbrechen:**

```bash
git merge --abort
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Wann brauche ich das?

- Wenn eine Änderung in ihrem eigenen Branch fertig und getestet ist
- Um Änderungen vom Server in deinen Branch zu holen (das macht `git pull`)

!!! tip "Fast-Forward oder Merge-Commit"
    Hat sich `main` seit dem Anlegen des Branches nicht bewegt, schiebt Git `main` einfach
    nach vorn (Fast-Forward). Sonst erzeugt es einen Merge-Commit mit zwei Eltern.

!!! warning "Alle Konfliktmarken entfernen"
    Git prüft nicht, ob `<<<<<<<`, `=======` und `>>>>>>>` noch in der Datei stehen. Eine
    Konfigurationsdatei mit diesen Zeilen legt den Dienst lahm. Prüf vor dem Commit mit
    `grep -n '^<<<<<<<' DATEI`.

## Verwandte Befehle

[git branch](git-branch.md) · [git switch](git-switch.md) · [git rebase](git-rebase.md) · [git pull](git-pull.md)
