# atrm

> Removes waiting jobs from the `at` queue before they run.

![atrm output](../assets/screenshots/16-scheduling/atrm.png)

## Syntax

```bash
atrm JOB...
```

## Options

| Option | Description |
|--------|-------------|
| `JOB` | The job number from `atq`; several numbers are possible |

## Examples

**Remove a job and check the queue:**

```bash
sudo atrm 6
sudo atq
```

```text
5       Mon Oct 26 22:00:00 2026 a nox
7       Tue Oct 27 09:00:00 2026 a nox
```

**A job number that doesn't exist:**

```bash
atrm 9
```

```text
Cannot find jobid 9
```

**Remove the safety job after a successful firewall change:**

```bash
sudo atq
sudo atrm 8
```

```text
8       Mon Oct 26 10:47:00 2026 a root
```

## When do I need it?

- When a scheduled job is no longer needed
- After a successful change, to remove the safety job that would undo it
- When a job was scheduled for the wrong time

!!! tip "Check afterwards"
    `atrm` prints nothing on success. Run `atq` to make sure the job is gone.

## Related commands

[at](at.md) · [atq](atq.md)
