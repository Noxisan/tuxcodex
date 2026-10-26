# w

> Zeigt, wer angemeldet ist und was gerade passiert – dazu Laufzeit und Systemlast.

## Syntax

```bash
w [OPTION]... [BENUTZER]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-h`, `--no-header` | Kopfzeile (Uhrzeit, Laufzeit, Last) weglassen |
| `-s`, `--short` | Kurzformat ohne Anmeldezeit, JCPU und PCPU |
| `-f`, `--from` | Spalte `FROM` (entfernter Host) ein- oder ausblenden |
| `-i`, `--ip-addr` | In `FROM` IP-Adressen statt Hostnamen zeigen |
| `-p`, `--pids` | PID des Prozesses in `WHAT` anzeigen |
| `-o`, `--old-style` | Altes Ausgabeformat: Leerlaufzeit unter einer Minute bleibt leer |
| `BENUTZER` | Nur die Sitzungen dieses Benutzers anzeigen |

## Beispiele

**Alle Sitzungen anzeigen:**

```bash
w
```

```text
 10:42:17 up 12 days,  3:05,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
nox      pts/0    192.0.2.10       09:12    0.00s  0.06s  0.00s w
nox      pts/1    198.51.100.23    10:30    5:12   0.03s  0.03s -bash
```

Die erste Zeile entspricht der Ausgabe von [`uptime`](uptime.md). Darunter folgt eine
Zeile pro Sitzung:

| Spalte | Bedeutung |
|--------|-----------|
| `USER` | Angemeldeter Benutzer |
| `TTY` | Terminal der Sitzung |
| `FROM` | Entfernte Adresse der Anmeldung |
| `LOGIN@` | Anmeldezeit |
| `IDLE` | Zeit seit der letzten Eingabe |
| `JCPU` | CPU-Zeit aller Prozesse an diesem Terminal |
| `PCPU` | CPU-Zeit des aktuellen Prozesses (`WHAT`) |
| `WHAT` | Gerade laufender Befehl |

**Nur die Sitzungsliste ohne Kopfzeile anzeigen:**

```bash
w -h
```

```text
nox      pts/0    192.0.2.10       09:12    0.00s  0.06s  0.00s w -h
nox      pts/1    198.51.100.23    10:30    5:12   0.03s  0.03s -bash
```

**Kurzformat:**

```bash
w -s
```

```text
 10:42:17 up 12 days,  3:05,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM              IDLE WHAT
nox      pts/0    192.0.2.10        0.00s w -s
nox      pts/1    198.51.100.23     5:12  -bash
```

**Nur die Sitzungen eines Benutzers anzeigen:**

```bash
w nox
```

```text
 10:42:17 up 12 days,  3:05,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
nox      pts/0    192.0.2.10       09:12    0.00s  0.06s  0.00s w nox
nox      pts/1    198.51.100.23    10:30    5:12   0.03s  0.03s -bash
```

<!-- SCREENSHOT: assets/screenshots/01-orientation/w.png -->

## Wann brauche ich das?

- Vor einem Neustart: Arbeitet noch jemand – oder ist eine Sitzung seit Stunden untätig?
- Um zu sehen, was andere Admins gerade tun, etwa ob jemand parallel zu dir ein
  `apt upgrade` laufen lässt
- Um vergessene Sitzungen mit langer `IDLE`-Zeit zu finden
- Als schneller Überblick nach der Anmeldung: Laufzeit, Last und aktive Benutzer in
  einem Befehl

!!! tip "`w` oder `who`?"
    [`who`](who.md) zeigt nur, **wer** angemeldet ist. `w` zeigt zusätzlich, **was** die
    Sitzungen gerade tun und wie lange sie schon untätig sind – plus Laufzeit und Last.

!!! warning "Vor dem Neustart nachsehen"
    Eine Sitzung, in der gerade `apt`, `dpkg` oder eine Datenbankmigration läuft, darf
    ein Neustart nicht unterbrechen. Wirf vorher einen Blick in die Spalte `WHAT`.

## Verwandte Befehle

[who](who.md) · [uptime](uptime.md)
