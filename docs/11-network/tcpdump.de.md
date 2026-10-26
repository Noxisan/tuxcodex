# tcpdump

> Zeichnet Netzwerkpakete auf einer Schnittstelle auf und zeigt sie Zeile für Zeile. Das letzte Mittel, wenn du genau wissen musst, was über die Leitung geht.

![tcpdump output](../assets/screenshots/11-network/tcpdump.png)

## Syntax

```bash
tcpdump [OPTION]... [FILTER]
```

Filter am Ende des Befehls begrenzen, was aufgezeichnet wird, zum Beispiel `port 443`, `host 198.51.100.23`, `tcp`, `icmp`, verknüpft mit `and`, `or` und `not`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-i GERÄT` | Schnittstelle, auf der gelauscht wird, `any` für alle |
| `-n` | Namen und Ports nicht auflösen, Zahlen zeigen |
| `-c ANZAHL` | Nach `ANZAHL` Paketen aufhören |
| `-w DATEI` | Die Pakete in eine Datei (`.pcap`) für Wireshark schreiben |
| `-r DATEI` | Pakete aus einer Datei lesen |
| `-v`, `-vv` | Mehr Details pro Paket |
| `-A` | Den Inhalt als Text zeigen, z. B. bei HTTP |

## Beispiele

**Zusehen, wie eine Verbindung zum Webserver aufgebaut wird:**

```bash
sudo tcpdump -n -i ens18 -c 3 port 443
```

```text
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on ens18, link-type EN10MB (Ethernet), snapshot length 262144 bytes
10:42:17.512304 IP 198.51.100.23.51744 > 192.0.2.10.443: Flags [S], seq 3104558611, win 64240, options [mss 1460,sackOK,TS val 1915203 ecr 0,nop,wscale 7], length 0
10:42:17.512351 IP 192.0.2.10.443 > 198.51.100.23.51744: Flags [S.], seq 2771046020, ack 3104558612, win 65160, options [mss 1460,sackOK,TS val 3324187 ecr 1915203,nop,wscale 7], length 0
10:42:17.524117 IP 198.51.100.23.51744 > 192.0.2.10.443: Flags [.], ack 1, win 502, options [nop,nop,TS val 1915215 ecr 3324187], length 0
3 packets captured
3 packets received by filter
0 packets dropped by kernel
```

| Flag | Bedeutung |
|------|-----------|
| `[S]` | SYN: Der Client will sich verbinden |
| `[S.]` | SYN-ACK: Der Server nimmt an |
| `[.]` | ACK: Die Verbindung steht |
| `[P.]`, `[F.]`, `[R]` | Daten, Verbindungsende, Abbruch |

**DNS-Anfragen beobachten:**

```bash
sudo tcpdump -n -i ens18 -c 2 port 53
```

```text
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on ens18, link-type EN10MB (Ethernet), snapshot length 262144 bytes
10:42:17.204118 IP 192.0.2.10.41322 > 192.0.2.53.53: 51234+ A? example.com. (29)
10:42:17.216502 IP 192.0.2.53.53 > 192.0.2.10.41322: 51234 1/0/0 A 198.51.100.7 (45)
2 packets captured
2 packets received by filter
0 packets dropped by kernel
```

Der Server fragt `192.0.2.53` nach der Adresse von `example.com` und bekommt eine Antwort.

**Herausfinden, ob Verbindungen blockiert werden:**

```bash
sudo tcpdump -n -i ens18 -c 3 port 5432
```

```text
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on ens18, link-type EN10MB (Ethernet), snapshot length 262144 bytes
10:42:17.512304 IP 198.51.100.23.51750 > 192.0.2.10.5432: Flags [S], seq 1840221573, win 64240, options [mss 1460,sackOK,TS val 1915511 ecr 0,nop,wscale 7], length 0
10:42:18.536219 IP 198.51.100.23.51750 > 192.0.2.10.5432: Flags [S], seq 1840221573, win 64240, options [mss 1460,sackOK,TS val 1916535 ecr 0,nop,wscale 7], length 0
10:42:20.584207 IP 198.51.100.23.51750 > 192.0.2.10.5432: Flags [S], seq 1840221573, win 64240, options [mss 1460,sackOK,TS val 1918583 ecr 0,nop,wscale 7], length 0
3 packets captured
3 packets received by filter
0 packets dropped by kernel
```

Der Client schickt SYN um SYN, aber der Server antwortet nie: Eine Firewall verwirft die
Pakete, oder es lauscht nichts. Lauscht nichts, würde der Server mit `[R.]` antworten.

**In eine Datei für Wireshark aufzeichnen:**

```bash
sudo tcpdump -n -i ens18 -w capture.pcap host 198.51.100.23 and not port 22
```

```text
tcpdump: listening on ens18, link-type EN10MB (Ethernet), snapshot length 262144 bytes
^C1284 packets captured
1291 packets received by filter
0 packets dropped by kernel
```

Beende die Aufzeichnung mit ++ctrl+c++. Kopiere `capture.pcap` auf deinen Rechner und öffne
sie in Wireshark für eine genaue Analyse.

## Wann brauche ich das?

- Wenn `ping`, `nc` und `curl` nicht erklären, warum eine Verbindung scheitert
- Um nachzuweisen, ob Pakete überhaupt am Server ankommen oder vorher verloren gehen
- Um DNS-, Mail- oder andere Protokollprobleme im Detail zu untersuchen

!!! tip "Die eigene SSH-Sitzung ausschließen"
    Über SSH zeichnet `tcpdump` auch seine eigene Ausgabe auf, die über SSH läuft, was eine
    Flut erzeugt. Ergänze den Filter um `and not port 22`.

!!! warning "Aufzeichnungen enthalten sensible Daten"
    Unverschlüsselter Verkehr wie HTTP, Mail oder Datenbankverbindungen ist in der
    Aufzeichnung vollständig lesbar, samt Passwörtern. Schütze `.pcap`-Dateien und lösche
    sie nach der Analyse.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorinstalliert | nein, Paket `tcpdump` | ja | nein, Paket `tcpdump` | nein, Paket `tcpdump` |

## Verwandte Befehle

[ss](ss.md) · [nc](nc.md) · [nft](nft.md) · [ping](ping.md)
