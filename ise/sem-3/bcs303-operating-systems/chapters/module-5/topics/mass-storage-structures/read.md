# Operating Systems - Module 5: Mass Storage Structures

## Introduction

In an operating system, the CPU and main memory are only part of the story. The vast majority of data is stored persistently on **mass storage devices**, primarily magnetic disks and solid-state drives. These devices are orders of magnitude slower than the CPU and RAM, making their efficient management critical to overall system performance. This module explores the hardware characteristics of these devices and the algorithms and structures the OS uses to manage them effectively.

## Core Concepts

### 1. Disk Structure and Scheduling

A traditional hard disk drive (HDD) is composed of multiple rotating **platters**, each with two **surfaces**. Each surface is divided into concentric circles called **tracks**, and tracks are further divided into **sectors** (typically 512 bytes or 4KB), which are the smallest unit of physical storage.

Accessing data on a disk requires three steps:

1.  **Seek Time:** The time to move the disk arm to the correct cylinder.
2.  **Rotational Latency:** The time for the desired sector to rotate under the read/write head.
3.  **Transfer Time:** The time to read from or write data to the sector.

Because seek and rotational delays are so high (milliseconds compared to nanoseconds for CPU operations), the OS employs **disk-scheduling algorithms** to minimize the total head movement (seek time).

**Common Disk Scheduling Algorithms:**

- **First-Come-First-Served (FCFS):** Simple but often results in inefficient, random head movement.
- **Shortest Seek Time First (SSTF):** Services the request closest to the current head position. While better than FCFS, it can lead to **starvation** for requests on outer/inner tracks.
- **SCAN (Elevator Algorithm):** The disk arm moves in one direction, servicing all requests until it reaches the end of the disk. It then reverses direction and repeats. This avoids starvation.
- **C-SCAN (Circular SCAN):** A variant of SCAN that treats the disk as a circular list. When it reaches one end, it immediately returns to the beginning to start again, providing a more uniform wait time.

_Example: Imagine a disk with 200 cylinders (0-199). The head is at cylinder 53, and the request queue is: 98, 183, 37, 122, 14, 124, 65, 67._

- **FCFS Order:** 98, 183, 37, 122, 14, 124, 65, 67 (Total head movement: 640 cylinders)
- **SSTF Order:** 65, 67, 37, 14, 98, 122, 124, 183 (Total head movement: 236 cylinders)
- **SCAN Order (moving towards 0 first):** 37, 14, 0, 65, 67, 98, 122, 124, 183 (Total head movement depends on the starting direction).

### 2. Disk Management

The OS is responsible for several disk management tasks:

- **Formatting (Low-Level):** Dividing the disk platter into sectors that the disk controller can read and write. Each sector is given a header, data area, and trailer.
- **Logical Formatting (Creation of a File System):** Creating data structures like the File Allocation Table (FAT) or inode structures on the disk to store files and directories.
- **Boot Block:** A small program stored in a predefined **boot sector** (often the first sector) of the disk is loaded into memory and executed at startup. This program then loads the entire operating system.

### 3. RAID Structure

**Redundant Array of Independent (or Inexpensive) Disks (RAID)** is a technology that combines multiple physical disk drives into a single logical unit for the purposes of **data redundancy**, **improved performance**, or both.

**Common RAID Levels:**

- **RAID 0 (Striping):** Data is split across disks. Improves performance but provides **no redundancy**. A single disk failure results in total data loss.
- **RAID 1 (Mirroring):** Data is duplicated on a second set of disks. Provides redundancy and fast read performance but doubles storage cost.
- **RAID 5 (Block-Level Striping with Distributed Parity):** Data and parity information are striped across all disks. It can tolerate the failure of any single disk. A good balance of performance, capacity, and redundancy.
- **RAID 10 (1+0):** A combination of mirroring and striping. Disks are mirrored in pairs, and then these pairs are striped. Provides high performance and redundancy.

### 4. Solid-State Drives (SSDs)

Unlike HDDs, SSDs have no moving parts. They use flash memory (NAND gates). Access time is incredibly fast and consistent as there is no seek or rotational latency. However, they introduce new challenges:

- **Wear Leveling:** Flash memory cells can withstand a limited number of write cycles. The OS/controller must distribute writes evenly across the drive to prevent specific blocks from wearing out prematurely.
- **Performance:** While reads are fast, writes can be slower due to the erase-before-write nature of flash memory.

## Key Points / Summary

- **Mass storage devices** (HDDs, SSDs) are critical for persistent data storage but are much slower than CPU/RAM.
- **Disk access time** is dominated by **seek time** and **rotational latency**.
- The OS uses **disk scheduling algorithms** (FCFS, SSTF, SCAN, C-SCAN) to minimize head movement and improve disk I/O performance.
- The OS handles **disk management** tasks like formatting and booting.
- **RAID** combines multiple disks to improve performance, provide redundancy, or both.
- **SSDs** offer fast, consistent access times but require special management techniques like **wear leveling** due to their limited write cycles.
- Efficient management of mass storage is a fundamental responsibility of the OS to ensure system stability and performance.
