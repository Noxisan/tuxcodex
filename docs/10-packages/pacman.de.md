# pacman

> Der Paketmanager von Arch Linux: installiert, aktualisiert und entfernt Pakete und fragt sowohl die Paketquellen als auch die installierten Pakete ab, alles in einem Werkzeug.

![pacman output](../assets/screenshots/10-packages/pacman.png)

## Syntax

```bash
pacman OPERATION [OPTION]... [PAKET]...
```

Der erste Großbuchstabe wählt die Operation: `-S` arbeitet mit den Paketquellen (Sync),
`-Q` mit den installierten Paketen (Query), `-R` entfernt.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-Syu` | Paketlisten aktualisieren und alle Updates installieren |
| `-S PAKET` | Ein Paket installieren |
| `-Ss WORT` | Die Paketquellen durchsuchen |
| `-Si PAKET` | Details eines Pakets aus den Paketquellen anzeigen |
| `-Q` | Installierte Pakete auflisten (`-Qe`: nur ausdrücklich installierte) |
| `-Qi PAKET` | Details eines installierten Pakets anzeigen |
| `-Qo PFAD` | Das Paket finden, dem eine Datei gehört |
| `-Qdt` | Waisen auflisten: Abhängigkeiten, die nichts mehr braucht |
| `-R PAKET` | Ein Paket entfernen (`-Rns`: auch unnötige Abhängigkeiten und Konfiguration) |
| `-Sc` | Alte Paketdateien aus dem Cache entfernen |

## Beispiele

**Ein Paket installieren:**

```bash
sudo pacman -S htop
```

```text
resolving dependencies...
looking for conflicting packages...

Package (1)  New Version  Net Change  Download Size

extra/htop   3.5.3-1        0.41 MiB       0.18 MiB

Total Download Size:   0.18 MiB
Total Installed Size:  0.41 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
checking keyring...
checking package integrity...
loading package files...
checking for file conflicts...
:: Processing package changes...
installing htop...
Optional dependencies for htop
    lm_sensors: show cpu temperatures
    lsof: show files opened by a process
    strace: attach to a running process
```

**Das ganze System aktualisieren:**

```bash
sudo pacman -Syu
```

```text
:: Synchronizing package databases...
 core downloading...
 extra downloading...
:: Starting full system upgrade...
 there is nothing to do
```

**Die Paketquellen durchsuchen:**

```bash
pacman -Ss "^nginx$"
```

```text
extra/nginx 1.30.6-2 [installed]
    Lightweight HTTP server and IMAP/POP3 proxy server
```

**Herausfinden, zu welchem Paket eine Datei gehört:**

```bash
pacman -Qo /usr/bin/nginx
```

```text
/usr/bin/nginx is owned by nginx 1.30.6-2
```

**Verwaiste Abhängigkeiten finden und entfernen:**

```bash
pacman -Qdt
```

```text
mailcap 2.1.54-3
```

`mailcap` wurde als Abhängigkeit von nginx installiert. Nach dem Entfernen von nginx
braucht es nichts mehr. `sudo pacman -Rns $(pacman -Qdtq)` entfernt alle Waisen.

**Ein Paket entfernen:**

```bash
sudo pacman -R nginx
```

```text
checking dependencies...

Package (1)  Old Version  Net Change

nginx        1.30.6-2      -1.68 MiB

Total Removed Size:  1.68 MiB

:: Do you want to remove these packages? [Y/n] y
:: Processing package changes...
removing nginx...
```

## Wann brauche ich das?

- Unter Arch für jede Installation und jedes Update
- Um herauszufinden, zu welchem Paket eine Datei gehört oder welche Pakete verwaist sind
- Um das System bei einem Rolling Release sauber zu halten, wo sich Pakete oft ändern

!!! tip "Vor dem Update die News lesen"
    Arch braucht bei Updates manchmal Handarbeit. Das wird auf
    <https://archlinux.org/news/> angekündigt. Lies die News vor jedem `pacman -Syu` auf
    einem Server.

!!! warning "Keine Teil-Updates"
    Führe nie `pacman -Sy PAKET` aus: Es aktualisiert die Paketlisten, aber nur ein
    Paket. Das kann Bibliotheken kaputt machen. Nimm immer `pacman -Syu`, auch vor dem
    Installieren.

!!! warning "Dienste werden nicht gestartet"
    Unter Arch wird ein neuer Dienst nach der Installation weder aktiviert noch
    gestartet. Nimm `sudo systemctl enable --now nginx`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Verfügbar | nein, [`apt`](apt.md) nutzen | nein, [`apt`](apt.md) nutzen | nein, [`dnf`](dnf.md) nutzen | ja |
| Konfiguration der Paketquellen | entfällt | entfällt | entfällt | `/etc/pacman.conf`, Spiegelserver in `/etc/pacman.d/mirrorlist` |

## Verwandte Befehle

[apt](apt.md) · [dnf](dnf.md) · [systemctl](../09-systemd/systemctl.md)
