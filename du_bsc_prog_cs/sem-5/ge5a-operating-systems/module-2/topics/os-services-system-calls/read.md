# Operating System Services and System Calls

## Introduction

An Operating System (OS) serves as the fundamental interface between computer hardware and user applications. While users interact with computers through graphical user interfaces and application software, the operating system performs a complex set of services behind the scenes to make this interaction possible. Understanding these services and the mechanism through which user programs request these services—known as system calls—is fundamental to comprehending how modern computing systems function.

Operating system services encompass a broad range of functionalities that both users and application programs depend upon daily. From file management and memory allocation to process control and device communication, these services form the backbone of system functionality. System calls, on the other hand, provide the programming interface through which user applications communicate with the kernel of the operating system. This distinction between user mode and kernel mode is crucial for understanding system security and resource management.

For students preparing for DU semester examinations, this topic holds significant weight as it forms the foundation for understanding process management, memory management, and file systems—all critical areas in operating system design and implementation. The concepts covered here also appear frequently in competitive examinations and technical interviews, making thorough understanding essential for career advancement in computer science.

## Key Concepts

### Operating System Services

Operating systems provide several essential services that can be categorized into multiple groups based on their functionality:

**1. Process Management**
Process management is one of the most fundamental services provided by any operating system. The OS is responsible for creating, scheduling, and terminating processes. Each process represents a program in execution, and the OS must allocate CPU time, manage process states (new, ready, running, waiting, terminated), and handle inter-process communication. The process control block (PCB) maintains all information about each process, including process ID, program counter, CPU registers, memory management information, and I/O status information.

**2. Memory Management**
Memory management service controls how computer memory is allocated and deallocated to processes. The OS tracks which portions of memory are in use and which are free, decides which process gets memory and how much, and allocates memory when requested. Modern operating systems employ various memory management techniques including paging, segmentation, and virtual memory. The OS must ensure memory protection—preventing one process from accessing memory belonging to another process—and implement memory allocation strategies like first-fit, best-fit, and worst-fit.

**3. File Management**
File management is crucial for organizing and accessing data on storage devices. The OS provides operations for creating, deleting, reading, and writing files. It maintains file system structure, manages free space on storage devices, and implements access control to protect files from unauthorized access. Common file systems include FAT32, NTFS, ext4, and APFS, each with different organizational strategies and performance characteristics.

**4. Device Management**
Operating systems manage hardware devices through device drivers. The OS handles device requests by buffering data, caching information, and scheduling operations to optimize performance. Device management includes recognizing devices, allocating memory buffers, handling interrupts, and providing uniform interfaces for different device types. This abstraction allows application programs to interact with devices without knowing hardware-specific details.

**5. Security and Protection**
The OS implements security mechanisms to protect system resources from unauthorized access. This includes user authentication (passwords, biometrics), permission management (read, write, execute), and access control lists. The protection system ensures that processes operate within their authorized boundaries and cannot interfere with other processes or the operating system itself.

**6. Networking**
Modern operating systems provide networking services that enable communication between computers. This includes protocol implementation (TCP/IP, UDP), socket programming interfaces, routing, and network management utilities. These services allow distributed computing and internet connectivity.

**7. Information Maintenance**
The OS maintains various system information including time, date, performance statistics, error messages, and debugging information. System calls allow programs to retrieve and set this information.

### System Calls

System calls are the programming interface through which user processes request services from the operating system kernel. They represent the boundary between user space (where application programs run) and kernel space (where the OS kernel operates). When a program needs OS services, it executes a system call, which triggers a transition from user mode to kernel mode.

**Types of System Calls**

System calls can be categorized based on their functionality:

**Process Control System Calls**
- fork(): Creates a new process
- exec(): Replaces the current process image
- wait(): Makes parent process wait for child termination
- exit(): Terminates a process
- getpid(): Returns process ID
- getppid(): Returns parent process ID

**File Management System Calls**
- open(): Opens a file
- close(): Closes a file
- read(): Reads data from file
- write(): Writes data to file
- lseek(): Repositions file pointer
- stat(): Gets file status information

**Device Management System Calls**
- read(): Reads from device
- write(): Writes to device
- ioctl(): Performs device-specific operations

**Information Maintenance System Calls**
- getpid(): Gets process ID
- getuid(): Gets user ID
- getgid(): Gets group ID
- time(): Gets current time
- uname(): Gets system name

**Communication System Calls**
- pipe(): Creates a pipe for inter-process communication
- socket(): Creates communication endpoint
- connect(): Connects to remote socket
- bind(): Binds socket to address

