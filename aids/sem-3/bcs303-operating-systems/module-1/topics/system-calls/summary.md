# System Calls - Summary

## Key Definitions

- **System Call**: A programmatic request made by a user program to the operating system kernel for services requiring privileged access
- **Kernel Mode**: The privileged execution mode of the processor where all instructions and memory are accessible
- **User Mode**: The restricted execution mode where applications run with limited privileges
- **System Call Number**: A unique identifier assigned to each system call used for dispatching
- **Trap**: A software-generated interrupt that transfers control from user mode to kernel mode

## Important Formulas

- **System Call Execution Flow**: User Call → Library Wrapper → Kernel Trap → Handler Execution → Return to User
- **Process Creation**: Parent PID (fork) → Child PID (new) → Exec replaces image → Exit returns status
- **File Operations**: Open returns fd → Read/Write use fd → Close releases fd

## Key Points

1. System calls are the only from user space to kernel space
2. They provide controlled access to hardware and protected system resources
3. The transition from user to kernel mode involves a trap or exception mechanism
4. Each system call has a unique number used for identification and dispatching
5. Parameters are typically passed through registers or stack before the trap
6. Common system call categories: Process Control, File Management, Device Management, Information Maintenance, Communication, and Protection
7. Library functions often provide higher-level abstractions over system calls
8. System calls return status values and set errno on failure
9. The number and nature of system calls varies between operating systems

## Common Mistakes

1. Confusing library functions with system calls—printf is NOT a system call, but read is
2. Forgetting to check return values from system calls for errors
3. Not closing file descriptors after opening files, leading to resource leaks
4. Misunderstanding that fork creates a new process with its own address space
5. Assuming all function calls in kernel space are system calls—some are internal kernel functions
