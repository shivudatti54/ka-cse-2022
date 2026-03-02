# What Operating Systems Do - Summary

## Key Definitions

- **Operating System**: System software that manages hardware resources and provides services to application programs, acting as an interface between users and computer hardware.

- **Process**: A program in execution, consisting of program code, current activity, and associated resources managed by the OS.

- **Process Control Block (PCB)**: A data structure maintained by the OS that contains information about a process including state, program counter, CPU registers, and memory management information.

- **Resource Manager**: The OS function of efficiently allocating and managing hardware resources among competing processes.

- **Virtual Memory**: A memory management technique that provides the illusion of a larger physical memory by using disk space to supplement RAM.

## Important Formulas

There are no specific formulas for this conceptual topic, but understanding the following relationships is important:

- **CPU Utilization**: Percentage of time the CPU is actively executing processes
- **Throughput**: Number of processes completed per unit time
- **Turnaround Time**: Time from process submission to completion
- **Waiting Time**: Time a process spends ready to run but waiting for CPU

## Key Points

1. The operating system serves dual purposes: providing user convenience through abstraction and managing hardware resources efficiently.

2. From the user view, the OS prioritizes ease of use and user-friendly interfaces over resource efficiency.

3. From the system view, the OS acts as a resource manager, controlling and coordinating hardware for multiple processes.

4. Process management involves creating, scheduling, and terminating processes, with the PCB serving as the central data structure.

5. Memory management allocates RAM to processes, implements virtual memory, and provides memory protection between processes.

6. File management organizes storage into files and directories, providing logical abstraction over physical storage devices.

7. I/O management handles device interactions through drivers, using buffering, caching, and spooling for efficiency.

8. Security mechanisms include user authentication, access control, and encryption to protect system resources.

9. Modern operating systems support multi-tasking, allowing multiple processes to execute concurrently through rapid CPU switching.

10. The OS provides process isolation, ensuring one process cannot interfere with another's memory or resources.

## Common Mistakes

1. Confusing the user view with the system view—remember user view emphasizes convenience while system view emphasizes resource management efficiency.

2. Believing processes and programs are the same—a program is passive code while a process is an active execution instance.

3. Overlooking that the OS must manage resources fairly, not just efficiently—fairness prevents starvation.

4. Assuming all operating systems have the same design goals—embedded systems, real-time systems, and general-purpose systems have different priorities.