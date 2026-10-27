---
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
