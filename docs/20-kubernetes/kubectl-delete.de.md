# kubectl delete

> Löscht Objekte aus dem Cluster, nach Name, nach Label oder so, wie sie in einem Manifest beschrieben sind.

![kubectl-delete output](../assets/screenshots/20-kubernetes/kubectl-delete.png)

## Syntax

```bash
kubectl delete TYP NAME | -f DATEI | -l LABEL [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `TYP NAME` | Etwa `pod broken` oder `deployment hello` |
| `-f DATEI` | Alles löschen, was das Manifest beschreibt |
| `-l LABEL=WERT` | Alle Objekte mit diesem Label |
| `-n NAMESPACE` | Namespace der Objekte |
| `--dry-run=client` | Nur zeigen, was gelöscht würde |
| `--grace-period=0 --force` | Einen hängenden Pod sofort löschen |

## Beispiele

**Ein Deployment löschen:**

```bash
kubectl delete deployment hello -n status
```

```text
deployment.apps "hello" deleted from status namespace
```

**Einen Pod ersetzen lassen:**

```bash
kubectl delete pod web-9bc5f7f5b-8ptw2 -n status
kubectl get pods -n status
```

```text
pod "web-9bc5f7f5b-8ptw2" deleted from status namespace
NAME                  READY   STATUS    RESTARTS   AGE
web-9bc5f7f5b-m8l96   1/1     Running   0          2h
web-9bc5f7f5b-q4zxn   1/1     Running   0          3s
```

**Erst prüfen, was gelöscht würde:**

```bash
kubectl delete -f ~/k8s/status.yaml --dry-run=client
```

```text
namespace "status" deleted (dry run)
deployment.apps "web" deleted (dry run)
service "web" deleted (dry run)
ingress.networking.k8s.io "web" deleted (dry run)
```

**Einen Namespace mit allem darin entfernen:**

```bash
kubectl delete namespace monitoring
```

```text
namespace "monitoring" deleted
```

## Wann brauche ich das?

- Um Testobjekte und Anwendungen zu entfernen, die du nicht mehr brauchst
- Um einen hängenden Pod ersetzen zu lassen: Das Deployment startet sofort einen neuen
- Um eine ganze Anwendung samt Namespace zu entfernen

!!! tip "Einen Pod löschen heißt ihn neu starten"
    Ein Pod, der zu einem Deployment gehört, wird nach `kubectl delete pod` sofort neu
    angelegt. So startest du schnell einen einzelnen Pod neu. Für alle Pods nimm
    `kubectl rollout restart`.

!!! danger "Ein Namespace nimmt alles mit"
    `kubectl delete namespace NAME` löscht jedes Objekt darin, auch Secrets und Volumes samt
    Daten, ohne Rückfrage.

## Verwandte Befehle

[kubectl apply](kubectl-apply.md) · [kubectl create](kubectl-create.md) · [kubectl rollout](kubectl-rollout.md) · [kubectl get](kubectl-get.md)
