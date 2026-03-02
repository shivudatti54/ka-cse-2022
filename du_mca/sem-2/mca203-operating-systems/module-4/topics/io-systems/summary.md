# I/O Systems - Summary

## Key Definitions and Concepts
- **DMA Controller**: Specialized processor for memory transfers without CPU
- **Seek Time**: Time to position disk head over correct track
- **RAID 5**: Block-level striping with distributed parity
- **Interrupt Vector**: Table containing ISR addresses
- **SCSI**: Small Computer System Interface protocol

## Important Formulas and Theorems
- **Disk Access Time** = Seek Time + Rotational Latency + Transfer Time
- **RAID 5 Parity**: P = D₁ ⊕ D₂ ⊕ ... ⊕ Dₙ
- **Amdahl's Law for I/O**: Speedup = 1 / [(1 - P) + P/S]
- **Interrupt Latency** = max(ISR execution time, kernel preemption delay)

## Key Points
- I/O subsystems account for >60% of OS code
- DMA reduces CPU overhead but requires cache coherency
- C-LOOK is preferred over SCAN for modern disks
- RAID 6 uses dual parity for two-disk failure tolerance
- NVMe supports 64K command queues vs AHCI's 32
- Memory-mapped I/O uses physical addresses directly
- Error correction costs increase exponentially with bit protection

## Common Mistakes to Avoid
- Confusing interrupt masking with disabling interrupts
- Assuming all RAID levels provide fault tolerance (RAID 0 doesn't)
- Neglecting rotational latency in disk scheduling
- Forgetting virtual filesystems in I/O stack diagrams
- Misapplying seek time formulas for SSDs

## Revision Tips
- Practice timing diagrams for interrupt processing
- Memorize RAID formulas: RAID 5 usable space = (n-1)*disk_size
- Use flowcharts for I/O request lifecycles
- Solve numericals on transfer rates with DMA
- Compare Linux's CFQ vs Kyber I/O schedulers

Length: 400-800 words