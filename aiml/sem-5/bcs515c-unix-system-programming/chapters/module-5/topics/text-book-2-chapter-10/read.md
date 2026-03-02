# UNIX SYSTEM PROGRAMMING

## Module: @#@#@#@#

### Topic: Text Book 2: Chapter 10

## Introduction

In this chapter, we will learn about the Advanced Programming Techniques in UNIX, including file descriptors, file locking, and pipes.

### File Descriptors

File descriptors are small integers that refer to open files in a process. They are used to read and write data to files.

### Creating File Descriptors

File descriptors can be created using the `open()` system call.

```c
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("file.txt", O_RDONLY);
    if (fd < 0) {
        perror("Error opening file");
        return 1;
    }
    // Use the file descriptor to read from the file
    char buffer[1024];
    read(fd, buffer, 1024);
    printf("%s\n", buffer);
    close(fd);
    return 0;
}
```

### File Descriptors Types

There are three types of file descriptors:

- **Read file descriptor**: used to read from a file.
- **Write file descriptor**: used to write to a file.
- **Append file descriptor**: used to append to a file.

### File Locking

File locking is used to prevent multiple processes from accessing the same file simultaneously.

### Pipes

Pipes are used to connect two processes and allow them to communicate with each other.

## Pipes

### Creating Pipes

Pipes can be created using the `pipe()` system call.

```c
#include <unistd.h>

int main() {
    int pipefd[2];
    pipe(pipefd);
    // Use the pipefd array to read from and write to the pipe
    char buffer[1024];
    write(pipefd[1], "Hello, World!", 13);
    read(pipefd[0], buffer, 1024);
    printf("%s\n", buffer);
    return 0;
}
```

### Multiple Processes and Pipes

Pipes can be used to connect multiple processes and allow them to communicate with each other.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int pipefd[2];

    // Create a new process
    pid = fork();

    if (pid < 0) {
        perror("Error creating process");
        return 1;
    }

    if (pid == 0) {
        // Child process
        close(pipefd[1]); // Close the write end of the pipe
        read(pipefd[0], buffer, 1024);
        printf("Child process: %s\n", buffer);
        close(pipefd[0]); // Close the read end of the pipe
    } else {
        // Parent process
        close(pipefd[0]); // Close the read end of the pipe
        write(pipefd[1], "Hello, World!", 13);
        close(pipefd[1]); // Close the write end of the pipe
        wait(NULL); // Wait for the child process to finish
    }

    return 0;
}
```

### Inter-Process Communication (IPC)

Pipes are a form of IPC that allows processes to communicate with each other.

### Synchronous and Asynchronous IPC

Pipes can be used for both synchronous and asynchronous IPC.

### Synchronous IPC

Synchronous IPC is used when the sending process waits for the receiving process to finish before continuing.

### Asynchronous IPC

Asynchronous IPC is used when the sending process continues to execute without waiting for the receiving process to finish.

## Conclusion

In this chapter, we learned about advanced programming techniques in UNIX, including file descriptors, file locking, and pipes. We also learned about creating pipes, using pipes with multiple processes, and inter-process communication.
