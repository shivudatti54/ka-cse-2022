# Linux on Raspberry Pi for IoT Applications


## Table of Contents

- [Linux on Raspberry Pi for IoT Applications](#linux-on-raspberry-pi-for-iot-applications)
- [Introduction to Linux on Raspberry Pi](#introduction-to-linux-on-raspberry-pi)
- [Why Linux for IoT on Raspberry Pi?](#why-linux-for-iot-on-raspberry-pi)
  - [Advantages of Using Linux](#advantages-of-using-linux)
  - [Comparison of Linux vs Other OS Options for Raspberry Pi](#comparison-of-linux-vs-other-os-options-for-raspberry-pi)
- [Setting Up Linux on Raspberry Pi](#setting-up-linux-on-raspberry-pi)
  - [Preparing the SD Card](#preparing-the-sd-card)
  - [First Boot and Configuration](#first-boot-and-configuration)
- [Linux Command Line Essentials for IoT](#linux-command-line-essentials-for-iot)
  - [Basic Command Line Operations](#basic-command-line-operations)
- [Navigation](#navigation)
- [File operations](#file-operations)
- [System monitoring](#system-monitoring)
  - [Network Configuration and Troubleshooting](#network-configuration-and-troubleshooting)
- [Check network configuration](#check-network-configuration)
- [WiFi management](#wifi-management)
- [Remote access](#remote-access)
- [Package Management and Software Installation](#package-management-and-software-installation)
  - [Using apt Package Manager](#using-apt-package-manager)
- [Update package lists](#update-package-lists)
- [Upgrade installed packages](#upgrade-installed-packages)
- [Install new software](#install-new-software)
- [Remove software](#remove-software)
- [Search for packages](#search-for-packages)
  - [Python Package Management with pip](#python-package-management-with-pip)
- [Install pip if not present](#install-pip-if-not-present)
- [Install Python packages](#install-python-packages)
- [Install for specific user to avoid system-wide changes](#install-for-specific-user-to-avoid-system-wide-changes)
- [Linux Services and Daemons for IoT](#linux-services-and-daemons-for-iot)
  - [Systemd Service Management](#systemd-service-management)
- [Check status of a service](#check-status-of-a-service)
- [Start a service](#start-a-service)
- [Stop a service](#stop-a-service)
- [Enable a service to start at boot](#enable-a-service-to-start-at-boot)
- [Disable a service from starting at boot](#disable-a-service-from-starting-at-boot)
  - [Common IoT-relevant Services](#common-iot-relevant-services)
- [File System Structure and Important Directories](#file-system-structure-and-important-directories)
- [GPIO Access from Linux](#gpio-access-from-linux)
  - [sysfs Interface](#sysfs-interface)
- [Export GPIO pin 17 for use](#export-gpio-pin-17-for-use)
- [Set direction as output](#set-direction-as-output)
- [Set pin high](#set-pin-high)
- [Set pin low](#set-pin-low)
- [Unexport when done](#unexport-when-done)
  - [Libraries for GPIO Access](#libraries-for-gpio-access)
- [Security Considerations for IoT Devices](#security-considerations-for-iot-devices)
  - [Basic Security Hardening](#basic-security-hardening)
  - [Implementing SSH Key Authentication](#implementing-ssh-key-authentication)
- [Generate SSH key pair on your development machine](#generate-ssh-key-pair-on-your-development-machine)
- [Copy public key to Raspberry Pi](#copy-public-key-to-raspberry-pi)
- [Disable password authentication in /etc/ssh/sshd_config](#disable-password-authentication-in-etcsshsshdconfig)
- [Process Management for IoT Applications](#process-management-for-iot-applications)
  - [Running Applications at Boot](#running-applications-at-boot)
  - [Example systemd Service File](#example-systemd-service-file)
- [Monitoring and Logging](#monitoring-and-logging)
  - [System Logging with journalctl](#system-logging-with-journalctl)
- [View all logs](#view-all-logs)
- [Follow logs in real-time](#follow-logs-in-real-time)
- [View logs for a specific service](#view-logs-for-a-specific-service)
- [View logs since boot](#view-logs-since-boot)
  - [Application-specific Logging](#application-specific-logging)
- [Performance Optimization for Resource-constrained Environments](#performance-optimization-for-resource-constrained-environments)
  - [Monitoring Resource Usage](#monitoring-resource-usage)
- [Check CPU usage](#check-cpu-usage)
- [Check memory usage](#check-memory-usage)
- [Check disk I/O](#check-disk-io)
- [Check temperature (important for Pi)](#check-temperature-important-for-pi)
  - [Optimization Techniques](#optimization-techniques)
- [Exam Tips](#exam-tips)

## Introduction to Linux on Raspberry Pi

The Raspberry Pi is a series of small, affordable single-board computers that have become immensely popular in IoT development. At the heart of most Raspberry Pi IoT implementations lies a Linux-based operating system. Linux provides the stability, flexibility, and extensive software ecosystem that makes the Raspberry Pi an ideal platform for IoT applications.

Linux is an open-source Unix-like operating system kernel that forms the basis for numerous operating system distributions. When we refer to "Linux on Raspberry Pi," we're typically talking about Raspberry Pi OS (formerly Raspbian), which is a Debian-based distribution specifically optimized for Raspberry Pi hardware.

## Why Linux for IoT on Raspberry Pi?

### Advantages of Using Linux

1. **Open Source Nature**: Linux is free to use, modify, and distribute, which aligns perfectly with the Raspberry Pi's educational and DIY ethos.

2. **Stability and Reliability**: Linux systems are known for their uptime and stability, crucial for IoT devices that may need to run continuously.

3. **Security**: Linux provides robust security features that can be crucial for IoT devices connected to networks.

4. **Package Management**: Linux distributions offer package managers (like apt in Debian-based systems) that simplify software installation and updates.

5. **Community Support**: Extensive documentation, forums, and communities provide support for developers.

6. **Hardware Support**: Linux has excellent driver support for the various peripherals and interfaces on the Raspberry Pi.

### Comparison of Linux vs Other OS Options for Raspberry Pi

| Feature                | Linux (Raspberry Pi OS) | Windows IoT Core        | Other Embedded OS |
| ---------------------- | ----------------------- | ----------------------- | ----------------- |
| Cost                   | Free                    | Free (with limitations) | Varies            |
| Resource Usage         | Moderate                | Higher                  | Typically lower   |
| Software Availability  | Extensive               | Limited                 | Varies            |
| Community Support      | Excellent               | Good                    | Varies            |
| Real-time Capabilities | With patches            | Limited                 | Native            |
| Security Updates       | Regular                 | Microsoft-managed       | Varies            |

## Setting Up Linux on Raspberry Pi

### Preparing the SD Card

The process of installing Linux on a Raspberry Pi involves:

1. **Downloading the OS image**: Typically Raspberry Pi OS from the official website
2. **Writing the image to an SD card**: Using tools like:
   - Raspberry Pi Imager (recommended for beginners)
   - BalenaEtcher
   - dd command on Linux/Mac
3. **Configuring initial settings**: Some tools allow pre-configuration of WiFi, SSH, and other settings

```
+----------------+     +-----------------+     +-----------------+
| Download OS    | --> | Write to SD     | --> | Insert SD Card  |
| Image          |     | Card using      |     | into Raspberry  |
|                |     | Imager Tool     |     | Pi and Boot     |
+----------------+     +-----------------+     +-----------------+
```

### First Boot and Configuration

Upon first boot, Raspberry Pi OS typically guides you through:

- Setting up country and language preferences
- Changing the default password (highly recommended)
- Connecting to WiFi networks
- Updating the system software

## Linux Command Line Essentials for IoT

### Basic Command Line Operations

IoT devices often run headless (without a monitor), making command line proficiency essential:

```bash
# Navigation
pwd          # Print working directory
ls           # List files
cd           # Change directory

# File operations
cp           # Copy files
mv           # Move/rename files
rm           # Remove files

# System monitoring
top          # Display Linux processes
htop         # Enhanced process viewer (install with sudo apt install htop)
df -h        # Check disk space usage
free -h      # Check memory usage
```

### Network Configuration and Troubleshooting

For IoT devices, network connectivity is crucial:

```bash
# Check network configuration
ifconfig     # Display network interface configuration (deprecated but still used)
ip addr      # Modern alternative to ifconfig
ping         # Test network connectivity

# WiFi management
nmcli        # NetworkManager command line interface
iwconfig     # Configure wireless interfaces

# Remote access
ssh          # Secure Shell for remote access
scp          # Secure copy for file transfer
```

## Package Management and Software Installation

### Using apt Package Manager

Raspberry Pi OS uses Debian's Advanced Package Tool (apt):

```bash
# Update package lists
sudo apt update

# Upgrade installed packages
sudo apt upgrade

# Install new software
sudo apt install package_name

# Remove software
sudo apt remove package_name

# Search for packages
apt search search_term
```

### Python Package Management with pip

Since Python is heavily used in IoT development:

```bash
# Install pip if not present
sudo apt install python3-pip

# Install Python packages
pip3 install package_name

# Install for specific user to avoid system-wide changes
pip3 install --user package_name
```

## Linux Services and Daemons for IoT

### Systemd Service Management

Modern Linux distributions use systemd for service management:

```bash
# Check status of a service
sudo systemctl status service_name

# Start a service
sudo systemctl start service_name

# Stop a service
sudo systemctl stop service_name

# Enable a service to start at boot
sudo systemctl enable service_name

# Disable a service from starting at boot
sudo systemctl disable service_name
```

### Common IoT-relevant Services

- **ssh**: For remote access
- **cron**: For scheduling tasks
- **nginx/apache**: Web servers for IoT dashboards
- **mosquitto**: MQTT broker for IoT messaging

## File System Structure and Important Directories

Understanding the Linux filesystem hierarchy is crucial for IoT development:

```
/
├── bin      -> Essential command binaries
├── boot     -> Boot loader files
├── dev      -> Device files
├── etc      -> System configuration files
├── home     -> User home directories
├── lib      -> Essential shared libraries
├── media    -> Mount points for removable media
├── mnt      -> Temporarily mounted filesystems
├── opt      -> Optional application software packages
├── proc     -> Process information pseudo-filesystem
├── root     -> Home directory for the root user
├── run      -> Run-time variable data
├── sbin     -> Essential system binaries
├── srv      -> Data for services provided by the system
├── sys      -> System information pseudo-filesystem
├── tmp      -> Temporary files
├── usr      -> Secondary hierarchy
└── var      -> Variable data
```

For IoT applications, particularly important directories include:

- `/etc/` for configuration files
- `/home/pi/` for user projects
- `/var/log/` for system and application logs

## GPIO Access from Linux

### sysfs Interface

Linux provides access to GPIO through the sysfs virtual filesystem:

```bash
# Export GPIO pin 17 for use
echo 17 > /sys/class/gpio/export

# Set direction as output
echo out > /sys/class/gpio/gpio17/direction

# Set pin high
echo 1 > /sys/class/gpio/gpio17/value

# Set pin low
echo 0 > /sys/class/gpio/gpio17/value

# Unexport when done
echo 17 > /sys/class/gpio/unexport
```

### Libraries for GPIO Access

While direct sysfs access works, libraries simplify GPIO programming:

- **RPi.GPIO**: The standard Python library for Raspberry Pi GPIO
- **gpiozero**: Higher-level Python library, beginner-friendly
- **pigpio**: Provides remote GPIO access
- **wiringPi**: C library with command-line tools

## Security Considerations for IoT Devices

### Basic Security Hardening

IoT devices are often vulnerable targets. Essential security practices:

1. **Change default passwords**: Especially the 'pi' user password
2. **Disable unnecessary services**: Reduce attack surface
3. **Keep system updated**: Regular security updates
4. **Use firewall**: Configure iptables or ufw
5. **Disable password authentication for SSH**: Use key-based authentication instead

### Implementing SSH Key Authentication

```bash
# Generate SSH key pair on your development machine
ssh-keygen -t rsa -b 4096

# Copy public key to Raspberry Pi
ssh-copy-id pi@raspberrypi.local

# Disable password authentication in /etc/ssh/sshd_config
PasswordAuthentication no
```

## Process Management for IoT Applications

### Running Applications at Boot

Several methods to ensure IoT applications start automatically:

1. **systemd services**: Create a custom service file in `/etc/systemd/system/`
2. **cron @reboot**: Add line to crontab with `@reboot command`
3. **/etc/rc.local**: Add commands to this file (deprecated but still works)

### Example systemd Service File

Create `/etc/systemd/system/my-iot-app.service`:

```ini
[Unit]
Description=My IoT Application
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/my_iot_app.py
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

## Monitoring and Logging

### System Logging with journalctl

Linux uses systemd-journald for logging:

```bash
# View all logs
journalctl

# Follow logs in real-time
journalctl -f

# View logs for a specific service
journalctl -u service_name

# View logs since boot
journalctl -b
```

### Application-specific Logging

For IoT applications, implement proper logging:

```python
import logging

logging.basicConfig(
    filename='/var/log/my-iot-app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('Application started')
```

## Performance Optimization for Resource-constrained Environments

### Monitoring Resource Usage

```bash
# Check CPU usage
top

# Check memory usage
free -h

# Check disk I/O
iotop

# Check temperature (important for Pi)
vcgencmd measure_temp
```

### Optimization Techniques

1. **Use light-weight software**: Choose alternatives to resource-heavy applications
2. **Disable GUI**: Run headless without desktop environment
3. **Use tmpfs**: For frequently accessed temporary files
4. **Adjust swappiness**: Control swap usage behavior
5. **Use zram**: Compressed RAM for swap

## Exam Tips

1. **Remember key directories**: /etc for configuration, /home/pi for user files, /var/log for logs
2. **Understand package management**: apt update vs upgrade difference is frequently tested
3. **Know GPIO access methods**: Both sysfs and library approaches are important
4. **Security practices**: Changing default passwords and SSH key authentication are crucial
5. **Service management**: systemctl commands for starting, stopping, and enabling services
6. **Troubleshooting steps**: Be familiar with basic network and process troubleshooting commands
7. **Resource monitoring**: Know commands to check CPU, memory, and temperature
