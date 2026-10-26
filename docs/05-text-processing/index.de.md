---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-search:{ .tc-hero-icon }

# Textverarbeitung

Text suchen, filtern, sortieren, zählen und ändern: die Alltagswerkzeuge für Logs,
Konfigurationsdateien und die Ausgaben anderer Befehle.

</div>

## Zählen und sortieren

<div class="grid cards" markdown>

-   :material-counter:{ .lg .middle } **[wc](wc.md)**

    ---

    Zählt Zeilen, Wörter und Bytes.

-   :material-sort-alphabetical-ascending:{ .lg .middle } **[sort](sort.md)**

    ---

    Sortiert Zeilen alphabetisch, numerisch oder nach Spalte.

-   :material-filter-variant-remove:{ .lg .middle } **[uniq](uniq.md)**

    ---

    Entfernt oder zählt wiederholte Zeilen.

</div>

## Zerschneiden und umwandeln

<div class="grid cards" markdown>

-   :material-content-cut:{ .lg .middle } **[cut](cut.md)**

    ---

    Schneidet Spalten oder Zeichen aus jeder Zeile heraus.

-   :material-swap-horizontal:{ .lg .middle } **[tr](tr.md)**

    ---

    Ersetzt, verdichtet oder löscht Zeichen.

-   :material-table-large:{ .lg .middle } **[column](column.md)**

    ---

    Formatiert Text in ausgerichtete Spalten.

</div>

## Suchen und ersetzen

<div class="grid cards" markdown>

-   :material-text-box-search-outline:{ .lg .middle } **[grep](grep.md)**

    ---

    Sucht und filtert Zeilen mit Mustern und regulären Ausdrücken.

-   :material-find-replace:{ .lg .middle } **[sed](sed.md)**

    ---

    Ersetzt Text, löscht Zeilen und gibt Bereiche aus, auch direkt in Dateien.

-   :material-code-braces:{ .lg .middle } **[awk](awk.md)**

    ---

    Wertet Text spaltenweise aus: filtern, zählen und summieren.

</div>

## Befehle mit Pipes verbinden

Ihre eigentliche Stärke zeigen diese Werkzeuge erst in Kombination. Jeder Befehl erledigt
eine Aufgabe, und du verbindest sie zu einer Kette:

| Zeichen | Bedeutung | Beispiel |
|---------|-----------|----------|
| `|` | Ausgabe eines Befehls an den nächsten weitergeben | `grep 404 access.log | wc -l` |
| `>` | Ausgabe in eine Datei schreiben und sie überschreiben | `sort names.txt > sorted.txt` |
| `>>` | Ausgabe an eine Datei anhängen | `date >> run.log` |
| `2>` | Fehlermeldungen in eine Datei schreiben | `find / -name x 2> errors.txt` |
| `2>&1` | Fehlermeldungen dorthin schicken, wo auch die Ausgabe landet | `./backup.sh > backup.log 2>&1` |

Ein Klassiker aus dem Admin-Alltag, die IP-Adressen mit den meisten Anfragen:

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

```text
      4 198.51.100.23
      2 192.0.2.77
      2 192.0.2.10
      1 192.0.2.55
```

`awk` nimmt die erste Spalte (die IP), `sort` gruppiert gleiche Adressen, `uniq -c` zählt
sie, `sort -rn` setzt die höchste Zahl nach oben, und `head` behält die Top 10.

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
