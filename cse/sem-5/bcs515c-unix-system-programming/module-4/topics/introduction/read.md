# Introduction to Unix System Programming

## Introduction

Unix System Programming refers to the practice of writing programs that interact with the Unix operating system at a low level, utilizing system calls, process management, inter-process communication (IPC), and file I/O operations. This branch of programming focuses on building software that directly leverages the services provided by the Unix kernel, enabling programmers to create efficient, robust, and portable applications. The Unix operating system, originally developed in the 1960s and 1970s at Bell Labs, has become the foundation for many modern operating systems including Linux, macOS, BSD, and Solaris.

System programming in Unix differs significantly from application programming. While application programmers work with high-level abstractions and standard libraries, system programmers must understand the underlying mechanisms of process control, memory management, file systems, and device I/O. This requires knowledge of the POSIX (Portable Operating System Interface) standards, which define a standardized interface ensuring portability across different Unix variants. The POSIX API provides approximately 1100 system calls and functions that form the backbone of Unix system programming.

This module introduces the fundamental concepts of Unix System Programming, covering process management, file descriptors, piping, FIFOs, message queues, semaphores, and shared memory. Understanding these concepts is essential for developing system utilities, daemons, network applications, and embedded systems. The knowledge gained from this module provides a solid foundation for advanced topics in operating systems, distributed computing, and software engineering.

## Key Concepts

### System Calls and the Kernel Interface

System calls are the fundamental interface between user applications and the Unix kernel. When a program requires services such as reading from a file, creating a process, or allocating memory, it invokes a system call that transfers control from user mode to kernel mode. The kernel performs the requested operation and returns control to the user program along with a status code. Common system calls include `read()`, `write()`, `fork()`, `exec()`, `open()`, `close()`, and `exit()`. Each system call has a specific purpose and returns specific values that the programmer must handle appropriately.

The transition between user mode and kernel mode involves a context switch, which is computationally expensive. Therefore, system programmers must minimize the number of system calls in performance-critical code. Additionally, error handling is crucial when working with system calls, as they can fail due to various reasons such as insufficient permissions, invalid arguments, or resource exhaustion. The conventional approach is to check the return value and set `errno` to diagnose the specific error.

### Process Management

A process in Unix is an instance of a program in execution, identified by a unique Process Identifier (PID). The Unix kernel manages processes through data structures called process control blocks (PCBs), which store information such as process state, program counter, register values, memory management details, and open file descriptors. Processes can be created using the `fork()` system call, which creates an exact copy of the parent process. The child process receives a new PID while sharing certain attributes with the parent.

The `exec()` family of functions replaces the current process image with a new program, allowing the child process to execute different code. This combination of `fork()` and `exec()` is the fundamental mechanism for process creation in Unix. The parent process can synchronize with child processes using `wait()` or `waitpid()` functions, which suspend execution until a child terminates. Understanding process management is essential for creating robust concurrent applications and proper resource cleanup.

### File Descriptors and I/O

In Unix, all I/O operations are performed through file descriptors, which are small non-negative integers that serve as references to open files, devices, pipes, sockets, or other I/O resources. The kernel maintains a per-process file descriptor table that maps file descriptors to file table entries, which in turn point to the inode table containing metadata about the underlying file. This abstraction allows uniform treatment of various I/O sources and destinations.

The standard file descriptors are stdin (0), stdout (1), and stderr (2). The `open()`, `creat()`, `pipe()`, `socket()`, and `dup()` functions create new file descriptors, while `close()` releases them. The `read()` and `write()` system calls perform unbuffered I/O, while standard I/O library functions like `fread()` and `fwrite()` provide buffered operations. Understanding the distinction between low-level and buffered I/O is important for writing efficient programs.

### Inter-Process Communication (IPC)

Unix provides various mechanisms for processes to communicate and synchronize with each other. Traditional methods include pipes and FIFOs (named pipes), which allow data flow between related or unrelated processes. Modern System V IPC includes message queues, semaphores, and shared memory segments. Each IPC mechanism has specific characteristics regarding performance, synchronization requirements, and use cases.

