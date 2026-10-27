# kubectl exec

> Führt einen Befehl in einem Container eines laufenden Pods aus, zum Beispiel eine Shell.

![kubectl-exec output](../assets/screenshots/20-kubernetes/kubectl-exec.png)

## Syntax

```bash
kubectl exec [-it] POD | TYP/NAME [-c CONTAINER] -- BEFEHL [ARG...]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `POD`, `deploy/NAME` | Ein Pod oder ein Pod dieses Deployments |
| `-it` | Interaktiv mit Terminal, nötig für eine Shell |
| `-c CONTAINER` | Container in einem Pod mit mehreren Containern |
| `-n NAMESPACE` | Namespace |
| `--` | Alles danach ist der Befehl im Container |

## Beispiele

**Die nginx-Konfiguration testen:**

```bash
kubectl exec -n status deploy/web -- nginx -t
```

```text
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**Eine Shell im Pod:**

```bash
kubectl exec -it -n status web-9bc5f7f5b-8ptw2 -- bash
```

```text
root@web-9bc5f7f5b-8ptw2:/# hostname -i
10.42.0.9
root@web-9bc5f7f5b-8ptw2:/# exit
```

**Prüfen, ob der Service im Cluster aufgelöst wird:**

```bash
kubectl exec -n status deploy/web -- getent hosts web.status.svc.cluster.local
```

```text
10.43.196.168   web.status.svc.cluster.local
```

## Wann brauche ich das?

- Um sich in einem Pod umzusehen, wenn etwas nicht funktioniert
- Um Konfiguration oder Netzwerk aus einem Pod heraus zu testen
- Um Wartungsbefehle auszuführen, etwa eine Datenbankmigration

!!! tip "Keine Shell im Image?"
    Minimale Images haben oft gar keine Shell. `kubectl debug -it POD --image=busybox
    --target=CONTAINER` startet einen Hilfscontainer mit Werkzeugen im selben Pod.

!!! warning "Änderungen sind vorübergehend"
    Was du in einem Pod änderst, ist weg, sobald der Pod ersetzt wird, und das passiert bei
    jedem Update. Dauerhafte Änderungen gehören ins Image oder ins Manifest.

## Verwandte Befehle

[kubectl logs](kubectl-logs.md) · [kubectl port-forward](kubectl-port-forward.md) · [kubectl describe](kubectl-describe.md) · [docker exec](../19-docker/docker-exec.md)
