# chkrootkit

> Prüft Systemprogramme und das System auf Anzeichen bekannter Rootkits; eine zweite Meinung neben rkhunter.

![chkrootkit output](../assets/screenshots/23-security-scanning/chkrootkit.png)

## Syntax

```bash
chkrootkit [OPTIONEN] [TEST...]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Alle Tests ausführen und jedes Ergebnis zeigen |
| `-q` | Leise: nur Funde zeigen |
| `-x` | Expertenmodus mit mehr Details |
| `-r VERZEICHNIS` | Ein eingehängtes System prüfen, etwa von einem Rettungssystem aus |
| `-l` | Die verfügbaren Tests auflisten |
| `TEST` | Nur diese Tests, etwa `sshd` oder `chkdirs` |

## Beispiele

**Alle Tests ausführen:**

```bash
sudo chkrootkit | head -12
```

```text
ROOTDIR is `/'
Checking `amd'...                                           not found
Checking `basename'...                                      not infected
Checking `biff'...                                          not found
Checking `chfn'...                                          not infected
Checking `chsh'...                                          not infected
Checking `cron'...                                          not infected
Checking `crontab'...                                       not infected
Checking `date'...                                          not infected
Checking `du'...                                            not infected
Checking `dirname'...                                       not infected
Checking `echo'...                                          not infected
```

**Nur Funde zeigen:**

```bash
sudo chkrootkit -q
```

```text
WARNING: The following suspicious files and directories were found:
/usr/lib/ruby/vendor_ruby/rubygems/ssl_certs/.document [From Debian package: ruby-rubygems]
/usr/lib/ruby/vendor_ruby/rubygems/vendor/net-http/.document [From Debian package: ruby-rubygems]
/usr/lib/ruby/vendor_ruby/rubygems/vendor/uri/.document [From Debian package: ruby-rubygems]
```

Dateien aus einem Debian-Paket, also harmlos. Ein echter Fund wäre eine versteckte Datei ohne Paket, etwa in `/dev` oder `/usr/lib`.

**Eine eingehängte Platte vom Rettungssystem aus prüfen:**

```bash
sudo mount /dev/sda2 /mnt
sudo chkrootkit -q -r /mnt
```

```text
ROOTDIR is `/mnt/'
```

## Wann brauche ich das?

- Als zweite Prüfung neben rkhunter, weil beide Unterschiedliches finden
- Um die Platte eines verdächtigen Servers mit `-r` von einem Rettungssystem aus zu prüfen
- Als nächtlicher Cronjob mit `-q`, damit nur bei Funden eine Mail kommt

!!! tip "Von außen prüfen mit -r"
    Starte ein Rettungssystem, häng die Platte des Servers unter `/mnt` ein und führe
    `chkrootkit -r /mnt` aus. Dann kann sich ein Rootkit auf dem Server nicht vor der Prüfung
    verstecken.

!!! warning "Funde lesen"
    Versteckte Dateien wie `.document` aus Debian-Paketen werden als verdächtig gemeldet,
    sind aber harmlos. chkrootkit nennt sogar das Paket, aus dem sie stammen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install chkrootkit` | `sudo apt install chkrootkit` | aus dem Quellcode (chkrootkit.org) | AUR |

## Verwandte Befehle

[rkhunter](rkhunter.md) · [clamscan](clamscan.md) · [aide](aide.md) · [mount](../13-disks-storage/mount.md)
