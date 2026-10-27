# helm

> Der Paketmanager für Kubernetes: installiert fertige Anwendungen (Charts) mit allen ihren Objekten und aktualisiert sie.

![helm output](../assets/screenshots/20-kubernetes/helm.png)

## Syntax

```bash
helm BEFEHL [RELEASE] [CHART] [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `repo add NAME URL`, `repo update` | Ein Chart-Repository hinzufügen, die Listen aktualisieren |
| `search repo WORT` | Die hinzugefügten Repositorys nach Charts durchsuchen |
| `install RELEASE CHART` | Ein Chart unter einem Namen (dem Release) installieren |
| `upgrade RELEASE CHART` | Ein Release aktualisieren oder seine Werte ändern; mit `--install` auch installieren |
| `-n NAMESPACE`, `--create-namespace` | Ziel-Namespace, bei Bedarf anlegen |
| `-f values.yaml`, `--set SCHLÜSSEL=WERT` | Eigene Einstellungen für das Chart |
| `list -A` | Installierte Releases in allen Namespaces |
| `history`, `rollback RELEASE N` | Versionen eines Releases, zurück zu Version N |
| `uninstall RELEASE` | Ein Release mit allen seinen Objekten entfernen |
| `show values CHART` | Die Einstellungen, die ein Chart anbietet |

## Beispiele

**Ein Repository hinzufügen und durchsuchen:**

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm search repo node-exporter
```

```text
"prometheus-community" has been added to your repositories
NAME                                            CHART VERSION   APP VERSION   DESCRIPTION
prometheus-community/prometheus-node-exporter   4.60.1          1.12.1        A Helm chart for prometheus node-exporter
```

**Ein Chart installieren:**

```bash
helm install node-exporter prometheus-community/prometheus-node-exporter \
  -n monitoring --create-namespace
```

```text
NAME: node-exporter
LAST DEPLOYED: Mon Oct 26 10:42:17 2026
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
TEST SUITE: None
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=prometheus-node-exporter,app.kubernetes.io/instance=node-exporter" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:9100 to use your application"
  kubectl port-forward --namespace monitoring $POD_NAME 9100
```

**Die installierten Releases:**

```bash
helm list -A
```

```text
NAME            NAMESPACE     REVISION   UPDATED                                   STATUS     CHART                             APP VERSION
node-exporter   monitoring    1          2026-10-26 10:42:17.493561963 +0100 CET   deployed   prometheus-node-exporter-4.60.1   1.12.1
traefik         kube-system   1          2026-10-23 14:20:33.815172573 +0200 CEST  deployed   traefik-34.2.1+up34.2.0           v3.3.2
traefik-crd     kube-system   1          2026-10-23 14:20:32.450321194 +0200 CEST  deployed   traefik-crd-34.2.1+up34.2.0       v3.3.2
```

**Versionsverlauf und Rückkehr:**

```bash
helm history node-exporter -n monitoring
helm rollback node-exporter 1 -n monitoring
```

```text
REVISION   UPDATED                    STATUS       CHART                             APP VERSION   DESCRIPTION
1          Mon Oct 26 10:42:17 2026   superseded   prometheus-node-exporter-4.60.1   1.12.1        Install complete
2          Mon Oct 26 10:44:03 2026   deployed     prometheus-node-exporter-4.60.1   1.12.1        Upgrade complete
Rollback was a success! Happy Helming!
```

**Ein Release entfernen:**

```bash
helm uninstall node-exporter -n monitoring
```

```text
release "node-exporter" uninstalled
```

## Wann brauche ich das?

- Um komplexe Software wie Monitoring, Datenbanken oder Ingress-Controller mit einem Befehl zu installieren
- Um Anwendungen zu aktualisieren und die eigenen Einstellungen in einer `values.yaml` zu behalten
- Um nach einem missglückten Update zur vorherigen Version zurückzukehren

!!! tip "Eigene Werte in eine Datei"
    Schreib deine Einstellungen in eine `values.yaml` und nutze
    `helm upgrade --install RELEASE CHART -f values.yaml`. Derselbe Befehl installiert und
    aktualisiert, und die Datei kann ins Git-Repository.

!!! warning "Die Chart-Version festlegen"
    Ohne `--version` installiert Helm das neueste Chart, das eine neue Hauptversion der
    Anwendung mitbringen kann. Setz auf Produktionsclustern `--version` ausdrücklich.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | Installationsskript von helm.sh | Installationsskript von helm.sh oder `sudo snap install helm --classic` | Installationsskript von helm.sh | `sudo pacman -S helm` |

## Verwandte Befehle

[kubectl apply](kubectl-apply.md) · [kubectl rollout](kubectl-rollout.md) · [kubectl port-forward](kubectl-port-forward.md) · [k9s](k9s.md)
