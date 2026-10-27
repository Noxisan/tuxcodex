---
icon: material/radar
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-radar:{ .tc-hero-icon }

# Sicherheitsprüfung

Die eigenen Server von außen und von innen prüfen: offene Ports und Dienste, Härtung,
Rootkits und Schadsoftware, veränderte Systemdateien und verwundbare Container-Images.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Angriffsfläche, was welches Werkzeug findet, was du installieren musst, und die Regeln fürs Scannen :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Von außen

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **[nmap](nmap.md)**

    ---

    Offene Ports, Dienste und Versionen.

-   :material-web:{ .lg .middle } **[nikto](nikto.md)**

    ---

    Bekannte Probleme eines Webservers.

</div>

## Härtung prüfen

<div class="grid cards" markdown>

-   :material-shield-check-outline:{ .lg .middle } **[lynis](lynis.md)**

    ---

    Sicherheitsaudit mit Vorschlägen.

</div>

## Einbrüche und Schadsoftware

<div class="grid cards" markdown>

-   :material-bug-outline:{ .lg .middle } **[rkhunter](rkhunter.md)**

    ---

    Nach Rootkits und Hintertüren suchen.

-   :material-bug-check-outline:{ .lg .middle } **[chkrootkit](chkrootkit.md)**

    ---

    Zweite Meinung zu Rootkits.

</div>
