---
title: "SELinux and AppArmor"
icon: material/shield-lock-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-shield-lock-outline:{ .tc-hero-icon }

# SELinux and AppArmor

Mandatory access control: why a service gets "Permission denied" although the file
permissions are right, and how to fix it properly instead of switching the protection off.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** How SELinux and AppArmor work, which distribution uses which, and the way from a denial to a fix :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## SELinux: status and mode

<div class="grid cards" markdown>

-   :material-shield-half-full:{ .lg .middle } **[getenforce](getenforce.md)**

    ---

    Show the SELinux mode.

-   :material-toggle-switch-outline:{ .lg .middle } **[setenforce](setenforce.md)**

    ---

    Switch between enforcing and permissive.

-   :material-information-outline:{ .lg .middle } **[sestatus](sestatus.md)**

    ---

    The full SELinux status.

</div>

## SELinux: fixing denials

<div class="grid cards" markdown>

-   :material-tag-text-outline:{ .lg .middle } **[semanage](semanage.md)**

    ---

    File labels, ports and booleans permanently.

-   :material-label-outline:{ .lg .middle } **[restorecon](restorecon.md)**

    ---

    Reset file labels.

-   :material-toggle-switch-off-outline:{ .lg .middle } **[setsebool](setsebool.md)**

    ---

    Switch ready-made exceptions.

-   :material-shield-alert-outline:{ .lg .middle } **[audit2allow](audit2allow.md)**

    ---

    Explain denials, create modules.

</div>

## AppArmor

<div class="grid cards" markdown>

-   :material-shield-check-outline:{ .lg .middle } **[aa-status](aa-status.md)**

    ---

    Loaded profiles and protected processes.

-   :material-wrench-outline:{ .lg .middle } **[aa-complain](aa-complain.md)**

    ---

    Switch profiles between complain and enforce.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-magnify-scan:{ .lg .middle } **[ausearch](../15-logs/ausearch.md)**

    ---

    `ausearch -m AVC -ts recent` finds the SELinux denials. Covered in the chapter Logs.

-   :material-format-list-bulleted:{ .lg .middle } **[ls](../02-navigation/ls.md)**

    ---

    `ls -Z` shows the SELinux label of files. Covered in the chapter Navigation.

-   :material-format-list-checks:{ .lg .middle } **[ps](../08-processes/ps.md)**

    ---

    `ps -eZ` shows the SELinux domain of processes. Covered in the chapter Processes.

-   :material-text-box-search-outline:{ .lg .middle } **[journalctl](../09-systemd/journalctl.md)**

    ---

    `journalctl -k` shows AppArmor denials in the kernel log. Covered in the chapter systemd.

</div>
