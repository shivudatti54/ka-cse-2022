# Secondary Storage Structure - Summary

## Key Definitions and Concepts

- **Secondary Storage**: Non-volatile memory devices providing permanent data storage, primarily magnetic hard disk drives (HDDs) and solid-state drives (SSDs).

- **Disk Geometry**: Physical organization into platters, tracks (concentric circles), sectors (pie-shaped divisions), and cylinders (tracks at same radius across all surfaces).

- **Logical Block Address (LBA)**: Modern disk addressing scheme that abstracts physical geometry, presenting disks as linear arrays of addressable sectors.

- **Disk Access Time Components**: Seek time (arm movement to cylinder), Rotational latency (waiting for sector rotation), Transfer time (actual data read/write).

- **Disk Cache**: On-disk DRAM buffer storing frequently accessed data; uses write-back or write-through policies.

## Important Formulas and Theorems

- **Average Rotational Latency** = (1/2) × Time for One Rotation = (1/2) × (60 / RPM) seconds

- **Average Access Time** = Average Seek Time + Average Rotational Latency + Transfer Time

- **RAID Capacity**: RAID 5 uses N+1 disks for N data disks; RAID 10 requires 2N disks for N data disks

## Key Points

- Magnetic disks remain the dominant form of secondary storage due to cost-effectiveness and large capacities, though SSDs are increasingly common.

- Seek time (3-12ms) typically dominates random access latency, while transfer time matters mainly for sequential operations.

- SCAN/LOOK algorithms significantly outperform FCFS by minimizing arm movement through directional sweeping.

- C-SCAN provides uniform wait times by servicing requests in only one direction, important for transaction processing systems.

- Disk caches dramatically improve performance but introduce data durability risks; battery-backed caches mitigate this for enterprise applications.

- RAID 5 provides good balance of performance, capacity, and fault tolerance for general business applications.

- RAID 10 offers superior write performance and fault tolerance for database and mission-critical applications at higher cost.

- Modern disks perform sector remapping, making the logical-to-physical mapping transparent to the operating system.

## Common Mistakes to Avoid

- Confusing SCAN with C-SCAN: Remember SCAN services both directions while C-SCAN only services in one direction and returns quickly to the beginning.

- Forgetting to halve rotational latency: Average rotational latency is exactly half the time for one complete rotation, not the full rotation time.

- Calculating RAID capacity incorrectly: RAID 5 loses the equivalent of one disk to parity, not half the total capacity.

- Ignoring the difference between seek time and access time: Seek time is only one component of total access time.

- Not considering write penalty in RAID 5: While reads are fast, writes require reading old data, old parity, writing new data, and calculating new parity.

## Revision Tips

1. Practice numerical problems: Calculate access times for different RPM values and transfer rates until the process becomes automatic.

2. Draw the disk scheduling scenarios: Visualize head movement for SCAN/C-SCAN to understand service order and total distance traveled.

3. Create a comparison table for RAID levels listing performance, fault tolerance, minimum disks, and use cases.

4. Remember the hierarchy: Bytes → Sectors → Tracks → Cylinders → Platters → Disk.

5. Relate concepts to real systems: Think about why your computer feels faster with an SSD (no seek time, no rotational latency) versus HDD.