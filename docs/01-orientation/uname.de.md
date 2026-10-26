# uname

> Zeigt Informationen über den laufenden Kernel und die Hardware-Architektur an.

## Syntax

```bash
uname [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-a`, `--all` | Alle Informationen ausgeben |
| `-s`, `--kernel-name` | Kernelnamen ausgeben (Standard ohne Optionen) |
| `-n`, `--nodename` | Hostnamen ausgeben |
| `-r`, `--kernel-release` | Kernel-Release ausgeben |
| `-v`, `--kernel-version` | Build-Version und -Datum des Kernels ausgeben |
| `-m`, `--machine` | Hardware-Architektur ausgeben |
| `-o`, `--operating-system` | Betriebssystem ausgeben |

## Beispiele

**Alle Informationen anzeigen:**

```bash
uname -a
```

```text
Linux tuxcodex-srv 6.12.48+deb13-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.12.48-1 (2025-09-20) x86_64 GNU/Linux
```

**Das Release des laufenden Kernels anzeigen:**

```bash
uname -r
```

```text
6.12.48+deb13-amd64
```

**Die Architektur anzeigen:**

```bash
uname -m
```

```text
x86_64
```

**Optionen kombinieren:**

```bash
uname -srm
```

```text
Linux 6.12.48+deb13-amd64 x86_64
```

**Prüfen, ob nach einem Kernel-Update ein Neustart nötig ist:**

```bash
uname -r
ls /boot/vmlinuz-*
```

```text
6.12.43+deb13-amd64
/boot/vmlinuz-6.12.43+deb13-amd64
/boot/vmlinuz-6.12.48+deb13-amd64
```

Der neueste installierte Kernel (`6.12.48`) läuft noch nicht – der Server braucht einen Neustart.

<!-- SCREENSHOT: assets/screenshots/01-orientation/uname.png -->

## Wann brauche ich das?

- Nach einem Kernel-Update: Zeigt `uname -r` noch die alte Version, wurde der Server
  noch nicht neu gestartet
- Um den richtigen Download zu wählen (`x86_64` oder `aarch64`), etwa für ein Binary
  oder ein Docker-Image
- Um passende Kernel-Header oder -Module zu installieren (DKMS, VirtualBox, WireGuard
  auf älteren Systemen)
- Für Bug-Reports und Hilfeanfragen – die Kernel-Version ist meist die erste Frage

!!! tip "Version der Distribution"
    `uname` kennt nur den Kernel, nicht die Distribution. Die Debian-Version bekommst du
    mit `cat /etc/os-release` oder [`hostnamectl`](hostnamectl.md).

!!! tip "Gut zu wissen"
    `-p` (Prozessor) und `-i` (Hardware-Plattform) liefern unter Linux meist nur
    `unknown`. Für die Architektur nimm stattdessen `-m`.

## Verwandte Befehle

[hostnamectl](hostnamectl.md) · [hostname](hostname.md)
