# Mass Storage Systems: Magnetic Disks and Solid State Drives

## Introduction

In the hierarchy of computer storage, mass storage devices occupy a crucial position as the primary form of secondary storage. While primary memory (RAM) provides fast access to data, it is volatile and limited in capacity. Mass storage systems provide persistent, high-capacity storage essential for any computing system. Understanding the architecture, performance characteristics, and operational principles of magnetic disks (Hard Disk Drives - HDDs) and Solid State Drives (SSDs) is fundamental for any computer science student, particularly in the context of operating systems where storage management plays a pivotal role in system performance.

The University of Delhi's Computer Science curriculum emphasizes this topic because storage systems directly impact operating system design decisions, file system implementation, and overall system performance. In modern computing environments, both HDDs and SSDs coexist, each serving different use cases based on their distinct performance profiles and cost characteristics. This chapter explores the internal workings, performance metrics, scheduling algorithms, and comparative analysis of these storage technologies.

## Key Concepts

### Magnetic Disk Structure and Organization

A magnetic disk consists of one or more circular platters coated with magnetic material, stacked on a central spindle. Each platter has two surfaces, and each surface is divided into concentric circles called **tracks**. Tracks are further subdivided into **sectors**, which are the smallest addressable units on a disk (typically 512 bytes or 4096 bytes in modern disks). The collection of tracks at the same radius across all surfaces forms a **cylinder**.

The disk controller interfaces with the operating system through several key parameters:
- **Cylinders (C)**: Number of tracks per surface
- **Heads (H)**: Number of read/write heads (typically equals number of surfaces)
- **Sectors per track (S)**: Variable depending on zone bit recording
- **Capacity**: C × H × S × sector size

Modern disks use **Zone Bit Recording (ZBR)**, where outer zones have more sectors per track than inner zones, maximizing storage capacity. The total capacity is calculated as: **Capacity = C × H × S × sector_size**

### Disk Access Time Components

The time to access data on a magnetic disk comprises several components:

1. **Seek Time (T_seek)**: Time to move the read/write head to the correct cylinder. This is typically 3-12 milliseconds for modern drives. Average seek time is approximately one-third of the full stroke seek time.

2. **Rotational Latency (T_rot)**: Time waiting for the desired sector to rotate under the head. For a disk rotating at R RPM, average rotational latency = (1/2) × (60/R) seconds = (30/R) milliseconds.

3. **Transfer Time (T_trans)**: Time to actually read/write the data. T_trans = (bytes to transfer) / (transfer rate)

4. **Controller Time (T_ctrl)**: Overhead for controller processing, typically 0.1-0.2 ms.

**Total Access Time = T_seek + T_rot + T_trans + T_ctrl**

### Disk Scheduling Algorithms

Operating systems employ various scheduling algorithms to minimize disk access time:

**FCFS (First Come First Served)**: Processes requests in order of arrival. Simple but often inefficient.

**SSTF (Shortest Seek Time First)**: Selects the request closest to the current head position. Improves throughput but may cause starvation.

**SCAN Algorithm**: The head moves from one end to the other, servicing all requests along the way, then reverses direction. Also known as the "elevator algorithm."

**C-SCAN (Circular SCAN)**: Similar to SCAN but returns to the beginning without servicing requests on the return trip, providing more uniform wait times.

**LOOK Algorithm**: Similar to SCAN but only goes as far as the last request in each direction, not to the end of the disk.

### Solid State Drives (SSDs)

SSDs represent a paradigm shift in storage technology, using flash memory chips instead of magnetic media. Key components include:

**NAND Flash Memory**: The fundamental storage medium, organized in arrays of memory cells. Types include:
- **SLC (Single-Level Cell)**: 1 bit per cell, fastest and most durable
- **MLC (Multi-Level Cell)**: 2 bits per cell, balanced performance
- **TLC (Triple-Level Cell)**: 3 bits per cell, higher capacity, lower endurance
- **QLC (Quad-Level Cell)**: 4 bits per cell, highest capacity, lowest endurance

**SSD Architecture**: SSDs consist of multiple NAND flash packages, a controller, and DRAM cache. Data is stored in **pages** (typically 4KB), which are grouped into **blocks** (typically 256-512 pages). Pages can be read or written individually, but blocks must be erased before being written to again.

**Key SSD Concepts**:
- **Wear Leveling**: Distributes write cycles across the entire drive to prevent early failure of specific cells
- **Garbage Collection**: Reclaims space by moving valid data and erasing invalidated blocks
- **TRIM Command**: Allows the OS to inform the SSD which data is no longer in use
- **Over-provisioning**: Reserved space for wear leveling and garbage collection operations

### SSD vs HDD Performance Characteristics

| Characteristic | HDD | SSD |
|----------------|-----|-----|
| Access Time | 5-10 ms | 0.1 ms |
| Sequential Read | 100-200 MB/s | 500-3500 MB/s |
| Sequential Write | 100-150 MB/s | 400-3000 MB/s |
| Random Read IOPS | ~100 IOPS | 10,000-100,000+ IOPS |
| Random Write IOPS | ~100 IOPS | 10,000-50,000 IOPS |
| Power Consumption | 5-10W | 2-5W |
| Latency | High | Very Low |
| Fragmentation Impact | Significant | Minimal |
| Price per GB | Lower | Higher |

