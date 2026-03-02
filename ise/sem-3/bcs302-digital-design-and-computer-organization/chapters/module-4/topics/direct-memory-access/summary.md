# Direct Memory Access - Summary

## Key Definitions and Concepts

- **Direct Memory Access (DMA):** A hardware mechanism that allows I/O devices to transfer data directly to/from main memory without continuous CPU intervention, improving system efficiency.

- **DMA Controller:** Specialized hardware that manages direct data transfers between I/O devices and memory, containing address registers, count registers, and control logic.

- **Bus Arbitration:** The process by which the DMA controller obtains control of the system bus from the CPU to perform data transfers.

## Important Formulas and Theorems

- **Burst Mode Transfer Time:** Transfer Time = Data Size / Device Transfer Rate (CPU completely blocked during transfer)

- **Cycle Stealing Transfer Time:** Total Time = Σ(DMA cycle time + CPU idle time per cycle) — CPU remains partially available

- **Transparent Mode Transfer Time:** Transfer occurs only during CPU idle cycles, resulting in slowest transfer but maximum CPU availability

## Key Points

- DMA eliminates CPU bottleneck in high-volume data transfer operations by allowing peripherals direct memory access.

- Three DMA modes exist: burst (fastest, blocks CPU), cycle stealing (balanced), and transparent (slowest, no CPU impact).

- DMA transfer involves three phases: initialization (CPU programs controller), data transfer (DMA manages), and completion (interrupt to CPU).

- The DMA controller contains address register (memory location), count register (bytes remaining), and control register (mode/direction).

- Bus arbitration ensures only one master (CPU or DMA) controls the system bus at any time, preventing data corruption.

- DMA is essential for disk operations, network packet handling, audio/video streaming, and memory-to-memory transfers.

- Interrupt-Driven I/O generates interrupt per data word; DMA generates only one interrupt per transfer block, dramatically reducing overhead.

## Common Mistakes to Avoid

- Confusing DMA with interrupt-driven I/O: DMA requires minimal CPU intervention after initialization, while interrupt-driven I/O requires CPU service for each data word.

- Assuming burst mode is always best: Burst mode blocks the CPU entirely, which may cause system responsiveness issues; cycle stealing provides better overall system performance.

- Forgetting that DMA requires bus arbitration: The DMA controller must request and obtain bus control before each transfer, temporarily blocking CPU memory access.

## Revision Tips

1. Create a comparison table of Programmed I/O, Interrupt-Driven I/O, and DMA covering CPU involvement, speed, and complexity.

2. Memorize the three DMA transfer modes and their characteristics—know when each is appropriate.

3. Trace through a complete DMA transfer example, writing out each step of initialization, transfer, and completion phases.

4. Understand bus arbitration conceptually—the DMA controller must "ask permission" before using the system bus.