**Protection System Calls**
- chmod(): Changes file permissions
- chown(): Changes file owner
- umask(): Sets file creation mask

### System Call Interface

The system call interface serves as the bridge between user applications and operating system services. When a program makes a system call, the following sequence typically occurs:

1. The application calls a library function (like printf or read)
2. The library function prepares parameters and places them in designated registers
3. The library function executes a special instruction (like syscall on x86-64) that triggers a transition to kernel mode
4. The kernel identifies the requested service from a system call number
5. The kernel executes the requested service
6. Control returns to user mode with the result

Parameters for system calls are typically passed through CPU registers. The system call number identifies which service is being requested, while additional registers hold any required arguments.

## Examples

### Example 1: Process Creation in C

Consider a simple program that demonstrates process creation using the fork() system call:

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    printf("Before fork - Process ID: %d\n", getpid());
    
    pid = fork();
    
    if (pid < 0) {
        // Fork failed
        fprintf(stderr, "Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child process - PID: %d, Parent PID: %d\n", 
               getpid(), getppid());
    }
    else {
        // Parent process
        printf("Parent process - PID: %d, Child PID: %d\n", 
               getpid(), pid);
        wait(NULL); // Wait for child to complete
    }
    
    printf("After fork - Process ID: %d\n", getpid());
    return 0;
}
```

**Step-by-step execution:**
1. The parent process prints its PID (e.g., 1234)
2. fork() system call is invoked, creating a child process
3. In the child process, fork() returns 0, so child-specific code executes
4. In the parent process, fork() returns child's PID (e.g., 1235)
5. Parent waits for child using wait() system call
6. Both processes print their final messages

### Example 2: File Operations

This example demonstrates basic file management system calls:

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    char buffer[] = "Hello, Operating Systems!";
    char read_buffer[50];
    
    // Create and open file using open() system call
    fd = open("test.txt", O_CREAT | O_WRONLY, 0644);
    
    if (fd < 0) {
        perror("Error opening file");
        return 1;
    }
    
    // Write to file using write() system call
    write(fd, buffer, strlen(buffer));
    close(fd); // Close file using close() system call
    
    // Open file again for reading
    fd = open("test.txt", O_RDONLY);
    
    if (fd < 0) {
        perror("Error opening file");
        return 1;
    }
    
    // Read from file using read() system call
    read(fd, read_buffer, strlen(buffer));
    read_buffer[strlen(buffer)] = '\0';
    
    printf("Read from file: %s\n", read_buffer);
    close(fd);
    
    return 0;
}
```

**System calls used:**
- open(): Creates file or opens existing file; returns file descriptor
- write(): Writes data to file using file descriptor
- close(): Closes the file descriptor
- read(): Reads data from file into buffer

### Example 3: Inter-Process Communication via Pipe

This example demonstrates pipe creation for parent-child communication:

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pid_t pid;
    char write_msg[] = "Message from parent";
    char read_msg[50];
    
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
        close(pipefd[0]); // Close read end
        
        // Write to pipe using write() system call
        write(pipefd[1], write_msg, strlen(write_msg) + 1);
        close(pipefd[1]); // Close write end
        
        wait(NULL);
    }
    else {
        // Child process
        close(pipefd[1]); // Close write end
        
        // Read from pipe using read() system call
        read(pipefd[0], read_msg, 50);
        printf("Child received: %s\n", read_msg);
        close(pipefd[0]); // Close read end
    }
    
    return 0;
}
```

## Exam Tips

1. **Understand the difference between OS services and system calls**: OS services are the functionalities provided, while system calls are the programming interface to access those services.

2. **Memorize common system calls**: Be familiar with at least 5-6 system calls from each category (process, file, device, information, communication, protection).

3. **Know the transition mechanism**: Understand how user mode switches to kernel mode during system call execution and why this security boundary exists.

4. **Difference between kernel and user mode**: The kernel has full access to hardware and system resources, while user programs run in restricted mode with limited privileges.

5. **Real-world examples**: When explaining OS services, connect them to familiar computer operations like opening a file or running an application.

6. **Process states and system calls**: Understand which system calls cause process state transitions (e.g., wait() moves process from running to blocked state).

7. **File descriptors**: Remember that file descriptors are small non-negative integers used to identify open files; stdin, stdout, and stderr have descriptors 0, 1, and 2 respectively.

8. **Be prepared for diagram questions**: Draw and explain the system call execution flow if asked in the exam.