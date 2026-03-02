# I/O Organization, Interrupts & DMA - Summary

## Key Definitions and Concepts
- **ISR**: Interrupt Service Routine - handler for specific interrupts
- **Bus Arbitration**: Process to resolve conflicts in bus access
- **End-of-Process (EOP)**: DMA termination signal
- **Chaining DMA**: Automatic chaining of multiple DMA operations

## Important Formulas and Theorems
- **Interrupt Latency** = Pipeline flush time + Context save time + ISR entry time
- **DMA Transfer Time**: T = (n * t_mem) + t_setup (n=blocks, t_mem=memory cycle)
- **I/O Throughput**: Throughput = (Data size) / (Total transfer time)

## Key Points
- DMA improves CPU utilization by 40-70% in data-intensive tasks
- Edge-triggered interrupts prevent signal bouncing issues
- Memory-mapped I/O simplifies programming but reduces available memory space
- USB uses polled interrupt mechanism with 1ms frame intervals
- Modern SSDs use NVMe protocol with 64K command queues
- RAID controllers employ multiple DMA channels for parallel stripe writes
- ARM processors use GIC (Generic Interrupt Controller) for IRQ management

## Common Mistakes to Avoid
- Confusing memory-mapped I/O with port-mapped I/O
- Neglecting interrupt priority in nested ISR scenarios
- Assuming DMA completely eliminates CPU involvement
- Forgetting to disable interrupts during critical sections

## Revision Tips
1. Practice timing diagrams for interrupt acknowledge cycles
2. Compare USB 2.0 (480 Mbps) vs USB 3.2 (20 Gbps) interrupt handling
3. Use Wireshark to analyze USB packet structures
4. Solve past DU papers on DMA transfer time calculations (2019 Q7, 2021 Q3)