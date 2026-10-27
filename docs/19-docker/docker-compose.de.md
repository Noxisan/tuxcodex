# docker compose

> Startet, aktualisiert und stoppt einen ganzen Stack von Containern, der in einer compose.yaml beschrieben ist.

![docker-compose output](../assets/screenshots/19-docker/docker-compose.png)

## Syntax

```bash
docker compose [-f DATEI] BEFEHL [OPTIONEN] [DIENST...]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `up -d` | Alle Dienste im Hintergrund anlegen und starten; geänderte Dienste werden neu angelegt |
| `down` | Die Container und das Netzwerk stoppen und entfernen (Volumes bleiben, außer mit `-v`) |
| `ps` | Die Container des Projekts zeigen |
| `logs [-f] [DIENST]` | Die Ausgabe aller oder einzelner Dienste zeigen |
| `pull` | Neuere Versionen der Images herunterladen |
| `restart [DIENST]` | Dienste neu starten |
| `exec DIENST BEFEHL` | Einen Befehl im Container eines Dienstes ausführen |
| `config` | Die Datei prüfen und die vollständige Konfiguration zeigen |
| `-f DATEI` | Eine andere Datei statt `compose.yaml` im aktuellen Verzeichnis |

## Beispiele

**Den Stack aus der compose.yaml starten:**

```bash
cd /srv/status
docker compose up -d
```

```text
[+] up 4/4
 ✔ Network status_default Created                                           0.0s
 ✔ Volume status_dbdata   Created                                           0.0s
 ✔ Container status-web-1 Started                                           0.3s
 ✔ Container status-db-1  Started                                           0.5s
```

Compose benennt alles nach dem Verzeichnis (`status`) und dem Dienst. Die Datei selbst steht in den [Grundlagen](basics.md).

**Die Container des Projekts:**

```bash
docker compose ps
```

```text
NAME           IMAGE         COMMAND                  SERVICE   CREATED         STATUS         PORTS
status-db-1    postgres:17   "docker-entrypoint.s…"   db        2 minutes ago   Up 2 minutes   5432/tcp
status-web-1   nginx:1.28    "/docker-entrypoint.…"   web       2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
```

**Die Logs aller Dienste:**

```bash
docker compose logs --tail 2
```

```text
web-1  | 2026/10/26 09:40:05 [notice] 1#1: start worker process 29
web-1  | 2026/10/26 09:40:05 [notice] 1#1: start worker process 30
db-1   | 2026-10-26 09:40:07.102 UTC [1] LOG:  database system is ready to accept connections
db-1   | 2026-10-26 09:40:07.104 UTC [62] LOG:  database system was shut down at 2026-10-26 09:40:06 UTC
```

**Alle Dienste aktualisieren:**

```bash
docker compose pull
docker compose up -d
```

```text
[+] pull 2/2
 ✔ Image postgres:17 Pulled                                                 1.7s
 ✔ Image nginx:1.28  Pulled                                                 1.6s
[+] up 2/2
 ✔ Container status-db-1  Running                                           0.0s
 ✔ Container status-web-1 Recreated                                         0.4s
```

Nur `web` hatte ein neues Image, deshalb wurde nur sein Container neu angelegt. `db` lief einfach weiter.

**Den Stack stoppen und entfernen:**

```bash
docker compose down
```

```text
[+] down 3/3
 ✔ Container status-db-1  Removed                                           0.5s
 ✔ Container status-web-1 Removed                                           0.4s
 ✔ Network status_default Removed                                           0.1s
```

Das Volume `status_dbdata` bleibt erhalten, die Datenbank ist beim nächsten `up` also wieder da.

## Wann brauche ich das?

- Für jeden Dienst, der aus mehr als einem Container besteht, etwa eine Anwendung mit Datenbank
- Um den Aufbau eines Servers in einer Datei zu dokumentieren, die ins Git-Repository kann
- Um alle Container eines Stacks mit zwei Befehlen zu aktualisieren

!!! tip "Einen Stack aktualisieren"
    `docker compose pull` und danach `docker compose up -d` bringt alle Dienste auf das
    neueste Image ihres Tags. Neu angelegt werden nur Container, deren Image oder
    Konfiguration sich geändert hat.

!!! warning "docker-compose mit Bindestrich ist die alte Version"
    `docker-compose` (mit Bindestrich) ist Compose Version 1, die nicht mehr gepflegt wird.
    Aktuell ist das Plugin `docker compose` (mit Leerzeichen). Die `compose.yaml`-Dateien
    sind weitgehend gleich.

!!! danger "down -v löscht die Daten"
    `docker compose down -v` löscht auch die Volumes des Projekts und damit die Datenbank.
    Lass `-v` weg, außer du willst wirklich bei null anfangen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Befehl | `docker compose` (`docker-compose-plugin`) | `docker compose` (`docker-compose-plugin`) | `docker compose` (`docker-compose-plugin`) oder `podman compose` | `docker compose` (`docker-compose`) |

## Verwandte Befehle

[docker run](docker-run.md) · [docker pull](docker-pull.md) · [docker logs](docker-logs.md) · [docker volume](docker-volume.md)
