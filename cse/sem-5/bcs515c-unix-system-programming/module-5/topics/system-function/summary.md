# System Calls and System Functions - Summary

## Key Definitions and Concepts

- **System Call**: A programmatic request made by a user program to the operating system kernel to perform privileged operations. The only legal way to access kernel services in UNIX systems.

- **File Descriptor**: A non-negative integer assigned by the kernel to identify an open file for a process. Standard file descriptors: 0 (stdin), 1 (stdout), 2 (stderr).

- **Process**: An executing program with its own address space, created using fork() system call.

- **Kernel Mode**: Privileged execution mode where all instructions are allowed and hardware protection can be bypassed.

- **User Mode**: Restricted execution mode where user programs run with limited privileges.

## Important Formulas and Theorems

- **fork() Return Value**: Returns child's PID to parent, returns 0 to child, returns -1 on failure.

- **File Permissions (octal)**: 0644 = rw-r--r-- (owner can read/write, others can read).

- **wait() Status Macros**: WIFEXITED(status) - checks if child terminated normally; WEXITSTATUS(status) - extracts exit status.

## Key Points

1. System calls are categorized into six groups: Process Control, File Manipulation, Device Management, Information Maintenance, Communication, and Protection.

2. fork() creates a new process by duplicating the parent process; exec() family replaces the process image with a new program.

3. open() returns a file descriptor; read() and write() use file descriptors for I/O operations.

4. System calls involve mode switch from user mode to kernel mode using trap or syscall instructions.

5. wait() blocks parent until child terminates; exit() terminates a process with an exit status.

6. Error handling: system calls return -1 on failure and set the global errno variable.

7. File descriptors are process-specific resources that must be closed using close() when no longer needed.

8. pipe() creates a unidirectional communication channel between parent and child processes.

## Common Mistakes to Avoid

1. Not checking return values of system calls, leading to unhandled errors.

2. Confusing fork() with exec(): fork() creates a copy, exec() replaces the program.

3. Forgetting to close file descriptors, causing resource leaks.

4. Not using proper error handling with perror() or strerror() functions.

5. Confusing file descriptors with file pointers (FILE \* from stdio library).

## Revision Tips

1. Practice writing C programs using system calls - hands-on practice is essential.

2. Remember the six categories of system calls with at least two examples each.

3. Understand the flow: fork() returns twice, exec() replaces program image, wait() blocks parent.

4. Memorize standard file descriptors: 0, 1, 2 for stdin, stdout, stderr.

5. Review previous question papers to understand the exam pattern and important topics.
