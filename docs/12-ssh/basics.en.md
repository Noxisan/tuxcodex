# Understanding SSH

SSH (Secure Shell) is the encrypted connection to a server. It protects everything you
type and see, including passwords, and it carries file transfers with `scp`, `sftp` and
`rsync` as well as tunnels for other connections.

## Two kinds of keys

| Key | Belongs to | Purpose |
|-----|------------|---------|
| **Host key** | The server, in `/etc/ssh/ssh_host_*_key` | Proves to the client that it talks to the right server |
| **User key** | You, in `~/.ssh/id_ed25519` | Proves to the server who you are, instead of a password |

## Host keys and `known_hosts`

On the first connection, the client shows the fingerprint of the server's host key and
asks whether you trust it. After `yes`, the key is saved in `~/.ssh/known_hosts`. On every
later connection, the client checks that the server still has the same key.

If the key changes, SSH refuses the connection with
`WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`. That happens after a reinstallation
of the server, but it can also be an attack. Only remove the old key with
`ssh-keygen -R HOST` if you know why it changed.

## Login with a key

A key pair consists of two files:

| File | Content | Who may see it |
|------|---------|----------------|
| `~/.ssh/id_ed25519` | Private key | Only you. Never copy it to a server |
| `~/.ssh/id_ed25519.pub` | Public key | Anyone. It goes onto the servers |

The public key is put into `~/.ssh/authorized_keys` on the server, for example with
`ssh-copy-id`. When you log in, the server checks with it that you have the private key,
without the private key ever leaving your computer.

Protect the private key with a passphrase. With `ssh-agent`, you only enter it once per
session.

## The files in `~/.ssh` and their permissions

SSH refuses keys and configuration files that other users could read or change.

| File | Permissions | Purpose |
|------|-------------|---------|
| `~/.ssh/` | `700` (`drwx------`) | The directory itself |
| `id_ed25519` | `600` (`-rw-------`) | Private key |
| `id_ed25519.pub` | `644` (`-rw-r--r--`) | Public key |
| `authorized_keys` | `600` | Public keys that may log in to this account |
| `known_hosts` | `644` | Host keys of known servers |
| `config` | `600` | Client configuration |

## The client configuration `~/.ssh/config`

Instead of typing user, port and key every time, you give each server a short name:

```text
Host web
    HostName 192.0.2.10
    User nox
    Port 22
    IdentityFile ~/.ssh/id_ed25519

Host db
    HostName 192.0.2.20
    User nox
    ProxyJump web

Host *
    ServerAliveInterval 60
```

Now `ssh web` connects to `nox@192.0.2.10`, and `ssh db` reaches the database server
through `web` as a jump host. `ServerAliveInterval` keeps idle connections open.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SSH server package | `openssh-server` | `openssh-server` | `openssh-server` | `openssh` |
| Service name | `ssh` | `ssh` (socket activated since 22.10) | `sshd` | `sshd` |
| Root login by default | only with a key | only with a key | only with a key | only with a key |

!!! tip "Use Ed25519 keys"
    `ssh-keygen -t ed25519` creates short, fast and secure keys. RSA keys still work, but
    should be at least 3072 bits long.

!!! danger "Never lock yourself out"
    Before you switch off password login on a server, test the key login in a **second**
    session. Keep the first session open until the new one works.
