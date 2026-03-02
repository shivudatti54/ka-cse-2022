# System Calls


## Table of Contents

- [System Calls](#system-calls)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Purpose](#definition-and-purpose)
  - [User Mode vs Kernel Mode](#user-mode-vs-kernel-mode)
  - [Types of System Calls](#types-of-system-calls)
  - [System Call Interface](#system-call-interface)
- [Examples](#examples)
  - [Example 1: Process Creation Using fork()](#example-1-process-creation-using-fork)
  - [Example 2: File Operations Using open(), read(), write()](#example-2-file-operations-using-open-read-write)
  - [Example 3: Inter-Process Communication Using Pipes](#example-3-inter-process-communication-using-pipes)
- [Exam Tips](#exam-tips)

## Introduction

System calls represent the fundamental interface through which user applications interact with the operating system's kernel. When a user program needs services from the operating system—such as reading from a file, creating a new process, allocating memory, or communicating over a network—it must request these services through system calls. Without system calls, user applications would have no controlled way to access privileged system resources, making the operating system's role in resource management and security impossible to enforce.

In the context of operating system architecture, system calls serve as the boundary between user mode (where application programs execute) and kernel mode (where the operating system kernel operates with full privileges). This boundary is critical for maintaining system stability and security. When a user program invokes a system call, the processor switches from user mode to kernel mode, executes the requested operation, and then returns control back to the user program along with the operation's result. This mechanism ensures that privileged operations remain protected while still being accessible to legitimate user requests.

For MCA students at the University of Delhi, understanding system calls is essential because they form the backbone of all system programming tasks. Whether you are developing system utilities, device drivers, or application software that interacts with operating system resources, a thorough grasp of system calls enables you to write efficient, correct, and portable code. Furthermore, questions on system calls frequently appear in University of Delhi examinations, making this topic crucial for academic success.

## Key Concepts

### Definition and Purpose

A system call is a programmatic way in which a computer program requests a service from the kernel of the operating system it is executing on. System calls provide the mechanism for transitioning from user space (unprivileged mode) to kernel space (privileged mode). While regular function calls within a user program execute in user space, system calls cross this privilege boundary to request operating system services.

The purpose of system calls extends beyond mere service requests. They serve as the operating system's primary mechanism for process management, memory management, file handling, device communication, and inter-process communication. By providing a standardized interface, system calls abstract the complexities of hardware interaction from application developers, enabling portability across different hardware platforms while maintaining consistent programming interfaces.

### User Mode vs Kernel Mode

Modern operating systems employ a protection mechanism that divides execution into two distinct privilege levels: user mode and kernel mode. User mode is where applications run with limited privileges—they cannot directly access hardware or modify critical system data structures. Kernel mode, also called supervisor mode or privileged mode, is where the operating system kernel executes with full access to all system resources, including hardware devices, memory management units, and critical data structures.

When a program in user mode needs to perform a privileged operation, it cannot do so directly. Instead, it must invoke a system call, which triggers a transition to kernel mode. This transition typically involves saving the current processor state, switching to kernel mode, locating and executing the appropriate system call handler, and then returning to user mode with the operation's result. This architecture prevents malicious or buggy user programs from compromising system stability.

### Types of System Calls

System calls are categorized based on the type of service they provide to user programs. Understanding these categories helps programmers select the appropriate system calls for their needs.

**Process Control System Calls** manage process lifecycle and execution. Key system calls in this category include fork() (creates a new process), exec() (replaces the current process image with a new program), wait() (allows parent process to wait for child completion), exit() (terminates a process), and kill() (sends signals to processes). These calls form the foundation of process management in Unix-like operating systems.

**File Management System Calls** handle file operations such as creation, deletion, reading, writing, and manipulation. Common file management system calls include open() (opens or creates a file), close() (closes an open file descriptor), read() (reads data from a file), write() (writes data to a file), lseek() (modifies the file position), and stat() (retrieves file metadata). These calls provide the basic file I/O capabilities that all applications use.

**Device Management System Calls** interface with hardware devices through device files. System calls in this category include ioctl() (performs device-specific operations), read() and write() (can also operate on device files), and select() or poll() (monitor multiple file descriptors for I/O readiness).

**Information Maintenance System Calls** retrieve or modify system and process information. Examples include getpid() (returns process ID), getuid() (returns user ID), uname() (returns system information), and time() (returns current time). These calls provide essential metadata about the system state and running processes.

**Communication System Calls** facilitate inter-process communication and network operations. Key system calls include pipe() (creates a pipe for unidirectional communication), socket() (creates a communication endpoint), bind() (associates a socket with an address), connect() (establishes connection to a remote socket), accept() (accepts incoming connections), and send()/recv() (transmit and receive messages).

**Protection System Calls** control access permissions and security policies. These include chmod() (changes file permissions), chown() (changes file ownership), umask() (sets file creation mask), and setuid()/setgid() (changes process user/group IDs).

### System Call Interface

The system call interface serves as the contract between applications and the operating system. Each system call is assigned a unique number that identifies the requested operation. When a user program invokes a system call, it places this number (along with necessary parameters) in predefined locations—typically processor registers or a designated memory region—and then executes a special instruction (such as syscall on x86-64 or svc on ARM) that triggers the mode switch.

The kernel maintains a system call table that maps system call numbers to their corresponding handler functions. Upon receiving a system call request, the kernel looks up the appropriate handler in this table, executes the handler with the provided parameters, and returns the result to the user program. Parameters are typically passed through registers, though some systems use the stack or a combination of registers and memory structures.

System calls often return status codes to indicate success or failure. Successful operations typically return non-negative values (such as file descriptors or byte counts), while failures return -1 and set the global errno variable to indicate the specific error condition. Understanding error handling in system calls is crucial for writing robust system programs.

## Examples

### Example 1: Process Creation Using fork()

Consider a simple C program that creates a child process using the fork() system call:

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    
    printf("Before fork: Process ID = %d\n", getpid());
    
    pid = fork();
    
    if (pid < 0) {
        // Fork failed
        fprintf(stderr, "Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child Process: PID = %d, Parent PID = %d\n", 
               getpid(), getppid());
        printf("Child process executing new program...\n");
        execlp("ls", "ls", "-l", NULL);
    }
    else {
        // Parent process
        printf("Parent Process: PID = %d, Child PID = %d\n", 
               getpid(), pid);
        wait(NULL); // Wait for child to complete
        printf("Child process completed\n");
    }
    
    return 0;
}
```

**Step-by-step explanation:**

1. The program first prints the parent process ID using getpid()
2. fork() is called, which creates a new child process
3. In the parent process, fork() returns the child's PID (positive value)
4. In the child process, fork() returns 0
5. The parent calls wait() to suspend execution until the child terminates
6. The child uses execlp() to replace its address space with the "ls -l" command

The fork() system call demonstrates the process control category and shows how system calls enable the creation of new processes, a fundamental capability of any operating system.

### Example 2: File Operations Using open(), read(), write()

This example demonstrates basic file management system calls:

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    char buffer[100];
    const char *message = "Hello, System Calls!\n";
    
    // Create and open file with read/write permissions
    fd = open("example.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Write to the file
    ssize_t bytes_written = write(fd, message, strlen(message));
    printf("Wrote %zd bytes to file\n", bytes_written);
    
    // Close the file
    close(fd);
    
    // Reopen for reading
    fd = open("example.txt", O_RDONLY);
    
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Read from the file
    ssize_t bytes_read = read(fd, buffer, sizeof(buffer) - 1);
    buffer[bytes_read] = '\0';
    printf("Read %zd bytes: %s\n", bytes_read, buffer);
    
    close(fd);
    return 0;
}
```

**Step-by-step explanation:**

1. open() is called with flags O_CREAT (create if not exists), O_WRONLY (write-only), and O_TRUNC (truncate to zero length)
2. The third parameter 0644 sets file permissions (owner read/write, others read)
3. write() system call writes the message string to the file descriptor
4. close() releases the file descriptor
5. The file is reopened with O_RDONLY flag for reading
6. read() retrieves the file contents into the buffer
7. Finally, the file is closed again

This example illustrates the complete lifecycle of file operations: create/open, read/write, and close.

### Example 3: Inter-Process Communication Using Pipes

This example demonstrates communication between parent and child processes using pipe():

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main() {
    int pipefd[2];
    pid_t pid;
    const char *message = "Message from parent to child";
    char buffer[100];
    
    // Create pipe before fork
    if (pipe(pipefd) == -1) {
        perror("pipe failed");
        return 1;
    }
    
    pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        return 1;
    }
    
    if (pid == 0) {
        // Child process
        close(pipefd[1]); // Close write end
        
        ssize_t bytes_read = read(pipefd[0], buffer, sizeof(buffer));
        printf("Child received: %s (%zd bytes)\n", buffer, bytes_read);
        
        close(pipefd[0]); // Close read end
    }
    else {
        // Parent process
        close(pipefd[0]); // Close read end
        
        write(pipefd[1], message, strlen(message));
        printf("Parent sent message\n");
        
        close(pipefd[1]); // Close write end
        
        wait(NULL); // Wait for child
    }
    
    return 0;
}
```

**Step-by-step explanation:**

1. pipe() creates a unidirectional communication channel with two file descriptors: pipefd[0] for reading and pipefd[1] for writing
2. The pipe must be created before fork() so both processes share the same pipe
3. In the parent process, close(pipefd[0]) closes the read end since the parent only writes
4. The parent writes the message through pipefd[1]
5. In the child process, close(pipefd[1]) closes the write end since the child only reads
6. The child reads the message through pipefd[0]
7. Both processes close their respective ends after use

This example showcases communication system calls and demonstrates how processes can exchange data through pipes.

## Exam Tips

1. **Distinguish between API and System Calls**: Remember that an API (Application Programming Interface) is a function specification that applications use, while a system call is the actual mechanism that transitions to kernel mode. POSIX provides an API that maps to system calls in Unix-like systems.

2. **Understand Mode Switching**: When answering questions about system call execution, emphasize the transition from user mode to kernel mode through a trap or interrupt mechanism, and the return path back to user mode.

3. **Categorize System Calls Correctly**: In examination questions, correctly identifying which category a system call belongs to (process control, file management, device management, information maintenance, communication, protection) demonstrates comprehensive understanding.

4. **Parameter Passing Methods**: Be familiar with three common methods: passing parameters in registers, passing parameters in a table whose address is in a register, and pushing parameters on the stack and executing a trap instruction.

5. **Error Handling**: Understand how system calls indicate errors—typically returning -1 and setting the errno variable. Know common error codes like EINVAL (invalid argument), ENOENT (no such file), and EACCES (permission denied).

6. **fork() and exec() Distinction**: fork() creates a new process by duplicating the calling process, while exec() replaces the current process image with a new program. Students often confuse these fundamental operations.

7. **Relationship Between File Descriptors and System Calls**: File descriptors are small non-negative integers that index into the per-process file descriptor table. System calls like open() return file descriptors, which subsequent calls like read() and write() use.

8. **Practice Code Examples**: Many exam questions require writing or analyzing code that uses system calls. Practice with real examples involving fork(), pipe(), open(), read(), write(), and wait() to build confidence.