### RAID (Redundant Array of Independent Disks)

RAID is a technology combining multiple physical disks into logical units for improved performance, reliability, or both:

- **RAID 0 (Striping)**: Distributes data across multiple disks for performance, no redundancy
- **RAID 1 (Mirroring)**: Duplicates data on two or more disks for redundancy
- **RAID 5**: Striping with distributed parity, allows one disk failure
- **RAID 6**: Double parity, allows two disk failures
- **RAID 10**: Combination of RAID 1 and RAID 0

## Examples

### Example 1: Calculating Disk Access Time

**Problem**: A disk has the following specifications:
- Average seek time: 8 ms
- Rotational speed: 7200 RPM
- Transfer rate: 60 MB/s
- Sector size: 512 bytes
- Read 64 KB of data from a random sector

**Solution**:

Step 1: Calculate average rotational latency
- Rotational latency = (1/2) × (60/7200) = 1/2 × 0.00833 = 0.00417 seconds = 4.17 ms

Step 2: Calculate transfer time
- Data to transfer = 64 KB = 64 × 1024 = 65,536 bytes
- Transfer time = 65,536 bytes / (60 × 10^6 bytes/s) = 0.00109 seconds = 1.09 ms

Step 3: Total access time
- Total = Seek time + Rotational latency + Transfer time
- Total = 8 ms + 4.17 ms + 1.09 ms = **13.26 ms**

### Example 2: Disk Scheduling with SSTF

**Problem**: Given a disk with 200 cylinders (0-199), the head is currently at cylinder 53, and the pending requests in order of arrival are: 98, 183, 37, 122, 14, 124, 65, 67. Using SSTF algorithm, determine the head movement sequence and total head travel.

**Solution**:

Starting position: cylinder 53

1. Find closest request to 53:
   - |53-37| = 16, |53-65| = 12, |53-67| = 14, |53-98| = 45, |53-122| = 69, |53-124| = 71, |53-14| = 39, |53-183| = 130
   - **Closest: 65** (distance 12)

2. From 65, find next closest:
   - |65-67| = 2, |65-37| = 28, |65-98| = 33, |65-122| = 57, |65-124| = 59, |65-14| = 51, |65-183| = 118
   - **Next: 67** (distance 2)

3. Continue this process:
   - 67 → 37 (distance 30)
   - 37 → 14 (distance 23)
   - 14 → 98 (distance 84)
   - 98 → 122 (distance 24)
   - 122 → 124 (distance 2)
   - 124 → 183 (distance 59)

**Head movement sequence**: 53 → 65 → 37 → 14 → 98 → 122 → 124 → 183

**Total head travel**: |65-53| + |67-65| + |37-67| + |14-37| + |98-14| + |122-98| + |124-122| + |183-124|
= 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = **236 cylinders**

### Example 3: SSD Wear Leveling Calculation

**Problem**: An SSD has 1000 write cycles per block endurance rating and uses a wear leveling algorithm. If a user writes 100 GB of data daily to a 500 GB SSD, estimate the minimum expected lifespan assuming worst-case wear.

**Solution**:

Step 1: Calculate daily write amplification
- Assuming typical write amplification factor of 3x due to garbage collection
- Actual writes to NAND = 100 GB × 3 = 300 GB/day

Step 2: Calculate total bytes written per cycle
- Total SSD capacity = 500 GB = 500,000 MB
- With typical over-provisioning of 7% (actual usable ~465 GB)
- Assume 400 GB of over-provisioned space for calculations

Step 3: Calculate days to reach endurance
- This depends on which blocks wear out first
- With wear leveling evenly distributing writes:
- If the SSD has 1000 blocks (simplified), and each block handles:
- Days = (1000 cycles × 400 GB) / (300 GB/day) = 1333 days ≈ **3.65 years**

In reality, modern SSDs with good wear leveling typically last 5-10 years under normal consumer usage.

## Exam Tips

1. **Remember the disk access time formula**: Total access time = Seek time + Rotational latency + Transfer time + Controller overhead. This is frequently tested in DU exams.

2. **Understand SCAN vs C-SCAN**: SCAN provides lower average wait time but C-SCAN provides more uniform wait times. Know when to apply each.

3. **SSD characteristics are increasingly important**: With SSDs becoming standard, understand why they have no seek time and minimal rotational latency.

4. **RAID levels and their purposes**: Be clear on RAID 0 (performance), RAID 1 (redundancy), RAID 5 (balanced), and RAID 6 (high redundancy).

5. **Disk capacity calculation**: Practice C × H × S × sector_size calculations; this is a common numerical problem.

6. **Difference between random and sequential access**: HDDs excel at sequential access due to caching and read-ahead, while SSDs maintain consistent performance.

7. **TRIM command significance**: Understand how TRIM improves SSD performance and longevity by allowing the drive to proactively erase deleted data.

8. **FCFS is always optimal for small loads**: In theory, FCFS provides fair scheduling but at the cost of performance. Know when each algorithm is preferred.