Pipes are created using the `pipe()` system call and provide a unidirectional byte stream communication channel between a parent and child process. FIFOs extend this concept to unrelated processes by creating special files in the file system. Message queues enable structured message passing with priority support. Semaphores provide counting mechanisms for process synchronization. Shared memory allows multiple processes to access common memory regions, offering the highest performance but requiring explicit synchronization through semaphores or other mechanisms.

## Examples

### Example 1: Basic Process Creation

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid = fork();

 if (pid < 0) {
 perror("fork failed");
 exit(EXIT_FAILURE);
 }

 if (pid == 0) {
 // Child process
 printf("Child process: PID = %d, Parent PID = %d\n",
 getpid(), getppid());
 execlp("ls", "ls", "-l", NULL);
 perror("execlp failed");
 exit(EXIT_FAILURE);
 } else {
 // Parent process
 int status;
 waitpid(pid, &status, 0);
 printf("Parent: Child %d terminated with status %d\n",
 pid, WEXITSTATUS(status));
 }

 return 0;
}
```

This example demonstrates the complete process creation cycle: `fork()` creates a child process, `execlp()` executes a new program in the child, and `waitpid()` allows the parent to synchronize with the child's termination.

### Example 2: Pipe Communication Between Processes

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
 int pipefd[2];
 pid_t pid;
 char write_msg[] = "Hello from parent!";
 char read_msg[100];

 if (pipe(pipefd) == -1) {
 perror("pipe failed");
 exit(EXIT_FAILURE);
 }

 pid = fork();

 if (pid < 0) {
 perror("fork failed");
 exit(EXIT_FAILURE);
 }

 if (pid == 0) {
 // Child: reads from pipe
 close(pipefd[1]); // Close write end
 read(pipefd[0], read_msg, sizeof(read_msg));
 printf("Child received: %s\n", read_msg);
 close(pipefd[0]);
 } else {
 // Parent: writes to pipe
 close(pipefd[0]); // Close read end
 write(pipefd[1], write_msg, strlen(write_msg) + 1);
 close(pipefd[1]);
 wait(NULL);
 }

 return 0;
}
```

This example shows unidirectional communication through a pipe, demonstrating proper file descriptor management and data transfer between parent and child processes.

### Example 3: Using Shared Memory

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main() {
 key_t key = ftok("/tmp", 'A');
 int shmid = shmget(key, 1024, IPC_CREAT | 0666);

 if (shmid == -1) {
 perror("shmget failed");
 exit(EXIT_FAILURE);
 }

 char *shm_ptr = (char *)shmat(shmid, NULL, 0);

 if (shm_ptr == (char *)-1) {
 perror("shmat failed");
 exit(EXIT_FAILURE);
 }

 strcpy(shm_ptr, "Shared data written to memory");
 printf("Data written to shared memory: %s\n", shm_ptr);

 shmdt(shm_ptr);
 shmctl(shmid, IPC_RMID, NULL);

 return 0;
}
```

This example demonstrates System V shared memory operations: creating a shared memory segment, attaching it to the process address space, writing data, and proper cleanup using `shmdt()` and `shmctl()`.

## Exam Tips

1. **Understand the difference between user mode and kernel mode**: System calls involve mode transitions and are expensive. Know which operations require kernel intervention versus user-space operations.

2. **Master process creation lifecycle**: Remember that `fork()` creates a copy, `exec()` replaces the program, and `wait()` synchronizes termination. These three operations form the foundation of Unix process management.

3. **File descriptor management is critical**: Always close unused file descriptors to prevent resource leaks. Remember that child processes inherit the parent's file descriptor table.

4. **Error handling with errno**: Always check return values from system calls and use `perror()` or `strerror()` to diagnose failures. Never ignore error conditions in system programs.

5. **Choose appropriate IPC mechanism**: Pipes are simple for parent-child communication, while message queues and shared memory suit complex multi-process scenarios. Consider synchronization requirements when using shared memory.

6. **POSIX vs System V IPC**: Understand that Unix has legacy System V IPC (semaphores, shared memory, message queues) and newer POSIX equivalents. Both may be available on modern systems.

7. **Resource cleanup**: Always properly release resources—close file descriptors, detach shared memory, delete IPC objects. Resource leaks in system programs can cause serious system degradation.

8. **Practice with actual code**: System programming concepts are best understood through implementation. Write, compile, and debug programs to gain practical experience with these system calls.
