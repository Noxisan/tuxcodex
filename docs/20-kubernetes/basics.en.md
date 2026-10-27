# Understanding Kubernetes

Kubernetes runs containers on a group of servers, the **cluster**. You no longer say "start
this container on that server", but describe the desired state: "three copies of nginx
1.28, reachable as `status.example.com`". Kubernetes makes sure this state is reached and
stays that way, even when a container crashes or a server fails.

## What you need to install

| Tool | What it is | Where it's needed |
|------|------------|-------------------|
| [`k3s`](k3s.md) | A complete, lightweight Kubernetes in a single binary, ideal for a single server or a small cluster | On every server of the cluster |
| [`kubectl`](kubectl-get.md) | The command line tool for every Kubernetes cluster | Where you work: on the server (included in k3s) or your own computer |
| [`helm`](helm.md) | Package manager for ready-made applications (charts) | Where you run `kubectl` |
| [`k9s`](k9s.md) | Terminal interface for browsing and managing the cluster | Optional, where you run `kubectl` |

The example server `tuxdex-srv` runs a single-node cluster with k3s. That's all you need
to practise; `kubectl` comes with it.

```text
$ curl -sfL https://get.k3s.io | sh -
$ sudo kubectl get nodes
NAME           STATUS   ROLES           AGE   VERSION
tuxdex-srv     Ready    control-plane   42s   v1.34.1+k3s1
```

Installation of the tools on the different distributions:

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| k3s | install script `get.k3s.io` | install script `get.k3s.io` | install script `get.k3s.io` (also installs `k3s-selinux`) | install script `get.k3s.io` |
| kubectl (without k3s) | repository `pkgs.k8s.io`, then `sudo apt install kubectl` | repository `pkgs.k8s.io`, then `sudo apt install kubectl` | repository `pkgs.k8s.io`, then `sudo dnf install kubectl` | `sudo pacman -S kubectl` |
| helm | install script from helm.sh | install script from helm.sh, or `sudo snap install helm --classic` | install script from helm.sh | `sudo pacman -S helm` |
| k9s | `.deb` package from the k9s releases on GitHub | `.deb` package from the k9s releases on GitHub | `.rpm` package from the k9s releases on GitHub | `sudo pacman -S k9s` |
| Firewall | open 6443/tcp if other machines use the cluster | `ufw` rules for 6443/tcp and the cluster networks | `firewalld` rules for 6443/tcp and the cluster networks, see the k3s documentation | as configured |

The install script for Helm: `curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-4 | bash`.

## The most important objects

| Object | What it is |
|--------|------------|
| **Node** | A server in the cluster |
| **Pod** | The smallest unit: one or more containers that run together on one node |
| **Deployment** | Keeps a number of identical pods running and replaces them during updates |
| **Service** | A fixed name and address in front of changing pods, with load balancing |
| **Ingress** | Makes a service reachable from outside by host name, like a reverse proxy |
| **Namespace** | A separate area in the cluster, for example one per application |
| **ConfigMap**, **Secret** | Configuration and passwords that pods get as files or variables |

## A manifest

Objects are described in YAML files, the manifests. `~/k8s/status.yaml` (shortened)
describes the status page from the Docker chapter as a deployment with two pods:

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

The full file also contains the namespace, a service and an ingress for
`status.example.com`, each separated by `---`. [`kubectl apply`](kubectl-apply.md) creates
everything in one go.

## kubeconfig: which cluster?

`kubectl` reads the address of the cluster and your access data from a kubeconfig file,
by default `~/.kube/config`. k3s writes its file to `/etc/rancher/k3s/k3s.yaml`, readable
by root only. To use the cluster as a normal user:

```text
$ mkdir -p ~/.kube
$ sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
$ sudo chown nox: ~/.kube/config
$ echo 'export KUBECONFIG=~/.kube/config' >> ~/.bashrc
```

To work from your own computer, copy the file there and replace `127.0.0.1` with the
address of the server. See [`kubectl config`](kubectl-config.md).

!!! tip "Short names and completion"
    `kubectl get po`, `deploy`, `svc`, `ns` and `no` are short for pods, deployments,
    services, namespaces and nodes. `source <(kubectl completion bash)` in `~/.bashrc`
    completes commands and object names with ++tab++.

!!! danger "The kubeconfig is a master key"
    Whoever has the kubeconfig of k3s has full admin rights on the cluster and, through
    privileged pods, on every node. Treat it like a root password and never commit it to Git.
