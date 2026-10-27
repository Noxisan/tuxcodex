---
icon: material/kubernetes
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-kubernetes:{ .tc-hero-icon }

# Kubernetes

Running containers in a cluster: setting up k3s, rolling out and scaling applications,
finding errors, maintaining nodes and installing software with Helm.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** What you need to install, pods, deployments and services, manifests and kubeconfig :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Setting up the cluster

<div class="grid cards" markdown>

-   :material-server:{ .lg .middle } **[k3s](k3s.md)**

    ---

    Kubernetes in a single binary.

-   :material-cog-outline:{ .lg .middle } **[kubectl config](kubectl-config.md)**

    ---

    Clusters, contexts and the default namespace.

</div>

## Looking at resources

<div class="grid cards" markdown>

-   :material-format-list-bulleted:{ .lg .middle } **[kubectl get](kubectl-get.md)**

    ---

    List pods, deployments and more.

-   :material-magnify:{ .lg .middle } **[kubectl describe](kubectl-describe.md)**

    ---

    Details and events of an object.

-   :material-text-box-outline:{ .lg .middle } **[kubectl logs](kubectl-logs.md)**

    ---

    Output of the containers in a pod.

-   :material-bell-outline:{ .lg .middle } **[kubectl events](kubectl-events.md)**

    ---

    What happened in the cluster.

-   :material-chart-line:{ .lg .middle } **[kubectl top](kubectl-top.md)**

    ---

    CPU and memory of nodes and pods.

</div>

## Rolling out applications

<div class="grid cards" markdown>

-   :material-file-upload-outline:{ .lg .middle } **[kubectl apply](kubectl-apply.md)**

    ---

    Create or update from manifests.

-   :material-plus-box-outline:{ .lg .middle } **[kubectl create](kubectl-create.md)**

    ---

    Create single objects directly.

-   :material-delete-outline:{ .lg .middle } **[kubectl delete](kubectl-delete.md)**

    ---

    Delete objects.

-   :material-arrow-expand-horizontal:{ .lg .middle } **[kubectl scale](kubectl-scale.md)**

    ---

    Change the number of pods.

</div>
