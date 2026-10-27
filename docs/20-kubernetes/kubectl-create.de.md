# kubectl create

> Legt ein einzelnes Objekt direkt auf der Kommandozeile an, etwa einen Namespace, ein Secret oder ein Deployment.

![kubectl-create output](../assets/screenshots/20-kubernetes/kubectl-create.png)

## Syntax

```bash
kubectl create TYP NAME [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `namespace NAME` | Einen Namespace anlegen |
| `deployment NAME --image=IMAGE` | Ein Deployment anlegen, mit `--replicas=N` |
| `secret generic NAME --from-literal=SCHLÜSSEL=WERT` | Ein Secret anlegen, auch `--from-file=DATEI` |
| `configmap NAME --from-file=DATEI` | Eine ConfigMap aus einer Datei anlegen |
| `job NAME --image=IMAGE -- BEFEHL` | Einen Befehl einmal ausführen |
| `--dry-run=client -o yaml` | Nichts anlegen, nur das Manifest ausgeben |
| `-f DATEI` | Aus einem Manifest anlegen (scheitert, wenn das Objekt existiert, anders als `apply`) |

## Beispiele

**Einen Namespace und ein Secret anlegen:**

```bash
kubectl create namespace monitoring
kubectl create secret generic db-pass -n status --from-literal=password=secret
```

```text
namespace/monitoring created
secret/db-pass created
```

**Ein Manifest erzeugen, statt das Objekt anzulegen:**

```bash
kubectl create deployment hello --image=nginx:1.28 --dry-run=client -o yaml
```

```text
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: hello
  name: hello
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello
  strategy: {}
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
      - image: nginx:1.28
        name: nginx
        resources: {}
status: {}
```

**Eine Konfigurationsdatei als ConfigMap:**

```bash
kubectl create configmap web-config -n status --from-file=default.conf
```

```text
configmap/web-config created
```

**Das Objekt gibt es schon:**

```bash
kubectl create namespace status
```

```text
Error from server (AlreadyExists): namespaces "status" already exists
```

## Wann brauche ich das?

- Für schnelle Tests, die kein Manifest brauchen
- Um Secrets anzulegen, ohne Passwörter in eine YAML-Datei zu schreiben
- Um mit `--dry-run=client -o yaml` einen Ausgangspunkt für ein Manifest zu bekommen

!!! tip "Manifeste erzeugen"
    `kubectl create deployment … --dry-run=client -o yaml > deploy.yaml` schreibt ein
    vollständiges Manifest, das du anpasst und dann mit `kubectl apply` ausrollst.

!!! warning "Secrets sind nur base64"
    Ein Secret wird base64-kodiert gespeichert, nicht verschlüsselt. Wer im Namespace Secrets
    lesen darf, entschlüsselt es mit `base64 -d`. Schränke den Zugriff mit RBAC ein.

## Verwandte Befehle

[kubectl apply](kubectl-apply.md) · [kubectl delete](kubectl-delete.md) · [kubectl get](kubectl-get.md) · [kubectl describe](kubectl-describe.md)
