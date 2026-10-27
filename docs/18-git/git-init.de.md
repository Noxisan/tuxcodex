# git init

> Legt in einem Verzeichnis ein neues, leeres Git-Repository an.

![git-init output](../assets/screenshots/18-git/git-init.png)

## Syntax

```bash
git init [-b BRANCH] [--bare] [VERZEICHNIS]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `VERZEICHNIS` | Das Repository dort anlegen (wird bei Bedarf erstellt), sonst im aktuellen Verzeichnis |
| `-b NAME`, `--initial-branch=NAME` | Name des ersten Branches, zum Beispiel `main` |
| `--bare` | Repository ohne Arbeitsverzeichnis, als zentrales Repository auf einem Server |
| `-q`, `--quiet` | Keine Ausgabe |

## Beispiele

**Ein Repository für deine Skripte anlegen:**

```bash
git init scripts
```

```text
Initialized empty Git repository in /home/nox/scripts/.git/
```

**Ein bestehendes Verzeichnis versionieren:**

```bash
cd /etc/nginx
sudo git init
sudo git add .
sudo git commit -m "Initial nginx configuration"
```

```text
Initialized empty Git repository in /etc/nginx/.git/
[main (root-commit) 2b8e0d4] Initial nginx configuration
 14 files changed, 412 insertions(+)
 create mode 100644 conf.d/default.conf
 create mode 100644 fastcgi_params
 create mode 100644 mime.types
 create mode 100644 nginx.conf
 ...
```

**Den Namen des ersten Branches festlegen:**

```bash
git init -b main monitoring
```

```text
Initialized empty Git repository in /home/nox/monitoring/.git/
```

**Ein zentrales Repository auf dem eigenen Server:**

```bash
sudo git init --bare /srv/git/scripts.git
sudo chown -R nox: /srv/git/scripts.git
```

```text
Initialized empty Git repository in /srv/git/scripts.git/
```

Andere klonen es per SSH mit `git clone nox@tuxdex-srv:/srv/git/scripts.git`.

## Wann brauche ich das?

- Um eine neue Skriptsammlung mit Versionsverlauf zu beginnen
- Um ein bestehendes Konfigurationsverzeichnis wie `/etc/nginx` zu versionieren
- Um auf dem eigenen Server ein zentrales Repository einzurichten, das andere per SSH klonen

!!! tip "Name des ersten Branches"
    Ist `init.defaultBranch` nicht gesetzt, nennt Git den ersten Branch `master` und gibt
    einen langen Hinweis aus. Setze einmal `git config --global init.defaultBranch main`
    oder nutze `-b main`.

!!! warning ".git in Systemverzeichnissen schützen"
    Das Verzeichnis `.git` enthält jede alte Version jeder Datei, auch von Dateien, deren
    Rechte du später eingeschränkt hast. In `/etc` und ähnlichen Orten sollte nur root es
    lesen dürfen: `sudo chmod 700 /etc/nginx/.git`.

## Verwandte Befehle

[git clone](git-clone.md) · [git config](git-config.md) · [git status](git-status.md) · [git remote](git-remote.md)
