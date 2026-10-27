# gh run

> Listet, verfolgt und startet die Läufe von GitHub-Actions-Workflows aus dem Terminal neu.

![gh-run output](../assets/screenshots/22-ci-cd/gh-run.png)

## Syntax

```bash
gh run list | view | watch | rerun | cancel | download [LAUF_ID] [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `list` | Die letzten Läufe mit Status, Workflow, Branch und Dauer |
| `view [ID]` | Zusammenfassung eines Laufs: Jobs, Hinweise, Artefakte |
| `view --log-failed` | Nur das Log der fehlgeschlagenen Schritte |
| `watch [ID]` | Einen laufenden Lauf bis zum Ende verfolgen |
| `rerun [ID] --failed` | Die fehlgeschlagenen Jobs erneut ausführen |
| `cancel ID` | Einen Lauf abbrechen |
| `download ID` | Die Artefakte eines Laufs herunterladen |
| `-R OWNER/REPO` | Ein anderes Repository als das aktuelle |
| `-w WORKFLOW`, `-b BRANCH`, `-L N` | Mit `list`: nach Workflow oder Branch filtern, N Läufe zeigen |

`gh` braucht einmal eine Anmeldung: `gh auth login`.

## Beispiele

**Die letzten Läufe:**

```bash
gh run list -L 4
```

```text
STATUS  TITLE                    WORKFLOW  BRANCH   EVENT         ID           ELAPSED  AGE
✓       Add deploy job           Deploy    main     push          13104225387  1m38s    about 5 minutes ago
✓       Add deploy job           CI        main     push          13104225381  52s      about 5 minutes ago
X       Fix nginx config         CI        fix-ssl  pull_request  13104119240  31s      about 1 hour ago
✓       Update status page text  CI        main     push          13103987745  49s      about 3 hours ago
```

**Zusammenfassung eines Laufs:**

```bash
gh run view 13104225381
```

```text
✓ main CI · 13104225381
Triggered via push about 5 minutes ago

JOBS
✓ lint in 9s (ID 36457713245)
✓ build in 38s (ID 36457731902)

For more information about a job, try: gh run view --job=<job-id>
View this run on GitHub: https://github.com/nox/status-page/actions/runs/13104225381
```

**Zeigen, warum der Lauf gescheitert ist:**

```bash
gh run view 13104119240 --log-failed
```

```text
lint  Check shell scripts  2026-10-26T08:41:13.4421337Z ##[group]Run shellcheck scripts/*.sh
lint  Check shell scripts  2026-10-26T08:41:13.4475012Z
lint  Check shell scripts  2026-10-26T08:41:13.5129843Z In scripts/deploy.sh line 2:
lint  Check shell scripts  2026-10-26T08:41:13.5130512Z rm -rf $TARGET/old
lint  Check shell scripts  2026-10-26T08:41:13.5131029Z        ^-----^ SC2086 (info): Double quote to prevent globbing and word splitting.
lint  Check shell scripts  2026-10-26T08:41:13.5287741Z ##[error]Process completed with exit code 1.
```

**Einen laufenden Lauf verfolgen:**

```bash
gh run watch
```

```text
✓ main CI · 13104225381
Triggered via push less than a minute ago

JOBS
✓ lint in 9s (ID 36457713245)
✓ build in 38s (ID 36457731902)

✓ Run CI (13104225381) completed with 'success'
```

**Nur die fehlgeschlagenen Jobs erneut ausführen:**

```bash
gh run rerun 13104119240 --failed
```

```text
✓ Requested rerun (failed jobs) of run 13104119240
```

## Wann brauche ich das?

- Direkt nach `git push`, um zu sehen, ob die Pipeline durchläuft
- Um den Fehler eines gescheiterten Laufs zu lesen, ohne den Browser zu öffnen
- Um einen Lauf neu zu starten, der an einem vorübergehenden Problem gescheitert ist

!!! tip "Pushen und zusehen in einer Zeile"
    `git push && sleep 5 && gh run watch` verfolgt den Lauf, den der Push gestartet hat,
    und `gh run watch --exit-status` liefert einen Fehlercode, wenn er scheitert, praktisch
    in Skripten.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install gh` | `sudo apt install gh` | Repository `cli.github.com`, dann `sudo dnf install gh` | `sudo pacman -S github-cli` |

## Verwandte Befehle

[gh workflow](gh-workflow.md) · [gh secret](gh-secret.md) · [act](act.md) · [git push](../18-git/git-push.md)
