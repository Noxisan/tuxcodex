# ausearch

> Durchsucht das Audit-Log des Linux-Audit-Systems: Anmeldungen, Änderungen an überwachten Dateien, Nutzung von `sudo` und andere sicherheitsrelevante Ereignisse.

![ausearch output](../assets/screenshots/15-logs/ausearch.png)

## Syntax

```bash
ausearch [OPTION]...
```

Das Audit-System schreibt Ereignisse nach `/var/log/audit/audit.log`. Mit `auditctl -w DATEI -p wa -k SCHLÜSSEL` legst du eine Regel an, die eine Datei überwacht.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-m TYP` | Ereignistyp, z. B. `USER_LOGIN`, `USER_CMD`, `AVC` |
| `-k SCHLÜSSEL` | Ereignisse einer Audit-Regel mit diesem Schlüssel |
| `--success no` | Nur fehlgeschlagene Ereignisse |
| `-ts`, `-te` | Start- und Endzeit, z. B. `-ts today` oder `-ts 10:00` |
| `-ua BENUTZER` | Ereignisse eines Benutzers, auch nach `sudo` |
| `-i` | Zahlen in Namen übersetzen (Benutzer, Systemaufrufe) |

## Beispiele

**Die fehlgeschlagenen Anmeldungen von heute finden:**

```bash
sudo ausearch -m USER_LOGIN --success no -ts today -i
```

```text
----
type=USER_LOGIN msg=audit(10/26/2026 10:31:05.412:2841) : pid=3301 uid=root auid=unset ses=unset subj=system_u:system_r:sshd_t:s0-s0:c0.c1023 msg='op=login acct=admin exe=/usr/sbin/sshd-session hostname=? addr=198.51.100.66 terminal=ssh res=failed'
----
type=USER_LOGIN msg=audit(10/26/2026 10:31:09.118:2843) : pid=3301 uid=root auid=unset ses=unset subj=system_u:system_r:sshd_t:s0-s0:c0.c1023 msg='op=login acct=admin exe=/usr/sbin/sshd-session hostname=? addr=198.51.100.66 terminal=ssh res=failed'
```

**`/etc/passwd` auf Änderungen überwachen:**

```bash
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
sudo auditctl -l
```

```text
-w /etc/passwd -p wa -k passwd_changes
```

**Herausfinden, wer die Datei geändert hat:**

```bash
sudo ausearch -k passwd_changes -i
```

```text
----
type=PROCTITLE msg=audit(10/26/2026 10:42:17.123:2907) : proctitle=useradd -m bob
type=SYSCALL msg=audit(10/26/2026 10:42:17.123:2907) : arch=x86_64 syscall=openat success=yes exit=5 items=1 ppid=2201 pid=4610 auid=nox uid=root gid=root tty=pts0 ses=4 comm=useradd exe=/usr/sbin/useradd key=passwd_changes
```

`auid=nox` hat um 10:42:17 mit `sudo` `useradd -m bob` ausgeführt.

## Wann brauche ich das?

- Nach einem Sicherheitsvorfall: Wer hat wann welche Datei geändert?
- Um Zugriffe auf sensible Dateien nachzuweisen, etwa für Compliance
- Unter RHEL, um herauszufinden, warum SELinux etwas blockiert hat (`-m AVC`)

!!! tip "`auid` ist der echte Benutzer"
    `uid=root` zeigt nur, dass ein Befehl als root lief. `auid` (Audit-Benutzer) ist der Benutzer,
    der sich ursprünglich angemeldet hat, er bleibt auch nach `sudo` und `su` gleich.

!!! warning "Regeln gehen beim Neustart verloren"
    Mit `auditctl` angelegte Regeln sind vorübergehend. Schreib dauerhafte Regeln in eine Datei in
    `/etc/audit/rules.d/` und lade sie mit `augenrules --load`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| auditd installiert und aktiv | nein, Paket `auditd` | nein, Paket `auditd` | ja | nein, Paket `audit` |

## Verwandte Befehle

[aureport](aureport.md) · [journalctl](../09-systemd/journalctl.md) · [sudo](../07-users-groups/sudo.md)
