# Logs lesen

| Aufgabe | Befehl |
|---------|--------|
| Ein Log live verfolgen, während du testest | `tail -f /var/log/nginx/error.log` |
| Die letzten 50 Zeilen anzeigen | `tail -n 50 /var/log/nginx/error.log` |
| Ein großes Log durchblättern und durchsuchen | `less /var/log/nginx/access.log`, dann `/` zum Suchen |
| Ein rotiertes, komprimiertes Log lesen | `zless /var/log/nginx/access.log.2.gz` |
| Die neuesten Zeilen zuerst anzeigen | `tac /var/log/nginx/access.log | less` |

!!! tip "Logs von systemd-Diensten"
    Auf Distributionen mit systemd schreiben viele Dienste keine eigenen Logdateien,
    sondern ins systemd-Journal. Diese liest du mit `journalctl`, das im Kapitel über
    Logs ausführlich behandelt wird.
