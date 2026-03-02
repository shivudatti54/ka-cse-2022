# What Operating Systems Do - Summary

## Key Definitions and Concepts

- **Operating System**: The most fundamental system software that acts as an intermediary between users and computer hardware, managing resources and providing services.

- **Resource Manager**: The OS function that allocates and controls computer system resources including CPU, memory, storage, and I/O devices among competing processes.

- **System Calls**: Programming interfaces that allow user programs to request services from the operating system kernel, forming the boundary between user space and kernel space.

- **User Mode**: The unprivileged mode in which user applications run, with restrictions on accessing hardware resources directly.

- **Kernel Mode** (Privileged Mode): The mode in which the operating system kernel executes, with full access to all hardware resources.

- **Batch Processing**: Early OS approach where jobs were collected and processed in groups without user interaction.

- **Time-Sharing**: OS design allowing multiple users to interact with the computer simultaneously through terminals.

## Important Formulas and Theorems

There are no specific formulas in this conceptual chapter. However, understanding the relationships between concepts is essential:

- **System Call Categories**: Process Control (fork, exec, wait), File Management (open, read, write, close), Device Management (read, write, ioctl), Information Maintenance (getpid, gettime), Communication (pipe, socket).

## Key Points

- The operating system serves three primary functions: resource management, user interface provision, and system call interface.

- As a resource manager, the OS performs allocation, accounting, and protection of CPU, memory, storage, and I/O devices.

- User interfaces have evolved from CLI to GUI to touch-based, each with distinct advantages.

- System calls are the only mechanism for user programs to request kernel services and involve mode switching between user and kernel modes.

- OS evolution progressed from batch processing to time-sharing to modern multiprocessing systems.

- Modern operating systems must balance efficiency with convenience while ensuring reliability and security.

## Common Mistakes to Avoid

- Confusing system calls with function calls: System calls involve privilege mode transitions while function calls do not.

- Assuming GUI is the only user interface: Many servers and embedded systems use CLI exclusively due to lower resource requirements.

- Overlooking the resource protection aspect: The OS must prevent processes from interfering with each other's execution and data.

- Misunderstanding the dual nature of OS: It serves both users (convenience) and system (efficiency), not just one perspective.

## Revision Tips

1. Create a comparison table of CLI vs GUI vs Touch interfaces with pros and cons for each.

2. Memorize the five categories of system calls with at least two examples of each.

3. Draw a timeline of OS evolution from the 1950s to present, noting major milestones.

4. Practice explaining how the OS manages resources when multiple applications run simultaneously.

5. Review past DU examination questions on this topic to understand the exam pattern and frequently asked concepts.