# Disk Attachment


## Table of Contents

- [Disk Attachment](#disk-attachment)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Disk Interface Standards](#disk-interface-standards)
  - [Disk Controller Architecture](#disk-controller-architecture)
  - [I/O Control Methods](#io-control-methods)
  - [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
  - [Buffering and Caching](#buffering-and-caching)
- [Examples](#examples)
  - [Example 1: Calculating Disk Access Time](#example-1-calculating-disk-access-time)
  - [Example 2: SCAN Algorithm Demonstration](#example-2-scan-algorithm-demonstration)
  - [Example 3: Buffer Cache Hit Rate Analysis](#example-3-buffer-cache-hit-rate-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Disk attachment is a fundamental concept in operating systems that deals with how secondary storage devices are physically and logically connected to a computer system. In modern computing environments, the operating system must manage various types of storage devices with different attachment interfaces, transfer rates, and performance characteristics. Understanding disk attachment mechanisms is crucial for system administrators, software developers, and computer science professionals who need to optimize storage performance and ensure reliable data access.

The evolution of disk attachment technologies has significantly impacted operating system design and file system implementation. From the early days of floppy disk controllers to modern NVMe solid-state drives, each interface has introduced new challenges and opportunities for OS designers. The operating system must provide a unified abstraction layer that allows applications to interact with storage devices regardless of their underlying attachment method. This abstraction is achieved through device drivers, controller interfaces, and the I/O subsystem, which together form the bridge between application requests and physical disk operations.

In the context of the University of Delhi's MCA program, disk attachment encompasses both the hardware interconnection standards and the software mechanisms that enable the operating system to effectively manage disk resources. This topic connects directly to broader concepts including file systems, memory management, and process scheduling, making it essential for understanding how operating systems orchestrate complex I/O operations across multiple hardware components.

## Key Concepts

### Disk Interface Standards

The disk interface defines the communication protocol between the computer's motherboard and the storage device. Several major interface standards have dominated the history of disk attachment.

**ATA (Advanced Technology Attachment)** and its later version **SATA (Serial ATA)** represent the most common interface for consumer hard drives. ATA, also known as IDE (Integrated Drive Electronics), uses parallel data transfer and has evolved through multiple standards including ATA/ATAPI-6 and ATA/ATAPI-7. SATA introduced serial transmission, higher transfer rates, and hot-swapping capabilities. SATA versions include SATA I (1.5 Gb/s), SATA II (3.0 Gb/s), and SATA III (6.0 Gb/s), with each generation doubling the bandwidth.

**SCSI (Small Computer System Interface)** provides higher performance and greater scalability than ATA, making it popular in server environments and high-performance workstations. SCSI supports multiple devices on a single bus with unique IDs, concurrent operations, and command queuing. Modern SAS (Serial Attached SCSI) combines SCSI's reliability with SATA's serial architecture.

**NVMe (Non-Volatile Memory Express)** represents the newest standard, designed specifically for solid-state drives using PCI Express lanes. NVMe eliminates the legacy bottleneck of SATA and AHCI controllers, providing dramatically lower latency and higher throughput. NVMe drives can achieve sequential read speeds exceeding 7 GB/s, compared to approximately 600 MB/s for SATA III.

### Disk Controller Architecture

The disk controller serves as the intermediary between the CPU and the disk drive. Modern controllers integrate multiple functions including host interface communication, data buffering, error detection and correction, and drive management.

A typical disk controller contains several key components: the host interface controller manages communication with the computer's bus system; the drive interface controller handles protocol-specific communication with the disk drive itself; a buffer (typically 8-256 MB of DRAM) stores data during transfers; and error correction circuitry implements algorithms like Reed-Solomon or LDPC codes to detect and correct data corruption.

The controller presents a logical view of the disk to the operating system, abstracting physical details such as sector geometry, bad sectors, and interleaving. This abstraction allows the OS to treat the disk as a linear array of addressable blocks, regardless of the underlying physical organization.

### I/O Control Methods

Operating systems provide multiple methods for initiating and managing disk I/O operations, each with different performance and complexity characteristics.

**Programmed I/O (PIO)** involves the CPU directly reading or writing each data word to or from the disk controller. While simple to implement, PIO consumes significant CPU cycles and limits transfer rates. Modern systems rarely use PIO for disk operations.

**DMA (Direct Memory Access)** allows the disk controller to transfer data directly to or from main memory without CPU intervention. The CPU programs the DMA controller with the source address, destination address, and transfer length, then continues executing other instructions while the transfer proceeds. DMA significantly reduces CPU overhead and enables higher data transfer rates.

**Interrupt-driven I/O** combines DMA with asynchronous notification. The CPU initiates a transfer and performs other work; when the transfer completes, the disk controller raises an interrupt, alerting the OS to process the completed operation. This approach maximizes CPU utilization while maintaining reasonable programming complexity.

### Disk Scheduling Algorithms

Because disk access involves mechanical movement (seek time) and rotational delay, the order in which I/O requests are serviced dramatically affects performance. Disk scheduling algorithms attempt to minimize these delays.

**FCFS (First-Come-First-Served)** processes requests in the order they arrive, providing fair but often inefficient service. This algorithm serves as a baseline for comparing more sophisticated approaches.

**SSTF (Shortest Seek Time First)** selects the request closest to the current head position, minimizing arm movement. While generally superior to FCFS, SSTF may cause starvation for requests at the disk's extremities.

**SCAN**, also known as the elevator algorithm, moves the disk head across the entire disk in one direction, servicing all requests along the path, then reverses direction. This approach provides uniform service time across the disk and prevents starvation.

**C-SCAN (Circular SCAN)** similar to SCAN but returns to the starting position without servicing requests during the return sweep, providing more uniform response times.

**LOOK** is a variant of SCAN that only travels as far as the last request in each direction, avoiding unnecessary movement to the disk edges.

### Buffering and Caching

Operating systems employ multiple buffering strategies to bridge the speed gap between fast processors and slower disk systems.

**Buffer Cache** maintains recently accessed disk blocks in memory, allowing subsequent requests for the same data to be satisfied from RAM rather than requiring disk access. The buffer cache uses algorithms like LRU (Least Recently Used) or its variants to determine which blocks to retain when memory pressure requires eviction.

**Write-behind** defers writes to disk, accumulating multiple updates in memory before flushing to stable storage. This approach improves write performance but risks data loss if the system crashes before pending writes complete. Write-through caching writes data to both cache and disk immediately, ensuring durability at the cost of performance.

**Prefetching** anticipates future read requests based on access patterns and loads data into cache before it is explicitly requested. Sequential access patterns benefit greatly from prefetching, as the system can initiate the next disk read while processing the current block.

## Examples

### Example 1: Calculating Disk Access Time

Consider a disk with the following specifications: average seek time of 8 ms, rotational speed of 7200 RPM (revolutions per minute), and 500 sectors per track. Calculate the average time to read 2000 sequential sectors starting from an arbitrary sector.

**Solution:**

First, convert rotational speed to rotational delay. At 7200 RPM, the disk completes one rotation every (60000 ms / 7200) = 8.33 ms. Average rotational delay is half of this: 4.17 ms.

Average seek time is given as 8 ms. Since we are reading sequential sectors, after the initial seek, subsequent sectors require only rotational delay (no additional seek).

For the first sector: average access time = average seek + average rotational delay + transfer time per sector.

Transfer time per sector depends on the data rate. With 500 sectors per rotation and 8.33 ms per rotation, the transfer rate is approximately 500 sectors per 8.33 ms, or 60 sectors per ms. Therefore, transfer time per sector is approximately 0.0167 ms.

For the first sector: 8 + 4.17 + 0.0167 = 12.19 ms

For the remaining 1999 sectors: each sector requires 0.0167 ms, so total sequential transfer time = 1999 × 0.0167 = 33.37 ms

Total average access time = 12.19 + 33.37 = 45.56 ms

This example illustrates why sequential access dramatically outperforms random access on mechanical hard drives—the seek and rotational delays dominate for random access, while transfer time dominates for sequential operations.

### Example 2: SCAN Algorithm Demonstration

Assume a disk queue contains requests for tracks (in order of arrival): 45, 12, 67, 38, 52, 28, 91, 15. The disk head is currently at track 30 and moving toward increasing track numbers. Calculate the head movement using the SCAN algorithm.

**Solution:**

With SCAN, the head moves in one direction (increasing track numbers) until it reaches the end, servicing all requests along the path.

Current head position: 30, direction: increasing

Requests sorted by track number: 12, 15, 28, 38, 45, 52, 67, 91

The head moves from position 30 toward increasing track numbers:

From 30 to 38: movement = 8 (serves request at 38)
From 38 to 45: movement = 7 (serves request at 45)
From 45 to 52: movement = 7 (serves request at 52)
From 52 to 67: movement = 15 (serves request at 67)
From 67 to 91: movement = 24 (serves request at 91)

Total forward movement: 8 + 7 + 7 + 15 + 24 = 61 tracks

After reaching 91, the head would reverse and service remaining requests (12, 15, 28) on the return path. However, in the basic SCAN algorithm, we consider complete traversal:

From 91 to 0 (assuming full sweep): movement = 91
From 0 to 12: movement = 12 (serves request at 12)
From 12 to 15: movement = 3 (serves request at 15)
From 15 to 28: movement = 13 (serves request at 28)

Total return movement: 91 + 12 + 3 + 13 = 119 tracks

Total head movement: 61 + 119 = 180 tracks

The LOOK variant would stop at track 28 (the highest request in the queue) rather than going to 91, resulting in less movement.

### Example 3: Buffer Cache Hit Rate Analysis

A file server experiences 1000 read requests per second. The buffer cache has a hit ratio of 85% for read operations. Each disk I/O takes 10 ms on average, while cache hits take 0.1 ms. Calculate the average read latency and the percentage of time saved by caching.

**Solution:**

For each request:
- Cache hit time (85% of requests): 0.1 ms
- Disk access time (15% of requests): 10 ms

Average read latency = (0.85 × 0.1) + (0.15 × 10) = 0.085 + 1.5 = 1.585 ms

Without caching, all 1000 requests would require disk access:
Average latency without cache = 10 ms

Time saved per request = 10 - 1.585 = 8.415 ms
Percentage time saved = (8.415 / 10) × 100 = 84.15%

This demonstrates the dramatic impact of effective caching on system performance. Even with a relatively modest 85% hit ratio, the system achieves an 84% reduction in average read latency.

## Exam Tips

For the University of Delhi operating systems examination, candidates should focus on the following aspects of disk attachment:

1. DIFFERENTIATE between PIO, DMA, and interrupt-driven I/O in terms of CPU utilization and implementation complexity. Expect questions requiring comparison of these methods.

2. MEMORIZE THE FORMULA for average disk access time: T_avg = T_seek + T_rotational + T_transfer. Understand how each component contributes to overall latency.

3. UNDERSTAND SCAN VS. C-SCAN differences: SCAN provides more uniform service while C-SCAN provides equal wait times for all requests. Know when each algorithm is preferable.

4. KNOW THE LIMITATIONS of the SSTF algorithm—specifically the starvation problem for requests at disk extremities. This is a common examination question.

5. DISTINGUISH BETWEEN write-through and write-back caching strategies, including the trade-off between data durability and write performance. Be prepared to recommend appropriate strategies for different scenarios.

6. RECOGNIZE THAT NVMe represents a paradigm shift from legacy interfaces, eliminating controller bottlenecks inherent in SATA/AHCI architecture.

7. UNDERSTAND THE ROLE of disk controllers in abstracting physical disk geometry from the operating system. This abstraction is fundamental to how operating systems manage storage.

8. PRACTICE CALCULATING head movement for different scheduling algorithms—these problems appear frequently in examinations and require systematic solution approaches.