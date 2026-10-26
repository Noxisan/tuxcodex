# The most important directories on a Linux server

| Directory | Contents |
|-----------|----------|
| `/` | Root of the file system, everything starts here |
| `/etc` | Configuration files of the system and all services |
| `/home` | Home directories of the users (`/home/nox`) |
| `/root` | Home directory of the `root` user |
| `/var/log` | Log files |
| `/var/lib` | Data of programs and services (databases, Docker, package lists) |
| `/var/www` | Web content on Debian and Ubuntu (RHEL: `/var/www/html`, Arch: `/srv/http`) |
| `/srv` | Data that the server provides (websites, FTP, Git repositories) |
| `/opt` | Additional software that is not installed via `apt` |
| `/usr/local` | Software and scripts you installed yourself |
| `/usr/bin` | Programs (`/bin` is a link to it) |
| `/tmp` | Temporary files; on Debian 13 and Arch kept in RAM and emptied on every reboot |
| `/boot` | Kernel and boot loader |
| `/proc`, `/sys` | Virtual file systems with live information from the kernel |
| `/dev` | Devices (disks, terminals) |
| `/mnt`, `/media` | Mount points for additional drives |
