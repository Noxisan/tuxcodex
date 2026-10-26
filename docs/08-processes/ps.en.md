# ps

> Shows a snapshot of the running processes, with owner, CPU, memory, state and command line.

![ps output](../assets/screenshots/08-processes/ps.png)

## Syntax

```bash
ps [OPTION]...
```

## Options

| Option | Description |
|--------|-------------|
| `aux` | All processes of all users, with CPU, memory and command line (BSD style) |
| `-ef` | All processes with parent process (`PPID`) and start time |
| `-u USER` | Only processes of `USER` |
| `-C NAME` | Only processes with this command name |
| `-p PID` | Only the process with this PID |
| `-o FIELDS` | Choose the columns, e.g. `pid,user,%cpu,%mem,cmd` |
| `--sort=FIELD` | Sort by a column, `-` in front for descending, e.g. `--sort=-%mem` |
| `--forest` | Show parent and child processes as a tree |

## Examples

**Show all processes:**

```bash
ps aux | head -n 5
```

```text
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3  24312 13460 ?        Ss   Oct14   0:21 /sbin/init
root         640  0.0  0.2  15444  9220 ?        Ss   Oct14   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         812  0.0  0.0  11360  1820 ?        Ss   Oct14   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data     813  0.0  0.1  12968  5876 ?        S    Oct14   0:03 nginx: worker process
```

| Column | Meaning |
|--------|---------|
| `%CPU`, `%MEM` | Share of CPU time and memory |
| `VSZ`, `RSS` | Virtual and actually used memory in KB |
| `TTY` | Terminal, `?` for services without a terminal |
| `STAT` | State (`S` sleeping, `R` running, `s` session leader, …) |
| `START`, `TIME` | Start time and CPU time used so far |

**Show the processes of a program with their parent:**

```bash
ps -fC nginx
```

```text
UID          PID    PPID  C STIME TTY          TIME CMD
root         812       1  0 Oct14 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data     813     812  0 Oct14 ?        00:00:03 nginx: worker process
www-data     814     812  0 Oct14 ?        00:00:03 nginx: worker process
```

The workers (`813`, `814`) were started by the master process (`812`).

**Find the processes that use the most memory:**

```bash
ps -eo pid,user,%mem,%cpu,comm --sort=-%mem | head -n 4
```

```text
    PID USER     %MEM %CPU COMMAND
    905 postgres  4.1  0.2 postgres
   1310 www-data  2.3  0.5 php-fpm8.4
    812 root      0.0  0.0 nginx
```

**Show how long a process has been running:**

```bash
ps -o pid,ppid,stat,etime,cmd -p 812
```

```text
    PID    PPID STAT     ELAPSED CMD
    812       1 Ss   12-03:05:21 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
```

`12-03:05:21` means 12 days, 3 hours, 5 minutes and 21 seconds.

**Find zombie processes:**

```bash
ps -eo stat,pid,ppid,comm | awk '$1 ~ /^Z/'
```

```text
Z       4021    4010 worker
```

The zombie `4021` waits for its parent `4010`. Only the parent can clean it up.

## When do I need it?

- To check whether a program or service is running at all
- To find the PID of a process before you end it or look at it more closely
- To find out which processes use the most CPU or memory
- To see who started a process, as which user, and with which options

!!! tip "`ps aux` or `ps -ef`?"
    Both show all processes. `ps aux` also shows CPU and memory, `ps -ef` the parent
    process. Use whichever fits the question, the result is the same list.

!!! warning "`ps aux | grep` finds itself"
    `ps aux | grep nginx` also shows the `grep` process itself. Use
    [`pgrep`](pgrep.md) instead, or the trick `ps aux | grep '[n]ginx'`.

## Related commands

[uptime](../01-orientation/uptime.md) · [grep](../05-text-processing/grep.md) · [pgrep](pgrep.md) · [pstree](pstree.md) · [top](top.md)
