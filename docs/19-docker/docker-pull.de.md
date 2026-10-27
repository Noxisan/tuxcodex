# docker pull

> Lädt ein Image aus einer Registry herunter, standardmäßig von Docker Hub.

![docker-pull output](../assets/screenshots/19-docker/docker-pull.png)

## Syntax

```bash
docker pull [OPTIONEN] NAME[:TAG]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `NAME` | Image-Name, etwa `nginx` oder `registry.example.com/nox/status-page` |
| `:TAG` | Version, etwa `1.28`; ohne Tag wird `latest` genommen |
| `@sha256:…` | Ein exaktes Image über seinen Digest statt eines Tags |
| `-a`, `--all-tags` | Alle Tags des Images herunterladen |
| `-q`, `--quiet` | Nur den Namen des Images ausgeben |
| `--platform PLATTFORM` | Eine andere Architektur, etwa `linux/arm64` |

## Beispiele

**Ein Image mit Versions-Tag herunterladen:**

```bash
docker pull nginx:1.28
```

```text
1.28: Pulling from library/nginx
5435b2dcdf5c: Pull complete
39a24e95a1e9: Pull complete
63ef37274310: Pull complete
400f8ac367e0: Pull complete
4744f2344932: Pull complete
6a7080264fc9: Pull complete
f176d5d8a1c1: Pull complete
Digest: sha256:146adea4768b83c607d0bdfa4188464e3da6e0a3ad4475db1d1d8f64f27c29cc
Status: Downloaded newer image for nginx:1.28
docker.io/library/nginx:1.28
```

**Das Image ist schon aktuell:**

```bash
docker pull nginx:1.28
```

```text
1.28: Pulling from library/nginx
Digest: sha256:146adea4768b83c607d0bdfa4188464e3da6e0a3ad4475db1d1d8f64f27c29cc
Status: Image is up to date for nginx:1.28
docker.io/library/nginx:1.28
```

**Aus der eigenen Registry:**

```bash
docker pull -q registry.example.com/nox/status-page:1.0
```

```text
registry.example.com/nox/status-page:1.0
```

**Ein Image, das es nicht gibt:**

```bash
docker pull nginx:1.82
```

```text
Error response from daemon: failed to resolve reference "docker.io/library/nginx:1.82": docker.io/library/nginx:1.82: not found
```

## Wann brauche ich das?

- Um eine neue Version eines Images zu holen, bevor du einen Container aktualisierst
- Um Images vorab herunterzuladen, damit ein späterer Start nicht warten muss
- Um die Sicherheitsupdates zu holen, die ein neuer Build desselben Tags enthält

!!! tip "Pull allein aktualisiert nichts"
    Laufende Container nutzen weiter das alte Image. Erst wenn du den Container neu anlegst
    (oder `docker compose up -d` ausführst), startet er aus dem neuen Image.

!!! warning "Begrenzte Pulls bei Docker Hub"
    Docker Hub begrenzt die Zahl der Pulls ohne Konto pro IP-Adresse. Auf Servern, die viel
    herunterladen, meldest du dich mit `docker login` an oder nutzt einen Mirror.

## Verwandte Befehle

[docker images](docker-images.md) · [docker run](docker-run.md) · [docker push](docker-push.md) · [docker compose](docker-compose.md)
