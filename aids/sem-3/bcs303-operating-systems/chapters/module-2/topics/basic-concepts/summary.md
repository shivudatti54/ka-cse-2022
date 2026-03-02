# Basic Concepts of Operating Systems - Summary

## Key Definitions and Concepts

- **Operating System**: System software that manages hardware resources and provides services to application programs; acts as an interface between users and computer hardware
- **System Call**: Programming interface allowing user programs to request services from the OS kernel
- **Kernel**: Core part of OS running in privileged mode, handling essential operations
- **Bootstrap Program**: Initial program that loads the OS when computer starts
- **Context Switching**: Saving and restoring CPU state to switch between processes

## Important Formulas and Theorems

There are no specific formulas in this conceptual topic, but key ratios to understand include:

- **CPU Utilization**: Percentage of time CPU is actively processing (goal: maximize)
- **Turnaround Time**: Time from job submission to completion (goal: minimize)
- **Waiting Time**: Time process spends ready to run but not getting CPU (goal: minimize)

## Key Points

- Operating systems serve dual purposes: resource management and providing a virtual machine abstraction
- Five main OS functions: Process Management, Memory Management, File Management, Device Management, Security/Protection
- OS types: Batch, Time-Sharing, Real-Time, Distributed, Network—each suited for different applications
- System calls provide controlled access to privileged kernel operations
- Common OS structures: Monolithic, Layered, Microkernel, Client-Server
- Bootstrap process includes POST, hardware detection, and kernel loading
- Time-sharing creates illusion of multiple simultaneous users through rapid CPU switching
- Modern OSes combine multiprocessing (true parallelism) with multiprogramming (apparent parallelism)

## Common Mistakes to Avoid

- Confusing time-sharing with multiprocessing—they are different mechanisms
- Believing OS runs only in kernel mode—user processes run in user mode with limited privileges
- Thinking system calls are same as library functions—system calls involve mode switch to kernel
- Ignoring the bootstrap process—it's fundamental to understanding system startup

## Revision Tips

1. Create a table comparing OS types with characteristics and examples
2. Draw and label the OS architecture showing user space, kernel, and hardware
3. List all system call types with examples of when each would be used
4. Trace the bootstrap sequence from power button to login prompt
5. Explain how a simple operation like opening a file involves multiple OS components