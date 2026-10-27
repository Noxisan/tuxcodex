# kubectl scale

> Ändert die Anzahl der Pods eines Deployments oder StatefulSets.

![kubectl-scale output](../assets/screenshots/20-kubernetes/kubectl-scale.png)

## Syntax

```bash
kubectl scale TYP/NAME --replicas=N [-n NAMESPACE]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `deployment/NAME` | Das Deployment (auch `statefulset/NAME`) |
| `--replicas=N` | Gewünschte Anzahl Pods; `0` hält die Anwendung an, ohne sie zu löschen |
| `--current-replicas=N` | Nur skalieren, wenn es gerade genau N Pods gibt |
| `-n NAMESPACE` | Namespace |

`kubectl autoscale deployment web --min=2 --max=5 --cpu-percent=70` passt die Anzahl automatisch an die Last an.

## Beispiele

**Drei statt zwei Pods:**

```bash
kubectl scale -n status deployment/web --replicas=3
kubectl get pods -n status
```

```text
deployment.apps/web scaled
NAME                  READY   STATUS    RESTARTS   AGE
web-9bc5f7f5b-8ptw2   1/1     Running   0          2h
web-9bc5f7f5b-m8l96   1/1     Running   0          2h
web-9bc5f7f5b-tgsdt   1/1     Running   0          5s
```

**Die Anwendung während einer Wartung anhalten:**

```bash
kubectl scale -n status deployment/web --replicas=0
kubectl get deploy -n status
```

```text
deployment.apps/web scaled
NAME   READY   UP-TO-DATE   AVAILABLE   AGE
web    0/0     0            0           2h
```

**Automatisch mit der Last skalieren:**

```bash
kubectl autoscale -n status deployment web --min=2 --max=5 --cpu-percent=70
kubectl get hpa -n status
```

```text
horizontalpodautoscaler.autoscaling/web autoscaled
NAME   REFERENCE        TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
web    Deployment/web   cpu: 6%/70%          2         5         2          15s
```

## Wann brauche ich das?

- Um kurzfristig mehr Last abzufangen
- Um eine Anwendung mit `--replicas=0` vorübergehend anzuhalten, etwa während einer Wartung
- Um zu testen, wie sich eine Anwendung mit mehreren Kopien verhält

!!! warning "apply setzt die Zahl zurück"
    Das nächste `kubectl apply` setzt die Zahl wieder auf `replicas:` aus dem Manifest. Für
    eine dauerhafte Änderung bearbeite die Datei.

## Verwandte Befehle

[kubectl rollout](kubectl-rollout.md) · [kubectl top](kubectl-top.md) · [kubectl apply](kubectl-apply.md) · [kubectl get](kubectl-get.md)
