# SELinux und AppArmor verstehen

Normale Linux-Rechte (Besitzer, Gruppe, `rwx`) sind **freiwillig**: Der Besitzer einer
Datei entscheidet. SELinux und AppArmor setzen **verpflichtende** Regeln obendrauf, die
selbst root nicht einfach übergehen kann. Wird nginx übernommen, kann es trotzdem nur
anfassen, was die Richtlinie für nginx erlaubt, nicht `/etc/shadow` und nicht deine
SSH-Schlüssel.

## Zwei Systeme, ein Ziel

| | SELinux | AppArmor |
|---|---------|----------|
| Prinzip | Jede Datei, jeder Prozess und Port hat ein **Label** (Kontext); die Richtlinie legt fest, welche Labels worauf zugreifen dürfen | Jedes Programm hat ein **Profil** mit den Pfaden, die es nutzen darf |
| Standardmäßig aktiv unter | RHEL, Rocky, Alma, Fedora | Debian, Ubuntu, SUSE |
| Stärke | Sehr feingranular, deckt das ganze System ab | Leichter zu lesen und zu schreiben |
| Typisches Problem | Dateien mit falschem Label, etwa nach `mv` | Ein Programm nutzt einen Pfad, der nicht in seinem Profil steht |

## Welche Distribution was nutzt

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Standardmäßig aktiv | AppArmor | AppArmor | SELinux (enforcing) | keins |
| Werkzeuge | `apparmor-utils` | `apparmor-utils` (vorinstalliert) | `policycoreutils` (vorinstalliert), `policycoreutils-python-utils` für `semanage` und `audit2allow` | AppArmor möglich: Paket `apparmor` plus Kernel-Parameter `lsm=` |
| Ablehnungen werden protokolliert in | `journalctl -k`, `/var/log/kern.log` | `journalctl -k`, `/var/log/kern.log` | `/var/log/audit/audit.log` | `journalctl -k` |

## SELinux in drei Begriffen

```text
system_u:object_r:httpd_sys_content_t:s0
   │         │            │            └─ level (MLS, rarely relevant)
   │         │            └─ type: this is what the rules are about
   │         └─ role
   └─ user
```

| Begriff | Beispiel | Bedeutung |
|---------|----------|-----------|
| **Typ** einer Datei | `httpd_sys_content_t` | Webinhalte, die der Webserver lesen darf |
| **Domäne** eines Prozesses | `httpd_t` | In dieser Domäne laufen nginx und Apache |
| **Boolean** | `httpd_can_network_connect` | Ein Schalter für eine häufige Ausnahme, etwa „Webserver darf sich mit anderen Servern verbinden“ |

`ls -Z` zeigt das Label von Dateien, `ps -eZ` das von Prozessen.

## Von der Ablehnung zur Lösung

```text
"Permission denied" in the service log, although chmod/chown are right
   │
   ├─ 1. Is it SELinux/AppArmor?    getenforce · aa-status · ausearch -m AVC
   ├─ 2. What exactly was denied?   ausearch -m AVC -ts recent · audit2why
   └─ 3. Fix it in this order:
          a) wrong file label   → semanage fcontext + restorecon
          b) unusual port       → semanage port
          c) known exception    → setsebool -P
          d) only if nothing fits → audit2allow -M (own policy module)
```

Der schnelle Test: `setenforce 0` (SELinux) oder `aa-complain` (AppArmor). Ist das Problem
weg, lag es an der Zugriffskontrolle. Schalte sie sofort wieder ein und behebe es richtig.

!!! tip "Erst die Ablehnung lesen, dann handeln"
    `audit2why` erklärt jede SELinux-Ablehnung in Klartext und nennt oft das Boolean, das
    sie behebt. Das ist meist eine Lösung in einer Zeile.

!!! danger "Nicht dauerhaft abschalten"
    `SELINUX=disabled` oder das Entfernen von AppArmor lässt den Fehler verschwinden und
    damit auch den Schutz, der den Schaden eines gehackten Dienstes begrenzt. Unter RHEL
    verlangt ein späteres Wiedereinschalten von SELinux, das ganze Dateisystem neu zu
    labeln.
