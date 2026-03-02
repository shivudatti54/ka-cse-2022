# Mass Storage Systems: Magnetic Disks and SSDs - Summary

## Key Definitions and Concepts

- **Track**: Concentric circle on a disk surface where data is magnetically recorded
- **Sector**: Smallest addressable unit on a disk, typically 512 bytes or 4 KB
- **Cylinder**: Set of tracks at the same radius across all surfaces
- **Seek Time**: Time to move read/write head to correct cylinder
- **Rotational Latency**: Time waiting for sector to rotate under head
- **SSD**: Storage device using NAND flash memory instead of magnetic media
- **NAND Flash**: Non-volatile memory with page-based read/write and block-based erase
- **Wear Leveling**: Technique to distribute write cycles evenly across SSD cells
- **RAID**: Redundant Array of Independent Disks for performance and/or reliability

## Important Formulas and Theorems

- **Disk Capacity**: C × H × S × sector_size
- **Average Rotational Latency**: (1/2) × (60/R) seconds = (30/R) ms (where R = RPM)
- **Transfer Time**: Bytes to transfer / Transfer rate
- **Total Access Time**: T_seek + T_rot + T_trans + T_ctrl

## Key Points

- Magnetic disks have mechanical components causing seek time (3-12ms) and rotational latency (2-8ms), limiting random I/O performance
- SSDs have no moving parts, providing sub-millisecond access times and thousands of times higher IOPS than HDDs
- SCAN algorithm moves head in both directions like an elevator; C-SCAN returns to beginning without servicing
- SSTF provides better performance than FCFS but may cause starvation
- SSDs require wear leveling to prevent individual cells from failing prematurely
- TLC and QLC SSDs offer higher capacity but lower endurance than SLC and MLC
- RAID 5 provides fault tolerance with single disk failure; RAID 6 handles two disk failures
- Write amplification in SSDs reduces effective lifespan and performance over time
- TRIM command allows OS to inform SSD which data is deleted, enabling proactive garbage collection

## Common Mistakes to Avoid

- Confusing rotational latency with seek time—these are distinct components of access time
- Assuming SSDs are always better for all use cases; HDDs remain cost-effective for bulk storage
- Forgetting that SSD blocks must be erased before being written (no in-place update)
- Overlooking the impact of write amplification on SSD endurance calculations
- Not considering that disk scheduling algorithms operate at the OS level, requiring kernel support

## Revision Tips

1. Practice numerical problems on disk access time calculations with varying RPM, seek time, and transfer rates
2. Trace through disk scheduling examples manually to understand head movement patterns
3. Create a comparison table of SSD types (SLC, MLC, TLC, QLC) highlighting performance vs endurance trade-offs
4. Remember that SSDs maintain near-constant access time regardless of data location, unlike HDDs
5. Review RAID levels and their specific use cases—RAID 5 for servers, RAID 10 for databases requiring both speed and redundancy