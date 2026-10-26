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
