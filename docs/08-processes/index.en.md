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

[:material-school-outline:{ .tc-basics-icon } **Basics:** PID, process states and signals :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

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

-   :material-eye-refresh-outline:{ .lg .middle } **[watch](watch.md)**

    ---

    Run a command repeatedly and watch it change.

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

## Jobs and background

<div class="grid cards" markdown>

-   :material-format-list-checks:{ .lg .middle } **[jobs](jobs.md)**

    ---

    Background and paused commands of this shell.

-   :material-play-pause:{ .lg .middle } **[bg](bg.md)**

    ---

    Continue a paused job in the background.

-   :material-arrow-up-bold-box-outline:{ .lg .middle } **[fg](fg.md)**

    ---

    Bring a job back to the foreground.

-   :material-shield-sun-outline:{ .lg .middle } **[nohup](nohup.md)**

    ---

    Keep a command running after logout.

</div>

## Priorities

<div class="grid cards" markdown>

-   :material-speedometer-slow:{ .lg .middle } **[nice](nice.md)**

    ---

    Start a command with a different priority.

-   :material-tune-variant:{ .lg .middle } **[renice](renice.md)**

    ---

    Change the priority of a running process.

</div>
