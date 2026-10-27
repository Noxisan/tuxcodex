# docker rm

> Löscht gestoppte Container samt allem, was sie außerhalb von Volumes geschrieben haben.

![docker-rm output](../assets/screenshots/19-docker/docker-rm.png)

## Syntax

```bash
docker rm [-f] [-v] CONTAINER...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `CONTAINER` | Name oder ID, mehrere sind möglich |
| `-f`, `--force` | Auch einen laufenden Container entfernen (stoppt ihn mit SIGKILL) |
| `-v`, `--volumes` | Auch die anonymen Volumes des Containers entfernen |

`docker container prune` entfernt alle gestoppten Container auf einmal.

## Beispiele

**Einen gestoppten Container entfernen:**

```bash
docker rm pg-test
```

```text
pg-test
```

**Ein laufender Container lässt sich nicht entfernen:**

```bash
docker rm web
```

```text
Error response from daemon: cannot remove container "web": container is running: stop the container before removing or force remove
```

**In einem Schritt stoppen und entfernen:**

```bash
docker rm -f web
```

```text
web
```

**Alle gestoppten Container entfernen:**

```bash
docker container prune
```

```text
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
7b2e91c4d0a3c5f18e6d2b4a9f0c3e7d1b5a8f2c6e4d0b9a3f7c1e5d8b2a6f04

Total reclaimed space: 63B
```

## Wann brauche ich das?

- Um Container aufzuräumen, die du nicht mehr brauchst
- Um einen Container mit anderen Ports, Volumes oder Variablen neu anzulegen
- Nach einem Image-Update: den alten Container entfernen und aus dem neuen Image einen neuen starten

!!! danger "Daten außerhalb von Volumes sind weg"
    Alles, was ein Container in sein eigenes Dateisystem geschrieben hat, verschwindet mit
    `docker rm`. Prüf mit `docker inspect -f "{{json .Mounts}}" CONTAINER`, dass die
    wichtigen Daten in einem Volume oder Bind Mount liegen.

## Verwandte Befehle

[docker stop](docker-stop.md) · [docker run](docker-run.md) · [docker rmi](docker-rmi.md) · [docker system](docker-system.md)
