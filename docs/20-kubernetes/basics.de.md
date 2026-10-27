# Kubernetes verstehen

Kubernetes betreibt Container auf einer Gruppe von Servern, dem **Cluster**. Du sagst nicht
mehr „starte diesen Container auf jenem Server“, sondern beschreibst den gewünschten
Zustand: „drei Kopien von nginx 1.28, erreichbar als `status.example.com`“. Kubernetes sorgt
dafür, dass dieser Zustand erreicht wird und bleibt, auch wenn ein Container abstürzt oder
ein Server ausfällt.

## Was du installieren musst

| Werkzeug | Was es ist | Wo es gebraucht wird |
|----------|------------|----------------------|
| [`k3s`](k3s.md) | Ein vollständiges, schlankes Kubernetes in einer einzigen Datei, ideal für einen einzelnen Server oder einen kleinen Cluster | Auf jedem Server des Clusters |
| [`kubectl`](kubectl-get.md) | Das Kommandozeilenwerkzeug für jeden Kubernetes-Cluster | Dort, wo du arbeitest: auf dem Server (bei k3s dabei) oder auf deinem eigenen Rechner |
| [`helm`](helm.md) | Paketmanager für fertige Anwendungen (Charts) | Dort, wo du `kubectl` nutzt |
| [`k9s`](k9s.md) | Oberfläche im Terminal, um den Cluster zu durchsuchen und zu verwalten | Optional, dort, wo du `kubectl` nutzt |

Auf dem Beispielserver `tuxdex-srv` läuft ein Cluster mit einem einzigen Node auf Basis
von k3s. Mehr brauchst du zum Üben nicht, `kubectl` ist schon dabei.

```text
$ curl -sfL https://get.k3s.io | sh -
$ sudo kubectl get nodes
NAME           STATUS   ROLES           AGE   VERSION
tuxdex-srv     Ready    control-plane   42s   v1.34.1+k3s1
```

So installierst du die Werkzeuge auf den einzelnen Distributionen:

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| k3s | Installationsskript `get.k3s.io` | Installationsskript `get.k3s.io` | Installationsskript `get.k3s.io` (installiert auch `k3s-selinux`) | Installationsskript `get.k3s.io` |
| kubectl (ohne k3s) | Repository `pkgs.k8s.io`, dann `sudo apt install kubectl` | Repository `pkgs.k8s.io`, dann `sudo apt install kubectl` | Repository `pkgs.k8s.io`, dann `sudo dnf install kubectl` | `sudo pacman -S kubectl` |
| helm | Installationsskript von helm.sh | Installationsskript von helm.sh oder `sudo snap install helm --classic` | Installationsskript von helm.sh | `sudo pacman -S helm` |
| k9s | `.deb`-Paket aus den k9s-Releases auf GitHub | `.deb`-Paket aus den k9s-Releases auf GitHub | `.rpm`-Paket aus den k9s-Releases auf GitHub | `sudo pacman -S k9s` |
| Firewall | 6443/tcp öffnen, wenn andere Rechner den Cluster nutzen | `ufw`-Regeln für 6443/tcp und die Cluster-Netze | `firewalld`-Regeln für 6443/tcp und die Cluster-Netze, siehe Doku von k3s | je nach Einrichtung |

Das Installationsskript für Helm: `curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-4 | bash`.

## Die wichtigsten Objekte

| Objekt | Was es ist |
|--------|------------|
| **Node** | Ein Server im Cluster |
| **Pod** | Die kleinste Einheit: ein oder mehrere Container, die zusammen auf einem Node laufen |
| **Deployment** | Hält eine Anzahl gleicher Pods am Laufen und tauscht sie bei Updates aus |
| **Service** | Ein fester Name und eine feste Adresse vor wechselnden Pods, mit Lastverteilung |
| **Ingress** | Macht einen Service über einen Hostnamen von außen erreichbar, wie ein Reverse Proxy |
| **Namespace** | Ein abgetrennter Bereich im Cluster, etwa einer pro Anwendung |
| **ConfigMap**, **Secret** | Konfiguration und Passwörter, die Pods als Dateien oder Variablen bekommen |

## Ein Manifest

Objekte werden in YAML-Dateien beschrieben, den Manifesten. `~/k8s/status.yaml` (gekürzt)
beschreibt die Statusseite aus dem Docker-Kapitel als Deployment mit zwei Pods:

```text
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  namespace: status
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: nginx
          image: nginx:1.28
          ports:
            - containerPort: 80
```

Die vollständige Datei enthält außerdem den Namespace, einen Service und einen Ingress für
`status.example.com`, jeweils getrennt durch `---`. [`kubectl apply`](kubectl-apply.md) legt
alles in einem Schritt an.

## kubeconfig: welcher Cluster?

`kubectl` liest die Adresse des Clusters und deine Zugangsdaten aus einer kubeconfig-Datei,
standardmäßig `~/.kube/config`. k3s schreibt seine Datei nach `/etc/rancher/k3s/k3s.yaml`,
lesbar nur für root. Um den Cluster als normaler Benutzer zu nutzen:

```text
$ mkdir -p ~/.kube
$ sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
$ sudo chown nox: ~/.kube/config
$ echo 'export KUBECONFIG=~/.kube/config' >> ~/.bashrc
```

Um vom eigenen Rechner aus zu arbeiten, kopiere die Datei dorthin und ersetze `127.0.0.1`
durch die Adresse des Servers. Siehe [`kubectl config`](kubectl-config.md).

!!! tip "Kurznamen und Vervollständigung"
    `kubectl get po`, `deploy`, `svc`, `ns` und `no` stehen für Pods, Deployments, Services,
    Namespaces und Nodes. `source <(kubectl completion bash)` in `~/.bashrc` ergänzt Befehle
    und Objektnamen mit ++tab++.

!!! danger "Die kubeconfig ist ein Generalschlüssel"
    Wer die kubeconfig von k3s hat, hat volle Admin-Rechte im Cluster und über privilegierte
    Pods auch auf jedem Node. Behandle sie wie ein Root-Passwort und committe sie nie in Git.
