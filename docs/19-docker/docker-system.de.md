# docker system

> Zeigt, wie viel Platz Docker belegt, und räumt gestoppte Container, ungenutzte Images, Netzwerke und den Build-Cache auf.

![docker-system output](../assets/screenshots/19-docker/docker-system.png)

## Syntax

```bash
docker system df [-v]
docker system prune [-a] [--volumes] [-f]
docker system info
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `df` | Belegter Platz durch Images, Container, Volumes und Build-Cache |
| `df -v` | Dasselbe, aufgeschlüsselt nach Image, Container und Volume |
| `prune` | Gestoppte Container, ungenutzte Netzwerke, namenlose Images und den Build-Cache löschen |
| `prune -a` | Auch alle Images löschen, die kein Container nutzt |
| `prune --volumes` | Auch ungenutzte anonyme Volumes löschen |
| `-f`, `--force` | Nicht nachfragen |
| `info` | Überblick über die Docker-Installation: Version, Speichertreiber, Anzahl der Container |

## Beispiele

**Sehen, wie viel Platz Docker belegt:**

```bash
docker system df
```

```text
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         2         1.355GB   473.2MB (34%)
Containers      3         2         4.096kB   63B (1%)
Local Volumes   2         2         79.98MB   0B (0%)
Build Cache     6         0         1.2kB     1.2kB
```

RECLAIMABLE ist, was `docker system prune -a` freigeben könnte.

**Aufräumen:**

```bash
docker system prune
```

```text
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
7b2e91c4d0a3c5f18e6d2b4a9f0c3e7d1b5a8f2c6e4d0b9a3f7c1e5d8b2a6f04

Deleted Networks:
backend

Deleted build cache objects:
wkc9ai887k3osdzs7fehpx8mq
vtck2exxroz70diuwiw6hluh8
4shp7pqvwo9swmcs9qtiaeeie

Total reclaimed space: 8.255kB
```

**Auch alle ungenutzten Images entfernen, ohne Nachfrage:**

```bash
docker system prune -a -f
```

```text
Deleted Images:
untagged: nginx:1.27
deleted: sha256:5ed8fcc66f4ed123c9e4a7c15a1c8b0e6d2f9a4b7c3e8d1f5a0b6c2e9d4f7a18
untagged: status-page:1.0
deleted: sha256:ffca3ce5b5cf86259c01a40d9b80f53639c1feaed663882b7a3ab8ee30c75693

Total reclaimed space: 473.2MB
```

**Eckdaten der Installation:**

```bash
docker system info -f "{{.ServerVersion}}, {{.Driver}}, {{.Containers}} containers, {{.DockerRootDir}}"
```

```text
29.9.2, overlayfs, 3 containers, /var/lib/docker
```

## Wann brauche ich das?

- Wenn `/var/lib/docker` die Platte füllt
- Als regelmäßige Aufräumarbeit auf Build-Servern
- Um die Docker-Installation und ihre Einstellungen zu prüfen

!!! tip "Regelmäßig aufräumen"
    Jedes Update lässt das alte Image zurück. Ein wöchentliches
    `docker image prune -a -f --filter until=168h` als Cronjob entfernt Images, die länger
    als eine Woche ungenutzt sind.

!!! warning "prune -a entfernt Images gestoppter Stacks"
    `docker system prune -a` löscht auch die Images von Containern, die gerade gestoppt
    sind. Sie werden beim nächsten Start neu heruntergeladen. Das dauert und setzt voraus,
    dass die Registry erreichbar ist.

## Verwandte Befehle

[docker images](docker-images.md) · [docker rmi](docker-rmi.md) · [docker volume](docker-volume.md) · [df](../13-disks-storage/df.md)
