# Archive verstehen

Zwei verschiedene Dinge werden oft vermischt:

| Schritt | Was passiert | Werkzeuge |
|---------|--------------|-----------|
| **Archivieren** | Viele Dateien und Verzeichnisse werden zu einer Datei, mit Namen, Rechten und Datum | `tar`, `zip` |
| **Komprimieren** | Eine Datei wird kleiner | `gzip`, `bzip2`, `xz`, `zstd` |

Unter Linux kombiniert man meist beides: `tar` packt das Verzeichnis, ein Kompressor
verkleinert das Ergebnis. `zip` erledigt beides in einem Schritt und ist der Standard für
den Austausch mit Windows.

## Dateiendungen

| Endung | Inhalt | Entpacken mit |
|--------|--------|---------------|
| `.tar` | Archiv, nicht komprimiert | `tar -xf` |
| `.tar.gz`, `.tgz` | tar-Archiv, mit gzip komprimiert | `tar -xzf` |
| `.tar.bz2` | tar-Archiv, mit bzip2 komprimiert | `tar -xjf` |
| `.tar.xz` | tar-Archiv, mit xz komprimiert | `tar -xJf` |
| `.tar.zst` | tar-Archiv, mit zstd komprimiert | `tar --zstd -xf` |
| `.gz`, `.bz2`, `.xz`, `.zst` | Eine einzelne komprimierte Datei | `gunzip`, `bunzip2`, `unxz`, `unzstd` |
| `.zip` | Archiv und Kompression in einem | `unzip` |

Ein aktuelles GNU tar erkennt die Kompression beim Entpacken selbst: `tar -xf datei.tar.zst`
reicht.

## Die Verfahren im Vergleich

Beispielwerte für einen Datenbank-Dump mit 412 MiB auf dem Beispielserver, jeweils mit der
Standardstufe:

| Verfahren | Größe danach | Zeit zum Komprimieren | Zeit zum Entpacken | Einsatz |
|-----------|--------------|-----------------------|--------------------|---------|
| gzip | 77 MiB | 14 s | 3 s | Überall kompatibel, der Klassiker |
| bzip2 | 69 MiB | 38 s | 12 s | Kaum noch genutzt |
| xz | 49 MiB | 2 min 10 s | 4 s | Kleinste Dateien, langsam, für Downloads und Releases |
| zstd | 54 MiB | 2 s | 1 s | Schnell und klein, heute die beste Wahl für Backups |

Die Werte hängen stark von den Daten ab: Text und SQL-Dumps schrumpfen stark, Bilder, Videos
und bereits komprimierte Dateien kaum.

!!! tip "zstd für Backups"
    zstd komprimiert fast so gut wie xz, aber um ein Vielfaches schneller. Bei regelmäßigen
    Backups spart das CPU-Zeit und verkürzt das Backup-Fenster. Nimm gzip nur, wenn das
    Archiv auf alten Systemen geöffnet werden muss.

!!! warning "Komprimieren ersetzt kein Prüfen"
    Ein kaputtes Archiv fällt oft erst beim Zurückspielen auf. Teste Archive nach dem
    Erstellen (`tar -tf`, `unzip -t`) und bewahre eine Prüfsumme mit
    [`sha256sum`](sha256sum.md) auf.
