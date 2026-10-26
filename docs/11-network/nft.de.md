# nft

> Das Kommandozeilenwerkzeug von nftables, dem Paketfilter im Linux-Kernel. Alle Firewalls wie `ufw` und `firewalld` bauen darauf auf; mit `nft` siehst und schreibst du die Regeln direkt.

![nft output](../assets/screenshots/11-network/nft.png)

## Syntax

```bash
nft [OPTION]... BEFEHL
```

Unter Debian liegen die Regeln in `/etc/nftables.conf` und werden beim Booten vom Dienst `nftables` geladen.

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `list ruleset` | Alle Tabellen, Ketten und Regeln anzeigen |
| `-a list chain FAMILIE TABELLE KETTE` | Eine Kette mit Regel-Handles anzeigen |
| `-c -f DATEI` | Eine Regeldatei nur auf Fehler prüfen |
| `-f DATEI` | Eine Regeldatei laden |
| `add rule ...` | Eine Regel am Ende einer Kette anhängen |
| `insert rule ... position HANDLE` | Eine Regel vor der Regel mit diesem Handle einfügen |
| `delete rule ... handle HANDLE` | Eine Regel löschen |
| `flush ruleset` | Alle Regeln löschen: Alles ist wieder erlaubt |

## Beispiele

**Alle Regeln anzeigen:**

```bash
sudo nft list ruleset
```

```text
table inet filter {
        chain input {
                type filter hook input priority filter; policy drop;
                ct state established,related accept
                iif "lo" accept
                meta l4proto { icmp, ipv6-icmp } accept
                tcp dport 22 accept
                tcp dport { 80, 443 } accept
                ip saddr 192.0.2.0/24 tcp dport 5432 accept
                counter packets 18342 bytes 1102644 drop
        }

        chain forward {
                type filter hook forward priority filter; policy drop;
        }

        chain output {
                type filter hook output priority filter; policy accept;
        }
}
```

| Teil | Bedeutung |
|------|-----------|
| `policy drop` | Alles, was keine Regel annimmt, wird verworfen |
| `ct state established,related accept` | Antworten auf eigene Verbindungen sind erlaubt |
| `counter ... drop` | Zählt und verwirft den Rest: hier 18342 blockierte Pakete |

**Die Regeln mit ihren Handles anzeigen:**

```bash
sudo nft -a list chain inet filter input
```

```text
table inet filter {
        chain input { # handle 1
                type filter hook input priority filter; policy drop;
                ct state established,related accept # handle 4
                iif "lo" accept # handle 5
                meta l4proto { icmp, ipv6-icmp } accept # handle 7
                tcp dport 22 accept # handle 8
                tcp dport { 80, 443 } accept # handle 10
                ip saddr 192.0.2.0/24 tcp dport 5432 accept # handle 11
                counter packets 18342 bytes 1102644 drop # handle 12
        }
}
```

**Einen weiteren Port vor dem abschließenden `drop` erlauben:**

```bash
sudo nft insert rule inet filter input position 12 tcp dport 8080 accept
sudo nft -a list chain inet filter input | tail -n 5
```

```text
                ip saddr 192.0.2.0/24 tcp dport 5432 accept # handle 11
                tcp dport 8080 accept # handle 13
                counter packets 18342 bytes 1102644 drop # handle 12
        }
}
```

`add` würde die Regel hinter `drop` anhängen, wo sie nie erreicht wird. `insert ...
position 12` setzt sie vor die Regel mit Handle 12.

**Die Regeldatei vor dem Laden prüfen:**

```bash
sudo nft -c -f /etc/nftables.conf
```

```text
/etc/nftables.conf:9:21-25: Error: syntax error, unexpected string
        tcp dport 22 acept
                     ^^^^^
```

Solange die Datei Fehler hat, wird nichts geladen, und die laufenden Regeln bleiben
erhalten.

**Die Regeln dauerhaft laden:**

```bash
sudo systemctl enable --now nftables
```

```text
Created symlink '/etc/systemd/system/sysinit.target.wants/nftables.service' → '/usr/lib/systemd/system/nftables.service'.
```

`systemctl enable --now` lädt `/etc/nftables.conf` jetzt und bei jedem Booten.

## Wann brauche ich das?

- Um zu sehen, was wirklich im Kernel steht, egal welches Firewall-Werkzeug die Regeln
  angelegt hat
- Um unter Debian eine schlanke Firewall ohne zusätzliches Werkzeug zu schreiben
- Um mit Zählern pro Regel herauszufinden, warum Pakete blockiert werden

!!! tip "`inet`-Tabellen nutzen"
    Eine Tabelle der Familie `inet` gilt für IPv4 und IPv6 gleichzeitig. Du brauchst
    keine getrennten Regeln für beide.

!!! danger "`policy drop` ohne SSH-Regel"
    Lädst du einen Regelsatz mit `policy drop` in der Input-Kette, ohne SSH zu erlauben,
    bricht deine Verbindung sofort ab. Achte darauf, dass `tcp dport 22 accept` und
    `ct state established,related accept` in der Datei stehen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorinstalliert | ja, Dienst deaktiviert | Paket `nftables`, üblich ist `ufw` als Oberfläche | ja, genutzt von `firewalld` | Paket `nftables` |
| Regeldatei | `/etc/nftables.conf` | `/etc/nftables.conf` | von `firewalld` verwaltet | `/etc/nftables.conf` |

## Verwandte Befehle

[ufw](ufw.md) · [ss](ss.md)
