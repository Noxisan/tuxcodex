---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-cog-transfer-outline:{ .tc-hero-icon }

# Processes

Finding running programs, watching CPU and memory, stopping processes that hang, and
controlling jobs and priorities.

</div>

## Find processes

<div class="grid cards" markdown>

-   :material-format-list-bulleted-square:{ .lg .middle } **[ps](ps.md)**

    ---

    Show running processes with CPU, memory and command line.

-   :material-magnify-scan:{ .lg .middle } **[pgrep](pgrep.md)**

    ---

    Find PIDs by name, user or command line.

-   :material-identifier:{ .lg .middle } **[pidof](pidof.md)**

    ---

    Print the PIDs of a running program.

-   :material-file-tree:{ .lg .middle } **[pstree](pstree.md)**

    ---

    Show processes as a tree of parents and children.

</div>

## Watch the system

<div class="grid cards" markdown>

-   :material-chart-line:{ .lg .middle } **[top](top.md)**

    ---

    Watch CPU, memory and the busiest processes live.

-   :material-monitor-dashboard:{ .lg .middle } **[htop](htop.md)**

    ---

    Comfortable live view with search, filter and tree.

-   :material-memory:{ .lg .middle } **[free](free.md)**

    ---

    Used, free and available memory and swap.

-   :material-file-lock-outline:{ .lg .middle } **[lsof](lsof.md)**

    ---

    Open files, ports and who holds them.

</div>

## Stop processes

<div class="grid cards" markdown>

-   :material-close-octagon-outline:{ .lg .middle } **[kill](kill.md)**

    ---

    Send a signal to a process by PID.

-   :material-close-circle-multiple-outline:{ .lg .middle } **[pkill](pkill.md)**

    ---

    Send a signal to processes by name.

-   :material-skull-crossbones-outline:{ .lg .middle } **[killall](killall.md)**

    ---

    Signal all processes with an exact name.

-   :material-timer-sand-complete:{ .lg .middle } **[timeout](timeout.md)**

    ---

    End a command after a time limit.

</div>

## Understanding processes

Every running program is a process with a number, the **PID**. Every process (except
PID 1) was started by another process, its parent (**PPID**).

Process states, as shown by `ps` and `top` in the `STAT` or `S` column:

| State | Meaning |
|-------|---------|
| `R` | Running, or waiting for the CPU |
| `S` | Sleeping, waiting for an event (most processes, most of the time) |
| `D` | Waiting for disk or network I/O, can't be interrupted |
| `T` | Stopped, for example with ++ctrl+z++ |
| `Z` | Zombie: finished, but the parent hasn't collected its exit status yet |

The most important signals:

| Signal | Number | Meaning | Typical use |
|--------|--------|---------|-------------|
| `HUP` | 1 | Hang up | Many services reload their configuration |
| `INT` | 2 | Interrupt | What ++ctrl+c++ sends |
| `KILL` | 9 | Kill | End immediately, the process can't react (last resort) |
| `TERM` | 15 | Terminate | End cleanly, the default of `kill` |
| `STOP` | 19 | Stop | Pause the process |
| `CONT` | 18 | Continue | Let a stopped process continue |

!!! tip "Services belong to systemd"
    Services like nginx or PostgreSQL are started and stopped with `systemctl`, which is
    covered in the chapter on systemd. The commands in this chapter help you find out
    what is running and handle processes that don't react any more.

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
