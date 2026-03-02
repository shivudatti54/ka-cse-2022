# Introduction to Operating Systems - Summary

## Key Definitions
- **Operating System**: A system software that acts as an intermediary between computer hardware and users, managing resources and providing services to application programs.
- **Kernel**: The core component of an OS that runs in privileged mode with direct access to hardware; handles critical functions like process scheduling and memory management.
- **System Calls**: Programming interface through which user programs request services from the operating system.
- **Multiprogramming**: Technique where multiple programs reside in memory simultaneously, improving CPU utilization.
- **Timesharing**: Extension of multiprogramming that allows multiple users to share the CPU simultaneously.

## Important Formulas
- **CPU Utilization**: The percentage of time the CPU is actively executing processes. Modern OS aims to maximize this while maintaining acceptable response times.
- **Throughput**: The number of processes completed per unit time. OS scheduling algorithms aim to maximize throughput.
- **Turnaround Time**: The total time from submission to completion of a process. Includes waiting time and execution time.

## Key Points
1. An OS serves two fundamental purposes: efficient resource management and providing user convenience through hardware abstraction.
2. The kernel is the heart of the OS operating in privileged mode, while system programs provide additional functionality.
3. System calls provide a controlled interface for user programs to access kernel services securely.
4. Operating systems have evolved from simple batch processors to complex multiuser, multitasking systems.
5. Modern OS classifications include general-purpose (Windows, Linux), embedded systems, and real-time operating systems.
6. Operating systems create virtual machines that hide hardware complexities from users and applications.
7. Memory management, process scheduling, and I/O management are core OS functions that ensure efficient resource utilization.
8. The distinction between kernel mode and user mode is fundamental to system security and stability.

## Common Mistakes
1. Confusing the kernel with the entire operating system—the kernel is just one component.
2. Believing that more processes always mean better CPU utilization—context switching overhead can reduce efficiency.
3. Misunderstanding that multitasking appears parallel on single-core systems due to rapid context switching.
4. Confusing multiprogramming with multiprocessing—multiprogramming works on single processors while multiprocessing uses multiple CPUs.