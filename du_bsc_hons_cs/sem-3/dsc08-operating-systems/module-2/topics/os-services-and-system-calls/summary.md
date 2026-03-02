# Operating System Services and System Calls - Summary

## Key Definitions and Concepts

- **Operating System Services**: Functions provided by the OS to enable efficient execution of user programs, including process management, memory management, file management, device management, protection, and networking.

- **System Calls**: Programming interface that allows user programs to request services from the OS kernel; involves transition from user mode to kernel mode using trap/syscall instructions.

- **User Mode**: Unprivileged mode where application programs execute with limited access to hardware resources.

- **Kernel Mode**: Privileged mode where the OS kernel executes with full access to all hardware instructions and memory.

- **File Descriptor**: A small non-negative integer used by the kernel to identify open files for a process.

## Important Formulas and Theorems

- Standard file descriptors: stdin=0, stdout=1, stderr=2
- Process creation: `fork()` returns child PID to parent, 0 to child
- Pipe creation: `pipe(int pipefd[2])` where pipefd[0]=read, pipefd[1]=write

## Key Points

- Operating systems provide six main categories of services: process management, memory management, file management, device management, protection/security, and networking.

- System calls are the only way user programs can request kernel services; they provide hardware abstraction and system security.

- Process control system calls include fork(), exec(), wait(), exit(), and kill() for creating and managing processes.

- File management system calls include open(), read(), write(), close(), lseek(), and stat() for file operations.

- System call parameter passing uses registers, block/table method, or stack-based approaches.

- APIs like POSIX provide portable interfaces that internally invoke system calls, enabling program portability across different operating systems.

- fork() creates a duplicate child process, while exec() replaces the current process image with a new program.

## Common Mistakes to Avoid

- Confusing system calls with library functions; library functions like printf() internally call system calls like write().

- Forgetting that fork() returns twice—once in parent with child's PID and once in child with value 0.

- Not closing file descriptors after use, which can lead to resource leaks.

- Assuming system calls always succeed; must check return values for errors.

## Revision Tips

1. Practice writing C programs using fork(), exec(), pipe(), open(), read(), and write() system calls.

2. Create a table listing each system call category with 2-3 examples and their purposes.

3. Trace through a simple fork()-exec() sequence to understand process creation and program replacement.

4. Review the difference between user mode and kernel mode transitions during system calls.

5. Remember that file descriptors 0, 1, 2 are reserved for standard input, output, and error respectively.