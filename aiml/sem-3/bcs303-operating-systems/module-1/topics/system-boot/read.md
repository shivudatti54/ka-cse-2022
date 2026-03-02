# System Boot


## Table of Contents

- [System Boot](#system-boot)
- [Introduction](#introduction)
- [The Boot Process Overview](#the-boot-process-overview)
- [Step 1: Bootstrap Program (BIOS/UEFI)](#step-1-bootstrap-program-biosuefi)
  - [BIOS (Basic Input/Output System)](#bios-basic-inputoutput-system)
  - [UEFI (Unified Extensible Firmware Interface)](#uefi-unified-extensible-firmware-interface)
  - [Comparison: BIOS vs UEFI](#comparison-bios-vs-uefi)
- [Step 2: POST (Power-On Self-Test)](#step-2-post-power-on-self-test)
- [Step 3: MBR vs GPT](#step-3-mbr-vs-gpt)
  - [MBR (Master Boot Record)](#mbr-master-boot-record)
  - [GPT (GUID Partition Table)](#gpt-guid-partition-table)
- [Step 4: Bootloader](#step-4-bootloader)
  - [GRUB (GRand Unified Bootloader)](#grub-grand-unified-bootloader)
  - [GRUB Configuration](#grub-configuration)
- [/boot/grub/grub.cfg (simplified)](#bootgrubgrubcfg-simplified)
  - [Other Bootloaders](#other-bootloaders)
- [Step 5: Kernel Loading and Initialization](#step-5-kernel-loading-and-initialization)
  - [initrd / initramfs](#initrd--initramfs)
- [Step 6: Init Process (PID 1)](#step-6-init-process-pid-1)
  - [Traditional init (SysVinit)](#traditional-init-sysvinit)
  - [systemd (Modern init)](#systemd-modern-init)
- [Boot from Different Media](#boot-from-different-media)
  - [PXE (Network Boot)](#pxe-network-boot)
- [Complete Boot Sequence Summary](#complete-boot-sequence-summary)
- [Exam Tips](#exam-tips)

## Introduction

The **system boot** process is the sequence of steps a computer follows from the moment it is powered on until the operating system is fully loaded and ready for use. Understanding the boot process is essential because it explains how the OS gets loaded into memory and takes control of the hardware.

> **Definition:** System boot (or bootstrapping) is the process of loading the operating system kernel into memory and starting its execution when the computer is powered on or restarted.

The term "bootstrapping" comes from the phrase "pulling oneself up by one's bootstraps" -- the computer must start itself without any software already running.

## The Boot Process Overview

```
Power On
 |
 v
+------------------+
| 1. BIOS/UEFI | (firmware in ROM/flash)
| POST, hardware |
| initialization |
+------------------+
 |
 v
+------------------+
| 2. Bootloader | (GRUB, Windows Boot Manager)
| Loads kernel |
| from disk |
+------------------+
 |
 v
+------------------+
| 3. OS Kernel | (vmlinuz / ntoskrnl.exe)
| Initializes |
| hardware, |
| starts init |
+------------------+
 |
 v
+------------------+
| 4. Init/Systemd | (PID 1 process)
| Starts system |
| services |
+------------------+
 |
 v
+------------------+
| 5. Login Screen | (User interface ready)
| System Ready |
+------------------+
```

## Step 1: Bootstrap Program (BIOS/UEFI)

When the computer is powered on, the CPU begins executing code stored in **firmware** (non-volatile memory on the motherboard). This firmware program is called the **bootstrap program** or **bootstrap loader**.

### BIOS (Basic Input/Output System)

BIOS is the traditional firmware used in older computers:

- Stored in **ROM** (Read-Only Memory) or **EEPROM/Flash** on the motherboard
- First code executed when the computer is powered on
- Performs **POST** (Power-On Self-Test) to check hardware
- Initializes hardware devices (CPU, memory, keyboard, display)
- Locates the bootloader on a storage device
- Uses **MBR** (Master Boot Record) partition scheme

### UEFI (Unified Extensible Firmware Interface)

UEFI is the modern replacement for BIOS:

- More advanced than BIOS with a graphical interface
- Supports **GPT** (GUID Partition Table) for larger disks (>2 TB)
- **Secure Boot** feature prevents loading unauthorized OS code
- Faster boot times
- Can boot from network, USB, or large disks
- Stores boot programs in an **EFI System Partition (ESP)**

### Comparison: BIOS vs UEFI

| Feature              | BIOS                                 | UEFI                                     |
| -------------------- | ------------------------------------ | ---------------------------------------- |
| **Year introduced**  | 1981                                 | 2005+                                    |
| **Interface**        | Text-based                           | Graphical (mouse support)                |
| **Partition scheme** | MBR (max 2 TB, 4 primary partitions) | GPT (no practical limit, 128 partitions) |
| **Boot mode**        | 16-bit real mode                     | 32/64-bit protected mode                 |
| **Secure Boot**      | Not supported                        | Supported                                |
| **Boot speed**       | Slower                               | Faster                                   |
| **Disk size limit**  | 2 TB (MBR limitation)                | >2 TB (GPT support)                      |
| **Network boot**     | Limited (PXE)                        | Enhanced network boot                    |

## Step 2: POST (Power-On Self-Test)

POST is a diagnostic process performed by the BIOS/UEFI before booting:

```
POST Sequence:
+------------------------------------------+
| 1. Test CPU registers |
| 2. Check BIOS/UEFI firmware integrity |
| 3. Test RAM (memory count) |
| 4. Initialize keyboard and display |
| 5. Detect storage devices |
| 6. Detect other hardware (USB, network) |
| 7. If all OK --> proceed to boot |
| If error --> beep codes / error msg |
+------------------------------------------+
```

If POST detects a hardware failure, it produces **beep codes** or displays an error message.

## Step 3: MBR vs GPT

The storage device uses either MBR or GPT to organize its partitions and locate the bootloader.

### MBR (Master Boot Record)

```
Disk Layout with MBR:
+------+------------------------------------------+
| MBR | Disk Partitions |
|512 B | Part 1 | Part 2 | Part 3 | Part 4|
+------+----------+----------+----------+--------+
 |
 +-- Contains:
 - Boot code (446 bytes) - loads bootloader
 - Partition table (64 bytes) - 4 entries
 - Boot signature (2 bytes) - 0x55AA
```

**Limitations:**

- Maximum disk size: 2 TB
- Maximum 4 primary partitions (or 3 primary + 1 extended)
- Boot code is only 446 bytes

### GPT (GUID Partition Table)

```
Disk Layout with GPT:
+----------+-------+---------------------------+-------+
|Protective| GPT | Disk Partitions | Backup|
| MBR |Header | Part 1 | Part 2 | ... | GPT |
+----------+-------+----------+--------+-------+-------+
```

**Advantages over MBR:**

- No practical disk size limit (up to 9.4 ZB)
- Up to 128 partitions
- Redundant partition table (backup at end of disk)
- CRC32 checksums for data integrity
- Each partition has a unique GUID

## Step 4: Bootloader

The bootloader is a small program that loads the OS kernel from disk into memory. It is the intermediate step between firmware (BIOS/UEFI) and the OS kernel.

### GRUB (GRand Unified Bootloader)

**GRUB** is the most common bootloader for Linux systems. It has two stages:

```
GRUB Boot Process:
+------------------------------------------+
| Stage 1 (in MBR or ESP) |
| - Very small (446 bytes for MBR) |
| - Loads Stage 1.5 or Stage 2 |
+------------------------------------------+
 |
 v
+------------------------------------------+
| Stage 1.5 (in disk gap after MBR) |
| - Contains filesystem drivers |
| - Can read /boot partition |
+------------------------------------------+
 |
 v
+------------------------------------------+
| Stage 2 (in /boot/grub/) |
| - Displays boot menu |
| - Allows kernel selection |
| - Loads selected kernel into memory |
| - Passes boot parameters to kernel |
+------------------------------------------+
 |
 v
+------------------------------------------+
| OS Kernel loaded and starts executing |
+------------------------------------------+
```

### GRUB Configuration

```
# /boot/grub/grub.cfg (simplified)
menuentry "Ubuntu Linux" {
 set root=(hd0,1)
 linux /vmlinuz root=/dev/sda1 quiet splash
 initrd /initrd.img
}

menuentry "Windows 10" {
 set root=(hd0,2)
 chainloader +1
}
```

### Other Bootloaders

| Bootloader               | Platform       | Description                               |
| ------------------------ | -------------- | ----------------------------------------- |
| **GRUB 2**               | Linux          | Most popular Linux bootloader             |
| **Windows Boot Manager** | Windows        | Default Windows bootloader (bootmgr)      |
| **LILO**                 | Linux (legacy) | Linux Loader (replaced by GRUB)           |
| **systemd-boot**         | Linux          | Simple UEFI bootloader                    |
| **U-Boot**               | Embedded       | Universal bootloader for embedded systems |
| **rEFInd**               | Multi-OS       | UEFI boot manager for multi-boot          |

## Step 5: Kernel Loading and Initialization

Once the bootloader loads the kernel into memory, the kernel takes over:

```
Kernel Initialization:
+------------------------------------------+
| 1. Decompress kernel (if compressed) |
| 2. Initialize CPU and memory management |
| 3. Set up interrupt descriptor table |
| 4. Initialize device drivers |
| 5. Mount root filesystem |
| 6. Start init process (PID 1) |
+------------------------------------------+
```

### initrd / initramfs

The **initial RAM disk** (initrd) or **initial RAM filesystem** (initramfs) is a temporary root filesystem loaded into memory by the bootloader alongside the kernel. It contains:

- Essential device drivers needed to access the real root filesystem
- Boot scripts for early initialization

```
Bootloader loads:
+---------+ +----------+
| Kernel | | initrd/ |
| vmlinuz | | initramfs|
+---------+ +----------+
 | |
 v v
+------------------------------------------+
| Kernel uses initrd to load drivers |
| needed to mount the real root filesystem |
+------------------------------------------+
 |
 v
+------------------------------------------+
| Real root filesystem (/dev/sda1) mounted|
| System continues booting normally |
+------------------------------------------+
```

## Step 6: Init Process (PID 1)

After the kernel initializes, it starts the **init** process (Process ID 1), which is the parent of all other processes in the system.

### Traditional init (SysVinit)

Uses **runlevels** to define system states:

| Runlevel | Description                            |
| -------- | -------------------------------------- |
| 0        | Halt (shutdown)                        |
| 1        | Single-user mode (maintenance)         |
| 2        | Multi-user without networking          |
| 3        | Multi-user with networking (text mode) |
| 4        | Unused (custom)                        |
| 5        | Multi-user with networking and GUI     |
| 6        | Reboot                                 |

### systemd (Modern init)

Most modern Linux distributions use **systemd** instead of SysVinit:

- Uses **units** and **targets** instead of runlevels
- Parallel service startup (faster boot)
- Socket and D-Bus activation
- On-demand service starting

```bash
$ systemctl start httpd # Start a service
$ systemctl enable sshd # Enable service at boot
$ systemctl status nginx # Check service status
$ systemctl list-units # List all active units
```

## Boot from Different Media

The boot process can begin from various sources:

| Boot Media          | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Hard Disk / SSD** | Most common, OS installed on local disk                      |
| **USB Drive**       | Bootable USB for installation or live OS                     |
| **CD/DVD**          | Bootable optical media                                       |
| **Network (PXE)**   | Pre-boot Execution Environment; loads OS from network server |
| **NFS**             | Network File System boot for diskless workstations           |

### PXE (Network Boot)

```
+----------+ DHCP Request +----------+
| Client | ------------------> | DHCP |
| (no disk)| | Server |
+----------+ IP + boot file +----------+
 | <------------------
 |
 | TFTP Request +----------+
 | -------------------> | TFTP |
 | | Server |
 | Boot image +----------+
 | <-------------------
 |
 v
 Boot from downloaded image
```

## Complete Boot Sequence Summary

```
+----------------------------------------------------------+
| COMPLETE BOOT SEQUENCE |
+----------------------------------------------------------+
| |
| 1. Power On |
| 2. CPU jumps to firmware address (BIOS/UEFI) |
| 3. POST: hardware diagnostics |
| 4. Firmware finds boot device (disk, USB, network) |
| 5. Reads MBR/GPT to find bootloader |
| 6. Bootloader (GRUB) loaded and executed |
| 7. GRUB displays menu, user selects kernel |
| 8. GRUB loads kernel (vmlinuz) and initrd into memory |
| 9. Kernel decompresses and initializes |
| 10. Kernel mounts root filesystem |
| 11. Kernel starts init/systemd (PID 1) |
| 12. Services started (networking, SSH, GUI, etc.) |
| 13. Login prompt / Desktop displayed |
| 14. System ready for use |
| |
+----------------------------------------------------------+
```

## Exam Tips

1. **Bootstrap program definition** is a standard question. Define it as the first program to run when the computer is powered on, stored in ROM/flash firmware.
2. **Boot process steps:** Know the sequence: BIOS/UEFI -> POST -> Bootloader (GRUB) -> Kernel -> init/systemd -> Login. This is a 10-mark question.
3. **BIOS vs UEFI comparison** is frequently asked. Know at least 5-6 differences (MBR vs GPT, Secure Boot, disk size limits, interface).
4. **MBR vs GPT:** MBR supports up to 2 TB and 4 primary partitions; GPT has no practical limit and supports 128 partitions.
5. **GRUB bootloader:** Know its two-stage boot process and that it displays a menu for kernel selection.
6. **initrd/initramfs:** Know that it provides essential drivers needed to mount the real root filesystem.
7. **PID 1 process:** The init process (or systemd) is the first user-space process and the parent of all other processes.
8. ** commonly asks:** "Explain the system boot process" or "Describe the role of the bootstrap program" or "Compare BIOS and UEFI."
