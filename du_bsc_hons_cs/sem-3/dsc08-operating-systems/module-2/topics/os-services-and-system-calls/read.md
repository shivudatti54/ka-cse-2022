# Operating System Services and System Calls

## Introduction

An Operating System (OS) serves as the fundamental interface between computer hardware and user applications. To fulfill its role effectively, an operating system provides a comprehensive set of services that enable programs to execute efficiently, access resources safely, and interact with hardware components. Understanding these services and the mechanism through which user programs request them—known as system calls—is essential for any computer science student.

In the University of Delhi's Computer Science curriculum, this topic forms the backbone of understanding how application software interacts with the underlying hardware. The operating system acts as a resource manager, allocating CPU time, memory, and I/O devices among competing processes while maintaining system integrity and security. System calls provide the gateway through which this interaction occurs, making them a critical concept for both theoretical understanding and practical programming skills. This chapter explores the various services offered by modern operating systems and examines the system call interface in detail, with particular emphasis on examples relevant to UNIX/Linux environments commonly used in DU practical examinations.

## Key Concepts

### Operating System Services

Operating systems provide a wide range of services to both users and application programs. These services can be categorized into several fundamental groups that collectively ensure the smooth functioning of a computer system.

**Process Management** is one of the most critical services provided by any operating system. The OS must create, schedule, and terminate processes efficiently. It handles process synchronization to prevent race conditions, manages inter-process communication, and ensures fair CPU allocation among competing processes. The scheduler, a key component of process management, determines which process runs at any given time using algorithms like Round Robin, First-Come-First-Served, or Shortest Job Next. Modern operating systems also support multithreading, where multiple threads within a single process share resources like code and data segments while maintaining separate stack registers.

**Memory Management** service oversees the allocation and deallocation of memory space to processes. The OS must track which portions of memory are in use and which are free, allocate memory when processes request it, and deallocate memory when processes terminate. Techniques like paging, segmentation, and virtual memory allow the OS to provide each process with the illusion of having more memory than physically available. The memory management unit (MMU) hardware works in conjunction with the OS to translate virtual addresses to physical addresses, enabling memory protection and sharing.

**File Management** enables users and programs to store and retrieve data persistently. The OS maintains file system structures, manages free space, handles file naming conventions, and implements access control mechanisms. Operations like create, delete, read, write, open, and close are facilitated through the file management subsystem. The OS also implements directory structures that help organize files hierarchically and supports various file systems such as FAT32, NTFS, and ext4.

**Device Management** handles all communication between the CPU and peripheral devices through device drivers. The OS abstracts hardware complexities by providing a uniform interface for device access. Buffering, caching, and spooling are techniques employed to improve I/O performance. Device drivers translate generic I/O requests into device-specific commands, and the OS manages device sharing among multiple processes through scheduling and queuing mechanisms.

**Protection and Security** services ensure that system resources are accessed only by authorized users and processes. The OS implements authentication mechanisms (passwords, biometrics), access control lists (ACLs), and permission schemes. It prevents unauthorized access to memory, files, and devices, and protects against external threats through firewalls and intrusion detection systems.

**Networking** services enable communication between computers over a network. The OS provides protocols like TCP/IP, socket programming interfaces, and routing capabilities. Distributed systems rely heavily on these networking services to coordinate resources across multiple machines.

**Information Maintenance** services keep track of system time, date, configuration information, and statistics about CPU usage, memory utilization, and I/O operations. System calls allow programs to query and set this information.

### System Calls

System calls represent the fundamental interface through which user programs request services from the operating system kernel. Unlike regular function calls in application programs, system calls transition the CPU from user mode (privilege level 3) to kernel mode (privilege level 0), where privileged instructions can be executed. This transition is facilitated by the trap or syscall instruction, which saves the current state and transfers control to the kernel.

The system call interface acts as an abstraction layer that hides the complexities of hardware manipulation from application programmers. Instead of directly programming hardware devices, programmers use standardized system calls that the OS translates into appropriate hardware operations. This abstraction improves portability—programs written using system calls can run on different hardware platforms without modification.

**Types of System Calls** can be categorized based on the type of service they provide:

*Process Control* system calls manage process execution. Examples include `fork()` to create a new process, `exec()` to replace a process image, `wait()` to synchronize process execution, `exit()` to terminate a process, and `kill()` to send signals to processes. In UNIX systems, the fork() system call creates a child process by duplicating the parent process, with both processes continuing execution from the point of the fork.

*File Management* system calls handle file operations. Key calls include `open()` to open a file and obtain a file descriptor, `read()` to read data from a file, `write()` to write data to a file, `close()` to close an open file, `lseek()` to change the file offset, and `stat()` to obtain file metadata.

*Device Management* system calls request and release devices, read and write to devices, and handle device configuration. Calls like `ioctl()` provide device-specific control operations.

*Information Maintenance* system calls retrieve or set system data. Examples include `getpid()` to get process ID, `getuid()` to get user ID, `time()` to get current time, and `uname()` to get system name information.

*Communication* system calls enable inter-process communication through message passing or shared memory. Calls like `pipe()` create pipes, `socket()` create communication endpoints, `bind()` associate addresses with sockets, and `shmget()` allocate shared memory segments.

*Protection* system calls control access to resources. Calls like `chmod()` change file permissions, `chown()` change file ownership, and `setuid()` set user ID for the process.

### System Call Parameter Passing

When programs invoke system calls, they must pass parameters specifying exactly what operation to perform. Three common methods exist for passing parameters to system calls:

The simplest method uses **registers**—parameters are placed in predefined CPU registers before invoking the system call. The kernel reads these registers to obtain the required information. This method is efficient but limited by the number of available registers.

