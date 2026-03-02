# Direct Memory Access - Summary

## Key Definitions and Concepts

- **Direct Memory Access (DMA):** A method allowing I/O devices to transfer data directly to/from memory without continuous CPU intervention
- **DMA Controller:** Dedicated hardware that manages data transfers between devices and memory
- **Bus Arbitration:** Process of resolving conflicts when multiple bus masters (CPU, DMA) compete for system bus access

## Important Formulas and Theorems

- DMA transfer time is typically measured in bus cycles
- CPU overhead reduction = (Transfer Size - DMA Setup Overhead) / Transfer Size
- In cycle stealing mode, each word transfer requires one bus cycle from DMA and leaves N cycles for CPU

## Key Points

- DMA enables autonomous data transfer, freeing CPU for other computations
- Three transfer modes: BURST (blocks CPU entirely), CYCLE STEALING (alternates), TRANSPARENT (CPU idle only)
- DMA controller registers: Address, Count, Mode, Command, Status
- Bus Request (BR) and Bus Grant (BG) signals coordinate bus access
- CPU programs DMA controller before transfer, receives interrupt upon completion
- DMA is ideal for block transfers of large data sizes
- Memory-to-memory transfers require two bus cycles per word

## Common Mistakes to Avoid

- Confusing DMA with interrupt-driven I/O; DMA requires NO CPU intervention during transfer
- Thinking DMA is always faster; for very small transfers, setup overhead may exceed the benefit
- Forgetting that DMA controllers require CPU programming before operation
- Assuming transparent mode is always best; it may be slow if CPU has high bus utilization

## Revision Tips

- Focus on the three DMA modes and understand when each is appropriate
- Remember the sequence: CPU programs DMA → DMA transfers data → DMA interrupts CPU
- Practice comparing DMA with programmed I/O and interrupt-driven I/O
- Review bus arbitration concepts as they frequently appear in exams
- Memorize the advantages and disadvantages of DMA for quick recall during exams