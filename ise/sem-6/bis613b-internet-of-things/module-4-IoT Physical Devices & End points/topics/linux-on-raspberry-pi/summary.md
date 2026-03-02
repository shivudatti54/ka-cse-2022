# Linux on Raspberry Pi

=====================================

### Overview

Linux is the primary operating system used on Raspberry Pi for IoT applications, with Raspberry Pi OS (formerly Raspbian) being the most common Debian-based distribution. It provides stability, security, an extensive software ecosystem, and strong hardware support essential for IoT development.

### Key Points

- **Raspberry Pi OS:** A Debian-based Linux distribution specifically optimized for Raspberry Pi hardware, installed via SD card using tools like Raspberry Pi Imager or BalenaEtcher.
- **Package Management:** Uses APT (Advanced Package Tool) with commands like apt update, apt upgrade, and apt install for software management.
- **Headless Operation:** IoT devices often run without a monitor, making command-line proficiency (pwd, ls, cd, ssh, scp) essential.
- **GPIO Access:** Linux provides GPIO control through the sysfs virtual filesystem (/sys/class/gpio/) and libraries like RPi.GPIO, gpiozero, and pigpio.
- **Service Management:** Systemd (systemctl) is used to start, stop, enable, and manage services and daemons including custom IoT applications.
- **Security Hardening:** Includes changing default passwords, using SSH key authentication, enabling firewalls (ufw/iptables), and disabling unnecessary services.
- **Process Automation:** IoT applications can auto-start at boot using systemd service files, cron @reboot, or /etc/rc.local.
- **Monitoring Tools:** Commands like top, free -h, df -h, and vcgencmd measure_temp help monitor system resources and temperature.

### Important Concepts

- Linux filesystem hierarchy: /etc (configuration), /home/pi (projects), /var/log (logs)
- apt update vs apt upgrade: update refreshes package lists, upgrade installs newer versions
- sysfs GPIO interface: export, direction, value, unexport sequence
- systemd service files with [Unit], [Service], and [Install] sections
- journalctl for centralized system and application logging

### Notes

- The difference between apt update (refresh package lists) and apt upgrade (install updates) is frequently tested in exams.
- Know both sysfs and library-based GPIO access methods as exam questions may cover either approach.
- Security practices like SSH key authentication and changing default credentials are crucial exam topics for IoT device deployment.
