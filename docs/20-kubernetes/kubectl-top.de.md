# kubectl top

> Zeigt die aktuelle CPU- und Speicherauslastung von Nodes und Pods.

![kubectl-top output](../assets/screenshots/20-kubernetes/kubectl-top.png)

## Syntax

```bash
kubectl top nodes | pods [NAME] [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `nodes` | Auslastung der Nodes |
| `pods` | Auslastung der Pods |
| `-n NAMESPACE`, `-A` | Pods eines Namespaces oder aller |
| `--containers` | Jeden Container eines Pods einzeln zeigen |
| `--sort-by=cpu`, `--sort-by=memory` | Nach Auslastung sortieren |

CPU wird in Millicores angegeben: `250m` ist ein Viertel eines CPU-Kerns.

## Beispiele

**Auslastung der Nodes:**

```bash
kubectl top nodes
```

```text
NAME           CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)
tuxdex-srv     231m         11%      721Mi           18%
```

**Die Pods mit dem meisten Speicher zuerst:**

```bash
kubectl top pods -A --sort-by=memory
```

```text
NAMESPACE     NAME                                      CPU(cores)   MEMORY(bytes)
kube-system   traefik-6f986b958c-v9bwd                  2m           41Mi
kube-system   metrics-server-7b9c9c4b9c-m8shl           9m           22Mi
kube-system   coredns-7896679cc-2dcm2                   3m           17Mi
status        web-9bc5f7f5b-8ptw2                       3m           12Mi
status        web-9bc5f7f5b-m8l96                       3m           12Mi
kube-system   local-path-provisioner-578895bd58-x8h47   1m           8Mi
```

**Ein Namespace:**

```bash
kubectl top pods -n status
```

```text
NAME                  CPU(cores)   MEMORY(bytes)
web-9bc5f7f5b-8ptw2   3m           12Mi
web-9bc5f7f5b-m8l96   3m           12Mi
```

## Wann brauche ich das?

- Wenn der Cluster langsam ist und du den Pod suchst, der die Ressourcen frisst
- Um sinnvolle Werte für `requests` und `limits` festzulegen
- Um zu sehen, wie voll ein Node ist, bevor du weitere Pods hinzufügst

!!! tip "Braucht den Metrics-Server"
    `kubectl top` holt seine Zahlen vom Metrics-Server. k3s installiert ihn mit; in anderen
    Clustern ohne ihn kommt `error: Metrics API not available`.

## Verwandte Befehle

[kubectl describe](kubectl-describe.md) · [kubectl get](kubectl-get.md) · [kubectl scale](kubectl-scale.md) · [top](../08-processes/top.md)
