# localectl

> Zeigt und setzt die Systemsprache (Locale) und das Tastaturlayout.

![localectl output](../assets/screenshots/09-systemd/localectl.png)

## Syntax

```bash
localectl [OPTION]... [BEFEHL] [ARGUMENT]...
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| *(keiner)*, `status` | Locale und Tastatureinstellungen anzeigen |
| `list-locales` | Die installierten Locales auflisten |
| `set-locale LANG=…` | Die System-Locale setzen |
| `list-keymaps` | Die Tastaturlayouts für die Konsole auflisten |
| `set-keymap LAYOUT` | Das Tastaturlayout der Konsole setzen |
| `set-x11-keymap LAYOUT` | Das Tastaturlayout für grafische Sitzungen setzen |

## Beispiele

**Die aktuellen Einstellungen anzeigen:**

```bash
localectl
```

```text
System Locale: LANG=en_US.UTF-8
    VC Keymap: (unset)
   X11 Layout: de
    X11 Model: pc105
```

`VC Keymap` ist das Layout an der Serverkonsole, `X11 Layout` das für grafische
Sitzungen. Über SSH gilt das Tastaturlayout deines eigenen Rechners.

**Die installierten Locales anzeigen:**

```bash
localectl list-locales
```

```text
C.UTF-8
de_DE.UTF-8
en_US.UTF-8
```

**Die Systemsprache ändern:**

```bash
sudo localectl set-locale LANG=de_DE.UTF-8
localectl status
```

```text
System Locale: LANG=de_DE.UTF-8
    VC Keymap: (unset)
   X11 Layout: de
    X11 Model: pc105
```

Die neue Einstellung gilt für neue Anmeldungen. Melde dich ab und wieder an, um sie zu
sehen.

## Wann brauche ich das?

- Nach der Installation, wenn der Server die falsche Sprache oder das falsche
  Tastaturlayout nutzt
- Wenn Programme Fragezeichen statt Umlauten zeigen, oft fehlt dann eine UTF-8-Locale
- Wenn ein Programm `Setting locale failed` meldet

!!! tip "Englisch auf Servern"
    Viele Admins lassen Server auf `en_US.UTF-8` oder `C.UTF-8`. Fehlermeldungen sind
    dann englisch, und du findest online viel mehr Hilfe dazu.

!!! warning "Die Locale zuerst installieren"
    `set-locale` setzt nur den Wert. Ist die Locale nicht installiert, fallen Programme
    auf `C` zurück und beschweren sich. Prüfe vorher mit `list-locales`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Eine Locale installieren | `sudo dpkg-reconfigure locales` | `sudo locale-gen de_DE.UTF-8` | `sudo dnf install glibc-langpack-de` | in `/etc/locale.gen` einkommentieren, dann `sudo locale-gen` |

## Verwandte Befehle

[hostnamectl](../01-orientation/hostnamectl.md) · [timedatectl](../01-orientation/timedatectl.md)
