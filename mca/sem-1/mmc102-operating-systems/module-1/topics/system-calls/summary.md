# System Calls - Summary

## Key Definitions and Concepts

- **System Call**: A programmatic request made by a user program to the operating system kernel to perform privileged operations such as file I/O, process management, and memory allocation

- **User Mode**: Execution mode with limited privileges where user applications run without direct access to hardware or critical system resources

- **Kernel Mode**: Privileged execution mode where the operating system kernel operates with full access to all system resources and hardware

- **System Call Interface**: The standardized mechanism through which applications request kernel services, typically involving a system call number, parameters, and a trap instruction

- **File Descriptor**: A small non-negative integer that serves as an index into the per-process file descriptor table, representing an open file or I/O resource

## Important Formulas and Theorems

- System call return value convention: Negative or -1 indicates error; zero or positive indicates success with the value being the requested data (file descriptor, bytes read/written, process ID)

- Process creation: fork() returns 0 to child process and child's PID to parent process; fork() returns -1 on failure

- File permissions (octal): Owner permissions (read=4, write=2, execute=1), group permissions, and other permissions combine additively

## Key Points

- System calls provide the only controlled pathway from user space to kernel space, maintaining system security and stability

- There are six major categories of system calls: process control, file management, device management, information maintenance, communication, and protection

- The fork() system call creates a new process by duplicating the parent process, while exec() family replaces the process image with a new program

- File operations follow a lifecycle: open() → read()/write() → close(), with each operation using the file descriptor returned by open()

- Pipes created by pipe() provide unidirectional inter-process communication, with the parent typically closing the read end and the child closing the write end

- System calls use registers or memory structures to pass parameters, with the system call number identifying the requested operation

- Error handling in system calls involves checking return values and examining the errno variable for specific error conditions

- The mode switch during system call execution involves saving processor state, transitioning to kernel mode, executing the handler, and returning to user mode

## Common Mistakes to Avoid

- Confusing fork() with exec(): fork() creates a new process, while exec() replaces the current process with a new program

- Forgetting to close file descriptors after use, which can lead to resource leaks

- Not checking return values from system calls for errors, causing programs to continue execution with failed operations

- Confusing the roles of pipe ends: pipefd[0] is for reading, pipefd[1] is for writing

- Assuming system calls always succeed without proper error handling and errno examination

## Revision Tips

1. Create a table mapping common system calls to their categories and purposes for quick reference during examination

2. Practice writing and tracing programs that use fork(), pipe(), and file I/O system calls to build practical understanding

3. Memorize the return value conventions: fork() returns 0 (child), positive (parent, child's PID), negative (failure); file operations return -1 (failure) or bytes processed

4. Review the sequence of events during a system call invocation, focusing on the user-to-kernel mode transition

5. Solve previous years' University of Delhi examination questions on system calls to understand the question patterns and expected answer depth