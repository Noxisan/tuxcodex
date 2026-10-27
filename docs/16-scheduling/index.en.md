---
icon: material/calendar-clock
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-calendar-clock:{ .tc-hero-icon }

# Scheduling

Running jobs regularly with cron and systemd timers, once at a set time with `at`, catching up
on missed jobs and making sure a job never runs twice at the same time.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** cron syntax, where cron jobs live and systemd timers compared :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## cron

<div class="grid cards" markdown>

-   :material-calendar-edit:{ .lg .middle } **[crontab](crontab.md)**

    ---

    Show and edit the cron jobs of a user.

-   :material-folder-play-outline:{ .lg .middle } **[run-parts](run-parts.md)**

    ---

    Run all scripts in a directory.

-   :material-calendar-refresh-outline:{ .lg .middle } **[anacron](anacron.md)**

    ---

    Catch up on missed daily jobs.

</div>

## One-time jobs

<div class="grid cards" markdown>

-   :material-clock-plus-outline:{ .lg .middle } **[at](at.md)**

    ---

    Run a command once at a given time.

-   :material-format-list-bulleted:{ .lg .middle } **[atq](atq.md)**

    ---

    List waiting at jobs.

</div>

## Avoid overlaps

<div class="grid cards" markdown>

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-cog-play-outline:{ .lg .middle } **[systemctl](../09-systemd/systemctl.md)**

    ---

    `systemctl list-timers` shows all systemd timers. Covered in the chapter systemd.

-   :material-rocket-launch-outline:{ .lg .middle } **[systemd-run](../09-systemd/systemd-run.md)**

    ---

    Run a command once at a later time as a temporary timer. Covered in the chapter systemd.

-   :material-chart-timeline:{ .lg .middle } **[systemd-analyze](../09-systemd/systemd-analyze.md)**

    ---

    Check timer expressions with `systemd-analyze calendar`. Covered in the chapter systemd.

</div>
