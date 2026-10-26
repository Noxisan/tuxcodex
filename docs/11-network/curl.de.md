# curl

> Schickt Anfragen an Webserver und APIs und zeigt die Antwort. Das Werkzeug, um Webseiten zu testen, Zertifikate zu prüfen und auf der Kommandozeile mit REST-APIs zu sprechen.

![curl output](../assets/screenshots/11-network/curl.png)

## Syntax

```bash
curl [OPTION]... URL
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-I` | Nur die Header holen (`HEAD`-Anfrage) |
| `-L` | Weiterleitungen folgen |
| `-o DATEI`, `-O` | In `DATEI` speichern oder unter dem Namen aus der URL |
| `-s`, `-S` | Still, aber `-S` zeigt Fehler trotzdem an |
| `-f` | Bei HTTP-Fehlern wie `404` mit Fehler abbrechen |
| `-v` | Ausführlich: Verbindung, TLS und alle Header |
| `-w FORMAT` | Nach der Anfrage Werte ausgeben, z. B. `%{http_code}` |
| `-X METHODE`, `-d DATEN` | Methode und Inhalt, z. B. für `POST`-Anfragen |
| `-H "Header: Wert"` | Einen zusätzlichen Header senden |
| `--resolve HOST:PORT:IP` | Für diesen Hostnamen eine bestimmte IP ansprechen |

## Beispiele

**Die Header einer Webseite anzeigen:**

```bash
curl -I https://example.com
```

```text
HTTP/2 200
server: nginx
date: Mon, 26 Oct 2026 09:42:17 GMT
content-type: text/html; charset=utf-8
content-length: 1256
last-modified: Mon, 12 Oct 2026 08:15:02 GMT
etag: "6a2b1f36-4e8"
accept-ranges: bytes
```

**Nur Statuscode und Antwortzeit:**

```bash
curl -sS -o /dev/null -w "%{http_code} %{time_total}s\n" https://example.com
```

```text
200 0.084215s
```

**Einer Weiterleitung von HTTP auf HTTPS folgen:**

```bash
curl -sIL http://example.com | grep -iE "^(HTTP|location)"
```

```text
HTTP/1.1 301 Moved Permanently
Location: https://example.com/
HTTP/2 200
```

**Prüfen, wann das TLS-Zertifikat abläuft:**

```bash
curl -svI https://example.com 2>&1 | grep -E "subject:|issuer:|expire date:"
```

```text
*  subject: CN=example.com
*  expire date: Dec 13 23:59:59 2026 GMT
*  issuer: C=US; O=Let's Encrypt; CN=R12
```

**Eine Webseite auf dem neuen Server testen, bevor der DNS umgestellt wird:**

```bash
curl -I --resolve example.com:443:192.0.2.10 https://example.com
```

```text
HTTP/2 200
server: nginx
date: Mon, 26 Oct 2026 09:42:17 GMT
content-type: text/html; charset=utf-8
content-length: 1256
last-modified: Mon, 12 Oct 2026 08:15:02 GMT
etag: "6a2b1f36-4e8"
accept-ranges: bytes
```

`curl` verbindet sich mit `192.0.2.10`, schickt aber `example.com` als Hostnamen und prüft
das Zertifikat dafür, genau wie ein Browser nach der DNS-Umstellung.

**Eine JSON-API aufrufen:**

```bash
curl -s -H "Accept: application/json" https://api.example.com/v1/status
```

```text
{"status":"ok","version":"2.4.1","uptime":1051200}
```

Für eine lesbare Ausgabe leitest du sie an [`jq`](../05-text-processing/jq.md) weiter.

**Wenn auf dem Port nichts lauscht:**

```bash
curl http://192.0.2.20:8080/
```

```text
curl: (7) Failed to connect to 192.0.2.20 port 8080 after 1 ms: Could not connect to server
```

## Wann brauche ich das?

- Um zu testen, ob eine Webseite oder API antwortet, und mit welchem Statuscode
- Um Weiterleitungen, Header und das TLS-Zertifikat einer Seite zu prüfen
- Um einen neuen Server unter dem echten Hostnamen zu testen, bevor der DNS umgestellt wird
- In Skripten und Healthchecks, etwa mit `-f` und dem Exit-Code

!!! tip "`-f` für Skripte"
    Ohne `-f` endet `curl` auch bei einer `500`-Fehlerseite mit `0`. Mit `-fsS` bricht es
    bei HTTP-Fehlern ab, bleibt bei Erfolg still und zeigt trotzdem die Fehlermeldung.

!!! warning "`-k` nie dauerhaft nutzen"
    `-k` (`--insecure`) ignoriert Zertifikatsfehler. Für einen schnellen Test ist das in
    Ordnung, in Skripten verdeckt es aber abgelaufene Zertifikate und
    Man-in-the-Middle-Angriffe.

## Verwandte Befehle

[wget](wget.md) · [nc](nc.md) · [dig](dig.md) · [jq](../05-text-processing/jq.md)
