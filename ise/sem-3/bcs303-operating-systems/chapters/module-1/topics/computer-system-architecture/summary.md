# Computer System Architecture - Summary

## Key Definitions and Concepts

- **Computer System Architecture:** The design and organization of a computer system's major hardware components and their interconnections

- **CPU (Central Processing Unit):** The primary processing unit containing the Control Unit (CU) and Arithmetic Logic Unit (ALU)

- **System Bus:** Communication channel consisting of data bus, address bus, and control bus connecting all system components

- **Interrupt:** A signal to the CPU indicating an event that requires immediate attention, suspending the current execution

- **DMA (Direct Memory Access):** Hardware mechanism allowing I/O devices to transfer data directly to/from memory without CPU intervention

- **Cache Memory:** High-speed memory layer between CPU and main memory that stores frequently accessed data

- **SMP (Symmetric Multiprocessing):** Multi-processor architecture where all processors share common memory and are controlled by a single OS

## Important Formulas and Theorems

- **Effective Access Time = (Hit Rate × Cache Time) + (Miss Rate × Main Memory Time)**
  - Used to calculate average memory access time considering cache performance

- **Fetch-Decode-Execute Cycle:** The fundamental sequence of operations performed by the CPU for every instruction

## Key Points

1. A computer system has four fundamental components: CPU, memory, I/O devices, and system bus

2. The CPU executes instructions through the Fetch-Decode-Execute cycle, controlled by the Program Counter

3. Interrupt-driven architecture allows efficient handling of asynchronous events without CPU polling

4. DMA significantly reduces CPU overhead for large I/O transfers by enabling direct memory access

5. Memory hierarchy balances speed, capacity, and cost through registers, cache, RAM, and secondary storage

6. Multi-core processors provide parallel processing capabilities within a single physical chip

7. The OS serves as an abstraction layer, managing hardware resources and providing services to applications

8. Cache coherency protocols ensure data consistency in multiprocessor systems

## Common Mistakes to Avoid

1. Confusing logical (virtual) addresses with physical addresses—understand the role of MMU in translation

2. Believing interrupts completely stop CPU execution—interrupts are handled, and execution resumes after context restoration

3. Underestimating the performance impact of I/O operations—always consider the speed mismatch between CPU and I/O devices

4. Forgetting that DMA still requires CPU setup and may generate interrupts upon completion

## Revision Tips

1. Draw and label a computer system architecture diagram showing all components and bus connections

2. Practice calculating effective memory access times with different cache hit rates

3. Trace through the interrupt handling sequence for a keyboard input scenario

4. Create a comparison table for programmed I/O, interrupt-driven I/O, and DMA covering speed, CPU usage, and complexity

5. Review how each hardware component is managed by the Operating System to understand the big picture