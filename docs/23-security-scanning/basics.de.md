# Sicherheitsprüfung verstehen

Jeder Dienst, den ein Server anbietet, ist eine Tür. Sicherheitsprüfung heißt, die eigenen
Server so anzusehen, wie es ein Angreifer tun würde, und von innen so, wie es ein Prüfer
tun würde: Welche Türen sind offen? Sind sie richtig verschlossen? War schon jemand drin?

## Erlaubt, und nur auf eigenen Systemen

!!! danger "Scanne nur, was du scannen darfst"
    Fremde Systeme ohne Erlaubnis zu scannen, ist in vielen Ländern strafbar, in
    Deutschland etwa nach § 202c StGB, und Provider sperren oder melden es oft. Scanne nur
    deine eigenen Server oder Systeme, für die du eine schriftliche Erlaubnis hast. Gib
    deinem Hoster vor größeren Scans Bescheid.

## Von außen und von innen

| Blick | Frage | Werkzeuge |
|-------|-------|-----------|
| **Von außen** | Welche Ports und Dienste sind aus dem Netz erreichbar, und welche Versionen laufen dort? | [`nmap`](nmap.md), [`nikto`](nikto.md) |
| **Härtung** | Wie gut ist das System konfiguriert? | [`lynis`](lynis.md) |
| **Einbruch** | Gibt es Hinweise auf ein Rootkit oder Schadsoftware? | [`rkhunter`](rkhunter.md), [`chkrootkit`](chkrootkit.md), [`clamscan`](clamscan.md) |
| **Integrität** | Wurden Systemdateien seit der Installation oder der letzten Prüfung verändert? | [`aide`](aide.md), [`debsums`](debsums.md) |
| **Container** | Enthalten Images Pakete mit bekannten Schwachstellen? | [`trivy`](trivy.md) |

Von innen zeigt [`ss -tlnp`](../11-network/ss.md), welche Dienste auf welchem Port lauschen.
Vergleiche das mit dem `nmap`-Scan von außen: Was dort auftaucht, aber von außen nicht
gebraucht wird, gehört hinter die Firewall, siehe [`ufw`](../11-network/ufw.md).

## Was du installieren musst

| Werkzeug | Debian | Ubuntu | RHEL | Arch |
|----------|--------|--------|------|------|
| nmap | `sudo apt install nmap` | `sudo apt install nmap` | `sudo dnf install nmap` | `sudo pacman -S nmap` |
| nikto | `sudo apt install nikto` (Repository-Bereich `non-free`) | `sudo apt install nikto` (multiverse) | von GitHub (`sullo/nikto`) | `sudo pacman -S nikto` |
| lynis | `sudo apt install lynis` | `sudo apt install lynis` | `sudo dnf install lynis` (EPEL) | `sudo pacman -S lynis` |
| rkhunter | `sudo apt install rkhunter` | `sudo apt install rkhunter` | `sudo dnf install rkhunter` (EPEL) | `sudo pacman -S rkhunter` |
| chkrootkit | `sudo apt install chkrootkit` | `sudo apt install chkrootkit` | aus dem Quellcode (chkrootkit.org) | AUR |
| ClamAV | `sudo apt install clamav` | `sudo apt install clamav` | `sudo dnf install clamav clamav-update` (EPEL) | `sudo pacman -S clamav` |
| AIDE | `sudo apt install aide` | `sudo apt install aide` | `sudo dnf install aide` | AUR |
| Paketprüfung | `debsums` | `debsums` | `rpm -Va` (eingebaut) | `pacman -Qkk` (eingebaut) |
| Trivy | Repository von Aqua Security | Repository von Aqua Security | Repository von Aqua Security | `sudo pacman -S trivy` |

## Ein Ablauf für den eigenen Server

| Wann | Was |
|------|-----|
| Nach dem Einrichten eines Servers | `nmap` von außen, `lynis audit system`, die `aide`-Datenbank anlegen |
| Jede Nacht (Cron oder Timer) | `rkhunter --check --cronjob`, `aide --check`, `clamscan` auf Upload-Verzeichnissen |
| Nach jedem Paket-Update | `rkhunter --propupd`, `aide --update` (sonst sieht jedes Update wie ein Angriff aus) |
| Vor jedem Deployment | `trivy image` in der CI-Pipeline |
| Alle paar Monate | `nmap` und `lynis` erneut, mit den letzten Ergebnissen vergleichen |

!!! tip "Scanner liefern Hinweise, keine Beweise"
    Die meisten Funde von `rkhunter`, `chkrootkit` oder `lynis` sind bei näherem Hinsehen
    harmlos: eine geänderte Datei nach einem Update, eine versteckte Datei aus einem Paket.
    Prüf jede Warnung, aber keine Panik. Ein echter Einbruch zeigt sich meist an mehreren
    Stellen gleichzeitig.

!!! warning "Ein kompromittiertes System lügt"
    Ein Rootkit kann sich vor Werkzeugen verstecken, die auf demselben System laufen. Hast
    du ernsthaft einen Einbruch im Verdacht, prüfe die Platte von einem Rettungssystem oder
    einem anderen Rechner aus und setze den Server lieber neu auf, statt ihn zu reinigen.
