---
icon: material/school-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-school-outline:{ .tc-hero-icon }

# Basics overview

Every chapter starts with a basics page: the concepts, tables and workflows you need
before the individual commands make sense. Here they are all in one place, in the order of
the handbook.

</div>

## Linux basics

<div class="grid cards tc-basics-cards" markdown>

-   :material-compass-outline:{ .lg .middle } **[Orientation](01-orientation/basics.md)**

    ---

    The first minute on a new server, as a command sequence

-   :material-folder-outline:{ .lg .middle } **[Navigation](02-navigation/basics.md)**

    ---

    The most important directories on a Linux server

-   :material-file-document-outline:{ .lg .middle } **[Files](03-files/basics.md)**

    ---

    Rules for working safely with files

-   :material-text-box-search-outline:{ .lg .middle } **[Viewing files](04-viewing-files/basics.md)**

    ---

    Reading logs: the right command for each task

-   :material-text-search:{ .lg .middle } **[Text processing](05-text-processing/basics.md)**

    ---

    Combining commands with pipes

-   :material-shield-lock-outline:{ .lg .middle } **[Permissions](06-permissions/basics.md)**

    ---

    Owner, group, rwx and octal notation explained

-   :material-account-multiple-outline:{ .lg .middle } **[Users and groups](07-users-groups/basics.md)**

    ---

    The important files: passwd, shadow, group, sudoers

-   :material-cog-transfer-outline:{ .lg .middle } **[Processes](08-processes/basics.md)**

    ---

    PID, process states and signals

-   :material-cog-sync-outline:{ .lg .middle } **[systemd and services](09-systemd/basics.md)**

    ---

    Units, unit files and their states

-   :material-package-variant-closed:{ .lg .middle } **[Packages](10-packages/basics.md)**

    ---

    Repositories, dependencies and `apt`, `dnf` and `pacman` side by side

-   :material-lan:{ .lg .middle } **[Network](11-network/basics.md)**

    ---

    IP addresses, subnets, ports, DNS and where each distribution keeps its network configuration

-   :material-console-network-outline:{ .lg .middle } **[SSH](12-ssh/basics.md)**

    ---

    Host keys, key authentication, the files in `~/.ssh` and the client configuration

-   :material-harddisk:{ .lg .middle } **[Disks and storage](13-disks-storage/basics.md)**

    ---

    Block devices, partition tables, file systems, `/etc/fstab` and LVM

-   :material-archive-arrow-down-outline:{ .lg .middle } **[Archives](14-archives/basics.md)**

    ---

    Archiving vs. compressing, file extensions and the methods compared

-   :material-text-box-multiple-outline:{ .lg .middle } **[Logs](15-logs/basics.md)**

    ---

    Where logs are kept, log levels and log rotation

-   :material-calendar-clock:{ .lg .middle } **[Scheduling](16-scheduling/basics.md)**

    ---

    cron syntax, where cron jobs live and systemd timers compared

-   :material-speedometer:{ .lg .middle } **[Performance and kernel](27-performance/basics.md)**

    ---

    The four resources, reading load, where the bottleneck is, and what to install

-   :material-backup-restore:{ .lg .middle } **[Backup](28-backup/basics.md)**

    ---

    The 3-2-1 rule, what to back up, restic or borg, and a complete backup routine

</div>

## Automation & DevOps

<div class="grid cards tc-basics-cards" markdown>

-   :material-script-text-outline:{ .lg .middle } **[Bash scripting](17-bash-scripting/basics.md)**

    ---

    How a script is built: shebang, quoting, variables, arguments and exit codes

-   :material-git:{ .lg .middle } **[Git](18-git/basics.md)**

    ---

    Working directory, staging area and repository, `.gitignore`, SSH keys and the daily workflow

-   :material-docker:{ .lg .middle } **[Docker](19-docker/basics.md)**

    ---

    Images and containers, installation, ports and volumes, a Dockerfile and a compose.yaml

-   :material-kubernetes:{ .lg .middle } **[Kubernetes](20-kubernetes/basics.md)**

    ---

    What you need to install, pods, deployments and services, manifests and kubeconfig

-   :material-ansible:{ .lg .middle } **[Ansible](21-ansible/basics.md)**

    ---

    Control node and managed servers, inventory, modules, playbooks, roles and installation

-   :material-infinity:{ .lg .middle } **[CI/CD](22-ci-cd/basics.md)**

    ---

    Pipelines, jobs and runners, what to install, a workflow for GitHub and one for GitLab

</div>

## Security

<div class="grid cards tc-basics-cards" markdown>

-   :material-radar:{ .lg .middle } **[Security scanning](23-security-scanning/basics.md)**

    ---

    Attack surface, what each tool finds, what to install, and the rules for scanning

-   :material-certificate-outline:{ .lg .middle } **[Certificates and encryption](24-certificates/basics.md)**

    ---

    How TLS works, certificate chains, file formats, where certificates live and what to install

-   :material-shield-lock-outline:{ .lg .middle } **[SELinux and AppArmor](25-selinux-apparmor/basics.md)**

    ---

    How SELinux and AppArmor work, which distribution uses which, and the way from a denial to a fix

-   :material-vpn:{ .lg .middle } **[VPN with WireGuard](26-wireguard/basics.md)**

    ---

    How WireGuard works, what to install, a complete server and client setup and the firewall

</div>
