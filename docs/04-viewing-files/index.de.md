---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-box-search-outline:{ .tc-hero-icon }

# Dateien anzeigen

Konfigurationsdateien, Logs und andere Dateien lesen, ohne sie zu verändern: von kurzen
Textdateien bis zu komprimierten Logs und Binärdateien.

</div>

## Ganze Datei ausgeben

<div class="grid cards" markdown>

-   :material-text-box-outline:{ .lg .middle } **[cat](cat.md)**

    ---

    Gibt Dateien aus und fügt sie zusammen.

-   :material-sort-reverse-variant:{ .lg .middle } **[tac](tac.md)**

    ---

    Gibt eine Datei rückwärts aus, letzte Zeile zuerst.

-   :material-format-list-numbered:{ .lg .middle } **[nl](nl.md)**

    ---

    Gibt eine Datei mit Zeilennummern aus.

</div>

## Seitenweise lesen

<div class="grid cards" markdown>

-   :material-book-open-page-variant-outline:{ .lg .middle } **[less](less.md)**

    ---

    Große Dateien und Logs durchblättern, durchsuchen und verfolgen.

</div>

## Anfang und Ende

<div class="grid cards" markdown>

-   :material-arrow-collapse-up:{ .lg .middle } **[head](head.md)**

    ---

    Zeigt die ersten Zeilen einer Datei.

-   :material-arrow-collapse-down:{ .lg .middle } **[tail](tail.md)**

    ---

    Zeigt die letzten Zeilen einer Datei und verfolgt Logs live.

</div>

## Komprimierte Dateien

<div class="grid cards" markdown>

-   :material-zip-box-outline:{ .lg .middle } **[zcat](zcat.md)**

    ---

    Gibt gzip-komprimierte Dateien aus, ohne sie zu entpacken.

-   :material-book-open-variant:{ .lg .middle } **[zless](zless.md)**

    ---

    Komprimierte Dateien seitenweise lesen und durchsuchen.

</div>

## Logs lesen

| Aufgabe | Befehl |
|---------|--------|
| Ein Log live verfolgen, während du testest | `tail -f /var/log/nginx/error.log` |
| Die letzten 50 Zeilen anzeigen | `tail -n 50 /var/log/nginx/error.log` |
| Ein großes Log durchblättern und durchsuchen | `less /var/log/nginx/access.log`, dann `/` zum Suchen |
| Ein rotiertes, komprimiertes Log lesen | `zless /var/log/nginx/access.log.2.gz` |
| Die neuesten Zeilen zuerst anzeigen | `tac /var/log/nginx/access.log | less` |

!!! tip "Logs von systemd-Diensten"
    Viele Dienste unter Debian schreiben keine eigenen Logdateien, sondern ins
    systemd-Journal. Diese liest du mit `journalctl`, das im Kapitel über Logs
    ausführlich behandelt wird.

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
