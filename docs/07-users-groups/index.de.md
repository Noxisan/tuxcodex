---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-account-multiple-outline:{ .tc-hero-icon }

# Benutzer und Gruppen

Benutzer und Gruppen anlegen, ändern und löschen, Passwörter verwalten und mit
Root-Rechten über `sudo` und `su` arbeiten.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Die wichtigen Dateien: passwd, shadow, group, sudoers :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Benutzer und Gruppen nachschlagen

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } **[groups](groups.md)**

    ---

    Zeigt die Gruppen eines Benutzers.

-   :material-account-search-outline:{ .lg .middle } **[getent](getent.md)**

    ---

    Schlägt Benutzer, Gruppen, Hosts und Dienste nach.

</div>

## Benutzer verwalten

<div class="grid cards" markdown>

-   :material-account-plus-outline:{ .lg .middle } **[adduser](adduser.md)**

    ---

    Legt Schritt für Schritt einen neuen Benutzer an (Debian, Ubuntu).

-   :material-account-plus:{ .lg .middle } **[useradd](useradd.md)**

    ---

    Legt einen Benutzer in einem Befehl an, für Skripte und jede Distribution.

-   :material-account-edit-outline:{ .lg .middle } **[usermod](usermod.md)**

    ---

    Ändert Gruppen, Shell, Name oder Sperre eines Benutzers.

-   :material-form-textbox-password:{ .lg .middle } **[passwd](passwd.md)**

    ---

    Setzt, sperrt, entsperrt oder erneuert ein Passwort.

-   :material-calendar-clock-outline:{ .lg .middle } **[chage](chage.md)**

    ---

    Legt Passwort- und Kontoablauf fest.

-   :material-account-minus-outline:{ .lg .middle } **[deluser](deluser.md)**

    ---

    Löscht einen Benutzer oder entfernt ihn aus einer Gruppe (Debian, Ubuntu).

-   :material-account-remove-outline:{ .lg .middle } **[userdel](userdel.md)**

    ---

    Löscht ein Benutzerkonto auf jeder Distribution.

</div>

## Gruppen verwalten

<div class="grid cards" markdown>

-   :material-account-multiple-plus-outline:{ .lg .middle } **[addgroup](addgroup.md)**

    ---

    Legt eine Gruppe an oder fügt ihr einen Benutzer hinzu (Debian, Ubuntu).

-   :material-account-multiple-plus:{ .lg .middle } **[groupadd](groupadd.md)**

    ---

    Legt eine Gruppe auf jeder Distribution an.

-   :material-account-cog-outline:{ .lg .middle } **[gpasswd](gpasswd.md)**

    ---

    Fügt Gruppenmitglieder hinzu oder entfernt sie.

-   :material-account-multiple-minus-outline:{ .lg .middle } **[delgroup](delgroup.md)**

    ---

    Löscht eine Gruppe oder entfernt einen Benutzer daraus (Debian, Ubuntu).

</div>

## Root-Rechte

<div class="grid cards" markdown>

-   :material-account-switch-outline:{ .lg .middle } **[su](su.md)**

    ---

    Wechselt zu einem anderen Benutzer, standardmäßig zu root.

-   :material-shield-crown-outline:{ .lg .middle } **[sudo](sudo.md)**

    ---

    Führt Befehle als root oder anderer Benutzer aus.

-   :material-file-document-edit-outline:{ .lg .middle } **[visudo](visudo.md)**

    ---

    Bearbeitet die sudo-Konfiguration sicher.

</div>
