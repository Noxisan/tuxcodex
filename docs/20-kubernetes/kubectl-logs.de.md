# kubectl logs

> Zeigt die Ausgabe der Container in einem Pod.

![kubectl-logs output](../assets/screenshots/20-kubernetes/kubectl-logs.png)

## Syntax

```bash
kubectl logs [OPTIONEN] POD | TYP/NAME [-c CONTAINER]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `POD`, `deploy/NAME` | Ein Pod oder ein Pod dieses Deployments |
| `-l LABEL=WERT` | Alle Pods mit diesem Label |
| `-f`, `--follow` | Neue Zeilen fortlaufend zeigen |
| `--tail N` | Nur die letzten N Zeilen |
| `--since 1h` | Nur Zeilen der letzten Stunde (oder `10m`, `30s`) |
| `-p`, `--previous` | Ausgabe des vorherigen, abgestürzten Containers |
| `-c CONTAINER` | Container in einem Pod mit mehreren Containern |
| `--prefix` | Pod- und Containername vor jede Zeile setzen |

## Beispiele

**Die letzten Zeilen eines Deployments:**

```bash
kubectl logs -n status deploy/web --tail 3
```

```text
Found 2 pods, using pod/web-9bc5f7f5b-8ptw2
198.51.100.23 - - [26/Oct/2026:09:42:10 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/8.14.1" "198.51.100.23"
198.51.100.23 - - [26/Oct/2026:09:42:12 +0000] "GET /status HTTP/1.1" 404 153 "-" "curl/8.14.1" "198.51.100.23"
198.51.100.23 - - [26/Oct/2026:09:42:15 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/8.14.1" "198.51.100.23"
```

**Alle Pods einer Anwendung auf einmal:**

```bash
kubectl logs -n status -l app=web --prefix --tail 1
```

```text
[pod/web-9bc5f7f5b-8ptw2/nginx] 198.51.100.23 - - [26/Oct/2026:09:42:15 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/8.14.1" "198.51.100.23"
[pod/web-9bc5f7f5b-m8l96/nginx] 198.51.100.23 - - [26/Oct/2026:09:42:13 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "-" "curl/8.14.1" "198.51.100.23"
```

**Herausfinden, warum der Container abgestürzt ist:**

```bash
kubectl logs -n status web-7d4c9b8f6-xk2lp --previous
```

```text
2026/10/26 09:40:02 [emerg] 1#1: unknown directive "sever_name" in /etc/nginx/conf.d/default.conf:3
nginx: [emerg] unknown directive "sever_name" in /etc/nginx/conf.d/default.conf:3
```

**Live mitlesen:**

```bash
kubectl logs -n status -f deploy/web --tail 0
```

```text
Found 2 pods, using pod/web-9bc5f7f5b-8ptw2
198.51.100.23 - - [26/Oct/2026:09:42:31 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/8.14.1" "198.51.100.23"
^C
```

## Wann brauche ich das?

- Wenn ein Pod in `CrashLoopBackOff` steckt und du wissen musst, warum
- Um beim Testen die Anfragen an eine Anwendung mitzulesen
- Um die Ausgabe eines Jobs oder einer Migration zu prüfen

!!! tip "Logs eines abgestürzten Containers"
    Nach einem Absturz zeigt `kubectl logs` die Ausgabe des neuen Containers, die oft noch
    leer ist. Der Grund für den Absturz steht in `kubectl logs --previous POD`.

!!! warning "Logs verschwinden mit dem Pod"
    Wird ein Pod gelöscht oder ersetzt, sind auch seine Logs weg. Was du aufbewahren musst,
    sammelst du zentral, etwa mit Loki oder dem ELK-Stack.

## Verwandte Befehle

[kubectl get](kubectl-get.md) · [kubectl describe](kubectl-describe.md) · [kubectl events](kubectl-events.md) · [kubectl exec](kubectl-exec.md)
