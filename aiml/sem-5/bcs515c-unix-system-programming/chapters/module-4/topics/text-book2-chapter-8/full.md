# **Text Book2: Chapter 8**

## **Process Control: Introduction, Process Identifiers, fork, vfork, exit, wait, waitpid, wait3**

## **Introduction**

Process control is a fundamental concept in operating system programming. It involves the creation, management, and termination of processes. In this chapter, we will delve into the world of process control, exploring the various techniques used to manage processes on a UNIX system.

### Historical Context

The concept of process control dates back to the early days of computing, when operating systems were first developed. The first operating system, CTSS (Compatible Time-Sharing System), was developed in the 1950s and introduced the concept of processes. Later, UNIX was developed in the 1970s, and it introduced the concept of process control as we know it today.

### Modern Developments

In recent years, process control has become increasingly important with the advent of distributed systems and cloud computing. The need to manage multiple processes and threads has led to the development of new techniques and technologies. Some of the modern developments in process control include:

- **Thread Synchronization**: The use of locks, semaphores, and monitors to synchronize access to shared resources.
- **Process Scheduling**: The allocation of resources to processes based on their priority and availability.
- **Process Migration**: The movement of processes from one machine to another.

## **Process Identifiers**

A process identifier (PID) is a unique number assigned to each process running on a system. PIDs are used to identify and manage processes. There are several types of PIDs, including:

- **Process ID (PID)**: A unique number assigned to each process.
- **Process Group ID (PGID)**: A unique number assigned to a group of processes.
- **Session ID (SID)**: A unique number assigned to a session of processes.

### Example

```bash
ps -ef | grep 1234
```

This command will display the process details for the process with PID 1234.

## **Fork**

The `fork` system call creates a new process by duplicating the current process. The new process is a copy of the current process, with its own memory space and resources.

### Example

```c
#include <unistd.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // This is the child process
        printf("Child process created\n");
    } else if (pid > 0) {
        // This is the parent process
        printf("Parent process created\n");
    } else {
        // Error occurred
        printf("Error creating process\n");
    }
    return 0;
}
```

This code will create two processes: a parent process and a child process.

## **Vfork**

The `vfork` system call is similar to the `fork` system call, but it also clones the parent process's memory space. This is useful when the child process needs to access the parent process's memory.

### Example

```c
#include <unistd.h>

int main() {
    pid_t pid = vfork();
    if (pid == 0) {
        // This is the child process
        printf("Child process created\n");
    } else if (pid > 0) {
        // This is the parent process
        printf("Parent process created\n");
    } else {
        // Error occurred
        printf("Error creating process\n");
    }
    return 0;
}
```

This code will create two processes: a parent process and a child process, with the child process's memory space cloned from the parent process.

## **Exit**

The `exit` system call terminates a process. It is used to exit a process cleanly, by calling the `exit` function and passing an exit code.

### Example

```c
#include <unistd.h>

int main() {
    exit(0);
    return 0;
}
```

This code will terminate the process with an exit code of 0.

## **Wait**

The `wait` system call suspends the execution of the current process until one of its child processes terminates.

### Example

```c
#include <unistd.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // This is the child process
        sleep(10);
        exit(0);
    } else {
        // This is the parent process
        wait(NULL);
        printf("Parent process terminated\n");
    }
    return 0;
}
```

This code will create a child process that sleeps for 10 seconds before terminating. The parent process will wait for the child process to terminate before continuing execution.

## **Waitpid**

The `waitpid` system call is similar to the `wait` system call, but it allows the caller to specify a specific child process ID.

### Example

```c
#include <unistd.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // This is the child process
        sleep(10);
        exit(0);
    } else {
        // This is the parent process
        waitpid(pid, NULL, 0);
        printf("Parent process terminated\n");
    }
    return 0;
}
```

This code will create a child process that sleeps for 10 seconds before terminating. The parent process will wait for the child process to terminate before continuing execution.

## **Wait3**

The `wait3` system call is similar to the `wait` system call, but it allows the caller to specify a specific child process ID and a signal to be sent to the child process when it terminates.

### Example

```c
#include <unistd.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // This is the child process
        sleep(10);
        exit(0);
    } else {
        // This is the parent process
        wait3(SIGCHLD, NULL, 0);
        printf("Parent process terminated\n");
    }
    return 0;
}
```

This code will create a child process that sleeps for 10 seconds before terminating. The parent process will wait for the child process to terminate and send a SIGCHLD signal to the parent process when the child process terminates.

## **Case Study**

Suppose we have a program that needs to check the status of multiple processes. We can use the `wait` system call to wait for each process to terminate and then print the exit code.

```c
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid1 = fork();
    if (pid1 == 0) {
        // This is the child process
        sleep(10);
        exit(0);
    }

    pid_t pid2 = fork();
    if (pid2 == 0) {
        // This is the child process
        sleep(10);
        exit(1);
    }

    wait(NULL);
    wait(NULL);

    return 0;
}
```

This code will create two child processes that sleep for 10 seconds before terminating. The parent process will wait for both child processes to terminate before continuing execution.

## **Applications**

Process control has many applications in operating system programming. Some of the applications include:

- **Process Management**: Process control is used to manage processes on a system. It includes creating, terminating, and suspending processes.
- **Thread Synchronization**: Process control is used to synchronize access to shared resources in a multithreaded program.
- **Resource Allocation**: Process control is used to allocate resources to processes on a system.

## **Further Reading**

- "Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- " UNIX System Administration" by David L. Robinson
- "Process Management in Operating Systems" by Andrew S. Tanenbaum

Note: The examples provided are in C programming language. The code can be modified to fit the desired programming language.
