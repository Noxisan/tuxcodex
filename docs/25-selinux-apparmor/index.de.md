---
title: "SELinux und AppArmor"
icon: material/shield-lock-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-shield-lock-outline:{ .tc-hero-icon }

# SELinux und AppArmor

Verpflichtende Zugriffskontrolle: warum ein Dienst „Permission denied“ bekommt, obwohl die
Dateirechte stimmen, und wie du das richtig behebst, statt den Schutz abzuschalten.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Wie SELinux und AppArmor arbeiten, welche Distribution was nutzt, und der Weg von der Ablehnung zur Lösung :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## SELinux: Status und Modus

<div class="grid cards" markdown>

-   :material-shield-half-full:{ .lg .middle } **[getenforce](getenforce.md)**

    ---

    Den SELinux-Modus zeigen.

-   :material-toggle-switch-outline:{ .lg .middle } **[setenforce](setenforce.md)**

    ---

    Zwischen enforcing und permissive umschalten.

-   :material-information-outline:{ .lg .middle } **[sestatus](sestatus.md)**

    ---

    Der vollständige SELinux-Status.

</div>

## SELinux: Ablehnungen beheben

<div class="grid cards" markdown>

-   :material-tag-text-outline:{ .lg .middle } **[semanage](semanage.md)**

    ---

    Datei-Labels, Ports und Booleans dauerhaft.

-   :material-label-outline:{ .lg .middle } **[restorecon](restorecon.md)**

    ---

    Datei-Labels zurücksetzen.

-   :material-toggle-switch-off-outline:{ .lg .middle } **[setsebool](setsebool.md)**

    ---

    Fertige Ausnahmen schalten.

-   :material-shield-alert-outline:{ .lg .middle } **[audit2allow](audit2allow.md)**

    ---

    Ablehnungen erklären, Module erzeugen.

</div>

## AppArmor

<div class="grid cards" markdown>

-   :material-shield-check-outline:{ .lg .middle } **[aa-status](aa-status.md)**

    ---

    Geladene Profile und geschützte Prozesse.

-   :material-wrench-outline:{ .lg .middle } **[aa-complain](aa-complain.md)**

    ---

    Profile zwischen complain und enforce umschalten.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-magnify-scan:{ .lg .middle } **[ausearch](../15-logs/ausearch.md)**

    ---

    `ausearch -m AVC -ts recent` findet die SELinux-Ablehnungen. Behandelt im Kapitel Logs.

-   :material-format-list-bulleted:{ .lg .middle } **[ls](../02-navigation/ls.md)**

    ---

    `ls -Z` zeigt das SELinux-Label von Dateien. Behandelt im Kapitel Navigation.

-   :material-format-list-checks:{ .lg .middle } **[ps](../08-processes/ps.md)**

    ---

    `ps -eZ` zeigt die SELinux-Domäne von Prozessen. Behandelt im Kapitel Prozesse.

-   :material-text-box-search-outline:{ .lg .middle } **[journalctl](../09-systemd/journalctl.md)**

    ---

    `journalctl -k` zeigt AppArmor-Ablehnungen im Kernel-Log. Behandelt im Kapitel systemd.

</div>
