# Docker verstehen

Ein Container betreibt einen Dienst mit allem, was er braucht (Bibliotheken, Konfiguration,
Laufzeitumgebung), abgeschottet vom Rest des Systems, aber ohne den Aufwand einer virtuellen
Maschine. Alle Container teilen sich den Kernel des Hosts.

## Image und Container

| Begriff | Was es ist | Vergleichbar mit |
|---------|------------|------------------|
| **Image** | Schreibgeschützte Vorlage: ein Dateisystem plus der Befehl zum Starten | Ein Paket oder ein Installationsmedium |
| **Container** | Eine laufende (oder gestoppte) Instanz eines Images mit eigener beschreibbarer Schicht | Ein laufender Prozess |
| **Registry** | Server, der Images speichert, etwa Docker Hub oder eine eigene Registry | Ein Paket-Repository |
| **Volume** | Von Docker verwalteter Speicher, der den Container überlebt | Eine eingehängte Festplatte |

Aus einem Image startest du beliebig viele Container. Löschst du einen Container, ist alles
weg, was er geschrieben hat, außer dem, was in einem Volume liegt.

## Installation

Die Pakete der Distributionen sind oft älter und heißen anders. Auf Servern ist das
offizielle Repository von Docker die übliche Wahl. Der Beispielserver `tuxdex-srv` nutzt
Docker CE von dort, siehe [docs.docker.com/engine/install](https://docs.docker.com/engine/install/).

```text
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
$ sudo systemctl enable --now docker
$ sudo docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Um ohne `sudo` zu arbeiten, nimm deinen Benutzer in die Gruppe `docker` auf und melde dich
neu an: `sudo usermod -aG docker nox`.

## Ports und Volumes

```text
docker run -d --name web -p 8080:80 -v /srv/www:/usr/share/nginx/html:ro nginx:1.28
                          ─────┬───  ──────────────────┬──────────────────
                               │                       └─ Host-Verzeichnis : Container-Verzeichnis (nur lesend)
                               └─ Host-Port : Container-Port
```

| Art des Speichers | Beispiel | Wofür |
|-------------------|----------|-------|
| Benanntes Volume | `-v pgdata:/var/lib/postgresql/data` | Daten von Datenbanken und Diensten, von Docker verwaltet |
| Bind Mount | `-v /srv/www:/usr/share/nginx/html:ro` | Dateien, die du auf dem Host bearbeitest, etwa Konfiguration oder eine Website |

## Ein Dockerfile

Ein `Dockerfile` beschreibt Schritt für Schritt, wie ein Image gebaut wird:

```text
FROM nginx:1.28
COPY index.html /usr/share/nginx/html/
HEALTHCHECK CMD curl -fs http://localhost/ || exit 1
```

[`docker build`](docker-build.md) macht daraus ein Image.

## Eine compose.yaml

Für Dienste aus mehreren Containern beschreibt eine `compose.yaml` alles in einer Datei.
`/srv/status/compose.yaml`:

```text
services:
  web:
    image: nginx:1.28
    ports:
      - "8080:80"
    restart: unless-stopped
  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - dbdata:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  dbdata:
```

[`docker compose up -d`](docker-compose.md) startet beide Container, ein gemeinsames Netzwerk
und das Volume. Die Container erreichen sich gegenseitig über ihre Dienstnamen, hier `web`
und `db`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket der Distribution | `docker.io` | `docker.io` | keins, stattdessen `podman` | `docker` |
| Offizielles Docker-Repository | ja (`docker-ce`) | ja (`docker-ce`) | ja (`docker-ce`) | nein |
| Compose | `docker-compose-plugin` | `docker-compose-plugin` | `docker-compose-plugin` | `docker-compose` |
| Alternative | `podman` | `podman` | `podman` (von Red Hat bevorzugt) | `podman` |

!!! tip "Die Image-Version festlegen"
    `nginx:1.28` ist vorhersehbar, `nginx` (also `nginx:latest`) kann nach dem nächsten Pull
    eine neue Hauptversion sein. Nutze auf Servern immer einen Versions-Tag.

!!! danger "Die Gruppe docker ist root"
    Wer in der Gruppe `docker` ist, kann einen Container starten, der `/` des Hosts einhängt,
    und hat damit volle Root-Rechte. Nimm nur vertrauenswürdige Admins in diese Gruppe auf.
