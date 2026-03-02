# Secondary Storage Structure

## Introduction

Secondary storage refers to non-volatile memory devices that provide permanent data storage for computer systems. While primary storage (RAM) offers lightning-fast access speeds, it comes with a critical limitation: data is lost when power is turned off. This is where secondary storage becomes indispensable in computing architecture. The most common form of secondary storage in traditional computing systems is the magnetic disk, commonly known as the Hard Disk Drive (HDD), though solid-state drives (SSDs) have gained significant prominence in modern systems.

For operating systems, understanding secondary storage structure is fundamental because file systems are built upon these storage devices. The Operating System must efficiently manage the physical characteristics of storage devices, provide reliable data access mechanisms, and optimize performance through intelligent scheduling algorithms. Whether you are accessing a document, running an application, or storing multimedia files, the underlying secondary storage structure determines how quickly and reliably your system responds. In the University of Delhi computer science curriculum, this topic forms a critical component of understanding how operating systems bridge the gap between applications and physical hardware.

The study of secondary storage structure encompasses disk geometry, physical organization, access mechanisms, and performance optimization techniques. These concepts are essential for system administrators, database engineers, and software developers who need to design applications that efficiently utilize storage resources. With the exponential growth of data in modern computing, understanding these underlying principles has become more important than ever.

## Key Concepts

### Physical Disk Structure

A magnetic disk consists of one or more circular platters coated with magnetic material. Each platter has two surfaces, and each surface is divided into concentric circles called tracks. Tracks are further subdivided into sectors, which represent the smallest addressable unit on a disk. The collection of tracks at a given radius across all surfaces forms a cylinder. This three-dimensional organization (surface, track, sector) is fundamental to understanding how data is stored and accessed on magnetic disks.

Modern disks use Zone Bit Recording (ZBR), where outer zones have more sectors per track than inner zones, maximizing storage capacity. Traditional disks used Constant Linear Velocity (CLV) where sector density was uniform, but current implementations typically use a combination approaches for optimal performance. The disk spins at constant speeds, typically 5400, 7200, or 15000 RPM in enterprise systems, with rotational latency directly proportional to angular velocity.

The disk controller interfaces between the operating system and the physical disk hardware. It handles error detection and correction, manages cache buffers, and translates logical block addresses (LBAs) to physical cylinder-head-sector (CHS) coordinates. Modern disks perform extensive remapping of defective sectors to spare areas, making the actual physical organization transparent to the operating system.

### Disk Access Time

The total time to access data on a disk consists of three components. **Seek time** is the time required to move the disk arm to the correct cylinder, typically ranging from 3 to 12 milliseconds for modern drives. **Rotational latency** is the time waiting for the desired sector to rotate under the read-write head, averaging half the time for one complete rotation. **Transfer time** is the actual time to read or write data, dependent on the transfer rate and the amount of data.

Average access time can be calculated as: T_average = T_seek + (1/2 × T_rotation) + (N_bytes / Transfer_rate)

Understanding these components is crucial because they reveal where performance bottlenecks occur. Seek time typically dominates in random access patterns, while transfer time becomes significant for sequential access. Operating systems employ various optimization strategies based on these characteristics.

### Disk Scheduling Algorithms

Given that disk I/O requests arrive asynchronously from multiple processes, the order in which they are serviced significantly impacts system performance. Disk scheduling algorithms aim to minimize total seek time, reduce rotational latency, and ensure fair access.

**First-Come-First-Served (FCFS)** is the simplest algorithm, servicing requests in the order they arrive. While fair, it performs poorly when requests are scattered across the disk as it results in excessive arm movement.

**Shortest Seek Time First (SSTF)** selects the request closest to the current head position, minimizing seek distance. This algorithm significantly outperforms FCFS but can cause starvation for requests at distant locations.

**SCAN algorithm**, also known as the elevator algorithm, moves the disk arm from one end to the other, servicing all requests along the path, then reverses direction. This approach provides good response time and avoids starvation. The C-SCAN variant services requests in a circular manner, providing more uniform wait times.

**LOOK** is a modified version of SCAN that only goes as far as the last request in each direction, avoiding unnecessary travel to the disk edges. Most modern operating systems implement some variant of LOOK or C-LOOK for optimal performance.

### Disk Cache and Buffering

Disk caches are memory buffers that store frequently accessed data and metadata. Modern disks incorporate significant DRAM caches (ranging from 8MB to 256MB) that dramatically improve read performance by serving requests from memory rather than performing physical disk operations.

Write operations can be handled in different ways. **Write-through** writes data to both cache and disk immediately, ensuring data integrity but adding latency. **Write-back** writes data to cache first and defers disk writes, improving performance but risking data loss in case of power failure. Most systems use write-back with battery backup for critical applications.

The operating system may also maintain its own buffer cache in main memory, providing an additional layer of caching between applications and the disk controller cache.

### RAID (Redundant Array of Independent Disks)

RAID technology combines multiple physical disks into a logical unit for improved performance, reliability, or both. RAID levels are numbered and each provides different trade-offs.

**RAID 0** (striping) distributes data across multiple disks without redundancy, improving performance but offering no fault tolerance. **RAID 1** (mirroring) duplicates data on paired disks, providing excellent reliability at double the storage cost. **RAID 5** distributes data and parity information across all disks, providing fault tolerance with efficient storage utilization. **RAID 6** extends RAID 5 with double parity, tolerating two disk failures. **RAID 10** combines striping and mirroring for both performance and reliability.

