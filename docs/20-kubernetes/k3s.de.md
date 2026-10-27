# k3s

> Eine vollständige Kubernetes-Distribution in einer einzigen Datei, mit einem Befehl installiert und als systemd-Dienst betrieben.

![k3s output](../assets/screenshots/20-kubernetes/k3s.png)

## Syntax

```bash
curl -sfL https://get.k3s.io | [VAR=WERT...] sh -s - [OPTIONEN]
k3s BEFEHL
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `INSTALL_K3S_VERSION=v1.34.1+k3s1` | Genau diese Version statt der neuesten stabilen installieren |
| `--write-kubeconfig-mode 644` | `/etc/rancher/k3s/k3s.yaml` für alle Benutzer lesbar machen |
| `--disable traefik` | Den mitgelieferten Ingress-Controller Traefik nicht installieren |
| `K3S_URL=https://SERVER:6443`, `K3S_TOKEN=…` | Einen weiteren Server als Agent-Node hinzufügen |
| `k3s kubectl`, `k3s crictl`, `k3s ctr` | Die mitgelieferten Werkzeuge (`kubectl`, `crictl` und `ctr` sind auch Links auf `k3s`) |
| `k3s check-config` | Prüfen, ob der Kernel alles hat, was k3s braucht |
| `k3s-uninstall.sh` | k3s vollständig entfernen, samt aller Daten |

Die Konfiguration lässt sich auch in `/etc/rancher/k3s/config.yaml` ablegen, etwa `write-kubeconfig-mode: "0644"`.

## Beispiele

**k3s installieren:**

```bash
curl -sfL https://get.k3s.io | sh -
```

```text
[INFO]  Finding release for channel stable
[INFO]  Using v1.34.1+k3s1 as release
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.34.1+k3s1/sha256sum-amd64.txt
[INFO]  Downloading binary https://github.com/k3s-io/k3s/releases/download/v1.34.1+k3s1/k3s
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
[INFO]  Skipping installation of SELinux RPM
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
[INFO]  Creating /usr/local/bin/ctr symlink to k3s
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink '/etc/systemd/system/multi-user.target.wants/k3s.service' → '/etc/systemd/system/k3s.service'.
[INFO]  systemd: Starting k3s
```

**Den Cluster prüfen:**

```bash
sudo kubectl get nodes -o wide
```

```text
NAME           STATUS   ROLES           AGE   VERSION        INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                       KERNEL-VERSION        CONTAINER-RUNTIME
tuxcodex-srv   Ready    control-plane   2m    v1.34.1+k3s1   192.0.2.10    <none>        Debian GNU/Linux 13 (trixie)   6.12.48+deb13-amd64   containerd://2.1.4-k3s2
```

**Der Dienst und die Version:**

```bash
systemctl is-active k3s
k3s --version
```

```text
active
k3s version v1.34.1+k3s1 (24fc436e)
go version go1.24.6
```

**Die Container auf dem Node, ohne Kubernetes:**

```bash
sudo k3s crictl ps
```

```text
CONTAINER           IMAGE               CREATED             STATE               NAME                     ATTEMPT             POD ID              POD                                       NAMESPACE
c55e2e4b44b11       fda7399e81045       2 hours ago         Running             nginx                    0                   b0ae7914d2596       web-9bc5f7f5b-8ptw2                       status
7074c9daf310f       fda7399e81045       2 hours ago         Running             nginx                    0                   279870aab17b8       web-9bc5f7f5b-m8l96                       status
4d4e184aa0d6c       3a1e150bf4c56       2 hours ago         Running             traefik                  0                   c5141082d8e70       traefik-6f986b958c-v9bwd                  kube-system
763d3fa5c629b       0392ee0389032       2 hours ago         Running             coredns                  0                   7d651a7e76583       coredns-7896679cc-2dcm2                   kube-system
```

`crictl` spricht direkt mit containerd. Das hilft, wenn `kubectl` selbst nicht antwortet.

**Einen zweiten Server als Agent hinzufügen:**

```bash
sudo cat /var/lib/rancher/k3s/server/node-token
curl -sfL https://get.k3s.io | K3S_URL=https://192.0.2.10:6443 K3S_TOKEN=K10…::server:4f… sh -
```

```text
K10a3c1f6b9e2d4870c5f1e8a7b3d6c9f2e1a4b8d7c0f3e6a9b2d5c8f1e4a7b0d3c6::server:4f8e2b7a1c9d3e6f0a5b8c2d7e4f1a9b
[INFO]  Finding release for channel stable
[INFO]  Using v1.34.1+k3s1 as release
...
[INFO]  systemd: Starting k3s-agent
```

Der erste Befehl läuft auf dem bestehenden Server, der zweite auf dem neuen.

## Wann brauche ich das?

- Um auf einem einzelnen Server einen Kubernetes-Cluster zum Lernen, Testen oder für kleine Dienste einzurichten
- Für kleine Cluster, Edge-Geräte und Homelabs, für die ein vollständiges Kubernetes zu schwer wäre
- Um einem bestehenden k3s-Cluster weitere Server hinzuzufügen

!!! tip "Was dabei ist"
    k3s bringt containerd, CoreDNS, Traefik als Ingress, einen Load Balancer für Services,
    den Metrics-Server und Speicher auf der lokalen Platte mit. Eine frische Installation ist
    sofort einsatzbereit.

!!! warning "Updates"
    Das Installationsskript mit einer neuen `INSTALL_K3S_VERSION` erneut auszuführen,
    aktualisiert k3s. Gehe immer nur eine Minor-Version weiter (1.33 auf 1.34, nicht 1.32
    auf 1.34) und lies vorher die Release Notes.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SELinux | nicht genutzt | nicht genutzt | das Skript installiert `k3s-selinux` | nicht genutzt |
| Firewall für andere Rechner | 6443/tcp öffnen | `ufw allow 6443/tcp`, 10.42.0.0/16 und 10.43.0.0/16 zulassen | 6443/tcp und die Netze 10.42.0.0/16 und 10.43.0.0/16 in `firewalld` eintragen oder es abschalten | je nach Einrichtung |

## Verwandte Befehle

[kubectl get](kubectl-get.md) · [kubectl config](kubectl-config.md) · [kubectl drain](kubectl-drain.md) · [systemctl](../09-systemd/systemctl.md)
