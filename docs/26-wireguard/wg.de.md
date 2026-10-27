# wg

> Erzeugt WireGuard-Schlüssel, zeigt den Zustand der Tunnel und ändert Peers im laufenden Betrieb.

![wg output](../assets/screenshots/26-wireguard/wg.png)

## Syntax

```bash
wg genkey | pubkey | genpsk
wg show [INTERFACE] [FELD]
wg set INTERFACE peer SCHLÜSSEL [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `genkey` | Einen neuen privaten Schlüssel ausgeben |
| `pubkey` | Einen privaten Schlüssel von der Eingabe lesen und seinen öffentlichen ausgeben |
| `genpsk` | Einen zusätzlichen Pre-Shared Key für einen Peer erzeugen |
| `show`, (keine) | Zustand aller Interfaces: Peers, Endpoints, Handshakes, Verkehr |
| `show wg0 latest-handshakes` | Einzelne Felder für Skripte; auch `transfer`, `endpoints`, `allowed-ips` |
| `set wg0 peer SCHLÜSSEL allowed-ips IP` | Einen Peer im laufenden Betrieb hinzufügen oder ändern |
| `set wg0 peer SCHLÜSSEL remove` | Einen Peer entfernen |
| `showconf wg0` | Die laufende Konfiguration im Dateiformat |

`wg show` braucht root, weil es auch den privaten Schlüssel lesen kann.

## Beispiele

**Der Zustand des Tunnels:**

```bash
sudo wg show
```

```text
interface: wg0
  public key: uYnlIayVbIBV2lDo84nK2O2R61sblMRycaxu8Y1W1kk=
  private key: (hidden)
  listening port: 51820

peer: HO2gBkM55TRjnkSr2Nwia5/L/gvPMnYjEGn/tR1B3mo=
  endpoint: 203.0.113.45:51701
  allowed ips: 10.8.0.2/32
  latest handshake: 2 seconds ago
  transfer: 564 B received, 476 B sent
```

`endpoint` ist die öffentliche Adresse, von der der Laptop gerade verbindet; sie ändert sich, wenn der Laptop das Netz wechselt, und WireGuard folgt ihr automatisch.

**Ein Schlüsselpaar erzeugen:**

```bash
cd /etc/wireguard
umask 077
wg genkey | tee server.key | wg pubkey > server.pub
cat server.pub
```

```text
uYnlIayVbIBV2lDo84nK2O2R61sblMRycaxu8Y1W1kk=
```

`umask 077` sorgt dafür, dass `server.key` nur für root lesbar ist. Weitergegeben wird nur der öffentliche Schlüssel aus `server.pub`.

**Die Seite des Clients:**

```bash
sudo wg
```

```text
interface: wg0
  public key: HO2gBkM55TRjnkSr2Nwia5/L/gvPMnYjEGn/tR1B3mo=
  private key: (hidden)
  listening port: 51701

peer: uYnlIayVbIBV2lDo84nK2O2R61sblMRycaxu8Y1W1kk=
  endpoint: 198.51.100.7:51820
  allowed ips: 10.8.0.0/24
  latest handshake: 2 seconds ago
  transfer: 476 B received, 564 B sent
  persistent keepalive: every 25 seconds
```

**Einen neuen Client im laufenden Betrieb hinzufügen:**

```bash
sudo wg set wg0 peer BkDTavLKk/pQ56N0h4A2mTMxhNgXm03Daqqp6jjg4QQ= allowed-ips 10.8.0.3/32
sudo wg show wg0 allowed-ips
```

```text
HO2gBkM55TRjnkSr2Nwia5/L/gvPMnYjEGn/tR1B3mo=  10.8.0.2/32
BkDTavLKk/pQ56N0h4A2mTMxhNgXm03Daqqp6jjg4QQ=  10.8.0.3/32
```

**Der letzte Handshake je Peer, für das Monitoring:**

```bash
sudo wg show wg0 latest-handshakes
```

```text
HO2gBkM55TRjnkSr2Nwia5/L/gvPMnYjEGn/tR1B3mo=  1793106175
BkDTavLKk/pQ56N0h4A2mTMxhNgXm03Daqqp6jjg4QQ=  0
```

Der Wert ist ein Unix-Zeitstempel; `0` heißt, der Peer hat sich noch nie verbunden.

## Wann brauche ich das?

- Um das Schlüsselpaar für einen neuen Server oder Client zu erzeugen
- Um zu prüfen, ob ein Peer verbunden ist: Ein frischer `latest handshake` heißt ja
- Um einen neuen Client hinzuzufügen, ohne den Tunnel neu zu starten

!!! tip "Handshake älter als 2 Minuten?"
    WireGuard erneuert den Handshake alle 2 Minuten, solange Verkehr fließt. Ist `latest
    handshake` viel älter oder fehlt, prüfe den Endpoint, den UDP-Port in der Firewall und die
    öffentlichen Schlüssel auf beiden Seiten.

!!! warning "wg set wird nicht gespeichert"
    Änderungen mit `wg set` sind weg, wenn das Interface neu startet. Trag den Peer auch in
    `/etc/wireguard/wg0.conf` ein oder speichere den laufenden Zustand mit
    `wg-quick save wg0`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install wireguard-tools` | `sudo apt install wireguard-tools` | `sudo dnf install wireguard-tools` | `sudo pacman -S wireguard-tools` |

## Verwandte Befehle

[wg-quick](wg-quick.md) · [ip](../11-network/ip.md) · [ufw](../11-network/ufw.md) · [ping](../11-network/ping.md)
