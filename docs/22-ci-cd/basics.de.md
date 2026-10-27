# CI/CD verstehen

**CI** (Continuous Integration) heißt: Jeder Push wird automatisch geprüft, durch Linter,
Tests und einen Build. **CD** (Continuous Delivery oder Deployment) geht einen Schritt weiter
und rollt aus, was die Prüfungen bestanden hat, etwa auf `tuxdex-srv`. Statt „das spiele
ich später von Hand ein“ nimmt jede Änderung denselben geprüften Weg.

```text
git push ──► lint ──► test ──► build image ──► deploy to the server
              │        │           │                  │
              └────────┴───────────┴── stops at the first error
```

## Die Begriffe

| Begriff | GitHub Actions | GitLab CI | Bedeutung |
|---------|----------------|-----------|-----------|
| Definition | `.github/workflows/*.yml` | `.gitlab-ci.yml` | Die Pipeline als YAML-Datei im Repository |
| Pipeline | Workflow Run | Pipeline | Ein Durchlauf, ausgelöst durch einen Push, einen Merge Request oder einen Zeitplan |
| Job | Job | Job | Eine Gruppe von Schritten auf einem Runner; Jobs können voneinander abhängen |
| Schritt | Step | Zeile unter `script` | Ein einzelner Befehl oder eine fertige Action |
| Runner | Von GitHub gehostet oder selbst betrieben | Shared Runner oder eigener `gitlab-runner` | Der Rechner, der die Jobs ausführt |
| Secret | Secret | CI/CD-Variable (maskiert, geschützt) | Passwörter und Schlüssel, nie in der YAML-Datei |
| Artefakt | Artifact | Artifact | Dateien, die ein Job weitergibt, etwa ein gebautes Paket |

## Was du installieren musst

Für die Pipeline selbst brauchst du keines dieser Werkzeuge: Sie läuft bei GitHub oder
GitLab. Sie helfen dir, Pipelines im Terminal zu verfolgen und zu steuern und Fehler vor
dem Push zu finden.

| Werkzeug | Für | Debian | Ubuntu | RHEL | Arch |
|----------|-----|--------|--------|------|------|
| [`gh`](gh-run.md) | GitHub | `sudo apt install gh` | `sudo apt install gh` | Repository `cli.github.com`, dann `sudo dnf install gh` | `sudo pacman -S github-cli` |
| [`act`](act.md) | GitHub, lokale Läufe | Installationsskript von nektos/act | Installationsskript von nektos/act | Installationsskript von nektos/act | `sudo pacman -S act` |
| [`actionlint`](actionlint.md) | GitHub | Release-Binary von GitHub | Release-Binary von GitHub | Release-Binary von GitHub | Release-Binary von GitHub |
| [`glab`](glab-ci.md) | GitLab | `sudo apt install glab` | `sudo apt install glab` | `.rpm` aus den glab-Releases | `sudo pacman -S glab` |
| [`gitlab-runner`](gitlab-runner.md) | GitLab, eigener Runner | Repository `packages.gitlab.com` | Repository `packages.gitlab.com` | Repository `packages.gitlab.com` | `sudo pacman -S gitlab-runner` |
| [`yamllint`](yamllint.md) | jedes YAML | `sudo apt install yamllint` | `sudo apt install yamllint` | `sudo dnf install yamllint` (EPEL) | `sudo pacman -S yamllint` |
| [`pre-commit`](pre-commit.md) | Git-Hooks | `sudo apt install pre-commit` | `sudo apt install pre-commit` | `pipx install pre-commit` | `sudo pacman -S pre-commit` |

Das `gh`-Paket von Debian und Ubuntu hinkt oft ein paar Versionen hinterher. Das Repository
unter `cli.github.com` hat die aktuelle Version auch für Debian und Ubuntu.

## Ein Workflow für GitHub Actions

`.github/workflows/ci.yml` prüft bei jedem Push die Shell-Skripte und baut danach das
Docker-Image aus dem [Docker-Kapitel](../19-docker/docker-build.md):

```text
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check shell scripts
        run: shellcheck scripts/*.sh

  build:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t status-page:${{ github.sha }} .
```

`needs: lint` lässt `build` auf `lint` warten und überspringt ihn, wenn `lint` scheitert.

## Auf den eigenen Server ausrollen

Ein Deploy-Job meldet sich per SSH auf dem Server an, mit einem Schlüssel, der als Secret
hinterlegt ist:

```text
  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to tuxdex-srv
        env:
          SSH_KEY: ${{ secrets.DEPLOY_KEY }}
          KNOWN_HOSTS: ${{ secrets.DEPLOY_KNOWN_HOSTS }}
        run: |
          mkdir -p ~/.ssh
          echo "$SSH_KEY" > ~/.ssh/id_ed25519 && chmod 600 ~/.ssh/id_ed25519
          echo "$KNOWN_HOSTS" > ~/.ssh/known_hosts
          ssh deploy@status.example.com "cd /srv/status && docker compose pull && docker compose up -d"
```

Auf dem Server bekommt der Benutzer `deploy` einen eigenen Schlüssel mit einem
eingeschränkten Eintrag in `authorized_keys`, siehe [`ssh-keygen`](../12-ssh/ssh-keygen.md).
Die Secrets setzt du mit [`gh secret`](gh-secret.md).

## Dasselbe für GitLab CI

`.gitlab-ci.yml`:

```text
stages:
  - lint
  - build

lint:
  stage: lint
  image: debian:trixie
  script:
    - apt-get update && apt-get install -y shellcheck
    - shellcheck scripts/*.sh

build:
  stage: build
  image: docker:29
  services:
    - docker:29-dind
  script:
    - docker build -t status-page:$CI_COMMIT_SHORT_SHA .
```

Jeder Job läuft im angegebenen Container-Image. Jobs derselben Stage laufen parallel, die
Stages nacheinander.

!!! tip "Erst lokal prüfen"
    [`actionlint`](actionlint.md), [`yamllint`](yamllint.md) und [`pre-commit`](pre-commit.md)
    finden die meisten Fehler in Sekunden, bevor überhaupt eine Pipeline startet. Das spart
    viele „fix CI“-Commits.

!!! danger "Geheimnisse gehören in die Plattform, nicht ins Repository"
    Ein Passwort in einer Workflow-Datei steht für immer im Git-Verlauf und ist für alle
    sichtbar, die das Repository lesen dürfen. Leg es als Secret oder CI/CD-Variable ab.
    GitHub und GitLab blenden solche Werte in den Logs aus.
