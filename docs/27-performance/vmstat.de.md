# vmstat

> Zeigt in einer Zeile pro Intervall, wie ausgelastet CPU, Speicher, Swap und Platten sind; der schnellste Überblick, wenn ein Server langsam ist.

![vmstat output](../assets/screenshots/27-performance/vmstat.png)

## Syntax

```bash
vmstat [OPTIONEN] [INTERVALL [ANZAHL]]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `INTERVALL` | Alle N Sekunden eine neue Zeile ausgeben |
| `ANZAHL` | Nach N Zeilen aufhören |
| `-w` | Breite Ausgabe, die Spalten laufen nicht ineinander |
| `-S M` | Speicher in MB statt KB zeigen |
| `-s` | Speicher- und Ereigniszähler als Liste |
| `-d` | Statistik pro Platte |
| `-t` | Jeder Zeile einen Zeitstempel geben |

Die wichtigsten Spalten:

| Spalte | Bedeutung | Aufpassen, wenn |
|--------|-----------|-----------------|
| `r` | Prozesse, die auf eine CPU warten | dauerhaft höher als die Zahl der Kerne |
| `b` | Blockierte Prozesse, meist wartend auf Platten-I/O | länger nicht 0 |
| `si`, `so` | Pro Sekunde ein- und ausgelagert | nicht 0: Speicher wird knapp |
| `us`, `sy` | CPU-Zeit für Programme und Kernel | zusammen nahe 100 |
| `wa` | CPU wartet auf I/O | über etwa 10: Die Platte ist der Engpass |
| `st` | Vom Hypervisor gestohlene Zeit | auf einer VM nicht 0: Der Host ist überlastet |

## Beispiele

**Fünf Messungen, alle zwei Sekunden:**

```bash
vmstat -S M 2 5
```

```text
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 0  0      0    812     98   1798    0    0    14    38  112  201  3  1 96  0  0  0
 0  0      0    811     98   1798    0    0     0    24  148  263  2  1 97  0  0  0
 1  0      0    811     98   1798    0    0     0     6  139  241  2  0 98  0  0  0
 0  0      0    810     98   1798    0    0     0    40  162  287  3  1 96  0  0  0
 0  0      0    810     98   1798    0    0     0     0  127  230  1  0 99  0  0  0
```

Ein ruhiger Server: `id` (idle) nahe 100, keine Swap-Aktivität, keine wartenden Prozesse.

**Ein Server, der auf die Platte wartet:**

```bash
vmstat -S M 2 3
```

```text
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 1  3      0    205     98   2310    0    0  8420 21650 1890 2410  6  9 37 48  0  0
 0  4      0    198     98   2321    0    0  9104 23102 1977 2533  5 10 36 49  0  0
 1  3      0    201     98   2319    0    0  8833 22410 1920 2487  6  9 35 50  0  0
```

`b` liegt bei 3 bis 4 und `wa` um 50 %: Prozesse warten auf die Platte, während die CPU Zeit hat. Nächster Schritt: [`iostat -x`](iostat.md) und [`iotop`](iotop.md).

**Der Speicher ist knapp, und der Server lagert aus:**

```bash
vmstat -S M 2 3
```

```text
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 3  1    612     54      4    121  310  498  1310  1902 1488 1720 41 12 22 25  0  0
 2  2    640     49      4    118  352  514  1402  2011 1530 1798 39 14 21 26  0  0
 4  1    671     51      3    115  288  476  1250  1876 1501 1755 43 12 20 25  0  0
```

`si` und `so` sind dauerhaft über null: Der Server schiebt ständig Speicher auf die Platte und zurück. Finde den Prozess, der so viel Speicher braucht, siehe [`top`](../08-processes/top.md).

## Wann brauche ich das?

- Als erster Befehl, wenn ein Server langsam ist: CPU, Speicher oder Platte?
- Um einen Lasttest oder einen Backup-Lauf live zu beobachten
- Um herauszufinden, ob eine VM unter einem überlasteten Host leidet (`st`)

!!! tip "Die erste Zeile ignorieren"
    Die erste Zeile zeigt Durchschnittswerte seit dem Start, nicht den aktuellen Zustand.
    Schau auf die folgenden Zeilen, etwa mit `vmstat 2 5`.

## Verwandte Befehle

[iostat](iostat.md) · [sar](sar.md) · [top](../08-processes/top.md) · [free](../08-processes/free.md)
