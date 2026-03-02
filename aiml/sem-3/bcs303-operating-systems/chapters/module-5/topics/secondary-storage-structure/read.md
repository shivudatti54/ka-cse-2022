# Secondary Storage Structure

## Introduction

Secondary storage refers to non-volatile storage devices that retain data even when the computer is powered off. While primary storage (RAM) provides fast access to data, it is volatile and expensive, making it unsuitable for permanent data retention. Secondary storage devices, primarily magnetic disks (hard disk drives) and solid-state drives, form the backbone of modern computer systems by providing persistent storage for operating systems, applications, and user data.

In the context of operating systems, understanding secondary storage structure is crucial for File System implementation and management. The Operating System must efficiently manage disk I/O operations, allocate space to files, schedule disk accesses to minimize seek time, and ensure data integrity. For University of Delhi students preparing for semester examinations, a thorough understanding of disk organization, scheduling algorithms, and storage management techniques is essential, as this topic frequently appears in both theoretical and practical components of the examination.

## Key Concepts

### Physical Disk Structure

A hard disk drive consists of one or more rotating platters coated with magnetic material. Each platter has concentric circles called tracks, and each track is divided into sectors. The collection of tracks at a given radius across all platters forms a cylinder. The basic unit of data transfer is the sector, typically holding 512 bytes or 4096 bytes in modern drives.

The disk geometry is defined by parameters: number of cylinders (C), number of heads (H), and number of sectors per track (S). This is often referred to as CHS addressing. Modern disks use Logical Block Addressing (LBA), which presents the disk as a linear array of sectors numbered from 0 to N-1, abstracting the physical geometry from the operating system.

The time required to access a sector comprises three components: seek time (time to move the read/write head to the correct cylinder), rotational latency (time waiting for the desired sector to rotate under the head), and transfer time (time to read or write the data). Seek time typically dominates, making disk scheduling algorithms essential for performance.

### Disk Scheduling Algorithms

Operating systems employ various algorithms to determine the order in which disk I/O requests are serviced. The primary goal is to minimize seek time and maximize throughput.

**First-Come-First-Served (FCFS)** is the simplest algorithm that services requests in the order they arrive. While fair, it provides no optimization for seek time. Consider a disk queue with requests at tracks: 98, 183, 37, 122, 14, 124, 65, 67, in that order starting from head position 53. The total head movement would be calculated by summing absolute differences between consecutive positions.

**Shortest Seek Time First (SSTF)** services the request closest to the current head position, minimizing seek distance. However, it can cause starvation for requests far from the current position. Using the same example with head at 53, SSTF would first service track 65 (distance 12), then 67, then 37, and so on, resulting in much shorter total head movement than FCFS.

**SCAN Algorithm**, also known as the elevator algorithm, moves the head from one end of the disk to the other, servicing all requests along the way, then reverses direction. This algorithm provides more uniform wait times and better throughput than SSTF. The head moves in one direction servicing all requests until it reaches the end, then sweeps back servicing remaining requests.

**C-SCAN (Circular SCAN)** is a variant that treats the disk as a circular buffer. The head sweeps from one end to the other servicing requests, then quickly returns to the beginning without servicing any requests on the return trip. This provides more uniform wait times than SCAN.

**LOOK Algorithm** is similar to SCAN but only moves as far as the last request in each direction, rather than going to the end of the disk. This optimization reduces unnecessary head movement and improves efficiency.

### RAID (Redundant Array of Independent Disks)

RAID is a technology that combines multiple physical disk drives into a single logical unit for improved performance, reliability, or both. Different RAID levels offer various trade-offs between performance, capacity, and fault tolerance.

**RAID Level 0 (Striping)** distributes data across multiple disks without parity or mirroring. It provides excellent performance but no redundancy; a single disk failure results in complete data loss. Minimum two disks are required.

**RAID Level 1 (Mirroring)** duplicates data across two or more disks, providing complete redundancy. Read performance improves as data can be read from any mirror, but write performance is limited by the slowest disk. Capacity utilization is only 50% with two disks.

**RAID Level 5** uses block-level striping with distributed parity. Data and parity are distributed across all disks, providing fault tolerance with minimal overhead. It can tolerate one disk failure and requires a minimum of three disks. RAID 5 offers good read performance and acceptable write performance.

**RAID Level 6** extends RAID 5 by adding a second parity block, allowing the array to tolerate two simultaneous disk failures. This is essential for large-capacity storage systems where rebuild times are long.

**RAID Level 0+1** combines striping and mirroring, providing both performance and redundancy. It stripes across mirrored pairs, offering fast performance with good protection against single disk failures.

### Swap Space Management

Swap space is a reserved portion of disk used as an extension of physical memory (RAM). When physical memory is full, the operating system moves less frequently used pages to swap space (a process called paging), freeing RAM for more active processes.

Swap space can be located either as a dedicated partition or as a file within the regular file system. Dedicated partitions offer better performance as they avoid file system overhead, while file-based swap is more flexible as it can be resized without repartitioning.

