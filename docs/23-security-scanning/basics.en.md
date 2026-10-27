# Understanding security scanning

Every service a server offers is a door. Security scanning means looking at your own
servers the way an attacker would, and from the inside the way an auditor would: Which
doors are open? Are they locked properly? Has someone already been inside?

## Allowed, and only on your own systems

!!! danger "Only scan what you are allowed to scan"
    Scanning other people's systems without permission is illegal in many countries,
    including Germany (§ 202c StGB) and under the UK Computer Misuse Act, and providers
    often block or report it. Only scan your own servers, or systems for which you have
    written permission. Inform your hosting provider before larger scans.

## Outside and inside

| View | Question | Tools |
|------|----------|-------|
| **From outside** | Which ports and services can be reached from the network, and which versions run there? | [`nmap`](nmap.md), [`nikto`](nikto.md) |
| **Hardening** | How well is the system configured? | [`lynis`](lynis.md) |
| **Intrusion** | Are there signs of a rootkit or malware? | [`rkhunter`](rkhunter.md), [`chkrootkit`](chkrootkit.md), [`clamscan`](clamscan.md) |
| **Integrity** | Were system files changed since installation or since the last check? | [`aide`](aide.md), [`debsums`](debsums.md) |
| **Containers** | Do images contain packages with known vulnerabilities? | [`trivy`](trivy.md) |

From the inside, [`ss -tlnp`](../11-network/ss.md) shows which services listen on which
port. Compare it with the `nmap` scan from outside: whatever appears there, but isn't needed
from the outside, belongs behind the firewall, see [`ufw`](../11-network/ufw.md).

## What you need to install

| Tool | Debian | Ubuntu | RHEL | Arch |
|------|--------|--------|------|------|
| nmap | `sudo apt install nmap` | `sudo apt install nmap` | `sudo dnf install nmap` | `sudo pacman -S nmap` |
| nikto | `sudo apt install nikto` (repository part `non-free`) | `sudo apt install nikto` (multiverse) | from GitHub (`sullo/nikto`) | `sudo pacman -S nikto` |
| lynis | `sudo apt install lynis` | `sudo apt install lynis` | `sudo dnf install lynis` (EPEL) | `sudo pacman -S lynis` |
| rkhunter | `sudo apt install rkhunter` | `sudo apt install rkhunter` | `sudo dnf install rkhunter` (EPEL) | `sudo pacman -S rkhunter` |
| chkrootkit | `sudo apt install chkrootkit` | `sudo apt install chkrootkit` | from source (chkrootkit.org) | AUR |
| ClamAV | `sudo apt install clamav` | `sudo apt install clamav` | `sudo dnf install clamav clamav-update` (EPEL) | `sudo pacman -S clamav` |
| AIDE | `sudo apt install aide` | `sudo apt install aide` | `sudo dnf install aide` | AUR |
| Package check | `debsums` | `debsums` | `rpm -Va` (built in) | `pacman -Qkk` (built in) |
| Trivy | repository of Aqua Security | repository of Aqua Security | repository of Aqua Security | `sudo pacman -S trivy` |

## A routine for your own server

| When | What |
|------|------|
| After setting up a server | `nmap` from outside, `lynis audit system`, create the `aide` database |
| Every night (cron or timer) | `rkhunter --check --cronjob`, `aide --check`, `clamscan` on upload directories |
| After every package update | `rkhunter --propupd`, `aide --update` (otherwise every update looks like an attack) |
| Before every deployment | `trivy image` in the CI pipeline |
| Every few months | `nmap` and `lynis` again, compare with the last results |

!!! tip "Scanners find hints, not proof"
    Most findings of `rkhunter`, `chkrootkit` or `lynis` are harmless on closer inspection:
    a changed file after an update, a hidden file from a package. Check every warning, but
    don't panic. A real intrusion usually shows up in several places at once.

!!! warning "A compromised system lies"
    A rootkit can hide itself from tools running on the same system. If you seriously
    suspect an intrusion, check the disk from a rescue system or another machine, and set
    the server up again from scratch instead of cleaning it.
