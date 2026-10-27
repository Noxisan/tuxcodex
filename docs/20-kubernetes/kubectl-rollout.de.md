# kubectl rollout

> Beobachtet, startet neu und macht Updates eines Deployments rückgängig.

![kubectl-rollout output](../assets/screenshots/20-kubernetes/kubectl-rollout.png)

## Syntax

```bash
kubectl rollout UNTERBEFEHL TYP/NAME [-n NAMESPACE]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `status` | Warten, bis das Update fertig ist, und das Ergebnis melden |
| `history` | Die bisherigen Versionen (Revisionen) auflisten |
| `undo` | Zur vorherigen Version zurück; mit `--to-revision=N` zu einer bestimmten |
| `restart` | Alle Pods nacheinander ersetzen, etwa um eine neue ConfigMap zu laden |
| `pause`, `resume` | Ein Update anhalten und fortsetzen |

Eine neue Image-Version setzt `kubectl set image deployment/web nginx=nginx:1.29` oder eine Änderung im Manifest.

## Beispiele

**Ein neues Image ausrollen und darauf warten:**

```bash
kubectl set image -n status deployment/web nginx=nginx:1.29
kubectl rollout status -n status deployment/web
```

```text
deployment.apps/web image updated
Waiting for deployment "web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "web" rollout to finish: 1 old replicas are pending termination...
deployment "web" successfully rolled out
```

**Die bisherigen Versionen:**

```bash
kubectl rollout history -n status deployment/web
```

```text
deployment.apps/web
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

**Zurück zur vorherigen Version:**

```bash
kubectl rollout undo -n status deployment/web
```

```text
deployment.apps/web rolled back
```

**Alle Pods nacheinander neu starten:**

```bash
kubectl rollout restart -n status deployment/web
```

```text
deployment.apps/web restarted
```

## Wann brauche ich das?

- Nach einer Änderung, um zu wissen, wann alle neuen Pods laufen
- Wenn eine neue Version Fehler macht und du schnell zurück musst
- Um alle Pods einer Anwendung ohne Ausfall neu zu starten

!!! tip "Updates ohne Ausfall"
    Ein Deployment tauscht Pods einzeln aus und entfernt einen alten erst, wenn der neue
    bereit ist. Ergänze eine `readinessProbe`, damit Kubernetes weiß, wann deine Anwendung
    wirklich bereit ist.

!!! warning "undo und dein Manifest"
    `kubectl rollout undo` ändert den Cluster, nicht deine YAML-Datei. Korrigiere auch die
    Datei, sonst bringt das nächste `kubectl apply` die fehlerhafte Version zurück.

## Verwandte Befehle

[kubectl apply](kubectl-apply.md) · [kubectl scale](kubectl-scale.md) · [kubectl get](kubectl-get.md) · [helm](helm.md)
