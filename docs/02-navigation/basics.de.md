# Die wichtigsten Verzeichnisse auf einem Linux-Server

| Verzeichnis | Inhalt |
|-------------|--------|
| `/` | Wurzel des Dateisystems, hier beginnt alles |
| `/etc` | Konfigurationsdateien des Systems und aller Dienste |
| `/home` | Home-Verzeichnisse der Benutzer (`/home/nox`) |
| `/root` | Home-Verzeichnis des Benutzers `root` |
| `/var/log` | Logdateien |
| `/var/lib` | Daten von Programmen und Diensten (Datenbanken, Docker, Paketlisten) |
| `/var/www` | Webinhalte unter Debian und Ubuntu (RHEL: `/var/www/html`, Arch: `/srv/http`) |
| `/srv` | Daten, die der Server bereitstellt (Websites, FTP, Git-Repositories) |
| `/opt` | Zusätzliche Software, die nicht über `apt` installiert wurde |
| `/usr/local` | Selbst installierte Software und Skripte |
| `/usr/bin` | Programme (`/bin` ist ein Link darauf) |
| `/tmp` | Temporäre Dateien; unter Debian 13 und Arch im RAM und bei jedem Neustart leer |
| `/boot` | Kernel und Bootloader |
| `/proc`, `/sys` | Virtuelle Dateisysteme mit Live-Informationen aus dem Kernel |
| `/dev` | Geräte (Festplatten, Terminals) |
| `/mnt`, `/media` | Einhängepunkte für zusätzliche Laufwerke |
