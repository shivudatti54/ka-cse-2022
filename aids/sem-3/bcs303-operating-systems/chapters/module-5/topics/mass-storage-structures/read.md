# Mass Storage Structures

## Introduction

For an Engineering student, understanding how an Operating System (OS) manages the vast amounts of data stored on hard disks, SSDs, and other secondary storage devices is crucial. This area of study, known as **Mass Storage Structures**, deals with the disk hardware, the algorithms the OS uses to manage it, and the services it provides for storing and retrieving data efficiently. The performance of the entire computer system is often hinged on the speed and efficiency of its disk subsystem.

## Core Concepts

### 1. Disk Structure and Scheduling

Modern hard disk drives (HDDs) are composed of multiple **platters** coated with magnetic material. Data is read and written by a **disk head** moving over concentric circles called **tracks**. Each track is divided into **sectors** (typically 512 bytes or 4KB), the smallest unit of data transfer.

The time to access data on a disk is determined by:
*   **Seek Time:** Time to move the disk arm to the correct cylinder.
*   **Rotational Latency:** Time for the desired sector to rotate under the disk head.
*   **Transfer Time:** Time to actually read or write the data.

To minimize access time, the OS employs **Disk Scheduling Algorithms**. Common algorithms include:
*   **First-Come, First-Served (FCFS):** Simple but often inefficient.
*   **Shortest Seek Time First (SSTF):** Services the request closest to the current head position. Can lead to starvation for distant requests.
*   **SCAN (Elevator Algorithm):** The disk arm moves from one end of the disk to the other, servicing requests along the way. It then reverses direction.
*   **C-SCAN (Circular SCAN):** A variant that treats the cylinders as a circular list, providing more uniform wait times.

**Example:** With a current head at cylinder 53 and a queue of requests: 98, 183, 37, 122, 14, 124, 65, 67.
*   **FCFS Order:** 53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67 (Total head movement: 640 cylinders).
*   **SSTF Order:** 53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183 (Total head movement: 236 cylinders). SSTF is significantly more efficient.

### 2. Disk Management

The OS is responsible for several disk management tasks:
*   **Formatting (Low-Level):** Dividing the disk into sectors that the disk controller can read and write.
*   **Partitioning:** Dividing the disk into one or more groups of cylinders, treated as a separate storage device.
*   **Logical Formatting (High-Level):** Creating a file system on the partition (e.g., creating a FAT table or inode structures).
*   **Boot Block:** A small program stored in a fixed location on the disk (the **boot sector**) is loaded into memory at startup to bootstrap the OS.

### 3. RAID Structure

**Redundant Array of Independent Disks (RAID)** is a technology that uses multiple physical disk drives to create a single logical unit for the purpose of data **redundancy**, **increased performance**, or both.

Common RAID Levels:
*   **RAID 0 (Striping):** Data is split across disks. Improves performance but offers no redundancy.
*   **RAID 1 (Mirroring):** Creates an exact copy (mirror) of data on two disks. Provides fault tolerance.
*   **RAID 5 (Block-Level Striping with Distributed Parity):** Data and parity information are striped across three or more disks. Offers a good balance of performance, capacity, and redundancy.

### 4. Swap-Space Management

**Swap-space** is an area on a disk used as an extension of main memory. When physical RAM is full, the OS can **swap out** (move) pages of memory to this disk space to free up RAM for active processes. This is a critical part of virtual memory management. The swap-space can be a dedicated partition (faster) or a special file within the main file system.

## Key Points / Summary

| Concept | Description |
| :--- | :--- |
| **Goal** | To manage secondary storage devices for **efficiency**, **reliability**, and **performance**. |
| **Disk Scheduling** | Algorithms like SSTF, SCAN, and C-SCAN minimize **seek time** and **total head movement**. |
| **Disk Management** | Involves **formatting**, **partitioning**, and creating a **boot block** to prepare the disk for use. |
| **RAID** | Uses multiple disks for **redundancy** (e.g., RAID 1, 5) and/or **performance** (e.g., RAID 0). |
| **Swap-Space** | Extends virtual memory onto the disk, allowing systems to run larger applications than physical RAM alone would allow. |
| **Importance** | The efficiency of mass storage management directly impacts overall system performance and data integrity. |