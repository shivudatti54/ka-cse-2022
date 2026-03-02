# Types Of System Calls

## Introduction

System calls provide the fundamental interface between a user program and the operating system kernel. When a user application needs to access hardware resources, perform I/O operations, create or terminate processes, or communicate with other processes, it must request these services through system calls. Unlike regular function calls, system calls transition the CPU from user mode (privilege level 3) to kernel mode (privilege level 0), allowing privileged operations to be executed safely.

The operating system acts as an intermediary between application software and computer hardware. System calls form the boundary through which programs request services from the OS. Each system call is typically implemented as a software interrupt or a specialized trap instruction that transfers control to the kernel. The return value from a system call indicates success or failure, and errno (error number) is often set to provide details about what went wrong. Understanding the various types of system calls is essential for comprehending how operating systems manage resources and provide services to applications.

## Key Concepts

System calls can be categorized into six major types based on the functionality they provide. Each category serves a specific purpose in operating system operations.

### 1. Process Control System Calls

Process control system calls are used to create, terminate, and control processes. The operating system must provide mechanisms for process creation, termination, suspension, and synchronization. Key system calls in this category include **fork()** (creates a new process), **exec()** (replaces the current process image), **wait()** (allows parent to wait for child process), **exit()** (terminates a process), and **abort()** (abnormal process termination). Process control also includes getting or setting process attributes like priority, affinity, and resource limits.

The **fork()** system call is particularly important as it creates an exact copy of the calling process (child process). The child process receives a copy of the parent's address space, including all open file descriptors. After fork(), both processes continue execution from the point where the call returns, but the return value differs: zero in the child process and the child's PID in the parent process.

### 2. File Management System Calls

File management system calls handle file creation, deletion, opening, closing, reading, and writing operations. These system calls abstract the complexities of physical storage devices and provide a uniform interface for file operations. Key system calls include **open()** (opens a file and returns a file descriptor), **close()** (closes an open file), **read()** (reads data from a file), **write()** (writes data to a file), **lseek()** (positions the file pointer), **mkdir()** (creates a directory), and **rmdir()** (removes a directory).

File descriptors are small non-negative integers that uniquely identify open files within a process. Each process maintains its own file descriptor table. When a process terminates, the operating system automatically closes all open file descriptors, ensuring proper cleanup of system resources.

### 3. Device Management System Calls

Device management system calls are used to communicate with hardware devices. Since devices are treated as files in many operating systems (the "everything is a file" philosophy), many file operations also apply to devices. Key system calls include **ioctl()** (device-specific control operations), **read()** and **write()** operations on device files, and device allocation functions.

These system calls handle device reservation, releasing devices after use, and performing device-specific operations. The operating system maintains a device driver interface that abstracts hardware differences, allowing applications to interact with diverse devices through a common API.

### 4. Information Maintenance System Calls

Information maintenance system calls are used to transfer information between the operating system and user programs. These calls maintain system data and provide status information. Key system calls include **getpid()** (returns process ID), **getuid()** (returns user ID), **getgid()** (returns group ID), **getpriority()** (returns scheduling priority), **uname()** (returns system name and information), **time()** (returns current time), and **clock()** (returns processor time used).

These system calls are essential for process management and system monitoring. They allow programs to retrieve essential information about their execution environment and the system state without directly accessing kernel data structures.

### 5. Communication System Calls

Communication system calls facilitate inter-process communication (IPC) and network communication. Modern operating systems provide various IPC mechanisms including message passing, shared memory, and pipes. Key system calls include **pipe()** (creates a pipe for communication), **socket()** (creates a communication endpoint), **connect()** (establishes connection to remote socket), **bind()** (binds socket to local address), **listen()** (listens for connections), and **accept()** (accepts incoming connections).

Message passing involves sending and receiving messages between processes, while shared memory allows multiple processes to access common memory regions. Pipes provide a simple unidirectional communication channel between related processes.

### 6. Protection System Calls

