# kubectl port-forward

> Leitet einen lokalen Port an einen Pod oder Service im Cluster weiter, ohne ihn öffentlich zu machen.

![kubectl-port-forward output](../assets/screenshots/20-kubernetes/kubectl-port-forward.png)

## Syntax

```bash
kubectl port-forward TYP/NAME [LOKAL:]ZIEL [-n NAMESPACE]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `svc/NAME`, `deploy/NAME`, `POD` | Ziel im Cluster |
| `8080:80` | Lokaler Port 8080 auf Port 80 des Ziels |
| `:80` | Einen freien lokalen Port automatisch wählen |
| `--address 0.0.0.0` | Auch Verbindungen von anderen Rechnern annehmen (Standard: nur localhost) |
| `-n NAMESPACE` | Namespace |

## Beispiele

**Einen Service lokal erreichbar machen:**

```bash
kubectl port-forward -n status svc/web 8080:80
```

```text
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
Handling connection for 8080
```

Die Weiterleitung läuft, bis du sie mit ++ctrl+c++ beendest. Solange erreicht `curl http://localhost:8080` nginx im Cluster.

**Aus einem zweiten Terminal testen:**

```bash
curl -s http://localhost:8080 | grep title
```

```text
<title>Welcome to nginx!</title>
```

**Ein automatisch gewählter lokaler Port:**

```bash
kubectl port-forward -n status deploy/web :80
```

```text
Forwarding from 127.0.0.1:38615 -> 80
Forwarding from [::1]:38615 -> 80
```

## Wann brauche ich das?

- Um eine Anwendung zu testen, bevor sie einen Ingress bekommt
- Um eine Datenbank oder eine Admin-Oberfläche im Cluster zu erreichen, ohne sie freizugeben
- Um bei der Fehlersuche einen Pod direkt mit anderen zu vergleichen

!!! tip "Über einen SSH-Tunnel"
    Vom eigenen Rechner aus: `ssh -L 8080:localhost:8080 nox@tuxdex-srv`, und auf dem
    Server `kubectl port-forward` starten. Dann funktioniert `http://localhost:8080` lokal.

## Verwandte Befehle

[kubectl exec](kubectl-exec.md) · [kubectl get](kubectl-get.md) · [ssh](../12-ssh/ssh.md) · [curl](../11-network/curl.md)
