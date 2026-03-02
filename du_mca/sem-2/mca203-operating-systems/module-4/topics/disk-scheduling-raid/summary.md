# Disk Scheduling & RAID - Summary

## Key Definitions and Concepts
- **Seek Time**: Time to position disk head over correct track
- **Rotational Latency**: Time for desired sector to rotate under head
- **Striping**: Data distribution across multiple disks (RAID 0)
- **Mirroring**: Duplicate data storage (RAID 1)
- **Parity**: Error-checking data distributed across disks

## Important Formulas and Theorems
- RAID 5 Capacity: (n-1) * disk_size
- RAID 6 Capacity: (n-2) * disk_size
- Average Seek Time (SCAN): ≈ 1/3 of total cylinders
- SSTF Complexity: O(n²) for naive implementations

## Key Points
- FCFS is fair but inefficient for large workloads
- RAID 10 offers best performance but 50% storage efficiency
- C-LOOK eliminates unnecessary end-track movements
- RAID 5/6 suffer from write penalty due to parity updates
- SCAN algorithm prevents starvation completely
- Modern SSDs use FTL (Flash Translation Layer) instead of traditional scheduling
- Hybrid RAID systems combine HDDs and SSDs

## Common Mistakes to Avoid
- Confusing RAID 5 (single parity) with RAID 6 (double parity)
- Forgetting to account for head direction in SCAN problems
- Assuming all RAID levels provide redundancy (RAID 0 doesn't)
- Missing starvation scenarios in SSTF questions

## Revision Tips
1. Practice head movement diagrams for all scheduling algorithms
2. Create a RAID comparison table with columns for redundancy, performance, and efficiency
3. Memorize minimum disk requirements for each RAID level
4. Solve previous years' DU questions on seek time calculations

Length: 650 words