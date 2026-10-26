---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-shield-lock-outline:{ .tc-hero-icon }

# Rechte

Wer darf eine Datei lesen, ändern oder ausführen? Besitzer, Gruppen, Rechte, ACLs und
Attribute, und wie du herausfindest, warum etwas „Permission denied“ meldet.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Besitzer, Gruppe, rwx und Oktalschreibweise erklärt :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Grundrechte

<div class="grid cards" markdown>

-   :material-lock-open-variant-outline:{ .lg .middle } **[chmod](chmod.md)**

    ---

    Ändert Rechte als Zahl oder mit Buchstaben.

-   :material-account-key-outline:{ .lg .middle } **[chown](chown.md)**

    ---

    Ändert Besitzer und Gruppe von Dateien.

-   :material-account-group-outline:{ .lg .middle } **[chgrp](chgrp.md)**

    ---

    Ändert nur die Gruppe von Dateien.

-   :material-shield-account-outline:{ .lg .middle } **[umask](umask.md)**

    ---

    Legt die Standardrechte für neue Dateien fest.

</div>

## Fehlersuche

<div class="grid cards" markdown>

-   :material-folder-search-outline:{ .lg .middle } **[namei](namei.md)**

    ---

    Zeigt die Rechte jedes Verzeichnisses entlang eines Pfads.

</div>

## Zugriffslisten (ACLs)

<div class="grid cards" markdown>

-   :material-playlist-check:{ .lg .middle } **[getfacl](getfacl.md)**

    ---

    Zeigt zusätzliche Rechte für einzelne Benutzer und Gruppen.

-   :material-playlist-edit:{ .lg .middle } **[setfacl](setfacl.md)**

    ---

    Gibt einzelnen Benutzern oder Gruppen zusätzliche Rechte.

</div>

## Dateiattribute

<div class="grid cards" markdown>

-   :material-tag-search-outline:{ .lg .middle } **[lsattr](lsattr.md)**

    ---

    Zeigt besondere Attribute wie unveränderlich oder nur anhängen.

-   :material-tag-edit-outline:{ .lg .middle } **[chattr](chattr.md)**

    ---

    Schützt Dateien mit Attributen wie unveränderlich.

</div>
