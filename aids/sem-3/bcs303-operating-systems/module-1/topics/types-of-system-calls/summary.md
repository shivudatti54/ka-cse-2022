# Types of System Calls - Summary

## Key Definitions

- **System Call**: A programmatic request made by a user program to the operating system kernel for privileged services or resources.

- **Kernel Mode**: A privileged execution mode where the operating system has full access to all hardware resources and memory.

- **User Mode**: A restricted execution mode where application programs run with limited privileges and cannot directly access hardware.

- **Mode Switch**: The transition between user mode and kernel mode that occurs during system call execution.

- **Inter-Process Communication (IPC)**: The mechanism by which processes communicate with each other, facilitated through communication system calls.

## Important Formulas

- System call execution involves the sequence: User call → Library wrapper → Mode switch → Kernel execution → Return value → Mode switch back to user.

- Parameters for system calls are typically passed through: CPU registers, stack, or a parameter block whose address is passed in a register.

## Key Points

1. System calls provide the boundary between user space and kernel space in operating systems.

2. There are six major types of system calls: process control, file management, device management, information maintenance, communication, and protection.

3. Process control system calls handle process creation (fork), execution (exec), termination (exit), and synchronization (wait).

4. File management system calls manage file operations including create, open, read, write, and close operations.

5. Device management system calls abstract hardware devices as special files for uniform access.

6. Information maintenance system calls retrieve system data including time, date, process attributes, and system information.

7. Communication system calls establish inter-process communication channels including pipes, message queues, and sockets.

8. Protection system calls implement security by controlling resource access through permissions and privileges.

9. Each system call is assigned a unique number that is used by the kernel to identify the requested operation.

10. The actual system call implementations and numbers vary significantly between different operating systems.

## Common Mistakes

1. Confusing library functions with system calls—library functions like printf() often make system calls internally, but they are not system calls themselves.

2. Forgetting that system calls involve a hardware-enforced privilege transition, which has overhead compared to regular function calls.

3. Misclassifying system calls into wrong categories—for example, treating chmod() as a file management call when it is actually a protection system call.

4. Assuming all operating systems use the same system call numbers or interface—they differ significantly between UNIX, Linux, and Windows.

5. Ignoring error handling—system calls return error codes that must be checked, and negative return values typically indicate failures.