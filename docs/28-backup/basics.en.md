# Understanding backups

A backup is only worth something if you can restore from it. Everything else in this
chapter serves that one goal: after a deleted file, a broken disk, ransomware or a fire in
the data center, you get your data back, and you know how long it takes.

## The 3-2-1 rule

| | Meaning | On tuxdex-srv |
|---|---------|---------------|
| **3** copies | The original plus two backups | Data on `sda`, backup on `/mnt/backup`, a second backup offsite |
| **2** different media | Not everything on the same disk or system | Local backup disk plus a storage at another provider |
| **1** copy offsite | At least one copy at another location | restic or borg repository on an external server or S3 |

Add one more rule: at least one copy must be **out of reach** of the server, so that an
attacker or ransomware with root access can't delete it (append-only repository,
object lock, or a backup server that pulls).

## What to back up

| What | How | Why not just copy the files |
|------|-----|------------------------------|
| Configuration (`/etc`) | restic or borg | Small, but expensive to rebuild |
| Web content, uploads (`/srv`) | restic or borg | |
| Databases | [`pg_dump`](pg_dump.md), [`mysqldump`](mysqldump.md) first, then back up the dump | Copying the data files of a running database gives a broken backup |
| Docker volumes | Dump of the database inside, plus the volume directories | Same reason |
| Package list | `dpkg --get-selections`, `dnf history` | To set up the same software again |

Not needed: `/proc`, `/sys`, `/dev`, `/run`, `/tmp`, caches and anything that comes from
packages or Git.

## restic or borg?

Both deduplicate (each block is stored only once), compress, encrypt and keep many
versions with little space.

| | [`restic`](restic.md) | [`borg`](borg.md) |
|---|-----------------------|-------------------|
| Targets | Local, SFTP, S3, Azure, Google Cloud, REST server, rclone | Local or SSH with `borg` on the other side |
| Encryption | Always | Selectable, usually `repokey` |
| Speed | Fast | Very fast, very good compression |
| Typical use | Backups to cloud storage | Backups to own servers or Hetzner Storage Box, BorgBase |

## A backup routine

```text
02:30  database dumps     pg_dump / mysqldump → /var/backups/db/
02:40  restic backup      /etc /srv /var/backups/db  → repository
03:30  restic forget      keep 7 daily, 4 weekly, 6 monthly, then prune
Sunday restic check       read part of the data and verify it
Monthly restore test      restore one file and one database into a test system
```

Run it as a systemd timer or cron job, see [`crontab`](../16-scheduling/crontab.md), and
let it report failures, for example to the journal with `logger` and to your monitoring.

## What you need to install

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| restic | `sudo apt install restic` | `sudo apt install restic` | `sudo dnf install restic` (EPEL) | `sudo pacman -S restic` |
| borg | `sudo apt install borgbackup` | `sudo apt install borgbackup` | `sudo dnf install borgbackup` (EPEL) | `sudo pacman -S borg` |
| pg_dump | with `postgresql-client` | with `postgresql-client` | with `postgresql` | with `postgresql` |
| mysqldump | with `mariadb-client` | with `mysql-client` or `mariadb-client` | with `mysql` or `mariadb` | with `mariadb-clients` |

!!! tip "Test the restore"
    Schedule a restore test, for example once a month: restore a random file and a database
    dump into a test system and check them. Only then do you know that the backup works and
    how long a restore takes.

!!! danger "Without the password, the backup is gone"
    restic and borg encrypt everything. Store the repository password (for borg also the
    exported key) outside the server, for example in your password manager. If the server
    burns, the password must not burn with it.
