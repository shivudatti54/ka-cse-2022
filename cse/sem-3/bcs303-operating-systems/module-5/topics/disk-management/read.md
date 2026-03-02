# Disk Management

## Introduction

Once a disk drive is manufactured, it must be prepared before the OS can use it to store data. **Disk management** covers the tasks the OS performs to initialize, organize, and maintain disks — including **disk formatting**, **boot block management**, **bad block recovery**, and **swap-space management**.

This topic corresponds to **Section 10.5** of Silberschatz (Operating System Concepts).

## Disk Formatting

A new disk is a blank platter with no structure. Before use, it must undergo two levels of formatting.

### Low-Level Formatting (Physical Formatting)

Low-level formatting divides the disk into **sectors** that the disk controller can read and write. Each sector has a specific structure:

```
Sector Structure:

+--------+------+--------+
| Header | Data | ECC |
+--------+------+--------+

Header → Sector number, cylinder/track info
Data → Typically 512 bytes or 4096 bytes (4K sectors)
ECC → Error-Correcting Code (detects and corrects small errors)
```

- Performed at the factory by the disk manufacturer
- Sets the sector size (usually 512 bytes, modern drives use 4 KB)
- Writes the header and ECC for every sector on every track

### Logical Formatting (High-Level Formatting)

After physical formatting, the OS writes its **file system data structures** onto the disk:

1. **Partition the disk** — Divide into one or more partitions (each treated as a separate disk)
2. **Create file system** — Write the file system structures (superblock, free-space management, empty root directory, etc.)

```
Disk After Formatting:

+------------------+-------------------+-------------------+
| Partition 1 | Partition 2 | Partition 3 |
| (ext4 - Linux) | (swap space) | (NTFS - Windows) |
| | | |
| Superblock | Swap header | MFT |
| Inode table | | Bitmap |
| Root directory | | Root directory |
| Data blocks | Swap pages | Data clusters |
+------------------+-------------------+-------------------+
```

Some OS allows a partition to be used as a **raw disk** (no file system) — used for swap space or databases that manage their own storage.

## Boot Block

For a computer to start, it needs a program to run — the **bootstrap loader**. The bootstrap is stored in a known, fixed location on disk so the hardware can find it.

### Boot Process

```
Boot Sequence:

1. Power on
 ↓
2. CPU executes firmware (BIOS/UEFI) from ROM/NVM
 ↓
3. Firmware reads the MBR (Master Boot Record) from disk
 - MBR is the first sector (sector 0) of the boot disk
 ↓
4. MBR contains a small bootstrap program + partition table
 ↓
5. Bootstrap identifies the active (boot) partition
 ↓
6. Loads the boot block from the active partition
 ↓
7. Boot block loads the full OS kernel
 ↓
8. Kernel initializes and starts the system
```

### Master Boot Record (MBR)

```
MBR Structure (512 bytes):

+----------------------------+
| Bootstrap code (446 bytes) |
+----------------------------+
| Partition table (64 bytes) | ← Up to 4 primary partitions
+----------------------------+
| Magic number (2 bytes) | ← 0x55AA (identifies valid MBR)
+----------------------------+
```

### Windows vs UNIX Boot

| System         | Boot Process                                                                              |
| :------------- | :---------------------------------------------------------------------------------------- |
| **Windows**    | MBR → active partition → boot sector → Windows Boot Manager → loads kernel (ntoskrnl.exe) |
| **UNIX/Linux** | MBR → GRUB boot loader → user selects OS/kernel → loads kernel → runs init/systemd        |

## Bad Block Management

Over time, disk sectors can become defective (bad blocks). The OS must detect and handle these to prevent data loss.

### Handling Bad Blocks

**Simple disks (IDE/ATA):**

- The OS handles bad blocks manually
- During logical formatting, a program scans the disk and marks bad blocks
- Bad blocks are added to a **bad block list** and are never allocated to files
- Example: MS-DOS `FORMAT` marks bad blocks in the FAT as unusable

**Sophisticated disks (SCSI, modern drives):**

- The disk controller handles bad blocks internally using **sector sparing** (also called sector forwarding)
- The controller maintains a list of bad sectors and transparently redirects access to **spare sectors**

```
Sector Sparing:

Logical sectors: [0] [1] [2] [3] [4] [5] ...
 ↑
 BAD SECTOR
 ↓
 Spare sector pool
 [S1] [S2] [S3] ...
 ↑
 Sector 2 remapped to S1

OS sees: [0] [1] [S1] [3] [4] [5] ...
 (transparent — OS doesn't know about the remapping)
```

**Sector slipping** — an alternative where instead of remapping to a distant spare, the controller shifts sectors to fill the gap:

