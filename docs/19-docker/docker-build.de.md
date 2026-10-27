# docker build

> Baut aus einem Dockerfile und den Dateien eines Verzeichnisses ein Image.

![docker-build output](../assets/screenshots/19-docker/docker-build.png)

## Syntax

```bash
docker build [OPTIONEN] VERZEICHNIS
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `VERZEICHNIS` | Build-Kontext: das Verzeichnis mit dem Dockerfile und den Dateien, die es kopiert, oft `.` |
| `-t`, `--tag NAME:TAG` | Name und Version des neuen Images, auch mehrfach möglich |
| `-f`, `--file DATEI` | Ein anderes Dockerfile verwenden |
| `--no-cache` | Jeden Schritt neu bauen, statt frühere Ergebnisse zu nutzen |
| `--pull` | Immer die neueste Version des Basis-Images holen |
| `--build-arg NAME=WERT` | Einen Wert für ein `ARG` im Dockerfile setzen |
| `--progress plain` | Einfache Ausgabe mit allen Zeilen, praktisch für Logs und Fehler |

## Beispiele

**Ein Image aus dem aktuellen Verzeichnis bauen:**

```bash
cd ~/status-page
docker build -t status-page:1.0 .
```

```text
[+] Building 2.1s (7/7) FINISHED                                 docker:default
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 145B                                       0.0s
 => [internal] load metadata for docker.io/library/nginx:1.28              0.0s
 => [internal] load .dockerignore                                          0.1s
 => => transferring context: 2B                                            0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 84B                                           0.0s
 => [1/2] FROM docker.io/library/nginx:1.28@sha256:146adea4768b83c607d0bd  1.4s
 => [2/2] COPY index.html /usr/share/nginx/html/                           0.4s
 => exporting to image                                                     0.4s
 => => naming to docker.io/library/status-page:1.0                         0.0s
 => => unpacking to docker.io/library/status-page:1.0                      0.1s
```

**Das Dockerfile dazu:**

```bash
cat ~/status-page/Dockerfile
```

```text
FROM nginx:1.28
COPY index.html /usr/share/nginx/html/
HEALTHCHECK CMD curl -fs http://localhost/ || exit 1
```

**Nach einer Änderung neu bauen, mit Cache:**

```bash
docker build -t status-page:1.1 .
```

```text
[+] Building 1.1s (7/7) FINISHED                                 docker:default
 => [internal] load build definition from Dockerfile                       0.1s
 => [internal] load build context                                          0.1s
 => => transferring context: 86B                                           0.0s
 => CACHED [1/2] FROM docker.io/library/nginx:1.28@sha256:146adea4768b83c  0.1s
 => [2/2] COPY index.html /usr/share/nginx/html/                           0.1s
 => exporting to image                                                     0.4s
 => => naming to docker.io/library/status-page:1.1                         0.0s
```

`CACHED` heißt, dass Docker das Ergebnis dieses Schritts wiederverwendet. Nur die Schritte ab der ersten Änderung laufen neu.

**Das Image gleich für die eigene Registry taggen:**

```bash
docker build -q -t registry.example.com/nox/status-page:1.1 .
```

```text
sha256:807c3828e0a86c119b6fc13680f7d9e2c08b7a5e4f1d3c6b9a2e8f0d4c7b1a35
```

## Wann brauche ich das?

- Um eine eigene Anwendung oder einen angepassten Dienst als Image zu verpacken
- Um einem offiziellen Image deine Konfiguration oder Zertifikate hinzuzufügen
- In einer CI/CD-Pipeline, die bei jeder Änderung ein Image baut

!!! tip "Den Build-Kontext klein halten"
    Docker schickt das ganze Verzeichnis an den Build. Eine Datei `.dockerignore` (gleiche
    Syntax wie `.gitignore`) hält `.git`, Logs und andere große Dateien heraus.

!!! danger "Keine Geheimnisse ins Image"
    Jede Datei, die du mit `COPY` kopierst, bleibt im Image, auch wenn ein späterer Schritt
    sie löscht. Wer das Image holen kann, kann sie lesen. Übergib Passwörter und Schlüssel
    erst zur Laufzeit.

## Verwandte Befehle

[docker images](docker-images.md) · [docker push](docker-push.md) · [docker run](docker-run.md) · [docker compose](docker-compose.md)
