# fg

> Brings a background or paused job back to the foreground, so you can see it and interact with it.

![fg output](../assets/screenshots/08-processes/fg.png)

## Syntax

```bash
fg [%JOB]
```

Without a job, `fg` uses the current job (`+` in [`jobs`](jobs.md)).

## Options

| Option | Description |
|--------|-------------|
| `%NUMBER` | The job with this number, e.g. `%2` |
| `%TEXT` | The job whose command starts with `TEXT`, e.g. `%vim` |

## Examples

**Get back to the editor you paused:**

```bash
fg
```

```text
vim /etc/nginx/nginx.conf
```

`fg` prints the command and continues it. The editor fills the terminal again, exactly
where you left it.

**Bring a background job to the foreground:**

```bash
fg %1
```

```text
tar -czf /mnt/backup/www.tar.gz /srv/www
```

The shell now waits for the job again. To stop it, press ++ctrl+c++. To pause it
again, press ++ctrl+z++.

**Select a job by its command:**

```bash
fg %vim
```

```text
vim /etc/nginx/nginx.conf
```

**A job number that doesn't exist:**

```bash
fg %7
```

```text
bash: fg: %7: no such job
```

## When do I need it?

- To get back to an editor or a `less` that you paused with ++ctrl+z++
- To watch the output of a background job or end it with ++ctrl+c++
- When a background job stopped because it waits for input

!!! tip "Quickly look something up while editing"
    In `vim`, press ++ctrl+z++, check something in the shell, and return with `fg`. This is
    faster than quitting and reopening the file.

!!! warning "Forgotten paused jobs"
    When you try to log out with paused jobs, bash warns once: `There are stopped jobs.`
    If you log out anyway, they are ended and unsaved changes in an editor are lost.

## Related commands

[jobs](jobs.md) · [bg](bg.md) · [kill](kill.md)
