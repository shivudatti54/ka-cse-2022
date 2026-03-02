# System Model - Summary

## Key Definitions and Concepts

- **Operating System**: A program that acts as an intermediary between users and computer hardware, managing resources and providing services
- **Kernel**: The core component of the operating system that runs in privileged mode with direct hardware access
- **System Calls**: Programming interfaces allowing user programs to request services from the operating system
- **Process**: An instance of a program in execution, with its own address space and process control block
- **Process Control Block (PCB)**: Data structure storing process information including state, program counter, CPU registers, and memory management details
- **Boot Loader**: Program that initializes the system and loads the operating system kernel
- **User Mode**: CPU execution mode where user programs run with restricted privileges
- **Kernel Mode**: Privileged mode where the operating system kernel executes with full hardware access

## Important Formulas and Theorems

No specific formulas apply to this conceptual topic. The key principles revolve around understanding architectural relationships rather than numerical computations.

## Key Points

- Operating systems serve dual purposes: resource management and providing a virtual machine abstraction
- The system architecture consists of hardware, kernel, system libraries, and user applications
- Multiprogramming enables concurrent execution of multiple processes to improve CPU utilization
- System calls provide controlled access to privileged operations through a well-defined interface
- Process states include new, ready, running, blocked, and terminated
- The boot process involves BIOS/UEFI initialization, boot loader execution, kernel loading, and service startup
- Memory is divided into kernel space (privileged) and user space (restricted)
- The system model foundation is essential for understanding process synchronization and deadlock topics

## Common Mistakes to Avoid

- Confusing multiprogramming with multiprocessing—they are different concepts
- Misunderstanding the distinction between the kernel and the entire operating system
- Thinking that all operating systems are the same type—they serve different purposes
- Overlooking the importance of user mode versus kernel mode in system security
- Failing to connect the system model concepts to later topics in the module

## Revision Tips

1. Draw the system architecture diagram repeatedly until you can reproduce it from memory
2. Create a table comparing different types of operating systems with their characteristics
3. Practice explaining the boot sequence step-by-step without referring to notes
4. Memorize the process states and draw the state transition diagram
5. Review how system calls work as this connects to synchronization concepts later in the module