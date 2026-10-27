# Understanding CI/CD

**CI** (continuous integration) means: every push is checked automatically, by linters,
tests and a build. **CD** (continuous delivery or deployment) goes one step further and
rolls out what passed the checks, for example to `tuxdex-srv`. Instead of "I'll deploy
it later by hand", every change takes the same tested route.

```text
git push ──► lint ──► test ──► build image ──► deploy to the server
              │        │           │                  │
              └────────┴───────────┴── stops at the first error
```

## The terms

| Term | GitHub Actions | GitLab CI | Meaning |
|------|----------------|-----------|---------|
| Definition | `.github/workflows/*.yml` | `.gitlab-ci.yml` | The pipeline as a YAML file in the repository |
| Pipeline | Workflow run | Pipeline | One run, triggered by a push, a merge request or a schedule |
| Job | Job | Job | A group of steps on one runner; jobs can depend on each other |
| Step | Step | `script` line | A single command or a ready-made action |
| Runner | GitHub-hosted or self-hosted runner | Shared or own `gitlab-runner` | The machine that runs the jobs |
| Secret | Secret | CI/CD variable (masked, protected) | Passwords and keys, never in the YAML file |
| Artifact | Artifact | Artifact | Files a job hands on, such as a built package |

## What you need to install

None of these tools is needed for the pipeline itself: it runs on GitHub or GitLab. They
help you to watch and control pipelines from the terminal and to find mistakes before the
push.

| Tool | For | Debian | Ubuntu | RHEL | Arch |
|------|-----|--------|--------|------|------|
| [`gh`](gh-run.md) | GitHub | `sudo apt install gh` | `sudo apt install gh` | repository `cli.github.com`, then `sudo dnf install gh` | `sudo pacman -S github-cli` |
| [`act`](act.md) | GitHub, local runs | install script from nektos/act | install script from nektos/act | install script from nektos/act | `sudo pacman -S act` |
| [`actionlint`](actionlint.md) | GitHub | release binary from GitHub | release binary from GitHub | release binary from GitHub | release binary from GitHub |
| [`glab`](glab-ci.md) | GitLab | `sudo apt install glab` | `sudo apt install glab` | `.rpm` from the glab releases | `sudo pacman -S glab` |
| [`gitlab-runner`](gitlab-runner.md) | GitLab, own runner | repository `packages.gitlab.com` | repository `packages.gitlab.com` | repository `packages.gitlab.com` | `sudo pacman -S gitlab-runner` |
| [`yamllint`](yamllint.md) | all YAML | `sudo apt install yamllint` | `sudo apt install yamllint` | `sudo dnf install yamllint` (EPEL) | `sudo pacman -S yamllint` |
| [`pre-commit`](pre-commit.md) | Git hooks | `sudo apt install pre-commit` | `sudo apt install pre-commit` | `pipx install pre-commit` | `sudo pacman -S pre-commit` |

The `gh` package of Debian and Ubuntu is often a few versions behind. The repository at
`cli.github.com` has the current version for Debian and Ubuntu too.

## A workflow for GitHub Actions

`.github/workflows/ci.yml` checks the shell scripts on every push and then builds the
Docker image from the [Docker chapter](../19-docker/docker-build.md):

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

`needs: lint` makes `build` wait for `lint` and skips it if `lint` fails.

## Deploying to your own server

A deploy job logs in to the server over SSH with a key that is stored as a secret:

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

On the server, the user `deploy` gets its own key with a restricted `authorized_keys` entry,
see [`ssh-keygen`](../12-ssh/ssh-keygen.md). The secrets are set with
[`gh secret`](gh-secret.md).

## The same for GitLab CI

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

Each job runs in the given container image. Jobs of the same stage run in parallel, the
stages one after the other.

!!! tip "Check locally first"
    [`actionlint`](actionlint.md), [`yamllint`](yamllint.md) and [`pre-commit`](pre-commit.md)
    find most mistakes in seconds, before a pipeline even starts. That saves a lot of
    "fix CI" commits.

!!! danger "Secrets belong in the platform, not in the repository"
    A password in a workflow file is in the Git history forever and visible to everyone who
    can read the repository. Store it as a secret or CI/CD variable. GitHub and GitLab hide
    such values in the logs.
