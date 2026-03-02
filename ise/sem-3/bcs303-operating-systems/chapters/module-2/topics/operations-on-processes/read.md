# Operations on Processes

=====================================================

## Overview

---

In operating system, a process is a program in execution. Processes are the basic units of execution in an operating system. There are two main types of processes: user-level processes and kernel-level processes. In this topic, we will discuss the operations performed on processes.

## Types of Operations on Processes

---

There are three main types of operations performed on processes:

- **Creation**: Creating a new process.
- **Termination**: Terminating a process.
- **Scheduling**: Scheduling a process for execution.
- **Communication**: Exchanging data between processes.

### Creation of a Process

---

Creating a new process involves several steps:

- **Process Creation**: The operating system creates a new process by allocating a memory space, stack, and other resources.
- **Process ID (PID)**: The operating system assigns a unique process ID (PID) to the new process.
- **Parent-Child Relationship**: The new process becomes a child of the parent process.

**Example:**

Suppose we have a parent process `P1` and we create a new process `P2` using the `fork()` system call.

```c
// Parent process
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child process
        printf("Child process created with PID %d\n", getpid());
    } else {
        // Parent process
        printf("Parent process created with PID %d\n", getpid());
    }
    return 0;
}
```

### Termination of a Process

---

Terminating a process involves several steps:

- **Process Termination**: The operating system terminates a process by releasing its allocated resources.
- **Exit Status**: The operating system returns an exit status to the parent process indicating the termination of the child process.

**Example:**

Suppose we have a parent process `P1` and we terminate a child process `P2` using the `exit()` system call.

```c
// Parent process
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child process
        printf("Child process created with PID %d\n", getpid());
        exit(0); // Exit the child process with exit status 0
    } else {
        // Parent process
        printf("Parent process created with PID %d\n", getpid());
        wait(NULL); // Wait for child process to terminate
        printf("Child process terminated\n");
    }
    return 0;
}
```

### Scheduling of a Process

---

Scheduling a process involves several steps:

- **Process Scheduling**: The operating system schedules a process for execution by allocating a time slice.
- **Time Slicing**: The operating system executes the process for a fixed time slice and then switches to another process.

**Example:**

Suppose we have a parent process `P1` and we schedule a child process `P2` for execution using the `scheduling()` system call.

```c
// Parent process
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child process
        printf("Child process created with PID %d\n", getpid());
        sleep(2); // Sleep for 2 seconds
        printf("Child process terminated\n");
    } else {
        // Parent process
        printf("Parent process created with PID %d\n", getpid());
        sleep(1); // Sleep for 1 second
        printf("Parent process terminated\n");
    }
    return 0;
}
```

### Communication between Processes

---

Communication between processes involves several steps:

- **Inter-Process Communication (IPC)**: The operating system provides several IPC mechanisms to enable communication between processes.
- **Synchronous Communication**: The operating system synchronizes communication between processes using semaphores or monitors.
- **Asynchronous Communication**: The operating system asynchronizes communication between processes using pipes or sockets.

**Example:**

Suppose we have a parent process `P1` and a child process `P2` that need to communicate with each other using IPC.

```c
// Parent process
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child process
        int msg = 0; // Initialize message
        while (msg != 10) {
            scanf("%d", &msg); // Read message from parent process
            printf("Child process received message %d\n", msg);
        }
        printf("Child process terminated\n");
    } else {
        // Parent process
        printf("Parent process created with PID %d\n", getpid());
        int msg = 10; // Initialize message
        printf("Parent process sending message %d to child process\n", msg);
        scanf("%d", &msg); // Read response from child process
        printf("Parent process received response %d from child process\n", msg);
        printf("Parent process terminated\n");
    }
    return 0;
}
```

## Key Concepts

- **Process Creation**: Creating a new process.
- **Process Termination**: Terminating a process.
- **Scheduling**: Scheduling a process for execution.
- **Inter-Process Communication (IPC)**: Communicating between processes.
- **Synchronous Communication**: Synchronizing communication between processes using semaphores or monitors.
- **Asynchronous Communication**: Asynchronizing communication between processes using pipes or sockets.

## Best Practices

- **Use IPC Mechanisms**: Use IPC mechanisms to enable communication between processes.
- **Use Synchronization Primitives**: Use synchronization primitives to synchronize communication between processes.
- **Use Asynchronous Communication**: Use asynchronous communication to improve performance.
- **Use Scheduling Algorithms**: Use scheduling algorithms to schedule processes for execution.
