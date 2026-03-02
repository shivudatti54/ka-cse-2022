# Types of System Calls


## Table of Contents

- [Types of System Calls](#types-of-system-calls)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What Are System Calls?](#what-are-system-calls)
  - [The System Call Interface](#the-system-call-interface)
  - [Categories of System Calls](#categories-of-system-calls)
- [Examples](#examples)
  - [Example 1: Process Creation Using fork() and exec()](#example-1-process-creation-using-fork-and-exec)
  - [Example 2: File Operations](#example-2-file-operations)
  - [Example 3: Inter-Process Communication Using Pipes](#example-3-inter-process-communication-using-pipes)
- [Exam Tips](#exam-tips)

## Introduction

System calls represent the fundamental interface between user applications and the operating system kernel. When a user program requires services from the operating system—such as reading from a file, creating a new process, or allocating memory—it must invoke a system call. These calls provide the boundary between user space (where applications run) and kernel space (where the operating system executes with privileged access). Understanding system calls is essential for any computer science student because they form the backbone of operating system functionality and enable the secure, controlled interaction between unprivileged user programs and the protected kernel resources.

In modern operating systems like UNIX, Linux, and Windows, system calls serve as the only legal gateway for user programs to access hardware and system resources. Without system calls, applications would have no means of performing essential operations like I/O, process management, or memory allocation. The operating system kernel maintains system integrity and security by mediating all such requests through system calls, ensuring that no user program can directly access hardware or compromise system stability. This mechanism allows the operating system to enforce security policies, manage resource allocation, and provide abstract interfaces to hardware.

## Key Concepts

### What Are System Calls?

System calls are programming interfaces that allow user-space applications to request services from the operating system's kernel. They are the means by which user programs transition from unprivileged mode (user mode) to privileged mode (kernel mode) to perform operations that require elevated permissions. When a system call is invoked, the processor switches from user mode to kernel mode, executes the requested operation, and returns control to the user program along with the operation's result.

The system call interface is typically provided through a library (such as libc in UNIX/Linux systems) that wraps the low-level assembly instructions needed to trigger the system call transition. From the programmer's perspective, system calls appear as regular function calls, but internally they involve a context switch and privileged execution. Each system call is identified by a unique number (system call number) that the kernel uses to determine which function to execute.

### The System Call Interface

The system call interface operates through a well-defined mechanism. In the x86 architecture, for example, a software interrupt (INT 0x80 on older systems) or the SYSENTER/SYSCALL instructions are used to transition from user mode to kernel mode. The calling program places the system call number in a designated register (typically EAX on x86) and passes arguments in other registers (EBX, ECX, EDX, ESI, EDI, EBP). The kernel then validates these arguments, executes the requested operation, and returns a status code in EAX.

This mechanism ensures that the kernel maintains complete control over what operations user programs can perform. The kernel can validate all arguments, check permissions, and ensure that the requested operation does not violate system policies or compromise security. This controlled entry point is what makes operating system protection possible.

### Categories of System Calls

System calls are broadly categorized into six major types based on the functionality they provide:

#### 1. Process Control System Calls

Process control system calls manage the creation, termination, and control of processes. These include operations for creating new processes (fork in UNIX), terminating processes (exit), loading and executing programs (exec family), waiting for process termination (wait), and process synchronization primitives.

The fork() system call creates a new process by duplicating the calling process. The child process receives a copy of the parent's address space, and both processes continue execution from the point where fork() returns. The parent process receives the child's process ID, while the child process receives zero. This mechanism is fundamental to UNIX process management and is used extensively in shell pipelines and server applications.

The exec family of system calls (execl, execv, execle, execve, execlp, execvp) replaces the current process image with a new program. After a successful exec, the process continues execution but with a completely new program and address space. Combined with fork(), exec() enables the UNIX concept of process creation—fork creates a new process, and exec loads a new program into that process.

The wait() system call allows a parent process to synchronize with its children by blocking until a child terminates. It also allows the parent to retrieve the child's exit status. The exit() system call terminates the calling process and returns an exit status to its parent.

#### 2. File Management System Calls

File management system calls handle file operations such as creating, opening, reading, writing, and deleting files. These include open(), close(), read(), write(), lseek(), stat(), chmod(), and mkdir().

The open() system call opens a file and returns a file descriptor—a small non-negative integer that identifies the file in subsequent operations. The file descriptor is used as an index into the process's file descriptor table, which maintains information about all open files. The open() function takes parameters including the file path, flags (specifying how the file should be opened—read-only, write-only, read-write, create, append, etc.), and optional permissions.

The read() system call reads data from an open file into a buffer. It takes the file descriptor, buffer address, and number of bytes to read as parameters, and returns the number of bytes actually read. Similarly, write() writes data from a buffer to an open file. The lseek() system call repositions the file offset, enabling random access to files.

The creat() system call creates new files, while unlink() removes existing files. The stat() system call retrieves file metadata such as size, permissions, timestamps, and ownership information. The chmod() and chown() system calls modify file permissions and ownership, respectively.

#### 3. Device Management System Calls

Device management system calls handle communication with hardware devices. In UNIX systems, devices are treated as special files, allowing the same file operations (read, write, open, close) to be used for device I/O. These include ioctl() for device-specific control operations, and the standard file operations applied to device files.

The ioctl() system call is particularly important as it provides a catch-all mechanism for device-specific operations that do not fit the standard read/write model. It is used to query and set device parameters, configure hardware, and perform device-specific control functions. For example, ioctl() is used to set terminal window size, configure network interface parameters, and control tape drives.

Device files are categorized as block devices (which allow random access in fixed-size blocks, like hard drives) and character devices (which handle data as a stream of characters, like keyboards and terminals). The operating system provides device drivers that translate these generic operations into device-specific commands.

#### 4. Information Maintenance System Calls

Information maintenance system calls retrieve or modify system and process information. These include getpid() (get process ID), getuid() (get user ID), getgid() (get group ID), uname() (get system information), time() (get current time), and getrlimit()/setrlimit() (manage resource limits).

The getpid() system call returns the process ID of the calling process, while getppid() returns the parent process ID. These identifiers are essential for process management and inter-process communication. The getuid() and getgid() calls return the real and effective user and group IDs, which determine the process's permissions and access rights.

The uname() system call retrieves system identification information including the operating system name, version, release, and hardware type. The time() system call returns the current time as seconds since the Unix epoch (January 1, 1970). The getrlimit() and setrlimit() system calls allow processes to query and modify resource limits such as maximum file size, maximum number of open files, and maximum CPU time.

#### 5. Communication System Calls

Communication system calls enable inter-process communication (IPC) and network communication. These include pipe() for creating pipes, socket() for creating communication endpoints, connect() for establishing network connections, bind() for binding sockets to addresses, listen() for listening for connections, accept() for accepting connections, and send()/recv() for data transfer.

The pipe() system call creates a unidirectional communication channel, returning two file descriptors—one for reading and one for writing. Pipes are fundamental to UNIX shell pipelines, allowing the output of one process to be connected to the input of another. Named pipes (FIFO) extend this concept by allowing unrelated processes to communicate through a named file system entry.

Socket-based communication provides more sophisticated IPC mechanisms. The socket() system call creates a communication endpoint and returns a socket descriptor. The connect() client establishes a connection to a remote socket, while the server uses listen() and accept() to accept incoming connections. Once connected, send() and recv() (or write() and read()) transfer data between processes or across a network.

#### 6. Protection System Calls

Protection system calls control access to system resources and implement security policies. These include chmod() (change file permissions), chown() (change file ownership), umask() (set file creation mask), setuid()/setgid() (set user/group IDs), and capabilities management.

The chmod() system call modifies the permission bits of a file, controlling who can read, write, or execute it. The permission scheme uses nine bits divided into three sets: owner, group, and others, each with read (r), write (w), and execute (x) permissions. Additionally, special bits setuid, setgid, and sticky bit modify the execution behavior.

The setuid() and setgid() system calls allow processes to change their effective user and group IDs. The setuid bit on an executable file causes the process to run with the file owner's UID rather than the user's UID, enabling controlled privilege escalation for system utilities that need elevated permissions.

## Examples

### Example 1: Process Creation Using fork() and exec()

Consider a simple C program that creates a child process to execute the "ls" command:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        // Fork failed
        perror("fork failed");
        exit(1);
    }
    else if (pid == 0) {
        // Child process
        execlp("ls", "ls", "-l", NULL);
        // If exec succeeds, this code is never reached
        perror("exec failed");
        exit(1);
    }
    else {
        // Parent process
        int status;
        waitpid(pid, &status, 0);
        printf("Child process completed\n");
    }
    
    return 0;
}
```

In this example:
1. The fork() system call creates a new process
2. The parent receives the child's PID (> 0), while the child receives 0
3. The child calls execlp() to replace its address space with the "ls -l" program
4. The parent calls waitpid() to wait for the child to complete
5. The parent retrieves the child's exit status through the status variable

### Example 2: File Operations

This example demonstrates basic file management system calls:

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Create and open a file
    int fd = open("test.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Write to the file
    char buffer[] = "Hello, System Calls!";
    ssize_t bytes_written = write(fd, buffer, sizeof(buffer));
    
    if (bytes_written < 0) {
        perror("write failed");
        close(fd);
        return 1;
    }
    
    // Close the file
    close(fd);
    printf("Written %zd bytes to file\n", bytes_written);
    
    return 0;
}
```

This program demonstrates:
1. open() with flags O_CREAT, O_WRONLY, O_TRUNC to create/overwrite a file
2. The permission mode 0644 (owner: rw-, group: r--, others: r--)
3. write() to output data to the file
4. close() to release the file descriptor

### Example 3: Inter-Process Communication Using Pipes

This example demonstrates process communication through pipes:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pid_t pid;
    
    // Create a pipe
    if (pipe(pipefd) == -1) {
        perror("pipe failed");
        exit(1);
    }
    
    pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        exit(1);
    }
    
    if (pid == 0) {
        // Child process - writes to pipe
        close(pipefd[0]); // Close read end
        
        const char *message = "Hello from child process!";
        write(pipefd[1], message, strlen(message) + 1);
        close(pipefd[1]); // Close write end after writing
        
        exit(0);
    }
    else {
        // Parent process - reads from pipe
        close(pipefd[1]); // Close write end
        
        char buffer[100];
        read(pipefd[0], buffer, sizeof(buffer));
        printf("Parent received: %s\n", buffer);
        close(pipefd[0]); // Close read end after reading
        
        wait(NULL); // Wait for child to finish
    }
    
    return 0;
}
```

Here, the pipe() system call creates a unidirectional channel. The child process writes to pipefd[1] (the write end), while the parent reads from pipefd[0] (the read end). This demonstrates how system calls enable communication between related processes.

## Exam Tips

1. MEMORIZE THE SIX CATEGORIES: The six types of system calls (Process Control, File Management, Device Management, Information Maintenance, Communication, Protection) are fundamental. Expect direct questions asking you to list and explain these categories.

2. UNDERSTAND THE DIFFERENCE BETWEEN fork() AND exec(): This is a frequently tested concept. Remember that fork() creates a new process (duplicates the current process), while exec() replaces the current process with a new program. Many exam questions test this distinction.

3. KNOW FILE DESCRIPTORS: Understand that file descriptors are small non-negative integers used to reference open files. Remember that 0, 1, and 2 are reserved for standard input, standard output, and standard error respectively.

4. UNDERSTAND THE TRANSITION FROM USER MODE TO KERNEL MODE: Be prepared to explain how system calls cause the processor to switch from user mode to kernel mode. Know the mechanism (software interrupt, SYSENTER, SYSCALL) and why this transition is necessary for security.

5. DIFFERENTIATE BETWEEN DEVICE TYPES: Know the difference between block devices and character devices, and understand how they are accessed differently.

6. COMMUNICATION MECHANISMS: Be clear on the difference between pipes (unnamed pipes for related processes) and named pipes (FIFOs for unrelated processes), and understand socket-based communication.

7. PROTECTION MECHANISMS: Understand the setuid and setgid bits, and know how they affect process privileges. The difference between real UID and effective UID is important.

8. REVISION OF COMMANDS: Know the common system call names for each category (fork, exec, wait, open, read, write, close, pipe, socket, chmod, getpid, etc.) and what each does.