# whoami

> Prints the name of the user you are currently logged in as.

## Syntax

```bash
whoami
```

## Example

```bash
whoami
```

```text
nox
```

![whoami in the terminal](../assets/screenshots/whoami.png)

## When do I need it?

- After `su` or `sudo -i`, to check which user you are working as
- In scripts, to make sure they don't run as root by mistake

!!! tip "Good to know"
    `whoami` shows the **effective** user. After `sudo whoami`, the output is `root`.

## Related commands

[id](id.md) · [hostname](hostname.md)
