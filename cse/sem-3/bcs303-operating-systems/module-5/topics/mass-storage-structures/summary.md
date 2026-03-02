# Mass Storage Structures - Summary

## Key Definitions

- **Track**: Concentric circle on a disk surface where data is recorded
- **Sector**: Smallest addressable unit on a disk, typically 512-4096 bytes
- **Cylinder**: Collection of tracks at the same radius across all surfaces
- **Seek time**: Time required to move the read-write head to the correct cylinder
- **Rotational latency**: Time waiting for the desired sector to rotate under the head
- **RAID**: Redundant Array of Independent Disks combining multiple physical disks

## Important Formulas

- **Average access time**: T_avg = T_seek + (1/2 × T_rotation) + T_transfer
- **Rotational latency**: T_rotational = 60,000 ms / (RPM × 2)
- **Transfer time**: T_transfer = (bytes requested) / (transfer rate)
- **Disk capacity**: Cylinders × Heads × Sectors per track × Bytes per sector

## Key Points

1. Disk access time primarily consists of seek time (3-15ms), rotational latency (2-8ms), and transfer time
2. SSTF provides better performance than FCFS but can cause starvation
3. SCAN (elevator algorithm) moves head in one direction servicing all requests before reversing
4. C-SCAN provides more uniform response times than SCAN
5. RAID 0 offers no redundancy; RAID 1 provides mirroring; RAID 5 uses distributed parity
6. SSDs have no seek time or rotational latency, providing uniform sub-millisecond access
7. Zoned bit recording places more sectors on outer tracks than inner tracks
8. Low-level formatting creates physical sectors; logical formatting creates file systems
9. Modern disks use defect management to remap bad sectors to spare locations
10. NVMe SSDs connect via PCIe bus providing significantly higher throughput than SATA

## Common Mistakes

1. Confusing rotational latency with seek time—rotational latency is half a rotation, seek time is head movement
2. Thinking RAID 5 provides protection against two simultaneous disk failures (only RAID 6 does)
3. Assuming SSD performance is the same across all locations—while better than HDD, performance varies by page/block
4. Forgetting that C-SCAN head "jumps" back to beginning without servicing requests
5. Not considering that higher RPM reduces rotational latency but increases power consumption and heat