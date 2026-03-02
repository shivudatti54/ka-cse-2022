# OS Structure, Services, and System Calls

## Introduction
Modern operating systems form the backbone of computing systems, managing hardware resources and providing essential services to applications. Understanding OS architecture is critical for system programmers and software developers working on performance-critical applications. The structure of an operating system determines its reliability, security, and maintainability - key concerns in enterprise environments and cloud computing infrastructures.

This topic covers three fundamental aspects: 1) Organizational structures of operating systems (monolithic, layered, microkernel), 2) Core services provided to applications and users, and 3) System call mechanisms that enable user-space programs to access kernel functionalities. These concepts form the foundation for advanced topics in process management, device drivers, and system security.

With the rise of containerization technologies and IoT devices, knowledge of OS architecture has become particularly valuable. For instance, Docker leverages Linux namespaces and cgroups - features directly tied to OS services and system calls. Understanding these low-level mechanisms enables developers to optimize application performance and troubleshoot complex system interactions.

## Key Concepts

**1. OS Structural Models**
- *Monolithic Architecture*: Single address space design (e.g., traditional UNIX). All components (scheduler, memory manager, file system) run in kernel space
- *Layered Approach*: Hierarchical organization with strict interfaces between layers (THE OS). Each layer only uses services from lower layers
- *Microkernel*: Minimal kernel with most services in user space (Mach, QNX). Uses message passing for IPC
- *Modular (Hybrid)*: Loadable kernel modules (Linux). Combines monolithic efficiency with microkernel flexibility

**2. Essential OS Services**
- Process Management: Creation/termination, scheduling, synchronization
- Memory Management: Allocation, virtual memory, swapping
- File System Management: File creation/deletion, directory services
- I/O System Management: Device drivers, buffering, spooling
- Protection and Security: Access control, authentication
- Networking: TCP/IP stack implementation, socket APIs

**3. System Call Implementation**
- Interface between user applications and OS kernel
- Types: Process control (fork, exec), file management (open, read), device management (ioctl), information maintenance (getpid), communication (pipe)
- Execution Flow: User mode → Trap instruction → Switch to kernel mode → Dispatch table lookup → Kernel routine execution → Return to user mode
- Parameter Passing: Registers, block/table in memory, stack

## Examples

**Example 1: Process Creation via fork()**
```c
#include <unistd.h>
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("Child process (PID %d)\n", getpid());
    } else {
        printf("Parent process (PID %d)\n", getpid());
    }
    return 0;
}
```
*Step-by-Step:*
1. User program executes fork() system call
2. CPU switches to kernel mode via software interrupt (int 0x80 on x86)
3. Kernel creates duplicate process structure
4. Returns twice: 0 to child, PID to parent
5. Both processes resume execution in user mode

**Example 2: File Read Operation**
```c
int fd = open("data.txt", O_RDONLY);
char buffer[1024];
ssize_t bytes_read = read(fd, buffer, sizeof(buffer));
```
*System Call Flow:*
1. open() validates path and checks permissions
2. read() checks file descriptor validity
3. Kernel copies data from disk cache to user buffer
4. Returns number of bytes actually read

**Example 3: Interprocess Communication (pipe)**
```c
int pipefd[2];
pipe(pipefd);
if (fork() == 0) {
    close(pipefd[0]);  // Close read end
    write(pipefd[1], "Hello", 6);
} else {
    close(pipefd[1]);
    read(pipefd[0], buf, 6);
    printf("Received: %s\n", buf);
}
```
*Kernel Operations:*
1. Allocates pipe buffer in kernel memory
2. Manages reader/writer synchronization
3. Implements blocking/non-blocking I/O semantics

## Exam Tips
1. Focus on differences between monolithic vs microkernel architectures (pros/cons)
2. Memorize system call numbers for Linux: __NR_open (2), __NR_read (0), __NR_write (1)
3. Understand complete lifecycle of a system call: user space → kernel transition → dispatch → return
4. Be prepared to diagram layered OS structure with actual layer names (THE OS layers)
5. Practice converting C library calls to actual system calls (e.g., printf → write → sys_write)
6. Know POSIX standards for system call interfaces (e.g., fork() behavior specifications)
7. Study real-world examples: Windows NT (hybrid kernel) vs Linux (monolithic with modules)