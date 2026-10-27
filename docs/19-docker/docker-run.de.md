# docker run

> Erzeugt aus einem Image einen Container und startet ihn.

![docker-run output](../assets/screenshots/19-docker/docker-run.png)

## Syntax

```bash
docker run [OPTIONEN] IMAGE [BEFEHL [ARG...]]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-d`, `--detach` | Im Hintergrund laufen lassen und die Container-ID ausgeben |
| `--name NAME` | Name des Containers, sonst wählt Docker einen zufälligen |
| `-p HOST:CONTAINER` | Einen Port veröffentlichen, etwa `-p 8080:80` |
| `-v QUELLE:ZIEL[:ro]` | Ein Volume oder ein Host-Verzeichnis einhängen |
| `-e NAME=WERT` | Eine Umgebungsvariable setzen |
| `--restart REGEL` | Automatisch neu starten: `no`, `on-failure`, `always`, `unless-stopped` |
| `--rm` | Den Container löschen, sobald er stoppt |
| `-it` | Interaktiv mit Terminal, für eine Shell im Container |
| `--network NAME` | Den Container mit diesem Netzwerk verbinden |

## Beispiele

**nginx im Hintergrund starten:**

```bash
docker run -d --name web -p 8080:80 --restart unless-stopped nginx:1.28
```

```text
0d306f9f64bf095289aac92fd5543790da5bff50734f905a8073759a819f9d2e
```

Die lange Zeichenkette ist die ID des neuen Containers. nginx antwortet jetzt auf Port 8080 des Servers.

**Eine Datenbank mit einem Volume für ihre Daten:**

```bash
docker run -d --name db -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data postgres:17
```

```text
f1971ec6019cd6b63bec27e35dd69ceae4e9504716d98e74ba691b6989040cae
```

**Einen Befehl einmal ausführen und den Container entfernen:**

```bash
docker run --rm debian:trixie cat /etc/debian_version
```

```text
13.1
```

**Eine Shell in einem frischen Container:**

```bash
docker run --rm -it ubuntu:24.04 bash
```

```text
root@5c1e8d3a7f20:/# cat /etc/lsb-release | tail -1
DISTRIB_DESCRIPTION="Ubuntu 24.04.3 LTS"
root@5c1e8d3a7f20:/# exit
```

`exit` beendet die Shell, und `--rm` löscht den Container sofort.

**Beim ersten Start wird das Image heruntergeladen:**

```bash
docker run hello-world
```

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
Digest: sha256:11a3eb1597e864c51b3f56733cb2e8a90bf0c284bfc05f9444d81c558bc848aa
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

## Wann brauche ich das?

- Um einen Dienst wie einen Webserver oder eine Datenbank im Container zu starten
- Um ein Werkzeug oder eine andere Distribution auszuprobieren, ohne etwas zu installieren
- Um eine einmalige Aufgabe, etwa einen Datenbank-Dump, in einem frischen Container auszuführen

!!! tip "Neustart nach einem Reboot"
    Ohne `--restart` bleibt ein Container nach dem Neustart des Servers gestoppt. Nimm für
    Dienste `--restart unless-stopped`.

!!! warning "Ports umgehen die Firewall"
    Mit `-p` veröffentlichte Ports trägt Docker direkt in den Paketfilter ein, an den Regeln
    von `ufw` und `firewalld` vorbei. Binde Ports, die nur der Host braucht, an localhost:
    `-p 127.0.0.1:5432:5432`.

## Verwandte Befehle

[docker ps](docker-ps.md) · [docker logs](docker-logs.md) · [docker stop](docker-stop.md) · [docker compose](docker-compose.md)
