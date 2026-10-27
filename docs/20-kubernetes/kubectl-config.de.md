# kubectl config

> Zeigt und ändert die kubeconfig: welche Cluster kubectl kennt, welcher aktiv ist und welcher Namespace als Standard gilt.

![kubectl-config output](../assets/screenshots/20-kubernetes/kubectl-config.png)

## Syntax

```bash
kubectl config UNTERBEFEHL [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `view` | Die Konfiguration zeigen (Schlüssel werden ausgeblendet) |
| `get-contexts` | Alle Kontexte auflisten (Cluster, Benutzer, Namespace); `*` markiert den aktiven |
| `current-context` | Den aktiven Kontext zeigen |
| `use-context NAME` | Zu einem anderen Cluster wechseln |
| `set-context --current --namespace=NS` | Den Standard-Namespace des aktiven Kontexts setzen |
| `rename-context ALT NEU` | Einem Kontext einen besseren Namen geben |
| `--kubeconfig DATEI` | Eine andere Datei nutzen (funktioniert auch bei jedem anderen `kubectl`-Befehl) |

## Beispiele

**Die Kontexte auflisten:**

```bash
kubectl config get-contexts
```

```text
CURRENT   NAME      CLUSTER   AUTHINFO   NAMESPACE
*         default   default   default
```

**Die Konfiguration zeigen:**

```bash
kubectl config view
```

```text
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://127.0.0.1:6443
  name: default
contexts:
- context:
    cluster: default
    user: default
  name: default
current-context: default
kind: Config
users:
- name: default
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
```

**status zum Standard-Namespace machen:**

```bash
kubectl config set-context --current --namespace=status
kubectl get pods
```

```text
Context "default" modified.
NAME                  READY   STATUS    RESTARTS   AGE
web-9bc5f7f5b-8ptw2   1/1     Running   0          2h
web-9bc5f7f5b-m8l96   1/1     Running   0          2h
```

**Dem Kontext einen klaren Namen geben:**

```bash
kubectl config rename-context default tuxcodex-srv
kubectl config current-context
```

```text
Context "default" renamed to "tuxcodex-srv".
tuxcodex-srv
```

## Wann brauche ich das?

- Um zu prüfen, mit welchem Cluster du sprichst, bevor du etwas änderst
- Um zwischen Test- und Produktionscluster zu wechseln
- Um nicht bei jedem Befehl `-n status` tippen zu müssen

!!! tip "Mehrere Dateien auf einmal"
    `KUBECONFIG=~/.kube/config:~/.kube/prod.yaml` fasst mehrere Dateien zusammen.
    `kubectl config view --flatten` schreibt sie als eine.

!!! warning "Wissen, wo du bist"
    Ein Befehl für den Testcluster kann die Produktion treffen, wenn der falsche Kontext
    aktiv ist. Gib Kontexten klare Namen (`rename-context default tuxcodex-srv`) und prüfe mit
    `kubectl config current-context`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| kubectl | bei k3s dabei; sonst Repository `pkgs.k8s.io`, dann `sudo apt install kubectl` | bei k3s dabei; sonst Repository `pkgs.k8s.io` oder `sudo snap install kubectl --classic` | bei k3s dabei; sonst Repository `pkgs.k8s.io`, dann `sudo dnf install kubectl` | bei k3s dabei; sonst `sudo pacman -S kubectl` |

## Verwandte Befehle

[kubectl get](kubectl-get.md) · [k3s](k3s.md) · [k9s](k9s.md)
