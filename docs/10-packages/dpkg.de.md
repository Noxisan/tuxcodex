# dpkg

> Das Paketwerkzeug der unteren Ebene von Debian und Ubuntu: listet installierte Pakete auf, zeigt, welche Dateien zu welchem Paket gehören, und installiert einzelne `.deb`-Dateien.

![dpkg output](../assets/screenshots/10-packages/dpkg.png)

## Syntax

```bash
dpkg [OPTION]... AKTION [PAKET | DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-l [MUSTER]` | Installierte Pakete mit ihrem Zustand auflisten |
| `-L PAKET` | Die Dateien eines installierten Pakets auflisten |
| `-S PFAD` | Das Paket finden, zu dem eine Datei gehört |
| `-s PAKET` | Zustand und Details eines Pakets anzeigen |
| `-i DATEI.deb` | Eine Paketdatei installieren |
| `-I DATEI.deb` | Die Details einer Paketdatei anzeigen, ohne sie zu installieren |
| `--configure -a` | Pakete nach einer abgebrochenen Installation fertig konfigurieren |

## Beispiele

**Installierte Pakete zu einem Muster anzeigen:**

```bash
dpkg -l "nginx*"
```

```text
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name               Version           Architecture Description
+++-==================-=================-============-=========================================================
ii  nginx              1.26.3-3+deb13u10 amd64        small, powerful, scalable web/proxy server
un  nginx-abi-1.26.3-1 <none>            <none>       (no description available)
ii  nginx-common       1.26.3-3+deb13u10 all          small, powerful, scalable web/proxy server - common files
un  nginx-core         <none>            <none>       (no description available)
```

| Code | Bedeutung |
|------|-----------|
| `ii` | Installiert und funktionsfähig |
| `rc` | Entfernt, aber die Konfigurationsdateien sind noch da |
| `un` | Nicht installiert, nur dem Namen nach bekannt |
| `iF`, `iU` | Installation wurde abgebrochen, `sudo dpkg --configure -a` ausführen |

**Herausfinden, zu welchem Paket eine Datei gehört:**

```bash
dpkg -S /usr/sbin/nginx /etc/nginx/nginx.conf
```

```text
nginx: /usr/sbin/nginx
nginx-common: /etc/nginx/nginx.conf
```

**Die Dateien eines Pakets auflisten:**

```bash
dpkg -L htop | head -n 8
```

```text
/.
/usr
/usr/bin
/usr/bin/htop
/usr/share
/usr/share/applications
/usr/share/applications/htop.desktop
/usr/share/doc
```

**Prüfen, ob ein Paket installiert ist:**

```bash
dpkg -s nginx | head -n 3
```

```text
Package: nginx
Status: install ok installed
Priority: optional
```

**Eine heruntergeladene Paketdatei installieren:**

```bash
sudo dpkg -i htop_3.4.1-5_amd64.deb
```

```text
Selecting previously unselected package htop.
(Reading database ... 12414 files and directories currently installed.)
Preparing to unpack htop_3.4.1-5_amd64.deb ...
Unpacking htop (3.4.1-5) ...
dpkg: dependency problems prevent configuration of htop:
 htop depends on libncursesw6 (>= 6); however:
  Package libncursesw6 is not installed.

dpkg: error processing package htop (--install):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 htop
```

`dpkg` holt keine Abhängigkeiten. `sudo apt install -f` installiert die fehlenden und
schließt die Installation ab.

## Wann brauche ich das?

- Um herauszufinden, aus welchem Paket eine Konfigurationsdatei oder ein Programm stammt
- Um zu prüfen, welche Version eines Pakets genau installiert ist
- Nach einem abgebrochenen Update, um es mit `dpkg --configure -a` abzuschließen
- Um Pakete im Zustand `rc` zu finden, deren Konfigurationsdateien noch herumliegen

!!! tip "`.deb`-Dateien mit `apt` installieren"
    `sudo apt install ./htop_3.4.1-5_amd64.deb` installiert eine Paketdatei und holt
    ihre Abhängigkeiten in einem Schritt aus den Paketquellen. Das `./` ist wichtig,
    sonst sucht `apt` in den Paketquellen nach einem Paket mit diesem Namen.

!!! tip "Übrig gebliebene Konfigurationsdateien entfernen"
    `dpkg -l | grep '^rc'` listet entfernte Pakete auf, deren Konfigurationsdateien noch
    existieren. `sudo apt purge PAKET` entfernt sie.

!!! warning "`.deb`-Dateien aus dem Internet"
    Eine `.deb`-Datei führt bei der Installation Skripte als root aus und bekommt keine
    Sicherheitsupdates aus deinen Paketquellen. Installiere nur Dateien aus Quellen, denen
    du vertraust.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paketwerkzeug der unteren Ebene | `dpkg` | `dpkg` | `rpm` | `pacman` |
| Zu welchem Paket gehört eine Datei? | `dpkg -S` | `dpkg -S` | `rpm -qf` | `pacman -Qo` |

## Verwandte Befehle

[apt](apt.md) · [apt-cache](apt-cache.md)
