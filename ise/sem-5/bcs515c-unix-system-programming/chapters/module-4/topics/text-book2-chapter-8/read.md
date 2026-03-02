# **UNIX SYSTEM PROGRAMMING**

## **Chapter 8: Process Control**

### Introduction

---

Process control is a fundamental concept in UNIX system programming that enables you to manage and interact with processes in a UNIX environment. This chapter will introduce you to process control concepts, including process identifiers, process creation, and process management.

### Process Identifiers

---

A process identifier (PID) is a unique number assigned to a process by the operating system. PIDs are used to identify and manage processes in a UNIX environment.

- **Process ID (PID):** A unique identifier assigned to a process by the operating system.
- **Process Name:** The name given to a process, usually by the programmer.
- **Process Status:** The current state of a process, including RUNNABLE, RUNNING, SLEEPING, ZOMBIE, DEAD, and more.

### Fork

---

The `fork` system call is used to create a new process from an existing one. When a process calls `fork`, the operating system creates a new process that is a copy of the calling process. The new process receives a new PID, while the calling process retains its original PID.

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // This is the child process
        printf("Child process with PID %d\n", getpid());
    } else {
        // This is the parent process
        printf("Parent process with PID %d\n", getpid());

        // Wait for the child process to finish
        wait(NULL);
    }

    return 0;
}
```

### Vfork

---

The `vfork` system call is similar to `fork`, but it also copies the parent process's memory space to the child process. This can be useful when the parent process needs to interact with the child process.

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = vfork();

    if (pid == 0) {
        // This is the child process
        printf("Child process with PID %d\n", getpid());
    } else {
        // This is the parent process
        printf("Parent process with PID %d\n", getpid());

        // Wait for the child process to finish
        wait(NULL);
    }

    return 0;
}
```

### Exit

---

The `exit` system call is used to terminate a process. When a process calls `exit`, the operating system terminates the process and releases any system resources associated with it.

- **Exit Status:** The exit status of a process is the value returned by the `exit` system call. A return value of 0 indicates that the process terminated normally, while a non-zero value indicates an error.
- **Signal Exit:** A process can be terminated by sending a signal to it. The operating system will then terminate the process and return an error.

**Example:**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Exit the process with a status code
    exit(0);

    return 0;
}
```

### Wait

---

The `wait` system call is used to wait for a process to finish. When a process calls `wait`, the operating system will return the status of the process that has finished.

- **Wait PID:** The `wait` system call returns the PID of the process that has finished.
- **Wait Result:** The result of the `wait` system call is the exit status of the process that has finished.

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // This is the child process
        printf("Child process with PID %d\n", getpid());
        sleep(5);
        printf("Child process finished with exit status %d\n", exit(0));
    } else {
        // This is the parent process
        printf("Parent process with PID %d\n", getpid());

        // Wait for the child process to finish
        pid_t status = wait(NULL);

        printf("Parent process finished with exit status %d\n", WEXITSTATUS(status));
    }

    return 0;
}
```

### Waitpid

---

The `waitpid` system call is used to wait for a process to finish, and also to specify the process ID of the process to wait for.

- **Wait for Process:** The `waitpid` system call returns the PID of the process that has finished.
- **Wait Result:** The result of the `waitpid` system call is the exit status of the process that has finished.

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // This is the child process
        printf("Child process with PID %d\n", getpid());
        sleep(5);
        printf("Child process finished with exit status %d\n", exit(0));
    } else {
        // This is the parent process
        printf("Parent process with PID %d\n", getpid());

        // Wait for the child process to finish
        pid_t status = waitpid(pid, NULL, 0);

        printf("Parent process finished with exit status %d\n", WEXITSTATUS(status));
    }

    return 0;
}
```

### Wait3

---

The `wait3` system call is used to wait for a process to finish, and also to specify the process ID of the process to wait for. The `wait3` system call also provides an additional argument `WNOHANG` to specify whether to wait for the process to finish or to return immediately.

- **Wait for Process:** The `wait3` system call returns the PID of the process that has finished.
- **Wait Result:** The result of the `wait3` system call is the exit status of the process that has finished.

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // This is the child process
        printf("Child process with PID %d\n", getpid());
        sleep(5);
        printf("Child process finished with exit status %d\n", exit(0));
    } else {
        // This is the parent process
        printf("Parent process with PID %d\n", getpid());

        // Wait for the child process to finish with WNOHANG
        pid_t status = wait3(0, NULL, WNOHANG);

        if (status != 0) {
            // Wait for the child process to finish
            waitpid(pid, NULL, 0);
        }

        printf("Parent process finished with exit status %d\n", WEXITSTATUS(status));
    }

    return 0;
}
```

By mastering these process control concepts, you can create and manage processes in a UNIX environment, and write efficient and effective programs.
