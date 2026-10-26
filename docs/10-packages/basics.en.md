# Understanding packages

On Linux, you rarely install software by downloading a file from a website. Programs come
as **packages** from the **repositories** of your distribution: signed archives with the
program, its configuration files and a list of what else it needs. A **package manager**
downloads them, resolves the dependencies and keeps track of every installed file.

## Package managers per distribution

| | Debian, Ubuntu | RHEL, Rocky, Alma | Arch |
|---|----------------|-------------------|------|
| Package format | `.deb` | `.rpm` | `.pkg.tar.zst` |
| Package manager | `apt` | `dnf` | `pacman` |
| Low-level tool (single files, no repositories) | `dpkg` | `rpm` | `pacman -U` |
| Repositories configured in | `/etc/apt/sources.list.d/` | `/etc/yum.repos.d/` | `/etc/pacman.conf` |
| Release model | Stable releases | Stable releases with long support | Rolling release |

The high-level tool (`apt`, `dnf`) talks to the repositories and resolves dependencies.
The low-level tool (`dpkg`, `rpm`) only works with package files and the database of
installed packages.

## The same task with `apt`, `dnf` and `pacman`

| Task | `apt` | `dnf` | `pacman` |
|------|-------|-------|----------|
| Refresh the package lists | `apt update` | `dnf makecache` | `pacman -Sy` (only together with `-u`) |
| Install all updates | `apt upgrade` | `dnf upgrade` | `pacman -Syu` |
| Install a package | `apt install nginx` | `dnf install nginx` | `pacman -S nginx` |
| Remove a package | `apt remove nginx` | `dnf remove nginx` | `pacman -R nginx` |
| Remove it with configuration | `apt purge nginx` | *(not available)* | `pacman -Rn nginx` |
| Remove unneeded dependencies | `apt autoremove` | `dnf autoremove` | `pacman -Rns $(pacman -Qdtq)` |
| Search | `apt search nginx` | `dnf search nginx` | `pacman -Ss nginx` |
| Show details | `apt show nginx` | `dnf info nginx` | `pacman -Si nginx` |
| Which package owns a file? | `dpkg -S /usr/sbin/nginx` | `rpm -qf /usr/sbin/nginx` | `pacman -Qo /usr/sbin/nginx` |
| List installed packages | `apt list --installed` | `dnf list --installed` | `pacman -Q` |
| Clean the download cache | `apt clean` | `dnf clean all` | `pacman -Sc` |

All changing commands need `sudo`.

## Dependencies

Most packages need other packages: `htop` needs the library `libncursesw6`, for
example. The package manager installs them automatically and marks them as
**automatically installed**. If nothing needs them anymore, `apt autoremove` or
`dnf autoremove` removes them again.

Packages that you installed yourself are marked as **manually installed**. They are
never removed automatically.

## Where updates come from

| Distribution | Security updates |
|--------------|------------------|
| Debian | Separate repository `trixie-security` |
| Ubuntu | Repository `noble-security` (or the codename of your release) |
| RHEL | Errata in the normal repositories `BaseOS` and `AppStream` |
| Arch | New package versions in the normal repositories |

!!! tip "Use the repositories of your distribution"
    Packages from the official repositories get security updates automatically.
    Software that you install by hand from a website, or from a third-party repository,
    you have to keep up to date yourself.

!!! warning "Never mix releases"
    Don't add repositories of another release or distribution, for example Ubuntu
    packages on Debian. The result is often a system that can no longer be updated
    cleanly.