The size of swap space depends on the system's workload. A common guideline suggests swap space equal to 2-4 times the physical RAM for systems with less than 2GB, and equal to RAM size for systems with more memory. However, modern systems with large RAM may require minimal swap space.

### Disk Reliability and Performance

Disk performance is measured by several metrics: throughput (data transferred per second), access latency (time from request to data arrival), and I/O operations per second (IOPS). Solid-state drives (SSDs) have largely eliminated mechanical delays, providing much lower latencies and higher IOPS than traditional hard disks.

Disk reliability is measured by Mean Time Between Failures (MTBF), indicating the average time a disk operates before failure. Enterprise-grade disks offer MTBF ratings of 1-2 million hours, while consumer-grade disks typically have lower ratings.

## Examples

### Example 1: FCFS vs SSTF Disk Scheduling

Given a disk with 200 tracks (0-199) and a read/write head initially at track 53, calculate the total head movement for the request queue: 98, 183, 37, 122, 14, 124, 65, 67 using FCFS and SSTF algorithms.

**FCFS Calculation:**
Starting at track 53:
- 53 → 98 = 45
- 98 → 183 = 85
- 183 → 37 = 146
- 37 → 122 = 85
- 122 → 14 = 108
- 14 → 124 = 110
- 124 → 65 = 59
- 65 → 67 = 2
Total head movement = 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 tracks

**SSTF Calculation:**
Starting at track 53, service nearest request first:
- 53 → 65 = 12 (service 65)
- 65 → 67 = 2 (service 67)
- 67 → 37 = 30 (service 37)
- 37 → 14 = 23 (service 14)
- 14 → 98 = 84 (service 98)
- 98 → 122 = 24 (service 122)
- 122 → 124 = 2 (service 124)
- 124 → 183 = 59 (service 183)
Total head movement = 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 tracks

SSTF reduces head movement by 404 tracks (63% improvement) compared to FCFS.

### Example 2: RAID Level Selection

An organization needs to store 4TB of data with the following requirements: fast read performance, ability to tolerate one disk failure, and cost efficiency. Evaluate RAID 1, RAID 5, and RAID 0+1.

**RAID 1 (Mirroring):**
- Usable capacity: 4TB (requires 8TB total with 2 disks)
- Read performance: Excellent (reads from both mirrors)
- Fault tolerance: 1 disk failure per mirror set
- Cost per GB: High (50% overhead)

**RAID 5:**
- Usable capacity: 4TB (requires 5TB total with 4+1 parity)
- Read performance: Excellent (striping across disks)
- Write performance: Moderate (parity calculation overhead)
- Fault tolerance: 1 disk failure
- Cost per GB: Moderate

**RAID 0+1:**
- Usable capacity: 4TB (requires 8TB total)
- Read performance: Excellent
- Write performance: Excellent
- Fault tolerance: 1 disk failure (in each mirror set)
- Cost per GB: High (50% overhead)

Recommendation: RAID 5 offers the best balance of capacity efficiency, fault tolerance, and cost for this scenario.

### Example 3: Swap Space Calculation

A system has 16GB of RAM and runs a mixture of server applications. Calculate appropriate swap space using the standard guidelines.

For systems with RAM greater than 2GB, the recommended formula is: Swap = RAM (for moderate workloads) or Swap = 2 × RAM (for heavy workloads).

**Minimum swap (equal to RAM):**
16GB RAM → 16GB swap space

**Maximum swap (2× RAM):**
16GB RAM → 32GB swap space

**Recommended configuration:**
- Minimum swap: 16GB
- Maximum swap: 32GB
- Actual allocated: 24GB (1.5× RAM for server workload)

This provides a safety net for memory-intensive operations while not wasting excessive disk space.

## Exam Tips

1. Understand the difference between seek time, rotational latency, and transfer time in disk I/O operations. Seek time typically dominates and is the primary target for scheduling algorithms.

2. For numerical problems involving disk scheduling, always calculate the total head movement by summing absolute differences between consecutive track positions. Show all steps for full marks.

3. Remember that SSTF can cause starvation for requests far from the current head position, while SCAN and C-SCAN provide more fair service to all requests.

4. Know the key differences between SCAN and C-SCAN: SCAN services requests in both directions while C-SCAN returns to the beginning without servicing requests (creating a circular pattern).

5. RAID levels are frequently tested: RAID 0 (striping, no redundancy), RAID 1 (mirroring, 50% capacity), RAID 5 (distributed parity, minimum 3 disks), and RAID 6 (dual parity).

6. Swap space management is essential for virtual memory implementation. Understand when paging occurs and how swap space size affects system performance.

7. In comparative questions, highlight trade-offs: FCFS is simple but inefficient, SSTF is efficient but can cause starvation, SCAN provides good throughput with fair wait times.

8. Solid-state drives (SSDs) have different performance characteristics than magnetic disks. They have no seek time or rotational latency, making traditional disk scheduling algorithms irrelevant for SSDs.

9. The formula for average rotational latency is (1/2) × (60 seconds / rotational speed in RPM), representing half a rotation on average.

10. Understand the relationship between disk geometry (cylinders, heads, sectors) and LBA (Logical Block Addressing) in modern storage systems.