Protection system calls control access to system resources and enforce security policies. These calls are crucial for multi-user operating systems where process isolation and access control are essential. Key system calls include **chmod()** (changes file permissions), **chown()** (changes file ownership), **umask()** (sets file creation mask), **setuid()** (sets user ID), **setgid()** (sets group ID), and **chroot()** (changes root directory).

Modern operating systems implement discretionary access control (DAC) where file owners can control who accesses their files. Some systems also support mandatory access control (MAC) and role-based access control (RBAC) for enhanced security.

## Examples

### Example 1: Process Creation and Control

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
 printf("Child process: PID = %d, Parent PID = %d\n",
 getpid(), getppid());
 execlp("/bin/ls", "ls", "-l", NULL);
 // If execlp succeeds, this line won't execute
 perror("execlp failed");
 exit(1);
 }
 else {
 // Parent process
 printf("Parent process: PID = %d, Child PID = %d\n",
 getpid(), pid);
 wait(NULL); // Wait for child to complete
 printf("Child process completed\n");
 }

 return 0;
}
```

This example demonstrates three types of system calls: fork() for process creation, getpid() and getppid() for information retrieval, and wait() for process synchronization. The execlp() system call demonstrates process image replacement.

### Example 2: File Management Operations

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
 int fd;
 char buffer[] = "Hello, Operating System!";
 char read_buffer[100];

 // Create and open file (open is a file management system call)
 fd = open("test.txt", O_CREAT | O_WRONLY, 0644);

 if (fd < 0) {
 perror("open failed");
 return 1;
 }

 // Write to file (write is a file management system call)
 if (write(fd, buffer, strlen(buffer)) < 0) {
 perror("write failed");
 close(fd);
 return 1;
 }

 close(fd); // Close file

 // Reopen for reading
 fd = open("test.txt", O_RDONLY);

 // Read from file
 read(fd, read_buffer, 100);
 printf("Read from file: %s\n", read_buffer);

 close(fd);
 return 0;
}
```

This example shows file creation with permissions, writing data to a file, and reading data back. The system calls used include open(), write(), read(), and close() - all file management system calls.

### Example 3: Inter-Process Communication via Pipe

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
 int pipefd[2];
 pid_t pid;
 char write_msg[] = "Message from parent";
 char read_msg[100];

 // Create pipe (communication system call)
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
 // Child process - close read end, write to pipe
 close(pipefd[0]);
 write(pipefd[1], write_msg, strlen(write_msg) + 1);
 close(pipefd[1]);
 exit(0);
 }
 else {
 // Parent process - close write end, read from pipe
 close(pipefd[1]);
 read(pipefd[0], read_msg, 100);
 printf("Parent received: %s\n", read_msg);
 close(pipefd[0]);
 wait(NULL);
 }

 return 0;
}
```

This example demonstrates inter-process communication using pipes. The pipe() system call creates a unidirectional channel, and the parent and child processes use read() and write() system calls to communicate.

## Exam Tips

1. **Remember the Six Categories**: The six types of system calls (Process Control, File Management, Device Management, Information Maintenance, Communication, Protection) are fundamental. Be able to list and explain each category with examples.

2. **Understand the Transition**: System calls involve a mode switch from user mode to kernel mode. This transition is typically triggered by a trap or interrupt instruction and involves saving the process state.

3. **Know Specific Examples**: Memorize common system calls like fork(), exec(), open(), read(), write(), pipe(), socket(), and chmod() and their categories.

4. **File Descriptor Concept**: Understand that file descriptors are small integers used to reference open files. By convention, stdin is 0, stdout is 1, and stderr is 2 in UNIX systems.

5. **fork() Return Value**: Remember that fork() returns 0 to the child process and the child's PID to the parent process. This is a common exam question.

6. **Error Handling**: System calls typically return -1 on error and set the global errno variable. Always check return values in practical implementations.

7. **Distinguish Between User and Kernel Mode**: System calls are the only way for user programs to perform privileged operations. The operating system acts as a trusted intermediary.

8. **Practice with System Calls**: Writing code that uses system calls helps reinforce understanding. Be familiar with basic system call usage in C programming.
