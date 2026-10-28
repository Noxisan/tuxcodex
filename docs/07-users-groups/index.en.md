---
title: "Users and groups"
icon: material/account-multiple-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-account-multiple-outline:{ .tc-hero-icon }

# Users and groups

Creating, changing and deleting users and groups, managing passwords and working with
root rights through `sudo` and `su`.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** The important files: passwd, shadow, group, sudoers :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Look up users and groups

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } **[groups](groups.md)**

    ---

    Show the groups a user belongs to.

-   :material-account-search-outline:{ .lg .middle } **[getent](getent.md)**

    ---

    Look up users, groups, hosts and services.

</div>

## Manage users

<div class="grid cards" markdown>

-   :material-account-plus-outline:{ .lg .middle } **[adduser](adduser.md)**

    ---

    Create a new user step by step (Debian, Ubuntu).

-   :material-account-plus:{ .lg .middle } **[useradd](useradd.md)**

    ---

    Create a user in one command, for scripts and every distribution.

-   :material-account-edit-outline:{ .lg .middle } **[usermod](usermod.md)**

    ---

    Change groups, shell, name or lock of a user.

-   :material-form-textbox-password:{ .lg .middle } **[passwd](passwd.md)**

    ---

    Set, lock, unlock or expire a password.

-   :material-calendar-clock-outline:{ .lg .middle } **[chage](chage.md)**

    ---

    Set password ageing and account expiry.

-   :material-account-minus-outline:{ .lg .middle } **[deluser](deluser.md)**

    ---

    Delete a user or remove it from a group (Debian, Ubuntu).

-   :material-account-remove-outline:{ .lg .middle } **[userdel](userdel.md)**

    ---

    Delete a user account on every distribution.

</div>

## Manage groups

<div class="grid cards" markdown>

-   :material-account-multiple-plus-outline:{ .lg .middle } **[addgroup](addgroup.md)**

    ---

    Create a group or add a user to it (Debian, Ubuntu).

-   :material-account-multiple-plus:{ .lg .middle } **[groupadd](groupadd.md)**

    ---

    Create a group on every distribution.

-   :material-account-cog-outline:{ .lg .middle } **[gpasswd](gpasswd.md)**

    ---

    Add or remove group members.

-   :material-account-multiple-minus-outline:{ .lg .middle } **[delgroup](delgroup.md)**

    ---

    Delete a group or remove a user from it (Debian, Ubuntu).

</div>

## Root rights

<div class="grid cards" markdown>

-   :material-account-switch-outline:{ .lg .middle } **[su](su.md)**

    ---

    Switch to another user, by default root.

-   :material-shield-crown-outline:{ .lg .middle } **[sudo](sudo.md)**

    ---

    Run commands as root or another user.

-   :material-file-document-edit-outline:{ .lg .middle } **[visudo](visudo.md)**

    ---

    Edit the sudo configuration safely.

</div>
