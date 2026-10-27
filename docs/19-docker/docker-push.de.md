# docker push

> Lädt ein Image in eine Registry hoch, etwa Docker Hub, GitLab oder eine eigene Registry.

![docker-push output](../assets/screenshots/19-docker/docker-push.png)

## Syntax

```bash
docker push NAME[:TAG]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `NAME:TAG` | Das Image; der Name muss mit der Adresse der Registry beginnen, etwa `registry.example.com/nox/…` |
| `-a`, `--all-tags` | Alle Tags des Images hochladen |
| `-q`, `--quiet` | Weniger Ausgabe |

Melde dich vor dem ersten Push mit `docker login registry.example.com` an. `docker tag QUELLE ZIEL` gibt einem vorhandenen Image einen zusätzlichen Namen.

## Beispiele

**Dem Image einen Namen mit Registry geben und hochladen:**

```bash
docker tag status-page:1.0 registry.example.com/nox/status-page:1.0
docker push registry.example.com/nox/status-page:1.0
```

```text
The push refers to repository [registry.example.com/nox/status-page]
f176d5d8a1c1: Pushed
63ef37274310: Pushed
eeb54fe99e2e: Pushed
4744f2344932: Pushed
44136fa355b3: Pushed
6a7080264fc9: Pushed
5435b2dcdf5c: Pushed
f2981f9e7841: Pushed
39a24e95a1e9: Pushed
400f8ac367e0: Pushed
1.0: digest: sha256:ffca3ce5b5cf86259c01a40d9b80f53639c1feaed663882b7a3ab8ee30c75693 size: 856
```

**Bei der Registry anmelden:**

```bash
docker login registry.example.com -u nox
```

```text
Password:

WARNING! Your credentials are stored unencrypted in '/home/nox/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded
```

**Eine neue Version: Nur die geänderte Schicht wird hochgeladen:**

```bash
docker push registry.example.com/nox/status-page:1.1
```

```text
The push refers to repository [registry.example.com/nox/status-page]
f176d5d8a1c1: Layer already exists
63ef37274310: Layer already exists
4744f2344932: Layer already exists
6a7080264fc9: Layer already exists
5435b2dcdf5c: Layer already exists
39a24e95a1e9: Layer already exists
400f8ac367e0: Layer already exists
a8c51e2d7f93: Pushed
1.1: digest: sha256:807c3828e0a86c119b6fc13680f7d9e2c08b7a5e4f1d3c6b9a2e8f0d4c7b1a35 size: 856
```

**Ohne vorherige Anmeldung:**

```bash
docker push registry.example.com/nox/status-page:1.1
```

```text
The push refers to repository [registry.example.com/nox/status-page]
push access denied, repository does not exist or may require authorization: authorization failed: no basic auth credentials
```

## Wann brauche ich das?

- Um ein eigenes Image anderen Servern zur Verfügung zu stellen
- Um aus einer CI/CD-Pipeline heraus eine Version zu veröffentlichen
- Um eine Kopie eines selbst gebauten Images aufzubewahren

!!! tip "Versions-Tags pushen, nicht nur latest"
    Push jedes Image mit einer festen Version, etwa `1.1`. Dann wählen Server genau aus,
    welche Version sie betreiben, und du kannst zur vorherigen zurück.

!!! warning "Zugangsdaten auf dem Server"
    `docker login` speichert die Zugangsdaten in `~/.docker/config.json`, standardmäßig nur
    base64-kodiert. Nimm auf Servern, die nur abholen, ein Access Token mit Lesezugriff.

## Verwandte Befehle

[docker build](docker-build.md) · [docker pull](docker-pull.md) · [docker images](docker-images.md) · [docker rmi](docker-rmi.md)
