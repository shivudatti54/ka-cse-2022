# Computer System Organization - Summary

## Key Definitions

- **CPU (Central Processing Unit)**: The primary computational component of a computer, consisting of the Control Unit, Arithmetic Logic Unit (ALU), and registers.
- **System Bus**: The communication pathway connecting CPU, memory, and I/O devices, comprising data, address, and control buses.
- **Interrupt**: An asynchronous signal sent to the CPU by hardware indicating an event that requires immediate attention.
- **DMA (Direct Memory Access)**: A method allowing peripheral devices to transfer data directly to/from memory without CPU intervention.
- **Kernel Mode**: The privileged execution mode where the operating system has full access to all hardware resources.
- **User Mode**: The restricted execution mode where user applications run with limited hardware access.
- **Bootstrap**: The process of loading the operating system into memory when a computer is powered on.
- **Device Controller**: Specialized hardware that manages communication between the CPU and specific I/O devices.

## Important Formulas

- **Average Memory Access Time (AMAT)**: AMAT = Hit Time + (Miss Rate × Miss Penalty)
- **Effective Access Time with Cache**: Average = Σ(probability_i × access_time_i)
- **CPU Cycle Time**: Cycle time = 1 / Clock frequency

## Key Points

1. Computer systems consist of CPU, main memory, I/O devices, and system buses working in coordination under operating system management.

2. The storage hierarchy balances speed, capacity, and cost through multiple levels from fast registers to slow archival storage.

3. Interrupts enable asynchronous device communication, allowing the CPU to perform useful work while waiting for slow I/O operations.

4. DMA controllers offload bulk data transfer responsibilities from the CPU, improving system throughput for I/O-intensive operations.

5. Dual-mode operation (kernel/user mode) is fundamental to system protection, preventing user programs from directly accessing hardware.

6. The bootstrap process involves BIOS/UEFI initialization, loading the kernel, and transitioning from firmware to operating system control.

7. Device drivers provide hardware abstraction, allowing the operating system to interact with diverse I/O devices through uniform interfaces.

8. The principle of locality (temporal and spatial) underlies caching strategies used by both hardware (CPU cache) and operating systems (page caching).

9. Multiprocessor and multi-core systems add complexity to operating system design, requiring synchronization and cache coherence mechanisms.

## Common Mistakes

1. **Confusing hardware components with OS functions**: Registers, cache, and memory are hardware; virtual memory, process scheduling, and file systems are OS functions built upon this hardware.

2. **Assuming interrupts are only software events**: Hardware interrupts from devices (keyboard, disk, network) are the primary source, not just software exceptions or traps.

3. **Forgetting that BIOS/UEFI is software**: Students sometimes confuse firmware with hardware; BIOS is software stored in ROM that performs hardware initialization.

4. **Misunderstanding DMA's role**: DMA does not eliminate CPU involvement entirely; the CPU still sets up the transfer and is interrupted when it completes, though data movement itself is direct.