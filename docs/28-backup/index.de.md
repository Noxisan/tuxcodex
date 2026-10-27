---
icon: material/backup-restore
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-backup-restore:{ .tc-hero-icon }

# Backup

Server richtig sichern: Datenbank-Dumps, verschlüsselte und deduplizierte Backups mit
restic und borg, Aufbewahrung und vor allem das Testen der Wiederherstellung.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Die 3-2-1-Regel, was gesichert wird, restic oder borg und ein vollständiger Backup-Ablauf :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Datenbank-Dumps

<div class="grid cards" markdown>

-   :material-database-export-outline:{ .lg .middle } **[pg_dump](pg_dump.md)**

    ---

    PostgreSQL im laufenden Betrieb sichern.

-   :material-database-arrow-down-outline:{ .lg .middle } **[mysqldump](mysqldump.md)**

    ---

    MySQL und MariaDB sichern.

</div>

## Backup-Werkzeuge

<div class="grid cards" markdown>

-   :material-backup-restore:{ .lg .middle } **[restic](restic.md)**

    ---

    Verschlüsselte Backups, auch in die Cloud.

</div>
