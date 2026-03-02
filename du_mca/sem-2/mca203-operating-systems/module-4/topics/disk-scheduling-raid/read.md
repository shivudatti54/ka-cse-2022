# Disk Scheduling & RAID

## Introduction
Modern computing systems rely heavily on efficient storage management. Disk scheduling algorithms and RAID (Redundant Array of Independent Disks) technologies form the backbone of storage system optimization in operating systems. 

Disk scheduling addresses the mechanical limitations of hard drives by optimizing the order of I/O requests to minimize seek time and rotational latency. With storage demands growing exponentially, effective scheduling can mean the difference between a responsive system and one plagued by I/O bottlenecks.

RAID technologies provide fault tolerance and performance improvements through data distribution across multiple disks. From enterprise databases to cloud storage systems, RAID implementations ensure data availability while improving read/write speeds. Understanding these concepts is critical for designing robust storage solutions in real-world scenarios like database management systems, video streaming platforms, and financial transaction processing.

## Key Concepts

**Disk Scheduling Algorithms:**
1. **FCFS (First-Come, First-Served):** Processes requests in arrival order. Simple but inefficient for large workloads.
2. **SSTF (Shortest Seek Time First):** Selects nearest track request. Reduces seek time but risks starvation.
3. **SCAN (Elevator Algorithm):** Moves back-and-forth across disk platters. Provides fair service.
4. **C-SCAN (Circular SCAN):** Services requests in one direction only. Reduces variance in wait time.
5. **LOOK/C-LOOK:** Improved versions that reverse direction only when needed.

**RAID Levels:**
- **RAID 0:** Striping without parity (high performance, no redundancy)
- **RAID 1:** Mirroring (100% redundancy)
- **RAID 5:** Block-level striping with distributed parity
- **RAID 6:** Dual parity for two-disk failure tolerance
- **RAID 10:** Nested combination of mirroring and striping

## Examples

**Example 1: SSTF Scheduling**
Request Queue: 98, 183, 37, 122, 14, 124, 65, 67  
Initial Head Position: 53  
Solution:
1. Calculate absolute differences: |53-14|=39, |53-37|=16, etc.
2. Select smallest difference (37 → 16)
3. Repeat until all requests served
Total Seek Time: 236 cylinders

**Example 2: RAID 5 Capacity Calculation**
Given 4 disks of 1TB each:
Usable Capacity = (n-1) * disk_size = 3 * 1TB = 3TB

**Example 3: SCAN Algorithm**
Request Queue: 38, 180, 98, 15, 122, 64  
Initial Head Position: 50 (moving towards higher tracks)
Service Order: 50 → 64 → 98 → 122 → 180 → 199 (end) → 38 → 15

## Exam Tips
1. Always draw head movement diagrams for scheduling problems
2. RAID 5 requires minimum 3 disks; RAID 6 needs 4 disks
3. SSTF can be tricked into starvation - mention this limitation
4. For numericals, track direction changes in SCAN/LOOK algorithms
5. RAID 10 combines mirroring (RAID 1) and striping (RAID 0)
6. Remember C-SCAN's "circular" property vs regular SCAN
7. Write-time penalty in RAID 5/6 due to parity calculations

Length: 2100 words, MCA (Master of Computer Applications) PG level