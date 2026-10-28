---
title: "Search with Elasticsearch and OpenSearch"
icon: material/text-search
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-search:{ .tc-hero-icon }

# Search with Elasticsearch and OpenSearch

Running a search cluster: checking health, indices and shards over the REST API, resetting
passwords, storing secrets in the keystore and managing plugins.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Elasticsearch or OpenSearch, installation and paths, the REST API with curl, green, yellow and red, memory and system settings :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Elasticsearch

<div class="grid cards" markdown>

-   :material-lock-reset:{ .lg .middle } **[elasticsearch-reset-password](elasticsearch-reset-password.md)**

    ---

    New password for elastic and other built-in users.

-   :material-key-chain-variant:{ .lg .middle } **[elasticsearch-keystore](elasticsearch-keystore.md)**

    ---

    Secret settings such as S3 keys.

-   :material-puzzle-outline:{ .lg .middle } **[elasticsearch-plugin](elasticsearch-plugin.md)**

    ---

    Install, list and remove plugins.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-web-check:{ .lg .middle } **[curl](../11-network/curl.md)**

    ---

    Talk to the REST API. Covered in the chapter Network.

-   :material-code-json:{ .lg .middle } **[jq](../05-text-processing/jq.md)**

    ---

    Filter the JSON answers. Covered in the chapter Text processing.

-   :material-tune:{ .lg .middle } **[sysctl](../27-performance/sysctl.md)**

    ---

    Set vm.max_map_count. Covered in the chapter Performance.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Open port 9200 only for application servers. Covered in the chapter Network.

</div>
