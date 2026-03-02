# Operating System Operations - Summary

## Key Definitions and Concepts

- **Operating System**: System software that manages hardware resources and provides services to application programs
- **Process**: A program in execution, represented by a Process Control Block (PCB) containing process state, program counter, registers, and memory information
- **Kernel Mode**: Privileged execution mode with unrestricted access to hardware and memory
- **User Mode**: Restricted execution mode where applications run with limited privileges
- **System Call**: Programmed interface for user programs to request kernel services
- **Boot Process**: Sequence from power-on through BIOS/POST, boot loader, kernel loading to user-space initialization
- **Virtual Memory**: Technique extending available memory using secondary storage
- **Page Fault**: Exception occurring when accessed page is not in physical memory

## Important Formulas and Theorems

- CPU Utilization = (Busy Time / Total Time) × 100%
- Throughput = Number of Processes Completed / Unit Time
- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time
- Response Time = First Response Time - Arrival Time

## Key Points

- DUAL-MODE OPERATION separates user and kernel privileges to ensure system security and prevent unauthorized hardware access
- THE BOOT PROCESS involves multiple stages: hardware initialization, boot loader execution, kernel loading, and system services startup
- PROCESS MANAGEMENT includes creation (fork/exec), scheduling, and termination with complete resource reclamation
- MEMORY MANAGEMENT TECHNIQUES (paging, segmentation) solve the problems of allocation, protection, and address translation
- INTERRUPTS enable asynchronous hardware-software communication, with handlers executing in kernel mode
- DEVICE DRIVERS provide abstraction between generic OS operations and specific hardware implementations
- FILE SYSTEMS organize secondary storage with hierarchical directories while managing free space and access permissions

## Common Mistakes to Avoid

1. Confusing system calls with regular function calls - system calls involve mode transitions and are handled by the kernel
2. Mixing up internal and external fragmentation - internal occurs within allocated blocks, external occurs between free blocks
3. Confusing paging with segmentation - paging uses fixed-size blocks for physical memory, segmentation uses variable-sized logical divisions
4. Misunderstanding page faults - they are normal events indicating needed page loading, not necessarily errors

## Revision Tips

1. Draw diagrams for the boot process sequence and process state transitions to reinforce visual memory
2. Create comparison tables for memory management techniques showing advantages, disadvantages, and use cases
3. Practice writing pseudo-code for system call interfaces to understand parameter passing and return values
4. Review previous year DU examination questions on this topic to understand the depth and format expected
5. Use mnemonics like "POST-BL-KI-SI" (POST → Boot Loader → Kernel → Init) for boot sequence