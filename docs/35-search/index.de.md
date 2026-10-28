---
title: "Suche mit Elasticsearch und OpenSearch"
icon: material/text-search
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-search:{ .tc-hero-icon }

# Suche mit Elasticsearch und OpenSearch

Einen Such-Cluster betreiben: Zustand, Indizes und Shards über die REST-API prüfen,
Passwörter zurücksetzen, Geheimnisse im Keystore ablegen und Plugins verwalten.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Elasticsearch oder OpenSearch, Installation und Pfade, die REST-API mit curl, grün, gelb und rot, Speicher und Systemeinstellungen :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Elasticsearch

<div class="grid cards" markdown>

-   :material-lock-reset:{ .lg .middle } **[elasticsearch-reset-password](elasticsearch-reset-password.md)**

    ---

    Neues Passwort für elastic und andere eingebaute Benutzer.

-   :material-key-chain-variant:{ .lg .middle } **[elasticsearch-keystore](elasticsearch-keystore.md)**

    ---

    Geheime Einstellungen wie S3-Schlüssel.

-   :material-puzzle-outline:{ .lg .middle } **[elasticsearch-plugin](elasticsearch-plugin.md)**

    ---

    Plugins installieren, auflisten und entfernen.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-web-check:{ .lg .middle } **[curl](../11-network/curl.md)**

    ---

    Mit der REST-API sprechen. Behandelt im Kapitel Netzwerk.

-   :material-code-json:{ .lg .middle } **[jq](../05-text-processing/jq.md)**

    ---

    Die JSON-Antworten filtern. Behandelt im Kapitel Textverarbeitung.

-   :material-tune:{ .lg .middle } **[sysctl](../27-performance/sysctl.md)**

    ---

    vm.max_map_count setzen. Behandelt im Kapitel Leistung.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Port 9200 nur für Anwendungsserver öffnen. Behandelt im Kapitel Netzwerk.

</div>
