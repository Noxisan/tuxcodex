# Understanding systemd

systemd is the first process on Debian, Ubuntu, RHEL and Arch: it runs with PID 1, starts
all services at boot, restarts them when they crash, collects their logs and shuts the
system down cleanly. Everything systemd manages is called a **unit**.

## Unit types

The type is the extension of the unit name:

| Type | Example | What it is |
|------|---------|------------|
| `.service` | `nginx.service` | A service or a one-off job |
| `.timer` | `logrotate.timer` | Starts a service at fixed times, like a cron job |
| `.socket` | `ssh.socket` | Starts a service when a connection arrives |
| `.target` | `multi-user.target` | A group of units, a bit like a runlevel |
| `.mount` | `srv-data.mount` | A mounted file system |
| `.path` | `systemd-ask-password-wall.path` | Starts a service when a file changes |

If you leave out the extension, `systemctl` assumes `.service`: `systemctl status nginx`
means `nginx.service`.

## Where unit files are

| Directory | Contents |
|-----------|----------|
| `/usr/lib/systemd/system/` | Unit files from packages. Don't edit, updates overwrite them |
| `/etc/systemd/system/` | Your own units and changes. They take precedence |
| `/run/systemd/system/` | Units created at runtime, gone after a reboot |

!!! tip "Change units with `systemctl edit`"
    `sudo systemctl edit nginx` creates an override file in
    `/etc/systemd/system/nginx.service.d/`. It only contains your changes and survives
    package updates. `sudo systemctl edit --full nginx` copies the whole file instead.

## States

A unit has two independent states: whether it is running **now**, and whether it starts
**at boot**.

| Running now | Meaning |
|-------------|---------|
| `active (running)` | Running, with at least one process |
| `active (exited)` | Ran once successfully and has no process left, e.g. a firewall setup |
| `inactive (dead)` | Not running |
| `failed` | Ended with an error, crashed or was killed |

| At boot | Meaning |
|---------|---------|
| `enabled` | Starts at boot |
| `disabled` | Doesn't start at boot, but can be started by hand |
| `static` | Can't be enabled, is only started by other units |
| `masked` | Blocked completely, can't be started at all |

`start` changes the first state, `enable` the second. A service that you only start is
gone after the next reboot.

## A simple unit file

`/etc/systemd/system/backup.service`:

```ini
[Unit]
Description=Nightly backup
After=network-online.target

[Service]
Type=oneshot
User=nox
ExecStart=/usr/local/bin/backup.sh

[Install]
WantedBy=multi-user.target
```

| Section | Purpose |
|---------|---------|
| `[Unit]` | Description and order: start after the network is up |
| `[Service]` | What is run, as which user, and how (`oneshot`: runs once and ends) |
| `[Install]` | Where `enable` hooks the unit in: `multi-user.target` is the normal boot |

After creating or changing a unit file, run `sudo systemctl daemon-reload`.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Service starts and is enabled when its package is installed | yes | yes | no | no |
| Typical next step after installing | none | none | `sudo systemctl enable --now nginx` | `sudo systemctl enable --now nginx` |
