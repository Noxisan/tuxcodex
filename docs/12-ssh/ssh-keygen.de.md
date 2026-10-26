# ssh-keygen

> Erzeugt und verwaltet SSH-Schlüssel: neue Schlüsselpaare, Passphrasen, Fingerprints und Einträge in `known_hosts`.

![ssh-keygen output](../assets/screenshots/12-ssh/ssh-keygen.png)

## Syntax

```bash
ssh-keygen [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-t TYP` | Schlüsseltyp, empfohlen ist `ed25519` |
| `-C KOMMENTAR` | Kommentar am Ende des öffentlichen Schlüssels, meist `benutzer@host` |
| `-f DATEI` | Dateiname des Schlüssels |
| `-l -f DATEI` | Den Fingerprint eines Schlüssels zeigen |
| `-p -f DATEI` | Die Passphrase ändern |
| `-y -f DATEI` | Den öffentlichen Schlüssel zu einem privaten ausgeben |
| `-R HOST` | Einen Host aus `known_hosts` entfernen |

## Beispiele

**Ein neues Schlüsselpaar erzeugen:**

```bash
ssh-keygen -t ed25519 -C "nox@tuxcodex-srv"
```

```text
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/nox/.ssh/id_ed25519):
Created directory '/home/nox/.ssh'.
Enter passphrase for "/home/nox/.ssh/id_ed25519" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/nox/.ssh/id_ed25519
Your public key has been saved in /home/nox/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:MH9iiNBiK1fYLz4X57tGWkD2uYd7TpgABke1SUynK1k nox@tuxcodex-srv
The key's randomart image is:
+--[ED25519 256]--+
|  ..o++ .        |
|   * .+=         |
|  = *oE. .       |
| . * *.*o        |
|. o = *.So.      |
| o . o *==.      |
|    o .++o.      |
|     o. oo.      |
|       .o+.      |
+----[SHA256]-----+
```

Drücke ++enter++ für den Standard-Dateinamen und gib zweimal eine Passphrase ein. Die
Eingabe wird nicht angezeigt.

**Die erzeugten Dateien prüfen:**

```bash
ls -l ~/.ssh
```

```text
total 8
-rw------- 1 nox nox 464 Oct 26 10:42 id_ed25519
-rw-r--r-- 1 nox nox  98 Oct 26 10:42 id_ed25519.pub
```

Der private Schlüssel darf nur für dich lesbar sein (`600`). Den öffentlichen darf jeder
sehen.

**Den öffentlichen Schlüssel anzeigen, um ihn einem Admin zu schicken:**

```bash
cat ~/.ssh/id_ed25519.pub
```

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAWZDtTcIe235G0EzeAQj/BESDJnWT39gRghXyiMZZal nox@tuxcodex-srv
```

**Den Fingerprint eines Schlüssels anzeigen:**

```bash
ssh-keygen -lf ~/.ssh/id_ed25519.pub
```

```text
256 SHA256:MH9iiNBiK1fYLz4X57tGWkD2uYd7TpgABke1SUynK1k nox@tuxcodex-srv (ED25519)
```

**Die Passphrase ändern:**

```bash
ssh-keygen -p -f ~/.ssh/id_ed25519
```

```text
Enter old passphrase:
Key has comment 'nox@tuxcodex-srv'
Enter new passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved with the new passphrase.
```

**Einen alten Host-Key nach der Neuinstallation eines Servers entfernen:**

```bash
ssh-keygen -R 192.0.2.10
```

```text
# Host 192.0.2.10 found: line 3
/home/nox/.ssh/known_hosts updated.
Original contents retained as /home/nox/.ssh/known_hosts.old
```

## Wann brauche ich das?

- Einmal pro Rechner, um dein eigenes Schlüsselpaar zu erzeugen
- Um die Passphrase eines vorhandenen Schlüssels zu ändern oder hinzuzufügen
- Wenn ein Server neu installiert wurde und SSH einen geänderten Host-Key meldet

!!! tip "Ein Schlüssel pro Rechner"
    Erzeuge auf jedem Rechner, von dem aus du arbeitest, einen eigenen Schlüssel. Geht ein
    Laptop verloren, entfernst du nur seinen öffentlichen Schlüssel von den Servern, die
    anderen funktionieren weiter.

!!! danger "Schlüssel ohne Passphrase"
    Ein privater Schlüssel ohne Passphrase ist wie ein Passwort in einer Textdatei: Wer
    ihn kopiert, kommt auf alle deine Server. Nutze Schlüssel ohne Passphrase nur für
    automatische Jobs und schränke sie auf dem Server ein.

## Verwandte Befehle

[ssh](ssh.md) · [ssh-copy-id](ssh-copy-id.md) · [ssh-agent](ssh-agent.md) · [ssh-add](ssh-add.md) · [ssh-keyscan](ssh-keyscan.md)
