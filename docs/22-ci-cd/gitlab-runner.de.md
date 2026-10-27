# gitlab-runner

> Führt die Jobs von GitLab-CI-Pipelines auf dem eigenen Server aus, in Docker-Containern oder direkt in einer Shell.

![gitlab-runner output](../assets/screenshots/22-ci-cd/gitlab-runner.png)

## Syntax

```bash
gitlab-runner register | list | verify | unregister | status | run [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `register` | Den Runner mit einer GitLab-Instanz verbinden (mit einem Runner-Token aus der Weboberfläche) |
| `--url URL`, `--token TOKEN` | Adresse von GitLab und das Runner-Token (`glrt-…`) |
| `--executor docker` | Jeden Job in einem Container ausführen (`shell` führt ihn direkt auf dem Host aus) |
| `--docker-image IMAGE` | Standard-Image für Jobs ohne `image:` |
| `--non-interactive` | Nicht nachfragen, alles aus den Optionen nehmen |
| `list` | Die registrierten Runner aus `/etc/gitlab-runner/config.toml` |
| `verify` | Prüfen, ob die Runner GitLab noch erreichen |
| `unregister --name NAME` | Einen Runner entfernen |

Der Runner selbst läuft als systemd-Dienst `gitlab-runner`. Seine Konfiguration steht in `/etc/gitlab-runner/config.toml`.

## Beispiele

**Einen Runner mit dem Docker-Executor registrieren:**

```bash
sudo gitlab-runner register --non-interactive \
  --url https://gitlab.example.com --token glrt-t3_Xq7mP2vKzR9wLc4N8aYb \
  --executor docker --docker-image debian:trixie --description tuxcodex-srv
```

```text
Runtime platform                                    arch=amd64 os=linux pid=24817 revision=f411f264 version=19.5.1
Running in system-mode.

Verifying runner... is valid                        correlation_id=01JB8M4X2Q5R7T9V3W6Y8Z0A1C runner=t3_Xq7mP2
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!

Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml"
```

**Die registrierten Runner:**

```bash
sudo gitlab-runner list
```

```text
Runtime platform                                    arch=amd64 os=linux pid=24901 revision=f411f264 version=19.5.1
Listing configured runners                          ConfigFile=/etc/gitlab-runner/config.toml
tuxcodex-srv                                        Executor=docker Token=glrt-t3_Xq7mP2vKzR9wLc4N8aYb URL=https://gitlab.example.com
```

**Prüfen, ob der Runner GitLab noch erreicht:**

```bash
sudo gitlab-runner verify
```

```text
Runtime platform                                    arch=amd64 os=linux pid=24937 revision=f411f264 version=19.5.1
Running in system-mode.

Verifying runner... is valid                        correlation_id=01JB8M6D4F8H1K3M5P7R9T2V4X runner=t3_Xq7mP2
```

**Der Runner als Dienst:**

```bash
systemctl is-active gitlab-runner
gitlab-runner --version | head -2
```

```text
active
Version:      19.5.1
Git revision: f411f264
```

## Wann brauche ich das?

- Wenn Jobs Zugriff auf das eigene Netz brauchen, etwa um auf interne Server auszurollen
- Wenn die Shared Runner zu langsam sind oder die enthaltenen Minuten ausgehen
- Für Jobs, die besondere Hardware oder große Caches brauchen

!!! tip "Tags entscheiden, wo ein Job läuft"
    Registriere den Runner mit Tags wie `--tag-list deploy,internal` und gib Jobs
    `tags: [deploy]`. Dann landen nur diese Jobs auf deinem Runner.

!!! danger "Der Shell-Executor ist root auf deinem Server"
    Mit `--executor shell` läuft jeder Job direkt auf dem Host als Benutzer
    `gitlab-runner`, und wer die `.gitlab-ci.yml` ändern darf, kann Befehle auf deinem Server
    ausführen. Nimm lieber den `docker`-Executor und eigene Runner nur für Projekte, denen du
    vertraust.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | Repository `packages.gitlab.com`, dann `sudo apt install gitlab-runner` | Repository `packages.gitlab.com`, dann `sudo apt install gitlab-runner` | Repository `packages.gitlab.com`, dann `sudo dnf install gitlab-runner` | `sudo pacman -S gitlab-runner` |

## Verwandte Befehle

[glab ci](glab-ci.md) · [docker run](../19-docker/docker-run.md) · [systemctl](../09-systemd/systemctl.md)
