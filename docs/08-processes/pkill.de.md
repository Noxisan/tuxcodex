# pkill

> Sendet allen Prozessen, deren Name zu einem Muster passt, ein Signal. Wie `kill`, nur ohne vorher die PID nachzuschlagen.

![pkill output](../assets/screenshots/08-processes/pkill.png)

## Syntax

```bash
pkill [-SIGNAL] [OPTION]... MUSTER
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-SIGNAL` | Zu sendendes Signal, Standard ist `TERM` |
| `-e` | Jeden Prozess ausgeben, der ein Signal bekommen hat |
| `-f` | Das Muster mit der ganzen Kommandozeile vergleichen |
| `-x` | Der Name muss exakt passen |
| `-o`, `-n` | Nur den ältesten oder neuesten passenden Prozess |
| `-u BENUTZER` | Nur Prozesse dieses Benutzers |
| `-t TERMINAL` | Nur Prozesse auf diesem Terminal, z. B. `pts/1` |

## Beispiele

**Alle Prozesse eines Skripts beenden und anzeigen, was passiert ist:**

```bash
pkill -e backup.sh
```

```text
backup.sh killed (pid 4410)
```

**Die ganze Kommandozeile durchsuchen:**

```bash
pkill -e -f "rsync .*/mnt/backup"
```

```text
rsync killed (pid 4415)
```

Der Prozessname ist nur `rsync`. Mit `-f` werden auch die Argumente durchsucht.

**Alle Prozesse eines Benutzers beenden:**

```bash
sudo pkill -e -u alice
```

```text
sshd-session killed (pid 3118)
bash killed (pid 3120)
```

Auch die SSH-Sitzung von `alice` wird dabei geschlossen.

**Einen Dienst seine Konfiguration neu laden lassen:**

```bash
sudo pkill -e -HUP -o -x nginx
```

```text
nginx killed (pid 812)
```

`-o` wählt den ältesten passenden Prozess, hier den nginx-Master. `killed` heißt nur, dass
das Signal gesendet wurde: Bei `HUP` läuft nginx weiter und lädt seine Konfiguration neu.

**Nichts gefunden:**

```bash
pkill keinsolcherprozess; echo $?
```

```text
1
```

Exit-Code `1` bedeutet: Kein Prozess hat gepasst.

## Wann brauche ich das?

- Um alle Prozesse eines Programms auf einmal zu beenden, z. B. hängende Worker
- Um alle Prozesse eines Benutzers zu beenden, dessen Konto du gesperrt hast
- In Skripten, um einen Hilfsprozess über seinen Namen zu beenden

!!! tip "Erst mit `pgrep` testen"
    `pkill` versteht dieselben Optionen wie [`pgrep`](pgrep.md). Führe zuerst `pgrep -a`
    mit demselben Muster aus und prüfe die Liste. Erst dann ersetzt du `pgrep -a` durch
    `pkill`.

!!! warning "`-f` findet auch deine eigene Shell"
    Mit `-f` wird das Muster auch in Kommandozeilen gefunden, die es nur als Text
    enthalten, etwa ein `bash -c "…"` oder ein `ssh`-Aufruf mit diesem Befehl. Ohne
    Kontrolle beendest du Prozesse, die du nicht gemeint hast.

!!! danger "Kurze Muster als root"
    `pkill` vergleicht Teile von Namen: `sudo pkill ss` beendet auch `sshd`, und deine
    Verbindung ist weg. Nimm `-x` für exakte Namen.

## Verwandte Befehle

[pgrep](pgrep.md) · [kill](kill.md) · [ps](ps.md) · [killall](killall.md)
