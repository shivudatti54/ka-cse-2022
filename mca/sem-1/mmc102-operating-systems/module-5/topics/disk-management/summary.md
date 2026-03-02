# Disk Management - Summary

## Key Definitions

- **Track**: Concentric circle on a disk surface where data is recorded
- **Sector**: Wedge-shaped portion of a track, typically holding 512 or 4096 bytes
- **Cylinder**: Set of tracks at the same radial distance on all surfaces
- **Seek Time**: Time required to move the disk head to the correct cylinder
- **Rotational Delay**: Time waiting for the desired sector to rotate under the head
- **Access Time**: Sum of seek time, rotational delay, and transfer time
- **Partition**: Logical division of a physical disk into independent sections
- **Boot Block**: Sector containing the initial bootstrap program
- **Bad Block**: Sector with permanent read/write errors

## Important Formulas

- **Access Time**: T_access = T_seek + T_rotational + T_transfer
- **Average Rotational Delay**: T_rotational = (1/2) × (1/RPM) × 60 seconds
- **Transfer Time**: T_transfer = (bytes requested) / (transfer rate)
- **Average Seek Time**: Approximately 1/3 of full seek time for typical workloads

## Key Points

1. Disk access time is dominated by seek time, which ranges from 1-10 milliseconds depending on the distance the head must travel.

2. FCFS is simple and fair but performs poorly when requests are scattered, resulting in excessive head movement.

3. SSTF minimizes seek distance for each request but can cause starvation for requests far from the current head position.

4. SCAN (elevator algorithm) services requests in one direction until reaching the end, then reverses, providing fair service with good performance.

5. C-SCAN provides uniform wait times by servicing requests in one direction only and jumping back to the beginning.

6. LOOK and C-LOOK are optimized versions that only travel to the last pending request rather than the full disk extent.

7. Low-level formatting writes sector headers, ECC, and data areas; OS formatting creates file systems on partitions.

8. Modern disks use defect management to remap bad sectors to spare areas automatically.

9. Disk interface choice (SATA, SCSI, SAS) affects performance, device count, and system capabilities.

10. Real systems may combine multiple algorithms or use variations optimized for specific workloads.

## Common Mistakes

1. **Confusing SSTF with FCFS**: Students often calculate SSTF as if requests arrived in order rather than choosing the nearest request each time.

2. **Forgetting direction in SCAN**: When calculating SCAN, forgetting the initial head direction leads to incorrect service order.

3. **Including current position as movement**: The head is already at the starting track; movement begins from there to the first served request.

4. **Ignoring the return pass in SCAN**: SCAN services requests on both passes; the return pass must be included in calculations.

5. **Mixing up LOOK and SCAN**: LOOK doesn't go to the disk edge, only to the last request, making it more efficient than SCAN.

6. **Assuming smaller numbers are always better**: While seek time reduction is good, some algorithms sacrifice overall throughput for fairness.

7. **Overlooking transfer time in access time calculations**: While seek and rotational delay dominate, transfer time matters for large sequential reads.