# Operating System Operations - Summary

## Key Definitions and Concepts

- **Bootstrap**: The initial program that starts when a computer is powered on, initializing hardware and loading the operating system kernel into memory.

- **Dual-Mode Operation**: The division of CPU execution into kernel mode (privileged, full hardware access) and user mode (restricted, limited instruction set) to protect system resources.

- **System Call**: A controlled programming interface allowing user programs to request privileged services from the operating system kernel.

- **Interrupt**: An asynchronous signal indicating an event requiring CPU attention, causing the current execution to be suspended and an interrupt service routine to be invoked.

- **Timer Interrupt**: A hardware-generated interrupt at regular intervals that enables the operating system to implement pre-emptive scheduling.

- **Context Switch**: The process of saving and restoring the state of a CPU so that execution can be switched between different processes.

- **Mode Switch**: A transition between kernel mode and user mode that changes CPU privilege level but may keep the same process in execution.

- **Process Control Block (PCB)**: A data structure maintained by the operating system that stores all information about a process, including state, registers, memory management, and I/O status.

## Important Formulas and Theorems

- **Interrupt Vector Table**: An array of pointers indexed by interrupt number that directs the CPU to the appropriate interrupt service routine.

- **System Call Execution Sequence**: User program → Prepare arguments → Execute trap instruction → Kernel mode execution → Validate and perform operation → Return result → User mode resumption.

- **Boot Sequence**: POST → Boot device selection → MBR/GPT reading → Boot loader execution → Kernel loading → Kernel initialization → Init process start.

## Key Points

- The bootstrap process initializes hardware through BIOS/UEFI and loads the operating system kernel through a multi-stage boot loader mechanism.

- Dual-mode operation is fundamental to operating system security, preventing user programs from directly accessing hardware or corrupting system data.

- System calls provide the only legal path for user programs to access privileged operations, with each call requiring at least one mode transition.

- Timer interrupts are essential for pre-emptive multitasking, allowing the operating system to reclaim CPU control before a process's time quantum expires.

- Interrupts can be classified as hardware (external devices), software (program-generated traps), and exceptions (fault conditions like division by zero).

- Process management involves creating, scheduling, and terminating processes, with the PCB serving as the central data structure for process information.

- Memory management operations ensure proper allocation, deallocation, and protection of system memory among competing processes.

- I/O device management involves device drivers, buffering, caching, and scheduling to efficiently handle communication between the CPU and peripheral devices.

## Common Mistakes to Avoid

1. **Confusing mode switch with context switch**: A mode switch only changes privilege level; a context switch changes the actual process being executed.

2. **Thinking system calls are the same as library functions**: Library functions often make system calls but may buffer data or combine multiple operations, making the actual number of system calls less obvious.

3. **Ignoring the role of hardware in OS operations**: Operating system operations depend heavily on hardware support, including timer hardware, interrupt controllers, and privileged CPU modes.

4. **Underestimating interrupt overhead**: While essential, interrupt handling incurs significant CPU overhead, and excessive interrupt generation can degrade system performance.

5. **Forgetting that interrupts cause mode switches**: Every hardware interrupt causes a transition to kernel mode, where the interrupt service routine executes with full privileges.

## Revision Tips

1. **Create a flowchart**: Draw the complete flow from power-on through boot sequence to user login, labeling each component's role.

2. **Practice system call tracing**: Use tools like `strace` on Linux to observe actual system calls made by simple programs and identify the mode transitions.

3. **Memorize the system call sequence**: The user-to-kernel-to-user cycle is fundamental and frequently tested in examinations.

4. **Understand interrupt priority**: Remember that certain interrupts (like machine check) have higher priority than others and cannot be masked.

5. **Review PCB structure**: The Process Control Block contains all necessary process state information and is essential for context switching.