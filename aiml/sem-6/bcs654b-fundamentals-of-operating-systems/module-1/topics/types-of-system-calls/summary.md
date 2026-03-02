# Types Of System Calls - Summary

## Key Definitions

- **System Call**: A programming interface that allows user programs to request services from the operating system kernel
- **File Descriptor**: A small non-negative integer that uniquely identifies an open file within a process
- **Kernel Mode**: A privileged CPU execution mode where all instructions are allowed and hardware can be accessed directly
- **User Mode**: A restricted CPU execution mode where only non-privileged instructions can be executed
- **Inter-Process Communication (IPC)**: Mechanisms that allow processes to communicate and synchronize with each other

## Important Formulas

- **Standard File Descriptors**: stdin = 0, stdout = 1, stderr = 2
- **fork() Return Values**: Returns 0 to child process, returns child's PID (>0) to parent, returns -1 on failure
- **umask Calculation**: Default file permission = requested_permission AND NOT umask

## Key Points

1. System calls provide the interface between user applications and the operating system kernel
2. There are six major types: Process Control, File Management, Device Management, Information Maintenance, Communication, and Protection
3. Process control system calls (fork, exec, wait, exit) manage process lifecycle
4. File management system calls (open, read, write, close) handle file operations
5. Device management system calls interact with hardware devices
6. Information maintenance system calls retrieve system and process information
7. Communication system calls enable IPC and network communication
8. Protection system calls enforce security through permissions and ownership
9. System calls involve a transition from user mode to kernel mode
10. File descriptors are used to reference open files and devices

## Common Mistakes

1. Confusing fork() return values (child gets 0, parent gets child's PID)
2. Forgetting to check return values for errors in system calls
3. Not closing file descriptors, leading to resource leaks
4. Confusing the roles of different types of system calls
5. Assuming system calls always succeed without error handling