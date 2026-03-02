# Computer System Organization - Summary

## Key Definitions and Concepts

- **Von Neumann Architecture**: Computer design where instructions and data share the same memory and bus system; consists of CPU, memory, and I/O units connected by system bus.
- **Fetch-Decode-Execute Cycle**: The fundamental operation cycle of the CPU involving fetching instructions, decoding them, executing operations, and storing results.
- **System Bus**: Communication pathway consisting of data bus (carries data), address bus (carries memory addresses), and control bus (carries control signals).
- **Cache Memory**: High-speed memory between CPU and main memory utilizing locality of reference; divided into L1, L2, and L3 levels.
- **Interrupt**: Signal to CPU requiring immediate attention, allowing efficient handling of asynchronous events without continuous polling.
- **DMA (Direct Memory Access)**: Method allowing I/O devices to transfer data directly to/from memory without CPU intervention.

## Important Formulas and Theorems

- **Locality of Reference**: Programs tend to access the same memory locations repeatedly (temporal) and access nearby locations (spatial). This principle makes caching effective.
- **Von Neumann Bottleneck**: The limitation arising from using a single bus for both instructions and data, limiting throughput between CPU and memory.

## Key Points

- The CPU consists of Control Unit (directs operation) and ALU (performs calculations), with registers for temporary storage during execution.
- Memory hierarchy follows the trade-off between speed, cost, and capacity: registers → cache → RAM → secondary storage.
- Cache memory uses spatial locality (neighboring addresses) and temporal locality (recently used data) to improve performance.
- Interrupt handling involves: interrupt detection → save state → execute ISR → restore state → continue execution.
- DMA significantly reduces CPU overhead for large data transfers by allowing direct memory-device communication.
- Multi-processor systems (SMP, multi-core) require OS support for parallel scheduling and synchronization.
- The operating system must manage hardware resources efficiently, accounting for the characteristics of each system component.

## Common Mistakes to Confuse

- Confusing address bus (unidirectional, CPU to memory) with data bus (bidirectional). ADDRESS BUS CARRIES ONLY MEMORY ADDRESSES, NOT DATA.
- Thinking cache completely replaces main memory — cache is a COPY of frequently accessed data, not the primary storage location.
- Believing interrupts slow down the system — interrupts actually IMPROVE efficiency by eliminating wasteful polling.

## Revision Tips

1. Draw the complete Von Neumann architecture diagram from memory, labeling all components and bus types.
2. Trace through a simple instruction execution example to reinforce the fetch-decode-execute cycle.
3. Create a comparison table for I/O methods: programmed, interrupt-driven, and DMA with advantages/disadvantages.
4. Relate every hardware concept back to its OS implication — how does the OS use each component?
5. Memorize the memory hierarchy order and typical sizes: L1 (KB), L2 (KB-MB), RAM (GB), Storage (TB).