# Pakete verstehen

Unter Linux installierst du Software selten, indem du eine Datei von einer Webseite lädst.
Programme kommen als **Pakete** aus den **Paketquellen** (Repositories) deiner
Distribution: signierte Archive mit dem Programm, seinen Konfigurationsdateien und einer
Liste, was es sonst noch braucht. Ein **Paketmanager** lädt sie herunter, löst die
Abhängigkeiten auf und merkt sich jede installierte Datei.

## Paketmanager pro Distribution

| | Debian, Ubuntu | RHEL, Rocky, Alma | Arch |
|---|----------------|-------------------|------|
| Paketformat | `.deb` | `.rpm` | `.pkg.tar.zst` |
| Paketmanager | `apt` | `dnf` | `pacman` |
| Werkzeug für die untere Ebene (einzelne Dateien, keine Paketquellen) | `dpkg` | `rpm` | `pacman -U` |
| Paketquellen eingetragen in | `/etc/apt/sources.list.d/` | `/etc/yum.repos.d/` | `/etc/pacman.conf` |
| Veröffentlichungsmodell | Stabile Versionen | Stabile Versionen mit langem Support | Rolling Release |

Das Werkzeug der oberen Ebene (`apt`, `dnf`) spricht mit den Paketquellen und löst
Abhängigkeiten auf. Das Werkzeug der unteren Ebene (`dpkg`, `rpm`) arbeitet nur mit
Paketdateien und der Datenbank der installierten Pakete.

## Dieselbe Aufgabe mit `apt`, `dnf` und `pacman`

| Aufgabe | `apt` | `dnf` | `pacman` |
|---------|-------|-------|----------|
| Paketlisten aktualisieren | `apt update` | `dnf makecache` | `pacman -Sy` (nur zusammen mit `-u`) |
| Alle Updates installieren | `apt upgrade` | `dnf upgrade` | `pacman -Syu` |
| Ein Paket installieren | `apt install nginx` | `dnf install nginx` | `pacman -S nginx` |
| Ein Paket entfernen | `apt remove nginx` | `dnf remove nginx` | `pacman -R nginx` |
| Samt Konfiguration entfernen | `apt purge nginx` | *(gibt es nicht)* | `pacman -Rn nginx` |
| Nicht mehr benötigte Abhängigkeiten entfernen | `apt autoremove` | `dnf autoremove` | `pacman -Rns $(pacman -Qdtq)` |
| Suchen | `apt search nginx` | `dnf search nginx` | `pacman -Ss nginx` |
| Details anzeigen | `apt show nginx` | `dnf info nginx` | `pacman -Si nginx` |
| Zu welchem Paket gehört eine Datei? | `dpkg -S /usr/sbin/nginx` | `rpm -qf /usr/sbin/nginx` | `pacman -Qo /usr/sbin/nginx` |
| Installierte Pakete auflisten | `apt list --installed` | `dnf list --installed` | `pacman -Q` |
| Den Download-Cache leeren | `apt clean` | `dnf clean all` | `pacman -Sc` |

Alle ändernden Befehle brauchen `sudo`.

## Abhängigkeiten

Die meisten Pakete brauchen andere Pakete: `htop` zum Beispiel braucht die Bibliothek
`libncursesw6`. Der Paketmanager installiert sie automatisch mit und markiert sie als
**automatisch installiert**. Braucht sie nichts mehr, entfernt `apt autoremove` oder
`dnf autoremove` sie wieder.

Pakete, die du selbst installiert hast, sind als **manuell installiert** markiert. Sie
werden nie automatisch entfernt.

## Woher Updates kommen

| Distribution | Sicherheitsupdates |
|--------------|--------------------|
| Debian | Eigene Paketquelle `trixie-security` |
| Ubuntu | Paketquelle `noble-security` (oder der Codename deiner Version) |
| RHEL | Errata in den normalen Paketquellen `BaseOS` und `AppStream` |
| Arch | Neue Paketversionen in den normalen Paketquellen |

!!! tip "Die Paketquellen der Distribution nutzen"
    Pakete aus den offiziellen Paketquellen bekommen automatisch Sicherheitsupdates.
    Software, die du von Hand von einer Webseite oder aus einer fremden Paketquelle
    installierst, musst du selbst aktuell halten.

!!! warning "Niemals Versionen mischen"
    Trag keine Paketquellen einer anderen Version oder Distribution ein, etwa
    Ubuntu-Pakete unter Debian. Das Ergebnis ist oft ein System, das sich nicht mehr
    sauber aktualisieren lässt.
