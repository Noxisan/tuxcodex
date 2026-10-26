---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-folder-outline:{ .tc-hero-icon }

# Navigation

Im Dateisystem bewegen: Wo bin ich, was liegt hier, und wo ist die Datei, die ich suche?

</div>

## Wo bin ich, und wohin kann ich?

<div class="grid cards" markdown>

-   :material-folder-marker-outline:{ .lg .middle } **[pwd](pwd.md)**

    ---

    Zeigt das Verzeichnis, in dem du gerade bist.

-   :material-folder-arrow-right-outline:{ .lg .middle } **[cd](cd.md)**

    ---

    Wechselt das aktuelle Verzeichnis.

-   :material-layers-plus:{ .lg .middle } **[pushd](pushd.md)**

    ---

    Wechselt das Verzeichnis und merkt sich das vorherige auf einem Stapel.

-   :material-layers-minus:{ .lg .middle } **[popd](popd.md)**

    ---

    Springt zum vorherigen Verzeichnis auf dem Stapel zurück.

</div>

## Was liegt hier?

<div class="grid cards" markdown>

-   :material-view-list-outline:{ .lg .middle } **[ls](ls.md)**

    ---

    Listet Verzeichnisinhalte mit Rechten, Besitzer, Größe und Datum.

-   :material-file-tree-outline:{ .lg .middle } **[tree](tree.md)**

    ---

    Zeigt ein Verzeichnis samt Unterverzeichnissen als Baum.

</div>

## Wo ist es?

<div class="grid cards" markdown>

-   :material-file-search-outline:{ .lg .middle } **[find](find.md)**

    ---

    Sucht Dateien nach Name, Typ, Größe, Alter oder Besitzer.

-   :material-database-search-outline:{ .lg .middle } **[locate](locate.md)**

    ---

    Findet Dateien blitzschnell über eine Datenbank.

</div>

## Die wichtigsten Verzeichnisse auf einem Debian-Server

| Verzeichnis | Inhalt |
|-------------|--------|
| `/` | Wurzel des Dateisystems, hier beginnt alles |
| `/etc` | Konfigurationsdateien des Systems und aller Dienste |
| `/home` | Home-Verzeichnisse der Benutzer (`/home/nox`) |
| `/root` | Home-Verzeichnis des Benutzers `root` |
| `/var/log` | Logdateien |
| `/var/lib` | Daten von Programmen und Diensten (Datenbanken, Docker, Paketlisten) |
| `/var/www` | Webinhalte (Standard für Apache und nginx unter Debian) |
| `/srv` | Daten, die der Server bereitstellt (Websites, FTP, Git-Repositories) |
| `/opt` | Zusätzliche Software, die nicht über `apt` installiert wurde |
| `/usr/local` | Selbst installierte Software und Skripte |
| `/usr/bin` | Programme (`/bin` ist ein Link darauf) |
| `/tmp` | Temporäre Dateien; seit Debian 13 im RAM und bei jedem Neustart leer |
| `/boot` | Kernel und Bootloader |
| `/proc`, `/sys` | Virtuelle Dateisysteme mit Live-Informationen aus dem Kernel |
| `/dev` | Geräte (Festplatten, Terminals) |
| `/mnt`, `/media` | Einhängepunkte für zusätzliche Laufwerke |

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
