# chage

> Legt fest, wie lange Passwörter gültig sind und wann ein Konto abläuft, und zeigt diese Einstellungen an.

![chage output](../assets/screenshots/07-users-groups/chage.png)

## Syntax

```bash
chage [OPTION]... BENUTZER
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-l`, `--list` | Passwort- und Kontoablauf des Benutzers anzeigen |
| `-M TAGE`, `--maxdays` | Das Passwort muss nach `TAGE` Tagen geändert werden |
| `-m TAGE`, `--mindays` | Das Passwort darf frühestens nach `TAGE` Tagen wieder geändert werden |
| `-W TAGE`, `--warndays` | `TAGE` Tage vor Ablauf des Passworts warnen |
| `-E DATUM`, `--expiredate` | Das Konto läuft am `DATUM` ab (`JJJJ-MM-TT`, `-1` = nie) |
| `-I TAGE`, `--inactive` | Konto `TAGE` Tage nach Ablauf des Passworts sperren |
| `-d 0`, `--lastday 0` | Passwortwechsel bei der nächsten Anmeldung erzwingen |

## Beispiele

**Passwörter nach 90 Tagen ablaufen lassen, mit Warnung 14 Tage vorher:**

```bash
sudo chage -M 90 -W 14 alice
sudo chage -l alice
```

```text
Last password change                                    : Oct 26, 2026
Password expires                                        : Jan 24, 2027
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 90
Number of days of warning before password expires       : 14
```

**Ein Konto an einem festen Datum ablaufen lassen:**

```bash
sudo chage -E 2026-12-31 bob
sudo chage -l bob | grep 'Account expires'
```

```text
Account expires                                         : Dec 31, 2026
```

Ab dem 1. Januar kann sich `bob` nicht mehr anmelden, auch nicht mit SSH-Schlüssel.

**Bei der nächsten Anmeldung ein neues Passwort erzwingen:**

```bash
sudo chage -d 0 alice
sudo chage -l alice | head -n 3
```

```text
Last password change                                    : password must be changed
Password expires                                        : password must be changed
Password inactive                                       : password must be changed
```

**Das Ablaufdatum eines Kontos wieder entfernen:**

```bash
sudo chage -E -1 bob
sudo chage -l bob | grep 'Account expires'
```

```text
Account expires                                         : never
```

## Wann brauche ich das?

- Für befristete Konten von Freelancern, Praktikanten oder externem Support, die
  automatisch enden sollen
- Um eine Passwortrichtlinie mit regelmäßigem Wechsel umzusetzen
- Um herauszufinden, warum sich ein Benutzer plötzlich nicht mehr anmelden kann: Ein
  abgelaufenes Konto oder Passwort ist ein häufiger Grund

!!! tip "Das Ablaufdatum stoppt auch SSH-Schlüssel"
    Anders als `passwd -l` blockiert ein abgelaufenes Konto (`chage -E`) auch Anmeldungen
    mit SSH-Schlüssel. Damit ist es das richtige Werkzeug, um ein Konto zu einem festen
    Datum abzuschalten.

!!! warning "Standardwerte für neue Benutzer"
    `chage` ändert nur vorhandene Benutzer. Die Standardwerte für neue Benutzer
    (`PASS_MAX_DAYS`, `PASS_WARN_AGE`) stehen in `/etc/login.defs`.

## Verwandte Befehle

[passwd](passwd.md) · [usermod](usermod.md)
