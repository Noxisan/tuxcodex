---
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

</div>
