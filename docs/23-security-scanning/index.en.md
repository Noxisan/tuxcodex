---
icon: material/radar
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-radar:{ .tc-hero-icon }

# Security scanning

Checking your own servers from the outside and the inside: open ports and services,
hardening, rootkits and malware, changed system files and vulnerable container images.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Attack surface, what each tool finds, what to install, and the rules for scanning :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## From outside

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **[nmap](nmap.md)**

    ---

    Open ports, services and versions.

-   :material-web:{ .lg .middle } **[nikto](nikto.md)**

    ---

    Known problems of a web server.

</div>

## Checking the hardening

<div class="grid cards" markdown>

-   :material-shield-check-outline:{ .lg .middle } **[lynis](lynis.md)**

    ---

    Security audit with suggestions.

</div>

## Intrusions and malware

<div class="grid cards" markdown>

-   :material-bug-outline:{ .lg .middle } **[rkhunter](rkhunter.md)**

    ---

    Search for rootkits and backdoors.

-   :material-bug-check-outline:{ .lg .middle } **[chkrootkit](chkrootkit.md)**

    ---

    Second opinion on rootkits.

-   :material-virus-outline:{ .lg .middle } **[clamscan](clamscan.md)**

    ---

    Scan files for malware.

</div>

## Integrity

<div class="grid cards" markdown>

-   :material-file-lock-outline:{ .lg .middle } **[aide](aide.md)**

    ---

    Report changed system files.

-   :material-package-variant-closed-check:{ .lg .middle } **[debsums](debsums.md)**

    ---

    Compare files with their packages.

</div>

## Containers

<div class="grid cards" markdown>

-   :material-docker:{ .lg .middle } **[trivy](trivy.md)**

    ---

    Vulnerabilities in images.

</div>
