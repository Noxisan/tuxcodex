# firewall-cmd

> Das Kommandozeilenwerkzeug von firewalld, der Firewall von RHEL, Rocky Linux und AlmaLinux: öffnet Dienste und Ports in Zonen, vorübergehend oder dauerhaft.

![firewall-cmd output](../assets/screenshots/11-network/firewall-cmd.png)

## Syntax

```bash
firewall-cmd [OPTION]...
```

firewalld unterscheidet zwei Konfigurationen: Die **Laufzeit**-Konfiguration ist jetzt aktiv und beim nächsten Neuladen weg; die **permanente** Konfiguration ist gespeichert und wird beim Booten geladen.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--state` | Läuft firewalld? |
| `--list-all` | Alles in der Standardzone: Schnittstellen, Dienste, Ports, Regeln |
| `--add-service=NAME` | Einen vordefinierten Dienst wie `http` oder `ssh` erlauben |
| `--add-port=PORT/PROTO` | Einen Port erlauben |
| `--remove-service`, `--remove-port` | Wieder entfernen |
| `--add-rich-rule='…'` | Ausführliche Regel, z. B. nur aus einem bestimmten Netz |
| `--permanent` | Die gespeicherte statt der laufenden Konfiguration ändern |
| `--reload` | Die permanente Konfiguration laden |
| `--get-services` | Alle vordefinierten Dienste auflisten |

## Beispiele

**Die aktive Zone anzeigen und was sie erlaubt:**

```bash
sudo firewall-cmd --list-all
```

```text
public (default, active)
  target: default
  ingress-priority: 0
  egress-priority: 0
  icmp-block-inversion: no
  interfaces: ens18
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

Auf einem frischen RHEL-Server sind nur `ssh`, `cockpit` und `dhcpv6-client` erlaubt.

**HTTP und HTTPS dauerhaft öffnen:**

```bash
sudo firewall-cmd --permanent --add-service=http --add-service=https
sudo firewall-cmd --reload
```

```text
success
success
```

Jeder Befehl antwortet mit `success`. Ohne `--reload` wäre die dauerhafte Änderung noch
nicht aktiv.

**Einen Port zum Testen öffnen, nur bis zum nächsten Neuladen:**

```bash
sudo firewall-cmd --add-port=8080/tcp
```

```text
success
```

**Die Datenbank nur aus dem eigenen Netz erlauben:**

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.0.2.0/24" port port="5432" protocol="tcp" accept'
```

```text
success
```

**Das Ergebnis prüfen:**

```bash
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```

```text
success
public (default, active)
  target: default
  ingress-priority: 0
  egress-priority: 0
  icmp-block-inversion: no
  interfaces: ens18
  sources:
  services: cockpit dhcpv6-client http https ssh
  ports:
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
        rule family="ipv4" source address="192.0.2.0/24" port port="5432" protocol="tcp" accept
```

Port `8080/tcp` ist weg: Er stand nur in der Laufzeit-Konfiguration, und das Neuladen hat
ihn verworfen. Die Rich Rule bleibt, weil sie mit `--permanent` gespeichert wurde.

## Wann brauche ich das?

- Unter RHEL, Rocky und Alma nach der Installation eines Dienstes: Der Port ist
  standardmäßig zu
- Um einen Port nur aus bestimmten Netzen zu erlauben
- Wenn ein Dienst läuft, von außen aber nicht erreichbar ist

!!! tip "Erst testen, dann speichern"
    Füge eine Regel ohne `--permanent` hinzu und teste sie. Funktioniert alles, speichert
    `sudo firewall-cmd --runtime-to-permanent` die laufende Konfiguration.

!!! warning "Vergessenes `--permanent`"
    Regeln ohne `--permanent` sind nach einem Neuladen oder Neustart weg. Ist ein Port
    nach einem Neustart plötzlich wieder zu, ist das fast immer der Grund.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Firewall-Werkzeug | `ufw` oder `nft` | `ufw` | `firewall-cmd`, standardmäßig aktiv | `ufw`, `nft` oder `firewalld` |

## Verwandte Befehle

[ufw](ufw.md) · [nft](nft.md) · [ss](ss.md)