Enterprise storage systems often use nested RAID configurations like RAID 60 or RAID 51 to achieve specific performance and reliability goals. The choice of RAID level depends on the application requirements, budget constraints, and performance expectations.

## Examples

### Example 1: Calculating Average Disk Access Time

Consider a disk with the following specifications: average seek time of 8ms, rotational speed of 7200 RPM, and a transfer rate of 80 MB/s. Calculate the average time to read a single 4KB sector.

**Solution:**

First, convert rotational speed to rotational latency: 7200 RPM means 7200 rotations per minute, or 120 rotations per second. Time per rotation = 1/120 seconds = 8.33 milliseconds. Average rotational latency = 8.33 / 2 = 4.17 ms.

Next, calculate transfer time: Transfer rate = 80 MB/s = 80 × 1024 KB/s = 81920 KB/s. For a 4KB sector: Transfer time = 4 / 81920 = 0.0000488 seconds = 0.0488 ms.

Average access time = Seek time + Rotational latency + Transfer time = 8 + 4.17 + 0.049 = 12.22 ms.

This calculation demonstrates that for small random reads, seek time and rotational latency dominate the access time, while transfer time is relatively insignificant.

### Example 2: SCAN Algorithm Illustration

A disk queue contains requests for cylinders (in order of arrival): 45, 12, 67, 38, 52, 19, 7, 61. The disk head is currently at cylinder 40 and moving toward higher cylinder numbers. Using the SCAN algorithm, determine the service order.

**Solution:**

With SCAN, the head moves in one direction servicing all requests until reaching the end, then reverses.

Current position: 40, direction: increasing

Requests above 40: 45, 52, 61, 67
Requests below 40: 38, 19, 12, 7

Service order: 45 → 52 → 61 → 67 (reach end) → 38 → 19 → 12 → 7

Total head movement: |45-40| + |52-45| + |61-52| + |67-61| + |67-38| + |38-19| + |19-12| + |12-7| = 5 + 7 + 9 + 6 + 29 + 19 + 7 + 5 = 87 cylinders

This example shows how SCAN eliminates the random movement seen in FCFS, resulting in more efficient disk access.

### Example 3: RAID Level Selection

An organization needs to store 10 TB of critical database files that require high performance for reads and must survive any single disk failure without data loss. Evaluate RAID 5 versus RAID 10.

**Solution:**

For RAID 5: The array requires N+1 disks where N stores data and 1 stores parity. To store 10 TB with 4 TB disks, we need ceil(10/4) = 3 data disks minimum, plus 1 parity disk = 4 disks total. Actual capacity: (4-1) × 4 TB = 12 TB, with 2 TB unused. Performance: Good read performance (data striped across 3 disks), write performance impacted by parity calculation overhead. Fault tolerance: 1 disk failure.

For RAID 10: This requires mirroring (RAID 1) combined with striping (RAID 0). We need pairs of disks for mirroring. To store 10 TB: minimum 6 disks (3 pairs) giving 12 TB usable. Performance: Excellent both reads and writes (striped mirrors). Fault tolerance: Up to 1 disk failure per mirrored pair (so 3 failures possible if they occur in different pairs).

Recommendation: For a critical database with high read performance requirements and need for maximum fault tolerance, RAID 10 is preferred despite higher cost. The write performance overhead of RAID 5 can be problematic for database workloads with frequent updates.

## Exam Tips

1. **Memorize the disk access time formula**: Average Access Time = Average Seek Time + (1/2 × Rotational Latency) + Transfer Time. This formula is frequently tested in DU examinations.

2. **Understand SCAN vs C-SCAN difference**: SCAN services requests in both directions like an elevator, while C-SCAN returns to the beginning quickly and services in only one direction, providing more uniform wait times.

3. **RAID levels and their characteristics**: Remember that RAID 0 provides no redundancy, RAID 1 provides mirroring, RAID 5 uses distributed parity, and RAID 6 uses double parity. Know the fault tolerance capability of each.

4. **Convert RPM to latency**: Remember that 7200 RPM means 120 rotations per second, so one rotation takes 8.33ms, and average rotational latency is half of this (4.17ms).

5. **SSTF vs FCFS**: In comparative questions, note that SSTF reduces average seek distance but can cause starvation, while FCFS is fair but inefficient.

6. **Cylinder concept**: A cylinder refers to all tracks at the same radius across all surfaces. Accessing data within the same cylinder requires no seek movement, only rotational latency.

7. **Buffer cache purposes**: The OS buffer cache serves three main purposes: caching frequently accessed data, buffering writes for batch processing, and providing a copy for applications to modify without affecting the disk.

8. **Real-world context**: DU exams often include application-based questions. Relate concepts to practical scenarios like database systems requiring RAID, or video streaming requiring sequential access optimization.

9. **Time calculation practice**: Be thorough with numerical problems involving disk scheduling and access time calculations. Show all steps as marks are awarded for procedure.

10. **Understand why SSDs change everything**: While HDDs are the primary focus, understanding that SSDs eliminate seek time and rotational latency entirely explains the dramatic performance improvements in modern systems.