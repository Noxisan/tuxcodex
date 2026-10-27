# kubectl drain

> Empties a node before maintenance: no new pods, and the running ones are moved to other nodes.

![kubectl-drain output](../assets/screenshots/20-kubernetes/kubectl-drain.png)

## Syntax

```bash
kubectl drain NODE [OPTIONS]
kubectl cordon | uncordon NODE
```

## Options

| Option | Description |
|--------|-------------|
| `cordon NODE` | Only stop new pods from being scheduled on the node |
| `drain NODE` | Cordon, then evict all pods |
| `--ignore-daemonsets` | Leave pods of DaemonSets, which run on every node anyway |
| `--delete-emptydir-data` | Also evict pods with temporary `emptyDir` volumes (their data is lost) |
| `--force` | Also delete pods that don't belong to a deployment or similar |
| `--timeout=5m` | Give up after this time |
| `uncordon NODE` | Allow pods on the node again after the maintenance |

## Examples

**Empty a node before maintenance:**

```bash
kubectl drain tuxcodex-srv --ignore-daemonsets --delete-emptydir-data
```

```text
node/tuxcodex-srv cordoned
Warning: ignoring DaemonSet-managed Pods: kube-system/svclb-traefik-db512acc-cmznz
evicting pod status/web-9bc5f7f5b-8ptw2
evicting pod status/web-9bc5f7f5b-m8l96
evicting pod kube-system/coredns-7896679cc-2dcm2
evicting pod kube-system/traefik-6f986b958c-v9bwd
evicting pod kube-system/metrics-server-7b9c9c4b9c-m8shl
evicting pod kube-system/local-path-provisioner-578895bd58-x8h47
pod/web-9bc5f7f5b-m8l96 evicted
pod/web-9bc5f7f5b-8ptw2 evicted
pod/local-path-provisioner-578895bd58-x8h47 evicted
pod/coredns-7896679cc-2dcm2 evicted
pod/metrics-server-7b9c9c4b9c-m8shl evicted
pod/traefik-6f986b958c-v9bwd evicted
node/tuxcodex-srv drained
```

**The node is locked for new pods:**

```bash
kubectl get nodes
```

```text
NAME           STATUS                     ROLES           AGE   VERSION
tuxcodex-srv   Ready,SchedulingDisabled   control-plane   3d    v1.34.1+k3s1
```

**A pod without a controller blocks the drain:**

```bash
kubectl drain tuxcodex-srv --ignore-daemonsets
```

```text
node/tuxcodex-srv already cordoned
error: unable to drain node "tuxcodex-srv" due to error: cannot delete cannot delete Pods that declare no controller (use --force to override): status/broken, continuing command...
There are pending nodes to be drained:
 tuxcodex-srv
cannot delete cannot delete Pods that declare no controller (use --force to override): status/broken
```

**Release the node after the maintenance:**

```bash
kubectl uncordon tuxcodex-srv
```

```text
node/tuxcodex-srv uncordoned
```

## When do I need it?

- Before updating or rebooting a node
- Before removing a node from the cluster
- To find out which pods can't be moved

!!! tip "Workflow for a kernel update"
    `kubectl drain NODE --ignore-daemonsets`, then update and reboot the server, then
    `kubectl uncordon NODE`. In a cluster with several nodes, the applications keep
    running.

!!! warning "Single node: drain means downtime"
    With only one node, there is nowhere to move the pods. They stop until
    `kubectl uncordon`, so on `tuxcodex-srv` drain is a planned downtime.

## Related commands

[kubectl get](kubectl-get.md) · [k3s](k3s.md) · [kubectl describe](kubectl-describe.md) · [reboot](../09-systemd/reboot.md)
