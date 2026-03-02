# System Calls and System Functions

## Introduction

System calls and system functions form the fundamental interface between user applications and the operating system kernel. In UNIX/Linux systems, system calls provide the only legal way for user programs to request services from the operating system. These calls act as a protective barrier, ensuring that privileged operations are only executed in a controlled manner while maintaining system stability and security.

System functions extend beyond basic system calls to include library functions that wrap system calls, providing higher-level abstractions for programmers. Understanding system calls is crucial for system programmers, as they form the backbone of system software development including compilers, editors, text formatters, and other utility programs. In the context of 's System Programming curriculum, this topic enables students to understand how high-level language constructs are translated into operating system operations.

The distinction between system calls and system functions is important: system calls directly invoke kernel services and switch from user mode to kernel mode (privileged mode), while system functions are library routines that may or may not make system calls. This module covers the major categories of system calls essential for system programming.

## Key Concepts

### Categories of System Calls

System calls in UNIX/Linux can be broadly categorized into six main groups:

**1. Process Control System Calls**

- `fork()`: Creates a new process by duplicating the calling process
- `exec()` family: Replaces the current process image with a new program
- `wait()`: Suspends execution until a child process terminates
- `exit()`: Terminates the calling process
- `getpid()`: Returns process ID of current process
- `getppid()`: Returns parent process ID

**2. File Manipulation System Calls**

- `open()`: Opens a file and returns a file descriptor
- `read()`: Reads data from a file descriptor
- `write()`: Writes data to a file descriptor
- `close()`: Closes a file descriptor
- `lseek()`: Repositions the file offset
- `stat()`: Gets file status information

**3. Device Management System Calls**

- `ioctl()`: Controls device parameters
- `read()` and `write()`: Can also work with devices (devices treated as files)
- `fcntl()`: Performs file descriptor operations

**4. Information Maintenance System Calls**

- `getpid()`, `getuid()`: Get process and user IDs
- `uname()`: Get system name information
- `gettimeofday()`: Get current time
- `getrlimit()`, `setrlimit()`: Get/set resource limits

**5. Communication System Calls**

- `pipe()`: Creates a pipe for interprocess communication
- `socket()`: Creates a communication endpoint
- `bind()`, `listen()`, `accept()`: Socket programming functions
- `msgget()`, `msgsnd()`, `msgrcv()`: Message queue operations
- `shmget()`, `shmat()`, `shmdt()`: Shared memory operations

**6. Protection System Calls**

- `chmod()`: Changes file permissions
- `chown()`: Changes file ownership
- `umask()`: Sets file creation mask
- `chroot()`: Changes root directory

### System Call Implementation Mechanism

When a program makes a system call, the following sequence occurs:

1. The program invokes a library function (wrapper function)
2. The wrapper function loads the system call number into a specific register (typically `%eax` in x86)
3. Arguments are placed in other registers (`%ebx`, `%ecx`, `%edx`)
4. The wrapper executes the `trap` or `syscall` instruction
5. The processor switches from user mode to kernel mode
6. The kernel identifies the system call number and dispatches to the appropriate handler
7. After execution, control returns to user mode with return value in register

### File Descriptors

A file descriptor is a small non-negative integer that the kernel uses to identify an open file for a process. When a process opens or creates a file, the kernel returns a file descriptor to the process. Standard file descriptors include:

- 0: Standard Input (stdin)
- 1: Standard Output (stdout)
- 2: Standard Error (stderr)

### Process States and System Calls

Processes can be in various states: running, ready, blocked, or terminated. System calls like `wait()` can cause a process to change from running to blocked state, waiting for child process termination.

## Examples

