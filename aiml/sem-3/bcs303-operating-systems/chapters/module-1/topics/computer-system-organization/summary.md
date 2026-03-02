# Computer System Organization - Summary

## Key Definitions and Concepts

- **CPU (Central Processing Unit)**: The primary computational component consisting of the Control Unit, ALU, and registers that executes instructions.

- **System Bus**: Communication pathway connecting CPU, memory, and I/O devices, comprising data, address, and control buses.

- **Fetch-Decode-Execute Cycle**: The fundamental instruction processing sequence where the CPU fetches an instruction from memory, decodes it, and executes the specified operation.

- **Cache Memory**: High-speed memory between CPU and main memory that stores frequently accessed data based on temporal and spatial locality principles.

- **DMA (Direct Memory Access)**: I/O technique allowing direct data transfer between devices and memory without CPU intervention.

- **Interrupt**: A signal requiring CPU attention, enabling asynchronous event handling without continuous polling.

## Important Formulas and Theorems

- **Locality Principle**: Programs tend to reuse data and instructions they have recently used (temporal) or use nearby data (spatial). This principle justifies cache memory effectiveness.

- **Memory Hierarchy Performance**: Access time increases dramatically from registers (nanoseconds) to cache (nanoseconds) to main memory (microseconds) to secondary storage (milliseconds).

## Key Points

- Computer systems consist of three interconnected subsystems: CPU, memory, and I/O, communicating via the system bus.

- The CPU's Control Unit directs operations, while the ALU performs arithmetic and logical computations.

- Registers like PC, IR, MAR, MDR, and ACC are essential for instruction execution and data movement.

- The instruction cycle involves fetching instructions from memory, decoding them, and executing operations—repeating continuously.

- Memory hierarchy balances speed, capacity, and cost through cache, primary memory, and secondary storage levels.

- I/O techniques vary from simple programmed I/O to efficient DMA transfers that offload CPU work.

- Interrupts enable asynchronous device communication, with the interrupt service routine handling specific events.

## Common Mistakes to Confuse

- Confusing the data bus (bidirectional) with the address bus (unidirectional from CPU).

- Misunderstanding that cache is separate from primary memory—it sits between CPU and main memory.

- Thinking interrupts stop the CPU entirely—the CPU finishes the current instruction and then handles the interrupt.

- Believing more cache always means better performance—cache size involves trade-offs with hit rate and access time.

## Revision Tips

1. Draw the computer system organization diagram repeatedly until you can reproduce it from memory, labeling all components and connections.

2. Practice tracing through the fetch-decode-execute cycle with different instruction types—memory-to-register, register-to-memory, and register-to-register operations.

3. Create a comparison table for I/O techniques, noting advantages, disadvantages, and typical use cases.

4. Memorize the seven-step interrupt handling process and be able to explain each step in your own words.

5. Solve previous year DU exam questions on this topic to understand the question patterns and answer style expected.