# podman

> Betreibt Container wie Docker, aber ohne Hintergrunddienst und auch ohne root. Unter RHEL ist es das Standardwerkzeug für Container.

![podman output](../assets/screenshots/19-docker/podman.png)

## Syntax

```bash
podman BEFEHL [OPTIONEN]
```

Fast alle `docker`-Befehle funktionieren mit `podman` genauso: `podman run`, `podman ps`, `podman logs`, `podman build` und so weiter.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `run`, `ps`, `logs`, `exec`, `stop`, `rm` | Wie die `docker`-Befehle dieses Kapitels |
| `images`, `pull`, `build`, `push`, `rmi` | Wie bei Docker |
| `pod create` | Einen Pod anlegen: mehrere Container mit gemeinsamem Netzwerk, wie bei Kubernetes |
| `generate systemd` | Eine systemd-Unit für einen Container erzeugen (veraltet, Nachfolger ist Quadlet) |
| `compose` | Eine `compose.yaml` ausführen (nutzt im Hintergrund `podman-compose` oder `docker-compose`) |
| `auto-update` | Container aktualisieren, deren Image eine neue Version hat |

## Beispiele

**nginx als normaler Benutzer starten:**

```bash
podman run -d --name web -p 8080:80 docker.io/library/nginx:1.28
podman ps
```

```text
a47a82367aa6f0a8d5939cc7e245c14232df60f6aa23b4e5434daf8ff563f202
CONTAINER ID  IMAGE                         COMMAND               CREATED        STATUS        PORTS                 NAMES
a47a82367aa6  docker.io/library/nginx:1.28  nginx -g daemon o...  2 seconds ago  Up 2 seconds  0.0.0.0:8080->80/tcp  web
```

**Ein Image herunterladen:**

```bash
podman pull docker.io/library/postgres:17
```

```text
Trying to pull docker.io/library/postgres:17...
Getting image source signatures
Copying blob sha256:99b43abe6052d4e1c8f5a6b2e7d3c9f0a4b8e1d5c2f7a3b6e9d0c4f8a1b5e2d7
Copying blob sha256:bee16f784947a2c5e8d1f4b7a0c3e6d9f2b5a8c1e4d7f0a3b6c9e2d5f8a1b4c7
...
Copying config sha256:b8faeff7712663c2773a190181e1246e37e364b887611c04658c28b44e2408fe
Writing manifest to image destination
b8faeff7712663c2773a190181e1246e37e364b887611c04658c28b44e2408fe
```

**Die Images deines Benutzers:**

```bash
podman images
```

```text
REPOSITORY                  TAG         IMAGE ID      CREATED      SIZE
docker.io/library/postgres  17          b8faeff77126  3 weeks ago  465 MB
docker.io/library/nginx     1.28        fda7399e8104  6 weeks ago  164 MB
```

**Ein Container als systemd-Dienst mit Quadlet:**

```bash
cat /etc/containers/systemd/web.container
sudo systemctl daemon-reload
sudo systemctl start web
systemctl is-active web
```

```text
[Container]
Image=docker.io/library/nginx:1.28
PublishPort=8080:80

[Install]
WantedBy=multi-user.target
active
```

## Wann brauche ich das?

- Unter RHEL, Rocky und Alma, wo Docker nicht zur Distribution gehört
- Wenn Benutzer Container ohne Root-Rechte und ohne die Gruppe `docker` betreiben sollen
- Um Container mit Quadlet als normale systemd-Dienste zu betreiben

!!! tip "Immer volle Image-Namen nutzen"
    Nimm `docker.io/library/nginx:1.28` statt `nginx:1.28`. Ohne Registry im Namen fragt
    Podman, welche Registry es nehmen soll, oder bricht mit `short-name ... did not resolve`
    ab.

!!! tip "Quadlet statt Compose"
    Aus einer Datei `/etc/containers/systemd/web.container` mit `[Container]`, `Image=` und
    `PublishPort=` wird nach `systemctl daemon-reload` der systemd-Dienst `web.service`.
    Dann funktionieren `systemctl start web` und `journalctl -u web` wie bei jedem anderen
    Dienst.

!!! warning "Rootless-Container und niedrige Ports"
    Container eines normalen Benutzers können keine Ports unter 1024 öffnen. Nimm einen
    höheren Port wie `-p 8080:80` oder starte den Container als root.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install podman` | `sudo apt install podman` | `sudo dnf install podman` | `sudo pacman -S podman` |
| Docker in der Distribution | ja (`docker.io`) | ja (`docker.io`) | nein, Podman ist der Standard | ja (`docker`) |

## Verwandte Befehle

[docker run](docker-run.md) · [docker compose](docker-compose.md) · [systemctl](../09-systemd/systemctl.md) · [docker ps](docker-ps.md)
