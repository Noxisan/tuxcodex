---
icon: material/infinity
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-infinity:{ .tc-hero-icon }

# CI/CD

Testing and deploying automatically: pipelines in GitHub Actions and GitLab CI, watching
runs from the terminal, keeping secrets out of the code and catching mistakes before they
are pushed.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Pipelines, jobs and runners, what to install, a workflow for GitHub and one for GitLab :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## GitHub Actions

<div class="grid cards" markdown>

-   :material-play-circle-outline:{ .lg .middle } **[gh run](gh-run.md)**

    ---

    List, watch and rerun workflow runs.

-   :material-sitemap-outline:{ .lg .middle } **[gh workflow](gh-workflow.md)**

    ---

    Start, enable and disable workflows.

-   :material-key-outline:{ .lg .middle } **[gh secret](gh-secret.md)**

    ---

    Store passwords and keys as secrets.

-   :material-laptop:{ .lg .middle } **[act](act.md)**

    ---

    Run workflows locally in Docker.

</div>

## GitLab CI

<div class="grid cards" markdown>

-   :material-server-outline:{ .lg .middle } **[gitlab-runner](gitlab-runner.md)**

    ---

    Run GitLab jobs on your own server.

-   :material-gitlab:{ .lg .middle } **[glab ci](glab-ci.md)**

    ---

    Pipelines from the terminal.

</div>

## Quality before the push

<div class="grid cards" markdown>

-   :material-file-check-outline:{ .lg .middle } **[actionlint](actionlint.md)**

    ---

    Find mistakes in workflow files.

-   :material-code-braces:{ .lg .middle } **[yamllint](yamllint.md)**

    ---

    Check any YAML file.

</div>
