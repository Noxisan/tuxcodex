# age

> Ein einfaches, modernes Werkzeug zum Verschlüsseln von Dateien, mit kurzen Schlüsseln und ohne Konfiguration.

![age output](../assets/screenshots/24-certificates/age.png)

## Syntax

```bash
age -r EMPFÄNGER [-o AUSGABE] DATEI
age -d -i SCHLÜSSELDATEI [-o AUSGABE] DATEI
age-keygen [-o SCHLÜSSELDATEI]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `age-keygen -o DATEI` | Ein Schlüsselpaar erstellen; die Datei enthält den geheimen Schlüssel, der öffentliche wird ausgegeben |
| `-r EMPFÄNGER` | Für diesen öffentlichen Schlüssel verschlüsseln (`age1…`); mehrere `-r` sind möglich |
| `-R DATEI` | Empfänger aus einer Datei, auch öffentliche SSH-Schlüssel (`~/.ssh/id_ed25519.pub`) |
| `-p`, `--passphrase` | Mit einer Passphrase statt mit Schlüsseln verschlüsseln |
| `-d -i SCHLÜSSELDATEI` | Mit einem geheimen Schlüssel entschlüsseln, auch einem privaten SSH-Schlüssel |
| `-o DATEI` | Ausgabedatei |
| `-a`, `--armor` | Textausgabe statt binär, für Mails und YAML |

## Beispiele

**Ein Schlüsselpaar erstellen:**

```bash
age-keygen -o key.txt
cat key.txt
```

```text
Public key: age1gwfwheqcuxa7fddp82afhw366tkv86aakll4jqdgrp6jplns7y0qrc6lq9
# created: 2026-10-26T10:42:17+01:00
# public key: age1gwfwheqcuxa7fddp82afhw366tkv86aakll4jqdgrp6jplns7y0qrc6lq9
AGE-SECRET-KEY-1X82M8DY497K82KRUZRUSTRZHDFAG4AQMZ9CHF8D3M8H6UPDTGLESPD0VQE
```

**Ein Backup für den öffentlichen Schlüssel verschlüsseln:**

```bash
age -r age1gwfwheqcuxa7fddp82afhw366tkv86aakll4jqdgrp6jplns7y0qrc6lq9 \
  -o backup-2026-10-26.tar.gz.age backup-2026-10-26.tar.gz
ls -l backup-2026-10-26.tar.gz.age
```

```text
-rw-r--r-- 1 nox nox 7892 Oct 26 10:42 backup-2026-10-26.tar.gz.age
```

Dafür reicht der öffentliche Schlüssel, die geheime `key.txt` muss also nicht auf dem Server liegen.

**Mit der Schlüsseldatei entschlüsseln:**

```bash
age -d -i key.txt -o backup.tar.gz backup-2026-10-26.tar.gz.age
ls -l backup.tar.gz
```

```text
-rw-r--r-- 1 nox nox 7692 Oct 26 10:43 backup.tar.gz
```

**Mit einer Passphrase verschlüsseln:**

```bash
age -p -o secrets.txt.age secrets.txt
```

```text
Enter passphrase (leave empty to autogenerate a secure one):
Confirm passphrase:
```

## Wann brauche ich das?

- Für Backups, die auf dem Server verschlüsselt und nur woanders entschlüsselt werden
- Für Geheimnisse in Skripten und Repositorys, etwa zusammen mit `sops`
- Wenn gpg zu kompliziert ist und du nur Dateien verschlüsseln willst

!!! tip "Vorhandene SSH-Schlüssel nutzen"
    age kann direkt für öffentliche SSH-Schlüssel verschlüsseln: `age -R ~/.ssh/authorized_keys`
    verschlüsselt für alle, die sich anmelden dürfen, und sie entschlüsseln mit
    `age -d -i ~/.ssh/id_ed25519`.

!!! danger "Die Schlüsseldatei ist der einzige Weg zurück"
    Es gibt keine Passwort-Wiederherstellung. Bewahre `key.txt` außerhalb des Servers auf,
    etwa in deinem Passwortmanager, bevor du das erste Backup damit verschlüsselst.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install age` | `sudo apt install age` | `sudo dnf install age` (EPEL) | `sudo pacman -S age` |

## Verwandte Befehle

[gpg](gpg.md) · [ssh-keygen](../12-ssh/ssh-keygen.md) · [tar](../14-archives/tar.md) · [ansible-vault](../21-ansible/ansible-vault.md)
