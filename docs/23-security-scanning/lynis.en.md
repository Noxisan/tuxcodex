# lynis

> Audits the security of a Linux system and gives a hardening index plus concrete suggestions.

![lynis output](../assets/screenshots/23-security-scanning/lynis.png)

## Syntax

```bash
lynis audit system [OPTIONS]
lynis show details TEST-ID
```

## Options

| Option | Description |
|--------|-------------|
| `audit system` | Check the whole system (as root for complete results) |
| `--quick`, `-Q` | Don't wait for a key press between sections |
| `--no-colors` | Plain output, for logs |
| `--tests-from-group GROUP` | Only one area, such as `ssh`, `firewalls` or `authentication` |
| `show details TEST-ID` | Details of a single test, such as `SSH-7408` |
| `show groups` | List the test groups |

Every run writes `/var/log/lynis.log` (details) and `/var/log/lynis-report.dat` (machine-readable results).

## Examples

**Audit the system:**

```bash
sudo lynis audit system --quick | tail -22
```

```text
================================================================================

  Lynis security scan details:

  Hardening index : 64 [############        ]
  Tests performed : 251
  Plugins enabled : 1

  Components:
  - Firewall               [V]
  - Malware scanner        [V]

  Scan mode:
  Normal [V]  Forensics [ ]  Integration [ ]  Pentest [ ]

  Lynis modules:
  - Compliance status      [?]
  - Security audit         [V]
  - Vulnerability scan     [V]

  Files:
  - Test and debug information      : /var/log/lynis.log
  - Report data                     : /var/log/lynis-report.dat
```

**The warnings and the first suggestions:**

```bash
sudo lynis audit system --quick | sed -n '/Warnings (/,/DEB-0831/p'
```

```text
  Warnings (1):
  ----------------------------
  ! No AIDE database was found, needed for AIDE functionality [FINT-4316]
      https://cisofy.com/lynis/controls/FINT-4316/

  Suggestions (38):
  ----------------------------
  * Install libpam-tmpdir to set $TMP and $TMPDIR for PAM sessions [DEB-0280]
    - Related resources
      * Website: https://cisofy.com/lynis/controls/DEB-0280/

  * Install apt-listbugs to display a list of critical bugs prior to each APT installation. [DEB-0810]
    - Related resources
      * Website: https://cisofy.com/lynis/controls/DEB-0810/

  * Install apt-listchanges to display any significant changes prior to any upgrade via APT. [DEB-0811]
    - Related resources
      * Website: https://cisofy.com/lynis/controls/DEB-0811/

  * Install needrestart, alternatively to debian-goodies, so that you can run needrestart after upgrades to determine which daemons are using old versions of libraries and need restarting. [DEB-0831]
```

**All suggestions in short form:**

```bash
sudo grep '^suggestion' /var/log/lynis-report.dat | cut -d'|' -f1,2 | head -5
```

```text
suggestion[]=DEB-0280|Install libpam-tmpdir to set $TMP and $TMPDIR for PAM sessions
suggestion[]=DEB-0810|Install apt-listbugs to display a list of critical bugs prior to each APT installation.
suggestion[]=DEB-0811|Install apt-listchanges to display any significant changes prior to any upgrade via APT.
suggestion[]=DEB-0831|Install needrestart, alternatively to debian-goodies, so that you can run needrestart after upgrades to determine which daemons are using old versions of libraries and need restarting.
suggestion[]=BOOT-5264|Consider hardening system services
```

## When do I need it?

- After setting up a server, as a checklist for hardening
- Regularly, to see whether the hardening index stays the same or drops
- Before an audit, to find and fix weak spots first

!!! tip "Track the hardening index"
    Note the index after every run. A drop after changes shows that something was opened
    or loosened. A value of 100 isn't the goal; every suggestion has to fit the server.

!!! warning "Don't apply blindly"
    Some suggestions don't fit every server, for example removing compilers on a build
    machine. Read the linked explanation and decide each one.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Install | `sudo apt install lynis` | `sudo apt install lynis` | `sudo dnf install lynis` (EPEL) | `sudo pacman -S lynis` |

## Related commands

[aide](aide.md) · [rkhunter](rkhunter.md) · [systemd-analyze](../09-systemd/systemd-analyze.md) · [needrestart](../10-packages/needrestart.md)
