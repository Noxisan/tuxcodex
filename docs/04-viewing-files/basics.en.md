# Reading logs

| Task | Command |
|------|---------|
| Follow a log live while you test | `tail -f /var/log/nginx/error.log` |
| Show the last 50 lines | `tail -n 50 /var/log/nginx/error.log` |
| Browse and search a large log | `less /var/log/nginx/access.log`, then `/` to search |
| Read a rotated, compressed log | `zless /var/log/nginx/access.log.2.gz` |
| Show the newest lines first | `tac /var/log/nginx/access.log | less` |

!!! tip "Logs of systemd services"
    On distributions with systemd, many services don't write their own log files, but
    log to the systemd journal. You read those with `journalctl`, which is covered in the
    chapter on logs.
