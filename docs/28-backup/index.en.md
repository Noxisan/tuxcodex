---
icon: material/backup-restore
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-backup-restore:{ .tc-hero-icon }

# Backup

Backing up servers properly: database dumps, encrypted and deduplicated backups with
restic and borg, retention and, above all, testing the restore.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** The 3-2-1 rule, what to back up, restic or borg, and a complete backup routine :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Database dumps

<div class="grid cards" markdown>

-   :material-database-export-outline:{ .lg .middle } **[pg_dump](pg_dump.md)**

    ---

    Back up PostgreSQL while it runs.

-   :material-database-arrow-down-outline:{ .lg .middle } **[mysqldump](mysqldump.md)**

    ---

    Back up MySQL and MariaDB.

</div>

## Backup tools

<div class="grid cards" markdown>

-   :material-backup-restore:{ .lg .middle } **[restic](restic.md)**

    ---

    Encrypted backups, also to the cloud.

-   :material-archive-arrow-up-outline:{ .lg .middle } **[borg](borg.md)**

    ---

    Deduplicated archives over SSH.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-folder-zip-outline:{ .lg .middle } **[tar](../14-archives/tar.md)**

    ---

    Simple archives for one-off copies. Covered in the chapter Archives.

-   :material-folder-sync-outline:{ .lg .middle } **[rsync](../12-ssh/rsync.md)**

    ---

    Mirror directories to another server. Covered in the chapter SSH.

-   :material-calendar-clock:{ .lg .middle } **[crontab](../16-scheduling/crontab.md)**

    ---

    Run the backup every night. Covered in the chapter Scheduling.

-   :material-file-lock-outline:{ .lg .middle } **[age](../24-certificates/age.md)**

    ---

    Encrypt single backup files. Covered in the chapter Certificates and encryption.

</div>
