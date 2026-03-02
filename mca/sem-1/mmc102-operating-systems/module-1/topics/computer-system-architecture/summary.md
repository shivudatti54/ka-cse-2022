# Computer System Architecture - Summary

## Key Definitions

- **Computer System Architecture**: The structural design of computer hardware components and their interconnections that determines system capabilities
- **Privilege Levels (Rings)**: Hierarchical protection domains in processors, typically user mode (low privilege) and kernel mode (high privilege)
- **Mode Bit**: Hardware indicator showing current execution privilege level
- **Memory Management Unit (MMU)**: Hardware component that translates virtual addresses to physical addresses
- **Page Table**: Data structure maintained by OS that maps virtual pages to physical frames
- **Translation Lookaside Buffer (TLB)**: Hardware cache storing recent virtual-to-physical address translations
- **Interrupt**: Asynchronous signal causing CPU to suspend execution and handle events
- **Device Controller**: Hardware managing specific I/O device types with data, control, and status registers
- **System Call**: Controlled entry point for user processes to request OS services

## Important Formulas

- **Physical Address** = (Frame Number × Page Size) + Offset
- **Effective Access Time** = Hit Rate × Cache Time + (1 - Hit Rate) × (Cache Time + Memory Access Time)

## Key Points

1. Operating systems must understand hardware architecture to efficiently manage resources and provide protection between processes.

2. The dual-mode operation (user/kernel) is fundamental to system security—hardware enforces privilege separation, preventing user programs from accessing sensitive instructions or memory regions.

3. Memory Management Units work with operating system page tables to implement virtual memory, enabling memory protection and allowing processes to use more memory than physically available.

4. The TLB is a critical performance optimization that caches address translations, dramatically reducing memory access latency for page table lookups.

5. Interrupt architecture enables asynchronous event handling—devices signal completion or errors without CPU polling, improving system efficiency and responsiveness.

6. Device drivers bridge hardware-specific details and OS abstractions, translating generic I/O requests into device-specific commands.

7. Multi-core systems present unique OS challenges including load balancing, synchronization primitives, and cache coherence protocols.

8. The system call interface provides a secure mechanism for controlled kernel access, with parameters validated before execution.

9. Bus architecture determines peripheral connectivity and bandwidth characteristics, influencing overall system performance.

## Common Mistakes

1. Confusing virtual memory (address translation) with physical memory management—virtual addresses are per-process, physical addresses are global.

2. Assuming interrupts immediately service the handler—in practice, the CPU must finish the current instruction and save state first.

3. Forgetting that page tables themselves occupy physical memory and require management, creating overhead in memory-intensive systems.

4. Overlooking that TLB coherency must be maintained across multiple CPU cores in SMP systems.

5. Misunderstanding that system calls are not subroutine calls—they involve a full context switch between privilege levels, not merely a function call.