```
Sector Slipping:

Before: [0] [1] [BAD] [3] [4] [5] [spare]
After: [0] [1] [3] [4] [5] [spare→3's old data]

Sectors 3, 4, 5 each "slip" by one position
Result: sequential access is preserved (no seeking to spare area)
```

### Soft Errors vs Hard Errors

| Type           | Description                                  | Recovery                                         |
| :------------- | :------------------------------------------- | :----------------------------------------------- |
| **Soft error** | Transient read error (e.g., dust, vibration) | ECC can recover data; retry succeeds             |
| **Hard error** | Permanent physical damage to the sector      | Sector must be spared/remapped; data may be lost |

## Swap-Space Management

**Swap space** is disk space used as an extension of main memory. When physical RAM is full, the OS moves (swaps) less-used pages to swap space on disk.

### Purpose of Swap Space

```
Without Swap:
 RAM: [P1][P2][P3] → FULL → Cannot start P4!

With Swap:
 RAM: [P1][P2][P3] → FULL
 Swap out P2 to disk:
 RAM: [P1][P4][P3] Swap: [P2]
 P2 can be swapped back in when needed
```

### Swap-Space Location

Swap space can be in two locations:

| Location               | Description                                                          | Pros                             | Cons                                                  |
| :--------------------- | :------------------------------------------------------------------- | :------------------------------- | :---------------------------------------------------- |
| **Normal file system** | A swap file within an existing partition (e.g., a regular file)      | Easy to create/resize            | Slower (file system overhead, external fragmentation) |
| **Raw partition**      | A separate partition with no file system, managed directly by the OS | Faster (no file system overhead) | Fixed size, harder to resize                          |

Most systems use a **raw partition** for performance, since swap is heavily used and must be fast.

### Swap-Space Management Approaches

**Approach 1: Swap entire process (older systems)**

```
Process P (100 KB) swapped out:
 Swap space: [P: 100 KB contiguous block]
 Managed like variable partitioning (first-fit, best-fit)
```

**Approach 2: Swap individual pages (modern systems)**

```
Swap space divided into page-sized slots (e.g., 4 KB each):

Swap space:
+------+------+------+------+------+------+
| P1:3 | P2:7 | free | P1:8 | free | P3:2 |
+------+------+------+------+------+------+

Each slot holds one page. A swap map tracks which pages
are in which slots.
```

### Linux Swap

Linux supports both swap partitions and swap files:

```bash
# Create a swap partition
mkswap /dev/sda3
swapon /dev/sda3

# Create a swap file
dd if=/dev/zero of=/swapfile bs=1M count=1024
mkswap /swapfile
swapon /swapfile

# View swap usage
swapon --show
free -h
```

Linux uses a **swap map** — an array of integers, one per page-sized slot in swap space. Each entry stores a counter indicating how many processes are sharing that swapped page (0 = free).

### Windows Swap (Page File)

Windows uses a **page file** (`pagefile.sys`) on the file system:

```
C:\pagefile.sys → Windows swap file
- Default: system-managed size
- Can be configured via System Properties → Advanced → Performance
```

## Summary

| Concept                     | Key Point                                                                   |
| :-------------------------- | :-------------------------------------------------------------------------- |
| Low-level formatting        | Creates sectors (header + data + ECC) on blank disk; done at factory        |
| Logical formatting          | Creates file system structures (superblock, root directory) on a partition  |
| Boot block                  | MBR (sector 0) holds bootstrap + partition table; loads OS kernel at boot   |
| Bad block — sector sparing  | Controller remaps bad sector to a spare sector transparently                |
| Bad block — sector slipping | Controller shifts adjacent sectors to fill gap, preserving sequential order |
| Swap space — raw partition  | Faster; OS manages directly without file system overhead                    |
| Swap space — file system    | Easier to manage; slower due to file system overhead                        |
| Swap map                    | Data structure tracking which swap slots are in use and shared page counts  |

## Exam Tips

1. **Disk formatting levels** — Distinguish between low-level (physical — creates sectors) and logical (creates file system). may ask "Explain the two levels of disk formatting."
2. **Boot process** — Be able to draw the boot sequence: firmware → MBR → boot block → kernel. This is a common 5-mark question.
3. **Bad block handling** — Explain sector sparing vs sector slipping with diagrams. Know the difference between soft errors (recoverable via ECC) and hard errors (require remapping).
4. **Swap-space management** — Compare raw partition vs file system swap. Know that modern systems swap individual pages, not entire processes.
5. **MBR structure** — Know the three parts: bootstrap code (446 bytes), partition table (64 bytes), magic number (2 bytes) = 512 bytes total.
6. **Numerical question possibility** — may ask to calculate swap space needed given number of processes and page sizes.