The **block or table** method stores parameters in a memory block, with the block's address passed in a register. This approach supports arbitrarily large amounts of data and is commonly used in modern operating systems.

The **stack** method pushes parameters onto the user-mode stack before the system call. The kernel then pops these parameters. However, kernel mode cannot always access user-mode stacks safely, making this method less common.

### API vs System Call

Application Programming Interfaces (APIs) and system calls are related but distinct concepts. An API is a collection of function definitions that programs can use to interact with a library or framework. For example, the C standard library (`libc`) provides functions like `printf()`, `malloc()`, and `fopen()`. These APIs internally invoke system calls to interact with the OS kernel.

The POSIX API is a standardized interface that provides portability across different UNIX-like systems. POSIX functions often map directly to system calls but may also involve additional processing. For instance, the `printf()` function calls `write()` system call internally but also handles formatting.

This layered approach—application → library function → system call → kernel—provides abstraction and portability. Programs can be compiled for different operating systems as long as the library implements the required API.

## Examples

### Example 1: Process Creation in UNIX

Consider a C program that creates a child process using the `fork()` system call:

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    
    printf("Before fork: Process ID = %d\n", getpid());
    
    pid = fork();
    
    if (pid < 0) {
        fprintf(stderr, "Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child Process: PID = %d, Parent PID = %d\n", 
               getpid(), getppid());
        execlp("/bin/ls", "ls", "-l", NULL);
    }
    else {
        // Parent process
        printf("Parent Process: PID = %d, Child PID = %d\n", 
               getpid(), pid);
        wait(NULL);
        printf("Child completed\n");
    }
    
    return 0;
}
```

**Step-by-step explanation:**

1. The parent process calls `fork()`, which creates an identical copy of the process
2. The kernel duplicates the parent's address space, creating a child process
3. `fork()` returns the child's PID to the parent and 0 to the child
4. The child process uses `execlp()` to replace its image with the `ls` command
5. The parent process calls `wait()` to wait for child completion
6. After child finishes, parent continues execution

This example demonstrates process control system calls: `fork()` for process creation, `execlp()` for program execution, `getpid()` for information retrieval, and `wait()` for synchronization.

### Example 2: File Operations

The following program demonstrates file management system calls by creating a file, writing data, and reading it back:

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    char buffer[100];
    const char *message = "Hello from Operating System Services!\n";
    
    // Create and open file using open() system call
    fd = open("test.txt", O_CREAT | O_WRONLY, 0644);
    
    if (fd < 0) {
        perror("Open failed");
        return 1;
    }
    
    // Write to file using write() system call
    write(fd, message, strlen(message));
    
    // Close file using close() system call
    close(fd);
    
    // Reopen for reading
    fd = open("test.txt", O_RDONLY);
    
    // Read from file using read() system call
    read(fd, buffer, 100);
    
    printf("Content read from file: %s", buffer);
    
    close(fd);
    
    return 0;
}
```

**Key system calls demonstrated:**
- `open()`: Creates/opens a file, returns file descriptor
- `write()`: Writes data to file using file descriptor
- `close()`: Releases the file descriptor
- `read()`: Reads data from file into buffer

The file descriptor is a small non-negative integer that the kernel uses to identify open files. By convention, file descriptors 0, 1, and 2 represent standard input, standard output, and standard error respectively.

### Example 3: Inter-Process Communication using Pipes

This example demonstrates communication system calls by creating a pipe between parent and child processes:

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pid_t pid;
    char parent_msg[] = "Message from parent to child";
    char child_buf[100];
    
    // Create pipe using pipe() system call
    if (pipe(pipefd) == -1) {
        perror("Pipe failed");
        return 1;
    }
    
    pid = fork();
    
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    }
    
    if (pid > 0) {
        // Parent process
        close(pipefd[0]);  // Close read end
        
        // Write to pipe using write() system call
        write(pipefd[1], parent_msg, strlen(parent_msg) + 1);
        close(pipefd[1]);  // Close write end
        
        wait(NULL);
    }
    else {
        // Child process
        close(pipefd[1]);  // Close write end
        
        // Read from pipe using read() system call
        read(pipefd[0], child_buf, 100);
        printf("Child received: %s\n", child_buf);
        
        close(pipefd[0]);  // Close read end
    }
    
    return 0;
}
```

**Step-by-step explanation:**
1. `pipe(pipefd)` creates a unidirectional communication channel
2. `pipefd[0]` is the read end, `pipefd[1]` is the write end
3. Parent closes unused read end, writes message to pipe
4. Child closes unused write end, reads message from pipe
5. Both processes close their respective ends when done

This demonstrates how the OS enables communication between processes that don't share memory.

## Exam Tips

1. **Distinguish between OS services and system calls**: Remember that services are high-level functionalities (like process management), while system calls are the programming interface to access those services (like fork(), exec()).

2. **Know the transition from user mode to kernel mode**: System calls involve a mode switch from user mode (less privileged) to kernel mode (more privileged) using trap or syscall instructions.

3. **Remember the five main categories of system calls**: Process control, file management, device management, information maintenance, and communication/protection.

4. **Understand file descriptors**: File descriptors are small integers used to identify open files. Remember that 0, 1, and 2 are reserved for standard input, output, and error respectively.

5. **Difference between fork() and exec()**: fork() creates a new process by duplicating the existing process, while exec() replaces the current process image with a new program.

6. **Parameter passing methods**: Be familiar with register-based, block/table-based, and stack-based parameter passing for system calls.

7. **API vs System Call distinction**: Remember that library functions (like printf) are APIs that may internally call system calls (like write), providing abstraction and portability.

8. **UNIX/Linux system calls are commonly tested**: Be comfortable with basic UNIX system calls like open, read, write, close, fork, exec, pipe, and wait for the practical examination.