# Secondary Storage Structure - Summary

## Key Definitions and Concepts

- **Secondary Storage**: Non-volatile storage (hard disks, SSDs) that retains data when power is off, used for permanent data storage
- **Track**: Concentric circle on a disk platter containing sectors
- **Sector**: Basic unit of data storage, typically 512 or 4096 bytes
- **Cylinder**: Collection of tracks at the same radius across all platter surfaces
- **Seek Time**: Time required to move disk head to correct cylinder
- **Rotational Latency**: Time waiting for desired sector to rotate under the head
- **LBA (Logical Block Addressing)**: Modern disk addressing scheme presenting disk as linear sector array

## Important Formulas and Theorems

- **Disk Access Time** = Seek Time + Rotational Latency + Transfer Time
- **Average Rotational Latency** = (1/2) × (60 / RPM) seconds
- **FCFS Total Movement** = Σ|track_i - track_(i-1)|
- **SSTF**: Service request closest to current head position
- **RAID 1 Capacity** = (N/2) × disk capacity (50% overhead)
- **RAID 5 Capacity** = (N-1) × disk capacity (1 disk for parity)
- **Swap Space Guidelines**: 2-4× RAM for <2GB systems, equal to RAM for >2GB systems

## Key Points

1. Seek time dominates disk access time, making disk scheduling critical for performance
2. SSTF minimizes seek distance but can cause starvation; SCAN/C-SCAN provide fairer service
3. SCAN moves in both directions while C-SCAN services only in one direction then returns empty
4. LOOK is optimized SCAN that only moves to extreme requests, not disk ends
5. RAID 0 provides no redundancy; RAID 1 mirrors data; RAID 5 uses distributed parity
6. RAID 5 requires minimum 3 disks and tolerates 1 failure; RAID 6 tolerates 2 failures
7. Swap space extends physical memory; can be dedicated partition or file
8. SSDs eliminate mechanical delays, making traditional scheduling algorithms obsolete

## Common Mistakes to Remember

- Confusing SCAN with C-SCAN: SCAN services both directions, C-SCAN returns empty
- Forgetting that RAID 0 has zero fault tolerance despite good performance
- Calculating total head movement incorrectly: use absolute differences between consecutive positions
- Assuming SSTF always performs best: it can cause starvation for distant requests

## Revision Tips

1. Practice numerical problems on disk scheduling with different request sequences
2. Create a comparison table for all RAID levels covering performance, redundancy, and capacity
3. Memorize the key characteristic of each scheduling algorithm (FCFS=simple, SSTF=shortest distance, SCAN=elevator)
4. Remember that magnetic disks have mechanical components (seek, rotation) while SSDs are purely electronic
5. Focus on understanding trade-offs between algorithms rather than just memorizing names