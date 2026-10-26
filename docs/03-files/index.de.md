---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-file-document-outline:{ .tc-hero-icon }

# Dateien

Dateien und Verzeichnisse anlegen, kopieren, verschieben, verlinken und löschen, und
herausfinden, was eine Datei wirklich ist.

</div>

## Sicher arbeiten mit Dateien

Die meisten Fehler mit Dateien passieren in einer Sekunde und lassen sich nicht
rückgängig machen. Diese Gewohnheiten schützen dich auf jedem Server:

| Gewohnheit | Beispiel |
|------------|----------|
| Vor dem Bearbeiten einer Konfiguration eine Kopie anlegen | `cp sshd_config{,.bak}` |
| Wildcards erst mit `ls` testen, dann mit `rm` oder `mv` verwenden | `ls *.log` → `rm *.log` |
| `cp`, `mv` und `rm` vor dem Überschreiben oder Löschen nachfragen lassen | `cp -i`, `mv -i`, `rm -i` |
| Mit Rechten und Zeitstempeln kopieren | `cp -a` statt `cp -r` |
| Vor relativen Pfaden prüfen, wo du bist | `pwd` |
| Namen mit Leerzeichen in Anführungszeichen setzen | `rm "old backup.tar.gz"` |

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
