---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-compass-outline:{ .tc-hero-icon }

# Orientation

Who am I, where am I, and what is going on on this machine? These are the first
commands to run after logging in to a server.

</div>

## Who am I?

<div class="grid cards" markdown>

-   :material-account-outline:{ .lg .middle } **[whoami](whoami.md)**

    ---

    Show the user you are working as.

-   :material-card-account-details-outline:{ .lg .middle } **[id](id.md)**

    ---

    Show user ID, group ID and group memberships.

</div>

## Which machine am I on?

<div class="grid cards" markdown>

-   :material-tag-outline:{ .lg .middle } **[hostname](hostname.md)**

    ---

    Show the host name and IP addresses, or set the name temporarily.

-   :material-cog-outline:{ .lg .middle } **[hostnamectl](hostnamectl.md)**

    ---

    Show system information and set the host name permanently.

-   :material-chip:{ .lg .middle } **[uname](uname.md)**

    ---

    Show kernel release and architecture.

</div>

## What is going on?

<div class="grid cards" markdown>

-   :material-timer-outline:{ .lg .middle } **[uptime](uptime.md)**

    ---

    Show uptime, logged-in users and load average.

-   :material-account-group-outline:{ .lg .middle } **[who](who.md)**

    ---

    Show who is logged in and from where.

-   :material-monitor-eye:{ .lg .middle } **[w](w.md)**

    ---

    Show who is logged in and what they are doing.

-   :material-history:{ .lg .middle } **[last](last.md)**

    ---

    Show the login and reboot history.

</div>

## The first minute on a new server

Five commands that give you a complete picture right after logging in:

```bash
whoami        # am I the right user?
hostnamectl   # which machine, OS and kernel?
uptime        # how long has it been running, how high is the load?
w             # who else is logged in, and what is running?
last -n 5     # who logged in recently?
```

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order –
    later pages build on the earlier ones.
