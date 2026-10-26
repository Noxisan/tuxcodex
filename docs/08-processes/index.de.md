---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-cog-transfer-outline:{ .tc-hero-icon }

# Prozesse

Laufende Programme finden, CPU und Arbeitsspeicher beobachten, hängende Prozesse beenden
und Jobs und Prioritäten steuern.

</div>

## Prozesse finden

<div class="grid cards" markdown>

-   :material-format-list-bulleted-square:{ .lg .middle } **[ps](ps.md)**

    ---

    Zeigt laufende Prozesse mit CPU, Speicher und Kommandozeile.

-   :material-magnify-scan:{ .lg .middle } **[pgrep](pgrep.md)**

    ---

    Findet PIDs nach Name, Benutzer oder Kommandozeile.

-   :material-identifier:{ .lg .middle } **[pidof](pidof.md)**

    ---

    Gibt die PIDs eines laufenden Programms aus.

-   :material-file-tree:{ .lg .middle } **[pstree](pstree.md)**

    ---

    Zeigt Prozesse als Baum aus Eltern und Kindern.

</div>

## Prozesse verstehen

Jedes laufende Programm ist ein Prozess mit einer Nummer, der **PID**. Jeder Prozess
(außer PID 1) wurde von einem anderen Prozess gestartet, seinem Elternprozess (**PPID**).

Prozesszustände, wie `ps` und `top` sie in der Spalte `STAT` bzw. `S` anzeigen:

| Zustand | Bedeutung |
|---------|-----------|
| `R` | Läuft oder wartet auf die CPU |
| `S` | Schläft und wartet auf ein Ereignis (die meisten Prozesse, die meiste Zeit) |
| `D` | Wartet auf Festplatten- oder Netzwerk-I/O, nicht unterbrechbar |
| `T` | Angehalten, zum Beispiel mit ++ctrl+z++ |
| `Z` | Zombie: beendet, aber der Elternprozess hat den Exit-Status noch nicht abgeholt |

Die wichtigsten Signale:

| Signal | Nummer | Bedeutung | Typischer Einsatz |
|--------|--------|-----------|-------------------|
| `HUP` | 1 | Auflegen | Viele Dienste laden ihre Konfiguration neu |
| `INT` | 2 | Unterbrechen | Das, was ++ctrl+c++ sendet |
| `KILL` | 9 | Töten | Sofort beenden, der Prozess kann nicht reagieren (letztes Mittel) |
| `TERM` | 15 | Beenden | Sauber beenden, Standard bei `kill` |
| `STOP` | 19 | Anhalten | Prozess pausieren |
| `CONT` | 18 | Fortsetzen | Einen angehaltenen Prozess weiterlaufen lassen |

!!! tip "Dienste gehören zu systemd"
    Dienste wie nginx oder PostgreSQL startest und stoppst du mit `systemctl`, das im
    Kapitel über systemd behandelt wird. Die Befehle in diesem Kapitel helfen dir
    herauszufinden, was läuft, und mit Prozessen umzugehen, die nicht mehr reagieren.

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
