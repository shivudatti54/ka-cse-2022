# Operating System Services and System Calls - Summary

## Key Definitions and Concepts

- **Operating System Services**: Essential functions provided by the OS including process management, memory management, file management, device management, security, networking, and information maintenance.

- **System Calls**: Programming interface that allows user applications to request services from the OS kernel. They represent the boundary between user mode and kernel mode.

- **User Mode**: Restricted execution mode where application programs run with limited privileges.

- **Kernel Mode**: Privileged mode where the OS kernel operates with full access to hardware and system resources.

- **Process Control Block (PCB)**: Data structure maintained by the OS containing all information about a process (PID, program counter, CPU registers, memory management info, I/O status).

- **File Descriptor**: Small non-negative integer that uniquely identifies an open file for the process.

## Important Formulas and Theorems

- Standard file descriptors: stdin = 0, stdout = 1, stderr = 2
- fork() returns 0 to child process, child's PID to parent, -1 on failure
- open() flags: O_CREAT (create), O_RDONLY (read), O_WRONLY (write), O_RDWR (read-write)

## Key Points

1. OS services enable efficient resource management and provide abstractions over hardware complexity.

2. System calls are the only way user programs can access kernel services and hardware resources.

3. The system call interface ensures security by preventing user programs from directly accessing privileged operations.

4. Process management system calls include fork(), exec(), wait(), exit(), getpid(), getppid().

5. File management system calls include open(), close(), read(), write(), lseek(), stat().

6. Device management system calls include read(), write(), ioctl() for device operations.

7. Communication system calls include pipe(), socket(), connect(), bind() for IPC and networking.

8. The system call execution involves: parameter setup → trap instruction → kernel execution → return to user mode.

9. Protection system calls include chmod(), chown(), umask() for security management.

10. Virtual memory and paging are memory management services that extend available memory using disk storage.

## Common Mistakes to Avoid

- Confusing OS services with system calls: services are the functionality, system calls are the interface to access them.
- Forgetting that fork() returns twice: once in parent with child's PID, once in child with 0.
- Not closing file descriptors after use, leading to resource leaks.
- Assuming system calls always succeed; always check return values for errors.
- Confusing the roles of different modes: kernel mode has privileges, user mode is restricted.

## Revision Tips

1. Practice writing C programs using system calls to reinforce theoretical concepts.

2. Create a table categorizing system calls by their functional area for quick reference.

3. Trace the execution flow of a simple fork() program to understand process creation.

4. Review how file descriptors work and remember standard file descriptors 0, 1, 2.

5. Relate concepts to real examples: opening a file in an editor involves multiple system calls.