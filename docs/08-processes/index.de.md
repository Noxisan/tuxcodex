---
icon: material/cog-transfer-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-cog-transfer-outline:{ .tc-hero-icon }

# Prozesse

Laufende Programme finden, CPU und Arbeitsspeicher beobachten, hängende Prozesse beenden
und Jobs und Prioritäten steuern.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** PID, Prozesszustände und Signale :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

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

## System beobachten

<div class="grid cards" markdown>

-   :material-chart-line:{ .lg .middle } **[top](top.md)**

    ---

    Zeigt CPU, Speicher und die aktivsten Prozesse live.

-   :material-monitor-dashboard:{ .lg .middle } **[htop](htop.md)**

    ---

    Komfortable Live-Ansicht mit Suche, Filter und Baum.

-   :material-memory:{ .lg .middle } **[free](free.md)**

    ---

    Belegter, freier und verfügbarer Speicher und Swap.

-   :material-file-lock-outline:{ .lg .middle } **[lsof](lsof.md)**

    ---

    Offene Dateien, Ports und wer sie hält.

-   :material-eye-refresh-outline:{ .lg .middle } **[watch](watch.md)**

    ---

    Einen Befehl wiederholt ausführen und Änderungen sehen.

</div>

## Prozesse beenden

<div class="grid cards" markdown>

-   :material-close-octagon-outline:{ .lg .middle } **[kill](kill.md)**

    ---

    Einem Prozess per PID ein Signal senden.

-   :material-close-circle-multiple-outline:{ .lg .middle } **[pkill](pkill.md)**

    ---

    Prozessen per Name ein Signal senden.

-   :material-skull-crossbones-outline:{ .lg .middle } **[killall](killall.md)**

    ---

    Allen Prozessen mit exaktem Namen ein Signal senden.

-   :material-timer-sand-complete:{ .lg .middle } **[timeout](timeout.md)**

    ---

    Einen Befehl nach einem Zeitlimit beenden.

</div>

## Jobs und Hintergrund

<div class="grid cards" markdown>

-   :material-format-list-checks:{ .lg .middle } **[jobs](jobs.md)**

    ---

    Hintergrund- und angehaltene Befehle dieser Shell.

-   :material-play-pause:{ .lg .middle } **[bg](bg.md)**

    ---

    Einen angehaltenen Job im Hintergrund fortsetzen.

-   :material-arrow-up-bold-box-outline:{ .lg .middle } **[fg](fg.md)**

    ---

    Einen Job in den Vordergrund zurückholen.

-   :material-shield-sun-outline:{ .lg .middle } **[nohup](nohup.md)**

    ---

    Einen Befehl nach dem Abmelden weiterlaufen lassen.

</div>

## Prioritäten

<div class="grid cards" markdown>

-   :material-speedometer-slow:{ .lg .middle } **[nice](nice.md)**

    ---

    Einen Befehl mit anderer Priorität starten.

-   :material-tune-variant:{ .lg .middle } **[renice](renice.md)**

    ---

    Die Priorität eines laufenden Prozesses ändern.

</div>
