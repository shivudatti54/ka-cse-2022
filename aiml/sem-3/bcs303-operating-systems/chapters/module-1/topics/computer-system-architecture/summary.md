# Computer System Architecture - Summary

## Key Definitions and Concepts

- **CPU (Central Processing Unit)**: The primary computational unit containing Control Unit, ALU, and registers that executes instructions
- **Memory Hierarchy**: Organized levels of storage (registers, cache, RAM, secondary storage) balancing speed, cost, and capacity
- **Bus**: Conductor system for transmitting data, addresses, and control signals between components
- **Interrupt**: Signal that causes CPU to suspend current execution and handle an event asynchronously
- **Dual-Mode Operation**: Hardware support distinguishing between user mode and kernel (privileged) mode
- **System Call**: Mechanism for user programs to request OS services with controlled privilege transition

## Important Formulas and Concepts

- **Memory Access Time**: Typical values—registers (1-2 ns), cache (2-10 ns), RAM (50-100 ms), SSD (25-100 μs), HDD (5-20 ms)
- **Effective Address Calculation**: For base/limit protection, legal addresses range from Base to (Base + Limit - 1)
- **Fetch-Decode-Execute Cycle**: The fundamental instruction processing sequence in CPU

## Key Points

- CPU consists of Control Unit (instruction processing), ALU (computations), and registers (fast storage)
- Memory hierarchy exists because fast memory is expensive; OS optimizes data placement
- I/O controllers abstract device complexity and provide standardized interfaces to CPU
- Interrupts enable asynchronous event handling without CPU polling overhead
- Dual-mode operation with mode bit prevents user programs from executing privileged instructions
- Base and limit registers provide hardware-level memory protection against unauthorized access
- Timer ensures OS regains CPU control periodically, enabling preemption and time-sharing
- System calls transition from user to kernel mode through controlled mechanisms (interrupt or syscall instruction)

## Common Mistakes to Avoid

- Confusing hardware interrupts with software interrupts—hardware are asynchronous events, software are synchronous traps
- Thinking RAM is non-volatile—RAM is volatile (loses data when power is off)
- Assuming all memory accesses are equally fast—cache misses incur significant penalties
- Confusing interrupt handling with system calls—system calls are one type of software interrupt
- Ignoring the role of hardware protection—OS protection relies on hardware support, not just software

## Revision Tips

1. Draw a diagram of computer system architecture showing CPU, memory, I/O, and buses—label all components
2. Trace through a simple instruction's fetch-decode-execute cycle step by step
3. List all hardware protection mechanisms and explain how each prevents unauthorized actions
4. Practice explaining the complete system call path from user program to kernel and back
5. Compare memory access times across hierarchy levels and explain why OS needs to manage this complexity