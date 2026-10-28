---
title: "Sicherheitsprüfung"
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

-   :material-virus-outline:{ .lg .middle } **[clamscan](clamscan.md)**

    ---

    Dateien auf Schadsoftware prüfen.

</div>

## Integrität

<div class="grid cards" markdown>

-   :material-file-lock-outline:{ .lg .middle } **[aide](aide.md)**

    ---

    Veränderte Systemdateien melden.

-   :material-package-variant-closed-check:{ .lg .middle } **[debsums](debsums.md)**

    ---

    Dateien mit ihren Paketen vergleichen.

</div>

## Container

<div class="grid cards" markdown>

-   :material-docker:{ .lg .middle } **[trivy](trivy.md)**

    ---

    Schwachstellen in Images.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-lan-connect:{ .lg .middle } **[ss](../11-network/ss.md)**

    ---

    `ss -tlnp` zeigt von innen, welche Dienste auf welchem Port lauschen. Behandelt im Kapitel Netzwerk.

-   :material-connection:{ .lg .middle } **[nc](../11-network/nc.md)**

    ---

    Einen einzelnen Port von Hand testen, ohne vollen Scan. Behandelt im Kapitel Netzwerk.

-   :material-access-point-network:{ .lg .middle } **[tcpdump](../11-network/tcpdump.md)**

    ---

    Sehen, welche Pakete bei einem Scan wirklich ankommen. Behandelt im Kapitel Netzwerk.

-   :material-wall-fire:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Die Ports schließen, die ein Scan zeigt, aber niemand braucht. Behandelt im Kapitel Netzwerk.

-   :material-shield-lock-outline:{ .lg .middle } **[fail2ban-client](../12-ssh/fail2ban-client.md)**

    ---

    Hosts sperren, die scannen oder Passwörter durchprobieren. Behandelt im Kapitel SSH.

</div>
