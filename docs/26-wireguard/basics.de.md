# WireGuard verstehen

WireGuard ist ein VPN, das direkt im Linux-Kernel steckt. Es ist klein, schnell und hat sehr
wenig zu konfigurieren: Jeder Rechner hat ein Schlüsselpaar, und jeder Verbindungspartner
(**Peer**) ist über seinen öffentlichen Schlüssel bekannt. Es gibt keine Zertifikate, keine
Benutzernamen und keine Handshake-Optionen, die man falsch setzen kann.

## Wie es zusammenhängt

```text
   laptop                                  tuxdex-srv
   10.8.0.2                                10.8.0.1
   wg0 ◄──── encrypted UDP, port 51820 ────► wg0
              over the internet             vpn.example.com (198.51.100.7)
```

| Begriff | Bedeutung |
|---------|-----------|
| **Interface** | Die VPN-Netzwerkkarte, meist `wg0`, mit einer Adresse im Tunnelnetz wie `10.8.0.1/24` |
| **Privater Schlüssel** | Geheimer Schlüssel dieses Rechners, bleibt auf ihm |
| **Öffentlicher Schlüssel** | Wird aus dem privaten abgeleitet und bei den anderen Peers eingetragen |
| **Peer** | Ein Verbindungspartner, erkannt an seinem öffentlichen Schlüssel |
| **AllowedIPs** | Welche Tunneladressen zu einem Peer gehören; beim Client auch, welche Netze durch den Tunnel gehen |
| **Endpoint** | Öffentliche Adresse und Port eines Peers, mindestens eine Seite braucht sie |

## Was du installieren musst

WireGuard selbst gehört seit Version 5.6 zum Linux-Kernel. Du brauchst nur die Werkzeuge:

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install wireguard-tools` | `sudo apt install wireguard-tools` | `sudo dnf install wireguard-tools` | `sudo pacman -S wireguard-tools` |
| Kernelmodul | enthalten | enthalten | enthalten | enthalten |
| Firewall für den Port | `ufw allow 51820/udp` | `ufw allow 51820/udp` | `firewall-cmd --add-port=51820/udp --permanent` | je nach Einrichtung |

Clients gibt es auch für Windows, macOS, Android und iOS; sie lesen dasselbe
Konfigurationsformat.

## Server: /etc/wireguard/wg0.conf

```text
[Interface]
Address = 10.8.0.1/24
ListenPort = 51820
PrivateKey = <private key of tuxdex-srv>

[Peer]
# laptop of nox
PublicKey = HO2gBkM55TRjnkSr2Nwia5/L/gvPMnYjEGn/tR1B3mo=
AllowedIPs = 10.8.0.2/32
```

## Client: /etc/wireguard/wg0.conf auf dem Laptop

```text
[Interface]
Address = 10.8.0.2/24
PrivateKey = <private key of the laptop>

[Peer]
# tuxdex-srv
PublicKey = uYnlIayVbIBV2lDo84nK2O2R61sblMRycaxu8Y1W1kk=
Endpoint = vpn.example.com:51820
AllowedIPs = 10.8.0.0/24
PersistentKeepalive = 25
```

`AllowedIPs = 10.8.0.0/24` schickt nur das Tunnelnetz durch das VPN. Mit
`0.0.0.0/0, ::/0` ginge der gesamte Verkehr des Laptops über den Server; dann braucht der
Server IP-Forwarding und NAT.

## Einrichtung Schritt für Schritt

| Schritt | Befehl |
|---------|--------|
| 1. Schlüssel auf jedem Rechner | `wg genkey \| tee private.key \| wg pubkey > public.key`, siehe [`wg`](wg.md) |
| 2. Konfigurationen schreiben | wie oben, mit dem öffentlichen Schlüssel der Gegenseite |
| 3. Den Port auf dem Server öffnen | `sudo ufw allow 51820/udp` |
| 4. Starten und aktivieren | `sudo systemctl enable --now wg-quick@wg0`, siehe [`wg-quick`](wg-quick.md) |
| 5. Prüfen | `sudo wg show`: Ein `latest handshake` heißt, der Tunnel funktioniert |

## Admin-Dienste nur über das VPN

Der nützlichste Einsatz eines VPN auf Servern: SSH, Monitoring und Admin-Oberflächen
lauschen nur auf der Tunneladresse oder sind nur aus dem Tunnelnetz erlaubt:

```text
$ sudo ufw allow in on wg0 to any port 22 proto tcp
$ sudo ufw delete allow 22/tcp
```

Dann ist SSH aus dem Internet gar nicht mehr erreichbar, nur noch über das VPN.

!!! tip "Einen Weg zurück offenhalten"
    Bevor du SSH zum Internet schließt, teste den VPN-Zugang in einer zweiten Sitzung und
    halte die Konsole deines Hosters bereit. Ein Tippfehler in der Firewall sperrt dich
    sonst aus.

!!! danger "Private Schlüssel bleiben auf ihrem Rechner"
    Kopiere einen privaten Schlüssel nie auf einen anderen Rechner, in ein Ticket oder ein
    Repository. Jeder Peer erzeugt sein eigenes Schlüsselpaar; ausgetauscht werden nur
    öffentliche Schlüssel. Die Konfigurationsdateien brauchen die Rechte `600`.
