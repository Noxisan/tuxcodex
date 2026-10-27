---
icon: material/kubernetes
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-kubernetes:{ .tc-hero-icon }

# Kubernetes

Container in einem Cluster betreiben: k3s einrichten, Anwendungen ausrollen und skalieren,
Fehler finden, Nodes warten und Software mit Helm installieren.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Was du installieren musst, Pods, Deployments und Services, Manifeste und kubeconfig :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Cluster einrichten

<div class="grid cards" markdown>

-   :material-server:{ .lg .middle } **[k3s](k3s.md)**

    ---

    Kubernetes in einer einzigen Datei.

-   :material-cog-outline:{ .lg .middle } **[kubectl config](kubectl-config.md)**

    ---

    Cluster, Kontexte und Standard-Namespace.

</div>

## Ressourcen ansehen

<div class="grid cards" markdown>

-   :material-format-list-bulleted:{ .lg .middle } **[kubectl get](kubectl-get.md)**

    ---

    Pods, Deployments und mehr auflisten.

-   :material-magnify:{ .lg .middle } **[kubectl describe](kubectl-describe.md)**

    ---

    Details und Events eines Objekts.

-   :material-text-box-outline:{ .lg .middle } **[kubectl logs](kubectl-logs.md)**

    ---

    Ausgabe der Container eines Pods.

-   :material-bell-outline:{ .lg .middle } **[kubectl events](kubectl-events.md)**

    ---

    Was im Cluster passiert ist.

-   :material-chart-line:{ .lg .middle } **[kubectl top](kubectl-top.md)**

    ---

    CPU und Speicher von Nodes und Pods.

</div>

## Anwendungen ausrollen

<div class="grid cards" markdown>

-   :material-file-upload-outline:{ .lg .middle } **[kubectl apply](kubectl-apply.md)**

    ---

    Aus Manifesten anlegen oder aktualisieren.

-   :material-plus-box-outline:{ .lg .middle } **[kubectl create](kubectl-create.md)**

    ---

    Einzelne Objekte direkt anlegen.

-   :material-delete-outline:{ .lg .middle } **[kubectl delete](kubectl-delete.md)**

    ---

    Objekte löschen.

-   :material-arrow-expand-horizontal:{ .lg .middle } **[kubectl scale](kubectl-scale.md)**

    ---

    Die Anzahl der Pods ändern.

-   :material-update:{ .lg .middle } **[kubectl rollout](kubectl-rollout.md)**

    ---

    Updates beobachten, neu starten, zurücknehmen.

</div>

## Fehlersuche

<div class="grid cards" markdown>

-   :material-console:{ .lg .middle } **[kubectl exec](kubectl-exec.md)**

    ---

    Einen Befehl oder eine Shell im Pod ausführen.

-   :material-lan-connect:{ .lg .middle } **[kubectl port-forward](kubectl-port-forward.md)**

    ---

    Einen Pod oder Service lokal erreichen.

</div>

## Wartung

<div class="grid cards" markdown>

-   :material-wrench-outline:{ .lg .middle } **[kubectl drain](kubectl-drain.md)**

    ---

    Einen Node vor der Wartung leeren.

</div>
