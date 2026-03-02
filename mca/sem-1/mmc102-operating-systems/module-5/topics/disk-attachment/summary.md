# Disk Attachment - Summary

## Key Definitions and Concepts

- DISK ATTACHMENT: The physical and logical interconnection between storage devices and the computer system, encompassing interface standards, controllers, and I/O control methods.

- DISK CONTROLLER: Hardware component that manages communication between the CPU and disk drive, providing logical abstraction over physical disk geometry.

- DMA (Direct Memory Access): I/O method allowing direct data transfer between disk and memory without CPU intervention, significantly reducing processor overhead.

- DISK SCHEDULING: Operating system algorithms that determine the order in which I/O requests are serviced to minimize seek time and rotational delay.

## Important Formulas and Theorems

- AVERAGE DISK ACCESS TIME = Average Seek Time + Average Rotational Delay + Transfer Time

- AVERAGE ROTATIONAL DELAY = (1/2) × (60 / Rotational Speed in RPM) × 1000 ms

- DISK TRANSFER TIME = (Number of Sectors / Sectors per Track) × Rotation Time

- CACHE HIT RATE IMPACT: Average Access Time = (Hit_Rate × Cache_Time) + ((1 - Hit_Rate) × Disk_Time)

## Key Points

- SATA replaced parallel ATA with serial transmission, enabling higher speeds and hot-swapping; current SATA III provides 6 Gb/s bandwidth.

- NVMe eliminates legacy bottlenecks by connecting SSDs directly to PCIe lanes, achieving latencies under 100 microseconds.

- SCAN (elevator algorithm) moves head monotonically in one direction, reversing only after reaching the end; provides good average performance with no starvation.

- C-SCAN provides uniform service times by always returning to the beginning without servicing requests during the return sweep.

- SSTF minimizes seek time but can cause starvation for requests at disk extremities.

- Buffer caching can reduce average I/O latency by orders of magnitude—the 85% hit ratio example showed 84% latency reduction.

- Write-back caching offers better performance but risks data loss; write-through ensures durability at performance cost.

## Common Mistakes to Avoid

- CONFUSING SCAN AND C-SCAN: Remember SCAN services requests in both directions while C-SCAN only services in one direction during each sweep.

- IGNORING ROTATIONAL DELAY: Many students focus only on seek time and forget that rotational latency can equal or exceed seek time on modern drives.

- MISUNDERSTANDING CACHE BEHAVIOR: Write-back does not immediately write to disk; the OS must explicitly flush caches to ensure durability.

- FORGETTING THAT DMA STILL REQUIRES CPU INITIALIZATION: Although DMA handles data transfer autonomously, the CPU must program the DMA controller before each operation.

## Revision Tips

- PRACTICE PROBLEMS: Work through multiple examples calculating disk access times and head movement for different scheduling algorithms until the process becomes automatic.

- CREATE COMPARISON TABLES: Build a table comparing disk interface generations (ATA → SATA → NVMe) with their bandwidth, latency, and typical use cases.

- MEMORIZE THE SEQUENCE: When applying SCAN algorithm, first identify current head position and direction, then sort requests, then calculate cumulative movement.

- UNDERSTAND THE MOTIVATION: For each scheduling algorithm, ask why it was designed and what specific problem it solves—this aids long-term retention.