### Example 1: Creating a Child Process with fork()

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
 pid_t pid;

 printf("Before fork - Process ID: %d\n", getpid());

 pid = fork(); // Creates a new process

 if (pid < 0) {
 // Fork failed
 fprintf(stderr, "Fork failed\n");
 return 1;
 }
 else if (pid == 0) {
 // Child process
 printf("Child Process - PID: %d, Parent PID: %d\n",
 getpid(), getppid());
 printf("I am the child\n");
 }
 else {
 // Parent process
 printf("Parent Process - PID: %d, Child PID: %d\n",
 getpid(), pid);
 printf("I am the parent\n");
 }

 return 0;
}
```

**Step-by-step explanation:**

1. Parent process calls `fork()`, which duplicates the process
2. `fork()` returns twice: once in parent (with child's PID) and once in child (with 0)
3. Parent process executes the `else` branch
4. Child process executes the `if(pid == 0)` branch
5. Both processes continue execution independently

### Example 2: File Operations using System Calls

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
 int fd;
 char buffer[100];
 ssize_t bytes_written, bytes_read;

 // Create a new file using open() with O_CREAT and O_WRONLY
 fd = open("example.txt", O_CREAT | O_WRONLY, 0644);

 if (fd < 0) {
 perror("Open failed");
 return 1;
 }

 // Write to the file using write()
 char message[] = "Hello, System Programming!";
 bytes_written = write(fd, message, strlen(message));

 if (bytes_written < 0) {
 perror("Write failed");
 close(fd);
 return 1;
 }

 printf("Wrote %zd bytes to file\n", bytes_written);
 close(fd);

 // Reopen to read
 fd = open("example.txt", O_RDONLY);

 if (fd < 0) {
 perror("Open for read failed");
 return 1;
 }

 // Read from file using read()
 bytes_read = read(fd, buffer, sizeof(buffer) - 1);

 if (bytes_read < 0) {
 perror("Read failed");
 close(fd);
 return 1;
 }

 buffer[bytes_read] = '\0'; // Null-terminate the string
 printf("Read: %s\n", buffer);
 printf("Read %zd bytes\n", bytes_read);

 close(fd);
 return 0;
}
```

**Step-by-step explanation:**

1. `open()` creates a new file with permissions 0644 (rw-r--r--)
2. Returns a file descriptor (non-negative integer)
3. `write()` writes the message to the file, returns bytes written
4. `close()` releases the file descriptor
5. Reopen the file with O_RDONLY flag
6. `read()` reads data into buffer, returns bytes read
7. Properly close the file descriptor after use

### Example 3: Process Execution with exec() Family

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
 pid_t pid;
 int status;

 pid = fork();

 if (pid < 0) {
 perror("Fork failed");
 return 1;
 }

 if (pid == 0) {
 // Child process - execute a new program
 // Using execl() which takes variable arguments
 execl("/bin/ls", "ls", "-l", "-a", NULL);

 // If execl() returns, an error occurred
 perror("execl failed");
 _exit(127);
 }
 else {
 // Parent process - wait for child to complete
 printf("Parent waiting for child (PID: %d)\n", pid);

 pid_t terminated_pid = wait(&status);

 if (terminated_pid > 0) {
 if (WIFEXITED(status)) {
 printf("Child (PID: %d) terminated with exit status: %d\n",
 terminated_pid, WEXITSTATUS(status));
 }
 }
 }

 return 0;
}
```

**Step-by-step explanation:**

1. Parent creates child process using `fork()`
2. Child process replaces its program image using `execl()`
3. `execl()` takes path to executable, arguments (including command name), and NULL terminator
4. If `execl()` succeeds, it never returns in child process
5. Parent uses `wait()` to wait for child termination
6. `wait()` returns child's PID and stores exit status in `status` variable
7. Macros `WIFEXITED()` and `WEXITSTATUS()` extract exit information

## Exam Tips

1. **Memorize the six categories** of system calls - this is a frequently asked question in exams. Write all six categories with at least two examples each.

2. **Understand the difference between fork() and exec()**: fork() creates a new process by duplicating the parent, while exec() replaces the current process image with a new program.

3. **File descriptors 0, 1, 2** represent stdin, stdout, and stderr respectively - remember this for I/O redirection questions.

4. **Process control sequence**: When a process calls fork(), it returns twice - once in parent (with child's PID) and once in child (with 0).

5. **System call vs library function**: System calls switch to kernel mode and are slower; library functions are user-space functions that may or may not use system calls.

6. **wait() and exit() relationship**: The wait() system call in parent blocks until a child process terminates. The exit() system call terminates a process and can pass an exit status.

7. **Permission formats**: Remember that open() takes a third argument for file permissions (e.g., 0644 = rw-r--r-- in octal).

8. **Error handling**: Always check return values of system calls. On error, they return -1 and set errno.

9. **Remember the sequence**: For process creation: fork() → (in child) exec() → (in parent) wait() for child termination.

10. **Device as file**: In UNIX, devices are treated as files - they can be opened, read from, and written to using the same system calls.
