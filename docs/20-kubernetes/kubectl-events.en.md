# kubectl events

> Shows what happened in the cluster: pods scheduled, images pulled, containers started, errors.

![kubectl-events output](../assets/screenshots/20-kubernetes/kubectl-events.png)

## Syntax

```bash
kubectl events [-n NAMESPACE | -A] [OPTIONS]
```

## Options

| Option | Description |
|--------|-------------|
| `-n NAMESPACE` | Events of this namespace |
| `-A`, `--all-namespaces` | Events of all namespaces |
| `--for TYPE/NAME` | Only events of one object, such as `--for pod/broken` |
| `--types=Warning` | Only warnings |
| `-w`, `--watch` | Keep showing new events |

## Examples

**What happened in a namespace:**

```bash
kubectl events -n status
```

```text
LAST SEEN   TYPE     REASON              OBJECT                     MESSAGE
21s         Normal   ScalingReplicaSet   Deployment/web             Scaled up replica set web-9bc5f7f5b from 0 to 2
21s         Normal   SuccessfulCreate    ReplicaSet/web-9bc5f7f5b   Created pod: web-9bc5f7f5b-8ptw2
21s         Normal   SuccessfulCreate    ReplicaSet/web-9bc5f7f5b   Created pod: web-9bc5f7f5b-m8l96
20s         Normal   Scheduled           Pod/web-9bc5f7f5b-8ptw2    Successfully assigned status/web-9bc5f7f5b-8ptw2 to tuxcodex-srv
20s         Normal   Pulling             Pod/web-9bc5f7f5b-8ptw2    Pulling image "nginx:1.28"
15s         Normal   Pulled              Pod/web-9bc5f7f5b-8ptw2    Successfully pulled image "nginx:1.28" in 5.754s (5.754s including waiting). Image size: 62916597 bytes.
15s         Normal   Created             Pod/web-9bc5f7f5b-8ptw2    Created container: nginx
14s         Normal   Started             Pod/web-9bc5f7f5b-8ptw2    Started container nginx
```

**Only warnings, in the whole cluster:**

```bash
kubectl events -A --types=Warning
```

```text
NAMESPACE   LAST SEEN   TYPE      REASON   OBJECT       MESSAGE
status      45s         Warning   Failed   Pod/broken   Failed to pull image "nginx:9.99": rpc error: code = NotFound desc = failed to pull and unpack image "docker.io/library/nginx:9.99": failed to resolve reference "docker.io/library/nginx:9.99": docker.io/library/nginx:9.99: not found
status      45s         Warning   Failed   Pod/broken   Error: ErrImagePull
status      44s         Warning   Failed   Pod/broken   Error: ImagePullBackOff
```

**Events of one object:**

```bash
kubectl events -n status --for deployment/web
```

```text
LAST SEEN   TYPE     REASON              OBJECT           MESSAGE
5m          Normal   ScalingReplicaSet   Deployment/web   Scaled up replica set web-9bc5f7f5b from 2 to 3
3m          Normal   ScalingReplicaSet   Deployment/web   Scaled up replica set web-754948957d from 0 to 1
3m          Normal   ScalingReplicaSet   Deployment/web   Scaled down replica set web-9bc5f7f5b from 3 to 2
```

## When do I need it?

- Right after `kubectl apply`, to see whether everything starts
- To find warnings in the whole cluster, such as failed image pulls or full disks
- When a pod disappeared and you want to know why

!!! tip "Events don't last long"
    Kubernetes keeps events for about an hour by default. For older problems, look at the
    logs of the node with `journalctl -u k3s`.

## Related commands

[kubectl describe](kubectl-describe.md) · [kubectl get](kubectl-get.md) · [kubectl logs](kubectl-logs.md) · [journalctl](../09-systemd/journalctl.md)
