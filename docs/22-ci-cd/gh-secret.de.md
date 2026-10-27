# gh secret

> Legt Passwörter und Schlüssel als GitHub-Secrets ab, die Workflows nutzen können, ohne dass sie je im Code stehen.

![gh-secret output](../assets/screenshots/22-ci-cd/gh-secret.png)

## Syntax

```bash
gh secret set | list | delete NAME [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `set NAME` | Ein Secret setzen; der Wert wird von der Eingabe gelesen |
| `set NAME < DATEI` | Den Wert aus einer Datei nehmen, etwa einen SSH-Schlüssel |
| `-b`, `--body WERT` | Den Wert direkt angeben (landet in der Shell-History) |
| `-f`, `--env-file DATEI` | Alle Variablen einer `.env`-Datei auf einmal setzen |
| `-e`, `--env UMGEBUNG` | Secret einer Deployment-Umgebung, etwa `production` |
| `list` | Namen und Datum aller Secrets (nie die Werte) |
| `delete NAME` | Ein Secret löschen |

Im Workflow nutzt du ein Secret als `${{ secrets.NAME }}`. `gh variable` funktioniert genauso für Werte, die nicht geheim sind.

## Beispiele

**Den SSH-Schlüssel für das Deployment ablegen:**

```bash
gh secret set DEPLOY_KEY < ~/.ssh/deploy_status
gh secret set DEPLOY_KNOWN_HOSTS --body "$(ssh-keyscan -q status.example.com)"
```

```text
✓ Set Actions secret DEPLOY_KEY for nox/status-page
✓ Set Actions secret DEPLOY_KNOWN_HOSTS for nox/status-page
```

**Die Secrets auflisten:**

```bash
gh secret list
```

```text
NAME                UPDATED
DEPLOY_KEY          less than a minute ago
DEPLOY_KNOWN_HOSTS  less than a minute ago
REGISTRY_TOKEN      about 2 months ago
```

**Ein Passwort ohne Shell-History eingeben:**

```bash
gh secret set REGISTRY_TOKEN
```

```text
? Paste your secret ********************************
✓ Set Actions secret REGISTRY_TOKEN for nox/status-page
```

**Ein Secret nur für die Produktionsumgebung:**

```bash
gh secret set DB_PASSWORD --env production < db_password.txt
```

```text
✓ Set Actions secret DB_PASSWORD for nox/status-page
```

## Wann brauche ich das?

- Um einem Deploy-Workflow den SSH-Schlüssel für deinen Server zu geben
- Um API-Tokens für Registrys und Cloud-Anbieter abzulegen
- Um ein Passwort zu wechseln: einfach mit demselben Namen neu setzen

!!! tip "Umgebungen für die Produktion"
    Secrets einer Umgebung wie `production` lassen sich mit Regeln schützen, etwa einer
    nötigen Freigabe. Dann kann ein Pull Request nicht einfach in die Produktion ausrollen.

!!! warning "Nicht lesbar, nur ersetzbar"
    Niemand kann ein Secret zurücklesen, weder in der Weboberfläche noch mit `gh`. Bewahre
    das Original in deinem Passwortmanager auf.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install gh` | `sudo apt install gh` | Repository `cli.github.com`, dann `sudo dnf install gh` | `sudo pacman -S github-cli` |

## Verwandte Befehle

[gh run](gh-run.md) · [gh workflow](gh-workflow.md) · [ssh-keygen](../12-ssh/ssh-keygen.md) · [ansible-vault](../21-ansible/ansible-vault.md)
